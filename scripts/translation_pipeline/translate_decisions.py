# -*- coding: utf-8 -*-
import json
import re

# Translation dictionary for decisions
translations = {
    # UI
    "DECISIONVIEW_TITLE": "Peristiwa dan Keputusan",
    "DECISIONSVIEW_EVENT_HEADER": "Peristiwa",
    "POPUP_NEWS": "Popup Berita",
    "POPUP_EVENTS": "Popup Peristiwa",
    "CATEGORY_COLLAPSE_DESC": "§GKlik§! untuk menciutkan",
    "CATEGORY_EXPAND_DESC": "§GKlik§! untuk memperluas",
    "DECISION_KEEP_NOTIFIED": "§HNotifikasi§!\\n\\n§GKlik§! agar §Rtidak diberi tahu§! saat keputusan ini dapat diambil.\\n",
    "DECISION_NOT_KEEP_NOTIFIED": "§HNotifikasi§!\\n\\n§GKlik§! agar §Gdiberi tahu§! saat keputusan ini dapat diambil.\\n",
    "TAKE_DECISION_HEADER": "§HAmbil keputusan§!\\n\\n",
    "NEWS_POPUP_CHECKBOX_TOOLTIP": "§GKlik§! untuk mengalihkan notifikasi Berita",
    "EVENT_POPUP_CHECKBOX_TOOLTIP": "§GKlik§! untuk mengalihkan notifikasi Peristiwa",
    "MINOR_EVENT_POPUP_CHECKBOX_TOOLTIP": "§GKlik§! untuk mengalihkan notifikasi peristiwa kecil, seperti peristiwa Penerbang Ulung (Ace).",
    "POPUP_MINOR_EVENTS": "Popup Kecil",
    "DECISION_COST_DESC": "Dibutuhkan £pol_power $VAL|H0$ untuk mengambil keputusan",
    "DECISION_COST_NOT_ENOUGH": "Dibutuhkan £pol_power $VAL|HR0$ untuk mengambil keputusan",
    "ON_MAP_DECISION_NAME_DEFAULT": "Cari keputusan di peta.",
    "ADD_DAYS_TO_DECISION": "Tambah $DAYS|H$ hari ke Keputusan $DECISION|H$",
    "REMOVE_DAYS_TO_DECISION": "Kurangi $DAYS|H$ hari dari Keputusan $DECISION|H$",
    "ADD_DAYS_TO_MISSION": "Tambah $DAYS|H$ hari ke Misi $MISSION|H$",
    "REMOVE_DAYS_TO_MISSION": "Kurangi $DAYS|H$ hari dari Misi $MISSION|H$",
    "CLICK_TO_TOGGLE_ALL_CATEGORY_DECISION_TRACKING": "§GKlik§! untuk mengalihkan status notifikasi untuk semua keputusan di bawah kategori ini.",
    "banned_communism_flag": "Telah melarang partai komunis",
    "FRA_civil_unrest_category": "Kerusuhan Sipil",
    "FRA_communist_civil_war_decision": "Pemberontakan Komunis Segera Meletus",
    "FRA_communist_civil_war_decision_desc": "Gejolak politik radikal yang kian memuncak semakin sulit diredam - pada akhirnya kita harus menghadapinya dengan satu atau lain cara.",
    "FRA_fascist_civil_war_decision": "Pemberontakan Fasis Segera Meletus",
    "FRA_fascist_civil_war_decision_desc": "Sentimen populis yang meningkat terbukti menjadi gelombang yang tak terbendung. Tak ada jalan untuk menghindari hal yang tak terelakkan.",
    "ETH_defeat_italy": "Kalahkan Para Penjajah",
    "ETH_defeat_italy_category": "Perang Italia-Etiopia Kedua",
    "ETH_defeat_italy_category_desc": "Italia sekali lagi berusaha menundukkan Etiopia menjadi sekadar wilayah jajahan. Kita telah mengalahkan para penyerbu ini sebelumnya, dan kita dapat mengalahkan mereka lagi jika kita berhasil mengusir mereka dari perbatasan kita untuk selamanya!",
    "seize_some_trains_woo": "Sita Kereta Api Sipil",
    "seize_some_trains_woo_desc": "Perusahaan kereta api komersial memegang kendali atas infrastruktur kita. Dengan perang yang membayangi, kita memiliki hak penuh untuk menyita peralatan demi kepentingan negara.",
    "random_general_monarchy_tt": "Seorang jenderal [FROM.GetAdjective] acak akan diam-diam bersimpati pada monarki.",
    "removed_when_cancelled_war_prop": "Kampanye propaganda telah dihentikan.",
    "war_propaganda_casualties": "Serukan Kepahlawanan",
    "war_propaganda_casualties_desc": "Meskipun jumlah korban jiwa bertambah, rakyat kita harus diberi pemahaman bahwa pahlawan hanya ditempa dalam pertempuran.",
    "war_propaganda_convoys": "Dorong Penghematan",
    "war_propaganda_convoys_desc": "Warga sipil pun dapat membantu memenangkan perang - melalui ketelitian dan penghematan material, setiap gram baja dapat bernilai ganda bagi upaya perang.",
    "war_propaganda_bombing": "Kobarkan Semangat",
    "war_propaganda_bombing_desc": "Meskipun bom berjatuhan di sekitar kita, para pekerja pemberani kita terus berjuang. Semangat pantang menyerah inilah yang akan membawa kita meraih kemenangan.",
    "war_support_during_war": "Dukungan Perang",
    "CHI_occupation_actions": "Tindakan Anti-Pendudukan",
    "CHI_breach_the_yellow_river": "Jebol Tanggul Sungai Kuning",
    "CHI_breach_the_yellow_river_desc": "Sungai Kuning adalah urat nadi kehidupan bagi wilayah-wilayah sekitarnya, namun membentang tepat di jalur invasi yang kian mendekat. Sebagai upaya terakhir untuk memperlambat laju pasukan penyerbu, usulan untuk meledakkan sistem tanggul dan bendungan yang rumit telah diajukan.\\n\\nEfektivitas tindakan ini sulit dipastikan, namun konsekuensinya akan sangat dahsyat.",
    "yellow_river_blown": "Banjir Bandang Parah",
    "yellow_river_blown_desc": "Wilayah ini terendam banjir parah akibat sabotase pertahanan banjir Sungai Kuning.",

    # Raj population decisions
    "RAJ_population_decisions": "Industrialisasi Pedesaan",
    "RAJ_industrialize_state": "Industrialisasi [FROM.GetName]",
    "RAJ_industrialize_state_desc": "Bangsa kita kembali bangkit. Meskipun tugas ini amat besar, memodernisasi daerah pedesaan dipastikan akan membuahkan hasil besar di masa depan.",
    "RAJ_industrialized_this_state": "§HWilayah pedesaan telah diindustrialisasi§!",
    "RAJ_reduce_agrarian_society_value_tooltip": "\\n§H$RAJ_agrarian_society$§!\\nFaktor Populasi yang Dapat Direkrut: [?RAJ_agrarian_society_increment|+=%]\\n",
    "RAJ_industrialize_state_goe": "$RAJ_industrialize_state$",
    "RAJ_industrialize_state_goe_desc": "$RAJ_industrialize_state_desc$",
    "war_propaganda_radio_industry": "Propaganda Radio",
    "war_propaganda_radio_industry_desc": "Teknologi telah berkembang hingga sebagian besar rakyat memiliki akses radio di kediaman mereka. Media yang disponsori negara adalah sarana sempurna untuk mengobarkan semangat perang di sanubari rakyat kita.",
    "war_propaganda_film_industry": "[ROOT.GetImportOrDomesticFilmIndustry]",
    "war_propaganda_film_industry_desc": "[ROOT.GetImportOrDomesticFilmIndustryDesc]",
    "DOMESTIC_FILM_INDUSTRY": "Manfaatkan Industri Perfilman Domestik",
    "IMPORTED_FILM_INDUSTRY": "Impor Film-Film Propaganda",
    "DOMESTIC_FILM_INDUSTRY_DESC": "Industri film [ROOT.GetAdjective] telah berkembang pesat dalam dekade terakhir. Dengan rakyat yang mendambakan hiburan, kita dapat memetik keuntungan besar dari karya sinematik yang dirancang untuk mengobarkan sentimen patriotisme.",
    "IMPORTED_FILM_INDUSTRY_DESC": "Penyokong dan sekutu kita memanfaatkan film propaganda secara strategis. Dengan sedikit investasi, kita dapat menayangkan produksi-produksi ini di seluruh negeri guna mengobarkan semangat perang rakyat kita.",

    # Film titles
    "the_lion_has_wings": "The Lion Has Wings",
    "the_battle_of_london": "The Battle of London",
    "queens_messengers": "Queen's Messengers",
    "in_which_we_serve": "In Which We Serve",
    "the_volunteer": "The Volunteer",
    "fires_were_started": "Fires Were Started",
    "men_of_timor": "Men of Timor",
    "soldiers_without_uniform": "Soldiers Without Uniform",
    "mid_east": "Mid East",
    "atlantic_patrol": "Atlantic Patrol",
    "front_of_steel": "Front of Steel",
    "home_front": "Home Front",
    "wings_of_youth": "Wings of Youth",
    "all_out_for_war": "All Out for War",
    "banshees_over_canada": "Banshees Over Canada",
    "the_planes_of_hindustan": "The Planes of Hindustan",
    "road_to_victory": "Road to Victory",
    "hes_in_the_navy": "He's in the Navy",
    "in_self_defence": "In Self Defence",
    "women_in_defense": "Women in Defense",
    "winning_your_wings": "Winning Your Wings",
    "the_world_at_war": "The World at War",
    "mission_accomplished": "Mission Accomplished",
    "the_fleet_that_came_to_stay": "The Fleet That Came to Stay",
    "fury_in_the_pacific": "Fury in the Pacific",
    "its_your_war_too": "It's Your War Too",
    "belguique_toujours": "Belgique Toujours",
    "high_stakes_in_the_east": "High Stakes in the East",
    "glorious_colours": "Glorious Colours",
    "litte_belgium": "Little Belgium",
    "for_the_front": "Demi Garis Depan",
    "the_peoples_avengers": "Pembalas Rakyat",
    "day_of_war": "Hari Peperangan",
    "film_motherland": "Tanah Air Tercinta",
    "sons_of_the_motherland": "Putra-Putri Ibu Pertiwi",
    "moscow_strikes_back": "Moskow Membalas",
    "fluchtlinge": "Flüchtlinge",
    "film_bismarck": "Bismarck",
    "wunschkonzert": "Wunschkonzert",
    "anschlag_auf_baku": "Anschlag Auf Baku",
    "die_entlassung": "Die Entlassung",
    "besatzung_dora": "Besatzung Dora",
    "opfergang": "Opfergang",
    "panorama": "Panorama",
    "kolberg": "Kolberg",
    "monkey_king": "Raja Kera",
    "genghis_khan": "Jengis Khan",
    "vow_in_the_desert": "Ikrar di Padang Pasir",
    "song_of_the_white_orchid": "Nyanyian Anggrek Putih",
    "five_scouts": "Lima Pengintai",
    "fire_on_that_flag": "Tembak Bendera Itu!",
    "momotarou_umi_no_shinpei": "Prajurit Laut Ilahi Momotaro",
    "condottieri": "Condottieri",
    "scipio_africano": "Scipio Africano",
    "the_man_with_the_cross": "Pria Bersalib",
    "mulan": "Mulan Maju ke Medan Perang",
    "defend_our_land": "Pertahankan Tanah Air Kita",
    "storm_on_the_border": "Badai di Perbatasan",
    "children_of_china": "Anak-Anak Tiongkok",
    "our_war": "Perang Kita",
    "the_war_for_our_existence": "Perang demi Eksistensi Kita",
    "war_in_the_skies": "Pertempuran di Angkasa",
    "flags_raised": "Bendera-Bendera Terkibar",
    "the_day_of_sacrifice": "Hari Pengorbanan",
    "blood_and_toil": "Darah dan Peluh",

    # MIO
    "available_mio_tt": "§GTersedia§! sebagai §YOrganisasi Industri Militer§!: ",
    "foreign_mio_decisions_category": "Undang Industri Asing",
    "invites_mio_tt": "\\n§YMengundang Organisasi Industri Militer Asing§!:",
    "unlock_mio_tt": "\\n§YMendirikan Organisasi Industri Militer§!",

    # Naval procurement & refits
    "generic_purchase_old_ships_category": "Pengadaan Armada Laut",
    "generic_purchase_old_ships_category_desc": "Seiring meningkatnya ketidakstabilan dunia, kita harus memperluas kemampuan proyeksi kekuatan laut kita. Beruntung bagi kita, sejumlah kekuatan laut utama mungkin bersedia melepas kapal-kapal mereka yang lebih tua.",
    "purchase_ships_eng": "[ENG.GetFlag] Beli Kapal Perusak Tua [ENG.GetAdjective]",
    "purchase_ships_sov": "[SOV.GetFlag] Beli Kapal Tempur Tua [SOV.GetAdjective]",
    "purchase_ships_ger": "[GER.GetFlag] Beli U-Boat Tua [GER.GetAdjective]",
    "purchase_ships_usa": "[USA.GetFlag] Beli Kapal Perusak Tua [USA.GetAdjective]",
    "generic_refit_civilian_ships_category": "Modifikasi Militer untuk Kapal Sipil",
    "generic_refit_civilian_ships_category_desc": "Armada kita secara realistis mustahil bersaing dengan armada laut musuh yang jauh lebih masif. Kita harus segera memperbesar armada dengan memodifikasi kapal-kapal sipil untuk kebutuhan tempur.",
    "refit_to_destroyer": "Modifikasi Kapal menjadi Kapal Perusak",
    "refit_to_cruiser": "Modifikasi Kapal menjadi Kapal Penjelajah",
    "diversify_special_forces": "Diversifikasi Pasukan Elit",
    "diversify_special_forces_desc": "Pasukan konvensional kita jelas tidak cukup untuk menghadang ancaman yang datang. Kita dituntut untuk berinovasi.",
    "add_potential_special_forces_tree_tt": "Menambahkan §H1§! §HSpesialisasi Cabang§! Pasukan Khusus secara gratis",
    "refit_to_destroyer_nor": "Modifikasi Konvoi menjadi Kapal Perusak",
    "refit_to_destroyer_mass_nor": "Modifikasi Massal Konvoi menjadi Kapal Perusak",
    "nor_building_ship": "Sedang Mengonversi Kapal",
}

with open('scripts/decisions.json', 'r', encoding='utf-8') as f:
    dec_items = json.load(f)

translated_items = []
unhandled = []

for item in dec_items:
    k = item['key']
    val = item['val']
    
    # Check if exact key in translations dict
    if k in translations:
        new_val = translations[k]
    # Check if invite MIO
    elif k.startswith('invite_') and k.endswith('_organization'):
        org_name = k.replace('invite_', '')
        new_val = f"Undang §Y${org_name}$§! ke §Y[ROOT.GetNameWithFlag]§!"
    # Check cost tooltips
    elif k.endswith('_tooltip'):
        # It costs ... to take the decision
        # It costs ... while this decision is active
        # It costs ... to take this decision
        m_active = re.match(r'^It costs (.*) while this decision is active$', val)
        m_take = re.match(r'^It costs (.*) to take (the|this) decision$', val)
        if m_active:
            cost_part = m_active.group(1)
            cost_part = cost_part.replace("Faction Influence", "Pengaruh Faksi")
            new_val = f"Dibutuhkan {cost_part} selama keputusan ini aktif"
        elif m_take:
            cost_part = m_take.group(1)
            cost_part = cost_part.replace("Faction Influence", "Pengaruh Faksi")
            cost_part = cost_part.replace("and", "dan")
            new_val = f"Dibutuhkan {cost_part} untuk mengambil keputusan ini"
        else:
            unhandled.append((k, val))
            new_val = val
    # Check pure cost indicators like £command_power §Y15§! or blocked £command_power §R15§!
    elif k.startswith('decision_cost_'):
        # keep as-is because it's just icons and numbers
        new_val = val
    else:
        unhandled.append((k, val))
        new_val = val

    translated_items.append({
        'key': k,
        'ver': item['ver'],
        'val': new_val,
        'comm': item['comm']
    })

print(f"Unhandled count: {len(unhandled)}")
for u in unhandled[:10]:
    print("  ", u)

with open('scripts/decisions_translated.json', 'w', encoding='utf-8') as f:
    json.dump(translated_items, f, ensure_ascii=False, indent=2)
