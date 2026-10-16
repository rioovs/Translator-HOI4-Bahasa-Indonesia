# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

usa_items = [x for x in mtg if x['key'].startswith('USA_')]
print(f"Total USA items: {len(usa_items)}")

with open('usa_keys.txt', 'w', encoding='utf-8') as out:
    for x in usa_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing usa_keys.txt")
