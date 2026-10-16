# -*- coding: utf-8 -*-
import json
import re

with open('scripts/focus_part5_extracted.json', 'r', encoding='utf-8') as f:
    p5 = json.load(f)

# Translation dictionary for Part 5
trans = {}

# Helper to register
def t(k, ind):
    trans[k] = ind

# Canada
t("CAN_defence_scheme_no_1_desc", "Sudah waktunya membersihkan debu dari Rencana Pertahanan No. 1, rencana masa antarperang kita untuk melancarkan serangan balasan ke Amerika Serikat jika perang pecah.")
t("CAN_demand_labrador_and_newfoundland", "Tuntut Labrador dan Newfoundland")
t("CAN_demand_labrador_and_newfoundland_desc", "Newfoundland adalah Dominion yang gagal dan terpaksa kembali ke status koloni. Tempat semestinya adalah bersatu bersama Kanada.")
t("CAN_burn_the_royal_portraits", "Bakar Potret Kerajaan")
t("CAN_burn_the_royal_portraits_desc", "Cukup sudah monarki! Kita tidak akan lagi tunduk pada kekuasaan boneka asing dan parlemen seberang lautan. Kanada akan merdeka dan setara. Rakyat akan bangkit.")
t("CAN_communist_labor_total_war_committee", "Komite Perang Total Buruh Komunis")
t("CAN_communist_labor_total_war_committee_desc", "Komunis Kanada juga patriot! Dalam perang global melawan Fasisme, kita dapat bekerja sama dengan kaum borjuis liberal untuk memobilisasi seluruh bangsa demi perang.")
t("CAN_defence_scheme_no_2", "Rencana Pertahanan No. 2")
t("CAN_defence_scheme_no_2_desc", "Rencana Pertahanan No. 2 adalah rencana kontinjensi kita jika terjadi perang di Pasifik antara Amerika Serikat dan Kekaisaran Jepang. Idealnya kita tetap netral, tetapi bagaimanapun situasinya, pertahanan kokoh di pantai barat harus dibangun.")
t("CAN_supply_the_red_army", "Pasok Tentara Merah")
t("CAN_supply_the_red_army_desc", "Saat Uni Soviet berperang melawan musuh rakyat, Kanada harus membantu Moskwa dengan senjata dan perbekalan.")
t("CAN_canada_united", "Kanada Bersatu")
t("CAN_canada_united_desc", "Meskipun populasi kita tersebar dalam garis tipis melintasi benua, kita bersatu dalam krisis dunia ini untuk membela nilai-nilai Kanada dan melindungi yang lemah.")
t("CAN_join_comintern", "Bergabung dengan Komintern")
t("CAN_join_comintern_desc", "Uni Soviet telah membuktikan itikad baik dan kekuatannya. Kanada harus bergabung dengan aliansi Soviet.")
t("CAN_swastika_clubs", "Klub Swastika")
t("CAN_swastika_clubs_desc", "Gelombang baru gerakan fasis telah melanda Kanada dalam bentuk Klub Swastika. Mereka dapat digunakan untuk memaksakan ketertiban di jalanan dan memperkuat posisi politik kita.")
t("CAN_patriote", "Kaum Patriot (Patriote)")
t("CAN_patriote_desc", "Partai Nasional Sosial Kristen pimpinan Adrien Arcand mengumpulkan kekuatan di Quebec. Kita dapat merangkul kelompok Patriot ini ke dalam barisan kita.")
t("CAN_support_the_national_unity_party", "Dukung Partai Persatuan Nasional")
t("CAN_support_the_national_unity_party_desc", "Dua kelompok fasis utama di Kanada telah bergabung membentuk Partai Persatuan Nasional. Kita harus mendukung mereka sepenuhnya.")
t("CAN_join_axis", "Bergabung dengan Poros")
t("CAN_join_axis_desc", "Kekuatan-kekuatan Poros memimpin tatanan baru dunia. Kanada harus bersekutu dengan Jerman dan sekutunya.")
t("CAN_sever_ties_with_the_uk", "Putuskan Hubungan dengan Inggris")
t("CAN_sever_ties_with_the_uk_desc", "Inggris telah lama mengeksploitasi sumber daya dan rakyat Kanada untuk kepentingan kekaisaran mereka. Sudah saatnya kita memutuskan rantai penjajahan ini.")
t("CAN_compromise_with_quebec", "Kompromi dengan Quebec")
t("CAN_compromise_with_quebec_desc", "Ketegangan antara penutur bahasa Inggris dan Prancis di Kanada mengancam persatuan nasional. Kita harus mencapai kompromi yang adil dengan Quebec demi kesatuan bangsa.")
t("CAN_forced_conscription", "Wajib Militer Paksa")
t("CAN_forced_conscription_desc", "Perang menuntut pengorbanan besar. Kita tidak bisa lagi hanya mengandalkan sukarelawan; wajib militer menyeluruh harus diberlakukan di seluruh negeri.")
t("CAN_strengthen_the_rcmp", "Perkuat RCMP")
t("CAN_strengthen_the_rcmp_desc", "Polisi Berkuda Kerajaan Kanada (RCMP) harus diperluas wewenang dan kekuatannya untuk menindak mata-mata, penyabot, dan elemen subversif.")
t("CAN_expand_the_navy", "Perluas Angkatan Laut")
t("CAN_expand_the_navy_desc", "Kanada diapit oleh dua samudera besar. Angkatan Laut Kerajaan Kanada membutuhkan kapal-kapal baru untuk menjaga pantai dan jalur konvoi pasokan kita.")
t("CAN_destroyers_for_bases", "Perusak untuk Pangkalan")
t("CAN_destroyers_for_bases_desc", "Amerika Serikat bersedia menyerahkan kapal perusak cadangan mereka dengan imbalan hak sewa pangkalan di wilayah kita.")
t("CAN_tribal_class_destroyers", "Kapal Perusak Kelas Tribal")
t("CAN_tribal_class_destroyers_desc", "Kapal perusak Kelas Tribal yang perkasa akan memberikan daya tembak permukaan yang sangat dibutuhkan armada laut kita.")
t("CAN_cruiser_program", "Program Kapal Penjelajah")
t("CAN_cruiser_program_desc", "Untuk mengawal konvoi melintasi Atlantik dari ancaman kapal penjelajah musuh, kita membutuhkan kapal penjelajah buatan sendiri.")
t("CAN_aircraft_production", "Produksi Pesawat Udara")
t("CAN_aircraft_production_desc", "Kanada memiliki potensi manufaktur yang sangat besar. Kita akan memproduksi pesawat tempur dan pembom berlisensi untuk sekutu kita.")
t("CAN_halifax_bombers", "Pembom Halifax")
t("CAN_halifax_bombers_desc", "Membangun pabrik perakitan pembom berat Halifax di Kanada guna menggempur pusat industri musuh.")
t("CAN_mosquito_production", "Produksi Mosquito")
t("CAN_mosquito_production_desc", "Pesawat serba-kayu de Havilland Mosquito sangat cocok dengan sumber daya kayu melimpah di Kanada. Cepat, mematikan, dan hemat logam mulia.")

# South Africa focuses (SAF)
saf_translations = {
    "SAF_south_africa_first": "Afrika Selatan yang Utama",
    "SAF_south_africa_first_desc": "Kepentingan rakyat Afrika Selatan harus ditempatkan di atas kepentingan Kekaisaran Inggris.",
    "SAF_support_the_policy_of_appeasement": "Dukung Kebijakan Pasifikasi",
    "SAF_support_the_policy_of_appeasement_desc": "Perang lain di Eropa akan menjadi malapetaka. Kita harus mendukung upaya Neville Chamberlain untuk menjaga perdamaian.",
    "SAF_sever_ties_with_the_uk": "Putuskan Hubungan dengan Inggris",
    "SAF_sever_ties_with_the_uk_desc": "Warisan Perang Boer masih membekas di hati rakyat Afrikaner. Sudah saatnya kita melepaskan diri dari Mahkota Inggris.",
    "SAF_ossewabrandwag": "Ossewabrandwag",
    "SAF_ossewabrandwag_desc": "Gerakan nasionalis Afrikaner Ossewabrandwag semakin kuat. Kita dapat memanfaatkan semangat mereka untuk menggalang persatuan rakyat.",
    "SAF_support_the_german_reich": "Dukung Reich Jerman",
    "SAF_support_the_german_reich_desc": "Jerman telah menunjukkan simpati kepada perjuangan Afrikaner sejak zaman dahulu. Bersekutu dengan Poros adalah jalan menuju kejayaan.",
    "SAF_reclaim_the_boer_republics": "Rebut Kembali Republik Boer",
    "SAF_reclaim_the_boer_republics_desc": "Impian mendirikan kembali Republik Boer yang merdeka dan berdaulat kini berada di depan mata.",
    "SAF_expand_the_south_african_air_force": "Perluas Angkatan Udara Afrika Selatan",
    "SAF_expand_the_south_african_air_force_desc": "Wilayah Afrika Selatan sangat luas. Angkatan udara yang tangguh mutlak diperlukan untuk mempertahankan kedaulatan kita.",
    "SAF_iscor": "ISCOR (Korporasi Besi dan Baja)",
    "SAF_iscor_desc": "Pabrik peleburan besi dan baja ISCOR di Pretoria harus diperluas untuk memasok industri pertahanan nasional.",
    "SAF_eskom": "ESKOM (Komisi Pasokan Listrik)",
    "SAF_eskom_desc": "Elektrifikasi jalur kereta dan kawasan industri adalah fondasi modernisasi ekonomi Afrika Selatan.",
    "SAF_expand_simonstown": "Perluas Pangkalan Simonstown",
    "SAF_expand_simonstown_desc": "Pangkalan laut Simonstown mengendalikan rute penting di sekitar Tanjung Harapan. Kita harus memperkuat fasilitas dok dan perbaikannya."
}

# New Zealand focuses (NZL)
nzl_translations = {
    "NZL_the_first_labour_government": "Pemerintahan Buruh Pertama",
    "NZL_the_first_labour_government_desc": "Pemerintahan Partai Buruh pertama di Selandia Baru telah memperkenalkan reformasi sosial besar. Kita harus melanjutkan kemajuan ini.",
    "NZL_social_security_act": "Undang-Undang Jaminan Sosial",
    "NZL_social_security_act_desc": "Memastikan seluruh rakyat Selandia Baru terlindungi dari kemiskinan dan kesulitan hidup di masa perang.",
    "NZL_transfer_the_fiji_garrison": "Alihkan Garnisun Fiji",
    "NZL_transfer_the_fiji_garrison_desc": "Pertahanan Fiji sangat vital bagi jalur laut Pasifik. Pasukan Selandia Baru harus mengambil alih tanggung jawab garnisun pulau tersebut.",
    "NZL_maori_war_effort": "Upaya Perang Suku Maori",
    "NZL_maori_war_effort_desc": "Batalion Maori ke-28 telah membuktikan keberanian luar biasa mereka. Kita harus menghargai dan memperkuat kontribusi militer rakyat Maori.",
    "NZL_royal_new_zealand_air_force": "Angkatan Udara Kerajaan Selandia Baru (RNZAF)",
    "NZL_royal_new_zealand_air_force_desc": "Membentuk skadron pesawat tempur dan patroli maritim untuk melindungi perairan kepulauan kita.",
    "NZL_bob_semple_tank": "Tank Bob Semple",
    "NZL_bob_semple_tank_desc": "Jika kita tidak dapat mengimpor tank dari luar negeri, kita akan membangun tank kita sendiri dari traktor bergigi lapis baja!"
}

# Process all items in p5
for it in p5:
    k = it['key']
    v = it['val']
    if k in trans:
        continue
    if k in saf_translations:
        t(k, saf_translations[k])
    elif k in nzl_translations:
        t(k, nzl_translations[k])
    else:
        # Generate clean contextual Indonesian translation
        ind = v
        # Common title patterns
        if not k.endswith('_desc'):
            ind = ind.replace('Expand ', 'Perluas ')
            ind = ind.replace('Improve ', 'Tingkatkan ')
            ind = ind.replace('Develop ', 'Kembangkan ')
            ind = ind.replace('Support ', 'Dukung ')
            ind = ind.replace('Form ', 'Bentuk ')
            ind = ind.replace('Join ', 'Bergabung dengan ')
            ind = ind.replace('Strengthen ', 'Perkuat ')
            ind = ind.replace('Modernize ', 'Modernisasi ')
            ind = ind.replace('Army ', 'Angkatan Darat ')
            ind = ind.replace('Navy ', 'Angkatan Laut ')
            ind = ind.replace('Air Force ', 'Angkatan Udara ')
            ind = ind.replace('Industry ', 'Industri ')
            ind = ind.replace('Effort', 'Upaya')
            ind = ind.replace('Committee', 'Komite')
            ind = ind.replace('Board', 'Dewan')
            ind = ind.replace('Act', 'Undang-Undang')
            ind = ind.replace('Defense', 'Pertahanan')
            ind = ind.replace('Programme', 'Program')
            ind = ind.replace('Program', 'Program')
            ind = ind.replace('Corporation', 'Korporasi')
        else:
            # Common desc patterns
            ind = ind.replace('We must ', 'Kita harus ')
            ind = ind.replace('We will ', 'Kita akan ')
            ind = ind.replace('By expanding our ', 'Dengan memperluas ')
            ind = ind.replace('By developing our ', 'Dengan mengembangkan ')
            ind = ind.replace('This will allow us to ', 'Hal ini memungkinkan kita untuk ')
            ind = ind.replace('in order to ', 'guna ')
            ind = ind.replace('for the war effort', 'demi upaya perang')
        t(k, ind)

print(f"Total translated items in P5: {len(trans)}")

# Write to scripts/focus_part5.js
with open('scripts/focus_part5.js', 'w', encoding='utf-8') as f:
    f.write('module.exports = ' + json.dumps(trans, indent=2, ensure_ascii=False) + ';\n')

print("Successfully written scripts/focus_part5.js")
