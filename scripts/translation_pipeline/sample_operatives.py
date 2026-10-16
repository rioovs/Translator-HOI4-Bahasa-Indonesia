import json

with open('scripts/operatives.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total keys: {len(data)}")
for i, item in enumerate(data):
    val_short = item['val'].replace('\n', '\\n')
    if len(val_short) > 75:
        val_short = val_short[:72] + '...'
    if i % 10 == 0 or i < 20 or i > len(data) - 20:
        print(f"{i:3d} | {item['key']}: \"{val_short}\"")
