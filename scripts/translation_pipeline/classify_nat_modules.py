# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

in_nat = False
nat_keys = []
for idx, line in enumerate(lines):
    if line.strip().startswith('### Nation Specific Modules'):
        in_nat = True
        continue
    if not in_nat:
        continue
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if m:
        nat_keys.append((idx + 1, m.group(1), m.group(3)))

print(f"Total nation specific module keys: {len(nat_keys)}")

# Let's see what nations are present
countries = set()
for _, k, _ in nat_keys:
    tag = k.split('_')[0]
    countries.add(tag)

print(f"Tags found: {sorted(list(countries))}")

# Check what kind of strings exist in values
patterns = {}
for _, k, v in nat_keys:
    # let's classify by text structure
    if re.search(r'\d+mm\s+Belt\s*/\s*\d+mm\s+Deck', v, re.I):
        patterns['Belt/Deck mm'] = patterns.get('Belt/Deck mm', 0) + 1
    elif re.search(r'\d+in\s+Belt\s*/\s*\d+in\s+Deck', v, re.I):
        patterns['Belt/Deck in'] = patterns.get('Belt/Deck in', 0) + 1
    elif 'Belt' in v or 'Deck' in v:
        patterns['Other Belt/Deck'] = patterns.get('Other Belt/Deck', 0) + 1
    elif re.search(r'\d+x\s+\d+mm\s+Torpedo\s+(Tubes|Launcher)', v, re.I):
        patterns['Torpedo Tubes/Launcher mm'] = patterns.get('Torpedo Tubes/Launcher mm', 0) + 1
    elif re.search(r'\d+x\s+\d+in\s+Torpedo\s+(Tubes|Launcher)', v, re.I):
        patterns['Torpedo Tubes/Launcher in'] = patterns.get('Torpedo Tubes/Launcher in', 0) + 1
    elif 'Torpedo' in v:
        patterns['Other Torpedo'] = patterns.get('Other Torpedo', 0) + 1
    elif 'Engine' in v or 'Shp' in v or 'hp' in v or 'Diesel' in v or 'Turbine' in v:
        patterns['Engine/Power'] = patterns.get('Engine/Power', 0) + 1
    elif 'Radar' in v or 'Sonar' in v:
        patterns['Radar/Sonar'] = patterns.get('Radar/Sonar', 0) + 1
    else:
        patterns['Weapon/Designation'] = patterns.get('Weapon/Designation', 0) + 1

print("\nValue classification:")
for p, c in sorted(patterns.items(), key=lambda x: -x[1]):
    print(f"  {p}: {c}")
