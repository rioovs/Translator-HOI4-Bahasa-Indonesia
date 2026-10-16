# -*- coding: utf-8 -*-
import json
import re

with open('scripts/unmatched_deep.txt', 'r', encoding='utf-8') as f:
    items = [line.strip() for line in f if line.strip()]

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

# Build a comprehensive translation dictionary for all remaining 779 items
# We'll use systematic rules + extensive vocabulary
REMAINING_DICT = {}

for item in items:
    # 1. Check exact Overlord
    if item == "$OVERLORDADJ$ Chinese colony":
        REMAINING_DICT[item] = "Koloni Tiongkok $OVERLORDADJ$"
        continue
    if item == "$OVERLORDADJ$ Occupation Zone of Lombardy and Venice":
        REMAINING_DICT[item] = "Zona Pendudukan Lombardia dan Venesia $OVERLORDADJ$"
        continue
    if item == "$OVERLORDADJ$ Occupation Zone of Naples and Sicily":
        REMAINING_DICT[item] = "Zona Pendudukan Napoli dan Sisilia $OVERLORDADJ$"
        continue
    if item == "$OVERLORDADJ$ Occupation Zone of Sardinia and Piedmont":
        REMAINING_DICT[item] = "Zona Pendudukan Sardinia dan Piedmont $OVERLORDADJ$"
        continue
    if item == "$OVERLORDADJ$ Occupation Zone of Tuscany":
        REMAINING_DICT[item] = "Zona Pendudukan Toskana $OVERLORDADJ$"
        continue
    if item == "$OVERLORDADJ$ Raj":
        REMAINING_DICT[item] = "Raj $OVERLORDADJ$"
        continue
        
    # Check if already in base_map or adj_map
    if item in base_map:
        REMAINING_DICT[item] = base_map[item]
        continue
    if item in adj_map:
        REMAINING_DICT[item] = adj_map[item]
        continue

print(f"Direct base/adj/overlord matched: {len(REMAINING_DICT)} out of {len(items)}")
