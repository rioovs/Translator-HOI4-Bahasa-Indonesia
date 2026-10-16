import re
import os

def validate_translation(src_path, dst_path):
    print(f'=== Validating {os.path.basename(dst_path)} ===')
    with open(src_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        src_lines = f.readlines()
    with open(dst_path, 'r', encoding='utf-8-sig', errors='ignore') as f:
        dst_lines = f.readlines()

    with open(dst_path, 'rb') as f:
        raw_head = f.read(3)
        assert raw_head == b'\xef\xbb\xbf', f"Missing UTF-8 BOM in {dst_path}!"
    assert dst_lines[0].strip() == 'l_braz_por:', f"Header is not l_braz_por: in {dst_path}"

    errors = []
    src_map = {}
    for line in src_lines[1:]:
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', line.strip())
        if m:
            key, ver, val = m.groups()
            src_map[key] = val

    dst_keys = set()
    for idx, line in enumerate(dst_lines[1:], 2):
        m = re.match(r'^\s*([a-zA-Z0-9_.\-]+):(\d*)\s*"(.*)"\s*$', line.strip())
        if m:
            key, ver, val = m.groups()
            dst_keys.add(key)
            if key not in src_map:
                errors.append(f'Line {idx}: Key {key} not found in source!')
                continue
            src_val = src_map[key]

            # Check variables $...$
            src_vars = sorted(re.findall(r'\$[a-zA-Z0-9_|^%0-9+~.-]+\$', src_val))
            dst_vars = sorted(re.findall(r'\$[a-zA-Z0-9_|^%0-9+~.-]+\$', val))
            if src_vars != dst_vars:
                errors.append(f'Line {idx} ({key}): Variables mismatch!\n  src: {src_vars}\n  dst: {dst_vars}')

            # Check icons £...
            src_icons = sorted(re.findall(r'£[a-zA-Z0-9_]+', src_val))
            dst_icons = sorted(re.findall(r'£[a-zA-Z0-9_]+', val))
            if src_icons != dst_icons:
                errors.append(f'Line {idx} ({key}): Icons mismatch!\n  src: {src_icons}\n  dst: {dst_icons}')

            # Check color tags count
            src_colors = re.findall(r'§[a-zA-Z0-9!+-]', src_val)
            dst_colors = re.findall(r'§[a-zA-Z0-9!+-]', val)
            if len(src_colors) != len(dst_colors):
                errors.append(f'Line {idx} ({key}): Color tags count mismatch!\n  src: {src_colors}\n  dst: {dst_colors}')

    missing_keys = set(src_map.keys()) - dst_keys
    if missing_keys:
        errors.append(f'Missing keys: {len(missing_keys)}: {list(missing_keys)[:5]}')

    if errors:
        print(f'Found {len(errors)} issues:')
        for e in errors[:10]:
            print(' ', e)
        return False
    else:
        print(f'SUCCESS! All {len(dst_keys)} keys validated perfectly.')
        return True

if __name__ == '__main__':
    src = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\designer_l_english.yml'
    dst1 = r'F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\designer_l_braz_por.yml'
    dst2 = r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\designer_l_braz_por.yml'
    validate_translation(src, dst1)
    validate_translation(src, dst2)
