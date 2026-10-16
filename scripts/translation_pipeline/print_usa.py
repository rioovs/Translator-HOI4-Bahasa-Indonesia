# -*- coding: utf-8 -*-
import json

with open('scripts/USA.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total USA items: {len(items)}")
for i, it in enumerate(items, 1):
    print(f"{i}. {it['key']}:\n   {it['val']}\n")
