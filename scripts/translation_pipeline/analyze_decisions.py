# -*- coding: utf-8 -*-
import re

def analyze(name, path):
    with open(path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        lines = f.readlines()
    entries = []
    unparsed = []
    for idx, line in enumerate(lines[1:], 2):
        sline = line.strip()
        if not sline or sline.startswith('#'):
            continue
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', line.strip())
        if m:
            key, ver, val = m.groups()
            entries.append((key, ver, val))
        else:
            unparsed.append((idx, line))
    print(f'{name}: {len(lines)} lines, {len(entries)} parsed entries, {len(unparsed)} unparsed lines')
    if unparsed:
        print('Sample unparsed lines:')
        for idx, l in unparsed[:5]:
            print(f'  L{idx}: {repr(l)}')
    prefixes = {}
    for k, v, s in entries:
        pfx = k.split('_')[0]
        prefixes[pfx] = prefixes.get(pfx, 0) + 1
    print('Prefix counts:', sorted(prefixes.items(), key=lambda x: -x[1])[:10])

analyze('wtt', r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_decisions_l_english.yml')
analyze('mtg', r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml')
