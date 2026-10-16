import json

with open('scripts/taog_decisions_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total decisions: {len(items)}")

# Print keys in blocks of 50 to inspect categories
for i in range(0, len(items), 50):
    chunk = items[i:i+50]
    print(f"--- Block {i} to {i+len(chunk)} ---")
    for item in chunk[:5]:
        print(f"  {item['key']}: {item['en'][:60]}")
