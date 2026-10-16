# -*- coding: utf-8 -*-
import json
import re
from collections import Counter

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

opt_vals = []
for l in lines[1:]:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        k = m.group(1)
        v = m.group(3)
        if re.search(r'\.[a-z]$', k) and not k.endswith('.d') and not k.endswith('.t'):
            opt_vals.append(v)

c = Counter(opt_vals)
for val, count in c.most_common(30):
    print(f"{count}x: {val}")
