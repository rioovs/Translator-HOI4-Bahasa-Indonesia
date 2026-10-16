import os
import sys
import json
sys.path.append('scripts')
from analyze_all_taog import parse_hoi4_loc

def extract_keys(fname, output_json, filter_func):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    entries = parse_hoi4_loc(path)
    to_trans = []
    for e in entries:
        if filter_func(e):
            to_trans.append({
                'key': e['key'],
                'version': e['version'],
                'en': e['content']
            })
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(to_trans, f, ensure_ascii=False, indent=2)
    print(f"{fname} -> {output_json}: {len(to_trans)} items extracted.")

def filter_events(e):
    k = e['key']
    p = k.split('_')[0].split('.')[0]
    if p in ['AST', 'SIA', 'siam']:
        return False
    return True

def filter_decisions(e):
    k = e['key']
    p = k.split('_')[0].split('.')[0]
    if p in ['AST', 'ast', 'SIA', 'NZL'] or k.startswith('idea_AST') or k.startswith('idea_SIA') or k.startswith('has_built_fortress') or k == 'open_mae_moh_lignite_mine':
        return False
    return True

def filter_focus(e):
    k = e['key']
    p = k.split('_')[0].split('.')[0]
    if p in ['AST', 'NZL', 'SIA']:
        return False
    if k.startswith('idea_AST') or k.startswith('idea_SIA') or k.startswith('modify_AST') or k.startswith('vichy') or k.startswith('modify_SIA') or k.startswith('modify_royal_thai_navy') or k == 'the_thunder_at_our_gates_artillery':
        return False
    return True

extract_keys('TAOG_events_l_english.yml', 'scripts/taog_events_to_trans.json', filter_events)
extract_keys('TAOG_decisions_l_english.yml', 'scripts/taog_decisions_to_trans.json', filter_decisions)
extract_keys('TAOG_focus_l_english.yml', 'scripts/taog_focus_to_trans.json', filter_focus)
