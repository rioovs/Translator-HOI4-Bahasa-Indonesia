# -*- coding: utf-8 -*-
import re

src_path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\ship_modules_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

categories = []
slots = []
modules = []
nation_modules = []
current_sec = "TOP"

for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if s.startswith('### EQUIPMENT MODULE CATEGORIES'):
        current_sec = "CAT"
        continue
    elif s.startswith('### EQUIPMENT MODULE SLOTS'):
        current_sec = "SLOT"
        continue
    elif s.startswith('### EQUIPMENT MODULES'):
        current_sec = "MOD"
        continue
    elif s.startswith('### Nation Specific Modules'):
        current_sec = "NAT"
        continue
    
    m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$', line)
    if m:
        key, val = m.group(1), m.group(3)
        if current_sec == "CAT":
            categories.append((key, val))
        elif current_sec == "SLOT":
            slots.append((key, val))
        elif current_sec == "MOD":
            modules.append((key, val))
        elif current_sec == "NAT":
            nation_modules.append((key, val))

print(f"Categories count: {len(categories)}")
print(f"Slots count: {len(slots)}")
print(f"Generic Modules count: {len(modules)}")
print(f"Nation Modules count: {len(nation_modules)}")

print("\n--- SAMPLE CATEGORIES (first 10) ---")
for k, v in categories[:10]:
    print(f"{k}: {v}")

print("\n--- SAMPLE SLOTS (all) ---")
for k, v in slots:
    print(f"{k}: {v}")

print("\n--- SAMPLE MODULES (first 15) ---")
for k, v in modules[:15]:
    print(f"{k}: {v}")

print("\n--- SAMPLE NATION MODULES (first 15) ---")
for k, v in nation_modules[:15]:
    print(f"{k}: {v}")
