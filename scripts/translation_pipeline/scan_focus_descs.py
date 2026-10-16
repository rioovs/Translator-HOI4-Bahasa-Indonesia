# -*- coding: utf-8 -*-
import re

file_path = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
with open(file_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
english_words = [' the ', ' to ', ' of ', ' and ', ' in ', ' that ', ' is ', ' was ', ' for ', ' with ', ' as ', ' on ', ' by ', ' will ', ' our ', ' we ', ' their ', ' have ', ' from ', ' which ']

matches = []
for idx, line in enumerate(lines, 1):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    # regex for key:0 "value" or key: "value"
    m = re.match(r'^([a-zA-Z0-9_]+):\s*(?:0\s*)?\"(.*)\"$', s)
    if m:
        key, val = m.group(1), m.group(2)
        if key.endswith('_desc'):
            val_clean = ' ' + re.sub(r'§[a-zA-Z0-9!]', ' ', val).lower() + ' '
            val_clean = re.sub(r'\$[a-zA-Z0-9_]+\$', ' ', val_clean)
            hits = [w.strip() for w in english_words if w in val_clean]
            if len(hits) >= 2 or any(w in val_clean for w in [' the ', ' and ', ' of ']):
                matches.append((idx, key, val, hits))

print(f"Found {len(matches)} suspicious _desc lines.")
for idx, key, val, hits in matches[:15]:
    print(f"L{idx} [{key}]: {val[:80]}... (hits: {hits[:5]})")

with open('scripts/suspicious_descs.txt', 'w', encoding='utf-8') as out:
    for idx, key, val, hits in matches:
        out.write(f"{idx} | {key} | {val}\n")
