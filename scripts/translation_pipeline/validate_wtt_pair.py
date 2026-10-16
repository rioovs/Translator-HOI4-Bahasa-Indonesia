# -*- coding: utf-8 -*-
import os
import re

pairs = [
    ("wtt_focus_l_braz_por.yml", 747, 748),
    ("wtt_events_l_braz_por.yml", 1118, 1142)
]

dirs = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por'
]

print("=== FINAL COMPREHENSIVE VALIDATION ===")
all_pass = True

for fname, expected_keys, expected_lines in pairs:
    for d in dirs:
        fpath = os.path.join(d, fname)
        if not os.path.exists(fpath):
            print(f"FAIL: File does not exist: {fpath}")
            all_pass = False
            continue
            
        # 1. Check BOM
        with open(fpath, 'rb') as f:
            b = f.read(6)
        if b[:3] != b'\xef\xbb\xbf' or b[3:6] == b'\xef\xbb\xbf':
            print(f"FAIL: BOM issue in {fpath} (bytes: {b})")
            all_pass = False
            continue
            
        # 2. Check lines
        with open(fpath, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            
        if lines[0].strip() != 'l_braz_por:':
            print(f"FAIL: Header in {fpath} is '{lines[0].strip()}' (expected 'l_braz_por:')")
            all_pass = False
            continue
            
        keys_found = 0
        bad_lines = []
        for idx, l in enumerate(lines[1:], 2):
            s = l.strip()
            if not s or s.startswith('#'):
                continue
            m = re.match(r'^[A-Za-z0-9_\.]+(:\d*)?\s+".*"$', s)
            if not m:
                bad_lines.append((idx, s))
            else:
                keys_found += 1
                
        if bad_lines:
            print(f"FAIL: {len(bad_lines)} bad lines in {fpath}: {bad_lines[:3]}")
            all_pass = False
        elif keys_found != expected_keys:
            print(f"FAIL: Found {keys_found} keys in {fpath}, expected {expected_keys}")
            all_pass = False
        else:
            print(f"PASS: {fpath}")
            print(f"      Header: l_braz_por:, Single UTF-8 BOM, Keys: {keys_found}/{expected_keys}, Lines: {len(lines)}")

if all_pass:
    print("\n>>> ALL WTT DLC LOCALIZATION FILES 100% VALIDATED AND PASSING! <<<")
else:
    print("\n>>> VALIDATION FAILED! Check errors above. <<<")
