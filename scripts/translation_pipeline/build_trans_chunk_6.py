import json
import re

c6_trans = {
  "ww_BEL_event_diplomatic.27.t": "[FROM.GetNameDefCap] Mengizinkan Federalisasi Terbatas",
  "ww_BEL_event_diplomatic.27.desc": "[FROM.GetNameDefCap] telah menyetujui permintaan kita untuk mengikat diri mereka lebih erat dengan [FROM.GetFactionName]. Kita akan diberikan wewenang tertentu atas kebijakan luar negeri mereka dan perdagangan antarnegara kita akan dipermudah.",
  "ww_BEL_event_diplomatic.27.a": "Luar biasa!",
  "ww_BEL_event_diplomatic.28.t": "[FROM.GetNameDefCap] Menolak Federalisasi Terbatas",
  "ww_BEL_event_diplomatic.28.desc": "Meskipun memiliki keuntungan yang jelas, [FROM.GetNameDef] telah memilih untuk tidak bergabung dengan gagasan Eropa berformat federal kita. Mereka berdalih bahwa kedaulatan mereka sendiri berdiri di atas kesejahteraan seluruh $EU_tech_sharing_group_name$, yang merupakan sentimen yang cukup mengkhawatirkan dari dalam persatuan.",
  "ww_BEL_event_diplomatic.28.a": "Hal itu sangat mengkhawatirkan",
  "ww_BEL_event_diplomatic.28.b": "Mereka adalah ancaman bagi kita semua!",
  "ww_BEL_event_diplomatic.29.t": "Otto von Habsburg Menawarkan Dukungannya",
  "ww_BEL_event_diplomatic.29.desc": "Kita telah menerima tawaran dukungan dari sosok yang cukup mengejutkan untuk didengar. Otto von Habsburg mungkin adalah pewaris Karl I, Kaisar Austria, Raja Hungaria, dan Raja Kroasia, namun tampaknya tidak seperti ayahnya, Otto jauh lebih condong ke arah kerja sama di Eropa. Ia menyambut baik upaya kita dan menawarkan bantuannya di ranah diplomatik; jaringan diplomatiknya yang luas dapat menjadi aset berharga bagi kita dan ini adalah bantuan yang dengan senang hati ia tawarkan.",
  "ww_BEL_event_diplomatic.29.a": "Merupakan kehormatan bagi kita untuk menerimanya bersama kita",
  "ww_BEL_event_diplomatic.29.b": "Wangsa Habsburg adalah bagian dari masa lalu.",
  "ww_BEL_event_diplomatic.30.t": "[FROM.GetNameDefCap] Memohon untuk Bergabung dengan [ROOT.GetFactionName]",
  "ww_BEL_event_diplomatic.30.desc": "Menyusul keputusan [FROM.GetAdjective] untuk menanggalkan aspirasi netralitas mereka, kepemimpinan [FROM.GetNameDef] telah menyelaraskan diri semakin erat dengan agenda politik kita. Mereka kini telah menghubungi kita dengan permintaan untuk bergabung langsung ke dalam [ROOT.GetFactionName]. Bantuan mereka dapat sangat berguna, membuka peluang baru bagi strategi ekspansi masa depan kita.",
  "ww_BEL_event_diplomatic.30.a": "Mereka disambut dengan hangat di sini",
  "ww_BEL_event_diplomatic.30.b": "Kita tidak membutuhkan mereka",
  "ww_BEL_event_diplomatic.31.t": "[FROM.GetNameDefCap] Menerima Kita ke dalam [FROM.GetFactionName]",
  "ww_BEL_event_diplomatic.31.desc": "Pemimpin [FROM.GetAdjective] [FROM.GetLeader] telah menghubungi untuk menyambut kita ke dalam [FROM.GetFactionName]. Mulai sekarang kita akan bertempur bahu-membahu melawan ancaman bersama. Masa-masa netralitas kita telah berakhir!",
  "ww_BEL_event_diplomatic.31.a": "Kabar Luar Biasa",
  "ww_BEL_event_diplomatic.32.t": "[FROM.GetNameDefCap] Menolak Keanggotaan Kita di [FROM.GetFactionName]",
  "ww_BEL_event_diplomatic.32.desc": "Terlepas dari berbagai manfaat nyata, pemimpin [FROM.GetAdjective] [FROM.GetLeader] telah menolak kita sebagai anggota [FROM.GetFactionName]. Kita sebenarnya dapat menyumbangkan banyak hal, namun menimbang tanggapan ini, kita harus mempertimbangkan kembali ambisi untuk bergabung dengan mereka, baik sekarang maupun di masa depan.",
  "ww_BEL_event_diplomatic.32.a": "Kita dapat menciptakan sesuatu yang lebih baik!",
  "BEL_tried_to_join_the_axis_flag": "Sudah pernah berupaya bergabung dengan [GER.GetFactionName]",
  "ww_BEL_event_diplomatic.33.t": "Masa Depan Netralitas [ROOT.GetAdjective]",
  "ww_BEL_event_diplomatic.33.desc": "Netralitas telah melayani negara kita dengan sangat baik, namun tetap bersikap netral dapat membuat pihak lain memandang kita tak lebih dari sekadar penonton pasif dan sasaran empuk. Kita harus mempertimbangkan dengan matang masa depan kebijakan luar negeri kita, serta sikap kita terkait perjuangan bersenjata mengingat konflik tampaknya akan segera melanda kita dalam waktu dekat.",
  "ww_BEL_event_diplomatic.33.a": "Kita harus memutus belenggu dan bersiap!",
  "ww_BEL_event_diplomatic.33.b": "Netralitas harus dipertahankan!",
  "ww_BEL_event_diplomatic.34.t": "[FRA.GetNameDefCap]: Kawan atau Lawan?",
  "ww_BEL_event_diplomatic.34.desc": "Betapa pun lengkapnya persenjataan kita, kita harus menerima kenyataan bahwa tetangga Selatan kita kemungkinan besar akan selalu memiliki kapasitas yang lebih besar. Kita harus mencapai kesepakatan bersama, apakah kita menganggap mereka sebagai kawan, ataukah lawan?",
  "ww_BEL_event_diplomatic.34.a": "Bangsa [FRA.GetAdjective] adalah kawan kita",
  "ww_BEL_event_diplomatic.34.b": "Bangsa [FRA.GetAdjective] tidak dapat dipercaya!",
  "ww_BEL_event_diplomatic.35.t": "[FROM.GetNameDefCap] Menghubungi Kita",
  "ww_BEL_event_diplomatic.35.desc": "Kita telah dihubungi oleh tetangga utara kita. Mereka berkehendak menjalin hubungan diplomatik yang lebih serius dengan kita. Tawaran mereka berpotensi menguntungkan kedua belah pihak, namun kita tetap harus berhati-hati dalam mengambil keputusan tepat perihal perkara ini.",
  "ww_BEL_event_diplomatic.35.a": "Tentu saja!",
  "ww_BEL_event_diplomatic.35.b": "Tidak, kita tidak melihat adanya manfaat dalam hal ini.",
  "ww_BEL_event_diplomatic.36.t": "Pihak [FROM.GetAdjective] Setuju",
  "ww_BEL_event_diplomatic.36.desc": "Pimpinan [FROM.GetNameDef] sepakat bahwa kita berdua dapat memetik manfaat dari memperdalam hubungan diplomatik. Kita dapat mengandalkan mereka sebagai kawan dan sekutu di dunia yang kian sarat permusuhan ini.",
  "ww_BEL_event_diplomatic.36.a": "Bagus sekali!",
  "ww_BEL_event_diplomatic.37.t": "Pihak [FROM.GetAdjective] Tidak Setuju",
  "ww_BEL_event_diplomatic.37.desc": "Terlepas dari keuntungan nyata bagi kedua belah pihak, tampaknya bangsa [FROM.GetAdjective] tidak bersedia memperluas hubungan diplomatik dengan kita melebihi apa yang telah ada. Kita menaruh harapan besar pada hal ini, namun harapan itu rupanya bertepuk sebelah tangan.",
  "ww_BEL_event_diplomatic.37.a": "Sungguh disayangkan...",
  "ww_BEL_event_war.1.t": "Industri Dirgantara yang Dipindahkan Diaktifkan",
  "ww_BEL_event_war.1.desc": "Pandangan jauh ke depan kita untuk membina hubungan kerja yang erat dengan perusahaan industri asing telah membuahkan hasil. Fasilitas mereka siap memulai produksi secepatnya.",
  "ww_BEL_event_war.1.a": "Inilah alasannya mengapa kita harus merencanakan masa depan!",
  "ww_BEL_event_war.2.t": "Simpati yang Masih Menjadi Misteri",
  "ww_BEL_event_war.2.desc": "Raja Leopold III selama ini hidup di bawah bayang-bayang kebesaran ayahnya, Raja Albert sang Raja Prajurit, yang termasyhur karena berhasil mempertahankan Belgia dalam kancah Perang Besar serta menggagalkan kemenangan Kekaisaran Jerman. Kendati dalam prosesnya negeri ini luluh lantak menjadi medan pertempuran, kehormatan militer bangsa tetap tak ternoda dan reputasi Belgia melambung tinggi di panggung dunia. \n\nKini, tatkala Belgia sekali lagi terseret ke dalam perang, ujian watak sesungguhnya bagi Leopold akan segera dimulai, dan riak keresahan yang mengkhawatirkan sudah mulai terdengar. \n\nBerdalih ingin melindungi nyawa rakyatnya, sang Raja telah mulai mencari celah perundingan damai, dan kita mencurigai bilamana Brussels, Liège, atau Antwerpen jatuh, sang Raja mungkin akan menyerah sebelum waktunya, tanpa memedulikan kehendak demokratis rakyat untuk terus bertempur.",
  "ww_BEL_event_war.2.a": "Raja Leopold akan memimpin kita menuju kemenangan.",
  "BEL_unknown_sympathies_tt": "§RRaja Leopold akan menyerah jika kita kehilangan salah satu dari Liège, Antwerpen, atau Brussels. Anda mungkin masih memiliki opsi jika saat itu tiba.§!",
  "ww_BEL_event_war.3.t": "Kapitulasi Sang Raja",
  "ww_BEL_event_war.3.desc": "Sang Raja, selaku Panglima Tertinggi angkatan bersenjata, hari ini telah menawarkan kapitulasi tanpa syarat bagi [BEL.GetName], tanpa menunggu ratifikasi terlebih dahulu dari parlemen [BEL.GetAdjective]. Secara teknis, selaku Panglima Tertinggi, beliau memiliki kewenangan untuk menyerahkan militer, namun bukan menyerahkan kedaulatan negara itu sendiri. \n\nParlemen sipil telah melarikan diri ke pengasingan, menegaskan dengan sangat gamblang niat mereka untuk melanjutkan pertempuran dengan mengerahkan segenap sumber daya Imperium [BEL.GetAdjective].",
  "ww_BEL_event_war.3.a": "Itu adalah kehendak sang Raja!",
  "ww_BEL_event_war.3.b": "Lanjutkan pertempuran!",
  "ww_BEL_event_war.3.c": "Beliau tidak memiliki hak untuk itu! Tahan sang raja sebagai tahanan rumah.",
  "ww_BEL_event_war.4.t": "Tawanan Kerajaan",
  "ww_BEL_event_war.4.desc": "Menyusul pengkhianatannya yang menyerahkan negara kepada sang penyerbu, Raja telah ditempatkan di bawah tahanan rumah dan dicopot dari posisinya sebagai Panglima Tertinggi angkatan bersenjata, dilucuti dari gelar-gelarnya, dan tentu saja dimakzulkan dari mahkotanya. Namun rakyat tetap membutuhkan seorang penguasa, dan kini menjadi pilihan kita mengenai siapa yang harus memimpin perwalian (regensi) hingga putranya cukup umur untuk naik takhta. Terdapat dua opsi: \n\nYang pertama adalah Léon Degrelle, sang Perdana Menteri dan pemimpin rakyat kita yang diangkat secara sah menurut hukum. Pilihan lainnya adalah Pangeran Charles, Pangeran Flandria, adik kandung Leopold yang akan memberikan nuansa legitimasi dan kesinambungan garis takhta.",
  "ww_BEL_event_war.4.a": "Jadikan Léon Degrelle sebagai pemangku takhta baru",
  "ww_BEL_event_war.4.b": "Amankan garis keturunan yang sah bersama Charles",
  "ww_BEL_event_war.5.t": "Kapitulasi Sang Raja",
  "ww_BEL_event_war.5.desc": "Menyusul perlawanan sengit demi mempertahankan bangsa, Raja Leopold III akhirnya menawarkan penyerahan diri [BEL.GetName] dan pemerintah kita terpaksa menyingkir ke pengasingan. Leopold memilih untuk tetap tinggal bersama rakyatnya, dan menjadi tawanan di istananya sendiri. Kita masih dapat bersandar pada niat baik para sekutu kita, serta mengerahkan segenap sumber daya Imperium [BEL.GetAdjective], agar pada saatnya nanti kita mampu memulihkan tanah air kita.",
  "ww_BEL_event_war.5.a": "Masa depan masih sarat ketidakpastian.",
  "ww_BEL_event_war.6.t": "Para Sekretaris Jenderal",
  "ww_BEL_event_war.6.desc": "Sekelompok pegawai negeri sipil Belgia telah mendatangi kita dengan sebuah tawaran; izinkan mereka melanjutkan tugas di kantor-kantor pemerintahan, dan mereka akan memastikan roda pemerintahan daerah tetap berputar lancar dalam masa transisi ini. Pemerintah Belgia telah mengesahkan undang-undang yang melegalkan kerja sama mereka dengan kita demi mengurangi dampak keras pendudukan terhadap rakyat mereka. Mereka bahkan telah memberikan izin kepada bank-bank Belgia untuk tetap membayarkan gaji para administrator ini. Ini adalah peluang bagi kita untuk menunjukkan kesediaan bekerja sama dengan penduduk setempat, dan akan sangat membantu meredam perlawanan aktif di wilayah tersebut.",
  "ww_BEL_event_war.6.a": "Prakarsa yang bagus, bekerja samalah dengan mereka demi memastikan pendudukan yang lancar.",
  "ww_BEL_event_war.6.b": "Gagasan yang menarik, kita akan mempertimbangkan tawaran mereka.",
  "ww_BEL_event_war.6.c": "Ini hanyalah kedok bagi perlawanan yang terorganisir. Tolak.",
  "BEL_set_secretaries_general_tt": "§YSekretaris Jenderal§! akan diberlakukan sebagai §YHukum Pendudukan§! di seluruh Belgia",
  "BEL_available_secretaries_general_tt": "§YSekretaris Jenderal§! kini tersedia sebagai §YHukum Pendudukan§! di Belgia",
  "BEL_no_secretaries_general_tt": "§YSekretaris Jenderal§! akan dihapus sebagai §YHukum Pendudukan§! di Belgia",
  "BEL_remove_secretaries_general_civs_tt": "Hilangkan 2 §YPabrik Sipil Luar Peta§!",
  "ww_BEL_event_war.7.t": "Potensi Perang Terbatas - Paris Harus Jatuh!",
  "ww_BEL_event_war.7.desc": "Para diplomat dan jenderal terkemuka kita baru-baru ini bertemu, dan memberi masukan bahwa jika konflik ini tetap berskala terbatas, yaitu tanpa campur tangan kekuatan-kekuatan besar lainnya, maka kita mungkin dapat membawa [FRA.GetName] ke meja perundingan dan mengamankan perjanjian damai yang cepat. Kita tahu bahwa mereka gentar akan meningkatnya ketegangan, dan sebagaimana kita, mereka tidak ingin terseret ke dalam kancah perang global lainnya. \n\nOleh sebab itu, perhitungan kita menyatakan bahwa apabila Paris jatuh, peristiwa itu akan menjadi unjuk keperkasaan yang cukup guna membuat mereka bersedia merundingkan penyerahan Calais yang disengketakan.",
  "ww_BEL_event_war.7.a": "Pasukan kita akan berderap melintasi jalanan Paris tak lama lagi!",
  "ww_BEL_event_war.8.t": "Paris Telah Jatuh!",
  "ww_BEL_event_war.8.desc": "Dalam sebuah malapetaka nasional, ibu kota kebanggaan kita, Paris, telah jatuh! Sekali lagi, angkatan bersenjata kita terbukti tidak memadai dalam menghadapi musuh yang secara militer seharusnya lebih lemah. Pihak [FROM.GetAdjective] telah menawarkan penarikan mundur pasukannya dan membiarkan bagian lain negara kita tetap utuh, namun sebagai imbalannya, mereka menuntut kita menyerahkan Calais kepada mereka. \n\nKita sudah dapat merasakan burung-burung nasar mulai berputar mengintai, dan perdamaian ini akan memberi kita waktu untuk memetik pelajaran berharga serta bersiap menghadapi musuh-musuh potensial yang jauh lebih besar kelak.",
  "ww_BEL_event_war.8.a": "Tawarkan Calais demi perdamaian.",
  "ww_BEL_event_war.8.b": "Terus bertempur! Peperangan ini belum usai.",
  "ww_BEL_event_war.9.t": "Prancis Menyetujui Perdamaian",
  "ww_BEL_event_war.9.desc": "Hari ini, kita menerima kedatangan delegasi Prancis yang datang merundingkan penyelesaian damai atas konflik yang tengah berlangsung menyusul jatuhnya ibu kota mereka. Setelah melalui musyawarah panjang, mereka akhirnya bersepakat menawarkan Calais kepada kita sebagai imbalan atas penghentian permusuhan seketika. \n\nPerlu diingat bahwa ini adalah tawaran satu kali, dan jika kita menolaknya, pertahanan mereka akan menjadi jauh lebih gigih serta kecil kemungkinan mereka akan menawarkannya kembali.",
  "ww_BEL_event_war.9.a": "Kita terima! Calais demi perdamaian.",
  "ww_BEL_event_war.9.b": "Terus bertempur! Kita sanggup merebut lebih banyak lagi.",
  "ww_BEL_event_war.10.t": "Paris di Bawah Kendali [ROOT.GetAdjective]",
  "ww_BEL_event_war.10.desc": "Sasaran-sasaran yang digariskan di hadapan kita dalam pembahasan pada hari-hari awal perang melawan bangsa [FRA.GetAdjective] kini telah tercapai. Paris kini berada di bawah kendali kita, dan dengan demikian, orang dapat berasumsi bahwa pihak [FRA.GetAdjective] kini cukup tertekan sehingga tawaran penarikan mundur pasukan kita sebagai imbalan penyerahan Calais akan disambut dengan persetujuan kendati dengan berat hati.\n\nPada saat yang sama, desakan mulai bergema kencang: kita telah melangkah sejauh ini, dan bangsa [FRA.GetAdjective] secara nyata terbukti tak berdaya membendung kita. Mengapa kita harus berhenti sekarang?",
  "ww_BEL_event_war.10.a": "Kita telah memperoleh apa yang kita tuju, ajukan perundingan damai!",
  "ww_BEL_event_war.10.b": "Kita menghendaki semuanya!",
  "ww_BEL_event_spanish_interaction.1.t": "[FROM.GetNameDefCap] Mengirim Perlengkapan",
  "ww_BEL_event_spanish_interaction.1.desc": "Kita telah menerima pengiriman senapan dari pemerintah [FROM.GetAdjective]. Mereka memiliki pandangan yang sama bahwa kaum nasionalis wajib dihentikan, dan berhasrat menyokong perjuangan kita, bukan sekadar lewat kata-kata belaka.",
  "ww_BEL_event_spanish_interaction.1.a": "Kita akan memanfaatkannya dengan sebaik-baiknya!",
  "ww_BEL_event_spanish_interaction.2.t": "Pengiriman Perlengkapan Lanjutan kepada Kaum Republikan [SPR.GetAdjective]",
  "ww_BEL_event_spanish_interaction.2.desc": "Pengiriman perlengkapan kita sebelumnya kepada bangsa [SPR.GetAdjective] telah terbukti amat berharga bagi sahabat-sahabat Republikan kita. Kendati demikian, perjuangan mereka masih jauh dari usai dan kita seharusnya sanggup memasok lebih banyak peralatan kepada mereka.",
  "ww_BEL_event_spanish_interaction.2.a": "Kirim lebih banyak senapan!",
  "ww_BEL_event_spanish_interaction.2.b": "Mereka membutuhkan sejumlah Perlengkapan Pendukung!",
  "ww_BEL_event_spanish_interaction.2.c": "Kirimkan artileri kepada mereka!",
  "ww_BEL_event_spanish_interaction.3.t": "[FROM.GetNameDefCap] Mengirimkan Pasokan Perlengkapan Tambahan",
  "ww_BEL_event_spanish_interaction.3.desc": "Kita telah menerima pengiriman tambahan perlengkapan [FROM.GetAdjective]. Bantuan mereka akan terbukti amat berharga dalam memukul mundur malapetaka kaum nasionalis yang memporak-porandakan tanah air kita.",
  "ww_BEL_event_spanish_interaction.3.a": "Luar biasa!",
  "ww_BEL_event_spanish_interaction.4.t": "Pidato [FROM.GetAdjective] Menyokong Perjuangan Kita",
  "ww_BEL_event_spanish_interaction.4.desc": "Kita telah diberi warta bahwa beberapa jam lalu sebuah rapat akbar dan pidato digelar demi mendukung kita di [FROM.GetNameDef]. Kepemimpinan [FROM.GetAdjective] sekali lagi menegaskan dukungan teguh mereka bagi kita, dengan harapan langkah ini akan memberi kita ruang gerak lebih leluasa seiring rakyat yang semakin menaruh kepercayaan kepada kita.",
  "ww_BEL_event_spanish_interaction.4.a": "Sampaikan rasa terima kasih kita kepada bangsa [FROM.GetAdjective]!",
  "ww_BEL_event_spanish_interaction.5.t": "Pemberian Dorongan bagi Emigrasi [FROM.GetAdjective]",
  "ww_BEL_event_spanish_interaction.5.desc": "Belakangan ini kita menyaksikan lonjakan imigrasi dari warga negara [FROM.GetAdjective]. Banyak dari kalangan pendatang ini menyatakan kesediaan untuk bergabung ke dalam angkatan bersenjata kita bilamana kita membutuhkan tenaga mereka. Tak diragukan lagi bahwa ini merupakan ikhtiar yang terencana dengan matang dari pihak [FROM.GetAdjective].",
  "ww_BEL_event_spanish_interaction.5.a": "Kabar luar biasa!",
  "ww_BEL_event_spanish_interaction.6.t": "[FROM.GetNameDefCap] Mengajukan Aliansi",
  "ww_BEL_event_spanish_interaction.6.desc": "Bangsa [FROM.GetAdjective] yang sebelumnya bersikukuh netral kini mengirimkan sebuah tawaran mengejutkan kepada kita. Mereka berhasrat menggalang aliansi militer dengan kita. Mereka berharap langkah ini memungkinkan pemberian sokongan yang lebih optimal bagi perjuangan kita dalam melawan kaum nasionalis.",
  "ww_BEL_event_spanish_interaction.6.a": "Gagasan yang sangat cemerlang!",
  "ww_BEL_event_spanish_interaction.6.b": "Kita menghargai dukungan mereka, namun terpaksa menolaknya.",
  "ww_BEL_event_spanish_interaction.7.t": "[FROM.GetNameDef] Bergabung dengan [ROOT.GetFactionName]",
  "ww_BEL_event_spanish_interaction.7.desc": "Pihak [FROM.GetAdjective] telah mengembalikan jawaban positif atas proposal kita untuk mendirikan [ROOT.GetFactionName]. Kita akan berdiri teguh bersama-sama menghadapi ancaman kaum nasionalis!",
  "ww_BEL_event_spanish_interaction.7.a": "Maju terus!",
  "ww_BEL_event_spanish_interaction.8.t": "[FROM.GetNameDefCap] Menolak Usulan Aliansi Kita",
  "ww_BEL_event_spanish_interaction.8.desc": "Menimbang dukungan nyata yang tiada henti kita curahkan kepada pihak [FROM.GetAdjective], kita semula menaruh harapan besar bahwa proposal kita akan disambut secara positif. Namun kenyataan berbicara lain; mereka menolak usulan kita, seraya menyatakan bahwa bantuan kita disambut baik, namun mereka tidak menghendaki adanya ikatan aliansi formal.",
  "ww_BEL_event_spanish_interaction.8.a": "Sungguh tidak tahu terima kasih!",
  "ww_BEL_event_spanish_interaction.9.t": "[FROM.GetNameDefCap] Membubarkan $BEL_SPR_alliance$",
  "ww_BEL_event_spanish_interaction.9.desc": "Seiring tuntasnya Perang Saudara kita, pihak [FROM.GetAdjective] telah menetapkan bahwa sudah tiba saatnya kemitraan kita disudahi. Kendati langkah ini mengakhiri aliansi kita untuk saat ini, mereka sangat bersikeras bahwa ini bukan berarti kita tak akan pernah bersekutu kembali di masa depan.",
  "ww_BEL_event_spanish_interaction.9.a": "Sungguh disayangkan",
  "ww_BEL_event_misc.1.t": "Sang Bos Telah Tiada",
  "ww_BEL_event_misc.1.desc": "Émile Vandervelde, yang berjuluk 'le patron' (sang bos), politisi Sosialis kawakan sekaligus Perdana Menteri [BEL.GetName], telah mengembuskan napas terakhirnya. Beliau termasyhur sebagai anggota delegasi Belgia di Konferensi Perdamaian Paris yang memungkasi Perang Besar, serta penentang gigih Fasisme yang bahkan memperjuangkan intervensi langsung membela kaum Republikan dalam Perang Saudara Spanyol. \n\nHenri de Man telah mengambil alih tampuk kepemimpinan sebagai Perdana Menteri baru, dan akan disumpah oleh Raja pada sore hari ini.",
  "ww_BEL_event_misc.1.a": "Penerusnya adalah orang yang tepat untuk menuntaskan pekerjaan ini!",
  "ww_BEL_event_misc.3.t": "Cockerill: Jantung Manufaktur Belgia",
  "ww_BEL_event_misc.3.desc": "Cockerill adalah perusahaan raksasa yang berdiri kokoh di jantung industri manufaktur Belgia. Sepanjang sejarahnya, perusahaan ini tidak hanya memproduksi besi dan baja bermutu tinggi, melainkan juga mesin-mesin rekayasa presisi termasuk mesin uap, kereta api, hingga kapal tempur perang. Reputasinya yang gilang-gemilang mengantarkannya menjadi kekuatan utama industri baja di seantero Eropa Barat. \n\nDirektur Utama Adolphe Greiner beserta jajaran manajemen lainnya memilih tetap bertahan di pos mereka selama Pengepungan Liège semasa Perang Besar, demi memastikan lapangan kerja tetap terbuka bagi para buruhnya selama mungkin. Saat wilayahnya diduduki, perusahaan tersebut menolak mentah-mentah berproduksi bagi pasukan penjajah, dan akibatnya sebagian besar peralatan berat pengerjaan bajanya dijarah habis. \n\nPerusahaan ini telah bangkit kembali selama masa antarperang dan tetap menjadi pilar terdepan industri nasional kita.",
  "ww_BEL_event_misc.3.a": "Merekalah yang sesungguhnya membangun roda penggerak ekonomi kita!",
  "ww_congo.1.t": "Belgia Berinvestasi dalam Pembangunan Kita",
  "ww_congo.1.desc": "Kantor kolonial Belgia hari ini meloloskan undang-undang untuk mengalokasikan sumber daya dalam jumlah yang jauh lebih masif bagi pembangunan industri kita, dan telah memulai pembangunan fasilitas-fasilitas industri di [295.GetName].",
  "ww_congo.1.a": "Sebuah anugerah yang luar biasa",
  "ww_congo.4.t": "Raoul van Overstraeten Kembali ke Belgia",
  "ww_congo.4.desc": "Perwira militer Belgia Raoul van Overstraeten, yang bertugas di negeri kita hingga belum lama ini, kini dengan tersiarnya kabar kemerdekaan kita yang baru, memutuskan untuk pulang kembali ke daratan Eropa. Kita tidak lagi membutuhkan orang-orang Eropa semacam dirinya, dan kepergiannya niscaya hanya akan membuat kita bertambah perkasa.",
  "ww_congo.4.a": "Enyahlah, hai Kaum Imperialis!",
  "ww_congo.5.t": "[COG.GetLeader] Ingin Meningkatkan Produksi Pangan di Kongo",
  "ww_congo.5.desc": "Gubernur kita di Kongo, [COG.GetLeader], telah mengutarakan keinginannya untuk mendongkrak produksi pangan dengan mengurangi kapasitas tambang sebagai bagian dari ikhtiarnya guna 'memperbaiki kondisi sosial penduduk kolonial'. Langkah ini niscaya akan merugikan profitabilitas koloni untuk saat ini, namun hampir dapat dipastikan akan mendatangkan keuntungan berlipat ganda dalam jangka panjang.",
  "ww_congo.5.a": "Hal itu akan menggerus keuntungan!",
  "ww_congo.5.b": "Jika ia menganggap itu yang terbaik...",
  "CONGO_refused_increased_food_production": "Tuan kolonial kita menolak Rencana Peningkatan Produksi Pangan kita",
  "CONGO_accepted_increased_food_production": "Tuan kolonial kita menyetujui Rencana Peningkatan Produksi Pangan kita",
  "ww_congo.6.t": "Pihak [BEL.GetAdjective] Menolak Rencana Produksi Pangan Kita",
  "ww_congo.6.desc": "Administrasi kolonial di [BEL.GetNameDef] telah menampik permohonan kita untuk mendongkrak produksi pangan melalui pengurangan hasil tambang demi 'memperbaiki kondisi sosial penduduk kolonial'.",
  "ww_congo.6.a": "Sudah dapat diduga sebelumnya",
  "ww_congo.7.t": "Pihak [BEL.GetAdjective] Menyetujui Rencana Produksi Pangan Kita",
  "ww_congo.7.desc": "Administrasi kolonial di [BEL.GetNameDef] telah menyetujui permohonan kita untuk meningkatkan produksi pangan dengan mengurangi kapasitas tambang demi 'memperbaiki kondisi sosial penduduk kolonial'.",
  "ww_congo.7.a": "Bagus sekali!",
  "ww_congo.8.t": "Munculnya Kelas Menengah Baru",
  "ww_congo.8.desc": "Terdapat segmen penduduk Kongo yang kian membesar dengan penguasaan bahasa Prancis yang fasih, memeluk agama Kristen, serta mengenyam pendidikan pascasekolah dasar. Para pejabat kolonial mulai menyebut mereka sebagai Évolué, kaum yang telah tereropanisasi. Kendati mobilitas sosial mereka masih dibatasi oleh hierarki kolonial, populasi yang kian berpendidikan ini niscaya akan menjadi tumpuan kemakmuran bangsa kita suatu hari nanti.",
  "ww_congo.8.a": "Kita akan mencermati perkembangannya lebih lanjut",
  "evolue_will_start_attempting_to_enter_politics_tt": "Kaum Évolué akan mulai berupaya terjun ke panggung politik, yang akan membuka peluang hadirnya berbagai §YPenasihat Politik§! baru",
  "evolue_have_entered_politics": "Berbagai §YTokoh Perjuangan Kemerdekaan§! dan §YPemikir Politik Kongo§! kini akan tersedia sebagai §YPenasihat Politik§!",
  "ww_congo.9.t": "Kaum Évolué Mulai Memasuki Panggung Politik [ROOT.GetAdjective]",
  "ww_congo.9.desc": "Dengan bertumbuhnya kelas menengah belakangan ini serta banyaknya warga di perkotaan yang mengenyam pendidikan lanjutan, banyak kaum [COG.GetAdjective] mulai mendalami risalah-risalah para pemikir politik kenamaan, dan sekumpulan tokoh politik serta pejuang kemerdekaan baru mulai bermunculan. Ini menandai fajar baru bagi bangsa [COG.GetAdjective]!",
  "ww_congo.9.a": "Orang-orang ini niscaya akan memimpin bangsa kita menuju kemerdekaan",
  "ww_congo.10.t": "[FROM.GetNameDefCap] Menuntut [772.GetName]",
  "ww_congo.10.d": "Pasukan Kongo telah bersiaga di sepanjang garis perbatasan koloni kita di [772.GetName], dan mereka menuntut akses penuh tanpa batas ke pangkalan dan instalasi militer kita! Bilamana kita menyepakati tuntutan mereka, secara de facto kita telah menyerahkan kendali atas [772.GetName] ke tangan mereka. Di sisi lain, kita tidak memiliki sarana yang memadai untuk melawan mereka dalam sengketa ini.",
  "ww_congo.10.a": "Kita tidak memiliki pilihan lain selain tunduk.",
  "ww_congo.10.b": "Tidak akan pernah!",
  "ww_congo.11.t": "Pihak Prancis Menerima Tuntutan Kita",
  "ww_congo.11.d": "Pihak Prancis telah bertekuk lutut menerima tuntutan kita, dan pangkalan beserta instalasi mereka di [772.GetName] kini sepenuhnya berada di bawah kendali kita. Secara efektif mereka telah menyerahkan kendali mutlak koloni mereka kepada kita.",
  "ww_congo.11.a": "Langkah yang sangat bijaksana.",
  "ww_congo.12.t": "Pihak Prancis Menolak Tuntutan Kita",
  "ww_congo.12.d": "Pihak Prancis secara keterlaluan telah menampik tuntutan kita! Tampaknya bilamana kita menghendaki [772.GetName], kita harus merebutnya dengan kekuatan senjata!",
  "ww_congo.12.a": "Orang-orang pandir!",
  "ww_congo.13.t": "[FROM.GetNameDefCap] Menuntut Integrasi Kita",
  "ww_congo.13.d": "Kekuatan militer Kongo telah bersiap di perbatasan kita, dan mereka menuntut kendali penuh atas pangkalan, institusi, serta instalasi kita! Jika kita menyetujui permintaan mereka, kita secara efektif mengakhiri kemerdekaan kita dan melebur menjadi bagian dari bangsa mereka. Namun di sisi lain, kita sama sekali tidak memiliki sarana untuk melawan mereka dalam perkara ini.",
  "ww_congo.13.a": "Kita akan bertambah kuat bersama-sama!",
  "ww_congo.13.b": "Tidak akan pernah!",
  "ww_congo.14.t": "[FROM.GetNameDefCap] Menerima Tuntutan Kita",
  "ww_congo.14.d": "[FROM.GetNameDefCap] telah menyetujui tuntutan kita, dan negara mereka akan lenyap sebagai entitas berdaulat dalam beberapa hari ke depan. Mereka secara efektif telah menyerahkan kendali penuh atas negeri mereka ke tangan kita.",
  "ww_congo.14.a": "Langkah yang sangat bijaksana.",
  "ww_congo.15.t": "[FROM.GetNameDefCap] Menolak Tuntutan Kita",
  "ww_congo.15.d": "[FROM.GetNameDefCap] secara lancang menolak tuntutan kita! Tampaknya bilamana kita menghendaki [772.GetName], kita terpaksa merebutnya melalui kekuatan perang!",
  "ww_congo.15.a": "Orang-orang pandir!",
  "ww_congo.16.t": "Afrika Latin Bersatu",
  "ww_congo.16.d": "Menanggapi memuncaknya ketegangan global, serta berkat kejayaan gemilang [FROM.GetLeader] baru-baru ini, penyatuan negara-negara Afrika Tengah penutur bahasa Roman akhirnya berhasil diwujudkan. Kini, mereka mendeklarasikan diri sebagai kekuatan dunia baru, dan berikrar melindungi segenap rakyat [FROM.GetAdjective], berapapun harganya.",
  "ww_congo.16.a": "Mereka pasti akan binasa",
  "ww_congo.16.b": "Hiduplah [ROOT.GetNameDef]!",
  "ww_congo.17.t": "Kemerdekaan Kongo Berhasil Diraih",
  "ww_congo.17.d": "Menyusul persetujuan dari otoritas [BEL.GetAdjective] di negeri ini, Perdana Menteri baru [COG.GetAdjective] Patrice Lumumba menyampaikan pidato singkat demi merayakan kemerdekaan baru tanah airnya. Di dalamnya termuat kecaman pedas terhadap kolonialisme, serta apa yang kerap didengungkan sebagai \"misi pembudayaan [BEL.GetAdjective]\". Kendati pidato ini disambut gegap gempita di dalam negeri, banyak kalangan luar negeri menilainya sebagai serangan personal langsung terhadap Kepala Negara [BEL.GetAdjective]. Era dekolonisasi baru saja menyingsing!",
  "ww_congo.17.a": "Keseimbangan Kekuatan di Afrika telah bergeser",
  "ww_congo.17.b": "Sudah saatnya membuktikan bahwa kita adalah dua bangsa merdeka yang setara",
  "ww_congo.17.c": "Mungkin ini memang jalan yang terbaik...",
  "ww_congo.18.t": "Pemberontakan Kongo Berhasil Ditumpas",
  "ww_congo.18.d": "Belum lama ini, pemerintah Kongo Merdeka di Stanleyville berupaya memisahkan diri dari imperium kolonial Belgia. Kendati sempat menuai dukungan besar di dalam negeri, pemberontakan mereka berhasil ditumpas tanpa ampun oleh pasukan yang setia kepada Belgia beserta serdadu bayaran asing.",
  "ww_congo.18.a": "Zaman Imperialisme belum lagi berakhir",
  "ww_congo.18.b": "Para pengkhianat itu menuai apa yang layak mereka dapatkan",
  "ww_congo.18.c": "Persatuan melahirkan kekuatan",
  "ww_congo.19.t": "Pemberontakan Kongo Menuai Kemenangan",
  "ww_congo.19.d": "Belum lama berselang, pemerintah Kongo Merdeka di Stanleyville mengobarkan perang kemerdekaan melawan imperium kolonial Belgia. Kendati memakan waktu berliku, pemberontakan mereka akhirnya sanggup menggulung pasukan kolonial yang ditempatkan di kawasan tersebut dan merebut kota-kota kunci di seantero Kongo. Kini, mereka secara resmi memproklamasikan kemerdekaan, dan kesepakatan damai tengah diupayakan antara mereka dan bekas penindas mereka..",
  "ww_congo.19.a": "Zaman Imperialisme telah tamat",
  "ww_congo.19.b": "Kemenangan adalah milik kita!",
  "ww_congo.19.c": "Pukulan telak yang membinasakan...",
  "ww_congo.20.t": "Revolusi Rwanda",
  "ww_congo.20.d": "Dengan cengkeraman kekuasaan pemerintah kita yang kian rapuh atas mandat Ruanda-Urundi serta merebaknya gelombang sentimen nasionalis di seantero kawasan, Mwami Mutara III Rudahigwa, Raja Rwanda, telah mendeklarasikan bangsanya sebagai negara merdeka, sekaligus memutus ikatan dengan pemerintah pusat kita. Haruskah kita melancarkan intervensi militer?",
  "ww_congo.20.a": "Bukan hak kita untuk menghalangi mereka",
  "ww_congo.20.b": "Siapa yang mengizinkan mereka untuk merdeka?",
  "ww_congo.21.t": "Deklarasi Mwambutsa",
  "ww_congo.21.d": "Dengan cengkeraman kekuasaan pemerintah kita yang kian melemah atas mandat Ruanda-Urundi serta berkobarnya sentimen nasionalisme di seantero wilayah, Mwami Mwambutsa IV, Raja Burundi, telah memproklamasikan bangsanya sebagai negara yang berdaulat, memutus tali hubungan dengan pemerintah pusat kita. Haruskah kita mengambil tindakan?",
  "ww_congo.21.a": "Bukan tempat kita untuk menghalangi mereka",
  "ww_congo.21.b": "Siapa yang memberi mereka hak untuk merdeka?",
  "threatened_us_opinion_modifier": "Mereka mengancam kita!",
  "attempted_diplomacy_opinion_modifier": "Mereka berupaya mendekati kita melalui jalur diplomasi",
  "BEL_commonwealth_faction": "Persemakmuran Belgia",
  "ww_congo.22.t": "[COG.GetLeader] Meminta Peningkatan Emigrasi ke Kongo",
  "ww_congo.22.desc": "Gubernur kita di Kongo, [COG.GetLeader], telah menyampaikan permohonan agar memacu imigrasi bangsa [ROOT.GetAdjective] ke wilayah tersebut, demi mendatangkan kaum terpelajar dan pemilik modal. Tanah Katanga yang subur, hangat, dan kaya raya akan sangat memikat banyak insan yang berjiwa petualang maupun berdedikasi, dan jika kita mendorong hal ini, niscaya akan menarik lebih banyak orang untuk berpindah..",
  "ww_congo.22.a": "Kita akan memenuhinya",
  "ww_congo.22.b": "Ia pikir siapa dirinya?",
  "ww_congo.23.t": "Pihak [FROM.GetAdjective] Menyetujui Rencana Imigrasi Kita"
}

def validate_and_save():
    with open('scripts/chunks/chunk_6.json', 'r', encoding='utf-8') as f:
        c6_source = json.load(f)
        
    print(f"Source count: {len(c6_source)}")
    print(f"Trans count: {len(c6_trans)}")
    assert len(c6_source) == len(c6_trans), f"Count mismatch: {len(c6_source)} vs {len(c6_trans)}"
    
    tag_errors = 0
    ordered = {}
    for item in c6_source:
        k = item['key']
        en_val = item['en']
        assert k in c6_trans, f"Missing key: {k}"
        id_val = c6_trans[k]
        
        # Check brackets
        en_b = set(re.findall(r'\[.*?\]', en_val))
        id_b = set(re.findall(r'\[.*?\]', id_val))
        if en_b != id_b:
            print(f"Bracket error in {k}:")
            print(f"  EN: {en_b}")
            print(f"  ID: {id_b}")
            tag_errors += 1
            
        # Check dollars
        en_d = set(re.findall(r'\$[A-Za-z0-9_]+\$', en_val))
        id_d = set(re.findall(r'\$[A-Za-z0-9_]+\$', id_val))
        if en_d != id_d:
            print(f"Dollar error in {k}:")
            print(f"  EN: {en_d}")
            print(f"  ID: {id_d}")
            tag_errors += 1
            
        # Check section colors
        en_s = set(re.findall(r'§[A-Za-z!]', en_val))
        id_s = set(re.findall(r'§[A-Za-z!]', id_val))
        if en_s != id_s:
            print(f"Section color error in {k}:")
            print(f"  EN: {en_s}")
            print(f"  ID: {id_s}")
            tag_errors += 1
            
        ordered[k] = id_val
        
    if tag_errors > 0:
        raise ValueError(f"{tag_errors} tag errors found!")
        
    out_path = 'scripts/chunks/trans_chunk_6.json'
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(ordered, f, ensure_ascii=False, indent=2)
        
    print(f"SUCCESS: Saved {out_path} with {len(ordered)} items.")

if __name__ == '__main__':
    validate_and_save()
