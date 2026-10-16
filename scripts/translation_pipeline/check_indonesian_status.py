# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_event_td_keys.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

braz_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
with open(braz_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

braz_dict = {}
for l in lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        braz_dict[m.group(1)] = m.group(3)

genuine_id = []
for item in items:
    k = item['key']
    en = item['en']
    br = braz_dict.get(k, "")
    
    # Check if br has substantial Indonesian words and is not just English with 'Kita harus'
    # Count some common English stop words
    en_words = set(re.findall(r'\b[a-z]{3,}\b', en.lower()))
    br_words = set(re.findall(r'\b[a-z]{3,}\b', br.lower()))
    
    # English stop words
    en_stops = {'the', 'and', 'that', 'have', 'for', 'not', 'with', 'you', 'this', 'but', 'his', 'from', 'they'}
    has_en_stops = len(br_words.intersection(en_stops)) > 2
    
    if br and br != en and not has_en_stops:
        genuine_id.append((k, en, br))

print(f"Genuine Indonesian items: {len(genuine_id)} out of {len(items)}")
for k, e, b in genuine_id[:10]:
    print(f"[{k}]\n  EN: {e}\n  ID: {b}\n")
