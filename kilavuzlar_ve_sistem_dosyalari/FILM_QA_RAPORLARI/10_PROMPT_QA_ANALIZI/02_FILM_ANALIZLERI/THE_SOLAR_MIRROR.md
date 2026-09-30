# 🧩 THE_SOLAR_MIRROR — prompt hata analizi

```
FORMAT      yatay 2 dk · 12 sahne · ⭐ IZGARA ÖLÇÜLDÜ (7 raporun künyesi: süre ÷ sahne = 10 s)
HAM RAPOR   12/12 geçerli · BULGU 25 → tekil 25
HÜKÜM       🅐 9 · 🅑 14 · 🅒 1 · 🅓 1      🅑/(🅐+🅑) = %61
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 12/12: sayı · parçacık · bloom · metin · filigran · kamera
  KISMİ: temas 1/12 · giysi 1/12 · efor 1/12 · g-ad 8/12
  ⛔ HİÇ YOK: SES · dış-ses · g-sayı
```

> ⭐ Bu film A2 grubundadır: `QA_SPEC`'inde `GRID:` satırı yok, ızgara **raporların
> kendi künyesinden ölçülerek** türetildi (7 rapor, süre ÷ sahne = 10 s).

---

## 🅑 SINIF 1 — VAKUM ADLANDIRILMAMIŞ · 4 🔴 · 2 🟠 ⭐ en ağır

| S | bulgu |
|:--:|---|
| S05 🔴 | *White gas vents and expands in a dense cloud as if within atmospheric pressure* |
| S06 🔴 | *Open atmospheric fire and combustion smoke burning along the truss in space vacuum* |
| S06 🔴 | *Billowing dark smoke clouds rolling upward in zero-atmosphere* |
| S06 🔴 | *Open flame/fire burning on structure in space vacuum* |
| S06 🟠 | *Atmospheric fire and thick smoke burn along metal truss in hard vacuum* |
| S00 🟠 | *Sparks from the welding arc float smoothly instead of spraying in straight ballistic trajectories* |

**Promptta ne yazıyordu:** parçacık cümlesi **12/12'de var** — ama ortamın **adı
yalnız 8/12'de**, **sayısı 0/12'de**. Motor "parçacıklar belirtilen yerçekimine
uyar" cümlesini okuyor, belirtilen bir şey bulamıyor ve ateşi Dünya'daki gibi
yakıyor. ⛔ **Vakumda açık alev yanmaz** — dört BLOCKER tek bir eksik cümleden.

**Hüküm 🅑 ×6.** Kılavuz §2'nin `PHYSICS:` satırı (§3.1 VAKUM) bu filmde yok.

## 🅑 SINIF 2 — JETON SIZINTISI · 3 🟠 ⭐⭐ SAHNE ETİKETİ KADRAJA BASILDI

| S | bulgu |
|:--:|---|
| S09 | *Emergent AI gibberish text (**"VI.DLIFE"**) stencilled on hatch structure* |
| S09 | *Decal text **"S04"** and "VI.DLIFE" warps across airlock frame movement* |
| S09 | *Warping text on airlock hull (**"S04"**)* |

⭐ **`S04` bir SAHNE ETİKETİDİR.** `PROMPT_HATA_ONLEME_KILAVUZU` §6 bu jetonu
(`S07` · `R3`) **varsayımsal örnek** olarak yazmıştı; burası onun **ölçülmüş
vakası**. Metin yasağı 12/12'de yazılı ve kurtarmadı.

Sınıf artık **dört filmde**: THE_PAYLOAD (`PHASE 1` · `EVA`) · THE_ROSE_COAT
(`rose`) · **THE_SOLAR_MIRROR (`S04`)** · THE_CRACKED_HELMET (`ORION`).

## 🅑 SINIF 3 — EFOR 1/12 · 6 (2 🔴)

S00 🔴 · S01 🔴 · S02 · S04 🔴 · S05 · S06 — *"glove joint stiffness, reduced fine
dexterity"* · *"body recoil, momentum transfer upon release"* · *"counter-push
leverage against hull"*. Efor cümlesi 12 sahnenin 1'inde.

## 🅑 SINIF 4 — TEMAS 1/12 · 1 🟠 · SINIF 5 — ÖLÇÜ · 1 🟠

S02 (raylara tutunma) · S11 ⑥ (*"structure frame openings exceed 3.5 m relative
to the astronaut"* — ölçü gövde boyu cinsinden değil [D138]).

---

## 🅐 MODEL SAPMASI · 9

**İnsan sayısı** S08 🔴 (*"Subject duplicate with identical facial features appears
opposite the primary subject"*) + S08 (*aynanın yansımasında ikinci figür, baş
dönüşü senkronsuz*) — `exactly N human` **12/12'de yazılı**.
**Parçacık/momentum** S01 ×2 (*alet momentum ve karşı dönme olmadan süzülüyor*) —
cümle 12/12'de. **Bloom** S00. **Mekân** S01 · S06 (*yok edilen ayna dizisi S7'de
sağlam*) · S11 (*arka plandaki figür yürümeden kayıyor*). **Kesme** S00 (*hard jump
cut*, kamera cümlesi 12/12'de).

## 🅒 BULGU DÜŞER · 1

S01 ⑦ (*"Origin and mechanism of the blue energy ring surrounding the lost tool"*)
— halka filmin **novumudur**, açıklanmaması tasarım kararıdır.

## 🎯 ÜÇ SATIR

```
1. VAKUMDA ATEŞ YANIYOR — dört 🔴. Parçacık cümlesi 12/12'de, ortam adı 8/12'de,
   ortam sayısı 0/12'de. "the stated gravity" yine stated edilmemiş.
2. SAHNE ETİKETİ "S04" GÖVDEYE BASILDI. Jeton sızıntısının dördüncü filmi ve
   kılavuz §6'nın varsayımsal örneğinin ölçülmüş kanıtı.
3. EFOR 1/12. Altı bulgu, ikisi 🔴, hepsi tek eksik cümleden.
```
