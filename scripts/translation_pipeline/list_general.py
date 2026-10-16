# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

known_prefixes = ('form', 'CHI', 'liberate', 'JAP', 'develop', 'GER', 'MAN', 'PRC', 'SOV', 'USA', 'FRA', 'ENG', 'reintegrate')

general_items = [x for x in wtt if x['key'].split('_')[0] not in known_prefixes]
print(f"Total General items: {len(general_items)}")

with open('general_keys.txt', 'w', encoding='utf-8') as out:
    for x in general_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing general_keys.txt")
