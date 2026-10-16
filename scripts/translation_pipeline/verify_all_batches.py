# -*- coding: utf-8 -*-
import json
import sys

from trans_batch1_can_misc import translations_batch1
from trans_batch2_saf import translations_batch2
from trans_batch3_nzl import translations_batch3
from trans_batch4_raj import translations_batch4
from trans_batch5_usa import translations_batch5

all_trans = {}
for name, b in [
    ('batch1', translations_batch1),
    ('batch2', translations_batch2),
    ('batch3', translations_batch3),
    ('batch4', translations_batch4),
    ('batch5', translations_batch5),
]:
    print(f"{name}: {len(b)} items")
    for k, v in b.items():
        if k in all_trans:
            print(f"DUPLICATE KEY: {k}")
        all_trans[k] = v

print(f"Total merged translations: {len(all_trans)}")

with open('scripts/all_english_descs.json', 'r', encoding='utf-8') as f:
    needed = json.load(f)

needed_keys = {it['key'] for it in needed}
print(f"Total needed keys: {len(needed_keys)}")

missing = needed_keys - set(all_trans.keys())
extra = set(all_trans.keys()) - needed_keys

print(f"Missing keys: {len(missing)}")
if missing:
    for m in missing:
        print(f"  Missing: {m}")

print(f"Extra keys: {len(extra)}")
if extra:
    for e in extra:
        print(f"  Extra: {e}")

if not missing and not extra:
    print("SUCCESS: Exact 1:1 match with all 335 English descriptions!")
