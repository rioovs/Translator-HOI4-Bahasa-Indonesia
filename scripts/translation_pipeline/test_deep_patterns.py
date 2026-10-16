# -*- coding: utf-8 -*-
import json
import re

with open('scripts/remaining_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scripts/all_bases_complete.json', 'r', encoding='utf-8') as f:
    base_map = json.load(f)

with open('scripts/all_adjs_complete.json', 'r', encoding='utf-8') as f:
    adj_map = json.load(f)

def trans_sub(s):
    s = s.strip()
    if s in base_map:
        return base_map[s]
    if s in adj_map:
        return adj_map[s]
    return s

MORE_PATTERNS = [
    (r'^Colony of (?:the )?(.*)$', 'Koloni {}'),
    (r'^Commonwealth of (?:the )?(.*)$', 'Persemakmuran {}'),
    (r'^Grand Principality of (?:the )?(.*)$', 'Kepangeranan Agung {}'),
    (r'^Principality of (?:the )?(.*)$', 'Kepangeranan {}'),
    (r'^Viceroyalty of (?:the )?(.*)$', 'Kewizuraian {}'),
    (r'^Archduchy of (?:the )?(.*)$', 'Keharyapatihan {}'),
    (r'^Margraviate of (?:the )?(.*)$', 'Markgrafiat {}'),
    (r'^Landgraviate of (?:the )?(.*)$', 'Landgrafiat {}'),
    (r'^Bishopric of (?:the )?(.*)$', 'Keuskupan {}'),
    (r'^Archbishopric of (?:the )?(.*)$', 'Keuskupan Agung {}'),
    (r'^Patriarchate of (?:the )?(.*)$', 'Patriarkat {}'),
    (r'^Order of (?:the )?(.*)$', 'Ordo {}'),
    (r'^Commandery of (?:the )?(.*)$', 'Komanditer {}'),
    (r'^Precipice of (?:the )?(.*)$', 'Tepian {}'),
    (r'^Crown of (?:the )?(.*)$', 'Mahkota {}'),
    (r'^Realm of (?:the )?(.*)$', 'Alam {}'),
    (r'^Dominion of (?:the )?(.*)$', 'Dominion {}'),
    (r'^Protectorate of (?:the )?(.*)$', 'Protektorat {}'),
    (r'^Mandate of (?:the )?(.*)$', 'Mandat {}'),
    (r'^Territory of (?:the )?(.*)$', 'Teritori {}'),
    (r'^Territories of (?:the )?(.*)$', 'Teritori {}'),
    (r'^Government of (?:the )?(.*)$', 'Pemerintahan {}'),
    (r'^Administration of (?:the )?(.*)$', 'Administrasi {}'),
    (r'^Directorate of (?:the )?(.*)$', 'Direktorat {}'),
    (r'^Regency of (?:the )?(.*)$', 'Keregenan {}'),
    (r'^Council of (?:the )?(.*)$', 'Dewan {}'),
    (r'^Committee of (?:the )?(.*)$', 'Komite {}'),
    (r'^Commission of (?:the )?(.*)$', 'Komisi {}'),
    (r'^Board of (?:the )?(.*)$', 'Dewan {}'),
    (r'^Assembly of (?:the )?(.*)$', 'Majelis {}'),
    (r'^League of (?:the )?(.*)$', 'Liga {}'),
    (r'^Union of (?:the )?(.*)$', 'Uni {}'),
    (r'^Federation of (?:the )?(.*)$', 'Federasi {}'),
    (r'^Confederation of (?:the )?(.*)$', 'Konfederasi {}'),
    (r'^Alliance of (?:the )?(.*)$', 'Aliansi {}'),
    (r'^Coalition of (?:the )?(.*)$', 'Koalisi {}'),
    (r'^Front of (?:the )?(.*)$', 'Front {}'),
    (r'^Party of (?:the )?(.*)$', 'Partai {}'),
    (r'^Faction of (?:the )?(.*)$', 'Faksi {}'),
    (r'^Brotherhood of (?:the )?(.*)$', 'Persaudaraan {}'),
    (r'^Society of (?:the )?(.*)$', 'Masyarakat {}'),
    (r'^Community of (?:the )?(.*)$', 'Komunitas {}'),
    (r'^People of (?:the )?(.*)$', 'Rakyat {}'),
    (r'^Peoples of (?:the )?(.*)$', 'Rakyat {}'),
    (r'^Nations of (?:the )?(.*)$', 'Bangsa-Bangsa {}'),
    (r'^Descendants of (?:the )?(.*)$', 'Keturunan {}'),
    (r'^Sons of (?:the )?(.*)$', 'Putra-Putra {}'),
    (r'^Daughters of (?:the )?(.*)$', 'Putri-Putri {}'),
    (r'^Children of (?:the )?(.*)$', 'Anak-Anak {}'),
    (r'^Voice of (?:the )?(.*)$', 'Suara {}'),
    (r'^Heart of (?:the )?(.*)$', 'Jantung {}'),
    (r'^Shield of (?:the )?(.*)$', 'Perisai {}'),
    (r'^Sword of (?:the )?(.*)$', 'Pedang {}'),
    (r'^Spear of (?:the )?(.*)$', 'Tombak {}'),
    (r'^Sun of (?:the )?(.*)$', 'Surya {}'),
    (r'^Star of (?:the )?(.*)$', 'Bintang {}'),
    (r'^Fathers of (?:the )?(.*)$', 'Bapa-Bapa {}'),
    (r'^Mothers of (?:the )?(.*)$', 'Ibu-Ibu {}'),
]

matched = {}
unmatched = []

for item in items:
    done = False
    for pat, template in MORE_PATTERNS:
        m = re.match(pat, item, re.IGNORECASE)
        if m:
            sub = m.group(1).strip()
            matched[item] = template.format(trans_sub(sub))
            done = True
            break
    if not done:
        unmatched.append(item)

print(f"Total tested: {len(items)}")
print(f"Matched by MORE_PATTERNS: {len(matched)}")
print(f"Unmatched remaining: {len(unmatched)}")
with open('scripts/unmatched_deep.txt', 'w', encoding='utf-8') as out:
    for u in sorted(unmatched):
        out.write(u + '\n')
