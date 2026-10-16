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

# Let's check status for each category
categories = {'title': [], 'desc': [], 'option': [], 'tooltip_other': []}

for k, v in eng_data.items():
    parts = k.split('.')
    suffix = parts[-1]
    if suffix in ('t', 'title') or 'title' in k:
        cat = 'title'
    elif suffix in ('d', 'desc') or suffix.startswith('d_') or suffix.startswith('desc_') or '.d.' in k:
        cat = 'desc'
    elif re.match(r'^[a-z]$', suffix) and suffix not in ('t', 'd'):
        cat = 'option'
    else:
        cat = 'tooltip_other'
    
    braz_val = braz_data.get(k, None)
    is_eng = (braz_val == v)
    categories[cat].append((k, v, braz_val, is_eng))

for cat, items in categories.items():
    total = len(items)
    identical_to_eng = sum(1 for x in items if x[3])
    modified = total - identical_to_eng
    print(f"Category {cat}: Total={total}, Identical to ENG={identical_to_eng}, Modified={modified}")
