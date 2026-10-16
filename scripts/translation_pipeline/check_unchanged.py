# -*- coding: utf-8 -*-
import json
import re
from test_nat_trans import translate_nat_value, nat_items

unchanged = []
for it in nat_items:
    k = it['key']
    orig = it['value']
    trans = translate_nat_value(k, orig)
    if trans == orig:
        unchanged.append((k, orig))

print(f"Total unchanged: {len(unchanged)}")
# Check for any English words in unchanged
english_triggers = [
    'Belt', 'Deck', 'Tubes', 'Tube', 'Launcher', 'Torpedo', 'Engine', 'Turbine', 'Boiler',
    'Snorkel', 'Schnorchel', 'Snort', 'Snuiver', 'Catapult', 'Hangar', 'Computer', 'Rangekeeper',
    'Radar', 'Sonar', 'Hydrophone', 'Thrower', 'Mortar', 'Rack', 'Rails', 'Sweep', 'Dual',
    'Battery', 'Cannon', 'Auto', 'Air', 'Piston', 'Loading'
]

flagged = []
for k, v in unchanged:
    for tr in english_triggers:
        if re.search(r'\b' + re.escape(tr) + r'\b', v, re.I):
            flagged.append((k, v, tr))
            break

print(f"Flagged for further check: {len(flagged)}")
for k, v, tr in flagged:
    print(f"  {k}: {repr(v)} (matched: {tr})")
