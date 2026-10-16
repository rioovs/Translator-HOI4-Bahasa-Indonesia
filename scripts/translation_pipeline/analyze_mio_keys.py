# -*- coding: utf-8 -*-
import re

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/military_industrial_organization_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

total_keys = 0
pure_vars = 0
text_keys = 0

for l in lines[1:]:
    m = re.match(r'^\s*([A-Za-z0-9_-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        total_keys += 1
        val = m.group(3).strip()
        if re.match(r'^\$[A-Za-z0-9_]+\$$', val):
            pure_vars += 1
        else:
            text_keys += 1

print(f"Total lines: {len(lines)}")
print(f"Total keys: {total_keys}")
print(f"Pure variables: {pure_vars}")
print(f"Text keys to translate: {text_keys}")
