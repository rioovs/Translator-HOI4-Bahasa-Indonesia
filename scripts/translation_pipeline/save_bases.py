# -*- coding: utf-8 -*-
import json

with open('scripts/tags_extracted.json', 'r', encoding='utf-8') as f:
    tags = json.load(f)

bases = sorted(list(set([t['base'] for t in tags if t['base']])))
with open('scripts/all_unique_bases.txt', 'w', encoding='utf-8') as out:
    for b in bases:
        out.write(b + '\n')
print(f"Wrote {len(bases)} base names to scripts/all_unique_bases.txt")
