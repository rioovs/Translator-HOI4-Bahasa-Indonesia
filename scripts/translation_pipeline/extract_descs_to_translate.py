# -*- coding: utf-8 -*-
import json

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

english_descs = []
for idx in range(1634, len(lines)):
    l = lines[idx]
    s = l.strip()
    if not s or s.startswith('#'):
        continue
    if '_desc:' in s:
        idx_colon = s.find(':')
        key = s[:idx_colon].strip()
        val = s[idx_colon+1:].strip()
        # Remove leading '0 ' if any
        if val.startswith('0 '):
            val = val[2:].strip()
        if val.startswith('"') and val.endswith('"'):
            val_unquoted = val[1:-1]
        else:
            val_unquoted = val
        
        # Check if value is a reference like $xxx$ or empty
        if val_unquoted.startswith('$') and val_unquoted.endswith('$'):
            continue
        if not val_unquoted:
            continue
            
        english_descs.append({
            'line': idx + 1,
            'key': key,
            'val': val_unquoted,
            'raw_line': l
        })

print(f"Total _desc between 1635 and end: {len(english_descs)}")
tags = set()
for item in english_descs:
    key_tag = item['key'].split('_')[0]
    tags.add(key_tag)

print(f"Tags found: {sorted(list(tags))}")

with open('scripts/descs_to_translate.json', 'w', encoding='utf-8') as f:
    json.dump(english_descs, f, indent=2, ensure_ascii=False)
