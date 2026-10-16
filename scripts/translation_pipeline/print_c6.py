import json

with open('chunks_5_6_7_raw.json', encoding='utf-8') as f:
    items = json.load(f)

c6 = items[60:120]
for i, x in enumerate(c6):
    print(f"{i+60}: {x['keys'][0]} -> {x['val'][:60]}...")
