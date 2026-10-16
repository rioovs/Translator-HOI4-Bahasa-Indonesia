# -*- coding: utf-8 -*-
with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\research_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    r_lines = f.readlines()

for line in r_lines:
    if any(k in line for k in ['depth_charge', 'torpedo', 'sonar', 'fire_control', 'battery', 'damage_control']):
        print(line.strip())
