# -*- coding: utf-8 -*-
import os

with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\focus_l_english.yml', 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    bp_lines = f.readlines()

clean_bp_lines = []
bp_idx = 0
for eng_idx, eline in enumerate(eng_lines):
    while bp_idx < len(bp_lines) and bp_lines[bp_idx].strip() == '' and eline.strip() != '':
        bp_idx += 1
    if bp_idx < len(bp_lines):
        clean_bp_lines.append(bp_lines[bp_idx])
        bp_idx += 1

assert len(clean_bp_lines) == len(eng_lines) == 2583, f"Expected 2583 lines, got {len(clean_bp_lines)}"

dest_paths = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
]

for p in dest_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8-sig', newline='\n') as out:
        out.writelines(clean_bp_lines)
    print(f"Saved {len(clean_bp_lines)} lines with UTF-8 BOM to {p}")

print("Finalization complete!")
