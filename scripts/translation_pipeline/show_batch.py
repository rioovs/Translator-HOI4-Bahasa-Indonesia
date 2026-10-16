# -*- coding: utf-8 -*-
import sys
import json

bname = sys.argv[1]
with open(f'scripts/{bname}.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i, it in enumerate(items, 1):
    print(f"{i}. {it['key']}:\n   {it['val']}\n")
