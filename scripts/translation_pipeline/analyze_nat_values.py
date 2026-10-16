# -*- coding: utf-8 -*-
import json
import re

with open('scripts/parsed_ship_modules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nat_items = [d for d in data if d['type'] == 'key_val' and d['line_idx'] >= 383 and not d['key'].startswith(('ship_light_battery_sub', 'EQ_MOD_CAT_ship_light_battery_sub', 'cruiser_submarine_specialization', 'midget_submarine_specialization'))]

print(f"Total nation specific items: {len(nat_items)}")

# Let's inspect unique patterns in nat_items
# Check for any items containing non-proper nouns:
unique_values = {}
for it in nat_items:
    unique_values[it['value']] = unique_values.get(it['value'], 0) + 1

print(f"Total unique values: {len(unique_values)}")

# Save to json for analysis
with open('scripts/nat_unique_values.json', 'w', encoding='utf-8') as f:
    json.dump(unique_values, f, ensure_ascii=False, indent=2)
