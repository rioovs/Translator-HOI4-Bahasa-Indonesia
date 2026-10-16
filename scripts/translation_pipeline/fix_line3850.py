# -*- coding: utf-8 -*-
import json
import re

p = 'scripts/wuw_batches/batch6_ger_part2_translated.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

val = data['GER_asian_spheres_of_influence_tt']
val = re.sub(r'___\s*TK\s*4\s*8\s*___', '[RAJ.GetNameWithFlag]', val)
data['GER_asian_spheres_of_influence_tt'] = val

with open(p, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Fixed GER_asian_spheres_of_influence_tt!")
