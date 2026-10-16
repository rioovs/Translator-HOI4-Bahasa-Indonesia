# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('scripts/tag_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

suffixes = Counter()
for tag, data in db.items():
    for s in data.keys():
        suffixes[s] += 1

print(f"Total unique suffixes: {len(suffixes)}")
for s, c in suffixes.most_common(50):
    print(f"  {s:35}: {c}")
