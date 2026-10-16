# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

eng_dict = {}
with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    for line in f:
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        m = re.match(r'^([a-zA-Z0-9_]+):\s*(?:0\s*)?\"(.*)\"$', s)
        if m:
            eng_dict[m.group(1)] = m.group(2)

missing_in_eng = []
for it in items:
    k = it['key']
    if k not in eng_dict:
        missing_in_eng.append(k)

print(f"Missing in focus_l_english.yml: {len(missing_in_eng)}")
if missing_in_eng:
    print(missing_in_eng[:10])
