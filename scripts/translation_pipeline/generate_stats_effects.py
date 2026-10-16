# -*- coding: utf-8 -*-
import os, sys, re, json
from stats_map import STATS_TRANSLATIONS
from effects_map import EFFECTS_TRANSLATIONS

BOM = b'\xef\xbb\xbf'

def process_file(src_path, targets, trans_map):
    print(f"\nProcessing {os.path.basename(src_path)}...")
    with open(src_path, 'r', encoding='utf-8-sig') as f:
        src_lines = f.readlines()

    output_lines = []
    # Line 0: Header
    output_lines.append("l_braz_por:\n")

    key_count = 0
    translated_count = 0

    for idx, line in enumerate(src_lines[1:], start=2):
        raw = line.rstrip('\r\n')
        if not raw.strip():
            output_lines.append("\n")
            continue
        if raw.strip().startswith('#'):
            output_lines.append(raw + "\n")
            continue

        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*(#.*)?$', raw)
        if m:
            indent, k, ver, val, cmt = m.groups()
            key_count += 1
            if k in trans_map:
                new_val = trans_map[k]
                translated_count += 1
            else:
                new_val = val

            cmt_str = f" {cmt}" if cmt else ""
            line_out = f'{indent}{k}:{ver} "{new_val}"{cmt_str}\n'
            output_lines.append(line_out)
        else:
            print(f"Warning: line {idx} did not match pattern: {raw}")
            output_lines.append(raw + "\n")

    full_text = "".join(output_lines)
    encoded = BOM + full_text.encode('utf-8')

    for tgt in targets:
        os.makedirs(os.path.dirname(tgt), exist_ok=True)
        with open(tgt, 'wb') as f:
            f.write(encoded)
        print(f"  Written {len(encoded)} bytes to: {tgt}")

    print(f"  Total keys: {key_count}, Translated: {translated_count}")

stats_src = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\stats_l_english.yml"
stats_targets = [
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\stats_l_braz_por.yml",
    r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\stats_l_braz_por.yml"
]

effects_src = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\effects_l_english.yml"
effects_targets = [
    r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\effects_l_braz_por.yml",
    r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\effects_l_braz_por.yml"
]

process_file(stats_src, stats_targets, STATS_TRANSLATIONS)
process_file(effects_src, effects_targets, EFFECTS_TRANSLATIONS)
print("\nGeneration completed successfully.")
