# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

with open('scripts/all_explicit_final.json', 'r', encoding='utf-8') as f:
    EXPLICIT = json.load(f)

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    all_roots = [line.strip() for line in f if line.strip()]

# Additional descriptive terms dictionary
DESC_WORDS = {
    "Almighty": "Maha Kuasa",
    "Holy": "Suci",
    "Grand": "Agung",
    "Great": "Besar",
    "Little": "Kecil",
    "Old": "Lama",
    "New": "Baru",
    "High": "Tinggi",
    "Low": "Rendah",
    "Upper": "Hulu",
    "Lower": "Hilir",
    "Central": "Tengah",
    "Middle": "Tengah",
    "North": "Utara",
    "South": "Selatan",
    "East": "Timur",
    "West": "Barat",
    "Northern": "Utara",
    "Southern": "Selatan",
    "Eastern": "Timur",
    "Western": "Barat",
    "Northeast": "Timur Laut",
    "Northwest": "Barat Laut",
    "Southeast": "Tenggara",
    "Southwest": "Barat Daya",
    "Maritime": "Maritim",
    "Inner": "Dalam",
    "Outer": "Luar",
    "Equatorial": "Khatulistiwa",
    "Tropical": "Tropis",
    "Arctic": "Arktik",
    "Alpine": "Alpen",
    "Pacific": "Pasifik",
    "Atlantic": "Atlantik",
    "Baltic": "Baltik",
    "Mediterranean": "Laut Tengah",
    "Black Sea": "Laut Hitam",
    "Caspian": "Kaspia",
    "Caribbean": "Karibia",
    "Danubian": "Donau",
    "Danube": "Donau",
    "Rhine": "Rhein",
    "Volga": "Volga",
    "Dnieper": "Dnieper",
    "Don": "Don",
    "Ural": "Ural",
    "Siberian": "Siberia",
    "Caucasian": "Kaukasus",
    "Caucasus": "Kaukasus",
    "Balkan": "Balkan",
    "Iberian": "Iberia",
    "Scandinavian": "Skandinavia",
    "Nordic": "Nordik",
    "Slavic": "Slavia",
    "Germanic": "Jermanik",
    "Celtic": "Keltik",
    "Latin": "Latin",
    "Hellenic": "Helenik",
    "Byzantine": "Bizantium",
    "Roman": "Romawi",
    "Ottoman": "Utsmaniyah",
    "Arab": "Arab",
    "Arabic": "Arab",
    "Islamic": "Islam",
    "Muslim": "Muslim",
    "Orthodox": "Ortodoks",
    "Catholic": "Katolik",
    "Protestant": "Protestan",
    "Christian": "Kristen",
    "Jewish": "Yahudi",
    "Buddhist": "Buddha",
    "Hindu": "Hindu",
    "Socialist": "Sosialis",
    "Communist": "Komunis",
    "Democratic": "Demokratis",
    "Republican": "Republikan",
    "Monarchist": "Monarkis",
    "Royal": "Kerajaan",
    "Imperial": "Kekaisaran",
    "Fascist": "Fasis",
    "Nationalist": "Nasionalis",
    "National": "Nasional",
    "Popular": "Populer",
    "People's": "Rakyat",
    "Workers": "Buruh",
    "Workers'": "Buruh",
    "Peasants": "Petani",
    "Peasants'": "Petani",
    "Farmers": "Petani",
    "Farmers'": "Petani",
    "Agrarian": "Agraria",
    "Labor": "Buruh",
    "Trade Union": "Serikat Buruh",
    "Syndicalist": "Sindikalis",
    "Anarchist": "Anarkis",
    "Revolutionary": "Revolusioner",
    "Radical": "Radikal",
    "Progressive": "Progresif",
    "Conservative": "Konservatif",
    "Liberal": "Liberal",
    "Reformist": "Reformis",
    "Traditionalist": "Tradisionalis",
    "Patriotic": "Patriotik",
    "Unitary": "Kesatuan",
    "Federal": "Federal",
    "Confederate": "Konfederasi",
    "Confederated": "Konfederasi",
    "United": "Bersatu",
    "Allied": "Sekutu",
    "Free": "Bebas",
    "Independent": "Independen",
    "Sovereign": "Berdaulat",
    "Autonomous": "Otonom",
    "Provisional": "Sementara",
    "Transitional": "Transisi",
    "Military": "Militer",
    "Naval": "Angkatan Laut",
    "Civil": "Sipil",
    "Colonial": "Kolonial",
    "Totalitarian": "Totaliter",
    "Authoritarian": "Otoriter",
}

PATTERNS = [
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
    (r'^(.*) Host$', 'Pasukan {}'),
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

def trans_text(t):
    if not t:
        return ""
    t_strip = t.strip()
    if t_strip in EXPLICIT:
        return EXPLICIT[t_strip]
    if t_strip in base_map:
        return base_map[t_strip]
    if t_strip in adj_map:
        return adj_map[t_strip]
    if t_strip in DESC_WORDS:
        return DESC_WORDS[t_strip]
    if re.match(r'^\$[A-Za-z0-9_]+\$$', t_strip):
        return t_strip
    if t_strip == "$OVERLORDADJ$ Occupation Zone":
        return "Zona Pendudukan $OVERLORDADJ$"

    # Strip leading the/The
    if t_strip.startswith('the ') or t_strip.startswith('The '):
        sub = re.sub(r'^[tT]he\s+', '', t_strip)
        return trans_text(sub)

    for pat, template in PATTERNS:
        m = re.match(pat, t_strip, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            sub_tr = trans_text(sub)
            if sub_tr:
                return template.format(sub_tr)

    # Word-by-word heuristic for composite titles
    words = t_strip.split()
    if len(words) > 1:
        # Check if last word is a government entity
        entities = {
            "Republic": "Republik", "Empire": "Kekaisaran", "Kingdom": "Kerajaan",
            "Federation": "Federasi", "Confederation": "Konfederasi", "Union": "Uni",
            "Commune": "Komune", "State": "Negara", "League": "Liga", "Junta": "Junta",
            "Council": "Dewan", "Protectorate": "Protektorat", "Sultanate": "Kesultanan",
            "Emirate": "Keamiran", "Territories": "Teritori", "Territory": "Teritori"
        }
        last_word = words[-1]
        if last_word in entities:
            prefix_words = words[:-1]
            prefix_tr = " ".join([trans_text(w) or w for w in prefix_words])
            return f"{entities[last_word]} {prefix_tr}"

    return None

results = {}
unresolved = []
for r in all_roots:
    res = trans_text(r)
    if res:
        results[r] = res
    else:
        unresolved.append(r)

print(f"Total roots: {len(all_roots)}")
print(f"Resolved: {len(results)} ({len(results)/len(all_roots)*100:.1f}%)")
print(f"Unresolved: {len(unresolved)}")

with open('scripts/unresolved_roots.txt', 'w', encoding='utf-8') as out:
    for u in sorted(unresolved):
        out.write(u + '\n')
