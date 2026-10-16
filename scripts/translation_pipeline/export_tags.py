# -*- coding: utf-8 -*-
import json

with open('scripts/tag_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

print(f"Total tags: {len(db)}")
items = []
for tag in sorted(db.keys()):
    d = db[tag]
    base = d.get('', '')
    adj = d.get('ADJ', '')
    dem = d.get('democratic', '')
    neu = d.get('neutrality', '')
    com = d.get('communism', '')
    fas = d.get('fascism', '')
    items.append({
        'tag': tag,
        'base': base,
        'adj': adj,
        'dem': dem,
        'neu': neu,
        'com': com,
        'fas': fas
    })

with open('scripts/tags_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

print("Saved tags_extracted.json")
