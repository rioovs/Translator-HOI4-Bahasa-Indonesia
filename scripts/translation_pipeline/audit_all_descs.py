# -*- coding: utf-8 -*-
import json
import re

with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    detected_335 = json.load(f)

detected_keys = {d['key'] for d in detected_335}

# Let's inspect every _desc in the entire file not in detected_335
not_detected = []
for idx, l in enumerate(lines, 1):
    s = l.strip()
    if not s or s.startswith('#'):
        continue
    if '_desc:' in s:
        parts = s.split(':', 1)
        k = parts[0].strip()
        v = parts[1].strip()
        if k not in detected_keys:
            not_detected.append((idx, k, v))

print(f"Total other descs: {len(not_detected)}")

# Let's check if any of these contain any English indicators:
suspicious = []
eng_test = [' the ', ' to ', ' of ', ' and ', ' with ', ' will ', ' our ', ' for ', ' from ', ' that ', ' this ', ' by ', ' on ', ' in ', ' as ', ' is ', ' was ', ' are ', ' were ', ' be ']

for idx, k, v in not_detected:
    # ignore variable references
    v_clean = v.strip('"')
    if v_clean.startswith('0 '):
        v_clean = v_clean[2:].strip('"')
    if v_clean.startswith('$') and v_clean.endswith('$'):
        continue
    if not v_clean:
        continue
    vlow = ' ' + v_clean.lower() + ' '
    hits = [w.strip() for w in eng_test if w in vlow]
    if hits:
        suspicious.append((idx, k, v_clean, hits))

print(f"Suspicious other descs: {len(suspicious)}")
for idx, k, v, hits in suspicious:
    print(f"L{idx} {k}: {v[:80]} (hits: {hits})")
