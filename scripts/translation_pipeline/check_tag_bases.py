# -*- coding: utf-8 -*-
import re
import json

def get_tag_dictionary(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    tag_map = {}
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        parts = k.split('_')
        tag = parts[0]
        suffix = '_'.join(parts[1:])
        if tag not in tag_map:
            tag_map[tag] = {}
        tag_map[tag][suffix] = val
        
    return tag_map

tm = get_tag_dictionary(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')

# Check tags without base name or adj
missing_base = []
for tag, data in tm.items():
    base = data.get('')
    adj = data.get('ADJ')
    if not base or not adj:
        missing_base.append((tag, base, adj, list(data.keys())[:3]))
        
print(f"Tags missing base or adj: {len(missing_base)}")
for m in missing_base[:20]:
    print(m)
