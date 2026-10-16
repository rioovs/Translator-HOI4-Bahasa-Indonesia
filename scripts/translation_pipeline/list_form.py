# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

form_items = [x for x in wtt if x['key'].startswith('form_') or x['key'].startswith('reintegrate_')]
print(f"Total Form items: {len(form_items)}")

with open('form_keys.txt', 'w', encoding='utf-8') as out:
    for x in form_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing form_keys.txt")
