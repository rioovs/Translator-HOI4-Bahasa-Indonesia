with open(r'f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\wtt_focus_l_braz_por.yml', 'r', encoding='utf-8-sig') as f:
    for l in f:
        if l.count('"') > 2:
            print(l.strip()[:80])
