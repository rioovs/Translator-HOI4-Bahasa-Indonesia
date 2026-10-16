# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('scripts/all_event_td_keys.json', 'r', encoding='utf-8') as f:
    keys = json.load(f)

namespaces = Counter()
for k in keys:
    ns = k['key'].split('.')[0]
    namespaces[ns] += 1

print("Event namespaces and count:")
for ns, c in namespaces.most_common():
    print(f"  {ns}: {c}")
