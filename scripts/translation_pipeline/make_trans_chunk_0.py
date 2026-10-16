# -*- coding: utf-8 -*-
import json

trans = {
    # 0 - 9: German News
    "wuw_GER_news.1.t": "Penyatuan Kembali Jerman",
    "wuw_GER_news.1.d": "Setelah sekian lama terpecah belah di antara berbagai negara bagian, oleh perbatasan semena-mena yang memisahkan saudara sebangsa, rakyat Jerman kini dapat kembali bersukacita saat sebuah negara Jerman baru tengah bangkit. Menyusul manuver politik terkini, [FROM.GetLeader] telah membuktikan diri sejalan dengan semangat Bismarck, dan memproklamasikan penyatuan kembali Jerman, sebuah bangsa yang akan berdiri tegak selama seribu tahun!",
    "wuw_GER_news.1.a": "Jerman akhirnya kembali utuh",
    "wuw_GER_news.1.b": "Ini baru permulaan",
    "wuw_GER_news.2.t": "Pemberontakan di Silesia",
    "wuw_GER_news.2.desc": "Untuk keempat kalinya sejak Perjanjian Versailles ditandatangani, para pemberontak di Silesia Jerman bangkit melawan pemerintah. Kali ini [SIL.GetLeader] mengklaim bahwa tujuan tindakan militer mereka terutama adalah untuk mengamankan kemerdekaan negara Silesia sekaligus melindungi rakyat Silesia dari marabahaya selama perang saudara Jerman, kendati pemberontakan sebelumnya lebih bertujuan meraih otonomi di dalam naungan negara Polandia. Hanya waktu yang akan membuktikan apakah mereka sanggup bertahan menghadapi tentara Jerman.",
    "wuw_GER_news.2.a": "Perkembangan situasi yang menarik",
    "wuw_GER_news.2.b": "Mereka sudah pernah mencoba dan gagal sebelumnya",
    "wuw_GER_news.2.c": "Inilah saatnya bagi kita!",
    "wuw_GER_news.2.d": "Semoga kali ini mereka berhasil",

    # 10 - 22: Creditanstalt & Phönix
    "AUS_political_events.1.t": "Nasib Creditanstalt-Bankverein",
    "AUS_political_events.1.desc": "Telah menjadi perhatian kita bahwa merger bank tahun 1934, di mana Creditanstalt yang telah direkapitalisasi mengambil alih seluruh aset dan kewajiban Wiener Bankverein serta operasi layak dari Niederösterreichische Escompte-Gesellschaft, kini menjadi bumerang bagi kita. Hal ini sangat menghambat perkembangan ekonomi kita dan secara tidak sengaja menciptakan semacam monopoli pada sektor keuangan. Mengingat kita kini meregulasi sektor ini, bagaimana kita harus menyikapi situasi tersebut?",
    "AUS_political_events.1.a": "Paling aman adalah membiarkannya apa adanya",
    "AUS_political_events.1.a_tt": "Tidak ada perubahan yang akan dilakukan pada Konsorsium Industri kita. Creditanstalt-Bankverein akan tetap tersedia, memberikan:",
    "AUS_political_events.1.b": "Österreichische Creditanstalt adalah pilihan paling cerdas",
    "AUS_political_events.1.c": "Wiener Bankverein tidak akan mengecewakan kita",
    "AUS_reestablish_creditanstalt": "Creditanstalt-Bankverein akan dibubarkan dan Österreichische Creditanstalt yang baru akan diberikan dukungan penuh kita.",
    "AUS_reestablish_benkverein": "Creditanstalt-Bankverein akan dibubarkan dan Wiener Bankverein yang baru akan diberikan dukungan penuh kita.",
    "AUS_political_events.2.t": "Skandal Asuransi Phönix",
    "AUS_political_events.2.desc": "Tak lama setelah kematian direktur jenderal mereka yang dicintai, Wilhelm Berliner, Asuransi Phönix terjerumus ke dalam kesulitan lebih lanjut. Neraca keuangan yang dipalsukan telah dilaporkan kepada pemerintah oleh direktur baru Eberhard Reininghaus, menyingkap defisit sejak tahun 1929 yang mencapai lebih dari 250 juta schilling.\\n\\nPerusahaan tersebut telah menyatakan bangkrut dan segera menghentikan seluruh operasinya. Asuransi Peserta Perang yang sangat populer telah terhenti secara tiba-tiba, memicu kecaman keras dari banyak pihak yang selama ini bergantung pada pembayaran klaim asuransi tersebut.",
    "AUS_political_events.2.a": "Mengerikan sekali!",
    "AUS_political_events.2.b": "Kita yang akan menanggung pembayaran klaimnya!",
    "AUS_political_events.2.b_tt": "Menanggung asuransi ini akan memungkinkan kita nantinya membangkitkan kembali Asuransi Phönix.",

    # 23 - 30: Remilitarization & Cardinal Innitzer
    "AUS_political_events.3.t": "Remiliterisasi Jerman Memicu Kekhawatiran Luas",
    "AUS_political_events.3.desc": "Remiliterisasi Rheinland baru-baru ini telah menimbulkan kekhawatiran besar di kalangan rakyat kita. Di dalam tubuh pemerintahan kita muncul pertanyaan, 'Mungkinkah kita sasaran berikutnya?' Kendati sang Führer terus-menerus menegaskan bahwa mencaplok Austria tidak termasuk dalam kepentingannya, kita harus mempertimbangkan bahwa tindakan semacam itu kini bukan lagi hal yang mustahil.",
    "AUS_political_events.3.a": "Kita harus bersiap menghadapi skenario terburuk...",
    "AUS_political_events.3.a_tt": "Membuka keputusan §YLangkah-Langkah Anti-Anschluss§!",
    "AUS_political_events.4.t": "Perubahan Sikap",
    "AUS_political_events.4.desc": "Kardinal Theodor Innitzer yang sebelumnya secara terbuka berhaluan fasis belakangan ini mengubah retorikanya secara radikal. Dari yang semula vokal dan terang-terangan mendukung Nazisme serta Führer [GER.GetAdjective], dalam sebuah misa pada tanggal 7 Oktober, ia secara tegas mengambil sikap menentang sang Führer. Alih-alih khotbahnya yang biasa tentang bagaimana massa harus menaruh iman mereka kepada [GER.GetLeader], ia kini mengarahkan mereka kembali kepada Tuhan.\\n\\nKepemimpinan [GER.GetAdjective] geram dan menuntut kita untuk mengambil tindakan tegas.",
    "AUS_political_events.4.a": "Singkirkan pengkhianat itu!",
    "AUS_political_events.4.b": "Herr Innitzer berhak atas pendapatnya sendiri.",

    # 31 - 47: Air Force Partnership
    "AUS_political_events.5.t": "[AUS.GetNameDefCap] Mengharapkan Kerja Sama Antar Angkatan Udara",
    "AUS_political_events.5.desc": "Sebuah usulan dari para diplomat [AUS.GetAdjective] di negara kita baru saja tiba. Setelah dibebaskan dari Perjanjian Saint-Germain-en-Laye, mereka kini bertekad membangun kembali angkatan darat dan udara mereka, yang mereka tegaskan murni demi langkah-langkah pertahanan. Negara mereka memiliki sejarah merancang badan pesawat yang cukup tangguh dan memiliki cukup banyak pilot berbakat, namun dengan adanya jurang dalam produksi dan pelatihan, mereka kini menghadapi tantangan membangun kembali kapasitas ini. Jika kita bersedia mengesampingkan tindakan mereka di Perang Besar, kita berpeluang memetik keuntungan dari kemitraan ini.",
    "AUS_political_events.5.a": "Ini sangat berharga, kita akan membantu sebanyak mungkin!",
    "AUS_political_events.5.b": "Kita dapat belajar untuk bekerja sama.",
    "AUS_political_events.5.c": "Kita tidak mempercayai dusta 'Pertahanan' yang mereka katakan.",
    "AUS_political_events.6.t": "[FROM.GetNameDefCap] Menerima Usulan Kita dan Memberi Izin Pembelian Peralatan",
    "AUS_political_events.6.desc": "[FROM.GetNameDefCap] menyambut positif saran kita untuk bekerja sama dalam membangun angkatan udara dan berbagi pengalaman tempur. Mereka memahami kesulitan yang kita hadapi setelah melepaskan diri dari Perjanjian Saint-Germain-en-Laye dan menawarkan kita kemungkinan untuk membeli kelebihan peralatan militer dari mereka!",
    "AUS_political_events.6.a": "Bersulang untuk kemitraan yang agung!",
    "AUS_political_events.7.t": "[FROM.GetNameDefCap] Menerima Usulan Kita",
    "AUS_political_events.7.desc": "[FROM.GetNameDefCap] merespons cukup baik saran terbaru kita untuk bekerja sama dalam pembangunan angkatan udara masing-masing. Kendati mereka tidak dapat menawarkan bantuan material, mereka sepakat untuk membagikan beberapa metode terbaru mereka dalam pelatihan pilot tempur.",
    "AUS_political_events.7.a": "Bagus sekali!",
    "AUS_political_events.8.t": "[FROM.GetNameDefCap] Menolak Usulan Kemitraan Kita",
    "AUS_political_events.8.desc": "[FROM.GetNameDefCap] telah menolak tawaran kita. Mereka menyatakan bahwa perjanjian itu akan berat sebelah dan tidak memberi manfaat bagi mereka, serta menegaskan bahwa kitalah yang menjerumuskan diri kita sendiri ke dalam situasi ini akibat tindakan kita di Perang Besar.",
    "AUS_political_events.8.a": "Lantas bagaimana situasi ini akan menguntungkan mereka?",
    "AUS_air_force_partnership_big": "Kemitraan Angkatan Udara Ekstensif",
    "AUS_air_force_partnership_small": "Kemitraan Angkatan Udara",
    "AUS_rejected_air_force_partnership": "Kemitraan Angkatan Udara Ditolak",

    # 48 - 61: Wilhelm Zehner
    "AUS_political_events.9.t": "Wilhelm Zehner Dibunuh",
    "AUS_political_events.9.desc": "Wilhelm Zehner, salah satu anggota Komando Tinggi Militer kita, telah ditemukan tewas di apartemennya. Para diplomat [GER.GetAdjective] menyangkal segalanya dan mengklaim mereka tidak terlibat, bersikeras bahwa Zehner pasti melakukan ini sendiri dengan senjata api yang ditemukan bersamanya. Namun penyelidikan kriminal mengarah ke arah yang sama sekali berbeda...",
    "AUS_political_events.9.a": "Jadi pihak [GER.GetAdjective] bukan hanya pembohong, tapi juga pembunuh...",
    "AUS_political_events.9.a_tt": "§YWilhelm Zehner§!§R tewas terbunuh!§!",
    "AUS_anschluss_ratio_lowered": "§YKekuatan Tempur Total Angkatan Darat§! yang dibutuhkan untuk §YAnschluss§! akan §YDiturunkan§!",
    "AUS_anschluss_ratio_raised": "§YKekuatan Tempur Total Angkatan Darat§! yang dibutuhkan untuk §YAnschluss§! akan §YDinaikkan§!",
    "AUS_political_events.10.t": "Upaya Pembunuhan Wilhelm Zehner Digagalkan",
    "AUS_political_events.10.desc": "Kemarin petang, Gestapo mendobrak masuk ke apartemen Wilhelm Zehner dan dihadang oleh para penjaga yang kita tempatkan di sekitar Komando Tinggi kita. Baku tembak tidak berlangsung lama, dan Zehner berhasil selamat dari insiden tersebut tanpa terluka sedikit pun.",
    "AUS_political_events.10.a": "Sudah kami duga!",
    "AUS_political_events.11.t": "[GER.GetNameDefCap] Menyatakan Ketidaksukaan terhadap Komando Tinggi Militer Kita",
    "AUS_political_events.11.desc": "Para diplomat dari [GER.GetNameDef] telah menyampaikan kekhawatiran perihal salah satu anggota komando tinggi militer kita. Mereka mengklaim bahwa kendati kita adalah negara berdaulat dan bebas bertindak sesuka hati, hal ini dapat menyebabkan hubungan diplomatik kita dengan [GER.GetNameDef] memburuk.\\n\\nKita dapat memperkirakan mereka akan mengambil tindakan sendiri jika kita gagal bertindak demi kepentingan terbaik mereka.",
    "AUS_political_events.11.a": "Ini bukan urusan mereka!",
    "AUS_political_events.11.a_tt": "Memicu misi §YPermusuhan [GER.GetAdjective] terhadap Komando Tinggi Militer§!\\n\\nKegagalan mencegah kematian Zehner akan menyebabkan §YKekuatan Tempur Total Angkatan Darat§! yang dibutuhkan untuk §YAnschluss§! §YDiturunkan§!.",
    "AUS_political_events.11.b": "Jika itu yang diperlukan untuk menghentikan keonaran mereka...",

    # 62 - 76: Embargo & Italy
    "AUS_political_events.12.t": "[FROM.GetNameDefCap] Menawarkan Peralatan Infanteri kepada Kita",
    "AUS_political_events.12.desc": "[FROM.GetNameDefCap] telah menghubungi kita menawarkan dukungan berupa peralatan infanteri. Mereka sangat menghargai kita sebagai sekutu yang paling berharga dan berharap senapan-senapan ini dimanfaatkan untuk upaya perang kita di [ETH.GetNameDef] demi memastikan kemenangan kita dalam peperangan ini.",
    "AUS_political_events.12.a": "Sungguh tak terduga, namun sangat disambut baik.",
    "AUS_political_events.13.t": "[FROM.GetNameDefCap] Keberatan atas Embargo terhadap [ITA.GetNameDef]",
    "AUS_political_events.13.desc": "Kita telah menerima protes menentang embargo yang telah kita terapkan terhadap [ITA.GetNameDef], sama seperti yang dilakukan banyak negara lain. Mengklaim bahwa embargo tersebut tidak masuk akal dan tak berdasar, kepemimpinan [AUS.GetAdjective] menuntut agar kita mencabut embargo itu.\\n\\nKetika didesak mengenai alasan mereka memprotes embargo tersebut, kepemimpinan [FROM.GetNameDef] menolak memberikan penjelasan lebih lanjut.",
    "AUS_political_events.13.a": "Pihak [AUS.GetAdjective] tidak punya hak menuntut hal ini.",
    "AUS_political_events.13.b": "Baiklah.",
    "AUS_political_events.14.t": "[FROM.GetNameDefCap] Menentang Keras Embargo terhadap Kita",
    "AUS_political_events.14.desc": "Pemerintah [FROM.GetAdjective] telah mengumumkan penentangan publik mereka terhadap embargo ekonomi yang baru-baru ini dijatuhkan kepada kita. Tindakan solidaritas ini membuktikan bahwa kita tidak berdiri sendirian di kancah internasional.",
    "AUS_political_events.14.a": "Sekutu sejati di masa genting.",
    "AUS_political_events.15.t": "[FROM.GetNameDefCap] Menolak Mencabut Embargo",
    "AUS_political_events.15.desc": "Meskipun kita telah melayangkan protes keras, [FROM.GetNameDefCap] tetap bersikeras mempertahankan embargo terhadap sekutu kita. Sikap keras kepala mereka menunjukkan bahwa diplomasi kata-kata tidak lagi dihiraukan.",
    "AUS_political_events.15.a": "Sikap yang sangat disayangkan.",
    "AUS_political_events.15.b": "Sungguh lancang!",
    "AUS_political_events.15.c": "Kita tidak punya waktu untuk urusan itu sekarang!",
    "AUS_banned_dnsap": "Melarang DNSAP",
    "AUS_meddling_with_our_politics": "Mencampuri Politik Dalam Negeri Kita",
    "AUS_political_events.16.t": "[FROM.GetNameDefCap] Mencabut Embargo",
    "AUS_political_events.16.desc": "Menanggapi protes diplomatik kita, [FROM.GetNameDefCap] telah sepakat untuk mencabut sanksi ekonomi dan embargo terhadap [ITA.GetNameDef]. Ini adalah kemenangan diplomasi yang nyata bagi kita.",
    "AUS_political_events.16.a": "Kabar yang sangat melegakan.",
    "AUS_political_events.16.b": "Sama sekali tidak boleh!",
    "AUS_political_events.16.a_tt": "Mengangkat §YArthur Seyss-Inquart§! sebagai Penasihat yang §Rtidak dapat diberhentikan§!\\n",

    # 77 - 94: Godwin von Brumowski & Military matters
    "AUS_political_events.17.t": "Penyelidikan Korupsi Heimwehr",
    "AUS_political_events.17.desc": "Laporan intelijen menyingkap skandal korupsi dan penggelapan dana di tubuh milisi Heimwehr. Para pemimpin paramiliter dituduh memperkaya diri sendiri dengan dana pertahanan negara.",
    "AUS_political_events.17.a": "Tindak tegas para koruptor!",
    "AUS_political_events.17.b": "Tutup mata demi stabilitas politik.",
    "AUS_political_events.18.t": "Restrukturisasi Angkatan Bersenjata",
    "AUS_political_events.18.desc": "Demi menghadapi ancaman ekspansi asing, para perwira tinggi mengusulkan modernisasi doktrin dan restrukturisasi menyeluruh atas Bundesheer.",
    "AUS_political_events.18.a": "Laksanakan reformasi militer!",
    "AUS_political_events.18.b": "Pertahankan struktur tradisional.",
    "AUS_political_events.19.t": "Kembalinya Godwin von Brumowski",
    "AUS_political_events.19.desc": "Penerbang ulung (ace) kita yang paling berprestasi dari Perang Besar telah menghadap kita menawarkan jasanya sekali lagi saat bangsa kita mendapati diri dalam kancah peperangan. Kendati tak lagi muda, ataupun mampu terbang seperti sedia kala menyusul kecelakaan fatal yang nyaris merenggut nyawanya pada tahun 1936, ia menawarkan diri untuk memimpin angkatan udara kita menuju kemenangan dari darat. Para pilot muda kita tetap memandangnya dengan rasa hormat yang mendalam dan ada keyakinan luas bahwa ia sanggup menggembleng para penerbang kita hingga mencapai kehebatan yang menandingi reputasinya sendiri.",
    "AUS_political_events.19.a": "Kita membutuhkan semua bantuan yang bisa kita peroleh!",
    "AUS_political_events.19.b": "Mengingat keterlibatannya dalam kudeta 1934, kita tidak boleh mengambil risiko.",
    "AUS_von_brumowski_recruited_flag": "Merekrut Godwin von Brumowski",

    # 95 - 123: St. Germain & Guarantees
    "AUS_political_events.20.t": "[FROM.GetNameDefCap] Mengharapkan Dukungan Kita",
    "AUS_political_events.20.desc": "[GetGuarantorFlavorText]",
    "AUS_guarantor_is_italy_key": "[FROM.GetNameDefCap] telah mengutus sang Jenderal dan atase militer berkala Emil Liebitzky kepada kita dengan membawa permohonan bantuan. Beliau, bersama para petinggi dalam kepemimpinan [FROM.GetAdjective], telah menyaksikan kecenderungan yang mengkhawatirkan dari [GER.GetNameDef] dan kini mengharapkan dukungan yang lebih resmi dari kita seandainya penilaian mereka atas situasi ini terbukti benar.\\n\\nSebagai pihak yang turut menandatangani Perjanjian Saint-Germain-en-Laye, kita kemungkinan besar diharapkan datang membantu mereka, kendati celah hukum dalam naskah perjanjian tersebut kemungkinan besar dapat ditemukan.",
    "AUS_guarantor_is_not_italy_key": "[FROM.GetNameDefCap] telah mengutus seorang duta besar kepada kita memohon bantuan kita. Kepemimpinan [FROM.GetAdjective] telah melihat gelagat mencemaskan dari pimpinan [GER.GetNameDef], dan karena mereka terikat larangan mobilisasi untuk menghadapi ancaman tersebut akibat Perjanjian Saint-Germain-en-Laye, mereka kini secara lebih resmi memohon dukungan kita. Dalam naskah perjanjian dan kesepakatan berikutnya kita memang telah setuju untuk membantu mereka, namun tidak ada rincian pasti mengenai bentuk nyata bantuan tersebut.",
    "AUS_political_events.20.a": "Kemerdekaan mereka adalah hal yang paling krusial bagi kita!",
    "AUS_political_events.20.b": "Kita akan mendukung mereka secara diplomatis",
    "AUS_political_events.20.c": "Mungkin kita dapat mencapai kesepakatan yang saling menguntungkan",
    "AUS_political_events.20.d": "Kita tidak akan mempertaruhkan apa pun demi mereka",
    "AUS_political_events.21.t": "[FROM.GetNameDefCap] Menjamin Kemerdekaan Kita",
    "AUS_political_events.21.desc": "Sesuai dengan apa yang tertulis dalam Perjanjian Saint-Germain-en-Laye, [FROM.GetNameDef] telah sepakat untuk menjamin kemerdekaan kita. Demi memastikannya, mereka juga memberi kita sarana untuk pengadaan sejumlah perlengkapan militer, mengingat saat ini kita belum sanggup memproduksi peralatan sendiri.",
    "AUS_political_events.21.a": "Luar biasa!",
    "AUS_political_events.22.t": "[FROM.GetNameDefCap] Mendukung Kemerdekaan Kita Secara Diplomatis",
    "AUS_political_events.22.desc": "Dengan memanfaatkan sejumlah klausul yang kurang dikenal dan pasal-pasal terselubung, [FROM.GetNameDef] memutuskan untuk tidak menawarkan jaminan militer, melainkan hanya dukungan diplomatis seandainya terjadi invasi. Mereka bersikeras bahwa kata-kata mereka sanggup membujuk [GER.GetLeader] sama efektifnya dengan ancaman intervensi senjata, sehingga mereka memandang tidak ada alasan untuk menyiagakan pasukan demi kita.",
    "AUS_political_events.22.a": "Bukan ini yang kita minta, tapi lebih baik daripada tidak sama sekali.",
    "AUS_political_events.22.b": "Diplomasi dan peralatan saja tidak akan sanggup menyelamatkan kita!",
    "AUS_political_events.23.t": "[FROM.GetNameDefCap] Menawarkan Jaminan Bersyarat",
    "AUS_political_events.23.desc": "[FROM.GetNameDefCap] menanggapi permohonan bantuan kita dengan mengajukan tuntutan balik. Sejak masa perjanjian ini dipaksakan kepada kita, kita selalu berikhtiar merebut kembali Alto Adige dan Trentino, karena wilayah itu secara sah adalah milik kita. Namun [FROM.GetNameDef] memandang tanah tersebut sebagai milik mereka, dan jika mereka harus menjamin kemerdekaan kita, mereka menuntut kita melepaskan klaim-klaim itu untuk selama-lamanya.",
    "AUS_political_events.23.a": "Keselamatan mendesak kita jauh lebih penting daripada klaim wilayah tersebut",
    "AUS_political_events.23.b": "Mereka berusaha memeras keuntungan dari kemalangan kita, jelas tidak bisa diterima.",
    "AUS_political_events.24.t": "[FROM.GetNameDefCap] Menolak Permohonan Bantuan Kita",
    "AUS_political_events.24.desc": "Dengan memanfaatkan berbagai celah hukum, tulisan halus, dan klausul kabur dalam Perjanjian Saint-Germain-en-Laye, [FROM.GetNameDef] entah bagaimana telah berhasil berkelit dari kewajiban membantu kita. Tertulis gamblang di atas kertas bahwa kita berhak atas bantuan eksternal sebagai kompensasi atas dilarangnya kita memiliki angkatan darat yang layak, namun kenyataannya [FROM.GetNameDef] memutuskan aturan itu tak berlaku bagi mereka. Kita terpaksa berjuang sendirian.",
    "AUS_political_events.24.a": "Kita sudah menunjukkan kelemahan fatal ini kepada pihak-pihak lain...",
    "AUS_political_events.24.b": "Kita akan memberi mereka imbalan yang menggoda!",
    "AUS_political_events.25.t": "[FROM.GetNameDefCap] Mencabut Klaim atas Wilayah Kita",
    "AUS_political_events.25.desc": "[FROM.GetNameDefCap] menanggapi tuntutan kita agar mereka mencabut klaim atas wilayah kita dengan tunduk pada tuntutan tersebut. Mereka telah sepenuhnya mengubur gagasan merebut wilayah ini sebagai imbalan atas dukungan kita.",
    "AUS_political_events.25.a": "Kabar yang Luar Biasa!",
    "AUS_political_events.26.t": "[FROM.GetNameDefCap] Menolak Mencabut Klaim Mereka",
    "AUS_political_events.26.desc": "Semula kita mengira pihak [FROM.GetAdjective] adalah bangsa yang berakal sehat ketika mereka mendekati kita memohon pertolongan baru-baru ini. Namun dugaan kita keliru besar. Ketika didesak untuk mencabut klaim mereka atas wilayah yang secara sah adalah milik kita, mereka menolak mentah-mentah.",
    "AUS_political_events.26.a": "Kalau begitu, tidak ada bantuan sedikit pun bagi mereka.",

    # 124 - 146: Treaty of Saint-Germain-en-Laye Break
    "AUS_political_events.27.t": "[AUS.GetNameDefCap] Berupaya Mempersenjatai Diri Kembali",
    "AUS_political_events.27.desc": "[AUS.GetNameDefCap] telah menghubungi kita memohon persetujuan untuk mempersenjatai diri kembali dan menghapuskan Perjanjian Saint-Germain-en-Laye. Menyatakan bahwa kawasan tetangga mereka kian bermusuhan belakangan ini, mereka menyampaikan bahwa mereka tidak lagi merasa aman tanpa tentara sendiri. Pertanyaan ini telah dilayangkan kepada ketiga kekuatan utama penandatangan perjanjian, yaitu [ITA.GetNameDef], [ENG.GetNameDef], dan [FRA.GetNameDef], serta [USA.GetNameDef], dan sesuai ketentuan perjanjian, masing-masing dari kita berhak mengajukan veto jika menginginkannya.",
    "AUS_political_events.27.a": "Mereka tidak akan menimbulkan bahaya apa pun.",
    "AUS_political_events.27.b": "Sama sekali tidak boleh.",
    "AUS_political_events.28.t": "Para Penjamin Menyetujui Persenjataan Kembali",
    "AUS_political_events.28.desc": "Kita akhirnya menerima jawaban dari para negara penjamin dan penantian itu terbayar lunas. Setelah serangkaian diskusi dan perundingan panjang di antara mereka, mereka sepakat bahwa kita boleh mempersenjatai diri kembali dan menyatakan Perjanjian Saint-Germain-en-Laye telah usang. Kita tidak lagi terbelenggu oleh dosa-dosa para pendahulu kita.",
    "AUS_political_events.28.a": "Luar biasa!",
    "AUS_political_events.29.t": "Para Penjamin Menolak Permohonan Persenjataan Kembali",
    "AUS_political_events.29.desc": "Setelah perundingan yang berlarut-larut dan sekian banyak perdebatan, para penjamin memutuskan untuk tidak merestui permohonan persenjataan kembali kita. Kita telah berupaya meyakinkan mereka dengan akal sehat, namun jawaban mereka tetap bergeming terlepas dari ancaman nyata terhadap kedaulatan dan kemerdekaan kita.",
    "AUS_political_events.29.a": "Kalau begitu kita tidak punya pilihan lain...",
    "AUS_political_events.29.a_tt": "§RDengan memilih ini, Anda akan menghapuskan Perjanjian Saint-Germain-en-Laye secara permanen, namun mungkin akan menimbulkan konsekuensi serius§!",
    "AUS_political_events.29.b": "Kita harus merundingkan hal ini kembali!",
    "AUS_political_events.29.c": "Mereka menjebak kita menuju kehancuran, tapi apa yang bisa kita perbuat?",
    "AUS_political_events.29.c_tt": "§RDengan memilih ini, Perjanjian Saint-Germain-en-Laye akan tetap aktif hingga 16 Juli 1940§!",
    "AUS_political_events.30.t": "[AUS.GetNameDefCap] Melanggar Perjanjian Saint-Germain-en-Laye",
    "AUS_political_events.30.desc": "[GetTreatyStatus]",
    "AUS_treaty_asked_permission_key": "Terlepas dari upaya terbaik kita untuk menghentikan mereka, pemerintah [AUS.GetAdjective] telah memutuskan untuk memerintahkan persenjataan kembali [AUS.GetNameDef] yang secara nyata melanggar perjanjian. Semula kita berharap hal ini tidak akan terjadi, namun tampaknya tidak ada yang dapat menghentikan mereka menempuh jalan ini.",
    "AUS_treaty_no_permission_key": "Tanpa peringatan apa pun sebelumnya, kita telah diberitahu bahwa [AUS.GetNameDef] tidak lagi bersedia mematuhi Perjanjian Saint-Germain-en-Laye beserta segala ketentuannya. Yang paling mencemaskan, ini berarti mereka kini bebas mempersenjatai diri tanpa mengindahkan batasan yang dijatuhkan pasca Perang Besar. Mengapa mereka mendadak bernafsu mempersenjatai diri masih menjadi tanda tanya besar.",
    "AUS_political_events.30.a": "Kita tidak dapat menghentikan mereka, tapi kita dapat memperlambat langkah mereka",
    "AUS_political_events.30.b": "Biarkan saja mereka berbuat sesuka hati.",
    "AUS_political_events.30.c": "Tidak ada lagi jaminan kemerdekaan untuk mereka!",
    "AUS_broke_the_treaty": "Melanggar Perjanjian Kita",
    "AUS_broke_the_treaty_democratic": "Melanggar Perjanjian Kita",

    # 147 - 160: Spanish Civil War Compensation
    "AUS_political_events.31.t": "[FROM.GetNameDefCap] Menuntut Kompensasi atas Bantuan Mereka",
    "AUS_political_events.31.desc": "Saat debu pertempuran mulai mereda pasca perang saudara, kita telah dihubungi oleh pihak [FROM.GetAdjective] mengenai masalah kompensasi atas pengorbanan mereka dalam perang saudara. Mereka menuntut semacam ganti rugi atas jasa yang mereka berikan, nyawa prajurit yang gugur, serta persenjataan yang digunakan dan rusak oleh para sukarelawan mereka.",
    "AUS_political_events.31.a": "Kita akan membantu di sektor industri.",
    "AUS_political_events.31.b": "Mereka boleh mengambil sebagian perlengkapan yang kita rampas dari musuh",
    "AUS_political_events.31.c": "Dukungan mereka sama sekali tidak berarti",
    "AUS_political_events.32.t": "[FROM.GetNameDefCap] Menawarkan Bantuan Membangun Pabrik Baru",
    "AUS_political_events.32.desc": "Permohonan kompensasi kita telah didengar oleh kaum nasionalis [FROM.GetAdjective] dan sebagai wujud terima kasih, mereka meminjamkan tenaga kerja serta material untuk membangun sebuah pabrik baru di Niederösterreich. Langkah ini memungkinkan kita mengganti perlengkapan yang hilang dan akan terbukti sangat bermanfaat di masa depan.",
    "AUS_political_events.32.a": "Bagus sekali!",
    "AUS_political_events.33.t": "[FROM.GetNameDefCap] Menawarkan Peralatan Militer Hasil Rampasan",
    "AUS_political_events.33.desc": "Permohonan kompensasi kita telah didengar oleh pihak [SPA.GetAdjective] dan sebagai wujud terima kasih, mereka mengirimkan sebagian perlengkapan yang mereka rampas dari lawan selama perang saudara guna mengganti sebagian peralatan kita yang hilang saat membantu mereka.",
    "AUS_political_events.33.a": "Bagus sekali!",
    "AUS_political_events.34.t": "[FROM.GetNameDefCap] Menolak Memberi Ganti Rugi",
    "AUS_political_events.34.desc": "Setelah membantu pihak [SPA.GetAdjective] dalam perang saudara mereka, hal paling minim yang kita harapkan adalah semacam ganti rugi dan rasa terima kasih, namun tampaknya harapan kita terlalu muluk. Dengan berdalih bahwa bantuan kita bukan hal yang istimewa, pimpinan [SPA.GetNameDef] menolak gagasan bahwa kita berhak menerima kompensasi atas dukungan yang telah kita kurbankan.",
    "AUS_political_events.34.a": "Sungguh tak tahu terima kasih...",

    # 161 - 173: Paramilitary & Greater Austria
    "AUS_political_events.35.t": "Aktivitas Paramiliter Memicu Keresahan Sipil",
    "AUS_political_events.35.desc": "Kerja sama kita terkini dengan [GetMilitiaName] telah menimbulkan dampak samping yang meresahkan. Seiring organisasi tersebut dilegitimasi oleh pucuk pimpinan negara, [GetMilitiaName] kian bertindak sewenang-wenang terhadap penduduk sipil.\\n\\nKeresahan di dalam negeri kian meruncing seiring rakyat kita tak lagi merasa tenteram dengan tindak-tanduk organisasi tersebut. Berbagai pertanyaan dilayangkan kepada pimpinan kita mengenai apakah kita sungguh-sungguh mengendalikan [GetMilitiaName], dan apakah keputusan ini benar-benar membantu menjaga keselamatan bangsa.",
    "AUS_political_events.35.a": "[GetMilitiaName] telah menyia-nyiakan kesempatan mereka.",
    "AUS_political_events.35.b": "Rakyat hanya perlu menyesuaikan diri.",
    "AUS_political_events.35.c": "Inilah tatanan baru [ROOT.GetName]!",
    "AUS_political_events.36.t": "Masa Depan [ROOT.GetNameDef]",
    "AUS_political_events.36.desc": "Perjalanan panjang kita bangkit dari kekuatan kecil yang lumpuh parah merupakan jalan terjal penuh rintangan. Menengok kembali titik awal perjuangan kita menegaskan betapa berharganya pengorbanan ini. Terlahir kembali dan kini jauh lebih perkasa dari sebelumnya, telah tiba saatnya bagi kita menentukan masa depan dan bagaimana bangsa ini ingin dikenal oleh dunia.",
    "AUS_political_events.36.a": "Pada saatnya kita akan dikenal sebagai [GetGrossosterreichCosmeticIdeology]",
    "AUS_grossosterreich_fascism_key": "Großösterreich",
    "AUS_grossosterreich_neutrality_key": "Kekaisaran Austria Raya",
    "AUS_political_events.36.a_tt": "§YMembuka keputusan§! untuk §YMengintegrasikan Inti Wilayah Jerman§! seiring berjalannya waktu.",
    "AUS_political_events.36.b": "Kita akan dikenal sebagai Süddeutschland (Jerman Selatan)",
    "AUS_political_events.36.c": "Kita sudah sempurna apa adanya",

    # 174 - 191: Ultimatum & Integration
    "AUS_political_events.37.t": "Ultimatum Dari [FROM.GetNameDef]",
    "AUS_political_events.37.desc": "[GetIntegrationEventTarget]",
    "AUS_integration_target_is_poland_key": "Sebuah pesan bernada keras telah disampaikan kepada kita dari pemerintah [FROM.GetAdjective]. Mereka menuntut kita menyerahkan [Get37PuppetOrNotDesc] kepada mereka dan memperingatkan bahwa akan ada konsekuensi fatal jika kita mencoba melawan.\\n\\nTindakan agresi dari [FROM.GetNameDef] ini sama sekali tidak mengejutkan menyusul serangkaian tuntutan serupa yang dilancarkan terhadap negara-negara lain di sekitar wilayah ini.",
    "AUS_integration_target_is_not_poland_key": "Pemerintah [FROM.GetAdjective] telah melayangkan ultimatum kepada kita: serahkan [Get37PuppetOrNotDesc] secara sukarela, atau hadapi kedahsyatan mesin perang mereka yang kini telah bangkit di medan laga. Apapun jalan yang kita pilih dalam persoalan ini, jelas tidak ada jalan keluar tanpa menanggung konsekuensi berat.",
    "AUS_political_events.37.a": "Kita tidak akan pernah tunduk kepada mereka!",
    "AUS_political_events.37.b": "Kita tidak memiliki peluang bertahan menghadapi mereka",
    "AUS_political_events.37_tt": "Kita akan menyerahkan wilayah bagian yang mereka klaim kepada mereka.",
    "37DescIsPuppet": "[FROM.FROM.OWNER.GetNameDef]",
    "37DescIsNotPuppet": "wilayah-wilayah lama mereka",
    "AUS_political_events.38.t": "[FROM.GetNameDefCap] Menolak Tuntutan Kita",
    "AUS_political_events.38.desc": "Kita bermaksud memberi kesempatan kepada pihak [FROM.GetAdjective] [Get38PuppetOrNotDesc] ke dalam masyarakat kita, namun tampaknya tawaran murah hati kita tidak digubris. Bagaimanapun juga, kita sangat menyadari bahwa [FROM.GetNameDef] akan bernasib jauh lebih baik di bawah kepemimpinan kita.",
    "AUS_political_events.38.a": "Mereka akan bergabung dengan kita, terlepas dari apa pun kehendak mereka.",
    "AUS_political_events.38_tt": "Membuat Tujuan Perang §YRebut Bagian Wilayah yang Diklaim§! terhadap §Y[FROM.FROM.OWNER.GetNameWithFlag]§!",
    "38DescIsPuppet": "untuk menyerahkan [FROM.FROM.OWNER.GetName] dan membiarkannya terintegrasi",
    "38DescIsNotPuppet": "untuk berintegrasi secara damai",
    "AUS_political_events.39.t": "[FROM.GetNameDefCap] Tunduk",
    "AUS_political_events.39.desc": "Tanggapan dari kepemimpinan [FROM.GetAdjective] sungguh sangat melegakan. Mereka bersedia meletakkan senjata dan tidak akan melawan saat kita mengintegrasikan apa yang secara sah adalah milik kita. Jelas mereka menyadari betapa sia-sianya menjerumuskan bangsa mereka ke dalam perang tak bermakna hanya demi persoalan ini.",
    "AUS_political_events.39.a": "Selamat datang di [ROOT.GetNameDef]!",

    # 192 - 199: Faction joining
    "AUS_political_events.40.t": "[FROM.GetNameDefCap] Berupaya Bergabung dengan [ROOT.GetFactionName]",
    "AUS_political_events.40.desc": "[FROM.GetNameDefCap] telah menghubungi kita memohon untuk bergabung ke dalam faksi kita. Mereka telah memulai program militerisasi dan menyampaikan keinginan untuk bekerja sama demi memperkuat kedua bangsa kita. Secara historis negara tersebut pernah menjadi kekuatan dahsyat yang disegani di medan tempur, dan kendati kini melemah, mereka tetap meyakinkan bahwa mereka akan menjadi sekutu yang sangat berharga bagi kita.",
    "AUS_political_events.40.a": "Mereka sangat disambut baik untuk bergabung bersama kita",
    "AUS_political_events.40.b": "Kita sama sekali tidak membutuhkan mereka.",
    "AUS_political_events.41.t": "[FROM.GetNameDefCap] Menyetujui Kita Bergabung dengan [FROM.GetFactionName]",
    "AUS_political_events.41.desc": "[FROM.GetNameDefCap] membalas permohonan kita untuk bergabung dengan penuh antusiasme dan menyambut kita ke dalam faksi mereka. Kita tidak akan lagi bertempur sendirian melawan mereka yang mengancam keselamatan kita!",
    "AUS_political_events.41.a": "Kita jauh lebih kuat bila bersatu!",
    "AUS_political_events.42.t": "[FROM.GetNameDefCap] Menolak Membiarkan Kita Bergabung dengan [FROM.GetFactionName]"
}

# Verify and save
with open('scripts/chunks/chunk_0.json', 'r', encoding='utf-8') as f:
    chunk_items = json.load(f)

missing = []
for it in chunk_items:
    k = it['key']
    if k not in trans:
        missing.append(k)

if missing:
    print(f"Warning: {len(missing)} missing keys in chunk 0: {missing[:10]}")
else:
    print(f"Success! All {len(chunk_items)} keys in chunk 0 are translated!")

with open('scripts/chunks/trans_chunk_0.json', 'w', encoding='utf-8') as f:
    json.dump(trans, f, indent=2, ensure_ascii=False)
print("Saved scripts/chunks/trans_chunk_0.json")
