# -*- coding: utf-8 -*-
import json

chunk7_translations = {
    # 875 - 880: wtt_news.45
    "wtt_news.45.t": "[new_leader.GetLeader] Mengambil Alih Kepemimpinan Nasional di Tiongkok",
    "wtt_news.45.desc": "Menyusul Perebutan Kekuasaan yang berkepanjangan antara [old_leader.GetLeader] dan [new_leader.GetLeader], pihak pertama akhirnya mengakui kekalahan dan bertemu dengan [new_leader.GetLeader] di kediamannya. Hanya setelah dua jam perundingan, [old_leader.GetLeader] dilaporkan menerima usulan pengalihan kekuasaan kepada [new_leader.GetLeader] dan mengundurkan diri sebagai Perdana Menteri Republik.\\n\\nKelompok pendukung dari kedua kubu sebelumnya telah berkumpul di luar gedung, memicu kekhawatiran akan bentrokan berdarah tergantung hasil perundingan.\\n\\nKendati demikian, tidak ada laporan kekerasan dan proses transisi kekuasaan tampaknya berlangsung cukup mulus.",
    "wtt_news.45.a": "Politik. Politik tidak pernah berubah.",
    "wtt_news.45.b": "Keberhasilan yang menakjubkan.",
    "wtt_news.45.c": "Lebih baik daripada pertumpahan darah.",
    "wtt_news.45.d": "Mereka mungkin baru saja mencegah terjadinya Perang Saudara.",

    # 881 - 884: wtt_news.46
    "wtt_news.46.t": "[From.GetLeader] Memproklamasikan Kebijakan Satu Tiongkok",
    "wtt_news.46.desc": "Berbicara di hadapan para pendukungnya, [From.GetLeader] hari ini mengumumkan pergeseran besar dalam pemerintahannya. Sebelumnya, [From.GetLeader] bersedia menoleransi kenyataan bahwa beberapa wilayah Tiongkok hampir sepenuhnya merdeka. Hal itu kini telah berakhir. Mulai hari ini, [From.GetNameDef] menganggap seluruh daratan Tiongkok sebagai tanggung jawab mereka sebagai satu-satunya pemerintah Tiongkok yang sah. Siapa pun yang menolak perintah dari pemerintah yang sah ini akan dianggap sebagai pemberontak atau pengkhianat, dan akan ditindak tegas.\\n\\nKendati demikian, masih harus dibuktikan apakah Pemerintah [From.GetLeader] sanggup mewujudkan ancaman ini atau ini sekadar manuver propaganda demi mendulang dukungan rakyat.",
    "wtt_news.46.a": "Sebuah ancaman langsung.",
    "wtt_news.46.b": "Kita akan menyatukan seluruh Tiongkok!",
    "wtt_news.46.d": "Orang-orang yang lebih hebat pun telah gagal.",

    # 885 - 891: wtt_news.47
    "wtt_news.47.t": "Tiongkok Menuntut Wilayah Konsesi Asing",
    "wtt_news.47.desc": "Menyusul pidato berapi-api oleh [From.GetLeader], perwakilan diplomatik [From.GetNameDef] telah menyampaikan nota kepada semua kekuatan asing yang memiliki konsesi atau wilayah sewaan di Tiongkok. Dalam nota tersebut, pemerintah [From.GetLeader] menuntut agar semua wilayah Tiongkok dikembalikan secepatnya ke pangkuan [From.GetNameDef].\\n\\nIni dilihat sebagai langkah pertama dari rencana besar untuk mengusir pengaruh asing dan membatalkan 'Perjanjian-Perjanjian Tidak Adil' abad sebelumnya.",
    "wtt_news.47.a": "Seseorang harus berani memulainya.",
    "wtt_news.47.b": "Datang dan rebutlah jika mampu!",
    "wtt_news.47.c": "Tentu saja tidak akan ada hal buruk yang terjadi dari ini.",
    "wtt_news.47.d": "Jangan memaksa kami turun tangan ke sana!",

    # 892 - 897: wtt_news.48
    "wtt_news.48.t": "Perang Kemerdekaan Manchuria",
    "wtt_news.48.desc": "Menyusul perebutan kekuasaan internal antara para administrator Jepang dan pemerintah [MAN.GetLeader], pertarungan demi supremasi di Manchuria akhirnya mencapai titik didih.\\n\\nKabarnya, konfrontasi dipicu oleh sebuah insiden di Lingkungan Kekaisaran, di mana seorang Jenderal Jepang diduga menghina Kaisar Manchukuo dengan menuntut agar beliau membungkuk hormat.\\n\\nDengan murka, [MAN.GetLeader] menjawab bahwa \"Putra Langit tidak pernah membungkuk\" lalu memukul jenderal tersebut dengan tongkatnya, sebelum memerintahkan pasukannya untuk segera mengusir seluruh tentara Jepang dari tanah Tiongkok.",
    "wtt_news.48.a": "Anak anjing mulai mengaum?",
    "wtt_news.48.b": "Kita akan merebut takdir kita!",
    "wtt_news.48.c": "Dasar pengkhianat kecil!",
    "wtt_news.48.d": "Sang Naga menyerang... Matahari?",

    # 898 - 903: wtt_news.50
    "wtt_news.50.t": "Hitler Dibunuh",
    "wtt_news.50.desc": "Radio Jerman hari ini mengumumkan bahwa elemen-elemen pengkhianat di tubuh militer telah mencoba melancarkan kudeta. Menyusul ledakan di Markas Besar Führer yang menewaskan Hitler dan melukai beberapa orang lainnya, unit-unit tentara menyerang sejumlah kantor dan unit SS.\\n\\nMeskipun [GER.GetLeader] mengklaim memegang kendali penuh atas negara dan militernya, laporan mengenai baku tembak antara pasukan loyalis dan pemberontak masih terus berdatangan dari seantero negeri.\\n\\nRumor menyebutkan bahwa anggota terkemuka lain dari partai Nazi tengah merencanakan perebutan kekuasaan mereka sendiri di tengah kekacauan ini.",
    "wtt_news.50.a": "Pengkhianatan yang keji!",
    "wtt_news.50.b": "Situasinya sama sekali tidak membaik.",
    "wtt_news.50.c": "Baguslah dia sudah tiada!",
    "wtt_news.50.d": "Ia telah menekan mereka terlalu jauh.",

    # 904 - 906: wtt_news.51
    "wtt_news.51.t": "Percobaan Pembunuhan terhadap [GER.GetLeader]",
    "wtt_news.51.desc": "Radio Jerman mengumumkan hari ini bahwa elemen-elemen pembangkang di tubuh militer telah mencoba melancarkan kudeta. Menyusul ledakan di Markas Besar Führer yang secara ajaib hanya melukai ringan Hitler dan beberapa perwira lainnya, unit-unit angkatan darat sempat berupaya merebut kendali beberapa gedung pemerintahan di Berlin.\\n\\nKabar selamatnya [GER.GetLeader] menyebar cepat, dan sebagian besar unit di bawah komando para pemberontak telah kembali ke barak masing-masing.\\n\\nSejumlah perwira tinggi Jerman memilih bunuh diri menyusul kegagalan tersebut daripada harus menanggung aib diadili di hadapan \"Pengadilan Rakyat\" yang terkenal kejam.",
    "wtt_news.51.c": "Awal dari akhir?",

    # 907: wtt_news.52
    "wtt_news.52.desc": "Radio Jerman mengumumkan hari ini bahwa [GER.GetLeader] telah mengambil alih tampuk pemerintahan. Menyusul baku tembak di dalam Führerbunker, di mana sang Führer terluka parah dan meregang nyawa, unit-unit SS bergerak cepat menguasai semua jalan raya utama dan persimpangan kereta api yang keluar dari Berlin. Sementara itu, unit-unit Luftwaffe dan Heer dilaporkan telah diperintahkan untuk merapat ke Berlin demi memulihkan ketertiban.",

    # 908 - 912: wtt_news.53 Scandinavia
    "wtt_news.53.t": "Penyatuan Skandinavia",
    "wtt_news.53.desc": "Melalui kekuatan senjata, [From.GetOldName] telah menyatukan bangsa-bangsa Skandinavia di bawah kekuasaannya, dan pemerintahannya kini tengah mengintegrasikan wilayah-wilayah yang baru ditaklukkan. Dalam upaya menggalang dukungan rakyat di belakang negara, propaganda pan-nasionalis dengan dukungan terang-terangan dari pemerintah kian digencarkan.\\n\\nSebagai akibatnya, para pendukung unifikasi Skandinavia mulai mengutip analogi historis, menunjukkan bahwa keadaan saat ini hanyalah kelanjutan alami dari upaya-upaya terdahulu untuk menyatukan kawasan tersebut. Pemerintah [From.GetOldAdjective] dengan antusias menyambut jalan pikiran ini, dan kini secara resmi memproklamasikan 'pemulihan Uni Kalmar', seraya mengganti nama negara menjadi '[From.GetNameDef]'.",
    "wtt_news.53.a": "Hari yang gemilang bagi seluruh rakyat Skandinavia!",
    "wtt_news.53.b": "Skandinavia lebih perkasa saat bersatu.",
    "wtt_news.53.c": "Itu tidak akan bertahan lama!",

    # 913 - 916: wtt_news.54 Nordics
    "wtt_news.54.t": "Penyatuan Kawasan Nordik",
    "wtt_news.54.desc": "Dengan ditaklukkannya seluruh bangsa di kawasan Nordik, pemerintah [From.GetOldAdjective] kini mulai mengambil langkah-langkah menuju integrasi wilayah-wilayah yang baru direbut. Akibatnya, dalam upaya menyatukan rakyat di belakang negara, terjadi lonjakan propaganda pan-nasionalis dengan dukungan resmi pemerintah.\\n\\nSeorang pejabat [From.GetOldAdjective] dikutip menyatakan bahwa \"Negara-negara Nordik selalu merasakan pertalian persaudaraan yang erat satu sama lain. Sangat alami bila kita bersatu, dan bangsa kita hidup berdampingan sebagai satu kesatuan.\" Tampaknya pemerintah bertekad memanfaatkan rasa persaudaraan ini sebagai cara mempersatukan rakyat, dan kini telah memproklamasikan \"persatuan sejati Nordik\", mengubah nama negara menjadi '[From.GetNameDef]'.",
    "wtt_news.54.a": "Kawasan Utara yang bersatu akan berdiri kokoh!",
    "wtt_news.54.b": "Kawasan Utara bisa jadi menimbulkan masalah bagi para tetangganya...",

    # 917 - 920: wtt_news.55 Gran Colombia
    "wtt_news.55.t": "Kelahiran Kembali [From.GetNameDef]",
    "wtt_news.55.desc": "Setelah merebut kembali seluruh tanah milik Gran Colombia masa lalu, pemerintah [From.GetOldAdjective] kini mulai melancarkan langkah integrasi terhadap wilayah-wilayah yang baru dikuasai. Akibatnya, demi menyatukan rakyat di belakang panji negara, propaganda pan-nasionalis yang didukung pemerintah meningkat drastis.\\n\\nPara pejabat [From.GetOldAdjective] berulang kali menegaskan keyakinan mereka bahwa seluruh Amerika Selatan bagian utara harus menengok sejarah bersama mereka dan memanfaatkan pertalian itu sebagai fondasi negara yang bersatu. Kini, pemerintah [From.GetOldAdjective] melangkah lebih jauh dan memproklamasikan \"kebangkitan kembali warisan Bolívar\", mengganti nama negara menjadi '[From.GetNameDef]'.",
    "wtt_news.55.a": "Impian Amerika Latin yang bersatu telah menanti!",
    "wtt_news.55.b": "Kelahiran kekuatan adidaya baru di benua Amerika?",

    # 921 - 924: wtt_news.56 Austria-Hungary
    "wtt_news.56.t": "Kelahiran Kembali [From.GetNameDef]",
    "wtt_news.56.desc": "Setelah mengamankan kembali seluruh tanah Kekaisaran Austria-Hongaria, pemerintah [From.GetOldAdjective], sebagai wakil dari negara penerus terakhir yang tersisa, kini mulai mengintegrasikan kembali wilayah-wilayah ini. Propaganda yang diarahkan pemerintah berkobar, memuji-muji \"masa kejayaan Kekaisaran\" dalam upaya nyata merangkul rakyat di balik reformasi nasional menyeluruh dan pemulihan tatanan kekaisaran.\\n\\nSebagai bagian dari langkah ini, pemerintah [From.GetOldAdjective] mengumumkan pemulihan [From.GetNameDef], dan mengubah nama resmi negara demi mencerminkan hal tersebut.",
    "wtt_news.56.a": "Indivisibiliter ac inseparabiliter!",
    "wtt_news.56.b": "Monarki Ganda bangkit kembali.",

    # 925 - 928: wtt_news.57 Polish-Lithuanian Commonwealth
    "wtt_news.57.t": "Kelahiran Kembali [From.GetNameDefCap]",
    "wtt_news.57.desc": "Saat Polandia dan Lituania sekali lagi diperintah oleh satu negara, pemerintah [From.GetOldAdjective] mulai memanfaatkan narasi sejarah untuk propagandanya demi menyatukan rakyat di belakang kebijakannya. 'Pakar sejarah' membombardir masyarakat dengan berbagai pemaparan bagaimana persatuan Polandia dan Lituania mampu menghadapi ancaman di perbatasan mereka, mengisahkan kembali masa keemasan Persemakmuran Polandia-Lituania. Pendekatan ini tampaknya membuahkan hasil dalam mengalihkan kemarahan rakyat dan memusatkan pikiran mereka pada kejayaan masa silam.\\n\\nHari ini, pemerintah [From.GetOldAdjective] mengambil langkah lebih jauh dan memproklamasikan pemulihan Persemakmuran, mengganti nama negara menjadi '[From.GetNameDef]'.",
    "wtt_news.57.a": "Jika Tuhan bersama kita, siapakah lawan kita?",
    "wtt_news.57.b": "Apakah ia akan selamat dari pemisahan kali ini?",

    # 929 - 944: wtt_news.58-61 Low Countries, Ottoman, etc.
    "wtt_news.58.t": "Reunifikasi Negeri-Negeri Rendah",
    "wtt_news.58.desc": "Dengan penaklukan seluruh Negeri-Negeri Rendah oleh [From.GetOldNameDef], pemerintah [From.GetOldAdjective] telah mulai mengonsolidasikan wilayah-wilayah barunya. Untuk memperkuat kekuasaannya, pemerintah telah memanfaatkan identitas bersama dan ikatan sejarah di antara masyarakat Negeri-Negeri Rendah.\\n\\nMenyusul kampanye propaganda terpadu yang memuji kejayaan masa lalu Tujuh Belas Provinsi dan Kerajaan Bersatu Belanda, pemerintah mengumumkan bahwa nama resmi negara telah diubah menjadi '[From.GetNameDef]'.",
    "wtt_news.58.a": "Persatuan membawa kekuatan!",
    "wtt_news.58.b": "Sebuah kekuatan baru bangkit di Negeri-Negeri Rendah.",
    "wtt_news.59.t": "Kelahiran Kembali [From.GetNameDef]",
    "wtt_news.59.desc": "Dengan mengamankan kembali kendali atas sebagian besar bekas wilayah kekuasaan mereka, kebangkitan [From.GetOldNameDef] telah memicu gelombang kebanggaan nasional. Merujuk pada masa keemasan penaklukan dan kejayaan kekaisaran, para propagandis telah membangkitkan ingatan tentang masa lalu kekaisaran demi melegitimasi ekspansi mereka.\\n\\nHari ini, di hadapan sorak-sorai massa, pemerintah secara resmi mengumumkan pembentukan kembali '[From.GetNameDef]'.",
    "wtt_news.59.a": "Kejayaan masa lalu telah kembali!",
    "wtt_news.59.b": "Kekaisaran bangkit dari abunya.",
    "wtt_news.60.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.60.desc": "Keberhasilan militer [From.GetOldNameDef] telah mengantarkan penyatuan wilayah-wilayah yang telah lama terpecah. Mengikuti seruan persatuan kebangsaan dan merujuk pada ikatan kebudayaan bersama, pemerintah mengumumkan penyatuan resmi seluruh wilayah ini di bawah naungan '[From.GetNameDef]'.",
    "wtt_news.60.a": "Bangsa kita akhirnya bersatu!",
    "wtt_news.60.b": "Peta politik telah berubah selamanya.",
    "wtt_news.61.t": "Pemulihan [From.GetNameDef]",
    "wtt_news.61.desc": "Setelah perjuangan panjang dan pertempuran sengit merebut kembali tanah air leluhur mereka, para pemimpin [From.GetOldNameDef] telah mengumumkan pemulihan penuh kedaulatan negara historis mereka. Pengumuman ini disambut dengan perayaan besar di seluruh negeri, seraya meresmikan kembalinya '[From.GetNameDef]'.",
    "wtt_news.61.a": "Akhirnya kita membatalkan pembagian wilayah masa lalu!",
    "wtt_news.61.b": "Negara Abadi telah bangkit kembali...",

    # 945 - 948: wtt_news.62 Europe
    "wtt_news.62.t": "Penyatuan Eropa",
    "wtt_news.62.desc": "Kekuatan-kekuatan utama benua Eropa kini terbentang takluk di hadapan [From.GetOldNameDef], dan untuk pertama kalinya impian lama tentang Eropa yang bersatu tampak dapat dicapai. Berbagai 'pakar', yang diduga didanai pemerintah, mulai berulang kali menyatakan situasi politik saat ini sebagai satu-satunya cara demi \"mencegah konflik Eropa di masa depan\".\\n\\nDalam upaya lanjutan untuk menampilkan citra \"bangsa bagi seluruh bangsa Eropa\", reformasi pemerintah di tingkat nasional dan daerah digulirkan dengan laju yang mengagumkan. Sebagai bagian dari langkah itu, diumumkan hari ini bahwa negara tersebut selanjutnya akan dikenal sebagai '[From.GetNameDef]', agar \"semua orang Eropa merasa diterima di dalamnya\".",
    "wtt_news.62.a": "Apakah ini akhir dari segala perang di Eropa?",
    "wtt_news.62.b": "Mari kita lihat apakah mereka sanggup mewujudkannya.",

    # 949 - 952: wtt_news.63 Zimbabwe / Mutapa
    "wtt_news.63.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.63.desc": "Seiring ekspansi bangsa [From.GetOldAdjective] ke wilayah para tetangganya, upaya pemerintah membangun kontinuitas historis menjadi semakin nyata, jelas dalam rangka mempersatukan rakyat. Pencapaian Kekaisaran Zimbabwe Raya telah sangat diromantisasi, dan propaganda bertubi-tubi tampak mulai memengaruhi opini publik.\\n\\nHari ini, pemerintah [From.GetOldAdjective] melangkah lebih jauh dan mengubah nama negara menjadi '[From.GetNameDef]', pengumuman yang disambut sorak-sorai riuh massa di jalan-jalan kota-kota besar.",
    "wtt_news.63.a": "Afrika untuk bangsa Afrika!",
    "wtt_news.63.b": "Apakah ini akhir dari imperialisme kolonial di Afrika?",

    # 953 - 956: wtt_news.64 Roman Empire
    "wtt_news.64.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.64.desc": "Kemajuan militer [From.GetOldAdjective] tampaknya sama sekali tak terbendung, dan gagasan yang sempat dicemooh banyak pihak dalam beberapa tahun terakhir — pembentukan Kekaisaran Romawi baru — kini berada tepat dalam genggaman bangsa Italia. Sebagian besar kekuatan Eropa kontinental yang dapat menentang mereka praktis telah disingkirkan, memberi kebebasan penuh bagi Italia untuk memaksakan kehendak mereka atas bangsa-bangsa taklukan.\\n\\nSelain memulai integrasi atas apa yang mereka sebut sebagai \"Wilayah Romawi yang Direbut Kembali\", pemerintah Italia kini telah mengumumkan kelahiran kembali Kekaisaran Romawi, mengganti nama negara menjadi '[From.GetNameDef]'.",
    "wtt_news.64.a": "Roma Invicta!",
    "wtt_news.64.b": "Mereka pasti bercanda!",

    # 957 - 960: wtt_news.65 Persian Empire
    "wtt_news.65.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.65.desc": "Seiring gerak maju [From.GetOldAdjective] yang terus berlanjut, kemiripan historis tidak luput dari perhatian mereka yang mendalami sejarah Persia. Tokoh-tokoh masyarakat terkemuka telah mulai membandingkan ekspansi ini dengan era Koresh yang Agung, dan kebanggaan nasionalis meluap di segenap lapisan masyarakat [From.GetOldAdjective].\\n\\nKetika kendali pemerintah diperluas atas wilayah-wilayah baru, dan seraya pemerintah menunggangi gelombang persetujuan publik yang tinggi ini, para pejabat telah mengonfirmasi bahwa nama negara secara resmi diganti menjadi '[From.GetNameDef]'.",
    "wtt_news.65.a": "Kekuatan kita terus berlipat ganda!",
    "wtt_news.65.b": "Akankah ini membawa perdamaian dan stabilitas di kawasan?",

    # 961 - 964: wtt_news.66 Byzantine Empire
    "wtt_news.66.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.66.desc": "Kenaikan pesat [From.GetOldAdjectiveCap] membingungkan banyak pakar militer di seantero dunia, namun hasilnya berbicara sendiri. Hanya dalam hitungan tahun, bangsa Yunani telah mendominasi Balkan sepenuhnya, merebut kembali Istanbul, dan menumpas setiap perlawanan terorganisir Turki di Anatolia. Tampaknya puncak penutup dari lebih lima abad konflik Yunani-Turki kini telah tercapai.\\n\\nDemi semakin mengobarkan kebanggaan nasional, pemerintah [From.GetOldAdjectiveCap] memanfaatkan kesinambungan sejarah, menggambarkan pencapaian militer mereka sebagai 'penaklukan kembali Bizantium melawan penyerbu Turkik'. Sebagai bagian dari propaganda ini, di tengah parade seremonial megah di Konstantinopel yang baru berganti nama, diumumkan bahwa [From.GetOldNameDef] telah mengubah nama resminya menjadi '[From.GetNameDef]'.",
    "wtt_news.66.a": "Biarkan penaklukan kembali dimulai.",
    "wtt_news.66.b": "Pembalikan nasib yang sungguh ajaib...",

    # 965 - 968: wtt_news.67 Arabia
    "wtt_news.67.t": "Penyatuan Jazirah Arab",
    "wtt_news.67.desc": "Dengan penaklukan sebagian besar Jazirah Arab oleh [From.GetOldAdjective], pemerintah memanfaatkan gelombang baru Pan-Arabisme yang menyebar ke seluruh kawasan. Saat perselisihan internasional telah 'diselesaikan' melalui penyingkiran langsung pemerintah asing yang keras kepala dengan kekuatan militer, unifikasi Arab terasa dalam jangkauan mudah, dan pemerintah [From.GetOldAdjective] telah menunjukkan kesediaannya untuk mengejar cita-cita ini.\\n\\nBaik sekadar 'menunggangi gelombang' itikad baik masyarakat ini, untuk memikat sebagai rumah bagi seluruh bangsa Arab, atau hanya untuk memfasilitasi integrasi kawasan, pejabat [From.GetOldAdjective] kini mengonfirmasi bahwa nama resmi negara diubah menjadi '[From.GetNameDef]'.",
    "wtt_news.67.a": "Impian Zaydan akhirnya terwujud.",
    "wtt_news.67.b": "Akankah ini mengarah pada perdamaian abadi di kawasan?",

    # 969 - 972: wtt_news.68 Majapahit / Nusantara / Indonesia
    "wtt_news.68.t": "Kebangkitan [From.GetNameDef]",
    "wtt_news.68.desc": "Seiring meluasnya bangsa [From.GetOldAdjective] ke wilayah-wilayah tetangganya, upaya pemerintah membangun kesinambungan sejarah kian tampak jelas, demi mempersatukan rakyat. Kejayaan Kemaharajaan Majapahit dan kerajaan-kerajaan nusantara lainnya telah diromantisasi secara mendalam, dan propaganda gencar tampaknya berhasil memikat hati khalayak ramai.\\n\\nHari ini, pemerintah [From.GetOldAdjective] mengambil langkah bersejarah lebih jauh dan mengganti nama negara menjadi '[From.GetNameDef]' sebagai penghormatan agung atas sejarah kawasan, dengan harapan bahwa ini adalah identitas yang dapat dirangkul oleh setiap jiwa di nusantara.",
    "wtt_news.68.a": "Inilah akhir dari belenggu kolonialisme di Asia!",
    "wtt_news.68.b": "Mereka telah merebut kembali takdir mereka sendiri.",

    # 973 - 976: wtt_news.69 Rattanakosin / Siam
    "wtt_news.69.t": "Kelahiran Kembali [From.GetNameDef]",
    "wtt_news.69.desc": "Seiring bangsa [From.GetOldAdjective] meluas ke negara-negara tetangganya, pemerintah telah meninjau kembali keputusan masa lalu mereka meninggalkan nama Rattanakosin. Karena perbatasan mereka saat ini semakin menyerupai wilayah kerajaan pada puncak kejayaan sejarahnya, pencapaian Kerajaan Rattanakosin kian gencar dimanfaatkan demi memengaruhi opini publik.\\n\\nHari ini, pemerintah [From.GetOldAdjective] melangkah lebih jauh dan secara resmi mengganti nama negara menjadi '[From.GetNameDef]' dalam upaya menarik legitimasi langsung dari lembaran sejarah masa lalu.",
    "wtt_news.69.a": "Kita telah menegakkan kembali hegemoni kita.",
    "wtt_news.69.b": "Apakah imperium kolonial sedang runtuh?",

    # 977 - 979: wtt_news.70 Holy Roman Empire
    "wtt_news.70.t": "Kelahiran Kembali [From.GetNameDef]",
    "wtt_news.70.desc": "Di bawah kepemimpinan [FROM.GetLeader], [From.GetOldNameDef] telah meluaskan perbatasannya secara spektakuler, bahkan melampaui wilayah Kekaisaran Romawi Suci masa lampau. Semua lawan di daratan Eropa yang berani menentang kekuasaannya telah ditundukkan oleh mesin perang [From.GetOldAdjective], membiarkannya bebas tanpa tandingan dalam menjalankan kebijakannya.\\n\\nKini, [FROM.GetLeader.GetSheHe] telah menitahkan bahwa peluang emas saat ini harus diraih, dan bangsa ini harus menjadi penerus spiritual dari Kekaisaran Romawi Suci. Untuk merefleksikan hal tersebut, negara ini kini telah resmi berganti nama, dan dengannya beliau akhirnya mencapai unifikasi politik kawasan yang telah luput dari genggaman para Kaisar selama berabad-abad.",
    "wtt_news.70.a": "Aquila Elegit Iovis Omnia Vincit!",

    # 980 - 986: wtt_news.70 options / wtt_warlord_vs_prc.1
    "wtt_news.70.b": "Kekaisaran Abadi bangkit dari abu masa lalu.",
    "wtt_warlord_vs_prc.1.t": "Bantuan dari Moskow",
    "wtt_warlord_vs_prc.1.desc": "Dalam upaya memperkuat posisi kita di Tiongkok barat laut dan membantu memajukan perjuangan revolusi, pemerintah [SOV.GetAdjective] telah mengalokasikan sejumlah besar bantuan ekonomi dan industri kepada kita. Dengan dukungan Soviet di pihak kita, kita dapat mengamankan kepemimpinan atas Partai Komunis.",
    "wtt_warlord_vs_prc.1.a": "Bersama kita membangun sosialisme!",
    "wtt_warlord_vs_prc.1.a_tooltip": "Hal ini akan memicu perang dengan §H[communist_china.GetNameDef]§! jika mereka menolak.\\n",
    "wtt_warlord_vs_prc.1.b": "Kita terima bantuan ini, tapi tetap waspada.",

    # 987 - 995: wtt_warlord_vs_prc.2, 3, 4
    "wtt_warlord_vs_prc.2.t": "Pesan dari [soviet.GetLeader]",
    "wtt_warlord_vs_prc.2.desc": "Perwakilan pemerintah [SOV.GetAdjective] telah memberitahu kita bahwa [SOV.GetLeader] memiliki keraguan mendalam mengenai ketepatan penafsiran teori Marxis oleh [communist_china.GetLeader]. Dalam fase kritis perjuangan kelas di Tiongkok ini, kita tidak boleh menyimpang dari penerapan ajaran Marxis-Leninis yang benar. Tampaknya Moskow meyakini bahwa [warlord.GetLeader] memiliki pemahaman yang lebih baik tentang apa yang dibutuhkan untuk memajukan perjuangan Komunis di Tiongkok. Sejauh yang menjadi perhatian Moskow, partai sebaiknya menerima [warlord.GetLeader] sebagai ketua baru, atau menanggung murka [SOV.GetLeader].",
    "wtt_warlord_vs_prc.2.a": "Kirim [communist_china.GetLeader] ke Moskow untuk meluruskan masalah ini.",
    "wtt_warlord_vs_prc.2.b": "Kita tidak akan pernah tunduk kepada pengkhianat!",
    "wtt_warlord_vs_prc.3.t": "[SOV.GetLeader] Menolak",
    "wtt_warlord_vs_prc.3.desc": "[SOV.GetLeader] dilaporkan tetap tidak yakin akan loyalitas atau kemampuan kita memimpin. Pemerintah [SOV.GetAdjective] terus mendukung [communist_china.GetLeader] sebagai ketua Partai Komunis Tiongkok.",
    "wtt_warlord_vs_prc.3.a": "Biarlah hal ini menjadi rahasia di antara kita.",
    "wtt_warlord_vs_prc.4.t": "[communist_china.GetNameDefCap] Tunduk",
    "wtt_warlord_vs_prc.4.desc": "Banding keputusasaan yang diajukan oleh [communist_china.GetLeader] kepada [SOV.GetLeader] tidak membuahkan hasil untuk menarik simpati Soviet ke pihaknya. Menyadari perjuangan yang sia-sia, [communist_china.GetLeader] secara terbuka mengakui kekeliruannya dan berjanji akan bekerja sama dengan kita demi memastikan kemenangan revolusi.",
    "wtt_warlord_vs_prc.4.a": "Bagus.",

    # 996 - 999: wtt_warlord_vs_prc.10
    "wtt_warlord_vs_prc.10.t": "Bergabung atau Binasa",
    "wtt_warlord_vs_prc.10.desc": "Dihadapkan pada pilihan antara menyerahkan kekuasaan atau menantang gertakan Soviet, [communist_china.GetLeader] memilih opsi kedua. Sayangnya, terbukti bahwa [SOV.GetLeader] tidak sekadar menggertak dan permusuhan bersenjata pun telah dimulai. Mengingat posisi kita yang genting, kita berada di bawah tekanan hebat dari kedua belah pihak, di mana Soviet menuntut kita membantu mereka menggulingkan sang pengkhianat.\\n\\nPenolakan, tegas mereka, sama saja dengan memilih memihak [communist_china.GetLeader].",
    "wtt_warlord_vs_prc.10.a": "Tidak ada gunanya mati demi [communist_china.GetLeader]",
    "wtt_warlord_vs_prc.10.b": "Kita tidak akan terlibat dalam pertikaian ini.",

    # 1000 - 1010: wtt_warlord_vs_prc.21, 22, 23
    "wtt_warlord_vs_prc.21.t": "[From.GetLeader] Menuntut Dukungan Kita",
    "wtt_warlord_vs_prc.21.desc": "Sebuah pesan dari [From.GetLeader] telah tiba, menuntut agar kita mempercepat pengiriman bantuan ekonomi yang telah disepakati sebelumnya.",
    "wtt_warlord_vs_prc.21.a": "Inilah harga yang harus kita bayar.",
    "wtt_warlord_vs_prc.21.b": "Ini pemerasan terang-terangan!",
    "wtt_warlord_vs_prc.22.t": "[From.GetNameDefCap] Menerima",
    "wtt_warlord_vs_prc.22.desc": "Meskipun disertai protes seperti biasa dari [From.GetLeader], ia telah setuju untuk meningkatkan laju pembayaran sebagaimana yang kita minta.",
    "wtt_warlord_vs_prc.22.a": "Sebaiknya ia berdoa agar kita tidak mengubah kesepakatan lebih jauh.",
    "wtt_warlord_vs_prc.23.t": "[From.GetNameDefCap] Menolak",
    "wtt_warlord_vs_prc.23.desc": "[From.GetLeader] telah menjawab permintaan kita akan dukungan tambahan dengan penolakan mentah-mentah, mengklaim bahwa negaranya sama sekali tidak sanggup melakukan pembayaran \"absurd\" yang kita tuntut.",
    "wtt_warlord_vs_prc.23.a": "Ia telah berjanji, dan kita akan menuntut apa yang menjadi hak kita!",
    "wtt_warlord_vs_prc.23.b": "Biarkan saja untuk kali ini.",

    # 1011 - 1023: wtt_warlord_vs_prc.31, 32, 33, 34
    "wtt_warlord_vs_prc.31.t": "[From.GetLeader] Menuntut Kerja Sama Lebih Erat",
    "wtt_warlord_vs_prc.31.desc": "Sebuah pesan dari [From.GetLeader] telah tiba, menyatakan bahwa tahap perjuangan revolusioner kita saat ini sangat rentan dan dapat dengan mudah menjadi korban kontra-revolusi. Perwakilan khususnya telah diinstruksikan untuk mengawasi dengan saksama jalannya pemerintahan di negara kita dan menasihati kita tentang cara meraih kemenangan dalam perjuangan kelas.\\n\\nNota tersebut lebih lanjut menyatakan bahwa setiap penyimpangan dari 'sarannya' akan dianggap sebagai tanda bahwa elemen reaksioner telah mencengkeram pemerintahan kita, dan langkah-langkah yang diperlukan kemudian akan diambil.",
    "wtt_warlord_vs_prc.31.a": "Kita menyambut baik kesempatan untuk belajar.",
    "wtt_warlord_vs_prc.31.b": "Kita tidak butuh orang lain mendikte tindakan kita.",
    "wtt_warlord_vs_prc.32.t": "[From.GetNameDefCap] Menerima",
    "wtt_warlord_vs_prc.32.desc": "[From.GetLeader] telah menyambut perwakilan khusus kita dan mengangkatnya sebagai penasihat pribadi. Kita kini memiliki kendali yang sangat kokoh atas kebijakan internal dan eksternal mereka.",
    "wtt_warlord_vs_prc.32.a": "Ia akhirnya berpikir rasional.",
    "wtt_warlord_vs_prc.33.t": "[From.GetNameDefCap] Menolak",
    "wtt_warlord_vs_prc.33.desc": "Meskipun terbuka terhadap gagasan itu, [From.GetLeader] dengan sopan namun tegas menolak tuntutan kita untuk mempengaruhi kebijakan mereka secara lebih langsung. Tampaknya menurut mereka kita 'tidak memahami' kondisi di lapangan dan sebaiknya menyerahkan penerapan ajaran Marxis kepada para pakar lokal.",
    "wtt_warlord_vs_prc.33.a": "Mungkin kita perlu menegaskannya dengan cara yang lebih keras.",
    "wtt_warlord_vs_prc.34.t": "[From.GetNameDefCap] Menolak Membayar",
    "wtt_warlord_vs_prc.34.desc": "[From.GetLeader] mengabaikan tuntutan kita yang semakin keras agar ia mentransfer pembayaran yang disepakati sebelumnya. Bahkan permintaan agar ia datang ke Moskow guna memberikan penjelasan pun dibiarkan tanpa jawaban.",
    "wtt_warlord_vs_prc.34.a": "Jadi ia berani menguji kesabaran kita?",

    # 1024 - 1031: wtt_warlord_vs_prc.35, 36
    "wtt_warlord_vs_prc.35.t": "Persekutuan [From.GetAdjective]",
    "wtt_warlord_vs_prc.35.desc": "[From.GetNameDefCap] telah meminta agar kaum komunis Tiongkok bergabung dalam satu faksi tunggal, sebuah Front Rakyat, untuk mengalahkan kaum nasionalis, reaksioner, dan penyerbu asing di bawah satu panji perjuangan.",
    "wtt_warlord_vs_prc.35.a": "Rakyatlah sang pahlawan sejati sekarang!",
    "wtt_warlord_vs_prc.35.b": "Ini bertentangan dengan kepentingan [Root.GetAdjective].",
    "wtt_warlord_vs_prc.36.t": "[From.GetLeader] Menolak Persekutuan",
    "wtt_warlord_vs_prc.36.desc": "[From.GetNameDefCap] telah menolak jalur Front Rakyat yang jelas menguntungkan untuk bersatu melawan kaum nasionalis, reaksioner, dan penjajah asing, seraya menyatakan bahwa persekutuan kita akan 'bertentangan dengan kepentingan [From.GetAdjective].'",
    "wtt_warlord_vs_prc.36.a": "Kita terpaksa berjuang sendirian.",
    "wtt_warlord_vs_prc.36.b": "Kita mungkin sebaiknya membubarkan Front Persatuan sama sekali.",

    # 1032 - 1046: wtt_manchukou.1, 2, 3, 11
    "wtt_manchukou.1.t": "[From.GetNameDefCap] Menuntut Ketundukan",
    "wtt_manchukou.1.desc": "Tampaknya [From.GetLeader] telah mengambil keputusan untuk akhirnya meluaskan otoritasnya ke penjuru pelosok Tiongkok. Utusan dari Pemerintah [From.GetAdjective] telah tiba, menuntut agar kita tunduk dan menyembah kepada satu-satunya Kaisar sejati Tiongkok, sang Putra Langit, [From.GetLeader]. Menolak untuk tunduk, lanjutnya, akan dihukum sebagai pengkhianatan tingkat tertinggi.",
    "wtt_manchukou.1.a": "Gagasan Republik ini sejak awal memang tidak pernah berhasil.",
    "wtt_manchukou.1.b": "Biarkan ia mencoba jika berani.",
    "wtt_manchukou.2.t": "[From.GetLeader] Tunduk",
    "wtt_manchukou.2.desc": "[From.GetLeader] telah memulangkan utusan kita dengan pesan pribadi, berjanji untuk taat sepenuhnya dan menyambut [MAN.GetLeader] sebagai pemimpin sejati Tiongkok.",
    "wtt_manchukou.2.a": "Ia tahu di mana tempatnya.",
    "wtt_manchukou.3.t": "[From.GetLeader] Menolak",
    "wtt_manchukou.3.desc": "[From.GetLeader] telah membalas tawaran murah hati kita dengan serentetan hinaan dan sumpah serapah, melontarkan pernyataan mengenai asal-usul keturunan dan kepribadian Kaisar [MAN.GetLeader] yang sama sekali tidak benar serta sangat menyinggung.",
    "wtt_manchukou.3.a": "Kita akan mengajarinya sopan santun.",
    "wtt_manchukou.11.t": "Rencana Lima Tahun",
    "wtt_manchukou.11.desc": "Rencana Lima Tahun yang merinci bagaimana pemerintah kita berencana menumbuhkan perekonomian pada tahun-tahun mendatang perlahan mulai terbentuk. Perbedaan pandangan yang signifikan masih ada di antara berbagai departemen mengenai di mana fokus utama harus diletakkan.\\n\\nMeskipun terdapat konsensus bahwa ekspansi industri berat harus menjadi tujuan utama, jenis produksi pabrik-pabrik baru ini masih dalam perdebatan.\\n\\nSebuah keputusan harus segera diambil untuk memecah kebuntuan ini.",
    "wtt_manchukou.11.a": "Bangun Industri Penerbangan Kita",
    "wtt_manchukou.11.b": "Investasikan pada Industri Otomotif",
    "wtt_manchukou.11.c": "Program Industrialisasi Umum",

    # 1047 - 1052: wtt_manchukou_bandit_sabotage
    "wtt_manchukou_bandit_sabotage.21.t": "Pabrik Senjata Disabotase",
    "wtt_manchukou_bandit_sabotage.21.desc": "Laporan berdatangan dari salah satu pabrik kita di [FROM.GetName], melaporkan bahwa kebakaran dahsyat berkobar tadi malam. Petugas pemadam kebakaran setempat masih berjuang memadamkan api, namun optimis dapat mengendalikannya menjelang akhir hari. Kerusakan pada pabrik diperkirakan sangat signifikan, karena api tampaknya bermula di area penyimpanan bahan kimia yang sangat mudah terbakar.\\n\\nIntelijen Militer telah memulai penyelidikan menyeluruh untuk mencari tahu bagaimana kebakaran dapat terjadi meski protokol keselamatan paling ketat telah diterapkan. Petunjuk awal mengarah kuat pada sabotase pembakaran terencana.",
    "wtt_manchukou_bandit_sabotage.21.a": "Para teroris ini harus diburu sampai dapat!",
    "wtt_manchukou_bandit_sabotage.22.t": "Pabrik Sipil Disabotase",
    "wtt_manchukou_bandit_sabotage.23.t": "Jembatan Diledakkan",
    "wtt_manchukou_bandit_sabotage.23.desc": "Pada suatu waktu tadi malam, sebuah jembatan rel kereta api utama di [FROM.GetName] runtuh di bawah beban kereta pembawa amunisi yang melintas. Upaya penyelamatan dan evakuasi dipersulit oleh ledakan sekunder dari amunisi. Awak kereta masih hilang dan diduga tewas.\\n\\nIntelijen Militer telah mengirim tim untuk menyelidiki lokasi segera setelah situasi dirasa aman, guna mencari tahu bagaimana jembatan sekokoh itu bisa runtuh tanpa tanda-tanda kerusakan sebelumnya.\\n\\nSaksi mata setempat melaporkan melihat sekelompok kecil orang di lembah di bawah jembatan pada hari sebelum keruntuhan. Keberadaan mereka saat ini tidak diketahui.",

    # 1053 - 1075: generic.11 - 16, tooltips
    "generic.11.t": "Perang Saudara Berakhir",
    "generic.11.d": "Perang yang mengoyak bangsa kita akhirnya telah usai. Kita kini dapat memulai tugas menyatukan kembali rakyat kita dan memulihkan kehancuran yang terjadi.",
    "generic.11.a": "Bersama, kita akan berjuang demi masa depan yang lebih baik!",
    "generic.12.t": "[From.GetAdjective] Berusaha Menyabotase Suez",
    "generic.12.d": "Intelijen militer mengindikasikan bahwa pihak [From.GetAdjective] berniat menggunakan peledakan skala besar dan kapal penyumbat untuk menyabotase Terusan Suez. Jika kita ingin menghentikan mereka, waktu kita tidak banyak.",
    "generic.12.a": "Kita tidak boleh membiarkan ini terjadi!",
    "generic.13.t": "[From.GetAdjective] Berusaha Menyabotase Panama",
    "generic.13.d": "Intelijen militer mengindikasikan bahwa pihak [From.GetAdjective] berniat menggunakan peledakan skala besar dan kapal penyumbat untuk menyabotase Terusan Panama. Jika kita ingin menggagalkan rencana mereka, kita tidak punya banyak waktu.",
    "generic.14.t": "[From.GetName] Melayangkan Protes Diplomatik",
    "generic.14.d": "Utusan [From.GetAdjective] telah mengajukan protes diplomatik keras kepada pemerintah kita mengenai keberadaan atase militer kita di negara-negara yang saat ini berkonflik senjata dengan mereka. Mereka menuntut penarikan segera misi militer kita.",
    "generic.14.a": "Itu adalah permintaan yang wajar.",
    "generic.14.b": "Atase kita akan dikirim ke mana pun kita kehendaki.",
    "attache_political_power_tt": "Berdasarkan kekuatan relatif kita dan §Yopini§! kita terhadap mereka, ini akan menimbulkan efek berikut:\\n",
    "attache_fascism_tt": "Berdasarkan tingkat dukungan §YFasisme§! di negara kita, ini akan memberikan pengaruh berikut:\\n",
    "attache_communism_tt": "Berdasarkan tingkat dukungan §YKomunisme§! di negara kita, ini akan memberikan dampak berikut:\\n",
    "attache_democratic_tt": "Berdasarkan tingkat dukungan §YDemokratis§! di negara kita, ini akan memiliki efek berikut:\\n",
    "attache_neutrality_tt": "Berdasarkan tingkat dukungan §YNetral / Non-Blok§! di negara kita, ini akan memberikan akibat berikut:\\n",
    "generic.15.t": "[From.GetName] Menarik Kembali Atase",
    "generic.15.d": "Menanggapi tuntutan kita, [From.GetNameDef] telah menarik misi militer mereka dari musuh-musuh kita.",
    "generic.16.t": "[From.GetName] Tetap Mempertahankan Atase",
    "generic.16.d": "Mengabaikan tuntutan kita, [From.GetNameDef] menolak menarik misi militer mereka dari musuh kita, seraya menyatakan bahwa \"kita tidak berhak mencampuri urusan internal [From.GetAdjective]\".",
    "generic.16.a": "Kita lihat saja nanti.",
    "canals_tt": "Rebut kendali atas tepi terusan dalam kurun waktu satu bulan ke depan guna menggagalkan rencana musuh.",

    # 1076 - 1096: japan_border_conflict
    "japan_border_conflict.1.t": "Provokasi Jepang di Perbatasan Kita",
    "japan_border_conflict.1.desc": "Sebagai bagian dari pemeliharaan garis demarkasi di perbatasan antara kita dan [JAP.GetNameDef], sebuah tim kerja dikirim untuk memeriksa patok demarkasi di dekat Danau Khasan. Saat mendekati perbatasan, tim kerja tersebut ditembaki oleh pos terdepan Jepang di daerah itu.\\n\\nKita telah mengajukan protes diplomatik resmi, namun duta besar Jepang bersikeras bahwa tim kerja itu dikirim untuk memindahkan patok agar kita dapat mengklaim lebih banyak wilayah.\\n\\nPihak Jepang meyakinkan kita bahwa mereka akan menghormati perbatasan tetapi tidak akan mentolerir adanya \"pengubahan\" apa pun terhadap demarkasi saat ini dan akan membalas dengan kekuatan militer bila kita berupaya melakukannya.\\n\\nIni secara efektif berarti kita tidak lagi dapat bergerak bebas di wilayah kita sendiri di kawasan tersebut.",
    "japan_border_conflict.1.a": "Tidak bisa diterima.",
    "japan_border_conflict.2.t": "Kemenangan Jepang di Danau Khasan",
    "japan_border_conflict.2.desc": "Menyusul bentrokan antara pasukan [SOV.GetAdjective] dan Jepang di wilayah perbatasan sekitar Danau Khasan, pasukan [SOV.GetAdjective] dilaporkan mundur sepenuhnya. Unit-unit Jepang telah menduduki sejumlah bukit strategis di sekitar area tersebut dan mulai membentengi posisi mereka.\\n\\nSelama pertempuran, pihak Jepang menyita sejumlah tank [SOV.GetAdjective], yang telah dikapalkan ke Tokyo untuk dievaluasi.",
    "japan_border_conflict.2.a": "Kita telah menuntaskan persoalan ini dengan terhormat.",
    "japan_border_conflict.2.b": "Kita harus mempersiapkan respons yang setimpal.",
    "japan_border_conflict.3.t": "Kekalahan Jepang di Danau Khasan",
    "japan_border_conflict.3.desc": "Menyusul bentrokan antara pasukan [SOV.GetAdjective] dan Jepang di kawasan perbatasan sekitar Danau Khasan, duta besar Jepang di Moskow telah meminta gencatan senjata.\\n\\nBeberapa serangan Jepang ke posisi [SOV.GetAdjective] gagal dengan korban jiwa yang sangat besar selama pertempuran, memicu kekhawatiran mendalam di kalangan militer Jepang mengenai kapabilitas tempur pasukan mereka.",
    "japan_border_conflict.3.a": "Lebih baik gagal secara terhormat daripada tidak mencoba sama sekali.",
    "japan_border_conflict.3.b": "Pasukan kita telah membuktikan ketangguhan mereka.",
    "japan_border_conflict.4.t": "Kebuntuan di Danau Khasan",
    "japan_border_conflict.4.desc": "Pertempuran antara pasukan Jepang dan [SOV.GetAdjective] di sekitar Danau Khasan telah mereda setelah kedua belah pihak mundur dari wilayah yang disengketakan untuk memulihkan diri dan memasok ulang perbekalan. Menyadari kesia-siaan serangan lanjutan, militer Jepang telah meminta gencatan senjata dan pembukaan negosiasi untuk menetapkan perbatasan.",
    "japan_border_conflict.4.a": "Kita memperoleh pengalaman tempur yang berharga.",
    "japan_border_conflict.5.t": "Eskalasi di Danau Khasan",
    "japan_border_conflict.5.desc": "Pertempuran sengit terus berlanjut antara pasukan Jepang dan [SOV.GetAdjective] di sekitar Danau Khasan. Dalam upaya memecah kebuntuan, pasukan Jepang di sektor lain juga mulai menyerang pasukan [SOV.GetAdjective] di wilayah itu. Laporan intelijen mengindikasikan bahwa Jepang kemungkinan akan segera memperkuat serangan dengan pasukan segar yang dipindahkan dari bagian lain Kekaisaran mereka.",
    "japan_border_conflict.5.a": "Kita harus mempertahankan garis ini!",
    "japan_border_conflict.6.t": "Eskalasi di Danau Khasan",
    "japan_border_conflict.6.desc": "Pertempuran terus berkecamuk antara pasukan [FROM.GetAdjective] dan [JAP.GetAdjective] di sekitar Danau Khasan. Dalam upaya memecahkan kebuntuan, pasukan [FROM.GetAdjective] di wilayah lain juga mulai menggempur pasukan [JAP.GetAdjective] di sektor tersebut. Intelijen mengindikasikan bahwa [FROM.GetNameDef] kemungkinan akan segera memperkuat serangan dengan divisi-divisi segar yang dipindahkan dari bagian lain negeri mereka.",
    "japan_border_conflict.6.a": "Kita harus bersiap menyerang!",
    "JAP_kalkin_gol": "Soviet Diuji",

    # 1097 - 1102: wtt_prc.30, 31, 32, 20.c
    "wtt_prc.30.t": "Provokasi Berhasil",
    "wtt_prc.30.desc": "Bergerak di bawah lindungan kegelapan malam, kawan-kawan kita di [JAP.GetManchuriaPuppet] telah menyabotase sebuah pabrik Jepang. Detail mengenai tingkat kerusakan masih terbatas karena kaum Imperialis telah menyatakan seluruh wilayah tersebut sebagai zona tertutup.\\n\\nFakta ini saja sudah cukup membuktikan bahwa pukulan kita tepat mengenai sasaran. Masih harus dilihat apakah ini akan memancing pihak Jepang untuk mengambil tindakan.",
    "wtt_prc.30.a": "Kita telah mengusik Sarang Lebah.",
    "wtt_prc.31.desc": "Bekerja di bawah kegelapan malam, kawan-kawan kita di [JAP.GetManchuriaPuppet] telah berhasil menyabotase jembatan rel vital. Pasukan komando kecil melaporkan bahwa jembatan hancur total dan turut menjatuhkan kereta amunisi saat runtuh.\\n\\nMereka sengaja menampakkan diri kepada penduduk setempat demi menegaskan bahwa ini adalah aksi sabotase terencana. Masih harus dilihat apakah hal ini akan memancing respons militer dari Jepang.",
    "wtt_prc.32.desc": "Kita telah berhasil menyergap dan memusnahkan patroli Jepang di [JAP.GetManchuriaPuppet]. Jasad mereka ditinggalkan di lokasi kejadian demi memastikan para Imperialis menerima pesan kita dengan sangat jelas.\\n\\nWaktu yang akan membuktikan apakah mereka menganggap aksi ini cukup sebagai alasan untuk mengobarkan perang.",
    "wtt_prc.20.c": "Kita sebaiknya mundur sepenuhnya dari benua ini.",

    # 1103 - 1105: wtt_germany.1006
    "wtt_germany.1006.t": "Kaisar Sedang Menyiapkan Kudeta!",
    "wtt_germany.1006.desc": "Servizio Informazioni Militare melaporkan adanya aktivitas mencurigakan di lingkaran dalam kaum monarkis. Tampaknya beberapa dari mereka yang hanya setia kepada raja baru-baru ini telah berhubungan dengan agen asing, dan itu adalah agen Jerman. Sepertinya kaum monarkis tengah direkrut dan dihimpun untuk menentang pemimpin agung kita, namun belum terlambat. Kita dapat mengirim geng preman jalanan untuk menghabisi mereka dan memukul mundur mereka selagi kita masih punya kesempatan. Bagaimana kita harus bertindak?",
    "wtt_germany.1006.a": "Banda Carità dapat membereskan mereka",

    # 1106 - 1117: britain.25, 26, 27
    "britain.25.t": "[ENG.GetNameDefCap] Menuntut Ketundukan",
    "britain.25.desc": "Pemerintah [ENG.GetAdjective], yang tampaknya cemas setelah jatuhnya [DEN.GetNameDef] serta kehadiran diplomat [GER.GetAdjective] di [ICE.GetNameDef], telah mengundang kita untuk bergabung dengan pihak Sekutu sebagai rekan berperang. Mereka mengutip kekhawatiran akan keamanan nasional mereka di mana pihak [GER.GetNameDef] berpotensi menggunakan pangkalan di Islandia sebagai batu loncatan untuk menyerbu konvoi atau kota-kota Inggris.\\nAncaman mereka terselubung tipis, mengutip situasi dunia saat ini bahwa setiap klaim \"netralitas semu\" dari pihak kita terhapus oleh keselamatan warga negara Inggris dan perang melawan fasisme.",
    "britain.25.a": "Kita tidak punya pilihan selain bergabung dengan [ENG.GetFactionName]",
    "britain.25.b": "Persetan dengan pihak [ENG.GetAdjective]",
    "britain.25.c": "Kita harus berpegang teguh pada netralitas kita, meski itu berarti invasi",
    "britain.26.t": "[ICE.GetNameDefCap] Mencari Perlindungan Kita dari [ENG.GetNameDef]",
    "britain.26.desc": "Para diplomat kita yang saat ini bertugas di [ICE.GetNameDef] telah mengirimkan rentetan pesan bahwa pemerintah muda [ICE.GetAdjective] telah diancam dengan pendudukan oleh pasukan Inggris kecuali mereka tunduk. Karena tidak memiliki alternatif lain yang memungkinkan, [ICE.GetLeader.GetName] telah meminta perlindungan kita dari ancaman Inggris. Mungkinkah sebuah pangkalan yang begitu dekat dengan daratan Inggris akan menguntungkan bagi kita?",
    "britain.26.a": "Rakyat [ICE.GetNameDef] harus dilindungi",
    "britain.26.b": "Kita tidak bisa menyia-nyiakan sumber daya untuk itu",
    "britain.27.t": "[ICE.GetNameDefCap] Menolak Usulan Kita",
    "britain.27.desc": "Pemerintah [ICE.GetAdjective] telah menolak ultimatum kepatuhan kita, seraya mengutip keyakinan mereka pada netralitas dan penentangan keras untuk diseret ke dalam perang yang tidak ada hubungannya dengan mereka.\\nMereka menuduh bahwa dengan perintah ini kemerdekaan mereka telah dilanggar secara terang-terangan. Sungguh menyedihkan ini adalah perang modern, dan dalam perang modern tidak ada pihak yang bisa netral; meski kita menyesali tindakan ini, kita harus melakukan apa yang harus dilakukan.",
    "britain.27.a": "Langkah yang patut disesali namun tak terhindarkan"
}

with open("wtt_events_raw.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

# Slice 875:1118
slice_raw = raw[875:1118]
out = []
missing = []

for item in slice_raw:
    k = item["key"]
    if k in chunk7_translations:
        out.append({"key": k, "id": chunk7_translations[k]})
    else:
        missing.append(k)

if missing:
    print("MISSING KEYS in chunk 7:", len(missing), missing)
else:
    with open("wtt_events_chunk7.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved events chunk 7: {len(out)} entries")
