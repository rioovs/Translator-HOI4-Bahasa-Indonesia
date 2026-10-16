# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
import json
import time

def translate_batch(texts, src='en', dest='id'):
    """
    Batches up to 30-40 texts into a single Google Translate request.
    Uses ' ||| ' as separator.
    """
    if not texts:
        return []
    
    separator = " ||| "
    joined = separator.join(texts)
    
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + src + '&tl=' + dest + '&dt=t&q=' + urllib.parse.quote(joined)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_tr = ''.join([p[0] for p in data[0] if p[0]])
                
                # Split back by separator (accounting for minor whitespace/case shifts)
                parts = raw_tr.split('|||')
                if len(parts) == len(texts):
                    return [p.strip() for p in parts]
                else:
                    # If separator got mangled, fallback to individual or return
                    print(f"[WARN] Batch split mismatch: expected {len(texts)}, got {len(parts)}")
                    return [p.strip() for p in parts]
        except Exception as e:
            print(f"[RETRY {attempt+1}] Error: {e}")
            time.sleep(2 * (attempt + 1))
            
    return texts

if __name__ == "__main__":
    sample = [
        "Bring Home the Exiled Republicans",
        "With our leader Eleftherios Venizelos finally back in charge, we can invite our comrades back from exile.",
        "Air Superiority",
        "Close Air Support",
        "Bomb enemy buildings, infrastructure and industry."
    ]
    res = translate_batch(sample)
    print("Test Results:")
    for orig, tr in zip(sample, res):
        print(f"  EN: {orig}\n  ID: {tr}\n")
