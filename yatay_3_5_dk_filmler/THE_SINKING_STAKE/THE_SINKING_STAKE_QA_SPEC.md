# 📋 THE SINKING STAKE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretir: `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>`

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
                   ATMOSFER · IŞIK TAKVİMİ · EKRAN YÖNÜ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE SINKING STAKE
FORMAT:            yatay 3-5 dk · 16:9 · text-to-video, sabit ızgara
RUNTIME:           249 seconds (4:09)  (title card: yok — screen text lock 0 s)
SCENE COUNT:       25
THEME:             ZAMAN
                   "Burada hiçbir iz kendi başına kalmaz; kalan her iz,
                    biri onu orada bırakmayı SEÇTİĞİ içindir."
THEME SCENES:      S3 · S12 · S21 · S24     (dört indeks — kapı üç ister)
INTENDED EMOTION:  soğuk huşu ve kabulleniş. ⛔ Tehdit, panik, hayatta kalma
                   gerilimi ya da kurtuluş sevinci HEDEFLENMEMİŞTİR; rapor
                   bunların yokluğunu eksik olarak yazmamalıdır.
ENDING TYPE:       TERSİNE DÖNÜŞ (twist) + TOHUM  [FINAL §2 · 3-5 dk bandı]
                   Twist: bu işareti yapan ilk insanlar onlar değildi.
                   Tohum: S3 · 0:31-0:33, ufuktaki ince dikey çizgi, 2 s,
                   karakterin bakışıyla vurgulanmadan.
PROTAGONIST:       iki isimsiz figür [D34]. "THE TALLER ONE" (188 cm, geniş
                   omuzlu, koyu kahverengi ten, kırlaşmış kısa saç, elli
                   ortaları, göğüs boyunduruğu) ve "THE SHORTER ONE" (165 cm,
                   ince, açık tenli çilli, kızıl-kahve saç, otuzlarının başı,
                   düz göğüs + kalçada sarılı beyaz halat).
                   ⛔ AYIRT ETME KANALI GEOMETRİDİR, renk değil — ikisi de
                     tepeden tırnağa beyazdır. Boy farkı 23 cm.
CENTRAL CHOICE:    S19 (3:09-3:19) — kısa boylu avucunu çekirdeğe yatırır
                   (onay), uzun boylu çekirdeği beşikten kaldırır (karar).
                   BEDEL: geminin tek yedek güç hücresi. S19 sonunda beşik
                   kadrajda BOŞ durur.
SECOND CHOICE:     S22 (3:39-3:49) — kazığı geri götürmez, bilerek bakir kara
                   yatırıp sütunu gösteren düz bir hendek bırakır. [D158 B2a]
FAILED ATTEMPTS:   2 — S5/S6 basınç plakası TUTMAZ · S12 dikilen kazık
                   DEVRİLİR. [D158 B2b]
CODA LENGTH:       5 sahne (S20-S24) — 3-5 bandının içinde. [D158 B2a]
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
                   Duyulan her ses giysinin içindendir (nefes, eklem, bot).
SILENT SCENES:     25 / 25 (replik yok) · MUTLAK sessiz: S16 · S24
VIRAL INTERSTITIALS: 4 — S8 · S12 · S16 · S20   ⛔ THESE MAY NOT BE CUT
TITLE:             "THE SINKING STAKE" — başlık filmin KURALINI vaat eder
                   (bir kazık batıyor), sonucunu değil. Film bunu 0:14'te
                   teyit eder.
LIBRARY CONTEXT:   aynı raftaki kardeşler (yatay 3-5 dk): THE_FROST_LINE
                   (kar/kırağı, Mars) · THE_RISING_SNOW (kar, süblimleşme
                   çizgisi) · THE_SKYLIGHT · THE_PAYLOAD · LOW_POWER.
                   ⚠️ Kar + süblimleşme bu rafta ÜÇÜNCÜ kez kullanılıyor;
                     ayrım noktası: burada kar AZOTTUR ve novum "sıcak olan
                     iner"dir — çizgi/hat novumu DEĞİLDİR.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme 0
SCENE COUNT:     25            (üç birim EŞİT — D101 kapısı böyle koşulur)
TARGET ASL BAND: 10,0 s (sabit ızgara — eğri yok, bilinçli sapma)
ASL CURVE:       ① 9,0 s · ② 10,0 · ③ 10,0 · ④ 10,0 · ⑤ 10,0
                 ⛔ GEREKÇE SATIRI [D74]: bu hat klibi sabit ~10 s üretiyor
                 ve film 0 kesme / 0 sahne-içi kesme ile tasarlandı. Değişken
                 ASL, kırpma bütçesi gerektirir; kırpma bütçesi olmayan
                 değişken süre KLİP DÜŞÜRÜR [D100 · Last Shift]. Ritim ASL'den
                 değil KADRAJ İÇİNDEN geliyor: ölçek merdiveni 25 sahnede hiç
                 duraklamıyor (ardışık her çift ≥1 kademe) ve palet tek
                 olduğu için örüntü kırıcı yükü ölçek + ses dokusundadır.
GRID:            sahne başlangıcı(n) = 9,0 s hook + (n−1) × 10,0 s klip
                 S0  = 0                     = 0:00
                 S1  = 9 + 0×10   =   9 s    = 0:09   ← katalizör +5,0 s = 0:14
                 S3  = 9 + 2×10   =  29 s    = 0:29   ← tohum +2,0 s = 0:31
                 S12 = 9 + 11×10  = 119 s    = 1:59   ← orta nokta
                 S18 = 9 + 17×10  = 179 s    = 2:59   ← her şeyin kaybı
                 S19 = 9 + 18×10  = 189 s    = 3:09   ← merkezi seçim
                 S21 = 9 + 20×10  = 209 s    = 3:29   ← doruk
                 S24 = 9 + 23×10  = 239 s    = 3:59   ← kapanış
                 film sonu = 239 + 10 = 249 s = 4:09 ✅
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     25 klip × 10,0 s = 250 s  ·  TRIM BUDGET: 1,0 s
                 KIRPMA TABLOSU: S0 ham 10,0 s → kurguda 9,0 s (baştan 1,0 s
                 kırpılır: kazık zaten inerken açılmalı, "hareketin ortası"
                 kuralı). Diğer 24 klip: ham 10,0 s → kurguda 10,0 s, kırpma 0.
                 ⛔ Satırı olmayan klip kırpılmamış sayılır — 25/25 satır var.
SCREEN TEXT:     0 saniye. Filmde başlık kartı, jenerik, altyazı, HUD, ekran,
                 gösterge, kadran ve okunabilir tek bir işaret YOKTUR.
CAMERA:          25 / 25 sabit lockoff (klip içi) · 14 kurulum
SETUP SEQUENCE:  E · D · C · B · A · B2 · F · G · H · D · C2 · B3 · A2 ‖
                 B2 · F · G · J · D · C · B · H · B2 · C2 · K · A2
                 (‖ = bölüm sınırı, S12↔S13)
ANGLE ARC:       5 açı TİPİ — göz hizası · alt açı · üst açı · tepe · OTS
                 (§2 en az 3 ister)
ŞOK BANDI:       2, ikisi de işaretli: S19→S20 ve S20→S21 (3'er kademe)
DORUK:           S21 → THE COLUMN (sahne başlangıcı 209 s = 3:29)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9,0 + (n−1) × 10,0 + promptun TIMELINE ofseti
   Bu filmde replik SAYISI 0'dır; formül boş koşar ve sapma üretemez.
   ⚠️ Rapor "replik zamanı yanlış" bulgusu yazamaz — kayıt yoktur.

FİNAL VURUŞ KANITI [D141]:
   nesne: ince dikey beyaz gaz sütunu · saniye: 245 (4:05) ·
   kaç tane: 2 (biri yakın, biri ufukta) + aralarında 1 düz sığ hendek ·
   BULUNAN mı BULUNMAYAN mı: **BULUNAN**
   ⛔ Bu bilinçli bir karardır [D76]: filmin işareti bir DELİK değil, delikten
     çıkan bir SÜTUNDUR. Yokluk taşıyan final bu depoda çalışmadı.
   ffmpeg -ss 245 -i "$M" -frames:v 1 kanit.jpg   → BAK ve SAY

DÖNGÜ KANITI: bilinçli olarak YOK. Yatay 3-5 dk'da döngü opsiyoneldir
   [FINAL §2]. İlk kare (ECU · tek nesne AŞAĞI) ile son kare (EWS · iki nesne
   YUKARI) bilerek AYNI DEĞİL, TERS kurulmuştur — açılış-kapanış çifti bir
   döngü değil bir DEĞİŞİM okutur [SENARYO §2.3③].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  2222222222222221022222120
       (S0 → S24, sahne başına kadrajdaki insan SAYISI)
       21 sahne × 2 insan · 2 sahne × 1 insan (S15 · S22) ·
        2 sahne × 0 insan (S16 · S24)
⛔ ÜÇÜNCÜ İNSAN 0 KARE. Mürettebat 0, pilot 0, yansımada figür 0,
  fazladan gölge 0. En riskli iki sahne S4 ve S23'tür (araç kadrajda /
  kamera araçta) — KART 4 bu hatayı tam orada ölçtü.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 2 · 25 sahnenin 21'inde ikisi de kadrajda · 2'sinde 1 ·
              2'sinde 0. Üçüncü insan 0 kare.
KASK          25/25 sahnede kapalı · açık 0 sahne · vizör optik berrak,
              tint 0, ayna kaplama 0, ÇEVRE YANSIMASI 0 · her iki yüz de
              her kafa açısında okunur · sırt ünitesi YOK, sırt tek sürekli
              beyaz panel — düz siluet [D79] · OTS sahnelerinde (S6 · S14)
              POZİTİF sırt yüzeyi cümlesi promptta yazılı [D139]
NOVUM         "Zemine bırakılan sıcak her şey karı gaza çevirerek kendi
              çukurunu kazar ve içine iner; hiçbir şey durduğu yerde
              kalmaz." İHLAL ETTİĞİ ŞEY: izleyicinin kar şeması — kara
              basılır, iz bırakılır, kazık dikilir. Burada iz BÜYÜMEYE
              DEVAM EDER ve kazık DURMAZ.
              TAŞIYICI: beyaz kazık ayağı × iki eldivenle bastırma jesti.
              KANIT SAHNELERİ: S0 · S1 · S5-S6 · S7 · S10-S11 · S20 (7 sahne,
              6 farklı nesne: kazık · plaka · kasa · bot izi · iniş bacağı ·
              çekirdek)
YERÇEKİMİ     0,40 g = 3,92 m/s²
              · göğüs yüksekliğinden (1,35 m) düşen nesne 0,83 s'de yerde
              · yürüyüş kadansı: 0,8 s'de bir tam adım, süzülme 0
              · 2,40 m'lik kazığın dikeyden devrilmesi ≈ 1,3 s (S12)
              · tekmelenen kar 1,5 s içinde yerde, düz yay, asılı kalma 0
ATMOSFER      azot buharı ~15 µbar (pratikte vakum) · RÜZGÂR 0 (25/25 sahne)
              · dış ses 0 (25/25) · sıvı 0 kare · erime 0 kare · ıslaklık 0
              · gaz sütunu: dikey, düz, nesneden geniş değil, ~4 m/s,
                6 m'de biter, kıvrılma 0, yanal kayma 0, duman okuması 0
              · gaz sütunu görünen sahne sayısı: 11
                (S0·S1·S2·S5·S6·S7·S8·S11·S18·S20·S21·S22·S23·S24 içinden
                 kadrajda FİİLEN duran: S0·S1·S2·S5·S6·S7·S8·S11·S20·S21·S24)
EKRAN YÖNÜ    Kara delik pusulada 000° / yükseklik 34° — 25/25 sahnede SABİT,
              hiç hareket etmez. Araç 220°'de (kara deliğin TERSİ tarafta) —
              25/25 sahnede aynı yön. Eski sütun 100°'de — S3 · S14 · S16 ·
              S24'te aynı yön. Hedefe hareket 2 sahne (S18 · S23); S23'te
              kamera HEDEFTEDİR ve ışık SIRTLARINDADIR [KART 9 · UZAMSAL §6.8]
SAYAÇ         iniş bacağında GÖRÜNEN teleskopik kademe sayısı:
              3 (S4) → 2 (S11) → 1 (S18). Monotonik ✅ · rakam 0 · çentik 0 ·
              bant 0 · derecelendirme 0. Sayaç bir CİHAZ değil, bir NESNENİN
              GEOMETRİSİDİR. S24'te araç kadrajda yoktur, orada okunmaz.
              ⛔ A1 çelişkisi imkânsız: bu filmde ekran/gösterge/kadran
                HİÇ YOKTUR, dolayısıyla "no text" hiçbir anlatımı silmiyor.
EŞ KADRAJ     **YOK — bilinçli karar [D153].** Metinle taşınamayan bir eş
              kadraj vaadi kurulmadı. S12 ve S24 aynı kurulum ailesindedir
              (A2) ama farklı azimut ve tamamen farklı içerik taşır ve
              "ayna" olarak SATILMAZ. ⚠️ Rapor "eş kadraj tutmamış" bulgusu
              yazamaz — çift yoktur.
YIPRANMA      sabit bölge sayısı: 0 [D42 · D147]. Bu dünyada toz yoktur;
              giysiler filmin başında ve sonunda AYNI temiz beyazdır.
              Kir merdiveni bilerek kurulmadı — dolayısıyla D155'in faz
              etiketi riski yapısal olarak sıfırdır.
              ⛔ Rapor "kir artmıyor" bulgusu yazamaz: artması TASARLANMADI.
              TEK sabit yüz işareti: uzun boylunun şakağında kurumuş tuz
              kabuğu (S15) — bu bir kir kademesi değil, tek bir devamlılık
              çapasıdır.
IŞIK TAKVİMİ  monotonik değil, SABİT: tek kaynak (kara deliğin halkası),
              000° azimut / 34° yükseklik, 25/25 sahnede AYNI yoğunluk ve
              AYNI renk. Gün yok, hava yok, döngü yok, gölge dönmez.
              ⛔ Işık değişimi bulgusu = ÜRETİM HATASI, tasarım değil.
SES REGISTER  HUMAN 0 · MACHINE 0 · DIEGETIC-INTERNAL yalnız.
              Müziksiz sahne: S0 · S16 · S24. Mutlak sessizlik: S16 · S24.
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Aşağıdaki dört kapı bu makinede 02.09.2026'da fiilen sınandı.

```
KAPI ①        KLİP İÇİ KAMERA SABİTLİĞİ — kamera klip içinde hareket etti mi
KOMUT         ffmpeg -hide_banner -v error -i "$K" \
                -vf "crop=96:96:24:24,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
                -f null - 2>&1 | awk -F= '/YAVG/{print $2}' \
                | sort -n | awk 'NR==1{m=$1} {M=$1} END{print "YAVG spread:", M-m}'
KABUL         köşe yaması boş gök/kar olduğu için sabit kamerada spread ≤ 4,0.
              Üstündeyse kamera kaymıştır → klip RET.
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " signalstats " → ✅ VAR
İKAME         gerekmiyor (filtre kurulu).

KAPI ②        FİLİGRAN / KÖŞE TESTİ [D150] — üretici ikonu master'da mı
KOMUT         ffmpeg -v error -ss 120 -i "$M" \
                -vf "crop=in_w/5:in_h/5:in_w*4/5:in_h*4/5" -frames:v 1 kose_sag_alt.png
              (aynı komut dört köşe için: 0:0 · in_w*4/5:0 · 0:in_h*4/5)
KABUL         dört köşenin dördünde de yalnız kar veya gök var → GEÇ.
              Sabit bir ikon/işaret varsa master MASTER DEĞİLDİR.
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 ·
              ffmpeg -hide_banner -filters | grep -q " crop " → ✅ VAR
İKAME         gerekmiyor.

KAPI ③ ⭐     BEYAZ-ÜSTÜNE-BEYAZ KONTRAST KAPISI — bu filmin kendi riski
              Giysi beyaz, kar beyaz, araç beyaz, gaz beyaz. Kadraj tek bir
              parlaklık lekesine çökerse film 120 px'te okunamaz.
KOMUT         ffmpeg -hide_banner -v error -i "$M" \
                -vf "signalstats,metadata=print:key=lavfi.signalstats.YMIN" -f null - 2>&1 \
                | awk -F= '/YMIN/{print $2}' | sort -n | tail -1
              (aynısı YMAX için, sort -n | head -1)
KABUL         her karede YMAX − YMIN ≥ 120 (8-bit). Siyah gök ile beyaz ova
              aynı karede olduğu sürece kolay geçilir; geçilemeyen kare, gökü
              kaybetmiş karedir → o klip yeniden üretilir.
DOĞRULANDI    ffmpeg 8.1 · 02.09.2026 · signalstats ✅ VAR
İKAME         gerekmiyor.

KAPI ④        KLİP SÜRESİ — ızgara araçtan ölçülür [D124]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$K"
KABUL         S0 → 9,0 ± 0,2 s · S1-S24 → 10,0 ± 0,2 s.
              Sapma varsa PLAN'ın IZGARA satırı ve bu SPEC'in GRID satırı
              ölçülen değerle YENİDEN yazılır; runtime da yeniden hesaplanır.
DOĞRULANDI    ffprobe 8.1 · 02.09.2026 · ikili PATH'te ✅ VAR
İKAME         gerekmiyor.

⛔ YAZILMAYAN KAPI — dürüst kayıt [D142]:
KAPI (yazılmadı) TİTREŞİM ANALİZİ (vidstabdetect)
SEBEP            ffmpeg 8.1 bu makinede libvidstab OLMADAN kurulu:
                 ffmpeg -hide_banner -filters | grep " vidstabdetect " → ❌ YOK
                 (02.09.2026'da sınandı). Kurulu olmayan filtreye yazılan kapı
                 SESSİZCE HİÇ KOŞMAZ — D142'nin tam olarak ölçtüğü arıza.
İKAME            KAPI ① yerine geçer ve aynı soruyu köşe yaması üzerinden
                 sorar. vidstabdetect kurulursa bu blok yeniden yazılır.
```
