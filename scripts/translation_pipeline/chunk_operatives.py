import json

with open('scripts/operatives.json', 'r', encoding='utf-8') as f:
    ops = json.load(f)

for i in range(0, len(ops), 80):
    chunk = ops[i:i+80]
    with open(f'scripts/ops_chunk_{i//80}.json', 'w', encoding='utf-8') as f_out:
        json.dump(chunk, f_out, ensure_ascii=False, indent=2)

print(f"Created {(len(ops)+79)//80} chunks for operatives")
