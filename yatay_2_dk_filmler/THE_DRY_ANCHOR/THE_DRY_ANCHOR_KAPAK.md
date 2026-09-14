# 🖼️ THE_DRY_ANCHOR — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S7 (ORTA NOKTA · 70-80 s)  ·  gerekçe: 120 PX'TE İKİ ŞEKİL
                Kolun dirseğe kadar zemine girmiş olması posta pulu boyutunda
                bile OKUNUR: beyaz uzuv + kırmızı-koru zemin + kolun bittiği
                yer. Filmin vaadi ("bu tozun tabanı yok") tek karede görünür.
                ⛔ "en güzel sahne" gerekçe değildir. Tek sınav 120 px'tir:
                  yüz 120 px'e inince gri lekedir, iki siluet okunur.
                ⚠️ SAPMA KAYDI [D74]: kılavuz §2 yüz odaklı kapakta yüzün
                  kadrajın ≥%60'ını kaplamasını ister. Bu kapak ŞEKİL odaklıdır
                  ve yüz ~%18'dir. Gerekçe: bu filmin merak boşluğu bir YÜZ
                  İFADESİ değil bir FİZİK İHLALİ; yüz odaklı varyant PLAN B
                  olarak yazıldı ve 48 saatlik tek değişkenli testte kapak
                  değişecekse o kullanılır.
BAŞLIKLA UYUM:  ✅ Başlık "This Dust Has No Bottom" · kapak dirseğe kadar
                gömülmüş bir kol gösteriyor — ikisi AYNI şeyi vaat ediyor,
                biri ötekini açıklamıyor (`THE_DRY_ANCHOR_YAYIN_PAKETI.md`
                → CROSS-PLATFORM NOTES).
PLAN B KAPAK:   ✅ S11 (DORUK · ⭐VİRAL) — yüz odaklı varyant: şeffaf pencere
                arkasında çenesi gevşemiş yüz + geri seken sürücü. Kart Y
                yayından ÖNCE hazır olmasını ister (§7.2).
ÖLÇÜ:           yatay 1280×720 (bu hat 16:9) · doygunluk son adımda %20 artar
GÜVENLİ ALAN:   sağ alt köşe (süre rozeti) BOŞ — kol da yüz de oraya düşmez
RENK (2-3):     kırmızı-koru zemin · beyaz giysi · tereyağı-solgun gök
                (+ tek vurgu: sağ koldaki yanık-turuncu bant)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.
> ⚠️ Kadraj S7'nin ANIdır, S7'nin KURULUMU değil: kapak için kamera yarım
> metre alçalır ve yaklaşır (35mm · 0,9 m · el −15°). Film karesi değildir.

```
Photorealistic cinematic still image, 16:9 widescreen, no text anywhere.

SUBJECT & ACTION: One figure in a white pressure suit kneels on a pale
red-ochre dust plain, left of centre, her right arm driven straight down into
the ground and swallowed to the elbow — the sleeve runs unbroken from the
shoulder into the dust and the sleeve seam bunches where the arm meets the
surface. Nothing of a tool is visible. Her helmet is turned three quarters to
camera: a hard white shell with a flat rectangular front window in a
brushed-metal frame, one small cyan lamp inside lighting the face from below,
the glass optically clear with zero tint and zero mirror coating so the face
reads through it. A single burnt-orange band runs down the outside of the
right arm. The back is flat and carries nothing.

ENVIRONMENT: the flat dust plain runs unbroken to the horizon under a
butter-pale sky; a low dark ridge fills the right half of the horizon line.
The right-hand third and the bottom-right corner stay empty ground — no
detail, no object, nothing the eye needs.

COMPOSITION: subject on the left third, eyes on the upper third line, the arm
entering the ground at the exact centre of frame. 35% of the frame is empty
plain and sky. Nothing story-critical in the bottom-right corner (platform
duration badge) or in the outer 8% of any edge.

CAMERA: 35mm lens, low, camera half a metre above the surface and about one
metre from the buried elbow, tilted slightly down, the far ridge held in the
top band.

LIGHTING: one low sun in the west at frame-left rims the white suit and
separates it from the ground; shadows are soft-edged and weak and the fill is
real — this softness is correct for this air, not a fault — and every shadow
runs left to right. The cyan helmet lamp is the only cool light in frame.

COLOUR: three colours only — red-ochre ground, white suit, butter-pale sky,
with the burnt-orange arm band as the single accent. High luminance contrast
between the white suit and the ground so the silhouette survives at postage
stamp size.

NEGATIVE: Exactly one human character — no duplicates, no clones, no second
person. 0% bloom, no glow filter, no soft focus — every surface keeps visible
texture. Photorealistic skin pores, sweat and fatigue retained — no
airbrushing, no plastic or waxy texture, no face morphing. No readable text,
no letters, no digits, no numerals and no symbols on any surface in frame: no
scale marks, no graduation ticks, no survey markers. No subtitles, no
captions, no title card, no watermark, no HUD overlay. The suit has NO
back-mounted unit: no backpack, no tank, no hose, no cable — the back
silhouette is flat. The visor is optically clear with zero tint and zero
mirror coating. No bare skin above the collar, no bare skin at the wrist, no
bare skin at the ankle. No tilt-shift or miniature look. No flag, no agency
logo, no mission patch. Nothing billows and nothing flaps. No water, no
liquid. Nothing is blown upward; no dust curtain. No second vehicle, no second
structure, no animals, no plants, no storm, no fire. Environment static and
stable — no melting terrain, no warping topology. No CGI look, no video game
aesthetic. Photorealistic with 35mm film grain.

Output: 1280×720, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
   BEYAZ BİR KOL ZEMİNE GİRİYOR VE ÇIKMIYOR.
   (beyaz uzuv · kırmızı zemin · kolun kaybolduğu nokta — üç şekil, tek okuma)

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)

⛔ Testi geçmenin İKİ bilinen yolu, sırayla denenir:
   ① kolu kadrajın tam merkezine al ve gövdeyi büyüt (kol/ekran eni ≥ %25)
   ② zemin doygunluğunu %20 artır — beyaz giysi ile zemin arasındaki
     parlaklık farkı okumayı taşıyan tek şeydir (renk değil, parlaklık)
```
