# 📋 KRONOS_SON_SINYAL — QA SPEC (rubriklere yapıştırılacak tek dosya)

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              KRONOS_SON_SINYAL
FORMAT:            yatay 8 dk
RUNTIME:           480 seconds (title card: no — screen text lock 0 s)
SCENE COUNT:       48
PART GRID:         B1 = S01-S24 · 24 clips · 0-240 s · B2 = S25-S48 · 24 clips · 240-480 s
THEME:             ZAMAN
THEME SCENES:      S03 · S08 · S18 · S46
INTENDED EMOTION:  Tragic tension, awe, sacrifice and inevitability
ENDING TYPE:       Loop closure / Rhyme
PROTAGONIST:       Female space commander and male engineer
CENTRAL CHOICE:    Kestrel's decision to detach Module B to save habitat Module A · S41
DIALOGUE LINES:    8 · register: HUMAN 8 / MACHINE 0
SILENT SCENES:     S43 (vacuum space)
VIRAL INTERSTITIALS: S01 · S03 · S24 · S40 · S41 · S42 · S46 · S48
TITLE:             KRONOS: SON SİNYAL — Gelecekten gelen acil durum mesajı ve zaman döngüsü
LIBRARY CONTEXT:   MARS_SON_CIKIS · THE_COLD_WELD
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ

```
CLIP COUNT:      48
SHOT COUNT:      48 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s   ASL CURVE: Sabit 10,000 saniye (240 kare)
GRID:            sahne başlangıcı(n) = (n−1) × 10 s
RUNTIME:         480 s
RAW FOOTAGE:     48 clips · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          35mm / 50mm / 65mm / 85mm sabit lockoff
SETUP SEQUENCE:  A B C B D B B C E B B D C B E F D B D B D B C D B D E D E B E E F E E D D E E D F E A D F B C A
KURULUM İSKELETİ: A B C B D B B C E B B D C B E F D B D B D B C D B D E D E B E E F E E D D E E D F E A D F B C A
KÜME:            5 küme (S06-S07, S10-S11, S21-S22, S31-S32, S36-S37)
DÖNÜŞ:           %52 (25 dönüş hareketi)
ANGLE ARC:       5 (Wide, Medium, Close-up, Macro, Over-shoulder)
DORUK:           S32 → Aras'ın sarı mekanik kolu çekmesi (05:10 s)

FİNAL VURUŞ KANITI: S48 · 07:50 s · 1 adet (Modül B'siz tek başına yörüngede dönen Modül A)
DÖNGÜ KANITI: S01 ↔ S48 — aynı kamera geometrisi ve 35mm wide açısı (değişen tek şey: B modülü eksiktir)
```

### 🧬 İNSAN ŞERİDİ

```
PLAN:  1 1 1 1 1 1 1 1 - 1 1 1 1 1 - 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 - 1 1 1 - 1 1 - - 1 1 1 1 -
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         Kestrel & Aras (2 astronot)
KASK          180 derece şeffaf polikarbon dome · vizör optik berrak · sırt ünitesi YOK — düz siluet
NOVUM         Deneysel dış röle R'nin canlı sesi 480 saniye geriye düşürmesi
YERÇEKİMİ     0 g (mikro yerçekimi)
ATMOSFER      Vakum (dış mekan) / Pressurized cabin (iç mekan)
EKRAN YÖNÜ    ilerleme "toward A" / "toward B" · 48 sahnenin 48'inde nesnel yön kilitli
SAYAÇ         Alıcı saati 12:00:30 → 12:08:30 (monotonik)
EŞ KADRAJ     S01 ↔ S48
DÜNYA ÇAPASI  Dünya yörüngesi ufku kadraj alt sağında sabit (World Bible ile birebir)
YIPRANMA      Sabit 2 aşınma bölgesi (kask kenarı, eldiven dikişi)
KİMLİK DİZİSİ Kestrel (petrol mavisi omuz) / Aras (turuncu omuz + sakal)
IŞIK TAKVİMİ  Monotonik (A nötr gri / B amber-kırmızı)
SES REGISTER  HUMAN 8 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI

```
KAPI          Sabit Kamera Lockoff Testi
KOMUT         ffmpeg -i <clip.mp4> -vf vidstabdetect -f null -
DOĞRULANDI    ffmpeg v6.1 · 15.09.2026
İKAME         Manuel kurgucu kare bazlı karşılaştırma
```
