# -*- coding: utf-8 -*-
import json
import re

with open('scripts/focus_part6_extracted.json', 'r', encoding='utf-8') as f:
    p6 = json.load(f)

# Translation dictionary for Part 6
trans = {}

def t(k, ind):
    trans[k] = ind

# British Raj (RAJ) focuses
raj_translations = {
    "RAJ_all_india_forward_bloc": "Blok Maju Seluruh India (Forward Bloc)",
    "RAJ_all_india_forward_bloc_desc": "Subhas Chandra Bose telah membentuk faksi militan yang menuntut kemerdekaan mutlak dari penjajahan Inggris sekarang juga.",
    "RAJ_indian_national_army": "Tentara Nasional India (INA)",
    "RAJ_indian_national_army_desc": "Membentuk tentara pembebasan India untuk berjuang bersama kekuatan anti-imperialis membebaskan tanah air kita.",
    "RAJ_quit_india_movement": "Gerakan Tinggalkan India (Quit India)",
    "RAJ_quit_india_movement_desc": "Mahatma Gandhi menyerukan gerakan pembangkangan sipil massal menuntut penarikan segera pasukan Inggris dari India.",
    "RAJ_indian_gentlemen_officers": "Perwira Pribumi India",
    "RAJ_indian_gentlemen_officers_desc": "Membuka akademi militer bagi pemuda pribumi India untuk memegang komando pasukan tempur kita sendiri.",
    "RAJ_lions_of_the_great_war": "Singa-Singa Perang Besar",
    "RAJ_lions_of_the_great_war_desc": "Mengingat kembali kepahlawanan resimen India di medan tempur Eropa dan Timur Tengah dalam Perang Dunia Pertama."
}

# Continuous focuses
continuous_translations = {
    "continuous_air_production": "Produksi Udara Berkelanjutan",
    "continuous_air_production_desc": "Mengarahkan sumber daya industri untuk mempercepat produksi pesawat militer.",
    "continuous_naval_production": "Produksi Angkatan Laut Berkelanjutan",
    "continuous_naval_production_desc": "Memfokuskan galangan kapal untuk mempercepat penyelesaian armada tempur laut.",
    "continuous_armor_production": "Produksi Kendaraan Lapis Baja Berkelanjutan",
    "continuous_armor_production_desc": "Mengoptimalkan jalur pabrik untuk menghasilkan tank dan kendaraan tempur lebih cepat.",
    "continuous_suppression": "Peredaman Perlawanan Berkelanjutan",
    "continuous_suppression_desc": "Mengerahkan unit militer untuk meredam aktivitas gerilya dan perlawanan di wilayah pendudukan.",
    "continuous_repair": "Perbaikan Infrastruktur Berkelanjutan",
    "continuous_repair_desc": "Menugaskan divisi zeni dan konstruksi untuk memperbaiki pabrik dan infrastruktur yang rusak akibat perang.",
    "continuous_tech_share": "Berbagi Teknologi Berkelanjutan",
    "continuous_tech_share_desc": "Membuka kerja sama riset yang lebih erat dengan para sekutu dalam faksi kita."
}

# USA focuses
usa_translations = {
    "USA_re-establish_the_gold_standard": "Pemberlakuan Kembali Standar Emas",
    "USA_re-establish_the_gold_standard_desc": "Menstabilkan mata uang dolar dengan mengaitkannya kembali secara ketat pada cadangan emas negara.",
    "USA_war_plan_white": "Rencana Perang Putih (War Plan White)",
    "USA_war_plan_white_desc": "Rencana operasi militer darurat untuk mengatasi kerusuhan domestik atau pemberontakan dalam negeri.",
    "USA_war_plan_black": "Rencana Perang Hitam (War Plan Black)",
    "USA_war_plan_black_desc": "Rencana pertahanan kontinjensi menghadapi potensi agresi dari Jerman.",
    "USA_war_plan_orange": "Rencana Perang Oranye (War Plan Orange)",
    "USA_war_plan_orange_desc": "Rencana strategis jangka panjang AL AS menghadapi perang maritim melawan Kekaisaran Jepang di Samudera Pasifik.",
    "USA_war_plan_red": "Rencana Perang Merah (War Plan Red)",
    "USA_war_plan_red_desc": "Rencana kontinjensi menghadapi potensi konflik bersenjata dengan Imperium Britania.",
    "USA_manhattan_project": "Proyek Manhattan",
    "USA_manhattan_project_desc": "Memusatkan ilmuwan terkemuka dunia di laboratorium rahasia untuk mengembangkan senjata fusi nuklir pertama umat manusia.",
    "USA_arsenal_of_democracy": "Gudang Senjata Demokrasi",
    "USA_arsenal_of_democracy_desc": "Amerika Serikat harus menjadi gudang senjata utama bagi bangsa-bangsa bebas yang berjuang melawan tirani.",
    "USA_two_ocean_navy_act": "Undang-Undang Angkatan Laut Dua Samudera",
    "USA_two_ocean_navy_act_desc": "Membangun armada tempur laut berkekuatan ganda yang mampu mendominasi Samudera Atlantik dan Pasifik secara bersamaan.",
    "USA_escort_effort": "Upaya Kapal Pengawal",
    "USA_escort_effort_desc": "Memproduksi ratusan kapal perusak pengawal untuk memburu kawanan kapal selam musuh di Atlantik."
}

for it in p6:
    k = it['key']
    v = it['val']
    if k in trans:
        continue
    if k in raj_translations:
        t(k, raj_translations[k])
    elif k in continuous_translations:
        t(k, continuous_translations[k])
    elif k in usa_translations:
        t(k, usa_translations[k])
    else:
        ind = v
        if not k.endswith('_desc'):
            ind = ind.replace('Expand ', 'Perluas ')
            ind = ind.replace('Support ', 'Dukung ')
            ind = ind.replace('Develop ', 'Kembangkan ')
            ind = ind.replace('War Plan ', 'Rencana Perang ')
            ind = ind.replace('Act', 'Undang-Undang')
            ind = ind.replace('Plan', 'Rencana')
            ind = ind.replace('Navy', 'Angkatan Laut')
            ind = ind.replace('Army', 'Angkatan Darat')
            ind = ind.replace('Air', 'Udara')
            ind = ind.replace('Production', 'Produksi')
            ind = ind.replace('Defense', 'Pertahanan')
            ind = ind.replace('Effort', 'Upaya')
        else:
            ind = ind.replace('We must ', 'Kita harus ')
            ind = ind.replace('We will ', 'Kita akan ')
            ind = ind.replace('This will allow us to ', 'Hal ini memungkinkan kita untuk ')
            ind = ind.replace('in order to ', 'guna ')
        t(k, ind)

print(f"Total translated items in P6: {len(trans)}")

# Write to scripts/focus_part6.js
with open('scripts/focus_part6.js', 'w', encoding='utf-8') as f:
    f.write('module.exports = ' + json.dumps(trans, indent=2, ensure_ascii=False) + ';\n')

print("Successfully written scripts/focus_part6.js")
