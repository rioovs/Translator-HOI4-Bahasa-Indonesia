# -*- coding: utf-8 -*-
import json
import re

with open('scripts/nat_unique_values.json', 'r', encoding='utf-8') as f:
    unique_vals = json.load(f)

# Exclude already analyzed categories
def is_already_categorized(v):
    if re.search(r'\bBelt\b', v, re.I) or re.search(r'\bDeck\b', v, re.I):
        return True
    if re.search(r'\bTorpedo\b', v, re.I) or re.search(r'\bTorp\b', v, re.I) or re.search(r'\bTTs?\b', v) or re.search(r'\bTubes\b', v, re.I):
        return True
    if re.search(r'\bEngine\b', v, re.I) or re.search(r'\bReactor\b', v, re.I) or re.search(r'\bDiesels?\b', v, re.I) or re.search(r'\bElectric\b', v, re.I) or re.search(r'\bPressurized\b', v, re.I):
        return True
    if re.search(r'\bRadar\b', v, re.I) or re.search(r'\bSonar\b', v, re.I) or re.search(r'\bHydrophone\b', v, re.I) or re.search(r'\bH\.phone\b', v, re.I):
        return True
    if re.search(r'\bAuto-Load(ing)?\b', v, re.I) or re.search(r'\bAuto\b', v, re.I):
        return True
    return False

remaining = [v for v in unique_vals if not is_already_categorized(v)]
print(f"Remaining model names to inspect: {len(remaining)}")

# Collect words in remaining
words = set()
for v in remaining:
    for w in re.findall(r'[a-zA-Z]+', v):
        words.add(w)

known_designations = {
    'in', 'mm', 'cm', 'BL', 'QF', 'Mk', 'CP', 'mt', 'RP', 'LA', 'Mark', 'SP', 'RPC', 'DP',
    'RF', 'FCT', 'Vickers', 'Armstrong', 'Ansaldo', 'OTO', 'SK', 'Tbts', 'KC', 'Model', 'Mle',
    'Rev', 'Type', 'Yr', 'Pattern', 'Ptn', 'SM', 'Minizini', 'bis', 'Schneider', 'Canet',
    'Bofors', 'Breda', 'Colt', 'Browning', 'Oerlikon', 'Hotchkiss', 'Dreyer', 'Admiralty',
    'Brown', 'Curtis', 'Parsons', 'Sulzer', 'Kampon', 'Gihon', 'Mitsubishi', 'Vulcan', 'Deschimag',
    'Impr', 'Desch', 'Schichau', 'Germania', 'Blohm', 'Voss', 'VTE', 'Boveri', 'GTZA', 'TV',
    'Tosi', 'NLSE', 'Nelseco', 'Normand', 'Vic', 'Laval', 'Motala', 'Götaverken', 'Atlas',
    'Werke', 'GHG', 'Gerät', 'FuMO', 'Arktur', 'Tamir', 'Redut', 'Giuis', 'Redan', 'Shp', 'hp',
    'PWR', 'S', 'W', 'VM', 'A', 'JK', 'QCA', 'QGA', 'XAF', 'CXAM', 'FC', 'Gufo', 'cal',
    'MG', 'AA', 'Quad', 'Twin', 'Quin', 'Pentad', 'Triple', 'Quintuple', 'Quadruple', 'TDC',
    'SIA', 'SPR', 'ARG', 'BRA', 'CHI', 'CHL', 'DEN', 'ENG', 'EST', 'FIN', 'FRA', 'GER',
    'GRE', 'HOL', 'ITA', 'JAP', 'LAT', 'NOR', 'POL', 'POR', 'PRU', 'ROM', 'SOV', 'SWE',
    'TUR', 'URG', 'USA', 'YUG', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'X', 'Y', 'Z', 'Vert'
}

suspicious_words = [w for w in words if w not in known_designations and not w.isupper() and len(w) > 2]
print(f"Suspicious words: {suspicious_words}")

for v in remaining:
    if any(re.search(r'\b' + re.escape(w) + r'\b', v) for w in suspicious_words):
        print(f"  {repr(v)}")
