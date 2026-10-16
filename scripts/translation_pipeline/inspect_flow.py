import json

with open('scripts/wuw_events_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Print intervals of 100 items to see the flow
for start in range(0, len(items), 200):
    chunk = items[start:start+200]
    first_k = chunk[0]['key']
    last_k = chunk[-1]['key']
    print(f"[{start:4d} - {start+len(chunk)-1:4d}] {first_k}  ==>  {last_k}")
