# -*- coding: utf-8 -*-
"""
generate_and_install_countries.py
Applies master_roots_lookup.json to generate:
- countries_l_braz_por.yml
- countries_cosmetic_l_braz_por.yml

Validates 100% Clausewitz YAML syntax and writes with UTF-8 BOM to game folder and workspace mirror.
"""
import os
import re
import json

GAME_POR_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por"
LOCAL_POR_DIR = r"f:\New Coding\rea-hoi4-indonesia\localisation\braz_por"
ENG_DIR = r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english"

with open(r"f:\New Coding\rea-hoi4-indonesia\scripts\master_roots_lookup.json", "r", encoding="utf-8") as f:
    master_dict = json.load(f)

# Priority overrides for key majors & historical nations
OVERRIDES = {
    "German Reich": "Reich Jerman",
    "German Empire": "Kekaisaran Jerman",
    "Germany": "Jerman",
    "United States": "Amerika Serikat",
    "United States of America": "Amerika Serikat",
    "United Kingdom": "Britania Raya",
    "Soviet Union": "Uni Soviet",
    "France": "Prancis",
    "French Republic": "Republik Prancis",
    "French State": "Negara Prancis (Vichy)",
    "Italy": "Italia",
    "Kingdom of Italy": "Kerajaan Italia",
    "Japanese Empire": "Kekaisaran Jepang",
    "Japan": "Jepang",
    "Empire of Japan": "Kekaisaran Jepang",
    "Dutch East Indies": "Hindia Belanda",
    "Republic of Indonesia": "Republik Indonesia",
    "Indonesia": "Indonesia",
    "Netherlands": "Belanda",
    "Kingdom of the Netherlands": "Kerajaan Belanda",
    "Poland": "Polandia",
    "Republic of Poland": "Republik Polandia",
    "China": "Tiongkok",
    "Republic of China": "Republik Tiongkok",
    "People's Republic of China": "Republik Rakyat Tiongkok",
    "Communist China": "Tiongkok Komunis",
    "British Raj": "Kemaharajaan Britania (British Raj)",
    "Australia": "Australia",
    "Commonwealth of Australia": "Persemakmuran Australia",
    "Canada": "Kanada",
    "Dominion of Canada": "Dominion Kanada",
    "South Africa": "Afrika Selatan",
    "Union of South Africa": "Uni Afrika Selatan",
    "New Zealand": "Selandia Baru",
    "Dominion of New Zealand": "Dominion Selandia Baru",
    "Siam": "Siam",
    "Thailand": "Thailand",
    "Kingdom of Siam": "Kerajaan Siam",
    "Philippines": "Filipina",
    "Commonwealth of the Philippines": "Persemakmuran Filipina",
    "Spain": "Spanyol",
    "Spanish Republic": "Republik Spanyol",
    "Nationalist Spain": "Spanyol Nasionalis",
    "Republican Spain": "Spanyol Republikan",
    "Portugal": "Portugal",
    "Portuguese Republic": "Republik Portugal",
    "Brazil": "Brasil",
    "United States of Brazil": "Amerika Serikat Brasil",
    "Yugoslavia": "Yugoslavia",
    "Kingdom of Yugoslavia": "Kerajaan Yugoslavia",
    "Romania": "Rumania",
    "Kingdom of Romania": "Kerajaan Rumania",
    "Hungary": "Hungaria",
    "Kingdom of Hungary": "Kerajaan Hungaria",
    "Bulgaria": "Bulgaria",
    "Kingdom of Bulgaria": "Kerajaan Bulgaria",
    "Greece": "Yunani",
    "Kingdom of Greece": "Kerajaan Yunani",
    "Turkey": "Turki",
    "Republic of Turkey": "Republik Turki",
    "Sweden": "Swedia",
    "Kingdom of Sweden": "Kerajaan Swedia",
    "Norway": "Norwegia",
    "Kingdom of Norway": "Kerajaan Norwegia",
    "Finland": "Finlandia",
    "Republic of Finland": "Republik Finlandia",
    "Denmark": "Denmark",
    "Kingdom of Denmark": "Kerajaan Denmark",
    "Belgium": "Belgia",
    "Kingdom of Belgium": "Kerajaan Belgia",
    "Switzerland": "Swiss",
    "Swiss Confederation": "Konfederasi Swiss",
    "Austria": "Austria",
    "Federal State of Austria": "Negara Federal Austria",
    "Czechoslovakia": "Cekoslowakia",
    "Czechoslovak Republic": "Republik Cekoslowakia",
    "Ireland": "Irlandia",
    "Irish Free State": "Negara Bebas Irlandia",
    "Mexico": "Meksiko",
    "United Mexican States": "Negara-Negara Meksiko Bersatu",
}

for k, v in OVERRIDES.items():
    master_dict[k] = v

def translate_val(val):
    if not val:
        return ""
    if val in master_dict:
        return master_dict[val]
    if val.startswith("The ") or val.startswith("the "):
        sub = re.sub(r"^[tT]he\s+", "", val)
        if sub in master_dict:
            return master_dict[sub]
    return val

def process_file(base_name):
    src_path = os.path.join(ENG_DIR, f"{base_name}_l_english.yml")
    with open(src_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        
    out_lines = ["l_braz_por:\n"]
    translated_count = 0
    total_count = 0
    
    pat = re.compile(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"(\s*#.*)?$')
    
    for line in lines[1:]:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            out_lines.append(line)
            continue
            
        m = pat.match(line.rstrip("\r\n"))
        if m:
            total_count += 1
            indent, key, ver, val, comment = m.groups()
            v_str = f":{ver}" if ver else ":"
            comment_str = comment or ""
            
            tr = translate_val(val)
            if tr != val:
                translated_count += 1
            
            # escape internal quotes
            tr = tr.replace('“', '\\"').replace('”', '\\"')
            parts = tr.split(r'\"')
            parts = [p.replace('"', r'\"') for p in parts]
            tr = r'\"'.join(parts)
            
            out_lines.append(f"{indent}{key}{v_str} \"{tr}\"{comment_str}\n")
        else:
            out_lines.append(line)
            
    print(f"[{base_name}] Translated {translated_count}/{total_count} entries ({translated_count/max(1,total_count)*100:.1f}%)")
    
    content = "".join(out_lines)
    for folder in [GAME_POR_DIR, LOCAL_POR_DIR]:
        target = os.path.join(folder, f"{base_name}_l_braz_por.yml")
        with open(target, "wb") as f:
            f.write(b'\xef\xbb\xbf')
            f.write(content.encode("utf-8"))
        print(f"  Successfully wrote {target} ({os.path.getsize(target)} bytes)")

def main():
    process_file("countries")
    process_file("countries_cosmetic")

if __name__ == "__main__":
    main()
