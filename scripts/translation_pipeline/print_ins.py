# -*- coding: utf-8 -*-
import re

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml', 'r', encoding='utf-8-sig') as f:
    for line in f:
        m = re.match(r'^\s*(INS[A-Za-z0-9_.-]*):(\d*)\s*"(.*)"', line)
        if m:
            print(f'{m.group(1)}: "{m.group(3)}"')
