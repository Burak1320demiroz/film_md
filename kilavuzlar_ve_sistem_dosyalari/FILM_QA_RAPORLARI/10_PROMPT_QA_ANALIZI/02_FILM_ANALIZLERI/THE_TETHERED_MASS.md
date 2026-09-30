# 🧩 THE_TETHERED_MASS — prompt hata analizi

```
FORMAT      yatay 2 dk · 16 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   12/12 geçerli · BULGU 22 → tekil 22
HÜKÜM       🅐 6 · 🅑 14 · 🅒 1 · 🅓 1      🅑/(🅐+🅑) = %70
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 16/16: parçacık · metin · filigran
  KISMİ: efor 1/16 · g-ad 2/16
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi · bloom · g-sayı · kamera
  bulgulu sahnelerde eksik: SES 0/11 · dış-ses 0/11 · sayı 0/11 · temas 0/11 · giysi 0/11 · bloom 0/11 · efor 1/11 · g-ad 1/11 · g-sayı 0/11 · kamera 0/11
```

> ⚠️ Çekirdeğin **altı cümlesi hiç yok**. Bu film, "negatif çekirdek nedir"
> sorusunun ters örneğidir: üç cümle 16/16, altı cümle 0/16.

---

## 🅑 SINIF 1 — BLOOM CÜMLESİ 0/16 · 2 🟠

S06 (*"Soft AI bloom haze surrounds the orange atmospheric horizon"*) ·
S08 (*"Engine nozzle interior displays diffuse glowing fog rather than sharp
thermal radiation falloff"*). `0% bloom` kalıbı hiçbir promptta yok.

## 🅑 SINIF 2 — VAKUM DAVRANIŞI YAZILMAMIŞ · 3 🟠

S04 (*"Thruster plume forms expanding cloud billows in space vacuum"*) ·
S08 ×2 (*"Main engine nozzle vents thick billowing steam in vacuum"* · *"Exhaust
particles vanish abruptly without continuous decay paths"*). Parçacık cümlesi
16/16'da var ama **ortam vakumu neredeyse hiç adlandırılmamış** (ad 2/16, sayı 0/16).

## 🅑 SINIF 3 — TEMAS SINIRI 0/16 · 2 (1 🔴)

S12 🔴 (*"Shattered glass shards morph, melt and reshape between frames"*) ·
S12 (*"Glove mesh deforms and merges into the red control lever casing"*).

## 🅑 SINIF 4 — KİMLİK/GİYSİ 0/16 · 2 🟠

S03 (*"Facial bone structure warps around jaw and mouth during high-g grimace"*) ·
S10 (*"Subject wears a heavy multi-layer pressurised suit with zero mobility effort
in S1–S21, then switches to …"*).

## 🅑 SINIF 5 — EFOR VE BEDEL 1/16 · 3 🟠

S09 (*"Standing in an expanding reactor blast — no defensive crouch, no backward
momentum"*) · S10 ×2 (*"absorbs the full reactor explosion yet appears unblemished"* ·
*"sustained walking with no chest breathing, no posture slackening"*).

## 🅑 SINIF 6 — ÖLÇÜ VE ORTAM GEÇİŞİ · 2 🟠 [D138]

S13 ⑥ (*"Blast door height measures 3,2 m in L3 and 5,4 m in L12"*) ·
S10 ⑤ (*"Snow-covered mountain ridge abruptly replaced by flat pine forest basin"*).

---

## 🅐 MODEL SAPMASI · 6

**Parçacık** S01 · S02 · S12 ⑥ (*"Falling sparks maintain a constant 2,08 m/s across
1,2 s instead of accelerating"*) — parçacık cümlesi 16/16'da yazılı.
**Ekrana yazı** S11 (*"Cockpit UI shows garbled AI pseudo-text"*) — metin yasağı
16/16'da. **Doku yüzmesi** S02 ×2.

## 🅒 BULGU DÜŞER · 1

S09 ⑦ (*"Whether the nozzle venting was a thruster pulse or a mechanical failure"*)
— belirsizlik **olayın kendisi**; sahne haritası bunu soru olarak kuruyor.

## 🎯 ÜÇ SATIR

```
1. ÇEKİRDEĞİN ALTI CÜMLESİ HİÇ YOK. 14 🅑'nin 11'i doğrudan bu altı boşluktan.
2. VAKUM ADLANDIRILMAMIŞ. Parçacık cümlesi var, hangi ortamda davranacağı yok —
   "the stated gravity" tuzağının ikinci biçimi.
3. EFOR 1/16. Reaktör patlamasını üstüne alıp çizilmeden yürüyor.
```
