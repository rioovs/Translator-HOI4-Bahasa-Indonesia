import os
import re
from analyze_all_taog import parse_hoi4_loc

for fname in ['TAOG_events_l_english.yml', 'TAOG_decisions_l_english.yml', 'TAOG_focus_l_english.yml']:
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    entries = parse_hoi4_loc(path)
    
    non_ast_sia = []
    for e in entries:
        k = e['key']
        # filter out AST (Australia), SIA/siam (Siam), NZL (New Zealand)
        first = k.split('_')[0].split('.')[0]
        if first in ['AST', 'ast', 'SIA', 'siam', 'NZL']:
            continue
        non_ast_sia.append(e)
        
    print(f"=== {fname} ===")
    print(f"Total non-AST/SIA/NZL entries: {len(non_ast_sia)}")
    prefixes = {}
    for e in non_ast_sia:
        p = e['key'].split('_')[0].split('.')[0]
        prefixes[p] = prefixes.get(p, 0) + 1
    print("Prefixes:", prefixes)
    print("Sample keys:")
    for e in non_ast_sia[:15]:
        print(f"  {e['key']}: {e['content'][:60]}")
    print()
