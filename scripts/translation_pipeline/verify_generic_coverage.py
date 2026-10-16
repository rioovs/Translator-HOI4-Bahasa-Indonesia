# -*- coding: utf-8 -*-
import json
from trans_chunk_1 import TRANS_CHUNK_1
from trans_chunk_2 import TRANS_CHUNK_2
from trans_chunk_3 import TRANS_CHUNK_3

all_trans = {}
duplicates = []

for c_name, c_dict in [('CHUNK 1', TRANS_CHUNK_1), ('CHUNK 2', TRANS_CHUNK_2), ('CHUNK 3', TRANS_CHUNK_3)]:
    for k, v in c_dict.items():
        if k in all_trans:
            duplicates.append((k, c_name))
        all_trans[k] = v

print(f"Total keys translated in generic chunks: {len(all_trans)}")
print(f"Duplicates: {duplicates}")

with open('scripts/part1_2.json', 'r', encoding='utf-8') as f:
    part1_2 = json.load(f)

part1_2_keys = [it['key'] for it in part1_2]
tail_keys = ['ship_light_battery_sub', 'ship_light_battery_sub_desc', 'EQ_MOD_CAT_ship_light_battery_sub_TITLE',
             'cruiser_submarine_specialization', 'cruiser_submarine_specialization_desc',
             'midget_submarine_specialization', 'midget_submarine_specialization_desc']

target_keys = set(part1_2_keys + tail_keys)

missing = target_keys - set(all_trans.keys())
extra = set(all_trans.keys()) - target_keys

print(f"Target keys total: {len(target_keys)}")
print(f"Missing keys: {len(missing)} -> {missing}")
print(f"Extra keys: {len(extra)} -> {extra}")
