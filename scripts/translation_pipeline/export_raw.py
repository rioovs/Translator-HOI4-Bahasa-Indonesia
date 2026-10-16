# -*- coding: utf-8 -*-
import json
import re

def export_wtt_focus():
    src = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_focus_l_english.yml'
    with open(src, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    entries = []
    for l in lines[1:]:
        if not l.strip() or l.strip().startswith('#'):
            continue
        m = re.match(r'^\s*([A-Za-z0-9_\.]+)(?::\d*)?\s+"(.*)"\s*$', l)
        if m:
            entries.append({"key": m.group(1), "en": m.group(2)})
    
    with open('wtt_focus_raw.json', 'w', encoding='utf-8') as out:
        json.dump(entries, out, indent=2, ensure_ascii=False)
    print(f"Exported {len(entries)} entries to wtt_focus_raw.json")

def export_wtt_events():
    src = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_events_l_english.yml'
    with open(src, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    entries = []
    for l in lines[1:]:
        if not l.strip() or l.strip().startswith('#'):
            continue
        m = re.match(r'^\s*([A-Za-z0-9_\.]+)(?::\d*)?\s+"(.*)"\s*$', l)
        if m:
            entries.append({"key": m.group(1), "en": m.group(2)})
    
    with open('wtt_events_raw.json', 'w', encoding='utf-8') as out:
        json.dump(entries, out, indent=2, ensure_ascii=False)
    print(f"Exported {len(entries)} entries to wtt_events_raw.json")

export_wtt_focus()
export_wtt_events()
