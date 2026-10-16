# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

with open('scripts/country_base_id.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/adjectives_id.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

# Master manual overrides dictionary
OVERRIDES = {
    "German Reich": "Reich Jerman",
    "Socialist Republic of Germany": "Republik Sosialis Jerman",
    "German Republic": "Republik Jerman",
    "German Empire": "Kekaisaran Jerman",
    "United States": "Amerika Serikat",
    "United States of America": "Amerika Serikat",
    "Free American Empire": "Kekaisaran Amerika Bebas",
    "Communist States of America": "Negara-Negara Komunis Amerika",
    "Confederate States of America": "Negara-Negara Konfederasi Amerika",
    "United Kingdom": "Britania Raya",
    "British Empire": "Imperium Britania",
    "Union of Britain": "Uni Britania",
    "Great Britain": "Britania Raya",
    "Soviet Union": "Uni Soviet",
    "Russian Federation": "Federasi Rusia",
    "Russian Empire": "Kekaisaran Rusia",
    "Russian Soviet Federative Socialist Republic": "Republik Sosialis Federasi Soviet Rusia",
    "France": "Prancis",
    "French Republic": "Republik Prancis",
    "French Commune": "Komune Prancis",
    "French State": "Negara Prancis",
    "Bourbon France": "Prancis Bourbon",
    "Nation Française": "Bangsa Prancis",
    "Vichy France": "Prancis Vichy",
    "Free France": "Prancis Bebas",
    "Italy": "Italia",
    "Italian Republic": "Republik Italia",
    "Italian Union": "Uni Italia",
    "Kingdom of Italy": "Kerajaan Italia",
    "Italian Empire": "Kekaisaran Italia",
    "Japanese Empire": "Kekaisaran Jepang",
    "Empire of Japan": "Kekaisaran Jepang",
    "Netherlands": "Belanda",
    "Kingdom of Netherlands": "Kerajaan Belanda",
    "Dutch East Indies": "Hindia Belanda",
    "Republic of Indonesia": "Republik Indonesia",
    "Dominion of Indonesia": "Dominion Indonesia",
    "United States of Indonesia": "Republik Indonesia Serikat",
    "Netherlands-Indonesia Union": "Uni Belanda-Indonesia",
    "Defenders of the Homeland": "Pembela Tanah Air",
    "People's Democratic Front": "Front Demokrasi Rakyat",
    "Union of Indonesian Provinces": "Uni Provinsi Indonesia",
    "Federation of Malayan Peoples": "Federasi Rakyat Melayu",
    "Union of Malayan Peoples": "Uni Rakyat Melayu",
    "Malayan Empire": "Kekaisaran Melayu",
    "British Malaya": "Malaya Britania",
    "British Raj": "Kemaharajaan Britania",
    "Dominion of India": "Dominion India",
    "Republic of India": "Republik India",
    "Provisional Government of Free India": "Pemerintahan Sementara India Bebas",
    "Manchukuo": "Manchukuo",
    "Empire of Manchuria": "Kekaisaran Manchuria",
    "Mengkukuo": "Mengkukuo",
    "Republic of China": "Republik Tiongkok",
    "Chinese People's Republic": "Republik Rakyat Tiongkok",
    "Reorganized Nationalist China": "Pemerintahan Nasionalis Tiongkok Rekorganisasi",
    "Reorganized Government of China": "Pemerintahan Tiongkok Rekorganisasi",
    "Austria-Hungary": "Austria-Hongaria",
    "Austro-Hungarian Empire": "Kekaisaran Austria-Hongaria",
    "Holy Roman Empire": "Kekaisaran Romawi Suci",
    "Roman Empire": "Kekaisaran Romawi",
    "Byzantine Empire": "Kekaisaran Bizantium",
    "Ottoman Empire": "Kekaisaran Utsmaniyah",
    "Third Rome": "Roma Ketiga",
    "Iberian Union": "Uni Iberia",
    "Scandinavian Union": "Uni Skandinavia",
    "Scandinavia": "Skandinavia",
    "Benelux": "Benelux",
    "Benelux Federation": "Federasi Benelux",
    "European Union": "Uni Eropa",
    "Danubian Federation": "Federasi Donau",
    "Danubian Confederation": "Konfederasi Donau",
    "Gran Colombia": "Kolombia Raya",
    "United Provinces of Central America": "Provinsi Bersatu Amerika Tengah",
    "Central American Federation": "Federasi Amerika Tengah",
    "Arab Federation": "Federasi Arab",
    "United Arab Republic": "Republik Arab Bersatu",
    "Arab Union": "Uni Arab",
    "Polynesian Empire": "Kekaisaran Polinesia",
    "Pacific Federation": "Federasi Pasifik",
    "League of Nations": "Liga Bangsa-Bangsa",
    "Weimar Republic": "Republik Weimar",
    "Generalgouvernement": "Pemerintahan Umum (Generalgouvernement)",
    "Reichsprotektorat Böhmen-Mähren": "Protektorat Bohemia-Moravia",
}

def translate_word(w):
    if w in base_map:
        return base_map[w]
    if w in adj_map:
        return adj_map[w]
    return w

def translate_root(r):
    if r in OVERRIDES:
        return OVERRIDES[r]
    if r in base_map:
        return base_map[r]
    if r in adj_map:
        return adj_map[r]
    
    # Pure variable
    if re.match(r'^\$[A-Za-z0-9_]+\$$', r):
        return r
    
    # Overlord prefixes
    m = re.match(r'^\$OVERLORDADJ\$\s+Occupation Zone of (.*)$', r)
    if m:
        return f"Zona Pendudukan {translate_root(m.group(1))} $OVERLORDADJ$"
    if r == "$OVERLORDADJ$ Occupation Zone":
        return "Zona Pendudukan $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+Protectorate of (.*)$', r)
    if m:
        return f"Protektorat {translate_root(m.group(1))} $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+Mandate of (.*)$', r)
    if m:
        return f"Mandat {translate_root(m.group(1))} $OVERLORDADJ$"
    m = re.match(r'^\$OVERLORDADJ\$\s+(.*)$', r)
    if m:
        sub = m.group(1)
        if sub.startswith('$') and sub.endswith('$'):
            return f"$OVERLORDADJ$ {sub}"
        return f"$OVERLORDADJ$ {translate_root(sub)}"

    # Common political patterns
    pats = [
        (r'^Democratic People\'s Republic of (.*)$', 'Republik Rakyat Demokratik {}'),
        (r'^Socialist Republic of (.*)$', 'Republik Sosialis {}'),
        (r'^People\'s Republic of (.*)$', 'Republik Rakyat {}'),
        (r'^Democratic Republic of (.*)$', 'Republik Demokratik {}'),
        (r'^Federal Republic of (.*)$', 'Republik Federal {}'),
        (r'^Islamic Republic of (.*)$', 'Republik Islam {}'),
        (r'^Arab Republic of (.*)$', 'Republik Arab {}'),
        (r'^Soviet Socialist Republic of (.*)$', 'Republik Sosialis Soviet {}'),
        (r'^Soviet Republic of (.*)$', 'Republik Soviet {}'),
        (r'^Republic of (.*)$', 'Republik {}'),
        (r'^Free State of (.*)$', 'Negara Bebas {}'),
        (r'^Free City of (.*)$', 'Kota Bebas {}'),
        (r'^Grand Duchy of (.*)$', 'Keharyapatihan {}'),
        (r'^Duchy of (.*)$', 'Kadipaten {}'),
        (r'^Principality of (.*)$', 'Kepangeranan {}'),
        (r'^Sultanate of (.*)$', 'Kesultanan {}'),
        (r'^Emirate of (.*)$', 'Keamiran {}'),
        (r'^Caliphate of (.*)$', 'Kekhalifahan {}'),
        (r'^Commonwealth of (.*)$', 'Persemakmuran {}'),
        (r'^Federation of (.*)$', 'Federasi {}'),
        (r'^Confederation of (.*)$', 'Konfederasi {}'),
        (r'^Kingdom of (.*)$', 'Kerajaan {}'),
        (r'^Empire of (.*)$', 'Kekaisaran {}'),
        (r'^State of (.*)$', 'Negara {}'),
        (r'^Union of (.*)$', 'Uni {}'),
        (r'^Commune of (.*)$', 'Komune {}'),
        (r'^Protectorate of (.*)$', 'Protektorat {}'),
        (r'^Dominion of (.*)$', 'Dominion {}'),
        (r'^Autonomous Region of (.*)$', 'Wilayah Otonom {}'),
        (r'^Provisional Government of (.*)$', 'Pemerintahan Sementara {}'),
        (r'^Military Junta of (.*)$', 'Junta Militer {}'),
        (r'^Military Administration of (.*)$', 'Administrasi Militer {}'),
        (r'^Military Government of (.*)$', 'Pemerintahan Militer {}'),
        
        # Suffix patterns
        (r'^(.*) Soviet Socialist Republic$', 'Republik Sosialis Soviet {}'),
        (r'^(.*) Soviet Republic$', 'Republik Soviet {}'),
        (r'^(.*) People\'s Republic$', 'Republik Rakyat {}'),
        (r'^(.*) Socialist Republic$', 'Republik Sosialis {}'),
        (r'^(.*) Democratic Republic$', 'Republik Demokratik {}'),
        (r'^(.*) Free Republic$', 'Republik Bebas {}'),
        (r'^(.*) Republic$', 'Republik {}'),
        (r'^(.*) Kingdom$', 'Kerajaan {}'),
        (r'^(.*) Empire$', 'Kekaisaran {}'),
        (r'^(.*) Federation$', 'Federasi {}'),
        (r'^(.*) Confederation$', 'Konfederasi {}'),
        (r'^(.*) Union$', 'Uni {}'),
        (r'^(.*) Commune$', 'Komune {}'),
        (r'^(.*) Sultanate$', 'Kesultanan {}'),
        (r'^(.*) Emirate$', 'Keamiran {}'),
        (r'^(.*) Protectorate$', 'Protektorat {}'),
        (r'^(.*) Dominion$', 'Dominion {}'),
        
        # Prefixes
        (r'^Greater (.*)$', '{} Raya'),
        (r'^New (.*)$', '{} Baru'),
        (r'^United (.*)$', '{} Bersatu'),
        (r'^Free (.*)$', '{} Bebas'),
        (r'^Autonomous (.*)$', '{} Otonom'),
        (r'^Independent (.*)$', '{} Independen'),
        (r'^European (.*)$', '{} Eropa'),
    ]
    
    for pat, template in pats:
        m = re.match(pat, r, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            trans_sub = translate_root(sub)
            return template.format(trans_sub)
            
    return None

translated_count = 0
untranslated = []
for r in roots:
    res = translate_root(r)
    if res:
        translated_count += 1
    else:
        untranslated.append(r)

print(f"Total roots: {len(roots)}")
print(f"Translated by rules + overrides: {translated_count} ({translated_count/len(roots)*100:.1f}%)")
print(f"Untranslated: {len(untranslated)}")

with open('scripts/untranslated_roots.txt', 'w', encoding='utf-8') as out:
    for u in sorted(untranslated):
        out.write(u + '\n')
