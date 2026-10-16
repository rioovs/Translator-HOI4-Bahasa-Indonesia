# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import time
import urllib.request
import urllib.parse
from translate_wuw_engine import mask_text, unmask_text, TERMS_MAP

BATCH_FILES = {
    1: ('batch1_ah_hun', 'scripts/wuw_batches/batch1_ah_hun.json'),
    2: ('batch2_aus', 'scripts/wuw_batches/batch2_aus.json'),
    3: ('batch3_bel', 'scripts/wuw_batches/batch3_bel.json'),
    4: ('batch4_cog', 'scripts/wuw_batches/batch4_cog.json'),
    5: ('batch5_ger_part1', 'scripts/wuw_batches/batch5_ger_part1.json'),
    6: ('batch6_ger_part2', 'scripts/wuw_batches/batch6_ger_part2.json'),
}

def translate_multiline_chunk(chunk_items, client='dict-chrome-ex'):
    masked_data = []
    pure_vars = {}
    
    for item in chunk_items:
        k = item['key']
        v = item['val']
        v_str = v.strip()
        if not v_str or re.match(r'^\$[A-Za-z0-9_.-]+\$$', v_str):
            pure_vars[k] = v
        else:
            masked, tokens = mask_text(v)
            masked_data.append((k, masked, tokens, v))
            
    results = dict(pure_vars)
    if not masked_data:
        return results
        
    combined = "\n".join(m[1] for m in masked_data)
    clients = [client, 'dict-chrome-ex', 'gtx']
    success = False
    translated_lines = []
    
    for c in clients:
        url = f'https://translate.googleapis.com/translate_a/single?client={c}&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(combined)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_text = "".join([p[0] for p in data[0] if p[0]])
                lines = raw_text.strip().split("\n")
                if len(lines) == len(masked_data):
                    translated_lines = lines
                    success = True
                    break
        except Exception:
            pass
            
    if success:
        for (k, _, tokens, orig_v), tr_line in zip(masked_data, translated_lines):
            results[k] = unmask_text(tr_line, tokens)
    else:
        # Fallback to single item translation
        for k, masked, tokens, orig_v in masked_data:
            time.sleep(0.05)
            single_success = False
            for c in ['dict-chrome-ex', 'gtx']:
                url = f'https://translate.googleapis.com/translate_a/single?client={c}&sl=en&tl=id&dt=t&q=' + urllib.parse.quote(masked)
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        data = json.loads(resp.read().decode('utf-8'))
                        raw_text = "".join([p[0] for p in data[0] if p[0]])
                        results[k] = unmask_text(raw_text, tokens)
                        single_success = True
                        break
                except Exception:
                    continue
            if not single_success:
                results[k] = unmask_text(masked, tokens)
                
    return results

def process_batch(batch_num, chunk_size=15):
    if batch_num not in BATCH_FILES:
        print(f"Invalid batch number: {batch_num}")
        return
        
    b_name, b_path = BATCH_FILES[batch_num]
    out_path = f"scripts/wuw_batches/{b_name}_translated.json"
    
    with open(b_path, 'r', encoding='utf-8') as f:
        items = json.load(f)
        
    print(f"=== Starting {b_name} ({len(items)} items) ===")
    
    translated_map = {}
    if os.path.exists(out_path):
        try:
            with open(out_path, 'r', encoding='utf-8') as f:
                translated_map = json.load(f)
            print(f"Loaded existing: {len(translated_map)} items.")
        except Exception:
            translated_map = {}
            
    items_to_do = [item for item in items if item['key'] not in translated_map]
    print(f"Items to process: {len(items_to_do)}")
    
    if not items_to_do:
        print(f"Batch {batch_num} is already complete!")
        return
        
    start_time = time.time()
    total_to_do = len(items_to_do)
    processed = 0
    
    for i in range(0, total_to_do, chunk_size):
        chunk = items_to_do[i:i+chunk_size]
        chunk_res = translate_multiline_chunk(chunk)
        translated_map.update(chunk_res)
        processed += len(chunk)
        
        # Save progress
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(translated_map, f, ensure_ascii=False, indent=2)
            
        elapsed = time.time() - start_time
        pct = (len(translated_map) / len(items)) * 100
        print(f"[{b_name}] {len(translated_map)}/{len(items)} ({pct:.1f}%) in {elapsed:.1f}s")
        time.sleep(0.4)
        
    print(f"=== Completed {b_name}: {len(translated_map)} items saved to {out_path} ===")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        batch_id = int(sys.argv[1])
        process_batch(batch_id)
    else:
        print("Usage: python scripts/run_batch_translation.py <batch_num 1-6>")
