# 🧩 THE_CRACKED_HELMET — prompt hata analizi

```
FORMAT      yatay 2 dk · 12 sahne · ⭐ IZGARA ÖLÇÜLDÜ (9 raporun künyesi: süre ÷ sahne = 10 s)
HAM RAPOR   12/12 geçerli · BULGU 22 → tekil 21
HÜKÜM       🅐 0 · 🅑 20 · 🅒 1 · 🅓 0      🅑/(🅐+🅑) = %100
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: efor 2/12
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi · parçacık · bloom · metin ·
             g-ad · g-sayı · filigran · kamera
```

> ⛔ **Çekirdeğin on üç cümlesinden on ikisi HİÇ YOK.** THE_SILENT_PERIHELION ile
> birlikte deponun 🅐'sı olmayan ikinci filmi — tutacak kilit yazılmamış.

---

## 🅑 SINIF 1 — ORTAM NE ADIYLA NE SAYISIYLA YAZILMAMIŞ · 2 🔴 · 4 🟠 ⭐

| S | bulgu |
|:--:|---|
| S07 🔴 | *Mixed gravity: a liquid sphere floats in a 1 g environment* |
| S07 🔴 | *Mixed gravity vectors in a single frame* |
| S07 | *Liquid forms a zero-g sphere despite established gravity* |
| S07 | *Liquid ignores 1 g physics to form a floating sphere* |
| S00 | *Plumes of smoke rise in thick convective buoyant columns requiring a dense atmosphere* |
| S07 | *AI bloom around the floating liquid* |

Ortam adı 0/12, ortam sayısı 0/12. Aynı karede sıvı 0 g'de, gövde 1 g'de
[D200]. ⭐ Rapor "established gravity" diyor — **kurulmuş bir yerçekimi yok.**

## 🅑 SINIF 2 — DÜNYA ÇAPASI YOK · 4 🟠 [D209]

S02 (*boş siyah gök ↔ halkalı dev gezegen*) · S11 ×2 (*tek beyaz güneşli siyah gök
↔ iki sarı güneşli turuncu puslu gök* · *havasız sivri arazi ↔ geniş kanyon ovası*).
**12 sahnelik filmde gökyüzü iki kez tamamen başka bir gök oldu.**

## 🅑 SINIF 3 — GİYSİ DEVAMLILIĞI 0/12 · 4 🟠

S02 · S03 (*siyah giysi ↔ beyaz giysi, iki kez*) · S10 (*düz göğüs kutusu ↔ **ORION**
yazılı büyük kutu*) · S11 (*mühürlü çatlaklı vizör ↔ kusursuz düz altın vizör*).

## 🅑 SINIF 4 — JETON SIZINTISI VE EKRAN YAZISI · 1 🔴 · 1 🟠

S02 🔴 (*Burned-in HUD text physically stuck on the exterior of the visor*) ·
S10 (*göğüs kutusunda **ORION** yazısı*). Metin yasağı **0/12** — yazılmamış bile.
⭐ `ORION` büyük harfli bir jetondur; sınıfın dördüncü filmi.

## 🅑 SINIF 5 — EFOR 2/12 · 6 (1 🔴)

S01 · S02 · S04 · S08 · S10 · S11 🔴 — *"waking to a critical air leak — increased
respiratory rate"* · *"pinching a crystal in space gloves — clumsiness"* ·
*"the suit reports CRITICAL pressure loss but the breathing is calm"* ·
S11 🔴 *"standing up after the ordeal — slumped posture, heavy exhaustion"*.

## 🅑 SINIF 6 — TEMAS 0/12 · 1 🟠

S08 ⑦ (*"the transition between holding a floating liquid sphere and applying a
solid shard to the glass"* — temas anı okunmuyor [D213]).

---

## 🅒 BULGU DÜŞER · 1

S02 ⑤ gök çelişkisinin bir kolu iki ayrı mekânı karşılaştırıyor; sahne haritası
geçişi taşıyor. ⚠️ Diğer gök bulguları düşmez: aynı sahnede iki gök meşru değildir.

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEK 12/13 CÜMLE EKSİK — 🅐 SIFIR. Tutacak kilit hiç yazılmamış;
   deponun 🅐'sı olmayan ikinci filmi.
2. AYNI KAREDE SIVI 0 g'DE, GÖVDE 1 g'DE. İki 🔴, ortam ne adıyla ne sayısıyla yok.
3. GÖKYÜZÜ İKİ KEZ BAŞKA BİR GÖK OLDU. 12 sahnede dört dünya-çapası bulgusu.
```
