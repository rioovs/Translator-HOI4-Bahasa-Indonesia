import json

with open('scripts/decisions.json', 'r', encoding='utf-8') as f:
    dec = json.load(f)

for i in range(0, len(dec), 50):
    chunk = dec[i:i+50]
    with open(f'scripts/dec_chunk_{i//50}.json', 'w', encoding='utf-8') as f_out:
        json.dump(chunk, f_out, ensure_ascii=False, indent=2)

print(f"Created { (len(dec)+49)//50 } chunks for decisions")
