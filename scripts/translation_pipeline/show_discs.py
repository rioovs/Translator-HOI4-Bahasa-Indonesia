# -*- coding: utf-8 -*-
import json

with open('scripts/tag_discrepancies.json', 'r', encoding='utf-8') as f:
    discs = json.load(f)

for d in discs:
    if d['chunk'] == 12:
        print('='*70)
        print(f"Chunk {d['chunk']} | {d['key']} | missing: {d['missing_tags']}")
        print(f"ENG: {d['eng']}")
        print(f"IND: {d['ind']}")
