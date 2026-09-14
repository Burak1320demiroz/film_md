# 🎵 THE RISING SNOW — MÜZİK PROMPTU

## Tek parça · 180 saniye · 120 BPM (yarım zaman hissi) · Si minör
### 31 sahne / 4:57 film · müzik 3:00 · **son 56 saniye müziksiz**
### _"Kar çizgisi yükselir. Hava sınırı durur. Müzik ikisinin arasıdır."_

> Kılavuz: `kilavuzlar_ve_sistem_dosyalari/GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md`
> Bu dosya **sadece müzik promptudur.** Ses tasarımı (rüzgar, kar ciyaklaması,
> gümbürtü, suit fanı) zaten Veo promptlarının içinde — PART_A/B/C'de yazılı.

---

## 🎯 TEK MÜZİKAL FİKİR

```
Filmde iki yatay çizgi var ve film ikisinin arasındaki 95 metredir:

  KAR ÇİZGİSİ    yükseliyor, hızlanarak, geri dönmüyor
  HAVA SINIRI    sabit, hiç kıpırdamıyor

MÜZİKTE:
  ALT DRONE      180 saniye boyunca çok yavaş YÜKSELİR (toplam +1 yarım ses).
                 Duyulmaz, hissedilir. Asla inmez, asla başladığı yere dönmez.
  ÜST SABİT TON  ince, yüksek, HİÇ DEĞİŞMEYEN tek bir ton. Hiç kıpırdamaz.

  → İki ton arasındaki aralık film boyunca DARALIR.
    Kuşağın kapanması budur. Kimse söylemez, kimse göstermez, duyulur.
```

---

## 📋 KÜNYE (§17)

```
FİLM:                   THE RISING SNOW · 4:57 (297s) · 31 sahne
                        Hook 9s + 24 × 10s + 6 ara sahne × 8s

NOVUM OKUMASI:          "İzleyici dağ duvarındaki keskin yatay çizgiyi
                        BİR SAAT olarak okumalı — manzara değil, tehdit
                        değil, gizem değil. Çalışan, sabırlı, geri
                        alınamaz bir sayaç."                     ← ÖNCE BU

MÜZİK-GÖRÜNTÜ İLİŞKİSİ: Anempatik zemin + karşıt ruh hali.
                        Müzik hiçbir olaya tepki vermez; kendi yükselişini
                        sürdürür. Gümbürtü olur — müzik duymaz.
                        S20'de doruk olur — müzik büyümez, KESİLİR.

TEMPO:                  120 BPM notasyonda · 4/4 · 1 ölçü = 2 saniye
                        HİSSEDİLEN nabız yarım zaman (2 saniyede bir).
                        §14 formülü: 240×5÷10 = 120 (10s sahne = 5 ölçü)
                                     240×4÷8  = 120 (8s ara sahne = 4 ölçü)
                        → Filmin İKİ sahne uzunluğuna da hizalanan tek tempo.
                        ⚠️ ÖLÇÜ GRİDİ 0:09'DA BAŞLAR (hook'un sonunda).
                          Hook 9 saniye olduğu için tüm sahne sınırları tek
                          sayıdadır; grid 0:09'dan sayılırsa hepsi ölçü başı olur.

TONALİTE:               Si minör (Aeolian). ÇÖZÜLME YOK — sıfır kadans.
                        Yükselen üç nota motifi 10 kez çalar, hiçbirinde
                        çözülmez, sonuncusu ÜÇÜNCÜ NOTASINDAN ÖNCE KESİLİR.

SESSİZLİK SAHNESİ:      S9.5 + S10 (1:55 – 2:13, 18 saniye) — dördüncü
                        terası görüş + filmin ilk duygusal zirvesi.
                        Müzik S9'un sonunda biter, S11'de tek notayla döner.

ÇÖZÜLMEYEN CÜMLE:       Motifin 10. (son) statement'ı S20'de başlar ve
                        üçüncü notası HİÇ GELMEZ. Filmin kalan 56 saniyesi
                        seyircinin o notayı beklediği süredir.

KAPANIŞ:                Müzik 4:01'de biter ve bir daha HİÇ girmez.
                        S20.5 · S21 · S22 · S23 · S23.5 · S24 = 56 saniye
                        tamamen müziksiz. Fade yok, son akor yok, son kart yok.
                        ⚠️ Bu karar PART_B özetinde zaten kayıtlı:
                          "Müzik S20 sonrası HİÇ YOK, film müziksiz biter ✅"

FREKANS TABANI:         ⚠️ BU FİLMDE SUB-BASS MÜZİKTE YOK.
                        30-60 Hz bandı DİEGETİK GÜMBÜRTÜYE ayrılmıştır
                        (kar oturması sesi — filmin saati). Müzik oraya
                        girerse filmin en önemli sesi maskelenir.
                        Müziğin alt sınırı: 90 Hz. Ağırlık 90-160 Hz'de
                        taşınır → telefon hoparlöründe zaten çalar (§15.1
                        oktav eşlikçisi sorunu bu filmde kendiliğinden çözülür).

KATMANLAR:              4 — aşağıda

LUFS HEDEFİ:            -14 nihai film · -17 müzik yatağı · log altında -6 dB

REVERB KARARI:          Ters yönlü, fizikle motiveli:
                        PART A (dışarıda, 1.4 atm yoğun hava) → uzun, soğuk,
                          GENİŞ yankı. Ses Dünya'dan bile iyi yayılır.
                        PART B (kar altı, S17'den sonra) → yankı ÇÖKER.
                          Kuru, ölü, kapalı. Müzik de onunla birlikte gömülür.
```

---

## 🎹 DÖRT KATMAN

| # | Katman | Neyi temsil eder | Kural |
|:---:|---|---|---|
| 1 | **ALT DRONE** (B1 civarı, 90-160 Hz gövde) | KAR ÇİZGİSİ | 180 saniyede **+1 yarım ses yükselir**. Asla inmez. |
| 2 | **ÜST SABİT TON** (ince yaylı flajole / cam) | HAVA SINIRI | Tek perde. **Hiç değişmez.** Baştan sona aynı. |
| 3 | **BAS KLARNET** — yükselen üç nota motifi | ADAM | Filmde **10 kez** çalar. 11. giriş YOK. |
| 4 | **KURU VURUŞ** — tek, alçak, ahşap-metal darbe | KAZIK / SAYAÇ | Önce 20 saniyede bir, sonra 12 saniyede bir. **Hızlanır.** |

```
KATMAN 3 — MOTİF KURALI (filmin bütün müzikal fikri):
Üç nota. Yükselir. Her dönüşünde bir öncekinin BİTTİĞİ yerden daha
YUKARIDAN başlar ve daha GENİŞ bir aralık tırmanır. Asla inmez, asla
başladığı perdeye dönmez, asla çözülmez.

  Part A (1-7. statement)   yukarı, aralık gitgide genişler
  Part B (8-9. statement)   AYNI motif TERS ÇEVRİLİR ve iner
  S20    (10. statement)    yükselir — ve üçüncü nota gelmeden KESİLİR

⚠️ Aralık genişlemesi = kar çizgisinin hızlanması (40 cm → 1.2 m → 4.1 m).
   Müzik bunu anlatmaz, aynısını yapar.

KATMAN 4 — MICKEY-MOUSING DEĞİL (§13):
Vuruş, ekrandaki çekiç darbelerine ASLA senkron değildir. Kendi sabit
takvimiyle gelir ve kadraja bakmaz. Senkronize edilirse film çizgi filme döner.

KATMAN 1 — 🎨 KURGUDA GARANTİ ALTINA ALINIR:
Suno/Lyria 180 saniyelik +100 sentlik yavaş bir glissandoyu güvenilir
üretmez. Prompta yazılır, ama kurguda drone stem'ine pitch otomasyonu ile
KESİN olarak uygulanır: 0:00'da 0 sent → 3:00'da +100 sent, doğrusal.
Bu, filmin tek vazgeçilmez müzikal olayıdır ve şansa bırakılmaz.
```

---

## 🗺️ MÜZİK HARİTASI — 5 PENCERE, 180 SANİYE, 90 ÖLÇÜ

| Pnc | Ölçü | Süre | **Film içi** | Sahneler | İşlev |
|:---:|:---:|:---:|:---:|---|---|
| — | — | 19s | 0:00 – 0:19 | S0, S1 | 🔇 Hook ve ölçek çekimi **müziksiz**. Çizgi soğuk gelir. |
| **W1** | 20 | 40s | **0:19 – 0:59** | S2–S5 | Motif 1-2-3. Rutin. S5 Overview'da motif **yükselmez** (karşıt ruh hali §7.1). |
| — | — | 8s | 0:59 – 1:07 | S5.5 | 🔇 Konsantratör makro. Ara sahneler müziksizdir. |
| **W2** | 5 | 10s | **1:07 – 1:17** | S6 | Boş koloni. Sadece iki drone, motif yok. |
| — | — | 8s | 1:17 – 1:25 | S6.5 | 🔇 Ranzalar. |
| **W3** | 15 | 30s | **1:25 – 1:55** | S7–S9 | Motif 4-5. Kayıtlar, keşif, hesap. |
| — | — | **18s** | **1:55 – 2:13** | S9.5, S10 | 🔇 **SESSİZLİK SAHNESİ (§10).** Dördüncü teras + yüz. |
| **W4** | 20 | 40s | **2:13 – 2:53** | S11–S14 | Motif 6-7 (tepe), sonra 8: **ilk kez ters çevrilir, iner.** |
| — | — | 8s | 2:53 – 3:01 | S14.5 | 🔇 Geriye sayan kazıklar. |
| **W5** | 30 | 60s | **3:01 – 4:01** | S15–S20 | Motif 9 (iner, dibe vurur). Yankı çöker. Motif 10 **kesilir**. |
| — | — | **56s** | **4:01 – 4:57** | S20.5 → S24 | 🔇🔇 **MÜZİK BİR DAHA HİÇ GİRMEZ.** Film müziksiz biter. |

```
TOPLAM MÜZİK   40+10+30+40+60 = 180 saniye = 90 ölçü  ✅ tam 3:00
TOPLAM SESSİZ  117 saniye (filmin %39'u)
SON 56 SANİYE  müziksiz — kayıtlı karar (PART_B özeti)
```

### 🔁 Beste zamanı ↔ film zamanı (kurgu için zorunlu)

| Pnc | Beste içi | Film içi | Ofset |
|:---:|:---:|:---:|:---:|
| W1 | 0:00 – 0:40 | 0:19 – 0:59 | **+0:19** |
| W2 | 0:40 – 0:50 | 1:07 – 1:17 | **+0:27** |
| W3 | 0:50 – 1:20 | 1:25 – 1:55 | **+0:35** |
| W4 | 1:20 – 2:00 | 2:13 – 2:53 | **+0:53** |
| W5 | 2:00 – 3:00 | 3:01 – 4:01 | **+1:01** |

```
KRİTİK OLAYLARIN İKİ ZAMANI:
  Motifin ters dönmesi (S13 KARAR)      beste 1:40  → film 2:33
  Motif ikinci kez iniyor (S16 KAZMA)   beste 2:14  → film 3:15
  Yankının çökmesi (S17 kuyuya iniş)    beste 2:20  → film 3:21
  Son statement başlıyor (S20)          beste 2:50  → film 3:51
  Üçüncü nota gelmiyor, müzik bitiyor   beste 3:00  → film 4:01

⚠️ Pencere sınırlarının HEPSİ sahne sınırıdır. Kurguda hiçbir pencere
   bir sahnenin ortasında başlamaz veya bitmez.
```

---

# 🎤 ANA MÜZİK PROMPTU

> Suno / Lyria 3 Pro / Stable Audio · **3:00** · enstrümantal · tek seferde
> tek parça. Bölüm bölüm üretilmez (§14.1).

```
A single continuous 3-minute cinematic instrumental score for a hard
science-fiction film set on a frozen mountain planet where the snow line
climbs a few metres every year and never comes back down. Strictly 120 BPM
notated in 4/4, but the FELT pulse is half-time and very slow — one felt beat
every two seconds. Key of B minor, Aeolian. No drums, no drum kit, no beat,
no percussion groove, no trailer braams, no risers, no epic build, no choir,
no vocals, no words.

FOUR LAYERS ONLY:

1. A low sustained drone in the low register, its body sitting between 90 and
160 Hz. It has NO sub-bass below 90 Hz at any point — that band must be left
completely empty. Over the full three minutes this drone RISES in pitch by
one semitone, extremely slowly and continuously, so slowly that it is felt
rather than heard. It never descends, never steps, never returns to where it
started, and it is still rising when the piece ends.

2. A single very thin, very high sustained tone — bowed glass, string
harmonic, or high sine — that NEVER CHANGES. Same pitch, same volume, same
timbre, from 0:00 to 3:00. It does not swell, does not move, does not react
to anything. The whole emotional effect of the piece is the shrinking
distance between this fixed high tone and the slowly rising low drone.

3. A solo bass clarinet, cold and breathy, playing a simple THREE-NOTE RISING
FIGURE. It plays this figure exactly ten times in the whole piece and never
plays anything else. Every time the figure returns it begins HIGHER than
where it last ended, and it climbs a WIDER interval than the time before, so
the climbing accelerates. It never descends in the first two minutes, never
returns to its starting pitch, and never resolves — there is no cadence
anywhere in this piece. Statement timings: 0:04, 0:22, 0:34, 0:52, 1:10,
1:24, 1:34, 1:40, 2:14 and 2:50.
THE ONE EXCEPTION is the statement at 0:34: it begins higher like the others
but it does NOT climb — it repeats its first note three times and stays
completely level. This is the only flat statement in the piece.
At 1:40 the figure is TURNED UPSIDE DOWN for the first time and falls instead
of rising. At 2:14 it falls again, lower, and lands at the bottom of its
range. At 2:50 it rises one last time — and IT IS CUT OFF BEFORE ITS THIRD
NOTE. The third note never arrives. The piece simply stops.

4. A single dry, low, wooden-metal impact — one hit, no reverb tail of its
own, no roll, no kit. It arrives on a fixed schedule that has nothing to do
with the music: once every 20 seconds for the first 100 seconds, then once
every 12 seconds for the rest. It gets faster and it never gets louder.

SPACE — this changes once and the change is the point:
From 0:00 to 2:20 the mix is WIDE and the reverb is LONG, cold and open, as
if the air itself were denser than Earth's and carried sound further than it
should. At exactly 2:20 the reverb COLLAPSES: from that moment to the end the
sound is completely dry, close, enclosed and dead, with no width and no tail,
as if the music had been buried under snow. It never opens back up.

STRUCTURE:
[0:00-0:40] Both drones establish. Bass clarinet figure twice. Sparse, patient.
[0:40-0:50] Drones alone. No clarinet. Emptiness.
[0:50-1:20] Figure returns twice, higher and wider each time. Tension rises
            but nothing swells and nothing gets louder.
[1:20-2:00] The figure reaches its highest point, then at 1:40 inverts and
            falls for the first time.
[2:00-2:20] The figure falls again at 2:14 and bottoms out, still in the
            open wide reverb.
[2:20-3:00] The reverb collapses to nothing and stays dead. Then at 2:50 the
            final rising statement begins and is cut off before its third note.
[3:00]      The piece is CUT at exactly 3:00. No fade out, no final chord, no
            ritardando, no resolution, no closing gesture of any kind.

EMOTION: patient, cold, procedural, inevitable. Not sad, not frightening, not
mysterious, not heroic, not hopeful. It is the sound of a measurement that
keeps coming out the same way. Nothing in this piece ever reacts to anything.

[Instrumental] [No Vocals] [No Lyrics] [No Drums] [No Percussion]
[Sustained] [No Sub-Bass] [Cut ending, no fade]
```

### ⛔ NEGATİF PROMPT

```
drums, percussion, kick, snare, hi-hat, taiko, beat, groove, braams, trailer
hits, risers, epic swell, orchestral tutti, string section, choir, vocals,
lyrics, words, singing, piano melody, arpeggio, synthwave, uplifting, major
key, hopeful, resolution, cadence, final chord, fade out ending, ritardando,
sub-bass, 808, rumble, tempo change, accelerando, shimmer, glowing pad,
ethereal, bloom, lo-fi crackle, wind sound effects, snow sound effects
```

> ⚠️ **Son iki madde önemli:** müzikte rüzgar/kar ses efekti OLMAZ. O katman
> zaten Veo promptlarının içinde diegetik olarak üretiliyor. Müziğe eklenirse
> iki rüzgar üst üste biner ve ikisi de kaybolur.

---

## ✅ ÇIKTI KABUL KRİTERLERİ

```
□ Süre tam 3:00, 3:00'da KESİLİYOR — fade yok
□ 120 BPM sabit, tempo değişimi yok
□ Davul / perküsyon / ritim YOK
□ Vokal, kelime, koro YOK
□ 90 Hz altında enerji YOK  ⚠️ spektrum analiziyle DOĞRULA — bu bant
  diegetik gümbürtüye ayrılmıştır
□ 90-160 Hz'de gövde VAR (telefon hoparlörü testi)
□ Bas klarnet giriş sayısı = 10, fazlası YOK
□ Motif hiçbir yerde çözülmüyor, kadans YOK
□ 2:50'de başlayan son motif üçüncü notasız kesiliyor
□ 2:20'de yankı çöküyor, sonrasında sonuna kadar kuru kalıyor
□ Üst sabit ton baştan sona hiç değişmiyor

🎨 KURGUDA YAPILACAK (üretime bırakılmaz):
□ Drone stem'ine pitch otomasyonu: 0:00 → 3:00 boyunca doğrusal +100 sent
□ 5 pencere yerleştirildi, saniyeler dönüşüm tablosuyla eşleşiyor
□ 1:55 – 2:13 penceresi gerçekten sessiz (-∞, "çok kısık" değil §16)
□ 4:01'den sonra 56 saniye boyunca müzik sıfır — hiçbir kalıntı yok
□ Diyalog sahnelerinde (S2, S8, S11, S18, S20) müzik -6 dB, stem otomasyonu
  ile — ducking DEĞİL. Bas klarnet 2-5 kHz'de dar notch alır.
□ S20'nin 7. saniyesindeki gümbürtü (filmin ses zirvesi) müzikle ÇAKIŞMAZ:
  müziğin son motifi 3:51'de başlar, gümbürtü 3:58'de gelir, müzik 4:01'de
  biter. Üçü de ayrı yerde — sıralama korunmalı.
□ Nihai miks -14 LUFS integrated, true peak ≤ -1 dBTP
□ ⚠️ Ses dosyası üretimden sonra 14 gün içinde yerel diske indirildi
```

---

## 🧩 KILAVUZ DENETİMİ

| Kural | Durum |
|---|---|
| §7.5 Kapanış tersine — çözülme yok, kesme | ✅ Sıfır kadans, son nota hiç gelmiyor |
| §7.1 Karşıt ruh hali | ✅ S5 Overview'da motif yükselmiyor |
| §9 Anempatik müzik | ✅ Hiçbir katman hiçbir olaya tepki vermiyor |
| §10 Sessizlik sahnesi | ✅ S9.5+S10, 18 saniye + son 56 saniye |
| §11 Çözülmeyi geciktirme | ✅ Motif 10 kez çalıyor, 10'unda da çözülmüyor |
| §12 Novum okuması cümlesi | ✅ Künyede, prompttan önce yazıldı |
| §13 Mickey-mousing yasağı | ✅ Vuruş çekiç darbelerine senkron DEĞİL |
| §14 Sahne-ölçü hizası | ✅ 120 BPM — 10s = 5 ölçü, 8s = 4 ölçü |
| §14.1 Tek parça | ✅ 180s tek seferde, sahne sahne değil |
| §15.1 Oktav eşlikçisi | ✅ Müziğin gövdesi zaten 90-160 Hz'de |
| §16 Reverb kararı | ✅ Yoğun hava = geniş / kar altı = ölü |
| §16 LUFS | ✅ -14 / -17 / -6 dB |
```
