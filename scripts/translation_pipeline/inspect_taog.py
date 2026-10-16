import re

def analyze(filename):
    path = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\\' + filename
    with open(path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    entries = re.findall(r'^\s*([A-Za-z0-9_]+):\d*\s*"(.*)"', content, flags=re.MULTILINE)
    print(f'=== {filename} ===')
    print('Total matched entries:', len(entries))
    tags = {}
    for k, v in entries:
        prefix = k.split('_')[0]
        tags[prefix] = tags.get(prefix, 0) + 1
    for p, c in sorted(tags.items(), key=lambda x: -x[1])[:20]:
        print(f'  {p}: {c}')

analyze('TAOG_events_l_english.yml')
analyze('TAOG_decisions_l_english.yml')
analyze('TAOG_focus_l_english.yml')
