# -*- coding: utf-8 -*-
import json
import re

with open('scripts/master_roots_lookup.json', 'r', encoding='utf-8') as f:
    master_dict = json.load(f)

def translate_raw(val):
    if not val:
        return ""
    v = val.strip()
    if re.match(r'^\$[A-Za-z0-9_.-]+\$$', v):
        return val # preserve raw variable
    if v in master_dict:
        # preserve trailing space if original had it
        return master_dict[v] + (' ' if val.endswith(' ') else '')
    if v.startswith('the ') or v.startswith('The '):
        sub = re.sub(r'^[tT]he\s+', '', v)
        if sub in master_dict:
            return master_dict[sub] + (' ' if val.endswith(' ') else '')
    return None

files = [
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml",
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml"
]

pat = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$')

total_entries = 0
unmatched_entries = []

for filepath in files:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        for idx, line in enumerate(f):
            m = pat.match(line)
            if m:
                total_entries += 1
                indent, key, ver, val, comment = m.groups()
                tr = translate_raw(val)
                if tr is None:
                    unmatched_entries.append((filepath, idx+1, key, val))

print(f"Total entries tested: {total_entries}")
print(f"Unmatched entries: {len(unmatched_entries)}")
if unmatched_entries:
    for u in unmatched_entries[:20]:
        print(u)
