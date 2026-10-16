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

print(f"Total merged keys: {len(total)}")

src_path = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_events_l_english.yml"
with open(src_path, "r", encoding="utf-8-sig") as f:
    lines = f.readlines()

print(f"Source file total lines: {len(lines)}")
print(f"Header: {repr(lines[0])}")

matched = 0
unmatched_keys = []
for idx, l in enumerate(lines[1:], 2):
    s = l.strip()
    if not s or s.startswith("#"):
        continue
    m = re.match(r'^(\s*)([A-Za-z0-9_\.]+)(:(\d*))?\s+"(.*)"\s*$', l)
    if m:
        key = m.group(2)
        if key in total:
            matched += 1
        else:
            unmatched_keys.append((idx, key))
    else:
        print(f"Non-matching line {idx}: {repr(l)}")

print(f"Matched keys in source: {matched}")
if unmatched_keys:
    print(f"Unmatched keys ({len(unmatched_keys)}): {unmatched_keys[:10]}")
