# -*- coding: utf-8 -*-
import json

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    detected = json.load(f)

detected_keys = {d['key'] for d in detected}

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

other_descs = []
for idx in range(1634, 2400):
    l = lines[idx].strip()
    if '_desc:' in l:
        parts = l.split(':', 1)
        key = parts[0].strip()
        val = parts[1].strip().strip('"')
        if key not in detected_keys:
            other_descs.append((idx + 1, key, val))

print(f"Descs not in detected: {len(other_descs)}")
for line_no, key, val in other_descs:
    print(f"L{line_no} {key}: {val}")
