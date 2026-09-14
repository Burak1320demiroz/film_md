# 📋 THE WHITE FLOOD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretti [D165]:
> `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_WHITE_FLOOD/PAKET_1..8`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar; ad değişirse üçü birden körleşir.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → C BLOĞU                          MOD D
③ 🔊 SES         → C BLOĞU (SES REGISTER satırı)    MOD D
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                   EKRAN YÖNÜ · IŞIK TAKVİMİ · YIPRANMA
                   (+ PLANTED DETAIL satırı — bilinçli tohum kaydı)
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri     MOD D
⑦ 🎯 AKSİYON     → A + C BLOĞU                       MOD D
⑧ 💪 EFOR        → C BLOĞU'nun EFOR satırı           MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE WHITE FLOOD
FORMAT:            yatay 3-5 dk (16:9)
RUNTIME:           299 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       30
THEME:             KİMLİK (identity)
THEME SCENES:      S9 · S18 · S26 · S29     ⛔ en az üç ✅
THEME SENTENCE:    "İnsan, geri dönemediği yerde başka biri olur."
INTENDED EMOTION:  daralma → kabul  (film imzası KAYGI · yorum + kaydetme).
                   HUŞU yalnız S28'dedir ve doruk yuvasının içindedir;
                   paylaşım yuvası S27'dir (kaygı). İkisi ayrı kliptir.
ENDING TYPE:       TWIST + tohum bilgi  (+ kompozisyon loop'u)
                   Twist: yukarıda onları bekleyen şey bir sığınak değil,
                   kendi eski boylarının üstünde duran ve aynı dağı yüzlerce
                   yıldır çıkan bir başkasıdır. Tohum: S3 · 0:31-0:32,
                   640 m'deki taraçanın kenarında duran soluk dikey şey.
PROTAGONISTS:      iki isimsiz figür (özel ad promptta geçmez [D34]) —
                   UZUN OLAN halat ve çapa işçisi (kırmızı şerit SAĞ) ·
                   GENİŞ OLAN geminin pilotu (elektrik mavisi şerit SOL)
CENTRAL CHOICE:    S26 · 4:19 — dört eldiven kasanın iki sapını AYNI ANDA
                   bırakır. Bedel: kasa ve dönüş. Kayıp S27'de görülüyor.
SECOND CHOICE:     S28 · 4:39 — ikisi de geri adım atmaz ve kalır
                   [D158 B2a: merkezî seçimden sonraki seçim = 1]
FAILED ATTEMPTS:   2 [D158 B2b] — ① S8 gemiye inme denemesi (dört adımda
                   kırağı halkası büyür, geri döner) ② S15-S16 "400 m'de
                   bekleriz" (S22'de duvar bunun imkânsız olduğunu gösterir)
SEPARATION SCENE:  **S8 · 1:19** [B5b] — uzatılan halat ALINMAZ.
                   Kanal: temas reddi + yön. İkinci ayrılık S16'da ve
                   roller TERSİNMİŞTİR.
DIALOGUE LINES:    16 · register: HUMAN 14 / MACHINE 2
                   Konuşan ağzın okunduğu kare: **0**
SILENT SCENES:     21 / 30
VIRAL INTERSTITIALS: 4 — S8 · S19 · S24 · S28   ⛔ THESE MAY NOT BE CUT
UNCUTTABLE (novum proof chain): S0 · S1 · S5 · S7 · S11 · S15 · S17 · S20 ·
                   S22 · S26 · S27 · S28 · S29
                   (kural ≥3 sahne / ≥2 nesne kapısı bu zincirde yaşıyor)
TITLE:             "THE WHITE FLOOD" — başlık yükselen beyaz şeyi vaat eder
                   ve film ilk 9 saniyede o beyazın sınırını gösterir.
                   ⭐ Vaadin tuzağı bilinçli: bu sel SIVI DEĞİLDİR, havadır.
LIBRARY CONTEXT:   aynı raftaki kardeşler — LOW_POWER (ince atm., 3-5 dk
                   referansı) · THE_SINKING_STAKE (iki astronot + zemin
                   fiziği, 02.09) · THE_RISING_SNOW (kar + dağ, 31 sahne) ·
                   THE_UPWARD_FALL (varlık + tek kural, 04.09)
                   ⚠️ AYRIŞMA: RISING SNOW'da kar YÜKSELİR ve çizgi KARIN
                   çizgisidir; burada yükselen şey HAVADIR ve çizgi bir
                   SICAKLIK sınırıdır. SINKING STAKE'te sıcak olan GÖMÜLÜR;
                   burada aşağıda olan DONAR. Üç filmin üç ayrı kuralı var.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      30
SHOT COUNT:      30 · sahne içi kesme 0
SCENE COUNT:     30          (üç sayım da EŞİT olmalı [D101])
TARGET ASL BAND: 10,0 s
ASL CURVE:       — (sabit ızgara, eğri yok)
⛔ GEREKÇE SATIRI [D74]: bu hat sahne = çekim = klip üretir ve kırpma
   bütçesi 0 s'dir. Ritim kadraj İÇİNDEN gelir (KURGU_RITMI §1 ① satırı):
   29 ardışık çiftin 29'unda ölçek kademesi değişir, palet beş blokta
   ilerler, ses dokusu sekiz blokta değişir. Bilinçli sapma.
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S0=0 · S8=79 · S15=149 · S19=189 · S22=219 · S26=259 ·
                 S28=279 · S29=289
RUNTIME:         299 s = 4:59
RAW FOOTAGE:     9 + 29 × 10 = 299 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0,0 saniye
CAMERA:          30 / 30 sabit lockoff (klip içi hareket 0)
SETUP SEQUENCE:  B·D·A·D·B·H·G·F·B·E·J·D·I·F·B·H·G·D·J·E·C·H·B·F·G·E·C·H·B·F
                 (10 kurulum: A 24mm EWS göz · B 50mm MS göz · C 100mm ECU
                  göz · D 24mm WS alt26 · E 50mm MCU göz · F 85mm LS üst24 ·
                  G 85mm MS OTS · H 100mm CU alt22 · I 32mm EWS üst18 ·
                  J 50mm MS eğik8)
ANGLE ARC:       5 açı TİPİ (göz hizası · alt açı · üst açı · OTS · eğik)
                 §2 en az 3 ister ✅ · ardışık çiftlerin 29/29'u güvenli
                 bantta (tam 1 ölçek kademesi + ≥45° azimut) · ŞOK 0/2
DORUK:           S28 → 4:39-4:49 (sahne başlangıcı 279 s; doruk anı 282-287 s)
BÖLÜM KESİĞİ:    S14 → S15 (B → H: 1 kademe + 100° azimut ✅)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti
   16 kaydın 16'sı formülle doğrulandı:
     S2  19 + 2,0 = 21,0    → 0:21      S16 159 + 3,0 = 162,0  → 2:42
     S4  39 + 4,0 = 43,0    → 0:43      S16 159 + 7,0 = 166,0  → 2:46
     S7  69 + 3,0 = 72,0    → 1:12      S19 189 + 4,0 = 193,0  → 3:13
     S8  79 + 3,0 = 82,0    → 1:22      S20 199 + 6,0 = 205,0  → 3:25
     S8  79 + 5,0 = 84,0    → 1:24      S22 219 + 8,0 = 227,0  → 3:47
     S9  89 + 5,0 = 94,0    → 1:34      S25 249 + 4,0 = 253,0  → 4:13
     S14 139 + 2,5 = 141,5  → 2:21,5    S25 249 + 9,0 = 258,0  → 4:18
     S14 139 + 5,5 = 144,5  → 2:24,5    S28 279 + 8,5 = 287,5  → 4:47,5
   ⛔ Sapma varsa paket TAM DEĞİLDİR: ölçüm ffprobe ile klip klip yapılır.

FİNAL VURUŞ KANITI [D141]:
   nesne: taraçada dimdik duran EL LAMBASI · saniye: 298 · adet: 1 ·
   üstündeki kırağı: 0 · BULUNAN (yokluk değil — sayılabilir, adı konabilir)
   ffmpeg -ss 298 -i "$M" -frames:v 1 kanit_final.jpg   → BAK:
   lamba DİMDİK duruyor mu ve üstünde tek zerre beyaz YOK mu? Üstünde
   kırağı varsa twist üretilmemiştir ve final vuruşu YOKTUR.

DÖNGÜ KANITI: ilk kare (0 s) ↔ son kare (298 s)
   AYNI NESNE (el lambası) · AYNI iki çift eldiven · ZIT DURUM (yarısı
   beyaz ve çekiliyor ↔ tertemiz ve kimse dokunmuyor) · kurulum BİLEREK
   farklı (B ↔ F) · ışık BİLEREK farklı (gölün içi ↔ tepe güneşi)
   → loop kadrajla değil KOMPOZİSYONLA kuruldu [SENARYO_VE_VIRAL §5⑤]
   ffmpeg -ss 0 -i "$M" -frames:v 1 kanit_ilk.jpg
   ffmpeg -ss 298 -i "$M" -frames:v 1 kanit_son.jpg     → YAN YANA KOY
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
KADRAJDAKİ İNSAN SAYISI, sahne başına bir karakter:
PLAN:  222222222 1 222222222 111 22222 1 22
       S0        S9 S10      S19 S22   S27 S28
       (ayrıntı: S0-S8 = 2 · S9 = 1 · S10-S18 = 2 · S19-S21 = 1 ·
        S22-S26 = 2 · S27 = 1 · S28-S29 = 2)

FİLMDEKİ İNSAN SAYISI HER SAHNEDE 2'DİR ve prompt bunu her seferinde
söyler ("Exactly 2 human figures in this film and no others").
⚠️ S20 ve S26'da kadrajda YALNIZ ELLER vardır — insan yine VARDIR ve
  film sayımı 2'dir. Bunu "insansız" okuyan mercek YANILIYOR.
⚠️ İnsansız sahne 0 → KART 10 (yapısal red) tetiklenmez.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN          tam 2 · 30/30 sahne · üçüncü figür 0 · mürettebat 0 ·
               pilot koltuğunda kimse 0 · yansıma 0 · ikinci gölge 0
KOSTÜM         MAT KÖMÜR GRİSİ yüzey giysisi: sert kömür grisi gövde
               kabuğu · grafit ribli uzuvlar · grafit diz/dirsek plakaları ·
               siyah eldiven ve bot. AYIRT EDİCİ: uzun figür KIRMIZI şerit
               SAĞ önkol + SAĞ uyluk · geniş figür ELEKTRİK MAVİSİ şerit
               SOL pazu + SOL uyluk. Şerit ÇEVRESEL (360°), tek taraflı.
KASK           kapalı 30/30 · cam optik BERRAK, sıfır ton, sıfır ayna
               kaplaması, sıfır çevre yansıması · kask İÇİ halka ışığı
               30/30 · yüz her açıda okunur · sırt ünitesi YOK — düz
               kesintisiz panel [D79 · D139]
RIME STAGE     vizör kırağı halkası, TEK cümlede tarif edilir [D176]:
               S0-S4 aşama 0 · S5-S7 aşama 1 (açık oval ~6 parmak) ·
               S8-S10 aşama 2 (~4 parmak) · S11-S12 aşama 1 (GERİ ÇEKİLİR
               — kuralın kanıtı) · S13-S21 aşama 0 · S22-S29 aşama 1
               ⛔ S8'de İKİ FİGÜR AYNI AŞAMADA DEĞİLDİR: aşağı inenin
                 halkası tek klipte 4 parmaktan 3'e iner, yukarıdakinin
                 halkası değişmez. Bu, kuralın gövde üstünde ölçülmesidir.
ÇIPLAK DERİ    0 kare · üç bölgeli negatif 60 promptun 60'ında
               (yaka üstü + bilek + ayak bileği) [D175]
NOVUM          Soğuk aşağıda durur ve yükselir: ağır soğuk hava havzaya
               dolar, üst yüzeyi PERFECTLY LEVEL bir düzlemdir, altında
               kırağı büyür üstünde çekilir, ve yüzey 2,0 cm/s yükselir.
               İhlal ettiği beklenti: "yukarısı soğuktur".
               ⛔ Bu ARŞİMET + RADYASYONLA SOĞUMADIR (sıcaklık tersinmesi),
                 bilinmeyen bir kuvvet değil.
NOVUM TAŞIYICI el lambası × iki eldivenin onu yukarı çekmesi → lambanın
               alt yarısı beyaz, üst yarısı çıplak metal, sınır düz.
               Kanıt zinciri: 10 sahne · 6 farklı nesne
               (lamba · dağ duvarı · kasa · gemi · botlar · buz duvarı)
YERÇEKİMİ      0,62 g = 6,08 m/s² · düşen nesne 1 s'de 3,04 m ·
               adım 0,95 m, 1,5 adım/s, gerçek zamanlı [D154 ③]
ATMOSFER       11 kPa havza tabanı · 9,4 kPa 640 m · solunamaz ·
               rüzgâr ≤0,4 m/s · ses BOĞUK, ZAYIF, yüksek frekanssız
SICAKLIK       74 K (−199 °C) gölün içi · 128 K (−145 °C) çizginin 3 m
               üstü · 151 K (−122 °C) 640 m'de. Sıçrama ÇİZGİDE ve
               dikey 3 metrede tamamlanır.
ÇİZGİ HIZI     2,0 cm/s = 72 m/saat · 10 s'lik klipte 20 cm — kadrajda
               ÖLÇÜLEBİLİR. Ölçüldüğü sahneler: S1 · S5 · S22 · S29
İRTİFA         S0-S9 0-6 m · S10-S13 6-150 m · S14-S18 150-440 m ·
               S19-S24 440-560 m · S25-S29 560-640 m (monotonik ARTAN)
EKRAN YÖNÜ     YAMAÇ her kadrajda SCREEN-LEFT'e yükselir · BEYAZ YÜZEY ve
               vadi her kadrajda SCREEN-RIGHT ve AŞAĞIDA · ters dönüş 0
               Yön kilidi NESNEYE bağlı [D174]: "the same side of the frame
               as the pale ice wall" · ikinci teyit: düşen her şey kadrajı
               SAĞ ALTTAN terk eder
SAYAÇ          YOK — gösterge, ekran, sayaç, bilek ünitesi 0 adet.
               Sayı taşıyan tek kanal MACHINE SESİDİR (2 replik) ve ses
               ekranda METİN DEĞİLDİR → A1 çelişkisi yapısal olarak yok
EŞ KADRAJ      S0 ↔ S4 ↔ S8 ↔ S14 ↔ S22 ↔ S28 (kurulum B) ·
               S1 ↔ S3 ↔ S11 ↔ S17 (D) · S5 ↔ S15 ↔ S21 ↔ S27 (H) ·
               S6 ↔ S16 ↔ S24 (G) · S7 ↔ S13 ↔ S23 ↔ S29 (F) ·
               S9 ↔ S19 ↔ S25 (E) · S10 ↔ S18 (J) · S20 ↔ S26 (C)
YIPRANMA       3 sabit bölge, 30 sahnede aynı yerde, hepsi GİYSİ
               YÜZEYİNDE [D42 · D175②]: uzun figürün SAĞ DİZ KAPAĞINDA
               soluk sürtünme izi · geniş figürün SOL ÖNKOL MANŞETİNDE
               ince soluk çizik · dört botun dış kenarında beyaz kırağı
               tozu. Yayılma 0, artış 0.
IŞIK TAKVİMİ   MONOTONİK ARTAN, 5 blok (irtifa ekseni · KART 6b):
               S0-S9   0-6 m     güneş YOK, gölge YOK, eşit donuk
                                 mavi-gri, 3 m üstte soluk gri tavan
                                 (EN KARANLIK)
               S10-S13 6-150 m   tavan yırtılır, gök mora döner, güneş
                                 diski ufkun 4° üstünde belirir, İLK
                                 zayıf gölgeler
               S14-S18 150-440 m güneş 7°, uzun zayıf gölgeler
               S19-S24 440-560 m buz ışığı İÇİNE alır, yerel kontrast
                                 en yüksek
               S25-S29 560-640 m güneş 11° (bu dünyanın en yükseği),
                                 EN PARLAK · tek yapay ışık: 2 göğüs lambası
               ⛔ Salınım YOK: parlak→karanlık→parlak dizisi bir üretim
                 hatasıdır (Canopy World vakası)
SES REGISTER   HUMAN 14 · MACHINE 2 · replik 16 · konuşan ağzın okunduğu
               kare 0 · dış ses/anlatıcı 0 · ekran metni 0,0 s
               MACHINE satırları: S7 (1:12) · S19 (3:13) — SAYI TAŞIYAN
               TEK KANAL BUDUR [D82]; 14 insan repliğinde sayı 0.
               Diegetik katmanlar: kask içi hava akışı · nefes · telsiz
               taşıyıcı hışırtısı · kırağı kristalinin kuru tıkırtısı ·
               bot altında kabuk · buzun alçak gıcırtısı
               MÜZİKSİZ SAHNE: **S26** (4:19-4:29) — mutlak sessizlik +
               iki nefes, planlı [GOOGLE_FLOW §10]
CANLI          CREATURE ANATOMY LOCK: 1 ayakta sütun · taban göğüs
               kalınlığında · boy ~2 gövde boyu · üst uçta TAM 2 dudak ·
               başka açıklık 0 · uzuv 0 · göz/baş/ağız kavramı prompta
               HİÇ GİRMEZ · yürüme 0 adım · yer değiştirme 0 m
               ⛔ Bu sayılar YALNIZ S28 ve S29 promptlarında yazılıdır;
                 K0-K3 sahneleri (S3·S17·S18·S20·S21·S27) yalnız kadrajın
                 GÖRDÜĞÜ parçayı tarif eder [UZAYLI_VARLIK §5]
               VARLIK ŞERİDİ: 000100000000000022202300000344
               Göründüğü sahne 8: K1 ×1 (S3) · K2 ×4 (S17·S18·S20 + S16
               arka plan) · K3 ×2 (S21·S27) · K4 ×2 (S28·S29)
               İNSANA TEMAS: **0 kare**, 30 sahnenin 30'unda
               ORBİT: 0° — S28 ve S29 varlığa AYNI yönden bakar
PLANTED DETAIL ⭐ BİLİNÇLİ TOHUM [UZAYLI_VARLIK §5 · SPEC kilidi]:
               sahne S3 · saniye 0:31-0:32 · ne: 640 m yukarıdaki
               taraçanın kenarında duran soluk dikey şey, bir kez kıpırdar ·
               kadrajda nerede: ÜST SAĞ üçte bir, kadraj yüksekliğinin
               ~%2'si · kademe: K1
               ⛔ ⑤ mercek bunu "anomali" yazarsa bu bir HATA DEĞİL
                 ÖLÇÜMDÜR: tohum fark edilebilir demektir. Kilit
                 çelişkisi defterine "BİLİNÇLİ TOHUM — film sapmadı"
                 olarak kapanır; skor düzeltilmez, dipnotla girer.
PARÇACIK       havada zerre **0** · düşen kar 0 kare · uçuşan kristal 0 ·
               toz 0 · duman 0. Kırağı KATIDIR ve YERİNDE büyür:
               cephe hızı 3 mm/dakika [KART 6 tasarımla kapatıldı]
SIVI           **0** sahne · kadrajda su, ıslaklık, damla, buğu damlası,
               çamur, eriyik 0. "Sel" HAVADIR ve hiçbir karede
               dalgalanmaz, dökülmez, sıçramaz, yansıtmaz [KART 1 kapalı]
EFOR           efor sahnesi 11: S0 · S4 · S6 · S10 · S14 · S16 · S22 ·
               S23 · S24 · S26 · S27 — her birinde EN AZ 2 gövde kanalı,
               MÜHÜRLÜ GİYSİ sözlüğünden [D169 + D175①]:
               eldivenin ribli parçalarının sıkışması · kavramanın bir
               parmak kayıp yeniden alınması · omuzların kalçadan aşağı
               inmesi · arka botun yüklenmesi · adım başına iki nefes,
               ikincisi kısa · dördüncü hareketin ilkinden yavaş olması ·
               parmakların eldivenin kendi sertliğine karşı yavaş kapanması
               ⛔ `through the glove` kalıbı 60 promptun 60'ında YOK [D175]
GÖZ BÜTÇESİ    4 sahne (S9 · S19 · S21 · S25) — 3-5 dk bandı 3-4 ✅
EL BÜTÇESİ     6 sahne (S5 · S14 · S15 · S20 · S24 · S26) — bant ~4;
               30 sahnede orantı ~4,8 → 6 BİLİNÇLİ (film elle yapılan
               bir iş üstüne kurulu)
YÜRÜYÜŞ        4 sahne (S6 · S10 · S18 · S23) — orantı ~3,6 ✅
EŞYA           2 sahne (S14 · S29) — ikisi de aynı iki nesne (turuncu
               kolan + el lambası); bant ~1, bilinçli
ÖLÇEK KONTRASTI 1:10 → S2 ve S12 — bant 1; iki tane BİLİNÇLİ:
               biri gölün İÇİNDEN, biri ÜSTÜNDEN
KULESHOV       9 döngü (S0·S4·S8·S9·S12·S18·S19·S28 + S1) — bant ≥8 ✅
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**

```
KAPI ①        FİLİGRAN / KÖŞE TESTİ — üretici ikonu her karede duruyor mu
              [D150: Skylight'ta 315/315 saniye, altı mercek görmedi]
KOMUT         bash kilavuzlar_ve_sistem_dosyalari/olcum_kapisi.sh <master>
              (veya elle: ffmpeg -ss 10 -i "$M" -vf "crop=200:120:iw-200:ih-120" \
               -frames:v 1 kose_sag_alt.jpg  → dört köşe için tekrarla)
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA — ffmpeg sürümü ve crop filtresi o gün
              doğrulanır; doğrulanmadan bu satır ✅ yazılmaz
İKAME         yoksa: ffprobe ile 3 kare çıkar, gözle dört köşeye bak

KAPI ②        KAMERA SABİTLİĞİ — klip içi hareket gerçekten 0 mı
KOMUT         ffmpeg -i "$M" -vf "cropdetect=24:2:0" -f null - 2>&1 | tail -20
              (kırpma kutusu klip boyunca değişiyorsa kadraj kaymıştır)
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         mpdecimate + frame farkı sayımı

KAPI ③        SINIR HAREKETİ — kırağı cephesi gerçekten İLERLİYOR mu
              (bu filmin tek ölümcül üretim hatası: sınırın DONMASI)
KOMUT         ffmpeg -ss <sahne başı> -i "$M" -vf "select='eq(n\,0)+eq(n\,240)'" \
                -vsync 0 sinir_%d.jpg
              → S1 · S5 · S22 · S29'da iki kareyi yan yana koy: beyaz
                kenarın kaya üstündeki konumu 10 saniyede ~20 cm ilerlemiş
                olmalı. İlerlememişse KURAL EKRANA GELMEMİŞTİR.
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA
İKAME         freezedetect=n=0.003:d=0.6 ile donmuş kare taraması

KAPI ④        SÜRE VE IZGARA — sahne başlangıçları formüle uyuyor mu
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              → 299,0 ± 0,5 s bekleniyor · her klip için ayrıca ölçülür [D124]
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA
İKAME         —

KAPI ⑤        IŞIK TAKVİMİ MONOTONLUĞU — parlaklık geri dönüyor mu
KOMUT         ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
              -f null - 2>&1 | grep YAVG | awk 'NR%250==0'
              → 5 bloğa göre MONOTONİK ARTAN bir eğri bekleniyor
                (S0-S9 en karanlık → S25-S29 en parlak)
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA
İKAME         5 blok ortasından birer kare çıkar, gözle sırala

KAPI ⑥        PROMPT KAPISI — üretimden ÖNCE, tek kare üretilmeden
KOMUT         python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
                yatay_4_dk_filmler/THE_WHITE_FLOOD
              ⛔ FİLM KLASÖRÜ verilir, tek bölüm dosyası DEĞİL. Çıktıda
                "📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik" satırı yoksa
                kapı KOŞMAMIŞTIR.
DOĞRULANDI    ✅ python3 · 04.09.2026 — koşuldu: 60 prompt · 0 BLOCK ·
              film klasörü **GO**. Sonuç PLAN'ın KAPI KOŞUSU bloğunda.
İKAME         —

KAPI ⑦        LİP-SYNC YOKLUĞU — ekranda konuşan ağız var mı
              (⚠️ DÜZELTME 04.09.2026: bu depoda replikli İKİNCİ film — THE HEALING GROUND aynı gün ve daha erken yazıldı, 4 replik. Bu film İLK ÇOK REPLİKLİ (16) ve İLK İKİ İNSANLI olandır. BASAMAK 3 kullanılmadı)
KOMUT         replik saniyelerinden birer kare çıkar ve BAK:
              ffmpeg -ss 21 -i "$M" -frames:v 1 agiz_S2.jpg   (16 saniye için tekrarla)
              → her karede ağız ya kadraj dışında, ya kamera arkasında, ya
                kırağı halkasının altında olmalı. Okunur bir ağız = BULGU.
DOĞRULANDI    ⬜ ÜRETİMDEN SONRA — sonucu `04_ARASTIRMA_BULGULARI` §TUR 6'ya
              geri yazılır (merdivenin BASAMAK 1-2 ilk ölçümü)
İKAME         —
```

---

## 🚫 KESME LİSTESİ — kurguda DÜŞÜRÜLEMEZ sahneler

```
S0   hook + novum kurulumu + KAPAK ANI kaynağı + loop çiftinin yarısı
S1   katalizör (0:13) + kuralın İKİNCİ nesnesi
S7   kural dev ölçekte (gemi) — novum kanıtı
S8   ⭐VİRAL #1 · AYRILIK (B5b)
S11  kuralın TERSİ ekranda (kırağı geri çekilir) — MAYA eşiğinin kanıtı
S15  ORTA NOKTA · kuralın üst sınırı
S17  buz duvarı — kuralın yüzlerce yıllık kaydı
S19  ⭐VİRAL #2 · ironi kapanışı
S20  en alt bant + düz metal kenar (insan izi)
S22  HER ŞEYİN KAYBI
S24  ⭐VİRAL #3 · son fiziksel engel
S26  MERKEZİ SEÇİM (bedel) · müziksiz sahne
S27  paylaşım sahnesi (kaygı yuvası)
S28  ⭐VİRAL #4 · DORUK · varlığın tam formu
S29  KAPANIŞ + TWIST + LOOP + final vuruş kanıtı

⚠️ Bu on beşi düşerse film içerikte değil KURGUDA kaybeder [D49 · D62 · D73].
   Kurgu kapısı: KURGU_VE_TESLIM_KILAVUZU.md — üç sayım (SCENE / SHOT /
   CLIP COUNT) eşit çıkmalı; süre tek başına ALDATIR [D100 · D101].
```
