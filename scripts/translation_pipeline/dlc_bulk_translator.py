# -*- coding: utf-8 -*-
r"""
dlc_bulk_translator.py
Universal high-speed translator for HOI4 DLC localisation files.
- Preserves variables ($VAR$), formatting tags (§X...§!), script tags ([...]), texticons (£...), and line breaks (\n).
- Ensures valid Clausewitz YAML syntax with UTF-8 BOM.
- Automatically writes to both F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\ and local workspace mirror.
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_POR_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"
ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

TERMS_MAP = [
    (r'\bFour[- ]Year Plan\b', 'Rencana Empat Tahun'),
    (r'\bInner Circle\b', 'Lingkaran Dalam'),
    (r'\bMEFO [Bb]ills?\b', 'Surat Utang MEFO'),
    (r'\btagihan MEFO\b', 'Surat Utang MEFO'),
    (r'\bSpecial Projects?\b', 'Proyek Khusus'),
    (r'\bGeneral Staff\b', 'Staf Umum'),
    (r'\bNational Focus\b', 'Fokus Nasional'),
    (r'\bfokus nasional\b', 'Fokus Nasional'),
    (r'\bCivilian Factor(?:y|ies)\b', 'Pabrik Sipil'),
    (r'\bpabrik sipil\b', 'Pabrik Sipil'),
    (r'\bMilitary Factor(?:y|ies)\b', 'Pabrik Militer'),
    (r'\bpabrik militer\b', 'Pabrik Militer'),
    (r'\bNaval Dockyards?\b', 'Galangan Kapal Angkatan Laut'),
    (r'\bSynthetic Refiner(?:y|ies)\b', 'Pabrik Pengilangan Sintetis'),
    (r'\bFuel Silos?\b', 'Silo Bahan Bakar'),
    (r'\bAir Bases?\b', 'Pangkalan Udara'),
    (r'\bResearch Slots?\b', 'Slot Riset'),
    (r'\bslot riset\b', 'Slot Riset'),
    (r'\bWorld Tension\b', 'Ketegangan Dunia'),
    (r'\bketegangan dunia\b', 'Ketegangan Dunia'),
    (r'\bWar Support\b', 'Dukungan Perang'),
    (r'\bdukungan perang\b', 'Dukungan Perang'),
    (r'\bPolitical Power\b', 'Kekuasaan Politik'),
    (r'\bkekuasaan politik\b', 'Kekuasaan Politik'),
    (r'\bConsumer Goods\b', 'Barang Konsumsi'),
    (r'\bbarang konsumsi\b', 'Barang Konsumsi'),
    (r'\bCivil War\b', 'Perang Saudara'),
    (r'\bNon-Aggression Pact\b', 'Pakta Non-Agresi'),
    (r'\bMutual Defense Pact\b', 'Pakta Pertahanan Bersama'),
    (r'\bPuppet state\b', 'Negara Boneka'),
    (r'\bpuppet state\b', 'Negara Boneka'),
    (r'\bkerja sama\b', 'kerja sama'),
    (r'\bkerjasama\b', 'kerja sama'),
    (r'\bKerjasama\b', 'Kerja Sama'),
]

def mask_text(text):
    tokens = []
    pattern = re.compile(
        r'(\\n)|(\\")|(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)'
    )
    def repl(m):
        tok = m.group(0)
        idx = len(tokens)
        tokens.append(tok)
        return f"___TK{idx}___"
    masked = pattern.sub(repl, text)
    return masked, tokens

def unmask_text(text, tokens):
    res = text
    for i, tok in enumerate(tokens):
        res = re.sub(r'___\s*TK\s*' + str(i) + r'\s*___', tok, res)
        
    res = re.sub(r'§([A-Za-z])\s+', r'§\1', res)
    res = re.sub(r'\s+§!', '§!', res)
    res = re.sub(r'\[\s+', '[', res)
    res = re.sub(r'\s+\]', ']', res)
    res = re.sub(r'([a-zA-Z0-9])§([A-Za-z])', r'\1 §\2', res)
    res = re.sub(r'§!\s*([a-zA-Z0-9])', r'§! \1', res)
    res = re.sub(r'\s*\\n\s*', r'\\n', res)
    
    # Internal quote safety
    res = res.replace('“', '\\"').replace('”', '\\"')
    res = re.sub(r'(?<!\\)"', r'\"', res)
    
    for pat, rep in TERMS_MAP:
        res = re.sub(pat, rep, res)
        
    res = re.sub(r'[ \t]+', ' ', res).strip()
    return res

def translate_single_val(val):
    val_stripped = val.strip()
    if not val_stripped:
        return val
    # If it's purely a variable reference like "$VAR$"
    if re.match(r'^\$[A-Za-z0-9_.-]+\$$', val_stripped):
        return val
        
    masked, tokens = mask_text(val)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_tr = ''.join([p[0] for p in data[0] if p[0]])
                return unmask_text(raw_tr, tokens)
        except Exception as e:
            if attempt == 3:
                return unmask_text(masked, tokens)
            time.sleep(1 + attempt * 0.5)

def parse_localisation_file(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    entries = []
    header = lines[0].strip() if lines else "l_braz_por:"
    
    for idx, line in enumerate(lines[1:], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            entries.append({'type': 'raw', 'text': line})
            continue
        
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            indent, key, version, val, comment = m.groups()
            entries.append({
                'type': 'key',
                'indent': indent,
                'key': key,
                'version': version,
                'val': val,
                'comment': comment or '',
                'line_no': idx
            })
        else:
            entries.append({'type': 'raw', 'text': line})
            
    return header, entries

def translate_file(base_filename, max_workers=20):
    eng_filename = base_filename.replace('_l_braz_por.yml', '_l_english.yml')
    if not eng_filename.endswith('_l_english.yml'):
        eng_filename += '_l_english.yml'
    por_filename = eng_filename.replace('_l_english.yml', '_l_braz_por.yml')
    
    eng_path = os.path.join(ENG_DIR, eng_filename)
    if not os.path.exists(eng_path):
        print(f"[ERROR] English source not found: {eng_path}")
        return False
        
    print(f"\n==========================================", flush=True)
    print(f"Translating: {eng_filename} -> {por_filename}", flush=True)
    print(f"==========================================", flush=True)
    
    header, entries = parse_localisation_file(eng_path)
    
    key_entries = [e for e in entries if e['type'] == 'key']
    print(f"Total keys to translate: {len(key_entries)}", flush=True)
    
    translations = {}
    
    def process_entry(entry):
        val = entry['val']
        tr_val = translate_single_val(val)
        return entry['key'], tr_val
    
    start_t = time.time()
    completed = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_entry, e): e for e in key_entries}
        for fut in as_completed(futures):
            k, tr = fut.result()
            translations[k] = tr
            completed += 1
            if completed % 100 == 0 or completed == len(key_entries):
                elapsed = time.time() - start_t
                rate = completed / elapsed if elapsed > 0 else 0
                print(f"  Progress: {completed}/{len(key_entries)} ({completed*100//len(key_entries)}%) - {rate:.1f} keys/s", flush=True)
                
    # Assemble target file
    out_lines = ["\ufeffl_braz_por:\n"]
    for e in entries:
        if e['type'] == 'raw':
            out_lines.append(e['text'])
        elif e['type'] == 'key':
            k = e['key']
            tr_val = translations.get(k, e['val'])
            # Ensure proper quote escaping
            clean_val = tr_val.replace('"', '\\"') if ('"' in tr_val and '\\"' not in tr_val) else tr_val
            clean_val = clean_val.replace('\n', '\\n')
            ver_str = f":{e['version']} " if e['version'] else ": "
            cmt_str = e['comment'] if e['comment'] else ""
            out_lines.append(f"{e['indent']}{k}{ver_str}\"{clean_val}\"{cmt_str}\n")
            
    content = "".join(out_lines)
    
    # Write to game and local target
    target_game = os.path.join(GAME_POR_DIR, por_filename)
    target_local = os.path.join(LOCAL_POR_DIR, por_filename)
    
    with open(target_game, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(target_local, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"[OK] Successfully wrote {len(key_entries)} keys to:")
    print(f"  - {target_game}")
    print(f"  - {target_local}")
    return True

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for fname in sys.argv[1:]:
            translate_file(fname)
    else:
        print("Usage: python dlc_bulk_translator.py <filename_or_base>")
