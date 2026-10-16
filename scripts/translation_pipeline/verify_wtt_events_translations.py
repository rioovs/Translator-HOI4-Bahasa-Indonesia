# -*- coding: utf-8 -*-
import json
import re

total = {}
for i in [1, 2, 3, 4]:
    with open(f"wtt_events_chunk{i}.json", "r", encoding="utf-8") as f:
        total.update(json.load(f))
for i in [5, 6, 7]:
    with open(f"wtt_events_chunk{i}.json", "r", encoding="utf-8") as f:
        for item in json.load(f):
            total[item["key"]] = item["id"]

issues = []

for key, val in total.items():
    # 1. Physical newlines
    if '\n' in val or '\r' in val:
        # Check if they are raw newlines
        issues.append((key, "Contains raw physical newline"))
    
    # 2. Check internal unescaped quotes
    # Replace all escaped quotes \" first
    val_no_escaped = val.replace('\\"', '')
    if '"' in val_no_escaped:
        issues.append((key, f"Contains unescaped double quote: {val}"))
    
    # 3. Check bracket balance []
    open_b = val.count('[')
    close_b = val.count(']')
    if open_b != close_b:
        issues.append((key, f"Mismatched square brackets: {val}"))
        
    # 4. Check dollar sign count $$
    dollar_count = val.count('$')
    if dollar_count % 2 != 0:
        issues.append((key, f"Odd number of dollar signs: {val}"))

print(f"Total checked: {len(total)}")
print(f"Total issues found: {len(issues)}")
for k, iss in issues[:20]:
    print(f"  [{k}]: {iss}")
