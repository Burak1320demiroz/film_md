# 🧩 THE_DRY_ANCHOR — prompt hata analizi

```
FORMAT      yatay 2 dk · 14 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   8/8 geçerli · BULGU 23 → tekil 23
HÜKÜM       🅐 17 · 🅑 6 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %26
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 14/14: SES · sayı · temas · giysi · parçacık · bloom · metin · g-ad · filigran · kamera
  KISMİ: efor 7/14
  ⛔ HİÇ YOK: dış-ses · g-sayı
  bulgulu sahnelerde eksik: dış-ses 0/8 · efor 4/8 · g-sayı 0/8
```

> ⭐ **Sekiz 🔴'nın altısı TEMAS.** Temas cümlesi 14/14'te yazılı. Bu film,
> "temas sınırı cümlesi yazmak yetiyor mu?" sorusunun **hayır** cevabıdır.

---

## 🅐 SINIF 1 — TEMAS FÜZYONU · 6 🔴 ⭐ kilit tam, sonuç sıfır

| S | bulgu |
|:--:|---|
| S04 🔴 | *Gloved fingers fuse and morph directly into the metal handle of the hammer during strokes* |
| S08 🔴 | *Right glove deforms and liquid-morphs into the sand surface while digging* |
| S09 🔴 | *Yellow tether strap clips cleanly through the solid metal lander leg* |
| S09 🔴 | *Geometry clipping — tether passing through solid lander leg* |
| S11 🔴 | *Left hand holding the ground pin melts into the metallic shaft* |
| S11 🔴 | *Multiple instances of mesh merging and finger-to-prop contact morphing* |

**Promptta ne yazıyordu:** `no merging, no phasing, clear boundary, no extra fingers`
— **14 sahnenin 14'ünde**. Cümle eksiksiz, sonuç altı BLOCKER.

**Hüküm 🅐 ×6.** ⭐ Karşılaştırmalı tablo artık dört filmden kuruldu:

```
temas cümlesi YOK   → FROST_LINE 5 🔴 · MARS 3 🟠 · RESONANT 0 (temas kadrajda az)
temas cümlesi VAR   → DRY_ANCHOR 6 🔴 · BENI_HATIRLAMA 2 🔴 · STILL_SWARM 2
```

**Cümle yazmak temas füzyonunu durdurmuyor.** Ders siparişi: el-nesne teması
**kadraj kararıyla** çözülür — temas anı ya perdelenir ya da eldiven ile nesne
arasına görünür bir ara katman (halka · sap kılıfı) konur. Prompt cümlesi tek
başına yetmiyor ve bu artık ölçülmüş bir gerçektir.

## 🅐 SINIF 2 — PARÇACIK VE NEDENSİZ OLUŞUM · 4 (2 🔴)

S03 🔴 (*"Footprints are pre-rendered into the soil **before** the boots land"*) ·
S07 🔴 (*"Ring of dark dust erupts out of air around the lander leg without physical
source"*) · S01 ×2 (*iniş aracı toz bulutu aniden donuyor / kütlesiz kayboluyor*).
Parçacık cümlesi 14/14.

## 🅐 SINIF 3 — DOKU YÜZMESİ · 3 · 🅐-4 · CİLT · 1 · 🅐-5 · ADIM · 1 · 🅐-6 · GEOMETRİ · 2

S03 · S06 (*silt yüzeyi "nefes alıyor"*) · S07 (*iniş aracı bacak geometrisi geniş
ve yakın kadrajda değişiyor*) · S03 (*airbrushed plastic skin*) · S04 (*ayak kayması*) ·
S11 🔴 (*çekiç başı darbe ortasında çift keskiye dönüşüyor*).

---

## 🅑 PROMPT BOŞLUĞU · 6

| # | S | bulgu | eksik |
|:--:|:--:|---|---|
| 🅑-1 | S04 | *Hammer hits the stake with zero soil displacement, shockwave or recoil mass* | darbenin **izi** yazılmamış [D213] |
| 🅑-2 | S01 | *Effortless heavy lift of crate without back curve, leg drive or neck strain* | efor cümlesi 7/14 |
| 🅑-3 | S01 | *Visor glass exhibits zero interior moisture/fogging during intense physical tasks* | vizör buğusu hiçbir promptta yok |
| 🅑-4 | S01 | *Pressurized suit gloves display bare-hand dexterity* | eldiven kalınlığının hareketi bozması yazılmamış |
| 🅑-5 | S06 🔴 | *Recovery Curve Honesty 2/10 — reset between Scene 7 and Scene 8* | yorgunluk birikimi yok [D207] |
| 🅑-6 | — | ortam ADI 14/14, ortam SAYISI **0/14** | düşüş süresi/ivme sayıyla yok |

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEK 14/14 TAM, YİNE DE 17 🅐. Prompt yazımının bu filmde yapacağı iş
   neredeyse yok; altı 🔴 temas füzyonu ve cümle yerli yerinde.
2. TEMAS CÜMLESİ YETMİYOR — ÖLÇÜLDÜ. Dört filmde cümle var/yok karşılaştırıldı;
   varken de altı BLOCKER çıkıyor. Çözüm kadraj kararında.
3. EFOR 7/14 VE DÖRT BULGU. Kalan altı 🅑'nin dördü tek bir eksik cümleden.
```
