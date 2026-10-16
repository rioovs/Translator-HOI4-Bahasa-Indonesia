# -*- coding: utf-8 -*-
import json
import re

# Load raw items for chunks 5, 6, 7
with open('chunks_5_6_7_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Comprehensive Indonesian translation mapping for chunks 5, 6, 7
trans = {}

# Helper to register translations
def add(orig, ind):
    trans[orig] = ind

# Chunk 5 - USA
add('The New York Class battleships were the first US Battleships to be armed with the 14"/45 caliber main guns. Numerous 5"/51 guns provided secondary armament and over 10" of armor.',
    'Kapal tempur Kelas New York adalah kapal tempur pertama AS yang dipersenjatai meriam utama kaliber 14 inci/45. Berbagai meriam 5 inci/51 menjadi persenjataan sekunder didukung lapisan baja lebih dari 10 inci.')

add('The North Carolina Class was a challenging design and was the first battleship class built by the US Navy in 20 years. The US Navy required this class to meet the standards of Washington Naval Treaty, limited to 36,000 tons yet be armed with the 16"/45 caliber guns and have improved armor while being capable of escorting the US Navy\'s fast aircraft carriers.',
    'Kelas North Carolina merupakan rancangan yang menantang dan menjadi kelas kapal tempur pertama yang dibangun Angkatan Laut AS dalam 20 tahun. AL AS mensyaratkan kelas ini mematuhi batas Perjanjian Angkatan Laut Washington seberat 36.000 ton namun tetap bersenjata meriam 16 inci/45 dan lapis baja yang ditingkatkan, serta mampu mengawal kapal induk cepat.')

add('The Iowa Class added all the innovations and capabilities of the earlier North Carolina, but substantially increases its displacement and tactical speed. The Iowa\'s was primarily responsible for escorting carriers groups and was designed with a second role of "cruiser killer" in mind.',
    'Kelas Iowa menggabungkan seluruh inovasi dan kemampuan pendahulunya, North Carolina, dengan peningkatan bobot benaman dan kecepatan taktis yang substansial. Tugas utamanya adalah mengawal gugus kapal induk serta dirancang dengan peran sekunder sebagai "pembunuh penjelajah".')

add('The Illinois Class continued with the design and role defined by the Iowa Class. It maintained speed and armament over armor. The Illinois Class increased the number of 16"/50 caliber guns from 9 to 12 while it also improved boilers and machinery in order to provide more efficient high cruise speeds. Like the Montana Class, initial designs included four 4 6" guns dual turrets, but this was reverted to the dual purpose 5" twin turret emplacements to maximize AA capabilities.',
    'Kelas Illinois melanjutkan rancangan dan peran Kelas Iowa dengan mempertahankan keunggulan kecepatan dan persenjataan. Kelas ini menambah jumlah meriam kaliber 16 inci/50 dari 9 menjadi 12 serta meningkatkan efisiensi permesinan. Penempatan kubah kembar 5 inci serbaguna dimaksimalkan untuk kemampuan pertahanan antipesawat.')

add('The Lexington Class carrier was born from the converted hulls of two Lexington Class battlecruisers in order to conform to the limitations imposed by the Washington Naval Treaty. The class was the first operational carrier class in the US Navy and spent several years improving carrier operations.',
    'Kapal induk Kelas Lexington lahir dari konversi dua lambung penjelajah tempur Kelas Lexington guna mematuhi pembatasan Perjanjian Angkatan Laut Washington. Kelas ini menjadi kelas kapal induk operasional pertama AL AS yang menyempurnakan doktrin operasi penerbangan laut.')

add('The Ranger Class was the first US Navy class designed as a carrier from the keel up. As a small, slow carrier that lacked torpedo defense, the Ranger saw limited service in WW2, but was instrumental in teaching the US Navy how to design and build carriers.',
    'Kelas Ranger adalah kelas pertama AL AS yang sejak awal dirancang khusus sebagai kapal induk. Meski berukuran kecil, lambat, dan minim perlindungan torpedo, Ranger sangat berjasa dalam memberikan pelajaran berharga bagi AL AS dalam merancang kapal induk masa depan.')

add('With the lessons learned from the preceding Lexington, Ranger, and Yorktown classes, the Essex Class was the first class of fleet carriers built without treaty limitations. The Essex Class carrier and its variants would become the backbone of the US Navy throughout WW2 and would serve into the early Cold War.',
    'Berbekal pelajaran dari kelas Lexington, Ranger, dan Yorktown, Kelas Essex adalah kelas kapal induk armada pertama yang dibangun tanpa terikat batasan traktat. Kapal induk Kelas Essex dan variannya menjadi tulang punggung kekuatan AL AS sepanjang PD II hingga awal Perang Dingin.')

add('The Midway Class was the ultimate in US Navy carrier capability at the end of the WW2. Displacing nearly 45,000 tons with a heavily armored flight deck, the Midway was the first carrier to integrate a heavily armored flight deck into the structure of the ship rather than on top of the hull. This allowed for significant increases in flight deck armor without an unacceptable sacrifice in stability.',
    'Kelas Midway merupakan puncak kemampuan kapal induk AL AS pada akhir PD II. Berbobot hampir 45.000 ton dengan geladak terbang berlapis baja tebal yang terintegrasi langsung ke dalam struktur lambung kapal, memastikan stabilitas prima tanpa mengorbankan perlindungan.')

add('In 1920 the construction of the large South Dakota Class battleships was approved by Congress. The South Dakota Class would have been equipped with twelve 16"/50 caliber guns and featured a significantly increased displacement over earlier US battleships. After signing the Washington Naval Treaty, the construction of this class was cancelled in 1922 and the partially built hulls were scrapped.',
    'Pada tahun 1920 pembangunan kapal tempur besar Kelas South Dakota disetujui oleh Kongres AS dengan dua belas meriam 16 inci/50. Namun setelah penandatanganan Traktat Washington, pembangunan kelas ini dibatalkan pada tahun 1922 dan lambung yang sudah dibangun dibongkar.')

add('The Montana Class was bigger and more armored than the Illinois Class, but sacrificed speed in the process. Displacing over 60,000 tons, the Montana Class would have been the largest and most heavily armed US battleships in history with twelve 16"/50 caliber guns in four triple turrets. However with the emergence of the aircraft carrier as the dominant naval weapon, construction was postponed in 1942 and eventually cancelled in 1943.',
    'Kelas Montana dirancang lebih besar dan lebih tebal perisainya dibanding Kelas Illinois, meski harus mengorbankan sedikit kecepatan. Berbobot lebih dari 60.000 ton dengan dua belas meriam 16 inci/50, kelas ini dibatalkan pada 1943 seiring dominasi kapal induk di medan laut.')

# Save to intermediate JSON
with open('trans_chunks_5_6_7_part.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, indent=2, ensure_ascii=False)

print(f"Added {len(trans)} translations so far.")
