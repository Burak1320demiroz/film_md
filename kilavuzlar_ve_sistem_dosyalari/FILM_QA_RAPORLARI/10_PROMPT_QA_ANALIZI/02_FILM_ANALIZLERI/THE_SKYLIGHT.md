# 🧩 THE_SKYLIGHT — prompt hata analizi

```
FORMAT      yatay 4 dk · 33 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   6/6 geçerli · BULGU 18 → tekil 18
HÜKÜM       🅐 8 · 🅑 9 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %53
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 30/33 · sayı 31/33 · temas 8/33 · giysi 22/33 · parçacık 22/33 · bloom 30/33 · metin 28/33 · efor 31/33 · g-ad 3/33 · g-sayı 27/33 · filigran 28/33 · kamera 30/33
  ⛔ HİÇ YOK: dış-ses
  bulgulu sahnelerde eksik: SES 8/10 · dış-ses 0/10 · sayı 8/10 · temas 3/10 · giysi 6/10 · parçacık 6/10 · bloom 8/10 · metin 8/10 · efor 8/10 · g-ad 0/10 · g-sayı 9/10 · filigran 8/10 · kamera 8/10
```

---

## 🅑 SINIF 1 — ORTAM ADI 3/33 · 3 🟠 ⭐ ve biri iki rejimi aynı kadraja koyuyor

S29 ⑥ (*"Floating bolts indicate a 0 g environment, but the astronaut's body,
harness and suit are entirely …"*) · S29 ×2 (*"Rigid 1 g character model suspended
in a zero-g environment"*) · S22 (*"Character glides/moonwalks over the terrain
without visibly planting"*). Ortam SAYISI 27/33'te var ama ortamın ADI yalnız 3/33'te: sayı yazılmış,
hangi ortamda geçerli olduğu yazılmamış.

## 🅑 SINIF 2 — TEMAS 8/33 · 3 🟠

S01 (*parmaklar kaya dokusuna kaynıyor*) · S13 (*düşen toz eldivenden geçiyor*) ·
S25 (*eller emniyet kemerine karışıyor*) — üçü de cümlenin düştüğü sahnelerde.

## 🅑 SINIF 3 — ARKA PLAN NESNE ENVANTERİ · 2 🟠

S11 ×2 (*"Orange/white striped pole stands next to the rock stack; then the pole is
completely absent"*). Kurulum dönüyor, arka plan cümlesi dönmüyor.

## 🅑 SINIF 4 — ARAÇ/GİYSİ DURUMU 22/33 · 4 🟠

S24 ×2 (*roketin siyah dikey şeridi beyaz yatay banda dönüşüyor · roket açık ovada
iken sonra kayalarla çevrili*) · S25 ×2 (*kask yanları opak iken saydam oluyor ·
giysi sırtı çok kirli iken tertemiz*).

---

## 🅐 MODEL SAPMASI · 8

S12 🔴 ×2 (*"A duplicate astronaut inexplicably spawns on the left side"*) —
insan sayısı 31/33'te yazılı. S26 🔴 ×2 (*"Rocket exhaust flames clip entirely
through the solid landing legs"*) — parçacık 22/33'te. S09 (*el feneri yönsüz bloom*) —
bloom 30/33'te.

## 🎯 ÜÇ SATIR

```
1. 33 SAHNELİK FİLMDE TEMAS CÜMLESİ 8'İNDE. Üç bulgu, üçü de boşlukta.
2. ORTAM ADI 3/33. Cıvata 0 g'de yüzüyor, gövde 1 g'de duruyor — aynı kadrajda.
3. ROKETİN BOYASI DEĞİŞİYOR. Araç durum merdiveni yok; dört bulgu oradan.
```
