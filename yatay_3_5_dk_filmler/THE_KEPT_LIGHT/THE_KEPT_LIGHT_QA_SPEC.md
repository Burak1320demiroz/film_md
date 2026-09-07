# 📋 THE KEPT LIGHT — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretti:
> `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_KEPT_LIGHT/PAKET_1..8`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                    EKRAN YÖNÜ · IŞIK TAKVİMİ · YAPI ANATOMİSİ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE KEPT LIGHT
FORMAT:            horizontal 3-5 min · 16:9
RUNTIME:           249 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       25
THEME:             TIME
THEME SCENES:      S1 · S10 · S15 · S19 · S21 · S24
INTENDED EMOTION:  quiet awe turning into recognition — not fear, not grief.
                   "Overview effect" register [§4.1 TON].
ENDING TYPE:       TWIST + seed (seed at 0:31, found at 2:19, paid in macro
                   at 2:29). Last-shot type: RETURN TO THE FIRST FRAME.
PROTAGONIST:       the keeper (unnamed — no proper name appears in any
                   prompt [D34]); the single worker of a disposal bay,
                   fifty-four, competent and unhurried.
CENTRAL CHOICE:    S19 · 189-199 s — he cuts the last clamp knowing the only
                   light below goes with it. THE COST IS SEEN IN S21
                   (209-219 s): the field below the lip is no longer lit.
FAILED ATTEMPTS:   2 — S16-S17 (pulls the line; nothing below the lip comes
                   back up) · S18 (works the eye off the pin; it will not pass)
CHOICES AFTER THE CENTRAL CHOICE: 2 — S22 (leaves the cut stub bolted,
                   deliberately) · S23-S24 (releases his own lamp)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     25 (no speech anywhere) · PLANNED ABSOLUTE SILENCE: S21
VIRAL INTERSTITIALS: 4 · S12 · S14 · S19 · S23   ⛔ THESE MAY NOT BE CUT
UNCUTTABLE (rule proof, ONERME §5): S0 · S1 · S4 · S8 · S13 · S17 · S20 ·
                   S21 · S24 — plus the four viral scenes and S0 (cover)
TITLE:             "THE KEPT LIGHT" promises a light that is held here, and
                   the film ends by showing who chose to leave it.
LIBRARY CONTEXT:   Same shelf: THE SINKING STAKE (25 scenes, a black hole in
                   the sky, theme TIME — the MIRROR of this film: there
                   nothing that is planted stays, here nothing that is
                   dropped leaves). Same environment family (§3.1 vacuum):
                   THE DEAD APPROACH · THE COLD WELD.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      22 · sahne içi kesme 0
                 (3 çekim ikiye bölündü: S3-S4 · S16-S17 · S20-S21 — bunlar
                  KÜMEDİR, kesme değil bölünmüş tek çekim [ACI_YAYI §3 🕰️])
CUT COUNT:       21 (24 sınır − 3 görünmez küme dikişi)
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, BİLİNÇLİ SAPMA)
                 ⛔ GEREKÇE SATIRI [D74]: bu hattın klibi sabittir ve klip
                 süresi ARAÇTAN ölçülür [D124]. Değişken çekim süresi
                 yazmak KART 11'i açar ve talimatsız kurgu KIRPMAZ, KLİP
                 DÜŞÜRÜR. Ritim kırpmadan değil KADRAJ İÇİNDEN gelir
                 (ölçek merdiveni · palet · ses dokusu — plan §örüntü kırıcı).
ASL CURVE:       ①10.0 ②10.0 ③10.0 ④10.0 ⑤10.0  (sabit ızgara)
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S0 0 · S1 9 · S2 19 · S3 29 · S4 39 · S5 49 · S6 59 ·
                 S7 69 · S8 79 · S9 89 · S10 99 · S11 109 · S12 119 ·
                 S13 129 · S14 139 · S15 149 · S16 159 · S17 169 · S18 179 ·
                 S19 189 · S20 199 · S21 209 · S22 219 · S23 229 · S24 239
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     25 klip × 10.0 s = 250.0 s · TRIM BUDGET: 1.0 s
KIRPMA TABLOSU [KART 11 · D100]:
                 S0   10.0 s ham → 9.0 s kurguda · baştan 1.0 s (hook)
                 S1-S24  10.0 s ham → 10.0 s kurguda · kırpma 0
                 ⛔ Kırpma klip DÜŞÜRMEK değildir. Satırı olmayan klip
                   kırpılmamış sayılır.
SCREEN TEXT:     0.0 saniye (jenerik · başlık kartı · kapanış kartı ·
                 filigran: 0 kare) [D34 · D70 · D72]
CAMERA:          25/25 sabit lockoff · klip içi hareket 0
SETUP SEQUENCE (sahne sahne kurulum imzası):
  A 50mm/0.6 m üstü/CU/tepe    B 85mm/0.9 m üstü/CU/üst açı
  C 50mm/2.0 m/MS/profil+göz   D 24mm/5.0 m/WS/göz hizası
  E 24mm/0.4 m üstü/EWS/tepe   F 28mm/9.0 m/EWS/alt açı
KURULUM İSKELETİ: A E D C C D C B C D F D C D C B C C B C E E D C A
                 (PLAN'daki ile AYNI — 25 harf = 25 sahne)
KÜME:            3 · S3-S4 · S16-S17 · S20-S21   (12+ sahnede ≥2 ✅)
                 her biri 2 klip (tavan 3) · üçü de DEVAM işaretini taşıyor
DÖNÜŞ:           15/25 = %60  (12+ sahnede ≥%40 ✅ · betiğin kendi ölçümü)
                 S4 S5 S6 S8 S9 S11 S12 S13 S14 S16 S17 S18 S19 S21 S23
ANGLE ARC:       5 açı TİPİ (tepe · üst açı · profil · göz hizası · alt açı)
                 ⛔ ≥3 ister ✅ · dutch 0 sahne · abartı eşiği aşılmadı
                 (üst açı ~30° · alt açı ~20°, ikisi de 15-30 meşru bandında)
BİLİNÇLİ ŞOK:    2/2 · S0→S1 (CU→EWS, 3 kademe) · S19→S20 (MS→EWS, 2 kademe)
DORUK:           S19 → 189 s (sahne başlangıcı) · kesim 192 s · sonucu
                 S20 (199 s) ve S21 (209 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9 s hook + (n−1) × 10 s klip + promptun TIMELINE ofseti
   ⛔ BU FİLMDE REPLİK 0 — formülün koşacağı kayıt yok. Formül yine de
     burada durur çünkü aynı formül aşağıdaki üç kaydı DOĞRULAR:
       tohum       S3  · 29 + 2.0  = 31.0 s  = 0:31 ✅
       katalizör   S3  · 29 + 5.0  = 34.0 s  = 0:34 ✅
       kapak anı   S0  · 0  + 4.0  =  4.0 s  = 0:04 ✅
       merkezî seçim S19 · 189 + 3.0 = 192.0 s = 3:12 ✅
       final kanıtı S24 · 239 + 8.0 = 247.0 s = 4:07 ✅
     Beşi de formülle doğrulandı; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   nesne: ağzın altında asılı duran PARLAK NESNE
   saniye: 247.0 (4:07)
   kaç tane: ALTI — beş kelepçe + bekçinin lambası
   BULUNAN mı BULUNMAYAN mı: **BULUNAN** (sayılabilir ve adı konabilir)
   ⛔ Sap (kesilmiş altıncı kelepçenin gövdesi) kadrajın ÜST kenarındadır,
     çerçeveye cıvatalıdır ve bu sayıya GİRMEZ.
   ffmpeg -ss 247 -i "$M" -frames:v 1 kanit.jpg   → BAK VE SAY

DÖNGÜ KANITI: bu film DÖNGÜ değil KAFİYE bandındadır [ACILIS_KAPANIS §1].
   İlk kare (S0 · 0:00) ile son kare (S24 · 4:09) AYNI kurulum (A), aynı
   ölçek, aynı ışık, aynı jest (açık eldiven, aynı koordinat).
   DEĞİŞEN TEK DEĞİŞKEN: avuçtan çıkan şey — eskimiş bir kelepçe →
   bekçinin kendi YANAN lambası. Kalçadaki klips son karede BOŞTUR.
   ⛔ İki kare yan yana konduğunda değişim okunmuyorsa çift BAŞARISIZDIR.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111
       (25 sahnenin 25'inde insan var · insansız sahne 0 — KART 10
        yapısal olarak tetiklenmez)
       ⚠️ S1 · S7 · S15 · S18 · S20 · S21'de insanın YALNIZ bir parçası
       kadrajdadır (botlar/dizler ya da iki eldiven). Bu bir insansız
       sahne DEĞİLDİR ve şeritte 1 sayılır.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 25 sahnenin 25'inde · mürettebat 0 · yansıma 0 · klon 0
KASK          kapalı 25/25 sahne · açık 0 sahne · vizör optik BERRAK (sıfır
              ton, sıfır ayna, sıfır çevre yansıması) · sırt ünitesi YOK,
              yakadan kalçaya kesintisiz TEK DÜZ PANEL [D79 · D139 · D146]
NOVUM         "Kapağın altına bırakılan hiçbir şey düşmesini bitirmez."
              Her nesne aynı yönde inmeye devam eder, indikçe daha az iner,
              ağır olan durmadan önce daha çok yol alır, ve aşağı giden
              hiçbir şey yukarı gelmez.
              İHLAL SAYISI: 1. Neyin ihlali: bir cismin serbest düşüşünün
              tamamlanması. ⛔ İhlal DIŞINDA her şey normal fizikle:
              kapağın ÜSTÜNDE bırakılan alet güverteye ÇARPAR.
              ⭐ Bir mercek bu davranışı "yerçekimine aykırı" diye 🔴 yazarsa
              bulgu ⑩ ÖNERME KAPISI'nda DÜŞER — filmin kuralı budur [D166].
YERÇEKİMİ     0.40 g · kapağın ÜSTÜNDE: bırakılan alet ilk saniyede ~bir
              gövde boyu iner ve güverteye çarpar
              kapağın ALTINDA: 1 s → bir gövde boyu · sonraki 3 s → bir karış
              · sonra daha az · modül ilk 10 s'de ~yirmi gövde boyu
              ⛔ İvme prompt gövdesine YAZILMADI; SÜRE ve MESAFE yazıldı [D127]
ATMOSFER      YOK — üssün dışı da içi de VAKUM. Toz 0 kare · asılı toz /
              toz perdesi / toz şelalesi 0 kare · rüzgâr 0 · pas 0 kare ·
              alev / egzoz / kıvılcım / duman 0 kare · gölge MUTLAK SİYAH ve
              jilet kenarlı · dolgu ışığı YOK
              ⭐ Havadan taşınan ses 0 kare: duyulan her şey giysinin
              İÇİNDEN (fan, nefes) ya da TEMASTAN gelir
EKRAN YÖNÜ    "Yukarı" = KAYA TAVANI · "aşağı" = KARA DİSK — ikisi de
              adlandırılmış NESNEDİR, koordinat değil [D174].
              Ağız her yatak kadrajında kadrajın ALT yarısında · alan her
              zaman ağızdan AŞAĞI gider · kaya her dış kadrajda ÜST üçte
              birde. 25/25 sahnede SABİT · ters dönüş 0.
SAYAÇ         ÜÇ metinsiz kanal, üçü de MONOTONİK ve geri dönmez:
              ① çerçevede kalan kelepçe: S2 5 · S5 4 · S9 2 · S11 2 ·
                S13 1 · S22 0 (S3-S4→4 · S6→3 · S8→2 · S12→1)
              ② ağzın altındaki yeni parlak nesne: 1→2→3→4→5→6
              ③ modülün yatma açısı: düz → bir karış → görünür → tek köşe
              ⛔ 0 ekran · 0 kadran · 0 gösterge · 0 tuş takımı · 0 rakam.
                Hiçbir sayı prompt gövdesine RAKAMLA yazılmadı.
EŞ KADRAJ     S0 ↔ S24 (kurulum A · konum kilidi) ·
              S3 ↔ S4 ↔ S6 ↔ S8 ↔ S12 ↔ S14 ↔ S16 ↔ S17 ↔ S19 ↔ S23 (C) ·
              S2 ↔ S5 ↔ S9 ↔ S11 ↔ S13 ↔ S22 (D) ·
              S1 ↔ S20 ↔ S21 (E) · S7 ↔ S15 ↔ S18 (B) · S10 tek (F)
              ⛔ [D153] Aynı harfin ikinci ve sonraki imajları, o harfin
                ONAYLI ilk karesinden ≤3 maddelik fark listesiyle türetilir.
YIPRANMA      SABİT BÖLGE SAYISI 2 → 3 [D42 · D147]:
              S0-S12: eldiven avuç içleri + dizler (2 bölge)
              S13-S24: + sağ ön kol MANŞETİNİN dış yüzü (3 bölge)
              Monotonik, hiç azalmaz, klip içinde sabit.
              ⛔ "Wear state: PHASE n" hiçbir prompta yazılmadı [D155]
IŞIK TAKVİMİ  ALTI BÖLGE, tek planlı değişken, MONOTONİK DEĞİL ama
              SINIRDA değişir [KART 6b · ACI_YAYI §7③]:
              Z1 YATAK  (S2-S9 · S11-S19 · S22-S23): tavandaki İKİ başlıklı
                        lamba, serin nötr beyaz, tepeden; ikincil yansıma YOK
              Z2 AĞIZ   (S0): üstte aynı iki lamba, altta eski lambanın
                        zayıflayan ışığı
              Z3 ALAN   (S1 · S20): YALNIZ eski lamba, çok aşağıda
              Z4 DIŞARI (S10): ağızdan taşan yatak ışığı, tek parlak
                        dikdörtgen; gerisi mutlak siyah
              Z3′       (S21): kaynak YOK; çok aşağıda tek nokta, konisi öteye
              Z2′       (S24): üstte iki lamba, altta bekçinin YENİ lambası
              ⭐ DEĞİŞEN TEK ŞEY: alanı hangi lambanın aydınlattığı.
                Değişim S19→S20→S21 ve S23→S24 SINIRLARINDA olur; hiçbir
                klibin İÇİNDE ışık kademesi değişmez.
YAPI ANATOMİSİ (film boyu SABİT, tek sayı) [KART 13]:
              kutu 1 · yatak 1 · ağız 1 · kelepçe YUVASI 6 · yatak lambası 2 ·
              eski lamba 1 · bekçinin lambası 1 · korkuluk 1 · modül 1 ·
              pencere 0 · ekran 0 · anten 0 · kanat 0 · ayak 0
              ÖLÇÜ (SPEC'te metre, PROMPTTA gövde boyu — 1H = 1.88 m):
              figür 1.88 m · kutu 6.5 m (3.5H) · yatak 4.0 m (2.1H) ·
              ağız 1.9 m (1.0H) · modül 2.1 m (1.1H) · kelepçe 0.26 m (0.14H) ·
              korkuluk 0.53 m (0.28H) · lamba 0.20 m (0.11H)
              ÖLÇEK ŞAHİDİ: S10'da ağzın içindeki figür (1:10 kontrast)
SES REGISTER  HUMAN 0 · MACHINE 0 · replik 0 · dış ses 0 · ekran metni 0
              Diegetik doku 5 + sessizlik: ①fan+klik ②ince fan ③güverte
              teması ④kesici ısırığı ⑤gövde iniltisi ⑥SESSİZLİK (S21)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**

```
KAPI          ⛔ PLANLI MUTLAK SESSİZLİK — 209.0-219.0 s [D180]
KOMUT         ffmpeg -hide_banner -nostats -i "$M" -af \
                "highpass=f=300,lowpass=f=3400,silencedetect=n=-50dB:d=0.3" \
                -f null - 2>&1 | grep silence
              (aynı komut -40dB ve -30dB ile İKİ KEZ DAHA koşulur)
DOĞRULANDI    ffmpeg 8.1 · 06.09.2026 · filtre mevcut ✅
              ffmpeg -hide_banner -filters | grep -q " silencedetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: ffmpeg -af ebur128=framelog=verbose ile saniyelik
              momentary loudness okunur; 209-219 bandında M değeri filmin
              medyanından en az 20 LU altında olmalıdır

KAPI          ⛔ KUYRUK KARTI — teslimde ekran metni 0.0 s [D70 · D72]
KOMUT         ffmpeg -hide_banner -nostats -i "$M" -vf \
                "freezedetect=n=-60dB:d=0.5" -f null - 2>&1 | grep freeze
              + ffmpeg -vf blackdetect=d=0.3:pix_th=0.10 -f null -
DOĞRULANDI    ffmpeg 8.1 · 06.09.2026 · freezedetect ✅ blackdetect ✅
İKAME         yoksa son 5 saniyeden 10 kare çıkarılır ve elle bakılır:
              ffmpeg -ss 244 -i "$M" -vf fps=2 kuyruk_%02d.jpg

KAPI          ⛔ IHRAÇ LOUDNESS — hedef −14 LUFS · −1.0 dBTP
KOMUT         ffmpeg -hide_banner -nostats -i "$M" -af ebur128=peak=true \
                -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 06.09.2026 · ebur128 ✅
İKAME         yoksa: ffmpeg -af volumedetect ile mean/max volume okunur
              (LUFS değil, yalnız kaba sapma yakalar)

KAPI          ⛔ IZGARA — 25 klip × 10.0 s, süre 249 ±2 s, 0 sahne düşmemiş
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              + her klip için aynı komut (klip süresi ARAÇTAN ölçülür [D124])
DOĞRULANDI    ffprobe mevcut ✅ · 06.09.2026
İKAME         yok — ffprobe olmadan ızgara doğrulanamaz, teslim durur

KAPI          ⛔ FİNAL VURUŞ KANITI — 4:07'de ALTI parlak nesne [D141]
KOMUT         ffmpeg -ss 247 -i "$M" -frames:v 1 kanit_4_07.jpg
DOĞRULANDI    ffmpeg 8.1 · 06.09.2026 ✅
İKAME         yok — bu kapı MAKİNE değil GÖZ kapısıdır; kare çıkarılır ve
              nesneler ELLE sayılır. Altıdan az sayılıyorsa film eksiktir.
```

---

## 🧾 KOŞU ÖNCESİ NOT — OPERATÖRE

```
⛔ Bu film HENÜZ ÜRETİLMEDİ. Bu SPEC yazımla birlikte üretildi [D165] ve
  QA paketi de aynı anda üretildi. Üretim bittiğinde:
   ① master ihraç edilir (−14 LUFS · 1440p+ · kuyruk kartı 0.0 s)
   ② kurguda HARD MUTE uygulanır: 209.0-219.0 s
   ③ E bloğunun beş kapısı koşulur
   ④ sekiz mercek PAKET_1..8 ile koşulur — ⛔ ÇIPLAK RUBRİK YAPIŞTIRILMAZ,
     çıplak rubrik mod V koşar ve mod V koşusu T tablolarına GİREMEZ [D129]
   ⑤ rapor_kontrol.py ile raporlar denetlenir
⛔ SPEC değişirse `rubrik_paketle.sh` YENİDEN KOŞULUR.
```
