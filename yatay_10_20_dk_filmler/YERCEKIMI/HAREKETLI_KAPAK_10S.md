# 🎬 YERÇEKİMİ — HAREKETLİ KAPAK (10 s · CTA KARTI)

## 16:9 · 10,000 s · tek çekim İM2V · **METİN PROMPTUN İÇİNDE**
### Kaynaklar: `KAPAK.md` §KAPAK B + §7 · `YERCEKIMI_FRAGMAN_YATAY.md` §1 §3 §11 · `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §6 · `FRAGMAN_KILAVUZU.md` §1.7
### Model: Veo 3.1 Fast · İM2V (imaj → video, start frame o imajın kendisi)
### ✅ `prompt_kontrol.py` 06.09.2026 — **GO** · 0 BLOCK · 0 FIX (image 4038 kr · video 2593 kr · tavan 4300)

> **Bu dosya `KAPAK.md` §10'un açık bıraktığı tek satırı kapatır:**
> _"Motion poster promptu | Ayrı iş; KAPAK §6 Runway akışı var ama bu film
> için fragman kılavuzu farklı bir yapı tanımlıyor — çakışırsa
> FRAGMAN_KILAVUZU kazanır."_ — Kart o yüzden Runway 4-5 s kalıbına değil,
> **fragmanın kendi 10 s'lik Blok Z yuvasına** yazıldı.

> ⚠️ **prompt_kontrol.py bilinçli sapma gerekçesi [D74]:** Bu dosya bir
> sahne değil, bir **kapanış kartıdır**. B5 hikâye omurgası (İSTEK ·
> ENGEL · BEDEL · MUHATAP) burada aranmaz — kartın anlatısı yoktur, filmin
> B5'i `00_PLAN.md`'dedir. Emsal: `apexaic/APEXAIC_INTRO_PROMPT.md` aynı
> sapmayı aynı gerekçeyle beyan etti. ⚠️ **Metin yasağı bu kartta
> BİLİNÇLE sapar** — emsal aynı dosya: _"Logo intro'nun konusu metnin
> kendisidir; yasak yalnız logo DIŞI her yazıyı kapsar."_ Kartta izin
> verilen DÖRT öge sayılıdır (§2); beşincisi bulgudur.

---

# 0. 🎯 BU KART NE, NE DEĞİL

```
NEDİR   Fragmanın son 10 saniyesi. Filmin kapak karesi HAREKET EDER
        ve üstünde DÖRT öge durur — modelin kendisi basar:
             Λ  logo işareti
             APEX AI CINEMA
             FULL FILM NOW
             ON YOUTUBE
        Tek çekim, kesme yok, kamera hareketi yok — hareket kadrajın
        İÇİNDEDİR (sürüklenme · serbest cıvata · camdaki kayan yay);
        YAZI 10 saniye boyunca kıpırdamaz.

DEĞİLDİR
  ⛔ FİLMİN parçası değil. Filmin klip zincirine ASLA girmez —
     kuyruk kartı D70/D72'nin en pahalı tekrarıdır (sayaç 12; en son
     05.09.2026 THE STANDING WIRE'da 5,0 s'lik kart kurguya sızdı ve
     planlı açılış-kapanış kafiyesini öldürdü).
  ⛔ YouTube kapak fotoğrafı değil. O `KAPAK.md`'dir, 1280×720 durağan.
     Bu kart onun HAREKETLİ ve ÇAĞRILI hâlidir, ayrı teslim.
  ⛔ APEXAIC logo introsu değil. O ayrı bir varlık
     (`apexaic/APEXAIC_INTRO_PROMPT.md`) ve Blok A'da yaşar.
```

**Neden 10 saniye üretilebilir:** 06.09.2026 ölçümü kapandı — sahibin
güncel hattı **12 segment · 120 s · klip 10,0 s** üretiyor
(`FAZ_07_SES/FAZ_07_QA_DERSLER.md` · `FAZ_09_DUSUS.md` ölçüm bloğu).
10 s bir tahmin değil, **ölçülmüş ızgara**. Fragmanın 8 s'lik gövde
ızgarasıyla da çakışmaz: Blok Z zaten 10,000 s'lik bir yuvadır.

---

# 1. ⚠️ ÜÇ ÇELİŞKİ — üretimden ÖNCE okunur

> Üçü de gerçek ve üçü de bu dosyanın dışında bir belgeyi ilgilendiriyor.
> Kural ① gereği hiçbiri sessizce düzeltilmedi; **rapor edildi**.

## ① BLOK Z DOLU — kart oraya girerse bir şey çıkar

`YERCEKIMI_FRAGMAN_YATAY.md` §1 master çizelgesi:

```
│ BLOK Z · APEXAIC KAPANIŞ      1:50.000 – 2:00.000    10.000 s   │
│          grafik · Veo değil · sabitlenmiş yorumda film linki    │
```

O yuva **doludur**. İki yerleşim var ve ikisinin de aritmetiği yazılı:

```
⭐ YERLEŞİM ① — KART, BLOK Z'NİN YERİNE GEÇER          ← ÖNERİM
   0:00-0:10 APEXAIC giriş · 0:10-1:50 gövde · 1:50-2:00 KART
   DEĞİŞMEYEN SAYILAR (hepsi §11'de):
     · toplam 120,000 s ± 2,0                        ✅ aynı
     · kesme listesi (son kesme 1:50.000)            ✅ aynı
     · K1 ffprobe beklentisi 120,000 ± 2,0           ✅ aynı
     · K2 penceresi 10-110 s, 13 iç geçiş            ✅ aynı
     · K3 button sessizliği 102-110 s                ✅ aynı
   BEDEL: kapanış logosu düşer, marka yalnız Blok A'da kalır.
   TELAFİ YOK, GEREKMİYOR: marka kartın İÇİNDE — Λ işareti +
     APEX AI CINEMA kadrajın sol yarısında, promptta yazılı.
   DEĞİŞECEK: §1 çizelgesi + §2 sapma ③ + §11 C METİN — üç satır (§8).

   YERLEŞİM ② — KART, BLOK Z'DEN SONRA (toplam 2:10)
   DEĞİŞEN SAYILAR: master toplam 120,000 → 130,000 · §11 B BİRİMLER ·
     K1 beklentisi 130,000 ± 2,0 · §1 çizelgesi · kesme listesine
     2:00.000 eklenir — BEŞ yerde, kural ① gereği AYNI ANDA.
   DEĞİŞMEYEN: K2 (10-110 s) ve K3 (102-110 s) pencereleri ✅
   KAZANÇ: kapanış logosu yerinde kalır.
```

## ② "NOW" DİYOR, PAKETLEME "COMING" DİYOR

```
Kart (bu dosya) :  FULL FILM NOW ON YOUTUBE
Fragman §10     :  "Full film coming to this channel."
                                ^^^^^^
```

İkisi aynı anda doğru olamaz. **Kart yalnız film YAYINDAYKEN geçerlidir.**
Ve YouTube yayınlanmış bir videonun dosyasını değiştirmeye izin vermez —
yani bu bir kurgu kararı değil, bir **yayın sırası** kararıdır:

```
(a) FRAGMAN FİLMDEN SONRA (ya da aynı gün) YAYINLANIYORSA
    → kart baştan Blok Z'dedir, §10 açıklaması "coming" → "now" olur.

(b) FRAGMAN ÖNCE YAYINLANIYORSA (teaser hattı — §10'un bugünkü hâli)
    → YouTube fragmanında kart YOKTUR (Blok Z = APEXAIC kalır);
      o sürümde işi bitiş ekranı + sabitlenmiş yorum yapar.
    → Kart, film çıktıktan sonra ÇAPRAZ YAYIN kopyalarının son 10
      saniyesi olarak yaşar (`apexaic/CAPRAZ_YAYIN.md`).
    ⭐ Ve "ON YOUTUBE" ifadesi tam da orada DOĞRU okunur: TikTok /
      Reels / Shorts izleyicisi başka bir platformdadır.
```

⭐ **Metin seçimi bu ayrımın kendisidir:**

```
"FULL FILM NOW ON YOUTUBE"      24 karakter · KİLİTLİ (sahip talebi)
                                → çapraz yayın kopyaları için DOĞRU
"WATCH THE FULL FILM NOW"       23 karakter · aynı ölçü, aynı blok
                                → YouTube'un KENDİ üstünde daha doğru
                                  ("on YouTube" orada gereksiz tekrar)
İkisi de §5'in ölçüleriyle sığar; değişen tek şey harf sayısıdır.
```

## ③ KAPAK A KULLANILAMADI — fragmanın kendi spoiler kapısı

`KAPAK.md`'nin lansman kapağı **KAPAK A**'dır (yüz %62 + gergin ip +
uzakta ikinci figür, kaynak S43-S45). Kart onunla yazılmadı, çünkü
`YERCEKIMI_FRAGMAN_YATAY.md` §3 birebir şunu yasaklıyor:

```
⛔ FEDA ZİNCİRİ (S37-S48): temas, dolanma, kancayı açan el, iki uç,
   ölçek karesi S45 — komutanın kaderi fragmanda YOKTUR
```

KAPAK A **tam olarak o karedir**: bir uçta kadın, gergin ipin öbür
ucunda çok küçük ikinci insan. Kart fragmanın İÇİNDE yaşadığı için
§3 kapısı onu da bağlar.

```
✅ SEÇİLEN: KAPAK B geometrisi — "AŞAĞISI YOK" (S1 · 0:05).
   ① §3'ün hiçbir maddesine dokunmaz.
   ② Planın KENDİ kapak anıdır (00_PLAN §HOOK·KAPAK·FİNAL) ve
      `PAKETLEME §1`in 0:00-0:10 bandı kuralının İÇİNDEDİR.
   ③ Fragmanın SAHNE 2'siyle ("AŞAĞISI YOK") kafiye kurar: fragman
      gökle açılır, aynı yalnız figürle kapanır.
   ④ 10 saniyede yüz-CTR argümanı zayıflar (izleyici zaten 2 dakika
      izledi); ölçek şoku — ayağının altında zemin değil gezegen —
      filmin ADINI söyleyen görüntüdür.
   ⑤ Serbest cıvatanın düz çizgisi 10 s'de gerçek bir 0g hareketi
      verir; KAPAK A'nın gergin ipi hareketsizdir.

⚠️ SAHİP KAPAK A İSTERSE: tek bir şey yapılır — §3'e yazılı bir
   sapma eklenir (gerekçe: kart filmin YAYINDAKİ küçük resmiyle aynı
   olsun diye). Prompt o zaman `KAPAK.md` §KAPAK A'dan alınır ve
   halat 10 s boyunca GERGİN kalır — gevşemesi fedanın işaretidir.
```

---

# 2. 🔤 METİN — PROMPTUN İÇİNDE, DÖRT ÖGE

```
✅ SAHİP KARARI: harfleri MODEL basar. İki prompt da metni birebir,
   tırnak içinde, büyük harfle ve konumuyla taşır.

İZİN VERİLEN DÖRT ÖGE — kadrajın SOL YARISI, siyah uzayın üstünde:
   ① Λ  logo işareti — kalın yukarı şevron, ince bir dairenin içinde
        ⭐ EN İYİ YOL: logo dosyası REFERANS GÖRSEL olarak eklenir.
           Emsal `apexaic/APEXAIC_INTRO_PROMPT.md` tam bunu yapıyor
           ("logo dosyası REFERANS GÖRSEL olarak eklenir") ve prompt
           o hâlde "reproduce the mark from the attached reference
           image exactly" der. Referanssız da çalışır — Λ tarif edildi.
   ② APEX AI CINEMA     küçük, harf araları geniş   (KANAL_KIMLIGI §1:
                        GÖRÜNEN AD "Apex AI Cinema")
   ③ FULL FILM NOW      büyük
   ④ ON YOUTUBE         büyük
   ⛔ BEŞİNCİ BİR YAZI BULGUDUR: alt yazı, filigran, web adresi,
      @handle, rakam, giysiye/panele yazı — hepsi RET (§7 RET ⑤).

⚠️ CTA NEDEN İKİ SATIR: "FULL FILM NOW ON YOUTUBE" tek satır 24
   karakterdir; görüntü modelleri uzun tek satırda harf düşürüyor.
   İki kısa satır aynı cümleyi söyler ve çok daha güvenilir çıkar.

⚠️ FİLM ADI KARTTA YOK — sebebi açık karar: kapaktaki İSİM hâlâ
   seçilmedi (KAPAK §0: YERÇEKİMİ / IT HOLDS ONE / NINETY MINUTES /
   HAND OVER HAND). Karar düşerse ③'ün ÜSTÜNE tek satır eklenir ve
   iki promptun TEXT bloğu beş ögeye çıkar. ⛔ "YERÇEKİMİ" seçilirse
   Ç ve İ modelde kırılır — o ad kartta post katmanıyla konur (§5).

🔴 BİLİNEN RİSK — YOK SAYILMADI, ÖLÇÜLDÜ [ADAY-7 · GOZLEM_DEFTERI]:
   bu filmin makaralarında model prompt İSTEMEDEN altyazı bastı —
   F5 2 · F6 3 · F7 7, yedisi de uydurma. Yani bu araç kadraja
   ÇAĞRILMADAN yazı koyabiliyor; çağrıldığında da yanlış yazabilir.
   → Bu yüzden §7'nin kabul kapısı artık "harf var mı" değil,
     "HARFLER DOĞRU MU" diye sorar: dört öge harfi harfine okunacak.
   → Model üç denemede doğru yazamazsa PLAN B hazır: aynı kare
     metinsiz üretilir, dört öge post'ta konur — ölçüleri §5'te.

⭐ BEDELSİZ ÖNLEM: video promptunda `Audio:` PARAGRAFI YOKTUR.
   ADAY-7'nin kapanışında elde kalan tek şüpheli değişken oydu ve
   kartın ses ihtiyacı sıfır (§6 — kuyruk sessiz).
   ⛔ Bu, F9/S107'ye kurulmuş deneyin YERİNE GEÇMEZ.
```

---

# 3. 🎬 KART — İLK KARE

`master 1:50.000-2:00.000 (yerleşim ①)` · 35mm · üst açı 25°, WS · lockoff · 10,0 s
**GEOMETRİ KAYNAĞI:** `KAPAK.md` §KAPAK B — aynı lens, aynı açı, aynı oranlar.

```
⚙️ Tek çekim, 0 kesme, 10,0 s. TEK hareket YOK — kamera tam kilitli.
İŞLEV: filmin kapak karesi NEFES ALIR; ayağının altında zemin değil
gezegen olduğu 10 saniye boyunca durur, yazı onun yanında sabit kalır.
⭐ KOMPOZİSYON KAPAK B'DEN BİR ADIM SAPTI: siyah uzay üçte birden
   SOL YARIYA çıkarıldı, çünkü yazı orada duruyor ve beyaz harf
   yalnız siyah zeminde 21:1 kontrast verir. Dünya'nın parlak kavisi
   62%'nin ALTINDA kalır; hiçbir harf gezegene değmez.
⭐ REFERANS GÖRSEL: logo dosyası imaj üretimine EKLENİR (§2 ①).
Kask çapası GÜNCEL kuşaktan (fragman §2④): biçim iddia edilmez [D146].
```

### 📸 IMAGE PROMPT

```
SCENE:
A cinematic end-card: one small astronaut alone above the lit curve of a
planet, with a studio logo and a call to action set in white type across
the black sky beside her.

TEXT — RENDER EXACTLY, AND THIS IS THE ONLY TEXT IN THE FRAME:
All type is left-aligned in the LEFT HALF of the frame, over black
space, in a heavy condensed sans-serif, solid near-white, edges sharp,
letter spacing even. Top to bottom:
FIRST, a logo mark — a bold upward chevron, a capital Greek lambda drawn
as two straight thick strokes meeting at a sharp apex, standing inside a
thin circle; if a reference logo image is attached, reproduce that mark
exactly instead.
SECOND, directly under the mark, one small widely letter-spaced line
reading APEX AI CINEMA.
THEN a clear empty gap, and below it two large stacked lines, the
biggest type in the frame, reading FULL FILM NOW on the upper line and
ON YOUTUBE on the lower line.
Every word is spelled exactly as written here, letter for letter, in
capitals, with no extra words, no punctuation, no duplicated line and no
misspelling.

ENVIRONMENT:
Hard vacuum in low orbit. Black space with hard pinpoint stars fills the
upper half of the frame. The sunlit curve of Earth fills the lower
left and the bottom, blue-white and streaked with cloud bands, its
horizon crossing the left edge at sixty-two percent of frame height. A
white lattice truss with ORANGE handrails runs in from the right edge to
a grey instrument cylinder with an open hinged panel. ONE loose bolt
drifts free beyond the panel edge, on a straight line. No spacecraft, no
station, no debris in frame.

SUBJECT:
Exactly one human figure, human count 1, small and alone in the RIGHT
THIRD of the frame at twenty-four percent of frame height. A 38-year-old
woman flight engineer in a warm off-white pressure suit with ORANGE
reinforcement stripes on shoulders, knees and glove cuffs, floating free,
feet off every surface, upright and calm. Her gloved
RIGHT hand holds the hinged cover half shut; her gloved LEFT hand grips
an orange handrail. An orange-and-white tether runs taut from her
hip to the rail behind her. Her head is inside a rigid white
helmet shell holding a clear front glass in a bright metal rim,
optically clear, zero tint, no mirror coating. Her back silhouette is
flat: off-white shell fabric, one spine seam, a low webbing belt, and no
pack, tank, hose or cable.

CAMERA:
Shot on a 35mm lens at f/8, from a fixed position 14 metres out and
above the platform, high-angle, camera pitched down 25 degrees. Deep
focus. Physically accurate perspective and true scale.

COMPOSITION: 16:9 horizontal. The truss and the astronaut hold the
screen-right third, her helmet on the upper-third line. The LEFT HALF
above Earth's horizon is empty black space and carries the type; no part
of any letter touches the planet, the truss or the figure.

LIGHTING: One hard white sun from the upper screen-right: a bright rim
along her helmet, her shoulder and the truss, lattice shadows absolute
black. Cool blue-white bounce from Earth below separates her pale suit
from the black space above. The type is flat and even,
lit by nothing, with no glow and no shadow.

PHYSICS: Zero gravity. The tether is straight and taut. Nothing hangs,
nothing settles, nothing falls. The free bolt sits on one straight line,
no arc and no trail.

NEGATIVE: Exactly one human figure, human count 1 — no second person, no
reflected person, no duplicate. Stripes stay ORANGE. Both glove cuffs
are bare: no ring, no band, no bracelet. No tears, no sweat, no liquid,
no fog inside the glass. 0% bloom, no glow filter, no lens flare, no
light rays, no haze. No fire, no smoke, no sparks. Apart from the logo mark, APEX AI CINEMA, FULL FILM
NOW and ON YOUTUBE, there is no other writing anywhere in the frame: no
subtitles, no caption, no watermark, no web address, no handle, no
numerals, and nothing written on the suit, the truss, the panel or any
surface. Photorealistic photography, 35mm film grain.

OUTPUT: 16:9, 4K, sharp legible type, no watermark.
```

---

# 4. 🎥 KART — HAREKET

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

> Start frame: yukarıdaki onaylanmış imaj. ⛔ `Audio:` paragrafı BİLEREK
> yok (§2). ⭐ Promptun İLK bloğu TEXT LOCK'tur, çünkü yazı kadrajın
> İÇİNDEDİR: kamera kayarsa harfler de kayar ve model onları her karede
> YENİDEN yazmak zorunda kalır — harf bozulmasının bir numaralı sebebi
> budur. Kamera 10 s boyunca kilitli; hareket kadrajın içinde.

```
Maintain the framing, the figure, the lighting and ALL THE TYPE exactly
as in the first frame.

TEXT LOCK — the type never changes. The logo mark, the small line
APEX AI CINEMA and the two large stacked lines FULL FILM NOW and
ON YOUTUBE stay in the left half of the frame at the same position, the
same size and the same spelling for all ten seconds. The letters never
drift, fade, flicker, warp, re-form, duplicate or turn into other words,
and no new writing appears anywhere in the frame.

MOTION — 10 seconds, 35mm, wide shot, fixed lockoff 14 metres out and
above the platform, high-angle, camera pitched down 25 degrees, no cuts,
no camera movement, no zoom:

SETUP: a white lattice truss with ORANGE handrails runs in from the
screen-right edge to a grey cylinder with an open hinged panel. Exactly one human figure, human count 1: a 38-year-old woman
flight engineer in a warm off-white pressure suit with ORANGE stripes,
at twenty-four percent of frame height in the screen-right third, feet
off every surface, her gloved right hand on the half-shut cover, her
gloved left hand on the rail, an orange-and-white tether taut from her
hip to the rail. Her back stays flat: no pack, tank, hose or cable. Earth's lit curve
fills the lower left and the bottom; the upper left stays black space.

0s — Nothing is settled: her body drifts a few centimetres against the
rail and keeps drifting. One loose bolt is already crossing frame on a
dead straight line at one constant speed.
2s — The bolt holds that line and speed, no arc and no trail, and
leaves frame at the screen-left, passing behind the type.
4s — Her right hand pushes the hinged cover the last of the way and it
seats flat. Nothing else in the frame moves.
6s — The blue-white arc of Earth reflected in her front glass
slides slowly toward the screen-left and keeps sliding — the only proof
that anything is turning.
8s — She lifts her head and looks out past the rail at the planet. One slow travelling wave runs along the taut tether and dies.
10s — Last frame: she is still holding, head up, the planet under her,
still drifting, the type unchanged. No cut.

Zero gravity: nothing hangs, nothing falls, nothing settles.
The tether never goes slack. No second person enters, no reflected
person, no duplicate. Both glove cuffs stay bare. Single unbroken take,
no cuts, no shake. 0% bloom, no glow filter, no lens flare,
no light rays, no haze, no smoke. Apart from the four locked elements
there is no other writing anywhere in the frame: no
subtitles, no caption, no watermark, no numerals. Photorealistic, 35mm
film grain.
```

---

# 5. ✍️ PLAN B — TİPOGRAFİ KATMANI (post)

> ⚠️ **BU BÖLÜM YEDEKTİR.** Ana yol §2'dir: harfleri model basar.
> Bu katman YALNIZ iki durumda açılır — ① model üç denemede dört ögeyi
> doğru yazamazsa, ② film adı kartta "YERÇEKİMİ" olarak istenirse
> (Ç ve İ modelde kırılır). O zaman kare METİNSİZ üretilir (iki
> promptun TEXT ve NEGATIVE blokları "no readable text ... anywhere in
> the frame" ile değiştirilir) ve yazı Photoshop / After Effects /
> DaVinci Resolve'da aşağıdaki ölçülerle konur.

## 5.1 ⭐ PUNTO DEĞİL PİKSEL — sayı testten geri hesaplandı

`KAPAK.md` §7.1 aynı işi 1280×720 **durağan** kapak için yapmıştı ve
zorunlu testi 120 px posta puluydu. **Video için test farklıdır:**

```
ZORUNLU TEST: 360 px genişlik — telefonda, en düşük kalitede, akışta.
  1920 → 360   ölçek = 0,1875
  okunabilirlik için versal yüksekliği ≥ 7 px  →  7 ÷ 0,1875 = 37,3 px
  yani 1920 tuvalde MUTLAK ALT SINIR versal 38 px.

TUVAL: 1920×1080. ⚠️ Çıktı 4K ise (promptlar 4K yazıyor) TÜM SAYILAR
  ×2 alınır — 3840×2160'ta versal 240/112 px, kenar boşluğu 192 px.
```

## 5.2 DÖRT ÖGE — ölçü ve genişlik

```
Λ İŞARETİ        yükseklik 72 px · çevresindeki ince daire çapı 96 px

APEX AI CINEMA   versal 40 px  →  360 px'te 7,5 px  ✅ (alt sınır 38 px)
  font 40 ÷ 0,73 ≈ 55 px · tracking +160/1000 em (geniş) ≈ +8,8 px/harf
  ilerleme 0,45 em ≈ 24,8 + 8,8 = 33,6 px/harf
    "APEX AI CINEMA"  14 karakter  →  ~470 px  ✅

CTA — İKİ SATIR  versal 120 px  →  360 px'te 22,5 px  ✅✅ baskın
  Bebas Neue versal ≈ 0,73 em  →  font 120 ÷ 0,73 ≈ 164 px
  tracking +40/1000 em ≈ +6,6 · ilerleme 0,45 em ≈ 73,8 + 6,6 = 80,4
    "FULL FILM NOW"   13 karakter  →  ~1045 px  ✅
    "ON YOUTUBE"      10 karakter  →  ~804 px   ✅
  kullanılabilir genişlik 1920 − 96 − 96 = 1728 px

  ⛔ TEK SATIRA ALINMAZ: "FULL FILM NOW ON YOUTUBE" 24 karakter ≈
     1930 px — 1728'i AŞAR. Tek satır ne bu tuvale sığıyor ne de
     modelin harf doğruluğuna uygun (§2). İki satır zorunlu.
  ↔ Alternatif satır: "WATCH THE FULL FILM NOW" → "WATCH THE" +
     "FULL FILM NOW" olarak aynı bloğa girer (§1②).

FİLM ADI (karar düşerse — KAPAK §0 hâlâ açık)
  CTA'nın ÜSTÜNE tek satır eklenir ve CTA versali 120 → 96 px'e iner
  (blok Dünya'nın ufkuna, y = 670 px'e değmesin diye). Dört adayın
  dördü de 96 px'te tek satır sığar; aritmetik yukarıdaki formülle
  aynen koşulur. ⛔ "YERÇEKİMİ" seçilirse bu ad MODELE YAZDIRILMAZ —
  Ç ve İ kırılır, o satır post'ta konur.
```

## 5.3 KONUM · RENK · KENAR

```
KONUM (1920×1080, sol-üst orijin · hepsi SOL yarıda, siyah uzayda)
  Λ İŞARETİ        x = 96   y = 96  – 192
  APEX AI CINEMA   x = 96   versal üstü y = 216   alt y = 256
  (boşluk)
  FULL FILM NOW    x = 96   versal üstü y = 360   alt y = 480
  ON YOUTUBE       x = 96   versal üstü y = 504   alt y = 624

  ✅ Dünya'nın ufku %62 = y 670 px. Blok 624'te biter → hiçbir harf
     gezegene DEĞMEZ; hepsi siyah uzayın üstünde, kontrast ≈ 21:1.
  ⛔ YASAK ŞERİT   y > 972  — oynatıcı ilerleme çubuğu + kontroller
  ⛔ YASAK BÖLGE   x > 1280 — YALNIZ bitiş ekranı öğesi kullanılacaksa
  ✅ ÇAKIŞMA YOK: özne ekran-SAĞ üçte birde, yazı SOL yarıda.

⚠️ 4K ÇIKTIDA TÜM SAYILAR ×2 — 3840×2160'ta versal 240/80 px,
   kenar boşluğu 192 px, ufuk y = 1340 px.

RENK VE KENAR  (KAPAK §7.3'ün 1280 ölçüleri 1,5× ile taşındı)
  Harf        yakın beyaz #E8F7FF   (KANAL_KIMLIGI §5.3 wordmark rengi)
  Dış çizgi   4 px saf siyah #000000, %100 opak
  Gölge       12 px siyah, %60 opak, 0° kayma (yönsüz halka gölge)
  Kontrast    beyaz üstüne siyah uzay ≈ 21:1  →  WCAG 4,5:1 ✅✅
  ⛔ TURUNCU HARF YASAK — turuncu bu filmde İNSANIN rengidir
     (klon kapısının ayırt edici işareti, REFERANS_PAKETI RC p3).
  ⛔ Glow / bloom / parlama YOK — kontur ve gölge dışında hiçbir efekt
     (LOGO_STING kuralı da aynı sınırı koyuyor: glow ≤ 12 px).

ZAMANLAMA (kart içi, 10,000 s)
  0,0 – 0,6 s   yazı yok — kare tek başına okunur
  0,6 – 1,0 s   Λ + APEX AI CINEMA 0,4 s'de açılır, sona kadar durur
  3,0 – 3,4 s   CTA iki satırı 0,4 s'de açılır, sona kadar durur
  → CTA ekranda 6,6 s ✅ (okuma + karar için fazlasıyla yeterli)
  ⛔ Kayma yok · ölçek yok · parlama yok · harf harf yazılma yok.
```

---

# 6. 🔊 SES — kart SESSİZDİR

```
Fragmanın müzik penceresi 0:10.000–1:42.000'dir; button ve KUYRUK
SESSİZ (§11 C · §1 "button + kuyruk sessiz"). Kart o kuyruğun içindedir.

KART SESİ: yalnız kabin/telsiz cızırtısı devam eder — müzik 0, replik 0.
  → §11 K3 kapısı (102-110 s, mean_volume ≤ −40 dB) DEĞİŞMEZ ✅
  → Sert frenden sonra gelen sessizlik TASARIMDIR, kusur değil.

⛔ Karta müzik/stinger/whoosh EKLENMEZ: eklenirse §11'in müzik penceresi
   sayısı ve K3 komutunun beklentisi aynı anda değişir [kural ①].
```

---

# 7. 🚪 KABUL / RET — kart teslim edilmeden önce

```
KABUL
  ① 360 px genişliğe küçült: APEX AI CINEMA ve iki CTA satırı okunuyor.
  ② Kamera 10 s boyunca 0 piksel oynadı — kaydırma, zoom, sarsıntı yok.
  ③ Serbest cıvata DÜZ çizgide, SABİT hızda geçti; kavis yok, iz yok,
     yavaşlama yok (0g kanıtı).
  ④ Halat 10 s boyunca GERGİN kaldı — hiç sarkmadı, hiç kıvrılmadı.
  ⑤ Kadın hiçbir yüzeye oturmadı; sürüklenme SON KAREDE de sürüyor
     ("hiçbir şey yerleşmiyor" — filmin kendi estetiği).
  ⑥ ⭐ DÖRT ÖGE HARFİ HARFİNE DOĞRU — 10 s'lik klip kare kare taranır:
        ffmpeg -i kart.mp4 -vf fps=5 -q:v 2 kare_%03d.jpg
        → 50 karenin 50'sinde de birebir şunlar okunacak:
             Λ   ·   APEX AI CINEMA   ·   FULL FILM NOW   ·   ON YOUTUBE
        ⛔ Tek harf eksik/fazla/yanlışsa, ya da bir karede değişiyorsa
           (titreme · yeniden şekillenme) → RET ⑤.
  ⑦ BEŞİNCİ YAZI YOK: altyazı, filigran, web adresi, @handle, rakam,
     giysi/panel üstünde yazı — hiçbiri yok.
  ⑧ Harfler siyah uzayın üstünde; hiçbiri Dünya'ya, kafese ya da
     figüre değmiyor (kontrast kaybı = 360 px'te okunmaz).
  ⑨ İki eldiven manşeti de çıplak: halka 0 kare, saat 0 kare [F7 K2 —
     iki nesne aynı bileğe yazılırsa model onları BİRLEŞTİRİYOR].

RET
  ① Kamera kaydıysa / zoom yaptıysa / titrediyse.
  ② Cıvata kavis çizdiyse veya arkasında iz bıraktıysa — yerçekimi sızdı.
  ③ Halat gevşediyse: o görüntü fedanın işaretidir ve §3 spoiler
     kapısını düşürür. SAYFA ATILIR.
  ④ İkinci bir insan, camda yansıyan insan ya da ikinci figür çıktıysa.
  ⑤ Harf bozuksa / eksikse / fazladan yazı varsa — YENİDEN ÜRETİLİR.
     ⛔ Bozuk harfin ÜSTÜNE tipografi yazılarak kurtarılmaz.
     ⛔ ÜÇ deneme sınırı: üçünde de tutmazsa §5 PLAN B'ye geçilir,
        dördüncü denemeye harcanmaz.
  ⑥ Vakumda pus, ışık hüzmesi, lens flare, halo varsa.
  ⑦ Bilekte halka ya da saat çıktıysa.
  ⑧ İmaj ile videonun ilk karesi arasında kadraj/ışık kayması varsa.

YABANCI GÖZ  Filmi bilmeyen birine 10 s göster, tek soru:
  "Bu kişi neyin üstünde duruyor?" → "Hiçbir şeyin / boşlukta" demeli.
  "Bir platformun üstünde" derse ayaklar yüzeye çok yakın kalmış.

SONUÇ  ☐ GEÇTİ   ☐ YENİDEN ÜRET      seed: __________
```

---

# 8. 📋 KURGU KAPISI — fragman dosyasında değişecek ÜÇ SATIR

> Yerleşim ① seçilirse. **Üçü birlikte değişir** [kural ①]; biri
> değişip öbürü kalırsa fragman kendi kendisiyle çelişir.

```
① §1 MASTER ÇİZELGE
   ESKİ  │ BLOK Z · APEXAIC KAPANIŞ      1:50.000 – 2:00.000    10.000 s │
         │          grafik · Veo değil · sabitlenmiş yorumda film linki  │
   YENİ  │ BLOK Z · HAREKETLİ KAPAK      1:50.000 – 2:00.000    10.000 s │
         │          İM2V · HAREKETLI_KAPAK_10S.md · yazı kadrajın içinde│

② §2 SAPMA ③ (EKRAN METNİ)
   ESKİ  "Marka grafiği YALNIZ Blok A ve Blok Z'de yaşar (0:00-0:10 ·
          1:50-2:00), FRAGMAN_PRO_YATAY emsalinin açtığı istisna."
   YENİ  "Ekran metni YALNIZ Blok A (APEXAIC marka grafiği) ve Blok Z'de
          (hareketli kapak: Λ + APEX AI CINEMA + CTA, promptta) yaşar."

③ §11 C — METİN KİLİDİ
   ESKİ  "METİN: gövdede (0:10-1:50) okunur metin 0,0 s; marka grafiği
          yalnız 0:00-0:10 ve 1:50-2:00 (bilinçli, sapma ③)."
   YENİ  "METİN: gövdede (0:10-1:50) okunur metin 0,0 s; ekran metni
          yalnız 0:00-0:10 (marka) ve 1:50-2:00 (Λ + APEX AI CINEMA +
          FULL FILM NOW / ON YOUTUBE) (bilinçli, sapma ③)."

⚠️ AYRICA — §10 PAKETLEME açıklaması:
   "Full film coming to this channel." → kart kullanılan sürümde bu
   cümle YALAN olur. §1②'nin (a)/(b) kararına göre ya "now on this
   channel" olur ya da kartsız sürüm yayınlanır.

⛔ BU DOSYA O ÜÇ SATIRI DEĞİŞTİRMEDİ. Değişiklik fragman dosyasının
   sahibinindir ve yerleşim kararı verilmeden yapılmaz.
```

---

# 9. ⛔ BU DOSYADA OLMAYANLAR — dürüst kayıt

| Yapılmayan | Neden |
|---|---|
| Dikey (9:16) kart | 16:9'un kırpımı sol üçte ikiyi ve metin alanını öldürür — dikey sürüm KENDİ imajını ister. Ayrı iş; fragmanın "⬜ dikey kesit" satırıyla birlikte açılır. |
| KAPAK A sürümünün promptu | §1③: fragman §3 spoiler kapısı yasaklıyor. Sahip sapmayı yazılı isterse prompt `KAPAK.md` §KAPAK A'dan türetilir. |
| Fragman dosyasının düzenlenmesi | §8'de üç satır hazır; yerleşim kararı sahibindir [kural ①]. |
| Başlık/açıklama metni | `PAKETLEME §6`nın işi; kart yalnız kareyi ve üstündeki iki satırı tanımlar. |
| Seed numarası | İmaj henüz üretilmedi. Üretilince §7'nin SONUÇ satırına yazılır. |
| Müzik / stinger | §6: kuyruk sessizdir ve sessizlik §11 K3'ün ölçtüğü sayıdır. |
| A/B testi | Depoda A/B altyapısı yok (`KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU §7`, 21.08.2026). |

---

> **Bu dosya ne zaman güncellenir**
> □ yerleşim kararı (① / ②) verilirse → §1 ve §8 sonuçla kapanır
> □ kapaktaki İSİM kararı düşerse (KAPAK §0) → §5.2 tek satır güncellenir
> □ imaj üretilirse → §7 SONUÇ + seed
> □ klip üretilirse → §7 ⑥ tarama sonucu; harf çıkarsa `GOZLEM_DEFTERI`
>   ADAY-7 kaydına **yeni vaka** olarak işlenir (araç şüphesi güçlenir)
> □ kart kurguya girerse → fragman §11 SPEC ile VIDEO_QA MOD D
