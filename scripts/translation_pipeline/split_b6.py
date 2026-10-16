import json

with open(r'f:\New Coding\rea-hoi4-indonesia\scripts\batch_6_source.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items: {len(items)}")

chunk_size = 70
for i in range(0, len(items), chunk_size):
    chunk = items[i:i+chunk_size]
    chunk_idx = i // chunk_size
    filename = f'f:\\New Coding\\rea-hoi4-indonesia\\scripts\\b6_chunk_{chunk_idx}.json'
    with open(filename, 'w', encoding='utf-8') as cf:
        json.dump(chunk, cf, ensure_ascii=False, indent=2)
    print(f"Chunk {chunk_idx}: {len(chunk)} items ({i} to {i+len(chunk)-1}) -> {filename}")
