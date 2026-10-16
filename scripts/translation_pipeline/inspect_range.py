# -*- coding: utf-8 -*-
import json
import sys

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
end = int(sys.argv[2]) if len(sys.argv) > 2 else 60

with open('scripts/part1_2.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx in range(start, min(end, len(items))):
    it = items[idx]
    print(f"[{idx}] {it['key']}: {it['value']}")
