# -*- coding: utf-8 -*-
import re

with open('scripts/trans_wtt_events_chunk6.py', 'r', encoding='utf-8') as f:
    text = f.read()

keys = re.findall(r'"([a-zA-Z0-9_.-]+)":', text)
print('Total keys in chunk 6:', len(keys))
print('Last 5 keys in chunk 6:', keys[-5:])
