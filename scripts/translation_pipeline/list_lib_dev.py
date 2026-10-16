# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

lib_dev_items = [x for x in wtt if x['key'].startswith('liberate_') or x['key'].startswith('develop_')]
print(f"Total liberate & develop items: {len(lib_dev_items)}")

with open('lib_dev_keys.txt', 'w', encoding='utf-8') as out:
    for x in lib_dev_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing lib_dev_keys.txt")
