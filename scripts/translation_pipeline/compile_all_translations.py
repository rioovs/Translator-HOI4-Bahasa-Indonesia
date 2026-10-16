# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

with open('scripts/vocab.json', 'r', encoding='utf-8') as f:
    vocab = json.load(f)

with open('scripts/all_explicit_final.json', 'r', encoding='utf-8') as f:
    explicit = json.load(f)

with open('scripts/missing_739_dict.json', 'r', encoding='utf-8') as f:
    missing_dict = json.load(f)
    explicit.update(missing_dict)

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    all_roots = [line.strip() for line in f if line.strip()]

# Core translation function
def translate_entity(text):
    if not text:
        return ""
    t = text.strip()
    
    # 1. Direct dictionaries
    if t in explicit:
        return explicit[t]
    if t in base_map:
        return base_map[t]
    if t in adj_map:
        return adj_map[t]
    if t in vocab:
        return vocab[t]
    if re.match(r'^\$[A-Za-z0-9_]+\$$', t):
        return t
        
    # 2. Definite article stripping
    if t.startswith('the ') or t.startswith('The '):
        sub = re.sub(r'^[tT]he\s+', '', t)
        return translate_entity(sub)
        
    # 3. Overlord structures
    if t == "$OVERLORDADJ$ Occupation Zone":
        return "Zona Pendudukan $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+Occupation Zone of (.*)$', t)
    if m:
        return f"Zona Pendudukan {translate_entity(m.group(1))} $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+Protectorate of (.*)$', t)
    if m:
        return f"Protektorat {translate_entity(m.group(1))} $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+Mandate of (.*)$', t)
    if m:
        return f"Mandat {translate_entity(m.group(1))} $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+(.*)$', t)
    if m:
        sub = m.group(1).strip()
        if sub.startswith('$') and sub.endswith('$'):
            return f"$OVERLORDADJ$ {sub}"
        return f"$OVERLORDADJ$ {translate_entity(sub)}"

    # 4. Conjunction 'and'
    if ' and ' in t:
        parts = t.split(' and ')
        # Translate each part
        trans_parts = [translate_entity(p) for p in parts]
        if all(trans_parts):
            return " dan ".join(trans_parts)

    # 5. Hyphenated compound names (e.g. Austria-Hungary, Finno-Russian)
    if '-' in t and ' ' not in t:
        parts = t.split('-')
        trans_parts = [translate_entity(p) for p in parts]
        if all(trans_parts):
            return "-".join(trans_parts)

    # 6. Compound patterns with 'of'
    # Pattern: [Prefix] of (the) [Rest]
    # e.g., "Socialist Republic of X", "Kingdom of X", "Commonwealth of X"
    m = re.match(r'^(.*?)\s+of\s+(?:the\s+)?(.*)$', t, re.IGNORECASE)
    if m:
        head, tail = m.group(1).strip(), m.group(2).strip()
        head_tr = translate_entity(head)
        tail_tr = translate_entity(tail)
        if head_tr and tail_tr:
            return f"{head_tr} {tail_tr}"

    # 7. Prefix modifiers
    # e.g. "Greater X" -> "X Raya", "New X" -> "X Baru", "Free X" -> "X Bebas"
    prefix_pats = [
        (r'^Greater\s+(.*)$', '{} Raya'),
        (r'^Great\s+(.*)$', '{} Besar'),
        (r'^New\s+(.*)$', '{} Baru'),
        (r'^Old\s+(.*)$', '{} Lama'),
        (r'^Free\s+(.*)$', '{} Bebas'),
        (r'^United\s+(.*)$', '{} Bersatu'),
        (r'^Autonomous\s+(.*)$', '{} Otonom'),
        (r'^Independent\s+(.*)$', '{} Independen'),
        (r'^Provisional\s+(.*)$', '{} Sementara'),
        (r'^Revolutionary\s+(.*)$', '{} Revolusioner'),
        (r'^Socialist\s+(.*)$', '{} Sosialis'),
        (r'^Communist\s+(.*)$', '{} Komunis'),
        (r'^Democratic\s+(.*)$', '{} Demokratis'),
        (r'^Nationalist\s+(.*)$', '{} Nasionalis'),
        (r'^Federal\s+(.*)$', '{} Federal'),
        (r'^Confederated\s+(.*)$', '{} Konfederasi'),
        (r'^Imperial\s+(.*)$', '{} Kekaisaran'),
        (r'^Royal\s+(.*)$', '{} Kerajaan'),
        (r'^Grand\s+(.*)$', '{} Agung'),
        (r'^Little\s+(.*)$', '{} Kecil'),
        (r'^Upper\s+(.*)$', '{} Hulu'),
        (r'^Lower\s+(.*)$', '{} Hilir'),
        (r'^Northern\s+(.*)$', '{} Utara'),
        (r'^Southern\s+(.*)$', '{} Selatan'),
        (r'^Eastern\s+(.*)$', '{} Timur'),
        (r'^Western\s+(.*)$', '{} Barat'),
        (r'^North\s+(.*)$', '{} Utara'),
        (r'^South\s+(.*)$', '{} Selatan'),
        (r'^East\s+(.*)$', '{} Timur'),
        (r'^West\s+(.*)$', '{} Barat'),
        (r'^Central\s+(.*)$', '{} Tengah'),
        (r'^European\s+(.*)$', '{} Eropa'),
        (r'^Asian\s+(.*)$', '{} Asia'),
        (r'^African\s+(.*)$', '{} Afrika'),
        (r'^American\s+(.*)$', '{} Amerika'),
        (r'^Pacific\s+(.*)$', '{} Pasifik'),
        (r'^Baltic\s+(.*)$', '{} Baltik'),
        (r'^Nordic\s+(.*)$', '{} Nordik'),
        (r'^Alpine\s+(.*)$', '{} Alpen'),
        (r'^Danubian\s+(.*)$', '{} Donau'),
        (r'^British\s+(.*)$', '{} Britania'),
        (r'^French\s+(.*)$', '{} Prancis'),
        (r'^German\s+(.*)$', '{} Jerman'),
        (r'^Italian\s+(.*)$', '{} Italia'),
        (r'^Spanish\s+(.*)$', '{} Spanyol'),
        (r'^Portuguese\s+(.*)$', '{} Portugal'),
        (r'^Dutch\s+(.*)$', '{} Belanda'),
        (r'^Russian\s+(.*)$', '{} Rusia'),
        (r'^Soviet\s+(.*)$', '{} Soviet'),
        (r'^Japanese\s+(.*)$', '{} Jepang'),
        (r'^Chinese\s+(.*)$', '{} Tiongkok'),
        (r'^Austrian\s+(.*)$', '{} Austria'),
        (r'^Polish\s+(.*)$', '{} Polandia'),
        (r'^Bundesstaat\s+(.*)$', 'Negara Bagian {}'),
        (r'^Volkskommissariat\s+(.*)$', 'Komisariat Rakyat {}'),
        (r'^Reichsprotektorat\s+(.*)$', 'Protektorat Reich {}'),
        (r'^Reichsland\s+(.*)$', 'Reichsland {}'),
    ]
    for p_pat, p_temp in prefix_pats:
        m = re.match(p_pat, t, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            sub_tr = translate_entity(sub)
            if sub_tr:
                return p_temp.format(sub_tr)

    # 8. Suffix entities
    # e.g. "X Republic" -> "Republik X", "X Empire" -> "Kekaisaran X"
    suffix_pats = [
        (r'^(.*)\s+Autonomous Soviet Socialist Republic$', 'Republik Sosialis Soviet Otonom {}'),
        (r'^(.*)\s+Autonomous SSR$', 'RSS Otonom {}'),
        (r'^(.*)\s+Independent SSR$', 'RSS Independen {}'),
        (r'^(.*)\s+Soviet Socialist Republic$', 'Republik Sosialis Soviet {}'),
        (r'^(.*)\s+Soviet Republic$', 'Republik Soviet {}'),
        (r'^(.*)\s+SSR$', 'RSS {}'),
        (r'^(.*)\s+People\'s Republic$', 'Republik Rakyat {}'),
        (r'^(.*)\s+Socialist Republic$', 'Republik Sosialis {}'),
        (r'^(.*)\s+Democratic Republic$', 'Republik Demokratik {}'),
        (r'^(.*)\s+Free Republic$', 'Republik Bebas {}'),
        (r'^(.*)\s+Republic$', 'Republik {}'),
        (r'^(.*)\s+Kingdom$', 'Kerajaan {}'),
        (r'^(.*)\s+Empire$', 'Kekaisaran {}'),
        (r'^(.*)\s+Federation$', 'Federasi {}'),
        (r'^(.*)\s+Confederation$', 'Konfederasi {}'),
        (r'^(.*)\s+Confederacy$', 'Konfederasi {}'),
        (r'^(.*)\s+Commonwealth$', 'Persemakmuran {}'),
        (r'^(.*)\s+Community$', 'Komunitas {}'),
        (r'^(.*)\s+Union$', 'Uni {}'),
        (r'^(.*)\s+Commune$', 'Komune {}'),
        (r'^(.*)\s+Sultanate$', 'Kesultanan {}'),
        (r'^(.*)\s+Emirate$', 'Keamiran {}'),
        (r'^(.*)\s+Caliphate$', 'Kekhalifahan {}'),
        (r'^(.*)\s+Khanate$', 'Kekhanan {}'),
        (r'^(.*)\s+Khaganate$', 'Kekhaganatan {}'),
        (r'^(.*)\s+Protectorate$', 'Protektorat {}'),
        (r'^(.*)\s+Dominion$', 'Dominion {}'),
        (r'^(.*)\s+State$', 'Negara {}'),
        (r'^(.*)\s+Unitary State$', 'Negara Kesatuan {}'),
        (r'^(.*)\s+Realm$', 'Alam {}'),
        (r'^(.*)\s+Clique$', 'Klik {}'),
        (r'^(.*)\s+League$', 'Liga {}'),
        (r'^(.*)\s+Council$', 'Dewan {}'),
        (r'^(.*)\s+Junta$', 'Junta {}'),
        (r'^(.*)\s+Host$', 'Pasukan {}'),
        (r'^(.*)\s+Territories$', 'Teritori {}'),
        (r'^(.*)\s+Territory$', 'Teritori {}'),
        (r'^(.*)\s+Colony$', 'Koloni {}'),
        (r'^(.*)\s+Colonies$', 'Koloni-Koloni {}'),
        (r'^(.*)\s+Directorate$', 'Direktorat {}'),
        (r'^(.*)\s+Regency$', 'Keregenan {}'),
        (r'^(.*)\s+Chiefdom$', 'Kedatuan {}'),
        (r'^(.*)\s+Government$', 'Pemerintahan {}'),
        (r'^(.*)\s+Administration$', 'Administrasi {}'),
        (r'^(.*)\s+Authority$', 'Otoritas {}'),
        (r'^(.*)\s+Region$', 'Wilayah {}'),
        (r'^(.*)\s+Autonomous Region$', 'Wilayah Otonom {}'),
        (r'^(.*)\s+Autonomous District$', 'Distrik Otonom {}'),
        (r'^(.*)\s+Autonomous Territory$', 'Teritori Otonom {}'),
        (r'^(.*)\s+Governorate$', 'Kegubernuran {}'),
        (r'^(.*)\s+Province$', 'Provinsi {}'),
        (r'^(.*)\s+Okrug$', 'Okrug {}'),
        (r'^(.*)\s+National Okrug$', 'Okrug Nasional {}'),
        (r'^(.*)\s+Autonomous Okrug$', 'Okrug Otonom {}'),
        (r'^(.*)\s+Collective$', 'Kolektif {}'),
        (r'^(.*)\s+Cooperative$', 'Koperasi {}'),
        (r'^(.*)\s+Monarchy$', 'Monarki {}'),
        (r'^(.*)\s+Communion$', 'Komuni {}'),
    ]
    for s_pat, s_temp in suffix_pats:
        m = re.match(s_pat, t, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            sub_tr = translate_entity(sub)
            if sub_tr:
                return s_temp.format(sub_tr)

    # 9. Multi-word phrase translation fallback (translating each constituent word)
    words = t.split()
    if len(words) > 1:
        w_trs = []
        all_ok = True
        for w in words:
            wt = translate_entity(w)
            if wt:
                w_trs.append(wt)
            else:
                all_ok = False
                break
        if all_ok:
            return " ".join(w_trs)

    return None

master_dict = {}
still_missing = []

for r in all_roots:
    res = translate_entity(r)
    if res:
        master_dict[r] = res
    else:
        still_missing.append(r)

print(f"Total roots: {len(all_roots)}")
print(f"Translated: {len(master_dict)} ({len(master_dict)/len(all_roots)*100:.2f}%)")
print(f"Still missing: {len(still_missing)}")

with open('scripts/master_roots_lookup.json', 'w', encoding='utf-8') as out:
    json.dump(master_dict, out, ensure_ascii=False, indent=2)
print("Saved master_roots_lookup.json successfully!")
