import json

with open('chunks_5_6_7_raw.json', encoding='utf-8') as f:
    items = json.load(f)

c7 = items[120:]
for i, x in enumerate(c7):
    print(f"{i+120}: {x['keys'][0]} -> {x['val'][:60]}...")
