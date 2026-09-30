# 🧩 BENI_HATIRLAMA — prompt hata analizi

```
FORMAT      yatay 8 dk · 48 sahne · ızgara sahne(n) = n × 10 s (hook 10 s)
HAM RAPOR   18/18 geçerli · raporlar yarım master (22-24 sahne)
BULGU       42 → tekil 42
HÜKÜM       🅐 30 · 🅑 8 · 🅒 3 · 🅓 1
OKUMA       🅑/(🅐+🅑) = %21
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 48/48: SES · temas · giysi · parçacık · bloom · metin · g-ad · filigran · kamera
  KISMİ: sayı 45/48 · efor 43/48
  ⛔ HİÇ YOK: dış-ses · g-sayı
  bulgulu sahnelerde eksik: dış-ses 0/16 · sayı 15/16 · efor 15/16 · g-sayı 0/16
```

> ⚠️ **BÖLÜM OFSETİ DÜZELTMESİ · 19.09.2026** — bu filmin QA'sı BÖLÜM
> birimiyle koşuldu ve ikinci yarımın masterı 0:00'dan başlıyor. İlk eşlemede
> o bulgular birinci yarının sahnelerine yazılmıştı; betiğe ofset eklendi ve
> **13 bulgunun sahne numarası değişti**. Sınıflar, sayılar ve hükümler AYNI;
> aşağıdaki prose ikinci-yarım bulgularında **düzeltme öncesi** numaraları
> taşıyabilir. ⛔ Kesin sahne numarası için [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md)
> (makine yazar, ofsetli) hakemdir.

---

## 🅑 SINIF 1 — "THE STATED GRAVITY" VAR, STATED EDİLEN SAYI YOK · 2 🔴  ⭐ ders

| S | bulgu |
|:--:|---|
| S15 🔴 | Cave sand falls at g ≈ 1.11 m/s² while wall-climbing dust falls at g ≈ 2.48 m/s² (**2,2×**) |
| S20 🔴 | Cave fissure cascade falls at g ≈ 1.13 m/s² while exterior cliff sand at g ≈ 0.39 m/s² (**2,9×**) |

**Promptta ne yazıyordu** — negatif çekirdek, 99 kez:

> `Particles obey the stated gravity with continuous momentum, never hovering …`

`the stated gravity` — **nerede stated edildiğini** aradım. PHYSICS satırında, tarifle:

> `PHYSICS: thick air, about two thirds of Earth's weight; heavy wool swings slowly`

`about two thirds of Earth's weight` ≈ 6,5 m/s². Ölçülen değerler 0,39 · 1,11 ·
1,13 · 2,48. Yani **hiçbiri** tarifin içinde değil ve her sahne kendi yerçekimini
uydurmuş — çünkü "yaklaşık üçte iki" bir aralıktır, bir sayı değil.

**Hüküm 🅑 ×2.** Yazım kuralı: yerçekimi **tek bir sayı** olarak yazılır ve her
promptta AYNI sayı geçer (`Gravity is 0.30 g` — THE_FALLING_WORLD kalıbı). Negatif
çekirdeğin `the stated gravity` ifadesi ancak o sayı gerçekten yazılıysa anlamlıdır;
yazılmamışsa cümle **kendi kendine gönderme** yapar ve hiçbir şeyi kilitlemez.

⭐ Bu deponun ölçülmüş tek gerçeğinin dördüncü doğrulaması:
*tarif kilidi %0 tuttu, sayısal kilit %100 tuttu.*

---

## 🅑 SINIF 2 — DIŞ SES CÜMLESİ YOK · 1 🟠 · 🅑 SINIF 3 — PALET GEÇİŞİ YAZILMAMIŞ · 1 🟠

`AUDIO:` satırı 48/48 var ama hiçbirinde ortamın ses yasası yok (film ince atmosferde
geçiyor, ses VAR ama boğuk olmalı). S09 🟠: *"Sudden shift to false-color thermal
palette without transition or optical justification"* — palet değişimi sahne
haritasında var, **promptta geçiş cümlesi yok**.

## 🅑 SINIF 4 — NESNE ÖLÇÜSÜ GÖVDE BOYU CİNSİNDEN DEĞİL · 1 🟠 [D138]

S08 🟠: *"Scarf is a 1.2 m narrow neck fabric in L6 but becomes a full-body garment
covering the 1.0 m creature in L10"*. Eşarp 90 promptta geçiyor, **uzunluğu hiç
yazılmamış**.

## 🅑 SINIF 5 — AYNI NESNENİN İKİ KOPYASI · 2 🟠

S03/S04: *"Woman wears yellow scarf on neck in S1; Astronaut pulls duplicate yellow
scarf from chest pocket in S5"*. İki ayrı sahnede aynı nesne bağımsız tarif edilmiş;
hiçbir promptta "bu S1'deki eşarptır, ikincisi yoktur" diyen bir cümle yok.

## 🅑 SINIF 6 — ELDİVEN İNCELİĞİ · 2 🔴

S04 🔴 · S10 🔴 (⑧ EFOR, Pattern ⑥): *"Unfolding fine knitted scarf with thick
gloves — glove stiffness, lack of tactile feedback"* · *"Operating tiny device dial
with heavy glove"*. Efor cümlesi 43/48 var ama **eldivenin kalınlığının hareketi
nasıl bozduğu** hiçbir promptta yazılı değil.

---

## 🅐 MODEL SAPMASI · 30 — ve bunların üçü çok şey söylüyor

### 🅐-1 · YARATIK ANATOMİSİ · 2 🔴

S13 🔴: *"seal-like organism suddenly sprouts six arthropod legs"*.

**Promptta ne yazıyordu** — 34 promptta, harfi harfine:

> `creature keeps the same number of legs and the same smooth hide throughout, no extra limbs`

Kilit **sayıya çevrilmiş hâliyle bile** ("aynı sayıda bacak") tutmadı.
Ders siparişi: canlı anatomisi metinle tutmuyor → **referans paneli** [D168 · D2].

### 🅐-2 · TEMAS SINIRI · 4 (2 🔴)

S02 🔴 ×2 · S14 ×2: *"gloved fingers merge and lose structural integrity while
touching glowing spots on creature skin"*. Temas cümlesi **48/48'de var.**

⭐ Karşılaştırma: FROST_LINE'da temas cümlesi bulgunun düştüğü sahnelerde **yoktu**
(🅑), burada **var** (🅐). Aynı kusur, iki farklı sahip. Sınıf tablosu ikisini
ayırmak zorunda.

### 🅐-3 · FİLİGRAN · 1 🔴

S20 🔴: *"Static four-pointed sparkle watermark burned into bottom-right corner
across all shots"* — `no watermark` 48/48. **Üçüncü film** (KRONOS S25 · FROST_LINE
S00/S22). Araç/ihraç kusuru [D150], prompt işi değil.

### 🅐-4 · KAYMA VE ADIM · 4 · 🅐-5 · EFOR · 6 · 🅐-6 · KİMLİK/GİYSİ · 3 · 🅐-7 · diğer · 10

S04 · S15 · S16 boot slide / moonwalk pivot · S16 ⑭ SLIDE · S10 🔴 yüz yapısı
kayması · S17 kol bandı sağdan sola aynalanıyor — hepsinde ilgili kilit yazılı.

---

## 🅒 BULGU DÜŞER · 3

| S | bulgu | neden |
|:--:|---|---|
| S11 | *Secondary female character transitions to transparent ghosting/hologram artifact* | Bu filmin **novumu** budur: ikinci figür saydamdır ve öyle yazılmıştır (`transparent` 60 promptta). Mercek tasarım kararını kusur saymış → ⑩ ÖNERME KAPISI. |
| S10 | *Transparent character legs phase through the creature without collision* | Aynı novum: saydam figürün çarpışması yoktur. |
| S07 | *Ceiling topology in S1 is closed rock vault; S9 introduces open ceiling chasm* | İki ayrı mekân; sahne haritası geçişi taşıyor. |

---

## 🎯 ÜÇ SATIR

```
1. "THE STATED GRAVITY" HİÇ STATED EDİLMEMİŞ. 99 promptta o ifadeye gönderme var,
   sayı hiçbir yerde yok; iki 🔴 tam oradan çıktı (2,2× ve 2,9× tutarsızlık).
2. NEGATİF ÇEKİRDEK KUSURSUZ, YİNE DE 30 🅐. temas · parçacık · bloom · metin ·
   filigran 48/48 — yazımın yapabileceği yapılmış.
3. CANLI METİNLE TUTMUYOR. "aynı sayıda bacak" 34 promptta yazılı ve yaratık
   S13'te altı bacak çıkardı → canlı REFERANS PANELİ ister.
```
