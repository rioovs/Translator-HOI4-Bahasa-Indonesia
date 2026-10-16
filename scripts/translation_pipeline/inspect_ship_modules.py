# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
header = lines[0].strip()
print(f"Header: {header}")

keys = []
comments = []
unmatched = []

for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if not s:
        continue
    if s.startswith('#'):
        comments.append((idx, s))
        continue
    m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if m:
        keys.append((idx, m.group(2), m.group(4)))
    else:
        unmatched.append((idx, line))

print(f"Total keys: {len(keys)}")
print(f"Comments: {len(comments)}")
print(f"Unmatched lines: {len(unmatched)}")
if unmatched:
    for u in unmatched[:10]:
        print(f"Unmatched {u[0]}: {repr(u[1])}")

print("\nSections / Comments:")
for c in comments:
    print(f"L{c[0]}: {c[1]}")
