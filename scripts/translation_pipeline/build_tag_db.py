# -*- coding: utf-8 -*-
import re
import json

def build_tag_database(path):
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
        
    with open('scripts/tag_db.json', 'w', encoding='utf-8') as f:
        json.dump(tags, f, indent=2, ensure_ascii=False)
        
    print(f"Dumped {len(tags)} tags to scripts/tag_db.json")

build_tag_database(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
