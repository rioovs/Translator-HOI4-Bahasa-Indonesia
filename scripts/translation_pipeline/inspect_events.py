# -*- coding: utf-8 -*-
import re

with open('F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Total lines in events_l_english: {len(lines)}")
# Sample lines 1 to 25
for i in range(1, 25):
    print(f"[{i+1}] {lines[i].strip()}")
