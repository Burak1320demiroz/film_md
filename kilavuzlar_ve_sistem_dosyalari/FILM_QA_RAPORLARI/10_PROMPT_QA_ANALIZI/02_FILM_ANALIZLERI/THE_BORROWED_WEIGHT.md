# 🧩 THE_BORROWED_WEIGHT — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   4/4 geçerli · BULGU 20 → tekil 19
HÜKÜM       🅐 8 · 🅑 10 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %56
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 23/25 · sayı 23/25 · temas 15/25 · giysi 18/25 · parçacık 16/25 · bloom 23/25 · metin 23/25 · efor 20/25 · g-sayı 21/25 · filigran 22/25 · kamera 23/25
  ⛔ HİÇ YOK: dış-ses · g-ad
  bulgulu sahnelerde eksik: SES 14/15 · dış-ses 0/15 · sayı 13/15 · temas 9/15 · giysi 10/15 · parçacık 9/15 · bloom 14/15 · metin 14/15 · efor 12/15 · g-ad 0/15 · g-sayı 12/15 · filigran 13/15 · kamera 14/15
```

---

## 🅑 SINIF 1 — AYNI SES ÖRNEĞİ İKİ KEZ · 3 🟠 ⭐ bu klasörde tek

| S | bulgu |
|:--:|---|
| S02 | *Prosody and timing are mathematically identical* |
| S03 | *Exact duplicate sample used for two separate narrative thoughts* |
| S01 | *Wind bed drops to digital zero across the cut* |

**Promptta ne yazıyordu:** replikler promptta **aynı cümleyle** iki kez geçiyor ve
hiçbir yerde "bu ikinci sefer farklı söylenir" yazmıyor. Oda tonu köprüsü de
yazılmamış → kesmede ses dijital sıfıra düşüyor [D216: her kesmede ≥ 0,2 s köprü].

**Hüküm 🅑 ×3.** Yazım kuralı: aynı replik iki kez geçiyorsa **ikincisi farklı
teslimatla** yazılır; her kesme oda tonu köprüsü taşır.

## 🅑 SINIF 2 — ORTAM ADI 0/25 · 1 🟠 · 🅑 SINIF 3 — ÖLÇEK · 1 🔴

S19 (*"The dropped scale falls with balloon-like, low-mass physics"*) ·
S12 🔴 (*"Pod scales from tiny to massive"*) — kapsülün boyu hiçbir promptta
gövde boyu cinsinden değil [D138].

## 🅑 SINIF 4 — TEMAS 15/25 · 3 🔴

S05 🔴 (*"Fingers fuse and melt into the metal wrenches"*) · S10 🔴 (*"hands push
completely through the solid metal geometry"*) · S15 🔴 (*"Fingers phase through
the flat surface of the metal wall"*) — üçü de cümlenin düştüğü sahnelerde.

## 🅑 SINIF 5 — KİR VE IŞIK DURUMU · 2 🟠

S20 (*"Dirty knees reset to clean"*) · S21 (*"Daylight instantly becomes night"*) —
kir merdiveni ve ışık takvimi yazılmamış [D193].

---

## 🅐 MODEL SAPMASI · 8

**Nesne morfolojisi** S07 🔴 ×3 (*"the entire brass scale dynamically morphs,
altering its geometry"*) · S13 (*terazi tasarımı değişiyor*) — filmin **taşıyıcı
nesnesi** pirinç terazi ve giysi/nesne cümlesi 18/25'te yazılı.
**Kimlik** S11 🔴 (*yüz kemik yapısı değişiyor*) · S07 (*göğüs plakası şekil
değiştiriyor*). **Bloom** S18 · S23 (bloom 23/25). **Parçacık** S10 (*toz donuyor*).

## 🎯 ÜÇ SATIR

```
1. TAŞIYICI NESNE (PİRİNÇ TERAZİ) DÖRT KEZ BİÇİM DEĞİŞTİRDİ. Cümle yazılı →
   novum taşıyıcısı REFERANS PANELİ ister, metin yetmiyor.
2. AYNI SES ÖRNEĞİ İKİ KEZ ÇALINDI. Depoda bu bulguyu veren tek film.
3. ÇEKİRDEK %60-90 ARASI YAMALI. Üç temas 🔴'sının üçü de cümlenin düştüğü yerde.
```
