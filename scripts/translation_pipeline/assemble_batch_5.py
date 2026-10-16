# -*- coding: utf-8 -*-
import json
import re

with open('scripts/batch_5_source.json', 'r', encoding='utf-8') as f:
    source_list = json.load(f)

with open('scripts/part1.json', 'r', encoding='utf-8') as f:
    p1 = json.load(f)
with open('scripts/part2.json', 'r', encoding='utf-8') as f:
    p2 = json.load(f)
with open('scripts/part3.json', 'r', encoding='utf-8') as f:
    p3 = json.load(f)
with open('scripts/part4.json', 'r', encoding='utf-8') as f:
    p4 = json.load(f)

merged = {}
merged.update(p1)
merged.update(p2)
merged.update(p3)
merged.update(p4)

print(f"Total merged entries: {len(merged)}")
assert len(merged) == len(source_list), f"Count mismatch: merged={len(merged)}, source={len(source_list)}"

tag_re = re.compile(r'\[[a-zA-Z0-9_.]+\]')
color_re = re.compile(r'§[a-zA-Z!]')
dollar_re = re.compile(r'\$[a-zA-Z0-9_]+\$')

errors = []

for idx, item in enumerate(source_list):
    key = item['key']
    if key not in merged:
        errors.append(f"Missing key in translation: {key}")
        continue
    
    trans_text = merged[key]
    src_text = item['en']
    
    if not trans_text or not trans_text.strip():
        errors.append(f"Empty translation for key: {key}")
    
    # Check bracket tags
    src_tags = sorted(tag_re.findall(src_text))
    trans_tags = sorted(tag_re.findall(trans_text))
    if src_tags != trans_tags:
        errors.append(f"Bracket tags mismatch in {key}:\n  Source: {src_tags}\n  Trans:  {trans_tags}")
        
    # Check color codes
    src_colors = sorted(color_re.findall(src_text))
    trans_colors = sorted(color_re.findall(trans_text))
    if src_colors != trans_colors:
        errors.append(f"Color tags mismatch in {key}:\n  Source: {src_colors}\n  Trans:  {trans_colors}")

    # Check dollar variables
    src_dollars = sorted(dollar_re.findall(src_text))
    trans_dollars = sorted(dollar_re.findall(trans_text))
    if src_dollars != trans_dollars:
        errors.append(f"Dollar tags mismatch in {key}:\n  Source: {src_dollars}\n  Trans:  {trans_dollars}")

if errors:
    print(f"Encountered {len(errors)} validation errors:")
    for err in errors:
        print(" -", err)
    raise SystemExit(1)
else:
    print("ALL 304 ENTRIES VALIDATED SUCCESSFULLY! Tags, colors, variables, and keys match 100%.")

out_path = 'scripts/batch_5_translated.json'
with open(out_path, 'w', encoding='utf-8') as out:
    json.dump(merged, out, indent=2, ensure_ascii=False)

print(f"Successfully written {out_path} with {len(merged)} items.")
