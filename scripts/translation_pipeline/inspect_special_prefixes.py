import os
from analyze_all_taog import parse_hoi4_loc

def inspect_prefixes(fname, prefixes_to_check):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    entries = parse_hoi4_loc(path)
    for e in entries:
        p = e['key'].split('_')[0].split('.')[0]
        if p in prefixes_to_check:
            print(f"[{fname}] {e['key']}: {e['content'][:80]}")

inspect_prefixes('TAOG_events_l_english.yml', ['taog', 'ABDA'])
inspect_prefixes('TAOG_decisions_l_english.yml', ['war', 'idea', 'indonesia', 'INSHOL', 'HOL', 'recognize', 'form', 'phillipines', 'will', 'is', 'has', 'open', 'improved'])
inspect_prefixes('TAOG_focus_l_english.yml', ['idea', 'vichy', 'modify', 'jungle', 'generic', 'indonesia', 'ABDA', 'abdacom', 'HOL'])
