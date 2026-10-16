# -*- coding: utf-8 -*-
import json
import os
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_events_l_english.yml'
src_data = {}
with open(src_path, 'r', encoding='utf-8-sig') as f:
    for line in f:
        m = re.match(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.rstrip('\r\n'))
        if m:
            k, ver, val, _ = m.groups()
            src_data[k] = val

discrepancies = []
for c in range(14):
    c_file = f'scripts/chunks/trans_chunk_{c}.json'
    if not os.path.exists(c_file):
        continue
    with open(c_file, 'r', encoding='utf-8') as f:
        t_data = json.load(f)
    for k, t_val in t_data.items():
        s_val = src_data.get(k, '')
        s_vars = set(re.findall(r'\$[a-zA-Z0-9_|\.\+\-\%]+\$', s_val))
        t_vars = set(re.findall(r'\$[a-zA-Z0-9_|\.\+\-\%]+\$', t_val))
        missing_vars = s_vars - t_vars

        s_tags = set(re.findall(r'\[[a-zA-Z0-9_\.\?\:\s]+\]', s_val))
        t_tags = set(re.findall(r'\[[a-zA-Z0-9_\.\?\:\s]+\]', t_val))
        missing_tags = s_tags - t_tags

        if missing_vars or missing_tags:
            discrepancies.append({
                'chunk': c,
                'key': k,
                'missing_vars': list(missing_vars),
                'missing_tags': list(missing_tags),
                'eng': s_val,
                'ind': t_val
            })

print(f"Total keys with discrepancies: {len(discrepancies)}")
with open('scripts/tag_discrepancies.json', 'w', encoding='utf-8') as f:
    json.dump(discrepancies, f, ensure_ascii=False, indent=2)

for d in discrepancies:
    print(f"Chunk {d['chunk']:2d} | Key: {d['key']}")
    if d['missing_vars']:
        print(f"   Missing vars: {d['missing_vars']}")
    if d['missing_tags']:
        print(f"   Missing tags: {d['missing_tags']}")
