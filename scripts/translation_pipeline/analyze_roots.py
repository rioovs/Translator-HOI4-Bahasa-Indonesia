# -*- coding: utf-8 -*-
from collections import Counter

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

single_word = [r for r in roots if ' ' not in r and '-' not in r]
multi_word = [r for r in roots if ' ' in r or '-' in r]

print(f"Total roots: {len(roots)}")
print(f"Single word roots: {len(single_word)}")
print(f"Multi-word roots: {len(multi_word)}")

# Count words in multi-word roots
word_counts = Counter()
for r in multi_word:
    for w in r.split():
        word_counts[w] += 1

print("\nTop 40 words in multi-word roots:")
for w, c in word_counts.most_common(40):
    print(f"  {w:15}: {c}")
