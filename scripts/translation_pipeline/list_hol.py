# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

hol_items = [x for x in mtg if x['key'].startswith('HOL_')]
print(f"Total HOL items: {len(hol_items)}")

with open('hol_keys.txt', 'w', encoding='utf-8') as out:
    for x in hol_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing hol_keys.txt")
