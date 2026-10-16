# -*- coding: utf-8 -*-
import json
import re
import os
from trans_chunk_1 import TRANS_CHUNK_1
from trans_chunk_2 import TRANS_CHUNK_2
from trans_chunk_3 import TRANS_CHUNK_3
from test_nat_trans import translate_nat_value

# Combine generic dictionaries
GENERIC_TRANS = {}
GENERIC_TRANS.update(TRANS_CHUNK_1)
GENERIC_TRANS.update(TRANS_CHUNK_2)
GENERIC_TRANS.update(TRANS_CHUNK_3)

with open('scripts/parsed_ship_modules.json', 'r', encoding='utf-8') as f:
    parsed_data = json.load(f)

out_lines = ['\ufeffl_braz_por:\n']

total_keys = 0
translated_count = 0
retained_model_count = 0

for item in parsed_data:
    if item['type'] == 'comment_or_empty':
        raw = item['raw']
        # If line contains commented out ITA line, let's keep it or translate it cleanly
        if '#ITA_ship_armor_cruiser_2:' in raw:
            out_lines.append(' #ITA_ship_armor_cruiser_2: "Sabuk 24mm/Geladak 20mm"\n')
        else:
            out_lines.append(raw)
        continue
    
    total_keys += 1
    key = item['key']
    val = item['value']
    indent = item['indent']
    version = item['version']
    comment = item['comment']
    ver_str = f":{version} " if version else ": "
    
    # Translate
    if key in GENERIC_TRANS:
        new_val = GENERIC_TRANS[key]
        translated_count += 1
    else:
        new_val = translate_nat_value(key, val)
        if new_val != val:
            translated_count += 1
        else:
            retained_model_count += 1
    
    # Ensure quotes inside string are escaped properly
    # Check if there are unescaped double quotes
    # Replace any literal newlines with \\n
    clean_val = new_val.replace('\r\n', '\\n').replace('\n', '\\n')
    
    # Check quotes: if string has unescaped quotes like "foo "bar" baz" -> "foo \"bar\" baz"
    # But if string already has \" keep it
    # We can do this cleanly:
    def escape_internal_quotes(s):
        parts = []
        i = 0
        while i < len(s):
            if s[i] == '"':
                if i > 0 and s[i-1] == '\\':
                    parts.append('"')
                else:
                    parts.append('\\"')
            else:
                parts.append(s[i])
            i += 1
        return ''.join(parts)
        
    clean_val = escape_internal_quotes(clean_val)
    
    out_lines.append(f"{indent}{key}{ver_str}\"{clean_val}\"{comment}\n")

content = ''.join(out_lines)

# Write to target paths
p1 = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\ship_modules_l_braz_por.yml'
p2 = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\ship_modules_l_braz_por.yml'

with open(p1, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Written to {p1}")

with open(p2, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Written to {p2}")

print(f"Total lines: {len(out_lines)}")
print(f"Total keys processed: {total_keys}")
print(f"Translated / transformed keys: {translated_count}")
print(f"Retained historical designations: {retained_model_count}")
