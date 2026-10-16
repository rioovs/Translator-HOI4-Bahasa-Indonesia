# -*- coding: utf-8 -*-
import re

target_file = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wuw_focus_l_braz_por.yml'
with open(target_file, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

sample_keys = [
    'HABSBURG_part_of_something_bigger',
    'HABSBURG_joint_consumer_goods_endeavors',
    'wuw_HUN_protect_austria',
    'AUS_second_brothers_war_desc',
    'BEL_defend_the_meuse',
    'COG_the_prussia_of_africa',
    'GER_the_four_year_plan',
    'GER_inner_circle_title_text',
    'GER_fuhrerprinzip_inner_circle_tt',
    'GER_the_mannheim_project_ww',
    'GER_wunderwaffe_dornberger_trait_tt',
    'GER_asian_spheres_of_influence_tt',
]

pattern = re.compile(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"')
found = {}
for line in lines:
    m = pattern.match(line)
    if m and m.group(1) in sample_keys:
        found[m.group(1)] = m.group(3)

for k in sample_keys:
    print(f"[{k}]")
    print(f"  -> {found.get(k)}\n")
