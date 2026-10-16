# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

print(f"Total MTG entries: {len(mtg)}")

# Categorize by prefix or group
groups = {}
for item in mtg:
    k = item['key']
    prefix = k.split('_')[0]
    if prefix in ['ENG', 'USA', 'HOL', 'MEX', 'MTG', 'mtg']:
        grp = prefix
    else:
        grp = 'OTHER'
    groups.setdefault(grp, []).append(item)

for g, items in groups.items():
    print(f"Group {g}: {len(items)} items")
