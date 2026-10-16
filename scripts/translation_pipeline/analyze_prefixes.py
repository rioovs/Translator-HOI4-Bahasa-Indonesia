# -*- coding: utf-8 -*-
import re
from collections import Counter

def analyze_patterns(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    vals = set()
    for line in lines[1:]:
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if m:
            vals.add(m.group(4))
            
    print(f"=== Patterns in {path} ===")
    prefixes = Counter()
    for v in vals:
        # Check starting phrases
        for p in ['the ', 'The ', 'Republic of ', 'Kingdom of ', 'State of ', 'Empire of ', 
                  'People\'s Republic of ', 'Socialist Republic of ', 'Democratic Republic of ',
                  'Federal Republic of ', 'Free State of ', 'Union of ', 'Federation of ',
                  'Grand Duchy of ', 'Duchy of ', 'Principality of ', 'Sultanate of ',
                  'Emirate of ', 'Commonwealth of ', 'Confederation of ', 'Protectorate of ',
                  'Dominion of ', 'Commune of ', 'Islamic Republic of ', 'Greater ']:
            if v.startswith(p):
                prefixes[p] += 1
                break
    for p, c in prefixes.most_common():
        print(f"  Starts with '{p}': {c}")

analyze_patterns(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml')
analyze_patterns(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml')
