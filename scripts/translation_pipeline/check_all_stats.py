# -*- coding: utf-8 -*-
import os
import re

dir_local = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por'
dir_game = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por'

files = [f for f in os.listdir(dir_local) if f.endswith('.yml')]
files.sort()

total_files = len(files)
total_lines = 0
total_keys = 0
bom_errors = []
missing_in_game = []

for f in files:
    lp = os.path.join(dir_local, f)
    gp = os.path.join(dir_game, f)
    if not os.path.exists(gp):
        missing_in_game.append(f)
    
    with open(lp, 'rb') as fb:
        content_bytes = fb.read()
        if not content_bytes.startswith(b'\xef\xbb\xbf'):
            bom_errors.append(f)
            
    with open(lp, 'r', encoding='utf-8-sig') as ft:
        lines = ft.readlines()
        total_lines += len(lines)
        for l in lines:
            if re.match(r'^\s*[A-Za-z0-9_.-]+:(\d*)\s*".*"\s*$', l):
                total_keys += 1

print(f"Total Translated Files: {total_files}")
print(f"Total Lines: {total_lines:,}")
print(f"Total Localisation Keys: {total_keys:,}")
print(f"BOM Errors: {len(bom_errors)} {bom_errors}")
print(f"Missing in Game: {len(missing_in_game)} {missing_in_game}")

major_files = [
    'core', 'frontend', 'topbar', 'alerts', 'country', 'production', 'trade',
    'deployment', 'constructions', 'peace', 'waroverview', 'war', 'autonomy',
    'politics', 'intel_ledger', 'intelligence_agencies', 'mapmode', 'musicplayer',
    'loading_tips', 'tactics', 'theater', 'ranks', 'rules', 'difficulty',
    'chat', 'videos', 'bookmarks', 'parties', 'game_rules', 'doctrines',
    'combat', 'diplomacy', 'modifiers', 'equipment', 'traits', 'equip_air',
    'ideas', 'focus', 'equip_naval', 'military_industrial_organization',
    'events', 'decisions', 'operatives', 'lar_operations', 'research',
    'designer', 'tank_modules', 'ship_modules', 'plane_designer', 'unit',
    'wtt_focus', 'wtt_events', 'wuw_focus', 'wuw_events'
]

print(f"\n=== REKAP {len(major_files)} BERKAS UTAMA GAMEPLAY (BAHASA INDONESIA) ===")
major_keys = 0
major_lines = 0
for name in sorted(major_files):
    fn = f"{name}_l_braz_por.yml"
    fp = os.path.join(dir_local, fn)
    if os.path.exists(fp):
        with open(fp, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
            keys = sum(1 for l in lines if re.match(r'^\s*[A-Za-z0-9_.-]+:(\d*)\s*".*"', l))
            major_keys += keys
            major_lines += len(lines)
            print(f" - {fn:<38} : {keys:>5} keys | {len(lines):>5} lines")

print("-" * 55)
print(f"TOTAL {len(major_files)} BERKAS UTAMA: {major_keys:,} keys | {major_lines:,} lines")


