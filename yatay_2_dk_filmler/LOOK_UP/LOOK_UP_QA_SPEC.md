# 📋 LOOK_UP — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              LOOK_UP
FORMAT:            yatay 16:9
RUNTIME:           120 seconds (title card: none — screen text lock 0 s)
SCENE COUNT:       12
PART GRID:         —
THEME:             Birbirini bırakmamak, hayatta kalma ihtimalini ortak bir sorumluluğa dönüştürür.
THEME SCENES:      S01 · S07 · S09 · S10 · S11
INTENDED EMOTION:  Claustrophobic tension, suspense, heroic rescue payoff, haunting cliffhanger
ENDING TYPE:       Cliffhanger (Threat clinging to cabin roof)
PROTAGONIST:       H1 (station commander)
CENTRAL CHOICE:    S07 (Mara leaves open escape route to rescue stranded Noah)
DIALOGUE LINES:    12 lines · register: HUMAN 12 / MACHINE 0
SILENT SCENES:     S01 (00:00-00:05 sound effects only before first dialogue)
VIRAL INTERSTITIALS: none
TITLE:             They Guarded the Door. The Ceiling Opened. | LOOK UP
LIBRARY CONTEXT:   THE_LAST_SHIFT, THE_HOLLOW_COUNT
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12
SHOT COUNT:      17 · sahne içi kesme: S01 (2), S03 (2), S08 (2), S09 (2), S12 (2)
TARGET ASL BAND: 7.0 s   ASL CURVE: Constant 10s per scene block (17 shots total)
                 Gerekçe: 120s runtime fixed across 12 equal 10-second scene blocks.
GRID:            sahne başlangıcı(n) = (n−1) × 10.0 s
RUNTIME:         120 s
RAW FOOTAGE:     12 clips · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          35mm / 28mm / 50mm / 65mm lockoff / panning
SETUP SEQUENCE:  A B C D D E F F G D E H
KURULUM İSKELETİ: A B C D D E F F G D E H
KÜME:            S04-S05 (D), S07-S08 (F)
DÖNÜŞ:           %17 (S10 returns to D, S11 returns to E)
ANGLE ARC:       5 (Eye-level, Low-angle, High-angle, Elevated 3/4, Close-up detail)
DORUK:           S09-S10 → Hat kesme, kalkan devri ve kapının kapatılması (sahne başlangıcı 80 s / 90 s)

REPLİK ZAMANLARI:
   S01: 00:05s (Noah)
   S02: 00:14s (Mara)
   S03: 00:22s (Mara)
   S04: 00:36s (Mara)
   S05: 00:44s (Cole)
   S06: 00:57s (Noah)
   S07: 01:05s (Mara)
   S08: 01:14s (Mara)
   S09: 01:27s (Eren)
   S10: 01:34s (Mara)
   S11: 01:47s (Noah)
   S12: 01:52s (Mara)

FİNAL VURUŞ KANITI:
   Creature C10 (with faint gray shoulder scratch) · 116.0 s · 1 creature · BULUNAN
DÖNGÜ KANITI: S01A (Tavandan tehdit fark etme) ↔ S12A (Tavandan tıkırtı duyuş ve yukarı bakış) — kafiye bağlantısı
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi

```
PLAN:  111111111111 (12/12 sahnede insan var)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         5 (Mara, Cole, Jun, Eren, Noah)
KASK          Tüm insanlarda yuvarlatılmış kask, berrak vizör (yüz görünür), sırt ünitesi tasmadan kalçaya tek düz panel (D79)
NOVUM         Basınçlı istasyonda mikro yerçekiminde tavandan gelen yaratık kuşatmasında emniyet hatlarıyla asansörü savunmak
YERÇEKİMİ     0 g (mikro yerçekimi)
ATMOSFER      Basınçlı istasyon iç havası (dekompresyon yok)
EKRAN YÖNÜ    Asansör ekran sağında, yanlış kapı ekran solunda (10/12 sahnede sabit soldan sağa ilerleyiş)
SAYAÇ         yok
EŞ KADRAJ     S01A↔S12A (Mara yakın bakış), S04↔S10 (Asansör kapı önü savunması)
DÜNYA ÇAPASI  3/3 — Yanlış kapı (Batı) · Tahliye asansörü (Doğu) · Servis tavan ızgarası (Orta-Batı)
YIPRANMA      5 sabit giysi/kalkan/bot hasar bölgesi (Cole sağ bot, Noah omuz/kalkan ezik, Mara sol kol çizik, kalkan oluk)
KİMLİK DİZİSİ Kask şeritleri: Mara (1 beyaz dikey), Noah (2 hardal sarısı çapraz), Cole (geniş grafit omuz zırhı), Jun (sağ ön kol alet modülü), Eren (göğüs kare makara kutusu)
IŞIK TAKVİMİ  Sabit nötr beyaz çalışma ışığı + arka plan kırmızı acil lambası
SES REGISTER  HUMAN 12 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI

```
KAPI          Kamera roll olmadığını ve kadraj yönünü denetleme
KOMUT         ffprobe -v error -show_entries stream=width,height yatay_2_dk_filmler/LOOK_UP/LOOK_UP_BOLUM_1.md
DOĞRULANDI    ffmpeg 6.0 · 2026-09-14
İKAME         Manuel kadraj denetimi
```
