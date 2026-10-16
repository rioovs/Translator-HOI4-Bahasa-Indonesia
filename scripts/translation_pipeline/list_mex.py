# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

mex_items = [x for x in mtg if x['key'].startswith('MEX_')]
print(f"Total MEX items: {len(mex_items)}")

for x in mex_items:
    print(f'    t["{x["key"]}"] = {repr(x["val"])}')
