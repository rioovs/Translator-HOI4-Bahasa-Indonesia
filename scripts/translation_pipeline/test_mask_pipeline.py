# -*- coding: utf-8 -*-
import json
import re
import urllib.request
import urllib.parse

def mask_text(text):
    tokens = []
    # Match order: escaped newlines, escaped quotes, script tags, variables, color tags, texticons
    pattern = re.compile(
        r'(\\n)|(\\")|(\[[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_.-]+)*\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)'
    )
    
    def repl(m):
        tok = m.group(0)
        idx = len(tokens)
        tokens.append(tok)
        return f" ___T{idx}___ "
        
    masked = pattern.sub(repl, text)
    return masked, tokens

def unmask_text(text, tokens):
    res = text
    for i, tok in enumerate(tokens):
        # Match ___T{i}___ with possible spaces
        ph = f"___T{i}___"
        res = res.replace(ph, tok)
        
    # Clean up spaces around formatting tags
    res = re.sub(r'§([A-Za-z])\s+', r'§\1', res)
    res = re.sub(r'\s+§!', '§!', res)
    res = re.sub(r'\[\s+', '[', res)
    res = re.sub(r'\s+\]', ']', res)
    res = re.sub(r'([a-zA-Z0-9])§([A-Za-z])', r'\1 §\2', res)
    res = re.sub(r'§!\s*([a-zA-Z0-9])', r'§! \1', res)
    res = re.sub(r'\s+', ' ', res).strip()
    return res

with open('scripts/wuw_batches/batch1_ah_hun.json', 'r', encoding='utf-8') as f:
    sample = json.load(f)[:10]

for item in sample:
    k = item['key']
    v = item['val']
    masked, tokens = mask_text(v)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        raw_tr = ''.join([p[0] for p in res[0] if p[0]])
    unmasked = unmask_text(raw_tr, tokens)
    print(f"KEY: {k}")
    print(f"  ORIG: {v}")
    print(f"  TRAN: {unmasked}\n")
