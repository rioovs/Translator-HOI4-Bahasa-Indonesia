# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    roots = [line.strip() for line in f if line.strip()]

with open('scripts/country_base_id.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/adjectives_id.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

# Add missing 40 tags
extra_bases = {
    "Altai": "Altai", "Kalmykia": "Kalmykia", "Karelia": "Karelia", "Crimea": "Krimea",
    "Tatarstan": "Tatarstan", "Chechen-Ingush": "Chechnya-Ingushetia", "Dagestan": "Dagestan",
    "Buryatia": "Buryatia", "Far Eastern": "Timur Jauh", "Chukotka": "Chukotka", "Sakha": "Sakha",
    "Vladivostok": "Vladivostok", "Karakalpakstan": "Karakalpakstan", "Taymyria": "Taymyr",
    "Yamalian": "Yamalia", "Ostyak-Vogul": "Ostyak-Vogul", "Nenetsia": "Nenetsia", "Komi": "Komi",
    "Abkhazia": "Abkhazia", "Kabardino-Balkarian": "Kabardino-Balkaria", "North Ossetia": "Ossetia Utara",
    "Volga Germany": "Jerman Volga", "Bashkortostan": "Bashkortostan", "Bukhara": "Bukhara",
    "Khiva": "Khiva", "Chuvashia": "Chuvashia", "Mari El": "Mari El", "Udmurtia": "Udmurtia",
    "Rif": "Rif", "Harar": "Harar", "Tigray": "Tigray", "Afar": "Afar", "Benishangul-Gumuz": "Benishangul-Gumuz",
    "Gambela": "Gambela", "Sidamo": "Sidama", "Oromo": "Oromo", "Qwara": "Qwara", "Khakassia": "Khakassia"
}
base_map.update(extra_bases)

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

ALL_PATTERNS = [
    (r'^\$OVERLORDADJ\$\s+Occupation Zone of (.*)$', 'Zona Pendudukan {} $OVERLORDADJ$'),
    (r'^\$OVERLORDADJ\$\s+Protectorate of (.*)$', 'Protektorat {} $OVERLORDADJ$'),
    (r'^\$OVERLORDADJ\$\s+Mandate of (.*)$', 'Mandat {} $OVERLORDADJ$'),
    (r'^\$OVERLORDADJ\$\s+(.*)$', '$OVERLORDADJ$ {}'),
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
    (r'^Bundesstaat (.*)$', 'Negara Bagian {}'),
    (r'^Volkskommissariat (.*)$', 'Komisariat Rakyat {}'),
    (r'^Danubian State of (?:the )?(.*)$', 'Negara Donau {}'),
    (r'^Danubian State (.*)$', 'Negara Donau {}'),
    (r'^Province of (?:the )?(.*)$', 'Provinsi {}'),
    (r'^(.*) Clique$', 'Klik {}'),
    (r'^(.*) Unitary State$', 'Negara Kesatuan {}'),
    (r'^(.*) Khanate$', 'Kekhanan {}'),
    (r'^Khanate of (.*)$', 'Kekhanan {}'),
    (r'^Governorate of (.*)$', 'Kegubernuran {}'),
    (r'^(.*) SSR$', 'Republik Sosialis Soviet {}'),
    (r'^(.*) Nation$', 'Bangsa {}'),
    (r'^(.*) Council$', 'Dewan {}'),
    (r'^(.*) League$', 'Liga {}'),
    (r'^(.*) Junta$', 'Junta {}'),
    (r'^Reichsprotektorat (.*)$', 'Protektorat Reich {}'),
    (r'^Reichsland (.*)$', 'Reichsland {}'),
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
    (r'^Greater (.*)$', '{} Raya'),
    (r'^New (.*)$', '{} Baru'),
    (r'^United (.*)$', '{} Bersatu'),
    (r'^Free (.*)$', '{} Bebas'),
    (r'^Autonomous (.*)$', '{} Otonom'),
    (r'^Independent (.*)$', '{} Independen'),
    (r'^European (.*)$', '{} Eropa'),
]

def translate_r(r):
    if r in OVERRIDES:
        return OVERRIDES[r]
    if r in base_map:
        return base_map[r]
    if r in adj_map:
        return adj_map[r]
    if re.match(r'^\$[A-Za-z0-9_]+\$$', r):
        return r
    if r == "$OVERLORDADJ$ Occupation Zone":
        return "Zona Pendudukan $OVERLORDADJ$"
        
    for pat, template in ALL_PATTERNS:
        m = re.match(pat, r, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            trans_sub = translate_r(sub)
            if trans_sub:
                return template.format(trans_sub)
    return None

still_untranslated = []
for r in roots:
    if not translate_r(r):
        still_untranslated.append(r)

print(f"Still untranslated: {len(still_untranslated)}")
with open('scripts/still_untranslated.txt', 'w', encoding='utf-8') as out:
    for s in sorted(still_untranslated):
        out.write(s + '\n')
