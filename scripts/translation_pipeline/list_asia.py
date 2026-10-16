# -*- coding: utf-8 -*-
import json

with open('wtt_en.json', 'r', encoding='utf-8') as f:
    wtt = json.load(f)

asia_items = [x for x in wtt if x['key'].split('_')[0] in ('CHI', 'PRC', 'JAP', 'MAN')]
print(f"Total Asia items: {len(asia_items)}")

with open('asia_keys.txt', 'w', encoding='utf-8') as out:
    for x in asia_items:
        out.write(f'    t["{x["key"]}"] = {repr(x["val"])}\n')
print("Done writing asia_keys.txt")
