# 🧷 THE HEALING GROUND — REFERANS PAKETİ

**Kaynak:** `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` §4 (I2V çapalama) ·
`SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1 (kelimesi kelimesine) ·
`KILAVUZ_REHBERI` §2.0 (paket kuralı) · emsal: `THE_BLIND_BERTH` 5 panel

> **Neden bu filmde var:** iskelet kuralı "iki insandan/araçtan fazlası varsa
> ZORUNLU" der ve bu filmde tek insan, sıfır araç vardır. Paket yine de
> yazıldı çünkü zorunluluğu başka bir kılavuz getiriyor:
> **UZAYLI_VARLIK §4** — "varlığın ÖN/YAN/ARKA üç görünümü imaj aşamasında
> üretilir ve video I2V ile koşulur; modelin görmediği yüzeyi uydurması
> (oklüzyon halüsinasyonu: gizli bölgeye İNSAN uzvu yamama) en sık
> uzuv-kayması sebebidir."
>
> ⛔ **Referans kareler KURGUYA GİRMEZ.** Bunlar üretim aletidir, sahne değil.
> ⛔ **Panelli resim start frame olarak KULLANILMAZ** (panel çizgisi ve olası
> yazı videoya taşınır [D34/D45]); I2V için panel tek başına kırpılır.
> ⛔ Bu dosyadaki promptlar `📸 GÖRSEL PROMPT` başlığı TAŞIMAZ — dizi
> kapılarına (kurulum yayı · açı tipi · tema) girmemeleri için.

---

## 📦 PAKET İÇERİĞİ — 3 referans, 7 panel

| # | referans | panel | ne zaman üretilir |
|---|---|---|---|
| R1 | VARLIK | 3 panel: üstten · yandan · ALT YÜZ | ⭐ EN BAŞTA — S12 ve S13'ten önce |
| R2 | ÖLÇÜM DİSKİ | 2 panel: üstten · kenardan | S0'dan önce |
| R3 | GİYSİ | 2 panel: önden · arkadan | S0'dan önce (S6'nın sırt kadrajı buna bağlı) |

```
ÜRETİM SIRASI [D168 ile uyumlu]: R1 → R3 → R2 → DORUK (S12) → S11 → S13 → S0
⛔ R1 üretilmeden S12 üretilmez. Doruk sahnesi filmin tek tam-anatomi
  karesidir; çapasız üretilirse ② DEVAMLILIK ve ⑥ FİZİK aynı anda düşer.
```

---

## R1 — VARLIK (üç görünüm)

> ⛔ Bu üç panel AYRI AYRI üretilir, tek kadrajda üç görünüm istenmez:
> tek promptta üç görünüm istemek modelin üç FARKLI yaratık çizmesinin en
> hızlı yoludur. Aynı seed ile üç koşu, sonra elle seçim.

### R1-a · ÜSTTEN (dorsal)

```
Photorealistic macro still, 35mm film grain. A single biological specimen
lying on a pale frozen crust, photographed from straight above.

One flat oval form, as wide across as a man's shoulders and as thin as a
folded glove. A single continuous rim runs all the way around it, unbroken,
and the outer third of that rim bends down onto the floor like a resting
ray's wing. Three short sensory stalks stand along its leading edge, evenly
spaced. Its upper surface carries a crust of pale frost, fine and dry, the
same colour as the ground it lies on but rougher; under the frost the
surface is a translucent grey-white with faint concentric growth banding.
The LEFT side of the rim carries a healed pale notch, a shallow bite out of
the edge that has grown smooth.

There is no head, no face, no mouth, no visible eye and no limb of any kind
on this surface. The form is at rest and nothing about it is raised.

The floor is a fine pale mat the colour of dry bone, one continuous crust
with no seams and no rocks. Soft shadowless daylight from the whole sky
dome; the shadow under the rim is shallow, soft-edged, never black.

Style: a plain specimen plate — the frame holds the animal and the bare crust
around it and nothing else, the way a field photograph of a single organism
looks. The surface is dry throughout. Every edge keeps visible texture, 0%
bloom, no glow filter, photorealistic with 35mm film grain, and every surface
in frame is bare: unmarked, unlabelled and unmeasured.

Output: 16:9, 3840x2160, no text, no watermark.
```

### R1-b · YANDAN (profil, kenar hattı)

```
Photorealistic macro still, 35mm film grain. The same single specimen,
photographed from the side at ground level, the lens 0.15 metres above the
crust.

One flat oval form, as wide across as a man's shoulders and as thin as a
folded glove, lying on a pale frozen crust. From this height its whole
profile is one shallow curve: the centre stands about a thumb's height off
the ground and the single continuous rim thins to a clean edge and bends
down onto the floor all the way around. Three short sensory stalks stand
along the leading edge, evenly spaced, each no longer than a finger joint.
The upper surface carries a crust of pale dry frost; the edge itself is
translucent and the light passes a little way into it.

The LEFT side of the rim carries a healed pale notch. There is no head, no
face, no mouth, no visible eye and no limb.

The floor is a fine pale mat the colour of dry bone. Soft shadowless daylight
from the whole sky dome; the shadow under the edge is shallow and soft.

Style: a plain specimen plate — the frame holds the animal and the bare crust
around it and nothing else. The surface is dry throughout, every edge keeps
visible texture, 0% bloom, no glow filter, photorealistic with 35mm film
grain, and every surface in frame is bare, unmarked and unmeasured.

Output: 16:9, 3840x2160, no text, no watermark.
```

### R1-c · ALT YÜZ (ventral — YALNIZ S12 için)

```
Photorealistic macro still, 35mm film grain. The leading edge of the same
specimen, lifted clear of the ground and turned over, photographed from a
high angle seventy centimetres away.

The leading third of a single continuous rim is raised off a pale frozen
crust and rolled over, showing the underside: smooth, translucent, faintly
veined, a shade warmer than the frosted upper surface. On that pale
underside there is one pair of dark eyes, evenly spaced, round, wet-dark and
without whites — the eyes of a resting mammal, set into a surface that is not
a face. Nothing else is on the underside: no mouth, no jaw, no teeth, no
opening of any kind.

Three short sensory stalks stand along the leading edge, evenly spaced. The
LEFT side of the rim carries a healed pale notch.

The floor is a fine pale mat the colour of dry bone. Soft shadowless daylight
from the whole sky dome; the shadow under the raised edge is shallow and
soft-edged, never black.

Style: a plain specimen plate — the frame holds the raised edge and the bare
crust around it and nothing else. The two eyes sit alone on an otherwise
featureless surface, and that surface stays continuous and unbroken all the
way to the rim. Everything is dry, every edge keeps visible texture, 0%
bloom, no glow filter, photorealistic with 35mm film grain, and every surface
in frame is bare, unmarked and unmeasured.

Output: 16:9, 3840x2160, no text, no watermark.
```

```
⚠️ R1-c NİYET KAPISI: bu panel EMPATİ üretmek için var (UZAYLI §1). Göz
  memeli gözüdür, avcı gözü değil: yuvarlak, ıslak-koyu, dikey bebek YOK.
  Panelde tehdit imzası (diş · çene · açılma) 0 kare — filmde de 0 kare.
⚠️ ORBİT YASAĞI: bu üç panelin DIŞINDA varlığın başka bir yüzeyi hiç
  üretilmez. Arka görünüm YOK ve gerekmiyor — kamera onu hiç görmüyor.
```

---

## R2 — ÖLÇÜM DİSKİ (iki panel)

```
Photorealistic macro still, 35mm film grain. A single small object on a plain
neutral grey surface, photographed from straight above.

One disc of dark blued steel the width of a man's palm, flat, plain and
slightly domed at the centre, with one raised rim around its edge and a
shallow cross-groove pressed into the face. The metal is matte, unpolished,
darkened by heat treatment, with fine machining circles visible under the
finish and a small burr on one edge where it was cut. It is a working object,
not a decoration.

Style: a plain workshop plate — the frame holds the disc and the neutral grey
surface under it and nothing else. The only things on the metal are the
raised rim, the cross-groove and the machining circles; the face of the disc
is otherwise completely bare. Every surface in frame is unmarked and
unmeasured. 0% bloom, no glow filter, photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

```
İKİNCİ PANEL: aynı prompt, tek fark kamera satırı —
"photographed from the side at surface level, so the thickness of the disc
and the height of its raised rim are readable".
⚠️ Bu obje filmin NOVUM TAŞIYICISIDIR; iki panel de S0 üretilmeden önce
  hazır olmalı. Diskin kalınlığı S12'de örtünün "kenarına gelip durduğu"
  yüzeyi belirler — kalınlık kayarsa doruk karesi okunmaz.
```

---

## R3 — GİYSİ (iki panel)

```
Photorealistic full-length still, 35mm film grain, plain neutral grey
backdrop, even studio light.

Exactly one human character — no clones, no second person. A man in his
fifties, grey hair, deep lines at the outer eyes, standing straight and
facing the lens, sealed in a matte dark slate-grey pressure suit with
articulated knee and elbow panels. A bold ochre-yellow band is wrapped all
the way around the RIGHT forearm and all the way around the RIGHT thigh. The
helmet is a plain rounded shell with four small box-shaped lamps across the
brow, all four unlit; the visor is optically clear glass with zero tint, zero
mirror coating and zero reflection of the environment, and his face is fully
readable through it. A flat chest module sits at the centre of his chest with
a plain hinged cover and one recessed metal latch. A vent sits below his
RIGHT hip. Fixed wear that never moves: a thin pale scratch along the LEFT
forearm SLEEVE of the suit, a pale scuffed patch on the RIGHT knee panel, and
the lower edge of the ochre band on the right thigh rubbed dull. No bare skin
anywhere — none above the collar, none at the wrists between glove and
sleeve, none at the ankles between boot and leg; every seam is closed and
every seal ring is visible.

NEGATIVE: exactly one human character, no clones, no second person, no
reflection of anyone in the visor. No backpack, no tank, no hose, no cable
and no rear housing of any kind. No readable text, letters, digits, numbers
or symbols on the suit, no patch writing, no name tape, no flag, no agency
emblem, no rank marking. No indicator, no gauge, no dial, no screen and no
lit readout anywhere on the suit. 0% bloom, no glow filter, no soft focus.
No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm film grain.

Output: 16:9, 3840x2160, no text, no watermark.
```

```
İKİNCİ PANEL — ARKADAN (S6'nın kadrajı buna bağlı, D139):
aynı prompt, tek fark özne satırı —
"standing straight with his back to the lens. The back of the suit is one
continuous smooth panel from collar to hip, unbroken, carrying nothing — one
smooth surface with a single flat vertical seam down its centre and no
housing, no unit, no fitting, no strap and no seam pocket on it. His back
silhouette is flat."
⛔ Yokluk listesi ("no backpack") arkadan çekimde TUTMAZ; model boş sırtı
  DOLDURMAK zorundadır ve yasak ona ne KOYACAĞINI söylemez. Panelin işi
  ona ne koyacağını söylemektir [D139].
```

---

## ✅ PAKET KAPISI — üretim başlamadan önce

```
□ R1-a · R1-b · R1-c üretildi ve ÜÇÜNDE DE aynı çentik SOL kenarda mı
□ R1-c'de göz sayısı tam 2 mi, ağız/diş/çene 0 mı
□ R2'nin iki panelinde disk üstünde tek harf/rakam/işaret var mı → varsa
  yeniden üret [D138 · D45]
□ R3-arka panelinde sırt DÜMDÜZ mü, sırt ünitesi doğmuş mu
□ Paneller I2V'ye TEK BAŞINA kırpılarak mı veriliyor (panelli sayfa değil)
□ Seed kaydedildi mi (SAHNE_DEVAMLILIK §6.1) — hangi panel hangi seed
⛔ Bu altı madde işaretlenmeden S12 üretilmez.
```
