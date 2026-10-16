import json

with open('scripts/events_part1_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx, i in enumerate(items):
    print(f"{idx:03d}: {i['key']} -> {i['en']}")
