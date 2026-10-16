# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

with open('scripts/all_unique_roots.txt', 'r', encoding='utf-8') as f:
    all_roots = [line.strip() for line in f if line.strip()]

# Test rule additions
colonial = [
    (r'^British (.*)$', '{} Britania'),
    (r'^French (.*)$', '{} Prancis'),
    (r'^German (.*)$', '{} Jerman'),
    (r'^Italian (.*)$', '{} Italia'),
    (r'^Spanish (.*)$', '{} Spanyol'),
    (r'^Portuguese (.*)$', '{} Portugal'),
    (r'^Dutch (.*)$', '{} Belanda'),
    (r'^Russian (.*)$', '{} Rusia'),
    (r'^Soviet (.*)$', '{} Soviet'),
    (r'^Japanese (.*)$', '{} Jepang'),
    (r'^American (.*)$', '{} Amerika'),
    (r'^Austrian (.*)$', '{} Austria'),
    (r'^Belgian (.*)$', '{} Belgia'),
    (r'^Swedish (.*)$', '{} Swedia'),
    (r'^Danish (.*)$', '{} Denmark'),
    (r'^Norwegian (.*)$', '{} Norwegia'),
    (r'^Polish (.*)$', '{} Polandia'),
    (r'^Greek (.*)$', '{} Yunani'),
    (r'^Turkish (.*)$', '{} Turki'),
    (r'^Romanian (.*)$', '{} Rumania'),
    (r'^Hungarian (.*)$', '{} Hongaria'),
    (r'^Bulgarian (.*)$', '{} Bulgaria'),
    (r'^Yugoslav (.*)$', '{} Yugoslavia'),
    (r'^Yugoslavian (.*)$', '{} Yugoslavia'),
    (r'^Chinese (.*)$', '{} Tiongkok'),
    (r'^Banovina of (.*)$', 'Banovina {}'),
    (r'^(.*) Autonomous Region$', 'Wilayah Otonom {}'),
    (r'^(.*) Autonomous District$', 'Distrik Otonom {}'),
    (r'^(.*) Autonomous Territory$', 'Teritori Otonom {}'),
    (r'^(.*) Governorate$', 'Kegubernuran {}'),
    (r'^Governorate of (.*)$', 'Kegubernuran {}'),
    (r'^(.*) Authority$', 'Otoritas {}'),
    (r'^Authority of (.*)$', 'Otoritas {}'),
    (r'^(.*) Cooperative$', 'Koperasi {}'),
    (r'^(.*) Confederacy$', 'Konfederasi {}'),
    (r'^(.*) Realm$', 'Alam {}'),
    (r'^(.*) Chiefdom$', 'Kedatuan {}'),
    (r'^(.*) Directorate$', 'Direktorat {}'),
    (r'^(.*) Junta$', 'Junta {}'),
    (r'^(.*) Regency$', 'Keregenan {}'),
    (r'^(.*) Territory$', 'Teritori {}'),
    (r'^(.*) Territories$', 'Teritori {}'),
]

matched = 0
for r in all_roots:
    for pat, template in colonial:
        if re.match(pat, r, re.IGNORECASE):
            matched += 1
            break

print(f"Matched by colonial / administrative patterns: {matched}")
