# -*- coding: utf-8 -*-
import re

def find_overlord_keys(files):
    for path in files:
        print(f"=== {path} ===")
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                if 'OVERLORD' in line:
                    print(line.strip())

find_overlord_keys([
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml'
])
