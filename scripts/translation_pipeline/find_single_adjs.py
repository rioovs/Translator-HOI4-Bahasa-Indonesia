# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

with open('scripts/adjectives_id.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

# Find adjectives in roots
adj_endings = ['ian', 'ean', 'an', 'ese', 'ish', 'ic', 'i']
found_adjs = {}
for r in roots:
    # If single word
    if ' ' not in r and '-' not in r:
        if r in adj_map:
            continue
        if r in base_map:
            continue
        for end in adj_endings:
            if r.endswith(end):
                found_adjs[r] = r

print(f"Potential single-word adjectives not yet in adj_map: {len(found_adjs)}")
for a in list(found_adjs.keys())[:40]:
    print("  ", a)
