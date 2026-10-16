# -*- coding: utf-8 -*-
import re

with open('localisation/braz_por/wuw_events_l_braz_por.yml', 'r', encoding='utf-8-sig', errors='ignore') as f:
    text = f.read()

ger_matches = re.findall(r'"([^"]*jerman[^"]*)"', text, re.IGNORECASE)
print('Indonesian matches in wuw_events:', len(ger_matches))
for m in ger_matches[:5]:
    print(' ', m[:80])
