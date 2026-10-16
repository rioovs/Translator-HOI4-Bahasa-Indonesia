import json

def examine(name, filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"=== {name} ({len(data)} items) ===")
    for i in range(min(15, len(data))):
        print(f"  {data[i]['key']}: {data[i]['val'][:70]}")
    print("...")
    for i in range(max(0, len(data)-10), len(data)):
        print(f"  {data[i]['key']}: {data[i]['val'][:70]}")

examine("DECISIONS", "scripts/decisions.json")
examine("OPERATIVES", "scripts/operatives.json")
examine("LAR_OPERATIONS", "scripts/lar_operations.json")
