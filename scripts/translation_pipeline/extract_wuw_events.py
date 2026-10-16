import re
import json

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/wuw_events_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

items = []
pattern = re.compile(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*(#.*)?$')

for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = pattern.match(line)
    if m:
        key = m.group(1)
        ver = m.group(2)
        val = m.group(3)
        comment = m.group(4) or ''
        items.append({
            'line': idx,
            'key': key,
            'ver': ver,
            'en': val,
            'comment': comment
        })
    else:
        print(f"Warning: line {idx} did not match: {line}")

print(f"Extracted {len(items)} items.")
with open('scripts/wuw_events_raw.json', 'w', encoding='utf-8') as out:
    json.dump(items, out, indent=2, ensure_ascii=False)
