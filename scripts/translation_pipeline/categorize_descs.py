# -*- coding: utf-8 -*-
import json
import re

with open('scripts/descs_to_translate.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

english_stopwords = {
    'the', 'to', 'of', 'and', 'in', 'that', 'is', 'was', 'for', 'with', 
    'as', 'on', 'by', 'will', 'our', 'we', 'their', 'have', 'from', 'which',
    'this', 'be', 'are', 'not', 'an', 'at', 'or', 'would', 'should', 'can',
    'has', 'had', 'been', 'its', 'us', 'they', 'them', 'if', 'into', 'more'
}

indonesian_stopwords = {
    'yang', 'dan', 'di', 'ke', 'dari', 'untuk', 'pada', 'dengan', 'adalah',
    'akan', 'kita', 'kami', 'ini', 'itu', 'bisa', 'dapat', 'oleh', 'harus',
    'telah', 'sudah', 'dalam', 'mereka', 'sebagai', 'tidak', 'juga', 'lebih'
}

english_items = []
indonesian_items = []
uncertain = []

for it in items:
    val = it['val']
    words = re.findall(r'\b[a-zA-Z]+\b', val.lower())
    eng_count = sum(1 for w in words if w in english_stopwords)
    id_count = sum(1 for w in words if w in indonesian_stopwords)
    
    if eng_count > id_count and eng_count >= 2:
        english_items.append(it)
    elif id_count > eng_count and id_count >= 2:
        indonesian_items.append(it)
    else:
        uncertain.append((it, eng_count, id_count))

print(f"Total: {len(items)}")
print(f"English: {len(english_items)}")
print(f"Indonesian: {len(indonesian_items)}")
print(f"Uncertain: {len(uncertain)}")

for u, ec, ic in uncertain:
    print(f"Uncertain: L{u['line']} {u['key']} (eng={ec}, id={ic}): {u['val']}")

with open('scripts/confirmed_english.json', 'w', encoding='utf-8') as f:
    json.dump(english_items + [u[0] for u in uncertain if u[1] > 0 or u[2] == 0], f, indent=2, ensure_ascii=False)
