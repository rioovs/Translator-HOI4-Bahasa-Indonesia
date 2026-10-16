# -*- coding: utf-8 -*-
import re

def analyze(path):
    print(f"=== Analyzing: {path} ===")
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    print(f"Total lines: {len(lines)}")
    key_count = 0
    non_matches = []
    keys = []
    values = []
    
    for idx, line in enumerate(lines):
        if idx == 0:
            print(f"Header: {line.strip()}")
            continue
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if m:
            key_count += 1
            indent, k, ver, val, cmt = m.groups()
            keys.append(k)
            values.append(val)
        else:
            non_matches.append((idx + 1, line))
            
    print(f"Matched keys: {key_count}")
    print(f"Non-matching lines: {len(non_matches)}")
    for line_no, content in non_matches[:10]:
        print(f"Line {line_no}: {content.strip()}")

analyze(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
analyze(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
