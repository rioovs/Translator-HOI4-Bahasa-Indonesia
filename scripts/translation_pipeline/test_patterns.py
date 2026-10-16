# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

patterns = [
    (r'^Republic of (.*)$', 'Republik {}'),
    (r'^Socialist Republic of (.*)$', 'Republik Sosialis {}'),
    (r'^People\'s Republic of (.*)$', 'Republik Rakyat {}'),
    (r'^Democratic Republic of (.*)$', 'Republik Demokratik {}'),
    (r'^Democratic People\'s Republic of (.*)$', 'Republik Rakyat Demokratik {}'),
    (r'^Federal Republic of (.*)$', 'Republik Federal {}'),
    (r'^Kingdom of (.*)$', 'Kerajaan {}'),
    (r'^Empire of (.*)$', 'Kekaisaran {}'),
    (r'^State of (.*)$', 'Negara {}'),
    (r'^Free State of (.*)$', 'Negara Bebas {}'),
    (r'^Grand Duchy of (.*)$', 'Keharyapatihan {}'),
    (r'^Duchy of (.*)$', 'Kadipaten {}'),
    (r'^Principality of (.*)$', 'Kepangeranan {}'),
    (r'^Sultanate of (.*)$', 'Kesultanan {}'),
    (r'^Emirate of (.*)$', 'Keamiran {}'),
    (r'^Caliphate of (.*)$', 'Kekhalifahan {}'),
    (r'^Commonwealth of (.*)$', 'Persemakmuran {}'),
    (r'^Federation of (.*)$', 'Federasi {}'),
    (r'^Confederation of (.*)$', 'Konfederasi {}'),
    (r'^Union of (.*)$', 'Uni {}'),
    (r'^Commune of (.*)$', 'Komune {}'),
    (r'^Protectorate of (.*)$', 'Protektorat {}'),
    (r'^Dominion of (.*)$', 'Dominion {}'),
    (r'^Islamic Republic of (.*)$', 'Republik Islam {}'),
    (r'^Arab Republic of (.*)$', 'Republik Arab {}'),
    (r'^Soviet Socialist Republic of (.*)$', 'Republik Sosialis Soviet {}'),
    (r'^Soviet Republic of (.*)$', 'Republik Soviet {}'),
    (r'^(.*) Soviet Socialist Republic$', 'Republik Sosialis Soviet {}'),
    (r'^(.*) Soviet Republic$', 'Republik Soviet {}'),
    (r'^(.*) People\'s Republic$', 'Republik Rakyat {}'),
    (r'^(.*) Socialist Republic$', 'Republik Sosialis {}'),
    (r'^(.*) Democratic Republic$', 'Republik Demokratik {}'),
    (r'^(.*) Free Republic$', 'Republik Bebas {}'),
    (r'^(.*) Republic$', 'Republik {}'),
    (r'^(.*) Kingdom$', 'Kerajaan {}'),
    (r'^(.*) Empire$', 'Kekaisaran {}'),
    (r'^(.*) Federation$', 'Federasi {}'),
    (r'^(.*) Confederation$', 'Konfederasi {}'),
    (r'^(.*) Union$', 'Uni {}'),
    (r'^(.*) Commune$', 'Komune {}'),
    (r'^Greater (.*)$', '{} Raya'),
    (r'^New (.*)$', '{} Baru'),
    (r'^United (.*)$', '{} Bersatu'),
    (r'^Free (.*)$', '{} Bebas'),
]

matched = 0
unmatched = []
for r in roots:
    is_match = False
    for pat, template in patterns:
        m = re.match(pat, r, re.IGNORECASE)
        if m:
            matched += 1
            is_match = True
            break
    if not is_match:
        unmatched.append(r)

print(f"Total roots: {len(roots)}")
print(f"Matched by common political formulas: {matched}")
print(f"Unmatched (base names, adjectives, special names): {len(unmatched)}")
