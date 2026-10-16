# -*- coding: utf-8 -*-
import re

def list_all_tags(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    tags = {}
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if not m:
            continue
        indent, k, ver, val, cmt = m.groups()
        parts = k.split('_')
        tag = parts[0]
        suffix = '_'.join(parts[1:])
        if tag not in tags:
            tags[tag] = {}
        tags[tag][suffix] = val
        
    print(f"Total tags: {len(tags)}")
    # Write to a file for review
    with open('scripts/all_tags_summary.txt', 'w', encoding='utf-8') as out:
        for t in sorted(tags.keys()):
            d = tags[t]
            base = d.get('', '')
            adj = d.get('ADJ', '')
            dem = d.get('democratic', '')
            fas = d.get('fascism', '')
            com = d.get('communism', '')
            neu = d.get('neutrality', '')
            out.write(f"{t} | Base: {base} | Adj: {adj} | Dem: {dem} | Fas: {fas} | Com: {com} | Neu: {neu}\n")
            
    print("Saved to scripts/all_tags_summary.txt")

list_all_tags(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
