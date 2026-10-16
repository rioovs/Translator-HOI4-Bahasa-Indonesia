import re

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/wuw_events_l_english.yml'
with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

total_words = 0
total_chars = 0
for l in lines[1:]:
    s = l.strip()
    if not s or s.startswith('#'):
        continue
    # extract value inside first and last quotes
    idx_first = l.find('"')
    idx_last = l.rfind('"')
    if idx_first != -1 and idx_last > idx_first:
        val = l[idx_first+1:idx_last]
        total_words += len(val.split())
        total_chars += len(val)

print(f"Total words: {total_words}")
print(f"Total characters: {total_chars}")
