import json

with open('scripts/lar_operations.json', 'r', encoding='utf-8') as f:
    lar = json.load(f)

print(f"\n==================== CHUNK: items 140 to 216 ====================")
for i in range(140, 217):
    val = lar[i]['val'].replace('\n', '\\n')
    if len(val) > 85:
        val = val[:82] + '...'
    print(f"{i:3d} | {lar[i]['key']}: \"{val}\"")
