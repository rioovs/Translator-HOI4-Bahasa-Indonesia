# -*- coding: utf-8 -*-
import json

with open('scripts/batch_5_source.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def dump_range(start, end, filename):
    with open(filename, 'w', encoding='utf-8') as out:
        for i in range(start, end):
            item = data[i]
            out.write(f"=== [{i}] {item['key']} ({item['type']}) ===\n")
            out.write(item['en'] + "\n\n")

dump_range(0, 71, 'scripts/chunk_1_china.txt')
dump_range(71, 143, 'scripts/chunk_2_italy_france.txt')
dump_range(143, 215, 'scripts/chunk_3_japan_italy_pol.txt')
dump_range(215, 304, 'scripts/chunk_4_pol_britain_japan_france.txt')
print("Dumped 4 chunks successfully!")
