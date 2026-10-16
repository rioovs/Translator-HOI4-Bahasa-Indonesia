import json

with open('scripts/taog_decisions_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx, i in enumerate(items):
    if idx % 10 == 0:
        print(f"[{idx}] {i['key']}: {i['en'][:60]}")
