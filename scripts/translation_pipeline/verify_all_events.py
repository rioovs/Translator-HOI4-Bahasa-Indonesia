import json
import sys
sys.path.append('scripts')
from translate_taog_events_part1 import EVENTS_PART1
from translate_taog_events_part2 import EVENTS_PART2
from translate_taog_events_part3 import EVENTS_PART3

all_events_dict = {}
all_events_dict.update(EVENTS_PART1)
all_events_dict.update(EVENTS_PART2)
all_events_dict.update(EVENTS_PART3)

with open('scripts/taog_events_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

missing = [i['key'] for i in items if i['key'] not in all_events_dict]
print(f"Total events in file: {len(items)}")
print(f"Total events in combined dict: {len(all_events_dict)}")
print(f"Missing: {len(missing)}")
if missing:
    print("Missing sample:", missing[:10])
