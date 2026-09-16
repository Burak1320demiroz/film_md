# 📋 MARS_SON_CIKIS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline rubrikle birlikte BU dosya verilir.

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              MARS_SON_CIKIS
FORMAT:            16:9 yatay 6dk
RUNTIME:           360 seconds (title card: none — screen text lock 0 s)
SCENE COUNT:       36
PART GRID:         PART 1 = S01-S12 · 12 clips · 0-120 s · PART 2 = S13-S24 · 12 clips · 120-240 s · PART 3 = S25-S36 · 12 clips · 240-360 s
THEME:             Tamamlayıcı Eylem ve Güven
THEME SCENES:      S01 · S14 · S24 · S31 · S36
INTENDED EMOTION:  Gerilim, Dayanışma, Rahatlama
ENDING TYPE:       KAFİYE FINAL
PROTAGONIST:       Lena (Pilot) & Aras (Mühendis)
CENTRAL CHOICE:    Manuel kenetlenmeye geçiş (S24)
DIALOGUE LINES:    7 · register: HUMAN 7 / MACHINE 0
SILENT SCENES:     29
VIRAL INTERSTITIALS: S01 · S02 · S05 · S08 · S10 · S11 · S13 · S14 · S15 · S17 · S18 · S20 · S21 · S23 · S26 · S28 · S29 · S30 · S31 · S32 · S33 · S36
TITLE:             MARS: SON ÇIKIŞ — LAST EXIT
LIBRARY CONTEXT:   Fiziksel hayatta kalma gerilim serisi
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      36
SHOT COUNT:      36 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s   ASL CURVE: Sabit 10,0 s kurgu ritmi
GRID:            sahne başlangıcı(n) = 00:00 + (n−1) × 10,0 s
RUNTIME:         360 s
RAW FOOTAGE:     36 clips · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          28mm / 35mm / 50mm sabit planlar
SETUP SEQUENCE:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z AA AB AC AD AE AF AG AH AI AJ
KÜME:            3 küme · S01-S02, S15-S16, S29-S30
DÖNÜŞ:           %42
ANGLE ARC:       3 açı TİPİ (Göz seviyesi, Alttan geniş, Üstten yakın)
DORUK:           S31 → Lever kilitlenme teması (05:15 s)

REPLİK ZAMANLARI:
  S01: 00:03 s (Lena)
  S02: 00:15 s (Aras)
  S13: 02:05 s (Lena)
  S23: 03:45 s (Aras)
  S24: 03:53 s (Lena)
  S28: 04:35 s (Aras)
  S31: 05:15 s (Lena)

FİNAL VURUŞ KANITI [D141]:
  Kenetlenme halkası ve kilit leveri · 05:15 saniye · 1 adet · BULUNAN

DÖNGÜ KANITI: S01 kasa frenleme pimi ↔ S31 kenetlenme leveri
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111111111111111111111111111111111
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         2 (Lena & Aras)
KASK          Vizör optik berrak · sırt ünitesi YOK — düz siluet [D79]
NOVUM         Otomatik navigasyon kaybında manuel kenetlenme mekanizması
YERÇEKİMİ     Yüzeyde 0.38g / Yörüngede 0.00g
ATMOSFER      Yüzeyde 610 Pa CO2 / Yörüngede vakum
EKRAN YÖNÜ    Kestrel burnu hep Horizon portuna bakıyor (S21-S32)
SAYAÇ         Fırtına Doz Gösterge Işığı (Yeşil -> Turuncu -> Kırmızı -> Mavi)
EŞ KADRAJ     S01↔S31
DÜNYA ÇAPASI  3/3 — Kızıl Mars ufku · Kestrel gövdesi · Horizon omurgası
YIPRANMA      S01 Mars tozu + S14 yangın isi (S15-S36 boyu)
KİMLİK DİZİSİ Lena (Petrol Mavi) / Aras (Oksit Turuncu + Sol Kol Askısı S14-S36)
IŞIK TAKVİMİ  Monotonik (Gündüz -> Acil Kırmızı -> Kokpit Mavi -> Sığınak Yumuşak Beyaz)
SES REGISTER  HUMAN 7 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142]

```
KAPI          Kamera Sabitliği Kapısı
KOMUT         ffmpeg -i scene.mp4 -vf vidstabdetect -f null -
DOĞRULANDI    ffmpeg 7.0 · 15.09.2026
İKAME         Manuel kare incelemesi
```
