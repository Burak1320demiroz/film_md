# 📋 THE SCOURED GLASS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[D117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle **birlikte** bu dosya verilir; koşu **MOD D** olur.
>
> ⛔ **YAPIŞTIRILMAZSA KOŞU YAPILMAMIŞ SAYILIR [D129].** Ham rapor arşive
> düşer, T tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi
> uygulanmaz. "ŞARTLI diye tabloya alayım" yasaktır.
>
> ⚠️ **BU FİLMİN SPEC'İ NEDEN ERKEN YAZILDI.** YERÇEKİMİ'nin dört fazı da
> mod V koştu ve bedeli ölçüldü: FAZ 9'da ⑥ FİZİK **planın kendi ivme
> rampasını** "TWO GRAVITIES 🔴" ilan edip filmin adını taşıyan olayın
> kırpılmasını istedi; THE SINKING STAKE'te ⑥ ve ② **filmin NOVUM'unu**
> en büyük kusur diye puanladı [D166, iki vaka]. Bu dosya tam olarak o
> arızayı önlemek için vardır.
>
> ⛔ **DOSYA ADI `*_QA_SPEC.md` KALIR** — `sayac.sh`, `rubrik_paketle.sh`
> ve `rapor_kontrol.py` üçü de bu deseni arar.

> 🔴 **KAPSAM DÜRÜSTLÜĞÜ (07.09.2026):** filmin **1/15'i yazıldı** (FAZ 1).
> A ve B bloklarının film ölçeğindeki alanları ⬜'dir ve faz faz dolar.
> **C BLOĞU ŞİMDİDEN TAMDIR** — çünkü mod V'nin yaptığı hasar oradan
> gelir. E BLOĞU koşulabilir durumdadır. ⛔ Üretim başlarsa QA bu dosyayla
> koşar; A/B'nin boş alanları o fazın `FAZ_nn_QA_PROMPT.md`'sinden gelir.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                        MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)        MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)        MOD V
④ 📖 HİKAYE      → A BLOĞU + FAZ KAPISI               MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri      MOD D
⑦ ⑧ ⑨ ⑩ ⑪ ⑫    → C BLOĞU + FAZ KAPISI

⛔ FAZ KAPISI [D185]: bu bir FİLM değil, filmin bir FAZIDIR.
   Hook · final · tutundurma · kafiye · döngü · terk eğrisi
   FAZ ÖLÇEĞİNDE ÖLÇÜLEMEZ. O hücreler `—` taşır, sayı taşımaz.
   Tek istisna FAZ 1'dir: hook YALNIZ orada ölçülebilir.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE SCOURED GLASS
FORMAT:            yatay 16:9 · 15 faz × 12 sahne × 10,0 s
RUNTIME:           1.800 s (30:00) · title card YOK · screen text lock 0 s
SCENE COUNT:       180
THEME:             BEDEL
THEME SCENES:      S8 · S31 · S94 · S140 · S176      (beş — ⛔ en az üç şartı ✅)
INTENDED EMOTION:  yorgun direnç — kahramanlık değil, devam etme
ENDING TYPE:       ⬜ (FAZ 15 yazılmadı) — planlanan: kapalı + mat cam ardından gök
PROTAGONIST:       isimsiz mühendis, kırklarında bir adam
                   ⛔ özel ad hiçbir promptta geçmez [D34]
CENTRAL CHOICE:    FAZ 13 · S176 — camı SİLMEMEYİ seçmek
                   (⛔ seçimden SONRAKİ seçim: FAZ 14'te tırmanmak) [D158]
DIALOGUE LINES:    ⬜ film toplamı · FAZ 1'de 2 (S4 telsiz ≤8 kl · S12 günlük 18-22 kl)
                   register: HUMAN tümü · MACHINE 0 (bu filmde konuşan makine YOK)
SILENT SCENES:     FAZ 1'de 10/12 · film toplamı ⬜
VIRAL INTERSTITIALS: yok
TITLE:             "aşınmış cam" — başlığın verdiği söz NOVUM'un kendisidir:
                   camın aşınması filmin olayıdır, metaforu değil
LIBRARY CONTEXT:   raftaki kardeşler THE_SECOND_SHIP · THE_SLOW_STONE · YERÇEKİMİ
                   ⭐ ayrıştığı yer: bu deponun ilk 30 dakikalık filmi ve
                     ilk 15 fazlı yapısı
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      180 (FAZ 1: 12)
SHOT COUNT:      180 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s SABİT — ⛔ GEREKÇE SATIRI [D74]:
                 ASL bir tercih değil ÜRETİM KISITIDIR. Hat I2V üretir ve
                 klip süresi motorun tavanıdır; kurgu hızıyla gerilim
                 kurulamaz. Bunun bedeli plana yazıldı: gerilim ritimle
                 değil, sayılabilir kaynak + görünür takvim + dramatik
                 ironi ile kurulur [TUR 14 · rapor 4].
                 ⛔ 10,0 s bu hatta HİÇ ÖLÇÜLMEDİ [D124] — test klibi borç
GRID:            sahne başlangıcı(n) = (n−1) × 10,0 s     · hook ofseti 0
RUNTIME:         1.800 s
RAW FOOTAGE:     ⬜ · TRIM BUDGET: 0 (ızgara sabit, kırpma yok)
SCREEN TEXT:     0 saniye  ⛔ film boyunca okunur metin SIFIR
CAMERA:          180/180 sabit lockoff · 0 kamera hareketi
SETUP SEQUENCE:  ⬜ film · FAZ 1: ECU·CU·EWS·WS·MS·MCU·CU·MCU·MS·MCU·CU·MCU
KURULUM İSKELETİ: ⬜ film · FAZ 1: A B F E D C B C D C B C
KÜME:            FAZ 1'de 3 küme (CU S2+S7+S11 · MCU S6+S8+S10+S12 · MS S5+S9)
                 ✅ 12+ sahnede ≥2 şartı [ACI_YAYI §4b]
DÖNÜŞ:           FAZ 1'de 8/12 = %67  ✅ (≥%40 şartı; dönüş = kaynağından
                 ≤3 sahne sonra aynı kurulum)
ANGLE ARC:       FAZ 1'de 4 açı TİPİ (üst · göz hizası · tepe · alçak)
                 ✅ §2 en az 3 ister
DORUK:           FAZ 14 · S157-S168 (sahne başlangıcı 1.560 s)
ŞOK BANDI:       film boyu 2 · S2→S3 (FAZ 1) ve ⬜ (FAZ 12)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = (n−1) × 10,0 + promptun TIMELINE ofseti
   S4  = 3 × 10,0 + 2,0  =  32,0 s
   S12 = 11 × 10,0 + 4,0 = 114,0 s
   ⛔ Yazılan her kayıt bu formülle DOĞRULANIR.

FİNAL VURUŞ KANITI [D141 · D76]:
   ⬜ FAZ 15 yazılmadı. Planlanan: BULUNAN nesne değil, BULUNMAYAN —
   son karede vizörün mat şeridi kadrajın yarısını kaplar ve ardındaki
   gökyüzü ilk kez okunmaz. Sayılabilir olması gereken şey ŞERİDİN
   KADEME SAYISIDIR (12). ⛔ SPEC kilitlenmeden bu satır doldurulmalı.
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK

DÖNGÜ KANITI:
   S1 (vizör camının içinden açılan göz, cam TEMİZ) ↔
   S180 (aynı kurulum, aynı ölçek, aynı ışık, cam 12 KADEME MAT)
   ⛔ Eş kadraj çifti: aynı lens (100mm), aynı mesafe (0,4 m), aynı
   üst açı 20°. Değişen TEK değişken CAMDIR — filmin tezi budur.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [D118]

```
PLAN (FAZ 1):  1 1 1 1 1 1 1 1 1 1 1 1
               ⛔ On iki sahnenin on ikisinde de insan VAR.
PLAN (film):   180 sahnenin 180'inde insan var — bu filmde insansız
               sahne YOKTUR. ⭐ Bu bir kısıt değil TASARIM: tek hatlı
               anlatıda kamera adamı hiç bırakmaz.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> ⛔ **BU BLOK MOD V'NİN PANZEHİRİDİR.** Tarif değil SAYI. Kaynağı burada
> YAZILI olan bulgu ⑩ ÖNERME KAPISI'nda DÜŞER ve puanı geri verilir.

```
İNSAN         1 · kadrajda tek insan, 180/180 sahne. İkinci insan, yansıma,
              manken, heykel YOK. Makine sesi de YOK.

KASK          Beyaz eliptik kubbe, TEK kavisli ön cam, optik berrak,
              tint YOK, ayna kaplama YOK — yüz camdan okunur.
              ⛔ Sırt ünitesi VARDIR ve büyüktür (arkadan girişli kare
              paket) — bu D79'un "düz siluet" kuralının BİLİNÇLİ
              istisnasıdır: gezegen giysisi yörünge giysisi değildir,
              gerçek yüzey giysilerinin sırt paketi taşıyıcıdır
              [TUR 14 · rapor 3, KAYNAK]. ⛔ ② ve ⑤ bunu kusur yazamaz.

NOVUM         ⭐ BU GEZEGENDE HİÇBİR YÜZEY İKİ KEZ TEMİZLENEMEZ.
              Toz elektrostatik yüklüdür: silmek onu kaldırmaz, yüzeye
              gömer ve ÇİZER. Her silme camı ve paneli kalıcı olarak
              matlaştırır.
              İHLALİ NE OLUR: silinen bir yüzeyin BERRAKLAŞMASI · tozun
              dökülmesi, savrulması ya da silkelenerek düşmesi · mat
              şeridin küçülmesi, kaybolması ya da yer değiştirmesi.
              ⛔ MAT ŞERİDİN BÜYÜMESİ KUSUR DEĞİLDİR — FİLMİN OLAYIDIR.
              ⛔ TOZUN YAPIŞIP KALMASI KUSUR DEĞİLDİR — KURALIN KENDİSİDİR.

YERÇEKİMİ     0,38 g (3,721 m/s²) · TEK VE SABİT, 180 sahnenin 180'inde.
              Düşen nesne Dünya'ya göre ~1,5 kat sürede iner ve SERT iner
              (ivme azalır, ATALET AZALMAZ) [D169].
              ⛔ "İki yerçekimi" bulgusu için ölçüm CETVELİ gerekir:
              0,3 s (7 kare @24fps) ve 0,5 m altındaki düşüşten SAYI
              ÇIKMAZ [⑥ RULER FLOOR]. Cetvelsiz FAIL DÜŞER.

ATMOSFER      610 Pa (Dünya'nın 1/600'ü) · %95 CO₂ · yoğunluk 0,020 kg/m³
              ⛔ RÜZGÂR TOZDAN AĞIR HİÇBİR ŞEYİ KIMILDATMAZ.
              30 m/s'de dinamik basınç ~9 Pa'dır. Kadrajda savrulan
              enkaz, devrilen ekipman, dalgalanan bez YOKTUR ve
              OLMAMASI DOĞRUDUR — bunu kusur yazan bulgu düşer.
              Toz havada UZUN SÜRE asılı kalır ve yavaş çöker.

EKRAN YÖNÜ    Hedef (yaşam modülü, sonra yükseliş aracı) HEP EKRAN-SAĞ.
              İlerleme HEP soldan sağa. FAZ 1'de S5 ve S9'da modül
              kadrajın EKRAN-SAĞ tarafındadır. 180/180 sahnede sabit.

SAYAÇ         GÖĞÜS İĞNESİ — rakamsız mekanik kadran, yeşil yay solda,
              kırmızı yay sağda, tek siyah iğne. MONOTONİK: yalnız
              dolum sahnelerinde geri gider, kendiliğinden ASLA.
              FAZ 1: iğne kırmızı yayın ortasında, S7'de 10 s'de bir
              iğne kalınlığı kadar kayar.
              ⛔ ÜSTÜNDE RAKAM YOKTUR VE OLMAMASI DOĞRUDUR — bunu
              "eksik bilgi" diye kusur yazan bulgu düşer.

EŞ KADRAJ     S1 ↔ S180 (kurulum · ölçek · ışık · jest aynı; CAM farklı)

YIPRANMA      Sabit bölge sayısı: 4 [D42]
              ① vizör camı — mat şerit, EKRAN-SOL ALT köşe, 15 kademe
              ② diz altı — pas rengi toz, 180/180 sahnede kaplı
              ③ sağ kalça yan panel — delik → zımba → kabuk → iz
              ④ sakal — beş kademe (SAKAL TOKENİ, faz sınırında değişir)
              ⛔ YIPRANMA HİÇ GERİ GİTMEZ. Bir kademe geri giderse kusurdur.
              ⛔ Toz her sahnede vardır ve TEMİZLENMİŞ görünmemelidir.

IŞIK TAKVİMİ  MONOTONİK DEĞİL, İKİ REJİMLİ ve rejim MEKÂNA bağlıdır:
              DIŞ  = tek sert güneş, ufkun 15° üstünde, EKRAN-SOL;
                     gölgeler EKRAN-SAĞA, jilet kenarlı, gölge içi
                     soğuk arduvaz mavisi; gökyüzü tereyağ-şeker.
              İÇ   = yalnız pratik ışık, ALTTAN (iki sıcak çalışma
                     lambası + zeminde cyan şerit), tavan karanlık.
              GÜN BATIMI (FAZ 9 · 12 · 15) = güneş çevresinde BUZ MAVİSİ
                     hale, çeper pas rengi. ⭐ Bu fizik olarak DOĞRUDUR
                     (Mie ileri saçılma) ve Dünya'nın tersidir
                     [TUR 14 · rapor 3, KAYNAK].
              ⛔ İç ile dış arasındaki ışık farkı KUSUR DEĞİLDİR —
                 filmin kimlik kilididir. ⑪ IŞIK bunu "grade sıçraması"
                 diye puanlayamaz.
              ⛔ MAVİ GÖKYÜZÜ YOKTUR ve olmaması doğrudur.

SES REGISTER  HUMAN: tek ses, tamamen İngilizce.
              MACHINE: 0 — bu filmde konuşan makine YOKTUR.
              ⛔ SESSİZLİK TASARIMDIR. FAZ 1'de 12 sahnenin 10'unda
                 replik yoktur ve olmaması doğrudur; ters U eğrisinin
                 şok evresidir [TUR 13 · rapor 2, ÖLÇÜLMÜŞ].
              ⛔ Dış mekân replikleri POST'TA binmiştir; ağız senkronu
                 aranmaz ve yokluğu kusur değildir.
              ORTAM: dışarıda neredeyse mutlak sessizlik + kask içi
              nefes; içeride yaşam destek uğultusu.
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI [D142]

> ⛔ **DOĞRULANDI SATIRI OLMAYAN KAPI YAZILMAMIŞTIR.** Bir SPEC'in kamera
> sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve sessizce hiç
> koşmadı. Aşağıdaki dört kapı **07.09.2026'da bu makinede fiilen sınandı.**

```
KAPI 1        IZGARA — klip süresi gerçekten 10,0 s mi [D124]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
DOĞRULANDI    ffprobe/ffmpeg 8.1 · 07.09.2026
İKAME         —  (ffprobe her zaman var)
⛔ İLK TEST KLİBİ ÜRETİLDİĞİNDE BU KAPI KOŞULUR ve sayı B BLOĞU'na yazılır.

KAPI 2        KAMERA SABİTLİĞİ — 180/180 sahne lockoff iddiası
KOMUT         ffmpeg -i <klip> -vf vidstabdetect -f null -
DOĞRULANDI    🔴 KOŞULAMADI — vidstabdetect bu makinede KURULU DEĞİL
              (ffmpeg -hide_banner -filters | grep " vidstabdetect " → boş)
İKAME         ✅ freezedetect ile TERS ölçüm: sabit kamerada arka planın
              statik bölgesi donuk kalır.
              ffmpeg -i <klip> -vf "crop=iw/4:ih/4:0:0,freezedetect=n=0.003:d=2" -f null -
              ⛔ Bu bir İKAMEDİR, kamera sabitliğini DOĞRUDAN ölçmez.

KAPI 3        KONTRAST — tekdüze kırmızıda kadrajın düzleşmesi
KOMUT         ffmpeg -i <klip> -vf signalstats -f null - 2>&1 | grep YDIF
              ⛔ EŞİK: her karede YMAX − YMIN ≥ 110
DOĞRULANDI    ffmpeg 8.1 · signalstats mevcut · 07.09.2026
İKAME         —
GEREKÇE       Bu filmin kendi riski. `02_RISK_KARTLARI` TEKDÜZE RENK kartı:
              kırmızı-turuncu tek renk havuzu difüzyon modelinde derinliği
              öldürüyor. Beyaz zırh + cyan pratik + siyah bazalt bu eşiği
              tutturmak için var.

KAPI 4        SES KANALI — plan sesli, master sessiz çıkarsa [D136]
KOMUT         ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 <master>
DOĞRULANDI    ffprobe 8.1 · 07.09.2026
İKAME         —
⛔ SES KANALI YOK + plan sesli → 🔴 TESLİM KUSURU: parti durur, master
   yeniden ihraç edilir, dört mercek yeniden koşulur.

KAPI 5        KUYRUK/BAŞ KART — S1↔S180 eş kadraj çiftini öldüren kart
KOMUT         ffmpeg -i <master> -vf "freezedetect=n=0.001:d=1.5" -f null -
              + ffmpeg -sseof -1 -i <master> -frames:v 1 son_kare.jpg → BAK
DOĞRULANDI    ffmpeg 8.1 · freezedetect mevcut · 07.09.2026
İKAME         —
⛔ Kart varsa kesilir ve ⑪ yeniden koşulur [D70 · D72, 9 vaka].
```

---

## 🚫 YANLIŞ POZİTİF DUVARI — bu filmde kusur SAYILMAYAN sekiz şey

```
1. Tozun yapışıp kalması, silkelenince dökülmemesi        → NOVUM
2. Silinen camın berraklaşmaması, mat şerit bırakması     → NOVUM
3. Mat şeridin fazdan faza BÜYÜMESİ                       → NOVUM
4. Rüzgârın hiçbir şeyi kımıldatmaması                    → ATMOSFER (9 Pa)
5. Göstergede rakam olmaması                              → METİN YASAĞI
6. İç ile dış arasındaki keskin ışık farkı                → IŞIK TAKVİMİ
7. On iki sahnenin onunda replik olmaması                 → SES REGISTER
8. Büyük sırt paketi (düz siluet değil)                   → KASK, D79 istisnası

⛔ Bu sekizden birini kusur olarak yazan bulgu ⑩ ÖNERME KAPISI'nda
   DÜŞER, puanı geri verilir ve merceğin toplamı yeniden hesaplanır.
```
