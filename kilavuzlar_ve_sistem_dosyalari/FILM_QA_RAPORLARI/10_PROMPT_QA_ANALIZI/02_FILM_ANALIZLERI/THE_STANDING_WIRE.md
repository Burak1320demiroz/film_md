# 🧩 THE_STANDING_WIRE — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   8/8 geçerli · BULGU 24 → tekil 24
HÜKÜM       🅐 11 · 🅑 11 · 🅒 2 · 🅓 0      🅑/(🅐+🅑) = %50
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 23/25 · dış-ses 5/25 · sayı 23/25 · temas 11/25 · giysi 16/25 · parçacık 10/25 · bloom 22/25 · metin 21/25 · efor 22/25 · g-ad 1/25 · g-sayı 19/25 · filigran 22/25 · kamera 24/25
  bulgulu sahnelerde eksik: SES 15/16 · dış-ses 3/16 · sayı 14/16 · temas 8/16 · giysi 9/16 · parçacık 7/16 · bloom 14/16 · metin 13/16 · efor 14/16 · g-ad 1/16 · g-sayı 12/16 · filigran 14/16
```

> ⭐ **Yamalı çekirdek.** Bu filmde çekirdek cümleleri VAR ama **sahnelerin bir
> kısmında**. Bulguların yarısı tam olarak cümlenin düştüğü sahnelerde.

---

## 🅑 SINIF 1 — PARÇACIK CÜMLESİ SAHNELERİN 15'İNDE YOK · 2 🔴

S00 🔴 ×2: *"Floating particles without gravitational cause near the base plate"* ·
*"Pebbles float and disappear without cause."* — **ve S00 o 15 sahneden biri.**
Filmin açılış karesi, parçacık kilidi olmadan üretilmiş.

## 🅑 SINIF 2 — GİYSİ/ELDİVEN DEVAMLILIĞI 9 SAHNEDE KİLİTSİZ · 4 🟠

S03 (*eldiven kalınlığı sahneler arası değişiyor*) · S10 (*kalın kaburgalı zırh
eldiven ↔ düz deri*) · S12 (*göğüs panelleri ince şerit ↔ kalın beyaz boyunduruk*) ·
S15 (*dizler kalın gri çamurlu ↔ tertemiz mavi*). Kir durumu merdiven taşımıyor.

## 🅑 SINIF 3 — VAKUMDA SES · 2 🟠

S21 (*"Airborne whoosh layered with hatch opening in vacuum"*) · S14 ③
(*"Footfall SFX do not align with the visible pace"*). `AUDIO:` 23/25'te var ama
**dış-ses yasası yalnız 5/25'te**.

## 🅑 SINIF 4 — ÖLÇÜ GÖVDE BOYU CİNSİNDEN DEĞİL · 2 🟠 [D138]

S21 ⑥ (*"Wire diameter ~2 cm at base vs ~20 cm at the space station"*) ·
S23 (*"Wire behaves like a 2D ribbon inside the cabin"*). Filmin **novumu teldir**
ve telin kalınlığı hiçbir promptta sayıyla yok.

## 🅑 SINIF 5 — SIFIR-G'DE MİKRO HAREKET · 1 🟠

S18: *"Character is completely rigid while floating in zero-g; no micro-motion or
limb drift."* Ortam ADI 1/25 (sayı 19/25 — sayı var, ortam adı yok).

---

## 🅐 MODEL SAPMASI · 11

**⑧ EFOR** S04 · S05 🔴 · S07 · S11 · S16 · S18 · S19 🔴 (efor 22/25) —
*"Effortless heavy"* · *"Grip that never fails"* · *"The suit that isn't there"* ·
S19 🔴: *"performs extreme mountaineering for 3 minutes but maintains the exact same
resting baseline"*. **③ SES** S05 (*sakin ses ↔ serbest tırmanış*).
**Geometri** S03 (taban kapağı telin içinden geçiyor). **Artefakt** S16 (dikey çizgi).

## 🅒 BULGU DÜŞER · 2

S24 🔴 ×2: *"'THE STANDING WIRE' text baked onto screen"* — **kapanış başlık
kartıdır**, tipografi post-prodüksiyondadır, promptun kapsamı dışındadır.
(⚠️ Ama kartın makaraya girmesi ⑨/④'ün işidir; ① onu "negatif ihlali" sayamaz.)

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEK YAMALI. temas 11/25 · parçacık 10/25 · giysi 16/25 — bulguların
   yarısı tam olarak cümlenin DÜŞTÜĞÜ sahnelerde.
2. FİLMİN NOVUMU ÖLÇÜSÜZ. Tel filmi; telin kalınlığı hiçbir promptta sayıyla yok.
3. YEDİ EFOR BULGUSU, KİLİT 22/25'TE YAZILI. Cümle var, oran düşüşü yok.
```
