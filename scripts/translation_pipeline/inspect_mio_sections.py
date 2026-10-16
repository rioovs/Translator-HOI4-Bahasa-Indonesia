# -*- coding: utf-8 -*-
with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/military_industrial_organization_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

sections = []
for i, l in enumerate(lines):
    if l.strip().startswith('####') or l.strip().startswith('#---'):
        sections.append((i+1, l.strip()))

for s in sections[:25]:
    print(f"Line {s[0]}: {s[1]}")
