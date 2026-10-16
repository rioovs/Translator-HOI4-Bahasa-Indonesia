# -*- coding: utf-8 -*-
import json
import sys

chunk_num = sys.argv[1] if len(sys.argv) > 1 else "1"
start_idx = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end_idx = int(sys.argv[3]) if len(sys.argv) > 3 else 9999

with open(f'scripts/b1_chunk_{chunk_num}_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx, it in enumerate(items[start_idx:end_idx], start=start_idx):
    print(f"[{idx+1}/{len(items)}] {it['key']} ({it['type']})")
    print(f"EN: {it['en']}")
    print("-" * 60)
