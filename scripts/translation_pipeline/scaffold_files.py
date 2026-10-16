"""
Script untuk membuat kerangka file lokalisasi braz_por dari file English.
Ini hanya copy + rename header, TANPA terjemahan - file-file akan diterjemahkan secara manual/batch.
"""
import os
import shutil
import re

ENGLISH_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"
OUTPUT_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"

os.makedirs(OUTPUT_DIR, exist_ok=True)

count = 0
for filename in os.listdir(ENGLISH_DIR):
    if not filename.endswith("_l_english.yml"):
        continue
    
    new_filename = filename.replace("_l_english.yml", "_l_braz_por.yml")
    src_path = os.path.join(ENGLISH_DIR, filename)
    dst_path = os.path.join(OUTPUT_DIR, new_filename)
    
    with open(src_path, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Replace ONLY the header line (first line)
    # l_english: -> l_braz_por:
    content = content.replace("l_english:", "l_braz_por:", 1)
    
    # Write with UTF-8 BOM (required by HOI4)
    with open(dst_path, 'w', encoding='utf-8-sig') as f:
        f.write(content)
    
    count += 1
    print(f"Created: {new_filename}")

print(f"\nTotal files created: {count}")
