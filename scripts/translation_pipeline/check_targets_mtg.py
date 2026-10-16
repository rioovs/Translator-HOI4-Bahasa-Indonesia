# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

for item in mtg:
    if 'gateway' in item['key'].lower() or 'dutch_trade' in item['key'].lower():
        print(f"{item['key']}: {repr(item['val'])}")
