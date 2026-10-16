# -*- coding: utf-8 -*-
import os
import re

eng_dir = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english'
bp_dir = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por'

results = []

for fn in sorted(os.listdir(bp_dir)):
    if not fn.endswith('.yml'): continue
    bp_path = os.path.join(bp_dir, fn)
    # matching english file
    en_fn = fn.replace('_l_braz_por.yml', '_l_english.yml')
    en_path = os.path.join(eng_dir, en_fn)
    
    if not os.path.exists(en_path):
        continue
        
    with open(bp_path, 'r', encoding='utf-8-sig', errors='ignore') as fbp:
        bp_lines = fbp.readlines()
    with open(en_path, 'r', encoding='utf-8-sig', errors='ignore') as fen:
        en_lines = fen.readlines()
        
    bp_dict = {}
    for l in bp_lines:
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)"\s*$', l)
        if m:
            bp_dict[m.group(1)] = m.group(2)
            
    en_dict = {}
    for l in en_lines:
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)"\s*$', l)
        if m:
            en_dict[m.group(1)] = m.group(2)
            
    total_keys = len(en_dict)
    if total_keys == 0: continue
    
    # count how many keys in bp are identical to english (excluding variables like $VAR$, numbers, empty)
    same_count = 0
    translated_count = 0
    for k, v_en in en_dict.items():
        v_bp = bp_dict.get(k)
        if v_bp is None:
            continue
        v_en_s = v_en.strip()
        v_bp_s = v_bp.strip()
        if not v_en_s or re.match(r'^\$[A-Za-z0-9_.-]+\$$', v_en_s) or re.match(r'^[0-9.+-]+$', v_en_s):
            continue
        if v_bp_s == v_en_s:
            same_count += 1
        else:
            translated_count += 1
            
    pct_translated = (translated_count / (same_count + translated_count) * 100) if (same_count + translated_count) > 0 else 100
    results.append((fn, total_keys, same_count, translated_count, pct_translated))

results.sort(key=lambda x: x[2], reverse=True)

print(f"{'File Name':<35} | {'Total':>5} | {'English':>7} | {'Indo':>5} | {'% Translated':>12}")
print("-" * 75)
for fn, tot, same, trans, pct in results[:40]:
    if same > 0:
        print(f"{fn:<35} | {tot:>5} | {same:>7} | {trans:>5} | {pct:>11.1f}%")
