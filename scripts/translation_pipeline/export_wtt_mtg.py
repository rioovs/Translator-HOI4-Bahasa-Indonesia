# -*- coding: utf-8 -*-
import json
import re

def export_entries(in_path, out_path):
    entries = []
    with open(in_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines[1:], 2):
        sline = line.strip()
        if not sline or sline.startswith('#'):
            continue
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"(?:\s*#.*)?$', line.strip())
        if m:
            key, ver, val = m.groups()
            entries.append({'key': key, 'ver': ver, 'val': val})
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f'Exported {len(entries)} from {in_path} to {out_path}')

export_entries(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml', 'wtt_en.json')
export_entries(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml', 'mtg_en.json')
