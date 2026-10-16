# -*- coding: utf-8 -*-
import json

with open('scripts/tags_extracted.json', 'r', encoding='utf-8') as f:
    tags = json.load(f)

# Inspect how many entries each tag has in countries_l_english.yml
with open('scripts/tag_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Total tags in db: {len(db)}")
total_keys_in_db = sum(len(v) for v in db.values())
print(f"Total keys across all tags: {total_keys_in_db}")
