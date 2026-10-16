import os

def search_terms(term, files):
    print(f"=== Searching for '{term}' ===")
    for f in files:
        if not os.path.exists(f):
            continue
        with open(f, 'r', encoding='utf-8-sig', errors='ignore') as fp:
            for line in fp:
                if term.lower() in line.lower():
                    print(f"[{os.path.basename(f)}] {line.strip()[:100]}")

target_files = [
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\intelligence_agencies_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\intel_ledger_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\traits_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\modifiers_l_braz_por.yml',
    r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\core_l_braz_por.yml',
]

search_terms('operative', target_files)
search_terms('spy', target_files)
search_terms('network', target_files)
search_terms('agency', target_files)
search_terms('decision', target_files)
