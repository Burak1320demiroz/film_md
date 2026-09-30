# 📖 THE_BRITTLE_EDGE — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 20.09.2026 15:30
> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.
>
> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna
> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş
> bırakılmaz — boş hücre "okudum" ile "atladım" arasını ayırt ettirmez.
>
> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.
> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.
> ⛔ 14.09.2026: her satırdan kilit ÇIKMAZ. "—" yazmak meşrudur; sıfır "—"
> çizelgeyi sahte yapar (`prompt_kontrol.py` ㉘ · LOCKED_PULSE 126/126 ölçümü).

### TUR 1 · YAŞAYAN DERSLER — `DERSLER/00_YASAYAN_DERSLER.md` (14.09.2026)

> Film dersi havuzu bu listedir; ders metni ETİKET filme uyuyorsa açılır. ETİKET
> uymuyorsa (`kask` etiketli ders kasksız filmde) satır **"—"** ile geçilir — bu
> "okumadım" değil "bu filme düşmüyor" demektir ve ㉘ kapısı tam bunu bekler.

| ⬜/✅ | ders | ETİKET | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | — |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | — |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | Her video tek kesintisiz çekim; montaj/kesme promptta yasak |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | Opak siyah vizör; kask içi yüz görünmez, morph riski sıfırlandı |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Prompt gövdesinde başlık kartı, logo veya jenerik metni yok |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | Araç ve giysi yıpranması sabit 3 görsel çapa kelimesiyle kilitlenir |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | V3 iskeleti nötr tarifle yazılır, meta-komutlar prompta sızmaz |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S11 finali tek yavaş kamera hareketiyle bağımsız vuruş olarak korunur |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | — |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | S02'de kırık yüzeyin yakın planı novumu tek karede gösterir |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Giysi ve araç gövdesi metinsiz; harf/rakam overlay promptlanmaz |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Sırt ünitesi dikey kompakt yaşam destek paketi olarak pozitif tanımlanır |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Her sahnede tek açık aksiyon fiili bulunur |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | Vizör açılı altıgen çerçeveli kask içine gömülü opak siyah vizör |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Kırık çekme kulağı ve sarı gövde tek karede net okunur |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Giysi için max 3 çapa: kirli kırık beyaz, turuncu kol şeritleri, siyah vizör |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | S05 ve S08'de eldivenli ellerde ve dizlerde mekanik zorlanma |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Sapan ve halat ayrı işlevsel nesneler olarak net ayrılır |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | Yönler krater duvarı ve uçurum kenarı referansıyla tanımlanır |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | — |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | Koyu bazalt krater zemini ve endüstriyel sarı gövde kontrastı |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IMAGE promptları eylemin öncesi t=0 anını gösterir |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | Modelden sessizlik istenmez; AUDIO satırında titreşim ve nefes yazılır |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | Kopma anı cam tozu değil keskin mekanik kırılma olarak tarif edilir |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | Krater kenarından 15° alçak açılı tek yönlü sert güneş ışığı |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | Ay yerçekimi 0,16g; kopan parça ve toz balistik yavaşça hareket eder |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | Astronot ve araç aynı 0,16g Ay yerçekimi dinamiğine uyar |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | Komşu sahnelerde ışık yönü değişmez, gölgeler derin siyah |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S05 sapanı geçirme seçimi, S08 son desteğin kopması bedeli bedende okunur |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | — |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | S08'de astronotun araca kilitlenen kaskı ve gerilen postürü |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | S00 kopmasından S03'e kadar temkinli ve gergin hareketler sürer |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Giysi kimlik dizisi S00-S11 arası değişmez |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | Kraterin sivri kenar zirvesi sabit arka plan çapasıdır |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | S00 kopan bağlantı ile S11 kurtarılan sağlam şasi kafiyesi |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S00 ilk 3 saniyede kopma sorusu, S11 kurtarma çıkışı |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | 12 sahnenin her biri farklı vuruş ve kurulum harfine sahiptir |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Kopma anı (S00) ve askıda kalma anı (S09) kadraj içinde verilir |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | — |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Promptlarda timecode veya overlay istenmez |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | Vakum dış çekimde ses yok; kask içi nefes ve kablo gerilimi |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | — |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | R1 kopma, R4 uçurum eğimi, R7 askıda yük |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 540 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A kapı listesi ve B5 (İstek/Engel/Bedel/Muhatap) tamlığı |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | B5 istek ve muhatap (ölümcül uçurum) netliği |
| ✅ | `KILAVUZ_REHBERI.md` | 2382 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.2 format, §3.1 VAKUM ortam kartı, negatif çekirdek 8 cümle |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 427 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3 şablonu, IN FRAME ve START FRAME kuralı |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | Fiziksel novum: Gevrek Kırılma (DBTT), taşıyıcı kırık çekme kulağı |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 314 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | Tema: UYUM VE ÖĞRENME (Kuvvet yerine metot değişimi) |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | S00 Nesne Hook (kopan metal kulak), ilk 3 saniye thumb-stop |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | Kurulum sayısı ≥3, ardışık açılarda ≥1 ölçek ve ≥45° fark |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | Yakın detay ile geniş uçurum kontrastı |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | 12 sahne × 10s = 120s süre |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | Ekin: sakin, gözlemci, mekanik odaklı davranış şeridi |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | Çapa üçlüsü: SEÇİM S05, BEDEL S08, FİNAL S10 |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 438 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | Her sahnede kilit süreç fiili ve ≤3 timeline satırı |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | Güvenli nesne etkileşimi; nötr mekanik tarif |
| ✅ | `PROMPT_HATA_ONLEME_KILAVUZU.md` | 411 | §1 on kilit · §2 ORTAM CÜMLELERİ (kopyala-yapıştır) · §3 15 hata sınıfı · §4 promptun kapatamadığı üç sınıf · §5 novum kilidi · §7 --kilit ölçümü (19.09.2026 · 31 film / 688 bulgu) | Vakum ortam cümleleri ve metal kırılma kuralları |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | — |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | — |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | — |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | Giysi kimliği: kırık beyaz, turuncu kol şeritleri, siyah vizör |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | Ağır keşif arketipi, kask içi ışıksız opak vizör |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | — |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1258 | Tamlık matrisine satır ekleme (0/4) |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | Mekanik kopma sahnelerinde red riski yok |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | Anlatı netliği ve B5 bedel doğrulaması |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Gevrek kırılma fiziğinin tutarlılığı |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Tek astronotun beden dili devamlılığı |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Vakum ortamında ses miksi |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | Kapak ve başlık optimizasyonu |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | Karakterin niyet ve bedelinin bedende okunması |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | Krater gölgesi ve sert tek yönlü ışık |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | İlk 3 saniyede kırılma anının thumb-stop gücü |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 104 | Prompt ile görsel üretim sadakati |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 64 | 0,16g Ay yerçekiminde beden ve nesne dinamiği |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 64 | Uçurum ve krater yönünün sahneler arası korunması |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | Sahne içi kompozisyon ve novum okunurluğu |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | 7 nesne durumunun (araç konumu, sapan, halat) devamlılığı |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | Kurguda ses katmanlarının ayrımı |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | Nedensellik zinciri |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 111 | Krater duvarları ve zemin dokusu tutarlılığı |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 95 | Gevrek kırılma ve balistik toz hareketi |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 77 | Askıda kalma ve çekme aksiyonunun okunurluğu |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 77 | Sapanı yerleştirirken ve vinç gerilirken efor |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | Kurulum haritaları ve kamera açı sadakati |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (70 dosya · 16957 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_LOCKED_PULSE.md` | ① aynı format | Yatay 2 dk ASL ve 12 sahne yapısı |
| ✅ | `THE_LAST_SHIFT.md` | ② aynı ortam kartı | Ay/Vakum ortamında sert gölgeler ve regolit davranışı |
| ✅ | `THE_BORROWED_WEIGHT.md` | ③ aynı tema | Yük dağılımı ve yöntem değişimi |
| ✅ | `KRONOS_SON_SINYAL.md` | ④ en düşük skor | Düşük skor sebeplerinden kaçınma (kurgu temposu) |
| ✅ | `THE_TETHERED_MASS.md` | ⑤ en yakın konsept | Halat, gerilim ve kütle kurtarma mekaniği |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  22  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   47
ZORUNLU SATIR:   15508
SEÇMELİ KAYIT:   5 / 70  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
