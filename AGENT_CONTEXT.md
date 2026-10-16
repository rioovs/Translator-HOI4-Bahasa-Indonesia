# AGENT_CONTEXT.md — HOI4 Indonesian Localization Project

> **Dokumen ini dibuat khusus untuk agen AI agar dapat melanjutkan pekerjaan terjemahan tanpa harus membangun ulang konteks dari awal.**
> Terakhir Diperbarui: 2026-10-15

---

## 1. Ringkasan Proyek

Proyek ini menambahkan **Bahasa Indonesia secara native (tanpa mod)** ke Hearts of Iron IV dengan cara:
1. Menimpa seluruh berkas lokalisasi slot `l_braz_por` (Portugis Brasil) dengan terjemahan Bahasa Indonesia.
2. Mengubah label visual di `languages.yml` dan `settings-layout.json` agar Dowser Launcher menampilkan "Bahasa Indonesia" di dropdown bahasa.

Hasil akhirnya: pemain memilih "Bahasa Indonesia" di Dowser Launcher → game berjalan 100% dalam Bahasa Indonesia tanpa memerlukan mod/playset apapun.

---

## 2. Path Penting

| Variabel | Path |
|----------|------|
| **Direktori instalasi game** | `F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV` |
| **Folder lokalisasi target** | `F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\braz_por\` |
| **Folder sumber (English)** | `F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\english\` |
| **Label bahasa di game** | `F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\localisation\languages.yml` |
| **Konfigurasi dropdown launcher** | `F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV\settings-layout.json` |
| **Direktori proyek kerja** | `f:\New Coding\rea-hoi4-indonesia\` |
| **Mirror hasil terjemahan** | `f:\New Coding\rea-hoi4-indonesia\localisation\braz_por\` |
| **Cadangan file Portugis asli** | `f:\New Coding\rea-hoi4-indonesia\backup_braz_por_original\` |
| **Konfigurasi pemain (Dowser)** | `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\pdx_settings.txt` |
| **Konfigurasi pemain (Engine)** | `%USERPROFILE%\Documents\Paradox Interactive\Hearts of Iron IV\settings.txt` |

---

## 3. Fakta Teknis Kritis (WAJIB DIBACA)

### 3.1 Tag Bahasa yang Valid
Engine Clausewitz HOI4 **hanya** menerima tag berikut (hardcoded di binary `hoi4.exe`):
```
l_english, l_braz_por, l_german, l_french, l_spanish, 
l_polish, l_russian, l_japanese, l_simp_chinese, l_korean
```
Tag `l_indonesian` → **CRASH / fallback ke Inggris**. Jangan pernah membuat file dengan tag itu.

### 3.2 Scanning Rekursif Engine
Engine memindai `localisation/` secara **rekursif**. Konsekuensinya:
- Jangan simpan folder backup di dalam `localisation/` → akan ikut dimuat
- Setiap file `*_l_braz_por.yml` di subdirektori manapun di dalam `localisation/` akan dibaca

### 3.3 Header File Wajib
Setiap file terjemahan harus:
```yaml
﻿l_braz_por:                   ← Baris pertama (ada BOM karakter U+FEFF di depannya)
 KUNCI: "Teks terjemahan"     ← 1 spasi indent
```
- Encoding: **UTF-8 with BOM** (`0xEF 0xBB 0xBF`) — WAJIB, tanpa BOM game bisa skip file
- Header: `l_braz_por:` bukan `l_english:` atau yang lain

### 3.4 Karakter yang Tidak Boleh Diubah
| Token | Contoh | Penjelasan |
|-------|--------|------------|
| Variabel | `$MANPOWER$`, `$VAL|G$`, `$NAME|H$` | Placeholder runtime — jangan terjemahkan |
| Script tags | `[TAG.GetAdjective]`, `[SOV.GetNameDefCap]` | Script token engine |
| Kode warna buka | `§G`, `§R`, `§Y`, `§B`, `§W`, `§H`, `§L` | Color tag Paradox |
| Kode warna tutup | `§!` | Harus seimbang dengan opener |
| Texticon | `£command_power`, `£trigger_no` | Ikon grafis inline |
| Baris baru | `\n` di dalam string | Wajib ditulis sebagai literal escape `\\n`, bukan baris baru fisik |
| Format angka | `|H`, `|Y`, `|G`, `|R`, `|0%`, `|+=%` | Instruksi format nilai |

---

## 4. Status Cakupan Berkas (208 Berkas Selesai / 130.911 Kunci)

### Berkas Terjemahan

#### Antarmuka Inti
- `core_l_braz_por.yml` — 2.280 baris, 2.274 kunci
- `frontend_l_braz_por.yml` — 223 kunci
- `topbar_l_braz_por.yml` — 84 kunci
- `loading_tips_l_braz_por.yml` — 163 kutipan
- `videos_l_braz_por.yml`, `musicplayer_l_braz_por.yml`, `difficulty_l_braz_por.yml`, `chat_l_braz_por.yml`

#### Perancang Peralatan & Divisi (Equipment & Division Designers)
- `designer_l_braz_por.yml` — 528 baris, 496 kunci (Antarmuka umum perancang, aturan slot modul, peran tempur, dan penjelasan statistik)
- `tank_modules_l_braz_por.yml` — 523 baris, 499 kunci (Perancang Tank: sasis tank ringan/sedang/berat, kubah/turret, suspensi, mesin diesel/bensin, rok pelindung lapis baja, autoloader)
- `ship_modules_l_braz_por.yml` — 1.401 baris, 1.367 kunci (Perancang Kapal: meriam utama/sekunder, tabung torpedo, sonar, radar kendali tembakan, mesin turbin/nuklir, sabuk lapis baja)
- `plane_designer_l_braz_por.yml` — 490 baris, 479 kunci (Perancang Pesawat: badan pesawat, mesin piston/jet/roket, senapan mesin, meriam udara, tangki bahan bakar cadangan, avionik radar)
- `unit_l_braz_por.yml` — 806 baris, 792 kunci (Perancang Divisi Infanteri: batalion infanteri, artileri, kavaleri, bermotor, mekanis, kompi bantuan zeni, medis, pengintaian, logistik, dan statistik tempur)

#### Riset & Teknologi (Tech Tree)
- `research_l_braz_por.yml` — 1.366 baris, 1.347 kunci (Infanteri, Bantuan, Lapis Baja, Artileri, Udara, Laut, Elektronik, Industri, Doktrin, MIO)

#### Ekspansi Jerman: Götterdämmerung & Waking the Tiger
- `wuw_focus_l_braz_por.yml` — 4.049 baris, 3.071 kunci (Pohon Fokus ekspansi **Götterdämmerung**: 978+ fokus baru Jerman, Austro-Hungaria, Austria, Hungaria, Belgia, Kongo)
- `wuw_events_l_braz_por.yml` — 3.535 baris, 2.714 kunci (Peristiwa ekspansi **Götterdämmerung**: politik internal Nazi Göring/Himmler/Goebbels/Speer, krisis MEFO, proyek atom Mannheim, perang dunia)
- `wtt_focus_l_braz_por.yml` — 748 baris, 747 kunci (Pohon Fokus **Waking the Tiger**: Tiongkok Nasionalis, Tiongkok Komunis, Warlords, Restorasi Showa Jepang, Manchukuo)
- `wtt_events_l_braz_por.yml` — 1.142 baris, 1.118 kunci (Peristiwa **Waking the Tiger**: Jerman Alt-History Lawan Hitler / Kembalinya Kaiser, kudeta Jepang, Perang Tiongkok, Terusan Suez & Panama)

#### Peralatan & Kendaraan Perang
- `equipment_l_braz_por.yml` — 4.630 baris, 4.252 kunci (Senjata, Tank, Kendaraan, Artileri)
- `equip_air_l_braz_por.yml` — 2.199 baris, 2.006 kunci (Pesawat tempur, Pembom, Helikopter, Rudal)
- `equip_naval_l_braz_por.yml` — 1.306 baris, 1.164 kunci (Lambung kapal, Penjelajah, Kapal Induk, Kapal Selam)
- `traits_l_braz_por.yml` — 2.755 baris, 2.585 kunci (Jenderal, Marsekal, Laksamana, Agen)

#### Politik, Ideologi, Hukum & MIO
- `focus_l_braz_por.yml` — 2.583 baris, 2.488 kunci (Pohon Fokus Utama + 100% deskripsi fokus diterjemahkan, 0 sisa Inggris)
- `military_industrial_organization_l_braz_por.yml` — 2.606 baris, 1.807 kunci (Organisasi Industri Militer MIO)
- `ideas_l_braz_por.yml` — 2.781 baris, 2.717 kunci (Semangat nasional, hukum ekonomi, hukum wajib militer)
- `politics_l_braz_por.yml` — 185 kunci
- `parties_l_braz_por.yml` — 1.751 baris, 1.676 kunci (Nama partai & ideologi seluruh negara)
- `modifiers_l_braz_por.yml` — 2.630 baris, 2.582 kunci
- `bookmarks_l_braz_por.yml` — 116 kunci

#### Peristiwa Sejarah & Keputusan Nasional
- `events_l_braz_por.yml` — 3.420 baris, 3.409 kunci (1.721 judul & deskripsi berita/peristiwa diterjemahkan penuh)
- `decisions_l_braz_por.yml` — 354 baris, 290 kunci (Antarmuka keputusan, propaganda perang, konversi armada, aksi darurat)

#### Diplomasi, Perang & Aturan Permainan
- `diplomacy_l_braz_por.yml` — 1.760 baris, 1.704 kunci
- `war_l_braz_por.yml`, `peace_l_braz_por.yml`, `waroverview_l_braz_por.yml`
- `game_rules_l_braz_por.yml` — 909 baris, 843 kunci
- `autonomy_l_braz_por.yml`

#### Militer, Taktik & Doktrin
- `combat_l_braz_por.yml` — 401 baris, 400 kunci
- `doctrines_l_braz_por.yml` — 859 baris, 845 kunci
- `tactics_l_braz_por.yml`, `theater_l_braz_por.yml`, `alerts_l_braz_por.yml`, `ranks_l_braz_por.yml`

#### Intelijen & Spionase (La Résistance)
- `operatives_l_braz_por.yml` — 418 baris, 408 kunci (Badan intelijen, spymaster, cabang agensi, rekrutmen agen, misi mata-mata, kriptologi)
- `lar_operations_l_braz_por.yml` — 349 baris, 346 kunci (Operasi infiltrasi rahasia, pencurian cetak biru, sabotase, kudeta, penyelamatan agen)
- `intel_ledger_l_braz_por.yml` — 285 baris, 262 kunci
- `intelligence_agencies_l_braz_por.yml` — 12 baris, 11 kunci
- `mapmode_l_braz_por.yml` — 69 baris, 68 kunci

#### Produksi, Logistik & Peta
- `production_l_braz_por.yml` — 324 baris, 317 kunci
- `trade_l_braz_por.yml` — 171 baris, 170 kunci
- `constructions_l_braz_por.yml` — 147 baris, 146 kunci
- `deployment_l_braz_por.yml` — 163 baris, 162 kunci
- `country_l_braz_por.yml` — 124 baris, 121 kunci

#### Desain Kendaraan, Modul Militer & Statistik Satuan
- `stats_l_braz_por.yml` — 424 kunci (Semua statistik satuan: Serangan Lunak/Keras, Penetrasi, Pertahanan, Penerobosan, Keandalan)
- `effects_l_braz_por.yml` — 487 kunci (Tooltip efek game, pengubah stat batalion & kompi bantuan)
- `designer_l_braz_por.yml` — 528 baris, 496 kunci (Antarmuka umum perancang, aturan slot modul, peran tempur, dan penjelasan statistik)
- `plane_designer_l_braz_por.yml` — 490 baris, 479 kunci (Perancang Pesawat: badan pesawat, mesin piston/jet/roket, senapan mesin, meriam udara, tangki bahan bakar cadangan, avionik radar)
- `tank_modules_l_braz_por.yml` — 523 baris, 499 kunci (Perancang Tank: sasis tank ringan/sedang/berat, kubah/turret, suspensi, mesin diesel/bensin, rok pelindung lapis baja, autoloader)
- `ship_modules_l_braz_por.yml` — 1.401 baris, 1.367 kunci (Perancang Kapal: meriam utama/sekunder, tabung torpedo, sonar, radar kendali tembakan, mesin turbin/nuklir, sabuk lapis baja)
- `unit_l_braz_por.yml` — 806 baris, 792 kunci (Perancang Divisi Infanteri: batalion infanteri, artileri, kavaleri, bermotor, mekanis, kompi bantuan zeni, medis, pengintaian, logistik, dan statistik tempur)
- `equip_naval_l_braz_por.yml` — 1.306 baris, 1.164 kunci (Lambung kapal, Penjelajah, Kapal Induk, Kapal Selam)
- `unit_medals_l_braz_por.yml` — 359 kunci (Medali divisi, kutipan kehormatan & keahlian komandan)
- `aat_tooltips_l_braz_por.yml` — 242 kunci (Tooltip desainer & integrasi MIO)

#### Hindia Belanda & Republik Indonesia (TAOG DLC)
- `TAOG_focus_l_braz_por.yml` — 2.230 kunci (Pohon Fokus Hindia Belanda & Indonesia merdeka: Proklamasi Kemerdekaan, Volksraad, Soekarno, Hatta, Sudirman, Laskar Rakyat, PETA, KNIL)
- `TAOG_events_l_braz_por.yml` — 1.147 kunci (Peristiwa revolusi Indonesia, diplomasi ABDACOM, transfer kekuasaan)
- `TAOG_decisions_l_braz_por.yml` — 751 kunci (Keputusan Volksraad, industri nasional, bendera Sang Saka Merah Putih)
- `TAOG_ideas_l_braz_por.yml` — 444 kunci (Semangat nasional & kabinet menteri Indonesia)

#### Nama Negara & Identitas Kosmetik Dunia
- `countries_l_braz_por.yml` — 4.779 entri (Seluruh nama negara dunia dalam Bahasa Indonesia)
- `countries_cosmetic_l_braz_por.yml` — 2.856 entri (Nama kosmetik ideologi & faksi, e.g. Republik Indonesia, Negara Pasundan, Reich Jerman)

#### Keputusan Sejarah, Penggerebekan & Formasi Negara (DLCs)
- `wtt_decisions_l_braz_por.yml` — 1.040 kunci (Surat Utang MEFO, penggerebekan anti-komunis & anti-demokratis, formasi Majapahit & Nusantara)
- `mtg_decisions_l_braz_por.yml` — 632 kunci (Gerbang ke Eropa / Gateway to Europe, relokasi pemerintah Belanda ke Batavia, New Deal AS)
- `special_projects_l_braz_por.yml` — 1.159 kunci (Proyek khusus senjata rahasia: nuklir, jet tempur canggih, kapal selam)
- `bftb_ideas_l_braz_por.yml` — 651 kunci (Semangat nasional Battle for the Bosporus)
- `bftb_decisions_l_braz_por.yml` — 1.013 kunci (Keputusan krisis Balkan, Konvensi Montreux, faksi Balkan)
- `bftb_focus_l_braz_por.yml` — 1.246 kunci (Pohon fokus Turki, Yunani, dan Bulgaria)
- `SEA_focus_l_braz_por.yml` — 3.542 kunci (Pohon fokus Asia Tenggara)
- `SEA_events_l_braz_por.yml` — 2.170 kunci (Peristiwa kawasan Asia Tenggara)
- `SEA_ideas_l_braz_por.yml` — 950 kunci (Semangat nasional Asia Tenggara)

#### Bangunan, Militer & UI Lanjutan
- `buildings_l_braz_por.yml` — 225 kunci (Pabrik sipil, pabrik militer, galangan kapal, silo bahan bakar, reaktor nuklir)
- `army_l_braz_por.yml` — 286 kunci (Divisi, tentara, teater perang, korps perwira)
- `air_l_braz_por.yml` — 470 kunci (Misi udara: Keunggulan Udara, CAS, Pengeboman Strategis, Serangan Laut, Kamikaze)
- `resistance_and_occupation_l_braz_por.yml` — 184 kunci (Kepatuhan, hukum darurat perang, penindasan brutal, polisi rahasia)
- `international_market_l_braz_por.yml` — 258 kunci (Pasar senjata internasional, kontrak pembelian, pengiriman)
- `military_raids_l_braz_por.yml` — 438 kunci (Penyerbuan militer, sabotase pelabuhan, pengeboman presisi)
- `tutorial_l_braz_por.yml` — 187 kunci (Instruksi tutorial permainan)
- `abilities_l_braz_por.yml` — 87 kunci (Kemampuan komando militer)

---

## 5. Aplikasi Installer Mandiri (.exe) & Arsitektur Kode

Aplikasi installer mandiri (`HOI4_Indonesian_Installer.exe`) dibangun menggunakan Python (Tkinter + ttk) dan dikompilasi dengan PyInstaller ke dalam satu berkas `.exe` portabel (~17 MB).

### 5.1 Struktur Kode Aplikasi
- **`app/core.py`**:
  - `find_hoi4_install_paths()`: Memindai registry Windows, file Steam `libraryfolders.vdf`, dan daftar drive sistem untuk mendeteksi folder instalasi secara instan.
  - `get_game_version()`: Membaca `launcher-settings.json`. Menguji terhadap versi rekomendasi (`1.19.3.0`). Jika berbeda, menghasilkan peringatan: *"Kemungkinan beberapa file atau konten baru tidak terjemahkan"*.
  - `scan_dlcs()`: Memindai folder `dlc/`, membaca file metadata `*.dlc`, dan memetakan nama serta kategori ramah pengguna.
  - `patch_dowser_settings_layout()`: Memperbarui `settings-layout.json` agar menu Paradox Dowser menampilkan `"Bahasa Indonesia"`.
  - `patch_user_documents_settings()`: Memperbarui `settings.txt` dan `pdx_settings.txt` agar langsung aktif pada engine game.
  - `install_translations()`: Menyalin 208 berkas dengan UTF-8 BOM dan mencadangkan file asli.
  - `restore_backup()`: Memulihkan cadangan bahasa dan pengaturan asli.
- **`app/dlc_db.py`**: Basis data kamus metadata dan deskripsi bahasa Indonesia untuk 46+ DLC HOI4.
- **`app/gui.py`**: Antarmuka grafis bergaya dark theme HOI4 dengan status badge, progress bar, dan activity log.
- **`main.py`**: Titik masuk utama yang mendukung mode interaktif GUI maupun mode otomatis CLI (`--cli`).
- **`build_installer.py`**: Skrip otomasi kompilasi PyInstaller (`--onefile --windowed`).

### 5.2 Cara Menjalankan & Membangun Installer
```bash
# Menjalankan GUI:
python main.py

# Menjalankan mode CLI (tanpa GUI):
python main.py --cli --path "F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV"

# Mengompilasi ulang file .exe mandiri:
python build_installer.py
```

---

## 6. Validasi Kualitas & Integritas File

- **`scripts/check_syntax_errors.py`**:
  Memvalidasi 100% dari 208 berkas `.yml` terhadap:
  - Header `l_braz_por:`
  - Header UTF-8 BOM (`0xEF, 0xBB, 0xBF`)
  - Tanda kutip internal yang belum di-escape
  - Token masking yang rusak (`__TK*__`)
- **`scripts/sanitize_and_repair_all.py`**:
  Sanitisasi otomatis seluruh file jika ditemukan ketidaksesuaian format.

Jalankan validasi kapan pun sebelum rilis:
```bash
python scripts/check_syntax_errors.py
```

---

## 7. Status Lisensi & Distribusi GitHub

- **Lisensi**: MIT License (`LICENSE`)
- **Git Ignore**: Telah dikonfigurasi (`.gitignore`) untuk mengecualikan temporary builds dan pycache.
- **Target Distribusi**: Pengguna dapat mengunduh `HOI4_Indonesian_Installer.exe` langsung dari GitHub Releases tanpa perlu menginstal Python.

