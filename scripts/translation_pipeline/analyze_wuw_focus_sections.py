# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    lines = f.readlines()

current_sec = 'HEADER'
sec_counts = {}

for line in lines:
    stripped = line.strip()
    if stripped.startswith('###'):
        current_sec = stripped
        if current_sec not in sec_counts:
            sec_counts[current_sec] = {'total': 0, 'titles': 0, 'descs': 0, 'tt': 0, 'other': 0}
        continue
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', line)
    if m:
        k = m.group(1)
        if current_sec not in sec_counts:
            sec_counts[current_sec] = {'total': 0, 'titles': 0, 'descs': 0, 'tt': 0, 'other': 0}
        sec_counts[current_sec]['total'] += 1
        if k.endswith('_desc'):
            sec_counts[current_sec]['descs'] += 1
        elif k.endswith('_tt'):
            sec_counts[current_sec]['tt'] += 1
        else:
            sec_counts[current_sec]['titles'] += 1

print("Section analysis:")
grand_total = 0
for sec, data in sec_counts.items():
    print(f"  {sec}: {data}")
    grand_total += data['total']

print(f"\nGrand Total Keys: {grand_total}")
