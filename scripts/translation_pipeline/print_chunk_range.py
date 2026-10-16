import json
import sys

chunk_name = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

with open(f'scripts/chunks/{chunk_name}.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(start, min(end, len(data))):
    item = data[i]
    print(f"=== [{i}] {item['key']} ===")
    print(item['en'])
