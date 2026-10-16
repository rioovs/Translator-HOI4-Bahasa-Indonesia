# -*- coding: utf-8 -*-
import json

with open('scripts/part1_2.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by category/module base
keys = [it['key'] for it in items]
print(f"Total keys: {len(keys)}")

# Let's verify tail keys
tail_keys = ['ship_light_battery_sub', 'ship_light_battery_sub_desc', 'EQ_MOD_CAT_ship_light_battery_sub_TITLE',
             'cruiser_submarine_specialization', 'cruiser_submarine_specialization_desc',
             'midget_submarine_specialization', 'midget_submarine_specialization_desc']
print(f"Tail keys present in part1_2? {[k in keys for k in tail_keys]}")
