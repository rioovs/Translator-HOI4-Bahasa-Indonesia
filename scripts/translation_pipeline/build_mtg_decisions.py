# -*- coding: utf-8 -*-
"""
Build and validate mtg_decisions_l_braz_por.yml
"""
import os
import re
import json
from draft_mtg_part1 import get_mtg_translations as get_part1
from mtg_translations_mex import get_mex_translations
from mtg_translations_hol import get_hol_translations
from mtg_translations_usa import get_usa_translations
from mtg_translations_eng import get_eng_translations

def build_mtg():
    translations = {}
    translations.update(get_part1())
    translations.update(get_mex_translations())
    translations.update(get_hol_translations())
    translations.update(get_usa_translations())
    translations.update(get_eng_translations())

    print(f"Total MTG translated keys defined: {len(translations)}")

    src = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\mtg_decisions_l_english.yml'
    with open(src, 'r', encoding='utf-8-sig', errors='ignore') as f:
        src_lines = f.readlines()

    out_lines = ['l_braz_por:\n']
    missing = []
    translated_count = 0

    for idx, line in enumerate(src_lines[1:], 2):
        raw = line.rstrip('\r\n')
        stripped = raw.strip()
        if not stripped or stripped.startswith('#'):
            out_lines.append(raw + '\n')
            continue
        m = re.match(r'^(\s*)([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"(\s*#.*)?$', raw)
        if m:
            indent, key, version, val, comment = m.groups()
            v_suffix = f":{version}" if version != "" else ":"
            comment_str = comment if comment else ""
            trans_val = translations.get(key)
            if trans_val is None:
                trans_val = translations.get(f"{key}:{version}")
            if trans_val is not None:
                translated_count += 1
                out_lines.append(f'{indent}{key}{v_suffix} "{trans_val}"{comment_str}\n')
            else:
                missing.append((idx, key, val))
                out_lines.append(f'{indent}{key}{v_suffix} "{val}"{comment_str}\n')
        else:
            out_lines.append(raw + '\n')

    print(f"MTG Decisions: {translated_count} translated, {len(missing)} missing.")
    if missing:
        for m in missing[:10]:
            print("  Missing:", m)
        return False

    content = ''.join(out_lines)
    dests = [
        r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\mtg_decisions_l_braz_por.yml',
        r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\mtg_decisions_l_braz_por.yml'
    ]
    for d in dests:
        os.makedirs(os.path.dirname(d), exist_ok=True)
        with open(d, 'wb') as fp:
            fp.write(b'\xef\xbb\xbf')
            fp.write(content.encode('utf-8'))
        print(f"Wrote {len(out_lines)} lines to {d}")

    return True

if __name__ == '__main__':
    build_mtg()
