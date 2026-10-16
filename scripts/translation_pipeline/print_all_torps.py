# -*- coding: utf-8 -*-
import json
import re

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

torps = [v for v in unique_vals if re.search(r'\bTorpedo\b', v, re.I) or re.search(r'\bTorp\b', v, re.I) or re.search(r'\bTTs?\b', v) or re.search(r'\bTubes\b', v, re.I)]
print(f"Total torpedo strings: {len(torps)}")
for t in sorted(torps):
    print(f"  {repr(t)}")
