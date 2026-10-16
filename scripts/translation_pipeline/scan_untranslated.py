# -*- coding: utf-8 -*-
import os
import glob
import re

por_dir = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
eng_dir = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

files = glob.glob(os.path.join(por_dir, "*_l_braz_por.yml"))
untranslated_files = []

eng_words = set(['the', 'and', 'with', 'for', 'this', 'that', 'our', 'their', 'when', 'will', 'from', 'have', 'been', 'which'])

for f in files:
    base = os.path.basename(f)
    try:
        with open(f, 'r', encoding='utf-8-sig', errors='ignore') as fp:
            content = fp.read()
    except Exception:
        continue
    
    vals = re.findall(r':\d*\s*\"(.*)\"', content)
    if not vals:
        continue
    
    total_words = 0
    eng_count = 0
    for v in vals:
        words = re.findall(r'[a-zA-Z]+', v.lower())
        total_words += len(words)
        for w in words:
            if w in eng_words:
                eng_count += 1
                
    if total_words > 50:
        ratio = eng_count / total_words
        if ratio > 0.08:
            untranslated_files.append((base, ratio, len(vals)))

print(f"Total braz_por files checked: {len(files)}")
print(f"Files with high English ratio (>8% stop words): {len(untranslated_files)}")
for b, r, n in sorted(untranslated_files, key=lambda x: -x[1]):
    print(f"  {b:38} | Eng ratio: {r*100:4.1f}% | Total keys: {n}")
