# -*- coding: utf-8 -*-
import re

def test_parse(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    entries = []
    for idx, line in enumerate(lines[1:], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            print(f"FAILED TO PARSE LINE {idx}: {line}")
            return False
        indent, k, ver, val, cmt = m.groups()
        entries.append((idx, indent, k, ver, val, cmt))
        
    print(f"Successfully parsed {len(entries)} entries in {path}")
    return True

test_parse(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
test_parse(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
