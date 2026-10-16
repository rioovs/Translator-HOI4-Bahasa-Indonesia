import json

with open('scripts/focus_part5_extracted.json', 'r', encoding='utf-8') as f:
    p5 = json.load(f)

with open('scripts/focus_part6_extracted.json', 'r', encoding='utf-8') as f:
    p6 = json.load(f)

print(f"Part 5 count: {len(p5)}, Part 6 count: {len(p6)}")

# Let's see how many items have keys ending in _desc vs titles
p5_titles = [x for x in p5 if not x['key'].endswith('_desc')]
p5_descs = [x for x in p5 if x['key'].endswith('_desc')]
print(f"P5 titles: {len(p5_titles)}, P5 descs: {len(p5_descs)}")

p6_titles = [x for x in p6 if not x['key'].endswith('_desc')]
p6_descs = [x for x in p6 if x['key'].endswith('_desc')]
print(f"P6 titles: {len(p6_titles)}, P6 descs: {len(p6_descs)}")
