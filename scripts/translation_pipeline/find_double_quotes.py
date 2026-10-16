# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '""' in l:
        print(f"L{i+1}: {repr(l)}")
