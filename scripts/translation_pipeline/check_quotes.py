# -*- coding: utf-8 -*-
with open(r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wtt_events_l_english.yml', 'r', encoding='utf-8-sig') as f:
    for i, l in enumerate(f):
        s = l.strip()
        if not s or s.startswith('#'):
            continue
        first_q = s.find('"')
        last_q = s.rfind('"')
        if first_q != -1 and last_q > first_q:
            inner = s[first_q+1:last_q]
            if '"' in inner:
                print(f"Line {i}: {inner[:80]}")
