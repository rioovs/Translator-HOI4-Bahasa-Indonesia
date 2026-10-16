# -*- coding: utf-8 -*-
import json

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    tag = it['key'].split('_')[0]
    if tag in ['HUN', 'confirm', 'ROM', 'AST', 'BEL', 'continuous']:
        print(f"L{it['line']} {it['key']}: {it['val']}")
