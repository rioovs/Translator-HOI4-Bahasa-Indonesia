# -*- coding: utf-8 -*-
"""
Translation script for Batch 3: Germany & AAT Germany Events (242 entries)
"""

import json
import re

translations_part1 = {
    "germany.4.t": "Anschluss",
    "germany.4.d": "Pemberontakan yang berulang kali terjadi di Austria dengan jelas menunjukkan bahwa rakyat di sana mendambakan persatuan dengan Reich kita. Kini saatnya untuk bertindak dan membiarkan kehendak rakyat terwujud secara nyata.",
    "germany.5.t": "Pakta Anti-Komintern",
    "germany.5.d": "Jerman mengusulkan agar kita menandatangani sebuah pakta untuk menanggapi tujuan Komintern dalam menyebarkan Komunisme ke seluruh dunia melalui subversi dan kekerasan. Dengan menandatangani pakta ini, kita sepakat untuk berbagi intelijen mengenai ancaman Komunis dan bertindak dalam kerja sama erat melawan ancaman ini.",
    "germany.6.t": "Pakta Tripartit",
    "germany.6.d": "Para penandatangan memandang sebagai prasyarat bagi perdamaian abadi bahwa setiap bangsa di dunia diberikan tempatnya masing-masing yang layak, dan telah memutuskan untuk saling berdiri berdampingan serta bekerja sama dalam upaya mereka masing-masing di Asia Timur Raya dan wilayah Eropa, di mana tujuan utama mereka adalah membangun dan memelihara suatu tatanan baru yang diperhitungkan demi memajukan kemakmuran dan kesejahteraan bersama bagi bangsa-bangsa yang bersangkutan.",
    "germany.11.t": "Pakta Molotov-Ribbentrop",
    "germany.11.d": "Kementerian Luar Negeri Jerman telah mengusulkan pakta non-agresi antara kedua negara kita. Perjanjian ini akan sangat meningkatkan perdagangan timbal balik kita, dan protokol rahasia tambahan mengusulkan pembagian Eropa Timur ke dalam lingkup pengaruh Jerman dan Soviet.\\n\\nMeskipun kaum fasis di Berlin mungkin tidak dapat dipercaya, pakta ini akan memungkinkan kita untuk menghadapi Finlandia, Negara-negara Baltik, dan Rumania tanpa takut akan campur tangan pihak luar. Wilayah timur Polandia juga akan jatuh ke tangan kita jika Polandia runtuh.",
    "germany.12.t": "Moskow Menandatangani Pakta",
    "germany.12.d": "[SOV.GetNameDefCap] telah dengan bijak setuju untuk menandatangani pakta non-agresi kita. Ini berarti kita bebas bertindak tanpa risiko intervensi Soviet.\\n\\nSayangnya, beberapa sekutu kita kini mempertanyakan komitmen Jerman terhadap pemusnahan akhir komunisme. Ketika urusan dengan Polandia dan Prancis telah diselesaikan, kita mungkin perlu meninjau kembali perjanjian ini, tetapi itu adalah pembahasan untuk lain waktu...",
    "germany.13.t": "Moskow Menolak Pakta",
    "germany.13.d": "[SOV.GetNameDefCap] telah menolak untuk menandatangani pakta non-agresi kita! Hal ini memperumit masalah, karena kita tidak dapat bertindak tegas terhadap Polandia atau Prancis tanpa risiko kaum Bolshevik ikut campur.",
    "germany.14.t": "Pembagian Polandia",
    "germany.14.d": "Polandia adalah milik kita, tetapi bagian timurnya jatuh ke dalam lingkup pengaruh [SOU.GetAdjective] sesuai ketentuan Pakta Molotov-Ribbentrop. Haruskah kita menarik pasukan kita dan membiarkan bangsa [SOU.GetAdjective] menduduki wilayah ini? Kegagalan untuk melakukannya akan membatalkan perjanjian kita.",
    "germany.15.t": "Jerman Menghormati Pakta",
    "germany.15.d": "Sesuai dengan Pakta Molotov-Ribbentrop, pasukan Jerman telah mengevakuasi Polandia timur dan pasukan kita sendiri telah bergerak maju untuk menduduki wilayah tersebut.",
    "germany.16.t": "[From.GetNonIdeologyName] Mengkhianati Pakta",
    "germany.16.d": "[From.GetNonIdeologyName] telah menolak untuk membagi Polandia bersama kita, suatu pelanggaran terang-terangan terhadap Pakta Molotov-Ribbentrop! Pengkhianatan ini telah membuat perjanjian kita dengan mereka batal demi hukum!",
    "germany.20.t": "Arbitrase Wina Kedua",
    "germany.20.d": "Menyadari bahwa suatu tatanan baru telah ditegakkan di Eropa, kita telah diminta oleh Hongaria dan Rumania untuk menengahi sengketa wilayah antara kedua negara tersebut. Transilvania direbut dari Hongaria dan digabungkan ke dalam Rumania dalam salah satu dari banyak perubahan keliru yang dipaksakan terhadap dunia di Versailles. Haruskah Transilvania Utara dikembalikan ke bawah kendali Hongaria?",
    "germany.21.t": "Rumania Menolak Putusan Kita",
    "germany.21.d": "Rumania telah menolak untuk mematuhi keputusan yang kita capai dalam Arbitrase Wina Kedua! Delegasi mereka telah ditarik kembali ke Bukares, dan tidak ada wilayah yang diserahkan kepada Hongaria.",
    "germany.22.t": "Memel - [FROM.GetNameDef] Tunduk",
    "germany.22.d": "Pemerintah [FROM.GetAdjective] telah menyetujui tuntutan kita, dan Memel akan digabungkan kembali ke Prusia Timur. Satu lagi provinsi yang dicuri secara tidak sah telah dikembalikan ke pangkuan bangsa Jerman!",
    "germany.23.t": "Memel - [FROM.GetNameDef] Menolak Tuntutan",
    "germany.23.d": "Pemerintah [FROM.GetAdjective] telah menolak tuntutan kita! Mereka bersembunyi di balik Konvensi Klaipeda, mengklaim bahwa Jerman tidak memiliki hak hukum atas wilayah Memel. Kita harus menjelaskan posisi kita kepada mereka melalui cara lain...",
    "germany.24.t": "Misi Militer Jerman ke Tiongkok",
    "germany.24.d": "Jerman menikmati hubungan baik dengan Tiongkok sejak akhir Perang Dunia sebelumnya, terlepas dari hilangnya wilayah milik kita di Tiongkok. Sebuah misi militer Jerman telah hadir di Tiongkok selama beberapa tahun, dan Alexander von Falkenhausen telah membuat kemajuan besar dalam mereformasi sebagian pasukan Kuomintang.\\n\\nHal ini tentu menjadi perhatian pihak Jepang, mengingat perang mereka saat ini melawan Tiongkok. Mereka menuntut penarikan segera seluruh dukungan Jerman untuk Tiongkok.",
    "germany.25.t": "Penasihat Militer Ditarik",
    "germany.25.d": "Hubungan yang memburuk dengan Tiongkok telah membuat kelanjutan misi militer di negara mereka tidak memungkinkan secara politis. Alexander von Falkenhausen dan para penasihat kita lainnya telah ditarik pulang.",
    "germany.26.t": "Tiongkok Menahan Penasihat Militer",
    "germany.26.d": "Jerman dan Tiongkok berada dalam keadaan perang, dan pihak Tiongkok akibatnya menahan para penasihat militer Jerman yang sedang mereformasi pasukan mereka. Von Falkenhausen dan beberapa perwiranya berhasil lolos dari penangkapan, dan kini sedang dalam perjalanan kembali ke Eropa.",
    "germany.27.t": "Memperkuat Tembok Barat",
    "germany.27.d": "Zeni angkatan darat telah menyelesaikan survei benteng pertahanan kita yang ada, dan mengidentifikasi lokasi-lokasi yang harus diperkuat. Perintah pembangunan yang diperlukan telah dikeluarkan.",
    "germany.28.t": "Jerman Mendesak Terjadinya Anschluss",
    "germany.28.d": "Kerusuhan sipil dan aksi kekerasan telah pecah saat para pengunjuk rasa menyuarakan keinginan mereka agar Austria bergabung dengan Jerman dalam suatu persatuan bangsa Jerman. Berlin mendesak keras terjadinya Anschluss, yang akan menganeksasi Austria ke dalam negara mereka.",
    "germany.29.t": "Austria Menolak Anschluss!",
    "germany.29.d": "Orang-orang bodoh di Wina telah menolak untuk menerima penggabungan kedua negara kita! Ini adalah pengabaian terang-terangan terhadap kehendak rakyat Austria, dan ini tidak dapat dibiarkan! Kita mungkin harus memaksakan Anschluss melalui kekuatan militer.",
    "germany.40.t": "Konferensi Munich",
    "germany.40.d": "Tuntutan Jerman atas wilayah Sudetenland di Cekoslowakia, tempat tinggal sejumlah besar etnis Jerman, telah mencapai puncaknya. [GER.GetLeader] telah menempatkan pasukan di sepanjang perbatasan Cekoslowakia sebagai persiapan untuk menyerang. Pembicaraan sedang diadakan di Munich antara Inggris, Prancis, Italia, dan Jerman dengan harapan dapat merundingkan penyelesaian damai atas Krisis Sudeten. Bagaimana sikap Inggris nantinya?",
    "germany.40.d_2": "Tuntutan Jerman atas wilayah Sudetenland di Cekoslowakia, tempat tinggal sejumlah besar etnis Jerman, telah mencapai puncaknya. [GER.GetLeader] telah menempatkan pasukan di sepanjang perbatasan Cekoslowakia sebagai persiapan untuk menyerang. Karena kita telah membuktikan bahwa kita tidak akan menerima ekspansionisme Jerman, ini berarti kita kini memiliki sekutu lain dalam perang melawan Jerman.",
    "germany.40.d_3": "Tuntutan Jerman atas wilayah Sudetenland di Cekoslowakia, tempat tinggal sejumlah besar etnis Jerman, telah mencapai puncaknya. [GER.GetLeader] telah menempatkan pasukan di sepanjang perbatasan Cekoslowakia sebagai persiapan untuk menyerang. Pembicaraan sedang berlangsung di Munich antara Belanda, Inggris, Prancis, Italia, dan Jerman dengan harapan merundingkan akhir yang damai bagi Krisis Sudeten. Bagaimana sikap Belanda nantinya?",
    "germany.41.d": "Tuntutan Jerman atas wilayah Sudetenland di Cekoslowakia, tempat tinggal sejumlah besar etnis Jerman, telah mencapai puncaknya. [GER.GetLeader] telah menempatkan pasukan di sepanjang perbatasan Cekoslowakia sebagai persiapan untuk menyerang. Pembicaraan sedang berlangsung di Munich antara Inggris, Prancis, Italia, dan Jerman demi merundingkan penyelesaian damai Krisis Sudeten.\\n\\nInggris telah menegaskan bahwa mereka tidak berniat berperang demi 'pertikaian di negeri yang jauh.' Haruskah kita mengikuti langkah mereka, atau akankah kita menghormati kewajiban kita kepada Cekoslowakia dengan memberikan dukungan kepada mereka?",
    "germany.42.d": "Tuntutan Jerman atas wilayah Sudetenland di Cekoslowakia, tempat tinggal sejumlah besar etnis Jerman, telah mencapai puncaknya. [GER.GetLeader] telah menempatkan pasukan di sepanjang perbatasan Cekoslowakia sebagai persiapan untuk menyerang. Pembicaraan sedang diadakan di Munich antara Inggris, Prancis, Italia, dan Jerman dengan harapan merundingkan penyelesaian damai Krisis Sudeten.\\n\\nInggris menolak untuk mundur, dan justru mengancam Jerman dengan perang jika mereka melanggar perbatasan Cekoslowakia. Perang mungkin akan segera pecah.",
    "germany.43.t": "Prancis Keluar dari Sekutu",
    "germany.43.d": "Bangsa Prancis yang keras kepala menolak untuk mengikuti langkah kita dalam Krisis Sudeten! Mereka tetap pada pendirian mendukung Cekoslowakia, dan karena kita tidak, mereka memutuskan untuk membatalkan persekutuan bersama kita. Bahkan saat ini, Prancis sedang bersiap untuk menghadapi perang yang tak terhindarkan dengan Jerman.",
    "germany.44.d": "Tuntutan Jerman atas wilayah kita di kawasan Sudetenland semakin bermusuhan, dan kini pasukan mereka sedang berkumpul di sepanjang perbatasan kita! Sebuah konferensi sedang diadakan di Munich di mana para pemimpin Eropa mendiskusikan masa depan Cekoslowakia, tetapi kita tidak diundang.\\n\\nUntungnya, tampaknya pihak Sekutu akan menepati janji dukungan awal mereka. Mereka telah mengancam [GER.GetLeader] dengan perang jika perbatasan kita dilanggar sedikit pun. Terlepas dari itu, kita harus bersiap menghadapi serangan Jerman yang dapat terjadi sewaktu-waktu.",
    "germany.45.d": "Tuntutan Jerman atas wilayah kita di wilayah Sudetenland semakin bermusuhan, dan kini pasukan mereka sedang berkumpul di sepanjang perbatasan kita! Sebuah konferensi sedang diadakan di Munich di mana para pemimpin Eropa memperbincangkan masa depan Cekoslowakia, namun kita tidak diundang.\\n\\nKaum pengecut Inggris telah menolak untuk mendukung kedaulatan kita, tetapi setidaknya Prancis membela kita! Mereka telah meninggalkan persekutuan dengan Inggris dan membentuk persekutuan baru bersama kita, berjanji untuk membela Cekoslowakia melawan agresi Jerman.",
    "germany.46.t": "Diktat Munich",
    "germany.46.d": "Tuntutan Jerman atas wilayah kita di kawasan Sudetenland semakin mengancam, dan kini pasukan mereka memadati sepanjang perbatasan kita! Sebuah konferensi sedang diadakan di Munich tempat para pemimpin Eropa mendiskusikan masa depan Cekoslowakia, tetapi kita tidak diundang.\\n\\nBaik Inggris maupun Prancis telah menarik kembali janji awal mereka untuk mendukung kita melawan agresi Jerman. Diplomat mereka telah menegaskan bahwa jika kita memilih melawan Jerman, kita harus melakukannya sendirian. Barangkali kita tidak punya pilihan selain menyerahkan Sudetenland...",
    "germany.47.d": "Pembicaraan telah digelar di Munich antara para pemimpin Jerman, Inggris, Prancis, dan Italia untuk membahas masa depan Cekoslowakia. Baik pihak Inggris maupun Sekutu mereka telah menolak klaim sah kita atas Sudetenland, dan mereka mengancam kita dengan perang jika kita 'melanggar' perbatasan Ceko!\\n\\nRencana invasi ke Cekoslowakia telah disusun, tetapi hal ini kemungkinan besar akan memicu perang Eropa secara umum. Kita harus memastikan bahwa kita siap untuk ini.",
    "germany.48.d": "Pembicaraan telah digelar di Munich antara para pemimpin Jerman, Inggris, Prancis, dan Italia untuk membahas masa depan Cekoslowakia. Pihak Inggris telah berpikir jernih dan menerima klaim kita atas Sudetenland sebagai klaim yang sah, tetapi pihak Prancis yang keras kepala menolak untuk mundur.\\n\\nMereka telah meninggalkan kerja sama dengan Inggris dan justru menjalin hubungan lebih erat dengan pihak Ceko. Tampaknya kita harus menghadapi mereka berdua secara bersamaan, tetapi setidaknya kini pihak Inggris diharapkan tidak akan campur tangan...",
    "germany.49.d": "Pembicaraan telah digelar di Munich antara para pemimpin Jerman, Inggris, Prancis, dan Italia untuk membahas masa depan Cekoslowakia. Baik Inggris maupun Prancis telah menerima klaim kita atas Sudetenland sebagai klaim yang sah, dan tawaran dukungan mereka sebelumnya kepada Ceko telah ditarik kembali.\\n\\nKendati situasi mereka tanpa harapan, pihak Ceko yang keras kepala menolak untuk menyerahkan wilayah mereka! Kita harus merebutnya dengan kekerasan. Rencana invasi telah disiapkan yang akan menghapus eksperimen tercela Versailles ini dari muka bumi!",
    "germany.50.d": "Pembicaraan telah digelar di Munich antara para pemimpin Jerman, Inggris, Prancis, dan Italia untuk membahas masa depan Cekoslowakia. Baik Inggris maupun Prancis telah menerima klaim kita atas Sudetenland sebagai klaim yang sah, dan tawaran dukungan mereka sebelumnya kepada bangsa Ceko telah dicabut.\\n\\nMenyadari situasi mereka yang mustahil, bangsa Ceko telah menyerahkan wilayah Sudeten kepada kita. Penduduk Jerman yang tertindas di sana akhirnya akan dibawa masuk ke pangkuan Vaterland!",
    "germany.51.t": "Arbitrase Wina Pertama",
    "germany.51.d": "Cekoslowakia adalah tumor kanker di jantung Eropa, dan akhirnya bangsa [GER.GetAdjective] memutuskan untuk mengambil tindakan tegas terhadap mereka. Sudetenland telah diserahkan kepada Jerman, dan kini, sebagai konsekuensi dari Perjanjian Munich, wilayah Cekoslowakia yang sah milik Hongaria akan dikembalikan kepada kita.",
    "germany.52.t": "Aneksasi Zaolzie",
    "germany.52.d": "Cekoslowakia sedang hancur lebur, dan kita harus bertindak cepat untuk melindungi wilayah dengan populasi Polandia yang signifikan sebelum direbut oleh Jerman. Kepemilikan Ceko atas Zaolzie selalu kami sengketakan, dan kini saatnya wilayah tersebut bergabung dengan bangsa kita.",
    "germany.53.t": "Nasib Cekoslowakia",
    "germany.53.d": "Tidak puas hanya dengan mencuri Sudetenland, bangsa Jerman kini memutuskan untuk merebut seluruh negeri kita. Ditinggalkan oleh mereka yang mengaku sebagai sekutu kita, dan dengan pertahanan terbaik kita lenyap dalam Diktat Munich, situasi tampak tanpa harapan...",
    "germany.54.t": "Ceko Melawan",
    "germany.54.d": "Entah bagaimana, bangsa Ceko berhasil mengumpulkan keberanian untuk melawan pendudukan kita atas negara mereka. Pertahanan terbaik mereka berada di Sudetenland, yang kini berada di bawah kendali kita, jadi ini mestinya menjadi kampanye militer yang singkat.",
    "germany.55.d": "Akhir dari Cekoslowakia sudah di depan mata, dan pasukan kita sedang berbaris memasuki Praha saat ini juga. Dengan menyerahnya militer Cekoslowakia, kita telah membebaskan persenjataan dalam jumlah besar. Tank-tank mereka, khususnya, akan sangat berguna bagi pasukan kita.\\n\\nBöhmen akan dianeksasi ke dalam Jerman sebagai protektorat, tetapi apa yang harus dilakukan terhadap Slowakia? Kita dapat menjadikannya negara boneka otonom di bawah pimpinan Jozef Tiso.",
    "germany.55.d_2": "Setelah menaklukkan Cekoslowakia, kita harus mempertimbangkan cara terbaik untuk membagi wilayah-wilayah ini.\\n\\nBöhmen tetap menjadi milik Jerman sebagai protektorat, tetapi bagaimana dengan Slowakia? Kita dapat menjadikannya negara boneka otonom di bawah pimpinan Jozef Tiso.",
    "germany.56.t": "Pembagian Cekoslowakia",
    "germany.56.d": "Pasukan Jerman telah memasuki Praha dan akhir dari Cekoslowakia sudah di ambang pintu. Mereka berniat menganeksasi Bohemia ke dalam Reich Jerman, tetapi mereka bersedia menyerahkan Slowakia kepada kita. Haruskah kita menyetujui pembagian ini? Ini berarti memasuki aliansi militer formal dengan Jerman.",
    "germany.56.d_2": "Setelah menganeksasi Cekoslowakia, Jerman berniat mempertahankan Bohemia sebagai bagian dari Reich, tetapi mereka bersedia menyerahkan Slowakia kepada kita. Haruskah kita menyetujui pembagian ini? Ini berarti menyepakati aliansi militer resmi dengan Jerman.",
    "germany.57.t": "Hongaria Menolak Tawaran Kita",
    "germany.57.d": "Pihak Hongaria secara keterlaluan menolak tawaran murah hati kita untuk menganeksasi Slowakia, mengklaim bahwa mereka tidak memiliki kepentingan di wilayah tersebut! Kita harus segera berurusan dengan mereka nanti. Untuk saat ini, kita harus mencari solusi untuk Masalah Slowakia.",
    "germany.58.t": "Masalah Polandia",
    "germany.58.d": "Reichsministerium Pencerahan Publik dan Propaganda telah melakukan pekerjaan luar biasa, dan rakyat Jerman — bahkan seluruh dunia — telah diberitahu mengenai ketidakadilan yang terpaksa dialami saudara-saudara Jerman kita di Polandia. Kini kita memiliki semua pembenaran yang kita butuhkan untuk perang!",
    "germany.59.desc": "Dalam sebuah langkah berani dan sepihak, [GER.GetNameDef] telah menetapkan pemindahan wilayah [664.GetName] kepada [FROM.GetNameDef]. Keputusan ini, yang didiktekan tanpa konsultasi maupun persetujuan, menandai pembongkaran lebih lanjut atas integritas teritorial [ROOT.GetNameDef] dan pengingat nyata akan kerentanan geopolitik kita.\\nDelegasi [GER.GetAdjective], dengan merujuk klaim sejarah lama, telah menekan para pemimpin kita untuk tunduk pada revisi teritorial ini. Hilangnya [664.GetName], kawasan yang kaya akan budaya dan sumber daya, ke tangan [FROM.GetNameDef] adalah pil pahit yang harus ditelan oleh rakyat kita dan tantangan langsung terhadap kedaulatan bangsa kita."
}

print(f"Loaded Part 1: {len(translations_part1)} entries")

translations_part2 = {
    "germany.60.t": "Remiliterisasi Rhineland",
    "germany.60.d": "Beberapa divisi Jerman baru-baru ini bergerak maju ke Rhineland, menandai pertama kalinya sejak berakhirnya Perang Besar bahwa Jerman menempatkan pasukannya di sebelah barat Rhein. Ini adalah pelanggaran nyata terhadap Perjanjian Versailles, di mana Jerman dilarang memiliterisasi wilayah tersebut! Kecuali kita mengeluarkan ultimatum yang menuntut penarikan mundur mereka, perjanjian itu tidak akan dapat ditegakkan.",
    "germany.61.d": "Beberapa divisi Jerman baru-baru ini bergerak maju ke Rhineland, menandai pertama kalinya sejak berakhirnya Perang Besar bahwa Jerman menempatkan pasukan di sebelah barat Rhein. Hal ini merupakan pelanggaran nyata terhadap Perjanjian Versailles, di mana Jerman dilarang memiliterisasi kawasan tersebut!\\n\\nPihak Prancis sedang memobilisasi pasukan mereka, dan tampaknya berniat mengeluarkan ultimatum. Jika Jerman menolak, mereka siap maju ke dalam wilayah Jerman untuk mengatasi ancaman ini. Opini publik di Inggris menentang perang, namun jika kita menolak mendampingi Prancis, aliansi kita dengan mereka akan dibubarkan.",
    "germany.62.d": "Beberapa divisi Jerman baru-baru ini bergerak maju ke Rhineland, menandai pertama kalinya sejak berakhirnya Perang Besar bahwa Jerman menempatkan pasukannya di sebelah barat Rhein. Ini merupakan pelanggaran nyata terhadap Perjanjian Versailles, di mana Jerman dilarang memiliterisasi wilayah tersebut!\\n\\nPihak Prancis tampaknya puas membatasi tanggapan mereka terhadap pelanggaran ini hanya pada keberatan diplomatik, dan opini publik di Inggris dengan tegas menentang peperangan.",
    "germany.63.t": "Inggris Menolak Perang",
    "germany.63.d": "Pihak Inggris menolak mendukung kita melawan Jerman, mengklaim bahwa orang Jerman 'hanya berjalan di halaman belakang rumah mereka sendiri.' Jika kita berperang dengan mereka, tampaknya kita harus berjuang sendirian.\\n\\nOpini publik di Prancis menentang perang, tetapi Jerman hanya akan bertambah kuat dan remiliterisasi Rhineland merupakan ancaman langsung terhadap perbatasan kita. Mengeluarkan ultimatum akan kurang mengancam tanpa Inggris di pihak kita. Haruskah kita maju melawan mereka sendirian?",
    "germany.64.t": "Inggris Mendukung Kita",
    "germany.64.d": "Meskipun dukungan publik untuk perang minim di Inggris, pemerintah Inggris telah menyadari ancaman yang ditimbulkan oleh Jerman dan mereka menawarkan dukungan penuh kepada kita. Kita akan mengeluarkan ultimatum terakhir kepada Jerman agar mundur dari zona demiliterisasi. Jika mereka menolak, saatnya bagi pasukan kita untuk merangsek jauh ke dalam wilayah Jerman dan mengakhiri rezim tiran mereka!",
    "germany.65.t": "Prancis dan Inggris Memobilisasi Pasukan!",
    "germany.65.d": "Pihak Inggris dan Prancis menolak menerima remiliterisasi Rhineland, menyebutnya sebagai 'pelanggaran tak termaafkan' terhadap Perjanjian Versailles. Mereka memobilisasi pasukan untuk melawan kita dan mengeluarkan ultimatum agar pasukan kita segera mundur dan Rhineland tetap didemiliterisasi, atau negara kita akan berada dalam keadaan perang.",
    "germany.66.t": "Prancis Memobilisasi Pasukan!",
    "germany.66.d": "Pihak Inggris dapat berpikir jernih dan menerima remiliterisasi Rhineland, tetapi pihak Prancis yang gila menolak untuk mundur! Dengan dalih bahwa insiden ini merupakan ancaman langsung terhadap keamanan negara mereka, mereka memobilisasi pasukannya dan dapat menyerbu melintasi perbatasan kapan saja! Kita berada dalam perang!",
    "germany.67.t": "Prancis Mundur",
    "germany.67.d": "Pihak Prancis dengan bijak memilih mundur ketika mereka menyadari bahwa rencana gila mereka tidak akan mendapat dukungan Inggris. Pasukan mereka telah didemobilisasi dan perang berhasil dihindari untuk saat ini. Demi Tuhan, nyaris saja!",
    "germany.68.t": "Prancis Menolak Mundur",
    "germany.68.d": "Prancis dengan keras kepala memutuskan untuk bertindak sendirian melawan Jerman, dan aliansi kita dengan mereka telah dicabut. Satu lagi perang Eropa telah meletus akibat perselisihan yang sia-sia. Barangkali sudah saatnya bagi Inggris untuk kembali menjaga jarak dari urusan benua Eropa...",
    "germany.70.t": "Konspirasi Oster",
    "germany.70.d": "Berkeyakinan bahwa Hitler telah menyeret Jerman ke dalam perang yang mustahil dimenangkan, sekelompok perwira senior di dalam Wehrmacht melancarkan kudeta! Kudeta ini tampaknya didalangi oleh Kolonel Hans Oster dari Abwehr, namun jenderal Beck, von Brauchitsch, Halder, serta Laksamana Canaris juga telah dipastikan terlibat!\\n\\nPasukan bersenjata lengkap yang menunggu di beberapa apartemen Berlin bergerak mengepung Reichskanzlei dengan niat melenyapkan Hitler dan rekan-rekan terdekatnya. Baku tembak sengit saat ini berkecamuk di dalam gedung.",
    "germany.71.t": "Sang Führer Telah Tewas",
    "germany.71.d": "Pasukan SS dan unit angkatan darat yang setia bergegas menuju Reichskanzlei dan berhasil menewaskan atau menangkap semua komando pengkhianat, tetapi anjing-anjing itu telah berhasil membunuh Hitler! Sang Führer ditemukan terkulai di atas mejanya dengan puluhan luka tembak — bekerja tanpa lelah demi Vaterland hingga hembusan napas terakhirnya, tak diragukan lagi! Orang kepercayaannya sejak lama, Eva Braun, terluka dalam baku tembak tersebut, namun tampaknya akan pulih pada waktunya.\\n\\nPara konspirator yang masih hidup akan diadili atas kejahatan keji mereka, tetapi saat ini Jerman sedang berperang dan seorang pemimpin baru sangat dibutuhkan. Siapakah yang akan menjadi Führer berikutnya?",
    "germany.72.t": "Konspirasi Gagal",
    "germany.72.d": "Pasukan SS dan unit angkatan darat yang setia bergegas menuju Reichskanzlei dan berhasil menewaskan atau menangkap semua komando pengkhianat, bahkan Hitler sendiri memimpin pembersihan itu dengan pistol Luger andalannya. Secara ajaib, sang Führer keluar dari pertempuran hanya dengan beberapa luka gores ringan.\\n\\nPara konspirator yang selamat akan membayar mahal atas ketidaksetiaan mereka, dan Hitler kini semakin berkomitmen untuk mengobarkan perang saat ini menuju kemenangan gilang-gemilang!",
    "germany.73.t": "Konspirasi Berhasil",
    "germany.73.d": "Pertempuran sengit di Reichskanzlei telah meluluhlantakkan gedung itu menjadi reruntuhan yang membara. Terlepas dari banyaknya tentara SS yang bergegas menolong Hitler, unit angkatan darat yang setia kepada para konspirator ikut terjun ke pertempuran dan menjadi penentu kemenangan. Sang Führer telah dipastikan tewas, teman dekatnya Eva Braun terluka parah dalam baku tembak, dan para konspirator telah berhasil menyerbu seluruh gedung pemerintahan di Berlin.\\n\\nSebagian besar Wehrmacht telah membelot ke pihak lain, tetapi banyak perwira yang masih setia kepada NSDAP. Siapakah yang pantas memimpin mereka?",
    "germany.74.t": "Mempersiapkan Landasan",
    "germany.74.d": "Rakyat Austria mendambakan untuk menjadi bagian dari Reich Jerman, namun pemerintah di Wina yang keras kepala sejauh ini menolak semua upaya untuk mewujudkan persatuan. Kita harus meningkatkan dukungan terhadap fasisme di Austria. Partai Nazi Austria kemudian akan menjadi alternatif yang kuat bagi kaum austrofasis yang berkuasa.\\n\\nSeorang agen Abwehr telah disiapkan untuk misi spionase. Gunakan dia untuk meningkatkan dukungan rakyat terhadap fasisme secara rahasia di Austria.",
    "germany.75.t": "Perjanjian Jerman-Soviet",
    "germany.75.d": "Terlepas dari retorika keras sebelumnya terhadap rakyat maupun kepemimpinan ideologis [Root.GetName], [From.GetLeader] dan Jerman kini menghubungi kita, meminta perjanjian riset yang saling menguntungkan. Walaupun pertukaran pengetahuan akan membantu upaya kita mengembangkan rancangan tank baru bersama janji manfaat riset lainnya di masa depan, mengingat pernyataan sebelumnya kecil keraguan bahwa Jerman melakukan ini demi kepentingan mereka sendiri. Haruskah kita melanjutkan perjanjian ini terlepas dari risiko membantu ambisi [From.GetLeader]?",
    "germany.76.t": "Soviet Menerima Perjanjian Jerman-Soviet",
    "germany.76.d": "Perundingan kita dengan [From.GetName] telah berhasil. Suatu kesepakatan telah dicapai di mana kedua negara kita akan saling membantu dalam pengembangan unit lapis baja baru, dengan kemungkinan perluasan ke bidang penelitian lain di masa depan.",
    "germany.77.t": "Soviet Menolak Perjanjian Jerman-Soviet",
    "germany.77.d": "[From.GetName] telah menolak usulan perjanjian kita yang bertujuan memajukan penelitian unit lapis baja di kedua negara, diduga karena khawatir senjata unggul kita kelak akan digunakan untuk melawan mereka.",
    "germany.78.t": "Riset Udara Bersama Jerman",
    "germany.78.d": "Sebagaimana ditetapkan oleh perjanjian dengan Jerman, beberapa proyek riset khusus mereka membagikan penemuan dengan para insinyur kita. Terobosan terbaru dalam teknologi radar telah menarik perhatian kita, membuka peluang tak terduga untuk memajukan riset kita di bidang tersebut.",
    "germany.79.t": "Ultimatum dari Jerman",
    "germany.79.d": "Dengan Yunani di bawah cengkeraman Jerman, [From.GetLeader] telah menekan pemerintah kita untuk bergabung dengan barisan mereka. Aliansi Soviet-Jerman menempatkan kita pada posisi di mana netralitas bukan lagi sebuah pilihan, dan kini sebuah ultimatum telah tiba dari Berlin yang menuntut kita menyerahkan wilayah timur kita kepada sekutu Soviet mereka dan bergabung dalam pakta yang mereka gunakan untuk menekan kita.\\n\\nKendati kita tidak dapat mempertahankan netralitas, ada pilihan lain. Mencari dukungan dari Inggris adalah salah satunya, mempertahankan posisi kita adalah yang lain. Namun, tak satu pun yang dapat menjamin masa depan republik dengan pasti.",
    "germany.80.t": "Danzig untuk Slowakia",
    "germany.80.d": "Bangsa Jerman telah lama mengincar Danzig demi menyatukan wilayah mereka di Ostpreussen dengan seluruh bangsa Jerman lainnya. Para diplomat telah memperingatkan bahwa harinya mungkin akan tiba ketika mereka memaksa kita memilih antara Danzig atau perang.\\n\\nSecara mengejutkan, kita telah disodori apa yang dianggap Jerman sebagai solusi yang lebih damai. Mereka menawarkan negara Slowakia yang baru dibentuk, yang saat ini tak lebih dari sekadar negara boneka di bawah kekuasaan Jerman, kepada kita sebagai imbalan atas Danzig.\\nLangkah apa yang akan diambil Jerman jika kita menolak tidak diketahui, namun kita telah diberi kesempatan untuk menyelesaikan konflik ini dengan beberapa keuntungan wilayah.",
    "germany.81.t": "Danzig Diserahkan demi Slowakia",
    "germany.81.d": "Polandia telah menyetujui pertukaran di mana Danzig akan diserahkan kepada [GER.GetNameDef], sementara Slowakia kini berada di bawah kendali Polandia. Melalui perjanjian ini, kita telah merebut kembali Danzig sembari mempertahankan hubungan yang bersahabat, atau setidaknya tidak bermusuhan secara terbuka, dengan tetangga timur kita.",
    "germany.82.t": "[From.GetNameDefCap] Menolak Menyerahkan Danzig",
    "germany.82.d": "Tawaran murah hati kita berupa wilayah Slowakia kepada [From.GetNameDef] sebagai ganti Danzig telah ditolak, membiarkan Danzig tetap di tangan Polandia. Jelas, [From.GetLeader] tidak memiliki pemahaman yang sama dengan kita bahwa Danzig adalah wilayah Jerman yang sah.\\n[Root.GetLeader] sangat murka, dan opsi diplomatik untuk merebut kembali Danzig tampaknya telah habis.",
    "germany.83.t": "Pakta Anti-Soviet",
    "germany.83.d": "Melalui Pakta Anti-Komintern, [From.GetNameDef] telah mengamankan landasan subur bagi sarana diplomatik untuk membendung ancaman Soviet. Namun, pakta tersebut bukan merupakan aliansi militer, dan juga tidak memuat kewajiban yang jelas bagi para penandatangannya. [From.GetLeader] kini berupaya memperluas pakta tersebut menjadi koalisi Anti-Soviet, sebuah perjanjian yang mengikat untuk bergabung bersama dalam perang jika ada salah satu penandatangan yang terlibat dalam keadaan perang dengan Uni Soviet.\\n\\nMeskipun jauh lebih berbahaya, dan kemungkinan besar mengakhiri segala diplomasi yang masih kita jalin dengan pihak Soviet, ini juga merupakan kesempatan kita untuk memastikan bahwa kita memiliki sekutu yang kuat di pihak kita jika terjadi perang.",
    "germany.84.t": "Memanggil Anggota Pakta untuk Berperang",
    "germany.84.d": "Tepat seperti dugaan kita saat menandatangani Pakta Anti-Soviet, kini kita mendapati diri kita dalam keadaan perang dengan Uni Soviet. Sudah saatnya bagi sesama penandatangan untuk menepati janji mereka dan bergabung bersama kita.",
    "germany.85.t": "[From.GetName] Memanggil Anggota Pakta untuk Berperang",
    "germany.85.d": "Pakta Anti-Soviet menetapkan bahwa seluruh penandatangan harus bergabung dalam setiap konflik pertahanan melawan Uni Soviet. [From.GetName] kini telah diserang oleh Soviet dan telah mengirimkan permintaan kepada seluruh anggota pakta untuk segera datang membantu. Kini saatnya menunjukkan dedikasi [Root.GetAdjective] untuk melindungi dunia dari ancaman Uni Soviet untuk selama-lamanya.",
    "germany.86.t": "Danzig atau Perang",
    "germany.86.d": "[GER.GetNameDefCap] telah lama mengumumkan tujuan mereka untuk merebut kembali wilayah yang hilang dalam Perang Besar. Secara khusus mereka mengincar wilayah Danzig, yang memisahkan Ostpreussen dari wilayah negara mereka lainnya.\\n\\nKini, mereka menuntut agar Danzig diserahkan kepada [GER.GetNameDef], dan sebagai imbalannya tidak menawarkan apa pun selain janji untuk membatalkan klaim mereka atas Poznań. Dengan bayang-bayang ancaman perang, menerima tawaran ini akan menunda kemungkinan konflik, tetapi dengan harga memberikan Jerman kekuatan lebih secara cuma-cuma demi apa pun yang ada di depan.",
    "germany.87.t": "Polandia Menyerahkan Danzig",
    "germany.87.d": "Dihadapkan pada ultimatum kita, Polandia telah sepakat untuk menyerahkan wilayah yang mereka peroleh secara tidak adil kepada kita, membuktikan bahwa mereka pasti tahu wilayah itu sah milik Jerman!",
    "germany.88.t": "Polandia Menolak Menyerahkan Danzig",
    "germany.88.d": "Terlepas dari upaya kita untuk membiarkan Polandia menyerahkan Danzig secara damai, bahkan berjanji melepaskan klaim kita atas wilayah Jerman lainnya sebagai gantinya, kita dihadapkan pada penolakan. Seperti yang sudah diduga, dunia tidak memberikan apa pun kepada kita selain apa yang kita rebut dengan kekerasan.",
    "germany.1002.t": "Menghormati Pakta Molotov-Ribbentrop?",
    "germany.1002.desc": "Jerman dan [SOU.GetNameDef] telah membuat kesepakatan untuk membagi Polandia menjadi bagian timur dan barat, namun pendudukan kita atas bagian timur telah menimbulkan komplikasi dalam pengaturan ini. Meskipun sekutu Jerman kita sepenuhnya berharap kita akan menyerahkan wilayah Polandia yang dijanjikan kepada [SOU.GetNameDef], kita malah bisa melanggar pakta tersebut dan melanjutkan pendudukan kita.",
    "germany.1003.t": "[From.GetNameDefCap] Melanggar Pakta!",
    "germany.1003.desc": "Terlepas dari keputusan untuk menyerahkan Polandia timur kepada [SOU.GetNameDef], sekutu kita di [From.GetNameDef] memilih untuk melanjutkan pendudukan mereka atas Polandia, secara resmi melanggar Pakta Molotov-Ribbentrop!",
    "germany.89.t": "Aliansi Durjana",
    "germany.89.d": "Setelah keberhasilan kerja sama kita baru-baru ini, pihak Jerman datang kepada kita dengan tawaran yang memikat. Mereka mengusulkan agar kita mengesampingkan perbedaan dan alih-alih menyia-nyiakan kekuatan kita untuk saling memerangi sementara negara-negara demokrasi barat menonton dan meraup untung, kita menggabungkan kekuatan dan menghancurkan mereka!",
    "germany.90.t": "Aliansi Ditolak",
    "germany.90.d": "Soviet telah menolak tawaran kita, jika kita menginginkan sumber daya [SOV.GetNameDef] kita harus merebutnya dengan kekerasan!",
    "germany.91.t": "Prancis Ingin Bergabung dengan Faksi Kita",
    "germany.91.d": "Para pemimpin kuat dari Mouvement Franciste telah membuat kemajuan besar dan menawarkan diri untuk bergabung dalam perjuangan kita. Bangsa Prancis siap berperang demi Reich.",
    "germany.92.t": "Jerman Menolak Ultimatum",
    "germany.92.d": "Terlepas dari penegasan kita bahwa remiliterisasi Rhineland akan dipandang sebagai tindakan perang, Jerman menolak untuk mundur dan bergerak maju ke zona demiliterisasi, mengabaikan peringatan kita. Ini berarti bahwa terlepas dari upaya terbaik kita untuk memelihara perdamaian, perang sekali lagi meletus di Eropa.",
    "germany.93.t": "Konferensi London",
    "germany.93.d": "Kita mengharapkan negara-negara besar Eropa duduk mengelilingi meja dan mencapai kesepakatan yang adil atas nama perdamaian. Sebaliknya, pihak Inggris dan Prancis memilih mendukung orang-orang Yugoslavia yang lancang beserta negara buatan mereka. Slovenia akan menjadi milik kita, dengan satu atau lain cara....",
    "germany.93.d_FRA_abandoned_yugoslavia": "Kita mengharapkan negara-negara besar Eropa duduk mengelilingi meja dan mencapai kesepakatan yang adil atas nama perdamaian. Meskipun Prancis melihat keadilan dari perkara kita, pihak Inggris yang bodoh telah memilih untuk mendukung orang-orang Yugoslavia yang lancang beserta negara buatan mereka. Slovenia akan menjadi milik kita, dengan satu atau lain cara....",
    "germany.94.t": "Penyerahan di London",
    "germany.94.d": "Dalam kemenangan lain atas keberanian dan tindakan nyata, Slovenia, yang akan segera dinamai kembali sebagai Karniola, telah dikembalikan ke rumah sahnya di dalam Reich Jerman.",
    "germany.95.t": "Pihak Yugoslavia Menolak",
    "germany.95.d": "Dengan rasa kepantasan yang keliru tentang tempat mereka di dunia, orang-orang Yugoslavia memilih untuk tidak menerima kesempatan yang telah kita tawarkan kepada mereka."
}

print(f"Loaded Part 2: {len(translations_part2)} entries")

translations_part3 = {
    "germany.96.t": "Konferensi London",
    "germany.96.d": "Orang-orang Yugoslavia, yang dihasut oleh pihak Italia yang bodoh, telah memutuskan untuk menentang kita. Orang-orang Italia yang tidak tahu berterima kasih akan binasa bersama pihak Yugoslavia. Jenderal Rommel meyakinkan kita bahwa mereka lari kocar-kacir pada waktu lalu, dan tak diragukan lagi mereka akan lari lagi.",
    "germany.97.t": "Konferensi London",
    "germany.97.d": "Konferensi London yang besar seharusnya membetulkan salah satu dari sekian banyak ketidakadilan yang telah ditimpakan kepada Jerman. Namun, pihak Prancis masih haus akan pembalasan dendam dan hanya ingin melihat Jerman berlutut. Mereka mendukung rezim di Beograd terlepas dari keadilan perjuangan kita. Apakah mereka sungguh mengira ancaman kosong mereka ada artinya bagi kita?",
    "germany.98.t": "Nasib Yugoslavia",
    "germany.98.d": "Kita selalu tahu bahwa negara Yugoslavia yang dibentuk dari pecahan Kekaisaran Habsburg adalah negara buatan yang ditakdirkan tidak akan bertahan lama. Kebencian etnis yang mendidih di bawah permukaan kini meluap dan negara tersebut hancur berantakan. Kita harus turun tangan untuk membenahi situasi ini.",
    "germany.99.t": "Membagi Yunani bersama [ITA.GetNameDef]",
    "germany.99.d": "Ketika kita menyarankan agar barangkali perbatasan Yunani harus disesuaikan kembali, duta besar Italia berkoar bahwa mereka akan membangun kembali Kekaisaran Romawi di atas puing-puing abu Yunani.",
    "germany.100.t": "Membagi Yunani bersama [BUL.GetNameDef]",
    "germany.100.d": "Wilayah yang dianggap milik Bulgaria diserahkan kepada Yunani setelah Perang Balkan Kedua dan Perang Besar. Jika kita membetulkan kesalahan ini, kita akan mengikat Bulgaria ke pihak kita. Namun, jika mereka tidak cukup kuat untuk merebutnya sendiri, apakah mereka sekutu yang layak bagi kita?",
    "germany.101.t": "Menuntut Wilayah Yunani",
    "germany.101.d": "Kurangnya sekutu yang cocok membuat Jerman berada dalam posisi strategis yang merugikan di Mediterania Timur. Namun, kita dapat memperbaikinya dengan menuntut pangkalan dan wilayah di sekitarnya dari Yunani demi mengamankannya.",
    "germany.102.t": "Yunani Menolak",
    "germany.102.d": "Yunani dengan bodohnya menolak bantuan kita dalam menyelesaikan sengketa perbatasan mereka.",
    "germany.103.t": "Yunani Menolak",
    "germany.103.d": "Yunani telah menolak tawaran perlindungan dan bantuan kita yang murah hati",
    "germany.104.t": "Italia Menuntut Wilayah Vichy",
    "germany.104.d_Savoy": "Pihak Italia mulai mengajukan tuntutan kepada Prancis Vichy dengan menunggangi kemenangan kita. Mereka menginginkan zona perbatasan Savoy demi memperkuat Italia. Namun, kitalah yang akan memutuskannya.",
    "germany.104.d_Corsica": "Pihak Italia menuntut Pulau Korsika dari Vichy sebagai bagian dari rampasan perang mereka. Apakah kita harus mengabulkannya?",
    "germany.104.d_Savoy_Corsica": "Italia menuntut agar Vichy menyerahkan Savoy dan Korsika. Hal ini akan menguntungkan Italia, tetapi ini akan merisaukan otoritas kolonial Prancis.",
    "germany.105.t": "Italia Meninggalkan [Root.GetFactionName]",
    "germany.105.d": "Menyusul keputusan kita untuk tidak memberikan wilayah mana pun kepada Italia, mereka memilih untuk meninggalkan [Root.GetFactionName] dengan dalih bahwa kita bukan sekutu yang cukup berharga bagi mereka.",
    "germany.106.t": "Perjanjian Craiova",
    "germany.106.d_second_vienna_accepted_north": "Dengan perolehan Transilvania Utara oleh Hongaria, Bulgaria mengingatkan kita akan sengketa perbatasan lama mereka dengan Rumania atas Dobruja Selatan, yang direbut oleh Rumania pada tahun 1913.",
    "germany.106.d_second_vienna_accepted_all": "Dengan perolehan Transilvania oleh Hongaria, Bulgaria mengingatkan kita akan sengketa perbatasan lama mereka dengan Rumania atas Dobruja Selatan, yang direbut oleh Rumania pada tahun 1913.",
    "germany.106.d_no_vienna": "Karena hubungan dengan Hongaria mendingin, di mana mereka memilih bergabung dalam aliansi lain, rencana awal kita untuk memberi mereka sebagian dari Transilvania tidak mungkin dilakukan. Sebagai gantinya, kita sebaiknya mendengarkan sengketa wilayah Bulgaria atas Dobruja Selatan, yang direbut oleh Rumania pada tahun 1913.",
    "germany.107.t": "Penerbangan Rudolf Hess",
    "germany.107.d": "Wakil Führer Rudolf Hess ditangkap oleh tentara Home Guard di Skotlandia kemarin setelah terjun payung dari pesawat tempur berat. Sebagai seorang pilot ulung, ia tampaknya terbang sendirian melintasi Laut Utara, berhati-hati agar tetap berada di luar jangkauan radar sebelum berbelok ke barat menuju Inggris.\\nHess tampaknya berinisiatif sendiri untuk merundingkan perjanjian damai antara Inggris dan Jerman, meskipun Berlin telah mengecamnya sebagai orang gila dan ia telah dicopot dari semua jabatan politiknya. Pihak berwenang Inggris belum dapat dimintai keterangan.",
    "germany.108.t": "Kematian Rudolf Hess",
    "germany.108.d": "Wakil Führer Rudolf Hess tewas kemarin ketika Angkatan Udara Kerajaan mencegat pesawat tempur berat yang ia terbangkan di lepas pantai Skotlandia. Hakikat sebenarnya dari misinya masih belum jelas — kendati Hess adalah seorang pilot berpengalaman, ia terbang sendirian dan pesawatnya tampaknya tidak dipersenjatai.\\nJasadnya ditemukan oleh pihak berwenang Inggris, tetapi pemakaman kenegaraan dengan peti kosong telah dijadwalkan di Berlin.\\n\\nHitler dilaporkan sangat terguncang atas kematian teman lamanya tersebut.",
    "germany.109.d": "Kapal udara Hindenburg, yang ditambatkan di Jerman sejak awal permusuhan, menemui akhir yang dramatis hari ini ketika meledak di atas Skotlandia. Pesawat itu tampaknya dikomandoi oleh Wakil Führer Rudolf Hess, yang berhasil menerbangkannya sendirian melintasi Laut Utara dalam misi pribadi untuk merundingkan perdamaian dengan Inggris.\\nStasiun radar Inggris tidak kesulitan mendeteksi pesawat raksasa tersebut, dan beberapa wing Angkatan Udara Kerajaan segera diarahkan menuju posisinya. Ketika Hindenburg gagal merespons melalui radio, mereka melepaskan tembakan.\\n\\nHess terjun payung dengan selamat, dan kini dipenjarakan di Menara London.",
    "germany.110.d": "Kapal udara Hindenburg, yang ditambatkan di Jerman sejak awal permusuhan, menemui akhir yang dramatis hari ini ketika meledak di atas Skotlandia. Pesawat itu tampaknya dikomandoi oleh Wakil Führer Rudolf Hess, yang berhasil menerbangkannya sendirian melintasi Laut Utara dalam misi pribadi untuk merundingkan perdamaian dengan Inggris.\\nStasiun radar Inggris tidak kesulitan mendeteksi pesawat raksasa tersebut, dan beberapa wing Angkatan Udara Kerajaan segera diarahkan ke posisinya. Ketika Hindenburg gagal merespons melalui radio, mereka melepaskan tembakan.\\n\\nJasad Hess ditemukan di antara puing-puing reruntuhan.",
    "germany.111.t": "Yugoslavia Menolak",
    "germany.111.d": "Yugoslavia dengan bodohnya menolak tawaran kita untuk meredakan ketegangan di kawasan tersebut.",
    "germany.113.t": "Jerman Secara Resmi Meminta Danzig",
    "germany.113.d": "Menganggap dukungan militer mereka sangat penting bagi keberhasilan apa pun di masa depan dalam perang saudara kita, [GER.GetNameDef] telah mengajukan rencana untuk menegakkan kendali [GER.GetAdjective] atas Danzig setelah pertempuran usai. Mereka juga menegaskan bahwa ketergantungan [Root.GetNameDef] pada dukungan militer mereka tidak memberi [Root.GetLeader] pilihan selain menandatangani 'Perjanjian Danzig' ini.",
    "germany.114.t": "Tuntutan Jerman atas Danzig",
    "germany.114.d": "Menyusul kemenangan kita dalam perang saudara [Root.GetAdjective], Jerman berulang kali mengingatkan kita akan permintaan mereka atas Danzig. Mereka juga mengingatkan kita akan akibat dari pembangkangan bagi suatu bangsa yang masih memulihkan diri dari konflik internal.",
    "germany.115.t": "Polandia Menyerahkan Danzig",
    "germany.115.d": "Sesuai dengan perjanjian Danzig, [GER.GetNameDef] telah menyetujui pemindahan Danzig ke bawah kendali [GER.GetNameDef].",
    "germany.116.t": "Polandia Mengingkari Perjanjian Danzig",
    "germany.116.d": "Mengabaikan dukungan tak ternilai yang kita berikan kepada mereka dalam perang saudara mereka, [From.GetName] telah memutuskan untuk mengabaikan klaim kita atas Danzig.",
    "germany.117.t": "Perjanjian Danzig",
    "germany.117.d": "[From.GetName] telah menyetujui permintaan kita atas Danzig sebagai imbalan atas dukungan dalam perang saudara mereka. Permintaan dan janji kita telah diresmikan dalam Perjanjian Danzig. Sekarang kita harus memastikan bahwa [From.GetName] keluar sebagai pemenang dari konflik mereka.",
    "germany.118.t": "Konferensi Yalta",
    "germany.118.d": "Dengan perang di Eropa yang berlangsung cepat, saatnya bagi pihak pemenang yang tak terelakkan untuk mempertimbangkan masa depan Eropa.\\n\\nKita dapat mengusulkan kepada [yalta_partner.GetNameDef] sebuah konferensi mengenai pembagian [GER.GetNameDef] setelah perang, untuk menggariskan lingkup pengaruh kita di benua itu.\\n\\n'Sekutu' kita di [yalta_partner.GetNameDef] telah mengindikasikan bahwa mereka tertarik dengan konferensi semacam itu. Tak diragukan lagi, mereka menginginkan semacam imbalan atas pengorbanan mereka.",
    "germany.119.t": "Konferensi Yalta",
    "germany.119.d": "Dengan perang melawan [GER.GetNameDef] yang kian mendekati akhir yang tak terelakkan, [yalta_origin.GetNameDef] telah menghubungi kita mengenai sebuah konferensi tentang masa depan Eropa.\\n\\nMereka mengusulkan pembagian [GER.GetNameDef] antara timur dan barat. Hal ini akan memungkinkan lingkup pengaruh kita meluas jauh ke dalam Eropa, yang akan menebus sebagian dari kerugian yang kita derita dalam perjuangan yang mengerikan ini.",
    "germany.1190.t": "Konferensi Toronto",
    "germany.1190.desc": "Dengan perang melawan [GER.GetNameDef] yang bergerak menuju akhir yang tak terelakkan, [yalta_origin.GetNameDef] telah mendekati kita mengenai sebuah konferensi tentang masa depan Eropa.\\n\\nMereka mengusulkan pembagian tiga arah atas [GER.GetNameDef] di mana kita akan mendapatkan pengaruh terbatas atas kawasan Timur. Kawasan industri utama akan berada di bawah kendali sekutu, dan pihak sekutu juga akan memiliki kendali terbatas atas wilayah Selatan. Hal ini akan mengurangi kekuatan Jerman, namun pengaruh kita atas Eropa tengah akan tetap tidak menentu.",
    "germany.120.t": "[yalta_partner.GetNameDefCap] Menolak untuk Berpartisipasi",
    "germany.120.d": "Usulan konferensi kita mengenai masa depan Eropa telah kandas.\\n\\nBerbicara tanpa ragu-ragu, [yalta_partner.GetLeader] menolak segala kebutuhan akan perencanaan dan kerja sama di Eropa pascaperang.\\n\\n'Kita akan bertemu saat saya mengajukan tuntutan saya terhadap [GER.GetNameDef] di meja perundingan damai. Saya tidak akan membiarkan manuver politik picik merintangi jalan [yalta_partner.GetNameDef].'",
    "germany.121.t": "Pembagian Jerman",
    "germany.121.d": "Sebagaimana ditetapkan dalam perjanjian Yalta, Jerman akan dibagi menjadi dua negara terpisah, masing-masing berada di bawah lingkup pengaruh salah satu pihak yang berperang.\\n\\nSemoga ini membawa akhir bagi konflik di Eropa.",
    "germany.122.t": "[From.GetNameDefCap] Menuntut Sudetenland",
    "germany.122.d": "Di tengah situasi yang terus berkembang, Jerman telah menuntut wilayah Sudetenland dari kita, demi 'melindungi populasi Jerman' di wilayah tersebut.\\n\\nDengan situasi saat ini, mereka telah menegaskan bahwa ini adalah batas akhir. Tidak akan ada perundingan atau diplomasi. Mereka akan merebut Sudetenland, atau mereka akan berperang demi itu.",
    "germany.122.desc_cze_subject_of_ger": "Pemimpin [FROM.GetAdjective], [FROM.GetLeader], telah menuntut wilayah Sudetenland dari kita, demi 'melindungi populasi Jerman' di wilayah tersebut.\\n\\nMengingat keadaan, dan ketatnya kendali yang diberlakukan [FROM.GetNameDef] atas negara kita, tidak ada yang dapat kita lakukan untuk menghentikan mereka. Mereka akan menguasai Sudetenland, dan kita harus berdamai dengan kenyataan pahit ini.",
    "germany.123.t": "[From.GetNameDefCap] Menolak Menyerahkan Sudetenland kepada Kita",
    "germany.123.d": "Dalam langkah diplomatik yang bodoh, [From.GetLeader], pemimpin [From.GetAdjective] telah menolak semua tuntutan [ROOT.GetAdjective]!\\n\\nMereka tidak akan menyerahkan Sudetenland, dan secara terang-terangan menantang kita untuk menyatakan perang, mencemooh keinginan kita untuk melindungi saudara-saudari [ROOT.GetAdjective] kita.",
    "germany.124.t": "[From.GetNameDefCap] Menyerahkan Sudetenland",
    "germany.124.d": "Menghadapi prospek perang dengan kita, [From.GetNameDef] telah setuju untuk menyerahkan seluruh kendali atas Sudetenland, dan melepaskan klaim apa pun di masa depan atas wilayah tersebut.\\n\\nPopulasi [ROOT.GetAdjective] di Sudetenland akhirnya akan aman berada di dalam naungan [ROOT.GetNameDef].",
    "germany.124.desc_cze_subject_of_ger": "Pemerintah [From.GetAdjective] tidak punya pilihan selain setuju untuk menyerahkan seluruh kendali atas Sudetenland, melepaskan klaim apa pun di masa depan atas kawasan tersebut.\\n\\nPopulasi [ROOT.GetAdjective] di Sudetenland akhirnya akan aman berada di dalam naungan [ROOT.GetNameDef]."
}

print(f"Loaded Part 3: {len(translations_part3)} entries")

translations_part4 = {
    "germany.125.t": "[FROM.GetNameDefCap] Menyerahkan Sudetenland kepada [GER.GetNameDef]",
    "germany.125.d": "Tuan [FROM.GetAdjective] kita telah memutuskan untuk menyerahkan Sudetenland kepada [GER.GetNameDef]. Mereka mengklaim bahwa tindakan tersebut diambil sebagai langkah demi menjaga perdamaian di kawasan dan bahwa tindakan lain akan menyebabkan nasib yang jauh lebih buruk menimpa kita. Kita tidak diajak berkonsultasi mengenai hal ini dan sekarang hanya bisa menyaksikan ketika wilayah sah kita direnggut dari kita.",
    "germany.126.t": "Anschluss atau Kehancuran",
    "germany.126.d": "Kerusuhan sipil dan aksi kekerasan telah merebak saat para pengunjuk rasa menyuarakan keinginan agar Austria bergabung dengan Jerman. Pergolakan internal yang telah diderita bangsa kita semakin menambah gaung suara rakyat yang menginginkan persatuan dengan Jerman. Berlin mendesak kuat demi terwujudnya Anschluss dan ini bisa jadi merupakan satu-satunya kesempatan kita untuk menjaga sebagian nilai-nilai sejati Austria tetap hidup.",
    "germany.127.t": "Meresmikan Aliansi",
    "germany.127.d": "Bersatu dalam pertempuran kita melawan [SOV.GetNameDef], barangkali saatnya telah tiba untuk meresmikan aliansi dan mengundang mitra baru kita dalam perang anti-komunis ini ke faksi kita.",
    "germany.128.t": "Pakta Anti-Soviet",
    "germany.128.d": "[From.GetNameDefCap] telah menawarkan diri untuk menyambut kita ke faksi mereka, sehingga kita dapat berkoordinasi lebih baik melawan ancaman komunis. Utusan untuk meresmikan aliansi ini telah tiba di ibu kota.",
    "germany.200.t": "Jerman yang Baru",
    "germany.200.desc": "Jerman tidak lagi menimbulkan ancaman seperti dahulu, sebaliknya [SOV.GetNameDef]-lah yang mengancam akan merusak tatanan dunia. Jerman yang kuat dan demokratis bisa menjadi sekutu yang sangat berguna dalam perjuangan ini. Mengizinkan Jerman bangkit kembali juga dapat memberikan keuntungan perdagangan yang kuat bagi kita dan mereka. Mungkin saatnya tepat untuk mengakhiri pendudukan dan meletakkan dasar bagi dunia demokratis yang kuat dan bersatu.",
    "germany.201.t": "[FROM.GetName] Ingin Menyatukan Kembali Jerman",
    "germany.201.desc": "[FROM.GetName] telah memutuskan untuk mengakhiri pendudukan mereka atas Jerman, dan memberi bangsa Jerman pemerintahan sendiri sebagai sebuah republik baru bernama [WGR.GetNameDef]. Mereka mengklaim hal ini demi menciptakan benteng pertahanan melawan komunisme, berargumen bahwa Jerman yang demokratis dan kuat adalah perlindungan yang lebih baik terhadap penyebaran komunisme daripada negara yang lemah dan terpecah-belah.\\nKita telah diminta untuk mendukung langkah ini dengan menggabungkan wilayah Jerman kita dengan [WGR.GetName] yang baru dibentuk. Dukungan rakyat untuk hal ini sangat kuat.",
    "germany.202.t": "Jerman yang Baru",
    "germany.202.desc": "[FROM.GetName] membiarkan wilayah Jerman mereka digabungkan ke dalam apa yang disebut sebagai [WGR.GetName]. Hal ini memicu banyak orang di zona Jerman kita menyerukan penyatuan kembali dengan Jerman yang merdeka juga.",
    "germany.999.t": "Kisah Dua Kota",
    "germany.999.desc": "Menyusul kemenangan gemilang pasukan Jerman, waktunya telah tiba untuk melenyapkan sisa-sisa terakhir kekuasaan Bolsyevik di Eropa. Bahkan hingga saat ini, nama Stalin dan Lenin menodai dua kota besar di Lebensraum Jerman yang baru, menghina prajurit yang mengorbankan nyawa demi merebutnya.\\n\\n'Asosiasi Veteran Perang Dunia' telah menyampaikan saran kepada pemerintah untuk memperbaiki keadaan yang mengerikan ini.",
    "germany.1041.t": "[FROM.GetNameDefCap] Menuntut Sudetenland",
    "germany.1041.desc": "Meskipun terjadi pergolakan perbatasan Ceko baru-baru ini, kebijakan luar negeri [FROM.GetAdjective] tetap teguh. Diplomat [FROM.GetAdjective] telah mengajukan ultimatum kepada kita — serahkan Sudetenland, atau perang akan diumumkan.",
    "germany.1041.desc_ally_or_subject": "Terlepas dari pergolakan perbatasan Ceko baru-baru ini, kebijakan luar negeri [FROM.GetAdjective] tidak berubah. Diplomat [FROM.GetAdjective] telah mengajukan tuntutan wilayah mereka kepada kita, mengharapkan kita menyerahkan Sudetenland tanpa penundaan.",
    "germany.1042.t": "[FROM.GetNameDefCap] Tunduk",
    "germany.1042.desc_default": "Keperkasaan [ROOT.GetAdjective] tiada tandingannya — wilayah Sudetenland yang sebelumnya berada di bawah lingkup pengaruh [FROM.GetAdjective] kini telah diserahkan kepada kita. [FROM.GetNameDefCap] tetap luput dari sasaran kita. Untuk saat ini.",
    "germany.1042.desc_ally": "Keperkasaan [ROOT.GetAdjective] tiada tandingannya — wilayah Sudetenland yang sebelumnya berada di bawah lingkup pengaruh [FROM.GetAdjective] kini telah diserahkan kepada kita. Tak butuh waktu lama bagi [FROM.GetLeader] dan diplomat [FROM.GetAdjective] untuk menyadari bahwa ini adalah yang terbaik bagi [ROOT.GetFactionName].",
    "germany.1042.desc_subject": "Keperkasaan [ROOT.GetAdjective] tiada batasnya — wilayah Sudetenland yang sebelumnya di bawah kendali [FROM.GetAdjective] kini telah dialihkan kepada kita. Penguasa boneka kita di [FROM.GetNameDef], [FROM.GetLeader], memastikan bahwa otoritas setempat dan organisasi [FROM.GetAdjective] mematuhi perjanjian tanpa keberatan.",
    "germany.1043.t": "[FROM.GetNameDefCap] Menolak Tuntutan",
    "germany.1043.desc": "Terlepas dari ketimpangan kekuatan, diplomat [FROM.GetAdjective] telah menolak tuntutan kita untuk penyerahan Sudetenland. Sudah dapat dipastikan bahwa perang akan menyusul.",
    "germany.1043.desc_ally": "Meskipun demi kepentingan terbaik seluruh anggota [ROOT.GetFactionName], diplomat [FROM.GetAdjective] telah menolak tuntutan kita atas penyerahan Sudetenland. Tidak banyak yang dapat dilakukan sekarang, mengingat perlunya menghormati otonomi sekutu kita.",
    "germany.1050.t": "Kematian Sang Führer",
    "germany.1050.desc": "Sang Führer, $GER_adolf_hitler$, telah ditemukan tewas di dalam bunkernya. Dengan pasukan musuh yang kian mendekat, tampaknya sang Führer memutuskan untuk mengakhiri hidupnya sendiri alih-alih menghadapi risiko ditawan. Demi mencegah demoralisasi pasukan, corong propaganda kita diinstruksikan menyebarkan kabar bahwa Hitler gugur secara heroik bertempur hingga napas terakhir menghadapi kekuatan musuh yang luar biasa besar. Namun, masalah kita yang lebih mendesak adalah siapa yang akan maju menggantikan sang Führer?",
    "AAT_germany.1.t": "[FROM.GetNameDefCap] Meminta Hak Sumber Daya",
    "AAT_germany.2.t": "[FROM.GetName] Menolak Kesepakatan Kita",
    "AAT_germany.2.desc": "[FROM.GetName] telah menolak tawaran kita, menyatakan bahwa saat ini kesepakatan tersebut bukan demi kepentingan terbaik mereka.\\nMereka menegaskan bahwa tidak ada niat buruk terhadap kita, melainkan mereka memiliki prioritas lain saat ini.",
    "AAT_germany.3.t": "[FROM.GetName] Menerima Kesepakatan Kita",
    "AAT_germany.3.desc": "[FROM.GetName] telah menerima kesepakatan kita, sesuatu yang pasti akan menguntungkan kedua belah pihak. Semoga pengaturan yang menguntungkan ini disusul oleh lebih banyak kerja sama lainnya.",
    "AAT_germany.1.desc": "[FROM.GetNameDefCap] telah mendekati kita dengan kesepakatan yang mereka klaim akan menguntungkan kedua perekonomian. Mereka membutuhkan sumber daya alam kita untuk industri mereka dan kita membutuhkan investasi mereka untuk memperluas industri kita. Tawaran yang menggiurkan, tapi apakah ini perjanjian terlarang yang menjebak?",
    "AAT_germany.10.desc": "Dengan pendudukan [144.GetName] baru-baru ini oleh [FROM.GetNameDef] dan antek-anteknya, [GER.GetLeader] telah meningkatkan tekanannya pada kita untuk memperdagangkan lebih banyak sumber daya dengan mereka guna menyalakan mesin perang mereka. Kesepakatan yang ditawarkan tidak sepenuhnya sepihak, dan menolaknya bisa membuat kita terseret ke dalam kancah peperangan..."
}

print(f"Loaded Part 4: {len(translations_part4)} entries")

# Merge all parts
all_translations = {}
all_translations.update(translations_part1)
all_translations.update(translations_part2)
all_translations.update(translations_part3)
all_translations.update(translations_part4)

print(f"Total merged translations: {len(all_translations)}")

# Validation with source
with open('scripts/batch_3_source.json', 'r', encoding='utf-8') as f:
    source_items = json.load(f)

source_keys = [it['key'] for it in source_items]
source_keys_set = set(source_keys)
trans_keys_set = set(all_translations.keys())

missing_keys = source_keys_set - trans_keys_set
extra_keys = trans_keys_set - source_keys_set

if missing_keys:
    print(f"ERROR: Missing {len(missing_keys)} keys: {missing_keys}")
if extra_keys:
    print(f"ERROR: Extra {len(extra_keys)} keys: {extra_keys}")

if not missing_keys and not extra_keys:
    print("SUCCESS: Exact 1-to-1 key match with source (242 entries)!")
    
    # Check variables/placeholders
    tag_regex = re.compile(r'\[[A-Za-z0-9_\.]+\]|\$[A-Za-z0-9_]+\$|§[A-Za-z!§]')
    tag_errors = 0
    for it in source_items:
        k = it['key']
        en_text = it['en']
        id_text = all_translations[k]
        
        en_tags = sorted(tag_regex.findall(en_text))
        id_tags = sorted(tag_regex.findall(id_text))
        if en_tags != id_tags:
            print(f"Tag mismatch in {k}:\n  EN: {en_tags}\n  ID: {id_tags}")
            tag_errors += 1
            
    print(f"Tag checking completed with {tag_errors} errors.")
    
    # Save output
    out_path = 'scripts/batch_3_translated.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(all_translations, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved to {out_path}")
