# -*- coding: utf-8 -*-
import json

# Entries 605 to 723 (wtt_japan events)
chunk5_translations = {
    # 605 - 614: Japan demanding colonies of fallen nations
    "wtt_japan.1.t": "[From.GetNameDefCap] Menginginkan Pertuanan atas Koloni Kita",
    "wtt_japan.1.desc": "Memanfaatkan peluang yang timbul dari kelemahan kita, pihak [From.GetAdjective] telah menawarkan untuk 'membantu' kita dalam 'menjaga ketertiban' di koloni-koloni kita. Mereka berpendapat bahwa, dengan jatuhnya daratan utama kita, kita tidak memiliki peluang untuk mempertahankan kendali kita.\\n\\nIni jelas merupakan siasat untuk merebut kendali koloni-koloni kita, namun pilihan apa lagi yang kita miliki?",
    "wtt_japan.1.a": "Sudah saatnya menerima dominasi Jepang di Timur.",
    "wtt_japan.1.b": "Mereka harus merebutnya dengan kekerasan!",
    "wtt_japan.2.t": "[From.GetNameDefCap] Memberikan Pertuanan atas Koloni",
    "wtt_japan.2.desc": "[From.GetNameDefCap] telah mempertimbangkan secara seksama tawaran kita untuk 'menjaga ketertiban' di koloni mereka, dan telah memutuskan untuk menerimanya. Mereka secara efektif telah menyerahkan kendali penuh kepada kita.",
    "wtt_japan.2.a": "Keputusan yang bijaksana.",
    "wtt_japan.3.t": "[From.GetNameDefCap] Menolak Pertuanan atas Koloni",
    "wtt_japan.3.desc": "[From.GetNameDefCap] telah mempertimbangkan dengan matang tawaran kita untuk 'menjaga ketertiban' di koloni mereka, dan memutuskan untuk menolaknya.",
    "wtt_japan.3.a": "Kita lihat saja bagaimana nasib mereka nanti.",

    # 615 - 624: Non-Aggression Pact
    "wtt_japan.11.t": "Pakta Non-Agresi dengan [From.GetNameDef]",
    "wtt_japan.11.desc": "Meskipun ketegangan antara [From.GetAdjective] dan [Root.GetNameDef] meningkat hingga akhir-akhir ini, pihak [From.GetAdjective] kini telah membuka perundingan untuk sebuah Pakta Non-Agresi. Keuntungan bagi kita sudah jelas, namun yang patut kita waspadai adalah keuntungan yang akan diperoleh pihak [From.GetAdjective], dan apakah kita kelak akan menyesali langkah ini.",
    "wtt_japan.11.a": "Kita harus menjaga perdamaian... untuk saat ini.",
    "wtt_japan.11.b": "Mencegah mereka meraih keuntungan adalah prioritas utama!",
    "wtt_japan.12.t": "[From.GetNameDefCap] Menerima Pakta Non-Agresi",
    "wtt_japan.12.desc": "[From.GetNameDefCap] telah secara resmi menerima tawaran Pakta Non-Agresi dari kita.",
    "wtt_japan.12.a": "Mereka masuk tepat ke dalam perangkap kita.",
    "wtt_japan.13.t": "[From.GetNameDefCap] Menolak Pakta Non-Agresi",
    "wtt_japan.13.desc": "Entah dengan alasan apa, [From.GetNameDef] telah menolak tawaran Pakta Non-Agresi dari kita.",
    "wtt_japan.13.a": "Apakah mereka sedang bersekongkol melawan kita?",

    # 625 - 630: Exchange of Generals
    "wtt_japan.21.t": "Pertukaran Jenderal [From.GetAdjective]",
    "wtt_japan.21.desc": "Pihak [From.GetAdjective] telah memutuskan untuk memanggil kembali pegawai negeri dan jenderal berhaluan kiri mereka, dan sebaliknya mengirimkan jenderal serta pegawai negeri berhaluan kanan mereka kepada kita dalam pengasingan tidak resmi.",
    "wtt_japan.21.a": "Tampaknya sesuatu sedang bergejolak di [From.GetNameDef]...",
    "wtt_japan.22.t": "Jenderal [Root.GetAdjective] Telah Ditukar",
    "wtt_japan.22.desc": "Proses pertukaran jenderal dan pegawai negeri berhaluan kanan kita dengan jenderal dan pegawai negeri berhaluan kiri yang sebelumnya kita kirim ke pengasingan tidak resmi di [From.GetNameDef] kini telah selesai.",
    "wtt_japan.22.a": "Ini akan memperkokoh cengkeraman kita atas [Root.GetNameDef].",

    # 631 - 637: Fate of the Imperial Family
    "wtt_japan.31.t": "Nasib Keluarga Kekaisaran",
    "wtt_japan.31.desc": "Waktunya telah tiba untuk menentukan nasib Kaisar dan keluarganya. Status sosial turun-temurun tidak memiliki tempat di Jepang baru yang sedang kita bangun. Apa yang harus kita lakukan terhadap mereka?",
    "wtt_japan.31.a": "Asingkan mereka!",
    "wtt_japan.31.b": "Penggal kepala mereka!",
    "wtt_japan.32.t": "Keluarga Kekaisaran yang Terasing",
    "wtt_japan.32.desc": "[From.GetNameDefCap] telah mengasingkan keluarga kekaisaran, memberikan anugerah besar bagi kita dengan melakukannya! Beliau kini telah tiba di [Root.GetNameDef], dan terlepas dari pengasingannya, pengaruh beliau di mata rakyat dan pasukan masih sangat besar.",
    "wtt_japan.32.a": "Kita harus layak menjadi rumah bagi beliau!",

    # 638 - 643: Manchurian Reunification
    "wtt_japan.101.t": "Reunifikasi Manchuria",
    "wtt_japan.101.desc": "Dengan kemenangan mereka baru-baru ini melawan [MAN.GetName], pemerintah Jepang kini mengakui ikatan Tiongkok dengan wilayah tersebut, dan segera mengalihkan seluruh kendali kepada kita. Dengan gestur itikad baik ini, mereka menawarkan persekutuan kepada kita.",
    "wtt_japan.101.a": "Mungkin bangsa Jepang memang masih bisa diajak berunding.",
    "wtt_japan.101.b": "Kita terima Manchuria, tapi bukan kebaikan mereka.",
    "wtt_japan.102.desc": "[From.GetNameDefCap] berterima kasih kepada kita atas pengembalian Manchuria, dan telah menerima tawaran persekutuan kita.",
    "wtt_japan.103.desc": "[From.GetNameDefCap] berterima kasih kepada kita atas pengembalian Manchuria, namun menolak tawaran persekutuan kita.",

    # 644 - 653: Philippine Sovereignty
    "wtt_japan.104.t": "Kedaulatan Filipina",
    "wtt_japan.104.desc": "[From.GetNameDefCap] telah membuat pernyataan terbuka dan tegas bahwa mereka 'tidak dapat lagi tinggal diam dan menyaksikan' sebuah bangsa di kawasan pengaruh mereka terus hidup di bawah sepatu lars Barat. Mereka kini menuntut agar kita mempercepat garis waktu dekolonisasi dan memberikan kedaulatan penuh kepada Filipina secepatnya.",
    "wtt_japan.104.a": "Mereka benar. Filipina berhak atas kebebasan mereka.",
    "wtt_japan.104.b": "Filipina akan tetap menjadi milik Amerika!",
    "wtt_japan.105.desc": "[From.GetNameDefCap] telah menanggapi tuntutan kita demi kemerdekaan penuh Filipina, dan pemerintah Amerika kini telah melakukan persiapan segera untuk memberikan kedaulatan penuh kepada wilayah Pasifik mereka.",
    "wtt_japan.105.a": "Setidaknya mereka masih berpikir jernih.",
    "wtt_japan.106.desc": "[From.GetNameDefCap] telah menanggapi tuntutan kita demi kemerdekaan penuh Filipina, dengan menegaskan kembali 'kepentingan vital Amerika' yang diwakili oleh Filipina di kawasan tersebut.",
    "wtt_japan.106.a": "Dan mereka menyebut diri mereka 'pembela Kebebasan'?",
    "wtt_japan.107.desc": "[From.GetNameDefCap] telah menanggapi tuntutan Jepang demi kemerdekaan penuh kita, dan pemerintah Amerika kini telah melakukan persiapan segera untuk memberi kita kedaulatan penuh!",
    "wtt_japan.107.a": "Pujilah bangsa Jepang!",

    # 654 - 656: Young Officer Coup
    "wtt_japan.108.t": "Kudeta Perwira Muda",
    "wtt_japan.108.desc": "Sekelompok perwira muda telah berhasil membunuh sejumlah pejabat pemerintah serta perdana menteri. Mereka telah menduduki kota Tokyo dan mengamankan Istana Kekaisaran, seraya mengumumkan niat mereka untuk membersihkan pemerintahan dari 'pejabat korup' dan 'ancaman ideologis', demi memulihkan Kaisar sebagai penguasa tunggal bangsa.\\n\\nTindakan mereka memperoleh dukungan militer yang luar biasa besar, di mana operasi tandingan yang direncanakan berhasil digagalkan lewat penangkapan massal dan pembunuhan terhadap elemen-elemen yang setia kepada pemerintah lama. Dihadapkan pada peristiwa yang begitu mendadak dan tak terbendung, serta kendali para pemberontak atas istana, Kaisar tidak menunjukkan tanda-tanda mengecam aksi mereka.\\n\\nPerlawanan terorganisir pemerintah tampaknya telah runtuh, dan para pemberontak diperkirakan akan segera mengumumkan berlakunya kendali Kekaisaran secara mutlak atas seluruh bidang kebijakan domestik, luar negeri, dan militer.",
    "wtt_japan.108.a": "Tennōheika Banzai!",

    # 657 - 667: Tripartite Pact
    "wtt_japan.109.t": "Jepang Mengusulkan Pakta Tripartit",
    "wtt_japan.109.desc": "[From.GetNameDefCap] telah mengirimkan utusan penjajakan untuk memastikan minat kita terhadap pakta tiga kekuatan antara kita, pihak [JAP_initiator.GetAdjective], dan pihak [ITA_fascism.GetAdjective]. Pihak [JAP_initiator.GetAdjective] berpendapat bahwa kita harus saling mendukung mengingat opini global yang kian memusuhi perjuangan kita.",
    "wtt_japan.109.a": "Gagasan yang luar biasa. Kita akan menandatangani Pakta ini.",
    "wtt_japan.109.b": "Tidak, kita tidak boleh mengambil risiko memusuhi dunia.",
    "wtt_japan.110.desc": "[JAP_initiator.GetNameDefCap] telah mengirim utusan penjajakan untuk memastikan minat kita terhadap pakta tiga kekuatan antara kita, pihak [JAP_initiator.GetAdjective], dan pihak [GER_fascism.GetAdjective]. Pihak [JAP_initiator.GetAdjective] berpendapat bahwa saling mendukung adalah keharusan di tengah opini global yang kian memusuhi perjuangan kita. Pihak [GER_fascism.GetAdjective] telah menyatakan persetujuannya terhadap gagasan ini.",
    "wtt_japan.111.t": "Pakta Tripartit Ditandatangani",
    "wtt_japan.111.desc": "Pemerintah [GER_fascism.GetAdjective] dan [ITA_fascism.GetAdjective] telah sepakat untuk menandatangani rancangan Pakta Tripartit, berikrar untuk berdiri di sisi kita apabila perang meletus.",
    "wtt_japan.112.t": "[From.GetNameDefCap] Menolak Pakta Tripartit",
    "wtt_japan.112.desc": "Pemerintah [From.GetAdjective] telah menolak usulan Pakta Tripartit, memilih untuk berjuang sendirian.",
    "wtt_japan.113.t": "[From.GetNameDefCap] Menandatangani Pakta Tripartit",
    "wtt_japan.113.desc": "Pemerintah [ITA_fascism.GetAdjective] telah sepakat untuk menandatangani usulan Pakta Tripartit, berikrar untuk berdiri di sisi kita apabila perang meletus.",

    # 668 - 670: Democratic coup
    "wtt_japan.114.t": "Elemen Demokratis Melancarkan Kudeta",
    "wtt_japan.114.desc": "Elemen-elemen demokratis di dalam tubuh pemerintahan telah memprakarsai pengambilalihan negara secara mengejutkan, setelah pihak militer mengancam akan kembali mengekang hak-hak demokratis rakyat yang diperoleh dengan susah payah. Dengan ketangkasan yang mencengangkan, sebagian besar militer justru angkat senjata demi membela rakyat dan hak-hak kebebasan mereka.\\n\\nPerpecahan di tubuh militer ini memungkinkan perwakilan rakyat merebut kekuasaan di cabang legislatif dan eksekutif. Kendati pertempuran baru saja dimulai, kecil kemungkinan pemerintahan saat ini dapat digulingkan dengan mudah.",
    "wtt_japan.114.a": "Jangan biarkan militer memerintah kita lagi!",

    # 671 - 680: Attack Soviet Union & Non-Aggression dilemmas
    "wtt_japan.115.t": "[From.GetName] Menyerang Uni Soviet",
    "wtt_japan.115.desc": "[From.GetNameDefCap] telah menyerang Uni Soviet secara sepihak, mengabaikan pakta non-agresi kita dengan mereka. Kita tidak punya pilihan lain selain menghormati persekutuan kita dan mendukung serangan [From.GetAdjective], atau menghormati pakta non-agresi kita dengan Soviet dan mengecam serangan tersebut.",
    "wtt_japan.115.a": "Kita akan bergabung dengan sekutu kita!",
    "wtt_japan.115.b": "Perjanjian kita tak boleh dilanggar... Untuk saat ini.",
    "wtt_japan.116.t": "[From.GetName] Bergabung dalam Perang",
    "wtt_japan.116.desc": "[From.GetNameDefCap] telah memutuskan untuk bergabung dalam perang kita melawan Soviet, mengabaikan pakta non-agresi mereka sebelumnya.",
    "wtt_japan.116.a": "Sudah seharusnya demikian.",
    "wtt_japan.117.t": "[From.GetName] Mengecam Perang Kita",
    "wtt_japan.117.desc": "[From.GetNameDefCap] telah memutuskan untuk menghormati pakta non-agresi mereka dengan Soviet, mengabaikan komitmen mereka kepada kita sebagai sekutu. Mereka telah mengecam agresi kita, yang tampaknya merupakan upaya untuk menyelamatkan situasi diplomatik dengan sesama anggota pakta.",
    "wtt_japan.117.a": "Sungguh sangat disayangkan.",

    # 681 - 692: South Sakhalin assistance / volunteers
    "wtt_japan.118.t": "[From.GetName] Memohon Bantuan",
    "wtt_japan.118.desc": "[From.GetNameDefCap] saat ini tengah terjebak dalam perang saudara yang menghancurkan, dan kesulitan mengimbangi kekuatan militer musuh mereka. Pemerintahan transisi mereka kini telah mendekati perwakilan kita dengan tawaran untuk menyerahkan semenanjung Sakhalin Selatan demi mendapatkan bantuan militer yang sangat mereka butuhkan.\\n\\nIni bisa menjadi cara mudah untuk memperoleh wilayah sebagai imbalan atas pengiriman divisi sukarelawan.",
    "wtt_japan.118.a": "Gagasan yang sangat bagus!",
    "wtt_japan_118_TT": "Para sukarelawan ini akan dikembalikan ke cadangan tenaga manusia jika §Y[From.GetName]§! memenangkan perang saudara.",
    "wtt_japan.118.b": "Ini bukan pertukaran yang menguntungkan bagi kita.",
    "wtt_japan.119.t": "[From.GetName] Menerima Pertukaran",
    "wtt_japan.119.desc": "[From.GetNameDefCap] telah menerima tawaran kita untuk menukar Semenanjung Sakhalin Selatan dengan dukungan militer. Mereka telah mengerahkan beberapa divisi 'sukarelawan' untuk membantu perjuangan kita!",
    "wtt_japan.119.a": "Mereka akan sangat berguna!",
    "wtt_japan.119.TT": "Dapatkan 8 unit dengan §Y12 batalion infanteri§! dan §Y3 batalion bantuan§!.",
    "wtt_japan.120.t": "[From.GetName] Menolak Pertukaran",
    "wtt_japan.120.desc": "[From.GetNameDefCap] telah memberitahu kita bahwa mereka menolak tawaran untuk menukar Semenanjung Sakhalin Selatan demi dukungan militer.",
    "wtt_japan.120.a": "Kita kini harus berjuang sendiri...",

    # 693 - 704: Taking Tokyo & Civil War end
    "wtt_japan.121.t": "[From.GetName] Merebut Tokyo",
    "wtt_japan.121.desc": "[From.GetNameDefCap] telah merebut ibu kota Jepang, dan pemerintah fasis [From.From.GetAdjective] telah runtuh. Jika kita ingin bertindak, kita harus melakukannya saat ini juga. Sangat penting bagi kita untuk bergerak cepat mengamankan kendali atas pulau-pulau luar Jepang dan mengambil alih komando elemen fasis yang tersisa, jika kita ingin membendung ancaman komunis.",
    "wtt_japan.121.a": "Jalankan rencana ini.",
    "wtt_japan.121.b": "Hal ini tidak menarik bagi kita saat ini.",
    "wtt_japan.122.t": "Kaum Fasis Melarikan Diri ke Manchuria",
    "wtt_japan.122.desc": "Dengan jatuhnya Tokyo, pemerintah fasis telah runtuh dan para pendukung serta unit militer mereka yang tersisa melarikan diri ke [MAN.GetName], yang telah mengambil alih kendali atas pulau-pulau terluar serta wilayah kekuasaan di Korea dan Tiongkok.\\n\\nPerang saudara secara efektif telah berakhir, namun gencatan senjata ini sangat rapuh, karena kaum fasis belum sepenuhnya ditumpas secara telak.",
    "wtt_japan.122.a": "Kita akan berurusan dengan mereka nanti.",
    "wtt_japan.123.t": "Perlawanan Fasis Runtuh",
    "wtt_japan.123.desc": "Dengan jatuhnya Tokyo, rezim fasis telah hancur lebur. Para pendukung dan unit militer mereka yang tersisa tidak lagi memiliki tempat bergantung dan mulai tercerai-berai, memungkinkan penguasaan yang mudah atas wilayah-wilayah yang tersisa dan terluar.",
    "wtt_japan.123.a": "Perang telah dimenangkan.",
    "wtt_japan.124.t": "Sukarelawan Kembali Pulang",
    "wtt_japan.124.desc": "Dengan kemenangan komunis di Jepang, para sukarelawan kita yang selamat kini telah kembali ke tanah air.",

    # 705 - 716: Manchuria & Peace offers
    "wtt_japan.125.t": "Soviet Mengembalikan Manchuria",
    "wtt_japan.125.desc": "Setelah membebaskan Manchuria dari cengkeraman Jepang dan menggulingkan kaisar Qing yang digulingkan, [From.GetNameDef] kini menawarkan pengembalian Manchuria kepada kita, seraya menyatakan bahwa wilayah itu harus kembali ke tangan sah [Root.GetAdjective].",
    "wtt_japan.126.t": "[From.GetName] Menawarkan Perdamaian",
    "wtt_japan.126.desc": "Para pejabat [From.GetAdjective] telah mendekati kita dengan tawaran perdamaian. Mereka bersedia angkat kaki sepenuhnya dari benua ini, sebagai imbalan atas penghentian permusuhan segera.",
    "wtt_japan.126.a": "Perang telah dimenangkan.",
    "wtt_japan.126.b": "Kita hanya akan puas dengan kemenangan mutlak!",
    "wtt_japan.127.t": "[From.GetName] Menerima Perdamaian",
    "wtt_japan.127.desc": "[From.GetNameDef] telah menerima tawaran perdamaian kita, dan telah menghentikan permusuhan sebagai imbalan atas wilayah kekuasaan kita di benua Asia.",
    "wtt_japan.127.a": "Mereka telah mengungguli kita... Untuk saat ini.",
    "wtt_japan.128.t": "[From.GetName] Menolak Perdamaian",
    "wtt_japan.128.desc": "[From.GetNameDef] telah menolak tawaran perdamaian kita, bersumpah untuk terus berperang hingga memperoleh penyerahan tanpa syarat.",
    "wtt_japan.128.a": "Maka kita akan bertempur sampai titik darah penghabisan!",

    # 717 - 723: Demands Manchuria & Military aid
    "wtt_japan.40.t": "[From.GetLeader] Menuntut Manchuria",
    "wtt_japan.40.desc": "Beberapa hari yang lalu, pemerintah [From.GetNameDef] mulai melancarkan upaya terpadu untuk menekan kita. Artikel utama di surat kabar menuntut agar kita mengembalikan Manchuria ke dalam kendali [From.GetAdjective]. Ini bukan sekadar manuver propaganda untuk konsumsi internal semata, sebab utusan [From.GetLeader] telah menjajaki kita melalui jalur belakang diplomatik untuk mencapai kesepakatan mengenai masa depan wilayah Manchuria.\\n\\nHari ini, [From.GetLeader] sendiri angkat bicara mengenai persoalan tersebut, menuntut pengembalian penuh Manchuria kepada [From.GetNameDef] sesegera mungkin. Jika tidak, pemerintahnya terpaksa meninjau kembali kerja sama kita saat ini.",
    "wtt_japan.40.a": "Wilayah itu milik mereka.",
    "wtt_japan.40.b": "Mereka belum siap untuk memerintah diri sendiri.",
    "wtt_japan.41.t": "Bantuan Militer dari [From.GetNameDef]",
    "wtt_japan.41.desc": "Markas Besar Kekaisaran Jepang telah memutuskan pergeseran mendasar dalam pandangan strategis mereka. Dalam konferensi bersama Kaisar, Menteri Angkatan Darat mempresentasikan rencana baru yang berasumsi bahwa perang melawan Uni Soviet akan pecah dalam waktu dekat. Demi mempersiapkan perang ini, Angkatan Darat Kekaisaran Jepang memutuskan bahwa militer kita harus mampu mempertahankan sebagian garis depan. Untuk tujuan ini, sejumlah besar perlengkapan yang hanya sedikit usang telah disediakan.",
    "wtt_japan.41.a": "Sungguh baik hati mereka."
}

with open("wtt_events_raw.json", "r", encoding="utf-8") as f:
    raw = json.load(f)

# Slice 605:724
slice_raw = raw[605:724]
out = []
missing = []

for item in slice_raw:
    k = item["key"]
    if k in chunk5_translations:
        out.append({"key": k, "id": chunk5_translations[k]})
    else:
        missing.append(k)

if missing:
    print("MISSING KEYS in chunk 5:", missing)
else:
    with open("wtt_events_chunk5.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved events chunk 5: {len(out)} entries")
