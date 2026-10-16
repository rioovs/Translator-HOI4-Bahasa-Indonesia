# -*- coding: utf-8 -*-
import json
import sys

chunk_num = sys.argv[1] if len(sys.argv) > 1 else '1'
with open(f'scripts/b2_chunk_{chunk_num}_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i, x in enumerate(items):
    print(f"{i}: {x['key']} ({x['type']})")
