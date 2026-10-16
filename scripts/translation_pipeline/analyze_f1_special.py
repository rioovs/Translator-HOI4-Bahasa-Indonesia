# -*- coding: utf-8 -*-
import json

with open('scripts/file1_special_entries.json', 'r', encoding='utf-8') as f:
    entries = json.load(f)

unique_vals = set(v for k, v in entries)
print(f"Total special entries: {len(entries)}")
print(f"Unique values in special entries: {len(unique_vals)}")

# Group by patterns
categories = {}
for k, v in entries:
    pattern = v
    if '$OVERLORDADJ$' in v:
        pattern = 'OVERLORD: ' + v
    elif '$' in v:
        pattern = 'VAR: ' + v
    categories[pattern] = categories.get(pattern, 0) + 1

print(f"Total distinct patterns: {len(categories)}")
for p, c in sorted(categories.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  {p[:60]:60}: {c}")
