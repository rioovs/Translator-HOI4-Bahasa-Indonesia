import json

with open('scripts/taog_events_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scripts/all_events.txt', 'w', encoding='utf-8') as f:
    for idx, item in enumerate(items):
        f.write(f"{idx:03d} | {item['key']} | {item['en']}\n")

print(f"Total events dumped: {len(items)}")
