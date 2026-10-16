# -*- coding: utf-8 -*-
"""
Validation script for MTG and WTT decisions localisation files.
"""
import os
import re
from validate_all import validate_file

DECISION_FILES = [
    {
        'name': 'mtg_decisions',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\mtg_decisions_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\mtg_decisions_l_braz_por.yml'
        ]
    },
    {
        'name': 'wtt_decisions',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wtt_decisions_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wtt_decisions_l_braz_por.yml'
        ]
    }
]

def main():
    all_ok = True
    for item in DECISION_FILES:
        print(f"\n==================== {item['name']} ====================")
        for dst in item['dsts']:
            ok, count = validate_file(item['src'], dst)
            if not ok:
                all_ok = False
            else:
                print(f"  [PASS] {item['name']}: {count} keys validated successfully on {os.path.basename(dst)}")

    if all_ok:
        print("\nALL DECISION LOCALISATION FILES PASSED VALIDATION!")
    else:
        print("\nSOME LOCALISATION FILES FAILED VALIDATION!")
    return all_ok

if __name__ == '__main__':
    main()
