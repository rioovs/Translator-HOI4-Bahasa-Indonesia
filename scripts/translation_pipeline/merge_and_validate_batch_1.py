# -*- coding: utf-8 -*-
import json
import re

# Load source
with open('scripts/batch_1_source.json', 'r', encoding='utf-8') as f:
    source_items = json.load(f)

print(f"Total source items: {len(source_items)}")

# Load all 4 chunks
merged = {}
for i in range(1, 5):
    with open(f'scripts/b1_chunk_{i}_translated.json', 'r', encoding='utf-8') as cf:
        ch = json.load(cf)
        print(f"Chunk {i}: {len(ch)} items")
        merged.update(ch)

print(f"Total merged items: {len(merged)}")

source_keys = [x['key'] for x in source_items]
source_key_set = set(source_keys)
merged_key_set = set(merged.keys())

missing = source_key_set - merged_key_set
extra = merged_key_set - source_key_set

print(f"Missing keys: {len(missing)}")
if missing:
    print("Missing:", missing)

print(f"Extra keys: {len(extra)}")
if extra:
    print("Extra:", extra)

# Check for empty or None
empty_keys = [k for k, v in merged.items() if not v or not v.strip()]
print(f"Empty values: {len(empty_keys)}")
if empty_keys:
    print("Empty keys:", empty_keys)

# Verify tag preservation
bracket_tag_pattern = re.compile(r'\[[A-Za-z0-9_.:]+\]')
dollar_tag_pattern = re.compile(r'\$[A-Za-z0-9_.]+\$')
color_tag_pattern = re.compile(r'§[A-Za-z0-9!]+')

tag_issues = 0
for it in source_items:
    k = it['key']
    en = it['en']
    tr = merged.get(k, '')
    
    en_brackets = set(bracket_tag_pattern.findall(en))
    tr_brackets = set(bracket_tag_pattern.findall(tr))
    if en_brackets != tr_brackets:
        print(f"Bracket tag mismatch in {k}:")
        print(f"  EN: {en_brackets}")
        print(f"  TR: {tr_brackets}")
        tag_issues += 1
        
    en_dollars = set(dollar_tag_pattern.findall(en))
    tr_dollars = set(dollar_tag_pattern.findall(tr))
    if en_dollars != tr_dollars:
        print(f"Dollar tag mismatch in {k}:")
        print(f"  EN: {en_dollars}")
        print(f"  TR: {tr_dollars}")
        tag_issues += 1

print(f"Tag mismatches found: {tag_issues}")

# Write to batch_1_translated.json
with open('scripts/batch_1_translated.json', 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print("Saved batch_1_translated.json successfully.")
