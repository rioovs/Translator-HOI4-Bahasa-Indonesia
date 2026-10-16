# -*- coding: utf-8 -*-
import re

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

english_words = [' the ', ' of ', ' to ', ' and ', ' with ', ' will ', ' our ', ' for ', ' from ', ' that ', ' this ']

for idx in range(1634):
    l = lines[idx].strip()
    if not l or l.startswith('#'):
        continue
    if '_desc:' in l:
        parts = l.split(':', 1)
        key = parts[0].strip()
        val = parts[1].strip().strip('"')
        vlow = ' ' + val.lower() + ' '
        count = sum(1 for w in english_words if w in vlow)
        if count >= 2:
            print(f'Line {idx+1}: {key} -> {val[:70]} (hits: {count})')
