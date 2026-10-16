# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

ger_items = [x for x in wtt if x['key'].startswith('GER_')]
print(f"Total GER items: {len(ger_items)}")

with open('ger_keys.txt', 'w', encoding='utf-8') as out:
    for x in ger_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing ger_keys.txt")
