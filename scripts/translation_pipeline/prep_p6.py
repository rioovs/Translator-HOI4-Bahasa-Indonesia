import json

with open('scripts/focus_part6_extracted.json', 'r', encoding='utf-8') as f:
    p6 = json.load(f)

with open('scripts/p6_for_trans.json', 'w', encoding='utf-8') as f:
    json.dump({it['key']: it['val'] for it in p6}, f, indent=2, ensure_ascii=False)

print(f"Dumped {len(p6)} items to scripts/p6_for_trans.json")
