import os
import sys
sys.path.append('scripts')
from analyze_all_taog import parse_hoi4_loc

entries = parse_hoi4_loc(os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', 'TAOG_focus_l_english.yml'))

keys_by_group = {
    'INS': [],
    'INSHOL': [],
    'ABDA': [],
    'HOL': [],
    'INDONESIA': [],
    'OTHER_NOT_AST_SIA': []
}

for e in entries:
    k = e['key']
    p = k.split('_')[0].split('.')[0]
    if p in ['AST', 'NZL', 'SIA']:
        continue
    if k.startswith('idea_AST') or k.startswith('idea_SIA') or k.startswith('modify_AST') or k.startswith('vichy'):
        continue
    if k.startswith('INS_') or k.startswith('INS.'):
        keys_by_group['INS'].append(e)
    elif k.startswith('INSHOL_'):
        keys_by_group['INSHOL'].append(e)
    elif k.startswith('ABDA_') or k == 'abdacom_member':
        keys_by_group['ABDA'].append(e)
    elif k.startswith('HOL_'):
        keys_by_group['HOL'].append(e)
    elif 'indonesia' in k.lower():
        keys_by_group['INDONESIA'].append(e)
    else:
        keys_by_group['OTHER_NOT_AST_SIA'].append(e)

for g, items in keys_by_group.items():
    print(f"Group {g}: {len(items)} items")

print("\nOTHER_NOT_AST_SIA items:")
for item in keys_by_group['OTHER_NOT_AST_SIA']:
    print(f"  {item['key']}: {item['content']}")
