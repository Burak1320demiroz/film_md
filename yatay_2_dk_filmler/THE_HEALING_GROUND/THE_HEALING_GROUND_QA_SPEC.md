# 📋 THE HEALING GROUND — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretti (04.09.2026):
> `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_HEALING_GROUND/PAKET_1..8`
> ⛔ **ÇIPLAK RUBRİK AÇMA.** THE STILL SWARM'da (01.09) ve THE UPWARD FALL'da
> (04.09) sekiz merceğin sekizi mod V koştu ve hiçbiri tabloya giremedi;
> ikincisinde paket ZATEN VARDI ve operatör yine rubriği açtı [D165 · D129].

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar; ad değişirse üçü birden körleşir.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                   EKRAN YÖNÜ · IŞIK TAKVİMİ · YIPRANMA
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎬 AKSİYON    → A BLOĞU
⑧ 💪 EFOR       → C BLOĞU'nun ZORLANMA satırı
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE HEALING GROUND
FORMAT:            yatay 2-4 dk · 16:9 · 14 sahne × sabit ızgara
RUNTIME:           139 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       14
THEME:             İLK-TEMAS  (FIRST-CONTACT)
                   "Temas, iki tarafın da aynı sıcaklıkta olmasıdır."
THEME SCENES:      S2 · S9 · S11 · S13     ⛔ en az üç ✅
INTENDED EMOTION:  quiet awe, then grief that is never named on screen.
                   ⛔ NOT horror, NOT threat: the creature is never framed as
                   a predator and the film contains no chase, no attack and
                   no contact that harms anyone.
ENDING TYPE:       TWIST + seeded (FINAL §2/§3). Seed: S1 · 0:15-0:17, one
                   thin dark rod standing uncovered on the horizon, 2 s,
                   unremarked. The final returns to what that rod meant.
                   OPEN QUESTIONS AT THE END: exactly 1 (why the cold thing is
                   left alone is answered; what the creature wanted is not).
PROTAGONIST:       an unnamed surveyor, a man in his fifties, alone
                   (isimsiz — özel ad promptta ve SPEC'te geçmez [D34])
CENTRAL CHOICE:    S11 · starts 109.0 s — he shuts down the suit heater so the
                   last marker can reach ambient temperature and stay
                   uncovered. The cost is visible in the same shot: the vapour
                   plume that has stood at his hip since 0.0 s goes out.
DIALOGUE LINES:    4 · register: HUMAN 4 / MACHINE 0
                   All four are a played-back recording, off-screen only; the
                   mouth is not readable in any of the four shots. On-screen
                   speaking mouth: 0 frames. Numbers spoken: 0 [D82].
SILENT SCENES:     10 (S0 S1 S2 S3 S5 S6 S8 S9 S10 S12)
VIRAL INTERSTITIALS: S8 · S10   ⛔ THESE MAY NOT BE CUT
TITLE:             "Nothing Warm Stays on This Ground | THE HEALING GROUND" —
                   promises the rule, not the outcome. The film delivers the
                   rule in the first 9 seconds and its price at 1:49.
LIBRARY CONTEXT:   nearest shelf-mates: THE COLD WELD (vacuum + clean metal:
                   what touches, joins) · THE SINKING STAKE (nitrogen snow:
                   what is set down, sinks) · THE HERD (thick atmosphere,
                   living creature). This film is the repository's FIRST film
                   in which an alien creature is shown at all — every earlier
                   creature stayed at reveal stage K0-K2.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      14
SHOT COUNT:      14 · sahne içi kesme 0
SCENE COUNT:     14
TARGET ASL BAND: 9.9 s (fixed grid — no ASL curve)
ASL CURVE:       ⛔ YOK — sabit ızgara. GEREKÇE SATIRI [D74]:
                 Bu hat klipleri Veo'da 8 s üretip 2 s extend ile 10 s'ye
                 çıkarıyor; değişken çekim süresi KIRPMA TABLOSU zorunluluğu
                 doğurur [D100] ve bu filmde kırpma bütçesi SIFIR tutuldu.
                 Ritim kırpmadan değil KADRAJ İÇİNDEN geliyor (KURGU_RITMI §1
                 ① kanca maddesi): ardışık 13 çiftin 13'ü ≥1 ölçek kademesi +
                 ≥45° taşıyor ve ölçek merdiveni EWS↔ECU arasında 13 kez yön
                 değiştiriyor.
GRID:            sahne başlangıcı(n) = 9,0 s hook + (n−1) × 10,0 s klip
                 S0 0,0 · S1 9,0 · S2 19,0 · S3 29,0 · S4 39,0 · S5 49,0 ·
                 S6 59,0 · S7 69,0 · S8 79,0 · S9 89,0 · S10 99,0 ·
                 S11 109,0 · S12 119,0 · S13 129,0 · SON 139,0
RUNTIME:         139 s = 2:19
RAW FOOTAGE:     14 klip × 10,0 s = 140 s (S0 9 s üretilir) → 139 s
TRIM BUDGET:     0 s   ⛔ kırpma tablosu GEREKMEZ çünkü değişken süre yok
SCREEN TEXT:     0,0 saniye — jenerik/başlık kartı DAHİL [D70/D72]
CAMERA:          14 / 14 sabit lockoff · klip içi hareket 0
SETUP SEQUENCE:  C · A · B · D · B · A · F · E · C · B · D · A · B · C
                 A 24mm EWS göz hizası h1,60 40 m · B 100mm makro ECU üst açı
                 h0,90 0,7 m · C 35mm MS alt açı 22° h0,45 4,0 m ·
                 D 75mm CU profil göz hizası h1,55 2,0 m · E 35mm WS tepe
                 h12 m · F 50mm MS omuz üstü h1,60 2,4 m
ANGLE ARC:       6 açı TİPİ (alt · üst · tepe · göz hizası · profil · OTS)
                 §2 en az 3 ister ✅ · kurulum sayısı 6, bandın içinde (≤7)
DORUK:           S12 → 119,0-129,0 s (sahne başlangıcı 119,0 s); doruk anı
                 sahnenin İÇİNDE: 7,5 s'de kenar kalkar → 126,5 s

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   R1  S4  = 9 + 30 + 2,0  = 41,0 s
   R2  S7  = 9 + 60 + 3,0  = 72,0 s
   R3  S11 = 9 + 100 + 4,5 = 113,5 s
   R4  S13 = 9 + 120 + 6,0 = 135,0 s
   ✅ Dördü de formülle doğrulandı; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   BULUNAN:     1 (bir) koyu ölçüm diski, üstü KAPANMAMIŞ
                + 1 (bir) çift koyu göz (filmin tek ve son gözü)
   BULUNMAYAN:  diskin üstünde beyaz kubbe — 0 tane
   SANİYE:      126,5 s (gözler) · 136,0 s (disk + varlık + adam tek karede)
   ffmpeg -ss 136 -i "$M" -frames:v 1 kanit.jpg   → BAK
   ⛔ "final duygusu" kanıt değildir; yukarıdaki üç sayı tek karede
     sayılabilir olmak zorundadır.
DÖNGÜ KANITI:    ilk kare (S0 · 0,0 s) ↔ son kare (S13 · 139,0 s):
                 AYNI kurulum (C · 35mm · alt açı 22° · h 0,45 m · 4,0 m),
                 aynı ışık, aynı palet, ayna jest (basan eller ↔ duran eller).
                 TEK FARK: ilk karede zeminden bir şey KALKIYOR, son karede
                 hiçbir şey kalkmıyor.
                 ffmpeg -ss 0 -i "$M" -frames:v 1 ilk.jpg
                 ffmpeg -sseof -0.2 -i "$M" -frames:v 1 son.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  11111111111111      (1 = insan var · - = insansız · 14 sahne)
⛔ İnsansız sahne 0: S4 ve S12 makro kadrajlarında bile eldiven kadrajdadır.
  Bu bilinçli bir karardır — KART 10 (insansız sahne + uzun NEGATIVE =
  yapısal red profili) böylece hiç tetiklenemez.

VARLIK ŞERİDİ (K0 iz · K1 çevre · K2 parça · K3 siluet · K4 tam form):
       10102133310244
  S0 1 · S1 0 · S2 1 · S3 0 · S4 2 · S5 1 · S6 3 · S7 3 · S8 3 · S9 1 ·
  S10 0 · S11 2 · S12 4 · S13 4
  ⭐ S9-S10'daki geri iniş bir KARARDIR: doruğun sessizliği orada kurulur.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤ ⑧'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 14 sahnenin 14'ünde · mürettebat 0 · yansıma 0 ·
              ikinci gölge 0 · araç 0 kare
KASK          14/14 KAPALI · açık 0 sahne · vizör optik berrak, tint 0,
              ayna kaplaması 0, yansıma 0 · sırt ünitesi YOK, düz siluet
              [D79] · kamera arkada olan tek sahne S6 ve orada POZİTİF sırt
              yüzeyi cümlesi yazılı [D139]
NOVUM         "Zemin sıcak olan her şeyin üstünü kapatır; ortam
              sıcaklığındaki nesneye dokunmaz." — İHLAL: bir yüzeyin bir
              nesneyi SEÇEREK örtmesi. Kanıt sahneleri S0 (disk) · S2 (bot
              izi) · S9 (soğuk çubuk — TERS kanıt) · S11 (soğumuş disk)
YERÇEKİMİ     0,38 g = 3,73 m/s² · bel yüksekliğinden bırakılan cisim
              0,73 s'de yere iner · kalkan kırağı 0,4 s'de oturur
ATMOSFER      0,90 bar N2+CH4 · 95 K · ~3,2 kg/m³ · ses 199 m/s ·
              rüzgâr 1-2 m/s ve hiçbir şeyi kıpırdatmaz · SIVI 0 kare
EKRAN YÖNÜ    hedef (kubbe dizisi ve uzaktaki çubuk) 14 sahnenin 14'ünde
              kadrajın AYNI yarısında: dizi SOL üçte birden ufka gider,
              çubuk SAĞ üçte birde durur. İlerleme: adam dizinin ucundan
              ufka doğru DEĞİL, dizinin YANINDA kalır — filmde hedefe
              koşulan hiçbir sahne yok (KART 9 yapısal olarak kapalı:
              güneş diski 0 kare, tek baskın kaynak yok)
SAYAÇ         VENT TÜYÜ, monotonik, metinsiz:
              S0-S1 40 cm · S2 36 · S3 33 · S4 30 · S5 28 · S6 25 · S7 22 ·
              S8 20 · S9 17 · S10 14 · S11 0 · S12 0 · S13 0
              ⛔ Hiçbir sahnede ARTMAZ. Gösterge/ekran/kadran 0 kare.
EŞ KADRAJ     S0 ↔ S13 (kurulum C, birebir) · S1 ↔ S5 ↔ S11 (kurulum A) ·
              S2 ↔ S4 ↔ S9 ↔ S12 (kurulum B) · S3 ↔ S10 (kurulum D)
YIPRANMA      3 sabit bölge, üçü de GİYSİ YÜZEYİNDE, göç etmez [D42 · D175]:
              ① SOL önkol MANŞETİNDE ince soluk çizik
              ② SAĞ diz panelinde soluk aşınma
              ③ sağ uyluktaki oker bandın ALT kenarı mat
              ⛔ Çıplak deri 0 kare; negatif ÜÇ BÖLGELİ (yaka üstü + bilek +
                ayak bileği) ve 14 promptun 14'ünde yazılı
IŞIK TAKVİMİ  TEK DURUM, 14/14 sahnede aynı — monotonik değil SABİT.
              Gerekçe: gezegende güneş diski yok, pus hiç açılmıyor, gün
              içinde değişim yok. Işık takvimi tablosu bu filmde
              GEREKMEZ ve yokluğu bir eksik DEĞİLDİR [KART 6b].
              ⛔ Zeminin rengi TEK yerde tarif edilir ("the colour of dry
                bone"), yalnız WORLD bloğunda [D176]. LIGHT bloğu hiçbir
                yüzeye renk atamaz.
SES REGISTER  HUMAN 4 · MACHINE 0 · ekranda konuşan ağız 0 kare
ZORLANMA (⑧)  Efor sahneleri S0 · S2 · S5 · S11. Her birinde EN AZ İKİ
              kanal, ikisi de ELDİVEN/GÖVDE üstünde, DERİ üstünde değil
              [D175]: "the glove's ribbed segments tighten and lift over the
              knuckles" · "two breaths per press, the second one shorter than
              the first" · "his shoulders drop below the line of his hips" ·
              "the rear boot loads and the knee bends before he leans".
              ⛔ `through the glove` kalıbı 28 promptun 28'inde 0 geçiş.
              ⚠️ prompt_kontrol ⑳ dört sahnede (S4 · S6 · S8 · S12) "efor
                fiili var, gövde tepkisi yok" GÖZLEMİ yazıyor. Dördünde de
                fiil VARLIĞA ya da KIRAĞIYA aittir ("the rim lifts", "frost
                lifts"), insana değil — bilinçli kayıt, düzeltme değil.
VARLIK (⑥)    1 yassı form · 1 kesintisiz kenar · 3 duyarga · 1 çift koyu göz
              (yalnız S12-S13) · 1 iyileşmiş SOL kenar çentiği · genişlik =
              adamın omuz genişliği · kütle sınıfı ~6 kg · hız bandı
              0,15-0,9 m/s · geçtiği hatta kırağı 0,4 s'de oturur
              ⛔ Kadrajda AYNI ANDA en fazla 1 varlık; film boyunca TEK varlık
              ⛔ K0-K3 sahnelerinde anatomi SAYISI yazılmaz — S4 · S6 · S7 ·
                S8'in promptlarında uzuv/göz/duyarga sayısı 0 geçiş
              ⛔ Kamera varlığın etrafında TAM TUR DÖNMEZ; iki azimut var
                (B zemin makrosu · F omuz üstü)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> `$M` = master dosyanın yolu.

```
KAPI ①        EKRAN METNİ = 0,0 s · başlık/jenerik kartı yok [D70/D72]
KOMUT         ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.5:pix_th=0.05" \
                -an -f null - 2>&1 | grep black_start
              → çıktı BOŞ olmalı; kuyrukta siyah/kart varsa satır düşer
DOĞRULANDI    ffmpeg 8.1 · 04.09.2026 (blackdetect filtresi kurulu ✅)
İKAME         filtre yoksa son 6 saniyenin kareleri elle çıkarılır:
              ffmpeg -sseof -6 -i "$M" -vf fps=2 kuyruk_%02d.jpg

KAPI ②        SÜRE = 139 s ± 2 s · KLİP SAYISI = 14
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              ffmpeg -hide_banner -i "$M" -vf "select='gt(scene,0.35)',metadata=print" \
                -an -f null - 2>&1 | grep -c pts_time
              → ikinci komut 13 kesme (14 klip) vermeli
DOĞRULANDI    ffmpeg 8.1 / ffprobe 8.1 · 04.09.2026
İKAME         kesme sayısı sahne eşiğine takılırsa eşik 0.25'e indirilir ve
              sonuç ELLE doğrulanır (ızgara sabit: kesmeler 9, 19, 29 … 129 s)

KAPI ③        KONTRAST — koyu giysi soluk zeminde kaybolmasın
KOMUT         ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX" \
                -an -f null - 2>&1 | tail -5
              (aynı komut YMIN ile) → her ölçümde YMAX − YMIN ≥ 110
DOĞRULANDI    ffmpeg 8.1 · 04.09.2026 (signalstats filtresi kurulu ✅)
              ffmpeg -hide_banner -filters | grep -q " signalstats " || kapıyı yeniden yaz
İKAME         filtre yoksa 14 sahnenin 14'ünden birer kare çıkarılır ve
              histogram elle okunur (ffmpeg -ss <t> -i "$M" -frames:v 1 k.jpg)

KAPI ④        SESSİZLİK BIÇAĞI — S12'de 124,5-126,5 s arası MUTLAK sessizlik
KOMUT         ffmpeg -hide_banner -i "$M" -af "silencedetect=n=-50dB:d=1.5" \
                -f null - 2>&1 | grep silence_
              → 124,5 s civarında başlayan ~2 s'lik TEK aralık bulunmalı
DOĞRULANDI    ffmpeg 8.1 · 04.09.2026 (silencedetect filtresi kurulu ✅)
İKAME         aralık yoksa ses yatağı kurguda kesilmemiş demektir; filtre
              yoksa dalga biçimi DaVinci'de elle okunur

KAPI ⑤        SESLİLİK — −14 LUFS · −1,0 dBTP
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12
DOĞRULANDI    ffmpeg 8.1 · 04.09.2026 (ebur128 filtresi kurulu ✅)
İKAME         yoksa DaVinci Fairlight ölçer paneli

KAPI ⑥        FİLİGRAN — köşede üretici ikonu 0 kare [D150 · 3 vaka]
KOMUT         for t in 5 40 75 110 135; do \
                ffmpeg -y -v error -ss $t -i "$M" -frames:v 1 -vf "crop=iw/4:ih/4:3*iw/4:3*ih/4" fil_$t.jpg; done
              → beş karenin beşine de BAK. Filigranlı master master değildir.
DOĞRULANDI    ffmpeg 8.1 · 04.09.2026 (crop filtresi kurulu ✅)
İKAME         yok — bu kapı gözle koşulur, ikamesi yoktur
```

---

## 🔒 ÖNERME KAPISI (⑩) İÇİN — kural tekrarı kesilemez

```
KESİLEMEZ SAHNELER (kurgu kapısı bu listeyi okur):
  S0   novum kurulumu (ölçüm diski kapanır) + KAPAK ANI
  S2   doğrulama, ikinci nesne (bot izi kapanır)
  S8   ⭐VİRAL #1
  S9   TERS kanıt (soğuk çubuk kapanmaz) — filmin mantık ekseni
  S10  ⭐VİRAL #2 + Her Şeyin Kaybı
  S11  MERKEZÎ SEÇİM + BEDEL
  S12  DORUK + FİNAL VURUŞ KANITI + sessizlik bıçağı
  S13  KAPANIŞ İMAJI + DÖNGÜ
⛔ Bu sekizinden biri kurguya girmezse film içerikte değil KURGUDA kaybeder
  [D62 · D72 · KURGU_VE_TESLIM §1]. THE UPWARD FALL'da planlı doruk S24
  kurguya hiç girmedi — aynı hattın en son vakası (04.09.2026).
```
