# -*- coding: utf-8 -*-
import os
import re

files = [
    {
        "name": "decisions_l_braz_por.yml",
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\decisions_l_english.yml",
        "targets": [
            r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\decisions_l_braz_por.yml",
            r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\decisions_l_braz_por.yml"
        ]
    },
    {
        "name": "operatives_l_braz_por.yml",
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\operatives_l_english.yml",
        "targets": [
            r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\operatives_l_braz_por.yml",
            r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\operatives_l_braz_por.yml"
        ]
    },
    {
        "name": "lar_operations_l_braz_por.yml",
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\lar_operations_l_english.yml",
        "targets": [
            r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\lar_operations_l_braz_por.yml",
            r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\lar_operations_l_braz_por.yml"
        ]
    }
]

total_errors = 0

for f_info in files:
    name = f_info["name"]
    src_path = f_info["src"]
    print(f"\n==================== VALIDATING {name} ====================")

    # Parse source keys and tokens
    src_keys = {}
    with open(src_path, 'r', encoding='utf-8-sig') as f:
        for idx, line in enumerate(f, start=1):
            m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.rstrip('\r\n'))
            if m:
                k, ver, val, _ = m.groups()
                # find vars like $VAR$
                vars_in_val = set(re.findall(r'\$[A-Za-z0-9_|\.\+\-\%]+\$', val))
                # find script tags like [...]
                tags_in_val = set(re.findall(r'\[[A-Za-z0-9_\.\?\:]+\]', val))
                src_keys[k] = {
                    'val': val,
                    'vars': vars_in_val,
                    'tags': tags_in_val
                }

    print(f"Source file: {len(src_keys)} keys found.")

    for target in f_info["targets"]:
        print(f"--- Checking target: {target} ---")
        if not os.path.exists(target):
            print(f"  [ERROR] File does not exist!")
            total_errors += 1
            continue

        with open(target, 'rb') as f:
            raw = f.read()

        if not raw.startswith(b'\xef\xbb\xbf'):
            print(f"  [ERROR] Missing UTF-8 BOM!")
            total_errors += 1
        else:
            print(f"  [OK] UTF-8 BOM present ({len(raw)} bytes).")

        text = raw.decode('utf-8-sig')
        lines = text.splitlines()

        if not lines:
            print(f"  [ERROR] Empty file!")
            total_errors += 1
            continue

        if lines[0] != 'l_braz_por:':
            print(f"  [ERROR] First line is '{lines[0]}', expected 'l_braz_por:'")
            total_errors += 1
        else:
            print(f"  [OK] Header is 'l_braz_por:'")

        target_keys = {}
        for idx, line in enumerate(lines[1:], start=2):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line)
            if not m:
                print(f"  [ERROR] Line {idx} failed regex: {line}")
                total_errors += 1
                continue
            k, ver, val, _ = m.groups()
            target_keys[k] = val

            # Check unescaped quotes inside val
            # A quote that is not preceded by \
            unescaped_quotes = re.findall(r'(?<!\\)"', val)
            if unescaped_quotes:
                print(f"  [ERROR] Unescaped quote in line {idx} ({k}): {val}")
                total_errors += 1

            # Check color tag balance
            color_open = len(re.findall(r'§[A-Za-z0-9!]', val))
            color_close = len(re.findall(r'§!', val))
            # open includes §! as well, so total openers is color_open - color_close
            openers_only = len(re.findall(r'§[A-Za-z0-9](?!§)', val))
            closers_only = len(re.findall(r'§!', val))
            # Note: in some Paradox files, color tag can end without §! or be closed on next line, but within single line usually balanced
            # Let's check variables against source
            if k in src_keys:
                src_vars = src_keys[k]['vars']
                tgt_vars = set(re.findall(r'\$[A-Za-z0-9_|\.\+\-\%]+\$', val))
                if src_vars != tgt_vars:
                    # In case variable was translated or corrupted
                    print(f"  [WARNING] Variable mismatch in {k}: src={src_vars}, tgt={tgt_vars}")

                src_tags = src_keys[k]['tags']
                tgt_tags = set(re.findall(r'\[[A-Za-z0-9_\.\?\:]+\]', val))
                if src_tags != tgt_tags:
                    print(f"  [WARNING] Script tag mismatch in {k}: src={src_tags}, tgt={tgt_tags}")

        if len(target_keys) != len(src_keys):
            print(f"  [ERROR] Key count mismatch: target has {len(target_keys)}, source has {len(src_keys)}")
            total_errors += 1
        else:
            print(f"  [OK] Key count perfectly matches ({len(target_keys)} keys).")

print(f"\n==================== VALIDATION RESULT ====================")
if total_errors == 0:
    print("ALL CHECKS PASSED PERFECTLY WITH 0 ERRORS!")
else:
    print(f"TOTAL ERRORS FOUND: {total_errors}")
