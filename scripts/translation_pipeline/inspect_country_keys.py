# -*- coding: utf-8 -*-
import re

def inspect_keys(path):
    print(f"=== Inspecting keys: {path} ===")
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    non_tag_keys = []
    sample_tags = {}
    special_keys = []
    
    for line in lines[1:]:
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"', line)
        if not m:
            continue
        k, ver, val = m.groups()
        parts = k.split('_')
        tag = parts[0]
        if len(tag) != 3 or not tag.isupper():
            special_keys.append((k, val))
        else:
            suffix = '_'.join(parts[1:])
            sample_tags[suffix] = sample_tags.get(suffix, 0) + 1
            
    print(f"Total special/non-3-letter keys: {len(special_keys)}")
    for k, val in special_keys[:30]:
        print(f"  {k}: \"{val}\"")
        
    print(f"\nTop 20 suffixes:")
    sorted_suffixes = sorted(sample_tags.items(), key=lambda x: x[1], reverse=True)[:20]
    for s, c in sorted_suffixes:
        print(f"  _{s}: {c}")

inspect_keys(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
inspect_keys(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
