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

print(f"Total nation items: {len(nat_items)}")

# Let's see some samples of Weapon/Designation:
weapons = []
for k, v in nat_items:
    if not any(w in v for w in ['Belt', 'Deck', 'Engine', 'Turbine', 'Diesel', 'Boiler', 'Shaft', 'Radar', 'Sonar', 'Torpedo']):
        weapons.append((k, v))

print(f"Total pure weapon/designations: {len(weapons)}")
print("Sample pure weapons:")
for k, v in weapons[:25]:
    print(f"  {k}: {v}")

print("Sample pure weapons (middle):")
for k, v in weapons[200:225]:
    print(f"  {k}: {v}")
