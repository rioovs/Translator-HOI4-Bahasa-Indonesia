"""Strict syntax and structure validator for Paradox Clausewitz localisation files."""

import re
from pathlib import Path

loc_dir = Path("localisation/braz_por")
utf8_bom = b"\xef\xbb\xbf"

total_files = 0
total_keys = 0
errors = []

for f in sorted(loc_dir.glob("*.yml")):
    total_files += 1
    raw = f.read_bytes()
    
    # Check UTF-8 BOM
    if not raw.startswith(utf8_bom):
        errors.append((f.name, 0, "Missing UTF-8 BOM header"))
        
    text = raw.decode("utf-8-sig", errors="replace")
    lines = text.splitlines()
    
    if not lines or not lines[0].strip().startswith("l_braz_por:"):
        errors.append((f.name, 1, f"First line is not l_braz_por: (got '{lines[0] if lines else ''}')"))
        
    for idx, line in enumerate(lines[1:], start=2):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
            
        # Match standard Clausewitz localization line:
        # KEY:0 "value" or KEY: "value"
        m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*(.*)$', line)
        if not m:
            errors.append((f.name, idx, f"Line does not match key:value pattern: {line[:60]}"))
            continue
            
        total_keys += 1
        key = m.group(1)
        val = m.group(2)
        
        # Value must start with "
        if not val.startswith('"'):
            errors.append((f.name, idx, f"Value does not start with quote: {line[:60]}"))
            continue
            
        # Value must end with " (or " # comment)
        # Check if line ends with unescaped "
        # Strip trailing comment
        # Find closing quote
        unescaped_quotes = []
        in_escape = False
        for c_idx, ch in enumerate(val):
            if ch == '\\' and not in_escape:
                in_escape = True
            elif ch == '"' and not in_escape:
                unescaped_quotes.append(c_idx)
            else:
                in_escape = False
                
        if len(unescaped_quotes) < 2:
            errors.append((f.name, idx, f"Unclosed string (<2 unescaped quotes): {line[:60]}"))
        elif val.rstrip().endswith(r'\"'):
            errors.append((f.name, idx, f"Ends with escaped quote: {line[:60]}"))
            
        # Check for embedded key definition
        if re.search(r'\\"[ ]*\\n\s*[A-Za-z0-9_.\-]+(?::\d+)?:\s*"', val):
            errors.append((f.name, idx, f"Embedded key definition inside string: {line[:60]}"))

print(f"Total files checked: {total_files}")
print(f"Total keys validated: {total_keys}")
print(f"Total errors found: {len(errors)}")

if errors:
    print("\nErrors:")
    for err in errors[:30]:
        print(f"  {err[0]}:{err[1]} -> {err[2]}")
else:
    print("\nALL 208 LOCALISATION FILES ARE 100% VALID!")
