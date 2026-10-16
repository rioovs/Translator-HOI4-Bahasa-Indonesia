# -*- coding: utf-8 -*-
"""
Comprehensive validation script for all 4 HOI4 translated localisation files.
"""
import os
import re
import sys

FILES = [
    {
        'name': 'designer',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\designer_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\designer_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\designer_l_braz_por.yml'
        ]
    },
    {
        'name': 'tank_modules',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\tank_modules_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\tank_modules_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\tank_modules_l_braz_por.yml'
        ]
    },
    {
        'name': 'plane_designer',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\plane_designer_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\plane_designer_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\plane_designer_l_braz_por.yml'
        ]
    },
    {
        'name': 'unit',
        'src': r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\unit_l_english.yml',
        'dsts': [
            r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\unit_l_braz_por.yml',
            r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\unit_l_braz_por.yml'
        ]
    }
]

def validate_file(src_path, dst_path):
    rel_name = os.path.basename(dst_path)
    print(f'Checking {dst_path}...')

    # 1. Existence
    if not os.path.exists(dst_path):
        print(f'  [FAIL] File does not exist: {dst_path}')
        return False, 0

    # 2. UTF-8 BOM
    with open(dst_path, 'rb') as fp:
        bom = fp.read(3)
        if bom != b'\xef\xbb\xbf':
            print(f'  [FAIL] Missing UTF-8 BOM in {dst_path}')
            return False, 0

    # 3. Read lines
    with open(src_path, 'r', encoding='utf-8-sig', errors='ignore') as fp:
        src_lines = fp.readlines()
    with open(dst_path, 'r', encoding='utf-8-sig', errors='ignore') as fp:
        dst_lines = fp.readlines()

    # 4. Header
    if not dst_lines or dst_lines[0].strip() != 'l_braz_por:':
        print(f'  [FAIL] Invalid header in {dst_path}, expected l_braz_por:')
        return False, 0

    # Parse src
    src_map = {}
    for line in src_lines[1:]:
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', line.strip())
        if m:
            key, ver, val = m.groups()
            src_map[key] = val

    errors = []
    dst_keys = set()
    for idx, line in enumerate(dst_lines[1:], 2):
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', line.strip())
        if m:
            key, ver, val = m.groups()
            dst_keys.add(key)
            if key not in src_map:
                errors.append(f'L{idx}: Key {key} not found in source')
                continue
            src_val = src_map[key]

            # Check variables $...$
            src_vars = sorted(re.findall(r'\$[a-zA-Z0-9_|^%0-9+~.-]+\$', src_val))
            dst_vars = sorted(re.findall(r'\$[a-zA-Z0-9_|^%0-9+~.-]+\$', val))
            if src_vars != dst_vars:
                errors.append(f'L{idx} ({key}): Var mismatch: src={src_vars} vs dst={dst_vars}')

            # Check icons £...
            src_icons = sorted(re.findall(r'£[a-zA-Z0-9_]+', src_val))
            dst_icons = sorted(re.findall(r'£[a-zA-Z0-9_]+', val))
            if src_icons != dst_icons:
                errors.append(f'L{idx} ({key}): Icon mismatch: src={src_icons} vs dst={dst_icons}')

            # Check color tags count
            src_colors = re.findall(r'§[a-zA-Z0-9!+-]', src_val)
            dst_colors = re.findall(r'§[a-zA-Z0-9!+-]', val)
            if len(src_colors) != len(dst_colors):
                errors.append(f'L{idx} ({key}): Color mismatch: src={src_colors} vs dst={dst_colors}')

    missing_keys = set(src_map.keys()) - dst_keys
    if missing_keys:
        errors.append(f'Missing keys ({len(missing_keys)}): {list(missing_keys)[:5]}')

    if errors:
        print(f'  [FAIL] {len(errors)} issues:')
        for e in errors[:5]:
            print('   ', e)
        return False, len(dst_keys)

    print(f'  [PASS] {len(dst_keys)} keys validated successfully.')
    return True, len(dst_keys)

def main():
    total_valid = 0
    all_ok = True
    print('========================================')
    print('HOI4 INDONESIAN TRANSLATION VALIDATION')
    print('========================================')
    for item in FILES:
        print(f"\n--- Checking {item['name']} (Source: {os.path.basename(item['src'])}) ---")
        for dst in item['dsts']:
            ok, cnt = validate_file(item['src'], dst)
            if not ok:
                all_ok = False
            else:
                total_valid += cnt

    print('\n========================================')
    if all_ok:
        print(f'ALL VALIDATION CHECKS PASSED!')
        print(f'Total key-value pairs validated across all targets: {total_valid // 2} (x2 destinations = {total_valid})')
    else:
        print('SOME VALIDATION CHECKS FAILED!')
        sys.exit(1)

if __name__ == '__main__':
    main()
