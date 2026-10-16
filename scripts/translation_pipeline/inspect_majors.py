# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

in_nat = False
nat_items = []
for line in lines:
    if line.strip().startswith('### Nation Specific Modules'):
        in_nat = True
        continue
    if not in_nat:
        continue
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if m:
        nat_items.append((m.group(1), m.group(3)))

majors = ['ENG', 'USA', 'FRA', 'GER', 'ITA', 'JAP', 'SOV']
for maj in majors:
    items = [x for x in nat_items if x[0].startswith(maj + '_')]
    print(f"\n--- {maj} ({len(items)} items) ---")
    for k, v in items[:15]:
        print(f"  {k}: {v}")
