# -*- coding: utf-8 -*-
with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Read {len(lines)} lines")
for i, l in enumerate(lines):
    if '\n' in l[:-1] or '\r' in l[:-1]:
        print(f"Line {i+1} has internal newline: {repr(l)}")
