import json
import re

def export_json(in_path, out_path):
    entries = []
    with open(in_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        for idx, line in enumerate(f, 1):
            raw = line.rstrip('\r\n')
            stripped = raw.strip()
            if not stripped or stripped.startswith('#') or stripped.startswith('l_english:'):
                continue
            m = re.match(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', raw)
            if m:
                indent, key, version, value = m.groups()
                entries.append({'key': key, 'ver': version, 'val': value})
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f'Exported {len(entries)} to {out_path}')

export_json(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\designer_l_english.yml', 'designer_en.json')
export_json(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\tank_modules_l_english.yml', 'tank_modules_en.json')
export_json(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\plane_designer_l_english.yml', 'plane_designer_en.json')
export_json(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\unit_l_english.yml', 'unit_en.json')
