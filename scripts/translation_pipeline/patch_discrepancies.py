# -*- coding: utf-8 -*-
import json
import os
import re

fixes = {
    # Chunk 0
    "AUS_political_events.14.desc": "Tekanan kita terhadap [FROM.GetNameDef] telah membuahkan hasil, dan Arthur Seyss-Inquart telah diangkat sebagai penasihat. Kendati kesetiaannya sempat dipertanyakan belakangan ini, ia jauh lebih bersimpati kepada partai kita dibanding kaum [FROM.GetAdjective].\\n\\nKini, [FROM.GetNameDefCap] seharusnya akan jauh lebih patuh terhadap permintaan kita.",
    "AUS_political_events.14.a": "Pihak [FROM.GetAdjective] tunduk pada tuntutan kita",
    "AUS_political_events.15.desc": "Kabar baru saja sampai kepada kita bahwa pemerintah [FROM.GetAdjective] telah memberlakukan pelarangan terhadap DNSAP di [FROM.GetNameDef]. Larangan lunak sebenarnya telah ada sejak tahun 1934, meski larangan tersebut sebagian besar diabaikan oleh partai-partai politik maupun pemerintah. Hal ini menandakan perubahan sikap dari kepemimpinan [FROM.GetAdjective] terhadap kita.\\n\\nDi luar penghinaan terang-terangan ini, tindakan tersebut juga dapat menghambat pengaruh kita atas [FROM.GetNameDef].",
    "AUS_political_events.16.desc": "Seperti yang telah diduga, [FROM.GetNameDef] bereaksi sangat keras terhadap pelarangan DNSAP baru-baru ini. Selain tuntutan nyata agar kita segera mencabut larangan tersebut, mereka juga menuntut agar kita mengangkat Arthur Seyss-Inquart sebagai penasihat. Mereka sangat bersikeras mengenai hal ini, dan walau kita selalu tahu bahwa ia sangat menyukai cara hidup [FROM.GetAdjective], hal ini tetap menimbulkan tanda tanya besar: mengapa?",
    "AUS_political_events.17.t": "[FROM.GetNameDefCap] Memprotes Pelarangan DNSAP Kita",
    "AUS_political_events.17.desc": "Seperti yang telah diduga, [FROM.GetNameDef] bereaksi sangat buruk terhadap pelarangan DNSAP oleh kita. Mereka menganggap ini sebagai serangan langsung terhadap ideologi mereka sendiri dan menyuarakan kekecewaan serta kemarahan besar atas keputusan kita. Kendati kita memiliki alasan kuat untuk melarang DNSAP, kepemimpinan [FROM.GetAdjective] kini menuntut agar kita segera mencabut larangan tersebut.",
    "AUS_political_events.18.t": "[FROM.GetNameDefCap] Mengangkat Arthur Seyss-Inquart sebagai Penasihat",
    "AUS_political_events.18.desc": "Tampaknya kaum [FROM.GetAdjective] akhirnya dapat diajak bernalar sehat. Larangan terhadap partai saudari kita di [FROM.GetNameDef] memang masih berlaku, namun setidaknya mereka telah mengangkat Arthur Seyss-Inquart sebagai penasihat, memberikan kita wawasan berharga tentang manuver politik mereka.",

    # Chunk 1
    "AUS_seeks_a_deal_desc_57": "Jawaban dari pihak [FROM.GetADjective] telah sampai kepada kita; mereka menolak kesepakatan tersebut. Menegaskan bahwa tanah air mereka tidak untuk diperjualbelikan, mereka dengan tegas menolak segala kemungkinan penjualan ataupun kesepakatan apa pun terkait wilayah yang bersangkutan.",
    "AUS_political_events.58.t": "[FROM.GetNameDefCap] Menuntut Kepemilikan atas [39.GetName] dan [850.GetName]",
    "AUS_political_events.58.desc": "[FROM.GetNameDefCap] telah menghubungi kita dengan apa yang tampak seperti sebuah ancaman terselubung. Tanpa kata-kata manis, mereka memberi tahu kita bahwa mereka menginginkan kepemilikan atas [39.GetName] dan [850.GetName] yang mereka klaim sebagai hak mereka. Wilayah-wilayah tersebut dulunya merupakan bagian dari jantung negeri [FROM.GetAdjective], namun sejak Perang Besar telah menjadi milik kita.",
    "AUS_political_events.59.t": "[FROM.GetNameDefCap] Mendukung Rencana Alfred Jansa",
    "AUS_political_events.59.desc": "Pemerintah [FROM.GetNameDef] sekali lagi menaruh kepercayaan mereka kepada Alfred Jansa, seorang marsekal lapangan dengan sentimen yang jelas-jelas anti-[ROOT.GetAdjective]. Dengan rancangan memperkuat perbatasan dan rencana pertahanan yang dirancang khusus untuk memukul balik serangan dari kita, marsekal ini telah menjadi duri dalam daging bagi kita sebelumnya dan kemungkinan besar akan menjadi ancaman serupa lagi.",
    "AUS_political_events.60.t": "[FROM.GetNameDefCap] Keberatan atas Rencana Pertahanan Alfred Jansa",
    "AUS_political_events.60.desc": "Sebuah nota keberatan resmi dari [FROM.GetNameDef] terkait komitmen kita belakangan ini terhadap rencana pertahanan yang digagas Alfred Jansa telah dilayangkan. Mereka mengklaim bahwa tindakan ini jelas-jelas diambil atas dasar permusuhan terhadap mereka dan akan merintangi hubungan diplomatik kita di masa depan. Kita sendiri tidak yakin mengapa hal ini memicu reaksi yang sedemikian sengit.",
    "AUS_political_events.61.desc": "Tekanan kita agar pihak [FROM.GetAdjective] segera mengganti Alfred Jansa beserta rencana pertahanannya yang gegabah telah membuahkan hasil. Sebagai pengganti Jansa yang sangat anti-[ROOT.GetAdjective], kaum [FROM.GetAdjective] kini menunjuk Franz Böhme yang jauh lebih kompromistis.",
    "AUS_political_events.75.desc": "Bagaimanapun upaya kita, para penjamin tetap bergeming. Kita tidak diizinkan untuk mempersenjatai diri kembali dalam keadaan apa pun. Usaha diplomatik kita untuk meyakinkan mereka dan menawarkan kompromi telah menemui jalan buntu. Rakyat [ROOT.GetAdjective] kini menyimpan kebencian mendalam terhadap para Penjamin tersebut.",

    # Chunk 2
    "AUS_GER_cannot_take_a_no": "Kendati tekanan terus berlanjut dan kian meningkat terhadap [FROM.GetNameDef], [FROM.GetLeader] tetap teguh mempertahankan sikap [FROM.GetLeader.GetHerHis]. Arthur Seyss-Inquart tidak akan diizinkan masuk sebagai penasihat dalam pemerintahan, apa pun yang kita katakan atau lakukan. Kita harus mencari jalan lain; ini hanyalah rintangan kecil belaka.",
    "AUS_political_events.102.desc": "Dalam sebuah konferensi yang baru-baru ini diselenggarakan oleh [ROOT.GetLeader], sang Führer memaparkan sebagian ambisinya bagi ekspansi masa depan [ROOT.GetNameDef]. Langkah ekspansi pertama tersebut dipandang oleh [ROOT.GetLeader.GetSheHe] mengandung risiko yang sangat kecil. Rakyat [AUS.GetAdjective] tiada bedanya dengan bangsa kita, dan mereka sebagian besar menganut pandangan serupa, sebagaimana terbukti dari iklim politik di negeri tersebut. Sang Führer meyakini bahwa ekspansi semacam itu akan dapat dicapai melalui jalur diplomasi, asalkan diberikan waktu yang cukup bagi bertumbuhnya sentimen ramah [ROOT.GetAdjective] di dalam [AUS.GetNameDef].",
    "AUS_political_events.105.desc": "Menyusul agresi belakangan ini dari [GER.GetNameDef], kita mulai mencari bantuan dari luar. Pihak [ITA.GetAdjective] di masa lalu tampak bersedia mendukung kita apabila kaum [GER.GetAdjective] mengambil tindakan militer terhadap kita. Mungkin kini saatnya kita menagih janji tersebut dan memohon bantuan mereka demi pertahanan kita.",
    "AUS_political_events.106.t": "[FROM.GetNameDefCap] Menjamin Kemerdekaan Kita",
    "AUS_political_events.106.desc": "Mengingat permusuhan baru-baru ini dari [GER.GetNameDef], pihak [ITA.GetAdjective] telah menghubungi kita untuk menegaskan kembali dukungan mereka. Terlepas dari segala ancaman yang ada, mereka akan menjamin kemerdekaan kita, dan bilamana pecah konflik bersenjata, mereka akan bertempur bahu-membahu di sisi kita.",
    "AUS_political_events.106.a": "Kaum [GER.GetAdjective] akan menyesali perbuatan mereka!",
    "AUS_political_events.107.t": "[FROM.GetNameDefCap] Tunduk pada Tekanan [GER.GetAdjective]",
    "AUS_political_events.107.desc": "Kabar memilukan telah sampai kepada kita bahwa [FROM.GetLeader] telah menyerah pada tuntutan [GER.GetAdjective] untuk integrasi ke dalam [GER.GetNameDef]. Kendati kita telah menawarkan jaminan kepada kaum [FROM.GetAdjective], tampaknya janji tersebut tidak cukup untuk membakar keberanian mereka melawan. Kita tetap memiliki kepentingan vital di kawasan ini, sehingga di masa depan, kita patut mempertimbangkan pembebasan kembali rakyat [FROM.GetAdjective].",
    "AUS_political_events.108.t": "[FROM.GetNameDefCap] Menggelar Latihan Militer di Perbatasan Kita",
    "AUS_political_events.108.desc": "Telah menjadi perhatian kita bahwa Angkatan Darat [FROM.GetAdjective] telah memulai latihan militer berskala cukup besar tepat di garis perbatasan kita. Kendati tiada ancaman lisan yang diucapkan secara terbuka, kita tidak dapat menepis firasat bahwa ini adalah semacam peringatan atas apa yang bakal terjadi. Kita harus sangat berhati-hati dalam setiap tindakan kita terhadap mereka, agar tidak memancing agresi yang lebih beringas.",
    "AUS_political_events.109.t": "[FROM.GetNameDefCap] Mempersenjatai Penjaga Perbatasan",
    "AUS_political_events.109.desc": "Belakangan ini patroli perbatasan kita melaporkan peningkatan signifikan jumlah patroli dan pos penjagaan di sisi perbatasan [FROM.GetAdjective]. Yang kian mencemaskan, para penjaga ini tidak lagi bersenjata ringan, melainkan menyandang senapan tempur yang setara dengan perlengkapan angkatan darat reguler. Apabila pernyataan-pernyataan mereka sebelumnya menjadi tolok ukur, ini merupakan sinyal bahaya yang patut diwaspadai.",
    "AUS_political_events.110.t": "Sentimen Anti-[ROOT.GetAdjective] Meningkat di [FROM.GetNameDef]",
    "AUS_political_events.110.desc": "Sebagai akibat dari unjuk rasa yang didanai pemerintah, kita menerima laporan mengenai lonjakan tajam sentimen anti-[ROOT.GetAdjective] di [FROM.GetNameDef]. Kepemimpinan [FROM.GetAdjective] sama sekali belum menghubungi kita secara langsung untuk membahas masalah ini, dan hanya dapat diasumsikan bahwa mereka sudah tidak lagi menaruh minat pada jalur diplomasi saat ini.",
    "AUS_political_events.111.t": "[FROM.GetNameDefCap] Menawarkan Pakta Non-Agresi",
    "AUS_political_events.111.desc": "Kawat diplomatik dari kepemimpinan [FROM.GetAdjective] baru saja tiba di meja kita. Mereka meminta agar kita menandatangani perjanjian damai timbal balik antarnegara kita. Mereka mengakui bahwa hubungan kita di masa lalu kerap diwarnai perselisihan, namun mereka kini mendambakan dialog yang lebih konstruktif untuk masa kini dan masa depan.",
    "AUS_political_events.111.b": "Mengingat tabiat kaum [FROM.GetAdjective] dan kekacauan yang mereka timbulkan, sama sekali tidak!",
    "AUS_political_events.112.t": "[FROM.GetNameDefCap] Menandatangani Pakta Non-Agresi",
    "AUS_political_events.112.desc": "Rencana kita untuk [FROM.GetNameDef] melangkah satu babak lebih maju hari ini, menyusul penandatanganan pakta non-agresi. Kita akan terus melanjutkan upaya untuk mengikat mereka semakin erat dengan kita. Masa depan masih berupa lembaran terbuka, namun kita harus terus melangkah maju dengan rencana-rencana kita.",
    "AUS_political_events.113.t": "[FROM.GetNameDefCap] Menolak Pakta Non-Agresi",
    "AUS_political_events.113.desc": "Tampaknya tawaran kita kepada kepemimpinan [FROM.GetAdjective] tidak memuaskan bagi mereka. Entah mereka telah mencium rencana masa depan kita atau mereka sendiri yang memendam niat jahat terhadap kita. Kita harus bersiap menghadapi segala kemungkinan, dan jika kita bertekad meneruskan rencana kita, tindakan yang lebih agresif mungkin akan diperlukan.",
    "AUS_news_events.5.t": "Bangsa [AUS.GetAdjective] Membatalkan Perjanjian Saint-Germain-en-Laye",
    "AUS_news_events.5.desc": "\\n[AUS.GetLeader] dari [AUS.GetNameDef] baru-baru ini menyatakan niat mereka untuk membatalkan Perjanjian Saint-Germain-en-Laye secara tuntas dan mempersenjatai diri kembali. Perjanjian tersebut diberlakukan pasca-Perang Besar guna mencegah [AUS.GetNameDef] mengulangi tindakan yang memicu perang serta memperluas wilayah demi meraih kekuasaan. Para pengamat berspekulasi bahwa ini adalah tanggapan atas kian memuncaknya ketegangan dunia; apakah upaya militerisasi ini murni bersifat defensif ataukah ofensif masih harus kita buktikan.",

    # Chunk 12
    "wuw_GER_realpolitik.27.t": "Perang Saudara di [ROOT.GetNameDef]",
    "wuw_GER_realpolitik.27.desc": "Setelah sekian lama sentimen komunis kian menguat, tampaknya anasir-anasir komunis [ROOT.GetAdjective] telah jenuh menanti peralihan kekuasaan secara damai. Mereka menyatakan bahwa pemerintahan kita saat ini berniat memonopoli seluruh kekuasaan dan harus digulingkan agar komunisme dapat bersemi. Menyusul perdebatan sengit, jalur diplomasi akhirnya runtuh dan konflik bersenjata pun tak terelakkan.",
    "wuw_GER_realpolitik.28.t": "Perang Saudara di [ROOT.GetNameDef]",
    "wuw_GER_realpolitik.28.desc": "Setelah sekian lama sentimen demokratis kian menguat, tampaknya anasir-anasir demokratis [ROOT.GetAdjective] telah jenuh menanti peralihan kekuasaan secara damai. Mereka menyatakan bahwa pemerintahan kita saat ini berniat memonopoli seluruh kekuasaan dan harus ditumbangkan demi mekarnya demokrasi. Menyusul perselisihan tajam, jalur diplomasi telah pupus dan pertempuran bersenjata pun meletus.",
    "wuw_GER_realpolitik.29.t": "Perang Saudara di [ROOT.GetNameDef]",
    "wuw_GER_realpolitik.29.desc": "Setelah sekian lama sentimen fasis kian menguat, tampaknya anasir-anasir fasis [ROOT.GetAdjective] telah jenuh menanti pergantian kekuasaan secara damai. Mereka mengebom sebuah kantor polisi setempat, memicu bentrokan berdarah di jalanan. Menyusul eskalasi tajam, jalur kompromi telah buntu dan konflik bersenjata tak terbendung. Kita hanya bisa menahan napas seraya menyaksikan ke mana arah masa depan bangsa [ROOT.GetAdjective] ini akan bermuara.",
    "wuw_GER_realpolitik.33.t": "[FROM.GetNameDefCap] Menuntut Integrasi Ekonomi",
    "wuw_GER_realpolitik.33.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah tiba di ibu kota kita hari ini untuk menyampaikan sebuah tawaran. Mereka menginginkan kita memperluas kegiatan serikat pabean dan memperdalam integrasi ekonomi dengan mereka. Hal ini tentu akan sangat mendongkrak perekonomian kita, namun ada aroma mencurigakan di balik semua ini...",
    "wuw_GER_realpolitik.34.t": "[FROM.GetNameDefCap] Menerima Tawaran Kita",
    "wuw_GER_realpolitik.34.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah menyambut baik tawaran kita, dan para diplomat mereka telah tiba di negeri kita untuk menandatangani dokumen-dokumen yang diperlukan guna memfasilitasi integrasi ekonomi lebih lanjut.",
    "wuw_GER_realpolitik.35.t": "[FROM.GetNameDefCap] Menolak Tawaran Kita",
    "wuw_GER_realpolitik.35.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah menanggapi undangan integrasi kita dengan ketidaksenangan yang nyata. Mereka menegaskan bahwa kemitraan ekonomi yang lebih erat antarnegara kita tidak akan pernah dipertimbangkan sama sekali. Mungkin mereka telah mencium niat tersembunyi kita...",
    "wuw_GER_realpolitik.36.t": "[FROM.GetNameDefCap] Mengusulkan Penyatuan",
    "wuw_GER_realpolitik.36.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah mengusulkan agar bangsa kita bersatu dengan bangsa mereka, mengingat rakyat kita serumpun dan akan merasa lebih terlindungi di bawah satu negara yang lebih perkasa. Tersirat nada pemaksaan dan agresi dalam pesan tersebut, namun barangkali memang yang terbaik adalah menjadi bagian dari entitas yang lebih agung?",
    "wuw_GER_realpolitik.49.t": "Tuan Penguasa Kita Menyerahkan Kita kepada [GER.GetNameDef]",
    "wuw_GER_realpolitik.49.desc": "Tuan penguasa kita telah mengkhianati kita seutuhnya dan memilih untuk menyerahkan tanah air kita kepada [GER.GetNameDef]. Haruskah kita mematuhi keputusan mereka ataukah berjuang melawan?",
    "wuw_GER_realpolitik.50.t": "[FROM.GetNameDefCap] Menolak Tawaran Kita",
    "wuw_GER_realpolitik.50.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah menolak usulan kita untuk membagi-bagi bekas wilayah Cekoslowakia era Austria-Hongaria. Tampaknya kesepakatan ini akhirnya batal sama sekali...",
    "wuw_GER_realpolitik.51.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] baru-baru ini mengecam apa yang mereka sebut sebagai pendudukan tanpa hak atas tanah Galicia kita, dengan dalih bahwa wilayah tersebut konon masih merupakan bagian sah dari Kekaisaran Austria-Hongaria masa lampau—klaim yang ditegaskan sepenuhnya oleh [FROM.GetNameDef] dan para sekutunya. Kini, kita telah menerima ultimatum [FROM.GetAdjective], dan pasukan mereka kian menumpuk di perbatasan kita. Bagaimana kita harus menanggapi?",
    "wuw_GER_realpolitik.52.t": "[FROM.GetNameDefCap] Menyerahkan Galicia",
    "wuw_GER_realpolitik.52.desc": "Sang pemimpin yang berpikiran jernih, [FROM.GetLeader] dari [FROM.GetNameDef], telah sepakat untuk menyerahkan wilayah mereka di Galicia kepada aliansi kita, serta telah memerintahkan pasukannya untuk bersiap siaga mundur dari kawasan tersebut. Kita sekali lagi berdiri sebagai pemenang!",
    "wuw_GER_realpolitik.53.t": "[FROM.GetNameDefCap] Tetap Teguh",
    "wuw_GER_realpolitik.53.desc": "Kendati tidak sepenuhnya di luar dugaan, tindakan gegabah [FROM.GetLeader] dari [FROM.GetNameDef] yang menetapkan status siaga penuh bagi pasukan negerinya pasca-menerima ultimatum kita, disusul pengiriman utusan yang menyatakan bahwa mereka tidak akan mundur walau satu langkah pun terkait sengketa ini.",

    # Chunk 13
    "GOT_GER_fading_eagle.01.t": "[FROM.GetNameDefCap] Menuntut Penundukan Kita",
    "GOT_GER_fading_eagle.01.desc": "[FROM.GetLeader] dari [FROM.GetNameDef] telah menuntut agar kita tunduk pada otoritas mereka di tengah kampanye untuk merebut kembali kendali atas Balkan dan bekas Kekaisaran Italia. Kita sesungguhnya tidak memiliki kekuatan untuk melawan mereka saat ini, namun barangkali inilah kesempatan menuju kemerdekaan yang selama ini kita nanti-nantikan?",
    "GER_inner_circle.02.desc": "Para Reichsleiter terdekat dengan [GER.GetLeader] mulai meragukan kepemimpinan [GER.GetLeader.GetHersHis] dan visi yang dipegang [GER.GetLeader.GetSheHe] bagi masa depan [GER.GetNameDef]. Mereka kini merajut konspirasi untuk menggulingkan [GER.GetLeader] dari tampuk kekuasaan dan merebut gelar Führer bagi diri mereka sendiri. Pertanyaannya adalah: siapakah yang akan mengungguli para rivalnya dan memimpin jalan menuju masa depan yang gemilang?",
    "GOT_guarantee_events.01.desc": "Jelas terlihat bahwa [GER.GetLeader] tidak lagi dapat diajak bernalar sehat dan tidak akan berhenti sebelum mencapai dominasi dunia. [GER.GetLeader.GetSheHe] kian yakin bahwa tiada satu kekuatan pun yang berani merintangi jalan [GER.GetNameDef] beserta ambisi ekspansinya yang rakus akan wilayah baru.",
    "GOT_guarantee_events.01.b": "Biarkan [GER.GetLeader] berbuat sesuka yang [GER.GetLeader.GetSheHe] kehendaki."
}

print(f"Total fixes defined: {len(fixes)}")

# Apply to each chunk
for c in range(14):
    chunk_file = f'scripts/chunks/trans_chunk_{c}.json'
    if not os.path.exists(chunk_file):
        continue
    with open(chunk_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for k, v in fixes.items():
        if k in data:
            data[k] = v
            modified = True
            print(f"Chunk {c:2d} | Patched {k}")
            
    if modified:
        with open(chunk_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved updated {chunk_file}")

print("=== All fixes applied successfully! ===")
