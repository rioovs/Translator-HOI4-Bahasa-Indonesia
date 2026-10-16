# -*- coding: utf-8 -*-
import json

with open('scripts/NZL.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(20):
    it = items[i]
    print(f"{i+1}. {it['key']}:\n   {it['val']}\n")
