# -*- coding: utf-8 -*-
import json
import time
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor

with open('scripts/wuw_batches/batch1_ah_hun.json', 'r', encoding='utf-8') as f:
    sample = json.load(f)[:50]

def fetch_one(item):
    val = item['val']
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(val[:300])
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return True, None
    except Exception as e:
        return False, str(e)

start = time.time()
with ThreadPoolExecutor(max_workers=10) as ex:
    results = list(ex.map(fetch_one, sample))

elapsed = time.time() - start
successes = sum(1 for r in results if r[0])
failures = sum(1 for r in results if not r[0])
print(f"50 requests in {elapsed:.2f}s: {successes} succeeded, {failures} failed")
