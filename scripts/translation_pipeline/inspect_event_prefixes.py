import re
from collections import Counter

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/wuw_events_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

prefixes = Counter()
key_data = []

# Pattern allowing trailing comments
pattern = re.compile(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$')

for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        key = m.group(1)
        version = m.group(2)
        val = m.group(3)
        comment = m.group(4) or ''
        parts = key.split('.')
        prefix = parts[0] if len(parts) > 1 else key.split('_')[0]
        prefixes[prefix] += 1
        key_data.append((idx, key, version, val, comment))
    else:
        print(f"Failed match at {idx}: {line}")

print(f"Total keys extracted: {len(key_data)}")
print("Prefix distribution:")
for p, c in prefixes.most_common(30):
    print(f"  {p}: {c}")
