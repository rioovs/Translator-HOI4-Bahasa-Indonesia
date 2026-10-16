# -*- coding: utf-8 -*-
import re
from collections import Counter

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

suffixes = Counter()
for line in lines[1:]:
    m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
    if not m:
        continue
    k = m.group(2)
    parts = k.split('_')
    prefix = parts[0]
    suffix = '_'.join(parts[1:])
    suffixes[suffix] += 1

print(f"Total cosmetic entries: {sum(suffixes.values())}")
print(f"Total unique cosmetic suffixes: {len(suffixes)}")
for s, c in suffixes.most_common(40):
    print(f"  {s:45}: {c}")
