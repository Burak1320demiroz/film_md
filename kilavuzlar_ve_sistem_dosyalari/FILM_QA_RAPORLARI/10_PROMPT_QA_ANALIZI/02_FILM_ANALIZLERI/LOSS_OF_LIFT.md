# 🧩 LOSS_OF_LIFT — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · HAM RAPOR 2/2 geçerli · BULGU 1 → tekil 1
HÜKÜM       🅐 0 · 🅑 1 · 🅒 0 · 🅓 0
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 23/25 · sayı 22/25 · temas 21/25 · parçacık 24/25 · bloom 23/25 · metin 23/25 · efor 21/25 · g-sayı 24/25 · filigran 23/25 · kamera 23/25
  ⛔ HİÇ YOK: dış-ses · giysi · g-ad
  bulgulu sahnelerde eksik: dış-ses 0/1 · sayı 0/1 · temas 0/1 · giysi 0/1 · g-ad 0/1
```

> ⚠️ **Tek bulgu, ama örneklem de küçük:** bu filmin yalnız **iki** ham raporu var
> (MANTIK · SENARYO) ve ikisi de **senaryo katmanı** merceğidir. On üç teknik
> merceğin hiçbiri koşulmamış. Düşük bulgu sayısı "film temiz" demek DEĞİL,
> **"film ölçülmemiş"** demektir.

## 🅑 TEK BULGU — SAYILABİLİR NESNE RAKAMLA YAZILMAMIŞ [D78/D151]
S19 ② (*"The gas rack in S11 has **~12 small nozzles** in a row. The rack in S20 has
**~6 large cylinders**"*). Rafın üzerindeki nozul sayısı hiçbir promptta yok.

## 🎯 ÜÇ SATIR
```
1. BİR BULGU — VE BU İYİ HABER DEĞİL. 13 teknik mercek hiç koşulmamış.
2. TEK BULGU DA SAYI SINIFINDAN: 12 nozul 6 silindire döndü.
3. ÖNCELİK: bu filme ①-④ dört zorunlu mercek koşulmalı, sonra bu dosya tazelenir.
```
