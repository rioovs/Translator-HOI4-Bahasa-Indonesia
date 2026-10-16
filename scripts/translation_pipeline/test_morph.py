# -*- coding: utf-8 -*-
import json
import re

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

with open('scripts/all_explicit_final.json', 'r', encoding='utf-8') as f:
    EXPLICIT = json.load(f)

with open('scripts/unresolved_roots.txt', 'r', encoding='utf-8') as f:
    unresolved = [line.strip() for line in f if line.strip()]

NOUN_PATTERNS = [
    (r'^Caliphate of (.*)$', 'Kekhalifahan {}'),
    (r'^(.*) Caliphate$', 'Kekhalifahan {}'),
    (r'^Authority of (.*)$', 'Otoritas {}'),
    (r'^(.*) Authority$', 'Otoritas {}'),
    (r'^(.*) Collective$', 'Kolektif {}'),
    (r'^(.*) Monarchy$', 'Monarki {}'),
    (r'^Province of (.*)$', 'Provinsi {}'),
    (r'^(.*) Province$', 'Provinsi {}'),
    (r'^(.*) Communion$', 'Komuni {}'),
    (r'^(.*) Autonomous Soviet Socialist Republic$', 'Republik Sosialis Soviet Otonom {}'),
    (r'^(.*) Autonomous SSR$', 'RSS Otonom {}'),
    (r'^(.*) Independent SSR$', 'RSS Independen {}'),
    (r'^(.*) SSR$', 'RSS {}'),
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
    (r'^(.*) Khanate$', 'Kekhanan {}'),
    (r'^(.*) Protectorate$', 'Protektorat {}'),
    (r'^(.*) Dominion$', 'Dominion {}'),
    (r'^(.*) State$', 'Negara {}'),
    (r'^(.*) Realm$', 'Alam {}'),
    (r'^(.*) Clique$', 'Klik {}'),
    (r'^(.*) League$', 'Liga {}'),
    (r'^(.*) Council$', 'Dewan {}'),
    (r'^(.*) Junta$', 'Junta {}'),
    (r'^(.*) Host$', 'Pasukan {}'),
    (r'^(.*) Territories$', 'Teritori {}'),
    (r'^(.*) Territory$', 'Teritori {}'),
    (r'^(.*) Directorate$', 'Direktorat {}'),
    (r'^(.*) Regency$', 'Keregenan {}'),
    (r'^(.*) Chiefdom$', 'Kedatuan {}'),
]

ADJ_MODIFIERS = [
    (r'^Catholic (.*)$', '{} Katolik'),
    (r'^Orthodox (.*)$', '{} Ortodoks'),
    (r'^Islamic (.*)$', '{} Islam'),
    (r'^Christian (.*)$', '{} Kristen'),
    (r'^Communist (.*)$', '{} Komunis'),
    (r'^Socialist (.*)$', '{} Sosialis'),
    (r'^Democratic (.*)$', '{} Demokratis'),
    (r'^Republican (.*)$', '{} Republikan'),
    (r'^Fascist (.*)$', '{} Fasis'),
    (r'^Nationalist (.*)$', '{} Nasionalis'),
    (r'^Revolutionary (.*)$', '{} Revolusioner'),
    (r'^Anarchist (.*)$', '{} Anarkis'),
    (r'^Syndicalist (.*)$', '{} Sindikalis'),
    (r'^Carlist (.*)$', '{} Karlis'),
    (r'^Integralist (.*)$', '{} Integralis'),
    (r'^Falangist (.*)$', '{} Falangis'),
    (r'^Centralist (.*)$', '{} Sentralis'),
    (r'^Provisional (.*)$', '{} Sementara'),
    (r'^Military (.*)$', '{} Militer'),
    (r'^Federal (.*)$', '{} Federal'),
    (r'^Confederated (.*)$', '{} Konfederasi'),
    (r'^United (.*)$', '{} Bersatu'),
    (r'^Greater (.*)$', '{} Raya'),
    (r'^New (.*)$', '{} Baru'),
    (r'^Free (.*)$', '{} Bebas'),
    (r'^Independent (.*)$', '{} Independen'),
    (r'^Autonomous (.*)$', '{} Otonom'),
    (r'^Danubian (.*)$', '{} Donau'),
    (r'^Baltic (.*)$', '{} Baltik'),
    (r'^Nordic (.*)$', '{} Nordik'),
    (r'^Alpine (.*)$', '{} Alpen'),
    (r'^Imperial (.*)$', '{} Kekaisaran'),
    (r'^Royal (.*)$', '{} Kerajaan'),
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
]

def sub_trans(s):
    s = s.strip()
    if s in EXPLICIT:
        return EXPLICIT[s]
    if s in base_map:
        return base_map[s]
    if s in adj_map:
        return adj_map[s]
    return s

resolved_now = {}
remaining = []

for u in unresolved:
    done = False
    # Check noun patterns
    for pat, template in NOUN_PATTERNS:
        m = re.match(pat, u, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            # check if sub has adj modifiers
            sub_res = None
            for a_pat, a_temp in ADJ_MODIFIERS:
                am = re.match(a_pat, sub, re.IGNORECASE)
                if am:
                    core = am.group(1).strip()
                    sub_res = a_temp.format(sub_trans(core))
                    break
            if not sub_res:
                sub_res = sub_trans(sub)
            resolved_now[u] = template.format(sub_res)
            done = True
            break
    if not done:
        # Check adj modifiers directly
        for a_pat, a_temp in ADJ_MODIFIERS:
            am = re.match(a_pat, u, re.IGNORECASE)
            if am:
                core = am.group(1).strip()
                resolved_now[u] = a_temp.format(sub_trans(core))
                done = True
                break
    if not done:
        remaining.append(u)

print(f"Total unresolved tested: {len(unresolved)}")
print(f"Resolved in this pass: {len(resolved_now)}")
print(f"Remaining after this pass: {len(remaining)}")

with open('scripts/remaining_after_morph.txt', 'w', encoding='utf-8') as out:
    for r in sorted(remaining):
        out.write(r + '\n')
