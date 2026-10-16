# -*- coding: utf-8 -*-
import re

def get_roots_for_file(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    roots = set()
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if m:
            v = m.group(4)
            if re.match(r'^\$[A-Za-z0-9_]+\$$', v):
                continue
            r = re.sub(r'^[tT]he\s+', '', v).strip()
            if r:
                roots.add(r)
    return roots

r1 = get_roots_for_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
r2 = get_roots_for_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')

print(f"File 1 roots: {len(r1)}")
print(f"File 2 roots: {len(r2)}")
print(f"Common roots: {len(r1.intersection(r2))}")
print(f"Roots only in File 1: {len(r1 - r2)}")
print(f"Roots only in File 2: {len(r2 - r1)}")
