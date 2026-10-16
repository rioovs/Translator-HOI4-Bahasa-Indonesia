# Hearts of Iron IV - Bahasa Indonesia Localization & Standalone Installer

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Game Version](https://img.shields.io/badge/HOI4%20Tested-v1.19.3.0%20Postern-green.svg)](https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/)
[![Translation Status](https://img.shields.io/badge/Translation-100%25%20Completed-brightgreen.svg)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%2010%20%7C%2011-blue.svg)]()
[![DLC Support](https://img.shields.io/badge/DLC%20Support-46%2B%20DLCs%20Included-orange.svg)]()

> **Proyek Open Source Lokalisasi Penuh Bahasa Indonesia untuk Hearts of Iron IV beserta Aplikasi Penginstal Otomatis (.exe) Modern.**

Proyek ini menghadirkan terjemahan komprehensif 100% Bahasa Indonesia untuk seluruh konten Hearts of Iron IV (game dasar + seluruh DLC hingga ekspansi terbaru *Götterdämmerung* dan *Thunder at Our Gates*). Terjemahan dipasang langsung ke dalam file game tanpa memerlukan mod, playset launcher yang rumit, ataupun modifikasi file biner `.exe`.

Aplikasi installer mandiri (`HOI4_Indonesian_Installer.exe`) secara otomatis mendeteksi folder instalasi game, memeriksa kompatibilitas versi, memindai DLC aktif, menyalin file terjemahan berformat UTF-8 BOM, serta mengonfigurasi Paradox Dowser Launcher agar menampilkan opsi **"Bahasa Indonesia"**.

---

## ⚡ Fitur Utama Aplikasi Installer (.exe)

- 🔍 **Deteksi Otomatis Folder Game**: Memindai registry Windows, seluruh Steam Library (`libraryfolders.vdf`), dan folder instalasi umum tanpa perlu mencari manual.
- ⚙️ **Pemeriksaan Versi Game & Peringatan Kompatibilitas**: Membaca `launcher-settings.json`. Mengonfirmasi kompatibilitas dengan versi rekomendasi (`v1.19.3.0`), dan memberikan notifikasi peringatan jika versi game pengguna berbeda.
- 📦 **Pemindaian Otomatis 46+ DLC**: Mendeteksi seluruh DLC dan ekspansi yang terpasang pada game pengguna (Götterdämmerung, Thunder at Our Gates, No Step Back, Man the Guns, Waking the Tiger, La Résistance, By Blood Alone, Arms Against Tyranny, dll).
- 🌐 **Otomatis Konfigurasi Paradox Dowser Launcher**: Memperbarui `settings-layout.json` sehingga dropdown bahasa di launcher menampilkan **"Bahasa Indonesia"** secara resmi.
- 🎮 **Otomatis Setel Pengaturan Game**: Memperbarui `pdx_settings.txt` dan `settings.txt` di dokumen pengguna agar bahasa langsung aktif saat game dijalankan.
- 🛡️ **Pencadangan & Pemulihan Aman (Safe Backup & Restore)**: Otomatis mencadangkan folder bahasa asli sebelum menimpa file, dilengkapi tombol **"Pulihkan Cadangan"** satu klik jika ingin kembali ke bahasa semula.
- 🚀 **Standalone & Portable**: Berjalan mandiri tanpa perlu menginstal Python pada komputer pemain.

---

## 🚀 Panduan Penggunaan Cepat

### Bagi Pemain / Pengguna Akhir (End User):
1. Unduh **`HOI4_Indonesian_Installer.exe`** dari tab [Releases](../../releases).
2. Jalankan file `HOI4_Indonesian_Installer.exe` (Akan langsung membuka antarmuka GUI modern).
3. Aplikasi akan otomatis mendeteksi folder Hearts of Iron IV Anda. Jika Anda menginstal di folder kustom, klik **"Pilih Folder..."**.
4. Periksa status versi game dan daftar DLC yang terdeteksi.
5. Klik **"▶ PASANG BAHASA INDONESIA"**.
6. Selesai! Buka game melalui Paradox Launcher (Dowser) atau langsung klik **"🚀 Buka Game / Dowser"**.

---

## 🔬 Latar Belakang Teknis

### Temuan Analisis Biner (via REA MCP)

Analisis terhadap `hoi4.exe` menggunakan REA (Reverse Engineering Agents) mengungkap:

- Engine Clausewitz memvalidasi tag bahasa secara **hardcoded** dalam tabel internal (`systemsettings.cpp`)
- Daftar tag yang diterima: `l_english`, `l_braz_por`, `l_german`, `l_french`, `l_spanish`, `l_polish`, `l_russian`, `l_japanese`, `l_simp_chinese`, `l_korean`
- Tag baru seperti `l_indonesian` **ditolak** oleh engine Clausewitz dan menyebabkan fallback/crash.
- **Solusi Rekayasa**: Menggunakan slot `l_braz_por` sebagai "wadah" bahasa Indonesia, lalu mengubah label visualnya di `languages.yml` dan `settings-layout.json` menjadi "Bahasa Indonesia".

### Mekanisme Pemuatan Berkas

Engine Clausewitz memindai direktori `localisation/` secara **rekursif**. Ini berarti:
- Seluruh subdirektori di dalam `localisation/` akan dipindai dan dimuat
- File cadangan atau backup yang disimpan di dalam `localisation/` akan ikut terbaca
- **PENTING**: Folder backup selalu disimpan di luar atau dipulihkan bersih agar tidak menimbulkan duplikasi kunci.

---

## 📁 Struktur Repositori Proyek

```
rea-hoi4-indonesia/
├── app/                               ← Modul Aplikasi Installer (Python)
│   ├── __init__.py
│   ├── core.py                        ← Engine logika deteksi, DLC, patching & instalasi
│   ├── dlc_db.py                      ← Basis data 46+ metadata & kategori DLC HOI4
│   └── gui.py                         ← Antarmuka Tkinter modern dark-theme
├── dist/
│   └── HOI4_Indonesian_Installer.exe  ← File executable standalone siap pakai
├── localisation/
│   ├── braz_por/                      ← 208 berkas terjemahan Bahasa Indonesia (UTF-8 BOM)
│   └── languages.yml                  ← Konfigurasi nama bahasa antarmuka HOI4
├── scripts/
│   ├── check_syntax_errors.py         ← Script verifikasi integritas sintaks YAML
│   ├── sanitize_and_repair_all.py     ← Script pembersih token rusak & pemeriksa BOM
│   └── translation_pipeline/          ← Arsip script batch translasi & kamus data
├── main.py                            ← Entry point aplikasi (GUI & CLI)
├── build_installer.py                 ← Script otomasi kompilasi PyInstaller
├── LICENSE                            ← Lisensi Open Source MIT
├── README.md                          ← Dokumentasi lengkap
└── .gitignore
```


## 📊 Statistik Terjemahan Saat Ini

| Metrik | Nilai |
|--------|-------|
| Total file di `braz_por/` | **208 file** (100% Berbahasa Indonesia) |
| Total baris di seluruh direktori `braz_por/` | **147.696 baris** |
| Total kunci di seluruh direktori `braz_por/` | **130.911 kunci** |
| Status pohon fokus nasional | **100% Selesai** (Seluruh negara & seluruh DLC) |
| Status event & keputusan | **100% Selesai** (Seluruh event & keputusan DLC) |
| Status perancang unit & statistik | **100% Selesai** (Infanteri, Tank, Kapal, Pesawat, Modul) |
| Encoding | **UTF-8 with BOM** (`0xEF, 0xBB, 0xBF`) pada semua 208 berkas |

---

## 📋 Berkas yang Telah Diterjemahkan Penuh

### Antarmuka & Menu Utama
| Berkas | Konten | Status |
|--------|--------|--------|
| `core_l_braz_por.yml` | UI inti, tanggal/bulan, dialog konfirmasi, tooltip perintah pasukan | ✅ Selesai (2.280 baris / 2.274 kunci) |
| `frontend_l_braz_por.yml` | Menu utama, pengaturan audio/video/kontrol, multipemain | ✅ Selesai (223 kunci) |
| `topbar_l_braz_por.yml` | Bilah atas UI (Stabilitas, Dukungan Perang, PP, Pabrik, Pasukan) | ✅ Selesai (84 kunci) |
| `loading_tips_l_braz_por.yml` | Kutipan tokoh sejarah & tips layar loading | ✅ Selesai (163 kutipan) |
| `videos_l_braz_por.yml` | Teks tooltip video tutorial | ✅ Selesai |
| `musicplayer_l_braz_por.yml` | Kontrol pemutar musik | ✅ Selesai |
| `difficulty_l_braz_por.yml` | Tingkat kesulitan permainan | ✅ Selesai |
| `chat_l_braz_por.yml` | Teks obrolan multipemain | ✅ Selesai |

### Perancang Peralatan & Divisi Militer (Equipment & Division Designers)
| Berkas | Konten | Status |
|--------|--------|--------|
| `designer_l_braz_por.yml` | Antarmuka umum perancang peralatan, aturan slot modul, peran tempur, dan penjelasan statistik | ✅ Selesai (528 baris / 496 kunci) |
| `tank_modules_l_braz_por.yml` | Perancang Tank: sasis tank ringan/sedang/berat, kubah (turret), suspensi, mesin diesel/bensin, rok pelindung lapis baja, autoloader, dan modul khusus | ✅ Selesai (523 baris / 499 kunci) |
| `ship_modules_l_braz_por.yml` | Perancang Kapal: meriam utama/sekunder (ringan s.d. super-berat), tabung torpedo, hidrofon/sonar, radar kendali tembakan, ketel uap & mesin turbin/nuklir, sabuk lapis baja | ✅ Selesai (1.401 baris / 1.367 kunci) |
| `plane_designer_l_braz_por.yml` | Perancang Pesawat: badan pesawat, mesin piston/jet/roket, senapan mesin, meriam udara, tangki bahan bakar cadangan, avionik radar | ✅ Selesai (490 baris / 479 kunci) |
| `unit_l_braz_por.yml` | Perancang Divisi Infanteri: batalion infanteri, artileri, kavaleri, bermotor, mekanis, kompi bantuan (zeni, medis, pengintaian, logistik), serta statistik tempur | ✅ Selesai (806 baris / 792 kunci) |

### Riset & Pohon Teknologi
| Berkas | Konten | Status |
|--------|--------|--------|
| `research_l_braz_por.yml` | Seluruh pohon riset: Infanteri, Kompi Bantuan, Lapis Baja, Artileri, Udara, Laut, Teknik Rekayasa & Elektronik, Industri, Doktrin & MIO | ✅ Selesai (1.366 baris / 1.347 kunci) |

### Ekspansi Jerman, Götterdämmerung & Waking the Tiger
| Berkas | Konten | Status |
|--------|--------|--------|
| `wuw_focus_l_braz_por.yml` | Pohon fokus ekspansi **Götterdämmerung**: 978+ fokus baru Jerman (Rencana 4 Tahun, Proyek Khusus *Wunderwaffe*, *Inner Circle*, MEFO, Wehrmacht), Austro-Hungaria, Austria, Hungaria, Belgia, Kongo | ✅ Selesai (4.049 baris / 3.071 kunci) |
| `wuw_events_l_braz_por.yml` | Peristiwa ekspansi **Götterdämmerung**: politik internal Jerman (Göring, Himmler, Goebbels, Speer), krisis MEFO, proyek atom Mannheim, serangan Big Ben, peristiwa perang | ✅ Selesai (3.535 baris / 2.714 kunci) |
| `wtt_focus_l_braz_por.yml` | Pohon fokus **Waking the Tiger**: jalur Tiongkok Nasionalis, Tiongkok Komunis, Panglima Perang (Warlords), Restorasi Showa Kekaisaran Jepang, dan Manchukuo | ✅ Selesai (748 baris / 747 kunci) |
| `wtt_events_l_braz_por.yml` | Peristiwa **Waking the Tiger**: Jerman Alt-History (Lawan Hitler / *Oppose Hitler*, Kembalinya Kaiser Wilhelm II), kudeta militer Jepang, Perang Saudara Tiongkok, Terusan Suez & Panama | ✅ Selesai (1.142 baris / 1.118 kunci) |

### Peralatan & Kendaraan Perang
| Berkas | Konten | Status |
|--------|--------|--------|
| `equipment_l_braz_por.yml` | Senjata infanteri, artileri, tank, kendaraan, rudal | ✅ Selesai (4.630 baris / 4.252 kunci) |
| `equip_air_l_braz_por.yml` | Pesawat tempur, pembom, helikopter, rudal udara | ✅ Selesai (2.006 kunci) |
| `equip_naval_l_braz_por.yml` | Lambung kapal, varian kapal perang, armada laut | ✅ Selesai (1.306 baris / 1.164 kunci) |
| `traits_l_braz_por.yml` | Sifat jenderal, marsekal, laksamana, penasihat, agen | ✅ Selesai (2.755 baris / 2.585 kunci) |

### Politik, Ideologi & Fokus Nasional Dasar
| Berkas | Konten | Status |
|--------|--------|--------|
| `focus_l_braz_por.yml` | Pohon fokus utama (Jerman, Soviet, Inggris, Prancis, AS, Jepang, Italia, dll) + **100% deskripsi fokus** diterjemahkan | ✅ Selesai (2.583 baris / 2.488 kunci) |
| `military_industrial_organization_l_braz_por.yml` | Organisasi Industri Militer (MIO), perancang senjata, kebijakan & riset | ✅ Selesai (2.606 baris / 1.807 kunci) |
| `ideas_l_braz_por.yml` | Semangat nasional, hukum ekonomi, hukum wajib militer, penasihat | ✅ Selesai (2.781 baris / 2.717 kunci) |
| `politics_l_braz_por.yml` | Panel politik & hukum konstitusi | ✅ Selesai (185 kunci) |
| `parties_l_braz_por.yml` | Nama partai & ideologi seluruh negara dunia | ✅ Selesai (1.751 baris / 1.676 kunci) |
| `modifiers_l_braz_por.yml` | Pengubah statistik nasional (output pabrik, kecepatan konstruksi, dll) | ✅ Selesai (2.630 baris / 2.582 kunci) |
| `bookmarks_l_braz_por.yml` | Skenario 1936 Blitzkrieg & 1939 Gathering Storm | ✅ Selesai (116 kunci) |

### Keputusan & Peristiwa Sejarah Dunia
| Berkas | Konten | Status |
|--------|--------|--------|
| `decisions_l_braz_por.yml` | Antarmuka keputusan, kategori keputusan, mobilisasi ekonomi, propaganda perang, aksi darurat | ✅ Selesai (354 baris / 290 kunci) |
| `events_l_braz_por.yml` | Peristiwa historis (Anschluss, Munich, Danzig, Perang Spanyol, dll) + **1.721 judul & deskripsi berita** diterjemahkan penuh | ✅ Selesai (3.420 baris / 3.409 kunci) |

### Diplomasi & Politik Luar Negeri
| Berkas | Konten | Status |
|--------|--------|--------|
| `diplomacy_l_braz_por.yml` | Semua opsi diplomasi, justifikasi perang, perjanjian, aliansi | ✅ Selesai (1.760 baris / 1.704 kunci) |
| `war_l_braz_por.yml` | Deklarasi perang & justifikasi | ✅ Selesai |
| `peace_l_braz_por.yml` | Konferensi perdamaian, aneksasi, reparasi | ✅ Selesai (286 kunci) |
| `waroverview_l_braz_por.yml` | Ringkasan perang & korban | ✅ Selesai |
| `game_rules_l_braz_por.yml` | Aturan kustom permainan, jalur AI historis | ✅ Selesai (909 baris / 843 kunci) |
| `autonomy_l_braz_por.yml` | Hierarki boneka & otonomi kolonial | ✅ Selesai |

### Militer & Pertempuran
| Berkas | Konten | Status |
|--------|--------|--------|
| `combat_l_braz_por.yml` | Lebar tempur, taktik, serangan laut & udara, log pertempuran | ✅ Selesai (401 baris / 400 kunci) |
| `doctrines_l_braz_por.yml` | Doktrin darat, laut, udara, & pasukan khusus | ✅ Selesai (859 baris / 845 kunci) |
| `tactics_l_braz_por.yml` | Taktik pertempuran darat | ✅ Selesai |
| `theater_l_braz_por.yml` | Pengelolaan teater perang & prioritas pasokan | ✅ Selesai |
| `alerts_l_braz_por.yml` | Notifikasi peringatan dalam game | ✅ Selesai (236 kunci) |
| `ranks_l_braz_por.yml` | Pangkat perwira militer | ✅ Selesai |

### Intelijen & Operasi Rahasia (La Résistance)
| Berkas | Konten | Status |
|--------|--------|--------|
| `operatives_l_braz_por.yml` | Badan intelijen, spymaster, cabang agensi, sifat & rekrutmen agen, kriptologi | ✅ Selesai (418 baris / 408 kunci) |
| `lar_operations_l_braz_por.yml` | Operasi infiltrasi rahasia, pencurian cetak biru, sabotase, kudeta, penyelamatan agen | ✅ Selesai (349 baris / 346 kunci) |
| `intel_ledger_l_braz_por.yml` | Buku besar intelijen militer, sipil, laut, udara | ✅ Selesai (262 kunci) |
| `intelligence_agencies_l_braz_por.yml` | Tingkatan & fasilitas badan intelijen | ✅ Selesai (11 kunci) |
| `mapmode_l_braz_por.yml` | Mode peta (Politik, Pasokan, Medan, Faksi, Sumber Daya) | ✅ Selesai (68 kunci) |

### Desain Kendaraan, Modul Militer & Statistik Satuan
| Berkas | Konten | Status |
|--------|--------|--------|
| `stats_l_braz_por.yml` | Semua statistik satuan (Serangan Lunak/Keras, Penetrasi, Pertahanan, Penerobosan, Keandalan, dll) | ✅ Selesai (424 kunci) |
| `effects_l_braz_por.yml` | Tooltip efek game, pengubah stat batalion & kompi bantuan | ✅ Selesai (487 kunci) |
| `designer_l_braz_por.yml` | Menu perancang templat divisi & Markas Besar AD | ✅ Selesai (496 kunci) |
| `plane_designer_l_braz_por.yml` | Perancang pesawat udara & modul mesin/senjata udara | ✅ Selesai (479 kunci) |
| `tank_modules_l_braz_por.yml` | Modul perancang tank lapis baja (mesin, suspensi, kubah, persenjataan) | ✅ Selesai (499 kunci) |
| `ship_modules_l_braz_por.yml` | Modul kapal perang (meriam cepat, baterai utama, torpedo, radar, sonar) | ✅ Selesai (1.367 kunci) |
| `unit_l_braz_por.yml` | Satuan infanteri, kavaleri, mekanis, lapis baja & penugasan komandan | ✅ Selesai (792 kunci) |
| `equip_naval_l_braz_por.yml` | Seluruh tipe kapal (kapal selam, perusak, penjelajah, kapal tempur, kapal induk) | ✅ Selesai (1.164 kunci) |
| `unit_medals_l_braz_por.yml` | Medali divisi, kutipan kehormatan & keahlian komandan | ✅ Selesai (359 kunci) |
| `aat_tooltips_l_braz_por.yml` | Tooltip desainer & integrasi MIO | ✅ Selesai (242 kunci) |

### Hindia Belanda & Republik Indonesia (TAOG DLC)
| Berkas | Konten | Status |
|--------|--------|--------|
| `TAOG_focus_l_braz_por.yml` | Pohon fokus Hindia Belanda & Indonesia merdeka (Proklamasi Kemerdekaan, Volksraad, Soekarno, Hatta, Sudirman, Laskar Rakyat, PETA, KNIL) | ✅ Selesai (2.230 kunci) |
| `TAOG_events_l_braz_por.yml` | Peristiwa revolusi Indonesia, diplomasi ABDACOM, transfer kekuasaan | ✅ Selesai (1.147 kunci) |
| `TAOG_decisions_l_braz_por.yml` | Keputusan Volksraad, industri nasional, bendera Sang Saka Merah Putih | ✅ Selesai (751 kunci) |
| `TAOG_ideas_l_braz_por.yml` | Semangat nasional & kabinet menteri Indonesia | ✅ Selesai (444 kunci) |

### Nama Negara & Identitas Kosmetik Dunia
| Berkas | Konten | Status |
|--------|--------|--------|
| `countries_l_braz_por.yml` | Seluruh nama negara dunia (Indonesia, Hindia Belanda, Jerman, Uni Soviet, dll) | ✅ Selesai (4.779 entri) |
| `countries_cosmetic_l_braz_por.yml` | Nama kosmetik ideologi & faksi (Republik Indonesia, Negara Pasundan, Reich Jerman, dll) | ✅ Selesai (2.856 entri) |

### Keputusan Sejarah, Penggerebekan & Formasi Negara (DLCs)
| Berkas | Konten | Status |
|--------|--------|--------|
| `wtt_decisions_l_braz_por.yml` | Surat Utang MEFO, penggerebekan anti-komunis & anti-demokratis, formasi Majapahit & Nusantara | ✅ Selesai (1.040 kunci) |
| `mtg_decisions_l_braz_por.yml` | Gerbang ke Eropa (Gateway to Europe), relokasi pemerintah Belanda ke Batavia, New Deal AS | ✅ Selesai (632 kunci) |
| `special_projects_l_braz_por.yml` | Proyek khusus senjata rahasia (senjata nuklir, kapal selam canggih, jet tempur) | ✅ Selesai (1.159 kunci) |
| `bftb_ideas_l_braz_por.yml` | Semangat nasional Battle for the Bosporus (Turki, Yunani, Bulgaria) | ✅ Selesai (651 kunci) |
| `bftb_decisions_l_braz_por.yml` | Keputusan krisis Balkan, Konvensi Montreux, faksi Balkan | ✅ Selesai (1.013 kunci) |
| `bftb_focus_l_braz_por.yml` | Pohon fokus Turki, Yunani, dan Bulgaria | ✅ Selesai (1.246 kunci) |
| `SEA_focus_l_braz_por.yml` | Pohon fokus Asia Tenggara | ✅ Selesai (3.542 kunci) |
| `SEA_events_l_braz_por.yml` | Peristiwa kawasan Asia Tenggara | ✅ Selesai (2.170 kunci) |
| `SEA_ideas_l_braz_por.yml` | Semangat nasional negara-negara Asia Tenggara | ✅ Selesai (950 kunci) |

### Produksi, Logistik & Ekonomi
| Berkas | Konten | Status |
|--------|--------|--------|
| `production_l_braz_por.yml` | Jalur produksi pabrik militer & galangan kapal | ✅ Selesai (317 kunci) |
| `trade_l_braz_por.yml` | Perdagangan, impor/ekspor, rute konvoi | ✅ Selesai (170 kunci) |
| `constructions_l_braz_por.yml` | Konstruksi infrastruktur, pabrik, benteng, pangkalan | ✅ Selesai (146 kunci) |
| `deployment_l_braz_por.yml` | Pelatihan divisi & penempatan pasukan | ✅ Selesai (162 kunci) |
| `country_l_braz_por.yml` | Panel negara & stabilitas nasional | ✅ Selesai (121 kunci) |
| `buildings_l_braz_por.yml` | Pabrik sipil, pabrik militer, galangan kapal, silo bahan bakar, reaktor | ✅ Selesai (225 kunci) |
| `army_l_braz_por.yml` | Divisi, tentara, teater perang, korps perwira | ✅ Selesai (286 kunci) |
| `air_l_braz_por.yml` | Misi udara (Keunggulan Udara, CAS, Pengeboman Strategis, Serangan Laut, Kamikaze) | ✅ Selesai (470 kunci) |
| `resistance_and_occupation_l_braz_por.yml` | Kepatuhan, hukum darurat perang, penindasan brutal, polisi rahasia | ✅ Selesai (184 kunci) |
| `international_market_l_braz_por.yml` | Pasar senjata internasional, kontrak pembelian, pengiriman | ✅ Selesai (258 kunci) |
| `military_raids_l_braz_por.yml` | Penyerbuan militer, sabotase pelabuhan, pengeboman presisi | ✅ Selesai (438 kunci) |

---

## 🛠 Cara Penggunaan

### Menjalankan Game dalam Bahasa Indonesia

1. Buka **`F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\dowser.exe`** (Dowser Launcher)
2. Masuk ke **Game Settings** → **SYSTEM** → **Language**
3. Pilih **Bahasa Indonesia**
4. Pastikan **tidak ada mod/playset aktif** di tab Playsets
5. Klik **Play**

> ⚠️ **Penting**: Karena terjemahan dipasang langsung ke file instalasi, **tidak perlu** mengaktifkan mod apapun. Jika ada mod bahasa Indonesia aktif di playset, nonaktifkan untuk menghindari konflik.

### Memperbarui Terjemahan

Untuk menambah atau memperbaiki terjemahan, edit file yang sesuai di:

```
F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\<nama_file>.yml
```

Simpan salinan juga ke:

```
f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\<nama_file>.yml
```

### Aturan Format File Wajib

Setiap file `.yml` harus memenuhi standar berikut:

```yaml
# Baris pertama WAJIB (dengan UTF-8 BOM di awal file):
l_braz_por:
 KUNCI_LOKALISASI: "Teks terjemahan Bahasa Indonesia"
 KUNCI_DENGAN_VARIABEL: "Teks dengan $VARIABEL$ dan §Gwarna§!"
```

| Aturan | Keterangan |
|--------|------------|
| **Encoding** | UTF-8 with BOM (`0xEF 0xBB 0xBF`) wajib di setiap file |
| **Header** | Baris pertama selalu `l_braz_por:` |
| **Indentasi** | 1 spasi sebelum nama kunci |
| **Variabel** | `$NAMA_VARIABEL$` harus dipertahankan persis seperti aslinya |
| **Kode warna** | `§G`, `§R`, `§Y`, `§B`, `§W`, `§H`, `§!` harus seimbang (buka–tutup) |
| **Texticon** | `£nama_icon` harus dipertahankan |
| **Baris baru** | `\n` di dalam string harus ditulis sebagai `\\n` (literal escape), jangan menjadi baris baru fisik |

---

## 🔧 Konfigurasi yang Telah Dimodifikasi

### `settings-layout.json` (Dowser Launcher)

File ini menentukan pilihan bahasa di dropdown Dowser Launcher. Baris terkait (sekitar baris 92):

```json
{
  "value": "l_braz_por",
  "displayName": "Bahasa Indonesia"
}
```

### `localisation/languages.yml` (Label In-game)

File ini menentukan nama bahasa yang muncul di pengaturan dalam game:

```yaml
l_braz_por: "Bahasa Indonesia"
```

### File Konfigurasi Pemain

- `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\pdx_settings.txt` → `"language": "l_braz_por"`
- `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\settings.txt` → `language="l_braz_por"`

---

## 🚫 Hal yang Tidak Boleh Dilakukan

| ❌ Larangan | Alasan |
|-------------|--------|
| Menyimpan folder backup di dalam `localisation/` | Engine memindai rekursif → file Portugis asli terbaca kembali |
| Mengganti tag `l_braz_por` dengan `l_indonesian` | Engine HOI4 menolak tag yang tidak dikenal → crash/fallback |
| Memodifikasi file di folder `localisation/english/` | Ini adalah file sumber yang digunakan engine sebagai fallback |
| Mengaktifkan mod bahasa Indonesia via playset bersamaan | Menyebabkan konflik kunci dan teks tercampur |

---

## 📌 Berkas Tidak Perlu Diterjemahkan (7 file)

File-file berikut **sengaja dibiarkan sama** dengan versi Portugis aslinya karena berisi nama proper atau teks yang sudah universal:

| Berkas | Alasan |
|--------|--------|
| `germanmarchorder_l_braz_por.yml` | Berisi judul lagu Mars Jerman dalam bahasa Jerman (proper noun) |
| `military_industrial_organization_department_l_braz_por.yml` | Berisi variabel generik (`$equipment_type$`) tanpa teks tertulis |
| `mun_music_l_braz_por.yml` | Judul lagu — teks Portugis sangat minimal |
| `names_l_braz_por.yml` | Hanya berisi nama orang (`Pablo`) |
| `sabatonsoundtrack_l_braz_por.yml` | Judul lagu band Sabaton — nama band/lagu dipertahankan |
| `togetherforvictory_music_l_braz_por.yml` | Judul lagu DLC TfV — nama proper |
| `wakingthetiger_music_l_braz_por.yml` | Judul lagu DLC WtT — nama proper |

---

## 🔍 Skrip Utilitas

| Skrip | Fungsi |
|-------|--------|
| `scripts/check_stats.js` | Statistik kunci terjemahan dari 41 file utama |
| `scripts/count_all.js` | Hitung total kunci di seluruh 208 file direktori game |
| `scripts/validate_equipment.py` | Validasi sintaks YAML pada `equipment_l_braz_por.yml` |
## 🛠️ Panduan Pengembang & Kompilasi Mandiri

Jika Anda ingin berkontribusi atau mengompilasi installer `.exe` sendiri:

### 1. Persyaratan Lingkungan
- Python 3.10+ (Teruji pada Python 3.15)
- Modul bawaan: `tkinter`, `winreg`, `json`, `pathlib`
- Paket build: `pip install pyinstaller`

### 2. Menjalankan Kode Sumber Langsung (Development)
```bash
# Menjalankan antarmuka grafis (GUI)
python main.py

# Menjalankan mode baris perintah (CLI) dengan path otomatis
python main.py --cli

# Menjalankan mode CLI dengan path manual
python main.py --cli --path "C:\Path\To\Hearts of Iron IV"
```

### 3. Mengompilasi Menjadi File `.exe` Standalone
Jalankan skrip otomasi build:
```bash
python build_installer.py
```
Skrip ini akan:
1. Memverifikasi kelengkapan seluruh 208 file terjemahan dan `languages.yml`.
2. Membersihkan direktori build lama.
3. Menjalankan PyInstaller dengan mode `--onefile` dan `--windowed`, menanamkan seluruh aset terjemahan ke dalam executable tunggal.
4. Menghasilkan file akhir di: `dist/HOI4_Indonesian_Installer.exe` (Ukuran ~17 MB).

---

## 🔍 Skrip Validasi & Pemeliharaan Kualitas

| Skrip | Fungsi |
|-------|--------|
| `scripts/check_syntax_errors.py` | Memeriksa 100% dari 208 berkas terhadap kesalahan kutip tidak tertutup, token rusak, atau header hilang. |
| `scripts/sanitize_and_repair_all.py` | Memperbaiki otomatis token masking yang rusak (`__TK*__`), merapikan tanda kutip ganda, dan memastikan UTF-8 BOM. |
| `build_installer.py` | Mengompilasi GUI installer menjadi file `.exe` mandiri. |

```bash
# Memverifikasi integritas seluruh berkas sebelum rilis:
python scripts/check_syntax_errors.py
```

---

## 🤝 Berkontribusi

Kontribusi dari komunitas sangat disambut!
1. **Fork** repositori ini ke akun GitHub Anda.
2. Buat branch fitur baru (`git checkout -b fitur-terjemahan-baru`).
3. Lakukan commit perubahan Anda (`git commit -m 'Menambahkan perbaikan istilah militer'`).
4. Pastikan validasi lolos: `python scripts/check_syntax_errors.py`.
5. Buka **Pull Request** ke repositori utama.

---

## 📄 Lisensi

Proyek aplikasi installer dan berkas lokalisasi ini dilisensikan di bawah lisensi terbuka [MIT License](LICENSE).

*Hearts of Iron IV dan Clausewitz Engine adalah hak cipta terdaftar milik © Paradox Interactive AB. Proyek ini merupakan inisiatif komunitas nirlaba yang dibuat oleh dan untuk komunitas pemain Indonesia.*

