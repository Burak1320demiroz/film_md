# 🧩 THE_UPWARD_FALL — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   8/8 geçerli · BULGU 21 → tekil 21
HÜKÜM       🅐 7 · 🅑 13 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %65
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 25/25: SES · sayı · bloom · metin · efor · g-sayı · filigran · kamera
  KISMİ: temas 8/25 · giysi 3/25 · parçacık 4/25 · g-ad 2/25
  ⛔ HİÇ YOK: dış-ses
  bulgulu sahnelerde eksik: dış-ses 0/11 · temas 3/11 · giysi 1/11 · parçacık 2/11 · g-ad 0/11
```

---

## 🅑 SINIF 1 — NESNE DEVAMLILIĞI CÜMLESİ 22 SAHNEDE YOK · 5 🟠

| S | bulgu |
|:--:|---|
| S10 | *Canister scale jumps from hand-sized to massive/torso-sized* |
| S12 | *Axe lodged in the trunk disappears in an identical environment* |
| S13 | *Visor frame changes from thin unlit black to thick glowing white* |
| S16 | *Green vine tied securely around the canister is completely missing when next held* |
| S07 · S21 | *Smooth banyan trunks become textured redwoods* · *ash flatland becomes deep pine valley* |

`identical throughout / no drift` kalıbı **3/25**. Bidonun boyu, baltanın yeri,
vizörün türü ve sarmaşığın varlığı hiçbir promptta kilitli değil.

## 🅑 SINIF 2 — İVME SABİT BİR SAYIYA BAĞLANMAMIŞ · 1 🔴 · 2 🟠 ⭐ filmin novumu

S15 🔴 (*"Upward acceleration triples floor→canopy"*) · S17 (*"Accelerates in S10,
drifts at constant velocity in S17"*) · S07 ⑥ (*"real-time environment vs
slow-motion biomechanics"*). Ölçüm: ortam SAYISI **25/25 promptta var**, ortam ADI
yalnız 2/25'te. Yani her sahne bir sayı taşıyor ama **aynı sayıyı taşımıyor** ve
ivmenin kat ettiği yol boyunca nasıl değiştiği hiçbir yerde yazılı değil —
filmin adı **yukarı düşüş** ve ivme onun novumu.

## 🅑 SINIF 3 — TEMAS 8/25 · 4 🟠

S14 ×2 (*"Hand geometry phases through green vine and container"*) ·
S19 ×2 (*"Fingers morph and fuse with the knife handle and vine"* ·
*"Left hand fuses with knife handle; blade clips through wood"*).

## 🅑 SINIF 4 — CANLI ANATOMİSİ KİLİTSİZ · 1 🟠

S17 ×3 mercek (*"Background alien lacks joint articulation during jump"* ·
*"leaps with a linear, rigid trajectory"*). Arka plandaki canlı hiçbir promptta
eklem/ağırlık cümlesi taşımıyor.

---

## 🅐 MODEL SAPMASI · 7

⑧ EFOR S10 · S14 · S19 (*"Effortless Heavy"* · *"The Suit That Isn't There"* ·
*"Grip That Never Fails"*) — efor 25/25. Doku yüzmesi S19. Ortam geçişi S20.

## 🎯 ÜÇ SATIR

```
1. FİLMİN NOVUMU (İVME) SAYISIZ. Bir 🔴 ve iki 🟠 doğrudan oradan.
2. NESNE DEVAMLILIĞI 3/25. Balta, sarmaşık, bidon ve vizör sahne sahne değişiyor.
3. TEMAS 8/25 VE DÖRT BULGU — hepsi cümlenin düşmediği sahnelerde.
```
