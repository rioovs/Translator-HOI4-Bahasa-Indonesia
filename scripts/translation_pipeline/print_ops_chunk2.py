import json

with open('scripts/operatives.json', 'r', encoding='utf-8') as f:
    ops = json.load(f)

print(f"\n==================== CHUNK 2: items 160 to 239 ====================")
for i in range(160, 240):
    val = ops[i]['val'].replace('\n', '\\n')
    if len(val) > 85:
        val = val[:82] + '...'
    print(f"{i:3d} | {ops[i]['key']}: \"{val}\"")
