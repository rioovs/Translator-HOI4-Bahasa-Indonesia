"""Hearts of Iron IV DLC Database.
Maps DLC folder names, steam IDs, and internal tags to descriptive titles and categories.
"""

# Map DLC folder names or tags to friendly titles and descriptions
DLC_INFO = {
    # Core Expansions
    "dlc018_together_for_victory": {
        "name": "Together for Victory",
        "title": "Together for Victory",
        "category": "Ekspansi Utama",
        "description": "Fokus Dominion Persemakmuran (Kanada, Australia, Afrika Selatan, Selandia Baru, British Raj)",
    },
    "dlc020_death_or_dishonor": {
        "name": "Death or Dishonor",
        "title": "Death or Dishonor",
        "category": "Ekspansi Utama",
        "description": "Fokus Eropa Tengah/Timur (Hungaria, Rumania, Cekoslowakia, Yugoslavia)",
    },
    "dlc022_waking_the_tiger": {
        "name": "Waking the Tiger",
        "title": "Waking the Tiger",
        "category": "Ekspansi Utama",
        "description": "Fokus Perang Sino-Jepang (Nasionalis, Komunis, Panglima Perang Tiongkok, Jerman Alternatif)",
    },
    "dlc023_man_the_guns": {
        "name": "Man the Guns",
        "title": "Man the Guns",
        "category": "Ekspansi Utama",
        "description": "Perombakan Angkatan Laut, Perancang Kapal Tempur, Fokus Baru AS, Britania, Belanda, Meksiko",
    },
    "dlc028_la_resistance": {
        "name": "La Résistance",
        "title": "La Résistance",
        "category": "Ekspansi Utama",
        "description": "Sistem Spionase & Badan Intelijen, Perang Saudara Spanyol, Fokus Prancis & Portugal",
    },
    "dlc031_battle_for_the_bosporus": {
        "name": "Battle for the Bosporus",
        "title": "Battle for the Bosporus",
        "category": "Country Pack",
        "description": "Fokus Negara Selat Bosporus & Balkan (Turki, Yunani, Bulgaria)",
    },
    "dlc034_no_step_back": {
        "name": "No Step Back",
        "title": "No Step Back",
        "category": "Ekspansi Utama",
        "description": "Perombakan Front Timur, Perancang Tank (Tank Designer), Fokus Uni Soviet & Polandia",
    },
    "dlc036_by_blood_alone": {
        "name": "By Blood Alone",
        "title": "By Blood Alone",
        "category": "Ekspansi Utama",
        "description": "Perombakan Mediterania & Perancang Pesawat (Plane Designer), Fokus Italia, Swiss, Ethiopia",
    },
    "dlc038_arms_against_tyranny": {
        "name": "Arms Against Tyranny",
        "title": "Arms Against Tyranny",
        "category": "Ekspansi Utama",
        "description": "Sistem Organisasi Industri Militer (MIO), Pasar Senjata Internasional, Fokus Negara Nordik",
    },
    "dlc040_trial_of_allegiance": {
        "name": "Trial of Allegiance",
        "title": "Trial of Allegiance",
        "category": "Country Pack",
        "description": "Fokus Negara Amerika Selatan (Brasil, Argentina, Chili, Paraguay, Uruguay)",
    },
    "dlc043_gotterdammerung": {
        "name": "Götterdämmerung",
        "title": "Götterdämmerung",
        "category": "Ekspansi Utama",
        "description": "Proyek Khusus & Senjata Rahasia / Nuklir, Fokus Baru Jerman, Austria, Hungaria, Belgia, Kongo",
    },
    "dlc046_graveyard_of_empires": {
        "name": "Graveyard of Empires",
        "title": "Graveyard of Empires",
        "category": "Country Pack",
        "description": "Fokus Wilayah Timur Tengah & Asia Selatan (India, Iran, Irak, Afganistan)",
    },
    "dlc052_thunder_at_our_gates": {
        "name": "Thunder at Our Gates",
        "title": "Thunder at Our Gates",
        "category": "Ekspansi Utama",
        "description": "Fokus Teater Asia Tenggara & Pasifik (Hindia Belanda / Indonesia, Malaya, Siam, Filipina)",
    },

    # Unit Packs, Flavor, and Content Packs
    "dlc001_german_historical_portraits": {
        "name": "German Historical Portraits",
        "title": "German Historical Portraits",
        "category": "Grafis & Potret",
        "description": "Potret otentik sejarah para pemimpin Jerman Perang Dunia II",
    },
    "dlc002_polish_content_pack": {
        "name": "Poland: United and Ready",
        "title": "Poland: United and Ready",
        "category": "Content Pack",
        "description": "Model 3D khusus, potret pemimpin, dan ikon teknologi Polandia",
    },
    "dlc003_rocket_launcher_unit_pack": {
        "name": "Rocket Launcher Unit Pack",
        "title": "Rocket Launcher Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model animasi peluncur roket artileri medan",
    },
    "dlc004_famous_battleships_unit_pack": {
        "name": "Famous Battleships Unit Pack",
        "title": "Famous Battleships Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D kapal tempur legendaris sejarah angkatan laut",
    },
    "dlc005_heavy_cruisers_unit_pack": {
        "name": "Heavy Cruisers Unit Pack",
        "title": "Heavy Cruisers Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D kapal penjelajah berat berbagai armada",
    },
    "dlc006_soviet_tanks_unit_pack": {
        "name": "Soviet Tanks Unit Pack",
        "title": "Soviet Tanks Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D kendaraan lapis baja dan tank tempur Uni Soviet",
    },
    "dlc007_german_tanks_unit_pack": {
        "name": "German Tanks Unit Pack",
        "title": "German Tanks Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D armada tank Panzer Jerman",
    },
    "dlc008_french_tanks_unit_pack": {
        "name": "French Tanks Unit Pack",
        "title": "French Tanks Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D tank dan kendaraan lapis baja Prancis",
    },
    "dlc009_british_tanks_unit_pack": {
        "name": "British Tanks Unit Pack",
        "title": "British Tanks Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D tank tempur Angkatan Darat Kerajaan Inggris",
    },
    "dlc010_us_tanks_unit_pack": {
        "name": "US Tanks Unit Pack",
        "title": "US Tanks Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D tank Sherman dan lapis baja Amerika Serikat",
    },
    "dlc011_german_march_order_music_pack": {
        "name": "German March Order Music Pack",
        "title": "German March Order Music",
        "category": "Musik & Audio",
        "description": "Lagu pawai dan orkestra militer Jerman",
    },
    "dlc012_allied_radio_music_pack": {
        "name": "Allied Radio Music Pack",
        "title": "Allied Radio Music",
        "category": "Musik & Audio",
        "description": "Stasiun radio musik bertema Sekutu Perang Dunia II",
    },
    "dlc013_sabaton": {
        "name": "Sabaton Soundtrack",
        "title": "Sabaton Soundtrack Vol. 1",
        "category": "Musik & Audio",
        "description": "Lagu heavy metal bertema perang karya band Sabaton",
    },
    "dlc014_wallpaper": {
        "name": "Wallpaper Pack",
        "title": "Official Wallpaper Pack",
        "category": "Bonus Media",
        "description": "Koleksi wallpaper seni resmi Hearts of Iron IV",
    },
    "dlc016_artbook": {
        "name": "Artbook",
        "title": "Digital Artbook",
        "category": "Bonus Media",
        "description": "Buku seni digital konsep desain pengembangan game",
    },
    "dlc017_original_soundtrack": {
        "name": "Original Soundtrack",
        "title": "Original Soundtrack (OST)",
        "category": "Musik & Audio",
        "description": "Album soundtrack simfoni orkestra tema Hearts of Iron IV",
    },
    "dlc019_sabaton_vol2": {
        "name": "Sabaton Soundtrack Vol. 2",
        "title": "Sabaton Soundtrack Vol. 2",
        "category": "Musik & Audio",
        "description": "Lagu tambahan band Sabaton (Ghost Division, Resist and Bite)",
    },
    "dlc021_anniversary_pack": {
        "name": "Anniversary Pack",
        "title": "Anniversary Celebration Pack",
        "category": "Content Pack",
        "description": "Paket perayaan tahunan: pengisi suara unit & potret tambahan",
    },
    "dlc024_man_the_guns_wallpaper": {
        "name": "Man the Guns Wallpaper",
        "title": "Man the Guns Wallpaper Pack",
        "category": "Bonus Media",
        "description": "Wallpaper seni ekspansi Man the Guns",
    },
    "dlc025_axis_armor_pack": {
        "name": "Axis Armor Pack",
        "title": "Axis Armor Pack",
        "category": "Model Unit 3D",
        "description": "53 model 3D kendaraan lapis baja Blok Poros (Jerman, Italia, Jepang)",
    },
    "dlc026_radio_pack": {
        "name": "Radio Pack",
        "title": "Radio Music Pack",
        "category": "Musik & Audio",
        "description": "35 stasiun lagu faksi bersejarah",
    },
    "dlc027_la_resistance_preorder_bonus": {
        "name": "La Résistance Pre-Order Bonus",
        "title": "La Résistance Pre-Order Bonus",
        "category": "Musik & Audio",
        "description": "Lagu aransemen Bella Ciao & Le Chant des Partisans",
    },
    "dlc029_allied_armor_pack": {
        "name": "Allied Armor Pack",
        "title": "Allied Armor Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D lapis baja Sekutu (AS, Inggris, Prancis, Soviet)",
    },
    "dlc030_allied_speeches_pack": {
        "name": "Allied Speeches Music Pack",
        "title": "Allied Speeches Pack",
        "category": "Musik & Audio",
        "description": "Pidato bersejarah Winston Churchill, FDR, de Gaulle, dan Stalin",
    },
    "dlc032_eastern_front_planes_pack": {
        "name": "Eastern Front Planes Pack",
        "title": "Eastern Front Planes Pack",
        "category": "Model Unit 3D",
        "description": "50+ model 3D pesawat tempur Front Timur",
    },
    "dlc033_songs_of_the_eastern_front": {
        "name": "Songs of the Eastern Front",
        "title": "Songs of the Eastern Front",
        "category": "Musik & Audio",
        "description": "Musik orkestra bertema Front Timur dan Soviet",
    },
    "dlc035_no_step_back_preorder_bonus": {
        "name": "No Step Back Pre-Order Bonus",
        "title": "No Step Back Pre-Order Bonus",
        "category": "Musik & Audio",
        "description": "Lagu tradisional perang Katyusha",
    },
    "dlc037_by_blood_alone_preorder_bonus": {
        "name": "By Blood Alone Pre-Order Bonus",
        "title": "By Blood Alone Pre-Order Bonus",
        "category": "Musik & Audio",
        "description": "Aransemen lagu opera dan partisipan Bella Ciao",
    },
    "dlc039_arms_against_tyranny_preorder_bonus": {
        "name": "Arms Against Tyranny Pre-Order Bonus",
        "title": "Arms Against Tyranny Pre-Order Bonus",
        "category": "Musik & Audio",
        "description": "Lagu tradisional Säkkijärven polkka",
    },
    "dlc041_trial_of_allegiance_preorder_bonus": {
        "name": "Trial of Allegiance Pre-Order Bonus",
        "title": "Trial of Allegiance Pre-Order Bonus",
        "category": "Musik & Audio",
        "description": "Lagu kebangsaan & tema Amerika Selatan",
    },
    "dlc042_content_creator_pack_soviet_union_2d_art": {
        "name": "Soviet Union 2D Art Creator Pack",
        "title": "Soviet Union 2D Art Creator Pack",
        "category": "Seni & Antarmuka",
        "description": "Ikon 2D karya kreator komunitas untuk Uni Soviet",
    },
    "dlc044_expansion_pass_1_ride_of_the_valkyries": {
        "name": "Ride of the Valkyries",
        "title": "Ride of the Valkyries Music Pack",
        "category": "Musik & Audio",
        "description": "Lagu klasik Ride of the Valkyries karya Richard Wagner",
    },
    "dlc045_expansion_pass_1_supporter_pack": {
        "name": "Expansion Pass 1 Supporter Content",
        "title": "Expansion Pass 1 Supporter Pack",
        "category": "Content Pack",
        "description": "Konten pendukung Expansion Pass 1",
    },
    "dlc047_prototype_vehicles": {
        "name": "Prototype Vehicles",
        "title": "Prototype Vehicles Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D kendaraan prototipe dan rancangan eksperimental",
    },
    "dlc048_expansion_pass_2_seaplane_tenders": {
        "name": "Seaplane Tenders",
        "title": "Seaplane Tenders Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D armada pengangkut pesawat amfibi",
    },
    "dlc049_no_compromise_no_surrender": {
        "name": "No Compromise, No Surrender",
        "title": "No Compromise, No Surrender",
        "category": "Musik & Audio",
        "description": "Musik orkestra dramatis untuk masa pertempuran sengit",
    },
    "dlc050_warships_of_the_pacific": {
        "name": "Warships of the Pacific",
        "title": "Warships of the Pacific Unit Pack",
        "category": "Model Unit 3D",
        "description": "Model 3D armada kapal perang teater Samudra Pasifik",
    },
    "dlc051_peace_for_our_time": {
        "name": "Peace for Our Time",
        "title": "Peace for Our Time Soundtrack",
        "category": "Musik & Audio",
        "description": "Soundtrack bertema ketegangan diplomatik pra-perang",
    },
}


def get_dlc_display_info(dlc_id: str, parsed_name: str = "", parsed_category: str = "") -> dict:
    """Returns friendly title, category, description and translation status for a DLC."""
    key = dlc_id.lower().strip()
    if key in DLC_INFO:
        info = DLC_INFO[key].copy()
        info["id"] = dlc_id
        info["is_translated"] = True
        return info

    # Format human-friendly name from identifier or parsed name
    clean_title = parsed_name
    if not clean_title:
        parts = dlc_id.split("_", 1)
        if len(parts) > 1:
            clean_title = parts[1].replace("_", " ").title()
        else:
            clean_title = dlc_id.replace("_", " ").title()

    cat_map = {
        "expansion": "Ekspansi Utama",
        "country_pack": "Country Pack",
        "unit_pack": "Model Unit 3D",
        "music": "Musik & Audio",
        "content_pack": "Content Pack",
    }
    category = cat_map.get(parsed_category.lower(), "Ekspansi / DLC")

    return {
        "id": dlc_id,
        "name": parsed_name or clean_title,
        "title": clean_title,
        "category": category,
        "description": f"Konten DLC {clean_title} terintegrasi dalam paket terjemahan.",
        "is_translated": True,
    }
