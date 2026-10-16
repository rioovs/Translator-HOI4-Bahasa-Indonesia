# -*- coding: utf-8 -*-
import os
import re

files_to_check = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\ship_modules_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\ship_modules_l_braz_por.yml'
]

def validate_file(filepath):
    print(f"\n==========================================")
    print(f"Validating: {filepath}")
    
    # 1. Check BOM
    with open(filepath, 'rb') as f:
        raw_bytes = f.read(3)
        if raw_bytes != b'\xef\xbb\xbf':
            print("❌ ERROR: Missing UTF-8 BOM!")
            return False
        else:
            print("✅ UTF-8 BOM detected (0xEF 0xBB 0xBF)")

    # 2. Read lines with utf-8-sig
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")
    if lines[0].strip() != 'l_braz_por:':
        print(f"❌ ERROR: Header is not 'l_braz_por:', got '{lines[0].strip()}'")
        return False
    else:
        print("✅ Header is 'l_braz_por:'")

    errors = 0
    key_count = 0

    for idx, line in enumerate(lines[1:], 2):
        s = line.strip()
        if not s or s.startswith('#'):
            continue

        # Regex for Clausewitz key-value line
        # Match indent, key, version, value, optional comment
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
        if not m:
            print(f"❌ Line {idx}: Invalid syntax: {line}")
            errors += 1
            if errors > 10:
                print("Too many errors, aborting line checks.")
                break
            continue

        key_count += 1
        indent, key, version, val, comment = m.groups()

        # Check quotes inside val: must be preceded by \
        # If there's an unescaped double quote:
        # Regex for unescaped quote: (?<!\\)"
        unescaped = re.findall(r'(?<!\\)"', val)
        if unescaped:
            print(f"❌ Line {idx} ({key}): Unescaped internal double quote in value: {val}")
            errors += 1

        # Check color tags: count §X vs §!
        color_open = len(re.findall(r'§[A-Z0-9]', val))
        color_close = len(re.findall(r'§!', val))
        if color_open != color_close:
            print(f"❌ Line {idx} ({key}): Unbalanced color tags: open={color_open}, close={color_close} in: {val}")
            errors += 1

        # Check bracket tags: count [ vs ]
        bracket_open = val.count('[')
        bracket_close = val.count(']')
        if bracket_open != bracket_close:
            print(f"❌ Line {idx} ({key}): Unbalanced brackets: {bracket_open} vs {bracket_close} in: {val}")
            errors += 1

        # Check variable placeholders: count $
        dollar_count = val.count('$')
        if dollar_count % 2 != 0:
            print(f"❌ Line {idx} ({key}): Odd number of $ (unclosed variable placeholder): {val}")
            errors += 1

    print(f"Total keys checked: {key_count}")
    if errors == 0:
        print(f"✅ PERFECT: 0 errors found in {os.path.basename(filepath)}!")
        return True
    else:
        print(f"❌ FAILED: {errors} errors found in {os.path.basename(filepath)}!")
        return False

all_ok = True
for f in files_to_check:
    if not validate_file(f):
        all_ok = False

if all_ok:
    print("\n🎉 ALL TARGET FILES FULLY VALIDATED AND READY!")
else:
    print("\n❌ VALIDATION FAILED ON ONE OR MORE FILES.")
