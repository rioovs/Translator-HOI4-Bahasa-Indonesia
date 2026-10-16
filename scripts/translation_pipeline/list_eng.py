# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

eng_items = [x for x in mtg if x['key'].startswith('ENG_')]
print(f"Total ENG items: {len(eng_items)}")

with open('eng_keys.txt', 'w', encoding='utf-8') as out:
    for x in eng_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing eng_keys.txt")
