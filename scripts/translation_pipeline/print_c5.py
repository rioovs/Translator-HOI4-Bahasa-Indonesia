import json

with open('chunks_5_6_7_raw.json', encoding='utf-8') as f:
    items = json.load(f)

c5 = items[:60]
for i, x in enumerate(c5):
    print(f"{i}: {x['keys'][0]} -> {x['val'][:60]}...")
