import json

with open('scripts/lar_operations.json', 'r', encoding='utf-8') as f:
    lar = json.load(f)

for chunk_idx in range(4):
    start = chunk_idx * 70
    end = min(len(lar), (chunk_idx + 1) * 70)
    print(f"\n==================== CHUNK {chunk_idx}: items {start} to {end-1} ====================")
    for i in range(start, end):
        val = lar[i]['val'].replace('\n', '\\n')
        if len(val) > 85:
            val = val[:82] + '...'
        print(f"{i:3d} | {lar[i]['key']}: \"{val}\"")
