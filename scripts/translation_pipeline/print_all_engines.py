# -*- coding: utf-8 -*-
import json
import re

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

engines = [v for v in unique_vals if re.search(r'\bEngine\b', v, re.I) or re.search(r'\bReactor\b', v, re.I) or re.search(r'\bDiesels?\b', v, re.I) or re.search(r'\bElectric\b', v, re.I) or re.search(r'\bPressurized\b', v, re.I)]
print(f"Total engine strings: {len(engines)}")
for e in sorted(engines):
    print(f"  {repr(e)}")
