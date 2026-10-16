import json

with open('scripts/lar_operations.json', 'r', encoding='utf-8') as f:
    lar = json.load(f)

print(f"Total lar keys: {len(lar)}")
for i in range(0, len(lar), 70):
    chunk = lar[i:i+70]
    with open(f'scripts/lar_chunk_{i//70}.json', 'w', encoding='utf-8') as f_out:
        json.dump(chunk, f_out, ensure_ascii=False, indent=2)

print(f"Created {(len(lar)+69)//70} chunks for lar_operations")
