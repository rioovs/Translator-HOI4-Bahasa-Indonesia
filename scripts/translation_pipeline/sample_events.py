# -*- coding: utf-8 -*-
import random
import re

with open('localisation/braz_por/events_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

pairs = []
for l in lines[1:]:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        k, v = m.group(1), m.group(3)
        if k.endswith('.t') or k.endswith('.d'):
            pairs.append((k, v))

random.seed(42)
for k, v in random.sample(pairs, 12):
    print(f"[{k}] -> {v}\n")
