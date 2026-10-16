# -*- coding: utf-8 -*-
import json

with open('mtg_en.json', 'r', encoding='utf-8') as f:
    mtg = json.load(f)

with open('mtg_eng_usa_utf8.txt', 'w', encoding='utf-8') as out:
    for g_name in ['USA', 'ENG']:
        out.write(f"\n=================== {g_name} ===================\n")
        for item in mtg:
            k = item['key']
            pfx = k.split('_')[0]
            if g_name == pfx:
                out.write(f"{k}: {repr(item['val'])}\n")
print("Done writing mtg_eng_usa_utf8.txt")
