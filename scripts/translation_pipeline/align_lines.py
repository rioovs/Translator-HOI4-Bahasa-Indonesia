# -*- coding: utf-8 -*-
import re

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

# Currently focus_l_braz_por.yml has 2918 lines because 335 blank lines were added after each translated desc.
# Let's filter out empty lines that were not empty in eng_lines!

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    bp_lines = f.readlines()

print(f"Eng lines: {len(eng_lines)}, BP lines: {len(bp_lines)}")

# Let's inspect where empty lines are in bp_lines vs eng_lines
clean_bp_lines = []
bp_idx = 0
for eng_idx, eline in enumerate(eng_lines):
    # Skip any extra empty line in bp_lines if eline is not empty
    while bp_idx < len(bp_lines) and bp_lines[bp_idx].strip() == '' and eline.strip() != '':
        bp_idx += 1
    if bp_idx < len(bp_lines):
        clean_bp_lines.append(bp_lines[bp_idx])
        bp_idx += 1

print(f"Clean BP lines: {len(clean_bp_lines)}")

# Check key match between clean_bp_lines and eng_lines
mismatches = 0
for i in range(1, len(eng_lines)):
    ekey = eng_lines[i].split(':')[0].strip()
    bkey = clean_bp_lines[i].split(':')[0].strip()
    if ekey != bkey:
        print(f"Line {i+1} mismatch: Eng='{ekey}' vs BP='{bkey}'")
        mismatches += 1
        if mismatches > 10:
            break

if mismatches == 0:
    print("ALL 2583 KEYS MATCH 100% PERFECTLY!")
