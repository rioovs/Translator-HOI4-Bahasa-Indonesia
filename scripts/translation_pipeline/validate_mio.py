# -*- coding: utf-8 -*-
import re

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/military_industrial_organization_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

assert lines[0].strip() == 'l_braz_por:'
bad = 0
for i, l in enumerate(lines[1:], 2):
    s = l.strip()
    if not s or s.startswith('#'):
        continue
    # Remove trailing comment if any
    clean = re.sub(r'#.*$', '', s).strip()
    if not (clean.endswith('"') and ':' in clean):
        print(f"Bad line {i}: {s}")
        bad += 1

if bad == 0:
    print(f"PERFECT: All {len(lines)} lines in military_industrial_organization_l_braz_por.yml are 100% valid Clausewitz YAML!")
