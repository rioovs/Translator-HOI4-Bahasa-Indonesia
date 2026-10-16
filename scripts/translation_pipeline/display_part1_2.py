# -*- coding: utf-8 -*-
import json

with open('scripts/part1_2.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(0, len(items), 50):
    print(f"=== Items {i} to {min(i+50, len(items))} ===")
    for it in items[i:min(i+50, len(items))]:
        print(f"{it['key']}: {repr(it['value'])}")
