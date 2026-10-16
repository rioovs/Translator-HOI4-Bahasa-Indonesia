# -*- coding: utf-8 -*-
import json

with open('scripts/batch_2_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items: {len(items)}")
print(f"Types: {set(x['type'] for x in items)}")
total_words = sum(len(x['en'].split()) for x in items)
print(f"Total words: {total_words}")

for i in [0, 50, 100, 150, 200, 250, 281]:
    print(f"[{i}] key: {items[i]['key']}, type: {items[i]['type']}")
    print(f"    en: {repr(items[i]['en'][:120])}")
