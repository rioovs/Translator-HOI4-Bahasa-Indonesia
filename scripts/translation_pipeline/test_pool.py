# -*- coding: utf-8 -*-
import json
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

with open('scripts/wuw_batches/batch1_ah_hun.json', 'r', encoding='utf-8') as f:
    data = json.load(f)[:10]

def test_trans(item):
    val = item['val']
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(val)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            t = ''.join([p[0] for p in res[0] if p[0]])
            return item['key'], t
    except Exception as e:
        return item['key'], f"ERR: {e}"

start = time.time()
with ThreadPoolExecutor(max_workers=5) as ex:
    results = list(ex.map(test_trans, data))

elapsed = time.time() - start
print(f"Translated 10 items in {elapsed:.2f} seconds")
for k, t in results[:5]:
    print(f"  {k}: {t}")
