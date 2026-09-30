# 📋 THE_LISTENING_WORLD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⑨-⑫ → B + F BLOĞU (mod V bu dörtlüde GEÇERSİZ'dir [D184 · D189])
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_LISTENING_WORLD
FORMAT:            yatay 16:9 · 2-4 dk uzay kartı (KILAVUZ_REHBERI §2.2)
RUNTIME:           160,0 seconds (title card: YOK — screen text lock 0,0 s)
SCENE COUNT:       16  (16 × 10,0 s · sabit ızgara · hook da 10,0 s)
THEME:             TEMAS VE CEVAP — "İnsan evrene seslendiğinde aradığı şey
                   yankı değil, dinlendiğinin kanıtıdır."
THEME SCENES:      S0 · S7 · S14   ⛔ en az üç (yazılmayan tema dekoratif)
                   ⭐ S9 = BEDEL sahnesi; B3'ün çapraz kapısı bunu ister
INTENDED EMOTION:  önce HUŞU ve İZOLASYON (S0-S4), sonra MERAK (S5-S7),
                   DORUKTA BÜYÜK HUŞU (S10-S12), KABUL VE HUZUR (S13-S15).
ENDING TYPE:       ÇÖZÜLMÜŞ TATMİN — sinyal cevaplanır; son kare tüm ayın
                   uyandığını gösteren devasa hilal görüntüsüdür.
PROTAGONIST:       isimsiz saha araştırmacısı (özel ad promptta geçmez [D34])
CENTRAL CHOICE:    batarya bitmesine rağmen beklemek ve elini buza basmak — S8-S9
DIALOGUE LINES:    1 · register: HUMAN 1 / MACHINE 0 (S14 4.0s: "Hello.")
SILENT SCENES:     müziksiz: S0 (hook) · S9 (bedel) · S11 (tepki)
                   MUTLAK sessizlik: 98,0-100,0 s (S9'un son 2 saniyesi)
VIRAL INTERSTITIALS: S10 (⭐VİRAL · TÜM VADİNİN UYANIŞI) · S14 (PAYLAŞIM · VİZÖR)
TITLE:             "The Listening World" — KURALI ve sonucu vaat ediyor
LIBRARY CONTEXT:   Niva kriyojenik buz ayı ve Ereon gaz devi evreni.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      16
SHOT COUNT:      16 · sahne içi kesme 0   (sahne = çekim = klip)
TARGET ASL BAND: 10,0 s SABİT (bant değil TEK DEĞER: 160,0 ÷ 16)
ASL CURVE:       UYGULANAMAZ
GRID:            sahne başlangıcı(n) = hook 10,0 s + (n−1) × 10,0 s klip
                 n = 1..16 → S0 0,0 · S1 10,0 · S2 20,0 · S3 30,0 · S4 40,0 ·
                 S5 50,0 · S6 60,0 · S7 70,0 · S8 80,0 · S9 90,0 · S10 100,0 ·
                 S11 110,0 · S12 120,0 · S13 130,0 · S14 140,0 · S15 150,0 → bitiş 160,0
RUNTIME:         160,0 s
RAW FOOTAGE:     16 × (Veo 8 s + 2 s extend) = 160,0 s · TRIM BUDGET: 0,0 s
SCREEN TEXT:     0,0 saniye (başlık kartı yok · alt yazı yok · son kart yok)
CAMERA:          16 / 16 sabit lockoff — pan · tilt · dolly · zoom SIFIR
SETUP SEQUENCE:  sahne sahne kurulum imzası (mesafe · yükseklik · lens · açı):
                 S0  A 24mm · 12,0 m · 1,70 m · EWS · göz hizası
                 S1  B 50mm · 1,2 m · 0,80 m · CU · üst açı
                 S2  A (dönüş · S0)
                 S3  B (dönüş · S1)
                 S4  C 35mm · 60,0 m · 20,0 m · EWS · alt açı
                 S5  B (dönüş · S3)
                 S6  C (dönüş · S4)
                 S7  D 28mm · 35,0 m · 3,00 m · WS · göz hizası
                 S8  E 40mm · 2,5 m · 1,00 m · MS · alt açı (küme 1)
                 S9  E (küme 1 devamı · S8'in devamı)
                 S10 F 35mm · 15,0 m · 1,50 m · WS · üst açı
                 S11 E (dönüş · S9)
                 S12 F (dönüş · S10)
                 S13 G 85mm · 0,9 m · 1,60 m · CU · göz hizası (küme 2)
                 S14 G (küme 2 devamı · S13'ün devamı)
                 S15 H 21mm · 120,0 m · 50,0 m · EWS · üst açı
KURULUM İSKELETİ: A B A B C B C D E E F E F G G H
KÜME:            2 küme — S8-S9 (E-E) · S13-S14 (G-G) (12+ sahnede ≥2 · ACI_YAYI §4b)
DÖNÜŞ:           8 / 16 = %50,0 (≥%40) — S2 · S3 · S5 · S6 · S9 · S11 · S12 · S14
ANGLE ARC:       3 açı TİPİ: göz hizası (A, D, G) · üst açı (B, F, H) · alt açı (C, E)
DORUK:           S10 → 100,0-110,0 s (sahne başlangıcı 100,0 s)

FİNAL VURUŞ KANITI [D141]:
   nesne: BİYOLÜMİNESANS TURKUAZ AY AĞI (tüm Niva hilalini kaplayan sinir ağı)
   saniye: 155,0 s   ·   kaç tane: BİR (1) devasa gezegensel ağ   ·   BULUNAN
   yanında sayılabilir ikinci kanıt: halkalı gezegen Ereon 1 (tek) · yörüngedeki araç 1 (tek)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111111111111-     (1 = insan var · - = insansız · sahne başına bir karakter)
       15/16 sahnede TEK insan; son sahnede (S15) insansız yörünge kadrajı.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 — S0-S14 arasında tam olarak bir insan; S15'te insan yok (0)
KASK          çerçeveli yekpare kask · vizör %100 opak jet-black cilalı cam (zero tint ·
              0 renk tonu · 0 ayna kaplaması · 0 yüz/ten görünürlüğü) · sırt ünitesi YOK —
              no back-mounted unit · sırt silueti düzdür
NOVUM         KURAL: Niva ayı ölü, hidrokarbon buzundan ibarettir; insan sinyali yoklukta söner.
              İHLAL: S8-S14 — telemetri kutusundan iletilen optik darbeler (2 kısa 1 uzun;
              ardından 4 kısa) buzun altındaki devasa biyolüminesans sinir ağını uyandırır;
              ay aynı ritimle cevap verir.
              TAŞIYICI: telemetri kutusu (mat siyah gövde, dairesel optik lens) — S1 · S3 · S5 · S8 · S9
YERÇEKİMİ     1,18 m/s² ≈ 0,12 g · yavaş çekim 0 kare
ATMOSFER      0 kPa (sert vakum) · %100 havasız uzay ortamı · sis, pus, buğu, asılı parçacık SIFIR
EKRAN YÖNÜ    hedef ve iniş aracı derin arka planda 11 o'clock yönünde, burnu ekran-sağına bakar
SAYAÇ         METİNSİZ, MONOTONİK:
              ① telemetri ışığı: S1 kapalı → S3 ilk darbe (2k1u) → S5 ikinci darbe (4k) →
                S9 batarya söner
              ② biyolüminesans yayılımı: S0 sönük damarlar → S6 ilk crevasse darbesi →
                S7 plain yayılımı → S10 tüm vadinin patlaması → S15 tüm ay hilali
EŞ KADRAJ     S0↔S2 (A) · S1↔S3↔S5 (B) · S4↔S6 (C) · S8↔S9↔S11 (E) · S10↔S12 (F) · S13↔S14 (G)
IŞIK TAKVİMİ  Ereon ufukta sabit konumdadır; halkalar ufku çapraz keser; turkuaz biyolüminesans
              S0'dan S15'e giderek tüm kadrajı aydınlatır.
SES REGISTER  HUMAN 1 (S14 4.0s: "Hello.") · MACHINE 0 — ses yatağı: giysi içi nefes,
              kalp atışı, kriyojenik buz çıtırtısı, derin bas rezonansı.
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI 1        KLİP İÇİ KESME YOK — her klip tek çekim
KOMUT         ffmpeg -hide_banner -i "$K" -vf "scdet=threshold=10,metadata=print:file=-" -f null - 2>&1 | grep -c "lavfi.scd.time"
DOĞRULANDI    ffmpeg 8.1 · 19.09.2026 · scdet VAR

KAPI 2        GÖLGE İÇİ DOLGU — Sert vakumda zemin yansıması
KOMUT         ffmpeg -hide_banner -ss <sn> -i "$M" -frames:v 1 -vf "signalstats,metadata=print" -f null - 2>&1 | grep -E "YMIN|YAVG"
DOĞRULANDI    ffmpeg 8.1 · 19.09.2026 · signalstats VAR

KAPI 3        MUTLAK SESSİZLİK 98,0-100,0 s (S9'un son iki saniyesi)
KOMUT         ffmpeg -hide_banner -i "$M" -af "silencedetect=noise=-60dB:d=1.8" -f null - 2>&1 | grep silence_
DOĞRULANDI    ffmpeg 8.1 · 19.09.2026 · silencedetect VAR
```
