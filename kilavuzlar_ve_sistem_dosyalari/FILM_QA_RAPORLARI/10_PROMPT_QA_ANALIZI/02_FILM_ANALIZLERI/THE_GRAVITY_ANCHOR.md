# 🧩 THE_GRAVITY_ANCHOR — prompt hata analizi

```
FORMAT      yatay 2 dk · 10 sahne · ⭐ IZGARA ÖLÇÜLDÜ (5 raporun künyesi: süre ÷ sahne = 10 s)
HAM RAPOR   11/11 geçerli · BULGU 16 → tekil 16
HÜKÜM       🅐 3 · 🅑 12 · 🅒 1 · 🅓 0      🅑/(🅐+🅑) = %80
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 10/10: parçacık · metin · filigran
  KISMİ: efor 4/10
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi · bloom · g-ad · g-sayı · kamera
```

> ⚠️ Filmin **adı yerçekimi çapası** ve ortam sayısı **0/10**.

---

## 🅑 SINIF 1 — BİLEK CİHAZI ÜÇ KEZ BAŞKA BİR ŞEY OLDU · 3 🟠 ⭐ tek nesne, üç bulgu

| S | bulgu |
|:--:|---|
| S01 | *Suit drift — the wrist device is a rectangular screen* |
| S03 | *Suit drift — the wrist device changes to a circular glowing 'M' or 'W' logo* |
| S06 | *Suit drift — the wrist device vanishes entirely during the wide touch shot* |

Giysi/donanım devamlılık cümlesi **0/10**. Filmin taşıyıcı nesnesi bilek
cihazıdır; dikdörtgen ekran → yuvarlak parlayan logo → yok.
⭐ Üçüncü bulguda cihaz bir **logoya** dönüşmüş: jeton/amblem sızıntısının komşusu.

## 🅑 SINIF 2 — ORTAM SAYISI 0/10 · 2 🟠

S04 ×2 (*"rising rocks move linearly like 2D assets without collision"* ·
*"floating debris lacks micro-rotation — the smaller pebbles rise rigidly without
individual spin"*). Parçacık cümlesi **10/10'da yazılı**, ortam sayısı yok.
⭐ İkinci bulgu **açısal momentumu** adlandırıyor: çekirdek cümlesi yalnız
doğrusal momentumu söylüyor, dönmeyi söylemiyor — `03_` §🅐-2'nin aynısı.

## 🅑 SINIF 3 — EFOR 4/10 · 4 (2 🔴)

S01 · S03 🔴 ×2 · S05 — *"forearm stiffness, glove resistance, neck bending
restricted"* · *"shoulder lift compensation, torso tilt, suit joint tightness"* ·
*"forearm tendon tension, finger flex against the pressurized glove"* ·
*"visor condensation, chest/shoulder drop"*.

## 🅑 SINIF 4 — DÜNYA ÇAPASI · 3 🟠 [D209]

S01 (*yoğun kar S4'te durağan sis pusuna dönüşüyor*) · S03 (*üst ufuk çam
silueti S7 geniş planla uyuşmuyor*) · S04 (*arka plan ağaç derinlik katmanı
S9'da duvara yapışıyor*).

---

## 🅐 MODEL SAPMASI · 3

S02 (*monolitteki gökkuşağı kırılması morfluyor*) · S07 (*yüz kayması — kemik yapısı
ve cilt dokusu geniş plana göre yumuşuyor*) · S08 (*tek sert gölge yanlış yöne
düşüyor*). Parçacık ve metin cümleleri 10/10'da yazılıyken doku ve ışık kaydı.

## 🅒 BULGU DÜŞER · 1

S03 🔴 (*"Compilation mode — interior/exterior or radical focal jump; the extreme
macro shot …"*) — ① merceği **derleme** sandı; bu bir makro plan kararıdır ve
sahne haritasında yazılıdır.

## 🎯 ÜÇ SATIR

```
1. FİLMİN ADI YERÇEKİMİ, ORTAM SAYISI 0/10.
2. BİLEK CİHAZI ÜÇ KEZ DEĞİŞTİ — giysi cümlesi 0/10. Tek nesne, üç bulgu.
3. AÇISAL MOMENTUM ÇEKİRDEKTE YOK. "Küçük çakıllar kendi ekseninde dönmeden
   yükseliyor" — cümle yalnız doğrusal momentumu söylüyor.
```
