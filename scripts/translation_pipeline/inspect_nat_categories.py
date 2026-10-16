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

armors = [x for x in nat_items if 'armor' in x[0]]
engines = [x for x in nat_items if 'engine' in x[0]]
torpedos = [x for x in nat_items if 'torpedo' in x[0]]
radars = [x for x in nat_items if 'radar' in x[0] or 'sonar' in x[0]]

print(f"Armor items: {len(armors)}")
for k, v in armors[:15]:
    print(f"  {k}: {v}")

print(f"\nEngine items: {len(engines)}")
for k, v in engines[:15]:
    print(f"  {k}: {v}")

print(f"\nTorpedo items: {len(torpedos)}")
for k, v in torpedos[:15]:
    print(f"  {k}: {v}")

print(f"\nRadar/Sonar items: {len(radars)}")
for k, v in radars:
    print(f"  {k}: {v}")
