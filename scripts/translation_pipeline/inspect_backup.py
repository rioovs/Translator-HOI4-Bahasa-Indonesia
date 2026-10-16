# -*- coding: utf-8 -*-
import re

def inspect_backup(path):
    print(f"=== Inspecting backup: {path} ===")
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    for i in range(1, 50):
        print(lines[i], end='')

inspect_backup(r'f:\New Coding\rea-hoi4-indonesia\backup_braz_por_original\countries_l_braz_por.yml')
