# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

for line in lines[383:]:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"', line)
    if m:
        k, v = m.group(1), m.group(3)
        tag = k.split('_')[0]
        if tag in ['EQ', 'cruiser', 'midget', 'ship']:
            print(f"{k} -> {v}")
