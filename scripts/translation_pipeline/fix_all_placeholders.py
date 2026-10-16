# -*- coding: utf-8 -*-
import json
import re
import os
from translate_wuw_engine import mask_text

batch_names = [
    'batch1_ah_hun',
    'batch2_aus',
    'batch3_bel',
    'batch4_cog',
    'batch5_ger_part1',
    'batch6_ger_part2'
]

pattern_tk = re.compile(r'_+\s*TK\s*(\d+)\s*_+')

fixed_total = 0

for bname in batch_names:
    src_path = f'scripts/wuw_batches/{bname}.json'
    tr_path = f'scripts/wuw_batches/{bname}_translated.json'
    
    with open(src_path, 'r', encoding='utf-8') as f:
        src_map = {item['key']: item['val'] for item in json.load(f)}
    with open(tr_path, 'r', encoding='utf-8') as f:
        tr_map = json.load(f)
        
    for k, tr_val in tr_map.items():
        if pattern_tk.search(tr_val):
            orig_val = src_map[k]
            # Check pure script tag or pure var
            if re.match(r'^\[[^\]]+\]$', orig_val.strip()):
                tr_map[k] = orig_val
                fixed_total += 1
                continue
                
            _, tokens = mask_text(orig_val)
            fixed_val = tr_val
            for i, tok in enumerate(tokens):
                fixed_val = re.sub(r'_+\s*TK\s*' + str(i) + r'\s*_+', tok, fixed_val)
            # Normalization
            fixed_val = re.sub(r'§([A-Za-z])\s+', r'§\1', fixed_val)
            fixed_val = re.sub(r'\s+§!', '§!', fixed_val)
            fixed_val = re.sub(r'\[\s+', '[', fixed_val)
            fixed_val = re.sub(r'\s+\]', ']', fixed_val)
            fixed_val = re.sub(r'([a-zA-Z0-9])§([A-Za-z])', r'\1 §\2', fixed_val)
            fixed_val = re.sub(r'§!\s*([a-zA-Z0-9])', r'§! \1', fixed_val)
            fixed_val = re.sub(r'\s*\\n\s*', r'\\n', fixed_val)
            tr_map[k] = fixed_val
            fixed_total += 1
            print(f"Fixed {k}: {fixed_val}")
            
    with open(tr_path, 'w', encoding='utf-8') as f:
        json.dump(tr_map, f, ensure_ascii=False, indent=2)

print(f"\nTotal fixed items: {fixed_total}")
