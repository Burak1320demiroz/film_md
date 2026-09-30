# 🧩 THE_LOCKED_PULSE — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   12/12 geçerli · BULGU 24 → tekil 24
HÜKÜM       🅐 15 · 🅑 8 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %35
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 25/25: SES · giysi · bloom · metin · filigran · kamera
  KISMİ: dış-ses 1/25 · sayı 24/25 · temas 24/25 · efor 24/25 · g-sayı 1/25
  ⛔ HİÇ YOK: parçacık · g-ad
  bulgulu sahnelerde eksik: dış-ses 1/12 · sayı 11/12 · temas 11/12 · parçacık 0/12 · efor 11/12 · g-ad 0/12 · g-sayı 0/12
```

---

## 🅑 SINIF 1 — ARKA PLAN ENVANTERİ KİLİTLİ DEĞİL · 3 🟠 ⭐ bu filme özgü

| S | bulgu |
|:--:|---|
| S02 | *Fabric wall strap hangs on left wall in S1; completely missing from the same wall angle in S3* |
| S02 | *Floor grate is bare in S1; a silver combination wrench appears lying on it in S3* |
| S05 | *Right corridor wall is bare panelling in S5; a large grey supply cabinet materializes in S6* |

**Promptta ne yazıyordu:** her sahne koridoru **kendi kelimeleriyle** tarif ediyor;
arka plandaki nesnelerin sabit bir envanteri yok. Kamera aynı duvara iki kez
bakıyor ve iki farklı duvar görüyor.

**Hüküm 🅑 ×3.** Yazım kuralı: aynı kurulum harfine dönen her sahne **aynı arka plan
cümlesini birebir** taşır (kurulum iskeletinin "işaret satırı" kuralı) —
model iskeleti görmez, metni görür.

## 🅑 SINIF 2 — PARÇACIK CÜMLESİ 0/25 · 1 🟠

S03: *"Venting steam particles lack physical mass and dissipate uniformly as flat haze."*

## 🅑 SINIF 3 — SESLE GÖRÜNTÜ ARASINDA SAYI KÖPRÜSÜ YOK · 1 🟠 ⭐ öğretici

S13 ③: *"Audio states 'Ring at four revolutions' (4 RPM) but the exterior shot
shows 0.21 RPM (2.1° of rotation)."* Replik bir **sayı söylüyor**; o sayı hiçbir
görsel prompta girmemiş. Ses ile görüntü arasındaki tek köprü sayıdır ve kurulmamış.

## 🅑 SINIF 4 — EFORUN ŞİDDETİ SAYIYLA YOK · 3 (⑧'in 🔴'ları)

S00 🔴 · S07 🔴 · S10 🔴 — *"Effortless Heavy"* · *"Infinite Stamina"*.
Efor cümlesi 24/25'te **var**; eksik olan **oran düşüşü**: kaç tur sonra ne kadar
yavaşladığı hiçbir promptta yazmıyor.

---

## 🅐 MODEL SAPMASI · 15

**⑧ EFOR** S01 · S02 · S05 🔴 · S08 · S11 · S17 (efor 24/25) — *"Breath Doesn't
Track"* · *"Fresh Reset"* · *"Grip That Never Fails"* · *"Recovery Faster Than
Exertion"*. **Temas** S03 ×2 · S12 (temas 24/25). **Kimlik** S01 (çene hattı
kayması, giysi 25/25). **Bloom/cilt** S00 ×2 · S07 (bloom 25/25 — *"airbrushed,
waxy skin"*). **Doku yüzmesi** S05 ×2.

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEK NEREDEYSE TAM, 🅑 ORANI %35. Eksik iki cümle: parçacık ve yerçekimi.
2. AYNI DUVARA İKİ KEZ BAKMAK. Üç bulgu arka plan envanterinden — kurulum
   harfi dönüyor, arka plan cümlesi dönmüyor.
3. REPLİK SAYI SÖYLÜYOR, PROMPT SÖYLEMİYOR. "Dört tur" denmiş, kadrajda 0,21.
```
