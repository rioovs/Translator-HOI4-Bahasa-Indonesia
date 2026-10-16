# -*- coding: utf-8 -*-
import re

file_path = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\focus_l_braz_por.yml'
with open(file_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

english_stopwords = {
    'the', 'to', 'of', 'and', 'in', 'that', 'is', 'was', 'for', 'with', 
    'as', 'on', 'by', 'will', 'our', 'we', 'their', 'have', 'from', 'which',
    'this', 'be', 'are', 'not', 'an', 'at', 'or', 'by', 'all', 'would', 'should'
}

english_descs = []

for idx, line in enumerate(lines, 1):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = re.match(r'^([a-zA-Z0-9_]+_desc):\s*(?:0\s*)?\"(.*)\"$', s)
    if m:
        key, val = m.group(1), m.group(2)
        # Tokenize words
        words = re.findall(r'\b[a-zA-Z]+\b', val.lower())
        stop_count = sum(1 for w in words if w in english_stopwords)
        # If substantial portion or count of english stopwords
        if stop_count >= 3:
            english_descs.append({
                'line': idx,
                'key': key,
                'val': val,
                'stop_count': stop_count,
                'total_words': len(words)
            })
        elif stop_count >= 1 and len(words) <= 10 and any(w in ['the', 'and', 'with', 'for', 'our', 'will'] for w in words):
            # Check short descs
            english_descs.append({
                'line': idx,
                'key': key,
                'val': val,
                'stop_count': stop_count,
                'total_words': len(words)
            })

print(f"Total detected English descs: {len(english_descs)}")
# Check line distribution
print(f"First English desc at line {english_descs[0]['line']}: {english_descs[0]['key']}")
print(f"Last English desc at line {english_descs[-1]['line']}: {english_descs[-1]['key']}")

import json
with open('scripts/detected_english_descs.json', 'w', encoding='utf-8') as f:
    json.dump(english_descs, f, indent=2, ensure_ascii=False)
