# -*- coding: utf-8 -*-
"""
translate_ui_pack.py
Translates core gameplay & UI files into Indonesian using the client=at batched engine.
Files:
- resistance_and_occupation
- aat_tooltips
- international_market
- tutorial
- abilities
"""
import os
import re
import json
import time
import urllib.request
import urllib.parse

GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_POR_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"
ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

GLOSSARY = [
    (r'\bCivilian Oversight\b', 'Pengawasan Sipil'),
    (r'\bLocal Police Force\b', 'Pasukan Kepolisian Lokal'),
    (r'\bSecret Police\b', 'Polisi Rahasia'),
    (r'\bMilitary Governor\b', 'Gubernur Militer'),
    (r'\bMartial Law\b', 'Hukum Darurat Militer'),
    (r'\bBrutal Oppression\b', 'Penindasan Brutal'),
    (r'\bForced Labor\b', 'Kerja Paksa'),
    (r'\bNo Garrison\b', 'Tanpa Garnisun'),
    (r'\bLiberated Workers\b', 'Pekerja yang Dibebaskan'),
    (r'\bAutonomous Occupation\b', 'Pendudukan Otonom'),
    (r'\bResistance Target\b', 'Target Perlawanan'),
    (r'\bCompliance\b', 'Kepatuhan (Kepatuhan Rakyat)'),
    (r'\bResistance\b', 'Perlawanan'),
    (r'\bInternational Market\b', 'Pasar Internasional'),
    (r'\bMarket Access\b', 'Akses Pasar'),
    (r'\bPurchase Contract\b', 'Kontrak Pembelian'),
    (r'\bDelivery\b', 'Pengiriman'),
    (r'\bIndustrial Concern\b', 'Konsorsium Industri'),
    (r'\bMilitary Industrial Organization\b', 'Organisasi Industri Militer (MIO)'),
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

def process_file(base_name):
    src_file = os.path.join(ENG_DIR, f"{base_name}_l_english.yml")
    if not os.path.exists(src_file):
        print(f"[SKIP] Not found: {src_file}")
        return
        
    print(f"\n==========================================")
    print(f"Processing: {base_name}")
    print(f"==========================================")
    
    with open(src_file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    entries = []
    keys_to_translate = []
    vals_to_translate = []
    
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('l_'):
            entries.append({'type': 'raw', 'text': line})
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            indent, key, ver, val, comment = m.groups()
            idx = len(keys_to_translate)
            keys_to_translate.append(key)
            vals_to_translate.append(val)
            entries.append({
                'type': 'key',
                'indent': indent,
                'key': key,
                'version': ver,
                'orig_val': val,
                'val_idx': idx,
                'comment': comment or ''
            })
        else:
            entries.append({'type': 'raw', 'text': line})
            
    print(f"Total keys: {len(keys_to_translate)}")
    
    BATCH_SIZE = 25
    translated_vals = [None] * len(vals_to_translate)
    
    for i in range(0, len(vals_to_translate), BATCH_SIZE):
        batch = vals_to_translate[i:i+BATCH_SIZE]
        print(f"  Batch {i//BATCH_SIZE + 1}/{(len(vals_to_translate)-1)//BATCH_SIZE + 1} ({len(batch)} items)...", flush=True)
        res = translate_batch(batch)
        for j, val in enumerate(res):
            translated_vals[i+j] = val
        time.sleep(0.3)
        
    out_lines = ["l_braz_por:\n"]
    for e in entries:
        if e['type'] == 'raw':
            if not e['text'].strip().startswith('l_'):
                out_lines.append(e['text'])
        elif e['type'] == 'key':
            tr = translated_vals[e['val_idx']]
            v_str = f":{e['version']}" if e['version'] else ":"
            out_lines.append(f"{e['indent']}{e['key']}{v_str} \"{tr}\"{e['comment']}\n")
            
    content = "".join(out_lines)
    for folder in [GAME_POR_DIR, LOCAL_POR_DIR]:
        target = os.path.join(folder, f"{base_name}_l_braz_por.yml")
        with open(target, 'wb') as f:
            f.write(b'\xef\xbb\xbf')
            f.write(content.encode('utf-8'))
        print(f"  [OK] Successfully wrote: {target}")

def main():
    target_files = [
        'resistance_and_occupation',
        'aat_tooltips',
        'international_market',
        'tutorial',
        'abilities',
        'military_raids'
    ]
    for tf in target_files:
        process_file(tf)

if __name__ == "__main__":
    main()
