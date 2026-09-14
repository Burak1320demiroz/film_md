# 📋 THE_SILENT_PERIHELION — QA SPEC

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline rubrikle birlikte BU dosya verilir.

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:               THE_SILENT_PERIHELION
FORMAT:             yatay_2_dk_filmler (16:9)
RUNTIME:            160 seconds (title card: 40 — screen text lock 0 s)
SCENE COUNT:        12
THEME:              Bilginin bedeli nesnenin büyüklüğüyle değil, gözlemcinin kırılganlığıyla ölçülür.
THEME SCENES:       S00 · S05 · S11
INTENDED EMOTION:   Huşu ve yalnızlık
ENDING TYPE:        Kapanış kafiyesi / mutlak kararma
PROTAGONIST:        Keşif Astronotu (Kael)
CENTRAL CHOICE:     S05
DIALOGUE LINES:     0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:      S00-S11
VIRAL INTERSTITIALS: S08
TITLE:              THE SILENT PERIHELION
LIBRARY CONTEXT:    THE_SOLAR_MIRROR · THE_HOLLOW_STATION
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ

```
CLIP COUNT:      12
SHOT COUNT:      12 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s   ASL CURVE: Linear
GRID:            sahne başlangıcı(n) = 0 hook + (n−1) × 10 klip
RUNTIME:         120 s klip + 40 s koda = 160 s
RAW FOOTAGE:     120 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          35mm anamorphic / 0 sabit lockoff
SETUP SEQUENCE:  S00(A), S01(A), S02(B), S03(C), S04(B), S05(C), S06(D), S07(D), S08(E), S09(D), S10(E), S11(D)
KURULUM İSKELETİ: A A B C B C D D E D E D
KÜME:            2 küme · S00-S01 (A A), S06-S07 (D D)
DÖNÜŞ:           %58 (7/12 dönüş)
ANGLE ARC:       5 açı TİPİ (EWS, MCU, MS, CU, ECU)
DORUK:           S08 → CME plasma yutumu (sahne başlangıcı 100 s)

FİNAL VURUŞ KANITI [D141]:
   Telemetry CRT ekranı · 150 saniye · 1 ekran · BULUNMAYAN ışık (OPTICAL RECORDING: ERROR metni kararıp zifiri karanlık kokpit kalır)

DÖNGÜ KANITI: ilk kare S00 Setup A kokpit EWS ↔ son kare S10 Setup A kokpit EWS kararma
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1-1-1-1-1-1-1-1--1-1-
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 karakter (Kael)
KASK          vizör optik berrak · sırt ünitesi YOK — düz siluet [D79]
NOVUM         CME plazmasını sıfır tepki ve sıfır ışıma ile yutan kadim perihelion mega-yapısı
YERÇEKİMİ     0 g
ATMOSFER      0 atm (vakum)
EKRAN YÖNÜ    hedef hep sağ üst · ilerleme sabit
SAYAÇ         yok
EŞ KADRAJ     S00↔S10
YIPRANMA      kuvars cam çatlağı (S07-S11)
IŞIK TAKVİMİ  monotonik kızıl artış → aniden kararma
SES REGISTER  HUMAN 0 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI

```
KAPI          Aspect ratio verification
KOMUT         ffmpeg -hide_banner -i video.mp4 -vf "cropdetect" -frames:v 100 -f null - 2>&1 | grep -q "crop=1920:1080"
DOĞRULANDI    ffmpeg 6.1.1 · 2026-09-13
İKAME         ffprobe -v error -select_streams v:0 -show_entries stream=width,height
```
