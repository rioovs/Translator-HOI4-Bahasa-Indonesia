# -*- coding: utf-8 -*-
import re

def count_stripped_per_file(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    vals = set()
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if m:
            v = m.group(4)
            v_strip = re.sub(r'^[tT]he\s+', '', v)
            vals.add(v_strip)
    print(f"{path}: {len(vals)} stripped unique values")
    return vals

v1 = count_stripped_per_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
v2 = count_stripped_per_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
