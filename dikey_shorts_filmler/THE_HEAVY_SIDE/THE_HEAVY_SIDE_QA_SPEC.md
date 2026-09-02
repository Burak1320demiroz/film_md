# 📋 THE HEAVY SIDE — QA SPEC (MOD D girdisi)

> **Ne işe yarar:** QA koşusunda operatörün elinde İKİ dosya olur — rubrik +
> bu dosya. Bu dosya verilmezse koşu MOD V'dir ve **ön koşu** sayılır [D94/D117]:
> skor satırı Ⓥ ⚠️ ŞARTLI girer, 00_INDEX tamlık matrisinde hücre ❌ kalır,
> kesme listeleri ve REMOVE reçeteleri uygulanmaz.
>
> ⚠️ **Film HENÜZ ÜRETİLMEDİ (29.08.2026).** Bu SPEC ilk üretim koşusu için
> yazıldı ve filmle **aynı gün** depoya indi [D117].
>
> Film dosyası: `THE_HEAVY_SIDE_DIKEY_SHORTS.md` (aynı klasör)

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## A BLOĞU — SAHNE SPESİFİKASYONU (① KARE · ⑥ FİZİK rubriklerine)

```
FILM: THE HEAVY SIDE
FORMAT: dikey shorts (9:16)
SCENE: <sahne numarası> ya da "Compilation" (tam kurgu)
CLIP LENGTH: 10,005 s (plan ızgarası ÖLÇÜLMÜŞ klip süresinden kuruldu [D124];
             koşuda ffprobe ile ölçülen gerçek süre yazılır)
PIPELINE: text-to-video (her sahnenin ayrıca I2V DEVAM sürümü var)

CHARACTER: 34 yaşında erkek, dönme sistemleri yapı mühendisi · 1,79 m ·
           zeytin-kahve ten, gözenek dokusu görünür, ÜST DUDAKTA ince
           ter parlaklığı, çukur koyu kahve gözler, kalın siyah kaşlar,
           SAĞ KAŞTA küçük beyaz yara izi, düzensiz üç günlük sakal,
           çatlak dudaklar, kısa siyah saç alına yapışık
SUIT: mat KEMİK BEYAZI yumuşak kabuk yüzey suit'i · göğüste ve dış ön
      kolda tek bant **KOYU BORDO** (TAM 1 kişide) · **sırt TAMAMEN DÜZ**
      (sırt ünitesi/tank/hortum/kablo YOK) [D79] · kask **sert kabuk +
      geniş düz vizör**, optik olarak berrak, tint YOK, ayna kaplama YOK,
      çevre yansıması YOK, BUĞU YOK · her iki diz, her iki ön kol ve iki
      eldiven avucu GRİ METAL CİLASIYLA aşınmış (her sahnede AYNI yerde)
      [D42] · **hiçbir arma, bayrak, yazı, rakam, sembol yok** ·
      eldivenler kemik beyazı, avuç içleri koyu gri, **6/6 ALETSİZ**
      (62 mm'lik cıvata yalnız S3'ün 1,8 saniyesinde avuçtadır ve alet
      değildir)
CHARACTER HEIGHT: 1,79 m · toplam yüklü kütle 96 kg

ENVIRONMENT: AÇIK UZAY · VAKUM + DÖNME YERÇEKİMİ (§3.1'in yeni alt kartı,
      KILAVUZ_REHBERI §3.7). Yarıçapı 9,00 m olan, hiç basınçlandırılmamış
      bir dönme modülünün İÇ güvertesi. İçeride de dışarıda da hava YOK.
GRAVITY: **SABİT DEĞİL — FİLMİN SAATİ BUDUR.**
      a = ω²R · dönme periyodu 0:00'da 13,00 s, 0:60'ta 8,00 s
      t=0,000   T=13,00 s · v=4,350 m/s · a=2,102 m/s² (0,214 g) · 202 N
      t=10,005  T=11,77 s · v=4,803 · a=2,563 (0,261 g) · 246 N
      t=20,010  T=10,76 s · v=5,256 · a=3,070 (0,313 g) · 295 N
      t=30,015  T= 9,90 s · v=5,709 · a=3,621 (0,369 g) · 348 N
      t=40,020  T= 9,18 s · v=6,162 · a=4,219 (0,430 g) · 405 N
      t=50,025  T= 8,55 s · v=6,615 · a=4,863 (0,496 g) · 467 N
      t=60,030  T= 8,00 s · v=7,069 · a=5,552 (0,566 g) · 533 N
      ⛔ "Ağırlık değişiyor" bir SÜREKLİLİK HATASI DEĞİLDİR, filmin
        konusudur. Rubrik bunu bulgu yazarsa YANLIŞ yazmıştır.
ATMOSPHERE: YOK (0 Pa). Havadan gelen ses 0. Alüminyumda ses 5.100 m/s;
      bir tık 56,55 m çevreyi 11 ms'de dolaşır → her temas, yapının her
      yerinden gelen uzun çok-yansımalı metalik bir kuyrukla duyulur.
      ⛔ DOLGU IŞIĞI YOK: gölgelerin içi MUTLAK SİYAH, kenarları JİLET
        KESKİN. Bu, THE THIN ROOF'un (ince atmosfer) TERSİDİR.
LOCOMOTION MODE: S0 YÜRÜYÜŞ 0,70 m/s (≈5 m) · S1 İLERİ KOŞU 2,60 m/s
      (üç adım) · S2 GERİ KOŞU 3,30 m/s (dört adım) + 1,15 saniyelik
      TEK serbest adım (3,80 m · tepe 8,7 cm) · S3 diz üstü ·
      S4-S5 güvertenin ALTINDA el ele geçiş ve salınım ·
      S5 sonu YÜRÜYÜŞ 1,10 m/s (≈2 m) + merdiven
      ⛔ Havada geçen TOPLAM süre 2,1 saniye. Kalan 57,9 saniyede gövde
        her an en az bir noktadan yapıya bağlıdır [D23 karşı tasarımı].
      ⛔ "Hareketsizlik" ya da "yavaşlık" bulgu DEĞİLDİR: 0,21-0,57 g.

LENS: 24 mm KÜRESEL → S0 · S2 · S4 · S5  |  75 mm KÜRESEL → S1 · S3
      (anamorfik YASAK — vakumda yatay parlama optik bir yalandır;
      32 mm ELENDİ, gerekçesi film dosyasının GÜVENLİ ALAN HARİTASI'nda:
      halkanın kapanışı 32 mm'de kadraja sığmıyor)
CAMERA DISTANCE: S0 5,8 m · S1 4,0 m · S2 6,4 m · S3 3,0 m (eldivene) ·
      S4 6,5 m · S5 12,7→13,7 m (hepsi promptta metre olarak)
CAMERA HEIGHT: A güverteden 0,32 m · B güverte düzleminden 1,55 m
      (eksenel bomda, kenardan 3,0 m dışarıda) · C güverteden 6,00 m
      İÇERİDE (halka merkezinden 3,00 m)
CAMERA PITCH: A +30,0° (yukarı) · B 0,0° · C −28,0° (aşağı) ·
      eğik/Dutch açı 0,0° · 6/6
CAMERA MOVE: **6/6 TAM LOCKOFF** — üç kurulumun üçü de modülün yapısına
      CIVATALIDIR ve halkayla BİRLİKTE DÖNER; bu yüzden kadrajda dönme
      YOKTUR ve kamera güverteye göre kımıldamaz.
      Pan/tilt/dolly/zoom/sarsıntı/hız rampası 0 kare
      ⛔ Bu satır KLİP İÇİ karardır ve sahneler ARASI kurulumu anlatmaz;
        onu SETUP SEQUENCE satırı anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE: A · B · C · B · C · A
      A = 24 mm · 0,32 m · ALT AÇI (güverte boyunca ileri)   → S0 · S5
      B = 75 mm · 1,55 m · GÖZ HİZASI (eksen boyunca enine)  → S1 · S3
      C = 24 mm · 6,00 m içeride · ÜST AÇI (aşağı-geri)      → S2 · S4
      kurulum sayısı 3 · 6 sahne → ACI_YAYI §4 bandı (≥3) ✅
      ardışık ikili hiçbir yerde aynı değil → §3 ✅
      azimutlar A 0° · B 90° · C 195°; ardışık farklar 90/105/105/105/165
ANGLE ARC: **3 açı TİPİ — alt açı (S0·S5) · göz hizası (S1·S3) ·
      üst açı (S2·S4)** [KAMERA_ACISI §2 eşiği ≥3 ✅]
      ⭐ Açı tipi bu filmde süsleme değil KOŞULDUR: A halkanın
      kapanmasını, B teğetsel yönü (ağırlık kuralı), C ise deliğin
      içini (güvertenin ALTINI) gösterebilen tek kurulumdur.
SCALE LADDER: WS · MS · WS · CU · WS · EWS
      ardışık kademe farkı 1 · 1 · 2 · 2 · 1 (iki ŞOK BANDI, §3 tavanı)
LIGHT SOURCES: (a) TEK yıldız — açısal çapı 0,53°, dönme EKSENİNİN
      üstünde, kadrajın DIŞINDA, 6/6 sahnede. Işık eksene paralel gelir,
      güverteyi YALAYARAK aydınlatır ve bu geometri halkanın dönüşüyle
      DEĞİŞMEZ · (b) VİZÖR İÇİ KONSOL — çene altı 15 cm, yüzü camın
      içinde okutur, 6/6 sahnede aynı. **BAŞKA KAYNAK YOK.**
FILL LIGHT ALLOWED: **HAYIR — ve bu mutlaktır.** Gölge içleri MUTLAK
      SİYAH, kenarlar JİLET KESKİN. Gri gölge içi = İHLAL.
VEHICLE/STRUCTURE: modülün kendisi — grafit siyahı anodize alüminyum
      güverte (2,40 m geniş), kaburgalar (1,20 m aralık), asit sarısı
      anodize emniyet korkuluğu, göbekte 1,60 m yarıçaplı fren volanı,
      s=+8,00'de göbeğe giden merdiven. Başka araç/bina/anten 0 kare.
DIALOGUE EXPECTED: **YOK — film tamamen repliksizdir** (tasarım, eksik değil)
      ⛔ D122 replik formülü bu filmde KOŞULMAZ: replik sayısı 0.
      Formülün kaydı: replik(S_n) = hook + (n−1) × klip + TIMELINE ofseti
AUDIO LAYERS (≤4): ① kask içi nefes + alçak fan (60,03 saniyenin
      60,03'ünde, hiç kesilmez [D83]) ② gövdeden İLETİLEN temas sesleri
      (bot, diz, eldiven, karabina, cıvata) — her biri uzun, çok
      yansımalı metalik kuyrukla ③ müzik yatağı (66 BPM, 2,80'de girer,
      58,60'ta çekilir) ④ dış hava sesi: YOK — ve bu tasarımdır (vakum)
```

---

## B BLOĞU — KURGU VE ŞERİT (④ HİKAYE · kurgu kapısı ④)

```
THEME (intended): ENTROPİ  (TEMA_MUHENDISLIGI §3 tablosu · §4'e göre
      dikey-uyumlu "anlık durum" teması · §3c'nin HİÇ KULLANILMAMIŞ
      listesinden seçildi; sayac.sh tema dağılımında ENTROPİ satırı yok)
      Tek cümle: "Bu film, biriktirilmiş her şeyin er geç dağılması
      hakkında." — cümlede novum kelimesi yok ✅
      ⭐ Cümle TAKAS kalıbı DEĞİLDİR ("X için Y'den vazgeç" yapısı yok)
      Fiziksel karşılığı birebir budur: fren volanının biriktirdiği
      açısal momentum halkaya dağılıyor; volan durdukça halka hızlanıyor.
THEME SCENES (§5 matrisi): S0 · S1 · S2 · S3 · S4 · S5 (on indeks)
      mutlak siyah ≥%65 (S0 · S2 · S4 · S5) · ağırlaşan/kısalan kinesik
      (S0 · S1 · S3) · nesne indeksi: dağılmış kayıp cıvatalar (S0 · S2 ·
      S3), açılan ve yatan halat (S4), yavaşlayan volan (S2 · S4 · S5) ·
      payoff: tek AÇILMA jesti S5'te (kendini yukarı atış)
      ⚠️ Sapma [D74]: §5'in "kararan kadraj" ve "boyun iflası" sütunları
      koşulmuyor; gerekçe film dosyasının "Plan satırları" bölümünde.
SCENE / SHOT / CLIP COUNT: 6 / 6 / 6
RAW FOOTAGE: 6 klip × 10,005 s = 60,03 s
RUNTIME: 60,03 s ± 0,5 s
TRIM BUDGET: 0,0 s — kırpma yoktur; ızgara aracın ÖLÇÜLEN klip süresine
      yazıldı [D124]. Araç başka bir süre veriyorsa kırpma PLANDA sahne
      sahne yazılır, yoksa kurgu kırpmaz [D100]
TARGET ASL BAND: 10,0 s — sabit ızgara, eğri yok (bilinçli sapma [D74])
KESME IZGARASI [D115]: S0 0,000 · S1 10,005 · S2 20,010 · S3 30,015 ·
      S4 40,020 · S5 50,025 · bitiş 60,030
İNSAN ŞERİDİ [D118]: 111111
FİNAL VURUŞ KANITI [D141]: S5 · 59,0 s · adam merdivenin üçüncü
      basamağında ve GÖVDESİ MERDİVENİN ÇİZGİSİNDEN ~12° SAPMIŞ
      durumda; merdiven dümdüz. Tek kareyle koşulur:
        ffmpeg -ss 59.0 -i teslim.mp4 -frames:v 1 kanit.jpg
      ⛔ Gövde merdivenle AYNI çizgideyse FİNAL TESLİM EDİLMEMİŞTİR —
        klip sayısı, süre ve şerit tutsa bile kurgu kapısı DÜŞER.
DÖNGÜ KANITI [D141]: ilk kare (0,10 s) ile son kare (59,90 s) yan yana —
      aynı kurulum (A) · aynı ışık · aynı palet · aynı jest (baş yukarı
      dönüyor). ⚠️ DÜRÜST KAYIT: bu bir KONUM eşleşmesi değil, bir
      TERSİNE ÇEVİRME döngüsüdür — ilk karede adam boşluğun BERİ
      yakasında ve merdiven onun üstünde; son karede adam merdivende ve
      boşluk onun ALTINDA. Eşleşen şey kurulum, ışık, palet ve jesttir.
      Arkasına eklenen HER KARE döngüyü öldürür, başlık kartı dâhil.
EKRAN METNİ: 0,0 saniye — başlık kartı DAHİL [D61a/D70]
KESİLEMEZ SAHNELER: S0 (kanca + tohum + kapak anı) · S2 (asimetri anı /
      beş cıvata) · S3 (ikinci görsel şok / yana inen cıvata) ·
      S4 (merkezi seçim) · S5 (doruk + twist + döngü)
DOĞAL DORUK: S5 · 53,60-56,30 — üçüncü salınım ve kendini yukarı atış
TOHUM → KARŞILIK: S0 07,60-08,30 (açık yuvasının 60 cm yanında yatan
      TEK cıvata, 0,70 s, tepkisiz, vurgusuz) → S2 24,60 (aynı türden
      BEŞ cıvata, hepsi aynı yönde) → S3 33,80-34,77 (adamın kendi
      eliyle bıraktığı cıvata 62 cm yana iner)
DÖNGÜ NOKTASI: 60,03 → 0,00 — jest eşleşmesi (S5 sonu: baş geriye
      yatıp merdiven boyunca YUKARI dönüyor · S0 başı: baş geriye yatıp
      kapanan halka boyunca YUKARI dönüyor; aynı kurulum, aynı ışık)

MUTLAK ZAMAN ÇİZELGESİ (kurgu kapısının okuyacağı liste)
  04,60        baş kalkar  ← KANCANIN TETİĞİ
  05,40        halka OKUNUR: güverte başının üstünde kapanır
  07,20        yakın dudakta durur
  07,60-08,30  TOHUM: yuvasının 60 cm yanında yatan cıvata (0,70 s)
  08,60        öne eğilir, karşıya bakar · KAPAK ANI
  13,40-14,80  üç adım ileri koşu (2,60 m/s)
  14,80        ⭐ DİZ KATLANIR — ağırlık 270 N → 621 N
  16,20-17,20  VİZÖR JESTİ ③ (el yüze gider, 10 cm kala durur, iner)
  20,60-22,40  dört adım geri koşu (3,30 m/s)
  22,40-23,55  ⭐ GÜVERTEYİ BIRAKIR: 1,15 s · 3,80 m · tepe 8,7 cm
  23,60        kaburgayı yakalar; nefes ritmi ilk kez kopar
  24,60        ⭐ ASİMETRİ ANI — beş cıvata, hepsi aynı yönde
  32,40-34,20  EL YUVASI — avuç açılır (alan payı ≥%27)
  33,80        cıvata BIRAKILIR
  34,77        cıvata iner: 0,97 s sonra, 62 cm YANA
  35,60-37,40  indiği yere bakar (1,80 s)
  37,40        başını çevirir ve ilk kez güvertenin ALTINA bakar
  40,40-41,60  ⭐ MERKEZİ SEÇİM — emniyet halatı açılır
  41,60        serbest uç 58 cm yana iner (BEDEL, aynı karede)
  42,30-43,60  kenardan aşağı sarkar
  44,40-49,00  üç el geçişi · 3,50 metre · her an ≥1 eldiven metalde
  50,00-53,60  iki salınım (kask tepesi kenarın üstünde belirir ve iner)
  53,60-54,50  ÜÇÜNCÜ SALINIM — yük 499 N'dan 157 N'a iner (0,9 s pencere)
  54,50-55,90  kendini yukarı atar, güverteye yuvarlanır
  56,00-57,20  ayağa kalkar
  57,20-58,40  iki adım (1,10 m/s) ve merdiveni yakalar
  58,40        ⭐ TWIST: gövde merdivenin çizgisinden 11,7° sapar
  58,60-60,03  baş geriye yatar, yukarı döner — döngü kurulur
  60,03        son kare = 0,00 karesinin jesti
```

---

## C BLOĞU — KİLİTLER VE SIK YAPILAN YANLIŞ OKUMALAR (⑩ önerme kapısı)

```
✅ TASARIM — bulgu DEĞİLDİR:
   · ADAMIN AĞIRLIĞININ FİLM BOYUNCA ARTMASI → bu bir süreklilik hatası
     değil, filmin KONUSUDUR. Dönme periyodu 13,00 s'den 8,00 s'ye
     iniyor; ağırlık 202 N'dan 533 N'a çıkıyor. "Yerçekimi tutarsız"
     bulgusu YANLIŞTIR ve bu rubriğin bu filmdeki en olası hatasıdır
   · AYNI ADAMIN AYNI GÜVERTEDE İKİ FARKLI AĞIRLIKTA GÖRÜNMESİ →
     a = (v ± u)²/R. İleri koşarken ağır, geri giderken hafif.
     Süreklilik hatası DEĞİL, filmin novum'u
   · GÜVERTENİN BAŞININ ÜSTÜNDE KAPANMASI → 9,00 m yarıçaplı bir
     halkanın içindeyiz; "tavan" alttan görülen aynı güvertedir.
     "Coğrafya tutarsız" bulgusu YANLIŞTIR
   · KADRAJIN ÜST BANDINDA BAŞ AŞAĞI KABURGA VE KORKULUK OLMASI →
     aynı sebep. Orada KİMSE YOKTUR ve olmamalıdır
   · GÖLGELERİN İÇİNİN MUTLAK SİYAH ve KENARLARININ JİLET KESKİN
     olması → vakum [ortam kartı §3.1]. "Gölgeler çok sert / dolgu
     eksik" bulgusu YANLIŞTIR
   · GÖKYÜZÜNDE YILDIZ OLMAMASI → pozlama güneş gören metale göre;
     yıldızlar bu pozlamada görünmez. Tasarım, eksik değil
   · CIVATANIN YANA İNMESİ → Coriolis. 1,40 m'den 0,97 saniyede
     düşer ve 62 cm yana oturur. "Fizik hatası" bulgusu YANLIŞTIR
   · TEK BİR ADIMIN 1,15 SANİYE SÜRMESİ → 0,053 g'de bir adım budur.
     Ağır çekim DEĞİL
   · DIŞARIDA SES OLMAMASI → vakum; duyulan her şey temas ya da kask
     içi. "Ses tasarımı eksik" bulgusu YANLIŞTIR
   · SESLERİN UZUN METALİK KUYRUKLA GELMESİ → alüminyumda 5.100 m/s;
     halka bir çandır. Reverb ARTEFAKTI değil, DİEGETİK
   · ADAMIN 4 SAHNEDE YERDE/ASILI olması → tasarım; film bir hareket
     problemi filmidir
   · REPLİKSİZLİK → ilan edilmiş kısıt [D113], düşük puan sebebi değil
   · S5'TE GÖVDENİN MERDİVENE EĞİK ASILI OLMASI → göbeğe tırmanırken
     Coriolis ivmesi 0,942 m/s²; yerel ağırlık düştükçe sapma büyür.
     "Poz hatası" DEĞİL, filmin son kanıtı

🔴 GERÇEK İHLAL — bulgu SAYILIR:
   · GÜVERTENİN DÜZ BİR KORİDOR OLARAK ÜRETİLMESİ — yukarı kıvrılıp
     kapanmaması, "tavan"da güverte plakası/kaburga/korkuluk
     görünmemesi  ← FİLMİN 1 NUMARALI KAPISI
   · Baş aşağı güvertede İKİNCİ BİR İNSAN belirmesi
   · Herhangi bir gölgenin içinin GRİ olması ya da kenarının yumuşak
     olması; herhangi bir yüzeyin ikinci bir yüzeye ışık sıçratması
   · Havada asılı toz, toz bulutu, duman, alev, kıvılcım, buhar, pus,
     ışık hüzmesi, görünür yıldız
   · Yapının eğilmesi, bükülmesi, titremesi, sallanması; deliğin
     büyümesi ya da küçülmesi; plaka düşmesi
   · Cıvatanın DÜZ AŞAĞI düşmesi, sekmesi, yuvarlanması, takla atması
   · Emniyet halatının serbest ucunun ayağının dibine inmesi
   · Adamın güvertenin altında HER İKİ ELİNİ birden metalden çekmesi
   · Ağır çekim, hız rampası, hareket bulanıklığı izi
   · Kamera hareketi (6/6 lockoff kilidi) ya da kadrajın dönmesi
   · İkinci insan, yansımada insan, klon, ikinci koyu bordo bant
   · Sırt ünitesi/tank/hortum/kablo, vizör tinti, ayna kaplama, buğu
   · Ekranda herhangi bir yazı/rakam/logo/arma (başlık kartı dahil) —
     güverte, kaburga, korkuluk ve volan yüzeyleri DAHİL [D138]
   · Güneş diskinin kadraja girmesi, parlama, hale, bloom
   · S5'te gövdenin merdivenle AYNI çizgide olması (twist silinir)
   · S5'te son karenin S0'ın ilk karesiyle kurulum/ışık/jest olarak
     eşleşmemesi (döngü ölür)
```

---

## D BLOĞU — SAYISAL KİLİT LİSTESİ (⑥ FİZİK merceğinin NUMERIC LOCK LIST'i)

> Bu blok doğrudan `6_FIZIK_QA_CRITIQUE_PROMPT.md`'nin lock list alanına
> kopyalanır. Her satır bir tablo satırı olur: PASS / FAIL / UNMEASURABLE /
> NOT EXERCISED.

```
ENVIRONMENT: hard vacuum, zero pressure inside and outside the ring
GRAVITY: none — the only acceleration is centrifugal, a = omega^2 * R,
      with R = 9.00 m and the spin period falling from 13.00 s at 0.00 s
      to 8.00 s at 60.03 s
LOCKS:
LOCK: the deck curves upward in both directions and closes overhead;
      the far side of the ring is visible upside down 16.2 m above the
      standing man in all six scenes
LOCK: nobody and nothing stands on the upside-down deck overhead,
      6/6 scenes, 0 frames
LOCK: every shadow interior is absolutely black and every shadow edge
      is razor sharp — zero fill light, zero bounce light, 6/6 scenes
LOCK: the only light source outside the visor is a single star on the
      ring's spin axis, never in frame, and its geometry does not change
      across the whole film — light level constant to measurement error
LOCK: standing weight of the 96 kg loaded man: 202 N at 0 s, 295 N at
      20 s, 405 N at 40 s, 533 N at 60 s
LOCK: at 14.80 s, running along the deck in the direction of spin at
      2.60 m/s, his weight is 621 N — 2.30x his standing weight of 270 N,
      and his loaded knee folds; he does not leave the plating
LOCK: the longest possible forward jump is R*w/(2v) = 1.97 m with a
      2.20 m/s push; the opening is 3.50 m — he never crosses it by jumping
LOCK: at 22.40 s, moving against the spin at 3.30 m/s, his weight is
      about 50 N; one push carries him 3.80 m over the deck in 1.15 s,
      never rising above 8.7 cm. This is real time, not slow motion
LOCK: the 62 mm bolt released at 33.80 s from 1.40 m falls for 0.97 s
      and lands 62 cm to one side, dead straight, no bounce, no roll,
      no tumble; it never moves again
LOCK: five further bolts lie on the deck in scene 2, every one about
      60 cm to the SAME side of an open socket
LOCK: the released safety line at 41.60 s comes down 58 cm to the same
      side and lies flat and still for the rest of the film
LOCK: total airborne time across the whole film = 2.1 s; in every other
      frame at least one glove or boot is on structure
LOCK: the opening in the plating is 3.50 m long and 2.40 m wide with
      three bare ribs 1.20 m apart; its size is IDENTICAL in all six
      scenes — it never grows and never closes
LOCK: the hub flywheel is 1.60 m in radius with one bright milled notch;
      it makes 1.5 turns during scene 2, half a turn during scene 4, and
      is completely still in scene 5
LOCK: climbing inward at 0.60 m/s at 59 s, Coriolis acceleration is
      0.942 m/s² and his body hangs 11.7 degrees off the ladder line at
      radius 7.40 m; the ladder itself is dead straight
LOCK: airborne particles of any kind = 0 frames, all six scenes
LOCK: visible stars, planets, moons, nebulae = 0 frames
LOCK: exactly 1 human, 6/6 scenes; deep maroon accent band on exactly 1 body
LOCK: helmet closed 6/6; flat back 6/6; zero visor reflection 6/6;
      zero visor fog 6/6
LOCK: visor state IDENTICAL in all six scenes — changed frames = 0
LOCK: camera movement = 0 in all six scenes; camera pitch A +30.0°,
      B 0.0°, C −28.0°; Dutch angle 0.0° in all six
LOCK: on-screen text = 0.0 s, including every surface of the structure
LOCK: clip duration 10.005 s each; total 60.03 s ± 0.5 s
```

---

## E BLOĞU — MAKİNEYLE KOŞULACAK ÜÇ KAPI [D125]

> Bu üç ölçüm modele SORULMAZ. Sayı makineden alınır.

```
① GÖLGE SİYAHLIĞI KAPISI (her sahne) — bu filmin varlık şartı
   Bir gölge içi bölgesi kırpılır ve ortalama parlaklığı ölçülür:
   ffmpeg -i S<n>.mp4 -vf "crop=200:200:<x>:<y>,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
   Kırpma penceresi: adamın gölgede kalan yanı ya da bir kaburganın
   gölge yüzü.
   ⛔ YAVG > 16/255  →  gölge içine DOLGU girmiş → SAHNE REDDEDİLİR.
      Beklenen bant: 0-12/255 (mutlak siyaha yakın).
   ⚠️ Bu kapı THE THIN ROOF'un aynı numaralı kapısının TERSİDİR
      (orada YAVG < 18 reddediliyordu). İki film iki ayrı ortam
      kartında duruyor; eşiği filmden okuyun, hafızadan değil.

② KAMERA SABİTLİK KAPISI (her sahne) — 6/6 lockoff kilidi
   ⛔ DOĞRULANDI: ffmpeg 8.1 yapısında `vidstabdetect` YOK [Ders 142].
   İKAME (koşulan ve işe yarayan): sahnenin +0,5 s ve +9,3 s karelerinin
      satır/sütun luma profilleri ±25 px çapraz korelasyonla eşlenir;
      kayma ≤ 2 px → kamera kilitli. Özne kadrajı dolduran sahnelerde
      ölçüm yapılamaz ve "⬜ ÖLÇÜLEMEDİ" yazılır (boş bırakılmaz).
   ⭐ BU FİLMDE EK BİR AVANTAJ VAR: kadrajın üst bandındaki baş aşağı
      kaburga dizisi sabit, yüksek kontrastlı bir referans ızgarasıdır;
      korelasyon oradan alınır.

③ KURGU KAPISI (tam teslim) [D124 · D125]
   ffprobe -v error -show_entries format=duration -of csv=p=0 teslim.mp4
   süre = klip_sayısı × ölçülen_klip_süresi ± 0,5 s
   Kesme ızgarası: (n − 1) × klip_süresi  [D115]
   Ekran metni: 0,0 s — başlık kartı dahil
   ⭐ Ayrıca ÜÇ BİRİM ayrı sayılır [D101]: SCENE 6 · SHOT 6 · CLIP 6
   ⭐ Ve ⑪ köşe testi (filigran) koşulur [Ders 150 · olcum_kapisi.sh]
```

```
⛔ DÖRDÜNCÜ KAPI MAKİNEYLE KOŞULAMAZ — ve bu dürüst kayıttır:
   HALKA KAPISI (S0 · 05,40 s). Güvertenin yukarı kıvrılıp başın
   üstünde kapanıp kapanmadığı bir GEOMETRİ yargısıdır; ne
   prompt_kontrol.py ne ffmpeg bunu ölçer. İnsan gözüyle koşulur ve
   ÜRETİM SIRASININ BAŞINDADIR: S0 ilk üretilir, halka kapanmıyorsa
   diğer beş sahne üretilmez.
   İKİNCİ İNSAN GÖZÜ KAPISI: S4 (05,60 s) — delikten aşağı bakan
   kadrajda gövde güvertenin ALTINDA asılı görünüyor mu? Görünmüyorsa
   (model gövdeyi güvertenin üstüne koyduysa) sahne yeniden yazılır.
```
