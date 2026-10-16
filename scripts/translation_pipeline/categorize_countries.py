# -*- coding: utf-8 -*-
import re

def categorize_all_keys(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    standard_suffixes = {
        '', 'DEF', 'ADJ',
        'democratic', 'democratic_DEF', 'democratic_ADJ',
        'fascism', 'fascism_DEF', 'fascism_ADJ',
        'communism', 'communism_DEF', 'communism_ADJ',
        'neutrality', 'neutrality_DEF', 'neutrality_ADJ'
    }
    
    special_entries = []
    standard_entries = []
    
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        parts = k.split('_')
        tag = parts[0]
        suffix = '_'.join(parts[1:])
        
        if suffix in standard_suffixes and (len(tag) == 3 and tag.isupper()):
            standard_entries.append((k, tag, suffix, val))
        else:
            special_entries.append((k, tag, suffix, val))
            
    print(f"Total lines: {len(lines)}")
    print(f"Standard country entries: {len(standard_entries)}")
    print(f"Special / subject entries: {len(special_entries)}")
    
    return standard_entries, special_entries

std, spec = categorize_all_keys(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
print("\nSample special entries in countries_l_english.yml (first 40):")
for k, tag, suffix, val in spec[:40]:
    print(f"  {k}: \"{val}\"")
