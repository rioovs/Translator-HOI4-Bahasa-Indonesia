import re
import os

def examine_keys(filename):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', filename)
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    print(f"================== {filename} ==================")
    comments = []
    keys = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('#'):
            comments.append(stripped)
        m = re.match(r'^\s*([A-Za-z0-9_\.\-]+):', stripped)
        if m:
            keys.append(m.group(1))
            
    print("Distinct comments / headers:")
    for c in comments:
        if any(w in c.upper() for w in ['INS', 'INDONESIA', 'EAST INDIES', 'DUTCH', 'BATAVIA', 'JAVA', 'REVOLUTION']):
            print("  ", c)
            
    # Check key prefixes
    prefix_counts = {}
    for k in keys:
        p = k.split('_')[0]
        prefix_counts[p] = prefix_counts.get(p, 0) + 1
    print("\nPrefix counts:")
    for p, count in sorted(prefix_counts.items(), key=lambda x: -x[1]):
        print(f"  {p}: {count}")

for fn in ['TAOG_events_l_english.yml', 'TAOG_decisions_l_english.yml', 'TAOG_focus_l_english.yml']:
    examine_keys(fn)
