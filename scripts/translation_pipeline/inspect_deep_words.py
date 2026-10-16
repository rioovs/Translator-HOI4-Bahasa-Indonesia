# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('scripts/unmatched_deep.txt', 'r', encoding='utf-8') as f:
    items = [line.strip() for line in f if line.strip()]

words = Counter()
for item in items:
    for w in item.split():
        words[w] += 1

print(f"Total items: {len(items)}")
print(f"Total unique words: {len(words)}")
for w, c in words.most_common(50):
    print(f"  {w:20}: {c}")
