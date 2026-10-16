import json

for i in range(1, 8):
    fname = f"wtt_events_chunk{i}.json"
    with open(fname, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, dict):
        print(f"{fname}: DICT with {len(data)} items")
    elif isinstance(data, list):
        print(f"{fname}: LIST with {len(data)} items, first element keys: {list(data[0].keys())}")
