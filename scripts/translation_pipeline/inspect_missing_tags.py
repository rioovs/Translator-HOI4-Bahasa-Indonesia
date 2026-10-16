# -*- coding: utf-8 -*-
import json

with open('scripts/tag_db.json', 'r', encoding='utf-8') as f:
    db = json.load(f)

missing = {}
for tag, data in db.items():
    if '' not in data:
        # Check democratic or neutrality or fascism or communism
        name = data.get('democratic', data.get('neutrality', data.get('communism', data.get('fascism'))))
        adj = data.get('democratic_ADJ', data.get('neutrality_ADJ', data.get('communism_ADJ', data.get('fascism_ADJ'))))
        missing[tag] = {'name': name, 'adj': adj, 'keys': list(data.keys())}

print(f"Tags without base key: {len(missing)}")
for tag, d in missing.items():
    print(f"{tag:4}: name='{d['name']}' | adj='{d['adj']}'")
