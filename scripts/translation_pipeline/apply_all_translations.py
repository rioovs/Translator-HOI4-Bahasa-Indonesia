# -*- coding: utf-8 -*-
import os
import re

from trans_batch1_can_misc import translations_batch1
from trans_batch2_saf import translations_batch2
from trans_batch3_nzl import translations_batch3
from trans_batch4_raj import translations_batch4
from trans_batch5_usa import translations_batch5

all_trans = {}
for b in [translations_batch1, translations_batch2, translations_batch3, translations_batch4, translations_batch5]:
    all_trans.update(b)

src_path = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
dest_paths = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
]

with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

replaced_keys = set()
new_lines = []

for idx, line in enumerate(lines):
    # Pattern to match key:number? "value"
    # Example: ' USA_continue_the_new_deal_desc: 1 "..."\n'
    # Example: ' CAN_support_the_world_revolution_desc: "..."\n'
    m = re.match(r'^(\s*[a-zA-Z0-9_]+:\s*(?:[0-9]+\s*)?\")(.*)(\"\s*(?:#.*)?)$', line)
    if m:
        prefix = m.group(1)
        old_val = m.group(2)
        suffix = m.group(3)
        # Extract the key name
        key = prefix.strip().split(':')[0].strip()
        if key in all_trans:
            trans_val = all_trans[key]
            # Escape unescaped double quotes in trans_val
            # Replace literal quotes with \" unless preceded by backslash
            escaped_val = re.sub(r'(?<!\\)"', r'\"', trans_val)
            new_line = f"{prefix}{escaped_val}{suffix}\n"
            new_lines.append(new_line)
            replaced_keys.add(key)
            continue

    new_lines.append(line)

print(f"Total lines: {len(new_lines)}")
print(f"Total keys replaced: {len(replaced_keys)} / {len(all_trans)}")

missing_replacements = set(all_trans.keys()) - replaced_keys
if missing_replacements:
    print(f"ERROR: {len(missing_replacements)} keys were not replaced:")
    for k in missing_replacements:
        print(f"  {k}")
    exit(1)

# Write to both target paths with UTF-8 with BOM
for p in dest_paths:
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8-sig') as out:
        out.writelines(new_lines)
    print(f"Successfully saved UTF-8-sig to: {p}")

print("All replacements applied successfully!")
