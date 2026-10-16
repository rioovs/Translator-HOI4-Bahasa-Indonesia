# Hearts of Iron IV - Bahasa Indonesia

[![Release](https://img.shields.io/github/v/release/rioovs/Translator-HOI4-Bahasa-Indonesia?color=blue&label=Release%20v1.0.1)](https://github.com/rioovs/Translator-HOI4-Bahasa-Indonesia/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Game Version](https://img.shields.io/badge/HOI4%20Tested-v1.19.3.0%20Postern-green.svg)](https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/)
[![Translation Status](https://img.shields.io/badge/Translation-100%25%20Completed-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-blue.svg)]()
[![DLC Support](https://img.shields.io/badge/DLC%20Support-46%2B%20DLCs%20Included-orange.svg)]()

Terjemahan Bahasa Indonesia untuk Hearts of Iron IV (game dasar dan seluruh DLC) yang dipasang langsung ke berkas instalasi game tanpa mod atau playset launcher.

Repositori ini mencakup 208 berkas lokalisasi (129.562 kunci terjemahan) dan aplikasi installer mandiri (`HOI4_Indonesian_Installer.exe`) untuk mendeteksi folder game, memeriksa versi, memindai DLC, dan mengonfigurasi launcher Paradox Dowser secara otomatis.

---

## Download

Unduh file installer langsung melalui tombol rilis di bawah:

> **[Download HOI4_Indonesian_Installer.exe (v1.0.1)](https://github.com/rioovs/Translator-HOI4-Bahasa-Indonesia/releases/download/v1.0.1/HOI4_Indonesian_Installer.exe)**  
> *Ukuran berkas: 17.16 MB • Bebas instalasi Python*

---

## Fitur Installer

- **Deteksi folder otomatis**: Memindai registry Windows, pustaka Steam (`libraryfolders.vdf`), dan folder instalasi umum tanpa konfigurasi manual.
- **Pemeriksaan versi game**: Membaca `launcher-settings.json`. Memvalidasi kompatibilitas dengan versi rekomendasi (`v1.19.3.0`) dan memunculkan peringatan jika versi berbeda.
- **Pemindaian 46+ DLC**: Membaca folder `dlc/` dan berkas `.dlc` untuk memverifikasi seluruh ekspansi aktif (Götterdämmerung, Thunder at Our Gates, No Step Back, Man the Guns, La Résistance, dll).
- **Konfigurasi launcher Paradox (Dowser)**: Mengedit `settings-layout.json` agar dropdown bahasa resmi menampilkan label "Bahasa Indonesia".
- **Pengaturan default pemain**: Memperbarui `settings.txt` dan `pdx_settings.txt` di dokumen pengguna agar game langsung berjalan dalam Bahasa Indonesia.
- **Pencadangan dan pemulihan terisolasi**: Salinan cadangan folder bahasa disimpan di `_hoi4_id_backups/` agar terisolasi dari pemindaian mesin game HOI4, lengkap dengan opsi pemulihan satu klik.
- **Executable mandiri**: Berkas tunggal `.exe` tanpa perlu menginstal Python di komputer pengguna.

---

## Cara Penggunaan

### Pengguna Akhir (Pemain)
1. Unduh **[HOI4_Indonesian_Installer.exe](https://github.com/rioovs/Translator-HOI4-Bahasa-Indonesia/releases/download/v1.0.0/HOI4_Indonesian_Installer.exe)** dari [GitHub Releases](https://github.com/rioovs/Translator-HOI4-Bahasa-Indonesia/releases/latest).
2. Jalankan `HOI4_Indonesian_Installer.exe`.
3. Aplikasi akan mendeteksi folder instalasi game secara otomatis. Jika game berada di folder kustom, klik **Pilih Folder...**.
4. Periksa ringkasan versi game dan DLC yang terdeteksi.
5. Klik **PASANG BAHASA INDONESIA**.
6. Buka game melalui Paradox Launcher (Dowser) atau tombol **Buka Game / Dowser**.

---

## Cara Kerja Teknis

### Temuan Analisis Biner

Analisis terhadap `hoi4.exe` mengungkap:
- Engine Clausewitz memvalidasi tag bahasa secara hardcoded dalam tabel internal (`systemsettings.cpp`).
- Tag yang diterima: `l_english`, `l_braz_por`, `l_german`, `l_french`, `l_spanish`, `l_polish`, `l_russian`, `l_japanese`, `l_simp_chinese`, `l_korean`.
- Tag baru seperti `l_indonesian` ditolak oleh engine dan memicu fallback ke bahasa Inggris atau crash.
- **Solusi**: Menggunakan slot `l_braz_por` sebagai penampung terjemahan Indonesia, lalu mengubah label tampilannya di `languages.yml` dan `settings-layout.json` menjadi "Bahasa Indonesia".

### Mekanisme Pemuatan Berkas

Engine Clausewitz memindai direktori `localisation/` secara rekursif:
- Setiap berkas `*.yml` di subdirektori manapun di dalam `localisation/` akan dibaca.
- Folder cadangan tidak boleh diletakkan di dalam `localisation/` karena akan ikut dibaca engine dan merusak terjemahan.

---

## Struktur Repositori

```
rea-hoi4-indonesia/
├── app/                               # Modul aplikasi installer Python
│   ├── __init__.py
│   ├── core.py                        # Logika deteksi, DLC scanner, patcher & instalasi
│   ├── dlc_db.py                      # Metadata dan nama 46+ DLC HOI4
│   └── gui.py                         # Antarmuka Tkinter modern
├── dist/
│   └── HOI4_Indonesian_Installer.exe  # Executable standalone siap pakai
├── localisation/
│   ├── braz_por/                      # 208 berkas terjemahan Bahasa Indonesia (UTF-8 BOM)
│   └── languages.yml                  # Konfigurasi nama bahasa antarmuka HOI4
├── scripts/
│   ├── check_syntax_errors.py         # Skrip verifikasi sintaks YAML
│   ├── sanitize_and_repair_all.py     # Skrip pembersih token dan pemeriksa BOM
│   └── translation_pipeline/          # Arsip skrip batch translasi
├── main.py                            # Titik masuk aplikasi (GUI & CLI)
├── build_installer.py                 # Skrip build PyInstaller
├── LICENSE                            # Lisensi MIT
├── README.md                          # Dokumentasi utama
└── .gitignore
```

---

## Cakupan Berkas

| Metrik | Nilai |
|--------|-------|
| Total berkas di `braz_por/` | 208 berkas (100% Bahasa Indonesia) |
| Total baris | 147.696 baris |
| Total kunci terjemahan | 130.911 kunci |
| Pohon fokus nasional | Selesai (seluruh negara dan DLC) |
| Event dan keputusan | Selesai (seluruh event dasar dan DLC) |
| Perancang unit & statistik | Selesai (infanteri, tank, kapal, pesawat, modul) |
| Encoding | UTF-8 with BOM (`0xEF, 0xBB, 0xBF`) pada 208 berkas |

---

## Rincian Berkas Terjemahan

### Antarmuka & Menu Utama
| Berkas | Konten | Status |
|--------|--------|--------|
| `core_l_braz_por.yml` | UI inti, tanggal/bulan, dialog konfirmasi, tooltip perintah pasukan | Selesai (2.280 baris / 2.274 kunci) |
| `frontend_l_braz_por.yml` | Menu utama, pengaturan audio/video/kontrol, multipemain | Selesai (223 kunci) |
| `topbar_l_braz_por.yml` | Bilah atas UI (Stabilitas, Dukungan Perang, PP, Pabrik, Pasukan) | Selesai (84 kunci) |
| `loading_tips_l_braz_por.yml` | Kutipan tokoh sejarah & tips layar loading | Selesai (163 kutipan) |
| `videos_l_braz_por.yml` | Teks tooltip video tutorial | Selesai |
| `musicplayer_l_braz_por.yml` | Kontrol pemutar musik | Selesai |
| `difficulty_l_braz_por.yml` | Tingkat kesulitan permainan | Selesai |
| `chat_l_braz_por.yml` | Teks obrolan multipemain | Selesai |

### Perancang Peralatan & Divisi Militer
| Berkas | Konten | Status |
|--------|--------|--------|
| `designer_l_braz_por.yml` | Antarmuka umum perancang peralatan, slot modul, peran tempur, dan penjelasan statistik | Selesai (528 baris / 496 kunci) |
| `tank_modules_l_braz_por.yml` | Perancang Tank: sasis tank ringan/sedang/berat, kubah, suspensi, mesin diesel/bensin, lapis baja, autoloader, modul khusus | Selesai (523 baris / 499 kunci) |
| `ship_modules_l_braz_por.yml` | Perancang Kapal: meriam utama/sekunder, tabung torpedo, sonar, radar kendali tembakan, mesin turbin/nuklir, sabuk lapis baja | Selesai (1.401 baris / 1.367 kunci) |
| `plane_designer_l_braz_por.yml` | Perancang Pesawat: badan pesawat, mesin piston/jet/roket, senapan mesin, meriam udara, tangki bahan bakar cadangan, avionik | Selesai (490 baris / 479 kunci) |
| `unit_l_braz_por.yml` | Perancang Divisi Infanteri: batalion infanteri, artileri, kavaleri, bermotor, mekanis, kompi bantuan (zeni, medis, pengintaian, logistik), statistik tempur | Selesai (806 baris / 792 kunci) |

### Riset & Pohon Teknologi
| Berkas | Konten | Status |
|--------|--------|--------|
| `research_l_braz_por.yml` | Seluruh pohon riset: Infanteri, Kompi Bantuan, Lapis Baja, Artileri, Udara, Laut, Teknik Rekayasa & Elektronik, Industri, Doktrin & MIO | Selesai (1.366 baris / 1.347 kunci) |

### Ekspansi Jerman, Götterdämmerung & Waking the Tiger
| Berkas | Konten | Status |
|--------|--------|--------|
| `wuw_focus_l_braz_por.yml` | Pohon fokus Götterdämmerung: 978+ fokus baru Jerman (Rencana 4 Tahun, Proyek Khusus Wunderwaffe, Inner Circle, MEFO, Wehrmacht), Austro-Hungaria, Austria, Hungaria, Belgia, Kongo | Selesai (4.049 baris / 3.071 kunci) |
| `wuw_events_l_braz_por.yml` | Peristiwa Götterdämmerung: politik internal Jerman, krisis MEFO, proyek atom Mannheim, serangan Big Ben, peristiwa perang | Selesai (3.535 baris / 2.714 kunci) |
| `wtt_focus_l_braz_por.yml` | Pohon fokus Waking the Tiger: Tiongkok Nasionalis, Tiongkok Komunis, Panglima Perang, Restorasi Showa Jepang, Manchukuo | Selesai (748 baris / 747 kunci) |
| `wtt_events_l_braz_por.yml` | Peristiwa Waking the Tiger: Jerman Alt-History (Oppose Hitler, Kembalinya Kaiser Wilhelm II), kudeta militer Jepang, Perang Saudara Tiongkok | Selesai (1.142 baris / 1.118 kunci) |

### Peralatan & Kendaraan Perang
| Berkas | Konten | Status |
|--------|--------|--------|
| `equipment_l_braz_por.yml` | Senjata infanteri, artileri, tank, kendaraan, rudal | Selesai (4.630 baris / 4.252 kunci) |
| `equip_air_l_braz_por.yml` | Pesawat tempur, pembom, helikopter, rudal udara | Selesai (2.006 kunci) |
| `equip_naval_l_braz_por.yml` | Lambung kapal, varian kapal perang, armada laut | Selesai (1.306 baris / 1.164 kunci) |
| `traits_l_braz_por.yml` | Sifat jenderal, marsekal, laksamana, penasihat, agen | Selesai (2.755 baris / 2.585 kunci) |

### Politik, Ideologi & Fokus Nasional Dasar
| Berkas | Konten | Status |
|--------|--------|--------|
| `focus_l_braz_por.yml` | Pohon fokus utama (Jerman, Soviet, Inggris, Prancis, AS, Jepang, Italia, dll) beserta seluruh deskripsi | Selesai (2.583 baris / 2.488 kunci) |
| `military_industrial_organization_l_braz_por.yml` | Organisasi Industri Militer (MIO), perancang senjata, kebijakan & riset | Selesai (2.606 baris / 1.807 kunci) |
| `ideas_l_braz_por.yml` | Semangat nasional, hukum ekonomi, hukum wajib militer, penasihat | Selesai (2.781 baris / 2.717 kunci) |
| `politics_l_braz_por.yml` | Panel politik & hukum konstitusi | Selesai (185 kunci) |
| `parties_l_braz_por.yml` | Nama partai & ideologi seluruh negara dunia | Selesai (1.751 baris / 1.676 kunci) |
| `modifiers_l_braz_por.yml` | Pengubah statistik nasional (output pabrik, kecepatan konstruksi, dll) | Selesai (2.630 baris / 2.582 kunci) |
| `bookmarks_l_braz_por.yml` | Skenario 1936 Blitzkrieg & 1939 Gathering Storm | Selesai (116 kunci) |

### Keputusan & Peristiwa Sejarah
| Berkas | Konten | Status |
|--------|--------|--------|
| `decisions_l_braz_por.yml` | Antarmuka keputusan, kategori keputusan, mobilisasi ekonomi, propaganda perang, aksi darurat | Selesai (354 baris / 290 kunci) |
| `events_l_braz_por.yml` | Peristiwa historis (Anschluss, Munich, Danzig, Perang Spanyol, dll) dan seluruh deskripsi berita | Selesai (3.420 baris / 3.409 kunci) |

### Diplomasi & Hubungan Internasional
| Berkas | Konten | Status |
|--------|--------|--------|
| `diplomacy_l_braz_por.yml` | Opsi diplomasi, justifikasi perang, pakta, aliansi | Selesai (1.760 baris / 1.704 kunci) |
| `war_l_braz_por.yml` | Deklarasi perang & justifikasi | Selesai |
| `peace_l_braz_por.yml` | Konferensi perdamaian, aneksasi, reparasi | Selesai (286 kunci) |
| `waroverview_l_braz_por.yml` | Ringkasan perang & korban | Selesai |
| `game_rules_l_braz_por.yml` | Aturan kustom permainan, jalur AI historis | Selesai (909 baris / 843 kunci) |
| `autonomy_l_braz_por.yml` | Hierarki boneka & otonomi kolonial | Selesai |

### Militer & Pertempuran
| Berkas | Konten | Status |
|--------|--------|--------|
| `combat_l_braz_por.yml` | Lebar tempur, taktik, serangan laut & udara, log tempur | Selesai (401 baris / 400 kunci) |
| `doctrines_l_braz_por.yml` | Doktrin darat, laut, udara, & pasukan khusus | Selesai (859 baris / 845 kunci) |
| `tactics_l_braz_por.yml` | Taktik pertempuran darat | Selesai |
| `theater_l_braz_por.yml` | Pengelolaan teater perang & prioritas pasokan | Selesai |
| `alerts_l_braz_por.yml` | Notifikasi peringatan dalam game | Selesai (236 kunci) |
| `ranks_l_braz_por.yml` | Pangkat perwira militer | Selesai |

### Intelijen & Operasi Rahasia (La Résistance)
| Berkas | Konten | Status |
|--------|--------|--------|
| `operatives_l_braz_por.yml` | Badan intelijen, spymaster, cabang agensi, sifat & rekrutmen agen, kriptologi | Selesai (418 baris / 408 kunci) |
| `lar_operations_l_braz_por.yml` | Operasi infiltrasi rahasia, pencurian cetak biru, sabotase, kudeta, penyelamatan agen | Selesai (349 baris / 346 kunci) |
| `intel_ledger_l_braz_por.yml` | Buku besar intelijen militer, sipil, laut, udara | Selesai (262 kunci) |
| `intelligence_agencies_l_braz_por.yml` | Tingkatan & fasilitas badan intelijen | Selesai (11 kunci) |
| `mapmode_l_braz_por.yml` | Mode peta (Politik, Pasokan, Medan, Faksi, Sumber Daya) | Selesai (68 kunci) |

### Desain Kendaraan, Modul Militer & Statistik Satuan
| Berkas | Konten | Status |
|--------|--------|--------|
| `stats_l_braz_por.yml` | Statistik satuan (Serangan Lunak/Keras, Penetrasi, Pertahanan, Penerobosan, Keandalan) | Selesai (424 kunci) |
| `effects_l_braz_por.yml` | Tooltip efek game, pengubah stat batalion & kompi bantuan | Selesai (487 kunci) |
| `designer_l_braz_por.yml` | Menu perancang templat divisi & Markas Besar AD | Selesai (496 kunci) |
| `plane_designer_l_braz_por.yml` | Perancang pesawat udara & modul mesin/senjata udara | Selesai (479 kunci) |
| `tank_modules_l_braz_por.yml` | Modul perancang tank lapis baja (mesin, suspensi, kubah, persenjataan) | Selesai (499 kunci) |
| `ship_modules_l_braz_por.yml` | Modul kapal perang (meriam cepat, baterai utama, torpedo, radar, sonar) | Selesai (1.367 kunci) |
| `unit_l_braz_por.yml` | Satuan infanteri, kavaleri, mekanis, lapis baja & penugasan komandan | Selesai (792 kunci) |
| `equip_naval_l_braz_por.yml` | Tipe kapal (kapal selam, perusak, penjelajah, kapal tempur, kapal induk) | Selesai (1.164 kunci) |
| `unit_medals_l_braz_por.yml` | Medali divisi, kutipan kehormatan & keahlian komandan | Selesai (359 kunci) |
| `aat_tooltips_l_braz_por.yml` | Tooltip desainer & integrasi MIO | Selesai (242 kunci) |

### Hindia Belanda & Republik Indonesia (TAOG DLC)
| Berkas | Konten | Status |
|--------|--------|--------|
| `TAOG_focus_l_braz_por.yml` | Pohon fokus Hindia Belanda & Indonesia merdeka (Proklamasi, Volksraad, Soekarno, Hatta, Sudirman, Laskar Rakyat, PETA, KNIL) | Selesai (2.230 kunci) |
| `TAOG_events_l_braz_por.yml` | Peristiwa revolusi Indonesia, diplomasi ABDACOM, transfer kekuasaan | Selesai (1.147 kunci) |
| `TAOG_decisions_l_braz_por.yml` | Keputusan Volksraad, industri nasional, bendera Sang Saka Merah Putih | Selesai (751 kunci) |
| `TAOG_ideas_l_braz_por.yml` | Semangat nasional & kabinet menteri Indonesia | Selesai (444 kunci) |

### Nama Negara & Identitas Kosmetik
| Berkas | Konten | Status |
|--------|--------|--------|
| `countries_l_braz_por.yml` | Seluruh nama negara dunia (Indonesia, Hindia Belanda, Jerman, Uni Soviet, dll) | Selesai (4.779 entri) |
| `countries_cosmetic_l_braz_por.yml` | Nama kosmetik ideologi & faksi (Republik Indonesia, Negara Pasundan, Reich Jerman, dll) | Selesai (2.856 entri) |

### Keputusan Sejarah, Penggerebekan & Formasi Negara (DLCs)
| Berkas | Konten | Status |
|--------|--------|--------|
| `wtt_decisions_l_braz_por.yml` | Surat Utang MEFO, penggerebekan anti-komunis/anti-demokratis, formasi Majapahit & Nusantara | Selesai (1.040 kunci) |
| `mtg_decisions_l_braz_por.yml` | Gerbang ke Eropa (Gateway to Europe), relokasi pemerintah Belanda ke Batavia, New Deal AS | Selesai (632 kunci) |
| `special_projects_l_braz_por.yml` | Proyek khusus senjata rahasia (nuklir, kapal selam canggih, jet tempur) | Selesai (1.159 kunci) |
| `bftb_ideas_l_braz_por.yml` | Semangat nasional Battle for the Bosporus (Turki, Yunani, Bulgaria) | Selesai (651 kunci) |
| `bftb_decisions_l_braz_por.yml` | Keputusan krisis Balkan, Konvensi Montreux, faksi Balkan | Selesai (1.013 kunci) |
| `bftb_focus_l_braz_por.yml` | Pohon fokus Turki, Yunani, dan Bulgaria | Selesai (1.246 kunci) |
| `SEA_focus_l_braz_por.yml` | Pohon fokus Asia Tenggara | Selesai (3.542 kunci) |
| `SEA_events_l_braz_por.yml` | Peristiwa kawasan Asia Tenggara | Selesai (2.170 kunci) |
| `SEA_ideas_l_braz_por.yml` | Semangat nasional negara-negara Asia Tenggara | Selesai (950 kunci) |

### Produksi, Logistik & Ekonomi
| Berkas | Konten | Status |
|--------|--------|--------|
| `production_l_braz_por.yml` | Jalur produksi pabrik militer & galangan kapal | Selesai (317 kunci) |
| `trade_l_braz_por.yml` | Perdagangan, impor/ekspor, rute konvoi | Selesai (170 kunci) |
| `constructions_l_braz_por.yml` | Konstruksi infrastruktur, pabrik, benteng, pangkalan | Selesai (146 kunci) |
| `deployment_l_braz_por.yml` | Pelatihan divisi & penempatan pasukan | Selesai (162 kunci) |
| `country_l_braz_por.yml` | Panel negara & stabilitas nasional | Selesai (121 kunci) |
| `buildings_l_braz_por.yml` | Pabrik sipil, pabrik militer, galangan kapal, silo bahan bakar, reaktor | Selesai (225 kunci) |
| `army_l_braz_por.yml` | Divisi, tentara, teater perang, korps perwira | Selesai (286 kunci) |
| `air_l_braz_por.yml` | Misi udara (Keunggulan Udara, CAS, Pengeboman Strategis, Serangan Laut, Kamikaze) | Selesai (470 kunci) |
| `resistance_and_occupation_l_braz_por.yml` | Kepatuhan, hukum darurat perang, penindasan, polisi rahasia | Selesai (184 kunci) |
| `international_market_l_braz_por.yml` | Pasar senjata internasional, kontrak pembelian, pengiriman | Selesai (258 kunci) |
| `military_raids_l_braz_por.yml` | Penyerbuan militer, sabotase pelabuhan, pengeboman presisi | Selesai (438 kunci) |

---

## Konfigurasi Launcher

### `settings-layout.json` (Dowser Launcher)
Mengatur entri bahasa pada antarmuka Paradox Dowser Launcher:
```json
{
  "value": "l_braz_por",
  "displayName": "Bahasa Indonesia"
}
```

### `localisation/languages.yml` (Label In-game)
Menentukan nama bahasa di menu pengaturan game:
```yaml
l_braz_por: "Bahasa Indonesia"
```

### Konfigurasi Dokumen Pemain
- `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\pdx_settings.txt` -> `"language": "l_braz_por"`
- `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\settings.txt` -> `language="l_braz_por"`

---

## Larangan & Batasan Engine

| Tindakan | Alasan |
|----------|--------|
| Menyimpan folder backup di dalam `localisation/` | Engine Clausewitz memindai secara rekursif; berkas cadangan akan ikut terbaca dan menimpa kunci. |
| Mengganti tag `l_braz_por` dengan `l_indonesian` | Engine HOI4 menolak tag yang tidak terdaftar di binary, memicu fallback ke bahasa Inggris atau crash. |
| Mengubah berkas di folder `localisation/english/` | Berkas bahasa Inggris merupakan sumber fallback engine jika ada kunci hilang. |
| Mengaktifkan mod bahasa Indonesia lain secara bersamaan | Menimbulkan tabrakan kunci dan teks tercampur. |

---

## Berkas yang Dipertahankan Asli (7 Berkas)

Tujuh berkas berikut dipertahankan sesuai aslinya karena berisi nama proper, judul lagu, atau variabel tanpa teks naratif:

| Berkas | Alasan |
|--------|--------|
| `germanmarchorder_l_braz_por.yml` | Judul lagu mars militer Jerman (nama proper) |
| `military_industrial_organization_department_l_braz_por.yml` | Variabel generik engine (`$equipment_type$`) tanpa teks naratif |
| `mun_music_l_braz_por.yml` | Judul lagu soundtrack |
| `names_l_braz_por.yml` | Daftar nama orang (`Pablo`) |
| `sabatonsoundtrack_l_braz_por.yml` | Judul lagu Sabaton |
| `togetherforvictory_music_l_braz_por.yml` | Judul lagu DLC Together for Victory |
| `wakingthetiger_music_l_braz_por.yml` | Judul lagu DLC Waking the Tiger |

---

## Panduan Pengembang

### Persyaratan Lingkungan
- Python 3.10+ (Teruji pada Python 3.15)
- Paket kompilasi: `pip install pyinstaller`

### Menjalankan dari Source Code
```bash
# Menjalankan antarmuka grafis (GUI)
python main.py

# Menjalankan mode baris perintah (CLI) dengan deteksi otomatis
python main.py --cli

# Menjalankan mode CLI dengan path manual
python main.py --cli --path "C:\Path\To\Hearts of Iron IV"
```

### Mengompilasi Ulang Executable
Jalankan skrip build otomatis:
```bash
python build_installer.py
```
Skrip akan:
1. Memeriksa kelengkapan 208 berkas terjemahan dan `languages.yml`.
2. Membersihkan direktori build lama.
3. Mengompilasi aplikasi menjadi file executable tunggal via PyInstaller (`--onefile --windowed`).
4. Menyimpan hasil akhir di: `dist/HOI4_Indonesian_Installer.exe`.

---

## Validasi & Skrip Kualitas

| Skrip | Fungsi |
|-------|--------|
| `scripts/check_syntax_errors.py` | Memeriksa 208 berkas terhadap kesalahan kutip, header hilang, atau token rusak. |
| `scripts/sanitize_and_repair_all.py` | Memperbaiki token masking, merapikan escape kutip, dan memastikan header UTF-8 BOM. |
| `build_installer.py` | Membangun executable mandiri. |

Jalankan pemeriksaan berkas sebelum rilis:
```bash
python scripts/check_syntax_errors.py
```

---

## Kontribusi

1. Fork repositori ini.
2. Buat branch fitur (`git checkout -b perbaikan-terminologi`).
3. Lakukan commit perubahan (`git commit -m "Perbaikan istilah divisi kavaleri"`).
4. Jalankan validasi: `python scripts/check_syntax_errors.py`.
5. Buka Pull Request.

---

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

Hearts of Iron IV dan Clausewitz Engine adalah hak cipta terdaftar milik © Paradox Interactive AB. Proyek ini merupakan inisiatif komunitas nirlaba.

---

## Kredit

Pengembang: [rioovs](https://github.com/rioovs)

