# -*- coding: utf-8 -*-
import json
from collections import defaultdict

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

def inspect_keys(data, name):
    groups = defaultdict(list)
    for item in data:
        k = item['key']
        # classify
        parts = k.split('_')
        g = parts[0]
        if g in ('form', 'liberate', 'develop', 'reintegrate', 'coring'):
            g = parts[0]
        elif len(parts) > 1 and parts[0] in ('GER', 'CHI', 'JAP', 'MAN', 'PRC', 'SOV', 'USA', 'ENG', 'HOL', 'MEX', 'FRA', 'ITA', 'YUG', 'POL'):
            g = parts[0]
        else:
            g = 'general'
        groups[g].append(item)
    print(f'=== {name} ({len(data)} entries) ===')
    for g, items in sorted(groups.items(), key=lambda x: -len(x[1])):
        print(f'  Group {g:12s}: {len(items):4d} entries')

inspect_keys(wtt, 'WTT')
inspect_keys(mtg, 'MTG')
