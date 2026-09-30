# 🧩 THE_RESONANT_STRAND — prompt hata analizi

```
FORMAT      yatay 2 dk · 14 sahne · ızgara sahne(n) = n × 8,9 s
HAM RAPOR   13/13 geçerli · BULGU 31 → tekil 31
HÜKÜM       🅐 6 · 🅑 20 · 🅒 3 · 🅓 2      🅑/(🅐+🅑) = %77
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 14/14: sayı · bloom · metin · filigran · kamera
  KISMİ: efor 5/14
  ⛔ HİÇ YOK: SES · dış-ses · temas · giysi · parçacık · g-ad · g-sayı
  bulgulu sahnelerde eksik: SES 0/10 · dış-ses 0/10 · temas 0/10 · giysi 0/10 · parçacık 0/10 · efor 4/10 · g-ad 0/10 · g-sayı 0/10
```

> ⚠️ ③ kimlik: 13/13 ham dosyada güçlü bayrak (`ad≠"THE RESONANT STRAND"` ·
> süre 144 s ∉ 124,6 s · sahne 11 ≠ 14). Sahne eşlemesi **±1 sahne** kabul edilir;
> sınıflar bundan etkilenmez, tek tek sahne iddiası edilmez.

---

## 🅑 SINIF 1 — EFOR VE BEDEL CÜMLESİ YOK · 3 🔴 · 5 🟠 ⭐ en ağır

| S | bulgu |
|:--:|---|
| S13 🔴 | *E1, E2, E3 complete absence of physical effort or recoil* |
| S13 🔴 | *E1, E3 suit gloves operate with zero mechanical stiffness* |
| S07 🔴 | *E2 flare gun held without recoil torque or hand tremor* |
| S00 | *Cost curve sits perpetually at zero despite exertions* |
| S07 | *E1, E2 walking gait and arm holding firearm display no suit weight* |
| S13 | *E1 to E3 physical state remains 100% rested across runtime* |
| S03 · S06 | *Figure retains rigid mannequin-like stance* · *Hands perform harness adjustments mechanically* |

**Promptta ne yazıyordu:** efor cümlesi **14 sahnenin 5'inde**; geri kalan 9'da
bedenin yükü hiç yazılmamış. Basınçlı eldivenin sertliği, silahın geri tepmesi ve
yorgunluk birikimi hiçbir promptta yok.

**Hüküm 🅑 ×8.** Yazım kuralı: efor fiili geçen her promptta eşleşen beden cevabı
zorunlu; **bedel filmin sonuna doğru birikir** ve son sahnedeki kapasite ilk
sahnedekiyle aynı olamaz [D206 · D207].

## 🅑 SINIF 2 — PARÇACIK VE SERBEST CİSİM · 4 🟠

S01 ×2 (*"Unstable debris gravity around rising slab"* · *"Particle clipping on
levitating slab"*) · S02 ×2 (*"Debris hover erratically without a clear magnetic or
gravitational grammar"* · *"Floating dust snaps out of existence at the plate
boundary"*). Parçacık cümlesi 0/14 **ve filmin novumu yüzen levhadır**.

⭐ THE_STILL_SWARM ile aynı kalıp: **filmin ana malzemesi kilitsiz.** İki filmde
tekrar → ders eşiği.

## 🅑 SINIF 3 — ATIŞIN HEDEFİ VE SONUCU KADRAJDA YOK · 3 🟠

S07 ×3 (⑦ AKSİYON): *"shot fired without showing target, impact, or consequence"* ·
*"leaves no persistent impact in environment"* · *"target of gun shot is entirely
off-screen"* · S08: *"threats appear directly overhead without approach trajectory"*.
Promptta atış var, **hedefi ve izi yok** [D213 aksiyon elipsi].

## 🅑 SINIF 4 — DONANIM DEVAMLILIĞI · 3 🟠 · 🅑 SINIF 5 — VİZÖR · 1 🟠

S02 · S13 (*"Suit chest harness geometry shifts"* · *"Harness detail drift on
close-up"*) — giysi cümlesi 0/14. S13 ⑪: *"Visor reflection switches between gold
chrome and translucent"* — vizörün türü hiçbir promptta kilitli değil [D79 · D146].

---

## 🅐 MODEL SAPMASI · 6

Doku yüzmesi S00 · S01 (bloom/doku cümlesi 14/14) · S09 ⑨ kafiye çifti
(*"S1 vs S11 framing and shot size do not rhyme"* — kamera cümlesi 14/14) ·
S13 ⑪ ortam pozlaması sıçraması · S03 · S06 ⑩ duruş.

## 🅒 BULGU DÜŞER · 3

S01 · S02 · S03 · S08 · S10'un ④/⑫ satırları (*"transition slows narrative
momentum"* · *"pacing drags"* · *"abrupt transition to end title card"* ·
*"title card presents starkly different art style"*): bunlar **kurgu ve paketleme**
bulgularıdır, promptun kapsamı dışındadır — başlık kartı post-prodüksiyondur.

---

## 🎯 ÜÇ SATIR

```
1. 🅑 ORANI %77 — deponun KRONOS'tan sonraki en yüksek prompt hatası oranı.
   Çekirdeğin dört cümlesi (ses · temas · giysi · parçacık) hiç yok.
2. FİLMİN NOVUMU KİLİTSİZ. Yüzen levha filmi, parçacık cümlesi 0/14.
3. ATIŞIN HEDEFİ KADRAJDA YOK. Üç bulgu tek bir eksik cümleden: atışın
   İZİ ortamda kalmalı.
```
