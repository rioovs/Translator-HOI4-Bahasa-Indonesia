import json
import re

source_path = 'scripts/batch_4_source.json'
target_path = 'scripts/batch_4_translated.json'

with open(source_path, 'r', encoding='utf-8') as f:
    source_items = json.load(f)

merged = {}
for i in range(1, 5):
    chunk_path = f'scripts/b4_chunks/trans_chunk_{i}.json'
    with open(chunk_path, 'r', encoding='utf-8') as f:
        chunk_data = json.load(f)
    print(f"Loaded chunk {i}: {len(chunk_data)} items")
    for k, v in chunk_data.items():
        if k in merged:
            print(f"WARNING: duplicate key {k}")
        merged[k] = v

print(f"Total merged keys: {len(merged)}")
print(f"Total source items: {len(source_items)}")

# 1. Check exact key count
assert len(merged) == len(source_items), f"Mismatch count: {len(merged)} vs {len(source_items)}"

# 2. Check each key exists and order
source_keys = [x['key'] for x in source_items]
for k in source_keys:
    assert k in merged, f"Missing key in translation: {k}"
    assert merged[k] and len(merged[k].strip()) > 0, f"Empty translation for key: {k}"

# 3. Tag and variable validation
tag_errors = 0
for item in source_items:
    k = item['key']
    en_val = item['en']
    id_val = merged[k]
    
    # check bracket tags e.g. [From.GetName], [?senators_support], etc.
    en_brackets = set(re.findall(r'\[.*?\]', en_val))
    id_brackets = set(re.findall(r'\[.*?\]', id_val))
    if en_brackets != id_brackets:
        print(f"Bracket tag mismatch in {k}:")
        print(f"  EN: {en_brackets}")
        print(f"  ID: {id_brackets}")
        tag_errors += 1
        
    # check dollar tags e.g. $SOV_iosif_stalin$
    en_dollars = set(re.findall(r'\$[A-Za-z0-9_]+\$', en_val))
    id_dollars = set(re.findall(r'\$[A-Za-z0-9_]+\$', id_val))
    if en_dollars != id_dollars:
        print(f"Dollar tag mismatch in {k}:")
        print(f"  EN: {en_dollars}")
        print(f"  ID: {id_dollars}")
        tag_errors += 1

    # check section colors e.g. §Y, §!
    en_sec = set(re.findall(r'§[A-Za-z!]', en_val))
    id_sec = set(re.findall(r'§[A-Za-z!]', id_val))
    if en_sec != id_sec:
        print(f"Section color tag mismatch in {k}:")
        print(f"  EN: {en_sec}")
        print(f"  ID: {id_sec}")
        tag_errors += 1

print(f"Tag validation completed. Total tag errors: {tag_errors}")
assert tag_errors == 0, f"There were {tag_errors} tag mismatches!"

# Save in identical key order as source
ordered_merged = {x['key']: merged[x['key']] for x in source_items}

with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(ordered_merged, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: Saved {target_path} with {len(ordered_merged)} entries.")
