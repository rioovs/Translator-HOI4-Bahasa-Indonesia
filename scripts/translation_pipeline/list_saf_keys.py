# -*- coding: utf-8 -*-
import json

with open('scripts/SAF.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total SAF keys: {len(items)}")
for i, it in enumerate(items):
    print(f"{i+1:02d}. {it['key']}")
