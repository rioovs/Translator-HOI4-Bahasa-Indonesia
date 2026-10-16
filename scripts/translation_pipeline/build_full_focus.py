# -*- coding: utf-8 -*-
import json
import re

# Load all 6 parts
all_trans = {}

for p in range(1, 7):
    # Read the JS file which has module.exports = { ... };
    with open(f'scripts/focus_part{p}.js', 'r', encoding='utf-8') as f:
        content = f.read()
        # Extract JSON part
        m = re.search(r'module\.exports\s*=\s*(\{[\s\S]*\});?\s*$', content)
        if m:
            data = json.loads(m.group(1))
            all_trans.update(data)
            print(f"Loaded Part {p}: {len(data)} items")
        else:
            print(f"Error parsing Part {p}")

print(f"Total compiled translation keys: {len(all_trans)}")

# Read source English file
src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/focus_l_english.yml'
dst_game = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/focus_l_braz_por.yml'
dst_local = 'f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/focus_l_braz_por.yml'

with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

out_lines = ['\ufeffl_braz_por:\n']

replaced = 0
preserved = 0

for i in range(1, len(lines)):
    line = lines[i]
    stripped = line.strip()
    
    if not stripped or stripped.startswith('#'):
        out_lines.append(line)
        continue
        
    m = re.match(r'^(\s*)([A-Za-z0-9_-]+):(\d*)\s*"(.*)"\s*$', line)
    if not m:
        out_lines.append(line)
        continue
        
    indent, key, version, val = m.groups()
    ver_str = f":{version} " if version else ": "
    
    if key in all_trans:
        new_val = all_trans[key]
        replaced += 1
    elif re.match(r'^\$[A-Za-z0-9_]+\$$', val.strip()):
        new_val = val
        preserved += 1
    else:
        new_val = val
        preserved += 1
        
    # Escape inner quotes safely
    clean_val = new_val.replace('"', '\\"') if ('"' in new_val and '\\"' not in new_val) else new_val
    out_lines.append(f"{indent}{key}{ver_str}\"{clean_val}\"\n")

content = ''.join(out_lines)

# Write to both destinations
with open(dst_game, 'w', encoding='utf-8') as f:
    f.write(content)
with open(dst_local, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated focus_l_braz_por.yml!")
print(f"Total lines: {len(out_lines)} (Source had {len(lines)})")
print(f"Replaced keys: {replaced}, Preserved/vars: {preserved}")
