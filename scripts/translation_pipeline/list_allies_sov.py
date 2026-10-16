# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

items = [x for x in wtt if x['key'].split('_')[0] in ('SOV', 'USA', 'FRA', 'ENG')]
print(f"Total Allies & SOV items: {len(items)}")

with open('allies_sov_keys.txt', 'w', encoding='utf-8') as out:
    for x in items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing allies_sov_keys.txt")
