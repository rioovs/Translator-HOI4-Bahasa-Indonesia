# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_raw_values.json', 'r', encoding='utf-8') as f:
    values = json.load(f)

unique_roots = set()
for val in values.keys():
    if re.match(r'^\$[A-Za-z0-9_]+\$$', val):
        continue
    # Strip leading the/The
    stripped = re.sub(r'^[tT]he\s+', '', val).strip()
    if stripped:
        unique_roots.add(stripped)

print(f"Total unique root strings to translate: {len(unique_roots)}")

# Save to file
with open('scripts/all_unique_roots.txt', 'w', encoding='utf-8') as out:
    for r in sorted(list(unique_roots)):
        out.write(r + '\n')

print("Saved scripts/all_unique_roots.txt")
