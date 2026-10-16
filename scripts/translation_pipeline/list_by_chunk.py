# -*- coding: utf-8 -*-
import json

with open('scripts/tag_discrepancies.json', 'r', encoding='utf-8') as f:
    discs = json.load(f)

by_chunk = {}
for d in discs:
    c = d['chunk']
    by_chunk.setdefault(c, []).append(d)

for c in sorted(by_chunk.keys()):
    print(f"\n=== CHUNK {c}: {len(by_chunk[c])} items ===")
    for item in by_chunk[c]:
        print(f"Key: {item['key']}")
        print(f"  ENG: {item['eng']}")
        print(f"  IND (old): {item['ind']}")
        print(f"  Missing: {item['missing_tags']}")
