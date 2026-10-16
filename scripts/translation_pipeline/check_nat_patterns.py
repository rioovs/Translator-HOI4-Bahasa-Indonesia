# -*- coding: utf-8 -*-
import json
import re

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

# Let's inspect which unique values have translatable components
translatable = {}
pure_names = {}

for val, count in unique_vals.items():
    # Check if has English common words
    has_translatable = False
    reasons = []
    
    if re.search(r'\bBelt\b', val, re.I):
        reasons.append('Belt')
    if re.search(r'\bDeck\b', val, re.I):
        reasons.append('Deck')
    if re.search(r'\bEngine\b', val, re.I):
        reasons.append('Engine')
    if re.search(r'\bReactor\b', val, re.I):
        reasons.append('Reactor')
    if re.search(r'\bPressurized\b', val, re.I):
        reasons.append('Pressurized')
    if re.search(r'\bTorpedo\b', val, re.I) or re.search(r'\bTorp\b', val, re.I) or re.search(r'\bTTs?\b', val) or re.search(r'\bTubes\b', val, re.I):
        reasons.append('Torpedo/Tubes/TT')
    if re.search(r'\bw/Comp\.?\s*Air\b', val, re.I):
        reasons.append('Comp. Air')
    if re.search(r'\bw/P\.?\s*Loading\b', val, re.I):
        reasons.append('P.Loading')
    if re.search(r'\bw/L\.?\s*Pistons?\b', val, re.I):
        reasons.append('L.Pistons')
    if re.search(r'\bAuto-Load(ing)?\b', val, re.I):
        reasons.append('Auto-Loading')
    if re.search(r'\bRadar\b', val, re.I):
        reasons.append('Radar')
    if re.search(r'\bSonar\b', val, re.I) or re.search(r'\bHydrophone\b', val, re.I) or re.search(r'\bH\.phone\b', val, re.I):
        reasons.append('Sonar/Hydrophone')
    if re.search(r'\bDiesels?\b', val, re.I):
        reasons.append('Diesel')
    if re.search(r'\bElectric\b', val, re.I):
        reasons.append('Electric')
    if re.search(r'\bSearch\b', val, re.I):
        reasons.append('Search')
    if re.search(r'\bThermal\b', val, re.I):
        reasons.append('Thermal')
    if re.search(r'\bBow\b', val, re.I):
        reasons.append('Bow')
    if re.search(r'\bTriple\b', val, re.I) or re.search(r'\bQuadruple\b', val, re.I) or re.search(r'\bQuintuple\b', val, re.I) or re.search(r'\bPentad\b', val, re.I) or re.search(r'\bTwin\b', val, re.I):
        reasons.append('Tuple/Plex')
    
    if reasons:
        translatable[val] = reasons
    else:
        pure_names[val] = count

print(f"Translatable or partial patterns: {len(translatable)}")
print(f"Pure model names: {len(pure_names)}")

print("\nSample translatable:")
for val, reasons in list(translatable.items())[:30]:
    print(f"  {val} -> {reasons}")

print("\nSample pure model names:")
for val, count in list(pure_names.items())[:30]:
    print(f"  {val}")
