# -*- coding: utf-8 -*-
"""
universal_dlc_translator.py
Universal robust batched translator for Hearts of Iron IV localisation files.
- Uses client=at POST batching (30 items/batch).
- Robust token masking and restoration.
- Writes with UTF-8 BOM to game directory and workspace mirror.
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.parse

GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_POR_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"
ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

GLOSSARY = [
    (r'\bFour[- ]Year Plan\b', 'Rencana Empat Tahun'),
    (r'\bNational Focus\b', 'Fokus Nasional'),
    (r'\bCivilian Factor(?:y|ies)\b', 'Pabrik Sipil'),
    (r'\bMilitary Factor(?:y|ies)\b', 'Pabrik Militer'),
    (r'\bNaval Dockyards?\b', 'Galangan Kapal Angkatan Laut'),
    (r'\bSynthetic Refiner(?:y|ies)\b', 'Pabrik Pengilangan Sintetis'),
    (r'\bFuel Silos?\b', 'Silo Bahan Bakar'),
    (r'\bAir Bases?\b', 'Pangkalan Udara'),
    (r'\bResearch Slots?\b', 'Slot Riset'),
    (r'\bWorld Tension\b', 'Ketegangan Dunia'),
    (r'\bWar Support\b', 'Dukungan Perang'),
    (r'\bPolitical Power\b', 'Kekuasaan Politik'),
    (r'\bConsumer Goods\b', 'Barang Konsumsi'),
    (r'\bCivil War\b', 'Perang Saudara'),
    (r'\bNon-Aggression Pact\b', 'Pakta Non-Agresi'),
    (r'\bPuppet state\b', 'Negara Boneka'),
    (r'\bpuppet state\b', 'Negara Boneka'),
    (r'\bSpecial Projects?\b', 'Proyek Khusus'),
    (r'\bGeneral Staff\b', 'Staf Umum'),
    (r'\bOfficer Corps\b', 'Korps Perwira'),
    (r'\bCommander\b', 'Komandan'),
    (r'\bCommanders\b', 'Komandan'),
    (r'\bAdmiral\b', 'Laksamana'),
    (r'\bAdmirals\b', 'Laksamana'),
    (r'\bGeneral\b', 'Jenderal'),
    (r'\bGenerals\b', 'Jenderal'),
    (r'\bField Marshal\b', 'Marsekal Lapangan'),
    (r'\bDivision\b', 'Divisi'),
    (r'\bDivisions\b', 'Divisi'),
    (r'\bTask Force\b', 'Satuan Tugas'),
    (r'\bTask Forces\b', 'Satuan Tugas'),
    (r'\bSoft Attack\b', 'Serangan Lunak'),
    (r'\bHard Attack\b', 'Serangan Keras'),
    (r'\bBreakthrough\b', 'Penerobosan'),
    (r'\bAir Superiority\b', 'Keunggulan Udara'),
    (r'\bClose Air Support\b', 'Bantuan Udara Jarak Dekat'),
    (r'\bStrategic Bombing\b', 'Pengeboman Strategis'),
    (r'\bNaval Strike\b', 'Serangan Laut'),
    (r'\bPort Strike\b', 'Serangan Pelabuhan'),
    (r'\bAir Reconnaissance\b', 'Pengintaian Udara'),
    (r'\bSubmarine\b', 'Kapal Selam'),
    (r'\bDestroyer\b', 'Kapal Perusak'),
    (r'\bLight Cruiser\b', 'Penjelajah Ringan'),
    (r'\bHeavy Cruiser\b', 'Penjelajah Berat'),
    (r'\bBattlecruiser\b', 'Penjelajah Tempur'),
    (r'\bBattleship\b', 'Kapal Tempur'),
    (r'\bAircraft Carrier\b', 'Kapal Induk'),
    (r'\bInfantry Equipment\b', 'Perlengkapan Infanteri'),
    (r'\bSupport Equipment\b', 'Perlengkapan Pendukung'),
    (r'\bMotorized\b', 'Bermotor'),
    (r'\bMechanized\b', 'Mekanis'),
    (r'\bLight Tank\b', 'Tank Ringan'),
    (r'\bMedium Tank\b', 'Tank Sedang'),
    (r'\bHeavy Tank\b', 'Tank Berat'),
    (r'\bSuper-Heavy Tank\b', 'Tank Super Berat'),
    (r'\bModern Tank\b', 'Tank Modern'),
    (r'\bCarrier\b', 'Kapal Induk'),
]

def mask_text(s):
    tokens = []
    pattern = re.compile(
        r'(\\n)|(\\")|(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)'
    )
    def repl(m):
        tok = m.group(0)
        idx = len(tokens)
        tokens.append(tok)
        return f"___TK{idx}___"
    masked = pattern.sub(repl, s)
    return masked, tokens

def unmask_text(s, tokens):
    res = s
    for i, tok in enumerate(tokens):
        res = re.sub(r'___\s*TK\s*' + str(i) + r'\s*___', tok, res)
    res = re.sub(r'§([A-Za-z])\s+', r'§\1', res)
    res = re.sub(r'\s+§!', '§!', res)
    res = re.sub(r'\[\s+', '[', res)
    res = re.sub(r'\s+\]', ']', res)
    res = re.sub(r'\s*\\n\s*', r'\\n', res)
    res = res.replace('“', '\\"').replace('”', '\\"')
    res = re.sub(r'(?<!\\)"', r'\"', res)
    for pat, rep in GLOSSARY:
        res = re.sub(pat, rep, res, flags=re.IGNORECASE)
    return res.strip()

def call_translate(text):
    url = 'https://translate.google.com/translate_a/single?client=at&sl=en&tl=id&dt=t'
    data = urllib.parse.urlencode({'q': text}).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=data,
        headers={
            'User-Agent': 'AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1',
            'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                res = json.loads(resp.read().decode('utf-8'))
                return ''.join(x[0] for x in res[0] if x and x[0])
        except Exception as e:
            time.sleep(1.0 * (attempt + 1))
            if attempt == 4:
                return text

def translate_batch(batch):
    masked_list = []
    tokens_list = []
    for orig in batch:
        m, t = mask_text(orig)
        masked_list.append(m)
        tokens_list.append(t)
    
    delim = "\n---DIV---\n"
    combined = delim.join(masked_list)
    tr_raw = call_translate(combined)
    parts = tr_raw.split('---DIV---')
    
    if len(parts) == len(batch):
        return [unmask_text(p.strip(), tok) for p, tok in zip(parts, tokens_list)]
    else:
        results = []
        for m, tok in zip(masked_list, tokens_list):
            single_tr = call_translate(m)
            results.append(unmask_text(single_tr, tok))
            time.sleep(0.1)
        return results

def is_already_indonesian(text, orig_val):
    if not text:
        return False
    if text.strip() == orig_val.strip():
        cleaned = re.sub(r'(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)', '', text).strip()
        return len(cleaned) == 0
    cleaned = re.sub(r'(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)', '', text).strip()
    if not cleaned:
        return True
    lower = f" {cleaned.lower()} "
    foreign = [' the ', ' of ', ' to ', ' and ', ' in ', ' is ', ' that ', ' will ', ' our ', ' de ', ' para ', ' com ', ' não ', ' do ', ' da ']
    if any(w in lower for w in foreign):
        return False
    indo = [' dan ', ' yang ', ' di ', ' untuk ', ' dengan ', ' pada ', ' ini ', ' itu ', ' tidak ', ' dari ', ' akan ', ' ke ', ' oleh ']
    if any(w in lower for w in indo):
        return True
    return True

def process_file(base_name):
    clean_base = base_name.replace('_l_braz_por.yml', '').replace('_l_english.yml', '')
    src_file = os.path.join(ENG_DIR, f"{clean_base}_l_english.yml")
    if not os.path.exists(src_file):
        print(f"[SKIP] Source file not found: {src_file}")
        return False
        
    print(f"\n==========================================", flush=True)
    print(f"Translating: {clean_base}_l_english.yml -> {clean_base}_l_braz_por.yml", flush=True)
    print(f"==========================================", flush=True)
    
    # Load existing translations if available
    existing_map = {}
    for folder in [GAME_POR_DIR, LOCAL_POR_DIR]:
        exist_path = os.path.join(folder, f"{clean_base}_l_braz_por.yml")
        if os.path.exists(exist_path):
            with open(exist_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
                for l in f:
                    m_ex = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)"', l.strip())
                    if m_ex:
                        k_ex, v_ex = m_ex.groups()
                        if k_ex not in existing_map:
                            existing_map[k_ex] = v_ex
    
    with open(src_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    entries = []
    keys_list = []
    vals_list = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('l_'):
            entries.append({'type': 'raw', 'text': line})
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            indent, key, ver, val, comment = m.groups()
            keys_list.append(key)
            vals_list.append(val)
            entries.append({
                'type': 'key',
                'indent': indent,
                'key': key,
                'version': ver,
                'orig_val': val,
                'comment': comment or ''
            })
        else:
            entries.append({'type': 'raw', 'text': line})
            
    final_translations = {}
    to_translate_keys = []
    to_translate_vals = []
    
    for k, v in zip(keys_list, vals_list):
        ex_val = existing_map.get(k)
        if ex_val is not None and is_already_indonesian(ex_val, v):
            final_translations[k] = ex_val
        else:
            to_translate_keys.append(k)
            to_translate_vals.append(v)
            
    print(f"Total keys: {len(keys_list)} | Already Indonesian: {len(final_translations)} | Need translation: {len(to_translate_vals)}", flush=True)
    
    if to_translate_vals:
        BATCH_SIZE = 30
        start_time = time.time()
        for i in range(0, len(to_translate_vals), BATCH_SIZE):
            batch = to_translate_vals[i:i+BATCH_SIZE]
            pct = (i + len(batch)) / len(to_translate_vals) * 100
            elapsed = time.time() - start_time
            speed = (i + len(batch)) / max(0.1, elapsed)
            print(f"  Progress: {i+len(batch)}/{len(to_translate_vals)} ({pct:.0f}%) - {speed:.1f} keys/s", flush=True)
            res = translate_batch(batch)
            for j, val in enumerate(res):
                key = to_translate_keys[i+j]
                final_translations[key] = val
            time.sleep(0.3)
        
    out_lines = ["l_braz_por:\n"]
    for e in entries:
        if e['type'] == 'raw':
            if not e['text'].strip().startswith('l_'):
                out_lines.append(e['text'])
        elif e['type'] == 'key':
            tr = final_translations.get(e['key'], e['orig_val'])
            v_str = f":{e['version']}" if e['version'] else ":"
            out_lines.append(f"{e['indent']}{e['key']}{v_str} \"{tr}\"{e['comment']}\n")
            
    content = "".join(out_lines)
    for folder in [GAME_POR_DIR, LOCAL_POR_DIR]:
        target = os.path.join(folder, f"{clean_base}_l_braz_por.yml")
        with open(target, 'wb') as f:
            f.write(b'\xef\xbb\xbf')
            f.write(content.encode('utf-8'))
        print(f"  [OK] Successfully wrote {len(keys_list)} keys to: {target}", flush=True)
    return True

if __name__ == "__main__":
    files = sys.argv[1:]
    if not files:
        print("Usage: python universal_dlc_translator.py <file1> <file2> ...")
        sys.exit(1)
    for f in files:
        process_file(f)
