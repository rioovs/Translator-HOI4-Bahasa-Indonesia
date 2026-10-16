# -*- coding: utf-8 -*-
import re

def analyze_cosmetic(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    entries = []
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        entries.append((k, val))
        
    print(f"Total cosmetic entries: {len(entries)}")
    # Look at some examples
    for k, val in entries[:40]:
        print(f"  {k}: \"{val}\"")

analyze_cosmetic(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
