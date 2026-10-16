# -*- coding: utf-8 -*-
import json

with open('scripts/wuw_batches/batch5_ger_part1.json', 'r', encoding='utf-8') as f:
    b5 = json.load(f)

with open('scripts/wuw_batches/batch6_ger_part2.json', 'r', encoding='utf-8') as f:
    b6 = json.load(f)

print("Sample titles in Batch 5:")
for item in b5:
    if not item['key'].endswith('_desc') and not item['key'].endswith('_tt'):
        print(f"  {item['key']}: {item['val']}")
    if len(b5) > 30 and item == b5[30]:
        break

print("\nSample titles in Batch 6:")
for item in b6:
    if not item['key'].endswith('_desc') and not item['key'].endswith('_tt'):
        print(f"  {item['key']}: {item['val']}")
    if len(b6) > 30 and item == b6[30]:
        break
