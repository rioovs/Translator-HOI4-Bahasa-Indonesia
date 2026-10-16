import re
import os

def check_multiline(fname):
    path = os.path.join(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english', fname)
    with open(path, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()
    
    multiline_entries = []
    in_entry = False
    cur_key = ""
    cur_start = 0
    
    for idx, line in enumerate(lines):
        line_str = line.rstrip('\r\n')
        if not in_entry:
            m = re.match(r'^\s*([A-Za-z0-9_\.\-]+):(\d*)\s*"(.*)', line_str)
            if m:
                rest = m.group(3)
                # Does it close on the same line?
                # Check for unescaped quote at end (ignoring trailing whitespace or comments)
                # Actually, check if rest has an unescaped ending quote
                # Let's see:
                clean_rest = re.sub(r'\s*#.*$', '', rest) # strip trailing comments
                # Check if ends with unescaped quote
                if not re.search(r'(?<!\\)(?:\\\\)*"$', clean_rest):
                    in_entry = True
                    cur_key = m.group(1)
                    cur_start = idx
        else:
            clean_line = re.sub(r'\s*#.*$', '', line_str)
            if re.search(r'(?<!\\)(?:\\\\)*"$', clean_line):
                in_entry = False
                multiline_entries.append((cur_key, cur_start, idx))
                
    print(f"{fname}: {len(multiline_entries)} multiline entries found.")
    for k, s, e in multiline_entries[:10]:
        print(f"  {k} lines {s+1}..{e+1}")

check_multiline('TAOG_events_l_english.yml')
check_multiline('TAOG_decisions_l_english.yml')
check_multiline('TAOG_focus_l_english.yml')
