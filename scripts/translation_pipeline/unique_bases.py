# -*- coding: utf-8 -*-
import json

with open('scripts/tags_extracted.json', 'r', encoding='utf-8') as f:
    tags = json.load(f)

# Let's see all unique base names and adjectives
base_names = {}
adj_names = {}
for t in tags:
    tag = t['tag']
    base = t['base']
    adj = t['adj']
    if base:
        base_names[base] = tag
    if adj:
        adj_names[adj] = tag

print(f"Unique base names: {len(base_names)}")
print(f"Unique adjectives: {len(adj_names)}")
