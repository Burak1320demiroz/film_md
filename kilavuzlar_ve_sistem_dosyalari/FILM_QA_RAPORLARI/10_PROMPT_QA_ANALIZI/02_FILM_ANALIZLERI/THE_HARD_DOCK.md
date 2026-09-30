# 🧩 THE_HARD_DOCK — prompt hata analizi

```
FORMAT      yatay 4 dk · 24 sahne · BULGU 5 → tekil 5
HÜKÜM       🅐 1 · 🅑 4 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %80
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 24/24: SES · bloom · metin · g-ad · filigran · kamera
  KISMİ: dış-ses 10/24 · sayı 14/24 · temas 14/24 · giysi 12/24 · parçacık 1/24 · efor 16/24
  ⛔ HİÇ YOK: g-sayı
  bulgulu sahnelerde eksik: dış-ses 3/5 · sayı 2/5 · temas 2/5 · giysi 2/5 · parçacık 1/5 · efor 3/5 · g-sayı 0/5
```

> ⭐ **Deponun en az bulgulu filmlerinden biri: 12 ham rapor, 5 bulgu.**
> Yazımı iyi; kalan dört boşluk da dar ve adlandırılabilir.

## 🅑 SINIF 1 — SAYILABİLİR DETAY RAKAMLA YAZILMAMIŞ · 1 🟠 [D78/D151]
S12 ⑤ (*"Circular porthole window rim changes bolt count from **8 to 10** perimeter
bolts"*). Cıvata sayısı promptta yok.

## 🅑 SINIF 2 — PARALAKS VE ÖLÇEK · 1 🟠
S06 ⑤ (*"Capsule craft and background planet surface move with **zero relative
parallax**"*) — derinlik cümlesi yok [D209 · D131].

## 🅑 SINIF 3 — YER ŞEKLİ DEVAMLILIĞI · 1 🟠
S13 ⑤ (*"Magma fissure topology shifts from a uniform grid to a large central
volcanic peak"*).

## 🅑 SINIF 4 — KENETLENME ANI PERDELENİYOR · 1 🟠 [D213]
S22 ⑦ (*"The exact physical contact, alignment and mechanical latching of the
docking ring onto the station …"*) — **filmin adı kenetlenme** ve kenetlenmenin
teması kadrajda okunmuyor.

## 🅐 MODEL SAPMASI · 1
S21 🔴 (*"spatial orientation cut mismatch, solar panel jitter"*) — kamera cümlesi
24/24'te yazılı.

## 🎯 ÜÇ SATIR
```
1. BEŞ BULGU, 12 HAM RAPOR — deponun en temiz filmlerinden.
2. FİLMİN ADI KENETLENME, KENETLENME ANI OKUNMUYOR. Tek 🟠 ama en pahalısı.
3. PARÇACIK 1/24 VE ORTAM SAYISI 0/24 — iki cümle hâlâ eksik.
```
