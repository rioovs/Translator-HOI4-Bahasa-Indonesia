import re

def check_file(path):
    print("Checking", path)
    with open(path, 'r', encoding='utf-8-sig') as f:
        text = f.read()
    lines = text.splitlines()
    print("Header:", lines[0])
    non_matching = []
    keys = []
    for i, l in enumerate(lines[1:], 2):
        if not l.strip() or l.strip().startswith('#'):
            continue
        m = re.match(r'^\s*([A-Za-z0-9_\.]+)(?::\d*)?\s+"(.*)"\s*$', l)
        if not m:
            non_matching.append((i, l))
        else:
            keys.append((m.group(1), m.group(2)))
    print("Total parsed keys:", len(keys))
    print("Non matching lines:", len(non_matching))
    for i, l in non_matching[:10]:
        print(f"Line {i}: {repr(l)}")
    return keys

focus_keys = check_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_focus_l_english.yml')
event_keys = check_file(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_events_l_english.yml')
