# -*- coding: utf-8 -*-
import json
import re

from trans_batch1_can_misc import translations_batch1
from trans_batch2_saf import translations_batch2
from trans_batch3_nzl import translations_batch3
from trans_batch4_raj import translations_batch4
from trans_batch5_usa import translations_batch5

all_trans = {}
for b in [translations_batch1, translations_batch2, translations_batch3, translations_batch4, translations_batch5]:
    all_trans.update(b)

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    needed = json.load(f)

mismatches = 0
for it in needed:
    k = it['key']
    orig = it['val']
    trans = all_trans[k]
    
    # Check variables $...$ and [ROOT...]
    orig_vars = set(re.findall(r'\$[a-zA-Z0-9_]+\$|\[[a-zA-Z0-9_\.]+\]', orig))
    trans_vars = set(re.findall(r'\$[a-zA-Z0-9_]+\$|\[[a-zA-Z0-9_\.]+\]', trans))
    if orig_vars != trans_vars:
        print(f"Var mismatch in {k}:")
        print(f"  Orig vars: {orig_vars}")
        print(f"  Trans vars: {trans_vars}")
        mismatches += 1
        
    # Check colors §X...§!
    orig_colors = set(re.findall(r'§[a-zA-Z0-9!]', orig))
    trans_colors = set(re.findall(r'§[a-zA-Z0-9!]', trans))
    if orig_colors != trans_colors:
        print(f"Color mismatch in {k}:")
        print(f"  Orig colors: {orig_colors}")
        print(f"  Trans colors: {trans_colors}")
        mismatches += 1

    # Check that literal \n are not real newlines
    if '\n' in trans or '\r' in trans:
        print(f"Real newline in translation {k}!")
        mismatches += 1

if mismatches == 0:
    print("PERFECT: All variables, bracketed tags, color codes, and literal escapes match 100%!")
else:
    print(f"Found {mismatches} mismatches.")
