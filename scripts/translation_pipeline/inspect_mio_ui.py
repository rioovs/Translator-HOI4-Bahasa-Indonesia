# -*- coding: utf-8 -*-
with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/military_industrial_organization_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

for i in range(6, 60):
    print(f"[{i+1}] {lines[i].strip()}")
