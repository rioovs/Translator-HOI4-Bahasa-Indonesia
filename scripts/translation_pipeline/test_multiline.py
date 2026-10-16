# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json

lines = [
    "An Expansionist State",
    "Great Military Chiefs",
    "Bananas are the lifeblood of our nation.",
    "Unify East Africa",
    "Our great Tutsi warriors helped defend the realm."
]

combined = "\n".join(lines)
url = 'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(combined)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

with urllib.request.urlopen(req, timeout=10) as resp:
    res = json.loads(resp.read().decode('utf-8'))
    translated_full = "".join([p[0] for p in res[0] if p[0]])
    print("Combined result:")
    print(repr(translated_full))
    split_lines = translated_full.strip().split("\n")
    print("\nLine by line (count:", len(split_lines), "):")
    for orig, tr in zip(lines, split_lines):
        print(f"  {orig} -> {tr}")
