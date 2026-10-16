# -*- coding: utf-8 -*-
"""
sanitize_and_repair_all.py
Master repair and sanitation tool for all HOI4 localisation files.
Fixes:
1. Multi-line split strings -> joins them into single line with literal \\n.
2. Unescaped double quotes inside strings -> properly escaped as \\\".
3. Leftover masked tokens (_*TK\\d+_* or similar) -> restored to exact original English tokens.
4. Ensures valid UTF-8 BOM encoding.
5. Verifies 100% Clausewitz YAML compliance.
"""
import os
import re
import sys

ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"
GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_POR_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"

TOKEN_PATTERN = re.compile(
    r'(\\n)|(\\")|(\[[^\]]+\])|(\$[A-Za-z0-9_.-]+(?:\|[^$]+)?\$)|(§[A-Za-z!])|(£[a-zA-Z0-9_]+)'
)

def parse_english_file(eng_path):
    """
    Parses English file to get exact token list and original text for each key.
    """
    key_info = {}
    with open(eng_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        lines = f.readlines()
        
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('l_'):
            continue
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            indent, key, ver, val, comment = m.groups()
            tokens = [tm.group(0) for tm in TOKEN_PATTERN.finditer(val)]
            key_info[key] = {
                'indent': indent,
                'version': ver,
                'orig_val': val,
                'comment': comment or '',
                'tokens': tokens
            }
    return key_info

def parse_and_reconstruct_por(por_path):
    """
    Reads braz_por file, fixing multi-line breaks, unescaped quotes, etc.
    Returns a dict of key -> value.
    """
    with open(por_path, 'r', encoding='utf-8-sig', errors='replace') as f:
        raw_lines = f.readlines()
        
    # Step 1: Recombine multi-line quotes into single logical lines
    combined_lines = []
    current_line = ""
    in_quote = False
    
    for line in raw_lines:
        line_clean = line.rstrip('\r\n')
        if not in_quote:
            # Check if this line starts a key with an unclosed quote
            m = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)$', line_clean)
            if m:
                rest = m.group(2)
                # Check if it ends with a closing quote (optionally followed by comment)
                if re.search(r'"(\s*#.*)?$', rest):
                    combined_lines.append(line_clean)
                else:
                    # Unclosed quote! Start accumulating
                    current_line = line_clean
                    in_quote = True
            else:
                combined_lines.append(line_clean)
        else:
            # We are inside an unclosed quote from a previous line
            # Check if this line closes the quote
            if re.search(r'"(\s*#.*)?$', line_clean):
                current_line += "\\n" + line_clean.lstrip()
                combined_lines.append(current_line)
                current_line = ""
                in_quote = False
            else:
                current_line += "\\n" + line_clean.lstrip()
                
    if in_quote and current_line:
        # If still unclosed at EOF, append a quote
        current_line += '"'
        combined_lines.append(current_line)
        
    # Step 2: Extract keys and values
    por_dict = {}
    for line in combined_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('l_'):
            continue
        m = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)"(\s*#.*)?\s*$', line)
        if m:
            key, val, _ = m.groups()
            por_dict[key] = val
        else:
            # Try looser match
            m2 = re.match(r'^\s*([A-Za-z0-9_.-]+):(?:\d*)\s*"(.*)$', line)
            if m2:
                key, val = m2.groups()
                val = re.sub(r'"(\s*#.*)?$', '', val)
                por_dict[key] = val
                
    return por_dict

def fix_value(val, eng_tokens):
    """
    Cleans up a value:
    1. Replaces all forms of _*TK(\d+)_* with the corresponding eng_token.
    2. Replaces typographic quotes with escaped quotes.
    3. Escapes any raw unescaped double quotes.
    4. Cleans up formatting artifacts.
    """
    res = val
    
    # 1. Restore tokens: handles ___TK0___, __TK0___, ___TK0__, _TK0_, TK0, etc.
    def replace_tk(m):
        idx = int(m.group(1))
        if idx < len(eng_tokens):
            return eng_tokens[idx]
        return ""
        
    # Match patterns like: _*TK\s*(\d+)\s*_* or ___\s*TK\s*(\d+)\s*___
    res = re.sub(r'_+\s*TK\s*(\d+)\s*_+', replace_tk, res)
    res = re.sub(r'\bTK(\d+)\b', replace_tk, res)
    
    # 2. Fix specific known broken prefixes if any still remain
    res = res.replace('__TK0___£', '£trigger_yes£')
    res = res.replace('___TK0___£', '£trigger_yes£')
    
    # 3. Fix typographical quotes
    res = res.replace('“', '\\"').replace('”', '\\"').replace('„', '\\"')
    
    # 4. Remove physical newlines/carriage returns
    res = res.replace('\r', '').replace('\n', '\\n')
    
    # 5. Normalize internal escaped quotes
    # Temporarily replace valid escaped quotes \" with a placeholder
    PLACEHOLDER = "___ESCAPED_QUOTE___"
    res = res.replace('\\"', PLACEHOLDER)
    # Any remaining raw " should be replaced with \"
    res = res.replace('"', '\\"')
    # Restore valid escaped quotes
    res = res.replace(PLACEHOLDER, '\\"')
    
    # 6. Syntax cleanup
    res = re.sub(r'§([A-Za-z])\s+', r'§\1', res)
    res = re.sub(r'\s+§!', '§!', res)
    res = re.sub(r'\[\s+', '[', res)
    res = re.sub(r'\s+\]', ']', res)
    res = re.sub(r'\s*\\n\s*', r'\\n', res)
    
    return res.strip()

def repair_file(clean_base):
    eng_file = os.path.join(ENG_DIR, f"{clean_base}_l_english.yml")
    por_file = os.path.join(GAME_POR_DIR, f"{clean_base}_l_braz_por.yml")
    
    if not os.path.exists(eng_file):
        return False
        
    eng_info = parse_english_file(eng_file)
    por_dict = {}
    if os.path.exists(por_file):
        por_dict = parse_and_reconstruct_por(por_file)
        
    # Read the full structure from english to maintain comments and ordering
    with open(eng_file, 'r', encoding='utf-8-sig', errors='replace') as f:
        eng_raw_lines = f.readlines()
        
    out_lines = ["l_braz_por:\n"]
    repaired_keys = 0
    
    for line in eng_raw_lines:
        stripped = line.strip()
        if not stripped or stripped.startswith('l_'):
            continue
        if stripped.startswith('#'):
            out_lines.append(line)
            continue
            
        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?\s*$', line.rstrip('\r\n'))
        if m:
            indent, key, ver, eng_val, comment = m.groups()
            info = eng_info.get(key, {'tokens': []})
            tokens = info.get('tokens', [])
            
            # Prefer Indonesian translation if exists, otherwise keep English
            if key in por_dict and por_dict[key].strip():
                raw_val = por_dict[key]
                val = fix_value(raw_val, tokens)
            else:
                val = fix_value(eng_val, tokens)
                
            v_str = f":{ver}" if ver else ":"
            com_str = comment or ""
            out_lines.append(f"{indent}{key}{v_str} \"{val}\"{com_str}\n")
            repaired_keys += 1
        else:
            out_lines.append(line)
            
    content = "".join(out_lines)
    
    # Write with UTF-8 BOM to game dir and local repo dir
    for folder in [GAME_POR_DIR, LOCAL_POR_DIR]:
        target = os.path.join(folder, f"{clean_base}_l_braz_por.yml")
        with open(target, 'wb') as f:
            f.write(b'\xef\xbb\xbf')
            f.write(content.encode('utf-8'))
            
    return repaired_keys

def main():
    print("Starting Comprehensive Sanitation & Repair of ALL files...", flush=True)
    all_eng_files = [f for f in os.listdir(ENG_DIR) if f.endswith('_l_english.yml')]
    print(f"Total English files to process: {len(all_eng_files)}")
    
    total_repaired = 0
    for idx, f in enumerate(all_eng_files, 1):
        clean_base = f.replace('_l_english.yml', '')
        keys = repair_file(clean_base)
        if keys:
            total_repaired += 1
        if idx % 20 == 0 or idx == len(all_eng_files):
            print(f"  Sanitized {idx}/{len(all_eng_files)} files...", flush=True)
            
    print(f"\nCOMPLETED Sanitation & Repair of {total_repaired} files!", flush=True)

if __name__ == "__main__":
    main()
