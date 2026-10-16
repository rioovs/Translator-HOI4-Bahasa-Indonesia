# -*- coding: utf-8 -*-
import json
import re

with open('scripts/parsed_ship_modules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

nat_items = [d for d in data if d['type'] == 'key_val' and d['line_idx'] >= 383 and not d['key'].startswith(('ship_light_battery_sub', 'EQ_MOD_CAT_ship_light_battery_sub', 'cruiser_submarine_specialization', 'midget_submarine_specialization'))]

def translate_nat_value(key, val):
    v = val.strip()
    
    # Fix typo quote if present
    if v.startswith('""'):
        v = v[1:]
    if v.startswith('"') and not v.endswith('"'):
        v = v[1:]

    # 1. Armor Belt / Deck patterns
    # e.g. "240mm Belt/40mm Deck" -> "Sabuk 240mm/Geladak 40mm"
    # e.g. "12.8in Belt/5.5in Deck" -> "Sabuk 12.8in/Geladak 5.5in"
    m_bd = re.match(r'^([\d.]+)\s*(mm|in)\s*Belt\s*/\s*([\d.]+)\s*(mm|in)\s*Deck$', v, re.I)
    if m_bd:
        b_num, b_unit, d_num, d_unit = m_bd.groups()
        b_u = "Inci" if b_unit.lower() == 'in' else "mm"
        d_u = "Inci" if d_unit.lower() == 'in' else "mm"
        if b_u == "Inci":
            return f"Sabuk {b_num} {b_u}/Geladak {d_num} {d_u}"
        return f"Sabuk {b_num}{b_u}/Geladak {d_num}{d_u}"

    # Flight Deck e.g. "50mm Flight Deck", "3.5in Flight Deck"
    m_fd = re.match(r'^([\d.]+)\s*(mm|in)\s*Flight\s*Deck$', v, re.I)
    if m_fd:
        num, unit = m_fd.groups()
        u = " Inci" if unit.lower() == 'in' else "mm"
        return f"Geladak Terbang {num}{u}"

    if v == "Open Hangar Deck":
        return "Geladak Hanggar Terbuka"
    if v == "Integrated Hangar":
        return "Hanggar Terintegrasi"

    # 2. Torpedo tubes / launchers
    # e.g. "3x 533mm Torpedo Tubes" -> "3x Tabung Torpedo 533mm"
    m_tt = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*(Torpedo\s*Tubes?|Torp\.\s*Tubes?|TTs?)$', v, re.I)
    if m_tt:
        count, cal, unit, _ = m_tt.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count}x Tabung Torpedo {cal}{u}"

    m_tl = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*(Torpedo\s*Launchers?)$', v, re.I)
    if m_tl:
        count, cal, unit, _ = m_tl.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count}x Peluncur Torpedo {cal}{u}"

    # English named torpedo tubes
    # e.g. "Triple 21 inch TT" -> "TT Tripel 21 Inci"
    # "Quadruple 21 inch TT" -> "TT Quadruple 21 Inci"
    # "Quintuple 21 inch TT" -> "TT Quintuple 21 Inci"
    # "Twin 550mm TTs" -> "TT Ganda 550mm"
    # "Triple 550mm TTs" -> "TT Tripel 550mm"
    # "Quad 550mm TTs" -> "TT Quad 550mm"
    # "Triple 450mm TT" -> "TT Tripel 450mm"
    # "Triple 533mm TT" -> "TT Tripel 533mm"
    # "Quadruple 533mm TT" -> "TT Quadruple 533mm"
    # "Quintuple 533mm TT" -> "TT Quintuple 533mm"
    # "Triple 21in TT" -> "TT Tripel 21 Inci"
    # "Quadruple 21in TT" -> "TT Quadruple 21 Inci"
    # "Quintuple 61cm TTs" -> "TT Quintuple 61cm"
    # "Quadruple 61cm TTs" -> "TT Quadruple 61cm"
    # "Triple 61cm TTs" -> "TT Tripel 61cm"
    # "Triple 53.3cm TTs" -> "TT Tripel 53,3cm"
    m_ntt = re.match(r'^(Twin|Triple|Quad|Quadruple|Quintuple|Pentad)\s+([\d.]+)\s*(mm|cm|in|inch)\s*(TTs?)$', v, re.I)
    if m_ntt:
        t_type, cal, unit, _ = m_ntt.groups()
        t_trans = {
            'Twin': 'Ganda', 'Triple': 'Tripel', 'Quad': 'Quad',
            'Quadruple': 'Quadruple', 'Quintuple': 'Quintuple', 'Pentad': 'Pentad'
        }.get(t_type.capitalize(), t_type)
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"TT {t_trans} {cal}{u}"

    if v == "Mk 15 Pentad TT":
        return "TT Pentad Mk 15"
    if v == "Pentad TT w/Comp. Air":
        return "TT Pentad dg Udara Bertekanan"
    if v == "Quin. TT w/Comp. Air":
        return "TT Quin. dg Udara Bertekanan"
    if v == "Quad 550mm w/Comp. Air":
        return "TT Quad 550mm dg Udara Bertekanan"
    if v == "Minelaying Tubes":
        return "Tabung Penebar Ranjau"

    # Bow TT
    # e.g. "4 x 21 in Bow TT" -> "4 x TT Haluan 21 Inci"
    # "6 x 533mm Bow TT" -> "6 x TT Haluan 533mm"
    m_btt = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*Bow\s*(TTs?)$', v, re.I)
    if m_btt:
        count, cal, unit, _ = m_btt.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count} x TT Haluan {cal}{u}"

    # w/Comp. Air
    # e.g. "4 x 533mm w/Comp. Air", "5x 533mm w/Comp. Air"
    m_ca = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*w/Comp\.?\s*Air$', v, re.I)
    if m_ca:
        count, cal, unit = m_ca.groups()
        return f"{count} x {cal}{unit} dg Udara Bertekanan"

    # w/L.Pistons
    # e.g. "6 x 21 in w/L.Pistons", "6 x 550mm w/L.Pistons", "6x 533mm w/L.Pistons"
    m_lp = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*w/L\.?\s*Pistons?$', v, re.I)
    if m_lp:
        count, cal, unit = m_lp.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count} x {cal}{u} dg Piston Peluncur"

    # w/P.Loading
    # e.g. "6 x 21 in w/P.Loading", "6 x 550mm w/P.Loading", "6x 533mm w/P.Loading"
    m_pl = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*w/P\.?\s*Loading$', v, re.I)
    if m_pl:
        count, cal, unit = m_pl.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count} x {cal}{u} dg Pengisian Bertenaga"

    # w/TDC
    # e.g. "4 x 21in TT w/Mk 1 TDC"
    m_tdc = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*TT\s*w/(.*)$', v, re.I)
    if m_tdc:
        count, cal, unit, tdc_type = m_tdc.groups()
        u = " Inci" if unit.lower() in ['in', 'inch'] else unit
        return f"{count} x TT {cal}{u} dg {tdc_type}"

    # Japanese TT models
    # "4 x 53.3cm Type 15 TTs"
    m_jtt = re.match(r'^(\d+)\s*x\s*([\d.]+)\s*(mm|cm|in|inch)\s*Type\s*(\d+)\s*TTs?$', v, re.I)
    if m_jtt:
        count, cal, unit, typenum = m_jtt.groups()
        return f"{count} x TT {cal}{unit} Tipe {typenum}"

    # 3. Engines & Reactors
    # e.g. "110,000 Shp Engine" -> "Mesin 110.000 Shp"
    # "Parsons 22,000 Shp Engine" -> "Mesin Parsons 22.000 Shp"
    # "Tosi 1,500 Shp Engine" -> "Mesin Tosi 1.500 Shp"
    # "Atlas 1,160 Shp Engine" -> "Mesin Atlas 1.160 Shp"
    m_eng = re.match(r'^(.*?)\s*([\d,]+)\s*(Shp|hp)\s*Engine$', v, re.I)
    if m_eng:
        brand, pwr, unit = m_eng.groups()
        pwr_id = pwr.replace(',', '.')
        if brand.strip():
            return f"Mesin {brand.strip()} {pwr_id} {unit}"
        return f"Mesin {pwr_id} {unit}"

    # Diesel engines
    # e.g. "MAN Diesels 76,000hp" -> "Diesel MAN 76.000hp"
    # "MAN Diesel 1,100 Shp" -> "Diesel MAN 1.100 Shp"
    # "Fiat Diesels 1,200hp" -> "Diesel Fiat 1.200hp"
    # "Tosi Diesels 3,400hp" -> "Diesel Tosi 3.400hp"
    # "38B8 Diesels 1,370hp" -> "Diesel 38B8 1.370hp"
    # "9DKR Diesels 8,400hp" -> "Diesel 9DKR 8.400hp"
    m_dsl = re.match(r'^(.*?)\s*Diesels?\s*([\d,]+)\s*(hp|Shp)$', v, re.I)
    if m_dsl:
        brand, pwr, unit = m_dsl.groups()
        pwr_id = pwr.replace(',', '.')
        return f"Diesel {brand.strip()} {pwr_id}{unit}"

    if v == "SSW Electric 4,626hp":
        return "Listrik SSW 4.626hp"

    # Nuclear Reactors
    if v == "Pressurized Water Reactor 1":
        return "Reaktor Air Bertekanan 1"
    if v == "Type K48 Pressurized Water Reactor":
        return "Reaktor Air Bertekanan Tipe K48"
    if v == "K48 Reactor":
        return "Reaktor K48"
    if v == "Submarine Thermal Reactor Mark II":
        return "Reaktor Termal Kapal Selam Mark II"
    if v == "VM-A Pressurized Water Reactor":
        return "Reaktor Air Bertekanan VM-A"
    if v == "VM-A Reactor":
        return "Reaktor VM-A"

    # 4. Radar & Sonar
    # e.g. "Type 79 Radar" -> "Radar Tipe 79"
    # "FuMO 22 Radar" -> "Radar FuMO 22"
    # "Tamir-1 Sonar" -> "Sonar Tamir-1"
    m_rad = re.match(r'^(.*?)\s*Radar$', v, re.I)
    if m_rad:
        name = m_rad.group(1).strip()
        if name.startswith('Type '):
            name = 'Tipe ' + name[5:]
        elif name == 'DEM Search':
            name = 'Pencari DEM'
        return f"Radar {name}"

    m_son = re.match(r'^(.*?)\s*Sonar$', v, re.I)
    if m_son:
        name = m_son.group(1).strip()
        if name.startswith('Type '):
            name = 'Tipe ' + name[5:]
        return f"Sonar {name}"

    if v == "Type 93 Hydrophone":
        return "Hidrofon Tipe 93"
    if v == "Arktur Hydrophone":
        return "Hidrofon Arktur"
    if v == "QCA Sonar/JK H.phone":
        return "Sonar QCA/Hidrofon JK"

    # 5. Anti-Submarine Equipment (Depth Charges, Mortars, Racks, Projectors)
    if v == "Mk I DC Rails":
        return "Rel Bom Laut Mk I"
    if v == "Mk IV DC Thrower":
        return "Pelontar Bom Laut Mk IV"
    if v == "Hedgehog A/S Mortar":
        return "Mortir AKS Hedgehog"
    if v == "Squid (DC Mortar)":
        return "Squid (Mortir Bom Laut)"
    if v == "Roller-chain DC Racks":
        return "Rak Bom Laut Rantai-Roller"
    if v == "Gatteschi-type DCR":
        return "Rak Bom Laut Tipe Gatteschi"
    if v == "430mm DC Projector":
        return "Proyektor Bom Laut 430mm"
    if v == "Mk 1 Mod 1 DC Rack":
        return "Rak Bom Laut Mk 1 Mod 1"
    if v == "Mk 6 DC Projector":
        return "Proyektor Bom Laut Mk 6"
    if v == "Type 94 DC Thrower":
        return "Pelontar Bom Laut Tipe 94"
    if v == "15cm rocket-prop'ld DC":
        return "Bom Laut Roket 15cm"
    if v == "Rheinmetall DC Thrower":
        return "Pelontar Bom Laut Rheinmetall"
    if v == "B-1 Depth Charge Rack":
        return "Rak Bom Laut B-1"
    if v == "BMB-1 DC Thrower":
        return "Pelontar Bom Laut BMB-1"
    if v == "Two-speed DD Sweep":
        return "Penyapu Ranjau DD Dua-Kecepatan"
    if v == "Minelaying Rails":
        return "Rel Penebar Ranjau"

    # 6. Snorkels & Catapults & Rangekeepers
    if v in ["Basic Snort", "Basic Snorkel", "Basic Snuiver"]:
        return "Snorkel Dasar"
    if v in ["Improved Snort", "Improved Snorkel", "Improved Snuiver", "Improved Schnorchel"]:
        return "Snorkel yang Disempurnakan"
    if v == "Float Valve Schnorchel":
        return "Snorkel Katup Pelampung"

    if v == "C.IV H 7,000lb Cat.":
        return "Katapel C.IV H 7.000 pon"
    if v == "E.III H 8,000lb Cat.":
        return "Katapel E.III H 8.000 pon"
    if v == "Type P Mk 1 Catapult":
        return "Katapel Tipe P Mk 1"
    if v == "Type P Mk 6 Catapult":
        return "Katapel Tipe P Mk 6"
    if v == "Type 2/No 5 Mod 1 Ct.":
        return "Katapel Tipe 2/No 5 Mod 1"
    if v == "Type 2/No 1 Mod 10 Ct.":
        return "Katapel Tipe 2/No 1 Mod 10"
    if v == "K-3 Catapult":
        return "Katapel K-3"
    if v == "K-12 Catapult":
        return "Katapel K-12"

    if v == "Ford Mk I Rangekeeper":
        return "Penyimpan Jarak Ford Mk I"
    if v == "Mk 8 Rangekeeper":
        return "Penyimpan Jarak Mk 8"
    if v == "Type 92 DCT/Computer":
        return "DCT/Komputer Tipe 92"
    if v == "Type 98 DCT/Computer":
        return "DCT/Komputer Tipe 98"
    if v == "Vickers FC Computer":
        return "Komputer FC Vickers"
    if v == "Galileo FC Computer":
        return "Komputer FC Galileo"

    # 7. Auto-loading guns
    # e.g. "8 in Auto-Loading" -> "8 in Isi-Otomatis"
    m_al = re.match(r'^(.*?)\s+Auto-Load(ing)?\.?$', v, re.I)
    if m_al:
        base = m_al.group(1).strip()
        return f"{base} Isi-Otomatis"

    if v == "20.3 cm/50 Bofors Auto":
        return "20.3 cm/50 Bofors Otomatis"
    if v == "20.3cm/60 Selbstlader":
        return "20.3cm/60 Selbstlader"  # German historical term for auto-loader

    # 8. Minor nations generic "Cannon"
    m_can = re.match(r'^([\d.]+)\s*(mm|cm)\s*RF\.\s*Cannon$', v, re.I)
    if m_can:
        cal, unit = m_can.groups()
        return f"Meriam TC {cal}{unit}"

    m_can2 = re.match(r'^([\d.]+)\s*(mm|cm)(/[\d.]+)?\s*RF\.\s*Cannon$', v, re.I)
    if m_can2:
        cal, unit, cal_len = m_can2.groups()
        clen = cal_len if cal_len else ""
        return f"Meriam TC {cal}{unit}{clen}"

    m_can3 = re.match(r'^([\d.]+)\s*(mm|cm)(/[\d.]+)?\s*Cannon(\s+RPC)?$', v, re.I)
    if m_can3:
        cal, unit, cal_len, rpc = m_can3.groups()
        clen = cal_len if cal_len else ""
        rpc_str = rpc if rpc else ""
        return f"Meriam {cal}{unit}{clen}{rpc_str}"

    if v == "20.3cm/50 Cannon w/RPC":
        return "Meriam 20.3cm/50 dg RPC"
    if v == "15.5 cm/50 w/RPC Cannon":
        return "Meriam 15.5 cm/50 dg RPC"
    if v == "15.5 cm/50 with RPC":
        return "15.5 cm/50 dg RPC"
    if v == "Two-pounder 'Pom-Pom'":
        return "Meriam 'Pom-Pom' 2-Pon"

    # Default: retain historical designation
    return v

# Test the function on all nat items
changes = []
unchanged = []
for it in nat_items:
    k = it['key']
    orig = it['value']
    trans = translate_nat_value(k, orig)
    if trans != orig:
        changes.append((k, orig, trans))
    else:
        unchanged.append((k, orig))

print(f"Total nation items: {len(nat_items)}")
print(f"Translated / transformed items: {len(changes)}")
print(f"Retained as historical model names: {len(unchanged)}")

print("\n--- SAMPLE TRANSLATED NATION ITEMS (first 25) ---")
for k, orig, trans in changes[:25]:
    print(f"{k}:\n  EN: {orig}\n  ID: {trans}")

print("\n--- SAMPLE RETAINED HISTORICAL MODEL NAMES (first 25) ---")
for k, orig in unchanged[:25]:
    print(f"{k}: {orig}")
