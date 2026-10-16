# -*- coding: utf-8 -*-
import json
import re

for filepath in [
    r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\focus_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
]:
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()

    english_stopwords = {
        'the', 'to', 'of', 'and', 'in', 'that', 'is', 'was', 'for', 'with', 
        'as', 'on', 'by', 'will', 'our', 'we', 'their', 'have', 'from', 'which',
        'this', 'be', 'are', 'not', 'an', 'at', 'or', 'would', 'should', 'can',
        'has', 'had', 'been', 'its', 'us', 'they', 'them', 'if', 'into', 'more'
    }

    all_english_descs = []

    for idx, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith('#'):
            continue
        if '_desc:' in s:
            idx_colon = s.find(':')
            key = s[:idx_colon].strip()
            val = s[idx_colon+1:].strip()
            if val.startswith('0 '):
                val = val[2:].strip()
            if val.startswith('"') and val.endswith('"'):
                val_unquoted = val[1:-1]
            else:
                val_unquoted = val
            
            if val_unquoted.startswith('$') and val_unquoted.endswith('$'):
                continue
            if not val_unquoted:
                continue
                
            words = re.findall(r'\b[a-zA-Z]+\b', val_unquoted.lower())
            eng_count = sum(1 for w in words if w in english_stopwords)
            
            if eng_count >= 2:
                all_english_descs.append({
                    'line': idx,
                    'key': key,
                    'val': val_unquoted,
                    'eng_count': eng_count
                })

    print(f"File: {filepath}")
    print(f"  Total lines: {len(lines)}")
    print(f"  Total English descs remaining: {len(all_english_descs)}")
    if all_english_descs:
        for it in all_english_descs:
            print(f"    L{it['line']} {it['key']}: {it['val']}")
