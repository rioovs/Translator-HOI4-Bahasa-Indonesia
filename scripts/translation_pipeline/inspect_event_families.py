import json

with open('scripts/taog_events_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group items by event family
families = {}
for item in items:
    k = item['key']
    fam = k.split('.')[0]
    families.setdefault(fam, []).append(item)

for fam, fam_items in sorted(families.items()):
    print(f"=== {fam} ({len(fam_items)} keys) ===")
    for item in fam_items[:6]:
        print(f"  {item['key']}: {item['en'][:70]}")
