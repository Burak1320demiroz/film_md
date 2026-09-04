# 📋 THE PRESSED FIELD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paket betikle ÜRETİLDİ: `QA_PROMPTLARI/FILME_OZEL/THE_PRESSED_FIELD/`

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                    İNSAN · EKRAN YÖNÜ · PLANTED DETAIL
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE PRESSED FIELD
FORMAT:            yatay 16:9 · 2-4 dk hattı (sahne kısıtıyla 1:40)
RUNTIME:           100 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       10
THEME:             FIRST CONTACT
THEME SCENES:      S4 · S5 · S7 · S9
INTENDED EMOTION:  dread turning into awe — the fear of an unseen agent
                   becoming the scale of an unstoppable process
ENDING TYPE:       reversal (twist) with an ambiguous tail — the surveyor
                   has been inside the field for some time without knowing
PROTAGONIST:       a surveyor, unnamed (no proper name appears in any prompt)
CENTRAL CHOICE:    S7 — she pulls up her own planted line and re-plants it
                   as a warning arc, giving up the job she came to finish
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     10 of 10 (ambient and effect audio only, no speech)
VIRAL INTERSTITIALS: S1 (10.0-20.0 s) · S7 (70.0-80.0 s)
                   ⛔ THESE MAY NOT BE CUT
TITLE:             "THE PRESSED FIELD" promises the GROUND. The confirmation
                   is in the first second of S0.
LIBRARY CONTEXT:   same shelf as the thin-atmosphere survey films
                   (LOW_POWER · THE_SKYLIGHT). First film in this repository
                   whose antagonistic force is a non-human presence, and it
                   is never shown: 0 frames, 10 scenes of 10.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      10
SHOT COUNT:      10 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, bilinçli sapma)
                 GEREKÇE [D74]: sahne = çekim = klip; kırpma bütçesi 0 s,
                 kırpılacak ham fazlalık yok. Ritim kadraj içinden gelir
                 (ölçek her ardışık sahnede değişir).
ASL CURVE:       ①10.0 ②10.0 ③10.0 ④10.0 ⑤10.0  (sabit)
GRID:            sahne başlangıcı(n) = 10.0 hook + (n−1) × 10.0 klip
                 S0 0.0 · S1 10.0 · S2 20.0 · S3 30.0 · S4 40.0 ·
                 S5 50.0 · S6 60.0 · S7 70.0 · S8 80.0 · S9 90.0
RUNTIME:         100.0 s
RAW FOOTAGE:     10 klip × 10.0 s = 100.0 s · TRIM BUDGET: 0.0 s
SCREEN TEXT:     0.0 saniye
CAMERA:          10 / 10 sabit lockoff · klip içi hareket 0
SETUP SEQUENCE:  C · E · B · D · A · D · B · E · B · C
                 A EWS 32mm göz hizası cephe 60 m · B MS 50mm alt açı 25°
                 profil 4 m · C ECU 100mm tepe 90° 0,9 m · D WS 75mm üst
                 açı 30° ön üç-çeyrek 14 m · E CU 75mm göz hizası cephe 2,2 m
ANGLE ARC:       5 açı TİPİ — tepe · göz hizası · alt açı · üst açı · profil
                 (§2 en az 3 ister) · bilinçli şok 1 (S8→S9)
DORUK:           S7 → merkezî seçim (sahne başlangıcı 70.0 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   DIALOGUE LINES = 0 → hesaplanacak replik YOK. Formül yine yazılıdır:
   bu filmde ⑨ HİZALAMA KAPISI replik ekseninde ÖLÇMEZ, yalnız kesme
   ekseninde ölçer (kesme n = 9 · her biri n × 10.0 s'de).

FİNAL VURUŞ KANITI [D141]:
   nesne: KENDİ BOT İZİ · saniye: 94.0 · kaç tane: SIFIR · BULUNMAYAN
   S0'da aynı kurulumda (0.0-2.0 s) kadrajda İKİ bot izi vardı; S9'un
   aynı kurulumunda iz sayısı SIFIRDIR. Sayılabilir ve adı konabilir.
   ffmpeg -ss 94.0 -i "$M" -frames:v 1 kanit.jpg   → BAK
   ⛔ Karede iz varsa novum teslim EDİLMEMİŞTİR ve S9 yeniden üretilir.
DÖNGÜ KANITI: ilk kare (0.0 s) ↔ son kare (99.9 s) — AYNI kurulum (C),
   aynı ölçek, aynı ışık, aynı jest (ökçe basıyor); DEĞİŞEN tek şey
   zeminin cevabı. Bu bir DÖNGÜ DEĞİL, bilinçli KAPANIŞ KONTRASTIDIR
   (yatayda döngü opsiyonel — FINAL §2). Arkasına kare EKLENMEZ.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111     (1 = insan var · - = insansız · sahne başına bir karakter)

⛔ ŞERİDİN ÇÖZÜNÜRLÜĞÜ ÖLÇÜLDÜ [Ders 163]:
   insansız sahne / toplam sahne = 0 / 10 = 0 ≤ 1/10
   → ŞERİT SABİTTİR ve SIRA EKSENİNİ ÖLÇMEZ.
   ④c satırı "GEÇTİ" değil **"ÖLÇMEDİ"** yazar.
   Sıra YALNIZ ⑪'in SAHNE IZGARASINDAN okunur:
     olcum_kapisi.sh → sahne_izgarasi.jpg ↔ bu SPEC'in B sahne haritası
   Beklenen ızgara imzası (sahne ortası kareleri, 5.0 s ofsetle):
     5 ECU zemin · 15 CU vizör · 25 MS profil · 35 WS yüksek ·
     45 EWS ova · 55 WS yüksek · 65 MS profil · 75 CU vizör ·
     85 MS profil · 95 ECU zemin
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 10 sahnenin 10'unda · mürettebat 0 · araç 0 · klon 0
              yansımada insan 0 · başka insana ait ayak izi 0
VARLIK        0 KARE · 10 sahnenin 10'unda. Uzaylı varlığın gövdesi, uzvu,
              gölgesi ve yansıması hiçbir karede YOKTUR. Varlık yalnız
              ETKİSİYLE vardır (sertleşmiş zemin). ⛔ Kadrajda bir gövde
              görünüyorsa bu bir ÜRETİM HATASIDIR, tasarım değil.
KASK          vizör optik berrak, sıfır ton, sıfır ayna kaplama · sırt
              ünitesi YOK — düz siluet, tek sürekli panel [D79]
              HELMET STATE: kapalı S0-S9 (10 sahne) · açık 0 sahne
NOVUM         Bir şeyin geçtiği yerde gevşek toz kalıcı olarak taşa
              sıkışır ve sıkışma yayılmaya devam eder.
              İHLAL: aynı gevşek tozda özdeş iki çubuktan biri dize kadar
              girer, öteki hiç girmez ve bükülür (S6 · 60-70 s).
              TAŞIYICI: ölçüm çubuğu × tokmakla sürme jesti
              KURULUM S0-S1 · DOĞRULAMA S6 · SONUÇ S9 (≥3 sahne, 3 nesne:
              bot · çubuk · kendi izi)
YERÇEKİMİ     0.38 g — serbest düşen nesne ilk saniyede 1,9 m yol alır,
              düz yay çizer, havada asılı kalmaz.
              MASS ≠ WEIGHT [D169]: 0,38 g ağırlığı azaltır, kütle ve
              ataleti azaltmaz — tokmak vuruşu aynı eforu ister.
ATMOSFER      ince atmosfer · %0,6 basınç · ses boğuk, yüksek frekans yok ·
              toz YAVAŞ ama KESİN çöker, girdap/kıvrım/bağlı kütle YOK [D39] ·
              gölge yumuşak kenarlı MEŞRUDUR, bloom teşhisi DOKU KAYBINA
              bakılarak konur [D41]
EKRAN YÖNÜ    sertleşmiş alan/sınır kadrajın SAĞ yarısını veya sağ üçte
              birini tutar — S3 · S4 · S8 · S5 (dört sahnede yazılı) ·
              yön dönüşü 0 · alçak güneş HER sahnede kamera-SOLDA ·
              kimse ışığa doğru yürümez [KART 9 dört kanal]
SAYAÇ         KOVANDAKİ ÇUBUK — monotonik, hiç artmaz:
                S2 dört · S3 üç · S5 üç · S8 sıfır
                (S6 ve S7 eylem sahnesidir; sayım o ikisinde kilitlenmez)
              YAYDAKİ ÇUBUK: S8'de tam ÜÇ dik duran + elde bir = dört
              ⛔ Sayaç METİNSİZDİR: rakam, ibre, ekran içeriği YOKTUR
EŞ KADRAJ     S0 ↔ S9 (kurulum C · ECU tepe 90° · 0,9 m) — tek değişken:
              zeminin cevabı. Bot izi sayısı 2 → 0
YIPRANMA      monotonik merdiven, toz yalnız EKLENİR [D147]:
                PHASE 1 S0-S2 · PHASE 2 S3-S6 · PHASE 3 S7-S9
              ⛔ Sonraki sahnede önceki fazdan AZ toz varsa devamlılık hatası
IŞIK TAKVİMİ  monotonik ve SABİT: tek alçak güneş, ufkun ~12° üstünde,
              10 sahnenin 10'unda kamera-SOLDAN girer. Faz değişimi YOK.
SES REGISTER  HUMAN 0 · MACHINE 0 · yalnız kask içi nefes + temas sesleri
PLANTED DETAIL ⭐ BİLİNÇLİ TOHUM [UZAYLI_VARLIK §5 · 04_ARASTIRMA T7.4③]
              sahne S1 · saniye 13.5-15.0 · konum kadrajın SOL ÜST arka
              planı, odak DIŞI · ne: geldiği hattın iki çubuğu arasındaki
              tozun pürüzsüz olması (alanın ikinci kolu, henüz adı yok)
              ⛔ Bu bir üretim hatası DEĞİLDİR. ⑤ ARKA PLAN merceği onu
                bulgu ya da bayrak olarak yazarsa sonuç HATA değil ÖLÇÜMDÜR
                (tohum fark edilebilir demektir) ve kilit çelişkisi
                defterine "BİLİNÇLİ TOHUM — film sapmadı" olarak kapatılır.
                Skor düzeltilmez; tabloya dipnotla girer.
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Beş kapının beşi 03.09.2026'da ffmpeg 8.1'de kuru koşuyla doğrulandı.

```
KAPI 1        KESME SAYISI — kurgu 10 klipten mi ibaret (beklenen 9 kesme)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "scdet=threshold=10" -f null - 2>&1 | grep -c "lavfi.scd.time"
DOĞRULANDI    ffmpeg 8.1 · 03.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " scdet " ✅
İKAME         ffmpeg -i "$M" -vf "select='gt(scene,0.4)',metadata=print" -f null -

KAPI 2        SÜRE — 100.0 s ± 2 s (ızgara aritmetiği)
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
DOĞRULANDI    ffprobe 8.1 · 03.09.2026 · temel araç, filtre gerektirmez ✅
İKAME         yok (ffprobe yoksa ölçüm yapılamaz, kapı DÜŞER)

KAPI 3        BAŞLIK/JENERİK KARTI — kurguda siyah kare var mı (olmamalı)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.5:pix_th=0.10" -f null -
DOĞRULANDI    ffmpeg 8.1 · 03.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " blackdetect " ✅
İKAME         ilk ve son 3 saniyenin kareleri çıkarılıp elle bakılır

KAPI 4        SES İHRACI — −14 LUFS · −1,0 dBTP [KURGU_RITMI §6.2]
KOMUT         ffmpeg -hide_banner -i "$M" -af "ebur128=peak=true" -f null -
DOĞRULANDI    ffmpeg 8.1 · 03.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " ebur128 " ✅
İKAME         yok

KAPI 5        DONMUŞ KLİP — bir klip üretimde donmuş mu (≥3 s hareketsiz)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=0.001:d=3" -f null -
DOĞRULANDI    ffmpeg 8.1 · 03.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " freezedetect " ✅
İKAME         signalstats ile ardışık kare farkı ölçümü
⚠️ EŞİK GEREKÇESİ: bu filmde karakter S3'te ve S5'te BİLEREK bir tam
   saniye hareketsiz kalır (tema motifi). d=3 eşiği o duraklamaları
   yanlış pozitif olarak yakalamaz; 3 saniyeyi aşan hareketsizlik
   tasarımda YOKTUR ve bulunursa üretim hatasıdır.
```
