# -*- coding: utf-8 -*-
with open('scripts/still_missing_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

single = [r for r in roots if ' ' not in r and '-' not in r]
multi = [r for r in roots if ' ' in r or '-' in r]

print(f"Total missing: {len(roots)}")
print(f"Single word missing: {len(single)}")
print(f"Multi word missing: {len(multi)}")

print("\nAll single word missing:")
for i, s in enumerate(single, start=1):
    print(f"{i:3}. {s}")
