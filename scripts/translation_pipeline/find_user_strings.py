# -*- coding: utf-8 -*-
import os

eng_dir = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english'

targets = [
    'Organization indicates combat readiness',
    'Having equal or greater Piercing',
    'We cannot risk waiting any longer, we must strike while the iron is hot',
    'In order to fund our growing military industry, and to keep this secret from British',
    'The Dutch form a \'back door\'',
    'We must crack down on communist elements in our nation',
    'Gain Base Stability:',
    'The Declaration of Independence',
    'MEFO Bills',
    'Anti-Communist Raids',
    'Improved Worker Conditions'
]

print("Searching across all files in english localisation...")
for f in os.listdir(eng_dir):
    if not f.endswith('.yml'): continue
    p = os.path.join(eng_dir, f)
    with open(p, 'r', encoding='utf-8-sig', errors='ignore') as fp:
        content = fp.read()
        for t in targets:
            if t.lower() in content.lower():
                print(f"Found '{t[:35]}' in: {f}")
