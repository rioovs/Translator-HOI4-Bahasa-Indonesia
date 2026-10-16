# -*- coding: utf-8 -*-
with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print(f"Current lines: {len(lines)}")
# Check line endings:
for i in range(10):
    print(f"L{i+1}: {repr(lines[i])}")
