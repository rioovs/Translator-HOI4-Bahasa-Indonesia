import json
import re

for p_num in [5, 6]:
    with open(f'scripts/p{p_num}_for_trans.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    vars_count = 0
    colors_count = 0
    icons_count = 0
    for k, v in data.items():
        if '$' in v: vars_count += 1
        if '§' in v: colors_count += 1
        if '£' in v: icons_count += 1
    print(f"P{p_num}: {len(data)} items | with vars: {vars_count} | with colors: {colors_count} | with icons: {icons_count}")
