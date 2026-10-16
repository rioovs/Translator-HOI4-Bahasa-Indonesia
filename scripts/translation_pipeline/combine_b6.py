# -*- coding: utf-8 -*-
import json
import re

# Load all chunk translation files
chunks = []
for i in range(5):
    with open(f'scripts/b6_trans_{i}.json', 'r', encoding='utf-8') as f:
        chunks.append(json.load(f))

combined = {}
for c in chunks:
    combined.update(c)

print(f"Total combined entries: {len(combined)}")

# Load original source
with open('scripts/batch_6_source.json', 'r', encoding='utf-8') as f:
    source_items = json.load(f)

source_keys = [x['key'] for x in source_items]
source_dict = {x['key']: x['en'] for x in source_items}

print(f"Total source items: {len(source_items)}")

# Verification checks
missing_keys = set(source_keys) - set(combined.keys())
extra_keys = set(combined.keys()) - set(source_keys)

if missing_keys:
    print(f"ERROR: Missing keys ({len(missing_keys)}): {missing_keys}")
else:
    print("SUCCESS: 0 missing keys.")

if extra_keys:
    print(f"ERROR: Extra keys ({len(extra_keys)}): {extra_keys}")
else:
    print("SUCCESS: 0 extra keys.")

# Check empty strings
empty_keys = [k for k, v in combined.items() if not v.strip()]
print(f"Empty translation keys: {empty_keys}")
for ek in empty_keys:
    print(f"  Source for {ek}: '{source_dict.get(ek)}'")

# Check dynamic tags preservation
tag_regex = re.compile(r'\[[A-Za-z0-9_\.\?\:]+\]|\$[A-Za-z0-9_]+\$|§[A-Za-z0-9!]+')
tag_mismatches = 0
for k in source_keys:
    src_text = source_dict[k]
    trans_text = combined[k]
    src_tags = set(tag_regex.findall(src_text))
    trans_tags = set(tag_regex.findall(trans_text))
    if src_tags != trans_tags:
        # Check if difference is intentional or issue
        print(f"Tag diff in {k}:")
        print(f"  Source tags: {src_tags}")
        print(f"  Trans tags:  {trans_tags}")
        tag_mismatches += 1

print(f"Tag mismatch count: {tag_mismatches}")

# Save to target file
target_path = 'scripts/batch_6_translated.json'
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print(f"Saved {len(combined)} translated entries to {target_path}")
