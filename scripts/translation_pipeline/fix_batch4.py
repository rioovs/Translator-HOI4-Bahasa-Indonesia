# -*- coding: utf-8 -*-
import json
import re
import time
import urllib.request
import urllib.parse
from translate_wuw_engine import mask_text, unmask_text

with open('scripts/wuw_batches/batch4_cog.json', 'r', encoding='utf-8') as f:
    src_items = {item['key']: item['val'] for item in json.load(f)}

with open('scripts/wuw_batches/batch4_cog_translated.json', 'r', encoding='utf-8') as f:
    tr_map = json.load(f)

# Find untranslated items (where tr_map[k] == src_items[k] and not pure var)
untrans_keys = [k for k, v in src_items.items() if tr_map.get(k) == v and not re.match(r'^\$[A-Za-z0-9_.-]+\$$', v.strip())]
print(f"Untranslated keys in batch 4: {len(untrans_keys)}")

def translate_multiline_chunk(chunk_keys):
    masked_data = []
    for k in chunk_keys:
        val = src_items[k]
        masked, tokens = mask_text(val)
        masked_data.append((k, masked, tokens))
        
    combined = "\n".join(m[1] for m in masked_data)
    
    clients = ['dict-chrome-ex', 'gtx']
    success = False
    translated_lines = []
    
    for client in clients:
        url = f'https://translate.googleapis.com/translate_a/single?client={client}&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(combined)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_text = "".join([p[0] for p in data[0] if p[0]])
                lines = raw_text.strip().split("\n")
                if len(lines) == len(chunk_keys):
                    translated_lines = lines
                    success = True
                    break
        except Exception as e:
            # print(f"Client {client} failed: {e}")
            pass
            
    if success:
        for (k, _, tokens), tr_line in zip(masked_data, translated_lines):
            tr_map[k] = unmask_text(tr_line, tokens)
    else:
        # Fall back to single item translation
        for k, masked, tokens in masked_data:
            time.sleep(0.1)
            url = f'https://translate.googleapis.com/translate_a/single?client=dict-chrome-ex&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    raw_text = "".join([p[0] for p in data[0] if p[0]])
                    tr_map[k] = unmask_text(raw_text, tokens)
            except Exception:
                tr_map[k] = unmask_text(masked, tokens)

# Process in chunks of 15
chunk_size = 15
for i in range(0, len(untrans_keys), chunk_size):
    chunk = untrans_keys[i:i+chunk_size]
    translate_multiline_chunk(chunk)
    time.sleep(0.5)
    print(f"Processed {min(i+chunk_size, len(untrans_keys))}/{len(untrans_keys)}")

with open('scripts/wuw_batches/batch4_cog_translated.json', 'w', encoding='utf-8') as f:
    json.dump(tr_map, f, ensure_ascii=False, indent=2)

same_now = sum(1 for k, v in src_items.items() if tr_map.get(k) == v and not re.match(r'^\$[A-Za-z0-9_.-]+\$$', v.strip()))
print(f"Remaining identical to source in Batch 4: {same_now}")
