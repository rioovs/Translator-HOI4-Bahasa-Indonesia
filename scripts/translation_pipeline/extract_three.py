import json
import re

def extract(path, out_json):
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    data = []
    for idx, line in enumerate(lines[1:], start=2):
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.rstrip('\r\n'))
        if m:
            indent, key, ver, val, comm = m.groups()
            data.append({
                'line_num': idx,
                'key': key,
                'ver': ver,
                'val': val,
                'comm': comm or ''
            })
        else:
            print(f'MISMATCH in {path} at line {idx}: {line}')
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'{path} -> {out_json}: {len(data)} items')

extract(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\decisions_l_english.yml', 'scripts/decisions.json')
extract(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\operatives_l_english.yml', 'scripts/operatives.json')
extract(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\lar_operations_l_english.yml', 'scripts/lar_operations.json')
