# 🧩 KRONOS_SON_SINYAL — prompt hata analizi

```
FORMAT      yatay 8 dk · 48 sahne · ızgara sahne(n) = (n−1) × 10 s
HAM RAPOR   30/30 geçerli   ③ kimlik: 2/30 güçlü bayrak (sahne 22 ≠ 48/1-4)
BULGU       60 → tekil 59   (🔴/🟠 · çapalı)
HÜKÜM       🅐 4 · 🅑 51 · 🅒 0 · 🅓 4
OKUMA       🅑/(🅐+🅑) = %93 → kusur ağırlıklı olarak PROMPTTADIR
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 48/48: bloom · metin · filigran · kamera
  KISMİ: sayı 24/48 · giysi 1/48 · parçacık 12/48 · efor 4/48 · g-ad 8/48
  ⛔ HİÇ YOK: SES · dış-ses · temas · g-sayı
  bulgulu sahnelerde eksik: SES 0/19 · dış-ses 0/19 · sayı 1/19 · temas 0/19 · giysi 1/19 · parçacık 8/19 · efor 2/19 · g-ad 3/19 · g-sayı 0/19
```

> ⚠️ **BÖLÜM OFSETİ DÜZELTMESİ · 19.09.2026** — bu filmin QA'sı BÖLÜM
> birimiyle koşuldu ve ikinci yarımın masterı 0:00'dan başlıyor. İlk eşlemede
> o bulgular birinci yarının sahnelerine yazılmıştı; betiğe ofset eklendi ve
> **38 bulgunun sahne numarası değişti**. Sınıflar, sayılar ve hükümler AYNI;
> aşağıdaki prose ikinci-yarım bulgularında **düzeltme öncesi** numaraları
> taşıyabilir. ⛔ Kesin sahne numarası için [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md)
> (makine yazar, ofsetli) hakemdir.

> Defter: [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md) · KRONOS_SON_SINYAL bölümü
> ⛔ Bu filmin promptuna DOKUNULMAZ. Çıktı sonraki filmin yazım standardıdır.

---

## 🅑 SINIF 1 — SES KİLİDİ HİÇ YOK  · 4 🔴 BLOCKER

| S | bulgu | mercek |
|:--:|---|:--:|
| S01 | Airborne thruster/mechanical rumble audible in space exterior vacuum | ① |
| S09 | Vented gas explosion roaring sound propagation in exterior space vacuum | ① |
| S15 | Airborne hull tearing and explosive decompression sound in vacuum | ① |
| S18 | Mechanical hatch disengagement audio propagating through vacuum | ① |

**Promptta ne yazıyordu:** hiçbir şey. 96 promptun **hiçbirinde `AUDIO:` satırı yok**;
`vacuum` kelimesi bütün filmde 3 kez, `silent/silence` 5 kez geçiyor ve hiçbiri
NEGATIVE'de değil. S15'in MOTION'ında tek ipucu var:

> `a tiny release of vapor escapes silently from a conduit joint into zero-gravity`

Bu bir sahne içi sıfat; motora "bu klip vakumda geçiyor, hava yoluyla ses yok"
diyen bir cümle yok. Motor boşluğu Hollywood sesiyle doldurdu — **dördü de aynı
boşluktan çıktı.**

**Hüküm 🅑 ×4.** Yazım kuralı: her video promptu `AUDIO:` satırı taşır ve
vakum sahnesinde o satır **neyin duyulduğunu** söyler (gövdeden iletilen tıkırtı,
kask içi nefes) — "ses yok" demekle yetinmez [D123: yasağı yazmak kavramı sokar].

---

## 🅑 SINIF 2 — İNSAN SAYISI TARİFLE KİLİTLENMİŞ · 2 🔴 BLOCKER

| S | bulgu | mercek |
|:--:|---|:--:|
| S04 | Duplicate character: second astronaut suit spawns on right frame edge | ① ② |
| S17 | Phantom background astronaut figure in Module A corridor | ⑤ |

**Promptta ne yazıyordu** — S04 IMAGE:

> `NEGATIVE: no bloom, no watermark, no text, no logo, no labels, no extra characters, …`

`no extra characters` bir **tariftir**, sayı değil. Deponun ölçülmüş tek gerçeği
bunun tersini söylüyor: *tarif kilidi %0 tuttu, sayısal kilit %100 tuttu*
(`01_DERS_ETKINLIK_RAPORU`). Filmde `exactly N human` kalıbı **96 promptun
yalnız 23'ünde** var ve **ikisi de o 23'ün dışında.**

S17 daha da öğretici: IMAGE negatifi `no extra crew` diyor, **VIDEO negatifi
demiyor** — negatif blok sahneden sahneye elle yazıldığı için çekirdek kayıyor.

**Hüküm 🅑 ×2.** Yazım kuralı: negatif çekirdek **film başına bir kez** yazılır ve
her prompta BİREBİR kopyalanır; insan sayısı satırı `Exactly N human characters,
no duplicates, no third person.` biçiminde **rakamla** girer.

---

## 🅑 SINIF 3 — TEMAS SINIRI CÜMLESİ YOK · 2 🟠

| S | bulgu | mercek |
|:--:|---|:--:|
| S02 | Glove material phases through carabiner latch metal geometry | ① |
| S13 | Glove material deforms and melts around brass valve knob contour | ① |

**Promptta ne yazıyordu:** hiçbir şey. `no merging` / `no phasing` /
`clear boundary` kalıplarının hiçbiri filmin 96 promptunda geçmiyor.
NEGATIVE'in taşıdığı `no morphing` genel bir sıfat; el-yüzey temasını adlandırmıyor.

**Hüküm 🅑 ×2.** Yazım kuralı: negatif çekirdek
`Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.`
satırını taşır — **eldivenin temas ettiği her sahnede.**

---

## 🅑 SINIF 4 — DEVAMLILIK TAŞIYICISI CÜMLESİ YOK · 1 🔴 · 3 🟠

| S | bulgu | mercek |
|:--:|---|:--:|
| S07 | Suit drifts from full EVA suit to orange cloth flight jacket without neck ring | ① |
| S11 | White EVA suit in S2/S5 → orange/brown jacket in S7 → white suit again in S11 | ② |
| S14 | Kestrel's facial bone structure shifts from narrow jaw to broad square features 🔴 | ② |
| S14 | Male suit wardrobe drift; orange-shouldered jacket vs white EVA suit | ① |

**Promptta ne yazıyordu:** her sahne giysiyi **kendi kelimeleriyle yeniden tarif
ediyor** (`white EVA suit`, `pressurized suit`, `suit-mounted wrist clock`) ve
hiçbir promptta `identical throughout, no drift` kalıbı yok. Kimlik yüz üzerinden
taşınıyor — S14'teki yüz kayması bunun doğrudan bedeli.

**Hüküm 🅑 ×4.** Yazım kuralı: Character Bible'ın giysi cümlesi **değiştirilmeden**
her prompta girer; negatif çekirdek `Equipment and clothing identical throughout,
no drift, no gear appearing or disappearing.` taşır. Kimlik yüzle değil
**renk + omuz geometrisi + sırt ünitesi** ile taşınır.

---

## 🅑 SINIF 5 — PARÇACIK VE ENKAZ FİZİĞİ YAZILMAMIŞ · 5 🟠

| S | bulgu | mercek |
|:--:|---|:--:|
| S01 | Vented gas plume forms turbulent atmospheric cloud instead of ballistic expansion | ① |
| S01 | Vented steam particles exhibit atmospheric drag and hanging behavior | ① |
| S09 | Vented gas forms swirling atmospheric eddies in space vacuum | ① |
| S11 | Steam/gas leak billows in dense atmospheric clouds inside zero-G cabin | ① |
| S15 | Debris particles float without directional momentum vector / hover like 2D assets | ① |

**Promptta ne yazıyordu** — S09 IMAGE, tek cümle:

> `a faint micro-cloud of frozen vapor lingering static in the vacuum`

`lingering static` **tarif**; hızı, yönü, sönüm süresi yok. Motor "buhar" görünce
atmosferik davranışı getirdi. Beş bulgunun beşi aynı boşluk.

**Hüküm 🅑 ×5.** Yazım kuralı: parçacık taşıyan her sahne negatif çekirdekte
`Particles obey the stated gravity with continuous momentum, never hovering,
never swirling like liquid.` satırını taşır **ve** pozitif gövde yönü + sönümü
sayıyla verir (`expands in a straight cone and is gone in 1,5 s`).

---

## 🅑 SINIF 6 — EFOR VE YORGUNLUK SÖZLÜĞÜ YOK · 2 🔴 · 9 🟠

⑧ EFOR merceği bu filmde **tek başına 11 bulgu** yazdı: S04 (kapak kütlesi gövdeyi
döndürmüyor) · S13 (basınçlı eldiven çıplak el inceliğinde) · S15 (patlamaya karşı
tutuş, oran düşüşü yok) · S16 (beş ayrı satır: nefes değişimi yok, duruş anında
sıfırlanıyor, önkol titremesi yok, gerginlik bir vuruşta kayboluyor) · S24
(*"scene 24'teki kapasite scene 2 ile aynı"* — 1/10).

**Promptta ne yazıyordu:** 96 promptun tamamında `strain` 4, `bracing`/`braces` 4,
`tremor` 1, `breath` 1 kez geçiyor. Bedenin yükü **hiç yazılmamış.**

**Hüküm 🅑 ×11.** Yazım kuralı: efor fiili (`hauls/pulls/drags/lifts/heaves`)
geçen her promptta **eşleşen beden cevabı** zorunlu — `his forearm tightens`,
`his shoulders drop`, `the fourth stride is shorter than the first`. Bu kural
zaten `prompt_kontrol.py` ⑳'de var; **KRONOS eski rejim klasörü olduğu için
hiç koşmadı** (`00_HIKAYE_ONAYI.md` yok).

---

## 🅑 SINIF 7 — SIFIR-G HAREKET MANTIĞI TARİFLE GEÇİLMİŞ · 2 🔴 · 4 🟠

| S | bulgu | tip |
|:--:|---|---|
| S03 | Splays both arms in open air to balance, no contact surface | PUPPET |
| S03 | Torso glides upward without leg or foot movement | SLIDE |
| S04 | Hand hovers between two knobs without turning either | ABANDONED |
| S05 🔴 | Legs pedal in a walking cadence while suspended in mid-air | SLIDE |
| S08 | Lever stutters and snaps back 2 cm while hands keep pulling | CONTRADICTION |
| S14 · S24 | Boots skate across deck plating without stepping weight | SLIDE |

**Promptta ne yazıyordu** — her sahnenin sonundaki aynı cümle:

> `Microgravity movement is subtle, realistic, and physically grounded.`

Üç sıfat, sıfır kural. Sıfır-G'de gövdenin **neye tutunarak** hareket ettiği hiçbir
promptta yazmıyor; motor yürüyüş animasyonunu havada oynattı.

**Hüküm 🅑 ×6.** Yazım kuralı: sıfır-G'de her hareket bir **temas noktasıyla**
yazılır (`he pulls himself along the rail with his right hand; his feet never
touch the deck`). "Physically grounded" sıfatı tek başına kilit değildir.

---

## 🅑 SINIF 8 — METİN YASAĞI İLE SAHNE TASARIMI ÇELİŞİYOR · 3 🟠

| S | bulgu | mercek |
|:--:|---|:--:|
| S04 | Digital timer numbers morph and flicker illegibly on control panel | ① |
| S10 | "POWER SYSTON" typo on control panel wall | ⑤ |
| S10 | Clean "MODULE B" corridor stencils morph into garbled "NO HB/4004ET" | ⑤ |

**Promptta ne yazıyordu:** NEGATIVE her sahnede `no text, no logo, no labels`
diyor — **ama filmin olayı saat okumaktır.** S04'ün Türkçe başlığı
`İstasyon Saati: 12:01:00–12:01:10` diyor, İngilizce gövde ise:

> `Both clock screens are glowing blank digital surfaces.`

Yani prompt aynı anda hem "boş ekran" hem "zaman ilerliyor" istiyor. Motor
çelişkiyi bulanık rakamla çözdü. Duvar stensilleri de tasarımda VAR, negatifte YASAK.

**Hüküm 🅑 ×3.** Yazım kuralı: sayaç **metinsiz** çözülür (D50/D78) — saat
`iki ışıklı çubuk arasındaki mesafe` gibi fiziksel bir gösterge olur, ya da metin
kadrajda meşru sayılır ve yasak o sahnede kaldırılır. İkisi aynı promptta duramaz.

---

## 🅑 SINIF 9 — REPLİK İNGİLİZCE PROMPTA HİÇ GİRMEMİŞ · 2 🔴

| S | bulgu | mercek |
|:--:|---|:--:|
| S06 | Line 7 spoken by Kestrel's voice on-screen instead of Aras over comms | ③ |
| S06 | Kestrel's voice identity calls herself "Kestrel" instead of Aras asking over radio | ③ |

**Promptta ne yazıyordu** — replik yalnız **Türkçe künye satırında**:

> `**Diyalog / EN:** Kestrel: That is my voice.`

İngilizce MOTION'da ise sadece:

> `she speaks her line with a quiet, breathy delivery of pure dread`

"Her line" motorun bilmediği bir şeye işaret ediyor; repliğin metni de, konuşanın
kimliği de, kanalı (telsiz mi odada mı) da İngilizce prompta hiç girmemiş.

**Hüküm 🅑 ×2.** Yazım kuralı: replik post-dub'a bırakılır ve promptta **0 replik**
üretilir (ağız kadrajdaysa lip-sync riski açılır), ya da konuşan + kanal İngilizce
gövdede adıyla yazılır. Türkçe künye satırı motora GİTMEZ.

---

## 🅑 SINIF 10 — ORTAM DEVAMLILIĞI SAHNELER ARASI YAZILMAMIŞ · 3 🔴 · 1 🟠

| S | bulgu | mercek |
|:--:|---|:--:|
| S09 | Hull intact with light smoke in S1, torn metal crater in S9 | ② |
| S14 🔴 | Red rigid circular hatch in S4 → wrinkled mylar padded door in S14 | ⑤ |
| S18 🔴 | Red hatch opens to Module B corridor in S3, opens directly to vacuum in S18 | ⑤ |
| S15 | Hull breach geometry morphs jagged edges between frames | ① |

**Promptta ne yazıyordu:** her sahne mekânı sıfırdan tarif ediyor; hiçbir promptta
"bu kapı S3'teki kapıdır" diyen bir **durum merdiveni** yok. Hasar da durum
taşımıyor: S1'de "light smoke", S9'da "torn metal crater" — aradaki geçiş
hiçbir promptta yazılı değil.

**Hüküm 🅑 ×4.** Yazım kuralı: tekrar eden her varlık **referans paketinde** bir
sayfa alır ve iki durumu (hasarsız / hasarlı) sahne numarasıyla kilitlenir
[D168 KAPI 0]. KRONOS'un referans paketi var ama durum merdiveni yok.

---

## 🅐 MODEL SAPMASI — kilit vardı, tutmadı · 4

| S | bulgu | promptta yazan | neden 🅐 |
|:--:|---|---|---|
| S25 🔴 | Persistent AI sparkle logo artifact in lower right corner **across all 24 scenes** | `no watermark` — **96 promptun 96'sında** | Kilit eksiksiz yazıldı ve hiç tutmadı. Bu prompt kusuru değil **araç/ihraç kusurudur** [D150 filigran · D215 araç ayarı]: master yeniden ihraç edilir. |
| S25 | Four-pointed star sparkle watermark anchored bottom-right across all 24 shots | aynı | aynı |
| S06 | Soft AI bloom/haze around helmet visor rim | `no bloom` — her negatifte | tarif kilidi; sayısal karşılığı yok (`0% bloom`) → tutmadı |
| S11 | Unmotivated volumetric light bloom from hull gas venting | `no bloom` | aynı |

⭐ `no bloom` dört filmde de aynı şekilde düştü — sayısal hâli (`0% bloom, no glow,
no soft focus, every surface keeps visible texture`) yeni filmlerde kullanılıyor.
Bu satır 🅐 ile 🅑 arasında duruyor: **kilit vardı ama tarifti.**

---

## 🅓 EŞLEŞEMEYEN · 4

⑧ EFOR'un film-boyu satırları (`Fatigue Accumulation 1/10 · E1–E13 across 24 scenes`,
`Recovery Curve Honesty 3/10`) tek sahneye oturmuyor — **film boyu** bulgular.
Sayılır, sınıfa girmez; SINIF 6'nın gerekçesini güçlendirirler.

---

## 🎯 BU FİLMİN ÜÇ SATIRI

```
1. NEGATİF ÇEKİRDEK YOK. 96 promptun negatifi tek tek elle yazılmış; aynı film
   içinde 8 farklı negatif varyantı var ve çekirdek sahneden sahneye kayıyor.
   İki BLOCKER (S04 · S17) doğrudan bu kaymadan çıktı.
2. SES HİÇ YAZILMAMIŞ. AUDIO satırı 0/96. Dört BLOCKER'ın dördü de vakumda ses.
3. BEDEN HİÇ YAZILMAMIŞ. Efor sözlüğü 96 promptta toplam 10 kelime;
   ⑧ EFOR tek başına 11 bulgu yazdı ve ⑭ HAREKET 6 bulgu daha ekledi.
```
