# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('scripts/unresolved_roots.txt', 'r', encoding='utf-8') as f:
    items = [line.strip() for line in f if line.strip()]

print(f"Total remaining items: {len(items)}")

# Count words
word_counts = Counter()
for i in items:
    for w in i.split():
        word_counts[w] += 1

print("\nTop 40 words in remaining items:")
for w, c in word_counts.most_common(40):
    print(f"  {w:20}: {c}")

# Show sample 30 items
print("\nSample 30 remaining items:")
for i in items[:30]:
    print("  ", i)
