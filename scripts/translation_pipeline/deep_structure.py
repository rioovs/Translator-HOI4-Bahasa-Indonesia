# -*- coding: utf-8 -*-
import re
from collections import Counter

def analyze_structure(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    tags = set()
    patterns = Counter()
    entries = []
    
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        entries.append((k, val))
        parts = k.split('_')
        tag = parts[0]
        tags.add(tag)
        suffix = '_'.join(parts[1:])
        patterns[suffix] += 1
        
    print(f"File: {path}")
    print(f"Total entries: {len(entries)}")
    print(f"Unique tags / prefixes: {len(tags)}")
    print("Common suffixes:")
    for s, c in patterns.most_common(25):
        print(f"  '{s}': {c}")
    return entries

e1 = analyze_structure(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
print()
e2 = analyze_structure(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
