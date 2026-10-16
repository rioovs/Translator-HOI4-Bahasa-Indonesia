# -*- coding: utf-8 -*-
with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/military_industrial_organization_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Sample lines 1 to 30
for i in range(1, 30):
    print(f"[{i+1}] {lines[i].strip()}")
