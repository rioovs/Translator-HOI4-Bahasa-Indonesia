# -*- coding: utf-8 -*-
import json
import re

# Load chunks 1 to 4 translations
with open('trans_chunks_1_to_4.json', 'r', encoding='utf-8') as f:
    desc_map = json.load(f)

# Define translation dictionary for hulls
hull_map = {
    "ship_hull_light_1": "Lambung Perusak Awal",
    "ship_hull_light_2": "Lambung Perusak Dasar",
    "ship_hull_light_3": "Lambung Perusak Ditingkatkan",
    "ship_hull_light_4": "Lambung Perusak Canggih",
    "ship_hull_cruiser": "Lambung Penjelajah",
    "ship_hull_cruiser_1": "Lambung Penjelajah Awal",
    "ship_hull_cruiser_2": "Lambung Penjelajah Dasar",
    "ship_hull_cruiser_3": "Lambung Penjelajah Ditingkatkan",
    "ship_hull_cruiser_4": "Lambung Penjelajah Canggih",
    "ship_hull_cruiser_coastal_defense_ship": "Lambung Kapal Pertahanan Pesisir",
    "ship_hull_cruiser_panzerschiff": "Lambung Kapal Lapis Baja (Panzerschiff)",
    "ship_hull_heavy": "Lambung Kapal Berat",
    "ship_hull_heavy_1": "Lambung Kapal Tempur Awal",
    "ship_hull_heavy_2": "Lambung Kapal Tempur Dasar",
    "ship_hull_heavy_3": "Lambung Kapal Tempur Ditingkatkan",
    "ship_hull_heavy_4": "Lambung Kapal Tempur Canggih",
    "ship_hull_carrier": "Lambung Kapal Induk",
    "ship_hull_carrier_conversion_bb": "Konversi Kapal Tempur Menjadi Kapal Induk",
    "ship_hull_carrier_conversion_ca": "Konversi Penjelajah Menjadi Kapal Induk",
    "ship_hull_carrier_1": "Lambung Kapal Induk Awal",
    "ship_hull_carrier_2": "Lambung Kapal Induk Dasar",
    "ship_hull_carrier_3": "Lambung Kapal Induk Ditingkatkan",
    "ship_hull_carrier_4": "Lambung Kapal Induk Canggih",
    "ship_hull_super_heavy_1": "Lambung Kapal Tempur Superberat",
    "ship_hull_submarine_1": "Lambung Kapal Selam Awal",
    "ship_hull_submarine_2": "Lambung Kapal Selam Dasar",
    "ship_hull_submarine_3": "Lambung Kapal Selam Ditingkatkan",
    "ship_hull_submarine_4": "Lambung Kapal Selam Canggih",
    "ship_hull_cruiser_submarine": "Lambung Kapal Selam Penjelajah",
    "ship_hull_midget_submarine": "Lambung Kapal Selam Mini",
    "ship_hull_torpedo_cruiser": "Lambung Penjelajah Torpedo",
    "ship_hull_pre_dreadnought": "Lambung Pra-Dreadnought",
    "ship_hull_carrier_escort": "Lambung Kapal Induk Pengawal",
    "ship_hull_cruiser_coastal_defense_ship_desc": "Kapal perang lapis baja berukuran relatif kecil dengan meriam berat, dirancang khusus untuk pertahanan perairan pesisir.",
    "ship_hull_cruiser_panzerschiff_desc": "Kapal penjelajah berbobot besar yang memadukan kecepatan penjelajah dengan persenjataan meriam kaliber kapal tempur.",
    "ship_hull_carrier_conversion_bb_desc": "Lambung kapal tempur atau penjelajah tempur yang dialihfungsikan menjadi kapal induk pengangkut pesawat.",
    "ship_hull_carrier_conversion_ca_desc": "Lambung kapal penjelajah berat yang dialihfungsikan menjadi kapal induk pengangkut pesawat.",
    "ship_hull_cruiser_submarine_desc": "Kapal selam berukuran besar dengan daya jelajah sangat jauh dan persenjataan meriam permukaan yang lebih kuat.",
    "ship_hull_midget_submarine_desc": "Kapal selam mini berukuran sangat kompak yang dirancang untuk operasi penyusupan dan serangan gerilya di perairan dangkal.",
    "ship_hull_torpedo_cruiser_desc": "Kapal penjelajah ringan yang dimodifikasi khusus untuk membawa tabung torpedo dalam jumlah sangat banyak."
}

# Define translation dictionary for other generic equipment
other_map = {
    "naval_equipment": "Kapal Perang",
    "submarine_1": "Kapal Selam I",
    "submarine_2": "Kapal Selam II",
    "submarine_3": "Kapal Selam III",
    "submarine_4": "Kapal Selam IV",
    "rocket_submarine": "Kapal Selam Peluncur Rudal",
    "nuclear_missile_submarine": "Kapal Selam Rudal Nuklir",
    "destroyer_1": "Kapal Perusak I",
    "destroyer_2": "Kapal Perusak II",
    "destroyer_3": "Kapal Perusak III",
    "destroyer_4": "Kapal Perusak IV",
    "light_cruiser_1": "Kapal Penjelajah Ringan I",
    "light_cruiser_2": "Kapal Penjelajah Ringan II",
    "light_cruiser_3": "Kapal Penjelajah Ringan III",
    "light_cruiser_4": "Kapal Penjelajah Ringan IV",
    "heavy_cruiser_1": "Kapal Penjelajah Berat I",
    "heavy_cruiser_2": "Kapal Penjelajah Berat II",
    "heavy_cruiser_3": "Kapal Penjelajah Berat III",
    "heavy_cruiser_4": "Kapal Penjelajah Berat IV",
    "battle_cruiser_1": "Kapal Penjelajah Tempur I",
    "battle_cruiser_2": "Kapal Penjelajah Tempur II",
    "battleship_1": "Kapal Tempur I",
    "battleship_2": "Kapal Tempur II",
    "battleship_3": "Kapal Tempur III",
    "battleship_4": "Kapal Tempur IV",
    "SH_battleship_1": "Kapal Tempur Superberat I",
    "SH_battleship_2": "Kapal Tempur Superberat II",
    "carrier_1": "Kapal Induk I",
    "carrier_2": "Kapal Induk II",
    "carrier_3": "Kapal Induk III",
    "carrier_4": "Kapal Induk IV",
    "escort_carrier_1": "Kapal Induk Pengawal I",
    "escort_carrier_2": "Kapal Induk Pengawal II",
    "light_carrier_1": "Kapal Induk Ringan I",
    "light_carrier_2": "Kapal Induk Ringan II",
    "coastal_defense_ship": "Kapal Pertahanan Pesisir",
    "panzerschiff": "Kapal Lapis Baja (Panzerschiff)",
    "pre_dreadnought": "Kapal Tempur Pra-Dreadnought"
}

print(f"Loaded {len(desc_map)} existing descriptions from chunks 1-4.")
print(f"Loaded {len(hull_map)} hull translations.")
print(f"Loaded {len(other_map)} generic equipment translations.")
