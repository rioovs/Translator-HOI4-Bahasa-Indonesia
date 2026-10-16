# -*- coding: utf-8 -*-
import json

with open('scripts/parsed_ship_modules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

part1_2 = [d for d in data if d['type'] == 'key_val' and d['line_idx'] < 383]
print(f"Total keys in Part 1 & 2: {len(part1_2)}")

with open('scripts/part1_2.json', 'w', encoding='utf-8') as f:
    json.dump(part1_2, f, ensure_ascii=False, indent=2)
