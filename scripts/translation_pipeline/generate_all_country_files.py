# -*- coding: utf-8 -*-
import os
import re
import json

with open('scripts/master_roots_lookup.json', 'r', encoding='utf-8') as f:
    master_dict = json.load(f)

def translate_value(val):
    if not val:
        return ""
    v = val.strip()
    # Check if purely a variable like $RSI$, $INS_HOL$, etc.
    if re.match(r'^\$[A-Za-z0-9_.-]+\$$', v):
        return val
    # Direct match in master_dict
    if v in master_dict:
        res = master_dict[v]
        if val.endswith(' '):
            res += ' '
        return res
    # Definite article "the " or "The "
    if v.startswith('the ') or v.startswith('The '):
        sub = re.sub(r'^[tT]he\s+', '', v)
        if sub in master_dict:
            res = master_dict[sub]
            if val.endswith(' '):
                res += ' '
            return res
    # Fallback to val
    print(f"WARNING: Unmatched value: {val}")
    return val

line_pat = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$')

def process_file(src_path, dst_paths):
    out_lines = []
    with open(src_path, 'r', encoding='utf-8-sig') as f:
        for idx, line in enumerate(f):
            # Header line
            if idx == 0 and line.strip().startswith('l_english:'):
                out_lines.append('l_braz_por:\n')
                continue
            
            m = line_pat.match(line)
            if m:
                indent, key, ver, val, comment = m.groups()
                tr_val = translate_value(val)
                # Escape any internal unescaped quotes if needed, but keep valid escapes
                # Notice in HOI4 localisation strings are enclosed in quotes ""
                # Replace backslashes/newlines properly
                cmt = comment if comment else ""
                ver_str = f":{ver}" if ver != "" else ":"
                out_line = f'{indent}{key}{ver_str} "{tr_val}"{cmt}\n'
                out_lines.append(out_line)
            else:
                out_lines.append(line)

    for dst in dst_paths:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8-sig', newline='\n') as f:
            f.writelines(out_lines)
        print(f"Wrote {len(out_lines)} lines to {dst}")

# 1. Countries
src_countries = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_l_english.yml"
dst_countries = [
    r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\countries_l_braz_por.yml",
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\countries_l_braz_por.yml"
]
print("Processing countries_l_english.yml...")
process_file(src_countries, dst_countries)

# 2. Countries Cosmetic
src_cosmetic = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\countries_cosmetic_l_english.yml"
dst_cosmetic = [
    r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\countries_cosmetic_l_braz_por.yml",
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\countries_cosmetic_l_braz_por.yml"
]
print("Processing countries_cosmetic_l_english.yml...")
process_file(src_cosmetic, dst_cosmetic)

print("All translations generated successfully!")
