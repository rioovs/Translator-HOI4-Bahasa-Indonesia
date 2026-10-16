# -*- coding: utf-8 -*-
import re

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

keys = []
for i, l in enumerate(lines[1:], 2):
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        keys.append((m.group(1), m.group(3)))

print(f"Total lines: {len(lines)}")
print(f"Total valid keys: {len(keys)}")

# Let's count types
t_keys = [k for k, v in keys if k.endswith('.t')]
d_keys = [k for k, v in keys if k.endswith('.d')]
opt_keys = [k for k, v in keys if re.search(r'\.[a-z]$', k) and not k.endswith('.d') and not k.endswith('.t')]
other_keys = [k for k, v in keys if k not in t_keys and k not in d_keys and k not in opt_keys]

print(f"Title keys (.t): {len(t_keys)}")
print(f"Description keys (.d): {len(d_keys)}")
print(f"Option buttons (.a, .b, .c...): {len(opt_keys)}")
print(f"Other keys: {len(other_keys)}")
