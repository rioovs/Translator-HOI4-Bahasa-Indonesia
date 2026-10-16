# -*- coding: utf-8 -*-
import re

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    wtt_text = f.read()

for kw in ['raid', 'press', 'ban', 'democrat', 'communis', 'worker']:
    matches = [line.strip() for line in wtt_text.splitlines() if kw in line.lower()]
    print(f'WTT {kw}: {len(matches)}')
    for m in matches[:5]:
        print('  ', m[:120])
