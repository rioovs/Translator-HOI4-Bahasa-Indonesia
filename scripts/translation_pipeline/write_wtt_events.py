# -*- coding: utf-8 -*-
import json
import re

total = {}
for i in [1, 2, 3, 4]:
    with open(f'wtt_events_chunk{i}.json', 'r', encoding='utf-8') as f:
        total.update(json.load(f))
for i in [5, 6, 7]:
    with open(f'wtt_events_chunk{i}.json', 'r', encoding='utf-8') as f:
        for item in json.load(f):
            total[item['key']] = item['id']

print(f"Total merged keys: {len(total)}")

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_events_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

out_lines = ['l_braz_por:\n']

translated_count = 0

for l in lines[1:]:
    if not l.strip() or l.strip().startswith('#'):
        out_lines.append(l)
        continue
    m = re.match(r'^(\s*)([A-Za-z0-9_\.]+)(:(\d*))?\s+"(.*)"\s*$', l)
    if not m:
        out_lines.append(l)
        continue
    indent = m.group(1) or ' '
    key = m.group(2)
    colon_num = m.group(3) or ':'
    
    val = total.get(key, m.group(5))
    if key in total:
        translated_count += 1
    
    # Sanitize newlines
    val_clean = val.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '')
    while '\\\\n' in val_clean:
        val_clean = val_clean.replace('\\\\n', '\\n')
        
    # Replace internal double quotes with single quotes to ensure clean YAML parsing
    # First handle escaped quotes \" -> '
    val_clean = val_clean.replace('\\"', "'").replace('"', "'")
    
    out_lines.append(f'{indent}{key}{colon_num} "{val_clean}"\n')

print(f"Translated keys incorporated: {translated_count}/{len(total)}")

targets = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wtt_events_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wtt_events_l_braz_por.yml'
]

for t in targets:
    with open(t, 'w', encoding='utf-8-sig', newline='\n') as f:
        f.writelines(out_lines)
    print(f"Written {len(out_lines)} lines to {t}")

print("\n--- Validating written files ---")
for t in targets:
    # 1. Byte-level BOM check
    with open(t, 'rb') as bf:
        raw_bytes = bf.read(6)
    if raw_bytes[:3] == b'\xef\xbb\xbf':
        if raw_bytes[3:6] == b'\xef\xbb\xbf':
            print(f"ERROR: Double BOM detected in {t}")
        else:
            print(f"PASS: Single UTF-8 BOM confirmed in {t}")
    else:
        print(f"ERROR: Missing UTF-8 BOM in {t}")
        
    # 2. Line-level validation
    with open(t, 'r', encoding='utf-8-sig') as f:
        check_lines = f.readlines()
    assert check_lines[0].strip() == 'l_braz_por:', f"Invalid header: {check_lines[0]}"
    
    bad = 0
    key_count = 0
    for idx, cl in enumerate(check_lines[1:], 2):
        s = cl.strip()
        if not s or s.startswith('#'):
            continue
        # Check standard key pattern
        m_chk = re.match(r'^[A-Za-z0-9_\.]+(:\d*)?\s+".*"$', s)
        if not m_chk:
            print(f"Bad line in {t} line {idx}: {s}")
            bad += 1
        else:
            key_count += 1
            
    if bad == 0:
        print(f"PASS: {t} is 100% valid Clausewitz YAML! ({key_count} keys, {len(check_lines)} lines)")
    else:
        print(f"FAIL: {bad} bad lines found in {t}")
