# -*- coding: utf-8 -*-
import json
from collections import Counter

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total English descs: {len(items)}")
tags = Counter(it['key'].split('_')[0] for it in items)
for tag, count in tags.most_common():
    print(f"  {tag}: {count}")
