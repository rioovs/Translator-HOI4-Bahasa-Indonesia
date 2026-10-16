# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

for g_name in ['OTHER', 'mtg', 'MTG', 'MEX', 'HOL']:
    print(f"\n=================== {g_name} ===================")
    for item in mtg:
        k = item['key']
        pfx = k.split('_')[0]
        if g_name == 'OTHER' and pfx not in ['ENG', 'USA', 'HOL', 'MEX', 'MTG', 'mtg']:
            print(f"{k}: {repr(item['val'])}")
        elif g_name == pfx:
            print(f"{k}: {repr(item['val'])}")
