# -*- coding: utf-8 -*-
import os
import re

eng_dir = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english'
for f in os.listdir(eng_dir):
    if not f.endswith('.yml'): continue
    with open(os.path.join(eng_dir, f), 'r', encoding='utf-8-sig', errors='ignore') as fp:
        c = fp.read()
        m = re.findall(r'([A-Za-z0-9_.-]+):\d*\s*"Oceania"', c)
        if m:
            print(f"{f}: {m}")
        m2 = re.findall(r'([A-Za-z0-9_.-]+):\d*\s*"Dutch East Indies"', c)
        if m2:
            print(f"{f} has Dutch East Indies: {m2[:3]}")

