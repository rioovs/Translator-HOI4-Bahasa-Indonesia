# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

needed_keys = {it['key'] for it in items}

# Let's inspect js files
import glob
found = {}
for js_file in sorted(glob.glob('scripts/focus_part*.js')):
    with open(js_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Simple regex to find "KEY": "VAL"
    matches = re.findall(r'"([a-zA-Z0-9_]+)":\s*"((?:\\.|[^"\\])*)"', content)
    for k, v in matches:
        if k in needed_keys:
            found[k] = (js_file, v)

print(f"Found {len(found)} of {len(needed_keys)} needed keys in focus_part*.js")
for k in list(found.keys())[:10]:
    print(f"  {k} in {found[k][0]}: {found[k][1][:60]}")
