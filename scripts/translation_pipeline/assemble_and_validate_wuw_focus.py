# -*- coding: utf-8 -*-
import os
import re
import json

src_file = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

targets = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wuw_focus_l_braz_por.yml',
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\WUW_focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wuw_focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\WUW_focus_l_braz_por.yml',
]

# Load all 6 batch files
all_trans = {}
batch_files = [
    'scripts/wuw_batches/batch1_ah_hun_translated.json',
    'scripts/wuw_batches/batch2_aus_translated.json',
    'scripts/wuw_batches/batch3_bel_translated.json',
    'scripts/wuw_batches/batch4_cog_translated.json',
    'scripts/wuw_batches/batch5_ger_part1_translated.json',
    'scripts/wuw_batches/batch6_ger_part2_translated.json',
]

for bf in batch_files:
    with open(bf, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_trans.update(data)
        print(f"Loaded {bf}: {len(data)} items")

print(f"\nTotal compiled translation keys: {len(all_trans)}")

# Read source file
with open(src_file, 'r', encoding='utf-8-sig', errors='replace') as f:
    src_lines = f.readlines()

print(f"Total lines in source: {len(src_lines)}")

pattern = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$')

out_lines = ['\ufeffl_braz_por:\n']
matched_keys = 0
missing_keys = []
replaced_keys = 0

for idx, line in enumerate(src_lines[1:], start=2):
    stripped = line.strip()
    if not stripped or stripped.startswith('#'):
        out_lines.append(line)
        continue
        
    m = pattern.match(line)
    if not m:
        out_lines.append(line)
        continue
        
    indent, key, ver, orig_val, comment = m.groups()
    ver_str = f":{ver} " if ver else ": "
    comment_str = comment if comment else ""
    matched_keys += 1
    
    if key in all_trans:
        new_val = all_trans[key]
        replaced_keys += 1
    else:
        missing_keys.append((idx, key, orig_val))
        new_val = orig_val
        
    # Validation & clean-up on new_val:
    # 1. No physical newlines
    new_val = new_val.replace('\r\n', '\\n').replace('\r', '\\n').replace('\n', '\\n')
    # 2. Internal quotes must be escaped
    # Avoid double escaping \\" -> \\"
    new_val = new_val.replace('“', '\\"').replace('”', '\\"')
    new_val = re.sub(r'(?<!\\)"', r'\"', new_val)
    
    out_lines.append(f"{indent}{key}{ver_str}\"{new_val}\"{comment_str}\n")

print(f"Total matched keys in source: {matched_keys}")
print(f"Replaced keys: {replaced_keys}")
print(f"Missing keys: {len(missing_keys)}")
if missing_keys:
    for mk in missing_keys[:10]:
        print(f"  Missing: {mk}")

final_content = ''.join(out_lines)

# Write to all targets
for target_path in targets:
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    # Check BOM and size
    size = os.path.getsize(target_path)
    with open(target_path, 'rb') as fb:
        bom = fb.read(3)
    has_bom = bom == b'\xef\xbb\xbf'
    print(f"Wrote {target_path}: {size} bytes, UTF-8 BOM: {has_bom}")
