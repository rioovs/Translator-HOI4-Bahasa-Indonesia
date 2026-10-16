# -*- coding: utf-8 -*-
import json
import re

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

standard_suffixes = {
    '', 'DEF', 'ADJ',
    'democratic', 'democratic_DEF', 'democratic_ADJ',
    'fascism', 'fascism_DEF', 'fascism_ADJ',
    'communism', 'communism_DEF', 'communism_ADJ',
    'neutrality', 'neutrality_DEF', 'neutrality_ADJ'
}

special = []
for line in lines[1:]:
    m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
    if not m:
        continue
    indent, k, ver, val, cmt = m.groups()
    parts = k.split('_')
    tag = parts[0]
    suffix = '_'.join(parts[1:])
    if suffix not in standard_suffixes or len(tag) != 3 or not tag.isupper():
        special.append((k, val))

print(f"Total special entries in countries_l_english.yml: {len(special)}")
with open('scripts/file1_special_entries.json', 'w', encoding='utf-8') as out:
    json.dump(special, out, indent=2, ensure_ascii=False)

print("Saved scripts/file1_special_entries.json")
