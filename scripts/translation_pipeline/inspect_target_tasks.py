# -*- coding: utf-8 -*-
import os
import re

eng_dir = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english'
files = [
    'designer_l_english.yml',
    'tank_modules_l_english.yml',
    'ship_modules_l_english.yml',
    'plane_designer_l_english.yml',
    'unit_l_english.yml',
    'wuw_focus_l_english.yml',
    'wuw_events_l_english.yml',
    'wtt_focus_l_english.yml',
    'wtt_events_l_english.yml'
]

print("=== TARGET FILES ANALYSIS ===")
for f in files:
    p = os.path.join(eng_dir, f)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8-sig', errors='ignore') as fp:
            lines = fp.readlines()
            keys = sum(1 for l in lines if re.match(r'^\s*[A-Za-z0-9_.-]+:(\d*)\s*"', l))
            print(f"{f:<30}: {keys:>5} keys | {len(lines):>5} lines")
    else:
        print(f"{f:<30}: NOT FOUND")
