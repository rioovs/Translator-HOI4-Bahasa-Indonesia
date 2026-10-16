# -*- coding: utf-8 -*-
import json

with open('scripts/wuw_batches/batch5_ger_part1.json', 'r', encoding='utf-8') as f:
    b5 = json.load(f)

with open('scripts/wuw_batches/batch6_ger_part2.json', 'r', encoding='utf-8') as f:
    b6 = json.load(f)

print("--- MEFO & Four Year Plan & Special Project keys in Batch 5 & 6 ---")
for b in [b5, b6]:
    for item in b:
        k = item['key'].lower()
        if any(w in k for w in ['mefo', 'four_year', 'wunderwaffe', 'wuw', 'project', 'inner_circle']):
            if not k.endswith('_desc'):
                print(f"  {item['key']}: {item['val']}")
