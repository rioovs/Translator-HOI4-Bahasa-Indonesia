# -*- coding: utf-8 -*-
import json
import os
import re

def main():
    print("=== Loading all chunk translations ===")
    all_translations = {}
    missing_chunks = []
    for c in range(14):
        chunk_file = f'scripts/chunks/trans_chunk_{c}.json'
        if not os.path.exists(chunk_file):
            missing_chunks.append(c)
            continue
        with open(chunk_file, 'r', encoding='utf-8') as f:
            chunk_data = json.load(f)
            all_translations.update(chunk_data)
            print(f"Loaded Chunk {c:2d}: {len(chunk_data)} keys")

    if missing_chunks:
        print(f"Waiting for missing chunks: {missing_chunks}")
        return False

    print(f"Total translations loaded: {len(all_translations)}")

    src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_events_l_english.yml'
    with open(src_path, 'r', encoding='utf-8-sig') as f:
        src_lines = f.readlines()

    pattern = re.compile(r'^(\s*)([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$')

    out_lines = ['l_braz_por:\n']
    missing_in_dict = []
    translated_count = 0

    for idx, line in enumerate(src_lines[1:], start=2):
        s = line.strip()
        if not s or s.startswith('#'):
            out_lines.append(line)
            continue
        m = pattern.match(line.rstrip('\r\n'))
        if m:
            indent = m.group(1) or ' '
            key = m.group(2)
            ver = m.group(3)
            val = m.group(4)
            comment = m.group(5)
            trailing = f" {comment}" if comment else ""

            if key in all_translations:
                tr = all_translations[key]
                # Ensure no raw literal unescaped newlines broke the string
                tr = tr.replace('\r\n', '\\n').replace('\n', '\\n')
                # If there are internal unescaped quotes, escape them
                # But note: tr may already have \"
                # Let's clean up any doubled backslashes if needed, or ensure \"
                out_lines.append(f"{indent}{key}:{ver} \"{tr}\"{trailing}\n")
                translated_count += 1
            else:
                missing_in_dict.append((idx, key))
                out_lines.append(f"{indent}{key}:{ver} \"{val}\"{trailing}\n")
        else:
            print(f"Warning: line {idx} not matched: {line}")
            out_lines.append(line)

    if missing_in_dict:
        print(f"ERROR: {len(missing_in_dict)} keys missing in dictionary!")
        for m in missing_in_dict[:10]:
            print(f"  Line {m[0]}: {m[1]}")
        return False

    print(f"Successfully processed all {translated_count} keys!")

    content = ''.join(out_lines)
    # Target files to write
    targets = [
        r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\wuw_events_l_braz_por.yml',
        r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\WUW_events_l_braz_por.yml',
        r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wuw_events_l_braz_por.yml',
        r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\WUW_events_l_braz_por.yml'
    ]

    # UTF-8 BOM
    bom_content = b'\xef\xbb\xbf' + content.encode('utf-8')

    for t in targets:
        os.makedirs(os.path.dirname(t), exist_ok=True)
        with open(t, 'wb') as f:
            f.write(bom_content)
        print(f"Written: {t} ({len(bom_content)} bytes)")

    return True

if __name__ == '__main__':
    main()
