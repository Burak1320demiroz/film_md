# 🧩 THE_FALLING_WORLD — prompt hata analizi

```
FORMAT      yatay 8 dk · 48 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   30/30 geçerli · ⭐ İKİNCİ YARIM QA'sı 19.09.2026'da TAM KOŞTU (PART2 ×15)
            ⚠️ iki mercek yarım: 04_HIKAYE_PART2_DURDURULDU · 13_UYUM_PART2_EKSIK
BULGU       68 → tekil 57   (adjudike edilen 47 · ⬜ son parti 10)
HÜKÜM       🅐 35 · 🅑 5 · 🅒 6 · 🅓 1  (47 bulgu üzerinden) · ⬜ 10 bulgu adjudike EDİLMEDİ
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 48/48: SES · giysi · parçacık · bloom · metin · g-ad · g-sayı · filigran · kamera
  KISMİ: sayı 46/48 · temas 46/48 · efor 45/48
  ⛔ HİÇ YOK: dış-ses
```

> ⚠️ **BÖLÜM OFSETİ DÜZELTMESİ · 19.09.2026** — bu filmin QA'sı BÖLÜM
> birimiyle koşuldu ve ikinci yarımın masterı 0:00'dan başlıyor. İlk eşlemede
> o bulgular birinci yarının sahnelerine yazılmıştı; betiğe ofset eklendi ve
> **21 bulgunun sahne numarası değişti**. Sınıflar, sayılar ve hükümler AYNI;
> aşağıdaki prose ikinci-yarım bulgularında **düzeltme öncesi** numaraları
> taşıyabilir. ⛔ Kesin sahne numarası için [`../01_BULGU_DEFTERI.md`](../01_BULGU_DEFTERI.md)
> (makine yazar, ofsetli) hakemdir.

> ⚠️ **CANLI KORPUS — 19.09.2026 14:24 anlık görüntüsü.** Bu filmin QA'sı oturum sırasında
> sürdü; son parti (10 bulgu) deftere girdi ama **hüküm verilmedi**. Sayılar
> `../01_BULGU_DEFTERI.md`'de makineyle güncel, buradaki hüküm dağılımı 47 bulguluk.
> ⚠️ Bölüm ofsetinin `Q` türetimi hangi raporların var olduğuna duyarlıdır: son
> parti gelince bazı sahne numaraları **1 kaydı** (S34→S35 · S39→S40 · S41→S42).
> Kesin numara defterdedir.
>
> ⭐ **Deponun en iyi kapsamalı filmi (%91) ve en düşük 🅑 oranı (%13).**
> Prompt tarafında yapılacak iş beş cümleye inmiş; 47 bulgunun 35'i kilit
> yazılıyken çıkmış.

---

## ③ KİMLİK VE TESLİM — iki kayıt

```
KİMLİK ✅ OKUNDU VE TUTTU. Ham dosya adları kural dışı (01_KARE_PART2_TEKRAR.md —
<FILM>_<MERCEK>_HAM.md değil) ve 18'in 11'i künyesiz; ama rapordaki nesneler
(kayış/kemer halkası · gri sandık · gümüş bant · tekerlekli araç · mercekli halka ·
beyaz+kobalt / turuncu+siyah giysiler) filmin promptlarıyla eşleşiyor.
Zaman damgası: promptlar 18.09 14:32 · ilk yarım raporları 18.09 22:44 ·
ikinci yarım raporları 19.09 13:42.

⚠️ TESLİM UYUŞMAZLIĞI ŞÜPHESİ [①.9 · D188 · doğrulanmalı]
   İkinci yarım 24 klip = 240 s olmalı. Ölçülen: 230 s (3:50) ve
   ② DEVAMLILIK raporu makarada 22 sahne saydı.
   → BİR YA DA İKİ KLİP MAKARADA YOK. Hangi sahne olduğu ①.9 ile bulunur.

⚠️ ÜRETİM DEFTERİ ESKİ: defter hâlâ dört referans sayfasını ⬜ ve üretimi
   0 kare gösteriyor; film BAŞTAN SONA üretilmiş ve QA'sı koşulmuş.
```

---

## 🅐 SINIF 1 — VİZÖR OPAKLIĞI KIRILDI · 1 🟠 ⭐⭐ FİLMİN EN SERT KISITI

| S | bulgu |
|:--:|---|
| S41 | *Reflective **opaque** visor (S3) turns **completely transparent displaying face** (S19)* |
| S41 | *Astronaut face inside helmet appears noticeably airbrushed/waxy with lost skin texture* |

**Promptta ne yazıyordu** — 48 promptun 48'inde, sahibin en sert kararı:

> `each pane fully opaque matte black`
> `IN FRAME:` satırına **`face` hiçbir promptta yazılmadı**

**Hüküm 🅐 ×2 — ve bu filmin en pahalı satırı.** S41 filmin **DORUĞU ve KAPAK
ANI**. Kapak promptu 120 px testini "iki leke, arada tek kol" üzerine kurmuştu;
vizör açılırsa kapak başka bir kapaktır.

⭐ Kilit kusursuz yazılıydı ve tutmadı → **kılavuz §4'e dördüncü satır adayı**:
opak vizör de metinle tutmayan bir kilit olabilir. ⚠️ Tek vaka — ADAY, ders değil.

## 🅐 SINIF 2 — YERÇEKİMİ SAYIYLA YAZILI, YİNE KIRILDI · 2 🔴 · 1 🔴 (ilk yarım)

| S | bulgu |
|:--:|---|
| S34 🔴 | *Catwalk grating collapses beneath the astronaut, causing the figure to **float/glide** unnaturally* |
| S34 🔴 | *Astronaut falls through the collapsed catwalk with **zero-G glide*** |
| S13 🔴 | *Cliff rockfall falls under g ≈ 4,4 m/s² while the platform collapse drops under g ≈ 2,2 m/s²* |

`Gravity is 0.30 g` **48/48 promptta, sayıyla**. Üç bulgu da düşen gövdede.
⭐ `03_` §🅑4'ün ölçüsü güncellendi: **sayı yarıya indiriyor ama sıfırlamıyor** —
BENI_HATIRLAMA tarifle 2 🔴, bu film sayıyla **3 🔴**.

## 🅐 SINIF 3 — TEMAS · 4 (2 ilk yarım · 2 ikinci)

S02 (eldiven kemer tokasına giriyor) · S17 (parmaklar bant rulosuna eriyor) ·
**S39 ×2** (*"Hand contact morphing and finger fusion when the orange-suited
astronaut grabs the white-suited astronaut's wrist"*). Temas cümlesi 46/48'de.

⭐ **S39 filmin NOVUM ANIDIR** — bilek tutuşu. `03_` §🅐2'nin en pahalı örneği:
filmin taşıyıcı jesti tam da temas füzyonuna düşen jest.

## 🅐 SINIF 4 — PARÇACIK VE ÇÖKME · 8 · SINIF 5 — DOKU/IŞIK · 5 · SINIF 6 — İNSAN SAYISI · 3 🔴 · SINIF 7 — EFOR · 5 · SINIF 8 — MEKÂN/DÜNYA · 5

**Parçacık** S05 · S10 · S24 ×2 · S25 · S29 · S43 ×2 — *"collapsing metal bridge
drops like lightweight …"* · *"thruster exhaust dust lacks momentum density"* —
cümle 48/48'de. **Doku/ışık** S32 ×2 · S29 (*anahtar ışık yönü geniş planla
uyuşmuyor*) · S39 (*jello*) · S41. **İnsan sayısı** S19 ×3 🔴 (üçüncü astronot) —
`Exactly 2 human characters` 46/48'de. **Efor** S01 🔴 · S03 · S04 🔴 · S11 · S12 🔴.
**Mekân** S30 (*halat düğümü ↔ karabina*) · S31 (*toprak ↔ metal platform*) ·
S34 (*ızgara sağlam → kırık → sağlam*) · S36 ×2 (*halka geometrisi · gök değişimi*).

---

## 🅑 PROMPT BOŞLUĞU · 5

| # | S | bulgu | eksik cümle |
|:--:|:--:|---|---|
| 🅑-1 | S04 | *Buggy shadow casts 80° right despite the ring being dead-ahead* | gölge açısı sayıyla yok; ışık yönü halkanın kadrajdaki yeriyle bağlanmamış |
| 🅑-2 | S09 | *50 kg rock onto the tire produces zero suspension compression* | aracın süspansiyonu hiçbir promptta tarif edilmemiş |
| 🅑-3 | S22 | *He turns his head fully toward a bare rock surface with nothing there* | baş dönüşü var, **neye baktığı** yok — opak vizörlü filmde bakış hedefi kadrajda olmak zorunda |
| 🅑-4 | S34 | *Metal catwalk grating intact → breaks open → resets intact* | ızgaranın **durum merdiveni** yok |
| 🅑-5 | — | dış-ses cümlesi 0/48 | ince atmosferin ses yasası `AUDIO:` satırında var ama NEGATIVE'de yok |

---

## 🅒 BULGU DÜŞER · 6 — sebebi ORTAM KARTI ve TASARIM

| S | bulgu | neden düşer |
|:--:|---|---|
| S05 🔴 | *airborne acoustic SFX propagate through exterior **atmospheric vacuum*** | mercek ortamı VAKUM sandı; film **§3.2 İNCE ATMOSFER** — ses VARDIR, boğuktur |
| S13 🟠 | *unnaturally **floaty** gravity* | 0,30 g tasarımdır ve 48/48'de sayıyla yazılı |
| S13 🟠 | *they watch the collapse without **flinching*** | kadrajda yüz yok (opak vizör); "flinching" okunabilir değil |
| S13 · S14 🟠 | *S12 enters airlock; S13 cuts to exterior* · *S14 buggy plunges; S15 routine* | sahne haritasının kendi geçişleri |
| S36 🟠 | *celestial background shifts from red desert eclipse to orbital planet view* | iki ayrı bakış yönü; W1-W3 dünya cümleleri kapsam kuralıyla yazılı |

⛔ Altısı da **⑩ ÖNERME KAPISI**'ndan geçti. Beşi raporun `INPUTS:` satırında
SPEC'in olmamasından doğdu — ⑬'ün girdi kuralı koşulsaydı yazılmazlardı.

---

## 🎯 ÜÇ SATIR

```
1. VİZÖR AÇILDI. Filmin en sert kısıtı 48/48 promptta yazılıydı ve doruk
   sahnesinde kırıldı — kapak anı da o sahne.
2. 🅑 %13 — DEPONUN EN DÜŞÜĞÜ. Prompt tarafında beş cümle kaldı; kalan 35
   bulgu kilit yazılıyken çıktı ve kadraj/araç/kurgu masasına aittir.
3. İKİNCİ YARIM 10 s EKSİK TESLİM EDİLMİŞ (230 s ≠ 240 s, 22 sahne sayıldı) —
   ①.9 ile doğrulanmalı, üretim defteri de güncel değil.
```
