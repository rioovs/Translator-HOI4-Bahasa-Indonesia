# -*- coding: utf-8 -*-
import re

def parse_file(path):
    with open(path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        lines = f.readlines()
    entries = []
    unparsed = []
    for idx, line in enumerate(lines[1:], 2):
        sline = line.strip()
        if not sline or sline.startswith('#'):
            continue
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"(?:\s*#.*)?$', line.strip())
        if m:
            key, ver, val = m.groups()
            entries.append((key, ver, val, line))
        else:
            unparsed.append((idx, line))
    print(f'{path}: total lines={len(lines)}, parsed={len(entries)}, unparsed={len(unparsed)}')
    for idx, l in unparsed:
        print(f'  L{idx}: {repr(l)}')
    return entries

wtt = parse_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml')
mtg = parse_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml')
