import sys
import json

filename = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

with open(filename, 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in range(start, min(end, len(data))):
    print(f"[{i}] {data[i]['key']}: \"{data[i]['en']}\"")
