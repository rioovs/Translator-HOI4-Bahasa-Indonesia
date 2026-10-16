# -*- coding: utf-8 -*-
import re

def check_terms_in_backup(terms):
    path = r'f:\New Coding\rea-hoi4-indonesia\backup_braz_por_original\countries_cosmetic_l_braz_por.yml'
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    for t in terms:
        print(f"=== Term: {t} ===")
        found = 0
        for line in lines:
            if t in line:
                print("  ", line.strip())
                found += 1
                if found >= 5:
                    break

check_terms_in_backup(['Reichskommissariat', 'Bundesstaat', 'Volkskommissariat', 'Danubian State', 'European'])
