# -*- coding: utf-8 -*-
import re

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

print(f"Total English lines: {len(eng_lines)}")
