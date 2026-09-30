# 🧩 THE_GREEN_CEILING — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · BULGU 12 → tekil 12
HÜKÜM       🅐 6 · 🅑 6 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %50
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 25/25: SES · bloom · metin · g-ad · filigran · kamera
  KISMİ: dış-ses 2/25 · sayı 17/25 · temas 17/25 · parçacık 19/25 · efor 19/25
  ⛔ HİÇ YOK: giysi · g-sayı
  bulgulu sahnelerde eksik: dış-ses 0/9 · sayı 8/9 · temas 8/9 · giysi 0/9 · parçacık 8/9 · g-sayı 0/9
```

## 🅑 SINIF 1 — AYNI KADRAJDA İKİ HIZ REJİMİ · 2 🔴 ⭐
S01 🔴 (*"Rain falls at real-time speeds while the tablet floats mid-air in the
same medium"*) · S05 🔴 (*"Rain falls normally while the nail experiences extreme
slow-motion/float"*). Ortam ADI **25/25'te** yazılı, ortam SAYISI **0/25**. İki bulgu da yağmurla
nesneyi aynı karede farklı yasaya tabi tutuyor [D200]: ortam adlandırılmış ama
yağmurun ve nesnenin hangi hızla düşeceği sayıyla verilmemiş.

## 🅑 SINIF 2 — GİYSİ 0/25 · 1 🟠 · SINIF 3 — SIFIR-G MİKRO HAREKET · 1 🟠
S10 (*"Suit material lacks proper cloth simulation or creasing during steps"*) ·
S05 (*"floating pin remains rigidly static instead of drifting"*).

## 🅑 SINIF 4 — TEMAS 17/25 · 2 🟠
S00 (*parmaklar sandık sapına kaynıyor*) · S19 (*eldiven kilide dokununca yapısını
kaybediyor*) — ikisi de cümlenin düştüğü sekiz sahnede.

## 🅐 MODEL SAPMASI · 6
S14 ×3 (*kapsül egzozu hafif CGI bloom · düzlemsel duman · hacimsiz kütle*) —
bloom 25/25 ve parçacık 19/25'te yazılı. S09 (*yüzen yapraklar 2D*) ·
S07 (*yapay ağır çekim yürüyüş*) · S15 (*airbrushed plastik cilt*).

## 🎯 ÜÇ SATIR
```
1. YAĞMUR GERÇEK ZAMANLI, NESNE AĞIR ÇEKİM — iki 🔴, aynı karede iki yasa.
2. GİYSİ CÜMLESİ 0/25. Kumaş kırışmıyor, giysi katı bir kabuk gibi duruyor.
3. ÇEKİRDEK GERİ KALANI İYİ — 🅑 %50, altı 🅐 kilidin yazılı olduğu yerlerde.
```
