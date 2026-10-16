import json

with open('scripts/taog_decisions_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for i in items[:40]:
    print(f"[{i['key']}]\n{i['en']}\n")
