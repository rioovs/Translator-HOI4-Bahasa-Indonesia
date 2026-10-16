# -*- coding: utf-8 -*-
import json

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

batches = {
    'CAN_continuous_misc': [],
    'SAF': [],
    'NZL': [],
    'RAJ': [],
    'USA': []
}

for it in items:
    k = it['key']
    tag = k.split('_')[0]
    if tag == 'CAN' or tag == 'continuous' or tag in ['confirm', 'ROM', 'AST', 'HUN', 'BEL']:
        batches['CAN_continuous_misc'].append(it)
    elif tag == 'SAF':
        batches['SAF'].append(it)
    elif tag == 'NZL':
        batches['NZL'].append(it)
    elif tag == 'RAJ':
        batches['RAJ'].append(it)
    elif tag == 'USA':
        batches['USA'].append(it)
    else:
        batches['CAN_continuous_misc'].append(it)

for bname, blist in batches.items():
    print(f"{bname}: {len(blist)} items")
    with open(f'scripts/{bname}.json', 'w', encoding='utf-8') as out:
        json.dump(blist, out, indent=2, ensure_ascii=False)
