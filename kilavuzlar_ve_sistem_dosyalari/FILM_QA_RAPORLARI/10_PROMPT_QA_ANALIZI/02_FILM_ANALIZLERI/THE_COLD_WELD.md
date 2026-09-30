# 🧩 THE_COLD_WELD — prompt hata analizi

```
FORMAT      yatay 2 dk · 15 sahne · BULGU 9 → tekil 8
HÜKÜM       🅐 2 · 🅑 6 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %75
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 15/15: bloom · g-sayı · kamera
  KISMİ: sayı 14/15 · temas 4/15 · parçacık 6/15 · metin 14/15 · efor 13/15 · filigran 12/15
  ⛔ HİÇ YOK: SES · dış-ses · giysi · g-ad
  bulgulu sahnelerde eksik: SES 0/5 · dış-ses 0/5 · temas 1/5 · giysi 0/5 · parçacık 2/5 · metin 4/5 · g-ad 0/5 · filigran 3/5
```

## 🅑 SINIF 1 — SES 0/15 · 1 🔴
S01 🔴 (*"Airborne sound propagating in a vacuum — audible footsteps/clanking"*).
`AUDIO:` satırı hiçbir promptta yok.

## 🅑 SINIF 2 — TEMAS 4/15 · 2 🔴
S09 🔴 ×2 (*"wrench head clips entirely through the metal bolt"* · *"glove and
wrench head phase through the metal surface"*) — ikisi de cümlenin düştüğü
on bir sahnede.

## 🅑 SINIF 3 — ORTAM ADLANDIRILMAMIŞ (ad 0/15, sayı 15/15) · 2 🟠
S11 (*"Heavy metal plates float upwards against the established gravity"*) ·
S14 (*"Dropped disc lacks appropriate low-g momentum/impact"*).
⭐ Ölçüm: sayısal değer **15/15 promptta var** (`0,30 g`), ama ortamın ADI
(vakum mu ince atmosfer mi) hiçbir promptta yok. Sayı tek başına yetmiyor:
motor hangi ortamda olduğunu bilmeden sayıyı uygulayamıyor.

## 🅑 SINIF 4 — ALETİN ÖLÇÜSÜ VE TUTUŞU · 2 🟠 [D138]
S08 ⑥ (*"Wrench scale shifts from a small one-handed tool to a massive two-handed
lever"*) · S09 ② (*"Wrench orientation and grip change instantly across the cut"*).
Anahtarın boyu ve hangi elle tutulduğu hiçbir promptta yok.

## 🅐 MODEL SAPMASI · 2
S09 ⑤ (*düz ufuk dikey duvara dönüşüyor*) — kamera cümlesi 15/15'te.

## 🎯 ÜÇ SATIR
```
1. SES 0/15 VE BİR 🔴. Vakumda ayak sesi.
2. ALETİN BOYU YOK. Tek elle tutulan anahtar iki elli manivelaya dönüştü.
3. SAYI VAR, ORTAM ADI YOK. 0,30 g 15/15'te yazılı; vakum/atmosfer hiç yazılmamış.
```
