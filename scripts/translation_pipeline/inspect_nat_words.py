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

# Collect all tokens
word_counts = {}
for k, v in nat_items:
    words = re.findall(r'[A-Za-z]+', v)
    for w in words:
        word_counts[w] = word_counts.get(w, 0) + 1

# Filter common designations like Mk, mm, cm, in, Shp, hp, QF, BL, etc.
naval_tech_terms = ['Belt', 'Deck', 'Engine', 'Turbine', 'Diesel', 'Diesels', 'Boiler', 'Boilers',
                    'Torpedo', 'Tubes', 'Tube', 'Launcher', 'Launchers', 'Radar', 'Sonar',
                    'Flight', 'Battery', 'Auto', 'Loading', 'Mount', 'Guns', 'Gun',
                    'Heavy', 'Light', 'Cruiser', 'Steam', 'Shaft', 'Armor', 'Armour', 'Hangar']

print("Occurrences of identifiable English words in Nation Modules:")
for w, c in sorted(word_counts.items(), key=lambda x: -x[1]):
    if w in naval_tech_terms or w.lower() in [x.lower() for x in naval_tech_terms]:
        print(f"  {w}: {c}")

print("\nLet's print every nation module that has any of these words:")
for k, v in nat_items:
    if any(re.search(r'\b' + re.escape(w) + r'\b', v, re.I) for w in naval_tech_terms):
        print(f"{k}: {v}")
