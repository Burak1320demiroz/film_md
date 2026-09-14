# 🎬 THE SINKING STAKE — PLAN

> _"Bu dünyada dikilen hiçbir şey ayakta kalmaz."_
> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarındadır.

```
FORMAT:        yatay 3-5 dk (16:9)          [KILAVUZ_REHBERI §2.3]
ORTAM:         §3.2 türevi — İNCE ATMOSFER, azot buharı ~15 µbar
               (Mars kartının SES/GÖLGE/RÜZGAR satırları geçerli;
                TOZ satırı geçerli DEĞİL — bu dünyada toz yok, KAR var)
TÜR:           bilimkurgu   (tek açık dal — §4.1)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124] — plan 10,0 s varsayar:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
SAHNE SAYISI:  25            RUNTIME: 249 s = 4:09 = 9 s hook + 24 × 10 s
               ⚠️ DEPODA ÇELİŞKİ VAR ve bu film §2.3'ü izliyor:
               KILAVUZ_REHBERI §2.3 kartı **25 sahne / 4:09** der,
               `yatay_4_dk_filmler/README.md` **24 sahne / 2×12** der.
               THE PAYLOAD (31.08) README'yi izledi ve çelişkiyi kaydetti;
               bu film KART A'nın işaret ettiği §2.3'ü izler (13+12).
               ⛔ Çelişki hâlâ depoda duruyor — iki kaynaktan biri
                 düzeltilene kadar her film hangisini izlediğini YAZAR.
LOGLINE:       Donmuş azot ovasında sıcak olan her şey kendi mezarını kazar;
               kalıcı bir işaret dikmeye gelen iki astronot, dikilecek hiçbir
               şeyin duramayacağını anlayınca geminin sıcak çekirdeğini
               bilerek gömer — ve ufukta aynı işaretten bir tane daha
               olduğunu görür.
```

---

## 🎭 TEMA

```
TEMA: ZAMAN      (TEMA_MUHENDISLIGI §3 · yatay SÜREÇ teması §4)
      — "Burada hiçbir iz kendi başına kalmaz; kalan her iz, biri onu
        orada bırakmayı SEÇTİĞİ içindir."

⛔ Takas kalıbı DEĞİL [§3c moratoryumu]: cümlede "X için Y feda edilir"
   yapısı yok. Cümle bir SEBEP cümlesidir (iz neden kalır).
⛔ Etiket TİRELİ yazıldı: sayac.sh boşluklu etiketi eler ve temayı
   "kullanılmamış" sayar.

MOTİF SAHNELERİ: S3 · S12 · S21 · S24
      S3  NESNE   — ufuk çizgisinde ince dikey beyaz çizgi (2 s, vurgusuz)
      S12 KİNESİK — dikili duran şey yatay hâle gelir; iki figür geri
                    çekilir ve DOKUNMAZ (bırakmanın ilk hâli)
      S21 KAMERA  — alt açı 25°; sütun kadrajın üst kenarından çıkar,
                    ovadaki tek dikey şey odur
      S24 IŞIK    — halka ışığı iki sütunu AYNI parlaklıkta yakalar;
                    yeni olanla eski olan birbirinden ayırt edilemez
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          FİZİKSEL YASA  (§1 birinci tercih)
NOVUM:               Bu ovada zemine bırakılan sıcak her şey durmaz —
                     zemini gaza çevirerek kendi çukurunu kazar ve
                     içine iner. Hiçbir şey durduğu yerde kalmaz.
NOVUM TAŞIYICISI:    beyaz kazık ayağı × iki eldivenle zemine bastırma
                     jesti → kazık durmuyor; ayağın çevresinden dimdik
                     beyaz gaz halkası fışkırıyor ve kazık kendi boyunca
                     aşağı gidiyor
TEK KARE (§4①):      S0 · 0:04 — beyaz kazık ayağı kara yarıya gömülmüş,
                     çevresinde dimdik beyaz gaz halkası, kar yüzeyi
                     ayağın etrafında içeri çökmüş. İzleyici 1 saniyede
                     "zemin kazığı yutuyor" der.
                     ⛔ D157 gereği bu cümle TAŞIYICI NESNENİN adını
                       taşır: kazık + ayağı. Başka nesneyle geçilen kapı
                       geçilmemiş kapıdır.
KİNETİK BAĞIMSIZLIK: ✅ 0 replik · 0 dış ses · 0 ekran metni. Kural yalnız
                     jestlerle kanıtlanır: bastır → gaz → in. Filmin
                     tamamı sessizdir.
BAŞLIK ŞEMASI:       "THE SINKING STAKE" (3 kelime) — izleyiciye NEREYE
                     bakacağını söyler: kazığa. Ve ne olduğunu: batıyor.
```

### §3 MAYA EŞİĞİ — tek ihlal

```
KABUK (tanıdık, yenilik KOYULMAZ): uzay giysisi · kask · el aleti · iniş
       aracı · kar · ova. Hepsi bilinen biçimde davranır.
İHLAL SAYISI: 1 — "sıcak olan iner". İkinci bağımsız kural YOK.
İHLAL DIŞI HER ŞEY normal fizikle: 0,40 g'de düşen alet, gerçek zamanlı
       yürüyüş, rüzgârsız hava, sessiz vakum. Kuralın kanıtı yanındaki
       normalin kusursuz çalışmasıdır.
```

### §5 KURAL TEKRARI — ≥3 sahne · ≥2 farklı nesne

```
KURULUM    S0-S1   kazık (nesne 1) — ilk temas, durmuyor
DOĞRULAMA  S6      basınç plakası (nesne 2) — kenarından halka
           S7      kasa köşeleri (nesne 3) — dört küçük sütun
           S8-S9   soğutulmuş kazık ayağı — bir süre TUTAR (kural sınırı)
           S10     bot (nesne 4) — çukur, bot kalktıktan SONRA büyümeye devam
           S11     iniş bacağı (nesne 5) — üç kademenin ikisi kar altında
SONUÇ      S20     çekirdek (nesne 6) — kural BİLEREK kullanılır, bedel budur
TOPLAM:    7 sahne · 6 farklı nesne ✅ (kapı ≥3 sahne / ≥2 nesne)
```

### ⛔ A4 YASAKLI SAHNE TİPİ DENETİMİ [03_PLAN_ONCESI]

```
· araç BİNİŞ / İNİŞ / KALKIŞ hareketi   → 0 kare. Lander S0'da zaten
  inmiş, S24'te hâlâ yerde. S23 kliplerinden hiçbiri araca temas anını
  içermez; yürüyüş klip bitmeden sona erer.       [D69 ① · D148]
· tek ışıklı loş iç mekâna GİRİŞ        → 0 sahne (film tamamen dış mekân)
· aynalı-yansıtıcı yüzey önünde figür   → 0 sahne; vizör optik berrak,
  yansıma SIFIR yazılır                            [D20 · D69 · D79]
· novum TÜRETİLMİŞ optik fenomende      → HAYIR. Taşıyıcı katı bir kazık
  ve fiziksel bir gaz akışıdır; gölge/yansıma/parlama DEĞİL   [D73]
· novum bir YOKLUK taşıyor              → HAYIR ve bu bilinçli bir karar:
  filmin bıraktığı işaret bir DELİK değil, delikten çıkan DİKEY BEYAZ GAZ
  SÜTUNUDUR. Delik yalnız kuralın sonucudur; final karesindeki nesne
  sayılabilir ve VARDIR (2 sütun).                            [D76 · D141]
· jenerik / başlık kartı çıktısı        → 0 kare (kurgu kapısı ayrıca)
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2.2 → 25 sahne)

| # | vuruş | % | sahne | not |
|---|---|---|---|---|
| 1 | Açılış imajı | %0-4 | S0 | Kapanış imajıyla ÇİFT: bir şey İNİYOR ↔ iki şey DURUYOR |
| 2 | Kurulum | %0-16 | S0-S4 | Dünya + ikisinin işi + yetkinlikleri |
| 3 | **Katalizör** | **%5,6 = 0:14** | **S1** | Kısa boylu olan bırakır, kazık kendi başına yarım metre daha iner — ⛔ 0:15 sınırının içinde |
| 4 | Tartışma | %16-28 | S5-S6 | Mühendislik cevabı denenir (basınç plakası) ve TUTMAZ |
| 5 | Orta nokta (sahte yenilgi) | %50 | S12 | Dikilen kazık devrilir ve boyunca batmaya başlar |
| 6 | Umut-önce-düşüş | %69 | S17 | Ufuktaki sütunun ne olduğunu ANLARLAR |
| 7 | Her Şeyin Kaybı | %75 | S18 | VAZGEÇİŞ: kasayı toplayıp araca dönerler; kazık arkalarında yatık ve yarı gömülü, ova işaretsiz, bacakta tek kademe kaldı. Geldikleri iş yapılamadı — somut ve geri dönülmez |
| 8 | **Merkezi seçim** | %78 | **S19** | Çekirdek kasadan kaldırılır — seçim EKRANDA tamamlanır |
| 9 | Doruk | %84 | S21 | Sütun kalkar; filmin en pahalı karesi · ⭐ KAPAK ANI B |
| 10 | İkinci seçim [D158 B2a] | %89 | S22 | Kazığı bilerek yatırıp sütunu gösteren bir iz bırakır |
| 11 | Kapanış imajı | %100 | S24 | İki sütun — twist: ilk gelenler onlar değildi |

```
⛔ BOŞ VURUŞ YOK. "Her Şeyin Kaybı" SOMUTTUR: boş çekirdek yuvası ve
   boş kasa beşiği aynı karede görünür (S18).
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU (§4)
                 Tamamen normal bir sahne — iki eldiven karda bir kazık
                 dikiyor — ve TEK anormal öğe: kazık durmuyor.
                 ⚠️ §4'ün risk satırı: anomali TÜRETİLMİŞ fenomen olursa
                   [D73] hook doğmaz. Burada anomali KATI BİR NESNE ve
                   FİZİKSEL BİR AKIŞTIR; tek-kare fizibilitesi §4① ile
                   geçildi. Tek tip kullanıldı, ikinci tip bindirilmedi.
S0 SORUSU:       "Zemin neden kazığı yutuyor?"
S1 İKİNCİ BİLGİ: Kazık durmuyor — bırakınca kendi başına iniyor.
                 0:14'te soru DEĞİŞİR: "yutuyor mu?" → "hiçbir şey
                 burada durabiliyor mu?"  (katalizör ≤0:15 ✅)
0. KARE:         örüntü kesintisi = rüzgârsız, sessiz bir dünyada
                 kendiliğinden fışkıran dikey beyaz gaz halkası;
                 süren hareket = kazık inmeye devam ediyor.
                 ⛔ 120 px testi MAKİNEYLE koşulacak (§0②) — üretimden
                   sonra, kare 120 px'e indirilip kontrast ölçülür.
BİLGİ ASİMETRİSİ: YOK — bilinçli karar. İzleyici ile karakterler AYNI
                 anda öğrenir; filmin gerilimi asimetriden değil
                 tekrarlanan başarısızlıktan gelir. (§3.1)
İLK 2 SN SESİ:   diegetik TEK ses — kask içi tek nefes. Müzik 0:09'a
                 kadar hiç girmez (erken müzik girişi elendi).
TOHUM BİLGİ:     S3 · 0:31-0:33 (pencere 25-38 s ✅) — ufuk çizgisinde
                 ince dikey beyaz çizgi, 2 saniye, kadrajın sağ üçte
                 birinde. ⛔ Karakterin bakışıyla VURGULANMAZ.
                 GERİ DÖNÜŞ: S16 ve S24 aynı ufka görsel olarak döner.
HOOK ↔ KAPANIŞ:  S0 tek nesne AŞAĞI gidiyor ↔ S24 iki nesne YUKARI duruyor.
                 İki imaj yan yana konduğunda değişim okunur ✅ [§2.3③]
```

---

## 🗺️ SAHNE HARİTASI

> Kurulum sütunu: `ACI_YAYI §3` güvenli bant (ardışık çift ≥1 ölçek kademesi
> VE ≥45°) · `KAMERA_ACISI §2` açı tipi · `KURGU_RITMI §2` örüntü kırıcı.
> **AZ** = kamera konumunun ova pusulasındaki azimutu (aşağıdaki harita).

| S | t | başlık | olay | kurulum (ID · lens · ölçek · açı · AZ) | ses | bütçe |
|---|---|---|---|---|---|---|
| S0 | 0:00 | THE FIRST TOUCH | Kazık ayağı kara değer, gaz halkası, 20 cm iner | **E** 100mm · ECU · göz hizası 0,35 m · AZ 200 | tek nefes | ✋ el · açılış imajı |
| S1 | 0:09 | IT DOES NOT STOP | İkisi tutar; 0:14'te kısa boylu bırakır, kazık yarım metre daha iner | **D** 85mm · CU · alt açı 18° · AZ 260 | nefes + eklem gıcırtısı | 🔁 tepki · ⭐KATALİZÖR |
| S2 | 0:19 | BOTH HANDS OFF | İkisi geri çeker, kazık kendi başına iner, izlerler | **C** 50mm · MS · üst açı 30° · 2,0 m · AZ 340 | iki nefes | 🔁 tepki |
| S3 | 0:29 | THE PLAIN | Uzun boylu ufku tarar; arkada ince dikey beyaz çizgi 2 s | **B** 35mm · WS · göz hizası 1,6 m · UFUK KİLİDİ · AZ 50 | sessiz | 👁️ göz · ⭐TOHUM |
| S4 | 0:39 | THE WHOLE WORLD | Ova · mekik ÜÇTE İKİ PROFİLDEN TAM BOY (dört pabuç, dört gaz sütunu) · kara disk · yukarıda halka gemi | **A** 24mm · EWS · üst açı 30° · 4 m (aracın kuyruğunun arkası) · AZ 220 | sessiz | 🌌 ölçek 1:10 |
| S5 | 0:49 | THE SECOND TRY | Geniş basınç plakası serilir, kazık üstüne dikilir — 4 s durur | **B2** 35mm · WS · alt açı 22° · 0,4 m · AZ 300 | çift ayak sesi (gövdeden) | 🔁 tepki |
| S6 | 0:59 | THE PLATE GOES TOO | Plakanın TÜM çevresinden halka; plaka da iner | **F** 50mm · MS · OTS · 1,5 m · AZ 130 | nefes hızlanır | ⭐BAŞARISIZ DENEME [B2b] |
| S7 | 1:09 | WHAT THEY BROUGHT | Kasa açılır: beşikte pürüzsüz beyaz silindir. Kasanın dört köşesi iniyor | **G** 85mm · CU · üst açı 30° · 1,8 m · AZ 20 | mandal · eldiven | 🎒 eşya · Çehov |
| S8 | 1:19 | COLD HANDS | Eldivenler kazık ayağını gevşek karla doldurup soğutur | **H** 100mm · ECU · TEPE 90° · 1,3 m | yalnız nefes | ✋ el · ⭐VİRAL #1 |
| S9 | 1:29 | IT STANDS | Soğutulmuş kazık dikilir ve DURUR; uzun boylu elini açar | **D** 85mm · CU · alt açı 18° · AZ 260 | tek uzun nefes | 🔁 tepki · küçük zafer |
| S10 | 1:39 | THE LEAN | Kazık dikilmiş ama ALTINDAKİ zemin çöküyor; kazık eğiliyor | **C2** 50mm · MS · göz hizası 1,6 m · AZ 170 | sessiz | kural genelleşir |
| S11 | 1:49 | THE BOWL | Çalıştıkları alan 10 m çapında bir çanağa dönmüş; lander bacağının üç kademesinden ikisi kar altında | **B3** 35mm · WS · üst açı 30° · 6 m · AZ 90 | uzak gövde uğultusu | ⭐SAYAÇ (3→1 kademe) |
| S12 | 1:59 | THE MAST GOES DOWN | Kazık yavaşça devrilir ve boyunca batmaya başlar; ikisi geri çekilir, dokunmaz | **A2** 24mm · EWS · göz hizası 1,6 m · UFUK KİLİDİ · AZ 10 | sessiz | ⭐ORTA NOKTA · VİRAL #2 |
| S13 | 2:09 | PULLING IT BACK | İkisi halatla kazığı çanaktan bakir kara çeker | **B2** 35mm · WS · alt açı 22° · 0,4 m · AZ 300 | halat + iki adım kadansı | 🚶 yürüyüş · 🔁 tepki |
| S14 | 2:19 | THE HORIZON AGAIN | Uzun boylu durur; ufuktaki dikey çizgi bu kez 10 saniye kadrajda | **F** 50mm · MS · OTS · 1,5 m · AZ 130 | sessiz | ⭐TOHUM 2. geçiş |
| S15 | 2:29 | READING IT | Vizörün ardındaki yüz: gözler yana kayar, durur, kilitlenir | **G** 85mm · CU · üst açı 30° · 1,8 m · AZ 20 | tek nefes | 👁️ göz · Kuleshov |
| S16 | 2:39 | THE COLUMN ON THE HORIZON | Yalnız ufuk ve üstünde duran tek ince dikey beyaz sütun. İnsan yok | **J** 200mm · ECU · göz hizası 1,6 m · UFUK KİLİDİ · AZ 100 | MUTLAK SESSİZLİK (müziksiz sahne) | ⭐VİRAL #3 · 0 insan |
| S17 | 2:49 | THE UNDERSTANDING | Uzun boylu çekirdeği kaldırıp kısa boyluya gösterir | **D** 85mm · CU · alt açı 18° · AZ 260 | iki nefes | 👁️ göz · umut-önce-düşüş |
| S18 | 2:59 | THE LAST SECTION | İkisi kasayı taşıyıp araca doğru yürür — vazgeçiş; arkalarında kazık yatık ve yarı gömülü, ova İŞARETSİZ; iniş bacağında tek kademe kaldı | **C** 50mm · MS · üst açı 30° · 2,0 m · AZ 340 | çift adım kadansı | ⭐HER ŞEYİN KAYBI · ⚠️KART 9 |
| S19 | 3:09 | THE CHOICE | Durup kasayı açarlar; kısa boylu avucunu çekirdeğe yatırır (onay), uzun boylu onu beşikten kaldırır (karar) — beşik boş kalır | **B** 35mm · WS · göz hizası 1,6 m · AZ 50 | ortak tutulan nefes | 👁️ göz · ⭐MERKEZİ SEÇİM |
| S20 | 3:19 | THE PILOT HOLE | Çekirdek bakir kara bırakılır; hızla iner, 10 s'de görünmez olur, geriye dikey gaz sütunu kalır | **H** 100mm · ECU · TEPE 90° · 1,5 m | tek nefes | ⚡ŞOK #1 · ⭐VİRAL #4 |
| S21 | 3:29 | THE COLUMN | Sütun kadrajın üstünden çıkar; iki figür geri çekilmiş bakar | **B2** 35mm · WS · alt açı 25° · 0,3 m · AZ 300 | derin nefes | ⚡ŞOK #2 · ⭐DORUK · KAPAK B |
| S22 | 3:39 | LAYING IT DOWN | Uzun boylu kazığı bakir kara YATIRIR; kazık boyunca batıp sütunu gösteren düz bir hendek bırakır | **C2** 50mm · MS · göz hizası 1,6 m · AZ 170 | tek adım · sessizlik | ⭐İKİNCİ SEÇİM [D158 B2a] |
| S23 | 3:49 | GOING | İkisi kameraya (araca) doğru yürür, kasa aralarında; yukarıda gemi halkayı ikinci kez geçer; klip onlar varmadan biter [D69] | **K** 35mm · WS · göz hizası 1,5 m · KAMERA HEDEFTE · AZ 220 | çift adım kadansı | 🚶 yürüyüş · ⚠️KART 9 V3 |
| S24 | 3:59 | TWO COLUMNS | Boş ova — insan 0, araç 0. Yakında yeni sütun, aralarında düz sığ hendek, ufukta eski sütun. İkisi aynı parlaklıkta | **A2** 24mm · EWS · göz hizası 1,6 m · UFUK KİLİDİ · AZ 10 | mutlak sessizlik | ⭐KAPANIŞ · TWIST |

```
AÇI TİPİ SAYISI: 5 ≥3 ✅  — göz hizası · alt açı · üst açı · tepe · OTS
                 (KAMERA_ACISI §2 sekizlisinden beşi)
KURULUM SAYISI:  14  ⚠️ BANT ÜSTÜ (betik ölçtü: 25 sahnede üst bant 13) — GEREKÇE [D74]:
                 üç kurulum kapı zorunluluğudur, estetik tercih değil.
                 ① K (S23) = KART 9'un iki-yenilgi kuralı: hedefe yürüyüş
                   sahnesinde kamera HEDEFE taşınır [UZAMSAL §6.8 V3].
                 ② A2 ve ③ J = D145 ufuk kilidi: alçak/göz hizası, ufku
                   İÇEREN kurulum olmadan düz ova kanyona dönüyor.
                 Bu üçü çıkarılırsa 11 olur — yani sapma tam üç kapıdır.
ABARTI BANDI:    dutch 0° (hiç yok) · alt açı 18-25° (bant 15-30 ✅) ·
                 üst açı 30° (bant 15-30 ✅) · tepe 90° (ayrı tip)
                 ⛔ 35°+ dutch, 45°+ alt açı, 45-60° üst açı: 0 sahne
BÖLÜM KESİĞİ:    S12 ile S13 arasında.
                 S12 = A2 · EWS(1) · göz hizası · AZ 10
                 S13 = B2 · WS(2)  · alt açı 22° · AZ 300
                 → ölçek 1 kademe ✅ · azimut 70° ✅ · pitch 0°→22° ✅
⚡ŞOK BANDI:      2 adet, ikisi de işaretli ve bilinçli (üst sınır 2 ✅)
                 S19 WS → S20 ECU (3 kademe) — eylemin başladığı an
                 S20 ECU → S21 WS (3 kademe) — sonucun göründüğü an
TEPE KURULUMU (H): tepe çekimin azimutu anlamsızdır; H ile komşuları
                 arasındaki ≥45° farkı PITCH taşır (30°→90° ve 90°→18°).
```

### 🧭 UZAMSAL HARİTA — kuşbakışı (`UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md`)

```
                        000°  KARA DELİK (gökte, yükseklik 34°) — HİÇ HAREKET ETMEZ
                          |
        eski sütun 100° ——+—— ÇALIŞMA YERİ (0,0)  ← kazık · çanak · yeni sütun
        (40 km, ufukta)   |
                        220°  LANDER (40 m)

EKRAN YÖNÜ KİLİDİ:
  · Kara delik pusulada 000°'de SABİTTİR. Kadrajda göründüğü her sahnede
    hangi azimuttan bakıldığını o söyler; ekran yönü kurulum azimutundan
    TÜRETİLİR, sahne sahne uydurulmaz.
  · Lander HER sahnede 220° yönündedir — yani kara deliğin TERSİ tarafta.
    Bu bilinçli: hedefe hareket ile baskın ışık AYNI yönde olmasın diye
    (KART 9 ışık mıknatısı yalıtıldı).
  · Eski sütun 100°'de; S3 · S14 · S16 · S24'te AYNI pusula yönünde durur.
⚠️ Sıçrama açıyı değiştirir, COĞRAFYAYI DEĞİŞTİRMEZ.
```

### ⚡ ÖRÜNTÜ KIRICI DENETİMİ (`KURGU_RITMI §2`)

```
MİKRO (her kesme bir kırıcı taşır): ölçek merdiveni 25 sahnede hiç
  duraklamaz — ardışık her çift en az 1 kademe ayrı (2 bilinçli şok hariç).
MAKRO (her 3-4 sahnede mekân/tempo): S0-S2 kazık dibi → S3-S4 ova →
  S5-S9 çalışma → S10-S12 çanak → S13-S16 ufuk → S17-S19 kasa →
  S20-S22 yeni delik → S23-S24 ayrılış.
PALET: tek palet (beyaz-siyah) — ⛔ bu filmde renk kırıcısı YOK.
  Telafisi ÖLÇEK ve SES dokusudur; ardışık iki sahne aynı ölçekte VE
  aynı ses dokusunda hiç değildir.
SES DOKUSU: nefes · eklem · halat · adım · gövde uğultusu · MUTLAK
  SESSİZLİK (S16 · S24). Sessizlik burada bir dokudur, yokluk değil.
```

---

## 🔧 REVİZYON 1 — ARAÇ TASARIMI  (02.09.2026 · sahip geri bildirimi)

```
SAHİP: "sahne 0,1,2,3 hazır ama sahne 4 ve sonrasında uzay mekiği çok kötü,
        yıldızlar arasındaki gibi olmalı"
```

**Neden bedelsiz yapılabildi:** üretilen dört sahnenin (S0-S3) hiçbirinde
araç yok. S0 kazık ayağı ECU · S1 kazık CU · S2 iki figür MS · S3 ova WS.
Araç ilk kez S4'te giriyor → **üretilen tek kare çöpe gitmedi.**

| | ÖNCE | SONRA |
|---|---|---|
| İNİŞ ARACI | dört bacaklı, 9,0 m YÜKSEK, dikey duran araç | **taşıyıcı gövde (lifting body) mekik** — 14,0 × 9,0 m, kuyrukta yalnız 4,2 m; ALÇAK ve UZUN. Kanat ayrı parça DEĞİL, gövdenin kendisi kanat. Küt burun · üç camlı dar pencere şeridi · arka köşelerde iki yatık kanatçık · kuyrukta iki gömük sönük lüle · karından açılan dört kısa strut (üç teleskopik kademe korunuyor) |
| YILDIZLARARASI GEMİ | 140 m düz omurga + üstünde iki halka | **kapalı halka** — kenar kenara eklenmiş on iki özdeş modül, tam çember, 64 m; dördü radyatörlü ve 12/3/6/9 saat konumunda (yönelim kilidi) |
| S4 KAMERA | 9,0 m, aracın kanadının üstünden | **4,0 m, kuyruğun 6 m arkasından** — araç artık ÜÇTE İKİ PROFİLDEN TAM BOY kadrajda (sahip aracı görmek istiyor, o hâlde araç GÖSTERİLİR) |

**⛔ KOPYA SINIRI [MESHUR_SAHNE §4].** Sahibin referansı bir FİLMDİR; film adı,
marka ve tescilli tasarım adı hiçbir prompta YAZILMADI. Referans, telifin
korumadığı tarafa — **geometriye, orana, malzemeye** — çevrildi ve gerçek
donanıma bağlandı:
```
taşıyıcı gövde mekik → NASA X-24A / X-24B ve HL-10 (1966-1975) · Dream Chaser
kapalı halka gemi    → von Braun 1952 dönen tekerlek · NASA Nautilus-X (2011)
```
Böylece kanalın "her film gerçek bir kuralla tartışır" tezi de bozulmadı;
YAYIN_PAKETI'nin VERIFIED SCIENCE alanına iki satır daha eklenebilir.

**⚠️ FİZİK İTİRAZI VE CEVABI — dürüst kayıt.**
15 µbar'da kanat hiçbir şey yapmaz; bu mekiğin kanatlı olması bir çelişki
gibi görünür. Değildir ve gizlenmez: mekik seferin ATMOSFERLİ dünyalara da
inebilen çok amaçlı aracıdır, buraya kanatlarıyla gelmiştir ve burada o
kanatlar ölü ağırlıktır. **Filmin kuralıyla aynı cümleyi kurar:** bu
gezegende hiçbir şey yapmak için tasarlandığı şeyi yapamıyor.
⛔ Bu gerekçe PROMPTTA AÇIKLANMAZ — yalnız görünür.

**⭐ REVİZYONUN BEDAVA KAZANCI — ÜÇ ÇEMBER MOTİFİ:**
gökte kara deliğin **parlak halkası** · gökte geminin **beyaz halkası** ·
yerde çekirdeğin açtığı **yuvarlak ağız**. Ölçekler 10^11 : 10^2 : 10^-1 ve
ilk ikisi S4 ile S23'te AYNI KAREDE. Tema tarafı: film zaten "bırakılan iz"
üstüne kurulu; şimdi üç ölçekte aynı biçim tekrarlanıyor.

**Dokunulan dosyalar:** PLAN (World Bible · Camera Bible A · sahne haritası
S4) · BOLUM_1 (S4 · S11 imaj+video) · BOLUM_2 (S18 · S23 imaj+video) ·
REFERANS_PAKETI (RA 4→5 panel yeniden yazıldı · RB 1→2 panel, öncelik
🟡→🟠). **S0-S3'e tek karakter dokunulmadı.**

**Yeni negatif kilitleri** (her araç sahnesinde): `the hull IS the wing — no
bolted-on wings, no swept airliner wings, no propellers, no rocket fins, and
it is not a tall vertical rocket` · `the distant ship stays a closed unbroken
ring — no spine, no cylinder, no broken arc`.

⛔ **ÜRETİM SIRASI DEĞİŞTİ:** RA ve RB referans sayfaları ONAYLANMADAN S4
üretilmez. RA'nın kabul sınavı (§5 sonu) iki maddeyle koşulur: yandan oran
14:4,2 mi · üstten kanat gövdeden ayrı mı. İkincisi ✗ ise sayfa RET.

---

## 🚦 KAPI KOŞUSU — `prompt_kontrol.py`, üretimden ÖNCE (02.09.2026)

```
KOMUT   python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
          yatay_4_dk_filmler/THE_SINKING_STAKE
ÇIKTI   📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik · 50 prompt
        ⛔ 0 BLOCK · ⚠️ 0 FIX · ✅ 1 GO
⛔ Klasör modu koştu (satır çıktıda var). Dosya modu tek başına koşulursa
   dizi kapıları bölüm sınırında körleşir ve ⑬/⑭ PLAN'ı göremez.
```

**Koşuda çıkıp DÜZELTİLEN bulgular** — kaydı olmayan kapı koşulmamış kapıdır [D74]:

| bulgu | kaç yerde | ne yapıldı |
|---|---|---|
| ⑯ T2 politika sözlüğü · `dead` yığılması | 40+ | `dead-straight` → `perfectly straight`. Bedava nötr hâl vardı; D123'ün tam olarak uyardığı yığılma |
| ⑯ T2 · `blast` ×2 + `explosion` ×1 (S20 IMAGE NEGATIVE) | 1 prompt | Yasak cümlesi TARİFE çevrildi: "the surface around it stays intact, level and unbroken to the edge of the frame". D123: yasak, yasakladığı kavramı prompta SOKAR |
| ⑯ T2 · `body-widths` | 1 | ölçü nesne göreli yazıldı ("half again as tall as a person") |
| §7 yasak kelime `swirl` [D39] | 5 | → `drift`. Toz/gaz sıvı gibi akıyor tuzağı |
| negatif çekirdek imzası: insan sayısı | 30+ prompt | "exactly two human" betiğin imzasına girmiyordu; "the human count in this film is two" yazıldı |
| ⑮ SIRT POZİTİF yanlış-pozitifi (S10) | 1 | "plain running behind them" → "plain beyond them"; kamera arkada değil, cümle ovayı anlatıyordu |
| ⑦ çapasız `toward` | 4 | hedefin ekran konumu AYNI cümleye yazıldı (S11 · S12 · S18 · S23) |
| araç yönelim kilidi yok (uzamsal §5.1) | 10 geçiş | "its one closed hatch face angled screen-left and its orientation never changes" — S4 · S11 · S18 · S23 |
| S16 · S24 kısa Style satırı imzasız | 4 prompt | KART 10 gereği uzun NEGATIVE bloğu yok; imzalar POZİTİF Style satırına indi [D59] |

### ⚠️ BİLİNÇLİ SAPMA 1 — KURULUM SAYISI 14 (üst bant 13)

Gerekçe sahne haritasının altında yazılı: üç kurulum estetik tercih değil
KAPI ZORUNLULUĞUDUR — **K** (S23) KART 9'un iki-yenilgi kuralı için kamerayı
hedefe taşır [UZAMSAL §6.8 V3]; **A2** ve **J** D145'in ufuk kilidini taşır.
Bu üçü çıkarılırsa 11 olur. Sapma tam üç kapıdır ve ölçülebilir.

### ⚠️ BİLİNÇLİ SAPMA 2 — PROMPT UZUNLUK BANDI (video tarafı)

```
ÖLÇÜM (kapı koşusu, 02.09.2026)
  video   1.704 - 3.374 karakter   (bant 2.000-2.600 · tavan 4.300)
  image   1.476 - 4.193 karakter   (tavan 4.300 · image bandı ÖLÇÜLMEDİ)
  ⛔ TAVANI AŞAN PROMPT: 0. Bant üstü: 16 video promptu.

NEDEN BANT TUTMUYOR — aritmetik, tercih değil:
  Bu filmin ZORUNLU blokları tek bir video promptunda şunlar:
    · iki insanlı kimlik kilidi (geometrik ayrım — renk kanalı yok)  ~330
    · D79/D139 sırt + vizör pozitif kilidi                            ~150
    · D154'ün SAYILI gaz cümlesi (her gaz sahnesinde ZORUNLU)         ~300
    · D154 ③ adım kadansı + 0,40 g fizik satırları                    ~250
    · TIMELINE (10 s'lik olayın kendisi)                              ~600
    · KART 9 dört kanal (yalnız S18 · S23)                            ~400
  Toplam zorunlu taban ≈ 2.400-2.800; bant tavanı 2.600.
  Yani bant, İKİ İNSANLI + tekrarlayan doğa olaylı bir filmde
  matematiksel olarak dolu geliyor.

NE YAPILDI: iki tur sıkıştırma koşuldu (~5.400 karakter düştü) —
  SCENE bloğu LOCKS ile birleştirildi, tekrar eden negatifler tekilleştirildi,
  sarım normalize edildi. Hiçbir KAPI İMZASI silinmedi.

⛔ İLK RED PROTOKOLÜ [§7 · Third Dune deseni]:
  · İlk red gelirse promptu KISALTMA — önce mesaj tipini sınıflandır
    (POLİTİKA / TEKNİK / YAPISAL · REHBER §7 ayrım tablosu).
  · Aynı filmde arka arkaya red gelip HİÇ geçen prompt yoksa sorun
    prompt değil ÜRETİM TARAFIDIR → §7 adım 4 probunu koş.
  · Üçüncü yeniden yazımdan önce prob BAŞA alınır.
  · Her red `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md`'ye satır açar
    ve MOTOR sütunu BOŞ BIRAKILMAZ.
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** sabitlenir ve her IMAGE promptuna
> tam yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).

### 👤 CHARACTER BIBLE — iki isimsiz figür [D34: özel ad promptta geçmez]

```
IMAGE PROMPTLARDA (kelimesi kelimesine — parafraz yasak):

Exactly two human figures in this film and no others. THE TALLER ONE is
about one hundred eighty-eight centimetres, broad-shouldered, dark brown
skin, close-cropped grey hair, deep lines at the outer eyes, mid-fifties.
THE SHORTER ONE is about one hundred sixty-five centimetres, slight,
pale freckled skin, red-brown hair pressed flat under the helmet ring,
early thirties. Both wear the same matte white surface suit: a hard white
torso shell over soft white limb layers, white gloves, white boots, no
colour anywhere on either suit. The back of each suit is one continuous
smooth white panel from collar to hip, unbroken, carrying nothing. Each
helmet is a hard white shell with one flat front pane of optically clear
glass, zero tint, zero mirror coating and zero reflection of the
environment; the face is fully readable through it at every head angle.
THE TALLER ONE carries a rigid white chest yoke with two vertical tool
loops, a white cuff on the left forearm only, and four flat white pouches
around the hips. THE SHORTER ONE has a flat chest with no yoke, a wide
white belt at the hips with a coiled white line at the right hip, two
flat pouches on each thigh and a white cuff on both forearms. Nothing on
either suit carries a patch, a mark, a stripe or a printed shape of any
kind — every surface is plain white.

VIDEO PROMPTLARDA (kompakt kilit satırı):
Exactly two humans total — the taller broad-shouldered one in the white
suit with the rigid chest yoke, and the shorter slight one with the flat
chest and the coiled white line at the right hip. Plain white suits, no
marks. Flat back panel on both, no back-mounted unit. Clear helmet pane,
both faces readable.

⛔ AYIRT ETME KANALI GEOMETRİDİR, RENK DEĞİLDİR: göğüs boyunduruğu
   (uzun boylu) ↔ düz göğüs + kalça halatı (kısa boylu) + boy farkı
   23 cm. İkisi de tepeden tırnağa beyazdır — sahibin isteği budur ve
   ayırt etme yükü tamamen SİLUETE bindirilmiştir.
⛔ KISALTMA YASAK [D155 ②]: "EVA", "MAV", "PLSS" gibi büyük harfli
   kısaltma hiçbir prompta yazılmaz — model onu giysiye BASILMIŞ bir
   etiket sanır. "surface suit" · "pressure suit" yazılır.
⛔ FAZ ETİKETİ YASAK [D155 ①]: "Wear state: PHASE n" hiçbir prompt
   gövdesinde geçmez. Bu filmde kir merdiveni ZATEN YOKTUR (aşağıya bak).
```

### 🌍 WORLD BIBLE

```
GEZEGEN: Yıldızı olmayan kayaç bir dünya. Süper kütleli bir kara deliğin
  çevresinde, deliğin yarıçapının yaklaşık 30 katı uzaklıkta, kararlı bir
  yörüngede. Kilitli dönüşlü — kara delik gökte HİÇ hareket etmez.

ZEMİN: Katı azot karı, 44 K. Koyu ana kayanın üstünde 0-3 m kalınlıkta.
  İnce taneli, mat beyaz, KABUKSUZ. Buz parlaklığı YOK, ıslaklık YOK,
  yansıma YOK. Kar hiçbir karede ERİMEZ — katıdan doğrudan gaza geçer.

ATMOSFER: azot buharı ~15 µbar — pratikte vakum.
  RÜZGÂR: SIFIR. Hiçbir karede hiçbir şey esmez, savrulmaz, dalgalanmaz.
  SES: dışarıda yok. Duyulan her ses giysinin İÇİNDEN gelir.

GÖKYÜZÜ: siyah. 000° azimut, 34° yükseklikte kusursuz siyah bir disk,
  3,2° çapında (Dünya'dan görülen dolunayın yaklaşık altı katı genişlik).
  Diskin kenarında ince, parlak, kesintisiz beyaz bir halka. Halkanın
  dışında yıldız alanı ince eşmerkezli yaylara gerilmiş.
  ⛔ YIĞILMA DİSKİ YOK. Plazma yok, turuncu yok, kızıl yok, spiral yok,
    akış yok. Yalnız siyah disk + ince beyaz halka + gerilmiş yıldızlar.
    Sebep: yığılma diski olsaydı bu gezegen donmuş olamazdı.

IŞIK: TEK kaynak o halka. Ova üstündeki aydınlık parlak bir dolunay
  gecesi kadardır. Kar %90 yansıttığı için gölgeler YUMUŞAK ve DOLGULU,
  hiçbir gölge siyah değil. Işık 000° azimut / 34° yükseklikten gelir ve
  25 sahnenin 25'inde AYNIDIR — gün yok, hava yok, döngü yok.
  ⭐ IŞIK TAKVİMİ bu yüzden trivial monotoniktir [KART 6b elendi].

LANDER — ⭐ TAŞIYICI GÖVDE (lifting body) MEKİK  [02.09.2026 · sahip revizyonu]
  Beyaz, alçak ve geniş bir TAŞIYICI GÖVDE mekiği: kanat ayrı bir parça
  değildir, GÖVDENİN KENDİSİ kanattır. 14,0 m uzun · 9,0 m kanat açıklığı ·
  kuyrukta yalnız 4,2 m yüksek (bir buçuk insan boyu). Karnı düz, burnu
  küt ve yuvarlak; burun üstünde ÜÇ düz camdan dar bir pencere şeridi;
  arka köşelerde dışa doğru hafif yatık İKİ alçak dikey kanatçık; kuyrukta
  İKİ gömük, içi karanlık motor lülesi (parıltı YOK). Yüzey mat beyaz
  seramik panel — ince panel dikişleri görünür, üst gövdede hafif kapitone
  ısı örtüsü dokusu. Sol yanda TEK gömme kapak, kapalı. Hiçbir yerinde
  işaret yok.
  Karnından açılan DÖRT kısa iniş ayağı; her ayak çapı aşağı doğru DARALAN
  ÜÇ teleskopik beyaz kademeden yapılır ve 900 mm'lik yuvarlak bir pabuçla
  biter. Açık hâlde ayak boyu 1,4 m — gövde karnı kardan bir kol boyu
  yukarıda durur.
  ⛔ Bacakta ÇENTİK, ÇİZGİ, DERECELENDİRME YOK — sayaç kademe SAYISIDIR.

  ⭐ NEDEN KANADI VAR — ve neden bu bir kusur değil, tema:
  15 µbar'da kanat hiçbir şey yapmaz. Bu mekik seferin ATMOSFERLİ dünyalara
  da inebilen çok amaçlı aracıdır; buraya kanatlarıyla gelmiştir ve burada
  o kanatlar ölü ağırlıktır. Filmin kuralıyla aynı cümleyi kurar: bu
  gezegende hiçbir şey yapmak için tasarlandığı şeyi yapamıyor.
  ⚠️ Bu bilinçli bir seçimdir ve promptta AÇIKLANMAZ; yalnız görünür.

  📐 TASARIM SOYU (gerçek donanım — kanal tezini bozmaz):
  NASA X-24A / X-24B ve HL-10 taşıyıcı gövde araçları (1966-1975) ·
  Dream Chaser (bugün uçuyor). ⛔ Hiçbir film adı, marka ya da tescilli
  tasarım adı promptta geçmez [MESHUR_SAHNE §4 kopya sınırı].

YILDIZLARARASI GEMİ — ⭐ KAPALI HALKA  [02.09.2026 · sahip revizyonu]
  Beyaz, KAPALI BİR HALKA: kenar kenara eklenmiş ON İKİ ÖZDEŞ beyaz modül
  tam bir çember kuruyor, çember çapı 64 m. Modüllerin dördü kısa yassı
  radyatör kanatları taşır ve bu dördü halkanın 12 · 3 · 6 · 9 saat
  konumlarındadır (yönelim kilidi — uzamsal §5.1). Mat beyaz, ince panel
  dikişli. Işık YOK, parıltı YOK, motor izi YOK.
  Kadrajda YALNIZ gökte ve YALNIZ CEPHEDEN görünür — o yüzden bir pirinç
  tanesi büyüklüğünde İNCE BEYAZ BİR HALKA olarak okunur (S4 ve S23).
  Yüzeye hiç inmez, hiçbir karede yakın plan değildir.

  ⭐ ÜÇ ÇEMBER MOTİFİ (bu revizyonun bedava kazancı):
  gökte kara deliğin PARLAK HALKASI · gökte geminin BEYAZ HALKASI ·
  yerde çekirdeğin açtığı YUVARLAK AĞIZ. Üçü de daire, üçü de aynı filmde,
  ölçekleri 10^11 : 10^2 : 10^-1. S4 ve S23'te ilk ikisi AYNI KAREDE.

  📐 TASARIM SOYU (gerçek donanım): von Braun'un 1952 dönen tekerlek
  istasyonu · NASA Nautilus-X santrifüj konsepti (2011).
```

### 🎥 CAMERA BIBLE — 14 kurulum

```
ID  lens    ölçek  yükseklik / açı        AZ    sahneler
──────────────────────────────────────────────────────────────
E   100mm   ECU    0,35 m · göz hizası    200   S0
D    85mm   CU     0,30 m · alt açı 18°   260   S1 · S9 · S17
C    50mm   MS     2,00 m · üst açı 30°   340   S2 · S18
B    35mm   WS     1,60 m · göz · UFUK     50   S3 · S19
A    24mm   EWS    4,00 m · üst açı 30°   220   S4
B2   35mm   WS     0,40 m · alt açı 22°   300   S5 · S13 · S21 (S21: 25°)
F    50mm   MS     1,50 m · OTS           130   S6 · S14
G    85mm   CU     1,80 m · üst açı 30°    20   S7 · S15
H   100mm   ECU    1,30 m · TEPE 90°       —    S8 · S20 (S20: 1,50 m)
C2   50mm   MS     1,60 m · göz hizası    170   S10 · S22
B3   35mm   WS     6,00 m · üst açı 30°    90   S11
A2   24mm   EWS    1,60 m · göz · UFUK     10   S12 · S24
J   200mm   ECU    1,60 m · göz · UFUK    100   S16
K    35mm   WS     1,50 m · göz · HEDEFTE 220   S23

KAMERA HAREKETİ: 25/25 sabit lockoff. Klip içinde zoom yok, pan yok,
  tilt yok, track yok, sarsıntı yok.  [KART 8 — klip İÇİ karar]
SAHNELER ARASI: kurulum HER sahnede değişir; bu karardan MUAFTIR ve
  zorunludur [KART 8 kapsam bloğu · 26.08.2026].
⛔ UFUK KİLİDİ (B · A2 · J · K) [D145]: bu kurulumların promptunda
  "the horizon is in frame and level; above the plain there is only
  black sky" cümlesi ZORUNLUDUR — alçak açıda boş üst alan bırakan
  kadraj modele kanyon duvarı icat ettiriyor.
⛔ OTS KURULUMU (F · S6 · S14) [D139 · ⑮ kapısı]: kamera omuz üstünde
  olduğu için bu iki promptta POZİTİF sırt yüzeyi cümlesi ZORUNLUDUR.
```

### 💡 LIGHTING BIBLE

```
TEK KAYNAK: kara deliğin çevresindeki ince parlak halka — 000° azimut,
  34° yükseklik, 25 sahnenin 25'inde AYNI.
YOĞUNLUK: parlak dolunay gecesi. Beyaz kar güçlü bir alttan dolgu verir.
GÖLGE: yumuşak kenarlı, dolgulu, HİÇBİRİ siyah değil. Bu bir hata değil,
  ortamın gerçeğidir [§3.2 · D41: yumuşak ışık ≠ bloom].
RENK: nötr beyaz ile çok soluk mavi-beyaz arası. Turuncu YOK, kırmızı
  YOK, altın YOK. Kadrajdaki tek doygun değer siyah gökyüzüdür.
⛔ "cinematic lighting" · "glowing" · "radiant" · "ethereal" ·
  "shimmering" hiçbir prompta yazılmaz [D33 · D29].
⛔ %0 bloom. Halka PARLAKTIR ama etrafına hâle yaymaz; kenarı keskindir.
```

### ⚙️ PHYSICS BIBLE — sayısal

```
YERÇEKİMİ: 0,40 g = 3,92 m/s².
  · Göğüs yüksekliğinden (1,35 m) düşen alet kara 0,83 saniyede varır.
  · Yürüyüş kadansı: her 0,8 saniyede bir tam adım; her bot bir sonraki
    kalkmadan ÖNCE basılır ve yüklenir; süzülme SIFIR. [D154 ③ · D44]
  · Tekmelenen kar taneleri temiz düz yaylar çizer ve 1,5 saniyede yere
    iner; havada asılı kalmaz, dönmez, sıvı gibi akmaz.

SÜBLİMLEŞME KURALI (novum'un fiziği):
  · Yaklaşık 65 K'nin üstündeki her yüzey, kara değdiği yerde karı
    doğrudan GAZA çevirir. Sıvı ASLA oluşmaz — 0 kare erime, 0 kare su,
    0 kare ıslaklık, 0 kare damla.
  · Gaz DİMDİK yukarı çıkar, saniyede ~4 metre, ve 6 metrede görünmez
    olur. Rüzgâr olmadığı için BÜKÜLMEZ.
  · Nesne, kendi altındaki karı gaza çevirdikçe kendi ağırlığıyla iner.
    İniş hızı nesnenin sıcaklığıyla artar.

⭐ GAZ SÜTUNU — SAYILI CÜMLE [D143 · D154 ①②]:
  "the escaping gas is a thin, dead-straight, translucent white column
   no wider than the object making it; the snow behind it stays clearly
   visible through it; it rises straight up and is gone within about six
   metres; it never curls, never widens, never drifts sideways and never
   reads as smoke."
  ⛔ Bu cümle, gazın göründüğü HER sahnenin promptuna aynen yazılır —
    S0'ın onayı S6'yı KORUMAZ [D154 ②].
  ⛔ Gaz bir OLAY DEĞİL VARLIKTIR [D154 ①]: S0'ın ONAYLI karesi, gazın
    göründüğü sonraki her sahnenin imaj üretimine REFERANS GÖRSEL olarak
    girer. Her seferinde yeniden tarif edilmez.

KABUL / RET ÖLÇÜTÜ (gaz sütunu) — kapı kaydına her sahnede kopyalanır:
  ✅ dikey · düz · nesneden geniş değil · arkası görünüyor · 6 m'de bitiyor
  ⛔ kıvrılma · genişleme · yanal kayma · duman/buhar okunması · perde
  Sapan kare RET.

SES FİZİĞİ: dışarıda ses YOK. Duyulan her şey giysi içinden: nefes,
  eklem yatağı gıcırtısı, gövdeden iletilen bot darbesi. Sublimleşme
  patlamaları TAMAMEN SESSİZDİR — bu bilinçli ve rahatsız edici.
```

### 🧱 PROP BIBLE — ölçü kilitli

```
KAZIK:          pürüzsüz beyaz sütun, 2,40 m uzun, 90 mm çap;
                düz beyaz disk ayak, 220 mm çap. Üstünde hiçbir işaret yok.
BASINÇ PLAKASI: düz beyaz disk, 700 mm çap, 20 mm kalın.
KASA:           beyaz kutu, 900 × 400 × 340 mm, menteşeli kapak,
                içinde beyaz köpük beşik.
ÇEKİRDEK:       pürüzsüz beyaz silindir, 320 mm uzun, 140 mm çap,
                yuvarlatılmış uçlar, hiçbir işaret yok. Filmin en sıcak
                nesnesi — bu yüzden en hızlı inen nesne.
HALAT:          beyaz, 12 mm, kısa boylunun sağ kalçasında sarılı.
⛔ Hiçbir prop üstünde yazı, rakam, sembol, çentik, derecelendirme,
  ölçü işareti yoktur. Ölçüler bu listede yaşar, prompt gövdesinde
  NESNE GÖRELİ anlatılır ("as wide as a glove", "chest height") [D138].
```

### 🚫 NEGATIVE BIBLE — `KILAVUZ_REHBERI` §5 çekirdeği + bu filmin farkları

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly two human characters and no others — no third person, no
duplicates, no clones, no crew, no reflected figure, no extra shadow.
0% bloom, no glow filter, no soft focus, no dreamy haze — every surface
keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no
smoothed skin, no face morphing, identical bone structure throughout.
Equipment and clothing identical to the description — no drift, no gear
appearing or disappearing mid-shot. No readable text, letters, digits,
numbers or symbols on any display, surface, patch or sign — not on the
suits, not on the equipment, and not on the ground, the rock, the snow
or any natural surface in the frame. Nothing in this world has been
measured, labelled, marked out or annotated by anyone: no scale marks,
no graduation ticks, no survey markers, no engraved or painted
characters of any kind. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers, rigid-body collision throughout. All
particles obey 0.40 g with continuous physical momentum — never
hovering, never frozen, never swirling or flowing like liquid.
Environment static and stable — no melting terrain, no warping topology,
no swimming texture. No Unreal Engine look, no CGI aesthetic, no video
game aesthetic. Photorealistic with 35mm film grain.

BU FİLMİN EK ÇEKİRDEĞİ (her prompta):
The suits have NO back-mounted unit: no backpack, no tank, no hose, no
cable, no rear housing of any kind — the back of each suit is one
continuous smooth white panel from collar to hip, carrying nothing. Each
helmet pane is optically clear glass with zero tint, zero mirror coating
and zero reflection of the environment; both faces are fully readable
through the panes in every frame. There is no wind anywhere in this
world: nothing flutters, nothing is blown, no fabric stirs, no snow
drifts sideways. Nothing melts and there is no liquid of any kind in
frame — no water, no wet surface, no drips, no slush, no ice sheen. The
black disc in the sky has no accretion disk: no plasma, no orange, no
red, no spiral, no flowing matter — only the black disc, one thin
bright white ring at its edge, and stretched starlight outside it.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | risk kartı | sahne |
|---|---|---|---|
| HUMAN COUNT LOCK | tam 2 insan × 21 sahne · tam 1 × 2 sahne (S15 · S22) · 0 × 2 sahne (S16 · S24). Üçüncü insan 0 kare; mürettebat 0; yansıma 0; fazladan gölge 0 | KART 4 | 25/25 |
| HELMET STATE SCHEDULE | kapalı S0-S24 = 25 sahne · açık 0 sahne · vizör optik berrak, tint 0, ayna kaplama 0, yansıma 0 | KART 3 | 25/25 |
| SIRT KİLİDİ | sırt ünitesi 0; sırt yüzeyi tek sürekli beyaz panel × 25 sahne. OTS kurulumunda POZİTİF cümle zorunlu | KART 3 · D79 · D139 | S6 · S14 |
| SIVI TEMASI | 0 sahne. Erime 0 kare, su 0 kare, ıslak yüzey 0 kare — fizik gereği (katı → gaz) | KART 1 | 0/25 |
| CANLI | 0 | KART 2 | 0/25 |
| YERÇEKİMİ | 0,40 g = 3,92 m/s². 1,35 m'den düşen alet 0,83 s'de yere varır. Adım kadansı: 0,8 s'de bir tam adım | KART 6 | 25/25 |
| PARÇACIK — GAZ SÜTUNU | genişlik ≤ nesne genişliği · yükseklik ≤6 m · hız ~4 m/s · kıvrılma 0 · yanal kayma 0. Sayılı cümle 11 sahnenin 11'inde | KART 6 · D143 · D154 | S0·S1·S2·S5·S6·S7·S8·S10·S20·S21·S24 |
| SAYAÇ (metinsiz, monotonik) | iniş bacağında GÖRÜNEN teleskopik kademe sayısı: **3 (S4) → 2 (S11) → 1 (S18)**. Üç değer, üç sahne, monotonik. Rakam 0, çentik 0, bant 0 — sayaç bir NESNENİN GEOMETRİSİDİR. S24'te araç kadrajda yoktur; sayaç orada okunmaz | KART 5 | S4 · S11 · S18 |
| EKRAN / GÖSTERGE | 0 adet. Bu filmde ekran, kadran, gösterge, HUD, sayaç cihazı HİÇ YOKTUR — A1 çelişkisi yapısal olarak imkânsız | KART 5 · A1 | 0/25 |
| DİYALOG | 0 replik · 25 sessiz sahne. Lip-sync riski 0 | KART 7 | 0/25 |
| KAMERA | 25/25 sabit lockoff (klip içi) · 14 kurulum · 5 açı tipi · 2 işaretli şok | KART 8 | 25/25 |
| IŞIK MIKNATISI | Hedefe hareket 1 sahne (S23) ve kamera HEDEFTE. Baskın ışık (000°) ile hedef (220°) 140° ayrı | KART 9 | S23 |
| İNSANSIZ SAHNE | 2 (S16 · S24) — ikisinde de NEGATIVE bloğu tek pozitif Style satırına iner | KART 10 | S16 · S24 |
| ÇEKİM SÜRESİ | sabit 10,0 s × 24 + hook 9,0 s. Sahne içi kesme 0. RAW 250 s → TRIM 1 s | KART 11 | 25/25 |
| KİR MERDİVENİ | YOK — 0 kademe. Bu dünyada toz yoktur; giysiler filmin sonuna kadar temiz beyaz kalır. D147 sayacı bu filmde TETİKLENMEZ, dolayısıyla D155'in faz etiketi riski yapısal olarak sıfırdır | D42 · D147 · D155 | 25/25 |

```
RİSK SAYISI: 7 / 13
  ✅ KART 3 (kask) · KART 4 (figür) · KART 6 (parçacık) · KART 8 (kamera) ·
     KART 9 (ışık mıknatısı) · KART 10 (insansız sahne) · KART 12 (politika)
  ⬜ KART 1 · 2 · 5 · 6b · 7 · 11 — malzeme çıkarılarak SIFIRA indirildi

⚠️ 5+ BANDININ ÜSTÜNDE — ve azaltma YAPILDI, aşağıda tek tek yazılı:
   · KART 1 (sıvı)      → fizik gereği imkânsız kılındı: katı azot, sıvı fazı yok
   · KART 2 (canlı)     → 0
   · KART 5 (sayaç)     → filmde ekran/gösterge CİHAZI yok; sayaç bir
                          NESNENİN GEOMETRİSİ (kaç kademe görünüyor)
   · KART 6b (katmanlı) → tek bölge, tek ışık, 25 sahnede DEĞİŞMEYEN aydınlatma
   · KART 7 (diyalog)   → 0 replik (KART 7'nin "EN GÜVENLİ" satırı)
   · KART 11 (süre)     → sabit ızgara, sahne içi kesme 0
   Kalan 7'nin 4'ü (3 · 4 · 8 · 12) bu depodaki HER uzay filminde vardır.
   Seçmeli olarak taşınan gerçek risk 3 tanedir: KART 6 · 9 · 10 —
   üçü de aşağıdaki ders kilitleriyle sahneye bağlandı.
```

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| **D157** | Tek kare testi novumun KENDİ taşıyıcısıyla koşulur; taşıyıcı kadrajın ≥1/10'unu kaplar ve değişimi TEK KLİP içinde olur; novum sahnesinde ikinci olay YOKTUR | TEK KARE satırı kazık+ayağı der. S0'da kazık ECU'da kadrajın ~%40'ı, iniş 9 s içinde tamamlanır, kadrajda başka hiçbir şey hareket etmez |
| **D158** | Merkezi seçimden SONRA en az bir seçim daha; ve en az bir BAŞARISIZ deneme | B2a: S22 ikinci seçim (kazığı bilerek yatırma) · koda 5 sahne (S20-S24), 3-5 bandında ✅ · B2b: S5-S6 basınç plakası TUTMAZ, S12'de dikilen kazık DEVRİLİR — iki başarısızlık |
| **D154** | Tekrarlayan doğa olayı bir VARLIKTIR: ilk onaylı kare referans görsel olur; kabul ölçütü HER olay sahnesine kopyalanır; insanın g'si adım SAYISIYLA yazılır | Gaz sütunu 11 sahnede; S0 onaylı karesi referans; kabul/ret satırı 11 kapı kaydında; "one full stride every 0.8 seconds, zero float" yürüyüş sahnelerinde |
| **D153** | Eş kadraj çifti metinle taşınmaz; ayna sahnenin imajı kaynağın ONAYLI karesinden türetilir | **EŞ KADRAJ ÇİFTİ YOK — bilinçli.** Metinle taşınamayan bir vaat kurulmadı. S12 ve S24 aynı setup ailesinde (A2) ama farklı azimut ve farklı içerik; ayna olarak SATILMIYOR |
| **D155** | Faz etiketi ve büyük harfli kısaltma prompt gövdesine girmez | Kir merdiveni bu filmde YOK (0 kademe); "EVA/MAV/PLSS" hiçbir promptta geçmez; giysi "surface suit" |
| **D143** | Işık/parçacık sütunu ZERRE SAYISIYLA yazılır, perde/şelale yasak | Gaz sütununun sayılı cümlesi Physics Bible'da, 11 promptta aynen |
| **D145** | Alçak açı + boş üst alan = model kanyon icat eder | 4 kurulum UFUK KİLİTLİ (B · A2 · J · K); "above the plain there is only black sky" cümlesi zorunlu |
| **D139** | Kamera arkadaysa yokluk kilidi yetmez, POZİTİF sırt yüzeyi yazılır | OTS kurulumu F (S6 · S14) — iki promptta pozitif sırt cümlesi |
| **D79** | Sırt ünitesi yok + vizör optik berrak, POZİTİF hâlde | Character Bible'da pozitif cümle; 25/25 sahnede |
| **D69/D148** | Biniş/iniş/kalkış 0 kare; kalkış klibinde bacak yazılmaz | Lander S0'da inmiş, S24'te yerde. Temas anı 0 kare |
| **D138** | Metin yasağının KAPSAMI: zemin, kaya, kar dâhil; ölçü prompt gövdesinde ETİKETE dönüşür | Negatif çekirdek tam kapsamlı; ölçüler Prop Bible'da, gövdede nesne göreli |
| **D34/D45** | Özel ad promptta geçmez | İki figür "the taller one" / "the shorter one" |
| **D124** | Klip süresi ARAÇTAN ölçülür | Plan 10,0 s varsayar; üretim öncesi ffprobe koşulacak |
| **D122** | Replik zamanları hesaplatılır | 0 replik — formül boş koşar, sapma imkânsız |
| **D74** | Kaydı olmayan kapı koşulmamış kapıdır | Kurulum sayısı bant üstü (14 > 12) ve gerekçesi sahne haritasının altında YAZILI |
| **D59/D123** | Yasak, yasakladığı kavramı prompta sokar; çözüm yasak değil TARİF | Bu filmin negatif bloklarında şiddet/yara sözlüğü SIFIRDIR — çünkü filmde 0 kare vardır ve YASAKLANMAMIŞTIR |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S20 (3:19-3:29)
NEDEN:               Tepeden bakan kadrajda beyaz bir silindir karın
                     içine iniyor ve etrafından basınçlı gaz çıkıyor —
                     "bir şeyin gömülmesi" + "basınçlı boşalma" birlikte
                     tehlike çerçevesi olarak okunabilir.
NÖTR TARİFİ:         "a smooth white cylinder rests on the snow and
                     settles slowly straight down into it under its own
                     weight, a thin straight column of white vapour
                     rising from the rim of the opening it makes;
                     the surface around it stays intact and level"
                     — patlama, fışkırma, basınç, tehlike, kaçış, gömme
                     kelimeleri kullanılmaz.

KART 12 TETİKLEYİCİ DENETİMİ:
  gövdeye değen kuvvet ......... YOK (0 kare temas, 0 kare darbe)
  kalabalık + kaçan kişi ....... YOK (2 insan, koşu 0 kare)
  ateş / duman ................. YOK (0 kare alev; gaz DUMAN DEĞİLDİR ve
                                 promptta "never reads as smoke" yazılı)
  tehlike çerçevesi ............ ⚠️ S20 — yukarıda nötr tarifi yazıldı
  bedenden bir şey çıkarma ..... YOK (kask/eldiven 0 kare çıkarılmaz)
  yüzsüz izolasyon ............. YOK (iki yüz de 25 sahnede okunur)
  konuşan yüz .................. YOK (0 replik)
  ⚠️ KASK / VİZÖR .............. HER filmde. Panzehir uygulandı: D79
                                 optik berrak vizör, iki yüz de okunur.
  ⚠️ KIRMIZI TON YOĞUNLUĞU ..... 0 — bu filmde kırmızı hiç yok.
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Diyalog tamamen kaldırıldı (0 replik) | İki karakter arasındaki ilişkiyi SÖZLE kurma imkânı; bir replik sahibi anlatıcı yok | **temassız gövde tepkisi**: S2 · S9 · S15 · S19'da bakış, açılan avuç, geri çekilen omuz; ve S19'da kısa boylunun avucunu çekirdeğe yatırması = onay jesti |
| Kimsenin batmadığı, kimsenin tehlikede olmadığı bir tasarım seçildi (insan gövdesi hiç risk altında değil) | Hayatta kalma gerilimi ve fiziksel bahis | **malzeme sonucu**: bahis nesneye taşındı — geminin bacağı iniyor (S11 · S18), çekirdek gidince marj kalmıyor. Kayıp GÖRÜNÜR bir nesnedir, hissedilen bir tehdit değil |
| Kalkış/iniş sahnesi çıkarıldı [D69] | Klasik "kurtuluş" finali ve kalkış görselliği | **alet tepkisi**: final, kalkışın değil BIRAKILAN ŞEYİN üstüne kuruldu; S24'te landerin pabuç sütunlarının SÖNMÜŞ olması, kalkış sahnesinden daha çok şey söyler (gemi soğudu = artık batmıyor) |
| Negatif bloklara şiddet/tehlike sözlüğü YAZILMADI [D123] | Hiçbir şey — bu filmde 0 kare şiddet var, dolayısıyla yasaklanacak bir şey de yok | **kütle-hız**: fizik cümleleri sayıyla yazıldı (0,40 g · 4 m/s · 0,83 s); yasak yerine TARİF kullanıldı |

```
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
   Denetim: prompt_kontrol.py ⑯ üretimden önce koşacak.
```

---

## 📋 QA'YA HAZIRLIK

> Tam blok ayrı dosyada: `THE_SINKING_STAKE_QA_SPEC.md` (D117 — blok
> okunmuyor, DOSYA okunuyor).

```
FILM:              THE SINKING STAKE
FORMAT:            yatay 3-5 dk · 16:9
RUNTIME:           249 s (4:09) — ⬜ kurgudan sonra ÖLÇÜLECEK
SCENE COUNT:       25
THEME:             ZAMAN
THEME SCENES:      S3 · S12 · S21 · S24
CENTRAL CHOICE:    S19 (3:09)
DIALOGUE LINES:    0
```
