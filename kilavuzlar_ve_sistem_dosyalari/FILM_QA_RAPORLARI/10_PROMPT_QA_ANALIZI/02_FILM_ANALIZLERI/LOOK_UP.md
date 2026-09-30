# 🧩 LOOK_UP — prompt hata analizi

```
FORMAT      yatay 2 dk · 12 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   12/12 geçerli · BULGU 37 → tekil 37
HÜKÜM       🅐 23 · 🅑 11 · 🅒 2 · 🅓 1      🅑/(🅐+🅑) = %32
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 12/12: sayı · temas · giysi · parçacık · bloom · metin · filigran · kamera
  KISMİ: efor 7/12 · g-ad 11/12
  ⛔ HİÇ YOK: SES · dış-ses · g-sayı
  bulgulu sahnelerde eksik: SES 0/12 · dış-ses 0/12 · efor 7/12 · g-ad 11/12 · g-sayı 0/12
```

> ⭐ Bu film **yaratıklı** — deponun canlı içeren az sayıda filminden biri.
> 37 bulgunun 11'i doğrudan canlı-insan temasında.

---

## 🅑 SINIF 1 — YERÇEKİMİ TARİFLE, ÜSTELİK İKİ REJİM AYNI KADRAJA GİRİYOR · 3 🔴

| S | bulgu |
|:--:|---|
| S02 🔴 | *Crew members float while others walk upright on the floor without magnetic boot indicators* |
| S02 🔴 | *Inconsistent gravity vectors with simultaneous zero-g floating and grounded walking* |
| S04 🔴 | Alien ceiling drop implies **g ≈ 1,73 m/s²**, debris drop **g ≈ 6,67 m/s²** — aynı güvertede |
| S09 🔴 | *Sudden shift between zero-g floating and heavy running without environmental trigger* |

**Promptta ne yazıyordu:** `gravity`, `gravity drift obeyed`, `gravity momentum` —
üç ifade de **sıfat**, sayı yok. Modül içinde kimin yürüdüğü kimin yüzdüğü
hiçbir promptta yazılı değil.

**Hüküm 🅑 ×4.** Yazım kuralı: ⛔ **iki yerçekimi rejimi aynı kadraja giremez**
[D200]. Giriyorsa ayıran şey (manyetik bot · el tutamağı · kemer) **kadrajda ve
promptta** olmak zorundadır.

## 🅑 SINIF 2 — SES KİLİDİ YOK · 1 🟠 (⑧ ile birlikte)

`AUDIO:` satırı 0/12. S02 🔴 ⑭ *"He shoots his weapon at the corridor wall — I do
not know why; nothing is there"* ve S02 🟠 *"Muzzle flash lacks dynamic directional
light casting"* — silah sesi/ışığı hiçbir promptta yazılı değil.

## 🅑 SINIF 3 — CANLI-İNSAN TEMASI KİMİN KURALINA TABİ, YAZILMAMIŞ · 4 (3 🔴)

| S | bulgu |
|:--:|---|
| S01 🔴 | *Alien limbs slide across ceiling grating without physical contact points* |
| S05 🔴 | *Creature geometry clipping through astronaut torso armor and helmet collar* |
| S05 🔴 | *Alien limb clips through suit shoulder plate* |
| S05 🟠 | *Point of impact and physical grab when alien drops onto operator's back* — ④ ELLIPSIS |

**Promptta ne yazıyordu:** temas cümlesi 12/12'de var **ama yalnız EL için**:
`no merging, no hand-surface fusion`. Canlının **uzuvlarının** insana teması
hiçbir promptta kurala bağlanmamış.

**Hüküm 🅑 ×4.** Yazım kuralı: canlı içeren filmde temas cümlesi **iki yönlüdür** —
elden yüzeye VE canlıdan gövdeye.

## 🅑 SINIF 4 — TUTMA/KAVRAMA ÇAPASIZ · 3 🔴🟠 · 🅑 SINIF 5 — YARATIK TASARIMI KİLİTLİ DEĞİL · 1

S04 ⑭ MISGRIP (*"gloved hand passes through the metal handle"*) · S05 ⑭ PHANTOM
(*"hands close on empty air 10 cm away"*) · S06 ⑭ SPIN (*"rotates 180° — no wall
push caused it"*): tutulan nesnenin **hangi elle ve nereden** tutulduğu yazılmamış.
S11 🟠: *"Black Xenomorph in S3 changes to pale fleshy mutant in S16"* — yaratığın
görünüşü sahne sahne yeniden tarif edilmiş, kilidi yok (BENI_HATIRLAMA'da bu kilit
YAZILMIŞTI ve yine tutmadı → sınıf tablosunda ikisi ayrı satır).

---

## 🅐 MODEL SAPMASI · 23

**Temas/el füzyonu** S05 🔴 ×2 (`no merging, no extra fingers` 12/12'de yazılı) ·
**kimlik** S01 kask şeridi, S02 kask kubbesi, S10 yüz yapısı, S10 kol çiziklerinin
kaybolması (giysi kilidi 12/12) · **parçacık** S04 · S06 · S09 (parçacık cümlesi
12/12) · **bloom** S07 · **doku yüzmesi** S01 · S03 · S07 · **⑧ EFOR** S01 · S06 ·
S08 🔴 · S09 🔴 (*"THE SUIT THAT ISN'T THERE"*, *"EFFORTLESS HEAVY"*) — efor
cümlesi 7/12'de var, dördünün üçünde yazılıydı.

## 🅒 BULGU DÜŞER · 2

S12 🔴 *"Burned-in text graphic 'LOOK UP' on promotional title card frame"* — bu bir
**başlık kartıdır**, sahne değil; tipografi post-prodüksiyondadır ve promptun
kapsamı dışındadır. S03 🔴 *"Duplicate background crew member spawns near door
frame"* — ⚠️ bu 🅐'dır (`exactly N human` 12/12), ayrıca sayılmıştır.

---

## 🎯 ÜÇ SATIR

```
1. İKİ YERÇEKİMİ AYNI KADRAJDA. Üç 🔴 buradan; ayıran işaret ne kadrajda ne promptta.
2. TEMAS CÜMLESİ TEK YÖNLÜ. Elden yüzeye yazılmış, canlıdan gövdeye yazılmamış —
   üç 🔴 canlının insana geçmesinden.
3. SES HİÇ YOK. 12 promptta AUDIO satırı sıfır; silahın sesi de ışığı da yazılmamış.
```
