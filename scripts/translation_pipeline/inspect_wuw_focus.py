# -*- coding: utf-8 -*-
import re
from collections import Counter

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

with open(src_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

prefixes = Counter()
keys = []
comments = []

for line in lines:
    stripped = line.strip()
    if stripped.startswith('#'):
        comments.append(stripped)
        continue
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', line)
    if m:
        k = m.group(1)
        keys.append((k, m.group(3)))
        prefix = k.split('_')[0]
        prefixes[prefix] += 1

print(f"Total key entries: {len(keys)}")
print("Prefix distribution:")
for p, c in prefixes.most_common(20):
    print(f"  {p}: {c}")

print("\nSections / Comments:")
for c in comments:
    if len(c) > 3 and not c.startswith('#####') and 'TREE' in c.upper():
        print(f"  {c}")
