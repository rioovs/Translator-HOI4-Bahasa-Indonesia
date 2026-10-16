# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

in_nat = False
nat_modules = []
for line in lines:
    if line.strip().startswith('### Nation Specific Modules'):
        in_nat = True
        continue
    if not in_nat:
        continue
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if m:
        nat_modules.append((m.group(1), m.group(3)))

print(f"Total nation modules: {len(nat_modules)}")
# Group by module type or check if any have words that need translation (like Belt, Deck, Engine, etc.)
types = {}
for k, v in nat_modules:
    prefix = k.split('_')[0]
    mtype = '_'.join(k.split('_')[1:])
    # check base type
    base = re.sub(r'_\d+$', '', mtype)
    types[base] = types.get(base, 0) + 1

print("\nNation module base types:")
for b, count in sorted(types.items(), key=lambda x: -x[1]):
    print(f"{b}: {count}")

print("\nChecking for words in values (e.g. Belt, Deck, Turbine, Engine, Diesel, Boilers, Armor, etc.):")
for k, v in nat_modules:
    if any(w in v for w in ['Belt', 'Deck', 'Engine', 'Turbine', 'Diesel', 'Boiler', 'Shaft', 'Armor', 'Armour', 'Gun', 'Battery', 'Torpedo', 'Radar', 'Sonar']):
        print(f"{k} -> {v}")
