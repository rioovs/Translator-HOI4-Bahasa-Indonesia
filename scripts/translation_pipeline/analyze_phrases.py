# -*- coding: utf-8 -*-
import re
from collections import Counter

def analyze_phrases(files):
    words = Counter()
    patterns = Counter()
    var_patterns = set()
    
    for path in files:
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"', line)
                if not m:
                    continue
                k, ver, val = m.groups()
                # Find vars
                for var in re.findall(r'\$[A-Za-z0-9_|+-^%*]+\$', val):
                    var_patterns.add(var)
                # Count keywords
                for w in ['Empire', 'Kingdom', 'Republic', 'Principality', 'Grand Duchy', 'Duchy', 
                          'Confederation', 'Federation', 'Commonwealth', 'Union', 'State', 'States',
                          'Protectorate', 'Dominion', 'Colony', 'Commune', 'People\'s', 'Socialist',
                          'Democratic', 'Free', 'Soviet', 'Military', 'Government', 'Junta', 'Territory',
                          'Reich', 'Sultanate', 'Emirate', 'Caliphate', 'Tsardom', 'Mandate', 'Zone',
                          'Occupation']:
                    if re.search(r'\b' + re.escape(w) + r'\b', val, re.IGNORECASE):
                        words[w] += 1
                        
    print("Found variables:", sorted(list(var_patterns)))
    print("Frequent government/political terms:")
    for w, c in words.most_common():
        print(f"  {w}: {c}")

analyze_phrases([
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml'
])
