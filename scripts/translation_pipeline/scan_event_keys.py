# -*- coding: utf-8 -*-
import re

braz_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
eng_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'

with open(braz_path, 'r', encoding='utf-8-sig') as f:
    braz_lines = f.readlines()

with open(eng_path, 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

eng_data = {}
for l in eng_lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        eng_data[m.group(1)] = m.group(3)

braz_data = {}
for l in braz_lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        braz_data[m.group(1)] = m.group(3)

diffs = [(k, eng_data[k], braz_data[k]) for k in braz_data if (k.endswith('.t') or k.endswith('.d')) and eng_data.get(k) != braz_data[k]]
print(f"Total diffs in .t and .d: {len(diffs)}")
for k, e, b in diffs[:15]:
    print(f"KEY: {k}")
    print(f"  ENG:  {e}")
    print(f"  BRAZ: {b}\n")
