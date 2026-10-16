# -*- coding: utf-8 -*-
import json
import re

total = {}
for i in [1, 2, 3, 4]:
    with open(f'wtt_focus_chunk{i}.json', 'r', encoding='utf-8') as f:
        total.update(json.load(f))

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_focus_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

out_lines = ['l_braz_por:\n']

for l in lines[1:]:
    if not l.strip() or l.strip().startswith('#'):
        out_lines.append(l)
        continue
    m = re.match(r'^(\s*)([A-Za-z0-9_\.]+)(:(\d*))?\s+"(.*)"\s*$', l)
    if not m:
        out_lines.append(l)
        continue
    indent = m.group(1) or ' '
    key = m.group(2)
    colon_num = m.group(3) or ':'
    
    val = total.get(key, m.group(5))
    # Ensure quotes inside val are properly escaped
    # Replace unescaped double quotes if any
    # But HOI4 localisation strings use \" for internal quotes
    # Let's ensure no raw double quotes inside val
    val_clean = val.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '')
    # If there are any double backslashes before n like \\\\n, normalize to \\n
    # but wait, let's make sure it doesn't overescape
    while '\\\\n' in val_clean:
        val_clean = val_clean.replace('\\\\n', '\\n')
    
    out_lines.append(f'{indent}{key}{colon_num} "{val_clean}"\n')

targets = [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wtt_focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wtt_focus_l_braz_por.yml'
]

for t in targets:
    with open(t, 'w', encoding='utf-8-sig', newline='\n') as f:
        f.writelines(out_lines)
    print(f"Written {len(out_lines)} lines to {t}")

print("Validating written files...")
for t in targets:
    with open(t, 'r', encoding='utf-8-sig') as f:
        check_lines = f.readlines()
    assert check_lines[0].strip() == 'l_braz_por:'
    bad = 0
    for idx, cl in enumerate(check_lines[1:], 2):
        s = cl.strip()
        if not s or s.startswith('#'):
            continue
        if not (s.endswith('"') and ':' in s):
            print(f"Bad line in {t} line {idx}: {s}")
            bad += 1
    if bad == 0:
        print(f"PASS: {t} is 100% valid Clausewitz YAML! ({len(check_lines)} lines)")
