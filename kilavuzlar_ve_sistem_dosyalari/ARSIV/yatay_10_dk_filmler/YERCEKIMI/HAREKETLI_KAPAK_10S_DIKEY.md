# 🎬 YERÇEKİMİ — HAREKETLİ KAPAK · DİKEY (10 s · CTA KARTI)

## 9:16 · 10,000 s · tek çekim İM2V · **METİN PROMPTUN İÇİNDE**
### Kaynaklar: `HAREKETLI_KAPAK_10S.md` (yatay kardeş) · `KAPAK.md` §KAPAK B · `FRAGMAN_DIKEY.md` §8 §11 · `KANAL_KIMLIGI.md` §1 §5
### Model: Veo 3.1 Fast · İM2V (imaj → video, start frame o imajın kendisi)
### ✅ `prompt_kontrol.py` 07.09.2026 — **GO** · 0 BLOCK · 0 FIX (image 4215 kr · video 2595 kr · tavan 4300)

> **Bu dosya yatay kartın KIRPILMIŞ hâli değildir.** 9:16 kare SIFIRDAN
> üretilir [FRAGMAN §1.1]: 16:9'u dikeye kırpmak sol üçte ikiyi ve
> metin alanını birden keser. Kompozisyon yeniden kuruldu, tipografi
> yeniden hesaplandı, iki prompt yeniden yazıldı.

> ⚠️ **prompt_kontrol.py bilinçli sapma gerekçesi [D74]:** Bu dosya bir
> sahne değil, bir **kapanış kartıdır**. B5 hikâye omurgası burada
> aranmaz — kartın anlatısı yoktur, filmin B5'i `00_PLAN.md`'dedir.
> Emsal: `apexaic/APEXAIC_INTRO_PROMPT.md`. ⚠️ **Metin yasağı bu kartta
> BİLİNÇLE sapar**; izin verilen DÖRT öge sayılıdır (§2), beşincisi
> bulgudur.

---

# 0. 🎯 BU KART NE, NE DEĞİL

```
NEDİR   Dikey fragmanın (ya da herhangi bir dikey kesitin) son 10
        saniyesi. Filmin kapak karesi HAREKET EDER ve üstünde DÖRT
        öge durur — modelin kendisi basar:
             Λ  logo işareti
             APEX AI CINEMA
             FULL FILM NOW
             ON YOUTUBE
        Tek çekim, kesme yok, kamera hareketi yok — hareket kadrajın
        İÇİNDEDİR (sürüklenme · serbest cıvata · camdaki kayan yay);
        YAZI 10 saniye boyunca kıpırdamaz.

DEĞİLDİR
  ⛔ FİLMİN parçası değil. Filmin klip zincirine ASLA girmez
     [D70/D72 · sayaç 12].
  ⛔ Yatay kartın kopyası değil: aynı VAAT, ayrı ÜRETİM. İkisi aynı
     anda kullanılabilir (16:9 fragmanın sonunda yatay kart, 9:16
     kesitin sonunda bu kart).
  ⛔ Shorts kapak fotoğrafı değil — o durağan bir kare, bu 10 s video.
```

---

# 1. ⭐ BU KART NEREYE GİRER — ve "ON YOUTUBE" burada TAM DOĞRU

Yatay kardeşin en büyük açık maddesi buydu: _"YouTube'un kendi üstünde
'on YouTube' gereksiz tekrar."_ **Dikey hatta o sorun yok** — dikey
kesitlerin asıl yeri TikTok ve Reels'tir ve orada izleyici başka bir
platformdadır.

```
⭐ ÖNERİLEN DAĞITIM — üç kopya, iki uzunluk

  TikTok kopyası      FRAGMAN_DIKEY 60 s  +  BU KART 10 s  =  70,000 s
  Reels kopyası       FRAGMAN_DIKEY 60 s  +  BU KART 10 s  =  70,000 s
  YouTube Shorts      FRAGMAN_DIKEY 60 s  KARTSIZ          =  60,000 s
                      → orada iş sabitlenmiş yorum + bitiş ekranıdır;
                        "ON YOUTUBE" satırı kendi evinde tekrar olur.

⛔ ZAMAN KAPISI: kart yalnız FİLM YAYINDAYKEN kesilir. YouTube
   yayınlanmış videonun dosyasını değiştirtmez; film çıkmadan kartlı
   sürüm yüklenirse kart YALAN söyler ve geri alınamaz.
```

```
📐 KARTLI SÜRÜMDE DEĞİŞEN SAYILAR [kural ① — hepsi birlikte]
   `FRAGMAN_DIKEY.md` §12 QA SPEC:
     BİRİMLER   6 klip × 10,000 s = 60,000 s   →   6 klip + kart = 70,000 s
     K1 SÜRE    beklenen 60,000 ± 1,0          →   70,000 ± 1,0
     KESME      5 iç geçiş                     →   6 (1:00,000 eklenir)
     METİN      okunur metin 0,0 s             →   0:00-1:00 metin 0,0 s ·
                                                   1:00-1:10 dört öge
   DEĞİŞMEYEN: ölçek dizisi · şok bandı 2 · insan şeridi · ışık sırası
   (kart bir VURUŞ değildir, kuyruk kartıdır — ölçüme girmez).
⛔ BU DOSYA O SATIRLARI DEĞİŞTİRMEDİ. Dağıtım kararı verilmeden yapılmaz.
```

---

# 2. 🔤 METİN — PROMPTUN İÇİNDE, DÖRT ÖGE

```
✅ SAHİP KARARI (yatay kartla aynı): harfleri MODEL basar.

İZİN VERİLEN DÖRT ÖGE — kadrajın ÜST bandında, siyah uzayın üstünde,
ORTALANMIŞ (yatay kartta sola dayalıydı; dikeyde merkez okunur):
   ① Λ  logo işareti — kalın yukarı şevron, ince bir dairenin içinde
        ⭐ EN İYİ YOL: logo dosyası REFERANS GÖRSEL olarak eklenir
           (emsal `apexaic/APEXAIC_INTRO_PROMPT.md`). Referanssız da
           çalışır — Λ promptta tarif edildi.
   ② APEX AI CINEMA     küçük, harf araları geniş
   ③ FULL FILM NOW      büyük
   ④ ON YOUTUBE         büyük
   ⛔ BEŞİNCİ BİR YAZI BULGUDUR: altyazı, filigran, web adresi,
      @handle, rakam, giysiye/panele yazı — hepsi RET (§7 RET ①).

⚠️ CTA İKİ SATIR KALIR. Dikeyde tek satır daha da imkânsız:
   "FULL FILM NOW ON YOUTUBE" 24 karakter ≈ 1.094 px eder ve 1080
   tuvalin kullanılabilir genişliği 936 px'tir (§5.2). İki satır hem
   sığıyor hem de modelin harf doğruluğuna uygun.

⚠️ FİLM ADI KARTTA YOK — kapaktaki İSİM hâlâ açık karar (KAPAK §0).
   Karar düşerse ③'ün ÜSTÜNE tek satır eklenir. ⛔ "YERÇEKİMİ"
   seçilirse Ç ve İ modelde kırılır; o ad post katmanıyla konur (§5).

🔴 BİLİNEN RİSK [ADAY-7]: bu filmin makaralarında model prompt
   İSTEMEDEN altyazı bastı — F5 2 · F6 3 · F7 7, yedisi de uydurma.
   Araç çağrılmadan yazı koyabiliyor; çağrıldığında da yanlış yazabilir.
   → §7 kabul kapısı "harf var mı" değil "HARFLER DOĞRU MU" diye sorar.
   → Üç denemede tutmazsa PLAN B (§5): kare metinsiz üretilir, dört öge
     post'ta konur. Ölçüler §5'te hazır.

⭐ BEDELSİZ ÖNLEM: video promptunda `Audio:` PARAGRAFI YOKTUR.
   ADAY-7'de elde kalan tek şüpheli değişken oydu; kartın ses ihtiyacı
   sıfır (§6). ⛔ F9/S107 deneyinin YERİNE GEÇMEZ.
```

---

# 3. 📱 GÜVENLİ ALAN VE KOMPOZİSYON — dikeyin kendi matematiği

```
┌─────────────────────────┐  0%
│  ÜST %13 — ARAYÜZ       │   kanal adı, başlık üst bandı
├─────────────────────────┤  13%
│  Λ + APEX AI CINEMA     │   %14 – %22
│                         │
│  FULL FILM NOW          │   %26 – %34
│  ON YOUTUBE             │
│                         │
│  🧍 ASTRONOT + KAFES     │   %42 – %62   ⭐ güvenli alanın ortası
│                         │
│  🌍 DÜNYA UFKU          │   %68'de geçer
├─────────────────────────┤  75%
│  ALT %25 — ARAYÜZ       │   yalnız bulut dokusu; okunacak şey YOK
└─────────────────────────┘  100%
     ⬅ sağ %12,5 ➡ beğen/yorum/paylaş sütunu — metin oraya girmez
```

```
⭐ YATAY KARTTAN ÜÇ FARK — ve üçünün de sebebi dikeyin kendisi:
  ① METİN SOLA DEĞİL ORTAYA. Yatayda özne sağ üçte birdeydi ve sol
     yarı boştu. Dikeyde özne ORTADADIR; boş olan ÜST banttır.
  ② YAZI ÖZNENİN ÜSTÜNDE, YANINDA DEĞİL. Okuma sırası da doğru
     olur: önce marka + çağrı, sonra kare.
  ③ ÖZNE %24 → %20. Dikeyde kadraj yüksekliği 1920'dir; %24 onu
     460 px yapar ve figür kartın konusu olur. Kartın konusu YAZIDIR;
     figür ölçek şokunu taşır, sahneyi çalmaz.
  ⛔ Dünya'nın ufku %68'dedir: hiçbir harf gezegene DEĞMEZ, hepsi
     siyah uzayın üstünde durur (kontrast ≈ 21:1).
```

---

# 4. 🎬 KART — İLK KARE

`master 1:00,000-1:10,000 (kartlı sürüm)` · 35mm · üst açı 25°, WS · lockoff · 10,0 s
**GEOMETRİ KAYNAĞI:** `KAPAK.md` §KAPAK B — aynı lens, aynı açı; oranlar 9:16 için yeniden kuruldu.

```
⚙️ Tek çekim, 0 kesme, 10,0 s. TEK hareket YOK — kamera tam kilitli.
İŞLEV: filmin kapak karesi NEFES ALIR; ayağının altında zemin değil
gezegen olduğu 10 saniye boyunca durur, yazı onun ÜSTÜNDE sabit kalır.
⭐ DİKEY KOMPOZİSYON: siyah uzay ÜST YARI (yazı orada), astronot ORTA
   banda, Dünya ALT ÜÇTE BİR. Yatay kartta yazı SOLDAYDI; burada
   ÜSTTE — çünkü dikeyde boş olan yer üsttür ve okuma sırası
   marka → çağrı → kare olur.
⭐ REFERANS GÖRSEL: logo dosyası imaj üretimine EKLENİR (§2 ①).
Kask çapası GÜNCEL kuşaktan (fragman §2④): biçim iddia edilmez [D146].
```

### 📸 IMAGE PROMPT

```
SCENE: A cinematic vertical end-card: one small astronaut floats alone
above the curve of a planet with nothing underneath her; above her,
across the black sky, a studio logo and a call to action in white type.

TEXT — RENDER EXACTLY, AND THIS IS THE ONLY TEXT IN THE FRAME: All type
is centred in the upper part of the frame over black space, in a heavy
condensed sans-serif, solid near-white, edges sharp, spacing even. Top
to bottom: FIRST, a logo mark — a bold upward chevron, a capital Greek
lambda drawn as two straight thick strokes meeting at a sharp apex,
standing inside a thin circle; if a reference logo image is attached,
reproduce that mark exactly instead. SECOND, directly under the mark,
one small widely letter-spaced line reading APEX AI CINEMA. THEN a clear
empty gap, and below it two large stacked lines, the biggest type in the
frame, reading FULL FILM NOW on the upper line and ON YOUTUBE on the
lower line. Every word is spelled exactly as written here, letter for
letter, in capitals, with no extra words, no punctuation, no duplicated
line and no misspelling.

ENVIRONMENT: Hard vacuum in low orbit. Black space with hard pinpoint
stars fills the upper half and carries the type. The sunlit curve of
Earth fills the lower third and the bottom, blue-white and banded with
cloud, its horizon a clean bright arc, the glare of daylit ocean through
thin cloud. A white lattice truss with ORANGE handrails runs in from the
screen-right edge to a grey cylinder with an open panel. ONE loose bolt
drifts free beyond the panel edge on a straight line. No spacecraft, no
station, no debris.

SUBJECT: Exactly one human figure, human count 1, small and alone at the
centre of the frame at twenty percent of frame height. A 38-year-old
woman flight engineer in a warm off-white pressure suit with ORANGE
reinforcement stripes on shoulders, knees and glove cuffs, floating
free, feet off every surface, upright and calm. Her gloved RIGHT hand
holds the hinged cover half shut; her gloved LEFT hand grips an orange
handrail. An orange-and-white tether runs taut from her hip to the rail.
Her head is inside a rigid white helmet shell holding a clear front
glass in a bright metal rim, optically clear, zero tint, no mirror
coating; her face a small pale shape tipped down toward her hands. Her
back silhouette is flat: off-white fabric, one spine seam, a low webbing
belt, no pack, tank, hose or cable.

CAMERA: Shot on a 35mm lens at f/8, from a fixed position 14 metres out
and above the platform, high-angle, camera pitched down 25 degrees. Deep
focus, accurate perspective and true scale.

COMPOSITION: Vertical 9:16. The logo mark and APEX AI CINEMA sit between
fourteen and twenty-two percent of frame height, the two large lines
between twenty-six and thirty-four percent, centred and clear of the
outer right eighth. The astronaut and the truss hold the middle of the
frame between forty-two and sixty-two percent. Earth's horizon crosses
at about sixty-eight percent; the bottom quarter carries only cloud
texture. No part of any letter touches the planet, the truss or the
figure.

LIGHTING: One hard white sun from the upper screen-right: a bright rim
along her helmet, her shoulder and the truss, lattice shadows absolute
black. Cool blue bounce from Earth separates her pale suit from the
black space above. The type is flat and even, lit by nothing, with no
glow and no shadow.

PHYSICS: Zero gravity. The tether is straight and taut. Nothing hangs,
settles or falls. The free bolt holds one straight line, no arc, no
trail.

NEGATIVE: Exactly one human figure, human count 1 — no second person, no
reflected person, no duplicate. Stripes stay ORANGE. Both glove cuffs
are bare: no ring, no band, no bracelet. No sweat, no liquid, no fog
inside the glass. 0% bloom, no glow filter, no lens flare, no light
rays, no haze, no smoke. Apart from the logo mark, APEX AI CINEMA, FULL
FILM NOW and ON YOUTUBE, there is no other writing anywhere in the
frame: no subtitles, no caption, no watermark, no web address, no
handle, no numerals, and nothing written on the suit, the truss or any
surface. Photorealistic photography, 35mm film grain.

OUTPUT: 9:16, 4K, sharp legible type, no watermark.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

> Start frame: yukarıdaki onaylanmış imaj. ⛔ `Audio:` paragrafı BİLEREK
> yok (§2). ⭐ Promptun İLK bloğu TEXT LOCK'tur: yazı kadrajın
> İÇİNDEDİR, kamera kayarsa harfler de kayar ve model onları her karede
> YENİDEN yazmak zorunda kalır — harf bozulmasının bir numaralı sebebi.

```
Maintain the framing, the figure, the lighting and ALL THE TYPE exactly
as in the first frame.

TEXT LOCK — the type never changes. The logo mark, the small line
APEX AI CINEMA and the two large stacked lines FULL FILM NOW and
ON YOUTUBE stay centred in the upper part of the frame at the same
position, the same size and the same spelling for all ten seconds. The
letters never drift, fade, flicker, warp, re-form, duplicate or turn
into other words, and no new writing appears anywhere in the frame.

MOTION — 10 seconds, 35mm, fixed lockoff 14 metres out and above the
platform, high-angle, camera pitched down 25 degrees, no cuts, no camera
movement, no zoom:

SETUP: vertical 9:16. Black space with hard stars fills the upper half
and carries the type; Earth's sunlit curve fills the lower third. A white lattice truss with ORANGE
handrails runs in from the screen-right edge to a grey cylinder with an
open panel. Exactly one human figure, human count 1: a
38-year-old woman flight engineer in a warm off-white pressure suit with
ORANGE stripes, at twenty percent of frame height in the middle of the
frame, feet off every surface, her gloved right hand on the half-shut
cover, her gloved left hand on the rail, a tether taut from her hip to
the rail. Her back stays flat: no pack, tank or hose.

0s — Nothing is settled: her body drifts a few centimetres against the
rail and keeps drifting. One loose bolt is already crossing frame on a
dead straight line at one constant speed.
2s — The bolt holds that line and speed, no arc and no trail, and leaves
frame at the screen-left, passing under the type.
4s — Her right hand pushes the hinged cover the last of the way and it
seats flat. Nothing else in the frame moves.
6s — The blue-white arc of Earth reflected in her front glass slides
slowly toward the screen-left and keeps sliding — the only proof
anything is turning.
8s — She lifts her head and looks out past the rail at the planet. One
slow travelling wave runs along the taut tether and dies.
10s — Last frame: she is still holding, head up, the planet under her,
the type unchanged. No cut.

Zero gravity: nothing hangs, nothing falls, nothing settles. The tether
never goes slack. No second person enters, no reflected person, no
duplicate. Stripes stay ORANGE. Both glove cuffs stay bare. Single
unbroken take, no cuts, no shake. 0% bloom, no glow filter, no lens
flare, no light rays, no haze, no smoke. Apart from the four locked elements there is
no other writing anywhere in the frame: no subtitles, no caption, no
watermark, no numerals. Photorealistic, 35mm film grain.
```

---

# 5. ✍️ PLAN B — TİPOGRAFİ KATMANI (post)

> ⚠️ **BU BÖLÜM YEDEKTİR.** Ana yol §2'dir: harfleri model basar. Bu
> katman YALNIZ iki durumda açılır — ① model üç denemede dört ögeyi
> doğru yazamazsa, ② film adı kartta "YERÇEKİMİ" olarak istenirse
> (Ç ve İ modelde kırılır). O zaman kare METİNSİZ üretilir (iki
> promptun TEXT ve NEGATIVE blokları "no readable text ... anywhere in
> the frame" ile değiştirilir) ve yazı aşağıdaki ölçülerle konur.

## 5.1 ⭐ PUNTO DEĞİL PİKSEL — sayı testten geri hesaplandı

```
ZORUNLU TEST: 360 px genişlik — telefonda, en düşük kalitede, akışta.
  1080 → 360   ölçek = 0,3333
  okunabilirlik için versal ≥ 7 px  →  7 ÷ 0,3333 = 21 px
  yani 1080 tuvalde MUTLAK ALT SINIR versal 21 px.

TUVAL: 1080×1920. ⚠️ 4K dikey (2160×3840) ise TÜM SAYILAR ×2.
⭐ Yatay kardeşin tuvali 1920 GENİŞtir, bu tuval 1080 geniştir —
   sayılar taşınmaz, YENİDEN hesaplanır. Aynı testin dikey cevabı.
```

## 5.2 DÖRT ÖGE — ölçü ve genişlik

```
Λ İŞARETİ        yükseklik 56 px · çevresindeki ince daire çapı 76 px

APEX AI CINEMA   versal 32 px  →  360 px'te 10,7 px  ✅ (alt sınır 21)
  Bebas Neue versal ≈ 0,73 em  →  font 32 ÷ 0,73 ≈ 44 px
  tracking +160/1000 em (geniş) ≈ +7,0 px/harf
  ilerleme 0,45 em ≈ 19,8 + 7,0 = 26,8 px/harf
    "APEX AI CINEMA"  14 karakter  →  ~375 px  ✅

CTA — İKİ SATIR  versal 68 px  →  360 px'te 22,7 px  ✅✅ baskın
  font 68 ÷ 0,73 ≈ 93 px · tracking +40/1000 em ≈ +3,7
  ilerleme 0,45 em ≈ 41,9 + 3,7 = 45,6 px/harf
    "FULL FILM NOW"   13 karakter  →  ~593 px  ✅
    "ON YOUTUBE"      10 karakter  →  ~456 px  ✅
  kullanılabilir genişlik 1080 − 72 − 72 = 936 px

  ⛔ TEK SATIR MATEMATİKSEL OLARAK İMKÂNSIZ:
     "FULL FILM NOW ON YOUTUBE" 24 karakter ≈ 1.094 px > 936 px.
     Yatayda "sığar ama riskli"ydi; dikeyde TAŞIYOR. İki satır zorunlu.
  ↔ Alternatif: "WATCH THE FULL FILM NOW" → "WATCH THE" + "FULL FILM
     NOW" olarak aynı bloğa girer. ⚠️ Dikey hatta GEREKMEZ (§1).

FİLM ADI (karar düşerse — KAPAK §0 hâlâ açık)
  CTA'nın ÜSTÜNE tek satır eklenir, CTA versali 68 → 56 px'e iner ve
  blok yeniden dizilir. 56 px'te (font ≈ 77, ilerleme ≈ 37,8):
    "YERÇEKİMİ" ~340 · "IT HOLDS ONE" ~454 ·
    "NINETY MINUTES" ~529 · "HAND OVER HAND" ~529      dördü de ✅
  ⛔ "YERÇEKİMİ" MODELE YAZDIRILMAZ — Ç ve İ kırılır; post'ta konur.
  🔴 UZUNLUK UYARISI: image promptu 4.215 karakterdir, tavan 4.300.
     Ada bir satır eklemek TEXT bloğunu ~120 karakter büyütür ve
     promptu TAVANIN ÜSTÜNE çıkarır → BLOCK. Ad eklenirse ENVIRONMENT
     ve NEGATIVE'den eşdeğer kısaltma yapılır ve betik TEKRAR koşulur.
```

## 5.3 KONUM · RENK · KENAR

```
KONUM (1080×1920, sol-üst orijin · hepsi ORTALANMIŞ, x merkezi 540)
  Λ İŞARETİ        y = 272 – 348
  APEX AI CINEMA   versal üstü y = 380   alt y = 412
  (boşluk)
  FULL FILM NOW    versal üstü y = 500   alt y = 568
  ON YOUTUBE       versal üstü y = 586   alt y = 654

  ✅ Dünya'nın ufku %68 = y 1306. Blok 654'te biter → hiçbir harf
     gezegene DEĞMEZ; hepsi siyah uzayda, kontrast ≈ 21:1.
  ✅ En geniş satır 593 px, ortalı → sağ kenarı x 836 < 945
     (sağ %12,5 sınırı) ✅ · sol kenarı x 244 > 72 ✅
  ⛔ YASAK ÜST ŞERİT   y < 250   (%13 arayüz)
  ⛔ YASAK ALT ŞERİT   y > 1440  (%25 arayüz: açıklama, ses, butonlar)
  ⛔ YASAK SÜTUN       x > 945   (%12,5 beğen/yorum/paylaş)

RENK VE KENAR
  Harf        yakın beyaz #E8F7FF   (KANAL_KIMLIGI §5.3 wordmark rengi)
  Dış çizgi   3 px saf siyah #000000, %100 opak
  Gölge       8 px siyah, %60 opak, 0° kayma (yönsüz halka gölge)
  ⚠️ Kontur/gölge YATAY KARTIN SAYISI DEĞİL: orada versal 120 px'ti,
     burada 68. Kenar TİPLE ölçeklenir, tuvalle değil.
  ⛔ TURUNCU HARF YASAK — turuncu bu filmde İNSANIN rengidir
     (klon kapısının ayırt edici işareti, REFERANS_PAKETI RC p3).
  ⛔ Glow / bloom / parlama YOK (LOGO_STING sınırı: glow ≤ 12 px).

ZAMANLAMA (kart içi, 10,000 s — yatay kartla AYNI)
  0,0 – 0,6 s   yazı yok — kare tek başına okunur
  0,6 – 1,0 s   Λ + APEX AI CINEMA 0,4 s'de açılır, sona kadar durur
  3,0 – 3,4 s   CTA iki satırı 0,4 s'de açılır, sona kadar durur
  → CTA ekranda 6,6 s ✅
  ⛔ Kayma yok · ölçek yok · parlama yok · harf harf yazılma yok.
```

---

# 6. 🔊 SES — kart SESSİZDİR

```
`FRAGMAN_DIKEY.md` §10: müzik 0:00-0:56 tırmanır, 0:56'da SERT KESİLİR,
son 4 saniye yalnız cızırtı ve nefes. Kart o sessizliğin devamıdır.

KART SESİ: yalnız telsiz taşıyıcı cızırtısı — müzik 0, replik 0.
  → Kartlı sürümde §12 K3 penceresi 0:56-1:10'a uzar; beklenti aynı
    kalır (mean_volume ≤ −40 dB).
⛔ Karta müzik/stinger/whoosh EKLENMEZ: vakumda dış ses 0 kuralını ses
   tasarımı da çiğnemez ve eklenirse §12'nin sayısı değişir [kural ①].
```

---

# 7. 🚪 KABUL / RET — kart teslim edilmeden önce

```
KABUL
  ① 360 px genişliğe küçült: APEX AI CINEMA ve iki CTA satırı okunuyor.
  ② ⭐ DÖRT ÖGE HARFİ HARFİNE DOĞRU — klip kare kare taranır:
        ffmpeg -i kart_dikey.mp4 -vf fps=5 -q:v 2 kare_%03d.jpg
        → 50 karenin 50'sinde birebir şunlar okunacak:
             Λ   ·   APEX AI CINEMA   ·   FULL FILM NOW   ·   ON YOUTUBE
  ③ BEŞİNCİ YAZI YOK: altyazı, filigran, web adresi, @handle, rakam,
     giysi/panel üstünde yazı — hiçbiri yok.
  ④ Harfler siyah uzayda; hiçbiri Dünya'ya, kafese ya da figüre
     değmiyor. Metin bloğu üst %13 ve sağ %12,5 sütununa girmiyor.
  ⑤ Kamera 10 s boyunca 0 piksel oynadı.
  ⑥ Serbest cıvata DÜZ çizgide, SABİT hızda geçti — kavis, iz,
     yavaşlama yok (0g kanıtı).
  ⑦ Halat 10 s boyunca GERGİN kaldı; hiç sarkmadı, hiç kıvrılmadı.
  ⑧ Kadın hiçbir yüzeye oturmadı; sürüklenme SON KAREDE de sürüyor.
  ⑨ İki eldiven manşeti de çıplak: halka 0 kare, saat 0 kare
     [F7 K2 — iki nesne aynı bileğe yazılırsa model onları BİRLEŞTİRİR].

RET
  ① Harf bozuksa / eksikse / fazladan yazı varsa — YENİDEN ÜRETİLİR.
     ⛔ Bozuk harfin ÜSTÜNE tipografi yazılarak kurtarılmaz.
     ⛔ ÜÇ deneme sınırı: üçünde de tutmazsa §5 PLAN B'ye geçilir.
  ② Yazı bir karede kayıyor / titriyor / yeniden şekilleniyorsa.
  ③ Kamera kaydıysa / zoom yaptıysa / titrediyse.
  ④ Cıvata kavis çizdiyse veya iz bıraktıysa — yerçekimi sızdı.
  ⑤ Halat gevşediyse (o görüntü fedanın işaretidir) ya da ikinci bir
     insan / camda yansıyan insan çıktıysa.
  ⑥ Vakumda pus, ışık hüzmesi, lens flare, halo varsa.
  ⑦ Bilekte halka ya da saat çıktıysa.
  ⑧ İmaj ile videonun ilk karesi arasında kadraj/ışık/yazı kayması
     varsa.

YABANCI GÖZ  Filmi bilmeyen birine 10 s göster, iki soru:
  "Bu kişi neyin üstünde duruyor?"  → "Hiçbir şeyin / boşlukta"
  "Şimdi ne yapman gerekiyor?"      → "YouTube'da filmi izlemek"
  İkincisi gelmiyorsa CTA yeterince baskın değildir (§5.2 versali).

SONUÇ  ☐ GEÇTİ   ☐ YENİDEN ÜRET      seed: __________
```

---

# 8. ⛔ BU DOSYADA OLMAYANLAR — dürüst kayıt

| Yapılmayan | Neden |
|---|---|
| Yatay kartın kırpılması | 16:9'u dikeye kırpmak metin alanını ve kompozisyonu birden keser [FRAGMAN §1.1]. Bu kare sıfırdan üretilir. |
| `FRAGMAN_DIKEY.md`'nin güncellenmesi | §1'de değişecek dört sayı hazır; dağıtım kararı (kartlı 70 s / kartsız 60 s) sahibindir [kural ①]. |
| KAPAK A geometrisi | Yatay kartın §1③'ü ile aynı sebep: `YERCEKIMI_FRAGMAN_YATAY.md` §3 "ölçek karesi S45"i yasaklıyor ve kart fragmanın içinde yaşıyor. |
| Film adı satırı | KAPAK §0 açık karar. Ölçüsü §5.2'de hazır bekliyor. |
| Seed numarası | İmaj henüz üretilmedi. Üretilince §7 SONUÇ satırına yazılır. |
| Müzik / stinger | §6: kuyruk sessizdir ve sessizlik §12 K3'ün ölçtüğü sayıdır. |
| Ayrı bir kare (yeni sahne) | Kart filmin KAPAK anını taşır (S1 · KAPAK B). Yeni içerik fragmana yazılmaz [FRAGMAN §5③]. |

```
⛔ ÇAKIŞMA DENETİMİ — SAHNE:
   FRAGMAN_DIKEY (6): S17 · S19 · S23 · S32 · S33 · S36
   BU KART        (1): S1 ailesi (KAPAK B geometrisi)
   Kesişim: 0 ✅ — kart altı vuruşun hiçbirini tekrar etmez.
   Yatay kardeş de aynı kareyi taşır: bu KASITLIDIR — iki formatta
   aynı kapak, aynı vaat, ayrı üretim.
```

---

> **Bu dosya ne zaman güncellenir**
> □ dağıtım kararı (kartlı 70 s / kartsız 60 s) verilirse → §1 kapanır
> □ kapaktaki İSİM kararı düşerse (KAPAK §0) → §5.2 tek blok güncellenir
> □ imaj üretilirse → §7 SONUÇ + seed
> □ klip üretilirse → §7 ② tarama sonucu; uydurma harf çıkarsa
>   `GOZLEM_DEFTERI` ADAY-7 kaydına **yeni vaka** olarak işlenir
> □ kart kurguya girerse → `FRAGMAN_DIKEY.md` §12 SPEC ile VIDEO_QA MOD D
