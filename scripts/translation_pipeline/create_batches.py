# -*- coding: utf-8 -*-
import json

with open('scripts/all_event_td_keys.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's split into 6 structured batches:
# Batch 1: news items 0 to 280
# Batch 2: news items 280 to end of news
# Batch 3: germany items
# Batch 4: soviet, war_justification, usa
# Batch 5: china, political, france, britain, italy, japan
# Batch 6: all remaining (generic, election, nuke, stability, spain, poland, finland, etc.)

news_items = [x for x in items if x['key'].startswith('news.')]
germany_items = [x for x in items if x['key'].startswith('germany.') or x['key'].startswith('AAT_germany.')]
b4_namespaces = ('soviet.', 'war_justification.', 'usa.')
b4_items = [x for x in items if any(x['key'].startswith(ns) for ns in b4_namespaces)]
b5_namespaces = ('china.', 'political.', 'france.', 'britain.', 'italy.', 'japan.')
b5_items = [x for x in items if any(x['key'].startswith(ns) for ns in b5_namespaces)]

handled_keys = set(x['key'] for x in news_items + germany_items + b4_items + b5_items)
b6_items = [x for x in items if x['key'] not in handled_keys]

b1_items = news_items[:285]
b2_items = news_items[285:]

batches = {
    'batch_1': b1_items,
    'batch_2': b2_items,
    'batch_3': germany_items,
    'batch_4': b4_items,
    'batch_5': b5_items,
    'batch_6': b6_items
}

for bname, bdata in batches.items():
    print(f"{bname}: {len(bdata)} items, words: {sum(len(x['en'].split()) for x in bdata)}")
    with open(f'scripts/{bname}_source.json', 'w', encoding='utf-8') as f:
        json.dump(bdata, f, ensure_ascii=False, indent=2)

print("All batch source files created.")
