# -*- coding: utf-8 -*-
import os
import json
import re

files_to_build = [
    {
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\decisions_l_english.yml",
        "trans_json": "scripts/decisions_translated.json",
        "dst_game": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\decisions_l_braz_por.yml",
        "dst_local": r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\decisions_l_braz_por.yml"
    },
    {
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\operatives_l_english.yml",
        "trans_json": "scripts/operatives_translated.json",
        "dst_game": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\operatives_l_braz_por.yml",
        "dst_local": r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\operatives_l_braz_por.yml"
    },
    {
        "src": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\lar_operations_l_english.yml",
        "trans_json": "scripts/lar_operations_translated.json",
        "dst_game": r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\lar_operations_l_braz_por.yml",
        "dst_local": r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\lar_operations_l_braz_por.yml"
    }
]

for item in files_to_build:
    src_path = item["src"]
    trans_json = item["trans_json"]
    dst_game = item["dst_game"]
    dst_local = item["dst_local"]

    with open(trans_json, 'r', encoding='utf-8') as f:
        trans_list = json.load(f)
    trans_map = {entry['key']: entry['val'] for entry in trans_list}

    with open(src_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    out_lines = ['\ufeffl_braz_por:\n']
    matched_keys = set()

    for idx, line in enumerate(lines[1:], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            out_lines.append(line)
            continue

        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', line.rstrip('\r\n'))
        if not m:
            out_lines.append(line)
            continue

        indent, key, version, val, comment = m.groups()
        ver_str = f":{version} " if version else ": "
        comment_str = f" {comment}" if comment else ""

        if key in trans_map:
            new_val = trans_map[key]
            matched_keys.add(key)
        else:
            print(f"WARNING: Key {key} not found in translation map for {src_path}!")
            new_val = val

        # Clean value: ensure literal \n is preserved and unescaped double quotes inside are escaped
        # but already escaped quotes \" are kept
        clean_val = new_val.replace('\r', '')
        # Escape quotes if unescaped
        # Replace non-escaped " with \"
        parts = clean_val.split('\\"')
        parts = [p.replace('"', '\\"') for p in parts]
        clean_val = '\\"'.join(parts)
        # Ensure newlines in string are literal \n
        clean_val = clean_val.replace('\n', '\\n')

        out_lines.append(f"{indent}{key}{ver_str}\"{clean_val}\"{comment_str}\n")

    content = ''.join(out_lines)
    # Ensure UTF-8 with BOM
    content_bytes = content.encode('utf-8')
    if not content_bytes.startswith(b'\xef\xbb\xbf'):
        content_bytes = b'\xef\xbb\xbf' + content_bytes

    # Write to game folder
    os.makedirs(os.path.dirname(dst_game), exist_ok=True)
    with open(dst_game, 'wb') as f:
        f.write(content_bytes)

    # Write to local repo folder
    os.makedirs(os.path.dirname(dst_local), exist_ok=True)
    with open(dst_local, 'wb') as f:
        f.write(content_bytes)

    print(f"Successfully generated {os.path.basename(dst_game)}: {len(matched_keys)} / {len(trans_map)} keys, {len(content_bytes)} bytes")
