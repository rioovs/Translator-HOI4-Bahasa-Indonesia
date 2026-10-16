import json
import sys
sys.path.append('scripts')
from translate_taog_focus_part1 import FOCUS_PART1

with open('scripts/focus_part1_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

missing = [i for i in items if i['key'] not in FOCUS_PART1]
print(f"Focus Part 1: Total {len(items)}, Translated in dict {len(FOCUS_PART1)}, Missing {len(missing)}")
for m in missing:
    print(f"{m['key']} | {m['en']}")
