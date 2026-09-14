# 🖼️ THE KEPT LIGHT — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` §1 — kapak ANI senaryoda
seçildi, üretimden sonra aranmadı.

```
KAPAK ANI:      S0 · 0:04
                gerekçe: filmin TEK KARE testinin karesidir [ONERME §4① ·
                D157]. Kapağın vaat ettiği şey, filmin ilk dört saniyesinde
                ekranda olan şeyin AYNISIDIR — vaat-teyit penceresi
                (ilk 10 saniye) hiç açık kalmaz [PAKETLEME §3].
                ⛔ "en güzel sahne" gerekçe DEĞİLDİR. Tek sınav 120 px.
KAYNAK BLOK:    0:00-0:10 bandı ✅ (PAKETLEME §1 sayısal kilidi)
KOMPOZİSYON:    üçte bir kuralı — açık eldiven sol-ÜST üçte bir, kelepçe
                sağ-ALT üçte bir çizgisi, siyah ağız alt yarı.
                ⛔ Kadraj ORTASI kullanılmadı.
KONTRAST:       kum beyazı kask + soluk çelik kelepçe ↔ MUTLAK SİYAH ağız.
                Ton eşitliği yok; siluet arka plandan tamamen kopuk.
ODAK:           açık parmaklarla kelepçe arasındaki BOŞLUK.
ÜÇ ODAKTAN HANGİSİ [PAKETLEME §2]: ② YÜKSEK KONTRASTLI SİLÜET.
                ⛔ ① vizör yansıması KULLANILMADI — bu filmde vizör optik
                  berraktır ve yansıması SIFIRDIR [D79]; o odağı kullanmak
                  kilidi delerdi.
                ⛔ ③ fraktal ölçek KULLANILMADI — kapak yakın plandır;
                  ölçek kontrastı filmin içinde S10'da ödenir.
BAŞLIKLA UYUM:  Başlık "THE KEPT LIGHT" bir IŞIĞA bakmayı söylüyor; kapak
                bir ışık göstermiyor, ışığın DÜŞMEDİĞİ bir yer gösteriyor.
                ⛔ Kapak başlığın söylediğini TEKRAR ETMİYOR (ret şartı
                  atlatıldı): başlık "tutulan ışık" der, kapak "bırakılan
                  ve gitmeyen şey" gösterir. Boşluk merak üretir.
                → `THE_KEPT_LIGHT_YAYIN_PAKETI.md` CROSS-PLATFORM NOTES
PLAN B KAPAK:   S10 · 1:41 — kayanın altındaki üs, tek aydınlık ağız, altında
                sütun. Yayından ÖNCE hazır [Kart Y · §7.2]. Plan B'nin işi
                farklı bir izleyiciyi durdurmaktır: A kapağı YAKIN ve
                tekinsiz, B kapağı GENİŞ ve kozmiktir.
ÖLÇÜ:          yatay 1280×720 (+ 1920×1080 master)
SPOILER BÜTÇESİ [D114 · §5]: dört yüzeyin toplamı — kapak novumun SONUCUNU
                gösterir (bırakılan şey gitmiyor), SEBEBİNİ göstermez;
                başlık ışığı adlandırır ama nerede olduğunu söylemez;
                açıklama ilk cümlede kuralı söylemez; etiketler nötr.
                Toplam ifşa: 1 yüzey / 4. ⛔ Modülün, hattın ve eski lambanın
                hiçbiri kapakta YOKTUR.
⛔ KESİLEMEZ:   S0 kurgu kapısının KESİLEMEZ listesindedir — kapağı taşıyan
                sahne düşerse elde tıklamayı karşılamayan bir kapak kalır
                [D62 / D100 örüntüsünün paketleme tarafı].
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 IMAGE PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic still image, 16:9 widescreen, 4K, poster crop.
Exactly one human figure.

SUBJECT: an open square hatch in the floor of a small vacuum work bay,
photographed from directly above it. In the upper-left third of the frame,
a heavy segmented glove is open palm-down, fingers spread, its cuff running
into the sleeve as one piece at the wrist. On the lower-right third line,
a hand-length matte grey clamp hangs in the black mouth of the hatch about
a hand's width under the fingers — freshly cut, still, and not moving away.
Below it, going down into the dark and getting smaller and fainter, are
four more separate solid shapes, one under the other. Along the right edge
of the frame is the top of a hip with a hooded hand-lamp the size of a fist
riding dark in a clip. At the top edge, the shoulder and helmet of a man of
fifty-four, heavy-shouldered, deep brown skin, in a matte dark olive
surface suit with faded sand-white shoulder bands; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable through it as he looks
down past his own glove. The back of the suit is one continuous smooth
panel from collar to hip, carrying nothing.

COMPOSITION: rule of thirds. The open glove holds the upper-left third,
the hanging clamp the lower-right third line, the black hatch mouth the
lower half. Nothing story-critical sits in the outer eighth of any edge or
in the lower-right corner tile — those bands are covered by platform UI.
The face reads at the top edge but the picture does not depend on it: at
120 px the readable shape is the bright open hand above a bright dot that
has not fallen away.

LIGHTING: two hooded work lamps out of frame above throw hard cool neutral
white onto the glove, the lip and the clamp; the metal walls of the bay
throw no second light and every shadow is absolutely black with a razor
edge. Below the lip there is almost no light at all — the deeper shapes are
lit only by a weak source far below and fall off to points. A low rim light
separates the shoulder and helmet from the background; the silhouette never
merges with what is behind it.

NEGATIVE: Exactly one human figure — no second person, no duplicates, no
clones, no reflected or doubled figure. 0% bloom, no glow filter, no soft
focus, no dreamy haze, no glow halo around anything. Photorealistic skin
with pores, sweat and fatigue retained — no airbrushing, no plastic or waxy
texture, no smoothed skin. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection of the environment. No back-mounted
unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in
frame: none above the collar seal, none at the wrist between glove and
sleeve, none at the ankle above the boot cuff. All hand-surface contacts
keep a clear structural boundary — no merging, no phasing, no extra
fingers. The hanging shapes are separate solid objects with hard edges,
each one countable — not sparks, not embers, not particles, not a dust
column. No dust, no haze. No smoke, no flame, no spark, no rust. No
readable text, letters, digits, numbers or symbols anywhere in the frame —
not on the suit, the glove, the clamp, the hatch frame or the lamp; no
scale marks, no graduation ticks, no engraved or painted characters of any
kind. No national flag, no agency logo, no mission patch. No subtitles, no
captions, no title card, no watermark, no HUD overlay, no logo lockup. No
lens flare, no anamorphic streak. Metal static and solid — no melting, no
warping. No tilt-shift look, no miniature or toy-model read. No Unreal
Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with
35mm film grain.

Output: 1280×720 (master 1920×1080), no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
  "AÇIK BİR EL, VE ALTINDA DÜŞMEYİ BİTİRMEMİŞ PARLAK BİR ŞEY."

Somut ölçüt: 120 px'e indirildiğinde kadrajda İKİ parlak leke ayrı ayrı
sayılabilmeli (el · kelepçe) ve aralarındaki karanlık boşluk kapanmamalı.
İkisi tek lekeye birleşiyorsa kapak düşer.

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — test manuel yapılır.)

⬜ 120 px testi koşulmadı — kapak henüz üretilmedi.
```

## 🔁 ÇİFT KARTIYLA BAĞ

```
Kapak karesi S0'ın karesidir; filmin SON karesi (S24 · 4:07) kompozisyon
olarak onun AYNISIDIR ve tek fark avuçtan çıkan şeydir
[ACILIS_KAPANIS §5 · konum kilidi]. Yani kapak, filmi izleyen için ikinci
kez ve başka anlamda geri gelir. Plan B kapağı bu bağı taşımaz ve
taşımamalıdır — ayrı bir izleyiciyi durdurmak için vardır.
```
