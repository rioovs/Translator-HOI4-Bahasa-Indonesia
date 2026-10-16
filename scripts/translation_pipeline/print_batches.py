# -*- coding: utf-8 -*-
import json

with open('scripts/tags_extracted.json', 'r', encoding='utf-8') as f:
    tags = json.load(f)

# Inspect tags by continent / region or alphabetical
print("Total tags:", len(tags))
for i in range(0, len(tags), 25):
    chunk = tags[i:i+25]
    print(f"\n--- Batch {i//25 + 1} ({i} to {min(i+25, len(tags))}) ---")
    for t in chunk:
        print(f"{t['tag']:4} | Base: {t['base']:20} | Adj: {t['adj']:18} | Dem: {t['dem']:25}")
