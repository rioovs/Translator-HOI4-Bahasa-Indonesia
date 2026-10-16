# -*- coding: utf-8 -*-
import json
import re

with open('scripts/unmatched_deep.txt', 'r', encoding='utf-8') as f:
    items = [line.strip() for line in f if line.strip()]

# Write items out as a template Python script with rule-based smart translation
with open('scripts/build_final_779.py', 'w', encoding='utf-8') as out:
    out.write('''# -*- coding: utf-8 -*-
import json

# Comprehensive manual mappings for all 779 deep items
MAP_779 = {
''')
    for item in items:
        out.write(f'    {repr(item)}: "",\n')
    out.write('''}\n''')

print("Template written to scripts/build_final_779.py")
