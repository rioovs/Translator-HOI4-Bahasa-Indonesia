import os
import re
from analyze_all_taog import parse_hoi4_loc

def scan_file(fname):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    entries = parse_hoi4_loc(path)
    
    ins_related = []
    other = []
    for e in entries:
        k = e['key']
        p = k.split('_')[0].split('.')[0]
        # Check if key is INS, INSHOL, ABDA, HOL (in TAOG), or contains indonesia/east_indies/volksraad
        is_ins = False
        if p in ['INS', 'INSHOL', 'ABDA']:
            is_ins = True
        elif 'indonesia' in k.lower() or 'east_indies' in k.lower() or 'volksraad' in k.lower() or 'soekarno' in k.lower():
            is_ins = True
        elif p == 'HOL' and ('indies' in e['content'].lower() or 'ins' in k.lower() or 'java' in e['content'].lower()):
            is_ins = True
        elif any(w in k.lower() for w in ['militia', 'tkr', 'peta', 'knil', 'batavia']):
            is_ins = True
            
        if is_ins:
            ins_related.append(e)
        else:
            other.append(e)
            
    print(f"=== {fname} ===")
    print(f"Total entries: {len(entries)}")
    print(f"INS / Indonesia related: {len(ins_related)}")
    print(f"Other entries: {len(other)}")
    
    # Check what 'other' prefixes are
    other_prefixes = {}
    for e in other:
        p = e['key'].split('_')[0].split('.')[0]
        other_prefixes[p] = other_prefixes.get(p, 0) + 1
    print("Other prefixes:", sorted(other_prefixes.items(), key=lambda x: -x[1])[:10])

scan_file('TAOG_events_l_english.yml')
scan_file('TAOG_decisions_l_english.yml')
scan_file('TAOG_focus_l_english.yml')
