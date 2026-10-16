# -*- coding: utf-8 -*-
import re

def count_unique_values(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    vals = set()
    total = 0
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        total += 1
        val = m.group(4)
        vals.add(val)
        
    print(f"{path}: total keys={total}, unique values={len(vals)}")
    return vals

v1 = count_unique_values(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
v2 = count_unique_values(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
print(f"Total unique values combined: {len(v1.union(v2))}")
