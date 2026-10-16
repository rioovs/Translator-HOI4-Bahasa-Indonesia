# -*- coding: utf-8 -*-
import re
import json

def inspect_cosmetic_all(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    entries = []
    groups = {}
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        entries.append((k, val))
        prefix = k.split('_')[0]
        if prefix not in groups:
            groups[prefix] = []
        groups[prefix].append((k, val))
        
    print(f"Total cosmetic entries: {len(entries)}")
    print(f"Total cosmetic groups: {len(groups)}")
    
    # Show largest groups
    sorted_groups = sorted(groups.items(), key=lambda x: len(x[1]), reverse=True)
    for p, items in sorted_groups[:30]:
        print(f"Group {p:15}: {len(items):3} entries. Example: {items[0][0]} -> \"{items[0][1]}\"")

inspect_cosmetic_all(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
