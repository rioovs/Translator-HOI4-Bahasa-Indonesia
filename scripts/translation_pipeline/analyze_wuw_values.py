# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

with open(src_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    lines = f.readlines()

pattern = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$')

pure_vars = []
short_titles = []
descriptions = []
tooltips = []
others = []

for idx, line in enumerate(lines[1:], start=2):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = pattern.match(line)
    if not m:
        continue
    indent, key, ver, val, comment = m.groups()
    
    if re.match(r'^\$[A-Za-z0-9_.-]+\$$', val.strip()):
        pure_vars.append((key, val))
    elif key.endswith('_desc'):
        descriptions.append((key, val))
    elif key.endswith('_tt'):
        tooltips.append((key, val))
    elif len(val.split()) <= 6 and not val.endswith('.'):
        short_titles.append((key, val))
    else:
        others.append((key, val))

print(f"Total entries: {len(pure_vars) + len(descriptions) + len(tooltips) + len(short_titles) + len(others)}")
print(f"Pure variables (e.g. $VAR$): {len(pure_vars)}")
print(f"Descriptions: {len(descriptions)}")
print(f"Tooltips: {len(tooltips)}")
print(f"Short titles / focus names: {len(short_titles)}")
print(f"Others: {len(others)}")

print("\nSample pure vars:")
for k, v in pure_vars[:10]:
    print(f"  {k}: {v}")
