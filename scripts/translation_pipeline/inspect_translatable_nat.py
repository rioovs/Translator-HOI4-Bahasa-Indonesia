# -*- coding: utf-8 -*-
import json
import re

with open('scripts/parsed_ship_modules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nat_items = [d for d in data if d['type'] == 'key_val' and d['line_idx'] >= 383 and not d['key'].startswith(('ship_light_battery_sub', 'EQ_MOD_CAT_ship_light_battery_sub', 'cruiser_submarine_specialization', 'midget_submarine_specialization'))]

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

# Let's inspect every value that is not purely alphanumeric designation
def classify(v):
    if re.search(r'\bBelt\b', v, re.I) or re.search(r'\bDeck\b', v, re.I):
        return 'ARMOR'
    if re.search(r'\bTorpedo\b', v, re.I) or re.search(r'\bTorp\b', v, re.I) or re.search(r'\bTTs?\b', v) or re.search(r'\bTubes\b', v, re.I):
        return 'TORPEDO'
    if re.search(r'\bEngine\b', v, re.I) or re.search(r'\bReactor\b', v, re.I) or re.search(r'\bDiesels?\b', v, re.I) or re.search(r'\bElectric\b', v, re.I):
        return 'ENGINE'
    if re.search(r'\bRadar\b', v, re.I) or re.search(r'\bSonar\b', v, re.I) or re.search(r'\bHydrophone\b', v, re.I) or re.search(r'\bH\.phone\b', v, re.I):
        return 'RADAR_SONAR'
    if re.search(r'\bAuto-Load(ing)?\b', v, re.I) or re.search(r'\bAuto\b', v, re.I):
        return 'AUTOLOAD'
    return 'MODEL_NAME'

categories = {}
for v, count in unique_vals.items():
    cat = classify(v)
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((v, count))

for cat, lst in categories.items():
    print(f"\n=== CATEGORY: {cat} ({len(lst)} unique values) ===")
    for v, c in lst[:20]:
        print(f"  {repr(v)} (count: {c})")
    if len(lst) > 20:
        print(f"  ... and {len(lst) - 20} more")
