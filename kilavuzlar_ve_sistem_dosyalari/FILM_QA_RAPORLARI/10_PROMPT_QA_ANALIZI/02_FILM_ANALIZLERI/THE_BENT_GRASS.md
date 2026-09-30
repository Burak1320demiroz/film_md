# 🧩 THE_BENT_GRASS — prompt hata analizi

```
FORMAT      yatay 2 dk · 14 sahne · BULGU 9 → tekil 8
HÜKÜM       🅐 1 · 🅑 5 · 🅒 2 · 🅓 0      🅑/(🅐+🅑) = %83
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 14/14: bloom · metin · g-sayı · filigran · kamera
  KISMİ: sayı 11/14 · temas 11/14 · giysi 11/14 · parçacık 11/14 · efor 11/14 · g-ad 11/14
  ⛔ HİÇ YOK: SES · dış-ses
  bulgulu sahnelerde eksik: SES 0/6 · dış-ses 0/6 · sayı 4/6 · temas 4/6 · giysi 4/6 · parçacık 4/6 · efor 4/6 · g-ad 4/6
```

## 🅑 SINIF 1 — IŞIK TAKVİMİ YAZILMAMIŞ · 1 🔴 · 2 🟠 ⭐ [D193]
| geçiş | bulgu |
|---|---|
| S1→S2 | *Key direction lost (9 → ?); temperature cools (warm → neutral); exposure drops* |
| S2→S3 🔴 | *Key direction returns but **flips sides** (3); temperature warms back up* |
| S6→S7 | *Key direction lost (9 → ?); temperature cools; exposure drops* |

Anahtar ışığın **saat yönü** hiçbir promptta yazılı değil. Üç geçişte de ışık
kayboluyor, bir kez de taraf değiştiriyor.

**Yazım kuralı:** ışık yönü **saat yönüyle** yazılır (`one hard sun out of frame at
9 o'clock`) ve ışık takvimi film boyunca monotoniktir.

## 🅑 SINIF 2 — CANLI ANATOMİSİ · 2 🟠
S07 ×2 (*"The middle hippo creature in the background has a merged or extra
**fifth leg** geometry"*). Canlının bacak sayısı yazılmamış.
⭐ BENI_HATIRLAMA'da bu cümle YAZILMIŞTI ve yine tutmadı (altı bacak).
**İki filmde tekrar, iki farklı sahiple** — sınıf tablosu ikisini ayırıyor.

## 🅑 SINIF 3 — ASİMETRİK YÜK · 1 🟠
S06 ⑧ *SYMMETRIC BODY UNDER ASYMMETRIC LOAD* (*"carrying a loaded case —
asymmetric shoulder drop, slower arm swing"* yok).

## 🅒 BULGU DÜŞER · 2
S13 🔴 ×2 (*"Title card with burned-in text appears, replacing the final scene
('THE BENT GRASS HERE…')"*) — **kapanış kartıdır**, tipografi post-prodüksiyondadır.
⚠️ Ama kartın **son sahnenin yerine geçmesi** ④ KURGU'nun işidir ve oraya rapor edilir.

## 🎯 ÜÇ SATIR
```
1. ANAHTAR IŞIK SAAT YÖNÜYLE YAZILMAMIŞ — üç geçişte kayboldu, bir kez taraf değişti.
2. ARKA PLANDAKİ CANLI BEŞ BACAKLI. Bacak sayısı promptta yok.
3. İKİ 🔴'NIN İKİSİ DE BAŞLIK KARTI — sahne değil, ① merceğinin kapsamı dışında.
```
