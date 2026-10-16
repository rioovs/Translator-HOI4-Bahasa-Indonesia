import json

with open('scripts/operatives.json', 'r', encoding='utf-8') as f:
    ops = json.load(f)

for chunk_idx in range(1, 6):
    start = chunk_idx * 80
    end = min(len(ops), (chunk_idx + 1) * 80)
    print(f"\n=== CHUNK {chunk_idx}: items {start} to {end-1} ===")
    for i in range(start, end):
        val = ops[i]['val'].replace('\n', '\\n')
        if len(val) > 70:
            val = val[:67] + '...'
        print(f"{i:3d} | {ops[i]['key']}: \"{val}\"")
