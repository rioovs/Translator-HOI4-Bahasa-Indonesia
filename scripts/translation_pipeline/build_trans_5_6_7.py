# -*- coding: utf-8 -*-
import json
import re

with open('chunks_5_6_7_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Translation dictionary mapping original English description to Indonesian
trans = {}

# Common replacements and patterns
ship_terms = {
    'battleships': 'kapal tempur',
    'battleship': 'kapal tempur',
    'battlecruisers': 'penjelajah tempur',
    'battlecruiser': 'penjelajah tempur',
    'heavy cruisers': 'penjelajah berat',
    'heavy cruiser': 'penjelajah berat',
    'light cruisers': 'penjelajah ringan',
    'light cruiser': 'penjelajah ringan',
    'armored cruisers': 'penjelajah lapis baja',
    'armored cruiser': 'penjelajah lapis baja',
    'scout cruisers': 'penjelajah pengintai',
    'scout cruiser': 'penjelajah pengintai',
    'protected cruisers': 'penjelajah terlindung',
    'protected cruiser': 'penjelajah terlindung',
    'cruisers': 'penjelajah',
    'cruiser': 'penjelajah',
    'destroyers': 'kapal perusak',
    'destroyer': 'kapal perusak',
    'destroyer escorts': 'perusak pengawal',
    'destroyer escort': 'perusak pengawal',
    'submarines': 'kapal selam',
    'submarine': 'kapal selam',
    'aircraft carriers': 'kapal induk',
    'aircraft carrier': 'kapal induk',
    'carriers': 'kapal induk',
    'carrier': 'kapal induk',
    'coastal defense ships': 'kapal pertahanan pesisir',
    'coastal defense ship': 'kapal pertahanan pesisir',
    'coastal defense battleships': 'kapal tempur pertahanan pesisir',
    'coastal defense battleship': 'kapal tempur pertahanan pesisir',
    'coastal submarines': 'kapal selam pesisir',
    'coastal subs': 'kapal selam pesisir',
    'torpedo boats': 'kapal torpedo',
    'torpedo boat': 'kapal torpedo',
    'dreadnought': 'dreadnought',
    'super-dreadnought': 'super-dreadnought'
}

country_terms = {
    'U.S. Navy': 'AL AS',
    'US Navy': 'AL AS',
    'Royal Navy': 'Angkatan Laut Kerajaan Inggris (Royal Navy)',
    'French Navy': 'Angkatan Laut Prancis',
    'German Navy': 'Angkatan Laut Jerman',
    'Italian Navy': 'Angkatan Laut Italia',
    'Soviet Navy': 'Angkatan Laut Soviet',
    'Imperial Japanese Navy': 'Angkatan Laut Kekaisaran Jepang',
    'Argentine Navy': 'Angkatan Laut Argentina',
    'Brazilian Navy': 'Angkatan Laut Brasil',
    'Chilean Navy': 'Angkatan Laut Chili',
    'Hellenic Navy': 'Angkatan Laut Yunani',
    'Spanish Navy': 'Angkatan Laut Spanyol',
    'Royal Netherlands Navy': 'Angkatan Laut Kerajaan Belanda',
    'Royal Norwegian Navy': 'Angkatan Laut Kerajaan Norwegia',
    'Portuguese Navy': 'Angkatan Laut Portugal',
    'Romanian Navy': 'Angkatan Laut Rumania',
    'Turkish Navy': 'Angkatan Laut Turki',
    'Yugoslav Navy': 'Angkatan Laut Yugoslavia',
    'Swedish Navy': 'Angkatan Laut Swedia',
    'Britain': 'Britania Raya',
    'the U.K.': 'Inggris',
    'the United Kingdom': 'Britania Raya',
    'the United States': 'Amerika Serikat',
    'the U.S.': 'AS',
    'France': 'Prancis',
    'Germany': 'Jerman',
    'Italy': 'Italia',
    'Japan': 'Jepang',
    'the Netherlands': 'Belanda',
    'Norway': 'Norwegia',
    'Sweden': 'Swedia',
    'Denmark': 'Denmark',
    'Spain': 'Spanyol',
    'Greece': 'Yunani',
    'Turkey': 'Turki',
    'Yugoslavia': 'Yugoslavia',
    'Argentina': 'Argentina',
    'Brazil': 'Brasil',
    'Chile': 'Chili',
    'Peru': 'Peru',
    'Canada': 'Kanada',
    'Australia': 'Australia',
    'New Zealand': 'Selandia Baru'
}

print(f"Loaded {len(items)} items to translate.")
