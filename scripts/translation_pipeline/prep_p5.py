import json

with open('scripts/focus_part5_extracted.json', 'r', encoding='utf-8') as f:
    p5 = json.load(f)

# Dump all p5 items to a format easy to translate
with open('scripts/p5_for_trans.json', 'w', encoding='utf-8') as f:
    json.dump({it['key']: it['val'] for it in p5}, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(p5)} items to scripts/p5_for_trans.json")
