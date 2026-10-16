# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_raw_values.json', 'r', encoding='utf-8') as f:
    values = json.load(f)

pure_vars = []
starts_with_the = []
contains_overlord = []
has_color_or_bracket = []
other = []

for val in values.keys():
    if re.match(r'^\$[A-Za-z0-9_]+\$$', val):
        pure_vars.append(val)
    elif val.startswith('the ') or val.startswith('The '):
        starts_with_the.append(val)
    elif 'OVERLORD' in val:
        contains_overlord.append(val)
    elif '§' in val or '[' in val:
        has_color_or_bracket.append(val)
    else:
        other.append(val)

print(f"Total values: {len(values)}")
print(f"Pure variables: {len(pure_vars)}")
print(f"Starts with 'the '/'The ': {len(starts_with_the)}")
print(f"Contains OVERLORD: {len(contains_overlord)}")
print(f"Has color code or bracket: {len(has_color_or_bracket)}")
print(f"Other unique values: {len(other)}")
