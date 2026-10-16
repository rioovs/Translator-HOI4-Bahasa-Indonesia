# -*- coding: utf-8 -*-
import json

with open('scripts/remaining_after_morph.txt', 'r', encoding='utf-8') as f:
    items = [line.strip() for line in f if line.strip()]

# Let's inspect items by chunks of 50
print(f"Total remaining: {len(items)}")
with open('scripts/remaining_items.json', 'w', encoding='utf-8') as out:
    json.dump(items, out, indent=2, ensure_ascii=False)
