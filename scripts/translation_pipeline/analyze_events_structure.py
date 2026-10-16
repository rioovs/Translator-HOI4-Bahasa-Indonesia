# -*- coding: utf-8 -*-
import re

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

key_types = {}
keys_by_suffix = {}
for l in lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        k = m.group(1)
        suffix = k.split('.')[-1] if '.' in k else 'NO_DOT'
        key_types[suffix] = key_types.get(suffix, 0) + 1
        if suffix not in keys_by_suffix:
            keys_by_suffix[suffix] = []
        keys_by_suffix[suffix].append(k)

print("Suffix counts:")
for s, count in sorted(key_types.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  .{s}: {count}")

# Check any other title/desc patterns
non_standard_t = [k for k in keys_by_suffix.get('title', [])]
non_standard_desc = [k for k in keys_by_suffix.get('desc', [])]
print(f"Keys with .title: {len(non_standard_t)}")
print(f"Keys with .desc: {len(non_standard_desc)}")
