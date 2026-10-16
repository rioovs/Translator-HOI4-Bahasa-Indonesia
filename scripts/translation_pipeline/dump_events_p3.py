import json

with open('scripts/events_part3_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scripts/events_p3.txt', 'w', encoding='utf-8') as f:
    for idx, i in enumerate(items):
        f.write(f"{idx:03d}: {i['key']} | {i['en']}\n")

print(f"Dumped {len(items)} items to events_p3.txt")
