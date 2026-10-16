# -*- coding: utf-8 -*-
import json

with open('scripts/batch_2_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

chunks = [
    (0, 70),
    (70, 140),
    (140, 210),
    (210, 282)
]

for idx, (s, e) in enumerate(chunks, 1):
    c_items = items[s:e]
    with open(f'scripts/b2_chunk_{idx}_source.json', 'w', encoding='utf-8') as out:
        json.dump(c_items, out, ensure_ascii=False, indent=2)
    print(f"Chunk {idx}: {len(c_items)} items, words: {sum(len(x['en'].split()) for x in c_items)}")
