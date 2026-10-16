# -*- coding: utf-8 -*-
import json
import re

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

armors = [v for v in unique_vals if re.search(r'\bBelt\b', v, re.I) or re.search(r'\bDeck\b', v, re.I)]
print(f"Total armor strings: {len(armors)}")
for a in sorted(armors):
    print(f"  {repr(a)}")
