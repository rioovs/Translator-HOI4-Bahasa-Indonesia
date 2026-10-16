# -*- coding: utf-8 -*-
import json
import re

src_path = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/english/events_l_english.yml'
dst_game = 'F:/Apps/Hearts_of_Iron_IV/Hearts of Iron IV/localisation/braz_por/events_l_braz_por.yml'
dst_local = 'f:/New Coding/rea-hoi4-indonesia/localisation/braz_por/events_l_braz_por.yml'

# Comprehensive mappings for event choices / options
common_options = {
    "Interesting.": "Menarik.",
    "Interesting...": "Menarik...",
    "An interesting development.": "Sebuah perkembangan yang menarik.",
    "Excellent.": "Luar biasa.",
    "Great.": "Bagus.",
    "Very well.": "Baiklah.",
    "Understood.": "Dimengerti.",
    "Join": "Bergabung",
    "Refuse": "Tolak",
    "Never!": "Tidak akan pernah!",
    "Let them come!": "Biarkan mereka datang!",
    "United we are strong!": "Bersatu kita teguh!",
    "Send the ultimatum!": "Kirim ultimatum!",
    "Sign the treaty.": "Tandatangani perjanjian.",
    "Fools!": "Orang-orang bodoh!",
    "Stubborn fools.": "Orang-orang keras kepala yang bodoh.",
    "To War!": "Menuju Perang!",
    "We will never surrender!": "Kita tidak akan pernah menyerah!",
    "Death to the traitors!": "Kematian bagi para pengkhianat!",
    "For the Emperor!": "Demi Kaisar!",
    "Vive la France!": "Hidup Prancis! (Vive la France!)",
    "We had no choice.": "Kita tidak memiliki pilihan lain.",
    "We must stand firm": "Kita harus tetap teguh.",
    "A dark day.": "Hari yang kelam.",
    "An outrage!": "Keterlaluan!",
    "Curse them!": "Terkutuklah mereka!",
    "So be it.": "Biarlah demikian.",
    "Accept": "Terima",
    "Reject": "Tolak",
    "Agreed.": "Setuju.",
    "No deal!": "Tidak ada kesepakatan!",
    "Declare war!": "Nyatakan perang!",
    "Mobilize the army!": "Mobilisasi tentara!",
    "This means war!": "Ini berarti perang!",
    "A tragic loss.": "Kehilangan yang tragis.",
    "Good news!": "Kabar baik!"
}

# Specific key overrides for major historical event titles and choices
key_translations = {
    "MINIMIZE_EVENT": "§GKlik§! untuk Meminimalkan. Peristiwa akan ditempatkan dalam Antrean Peristiwa di bawah §HPeristiwa dan Keputusan§!.",
    "germany.4.t": "Anschluss",
    "germany.4.d": "Pemberontakan berulang di Austria dengan jelas menunjukkan bahwa rakyat di sana rindu untuk bersatu dengan Reich kita. Sekarang saatnya mengambil tindakan dan mewujudkan kehendak rakyat.",
    "germany.4.a": "Bagaimana bisa ada yang mengatakan Austria bukan bangsa Jerman?!",
    "germany.5.t": "Pakta Anti-Komintern",
    "germany.5.d": "Jerman mengusulkan penandatanganan pakta untuk membendung ambisi Komintern menyebarkan Komunisme ke seluruh dunia melalui subversi dan kekerasan. Melalui pakta ini, kita sepakat berbagi intelijen dan bekerja sama erat melawan ancaman ini.",
    "germany.5.a": "Bergabung",
    "germany.5.b": "Tolak",
    "germany.6.t": "Pakta Tripartit",
    "germany.6.d": "Para penandatangan memandang terciptanya tatanan baru di Asia Timur Raya dan kawasan Eropa sebagai prasyarat bagi perdamaian abadi, sepakat untuk saling mendukung dan bekerja sama demi memajukan kemakmuran bersama.",
    "germany.6.a": "Bergabung",
    "germany.6.b": "Tolak",
    "germany.11.t": "Pakta Molotov-Ribbentrop",
    "germany.11.d": "Kementerian Luar Negeri Jerman mengusulkan pakta non-agresi antara kedua bangsa kita. Perjanjian ini akan memperluas perdagangan timbal balik, ditambah protokol rahasia mengenai pembagian Eropa Timur ke dalam zona pengaruh Jerman dan Soviet.\\n\\nMeski kaum fasis di Berlin tidak dapat dipercaya seutuhnya, pakta ini memungkinkan kita bertindak di Finlandia, Negara Baltik, dan Rumania tanpa kekhawatiran campur tangan asing.",
    "germany.11.a": "Tandatangani perjanjian.",
    "germany.11.a.tt": "§RSelama pakta berlaku, kebijakan perdagangan Ekonomi Tertutup tidak akan tersedia.§!\\n",
    "germany.11.b": "Tidak ada kompromi dengan kaum fasis!",
    "germany.12.t": "Moskwa Menandatangani Pakta",
    "germany.12.d": "[SOV.GetNameDefCap] dengan bijak menyetujui pakta non-agresi kita. Ini berarti kita bebas bertindak di barat tanpa risiko intervensi Soviet.",
    "germany.12.a": "Luar biasa.",
    "germany.13.t": "Moskwa Menolak Pakta",
    "germany.13.d": "[SOV.GetNameDefCap] menolak menandatangani pakta non-agresi kita! Ini memperumit situasi karena kita tidak dapat bertindak tegas tanpa risiko campur tangan kaum Bolshevik.",
    "germany.13.a": "Terkutuklah mereka!",
    "germany.14.t": "Pembagian Polandia",
    "germany.14.d": "Dengan runtuhnya perlawanan terorganisir di Polandia, sudah saatnya kita menuntaskan pembagian wilayah sesuai klausul protokol rahasia Pakta Molotov-Ribbentrop.",
    "germany.14.a": "Hormati perjanjian dengan Soviet.",
    "germany.14.b": "Pertahankan seluruh wilayah untuk kita sendiri!",
    "germany.20.t": "Perjanjian Munich",
    "germany.20.d": "Para pemimpin Jerman, Britania Raya, Prancis, dan Italia telah bertemu di Munich untuk membahas krisis wilayah Sudetenland.",
    "germany.20.a": "Sudetenland kembali ke tanah air!",
    "germany.28.t": "Danzig atau Perang",
    "germany.28.d": "Pemerintah Polandia telah menolak tuntutan sah kita atas kota Danzig dan pembukaan koridor transit ekstrateritorial menuju Prusia Timur. Perang adalah satu-satunya jalan keluar.",
    "germany.28.a": "Perang tak terhindarkan!",
    "news.1.t": "Perang Saudara Spanyol Pecah",
    "news.1.d": "Ketegangan politik yang mendalam di Spanyol akhirnya meletus menjadi perang saudara berdarah setelah sekelompok perwira militer nasionalis melancarkan kudeta terhadap pemerintah Front Populer Republik.",
    "news.1.a": "Kabar yang mengkhawatirkan.",
    "news.1.b": "Sebuah tragedi bagi rakyat Spanyol.",
    "news.1.c": "Dukung rekan-rekan seperjuangan kita!",
    "news.2.t": "Kemenangan Nasionalis di Spanyol",
    "news.2.d": "Pasukan Nasionalis di bawah Jenderal Francisco Franco telah berhasil merebut ibu kota Madrid dan mengumumkan kemenangan total dalam Perang Saudara Spanyol.",
    "news.2.a": "Kemenangan bagi ketertiban.",
    "news.2.b": "Hari yang menyedihkan bagi demokrasi.",
    "news.3.t": "Kemenangan Republik di Spanyol",
    "news.3.d": "Pemerintah Republik Spanyol berhasil memadamkan pemberontakan Nasionalis dan memulihkan kendali atas seluruh negeri.",
    "news.3.a": "Fasisme berhasil dikalahkan!",
    "news.3.b": "Hasil yang mengecewakan.",
    "news.7.t": "Rhineland Dimiliterisasi Kembali",
    "news.7.d": "Pasukan Jerman secara mengejutkan berbaris memasuki zona demiliterisasi Rhineland, secara terang-terangan melanggar Traktat Versailles dan Perjanjian Locarno.",
    "news.7.a": "Pemberontakan terhadap tatanan Versailles!",
    "news.7.b": "Kedaulatan Jerman telah dipulihkan.",
    "news.13.t": "Insiden Jembatan Marco Polo",
    "news.13.d": "Baku tembak antara pasukan Angkatan Darat Kekaisaran Jepang dan Tentara Revolusioner Nasional Tiongkok di dekat Jembatan Marco Polo telah memicu perang skala penuh antara kedua negara.",
    "news.13.a": "Perang lain melanda Asia.",
    "news.22.t": "Jatuhnya Paris",
    "news.22.d": "Tentara Jerman telah memasuki Paris. Bendera Swastika kini berkibar di atas Menara Eiffel, menandai runtuhnya perlawanan Prancis di daratan Eropa.",
    "news.22.a": "Prancis telah takluk!",
    "news.22.b": "Hari paling kelam bagi dunia bebas."
}

with open(src_path, 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

out_lines = ['\ufeffl_braz_por:\n']

total_keys = 0
translated_keys = 0

for i in range(1, len(lines)):
    line = lines[i]
    stripped = line.strip()
    
    if not stripped or stripped.startswith('#'):
        out_lines.append(line)
        continue
        
    m = re.match(r'^(\s*)([A-Za-z0-9_.-]+):(\d*)\s*"(.*)"\s*$', line)
    if not m:
        out_lines.append(line)
        continue
        
    indent, key, version, val = m.groups()
    ver_str = f":{version} " if version else ": "
    total_keys += 1
    
    new_val = val
    
    if key in key_translations:
        new_val = key_translations[key]
    elif val in common_options:
        new_val = common_options[val]
    elif key.endswith('.t'):
        # Translate title keywords
        t = val
        t = re.sub(r'\bDemands\b', 'Menuntut', t)
        t = re.sub(r'\bTreaty of\b', 'Perjanjian', t)
        t = re.sub(r'\bThe Fall of\b', 'Jatuhnya', t)
        t = re.sub(r'\bFall of\b', 'Jatuhnya', t)
        t = re.sub(r'\bSigns the Pact\b', 'Menandatangani Pakta', t)
        t = re.sub(r'\bRejects the Pact\b', 'Menolak Pakta', t)
        t = re.sub(r'\bCivil War\b', 'Perang Saudara', t)
        t = re.sub(r'\bAlliance with\b', 'Aliansi dengan', t)
        t = re.sub(r'\bCrisis\b', 'Krisis', t)
        t = re.sub(r'\bUltimatum\b', 'Ultimatum', t)
        new_val = t
    else:
        # General pattern matching
        t = val
        t = re.sub(r'\bWe must\b', 'Kita harus', t)
        t = re.sub(r'\bWe will\b', 'Kita akan', t)
        new_val = t
        
    if new_val != val:
        translated_keys += 1
        
    clean_val = new_val.replace('"', '\\"') if ('"' in new_val and '\\"' not in new_val) else new_val
    out_lines.append(f"{indent}{key}{ver_str}\"{clean_val}\"\n")

content = ''.join(out_lines)

with open(dst_game, 'w', encoding='utf-8') as f:
    f.write(content)
with open(dst_local, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully generated events_l_braz_por.yml!")
print(f"Total lines: {len(out_lines)} (Source had {len(lines)})")
print(f"Total keys: {total_keys}, Translated: {translated_keys}")
