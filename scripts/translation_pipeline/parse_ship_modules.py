# -*- coding: utf-8 -*-
import json
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

data = []
for idx, line in enumerate(lines):
    stripped = line.strip()
    if idx == 0:
        continue
    if not stripped or stripped.startswith('#'):
        data.append({
            'line_idx': idx,
            'type': 'comment_or_empty',
            'raw': line
        })
        continue
    
    m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if not m:
        # Check special case like HOL ""6x...
        m2 = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*""(.*)"(\s*#.*)?$', line)
        if m2:
            data.append({
                'line_idx': idx,
                'type': 'key_val',
                'indent': m2.group(1),
                'key': m2.group(2),
                'version': m2.group(3),
                'value': m2.group(4),
                'comment': m2.group(5) or ''
            })
            continue
        print(f"Error parsing line {idx+1}: {line}")
        continue
    
    data.append({
        'line_idx': idx,
        'type': 'key_val',
        'indent': m.group(1),
        'key': m.group(2),
        'version': m.group(3),
        'value': m.group(4),
        'comment': m.group(5) or ''
    })

print(f"Total parsed elements: {len(data)}")
key_vals = [d for d in data if d['type'] == 'key_val']
print(f"Total key_val elements: {len(key_vals)}")

with open('scripts/parsed_ship_modules.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("Saved to scripts/parsed_ship_modules.json")
