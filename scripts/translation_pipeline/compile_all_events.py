# -*- coding: utf-8 -*-
import json
import re
import os
import subprocess

dst_game = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
dst_local = 'f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/events_l_braz_por.yml'
src_eng = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'

# Common option translations if not already translated
common_options = {
    "Interesting.": "Menarik.",
    "Interesting...": "Menarik...",
    "An interesting development.": "Sebuah perkembangan yang menarik.",
    "Excellent.": "Luar biasa.",
    "Great.": "Bagus.",
    "Very well.": "Baiklah.",
    "Understood.": "Dimengerti.",
    "Join": "Bergabung",
    "Refuse": "Tolak",
    "Never!": "Tidak akan pernah!",
    "Let them come!": "Biarkan mereka datang!",
    "United we are strong!": "Bersatu kita teguh!",
    "Send the ultimatum!": "Kirim ultimatum!",
    "Sign the treaty.": "Tandatangani perjanjian.",
    "Fools!": "Orang-orang bodoh!",
    "Stubborn fools.": "Orang-orang keras kepala yang bodoh.",
    "To War!": "Menuju Perang!",
    "We will never surrender!": "Kita tidak akan pernah menyerah!",
    "Death to the traitors!": "Kematian bagi para pengkhianat!",
    "For the Emperor!": "Demi Kaisar!",
    "Vive la France!": "Hidup Prancis! (Vive la France!)",
    "We had no choice.": "Kita tidak memiliki pilihan lain.",
    "We must stand firm": "Kita harus tetap teguh.",
    "A dark day.": "Hari yang kelam.",
    "An outrage!": "Keterlaluan!",
    "Curse them!": "Terkutuklah mereka!",
    "So be it.": "Biarlah demikian.",
    "Accept": "Terima",
    "Reject": "Tolak",
    "Agreed.": "Setuju.",
    "No deal!": "Tidak ada kesepakatan!",
    "Declare war!": "Nyatakan perang!",
    "Mobilize the army!": "Mobilisasi tentara!",
    "This means war!": "Ini berarti perang!",
    "A tragic loss.": "Kehilangan yang tragis.",
    "Good news!": "Kabar baik!"
}

def main():
    all_trans = {}
    missing_batches = []
    
    for i in range(1, 7):
        p = f'scripts/batch_{i}_translated.json'
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                b_data = json.load(f)
                all_trans.update(b_data)
                print(f"Loaded batch_{i}: {len(b_data)} keys")
        else:
            missing_batches.append(f"batch_{i}")

    print(f"Total translated keys loaded: {len(all_trans)}")
    if missing_batches:
        print(f"Waiting for batches: {', '.join(missing_batches)}")
        return False

    with open(src_eng, 'r', encoding='utf-8-sig') as f:
        src_lines = f.readlines()

    # Also load existing braz_por to preserve any button translations already made
    existing_braz = {}
    if os.path.exists(dst_local):
        with open(dst_local, 'r', encoding='utf-8-sig') as f:
            for l in f:
                m = re.match(r'^\s*([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', l)
                if m:
                    existing_braz[m.group(1)] = m.group(3)

    out_lines = ['\ufeffl_braz_por:\n']
    replaced_count = 0
    preserved_existing_count = 0
    option_trans_count = 0

    for i in range(1, len(src_lines)):
        line = src_lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            out_lines.append(line)
            continue

        m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', line)
        if not m:
            out_lines.append(line)
            continue

        indent, key, version, en_val = m.groups()
        ver_str = f":{version} " if version else ": "

        if key in all_trans:
            val = all_trans[key]
            replaced_count += 1
        elif key in existing_braz and existing_braz[key] != en_val:
            val = existing_braz[key]
            preserved_existing_count += 1
        elif en_val in common_options:
            val = common_options[en_val]
            option_trans_count += 1
        else:
            val = en_val

        # Escape internal double quotes if needed
        # Be careful: don't double escape already escaped \"
        # First normalize: replace \\\" with \" and unescaped " with \"
        # Safer regex for unescaped quote:
        parts = []
        # split by already escaped quote
        sub_tokens = re.split(r'(\\")', val)
        clean_tokens = []
        for t in sub_tokens:
            if t == '\\"':
                clean_tokens.append(t)
            else:
                clean_tokens.append(t.replace('"', '\\"'))
        val_clean = ''.join(clean_tokens)

        out_lines.append(f"{indent}{key}{ver_str}\"{val_clean}\"\n")

    content = ''.join(out_lines)

    # Save to both target locations
    with open(dst_game, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(dst_local, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Successfully wrote events_l_braz_por.yml to game and local!")
    print(f"Replaced event title/desc: {replaced_count}")
    print(f"Preserved existing translations: {preserved_existing_count}")
    print(f"Option common translations: {option_trans_count}")
    print(f"Total lines: {len(out_lines)}")

    # Run validation
    res = subprocess.run(['python', 'scripts/validate_events.py'], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    return True

if __name__ == '__main__':
    main()
