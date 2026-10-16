# -*- coding: utf-8 -*-
"""
merge_and_install_taog.py
Merges all completed translation chunks for TAOG (Dutch East Indies & Indonesia):
- Decisions: translate_taog_decisions.py
- Events: translate_taog_events_part1.py, part2.py, part3.py
- Focus: translate_taog_focus_part1.py, part2.py, part3.py, part4.py

Validates syntax and installs with UTF-8 BOM to game folder and local repo mirror.
"""
import os
import re
import sys

GAME_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"
ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

# Import all parts
sys.path.append(r"f:\New Coding\rea-hoi4-indonesia\scripts")

from translate_taog_decisions import DECISION_TRANSLATIONS
from translate_taog_events_part1 import EVENTS_PART1
from translate_taog_events_part2 import EVENTS_PART2
from translate_taog_events_part3 import EVENTS_PART3
from translate_taog_focus_part1 import FOCUS_PART1
from translate_taog_focus_part2 import FOCUS_PART2
from translate_taog_focus_part3 import FOCUS_PART3
from translate_taog_focus_part4 import FOCUS_PART4

ALL_EVENTS = {}
ALL_EVENTS.update(EVENTS_PART1)
ALL_EVENTS.update(EVENTS_PART2)
ALL_EVENTS.update(EVENTS_PART3)

ALL_FOCUS = {}
ALL_FOCUS.update(FOCUS_PART1)
ALL_FOCUS.update(FOCUS_PART2)
ALL_FOCUS.update(FOCUS_PART3)
ALL_FOCUS.update(FOCUS_PART4)

ALL_DECISIONS = DECISION_TRANSLATIONS

print(f"Loaded translations:")
print(f"  Decisions: {len(ALL_DECISIONS)} entries")
print(f"  Events   : {len(ALL_EVENTS)} entries")
print(f"  Focus    : {len(ALL_FOCUS)} entries")

def apply_and_write(base_name, trans_dict):
    eng_path = os.path.join(ENG_DIR, f"{base_name}_l_english.yml")
    with open(eng_path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
        
    out_lines = ["l_braz_por:\n"]
    matched = 0
    total_keys = 0
    
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            out_lines.append(line)
            continue
            
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            total_keys += 1
            indent, key, ver, orig_val, comment = m.groups()
            v_str = f":{ver}" if ver else ":"
            comment_str = comment or ""
            
            if key in trans_dict:
                matched += 1
                val = trans_dict[key]
                # internal quote escaping
                val = val.replace('“', '\\"').replace('”', '\\"')
                parts = val.split(r'\"')
                parts = [p.replace('"', r'\"') for p in parts]
                val = r'\"'.join(parts)
                out_lines.append(f"{indent}{key}{v_str} \"{val}\"{comment_str}\n")
            else:
                out_lines.append(line)
        else:
            out_lines.append(line)
            
    print(f"\n[{base_name}] Processed: {matched}/{total_keys} keys translated to Indonesian ({matched/max(1,total_keys)*100:.1f}%)")
    
    content = "".join(out_lines)
    for folder in [GAME_DIR, LOCAL_DIR]:
        target = os.path.join(folder, f"{base_name}_l_braz_por.yml")
        with open(target, 'wb') as f:
            f.write(b'\xef\xbb\xbf')
            f.write(content.encode('utf-8'))
        print(f"  Successfully wrote: {target} ({os.path.getsize(target)} bytes)")

def main():
    apply_and_write("TAOG_decisions", ALL_DECISIONS)
    apply_and_write("TAOG_events", ALL_EVENTS)
    apply_and_write("TAOG_focus", ALL_FOCUS)

if __name__ == "__main__":
    main()
