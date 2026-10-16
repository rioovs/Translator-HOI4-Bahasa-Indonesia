# -*- coding: utf-8 -*-
"""
Append missing 22 keys to EVENTS_PART1
"""
from translate_taog_events_part1 import EVENTS_PART1

ADDITIONS = {
    "INS_industrial_events.5.t": "[INS_industrial_events_5_t_scripted]",
    "INS_industrial_events.5.desc": "[INS_industrial_events_5_desc_scripted]",
    "INS_industrial_events.5.c": "Kita akan mematok Gulden Hindia ke Dolar AS.",
    "INS_industrial_events.6.t": "Persetujuan yang Lebih Menguntungkan",
    "INS_industrial_events.6.desc": "Biro Kina (Kina Bureau) telah menerima persyaratan kita. Dengan malaria yang melanda separuh wilayah tropis dan tiadanya pengganti kina yang sepadan, mereka tidak punya banyak pilihan. Perjanjian baru ini menjamin bagi kita bagian keuntungan yang jauh lebih besar dari setiap gram kina yang diekspor dari pesisir kita. Pertanyaannya sekarang adalah ke mana keuntungan tak terduga ini harus diarahkan.",
    "INS_industrial_events.6.a": "Investasikan di kota-kota kita.",
    "INS_industrial_events.6.b": "Kembangkan pulau-pulau luar.",
    "INS_industrial_events.6.c": "Perkuat industri militer kita.",
    "INS_industrial_events.28.t": "Pengiriman Karet Diberangkatkan",
    "INS_industrial_events.28.desc": "Konvoi kapal telah memuat tuntas pasokan karet terakhir dan berlayar ke laut lepas. Para pembeli kita akan menerima apa yang mereka bayar, dan pembukuan kita akan mencatat kompensasi yang telah disepakati pada waktunya. Selama dua tahun ke depan, beban biaya transaksi ini akan tercatat dalam neraca keuangan kita, sebuah pengingat akan beratnya tuntutan Depresi Besar bagi kita.",
    "INS_industrial_events.28.a": "Dipahami.",
    "INS_industrial_events.28.b": "Atur pengiriman berikutnya.",
    "INS_industrial_events.36.t": "Pengiriman Minyak Bumi Diberangkatkan",
    "INS_industrial_events.36.desc": "Kapal-kapal tanker telah bertolak dari kilang minyak kita, membawa muatannya menuju pelabuhan para pembeli. Kompensasi telah disetujui dan akan diterima penuh, meski beban penjualan ini akan membebani perekonomian kita selama dua tahun ke depan. Begitulah kenyataan pahit yang ditawarkan dunia kepada kita di masa-masa sulit ini.",
    "INS_industrial_events.36.a": "Dipahami.",
    "INS_industrial_events.36.b": "Atur pengiriman berikutnya.",
    "INS_dutch_events.4.t": "[HOL.GetNameDefCap] Membentuk Program Angkatan Laut [HOL.GetName]-[INS.GetName]",
    "INS_dutch_events.4.desc": "[HOL.GetNameDefCap] telah mengumumkan pembentukan Program Angkatan Laut [HOL.GetName]-[INS.GetName], sebuah prakarsa gabungan guna mereorganisasi dan memperluas armada maritim kita. Keahlian teknis [HOL.GetAdjective] dipadukan dengan kekuatan prajurit [INS.GetAdjective] akan bersama-sama menjadi tulang punggung jaringan pertahanan Pasifik yang baru.",
    "INS_dutch_events.4.a": "Langkah nyata menuju keselamatan bersama.",
    "INS_chaos_events.2.b": "Tidak ada waktu untuk berpolitik, umumkan darurat militer!",
    "INS_chaos_events.4.b": "Partai Sosialis akan mengambil alih kepemimpinan.",
    "INS_chaos_events.4.c": "Bubarkan Republik, Tan Malaka yang akan memimpin kita menuju kejayaan!",
}

EVENTS_PART1.update(ADDITIONS)

# Now overwrite translate_taog_events_part1.py with full dict
import pprint
with open('scripts/translate_taog_events_part1.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n')
    f.write('EVENTS_PART1 = ')
    f.write(pprint.pformat(EVENTS_PART1, indent=4, width=120))
    f.write('\n')

print("Updated EVENTS_PART1 with additions!")
