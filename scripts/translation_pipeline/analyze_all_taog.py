import re
import os

def parse_hoi4_loc(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    entries = []
    # In HOI4 localisation, line format is:
    #   KEY:0 "Text..."
    # or KEY: "Text..."
    # Multi-line text can occur if a string doesn't end with '"'
    i = 0
    while i < len(lines):
        line = lines[i]
        # check for entry start
        m = re.match(r'^\s*([A-Za-z0-9_\.\-]+):(\d*)\s*"(.*)', line.rstrip('\r\n'))
        if m:
            key = m.group(1)
            version = m.group(2)
            content = m.group(3)
            start_line = i
            # Check if content ends with unescaped quote
            # Count trailing backslashes before ending quote if any
            # Or loop until line ends with '"' (and not '\"')
            while True:
                # check if line ends with unescaped quote:
                # regex: (?<!\\)(\\\\)*"$
                if re.search(r'(?<!\\)(?:\\\\)*"$', content):
                    # remove trailing quote
                    content = re.sub(r'"$', '', content)
                    break
                else:
                    i += 1
                    if i < len(lines):
                        content += "\n" + lines[i].rstrip('\r\n')
                    else:
                        break
            entries.append({
                'key': key,
                'version': version,
                'content': content,
                'start_line': start_line,
                'end_line': i
            })
        i += 1
    return entries

for name in ['TAOG_events_l_english.yml', 'TAOG_decisions_l_english.yml', 'TAOG_focus_l_english.yml']:
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', name)
    entries = parse_hoi4_loc(path)
    print(f"=== {name} ===")
    print(f"Total entries: {len(entries)}")
    
    # Categorize by prefix / topic
    prefixes = {}
    for e in entries:
        k = e['key']
        p = k.split('_')[0].split('.')[0]
        prefixes[p] = prefixes.get(p, 0) + 1
    print("Top prefixes:", sorted(prefixes.items(), key=lambda x: -x[1])[:10])

