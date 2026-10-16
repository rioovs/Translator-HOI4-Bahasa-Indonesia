# -*- coding: utf-8 -*-
"""
check_syntax_errors.py
Scans all .yml files in braz_por for:
1. Unclosed quotes (physical newlines inside quotes, missing closing quote).
2. Unescaped double quotes inside strings.
3. Leftover unreplaced tokens like __TK0___, ___TK0___, etc.
4. Header issues.
"""
import os
import re

GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"

def check_file(filepath):
    errors = []
    with open(filepath, 'r', encoding='utf-8-sig', errors='replace') as f:
        lines = f.readlines()
        
    for lno, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('l_'):
            continue
            
        # Leftover tokens check
        m_tk = re.search(r'_+TK\d+_+', stripped)
        if m_tk:
            errors.append((lno, f"LEFTOVER_TOKEN: {m_tk.group(0)} in: {stripped[:100]}"))
            
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*(.*)$', stripped)
        if not m:
            continue
        key, rest = m.groups()
        if not rest.startswith('"'):
            continue
            
        # Check if line ends with a closing quote (optionally followed by # comment)
        if not re.search(r'"(\s*#.*)?$', rest):
            errors.append((lno, f"UNCLOSED_QUOTE: {stripped[:100]}"))
            continue
            
        # Strip outer quotes and comments
        inner = rest[1:]
        inner = re.sub(r'"(\s*#.*)?$', '', inner)
        
        # Check for unescaped internal double quotes: any " not preceded by \
        unescaped = re.findall(r'(?<!\\)"', inner)
        if unescaped:
            errors.append((lno, f"UNESCAPED_QUOTE: found {len(unescaped)} unescaped quotes in: {stripped[:100]}"))
            
    return errors

def main():
    total_errors = 0
    files_with_errors = []
    
    for f in sorted(os.listdir(GAME_POR_DIR)):
        if not f.endswith('.yml'):
            continue
        p = os.path.join(GAME_POR_DIR, f)
        errs = check_file(p)
        if errs:
            total_errors += len(errs)
            files_with_errors.append((f, errs))
            
    print(f"Total files with errors: {len(files_with_errors)}")
    print(f"Total syntax/token errors: {total_errors}\n")
    
    for f, errs in files_with_errors:
        print(f"=== {f} ({len(errs)} errors) ===")
        for lno, msg in errs[:10]:
            print(f"  Line {lno}: {msg}")
        if len(errs) > 10:
            print(f"  ... and {len(errs)-10} more errors")

if __name__ == "__main__":
    main()
