# 🎼 THE SECOND SHIP — FRAGMAN MÜZİĞİ · ÜRETİM DOSYASI

## Üç Master · İki Aile · 96 BPM · Sol Minör
### _"Filmin saati iki kat hızlı çalıyor — ama beşli yine açılmıyor."_

> **Bu dosyanın işi:** fragman müziğinin ÜRETİMİNİ tek masada toplamak.
> THE SECOND SHIP'in iki ayrı fragman teslimi var ve müzik tarafında
> İKİ AİLE yazılıdır — kurguda A/B dinlenip biri seçilir (§0.1):
>
> | Aile | Master | Teslim | Kurgu dosyası |
> |---|---|---|---|
> | 🧊 SAKİN | **MASTER T** — 90 s | 9:16 teaser (60 s) + 16:9 varyant (90 s) | `FRAGMAN.md` |
> | 🧊 SAKİN | **MASTER P** — 120 s | 16:9 PRO trailer (2:00, logolu) | `FRAGMAN_PRO_YATAY.md` |
> | 🔥 VURUCU | **MASTER V** — 120 s | üç teslimin ÜÇÜNÜ de karşılar (§4.2) | ikisi de |
>
> **Görev bölüşümü, pazarlıksız:**
> · Kurgu sayıları (TC, EDL, IN/OUT, vuruş haritası) → **kurgu dosyasından** okunur.
> · Beste kararları ve üretim promptları → **bu dosyadan** çalıştırılır.
> T ve P promptları kaynak bölümlerden birebir alınmıştır
> (`FRAGMAN.md` BÖLÜM 3 · `FRAGMAN_PRO_YATAY.md` §11); bir prompt
> değişecekse İKİ YERDE BİRDEN değişir. MASTER V'nin tek kaynağı BU dosyadır.
>
> Filmin kendi bestesi: `MUZIK_VE_SES.md` (330 s · 48 BPM · anempatik).
> Fragman müziği ondan **türer**, onu kopyalamaz ve kurallarını
> kayıtlı sapmalarla bozar (§1).
>
> Referans kılavuz: `../../kilavuzlar_ve_sistem_dosyalari/GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md`
> §12 novum okuması · §14 ölçü hizası · §15.1 oktav eşlikçisi · §16 LUFS · §17 künye

---

# 0. TEK BAKIŞTA — üç master

```
                MASTER T (90 s)        MASTER P (120 s)       MASTER V (120 s)
                ───────────────        ────────────────       ────────────────
AİLE            🧊 sakin               🧊 sakin               🔥 vurucu (epik)
KARAKTER        soğuk, sabırlı,        ağır, kademeli         Marvel bandı:
                tek darbe              build                  vurmalı, vurgulu,
                                                              nefes aldırmayan
RİTİM           yeraltı nabzı          yumuşak tokmak         taiko + timpani +
                (girdap türevi)        perküsyon              staccato ostinato
DARBE           1 (1:20,000)           4 downbeat             her perdede;
                                       (31/35/38/40)          finalde üçlü vuruş
BRAAM/RISER     ⛔ yasak               ⛔ yasak               ✅ serbest (§1 sapma)
KORO            ⛔ yasak               ⛔ yasak               ✅ sözsüz, yalnız doruk
KESME NOKTASI   1:30,000 sert          1:41,875 kesme →       1:41,875 kesme →
                                       G1 yalnız döner        G1 yalnız döner
NİHAİ LUFS      -12 entegre            -14 entegre            -14 entegre (§7)

HER ÜÇÜNDE DE PAZARLIKSIZ — ortak DNA:
  · Tam beşli Sol–Re HİÇBİR YERDE açılmaz (filmin tek çözülmesi S119'da)
  · 96 BPM · 4/4 · 1 ölçü = 2,500 s · Sol minör (Aeolian)
  · Sub G1 49,0 Hz + G2 98,0 Hz + G3 196,0 Hz oktav eşlikçileri (§15.1)
  · Fade out yok — her bitiş kesmedir; button/son vuruş MÜZİKSİZ kalır
  · Söz yok, anlaşılır hece yok
```

## 0.1 A/B KARARI — aile seçimi

```
İKİ AİLE DE ÜRETİLİR — müzik üretimi ucuzdur, A/B meşrudur.
Kurguda ikisi de görüntüye serilir ve BİRİ seçilir.

⛔ AİLELER KARIŞTIRILMAZ: teaser sakin + trailer vurucu (ya da tersi)
   yapılmaz. Üç teslim tek kanalda yaşıyor; iki ayrı müzik kimliği
   markayı böler. Seçilen aile ÜÇ teslime birden uygulanır:
     🧊 seçilirse → T (teaser + dikey montaj) ve P (PRO trailer)
     🔥 seçilirse → V'nin üç kesimi (§4.2)

SEÇİM ÖLÇÜTÜ — zevk değil, iş:
  🧊 sakin aile filmin tonunu birebir taşır; "bu gezegen sabırlı"
     cümlesini müzik de kurar. Risk: ilk 3 saniyede tık üretmeyebilir.
  🔥 vurucu aile tık üretir; nefes kesme işini müzik üstlenir.
     Risk: fragman filmden daha aksiyoncu bir söz verir — film o sözü
     tutmaz (kılavuz FRAGMAN_KILAVUZU §5 ④: kanıtsız söz).
  Karar sahibi: proje sahibi. Bu dosya iki aileyi de eksiksiz hazırlar.
```

**⭐ NOVUM OKUMASI — üç masterdan önce yazıldı, filmin künyesiyle aynı:**

```
"İzleyici topraktan büyüyen ikinci gemiyi bir TEHDİT değil, bir SABIR
olarak okumalı. Bu gezegen saldırmıyor, kaydediyor."

Fragman filmin okumasını değiştirmez, yalnız hızını değiştirir.
MASTER V bu cümleyi RİTİMLE çelmeden taşımak zorundadır: vuruş
"saldırı" değil "yaklaşan adım" gibi duyulmalı — bu yüzden V'de bile
major dönüş, zafer fanfarı ve çözülme YOKTUR. Nefes kesen şey
kapanmayan bir yükseliştir.
```

---

# 1. ⚠️ SAPMA KAYDI — film kurallarından hangi master neyi bozuyor

```
Filmin tek yönetici müzik kuralı: "müzik olaylara tepki VERMEZ,
yalnızca Bekçi'ye tepki verir" (MUZIK_VE_SES.md). ÜÇ MASTER DA bu
kuralı BOZAR: üçü de yükselir, üçü de darbe taşır.

GEREKÇE: Fragman filmin bir parçası değil, filme yapılan bir davettir.
Anempatik bir teaser 60 saniyede tık üretmez; ilk üç saniyede tutmayan
bir trailer anempatik olduğu için değil, izlenmediği için batar.

SAPMA TABLOSU — hangi sınır kimde duruyor:

  SINIR                              T        P        V
  ─────────────────────────────      ──       ──       ──
  ① BEŞLİ AÇILMAZ (Sol–Re)          ✅ durur  ✅ durur  ✅ durur
  ② ENERJİ İÇERİDEN TÜRER            ✅ durur  ✅ durur  ⚠️ BOZULUR
     (nabız = girdap türevi)                            (taiko/timpani
                                                         dışarıdan ithal)
  ③ TRAILER KLİŞESİ YOK              ✅ durur  ✅ durur  ⚠️ BOZULUR
     (braam/riser/taiko/koro)                           (bilinçli — aşağıda)

⚠️ SINIR ② ve ③'ÜN AÇILMA KAYDI (14.08.2026, proje sahibi kararı):
   "Daha Marvel gibi, vurmalı vurgulamalı, nefes kesici" — MASTER V bu
   talebin karşılığıdır. Açılan şey RİTİM VE ORKESTRASYON dilidir;
   açılMAyan şey armonidir: V'de bile beşli kapalı kalır, parça
   çözülmeden biter, son vuruş sessizdir. Marvel'ın "bwaaah"ı gelir,
   Marvel'ın zafer akoru GELMEZ — çünkü o akor filmin finalidir ve
   fragman onu harcayamaz.

⚠️ İZLEYİCİYE VERİLEN SÖZ: sakin ailenin tonu filmde birebir bulunur.
   Vurucu ailenin RİTMİ filmde yoktur — bu, A/B kararının gerçek
   bedelidir ve §0.1'de açıkça yazılıdır. Sapma bir yalan değil,
   kayıtlı bir tercihtir.
```

---

# 2. 🅣 MASTER T — TEASER BESTESİ (🧊 sakin) · 90,000 s

> Kurgu eşlemesi (pencere haritası, katman tablosu, dikey kayma
> uyarısı): `FRAGMAN.md` BÖLÜM 3. Buradaki künye ve promptlar o bölümle
> birebir aynıdır.

## 2.1 Künye

```
PARÇA:          THE SECOND SHIP — FRAGMAN TEMASI · 90,000 saniye
TEMPO:          96 BPM · 4/4 · filmin 48 BPM'inin TAM İKİ KATI
                1 ölçü = 2,500 s → 1 vuruş (10 s) = TAM 4 ÖLÇÜ
                yatay kesim 90 s = 36 ölçü · dikey kesim 60 s = 24 ölçü
TONALİTE:       Sol minör (Aeolian). Tam beşli Sol–Re HİÇ duyulmaz.
                Armoni daima dördüncüye (Do) ya da altıncıya (Mi bemol)
                kayar. Parça çözülmemiş dörtlünün üstünde kesilir.
ÜRETİM:         TEK 90 saniyelik master üretilir. Dikey kesim ondan
                MONTAJLA çıkar — ayrı parça üretilmez (§14.1).
DARBE:          1:20,000'de tek sub darbe. Parçanın tek vurma olayı.
KAPANIŞ:        Fade YOK. 1:30,000'da sert kesme.
FREKANS TABANI: sub G1 49,0 Hz + G2 98,0 Hz + G3 196,0 Hz
LUFS:           -12 entegre · true peak -1,0 dBTP (gerekçe §7)
```

## 2.2 İki kesim, tek master — montaj reçetesi

```
YATAY KESİM (90 s):  masterın tamamı, 0:00 → 1:30
DİKEY KESİM (60 s):  0:00 – 0:20  +  0:50 – 1:30
                     ✂️ birleşme noktası: 0:20,000 ↔ 0:50,000

⭐ 0:20'de yalnız sub drone ve granüler doku çalar; 0:50'de nabız ve
   yaylı küme zaten devrededir. Dikey kesimde bu ikisi tek karede
   birden girer ve bir "drop" gibi okunur — tam dikey S1 (ATIŞ)
   vuruşunun üstüne.

⚠️ BESTE KABUL ŞARTI: 0:20,000 ve 0:50,000'in İKİSİ DE ölçü başıdır
   ve ikisinde de armoni aynı akordadır (Sol minör pedal). Üretilen
   parçada bu iki koşuldan biri tutmuyorsa parça REDDEDİLİR — dikey
   kesim dikişli duyulur.

⚠️ HİZALAMA: darbe dikey kesimde tam 50,000'e düşer ve dikey S5
   (BİRİ DÖNÜYOR) tam orada başlar. Kayma varsa müzik değil GÖRÜNTÜ
   kaydırılır (kılavuz §14 madde 3).
```

## 2.3 🎧 Global prompt (tek parça · 90 saniye)

```
GLOBAL TRAILER SCORE PROMPT — THE SECOND SHIP (TEASER)

Instrumental cinematic teaser score, exactly 90 seconds, one continuous
unbroken piece with no fade in and no fade out.

TEMPO AND KEY: 96 BPM, 4/4, G minor (Aeolian). One bar equals 2.5 seconds.
CRITICAL HARMONIC RULE: the perfect fifth G–D is NEVER sounded anywhere in
this piece, not even at the climax. The harmony always slips to the fourth
(C) or the sixth (E flat) instead of resolving. The piece ends unresolved.

WHAT THIS IS: a patient, cold, slow-building teaser cue for a science
fiction film about a planet that copies whatever rests on it. It builds,
but it never becomes heroic, never becomes triumphant and never becomes
frightening. It should feel like something enormous being patient.

LAYERS, in order of entry:
1. From the very first second and in every single bar: a sustained
   sub-bass drone on G, never changing pitch and never changing volume,
   doubled one and two octaves up (49 Hz, 98 Hz, 196 Hz) so it survives on
   a phone speaker.
2. From 0:10: a dry granular stone texture — fine, grainy, dusty, like
   small mineral particles settling on hard stone. Non-pitched, quiet,
   slightly irregular, no reverb tail.
3. From 0:20: a low sustained string cluster of exactly three notes that
   never resolve to the tonic and never move to a cadence. They hang
   unfinished for the rest of the piece.
4. From 0:30: a deep, soft-attack pulse in the 40 to 90 Hz range — a
   subterranean thud, not a drum, with no snap, no click and no room
   sound, as if it comes from under the ground. It enters as half notes at
   0:30, doubles to quarter notes at 0:40, and doubles again to eighth
   notes at 1:00.
5. From 0:50: a single wordless human vocal tone, one held note at a time,
   processed as if replayed through a very old degraded tape machine —
   band-limited, slight wow and flutter, soft tape hiss. No words, no
   syllables, no melody, no choir, no vocal harmony. One tired human tone.
6. At 1:00 only, and only once in the whole piece: a solo viola, warm and
   human but restrained, playing a slow rising figure of five notes that
   STOPS BEFORE ITS FINAL NOTE and does not return.

STRUCTURE, exact:
- 0:00 to 0:10 — drone alone. Nothing else. Almost empty.
- 0:10 to 0:50 — layers enter one at a time exactly as listed above, each
  on a bar line, each arriving without a swell and without a crescendo
  into it. Density increases; volume increases only slightly.
- 0:50 to 1:10 — the emotional centre: the degraded human vocal tone over
  the accelerating pulse, with the viola's unfinished phrase at 1:00. This
  is the densest passage in the piece.
- 1:10 to 1:20 — SUDDEN REMOVAL: the pulse and the string cluster cut out
  completely on the bar line at 1:10. Only the drone, the granular texture
  and the degraded vocal tone remain. Ten seconds of near-emptiness.
- 1:20 exactly — ONE single deep sub-bass impact, the only percussive
  event in the entire piece. It lands on the downbeat, on an unresolved
  G–C fourth, and decays naturally.
- 1:20 to 1:30 — the impact decays and the degraded human vocal tone is
  left alone over the drone. At 1:30.000 the piece STOPS ABRUPTLY on the
  unresolved fourth. No fade, no repeat, no final chord, no tail.

EDIT REQUIREMENT — the piece must be cuttable: the moments at 0:20.000 and
at 0:50.000 must both fall exactly on a bar line and must both sit on the
same G minor pedal harmony, so that an editor can splice 0:20 directly to
0:50 without a harmonic seam.

MIX AND SPACE: extremely dry. Almost no reverb anywhere. No large hall, no
cathedral, no ambience wash. Wide low end, narrow high end. Nothing above
8 kHz is prominent.

STRICTLY EXCLUDE: drums, drum kit, snare, snare rolls, taiko, timpani,
cymbals, hi-hats, electronic kick drums, trailer hits, braams, risers,
downers, reverse whooshes, orchestral swells, crescendos into silence,
choir, lyrics, spoken word, synth arpeggios, ostinato patterns, pulsing
eighth-note synths, piano, guitar, brass fanfare, sci-fi laser sounds,
heartbeat samples, ticking clocks, breathing sounds, glitch edits, key
changes, tempo changes, and any moment that feels triumphant, heroic,
menacing, scary or action-driven.
```

## 2.4 🎹 Suno / Udio promptu (kısa alan sürümü)

```
SUNO STYLE PROMPT:

instrumental, cinematic teaser score, 96 bpm, G minor, cold, patient,
slow build, sub-bass drone, dry granular stone texture, subterranean soft
pulse accelerating, three-note unresolving string cluster, wordless
degraded tape vocal tone, one solo viola phrase that stops before its last
note, single sub impact near the end, extremely dry mix, no reverb, no
drums, no snare, no taiko, no braams, no risers, no trailer hits, no
choir, no lyrics, no synth arpeggio, never triumphant, never heroic, never
scary, ends abruptly on an unresolved fourth

METATAGS:
[Intro: sub drone alone, almost empty]
[Granular stone texture enters, very quiet]
[Three-note string cluster enters, unresolving]
[Subterranean pulse enters as half notes]
[Pulse doubles to quarter notes]
[Degraded wordless human vocal tone enters, tired]
[Pulse doubles to eighth notes — densest passage]
[Solo viola rises and stops before its final note]
[Pulse and strings cut out — near silence]
[One single sub impact]
[Vocal tone alone over drone, hard stop, no fade]
[End]
```

---

# 3. 🅟 MASTER P — PRO TRAILER BESTESİ (🧊 sakin) · 120,000 s

> Kurgu eşlemesi (48 ölçülük harita, sting/kapanış blokları, sessizlik
> bütçesi): `FRAGMAN_PRO_YATAY.md` §9–§11. Global prompt oradan birebir;
> Suno kısa sürümü ve stem teslimi bu dosyada yazılıdır.

## 3.1 Künye

```
PARÇA:          THE SECOND SHIP — PRO TRAILER CUE · 120,000 saniye
TEMPO:          96 BPM · 4/4 · 1 ölçü = 2,500 s · toplam 48 ölçü
YAPI:           4 ölçü sting + 40 ölçü gövde + 4 ölçü kapanış
                (sting ve kapanış APEXAIC logo bloklarının altıdır;
                 blok zamanlamaları FRAGMAN_PRO_YATAY.md §9–§10)
TONALİTE:       Sol minör · tam beşli Sol–Re HİÇBİR YERDE açılmaz ·
                armoni askıda dörtlüde kalır ve çözülmeden biter
KESME:          1:41,875'te müzik KESİLİR — fade değil, kesme.
                Button (C27) tamamen müziksizdir.
SESSİZLİK:      1:41,875 – 1:53,000 arası 11,125 s müziksiz (%9,3) —
                bilinçli; filmin temasında sessizlik zaferin kendisidir.
KAPANIŞ:        1:53,000'de yalnız G1 döner, tek başına, çözülmeden
                söner ve 2:00,000'de biter.
FREKANS TABANI: sub G1 49,0 Hz + G2 98,0 Hz + G3 196,0 Hz
                (sting'in 38 Hz sub swell'i bir İSTİSNADIR: yalnız
                 0:00–0:06,5 arasında yaşar ve tek başına duygu
                 taşımaz — üstüne 60 Hz darbe ve G1 gelir)
LUFS:           -14 entegre · true peak -1,0 dBTP (gerekçe §7)
```

## 3.2 🎧 Global prompt (tek parça · 120 saniye)

```
A single continuous cinematic trailer cue, 120 seconds, 96 BPM, 4/4,
G minor, dark science-fiction, patient and heavy.

BARS 1-4 — a deep 38 Hz sub swell rises alone out of silence; a single
soft low impact lands at bar 3; one sustained low string note on G
enters and holds.

BARS 5-11 — the sustained G continues as a pedal tone beneath a very
low room hum. No melody, no percussion, no movement. Space and dread.

BARS 12-19 — a single low cello figure enters over the pedal, four
bars apart, sparse and unhurried. Still no percussion.

BARS 20-30 — soft mallet percussion enters low in the mix and builds
bar by bar; layered low strings thicken; the pedal never leaves.

BARS 31-40 — full weight: low brass swells, mallet pattern tightens,
impacts land on the downbeat of bars 31, 35, 38 and 40. Maximum
density and maximum tension.

END OF BAR 40 — the cue stops dead. Not a fade, a hard stop.

BARS 41-44 — after four and a half bars of complete silence, the same
single sustained low G returns alone and decays into nothing.

CRITICAL HARMONIC RULE, absolute: the perfect fifth G-D is never
sounded anywhere in this cue. The harmony stays on an unresolved
suspended fourth throughout and never resolves. The piece ends
unresolved.

No vocals, no lyrics, no choir, no whooshes, no risers, no braams,
no bass drops, no electronic synth leads, no drum kit, no cymbals,
no reverse cymbals, no sound-effect stingers.
```

## 3.3 🎹 Suno / Udio promptu (kısa alan sürümü)

```
SUNO STYLE PROMPT:

instrumental, cinematic trailer cue, 96 bpm, G minor, dark science
fiction, patient and heavy, deep sub-bass swell opening, sustained low
string pedal on G, single sparse low cello figure, soft mallet
percussion building bar by bar, layered low strings thickening, low
brass swells at full weight, heavy downbeat impacts, sudden hard stop,
long dead silence, one low G string note returns alone and decays,
extremely dry mix, no vocals, no lyrics, no choir, no whooshes, no
risers, no braams, no bass drops, no synth leads, no drum kit, no
cymbals, never resolves, ends unresolved

METATAGS:
[Intro: deep sub swell out of silence, one soft low impact, low G enters]
[G pedal alone over very low room hum — no melody, no percussion]
[Single low cello figure, four bars apart, sparse and unhurried]
[Soft mallet percussion enters low, builds bar by bar, strings thicken]
[Full weight: low brass swells, mallet tightens, downbeat impacts]
[Hard stop — dead silence, no fade]
[Single sustained low G returns alone, decays into nothing]
[End]

⚠️ Metatag sırası §3.2'deki ölçü bloklarını birebir izler; Suno bölüm
   sürelerini garanti etmez — kesme noktası (1:41,875) tutmuyorsa
   kurguda GÖRÜNTÜ kaydırılmaz, parça yeniden üretilir: buradaki tek
   sabit nokta budur ve stem'le düzeltilemez.
```

---

# 4. 🅥 MASTER V — VURUCU SÜRÜM (🔥 epik trailer) · 120,000 s

> **Bu masterın tek kaynağı bu dosyadır.** 14.08.2026 kararıyla açıldı:
> "daha Marvel gibi, vurmalı vurgulamalı, nefes kesici." Sapma kaydı §1.
>
> V, P'nin yerine geçen bir A/B alternatifidir ve TEK üretimle üç
> teslimi de karşılar: PRO trailer 120 s (tamamı) + yatay teaser 90 s
> + dikey teaser 60 s (montaj reçetesi §4.2).

## 4.1 Künye

```
PARÇA:          THE SECOND SHIP — EPIC TRAILER CUE · 120,000 saniye
TEMPO:          96 BPM · 4/4 · 1 ölçü = 2,500 s · toplam 48 ölçü
YAPI:           4 ölçü sting + 40 ölçü gövde + 4 ölçü kapanış
                ⭐ STING VE KAPANIŞ P İLE BİREBİR AYNI SES YATAĞIDIR
                (APEXAIC marka bloğu filme/mastera göre değişmez —
                 FRAGMAN_PRO_YATAY.md §9: "değişkense marka değildir")
TONALİTE:       Sol minör · ⛔ tam beşli Sol–Re V'DE DE açılmaz.
                Yükseliş ritimden ve orkestrasyondan gelir, çözülmeden
                değil. Askıda dörtlü; parça çözülmeden biter.
DİL:            hibrit orkestral trailer — taiko topluluğu, timpani,
                staccato yaylı ostinato, alçak bakır, braam, riser,
                sözsüz karanlık koro (yalnız dorukta)
DARBE HARİTASI: ölçü 12 · 16 · 20 · 24 · 28 downbeat + braam 9 · 31 · 35
                + ölçü 40'ta ÜÇLÜ final vuruşu (1., 3., 4. vuruş)
KESME:          1:41,875'te müzik KESİLİR — fade değil, kesme.
                Button V'de de tamamen müziksizdir. Nefes kesmenin son
                hamlesi gürültü değil, gürültünün ANİDEN yok olmasıdır.
KAPANIŞ:        1:53,000'de yalnız G1 döner, tek başına, çözülmeden.
FREKANS TABANI: sub G1 49,0 Hz + G2 98,0 Hz + G3 196,0 Hz
LUFS:           -14 entegre · true peak -1,0 dBTP (gerekçe §7)
                ⚠️ "Daha gür" diye -14'ün üstüne ÇIKILMAZ — YouTube
                   kısar ve vuruşların dinamiği ölür. Vuruş gürlükten
                   değil, KONTRASTTAN gelir.
MİKS:           P'den daha geniş — kısa salon kuyruğu serbest (0,8 s'ye
                kadar), ama katedral/wash yok; alçaklar mono uyumlu.
```

## 4.2 Üç kesim, tek master — montaj reçetesi

```
PRO TRAILER (120 s):  masterın tamamı, 0:00 → 2:00
YATAY TEASER (90 s):  0:10 → 1:40 (gövde, ölçü 5–40) + kurguda sonuna
                      kapanış G1 stem'inden 0–2 s kuyruk; sert kesme
                      korunur. Sting'siz açılış = teaser'ın kendi
                      soğuk açılışı.
DİKEY TEASER (60 s):  0:10 – 0:40 (ölçü 5–16, build)
                      + 1:10 – 1:40 (ölçü 29–40, tam enerji)
                      ✂️ birleşme: 0:40,000 ↔ 1:10,000

⭐ DİKEY BİRLEŞME NOKTASI T İLE AYNI MANTIK: 0:40'ta build henüz
   ölçülü; 1:10'da ostinato ve perküsyon tam yükte. Sıçrama bir
   "drop" gibi okunur — dikey S3 (KABARAN ZEMİN) → S4 (İKİNCİ GEMİ)
   geçişinin üstüne düşer.

⚠️ BESTE KABUL ŞARTI: 0:40,000 ve 1:10,000'in İKİSİ DE ölçü başıdır
   ve ikisinde de zemin aynı Sol minör pedaldadır. Tutmuyorsa dikey
   kesim çıkarılamaz → parça REDDEDİLİR.

⚠️ HİZALAMA: V seçilirse dikey teaser'ın kurgusu darbeye göre kayar:
   ölçü 31 braam'ı (master 1:15,000 → dikey TC 0:35,000) dikey S4'ün
   ilk karesine, ölçü 40 üçlü vuruşu (dikey TC 0:57,5–1:00) S5'in
   son saniyelerine oturtulur. Kayma varsa müzik değil GÖRÜNTÜ
   kaydırılır.
```

## 4.3 🎧 Global prompt (tek parça · 120 saniye)

```
GLOBAL EPIC TRAILER SCORE PROMPT — THE SECOND SHIP (MASTER V)

A single continuous hybrid-orchestral epic trailer cue, 120 seconds,
96 BPM, 4/4, G minor, dark science-fiction. Relentless, percussive,
breath-taking — modern blockbuster trailer language — but it NEVER
turns triumphant, never turns major, and never resolves.

BARS 1-4 — identical opening bed to a minimal logo sting: a deep 38 Hz
sub swell rises alone out of silence; a single soft low impact lands at
bar 3; one sustained low string note on G enters and holds. No epic
elements yet.

BARS 5-11 — the G pedal continues. A deep taiko heartbeat enters
immediately: two heavy soft hits per bar, patient, like approaching
footsteps. At bar 9, one distant dark braam, long and low, decaying
slowly. Tension, not action.

BARS 12-19 — a staccato low-string ostinato in driving eighth notes
enters and locks to the taiko. Short dark low-brass swells answer every
four bars. Orchestral impact hits land on the downbeats of bars 12 and
16. Through bars 18-19 a slow riser climbs underneath.

BARS 20-30 — full taiko ensemble takes over: rolling, layered,
relentless. Timpani doubles the downbeats. The string ostinato tightens
and rises in register. French horns and low brass state short minor
theme fragments that never complete. Impact hits on the downbeats of
bars 20, 24 and 28. A long riser builds through bars 29-30 into the
final section.

BARS 31-40 — maximum force: a huge braam on the downbeat of bar 31 and
another on bar 35, a dark wordless low choir swelling underneath, the
ostinato doubling to sixteenth notes, timpani rolls, massive orchestral
hits on the downbeats of bars 31, 35 and 38. Bar 40 is a TRIPLE HIT:
three colossal impacts on beats one, three and four.

END OF BAR 40 — the cue stops DEAD on the last hit. Not a fade, not a
decay — a hard stop into absolute silence.

BARS 41-44 — after the long silence, the same single sustained low G
returns alone, small and cold, and decays into nothing.

CRITICAL HARMONIC RULE, absolute: the perfect fifth G-D is never
sounded anywhere in this cue, not even inside the biggest hits. The
harmony stays on an unresolved suspended fourth (G-C) or slips to the
sixth (E flat). No major chords, no heroic cadence, no resolution. The
piece ends unresolved.

EDIT REQUIREMENT — the piece must be cuttable: the bar lines at
0:40.000 and 1:10.000 must both sit on the same G minor pedal so an
editor can splice 0:40 directly to 1:10 without a harmonic seam.

MIX AND SPACE: wide and powerful but controlled — short hall tails up
to 0.8 seconds on percussion and brass, no cathedral wash. The sub
layer is doubled at 49, 98 and 196 Hz and stays mono-compatible.
Impacts get contrast from the arrangement dropping around them, not
from limiting.

STRICTLY EXCLUDE: lyrics, intelligible words or syllables, solo vocals,
drum kit, snare rolls, hi-hats, electronic kick patterns, EDM drops,
dubstep wobble, synth leads, glitch edits, sci-fi laser sounds,
heartbeat samples, ticking clocks, major-key turns, heroic fanfares,
any resolved final chord, key changes, tempo changes, fade-outs.
```

## 4.4 🎹 Suno / Udio promptu (kısa alan sürümü)

```
SUNO STYLE PROMPT:

instrumental, epic hybrid orchestral trailer cue, 96 bpm, G minor, dark
science fiction, relentless and breath-taking, deep sub swell opening,
taiko heartbeat like approaching footsteps, dark distant braams,
driving staccato low string ostinato, short dark low brass swells,
full taiko ensemble with timpani, massive downbeat orchestral hits,
long risers, dark wordless low choir at the climax, triple hit finale,
sudden dead stop into silence, single cold low G returns alone and
decays, no lyrics, no drum kit, no snare, no hi-hats, no EDM drop, no
synth leads, no major chords, no heroic fanfare, never resolves, ends
unresolved

METATAGS:
[Intro: deep sub swell out of silence, one soft low impact, low G enters]
[Taiko heartbeat enters, two heavy hits per bar — approaching footsteps]
[Distant dark braam, long and low]
[Staccato low string ostinato locks to the taiko, hits on downbeats]
[Low brass answers, slow riser underneath]
[Full taiko ensemble, timpani doubles downbeats, ostinato tightens]
[Long riser into the final section]
[Maximum force: braam, dark wordless choir, sixteenth-note ostinato]
[Massive downbeat hits, timpani rolls]
[TRIPLE HIT finale — then dead stop, absolute silence]
[Single cold low G returns alone, decays into nothing]
[End]

⚠️ Metatag sırası §4.3'ün ölçü bloklarını izler. Kesme noktası
   (1:41,875 = üçlü vuruşun sonu) tutmuyorsa parça yeniden üretilir —
   §3.3'teki kural V için de geçerlidir: bu nokta stem'le düzeltilemez.
```

---

# 5. 🌊 GOOGLE FLOW / LYRIA — ZEMİN KATMANI · üç master için TEK üretim

```
Sub drone + granüler doku zemini transient içermez → tek 2 dakikalık
üretim ÜÇ masterın da altına serilir ve kurguda kesintisiz uzatılır/
kısaltılır. Ayrı ayrı üretilmez. (V'de zemin, vuruşların arasındaki
boşlukları doldurur — vuruş sustuğunda gezegen hâlâ oradadır.)
```

```
FLOW / LYRIA PROMPT — SUB LAYER ONLY:

A single sustained sub-bass drone on the note G, 2 minutes long,
absolutely unchanging in pitch and in volume from the first second to the
last. Doubled at 49 Hz, 98 Hz and 196 Hz. No melody, no rhythm, no
movement, no swell, no modulation, no filter sweep, no evolution, no
arrival, no ending.

Over it, a very quiet dry granular texture: fine mineral grains settling on
stone, non-pitched, irregular, no reverb, no tail, never rhythmic.

No instruments, no percussion, no voice, no reverb, no ambience wash, no
sci-fi atmosphere pads, no cinematic swells. This is a floor, not a piece
of music, and it must never draw attention to itself.
```

---

# 6. ⛔ RED KRİTERLERİ — üretilen parça bu kapılardan geçmeden kurguya girmez

```
ÜÇ MASTER İÇİN ORTAK — biri varsa parça REDDEDİLİR, yeniden üretilir:
 ① söz, anlaşılır hece ya da solo vokal
 ② sonda ya da herhangi bir yerde çözülen tam beşli (Sol–Re)
    — ⛔ EN KRİTİK KONTROL. Kulakla yapılır: parça bitiminde
    "kapandı" hissi VARSA parça yanlıştır. Doğru parça askıda biter.
    V'de darbelerin İÇİ de dinlenir — büyük hit'lerin altına model
    sıklıkla tam akor gömer.
 ③ fade out — her master kesmeyle biter
 ④ MONO KONTROLÜ: miks mono'ya indirilince zemin kaybolmamalı.
    Telefon hoparlörü testi: zemin G2'den (98 Hz) taşınmalı;
    49 Hz telefonda YOK, tek taşıyıcı olamaz (§15.1).
 ⑤ major dönüş / kahramanlık kadansı — üç masterda da yasak

SAKİN AİLEYE (T + P) ÖZEL:
 ⑥ herhangi bir davul seti / trampet / taiko / zil sesi
 ⑦ braam, riser, ters whoosh, bass drop
 ⑧ koro
 ⑨ T: 0:20,000 ve 0:50,000 ölçü başında mı, ikisi de Sol minör
    pedalda mı (değilse dikey kesim çıkarılamaz — §2.2)
 ⑩ T: 1:20,000 darbesi parçanın TEK vurma olayı mı; erken/geç ya da
    ikinci darbe varsa RED
 ⑪ T: nabız katmanı davul gibi mi duyuluyor — transient sert, atak
    hızlıysa RED (yeraltı, oda değil)
 ⑫ P: kesme gerçekten ÖLÜ mü — reverb kuyruğu kalıyorsa RED

VURUCU AİLEYE (V) ÖZEL:
 ⑬ darbeler downbeat'e oturuyor mu — off-beat'e kayan hit'li parça
    kurguda hizalanamaz, RED
 ⑭ ölçü 40 üçlü vuruşu net üç ayrı hit mi — tek bulamaç crescendo
    ise RED
 ⑮ kesme ÖLÜ mü: üçlü vuruşun son hit'inden sonra kuyruk, şınlama,
    salon sönümü YOK — button'ın sessizliği V'nin asıl silahıdır
 ⑯ drum kit / hi-hat / EDM drop sızmış mı — hibrit orkestral kalmalı
 ⑰ koro sözsüz ve YALNIZ dorukta mı (ölçü 31-40 dışında koro RED)
 ⑱ 0:40,000 ↔ 1:10,000 dikiş şartı tutuyor mu (§4.2)
```

---

# 7. 🎚️ MİKS, STEM VE TESLİM

## 7.1 LUFS hedefleri

```
MASTER T   -12 LUFS entegre
           Teaser tek başına, telefonda, sessize alınabilir bir dikey
           akışta çalıyor — FRAGMAN.md künyesinin kararı, film
           hedefinden 2 LUFS yüksek.
MASTER P   -14 LUFS entegre
MASTER V   -14 LUFS entegre
           İkisi de YouTube'a gidiyor; platform ~-14'e normalize eder
           (kılavuz §16). V'de "daha gür" isteği limiter'la DEĞİL
           aranjmanla çözülür: vuruş anında diğer katmanlar çekilir,
           kontrast vuruşu büyütür.
FİLM       -14 LUFS (MUZIK_VE_SES.md) — hedefler birbirine karışmaz.
⚠️ V'nin dikey 60 s kesimi teaser olarak çıkarsa o KESİM -12'ye
   yeniden masterlanır (T ile aynı gerekçe).
```

## 7.2 Stem tabloları

```
MASTER T — 8 stem · 48 kHz / 24 bit WAV · toplam 90.000 ms
  1. sub drone        (transient yok → kesintisiz uzatılabilir)
  2. granüler doku
  3. nabız            ← ⚠️ AYRI ŞART: atış boşluğu bu stem'de kesilir
  4. yaylı küme
  5. bantlı vokal tonu
  6. viyola
  7. sub darbe        (tek olay, ayrı stem — kurguda 1 kare hassas)
  8. girdap           ← müzik değil, ses tasarımı; ayrı stem şart

  Seviyeler: nihai -12 LUFS · darbe tepe ≤ -3 dBTP · girdap -20 LUFS

MASTER P — 7 stem · 48 kHz / 24 bit WAV · toplam 120.000 ms
  1. sub drone + sting swell   (38 Hz swell yalnız 0:00–0:06,5)
  2. yaylı pedal + katmanlı alçak yaylılar
  3. çello figürü
  4. tokmak perküsyon
  5. alçak bakır
  6. darbeler                  (ölçü 31/35/38/40 downbeat — ayrı stem)
  7. girdap
  ⚠️ kapanış G1'i ayrı dosya olarak da teslim edilir: logo bloğu
     kurgusu (Blok Z) müzik kurgusundan bağımsız kayabilir.

  Seviyeler: nihai -14 LUFS · darbe tepe ≤ -3 dBTP · girdap -18 LUFS

MASTER V — 9 stem · 48 kHz / 24 bit WAV · toplam 120.000 ms
  1. sub drone + sting swell
  2. yaylı pedal
  3. staccato ostinato yaylılar
  4. taiko + timpani
  5. alçak bakır + korno
  6. braam'lar                 (3 olay: ölçü 9 · 31 · 35 — ayrı stem,
                                kurguda 1 kare hassas)
  7. hit'ler + üçlü final      (ayrı stem — dikey kesim hizası bununla
                                yapılır, §4.2)
  8. koro (sözsüz)
  9. riser'lar                 (ayrı stem — kurgu isterse riser'ı kısar,
                                masterı bozmadan)
  girdap → ses tasarımı stem'i olarak V'ye de aynen serilir (-18 LUFS)

  Seviyeler: nihai -14 LUFS · hit tepe ≤ -3 dBTP · braam tepe ≤ -6 dBTP
  ⚠️ kapanış G1 ayrı dosya — P ile aynı sebep.
```

## 7.3 Üretim sonrası ayrıştırma

```
Suno/Udio stem vermezse: UVR5 · Overlap 0.85 · Spectral Inversion açık
(kılavuz §5). Darbe/braam stem'i temiz ayrılmıyorsa o olayı ayrı bir
tek-olay üretimiyle al ve kurguda bindir — masterı yeniden üretmekten
ucuzdur. V'de bu neredeyse kesin gerekecek: hit kütüphanesi ayrı üret,
downbeat'lere kurguda oturt.
```

---

# 8. 🔊 MÜZİK DIŞI SES — fragmanla paylaşılan kilitler

> Ses tasarımının tamamı kurgu dosyalarında yazılıdır
> (`FRAGMAN.md` BÖLÜM 3 ses tasarımı bloğu · `FRAGMAN_PRO_YATAY.md`
> §11.4). Burada yalnız MÜZİKLE KESİŞEN üç kilit tekrarlanır, çünkü
> üçü de beste/miks kararıdır:

## 8.1 Atış boşluğu — hangi ailede nasıl

```
Atış anında (dikey S1 / yatay Y3 / PRO C8→C9) TAM SESSİZLİK; tam
1,00 saniye sonra boğuk basınç darbesi (40–90 Hz).
  T'de: nabız o saniyede TEK VURUŞ ATLAR — nabız stem'inde kesilir.
  V'de: ostinato ve taiko o saniyede SUSAR ve boşluğun sonundaki
        basınç darbesi bir hit'le çakıştırılır — V'nin en ucuz
        "nefes kesme" anı budur: gürültünün içinde bir saniyelik delik.
Bilinçli mickey-mousing'dir: atışın gecikmesi filmin ses imzasıdır.
```

## 8.2 Girdap — müziğin altındaki diegetik saat

```
Girdap müzik DEĞİLDİR; ayrı stem şarttır ve ÜÇ masterın altına da
serilir. T'nin nabzı girdap türevidir; V'nin taiko'su DEĞİLDİR (§1
sapma ②) — bu yüzden V'de girdap, taiko sustuğu anlarda duyulur ve
seyirciye "vuruş bitse de gezegen sayıyor" der.
MASTER P/V altında: FRAGMAN_PRO_YATAY.md §11.4'teki hızlanan zaman
listesi geçerlidir; 1:45,500'deki TEK vuruş, müzik olmadığı için ilk
kez tam duyulur.
```

## 8.3 İnsan sesi bütçesi

```
Dikey teaser'da HİÇBİR insan sesi yok (anons yalnız yatay Y2'de;
PRO'da yalnız iki replik: C6 "QUARANTINE. DO NOT LAND." · C22 "DO
NOT."). V'nin korosu SÖZSÜZDÜR ve dorukla sınırlıdır — Bekçi'nin bant
bozulmuş ses kimliğiyle karışmaz; koro geniş ve derin, Bekçi dar bantlı
(300 Hz–3,4 kHz) kalır. Miks ikisini aynı kadraja sokmaz.
```

---

# 9. ✅ ÜRETİM SIRASI VE KONTROL LİSTESİ

```
SIRA — ucuzdan pahalıya:
 1. LYRIA ZEMİN (§5)         tek üretim, üç mastera da hizmet eder
 2. MASTER T (§2)            sakin ailenin teaser'ı · §6 kapıları ①–⑤ + ⑥–⑪
 3. MASTER V (§4)            vurucu aile · §6 kapıları ①–⑤ + ⑬–⑱
 4. 🅰🅱 AİLE SEÇİMİ (§0.1)   T ve V kurguda görüntüye serilir, dinlenir,
                             proje sahibi seçer. Seçim ÜÇ teslimi bağlar.
 5a. 🧊 seçildiyse           MASTER P üretilir (§3, kapılar ⑫ dahil) +
                             T'nin dikey 60 s montajı (§2.2)
 5b. 🔥 seçildiyse           V'nin 90 s ve 60 s kesimleri çıkarılır
                             (§4.2) · dikey kesim -12'ye masterlanır (§7.1)
 6. Stem teslimi (§7.2)      eksik stem varsa UVR5 / hit kütüphanesi (§7.3)
 7. Kurguya teslim           hizalama kuralı: kayma varsa müzik değil
                             GÖRÜNTÜ kaydırılır — tek istisna kesme
                             noktaları (§3.3 / §4.4): yeniden üretim

KONTROL LİSTESİ:
 □ Novum okuması cümlesi prompttan önce okundu mu                (§0)
 □ 96 BPM ızgarası: T 36 ölçü / P·V 48 ölçü, bloklar ölçü başında mı
 □ Beşli kontrolü kulakla yapıldı mı — ÜÇ masterda da, V'de
   hit'lerin içi dahil                                           (§6 ②)
 □ T: 0:20/0:50 dikiş şartı                                      (§2.2)
 □ V: 0:40/1:10 dikiş şartı                                      (§4.2)
 □ T: darbe tam 1:20,000'de ve tek mi                            (§6 ⑩)
 □ P/V: kesme ölü mü, button tamamen sessiz mi                   (§6 ⑫/⑮)
 □ V: darbeler downbeat'te mi, üçlü final üç ayrı hit mi         (§6 ⑬⑭)
 □ V: koro sözsüz ve yalnız dorukta mı                           (§6 ⑰)
 □ Kapanış G1 tek başına mı, D yok mu — P ve V                   (§3.1/§4.1)
 □ Mono/telefon testi geçti mi                                   (§6 ④)
 □ LUFS: T -12 / P -14 / V -14 · true peak -1,0 dBTP             (§7.1)
 □ Girdap ayrı stem mi, müziğe karışmadı mı                      (§8.2)
 □ Fade out hiçbir teslimde yok mu
 □ Aile seçimi yapıldı mı ve üç teslim aynı ailede mi            (§0.1)
```

---

> **Bu dosya ne zaman güncellenir**
> □ T veya P promptu değişirse → kaynak kurgu dosyasıyla BİRLİKTE
>   (`FRAGMAN.md` BÖLÜM 3 · `FRAGMAN_PRO_YATAY.md` §11) — tek başına değil
> □ V promptu değişirse → yalnız burada (tek kaynak bu dosyadır)
> □ Aile seçimi yapılınca → §0.1'e seçim + tarih yazılır, seçilmeyen
>   ailenin bölümleri SİLİNMEZ (başına ⏸️ RAFTA yazılır)
> □ Master üretilip red/kabul kararı çıkınca → §6'ya ölçülmüş yeni kapı
