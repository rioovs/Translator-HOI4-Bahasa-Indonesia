import os
import sys
sys.path.append('scripts')
from analyze_all_taog import parse_hoi4_loc

entries = parse_hoi4_loc(os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', 'TAOG_decisions_l_english.yml'))

keys_by_group = {
    'INS': [],
    'INSHOL': [],
    'HOL': [],
    'INDONESIA_NUSANTARA_WAR': [],
    'OTHER_NOT_AST_SIA': []
}

for e in entries:
    k = e['key']
    p = k.split('_')[0].split('.')[0]
    if p in ['AST', 'ast', 'SIA', 'NZL'] or k.startswith('idea_AST') or k.startswith('idea_SIA') or k.startswith('has_built_fortress') or k == 'open_mae_moh_lignite_mine':
        continue
    if k.startswith('INS_'):
        keys_by_group['INS'].append(e)
    elif k.startswith('INSHOL_'):
        keys_by_group['INSHOL'].append(e)
    elif k.startswith('HOL_'):
        keys_by_group['HOL'].append(e)
    elif any(w in k.lower() for w in ['indonesia', 'majapahit', 'maphilindo', 'war_escalation', 'limited_war', 'phillipines', 'will_complete_when_conditions_met']):
        keys_by_group['INDONESIA_NUSANTARA_WAR'].append(e)
    else:
        keys_by_group['OTHER_NOT_AST_SIA'].append(e)

for g, items in keys_by_group.items():
    print(f"Group {g}: {len(items)} items")

print("\nOTHER_NOT_AST_SIA items:")
for item in keys_by_group['OTHER_NOT_AST_SIA']:
    print(f"  {item['key']}: {item['content']}")
