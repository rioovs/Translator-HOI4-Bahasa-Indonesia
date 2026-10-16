# -*- coding: utf-8 -*-
import json

with open('scripts/batch_1_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

chunks = [
    items[0:72],
    items[72:144],
    items[144:215],
    items[215:285]
]

for i, ch in enumerate(chunks):
    word_count = sum(len(x['en'].split()) for x in ch)
    print(f"Chunk {i+1}: {len(ch)} items, {word_count} words ({ch[0]['key']} to {ch[-1]['key']})")
    with open(f'scripts/b1_chunk_{i+1}_source.json', 'w', encoding='utf-8') as cf:
        json.dump(ch, cf, ensure_ascii=False, indent=2)

print("Split completed successfully.")
