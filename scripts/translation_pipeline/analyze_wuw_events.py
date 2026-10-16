import re

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/wuw_events_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

print('Total lines in source:', len(lines))

pattern = re.compile(r'^\s*([a-zA-Z0-9_\.\-]+):(\d*)\s*"(.*)"\s*$')
matches = []
comments_and_empty = 0
unmatched = []

for idx, line in enumerate(lines[1:], 2):
    s = line.strip()
    if not s or s.startswith('#'):
        comments_and_empty += 1
        continue
    m = pattern.match(line)
    if m:
        matches.append((m.group(1), m.group(2), m.group(3)))
    else:
        unmatched.append((idx, line))

print('Matched keys:', len(matches))
print('Comments and empty:', comments_and_empty)
print('Unmatched lines:', len(unmatched))
if unmatched:
    for u in unmatched[:10]:
        print('  Line', u[0], repr(u[1]))
