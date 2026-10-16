# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

with open(src_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    lines = f.readlines()

pattern = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$')

matched = []
unmatched = []
comments_and_empty = []

for idx, line in enumerate(lines[1:], start=2):
    s = line.strip()
    if not s or s.startswith('#'):
        comments_and_empty.append((idx, line))
        continue
    m = pattern.match(line)
    if m:
        indent, key, ver, val, comment = m.groups()
        matched.append((idx, indent, key, ver, val, comment))
    else:
        unmatched.append((idx, line))

print(f"Matched entries: {len(matched)}")
print(f"Comments and empty: {len(comments_and_empty)}")
print(f"Unmatched lines: {len(unmatched)}")

if unmatched:
    print("Sample unmatched lines:")
    for u in unmatched:
        print(f"  Line {u[0]}: {repr(u[1])}")
