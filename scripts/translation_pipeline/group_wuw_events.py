import json

with open('scripts/wuw_events_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Group by major prefix / theme
groups = {}
for i, item in enumerate(items):
    k = item['key']
    prefix = k.split('.')[0] if '.' in k else k.split('_')[0]
    # simplify prefix
    if prefix.startswith('AUS'):
        cat = 'AUS (Austria)'
    elif prefix.startswith('WW_hungary') or prefix.startswith('wuw_HUN') or prefix.startswith('HUN'):
        cat = 'HUN (Hungary)'
    elif 'BEL' in prefix or prefix.startswith('ww_BEL') or prefix.startswith('BEL'):
        cat = 'BEL (Belgium)'
    elif 'congo' in prefix.lower() or 'cog' in prefix.lower() or prefix in ['evolue', 'lokot', 'congolese', 'CONGO']:
        cat = 'COG (Congo)'
    elif 'GER' in prefix or 'germany' in prefix or prefix.startswith('GOT_GER'):
        cat = 'GER (Germany)'
    else:
        cat = f'Other ({prefix})'
    
    if cat not in groups:
        groups[cat] = []
    groups[cat].append((i, item))

for cat, lst in groups.items():
    print(f"{cat}: {len(lst)} items (index range {lst[0][0]} to {lst[-1][0]})")
