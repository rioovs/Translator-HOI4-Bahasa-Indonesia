import json
import os

os.makedirs('scripts/chunks', exist_ok=True)

with open('scripts/wuw_events_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

chunk_size = 200
num_chunks = (len(items) + chunk_size - 1) // chunk_size

for c_idx in range(num_chunks):
    start = c_idx * chunk_size
    end = min(start + chunk_size, len(items))
    chunk_items = items[start:end]
    filepath = f'scripts/chunks/chunk_{c_idx}.json'
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chunk_items, f, indent=2, ensure_ascii=False)
    print(f"Saved {filepath} with {len(chunk_items)} items ({start} to {end-1})")
