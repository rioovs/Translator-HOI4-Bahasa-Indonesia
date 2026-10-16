import json

with open('scripts/taog_focus_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

part1 = [] # INSHOL, ABDA, HOL, generic
ins_items = []

for item in items:
    k = item['key']
    if k.startswith('INSHOL_') or k.startswith('ABDA_') or k.startswith('HOL_') or not k.startswith('INS_'):
        part1.append(item)
    else:
        ins_items.append(item)

print(f"Total focus items: {len(items)}")
print(f"Part 1 (INSHOL, ABDA, HOL, generic): {len(part1)}")
print(f"INS items: {len(ins_items)}")

# Split ins_items into 3 chunks of roughly equal size (~172 each)
part2 = ins_items[:175]
part3 = ins_items[175:350]
part4 = ins_items[350:]

print(f"Part 2: {len(part2)}")
print(f"Part 3: {len(part3)}")
print(f"Part 4: {len(part4)}")

with open('scripts/focus_part1_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part1, f, ensure_ascii=False, indent=2)
with open('scripts/focus_part2_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part2, f, ensure_ascii=False, indent=2)
with open('scripts/focus_part3_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part3, f, ensure_ascii=False, indent=2)
with open('scripts/focus_part4_raw.json', 'w', encoding='utf-8') as f:
    json.dump(part4, f, ensure_ascii=False, indent=2)
