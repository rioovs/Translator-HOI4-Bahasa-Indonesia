import os
import re

files = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\decisions_l_english.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\operatives_l_english.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\lar_operations_l_english.yml'
]

for fpath in files:
    with open(fpath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    print(f'=== {os.path.basename(fpath)} === (Total lines: {len(lines)})')
    keys = []
    multiline_count = 0
    for idx, line in enumerate(lines[1:], start=2):
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.strip())
        if m:
            keys.append((m.group(1), m.group(2), m.group(3)))
        elif line.strip() and not line.strip().startswith('#'):
            multiline_count += 1
            # print odd lines
            print(f'Line {idx}: {line[:60]}...')
    print(f'Parsed keys: {len(keys)}, odd lines: {multiline_count}')
