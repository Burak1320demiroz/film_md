# 🧩 THE_AMBER_LATTICE — prompt hata analizi

```
FORMAT      yatay 2 dk · 10 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   12/12 geçerli · BULGU 19 → tekil 18
HÜKÜM       🅐 3 · 🅑 13 · 🅒 1 · 🅓 1      🅑/(🅐+🅑) = %81
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 10/10: metin · filigran
  KISMİ: efor 1/10 · g-ad 2/10 · g-sayı 2/10
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi · parçacık · bloom · kamera
  bulgulu sahnelerde eksik: SES 0/7 · dış-ses 0/7 · sayı 0/7 · temas 0/7 · giysi 0/7 · parçacık 0/7 · bloom 0/7 · efor 1/7 · g-ad 2/7 · g-sayı 1/7 · kamera 0/7
```

> ⛔ **Çekirdeğin on üç cümlesinden ikisi tam.** Ses · insan sayısı · temas ·
> giysi · parçacık · bloom · kamera hiçbir promptta yok; ortam adı ve sayısı
> 10 sahnenin yalnız 2'sinde.

---

## 🅑 SINIF 1 — GÖK VE MEKÂN AYNI FİLMDE İKİ KEZ DEĞİŞİYOR · 4 🟠 ⭐ en ağır

| S | bulgu |
|:--:|---|
| S07 | *Overcast blue-grey daylight cloud deck in S6 vs deep night sky with stars and nebulae in S7* |
| S07 | *Daytime sky in S8 vs starry night sky overhead in S10* |
| S08 | *Deep starry night sky in S7 vs bright daytime sky behind the boots in S8* |
| S07 | *Open flat plain with distant peaks vs high vertical canyon cliff walls* |

**Promptta ne yazıyordu:** dünya çapası cümlesi yok [D209]. Gökyüzü her sahnede
sıfırdan tarif edilmiş; ışık takvimi de yok [D193]. On sahnelik bir filmde gökyüzü
**üç kez** gece ile gündüz arasında gidip gelmiş.

**Hüküm 🅑 ×4.** Yazım kuralı: dünya cümlesi (gök · ufuk · ışık kaynağı) film
başına bir kez yazılır ve **her dış sahneye birebir** girer.

## 🅑 SINIF 2 — EFOR 1/10 · 4 🟠

S02 · S03 · S09 ×2 (*"High-energy explosion occurs near the feet, but body posture
remains identically unbothered"*).

## 🅑 SINIF 3 — PARÇACIK 0/10 · 2 🟠 · 🅑 SINIF 4 — TEMAS 0/10 · 2 (1 🔴)

S08 ×2 (*"Floating rocks lack physical momentum, hanging statically"*) ·
S03 🔴 (*"Hand geometry fuses directly into the scanner casing"*) ·
S09 (*"Right hand holding the emitter shows phantom digits"*).

## 🅑 SINIF 5 — AKSİYONUN SONUCU KADRAJ DIŞINDA · 2 🟠 [D213]

S04 🔴 ⑦ (*"Whether the astronaut's hand successfully grabbed the panel handle
before the edit cut"*) · S08 ⑦ (*"Whether the drifting tether end was secured or
missed"* — Stakes Object Off-Screen).

---

## 🅐 MODEL SAPMASI · 3

S03 🔴 ×2 (*"Burned-in text on the scanner display"* · *"AI-generated text/symbols
appear on the screen"*) — metin yasağı 10/10'da **yazılı**. ⚠️ Altındaki sebep
tasarım: sahnede bir **tarayıcı ekranı** var ve ne göstereceği yazılmamış.
S06 (*vizör içi yansıma baş hareketinden bağımsız*) — bloom/kamera cümlesi yok,
ama yansıma fiziği ayrı bir eksen.

## 🅒 BULGU DÜŞER · 1

S07 ⑤ (*açık ova ↔ dik kanyon*) — iki ayrı mekân; sahne haritasında geçiş var.
⚠️ Gökyüzü bulguları düşmez: aynı sahnede gece/gündüz çelişkisi meşru değildir.

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEĞİN 8/10 CÜMLESİ YOK. 🅑 oranı %81 — deponun en yükseği.
2. GÖKYÜZÜ ÜÇ KEZ GECE-GÜNDÜZ ARASINDA GİTTİ GELDİ. Dünya çapası cümlesi yok.
3. EKRAN VAR, NE GÖSTERDİĞİ YOK. Metin yasağı yazılı, tarayıcı ekranı boş
   bırakılmış; motor doldurdu.
```
