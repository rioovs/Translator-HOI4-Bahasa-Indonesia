# -*- coding: utf-8 -*-
import re

def extract_country_catalog(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    tag_data = {}
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        parts = k.split('_')
        tag = parts[0]
        suffix = '_'.join(parts[1:])
        if tag not in tag_data:
            tag_data[tag] = {}
        tag_data[tag][suffix] = val
        
    print(f"Total tags in {path}: {len(tag_data)}")
    # Print sample tags
    for tag in list(tag_data.keys())[:25]:
        d = tag_data[tag]
        base_name = d.get('', d.get('democratic', d.get('neutrality', d.get('fascism', 'N/A'))))
        print(f"{tag}: base='{base_name}' | dem='{d.get('democratic')}' | fas='{d.get('fascism')}' | com='{d.get('communism')}' | neu='{d.get('neutrality')}'")
    return tag_data

tag_data = extract_country_catalog(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
