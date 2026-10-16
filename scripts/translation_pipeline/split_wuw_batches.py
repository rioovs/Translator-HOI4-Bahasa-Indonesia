# -*- coding: utf-8 -*-
import os
import re
import json

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

with open(src_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    lines = f.readlines()

os.makedirs('scripts/wuw_batches', exist_ok=True)

pattern = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$')

current_section = 'UNKNOWN'
sections = []

current_batch_name = None
batches = {
    'batch1_ah_hun': [],     # Austro-Hungarian joint & Hungary
    'batch2_aus': [],        # Austria
    'batch3_bel': [],        # Belgium & tooltips
    'batch4_cog': [],        # Congo & tooltips
    'batch5_ger_part1': [],  # Germany Part 1
    'batch6_ger_part2': []   # Germany Part 2
}

ger_keys = []

for idx, line in enumerate(lines[1:], start=2):
    s = line.strip()
    if s.startswith('###'):
        current_section = s
        continue
    m = pattern.match(line)
    if not m:
        continue
    indent, key, ver, val, comment = m.groups()
    entry = {
        'idx': idx,
        'indent': indent,
        'key': key,
        'ver': ver,
        'val': val,
        'comment': comment or '',
        'section': current_section
    }
    
    if 'AUSTRO-HUNGARIAN' in current_section or 'HUNGARIAN' in current_section:
        batches['batch1_ah_hun'].append(entry)
    elif 'AUSTRIAN' in current_section:
        batches['batch2_aus'].append(entry)
    elif 'BELGI' in current_section:
        batches['batch3_bel'].append(entry)
    elif 'CONGO' in current_section:
        batches['batch4_cog'].append(entry)
    elif 'GERMAN' in current_section:
        ger_keys.append(entry)
    else:
        # Check prefix
        if key.startswith('GER_') or key.startswith('wuw_'):
            ger_keys.append(entry)
        elif key.startswith('BEL_'):
            batches['batch3_bel'].append(entry)
        elif key.startswith('AUS_'):
            batches['batch2_aus'].append(entry)
        elif key.startswith('HUN_') or key.startswith('HABSBURG_'):
            batches['batch1_ah_hun'].append(entry)
        elif key.startswith('COG_') or key.startswith('CONGO_'):
            batches['batch4_cog'].append(entry)
        else:
            ger_keys.append(entry)

# Split German tree into 2 roughly equal halves
half = len(ger_keys) // 2
batches['batch5_ger_part1'] = ger_keys[:half]
batches['batch6_ger_part2'] = ger_keys[half:]

for b_name, b_items in batches.items():
    print(f"{b_name}: {len(b_items)} entries")
    with open(f'scripts/wuw_batches/{b_name}.json', 'w', encoding='utf-8') as f:
        json.dump(b_items, f, ensure_ascii=False, indent=2)

total_batched = sum(len(b) for b in batches.values())
print(f"Total entries batched: {total_batched} (Source has 3071)")
