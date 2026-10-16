# -*- coding: utf-8 -*-
import re

def count_stripped_unique():
    paths = [
        r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml',
        r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml'
    ]
    raw_vals = set()
    stripped_vals = set()
    for path in paths:
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
                if m:
                    v = m.group(4)
                    raw_vals.add(v)
                    v_strip = re.sub(r'^[tT]he\s+', '', v)
                    stripped_vals.add(v_strip)
                    
    print(f"Total raw unique values: {len(raw_vals)}")
    print(f"Total stripped unique values: {len(stripped_vals)}")

count_stripped_unique()
