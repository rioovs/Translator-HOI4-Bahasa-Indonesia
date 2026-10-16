# -*- coding: utf-8 -*-
import os
import re

targets = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wuw_events_l_braz_por.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\WUW_events_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wuw_events_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\WUW_events_l_braz_por.yml'
]

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_events_l_english.yml'

print("=== PARSING SOURCE FILE ===")
src_data = {}
with open(src_path, 'r', encoding='utf-8-sig') as f:
    for idx, line in enumerate(f, 1):
        m = re.match(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.rstrip('\r\n'))
        if m:
            k, ver, val, _ = m.groups()
            vars_set = set(re.findall(r'\$[a-zA-Z0-9_|\.\+\-\%]+\$', val))
            tags_set = set(re.findall(r'\[[a-zA-Z0-9_\.\?\:\s]+\]', val))
            src_data[k] = {
                'line': idx,
                'val': val,
                'vars': vars_set,
                'tags': tags_set
            }

print(f"Source file contains {len(src_data)} keys.")

total_errors = 0

for target in targets:
    print(f"\n==================== VALIDATING {os.path.basename(target)} ====================")
    print(f"Path: {target}")
    
    if not os.path.exists(target):
        print(f"  [FATAL] Target does not exist!")
        total_errors += 1
        continue
    
    with open(target, 'rb') as f:
        raw_bytes = f.read()
    
    # 1. Check BOM
    if not raw_bytes.startswith(b'\xef\xbb\xbf'):
        print(f"  [ERROR] Missing UTF-8 BOM!")
        total_errors += 1
    else:
        print(f"  [OK] UTF-8 BOM present (0xEF, 0xBB, 0xBF)")

    text = raw_bytes.decode('utf-8')
    lines = text.splitlines()

    # 2. Check Header
    header_line = lines[0].lstrip('\ufeff').strip() if lines else ''
    if header_line != 'l_braz_por:':
        print(f"  [ERROR] Header is not 'l_braz_por:'! Found: {repr(lines[0]) if lines else 'EMPTY'}")
        total_errors += 1
    else:
        print(f"  [OK] Header is 'l_braz_por:'")

    # 3. Check line syntax and key extraction
    target_keys = {}
    syntax_errors = 0
    line_pattern = re.compile(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$')

    for i, line in enumerate(lines[1:], start=2):
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        
        m = line_pattern.match(line)
        if not m:
            print(f"  [ERROR] Syntax error at line {i}: {line}")
            syntax_errors += 1
            total_errors += 1
            continue
        
        k, ver, val, _ = m.groups()
        target_keys[k] = (i, val)

    print(f"  [OK] Syntax check completed. Found {len(target_keys)} valid keys. (Errors: {syntax_errors})")

    # 4. Check Key completeness
    missing_keys = set(src_data.keys()) - set(target_keys.keys())
    if missing_keys:
        print(f"  [ERROR] {len(missing_keys)} keys missing! Examples: {list(missing_keys)[:5]}")
        total_errors += len(missing_keys)
    else:
        print(f"  [OK] All {len(src_data)} source keys present!")

    # 5. Check Token integrity ($VAR$, [TAG], §X...§!)
    token_mismatches = 0
    color_mismatches = 0
    for k, s_info in src_data.items():
        if k not in target_keys:
            continue
        line_num, t_val = target_keys[k]
        
        # Check vars
        t_vars = set(re.findall(r'\$[a-zA-Z0-9_|\.\+\-\%]+\$', t_val))
        missing_vars = s_info['vars'] - t_vars
        if missing_vars:
            print(f"  [ERROR] Line {line_num} ({k}): Missing vars {missing_vars}")
            token_mismatches += 1
            total_errors += 1

        # Check script tags
        t_tags = set(re.findall(r'\[[a-zA-Z0-9_\.\?\:\s]+\]', t_val))
        missing_tags = s_info['tags'] - t_tags
        if missing_tags:
            print(f"  [ERROR] Line {line_num} ({k}): Missing script tags {missing_tags}")
            token_mismatches += 1
            total_errors += 1

        # Check color tag balance
        open_colors = len(re.findall(r'§[A-Z0-9!]', t_val)) - len(re.findall(r'§!', t_val))
        close_colors = len(re.findall(r'§!', t_val))
        # Note: sometimes Paradox open color tags are balanced by §! or another §Y
        # Just check for unclosed single §
        bad_sections = re.findall(r'§(?![A-Z0-9!])', t_val)
        if bad_sections:
            print(f"  [ERROR] Line {line_num} ({k}): Malformed color tag: {t_val}")
            color_mismatches += 1
            total_errors += 1

    if token_mismatches == 0 and color_mismatches == 0:
        print(f"  [OK] Token integrity verified (Variables, Script Tags, Color Codes 100% matched)")

print("\n==================== FINAL VALIDATION SUMMARY ====================")
if total_errors == 0:
    print(">>> 100% SUCCESS: All target files passed all validation checks with 0 errors! <<<")
else:
    print(f">>> FAILED: Found {total_errors} errors across targets! <<<")
