# -*- coding: utf-8 -*-
import re

for name, path in [
    ('wtt', r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml'),
    ('mtg', r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml')
]:
    with open(path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        content = f.read()
    print(f'=== {name} ===')
    for kw in ['mefo', 'gateway', 'anti_communist', 'anti-communist', 'worker', 'censor', 'ban_']:
        matches = [line.strip() for line in content.splitlines() if re.search(r'\b' + kw + r'\b', line, re.I)]
        print(f'Keyword {kw}: {len(matches)} matches')
        for m in matches[:3]:
            print('  ', m[:100])
