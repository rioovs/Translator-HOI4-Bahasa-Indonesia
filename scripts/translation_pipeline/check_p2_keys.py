import json
import sys
sys.path.append('scripts')
from translate_taog_events_part2 import EVENTS_PART2

with open('scripts/events_part2_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

missing = [i for i in items if i['key'] not in EVENTS_PART2]
print(f"Part 2: Total {len(items)}, Translated in dict {len(EVENTS_PART2)}, Missing {len(missing)}")
for m in missing:
    print(f"{m['key']} | {m['en']}")
