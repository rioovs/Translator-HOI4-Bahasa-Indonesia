# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import re

test_str = 'Is either §Y[AUS.GetNameDef]§! or §Y[HUN.GetNameDef]§! and has any §YAustro-Hungarian Contingent State§! as their subject.'

# Test different token placeholders
patterns = [
    ('XZX{i}XZX', r'XZX\d+XZX'),
    ('___NUM{i}___', r'___NUM\d+___'),
    ('QZX{i}', r'QZX\d+'),
]

tokens = re.findall(r'§[A-Za-z!]|\[[^\]]+\]', test_str)
print("Tokens found:", tokens)

for placeholder_fmt, placeholder_re in patterns:
    masked = test_str
    # Replace each token
    for i, tok in enumerate(tokens):
        masked = masked.replace(tok, placeholder_fmt.format(i=i), 1)
    
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            trans = ''.join([part[0] for part in data[0] if part[0]])
            print(f"\nFormat {placeholder_fmt}:")
            print("  Masked:    ", masked)
            print("  Translated:", trans)
            
            # Unmask
            unmasked = trans
            for i, tok in enumerate(tokens):
                ph = placeholder_fmt.format(i=i)
                # handle possible spaces introduced around placeholder
                unmasked = re.sub(r'\s*' + re.escape(ph) + r'\s*', tok, unmasked)
            print("  Unmasked:  ", unmasked)
    except Exception as e:
        print("Error:", e)
