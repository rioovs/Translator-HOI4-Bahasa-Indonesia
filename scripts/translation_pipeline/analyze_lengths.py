import json

with open('scripts/wuw_events_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

short_items = [it for it in items if len(it['en']) <= 60]
med_items = [it for it in items if 60 < len(it['en']) <= 250]
long_items = [it for it in items if len(it['en']) > 250]

print(f"Total: {len(items)}")
print(f"Short (<=60 chars, e.g. titles/options): {len(short_items)} ({len(short_items)/len(items)*100:.1f}%)")
print(f"Medium (61-250 chars): {len(med_items)} ({len(med_items)/len(items)*100:.1f}%)")
print(f"Long (>250 chars, descriptions): {len(long_items)} ({len(long_items)/len(items)*100:.1f}%)")
