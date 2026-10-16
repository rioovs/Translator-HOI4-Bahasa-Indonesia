# -*- coding: utf-8 -*-
from collections import Counter

with open('scripts/untranslated_roots.txt', 'r', encoding='utf-8') as f:
    untranslated = [line.strip() for line in f if line.strip()]

words = Counter()
for u in untranslated:
    for w in u.split():
        words[w] += 1

print(f"Total untranslated roots: {len(untranslated)}")
print("Top 50 words in untranslated roots:")
for w, c in words.most_common(50):
    print(f"  {w:18}: {c}")
