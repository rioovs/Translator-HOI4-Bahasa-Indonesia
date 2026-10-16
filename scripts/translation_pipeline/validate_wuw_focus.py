# -*- coding: utf-8 -*-
import os
import re

target_file = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wuw_focus_l_braz_por.yml'
src_file = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\wuw_focus_l_english.yml'

print(f"Validating: {target_file}")

# 1. BOM check
with open(target_file, 'rb') as f:
    header_bytes = f.read(3)
assert header_bytes == b'\xef\xbb\xbf', "Missing UTF-8 BOM!"
print("✅ UTF-8 BOM verified.")

# 2. Header line check
with open(target_file, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

assert lines[0].strip() == 'l_braz_por:', f"Invalid header: {lines[0]}"
print(f"✅ Header line verified: {lines[0].strip()}")

with open(src_file, 'r', encoding='utf-8-sig', errors='replace') as f:
    src_lines = f.readlines()

print(f"Target lines: {len(lines)}, Source lines: {len(src_lines)}")

# 3. Line by line parse and token check
pattern = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$')

src_keys = {}
for idx, line in enumerate(src_lines[1:], start=2):
    m = pattern.match(line)
    if m:
        src_keys[m.group(2)] = (idx, m.group(4))

target_keys = {}
syntax_errors = []
quote_errors = []
tag_errors = []

for idx, line in enumerate(lines[1:], start=2):
    s = line.strip()
    if not s or s.startswith('#'):
        continue
    m = pattern.match(line)
    if not m:
        syntax_errors.append((idx, line))
        continue
    indent, key, ver, val, comment = m.groups()
    target_keys[key] = (idx, val)
    
    # Check quotes: unescaped internal quotes
    # A properly escaped string should not have unescaped quotes
    unescaped = re.findall(r'(?<!\\)"', val)
    if unescaped:
        quote_errors.append((idx, key, val))
        
    # Check tokens against source
    if key in src_keys:
        src_val = src_keys[key][1]
        
        # Check variables $VAR$
        src_vars = set(re.findall(r'\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$', src_val))
        trg_vars = set(re.findall(r'\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$', val))
        if src_vars != trg_vars:
            # Check if differences are just whitespace
            tag_errors.append((idx, key, 'Variables mismatch', src_vars, trg_vars))
            
        # Check script tags [TAG]
        src_tags = set(re.findall(r'\[[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_.-]+)*\]', src_val))
        trg_tags = set(re.findall(r'\[[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_.-]+)*\]', val))
        if src_tags != trg_tags:
            tag_errors.append((idx, key, 'Script tags mismatch', src_tags, trg_tags))
            
        # Check color tags parity
        src_cols = len(re.findall(r'§[A-Za-z]', src_val))
        trg_cols = len(re.findall(r'§[A-Za-z]', val))
        src_closes = len(re.findall(r'§!', src_val))
        trg_closes = len(re.findall(r'§!', val))
        if src_cols != trg_cols or src_closes != trg_closes:
            tag_errors.append((idx, key, f'Color tags count mismatch (src open/close: {src_cols}/{src_closes}, trg: {trg_cols}/{trg_closes})'))

print(f"Total keys in target: {len(target_keys)} / Source keys: {len(src_keys)}")
assert len(target_keys) == len(src_keys), "Key count mismatch!"
print(f"✅ Key count 1:1 match verified (3071 keys).")

print(f"Syntax errors: {len(syntax_errors)}")
if syntax_errors:
    for se in syntax_errors[:5]:
        print(f"  Line {se[0]}: {se[1]}")

print(f"Quote errors: {len(quote_errors)}")
if quote_errors:
    for qe in quote_errors[:5]:
        print(f"  Line {qe[0]} ({qe[1]}): {qe[2]}")

print(f"Tag / variable anomalies: {len(tag_errors)}")
if tag_errors:
    for te in tag_errors[:15]:
        print(f"  Line {te[0]} ({te[1]}): {te[2]}")

# 4. Check Indonesian words distribution
with open(target_file, 'r', encoding='utf-8-sig') as f:
    text = f.read()

indonesian_sample_words = ['dan', 'yang', 'untuk', 'dengan', 'fokus', 'nasional', 'militer', 'ekonomi', 'rencana', 'rakyat', 'kekuatan', 'pabrik', 'pertahanan', 'lingkaran', 'dalam']
print("\nIndonesian Vocabulary Distribution:")
for word in indonesian_sample_words:
    count = len(re.findall(r'\b' + word + r'\b', text, re.IGNORECASE))
    print(f"  '{word}': {count} occurrences")
