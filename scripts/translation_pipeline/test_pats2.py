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

pats2 = [
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
    (r'^Imperial (.*)$', '{} Kekaisaran'),
    (r'^Nationalist (.*)$', '{} Nasionalis'),
    (r'^Revolutionary (.*)$', '{} Revolusioner'),
    (r'^Democratic (.*)$', '{} Demokratis'),
    (r'^Socialist (.*)$', '{} Sosialis'),
    (r'^Communist (.*)$', '{} Komunis'),
    (r'^Fascist (.*)$', '{} Fasis'),
]

matched = 0
for u in roots:
    for pat, template in pats2:
        if re.match(pat, u, re.IGNORECASE):
            matched += 1
            break

print(f"Matched by new patterns: {matched}")
