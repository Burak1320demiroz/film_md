# 🧩 THE_COUNTED_TURN — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   11/11 geçerli · BULGU 23 → tekil 20
HÜKÜM       🅐 16 · 🅑 3 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %16
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 25/25: SES · metin · filigran · kamera
  KISMİ: sayı 22/25 · temas 22/25 · giysi 22/25 · parçacık 22/25 · bloom 22/25 · efor 24/25 · g-ad 22/25
  ⛔ HİÇ YOK: dış-ses · g-sayı
  bulgulu sahnelerde eksik: dış-ses 0/15 · sayı 14/15 · temas 14/15 · giysi 14/15 · parçacık 14/15 · bloom 14/15 · g-ad 14/15 · g-sayı 0/15
```

> ⭐ **On üç 🔴, çekirdek neredeyse tam.** Bu film DRY_ANCHOR'ın ikizi: temas
> cümlesi 22/25'te yazılı ve **altı temas BLOCKER'ı** çıkmış.

---

## 🅐 SINIF 1 — KAYIŞ/KARABİNA TEMASI · 6 🔴 · 2 🟠 ⭐ filmin tamamı bu

| S | bulgu |
|:--:|---|
| S02 🔴 | *Left hand fingers severely morph and melt, fusing completely with the strap geometry* |
| S03 🔴 | *The right thumb phases entirely through the solid metal of the orange carabiner* |
| S08 🔴 | *The grey fabric strap passes directly through the palm* |
| S10 🔴 | *The fabric strap phases through the solid metal floor pin* |
| S16 🔴 | *The orange carabiner phases completely through the solid metal rail* |
| S18 🔴 | *The grey strap becomes embedded inside the geometry of the ring* |
| S20 🔴 | *The fingers of the right hand merge into and fuse with the orange carabiner* |
| S04 · S11 🟠 | ⑦ *Contact Without Occlusion* — kancanın kapağının kapandığı an okunmuyor |

**Promptta ne yazıyordu:** `no merging, no phasing …` **22/25'te**. Filmin novumu
**kayış ve karabinadır**; her sahne bir temas sahnesidir ve yedi BLOCKER da
tam oradan çıkmıştır.

**Hüküm 🅐 ×7.** ⭐ Bu, temas sınıfının **en ağır kanıtı**: cümle yazılı, film
baştan sona temas üzerine kurulu, sonuç yedi BLOCKER. Ders siparişi DRY_ANCHOR ile
aynı ve artık iki filmde ölçülü: **temas anı kadraj kararıyla çözülür**
(perdeleme · ara katman · temasın öncesi/sonrası gösterilip anının atlanması).

## 🅐 SINIF 2 — EFOR VE BEDEL · 6 🔴

S01 🔴 *EFFORTLESS HEAVY* · S07 🔴 *EFFORTLESS HEAVY* · S08 🔴 *GRIP THAT NEVER
FAILS* · S09 🔴 *SYMMETRIC BODY UNDER ASYMMETRIC LOAD* · S18 🔴 *THE SUIT THAT
ISN'T THERE* · S22 🔴 *INFINITE STAMINA*. Efor cümlesi 24/25'te yazılı.

## 🅐 SINIF 3 — KİMLİK · 2 🔴 · 1 🟠

S11 🔴 (*"Male face with stubble vs smooth female face"*) · S12 🔴 (*"White bulky
spacesuit vs dark ribbed leather jacket"*) · S11 (*turuncu kemer klipsleri var/yok*).
Giysi cümlesi 22/25'te.

---

## 🅑 PROMPT BOŞLUĞU · 3

| # | S | bulgu | eksik |
|:--:|:--:|---|---|
| 🅑-1 | S19 | *The initial fall (S0) is visually almost as fast as the late fall (S19/S23)* | düşüş hızının **artışı** hiçbir promptta sayıyla yok · ortam ADI 22/25'te var ama ortam SAYISI 0/25 |
| 🅑-2 | S07 | *The astronaut's upward movement as they rise from the spool is unusual* | kalkış hareketi temas noktasıyla yazılmamış |
| 🅑-3 | — | dış-ses 0/25 | ortamın ses yasası hiç yazılmamış |

## 🎯 ÜÇ SATIR

```
1. 🅑 ORANI %16 — prompt tarafında üç cümlelik iş kaldı. Kusur motorda.
2. YEDİ TEMAS BLOCKER'I, CÜMLE 22/25'TE YAZILI. DRY_ANCHOR ile ikinci ölçüm:
   temas cümlesi yetmiyor, kadraj kararı gerekiyor.
3. ALTI EFOR BLOCKER'I, CÜMLE 24/25'TE YAZILI. Cümle var, oran düşüşü yok.
```
