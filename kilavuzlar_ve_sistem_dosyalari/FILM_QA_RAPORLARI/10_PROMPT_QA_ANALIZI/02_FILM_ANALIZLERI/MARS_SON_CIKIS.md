# 🧩 MARS_SON_CIKIS — prompt hata analizi

```
FORMAT      yatay 6 dk · 36 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   30/30 geçerli · BULGU 36 → tekil 36
HÜKÜM       🅐 12 · 🅑 21 · 🅒 2 · 🅓 1      🅑/(🅐+🅑) = %64
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 36/36: parçacık · bloom · metin · filigran · kamera
  KISMİ: efor 8/36 · g-ad 3/36 · g-sayı 1/36
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi
  bulgulu sahnelerde eksik: SES 0/16 · dış-ses 0/16 · sayı 0/16 · temas 0/16 · giysi 0/16 · efor 3/16 · g-ad 1/16 · g-sayı 1/16
```

> ⚠️ **BÖLÜM OFSETİ DÜZELTMESİ · 19.09.2026** — bu filmin QA'sı BÖLÜM
> birimiyle koşuldu ve ikinci yarımın masterı 0:00'dan başlıyor. İlk eşlemede
> o bulgular birinci yarının sahnelerine yazılmıştı; betiğe ofset eklendi ve
> **21 bulgunun sahne numarası değişti**. Sınıflar, sayılar ve hükümler AYNI;
> aşağıdaki prose ikinci-yarım bulgularında **düzeltme öncesi** numaraları
> taşıyabilir. ⛔ Kesin sahne numarası için [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md)
> (makine yazar, ofsetli) hakemdir.

> ⭐ **Yarım negatif çekirdek.** Bu film çekirdeğin ÜST yarısını (parçacık · bloom ·
> metin · filigran · kamera) her promptta taşıyor, ALT yarısını (insan sayısı ·
> temas · giysi · ses) hiç taşımıyor. Bulgu dağılımı bu bölünmeyi birebir izliyor.

---

## 🅑 SINIF 1 — GİYSİ VE DONANIM DEVAMLILIĞI CÜMLESİ YOK · 4 🔴 · 4 🟠  ⭐ en ağır

| S | bulgu |
|:--:|---|
| S15 🔴 | *Suit wardrobe drifts from standard white suit to blue chest paneling mid-sequence* |
| S15 🔴 | *In S16 helmets are sealed; in S17 carried in hand; in S18 re-sealed* |
| S18 🔴 | *In S2/S5/S16/S18 sling is on RIGHT arm; in S20 sling is on LEFT arm* |
| S09 🟠 | *Orange shoulder patch on left arm in S1 flips to right arm in S9* |
| S15 🟠 | *Sooted suit from hatch escape resets to clean suit during surface run* |
| S15 🟠 | *Plain tan suit → dark blue chest armor → plain tan again* |
| S15 🔴 | *Copilot suit shifts colour scheme to blue torso accents before reverting* |

**Promptta ne yazıyordu:** hiçbir şey. `identical` / `no drift` kalıbı **36 promptun
hiçbirinde yok**; askı (sling), omuz yaması ve is/kir durumu hiçbir promptta
durum merdiveni taşımıyor.

**Hüküm 🅑 ×7.** Yazım kuralı: giysi cümlesi Bible'dan **birebir** kopyalanır;
asimetrik her işaret (yama · askı) **hangi kolda olduğuyla** yazılır; kir/is bir
**durum merdivenidir** (PHASE n) ve geri sayılmaz.

## 🅑 SINIF 2 — SES KİLİDİ YOK · 2 🔴

S01 🔴 ×2: *"Unfiltered airborne voiceover played over vacuum exterior without suit
radio acoustic processing"*. `AUDIO:` satırı 0/36; telsiz band-pass hiçbir promptta
yazılı değil.

## 🅑 SINIF 3 — TEMAS SINIRI YOK · 3 🟠

S01 ×2 (*"Glove structure morphs and phases into metal lever handle"*) ·
S10 (*"Extinguisher foam clips through metal floor lattice"*). Temas cümlesi 0/36.

## 🅑 SINIF 4 — ORTAM DEVAMLILIĞI VE GEÇİŞ · 3 🔴 · 3 🟠

S08 🔴 (yuvarlak kenetleme portu → dikdörtgen pim bileziği) · S12 🔴 (kelepçesiz
bilezik → dört eklemli mekanik kol) · S13 🔴 (temiz koridor → dar yanan kapak) ·
S15 🔴 (iç koridor → dış yüzey koşusu, hava kilidi döngüsü yok) · S16 · S18
(alçak Dünya yörüngesi → derin uzayda Mars diski). Mekân geçişleri promptta yok.

## 🅑 SINIF 5 — YERÇEKİMİ · 2 🟠

S04 (*"Liquid water stream flows with standard 1G Earth pour rate"*) ·
S08 (*"RCS thruster plume expands like dense atmospheric vapour in hard vacuum"*).
Ortam ADI 3/36'da, ortam SAYISI 1/36'da yazılı — ikisi de yok sayılır.

---

## 🅐 MODEL SAPMASI · 12

### 🅐-1 · EKRANA YAZI · 4 🔴 ⭐ ama altında bir tasarım çelişkisi var

| S | bulgu |
|:--:|---|
| S05 🔴 | *On-screen computer HUD text graphics burned directly over video frame* |
| S13 🔴 | *Garbled AI text ("RESTRICGET FLTACK 7/") on emergency bulkhead door panel* |
| S17 🔴 | *Text labels ("RADIATION DOSIMETER") rendered on wall monitor prop* |
| S06 · S07 | *Visor HUD target graphic* · *Scope reticle overlay* |

Metin yasağı **bulgunun düştüğü sahnelerin hepsinde yazılı** (metin 36/36) →
tanım gereği 🅐. Ama altındaki sebep yazımda: filmde `screen · monitor · display ·
readout` **79 kez** geçiyor. Prompt aynı anda hem ekran istiyor hem yazı yasaklıyor;
motor çelişkiyi bulanık harfle çözüyor.

⭐ KRONOS'ta aynı çelişki **🅑** olarak çıkmıştı (orada metinsiz çözüm de yoktu).
Sınıf tablosunda tek satır, iki sahibiyle.

### 🅐-2 · PARÇACIK · 3 · 🅐-3 · BLOOM · 2 · 🅐-4 · diğer · 3

S01 (toz kamerayla sürükleniyor) · S11 ×2 (meşale alevi tutamaktan ayrı duruyor) —
parçacık cümlesi 36/36. S01 · S05 bloom — 36/36.

## 🅒 BULGU DÜŞER · 2

S13 ⑦ (*yangın kapısının gövdeye temas noktası kapı çerçevesi altında perdeleniyor*)
— **perdeleme bir kadraj kararıdır**, politika gereği bilinçlidir. S14 (kapı S13'te
tam kapanıp S14'te kısmen açılıyor) — olay bu; sahne haritasında yazılı.

---

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEĞİN ALT YARISI HİÇ YOK. insan sayısı 0/36 · temas 0/36 · giysi 0/36 ·
   ses 0/36. 21 🅑'nin 14'ü doğrudan bu dört eksik cümleden.
2. ASİMETRİK İŞARET AYNALANIYOR. Askı ve omuz yaması kol değiştiriyor — hangi
   kolda olduğu hiçbir promptta yazmıyor. İki 🔴.
3. EKRAN İSTEYİP YAZI YASAKLAMAK. 79 ekran, mutlak metin yasağı, dört 🔴.
   Ya sayaç metinsiz çözülür ya yasak o sahnede kalkar.
```
