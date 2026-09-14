# 📋 THE_TETHERED_MASS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_TETHERED_MASS
FORMAT:            yatay 2-4 dk (16:9)
RUNTIME:           160.0 seconds (title card: 0.0s)
SCENE COUNT:       16
THEME:             BEDEL
THEME SCENES:      S00 · S06 · S11 · S13 · S15
INTENDED EMOTION:  Awe, tension, deep cosmic sacrifice, satisfaction
ENDING TYPE:       Loop Rhyme (S00 hook tether strand <-> S15 loop tether strand)
PROTAGONIST:       Unnamed female astronaut tug engineer
CENTRAL CHOICE:    S11 (Breaking acrylic glass, pulling manual override lever)
DIALOGUE LINES:    0 (Diyalogsuz narrative)
SILENT SCENES:     S00-S15
VIRAL INTERSTITIALS: S00, S02, S06, S07, S11, S13, S15
TITLE:             THE_TETHERED_MASS — Orbital momentum takası ve bedeli
LIBRARY CONTEXT:   THE_GRAVITY_ANCHOR, THE_HOLLOW_STATION, THE_COLD_WELD
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      16
SHOT COUNT:      16 (sahne içi kesme yok, locked off clips)
TARGET ASL BAND: 10.0s (sabit ızgara 10.0s)
GRID:            sahne başlangıcı(n) = 0.0s + (n−1) × 10.0s
RUNTIME:         160.0s (2:40)
RAW FOOTAGE:     160.0s · TRIM BUDGET: 0.0s
SCREEN TEXT:     0.0s
CAMERA:          24mm / 50mm / 85mm prime locked-off
SETUP SEQUENCE:  S00(50mm) S01(50mm) S02(85mm) S03(24mm) S04(85mm) S05(24mm) S06(50mm) S07(50mm) S08(50mm) S09(24mm) S10(50mm) S11(50mm) S12(85mm) S13(24mm) S14(50mm) S15(50mm)
KURULUM İSKELETİ: A A B C B C D E E C D A B C E A
KÜME:            5 (A, B, C, D, E)
DÖNÜŞ:           9/16 (%56.25)
ANGLE ARC:       3 (Low-angle, Eye-level, High-angle)
DORUK:           S13 → 130.0s (sahne başlangıcı 130.0s)

REPLİK ZAMANLARI: N/A (Diyalogsuz)

FİNAL VURUŞ KANITI [D141]:
   Serbest kalan metal halat ucu · 155.0 saniye · 1 adet · BULUNAN nesne

DÖNGÜ KANITI: S00 ilk kare gergin halat lifi <-> S15 son kare serbest dönen kopmuş halat lifi ucu (Kafiye döngüsü)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  - - 1 - 1 - - - - - 1 1 1 - - -     (1 = astronot var · - = insansız uzay/mekan)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
① KASK VİZÖR OPASİTESİ: %100 transparent clear glass (D197)
② VAKUM FİZİĞİ: Kıvılcım yok, alev yok, mikro ark yok (D198, MÇ Red)
③ SIFIR-G MOMENTUM TAKASI: Halat lifi gerilim dalgası ve ivmelenme zıtlığı (D200)
④ BEDEN EYLEMİ: S11'de akrilik cam kırma ve manuel kol çekme (D202)
⑤ GÜNEŞ IŞIĞI SABİTLİĞİ: Sol üst 45 derece orbital kaynak (D201)
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI

```
KOMUT: ffmpeg -hide_banner -i input.mp4 -vf "select=gte(n\,0)" -frames:v 1 frame0.jpg
DOĞRULANDI: ffmpeg 6.1 · 10.09.2026
İKAME: python script dry run
```
