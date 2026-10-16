# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

patterns = [
    r'^Republic of (.*)$',
    r'^Socialist Republic of (.*)$',
    r'^People\'s Republic of (.*)$',
    r'^Democratic Republic of (.*)$',
    r'^Democratic People\'s Republic of (.*)$',
    r'^Federal Republic of (.*)$',
    r'^Kingdom of (.*)$',
    r'^Empire of (.*)$',
    r'^State of (.*)$',
    r'^Free State of (.*)$',
    r'^Grand Duchy of (.*)$',
    r'^Duchy of (.*)$',
    r'^Principality of (.*)$',
    r'^Sultanate of (.*)$',
    r'^Emirate of (.*)$',
    r'^Caliphate of (.*)$',
    r'^Commonwealth of (.*)$',
    r'^Federation of (.*)$',
    r'^Confederation of (.*)$',
    r'^Union of (.*)$',
    r'^Commune of (.*)$',
    r'^Protectorate of (.*)$',
    r'^Dominion of (.*)$',
    r'^Islamic Republic of (.*)$',
    r'^Arab Republic of (.*)$',
    r'^Soviet Socialist Republic of (.*)$',
    r'^Soviet Republic of (.*)$',
    r'^(.*) Soviet Socialist Republic$',
    r'^(.*) Soviet Republic$',
    r'^(.*) People\'s Republic$',
    r'^(.*) Socialist Republic$',
    r'^(.*) Democratic Republic$',
    r'^(.*) Free Republic$',
    r'^(.*) Republic$',
    r'^(.*) Kingdom$',
    r'^(.*) Empire$',
    r'^(.*) Federation$',
    r'^(.*) Confederation$',
    r'^(.*) Union$',
    r'^(.*) Commune$',
    r'^Greater (.*)$',
    r'^New (.*)$',
    r'^United (.*)$',
    r'^Free (.*)$',
]

unmatched = []
for r in roots:
    matched = False
    for pat in patterns:
        if re.match(pat, r, re.IGNORECASE):
            matched = True
            break
    if not matched:
        unmatched.append(r)

single = [r for r in unmatched if ' ' not in r and '-' not in r]
multi = [r for r in unmatched if ' ' in r or '-' in r]

print(f"Unmatched total: {len(unmatched)}")
print(f"Unmatched single word: {len(single)}")
print(f"Unmatched multi word: {len(multi)}")

# Inspect first 40 multi word unmatched
print("\nFirst 40 multi-word unmatched:")
for m in multi[:40]:
    print("  ", m)
