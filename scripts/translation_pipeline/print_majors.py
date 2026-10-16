# -*- coding: utf-8 -*-
import re

def print_tag_keys(path, tags):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    for line in lines:
        for t in tags:
            m = re.match(r'^\s*(' + t + r'(_[A-Za-z0-9_.-]+)?):(\d*)\s*"(.*)"', line)
            if m:
                k, sub, ver, val = m.groups()
                print(f"{k}: \"{val}\"")
                break

print("=== countries_l_english.yml ===")
print_tag_keys(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml', 
               ['GER', 'ENG', 'SOV', 'USA', 'FRA', 'ITA', 'JAP', 'HOL', 'INS'])

print("\n=== countries_cosmetic_l_english.yml ===")
print_tag_keys(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml', 
               ['GER', 'ENG', 'SOV', 'USA', 'FRA', 'ITA', 'JAP', 'HOL', 'INS'])
