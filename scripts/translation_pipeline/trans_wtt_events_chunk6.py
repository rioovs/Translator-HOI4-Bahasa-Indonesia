# -*- coding: utf-8 -*-
import json

# Entries 724 to 874 (wtt_news 25-44, wtt_warlord, wtt_britain_lease_azores, soviet hold city, decisions 1-2)
chunk6_translations = {
    # 724 - 728: wtt_news.25
    "wtt_news.25.t": "[JAP.GetNameDefCap] Mengambil Alih Kendali atas Koloni [From.GetAdjective]",
    "wtt_news.25.desc": "Mengingat kelemahan [From.GetNameDef] saat ini, tidaklah mengejutkan bahwa pihak [JAP.GetAdjective] telah meningkatkan tekanan untuk menguasai wilayah jajahan [From.GetAdjective] di Asia Timur. Pagi ini, para pejabat dari pemerintah [From.GetAdjective] membuat pengumuman mengejutkan bahwa kendali atas koloni-koloni [From.GetAdjective] dialihkan kepada [JAP.GetNameDef], berlaku sesegera mungkin.",
    "wtt_news.25.a": "Asia untuk bangsa Asia!",
    "wtt_news.25.b": "Hari yang menyedihkan bagi Eropa...",
    "wtt_news.25.c": "Apakah ini akhir dari kolonialisme?",

    # 729 - 732: wtt_news.26
    "wtt_news.26.t": "Kemerdekaan Filipina",
    "wtt_news.26.desc": "Sebagai akibat dari tekanan [JAP.GetAdjective], pemerintah [From.GetAdjective] kini telah mengumumkan penghentian segera kekuasaan kolonial [From.GetAdjective] atas kepulauan tersebut. Mulai hari ini, kedaulatan penuh telah diserahkan kepada [PHI.GetNameDef].",
    "wtt_news.26.b": "Bagaimanapun juga, kita memang berniat melakukan dekolonisasi.",
    "wtt_news.26.c": "Hari yang penuh sukacita!",

    # 733 - 738: wtt_news.27
    "wtt_news.27.t": "Kudeta Perwira Muda Jepang",
    "wtt_news.27.desc": "Sekelompok perwira muda telah berhasil menggulingkan pemerintah dan memulihkan Kaisar sebagai penguasa tertinggi bangsa Jepang. Tampaknya ini merupakan reaksi terhadap ancaman korupsi pemerintah yang meluas dan para pengikut ideologi yang bermusuhan.\\n\\nDengan semakin konsisten menyebut negara dalam istilah Kekaisaran, para perwira telah mengumumkan bahwa pembersihan akan terus berlanjut hingga 'semua elemen yang tidak diinginkan telah disingkirkan dari militer dan pemerintahan'. Kaisar Hirohito sendiri telah merilis pernyataan singkat menerima kepemimpinan yang ditawarkan kepadanya oleh para pemberontak, dan menyampaikan sinyal rekonsiliasi yang jelas dengan Tiongkok serta kekuatan kolonial Barat di Pasifik.",
    "wtt_news.27.a": "Banzai!",
    "wtt_news.27.b": "Kabar yang mencemaskan... Mereka tidak menunjukkan sinyal seperti itu kepada kita...",
    "wtt_news.27.c": "Apakah ini menjamin perdamaian di Pasifik?",
    "wtt_news.27.d": "Pembalikan peristiwa yang mendadak.",

    # 739 - 744: wtt_news.30
    "wtt_news.30.t": "Chiang Kai-Shek Dieksekusi",
    "wtt_news.30.desc": "Menyusul penangkapannya oleh [CHI_xian_instigator.GetLeader], Chiang Kai-Shek dilaporkan telah ditembak mati oleh regu tembak Komunis pagi ini. Setelah persidangan kilat atas kejahatan terhadap rakyat dan partai, [PRC.GetLeader] menjatuhkan vonis mati kepada Chiang Kai-Shek. Bahkan intervensi langsung dari perwakilan Pemerintah Soviet tidak cukup untuk menyelamatkan nyawanya.\\n\\n[SOV.GetLeader] dilaporkan sangat murka atas \"pengkhianatan\" oleh [PRC.GetLeader] ini dan telah memerintahkan penangkapan delegasi Komintern Tiongkok.\\n\\nPemimpin Nasionalis baru [CHI.GetLeader] telah bersumpah bahwa kematian Chiang akan dibalas dan kaum Komunis akan \"dimusnahkan\".",
    "wtt_news.30.a": "Ia mendapatkan apa yang layak diterimanya.",
    "wtt_news.30.b": "Mereka melakukan pembunuhan dan menyebutnya keadilan!",
    "wtt_news.30.c": "Ini akan memicu konsekuensi serius.",
    "wtt_news.30.d": "Tiongkok akan semakin tidak stabil.",

    # 745 - 747: wtt_news.31
    "wtt_news.31.t": "Chiang Kai-Shek Dieksekusi",
    "wtt_news.31.desc": "Menyusul penangkapannya oleh [CHI_xian_instigator.GetLeader], Chiang Kai-Shek dilaporkan telah dihukum mati oleh regu tembak komunis pagi ini. Setelah pengadilan singkat atas tuduhan kejahatan terhadap rakyat dan partai, pengkhianatan tingkat tinggi, serta aktivitas kontra-revolusioner, [PRC.GetLeader] membacakan vonis mati untuk Chiang Kai-Shek. Perwakilan Soviet bertindak sebagai jaksa dalam persidangan tersebut, memicu spekulasi bahwa [SOV.GetLeader] secara diam-diam menyetujui keputusan ini.\\nPemimpin Nasionalis baru [CHI.GetLeader] telah berikrar bahwa kematian Chiang akan dibalas dan kaum Komunis akan \"dimusnahkan\".",
    "wtt_news.31.c": "Kita mengambil keputusan yang tepat.",

    # 748 - 753: wtt_news.32
    "wtt_news.32.t": "Chiang Kai-Shek Dibebaskan dari Tahanan Rumah",
    "wtt_news.32.desc": "Setelah ditangkap oleh [CHI_xian_instigator.GetLeader] dan diserahkan kepada pihak komunis, [CHI.GetLeader] dilaporkan telah kembali ke kediamannya menyusul perundingan yang alot. Laporan masih belum lengkap, namun bukti-bukti mengindikasikan bahwa [PRC.GetLeader] menawarkan persekutuan melawan Jepang. Kedua belah pihak telah membantah rumor tersebut, dengan [PRC.GetLeader] menyatakan bahwa ia lebih suka melihat negeri ini menjadi abu daripada bersekutu dengan kaum Nasionalis, sebuah sentimen yang langsung dibalas setimpal oleh [CHI.GetLeader].",
    "wtt_news.32.a": "Rencana apa yang sedang mereka siapkan terhadap kita?",
    "wtt_news.32.c": "Seperti anak-anak yang bertengkar...",
    "wtt_news.32.d": "Jepang akan memanfaatkan situasi ini demi keuntungan mereka.",
    "wtt_news.32.e": "Kita bisa memanfaatkan ini untuk keuntungan kita.",

    # 754 - 756: wtt_news.33
    "wtt_news.33.t": "[PRC.GetLeader] Mengecam Pengkhianatan Nasionalis",
    "wtt_news.33.desc": "\\nMenyusul pertemuan antara [CHI.GetLeader] dan [PRC.GetLeader], pihak terakhir mengecam apa yang ia sebut sebagai \"upaya terang-terangan dan murahan untuk mencaplok Tentara Merah demi kepentingan Nasionalis dan kontra-revolusioner.\" [CHI.GetLeader] menolak berkomentar mengenai isu ini, hanya menyatakan bahwa tentara Nasionalis siap membela Tiongkok dari penyerang mana pun.\\n\\nKabarnya, kedua pemimpin tersebut sempat membahas kemungkinan pembentukan Front Persatuan melawan Jepang.\\n\\nApakah kebuntuan ini akan berujung pada pecahnya kembali konflik antara kedua pihak masih harus dilihat.",
    "wtt_news.33.b": "Mengapa kita sempat berpikir bahwa mereka akan berubah?",

    # 757 - 762: wtt_news.34
    "wtt_news.34.t": "Macan Terbang (Flying Tigers) Dibentuk",
    "wtt_news.34.desc": "Menanggapi permohonan Tiongkok agar pilot dan mekanik Amerika bergabung dalam unit sukarelawan, Presiden AS [USA.GetLeader] secara resmi telah menyetujui transfer lebih dari seratus pesawat tempur modern ke Angkatan Udara Tiongkok. Pilot di Angkatan Darat, Angkatan Laut, atau Korps Marinir AS juga diberi izin cuti untuk bergabung dengan unit ini.\\n\\nKapal-kapal pertama yang mengangkut pesawat tempur baru tersebut dijadwalkan berangkat segera setelah perlengkapan yang diperlukan terkumpul. Para pemimpin Kongres menyatakan keprihatinan bahwa tindakan yang menyerempet batas hukum internasional seperti ini akan mengundang dampak balasan.",
    "wtt_news.34.a": "Selamat berburu!",
    "wtt_news.34.b": "Kedatangan mereka sangat disambut baik.",
    "wtt_news.34.c": "Sukarelawan? Lebih mirip Tentara Bayaran!",
    "wtt_news.34.d": "Akhir dari isolasionisme AS?",

    # 763 - 768: wtt_news.35
    "wtt_news.35.t": "Insiden Shanghai",
    "wtt_news.35.desc": "Ketegangan antara Tiongkok dan Jepang meningkat tajam menyusul bentrokan di Shanghai tadi malam.\\n\\nLaporan para pengamat barat mengindikasikan bahwa perkelahian massal pecah antara Polisi Tiongkok dan sekelompok pelaut Jepang, di mana kedua pihak menderita luka-luka. Ketika patroli Jepang tiba untuk menyelidiki, unit Tentara Tiongkok telah memblokir semua akses ke lokasi dan menangkap para pelaut Jepang, yang akan didakwa atas percobaan pembunuhan.\\n\\nPemerintah Jepang telah mengeluarkan peringatan keras bahwa, kecuali para pelaut itu dibebaskan seketika, tindakan tegas akan diambil untuk membebaskan mereka.",
    "wtt_news.35.a": "Keterlaluan!",
    "wtt_news.35.b": "Semua berjalan sesuai rencana.",
    "wtt_news.35.c": "Bau mesiu dan perang mulai tercium.",
    "wtt_news.35.d": "Tampaknya ini sudah direncanakan sebelumnya.",

    # 769 - 773: wtt_news.36
    "wtt_news.36.t": "Chiang Kai-Shek Tewas dalam Kecelakaan Pesawat",
    "wtt_news.36.desc": "Tragedi melanda [CHI.GetNameDef] tadi pagi saat pesawat yang membawa Chiang Kai-Shek meledak di udara sesaat setelah lepas landas. Tim penyelamat masih menyisir puing-puing reruntuhan, namun sedikit yang masih berharap akan menemukan korban selamat dari antara awak dan penumpang.\\n\\nBaik Generalissimo maupun istrinya diduga kuat telah tewas.\\n\\nPemimpin baru Tiongkok [CHI.GetLeader] telah berjanji akan melakukan penyelidikan menyeluruh terhadap penyebab bencana ini. Rumor beredar luas mengenai adanya konspirasi untuk menghabisi sang Generalissimo, yang dipandang oleh banyak kalangan sebagai batu sandungan dalam menyatukan berbagai faksi di Tiongkok.",
    "wtt_news.36.a": "Berkurang satu masalah yang harus dirisaukan.",
    "wtt_news.36.b": "Ini jelas bukan kecelakaan biasa.",
    "wtt_news.36.d": "Sungguh tragis.",

    # 774 - 778: wtt_news.37
    "wtt_news.37.t": "Republik Rakyat Tiongkok Diproklamasikan",
    "wtt_news.37.desc": "Dalam pidato kemenangannya, [PRC.GetLeader] menyatakan bahwa \"rakyat Tiongkok telah bangkit berdiri\" dan menghantarkan kaum Komunis meraih kemenangan dalam Perang Saudara Tiongkok. Dengan mundurnya kaum Nasionalis secara menyeluruh, Partai Komunis akhirnya mengamankan kemenangan setelah pertikaian selama berdekade-dekade. Mulai saat ini, kelompok pemberontak kecil yang tadinya bersembunyi di desa-desa pegunungan terpencil telah menjadi pemerintahan penuh di Republik Rakyat Tiongkok.",
    "wtt_news.37.a": "Hari yang agung.",
    "wtt_news.37.b": "Sekadar formalitas belaka.",
    "wtt_news.37.d": "Mereka tidak akan pernah mencapai apa pun.",

    # 779 - 784: wtt_news.38
    "wtt_news.38.t": "[PRC.GetLeader] Memenangkan Perebutan Kekuasaan Internal",
    "wtt_news.38.desc": "Pertikaian antarfaksi internal di tubuh Partai Komunis Tiongkok tampaknya telah mereda, dengan [PRC.GetLeader] tampil sebagai pemimpin tertinggi. Mao Tse-Tung dan faksi-faksi yang lebih moderat kehilangan pengaruh yang signifikan, karena [PRC.GetLeader] yang didukung Soviet berhasil mengungguli manuver mereka berdua. Peran apa, jika ada, yang dimainkan [SOV.GetLeader] dalam peristiwa ini menjadi bahan perdebatan hangat.",
    "wtt_news.38.a": "Semoga beliau memimpin kita menuju kemenangan!",
    "wtt_news.38.b": "Tidak penting.",
    "wtt_news.38.c": "Sekutu yang berguna.",
    "wtt_news.38.d": "Ia mewarisi posisi yang sangat sulit.",

    # 785 - 791: wtt_news.39
    "wtt_news.39.t": "Kampanye Pasifikasi Tiongkok",
    "wtt_news.39.desc": "Menyusul serangkaian insiden yang digambarkan sebagai \"provokasi terang-terangan\", pemerintah Jepang telah menyatakan bahwa keadaan \"konflik bersenjata\" kini berlangsung di Tiongkok. Mereka mengklaim bahwa pemerintah pusat [CHI.GetLeader] menunjukkan ketidakmauan atau ketidakmampuan untuk menindak tegas pihak-pihak yang bertanggung jawab. Oleh karena itu, mereka mengumumkan bahwa pasukan \"penjaga perdamaian\" tentara Jepang telah dikerahkan ke negeri tersebut demi memulihkan ketertiban dan mencegah serangan lanjutan.",
    "wtt_news.39.a": "Sesuai rencana.",
    "wtt_news.39.b": "Siapa yang melakukan ini?",
    "wtt_news.39.c": "Apa yang telah kita perbuat!?",
    "wtt_news.39.d": "Alasan yang mengada-ada.",
    "wtt_news.39.e": "Mereka akan menyadari kekeliruan langkah mereka.",

    # 792 - 801: wtt_warlord.1, .2, .3
    "wtt_warlord.1.t": "[From.GetNameDefCap] Menawarkan Ketundukan",
    "wtt_warlord.1.desc": "Dengan pemerintah pusat Tiongkok yang sama sekali tak sanggup menjamin keselamatan rakyatnya dari bandit dan komunis, [From.GetLeader] akhirnya menyadari posisinya dan menghubungi kita dalam upaya mengamankan kedudukannya. Ia bersedia bekerja sama penuh dan mengizinkan perlintasan bebas bagi pasukan kita. Sebagai imbalannya, ia hanya meminta agar kita menempatkan sejumlah pasukan guna melindungi wilayahnya dan mengingat jasanya kelak saat kita selesai menata ulang Tiongkok.",
    "wtt_warlord.1.a": "Akhirnya, seseorang yang berpikiran rasional!",
    "wtt_warlord.1.b": "Tidak ada tempat bagi mereka dalam rencana kita.",
    "wtt_warlord.2.t": "[From.GetNameDefCap] Menerima",
    "wtt_warlord.2.desc": "Pemerintah [From.GetAdjective] telah menerima usulan kita. Sebagai imbalan atas perlindungan mereka, kita diminta untuk \"mempertimbangkan dengan sungguh-sungguh\" nasihat yang diberikan mengenai bagaimana kita bertindak. Seorang pejabat pemerintah [From.GetAdjective] telah tiba untuk mengoordinasikan kebijakan kita.",
    "wtt_warlord.2.a": "Harga kecil demi kelangsungan hidup kita.",
    "wtt_warlord.3.t": "[From.GetNameDefCap] Menolak",
    "wtt_warlord.3.desc": "Pemerintah [From.GetAdjective] telah mengembalikan nota kita dengan penolakan mentah-mentah untuk membahasnya, menyatakan bahwa kita tidak memiliki wewenang untuk berunding dengan pemerintah nasional yang sah.",
    "wtt_warlord.3.a": "Kita akan tumbuh kuat dan membuktikan kemampuan kita kepada mereka.",

    # 802 - 817: wtt_britain_lease_azores
    "wtt_britain_lease_azores.1.t": "[From.GetNameDefCap] Meminta Sewa Kepulauan Azores",
    "wtt_britain_lease_azores.1.desc": "Pihak [From.GetAdjective] telah mendekati kita dengan permintaan untuk menyewa Kepulauan Azores selama masa perang. Lokasi strategis kepulauan ini menjadikannya pangkalan penting untuk mengawal jalur pelayaran melintasi Samudra Atlantik. Kepulauan tersebut akan dikembalikan setelah permusuhan usai.",
    "wtt_britain_lease_azores.1.a": "Lebih baik daripada menyeret kita ke dalam kancah perang...",
    "wtt_britain_lease_azores.1.b": "Di mana keuntungan bagi kita?",
    "wtt_britain_lease_azores.2.t": "[From.GetNameDefCap] Menerima",
    "wtt_britain_lease_azores.2.desc": "Pemerintah [From.GetAdjective] telah menyetujui permintaan kita dan memberi kita kendali penuh atas Azores, dengan pemahaman bahwa kita kini bertanggung jawab untuk melindunginya dari serangan apa pun. Pasukan pendahulu kecil telah tiba di kepulauan tersebut untuk mendirikan pangkalan operasi.",
    "wtt_britain_lease_azores.2.a": "Ini akan terbukti sangat berguna.",
    "wtt_britain_lease_azores.3.t": "[From.GetNameDefCap] Menolak",
    "wtt_britain_lease_azores.3.desc": "Menyatakan sikap netralitas serta hukum perang, pemerintah [From.GetLeader] telah menolak permintaan kita atas hak pangkalan di Azores. Kecuali kita menemukan cara untuk membawa mereka ke dalam perang di pihak kita, kepulauan itu tetap tertutup bagi kita.",
    "wtt_britain_lease_azores.3.a": "Kita akan mengingat perlakuan ini.",
    "wtt_britain_lease_azores.4.t": "Sewa Azores Telah Berakhir",
    "wtt_britain_lease_azores.4.desc": "Dengan berakhirnya permusuhan di Eropa, pemerintah [POR.GetAdjective] mengingatkan kita bahwa sewa Azores hanya berlaku selama masa perang. Waktunya telah tiba untuk mengembalikan kendali atas kepulauan itu kepada mereka.",
    "wtt_britain_lease_azores.4.a": "Bangsa Inggris selalu melunasi kewajibannya.",
    "wtt_britain_lease_azores.5.t": "Inggris Meninggalkan Azores",
    "wtt_britain_lease_azores.5.desc": "Dengan perang di Eropa yang telah usai, [From.GetNameDef] telah menghormati perjanjian kita dan mengembalikan Kepulauan Azores kepada kita. Kita telah mengirim sekelompok administrator untuk mengambil alih kendali kembali.",
    "wtt_britain_lease_azores.5.a": "Hasil terbaik yang bisa diharapkan.",

    # 818 - 822: Soviet city defense
    "wtt_soviet_hold_city_t_success": "[soviet_city.GetName] Bertahan Kokoh",
    "wtt_soviet_hold_city_d_success": "Meskipun diterjang gempuran musuh, para pembela [soviet_city.GetName] tetap teguh bertahan dan memukul mundur musuh. Pasukan penyerbu menderita kerugian darah yang luar biasa di hadapan garis pertahanan, membayar mahal untuk setiap sentimeter tanah yang direbut. Kisah-kisah Pahlawan [state.GetName] akan dikenang turun-temurun hingga generasi mendatang!",
    "wtt_soviet_hold_city_o_success": "[soviet_city.GetName] akan tetap menjadi milik kita!",
    "wtt_soviet_hold_city_t_fail": "[soviet_city.GetName] Jatuh",
    "wtt_soviet_hold_city_d_fail": "Mengerahkan segenap kekuatan yang tersedia, para penyerbu [controller.GetAdjective] menghancurkan pertahanan kita di luar [soviet_city.GetName]. Pasukan [controller.GetAdjective] telah memasuki kota. Saat pasukan pertahanan kita bertempur sengit dalam perang kota yang brutal, kota ini diperkirakan akan jatuh dalam hitungan hari.",

    # 823 - 830: decisions 1-2 Army Command Loyalty
    "decisions.1.t": "Loyalitas Komando Angkatan Darat Tingkat Bawah",
    "decisions.1.desc": "Perwira tertentu di eselon bawah militer telah menyatakan pandangan 'alternatif' mengenai kepemimpinan negara. Untuk membatasi kecurigaan, kita harus membatasi upaya kita dengan hanya mendekati satu calon pendukung, dan kita tidak boleh menghemat sumber daya dalam membeli loyalitas mereka.",
    "decisions.1.a": "Siapa pun boleh, kita hanya butuh seseorang untuk memimpin pasukan kita.",
    "decisions.1.b": "Kita membutuhkan seseorang yang setidaknya memahami tugasnya.",
    "decisions.1.c": "Kualitas adalah yang terpenting, kita tidak boleh berkompromi soal biaya.",
    "decisions.1.d": "Hanya yang terbaik dari yang terbaik yang dapat diterima.",
    "decisions.2.t": "Loyalitas Komando Angkatan Darat Tingkat Atas",
    "decisions.2.desc": "Perwira tertentu di eselon atas militer telah menyatakan pandangan 'alternatif' mengenai kepemimpinan negara. Untuk membatasi kecurigaan, kita harus membatasi upaya kita dengan hanya mendekati satu calon pendukung, dan kita tidak boleh menghemat sumber daya dalam membeli loyalitas mereka.",
    "wtt_soviet_hold_city_o_fail": "Kemunduran kecil belaka.",

    # 832 - 842: wtt_news.40 Suez Canal Blown
    "wtt_news.40.t": "Terusan Suez Diledakkan",
    "wtt_news.40.desc_eng": "Menanggapi pergerakan pasukan musuh yang kian mendekati Terusan Suez, dan risiko hilangnya urat nadi perdagangan penting ke tangan musuh, [From.GetNameDef] memilih untuk meledakkan terusan tersebut demi memastikan penggunaannya tidak jatuh ke pihak lawan. Melalui kombinasi kapal penyumbat, peledakan terarah, dan ranjau, kehancuran yang ditimbulkan sangat masif, dan kemungkinan butuh waktu berbulan-bulan upaya industri intensif untuk memperbaikinya.",
    "wtt_news.40.desc_not_eng": "Dalam apa yang hanya bisa digambarkan sebagai operasi militer yang berani dan brilian, [From.GetNameDef] telah berhasil memutus urat nadi perdagangan vital Terusan Suez. Melalui kombinasi kapal pemblokir, peledakan terarah, dan ranjau, kehancurannya sangat parah, dan diperkirakan akan membutuhkan waktu berbulan-bulan upaya industri besar-besaran untuk memperbaikinya.",
    "wtt_news.40.a": "Sebuah malapetaka!",
    "wtt_news.40.b": "Kita tidak boleh membiarkan musuh memanfaatkannya.",
    "wtt_news.40.c": "Kita tidak akan meremehkan tekad mereka lagi.",
    "wtt_news.40.d": "Kita telah memutus tali penghubung ke Kekaisaran mereka!",
    "wtt_news.40.e": "Pukulan telak nan luar biasa terhadap bangsa Inggris!",
    "wtt_news.40.f": "Mereka mengambil keputusan yang tepat.",
    "wtt_news.40.g": "Pukulan berat bagi sekutu kita...",
    "wtt_news.40.h": "Ini akan berdampak pada seluruh dunia...",

    # 843 - 853: wtt_news.41 Panama Canal Blown
    "wtt_news.41.t": "Terusan Panama Diledakkan",
    "wtt_news.41.desc_usa": "Menanggapi ketidakmampuan mereka mempertahankan Terusan Panama, dan risiko hilangnya urat nadi komunikasi militer vital ke tangan musuh, [From.GetNameDef] memilih untuk meledakkan terusan tersebut guna memastikan musuh tidak dapat menggunakannya. Melalui kombinasi penenggelaman kapal perintang, pembongkaran bahan peledak, dan penyebaran ranjau, kerusakan yang ditimbulkan sangat parah, dan kemungkinan butuh berbulan-bulan upaya industri berat untuk memperbaikinya.",
    "wtt_news.41.desc_not_usa": "Dalam aksi yang hanya bisa diartikan sebagai operasi militer yang berani dan gemilang, [From.GetNameDef] berhasil memutus urat nadi komunikasi militer yang sangat penting yaitu Terusan Panama. Melalui perpaduan kapal penghalang, peledakan, dan ranjau, kehancurannya nyaris total, dan dipastikan akan menuntut kerja keras industri selama berbulan-bulan untuk memulihkannya.",
    "wtt_news.41.a": "Sebuah malapetaka!",
    "wtt_news.41.b": "Kita tidak boleh membiarkan musuh mempergunakannya.",
    "wtt_news.41.c": "Kita tidak akan meremehkan ketetapan hati mereka lagi.",
    "wtt_news.41.d": "Armada laut mereka terputus di sisi seberang!",
    "wtt_news.41.e": "Pukulan spektakuler terhadap bangsa Amerika!",
    "wtt_news.41.f": "Mereka mengambil langkah yang tepat.",
    "wtt_news.41.g": "Pukulan hebat bagi sekutu kita...",
    "wtt_news.41.h": "Pasifik dan Atlantik terpisahkan sekali lagi.",

    # 854 - 860: wtt_news.42 Suez Canal Repaired
    "wtt_news.42.t": "Terusan Suez Diperbaiki",
    "wtt_news.42.desc": "Dengan pengerahan tenaga industri yang luar biasa, [From.GetNameDef] telah berhasil memperbaiki Terusan Suez. Pagi ini menandai pembukaan kembali urat nadi perdagangan vital menuju Laut Mediterania, setelah lebih dari setengah tahun pekerjaan perbaikan intensif.",
    "wtt_news.42.a": "Kita telah memulihkan jalur penghubung ke Kekaisaran kita.",
    "wtt_news.42.b": "Investasi yang mutlak diperlukan bagi bangsa kita.",
    "wtt_news.42.c": "Ini akan sangat membantu perjuangan kita.",
    "wtt_news.42.d": "Mereka telah membalikkan kemunduran itu...",
    "wtt_news.42.e": "Dampaknya akan dirasakan oleh semua pihak.",

    # 861 - 867: wtt_news.43 Panama Canal Repaired
    "wtt_news.43.t": "Terusan Panama Diperbaiki",
    "wtt_news.43.desc": "Dengan pengerahan daya industri yang amat besar, [From.GetNameDef] telah berhasil memulihkan Terusan Panama. Pagi ini menyaksikan pembukaan kembali jalur militer vital antara Samudra Atlantik dan Pasifik, menyusul lebih dari satu tahun perbaikan terpadu.",
    "wtt_news.43.a": "Kita telah memulihkan penghubung penting di antara kedua samudra kita.",
    "wtt_news.43.b": "Kita kini dapat kembali berlayar bebas dari Pasifik ke Atlantik.",
    "wtt_news.43.c": "Ini akan sangat menunjang upaya perang kita.",
    "wtt_news.43.d": "Mereka telah mengatasi kemunduran tersebut...",
    "wtt_news.43.e": "Dampaknya akan dirasakan oleh seluruh dunia.",

    # 868 - 874: wtt_news.44 MAN claims Mandate of Heaven
    "wtt_news.44.t": "[MAN.GetLeader] Mengklaim Mandat Langit",
    "wtt_news.44.desc": "Mengenakan jubah berhias mewah yang layak bagi seorang Kaisar Tiongkok, [MAN.GetLeader], Putra Langit, Penguasa Sepuluh Ribu Tahun, Kaisar Dinasti Qing yang Agung, telah bertakhta di Takhta Naga dalam upacara Penobatan kedua yang tak lazim dan kini bersemayam di dalam Kota Terlarang sebagaimana para leluhurnya dahulu. Merujuk pada adat istiadat kuno, [MAN.GetLeader] mengklaim bahwa kemenangan pasukannya dalam Perang Saudara Tiongkok membuktikan bahwa ia memegang Mandat Langit untuk memimpin Tiongkok.\\n\\nApakah ia bermaksud meluaskan kekuasaannya hingga mencakup 'Segala Sesuatu di Bawah Langit', seperti yang diklaim oleh para Kaisar sebelumnya, masih harus dinantikan.",
    "wtt_news.44.a": "Sang Putra Langit telah kembali.",
    "wtt_news.44.b": "Kesalahan masa lalu telah diluruskan.",
    "wtt_news.44.c": "Ia pikir ia ini siapa?",
    "wtt_news.44.d": "Kemunculan kembali yang luar biasa.",
    "wtt_news.44.e": "Sangat mustahil dan mengada-ada!"
}

with open("wtt_events_raw.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

# Slice 724:875
slice_raw = raw[724:875]
out = []
missing = []

for item in slice_raw:
    k = item["key"]
    if k in chunk6_translations:
        out.append({"key": k, "id": chunk6_translations[k]})
    else:
        missing.append(k)

if missing:
    print("MISSING KEYS in chunk 6:", missing)
else:
    with open("wtt_events_chunk6.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved events chunk 6: {len(out)} entries")
