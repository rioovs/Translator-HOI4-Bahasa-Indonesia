# -*- coding: utf-8 -*-
import re
import json

paths = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml'
]

unique_strings = {}

for path in paths:
    with open(path, 'r', encoding='utf-8-sig') as f:
        for line in f:
            m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
            if m:
                k, v = m.group(2), m.group(4)
                if v not in unique_strings:
                    unique_strings[v] = []
                unique_strings[v].append(k)

print(f"Total unique raw values: {len(unique_strings)}")

# Save list of all unique values
with open('scripts/all_raw_values.json', 'w', encoding='utf-8') as f:
    json.dump({k: len(v) for k, v in unique_strings.items()}, f, indent=2, ensure_ascii=False)

print("Saved scripts/all_raw_values.json")
