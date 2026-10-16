import json
import sys

chunk_num = sys.argv[1] if len(sys.argv) > 1 else '1'
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else 100

with open(f'scripts/b4_chunks/chunk_{chunk_num}.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in range(start, min(end, len(items))):
    print(f"[{i}] {items[i]['key']}")
    print(items[i]['en'])
    print("-" * 50)
