import json

with open('scripts/decisions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(0, 88):
    val_short = data[i]['val'].replace('\n', '\\n')
    if len(val_short) > 75:
        val_short = val_short[:72] + '...'
    print(f"{i:3d} | {data[i]['key']}: \"{val_short}\"")
