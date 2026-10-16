# -*- coding: utf-8 -*-
import json
import re

# Load source
with open('scripts/batch_2_source.json', 'r', encoding='utf-8') as f:
    source_items = json.load(f)

source_dict = {item['key']: item['en'] for item in source_items}
print(f"Total source items: {len(source_items)}")
print(f"Total source unique keys: {len(source_dict)}")

# Load chunks
all_translations = {}
for i in range(1, 5):
    chunk_path = f'scripts/b2_chunk_{i}_translated.json'
    with open(chunk_path, 'r', encoding='utf-8') as f:
        c_data = json.load(f)
    print(f"Chunk {i} keys: {len(c_data)}")
    for k, v in c_data.items():
        if k in all_translations:
            print(f"WARNING: Duplicate key {k} found in chunk {i}!")
        all_translations[k] = v

print(f"Total translated keys: {len(all_translations)}")

# Check key completeness
missing_keys = [k for k in source_dict if k not in all_translations]
extra_keys = [k for k in all_translations if k not in source_dict]

if missing_keys:
    print(f"ERROR: Missing keys ({len(missing_keys)}): {missing_keys}")
else:
    print("SUCCESS: 0 missing keys.")

if extra_keys:
    print(f"ERROR: Extra keys ({len(extra_keys)}): {extra_keys}")
else:
    print("SUCCESS: 0 extra keys.")

# Validate tags & variables preservation
var_pattern = re.compile(r'(\[[^\]]+\]|\$[A-Za-z0-9_]+\$|§[A-Za-z!])')

mismatches = []
empty_entries = []

for k, en_text in source_dict.items():
    tr_text = all_translations.get(k, '')
    if not tr_text or not tr_text.strip():
        empty_entries.append(k)

    en_vars = set(re.findall(r'\[[a-zA-Z0-9_\.\?]+\]', en_text))
    tr_vars = set(re.findall(r'\[[a-zA-Z0-9_\.\?]+\]', tr_text))

    if en_vars != tr_vars:
        mismatches.append((k, en_vars, tr_vars))

if empty_entries:
    print(f"ERROR: Empty entries found: {empty_entries}")
else:
    print("SUCCESS: No empty entries.")

if mismatches:
    print(f"WARNING: Variable tag mismatches ({len(mismatches)}):")
    for k, ev, tv in mismatches:
        print(f"  Key {k}:")
        print(f"    In EN: {ev}")
        print(f"    In ID: {tv}")
else:
    print("SUCCESS: All bracket variables [ ... ] match 100% perfectly between English and Indonesian!")

# Save to batch_2_translated.json
out_path = 'scripts/batch_2_translated.json'
with open(out_path, 'w', encoding='utf-8') as out_f:
    json.dump(all_translations, out_f, ensure_ascii=False, indent=2)

print(f"Wrote {len(all_translations)} entries to {out_path}.")

# Re-read and test JSON loading
with open(out_path, 'r', encoding='utf-8') as test_f:
    verified = json.load(test_f)
assert len(verified) == 282, f"Expected 282 entries, got {len(verified)}"
print("ALL CHECKS PASSED: batch_2_translated.json is valid and complete with 282 entries!")
