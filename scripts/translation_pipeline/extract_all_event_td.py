# -*- coding: utf-8 -*-
import re
import json

eng_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'

with open(eng_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

event_keys = []
for l in lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        k, ver, v = m.group(1), m.group(2), m.group(3)
        parts = k.split('.')
        suffix = parts[-1]
        
        # Check if it's a title or description
        is_title = (suffix in ('t', 'title') or 'title' in k)
        is_desc = (suffix in ('d', 'desc') or suffix.startswith('d_') or suffix.startswith('desc_') or '.d.' in k)
        
        if is_title or is_desc:
            event_keys.append({
                'key': k,
                'version': ver,
                'type': 'title' if is_title else 'desc',
                'en': v
            })

print(f"Total event title/desc keys: {len(event_keys)}")
title_count = sum(1 for x in event_keys if x['type'] == 'title')
desc_count = sum(1 for x in event_keys if x['type'] == 'desc')
print(f"Titles: {title_count}, Descs: {desc_count}")

with open('scripts/all_event_td_keys.json', 'w', encoding='utf-8') as f:
    json.dump(event_keys, f, ensure_ascii=False, indent=2)

print("Saved to scripts/all_event_td_keys.json")
