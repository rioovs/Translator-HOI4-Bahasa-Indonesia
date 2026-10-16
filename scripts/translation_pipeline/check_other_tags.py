import os
from analyze_all_taog import parse_hoi4_loc

def check_other(fname, tags):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    entries = parse_hoi4_loc(path)
    for e in entries:
        k = e['key']
        p = k.split('_')[0].split('.')[0]
        if p in tags:
            print(f"[{fname}] {k}: {e['content']}")

check_other('TAOG_events_l_english.yml', ['taog'])
print("-" * 50)
check_other('TAOG_decisions_l_english.yml', ['war', 'idea', 'has', 'HOL', 'recognize', 'form', 'phillipines', 'will', 'is', 'open', 'improved'])
print("-" * 50)
check_other('TAOG_focus_l_english.yml', ['HOL', 'idea', 'vichy', 'modify', 'jungle', 'generic', 'add', 'available', 'in', 'the', 'effects', 'potential', 'remove', 'effect', 'abdacom'])
