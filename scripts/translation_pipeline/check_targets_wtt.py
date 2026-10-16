# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

# Find specific keys mentioned by prompt
target_keys = [
    'GER_mefo_bills_category',
    'GER_mefo_bills_category_desc',
    'GER_cancel_mefos',
    'GER_mefo_bills_mission',
    'anti_communist_raids',
    'anti_communist_raids_desc',
    'anti_democratic_raids',
    'improved_worker_conditions',
    'ban_democratic_party',
    'ban_communist_party',
    'institute_press_censorship_fascist_state'
]

for item in wtt:
    if item['key'] in target_keys or 'mefo' in item['key'].lower() or 'worker' in item['key'].lower():
        print(f"{item['key']}: {repr(item['val'])}")
