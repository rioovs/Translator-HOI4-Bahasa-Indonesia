# -*- coding: utf-8 -*-
import re

braz_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
eng_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'

with open(braz_path, 'r', encoding='utf-8-sig') as f:
    braz_lines = f.readlines()
with open(eng_path, 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

eng_data = {re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l).group(1): re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l).group(3) for l in eng_lines if re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)}
braz_data = {re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l).group(1): re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l).group(3) for l in braz_lines if re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)}

mod_t = [(k, eng_data[k], braz_data[k]) for k in braz_data if (k.endswith('.t') or k.endswith('.title')) and eng_data.get(k) != braz_data[k]]
mod_d = [(k, eng_data[k], braz_data[k]) for k in braz_data if (k.endswith('.d') or k.endswith('.desc') or '.d.' in k or k.startswith('d_')) and eng_data.get(k) != braz_data[k]]

print(f"Modified titles: {len(mod_t)}")
for k, e, b in mod_t[:20]:
    print(f"[{k}]\n  ENG:  {e}\n  BRAZ: {b}")

print("\n" + "="*50 + "\n")
print(f"Modified descs: {len(mod_d)}")
for k, e, b in mod_d[:20]:
    print(f"[{k}]\n  ENG:  {e}\n  BRAZ: {b}")
