import json

with open('scripts/taog_events_to_trans.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

series = {}
for idx, item in enumerate(items):
    k = item['key']
    prefix = k.split('.')[0]
    series[prefix] = series.get(prefix, 0) + 1

for s, count in sorted(series.items(), key=lambda x: -x[1]):
    print(f"{s}: {count} keys")
