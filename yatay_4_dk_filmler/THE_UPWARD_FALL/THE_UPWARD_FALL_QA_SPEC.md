# 📋 THE UPWARD FALL — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretti [D165]:
> `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_UPWARD_FALL/PAKET_1..8`

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
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri     MOD D
⑦ 🎯 AKSİYON     → A + C BLOĞU                       MOD D
⑧ 💪 EFOR        → C BLOĞU'nun EFOR satırı           MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE UPWARD FALL
FORMAT:            yatay 3-5 dk (16:9)
RUNTIME:           249 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       25
THEME:             FEDAKÂRLIK (sacrifice)
THEME SCENES:      S14 · S19 · S22 · S24     ⛔ en az üç ✅
THEME SENTENCE:    "Bir yük, ancak biri onunla birlikte kalmayı göze
                   aldığında yük olur."
INTENDED EMOTION:  huşu → daralma → kabul  (kaygı DEĞİL; kamera yargısız)
ENDING TYPE:       TWIST + tohum bilgi  (+ kompozisyon loop'u)
                   Twist: taşıdığı ölü parça artık yükselmiyor — avucuna
                   AĞIRLIK yapıyor. Tohum: S3 · 0:31-0:33, kanopiye takılı
                   gri kütle bir kez kıpırdar.
PROTAGONIST:       isimsiz bir adam — saha biyoloğu (özel ad promptta
                   geçmez [D34])
CENTRAL CHOICE:    S22 · 3:39 — yarığın üstündeki köprüyü tutan BEŞ canlı
                   kökü keser. Bedel: dönüş yolu. Kayıp S24'te görülüyor.
SECOND CHOICE:     S23 · 3:56 — göğüs lambasını söndürür (görünmemeyi
                   seçer) [D158 B2a: merkezi seçimden sonraki seçim = 1]
FAILED ATTEMPTS:   2 [D158 B2b] — ① S9-S10 taş denemesi ② S14→S19 sarmaşık
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     25
VIRAL INTERSTITIALS: 4 — S7 · S12 · S21 · S24   ⛔ THESE MAY NOT BE CUT
UNCUTTABLE (novum proof chain): S0 · S1 · S6 · S7 · S12 · S14 · S22 · S24
                   (kural ≥3 sahne / ≥2 nesne kapısı bu zincirde yaşıyor)
TITLE:             "THE UPWARD FALL" — başlık düşmenin YÖNÜNÜ vaat eder ve
                   film ilk 6 saniyede o yönü gösterir.
LIBRARY CONTEXT:   aynı raftaki kardeşler — LOW_POWER (ince atm., 3-5 dk
                   referansı) · THE_SINKING_STAKE (zemin fiziği novum'u,
                   02.09) · THE_HERD (kalın atmosfer kartının açıcısı)
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme 0
SCENE COUNT:     25          (üç sayım da EŞİT olmalı [D101])
TARGET ASL BAND: 10,0 s
ASL CURVE:       — (sabit ızgara, eğri yok)
⛔ GEREKÇE SATIRI [D74]: bu hat sahne = çekim = klip üretir ve kırpma
   bütçesi 0 s'dir. Ritim kadraj İÇİNDEN gelir (KURGU_RITMI §1 ① satırı):
   24 ardışık çiftin 24'ünde ölçek kademesi değişir, palet beş blokta
   ilerler, ses dokusu altı blokta değişir. Bilinçli sapma.
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S0=0 · S7=69 · S12=119 · S19=189 · S22=219 · S24=239
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     9 + 24 × 10 = 249 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0,0 saniye
CAMERA:          25 / 25 sabit lockoff (klip içi hareket 0)
SETUP SEQUENCE:  B·D·A·D·B·E·C·E·J·F·A·D·B·E·C·H·J·F·I·D·G·H·C·E·B
                 (10 kurulum: A 32mm EWS alt12 · B 50mm MS göz · C 100mm ECU
                  göz · D 24mm WS alt28 · E 50mm MCU göz · F 85mm LS üst22 ·
                  G 85mm MS OTS · H 100mm CU alt25 · I 24mm EWS göz ·
                  J 50mm MS eğik8)
ANGLE ARC:       5 açı TİPİ (alt açı · göz hizası · üst açı · OTS · eğik)
                 §2 en az 3 ister ✅ · ardışık çiftlerin 24/24'ü güvenli
                 bantta (tam 1 ölçek kademesi + ≥45° azimut) · ŞOK 0/2
DORUK:           S24 → 3:59-4:09 (sahne başlangıcı 239 s; doruk anı 239-243 s)
BÖLÜM KESİĞİ:    S12 → S13 (B → E: 1 kademe + 50° azimut ✅)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti
   Bu filmde replik SAYISI 0'dır → doğrulanacak kayıt yok; formül sapma
   denetimi için burada durur.

FİNAL VURUŞ KANITI [D141]:
   nesne: avuçtaki soluk gri ölü doku parçası · saniye: 248 · adet: 1 ·
   BULUNAN (yokluk değil — sayılabilir ve adı konabilir)
   ffmpeg -ss 248 -i "$M" -frames:v 1 kanit_final.jpg   → BAK:
   parça avuçta DURUYOR ve eldivenin yüzeyini ÇÖKERTİYOR mu? Yükseliyorsa
   twist üretilmemiştir ve final vuruşu YOKTUR.

DÖNGÜ KANITI: ilk kare (0 s) ↔ son kare (248 s)
   aynı kurulum B (50mm · MS · göz hizası 1,2 m) · aynı jest (açık avuç +
   gri parça) · ZIT yön · ışık BİLEREK farklı (sabah ↔ akşam) → loop
   kadrajla değil KOMPOZİSYONLA kuruldu [SENARYO_VE_VIRAL §5⑤]
   ffmpeg -ss 0 -i "$M" -frames:v 1 kanit_ilk.jpg
   ffmpeg -ss 248 -i "$M" -frames:v 1 kanit_son.jpg     → YAN YANA KOY
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111
       (1 = insan var · - = insansız · sahne başına bir karakter)
       25 sahnenin 25'inde tam 1 insan. İnsansız sahne 0 → KART 10
       (yapısal red) tetiklenmez.
       ⚠️ S6 · S14 · S22'de kadrajda yalnız ELLER vardır — insan yine
         VARDIR ve sayım 1'dir. Bunu "insansız" okuyan mercek YANILIYOR.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN          tam 1 · 25/25 sahne · mürettebat 0 · pilot 0 · yansıma 0 ·
               ikinci gölge 0
KOSTÜM 🔧      MODERN MAT SİYAH yüzey giysisi (revizyon 1 · 02.09): sert
               siyah gövde kabuğu · GRAFİT ribli uzuvlar · grafit diz/dirsek
               plakaları · siyah eldiven ve bot · renk 0
KASK           kapalı 25/25 · vizör optik BERRAK, sıfır ton, sıfır ayna
               kaplaması, sıfır çevre yansıması · ⭐ kask İÇİ halka ışığı
               25/25 (siyah kaskta yüzü okunur tutan tek kanal) · yüz her
               açıda okunur · sırt ünitesi YOK — düz siyah panel [D79 · D139]
UYLUK KILIFI 🆕 sağ uylukta sert siyah kılıf, kapağı TOKALI, üstünden kısa
               ribli kabza çıkıyor · KAPALI 25/25 sahne · çıkarılan 0 kare ·
               doğrultulan 0 kare · kadrajda 15 sahnede · ⛔ nesne promptta
               ADLANDIRILMADI (T1: weapon/gun/pistol/sidearm/holster = 0
               geçiş) — form tarifi kullanıldı [POLİTİKA §2 · D67 · D123]
               ⭐ tek jest: S19 · 6,0 s — eli kılıfa DEĞER, kaba döner
SİLUET 🆕      koyu figür / açık zemin: giysi mat siyah, zemin soluk gri lif,
               gövdeler soluk gri-yeşil · siluet cümlesi 8 sahnede
               (S2·S10·S17·S18·S20·S21·S23·S24) · ölçüm: E bloğu KAPI ⑦
NOVUM          Ölmüş doku ağırlığını kaybeder ve yukarı gider: 0,60 m/s
               (küçük parça) · 0,35 m/s (büyük kütle) · DÜZ dikey çizgi ·
               sürekli. İhlal ettiği kural: yerçekimi altında düşme.
               CANLI doku KALKMAZ — kuralın sınırı S14'te ekranda.
               ⛔ Bu ARŞİMET kaldırmasıdır (3,2 atm), anti-gravite değil.
NOVUM TAŞIYICI ölü doku parçası × avucun açılması → parça avuçtan YUKARI
               ayrılır. Kanıt zinciri: 8 sahne · 6 farklı nesne
               (parça · kabuk · kap+taş · dal · sarmaşık[sınır] · köprü)
YERÇEKİMİ      0,42 g = 4,12 m/s² · düşen nesne 1 s'de 2,06 m ·
               adım 1,15 m, 1,4 adım/s, gerçek zamanlı
ATMOSFER       3,2 atm · solunamaz · rüzgâr ≤0,3 m/s · ses GÜÇLÜ-ALÇAK-YAKIN
               (vakum sessizliği YOK) · toz 3 saniyede çöker
EKRAN YÖNÜ     yarık ve karşı kıyı ışığı HER kadrajda SCREEN-RIGHT
               (S16 · S17 · S18 · S20 · S24 — 5 sahnenin 5'inde) ·
               ilerleme screen-right · ters dönüş 0
               Yön kilidi NESNEYE bağlı [D174]: "the same side of the frame
               as the fallen trunk's root end" · ikinci teyit: yükselen her
               parça AYNI kanopi boşluğuna gider
SAYAÇ          YOK — filmde gösterge, ekran, sayaç, bilek ünitesi 0 adet.
               Bilgi taşıyan tek kanal fiziksel nesnedir.
EŞ KADRAJ      S0 ↔ S24 (kurulum B) · S1 ↔ S3 ↔ S11 ↔ S19 (kurulum D) ·
               S6 ↔ S14 ↔ S22 (kurulum C) · S5 ↔ S7 ↔ S13 ↔ S23 (kurulum E)
YIPRANMA       3 sabit bölge, 25 sahnede aynı yerde [D42]:
               sağ diz soluk sürtünme izi · sol önkol ince çizik ·
               bot dış kenarında gri lif tozu. Yayılma 0, artış 0.
IŞIK TAKVİMİ   MONOTONİK AZALAN, 5 blok:
               S0-S4 09:00 dik altın-yeşil sütunlar (en parlak)
               S5-S9 11:00 dar dik sütunlar, kontrast en yüksek
               S10-S14 14:00 eğik yeşil-gri, kontrast düşer
               S15-S19 16:30 sütun yok, soluk yanal yeşil-gri
               S20-S24 18:00 mavi-gri alacakaranlık (en karanlık)
               ⛔ Salınım YOK: parlak→karanlık→parlak dizisi bir üretim
                 hatasıdır (Canopy World vakası)
SES REGISTER   HUMAN 0 · MACHINE 0 · replik 0 · dış ses 0 · ekran metni 0,0 s
               Diegetik katmanlar: orman uğultusu · kuru sürtünme · lif
               kopması · adım · derin hava kayması
               MÜZİKSİZ SAHNE: S21 (3:29-3:39) — mutlak sessizlik, planlı
CANLI          CREATURE ANATOMY LOCK: 1 gövde (4 m) · 4 uzuv (9 m) ·
               0 bacak · 0 baş · 0 göz · 0 ağız · 0 diş · 0 pençe ·
               YÜRÜME 0 adım (hareket tek eksende: aşağı-yukarı, 3 m/s)
               Göründüğü sahne 4: S11 (uzak tek uzuv) · S13 (60 m, tek
               uzuv) · S21 (tek uzuv, 1,5 m, gövde kadraj dışı) · S24
               (dört uzuv + gövdenin alt yarısı, 25 m)
               İNSANA TEMAS: 0 kare, 25 sahnenin 25'inde
PARÇACIK       S7'de tam 40 parça · her biri ayrı ve sayılabilir · aralarından
               arka plan görünür · 0,6 m/s · asılı kalma 0 · kıvrılma 0 ·
               dönme 0 · yanal kayma 0 · bulut/perde 0 [D143]
SIVI           0 sahne · kadrajda su, ıslaklık, damla, sap, çamur 0
EFOR           efor sahnesi 8: S4 · S6 · S8 · S9 · S10 · S16 · S19 · S22
               her birinde EN AZ 2 gövde kanalı yazılı [D169]:
               S4 kavrama+gövde · S6 eldiven sertliği+parmak kadansı ·
               S8 kadans+gövde eğimi · S9 bacak+kadans · S10 nefes+kavrama ·
               S16 kavrama+adım kısalması · S19 kavrama+nefes ·
               S22 önkol tendonu+kadans
               ⛔ 0,42 g ağırlığı azaltır, KÜTLEYİ VE ATALETİ AZALTMAZ
GÖZ BÜTÇESİ    4 sahne (S5 · S7 · S13 · S19) — 3-5 dk bandı 3-4 ✅
EL BÜTÇESİ     4 sahne (S6 · S10 · S14 · S22) — bant ~4 ✅
YÜRÜYÜŞ        3 sahne (S8 · S16 · S20) — bant ~3 ✅
ÖLÇEK KONTRASTI 1:10 → S2 ve S17 — bant 1 ✅ (iki tane, bilinçli)
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI ①        FİLİGRAN / KÖŞE TESTİ — üretici ikonu her karede duruyor mu
              [D150: Skylight'ta 315/315 saniye, altı mercek görmedi]
KOMUT         bash kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/../olcum_kapisi.sh <master>
              (veya elle: ffmpeg -ss 10 -i "$M" -vf "crop=200:120:iw-200:ih-120" \
               -frames:v 1 kose_sag_alt.jpg  → dört köşe için tekrarla)
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 — crop filtresi mevcut ✅
İKAME         yoksa: ffprobe ile 3 kare çıkar, gözle dört köşeye bak

KAPI ②        KAMERA SABİTLİĞİ — klip içi hareket gerçekten 0 mı
KOMUT         ffmpeg -i "$M" -vf "cropdetect=24:2:0" -f null - 2>&1 | tail -20
              (kırpma kutusu klip boyunca değişiyorsa kadraj kaymıştır)
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 — cropdetect mevcut ✅
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         mpdecimate + frame farkı sayımı

KAPI ③        DONMUŞ KARE / ASILI NESNE — yükselen doku "asılı kalıyor" mu
              [novum'un tek ölümcül üretim hatası]
KOMUT         ffmpeg -i "$M" -vf "freezedetect=n=0.003:d=0.6" -map 0:v -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 — freezedetect mevcut ✅
İKAME         yükselme sahnelerinden 0,5 s aralıklı kare çifti çıkarıp
              parçanın y konumunu elle karşılaştır

KAPI ④        SÜRE VE IZGARA — sahne başlangıçları formüle uyuyor mu
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              → 249,0 ± 0,5 s bekleniyor · her klip için ayrıca ölçülür [D124]
DOĞRULANDI    ffprobe 8.1 · 02.09.2026 ✅
İKAME         —

KAPI ⑤        IŞIK TAKVİMİ MONOTONLUĞU — parlaklık geri dönüyor mu
KOMUT         ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
              -f null - 2>&1 | grep YAVG | awk 'NR%250==0'
              → sahne bloklarına göre AZALAN bir eğri bekleniyor
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 — signalstats mevcut ✅
İKAME         5 blok ortasından birer kare çıkar, gözle sırala

KAPI ⑦ 🆕     KONTRAST — siyah giysi zeminde/karanlıkta kayboluyor mu
              (revizyon 1'in getirdiği risk · Blind Berth "iki siyah gövde"
              emsalinin bu filmdeki hâli)
KOMUT         ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMIN:file=-" \
              -f null - 2>&1 | head -40
              ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX:file=-" \
              -f null - 2>&1 | head -40
              → her karede YMAX − YMIN ≥ 110 bekleniyor. Alacakaranlık
              bloğunda (S20-S24, 199-249 s) ayrıca GÖZLE: figürün kenarı
              zeminden ayrışıyor mu, kask içi halka ışığı yüzü okutuyor mu?
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 — signalstats mevcut ✅
İKAME         5 blok ortasından birer kare çıkar (0 · 60 · 130 · 190 · 245 s),
              120 px'e indir, siluet hâlâ okunuyor mu diye bak

KAPI ⑥        PROMPT KAPISI — üretimden ÖNCE, tek kare üretilmeden
KOMUT         python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
                yatay_4_dk_filmler/THE_UPWARD_FALL
              ⛔ FİLM KLASÖRÜ verilir, tek bölüm dosyası DEĞİL. Çıktıda
                "📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik" satırı yoksa
                kapı KOŞMAMIŞTIR.
DOĞRULANDI    python3 · 02.09.2026 — koşuldu, sonucu PLAN'ın kapı bloğunda
İKAME         —
```

---

## 🚫 KESME LİSTESİ — kurguda DÜŞÜRÜLEMEZ sahneler

```
S0   hook + novum kurulumu + KAPAK ANI kaynağı
S1   katalizör (0:13)
S6   novum doğrulama, nesne 2
S7   ⭐VİRAL #1 · novum doğrulama, çoğul
S12  ⭐VİRAL #2 · ORTA NOKTA · novum ölçek kanıtı
S14  kuralın SINIRI (canlı doku kalkmaz) + TEMA motifi
S21  ⭐VİRAL #3 · müziksiz sahne · en red-riskli kare
S22  MERKEZİ SEÇİM (bedel)
S24  ⭐VİRAL #4 · DORUK + KAPANIŞ + TWIST + final vuruş kanıtı

⚠️ Bu dokuzu düşerse film içerikte değil KURGUDA kaybeder [D49 · D62 · D73].
   Kurgu kapısı: KURGU_VE_TESLIM_KILAVUZU.md — üç sayım (SCENE / SHOT /
   CLIP COUNT) eşit çıkmalı; süre tek başına ALDATIR [D100 · D101].
```
