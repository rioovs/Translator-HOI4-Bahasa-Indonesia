# -*- coding: utf-8 -*-
import re

p_game = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
p_local = 'f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/events_l_braz_por.yml'
p_eng = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'

with open(p_game, 'rb') as f:
    raw_game = f.read()

with open(p_local, 'rb') as f:
    raw_local = f.read()

assert raw_game.startswith(b'\xef\xbb\xbf'), "Game file missing UTF-8 BOM!"
assert raw_local.startswith(b'\xef\xbb\xbf'), "Local file missing UTF-8 BOM!"
assert raw_game == raw_local, "Files do not match!"

with open(p_game, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

with open(p_eng, 'r', encoding='utf-8-sig') as f:
    eng_lines = f.readlines()

eng_data = {}
for l in eng_lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        eng_data[m.group(1)] = m.group(3)

game_data = {}
for l in lines:
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
    if m:
        game_data[m.group(1)] = m.group(3)

identical_td = []
for k, v in game_data.items():
    suffix = k.split('.')[-1]
    is_td = suffix in ('t', 'title', 'd', 'desc') or suffix.startswith('d_') or suffix.startswith('desc_') or '.d.' in k or 'title' in k
    if is_td:
        en = eng_data.get(k, '')
        if v == en and len(en.strip()) > 0:
            # Check if it's not a pure variable like $VAR$ or identical proper noun like "Anschluss"
            identical_td.append((k, v))

print(f"Total lines: {len(lines)}")
print(f"Total keys: {len(game_data)}")
print(f"Identical .t/.d to English count: {len(identical_td)}")
if identical_td:
    print("Identical keys:")
    for k, v in identical_td[:10]:
        print(f"  {k}: {v}")
else:
    print("ALL .t and .d keys are successfully translated to Indonesian!")
