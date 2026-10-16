# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

with open('wtt_general_samples.txt', 'w', encoding='utf-8') as out:
    for item in wtt:
        k = item['key']
        pfx = k.split('_')[0]
        if pfx not in ('form', 'CHI', 'liberate', 'JAP', 'develop', 'GER', 'MAN', 'PRC', 'SOV', 'USA', 'FRA', 'ENG', 'reintegrate'):
            out.write(f"{k}: {repr(item['val'])}\n")

print("Done writing wtt_general_samples.txt")
