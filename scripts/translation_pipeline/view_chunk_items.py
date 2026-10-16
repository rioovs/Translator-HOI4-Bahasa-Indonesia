import json

def show(chunk_idx, start, end):
    with open(f'scripts/chunks/chunk_{chunk_idx}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for i in range(start, min(end, len(data))):
        item = data[i]
        print(f"[{i}] {item['key']}")
        print(item['en'])
        print("-" * 50)

if __name__ == '__main__':
    import sys
    c = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    s = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    e = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    show(c, s, e)
