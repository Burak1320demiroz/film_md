```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_COLD_WELD
mercek    : ⑧ EFOR
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_COLD_WELD_QA_SPEC.md  (aile: yatay)
üretildi  : 02.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_2_4_dk_filmler_uzay/THE_COLD_WELD
belge: A (sahne haritası) + C (kilitler). ⛔ FATURA CÜMLESİ önce EKRANDAN. ⚠️ Düşük yerçekimi düşük efor değildir — kütle ve atalet değişmez
```

# ⑧ EFOR QA — EFFORT & BODILY COST CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑧. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **EFFORT AND BODILY COST** —
whether physical work visibly costs the body something, and whether the
screen shows the bill being paid.

Generated video is very good at showing a body performing a task and very
bad at showing that the task was hard. The hands do not tighten. The
shoulders do not round. The breath does not change. The next scene begins
with a fresh, unmarked, unwinded body. **The action happens; nobody pays
for it.** That is what you measure.

⛔ This is not the physics lens. They ask whether a lift is numerically
plausible for the mass and the gravity. **You ask whether the lift LOOKS
LIKE IT COST SOMETHING, and whether the cost persists.** A lift can be
perfectly plausible arithmetically and completely weightless dramatically;
that finding is yours alone and no other lens will catch it.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, cuts, scene counts,
durations, or bodily behaviour of any kind. Write `MEDIA: nothing played`,
put every question in FLAGS, and stop. **A run that invents a timeline is
worse than a run never made.**

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied with the video
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated.

**MODE D** — the plan states loads, distances, durations and the character's
declared limits. You verify the body against them.

**MODE V** — you have no plan. You may never report that a cost is MISSING
in the sense of "the plan said it should be there". You CAN report that a
cost is missing in the sense of "work was shown and no cost followed" —
that is an on-screen contradiction and it is scoreable in both modes.

---

## 📋 EFFORT LOCK LIST — MODE D ONLY

### ⬇️ OPERATÖR DOLDURDU — THE_COLD_WELD_QA_SPEC.md'den A + C · MODE D

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE COLD WELD
FORMAT:               16:9 yatay · 2-4 dk · bilimkurgu (keşif / aksiyon) ·
                      HARD VACUUM üzerinde bir ay yüzeyi (0,30 g · atmosfer
                      yok · gölge içi mutlak siyah) · gündüz, alçak ve
                      sabit yükseklikte tek yıldız
SCENE COUNT:          15   (S0-S14)
RUNTIME:              150 seconds (title card: none — screen text lock 0.0 s)
REVIEW INPUT:         video only

LOGLINE (intended):   On an airless moon where bare metal that touches bare
                      metal fuses permanently on contact — so that a wrecked
                      ship has become one continuous metal reef — a lone
                      technician must cross seventy-eight metres of that reef
                      while the advancing edge of sunlight breaks it back
                      into separate plates, using the only two bare-metal
                      surfaces she has: the grip disc in each palm, each of
                      which can be used exactly once.
THEME (intended):     YALNIZLIK — "Nothing is ever lost here and nobody ever
                      comes back. Everyone who came is still here, and none
                      of them is still themselves."
THEME SCENES:         ✅ YAZILDI — S3 (boşluk: tepe kadrajı, %82 negatif
                      alan, figür 38 piksel) · S8 (yankı: otuz bir parlak
                      disk, insan yok) · S12 (içe kapanma: diz çöküş,
                      omuzlar kısılır, avuç yere kapanır) · S14 (tekil
                      soğuk kaynak: son 3,5 saniyede ekranda insan yok)
                      → TEMA_MUHENDISLIGI §5 matrisi · §3 tablosundan
                      HİÇ KULLANILMAMIŞ tema; §3c takas kalıbı KULLANILMADI
INTENDED EMOTION:     cold procedural focus turning into a two-count dread —
                      the viewer arrives asking "why didn't the wrench
                      fall?", stays asking "how many palms are left?",
                      leaves asking "how does she climb that ladder now?"
ENDING TYPE:          AMBIGUOUS (open) + visual dilemma. Both palms are
                      matte dark, one mirror disc is left in the plate, the
                      lander stands unclimbed in the RIGHT third, and the
                      last 3.5 seconds have no human in frame. Nobody
                      boards: no ladder climb, no lift-off, no answer.

PROTAGONIST:          a woman in her late thirties, 1.71 m, unnamed in
                      prompts, identified by three physical channels only:
                      height, matte pale bone-white suit, and a 14 cm old
                      scuff on the LEFT shoulder.
                      Wants: to cross the reef to the regolith and her
                      lander. Fears: not the light — running out of palms.
SECOND FIGURE:        NONE. Exactly one living human, in 14 of 15 scenes.
                      S0 has zero humans.
ANTAGONIST/FORCE:     no villain, no creature, no pursuit. The force is a
                      SPEED: the edge of sunlight advancing at 0.40 m/s,
                      which never accelerates, never stops and never targets
                      anyone — plus the contact law itself.
CENTRAL CHOICE:       S12 (120-130 s) — she presses her last bright palm
                      onto the plate ON PURPOSE, spending it to be carried
                      by the thing that is about to be released. Cost lands
                      IN THE SAME SHOT: her already-dark right palm is in
                      frame throughout.

DIALOGUE LINES:       0 — completely silent film. No human speech, no
                      machine voice, no radio, no voice-over. There is no
                      "utterance" of any kind anywhere in the film.
SILENT SCENES:        15 (all of them)
MUSIC-FREE SCENES:    2 — S0 (hook) and S12 (the choice)
VIRAL INTERSTITIALS:  S3 · S9 · S13   ⛔ THESE MAY NOT BE CUT
UNCUTTABLE LIST:      S0 · S3 · S6 · S8 · S9 · S12 · S13 · S14
                      (cover moment · scale · cost 1 · Chekhov payoff ·
                       viral 2 · climax · viral 3 · final)
SEED (planted clue):  S2 at 22.0-24.0 s — ONE mirror-bright disc on a
                      vertical plate 3 m behind her, unremarked, ≤2 s.
                      Payoff at S8 (thirty-one of them). [FINAL §3, window
                      for 2-4 min is 15-22 s]
COVER/THUMBNAIL:      A: S0 at 6.0 s — the airborne plate with the wrench
                      standing perpendicular on it, RIGHT third, straight
                      light edge across the LEFT two thirds.
                      B: S12 at 1.5 s — the raised bright palm above the
                      metal with the dark palm in the same frame.
TITLE:                THE COLD WELD — welding without fire; the thing this
                      world does to anything that touches it.
LIBRARY CONTEXT:      First film in the library on cold welding, and the
                      first with a two-item cost counter (2 palms → 0).
                      Nearest neighbour is THE REMEMBERING DUST (a ground
                      that RECORDS and rewrites); this ground KEEPS the
                      object itself and never erases. Structure inherited
                      from THE ROSE COAT (0 cuts, fixed 10 s grid,
                      environmental counters, separate SPEC file); the
                      resource there was 80 brush strokes, here it is 2.
```

---


## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
CANLI İNSAN   tam 1 · 14 sahnede görünür · 1 sahne insansız (S0).
              İkinci figür 0 · kopya 0 · klon 0 · yansımada figür 0 ·
              uzakta figür 0 · inicin yanında figür 0 · merdivende
              figür 0.
KİMLİK        Üç kanal, hiçbiri yüze bağlı değil: 1,71 m boy · mat soluk
              kemik beyazı giysi · SOL omuzda 14 cm'lik eski çentik.
              ⛔ Prompt gövdesinde özel ad ve milliyet YOK [D34/D45].
BAŞ/YÜZ       Tek yüz, 15/15 sahnede kask içinde. Vizör tek parça,
              optik olarak ŞEFFAF; sıfır renk, sıfır ayna kaplaması,
              sıfır çevre yansıması; yüz her baş açısında okunur
              [D5 · D79]. Vizör 0 kare açılır, 0 kare buğulanır.
SIRT          Boyundan kalçaya TEK PARÇA düz panel: çanta 0 · tank 0 ·
              hortum 0 · kablo 0 · çıkıntı 0 [D79]. ⭐ S12'de kamera
              gövdenin ARDINDADIR (azimut 20°) ve o promptta yokluk
              listesi POZİTİF YÜZEY TARİFİNE çevrilmiştir [D139].
              "Sırtta bir şey var" bulgusu yalnız SİLÜET BOZULMUŞSA
              geçerlidir.
⭐ SOĞUK KAYNAK  ⭐ FİLMİN NOVUM'U — üç maddelik kapalı liste:
              ① Çıplak metal ↔ çıplak metal teması KALICIDIR.
              ② Seramik kaplı yüzey (bot tabanı 26×11 cm · diz koruması ·
                önkol manşeti 12 cm · kalça paneli) KAYNAMAZ.
              ③ Kumaş, cam ve boya KAYNAMAZ.
              ⛔ "Neden avucunu kaldıramıyor" / "neden yapıştı" soruları
                 BULGU DEĞİLDİR; filmin ÖNERMESİDİR [D87/D116 önerme
                 kapısı]. ⛔ "Botları neden yapışmıyor" da bulgu değildir:
                 asimetri TASARIMDIR ve 15/15 promptta yazılıdır.
              ⛔ Bağ ATOMİKTİR, GEOMETRİK DEĞİL: iki yüzey ayrı ayrı
                 görünür kalır ve aralarında net bir sınır vardır.
                 "El metale eriyor / batıyor" bir ÜRETİM HATASIDIR ve
                 bulgu olarak yazılır [D24 temas bütünlüğü].
AVUÇ SAYACI   ⭐ FİLMİN ANA SAYACI, iki durum:
              PARLAK   9 cm ayna gibi cilalı nikel disk, avuca gömülü
              KARANLIK 9 cm mat koyu gri kumaş daire, ışık yakalamaz
              Takvim: S1-S5 iki avuç da PARLAK (2) · S6 sağ avuç
              KARANLIK (1) · S7-S11 sol PARLAK / sağ KARANLIK (1) ·
              S12-S13 sol PARLAK ama KAYNAMIŞ · S14 ikisi de KARANLIK (0)
              ⛔ Sayaç asla geri gitmez. Bir sahnede karanlık bir avuç
                 yeniden parlaksa bu bir ÜRETİM HATASIDIR.
              ⛔ Diskler hiçbir karede İNSAN yansıtmaz: yüz 0, gövde 0,
                 figür 0. Yalnız çıplak ışığı yansıtırlar — bu TASARIMDIR.
YAMALAR       S2'de 1 · S8'de 31 disk + 6 bot-tabanı boyutunda dikdörtgen
              + 1 dar bilezik · S9'da aynı 31 disk yer değiştirir ama
              HİÇBİRİ KAYBOLMAZ · S14'te 1 disk daha (kadının bıraktığı).
              ⛔ HEPSİ DÜZ SACTIR ve levhanın DÜZLEMİNDE durur. Duvarda
                 gövde, uzuv, yüz ya da üç boyutlu hiçbir şey YOKTUR;
                 hiçbir şey duvardan dışarı taşmaz. "Duvarda insan var"
                 bulgusu bir ÜRETİM HATASIDIR ve öyle yazılır.
IŞIK ÇİZGİSİ  ⭐ FİLMİN SAATİ: krater gölgesinin kenarı. JİLET GİBİ DÜZ,
              0,40 m/s, EKRAN-SOLDAN EKRAN-SAĞA, 15/15 sahnede aynı
              yönde. Hiç durmaz, hızlanmaz, yön değiştirmez, dalgalanmaz.
              Mesafe takvimi (kadının botlarından): S1 34 m · S2 31 m ·
              S3 28 m · S4 24 m · S5 19 m · S6 15 m · S7 12 m · S8 9 m ·
              S9 6 m · S10 4,5 m · S11 3,0 m · S12 1,5 m · S13 0 m ·
              S14 geçmiş.
              ⛔ MONOTONİKTİR — geri gitme = ihlal.
              ⛔ Çizgi bir IŞIN, HÜZME, PROJEKTÖR ya da TARAYICI DEĞİLDİR:
                 bir GÖLGE KENARIDIR. Hüzme görünüyorsa üretim hatasıdır
                 (vakumda saçılma yok).
DİKİŞ KOPUŞU  Gölge 98 K · ışık 371 K · 4,0 m levha ışıkta 5,2 mm uzar ·
              dikiş ışığın geçmesinden 0,4-1,2 s sonra kopar. Kopuş
              SOĞUKTUR: kıvılcım 0 · ısı parlaması 0 · duman 0 · ark 0 ·
              erimiş metal 0 · patlama 0.
SERBEST CİSİM Kopan levha 0,35 m yükselir, 0,9 m yana gider, 0,49 s'de
              tepe yapar, 0,70 s'de OTURUR ve bir daha kımıldamaz [D127].
              ⛔ 1 saniyeden uzun havada kalan levha ihlaldir. Asılı
                 kalma 0 · süzülme 0 · yavaşlama 0 · dönerek uçma 0.
YERÇEKİMİ     0,30 g (2,94 m/s²) — gövde 1,00 m'yi 0,82 s'de düşer.
              Ağır çekim 0 kare · hız rampası 0 kare.
              ⛔ SIÇRAYIŞ 0 KARE: iki bot hiçbir karede aynı anda yerden
                 kesilmez; havada geçen toplam süre 0,0 saniyedir. Bu
                 TASARIMDIR [D23 yapısal olarak tetiklenemez], eksiklik
                 değil.
KAYIŞ         S13: 22° eğimli levha 5,0 m'yi 3,0 saniyede alır, sonda
              3,3 m/s. Sekme 0 · takla 0 · ikinci kayış 0.
TOZ           ⭐ RESİFTE 0 KARE TOZ — zemin çıplak metaldir ve toz
              tutmaz. Bu TASARIMDIR, eksiklik değil. Toz yalnız S13'te
              ve yalnız regolitte: ≤0,4 m yükselir, tamamı 0,6 s'de
              oturur, düz aşağı iner. Girdap 0 · sıvı gibi akma 0 ·
              asılı perde 0 [D39].
IŞIK          ⭐ TEK KAYNAK: yıldız, EKRAN-SOLDA, 4,2°. Yapay ışık 0 kare
              (far · seyir lambası · kapak ışığı · fener · ekran · uyarı
              lambası · kask içi lamba). İniç 15/15 sahnede SÖNÜK ve
              soğuktur; motor alevi 0 kare, egzoz 0 kare.
              ⭐ VAKUMDA DOLGU IŞIĞI YOKTUR: gölge içi MUTLAK SİYAH ve
              gölge kenarı JİLETTİR. "Gölgeler çok sert / detay yok"
              bulgusu DÜŞER — ortamın kuralıdır [§3.1].
              ⛔ Lens parlaması ve anamorfik yatay parlama fiziksel
                 olarak YANLIŞTIR (saçılma yok) ve görülürse bulgudur.
GÖKYÜZÜ       MUTLAK SİYAH ve BOŞ. Yıldız alanı 0 · gezegen 0 · bulutsu
              0 · gradyan 0. "Gökyüzü boş" bulgusu TASARIMDIR.
EKRAN YÖNÜ    15/15 sahnede: yıldız SOL · gölgeler SAĞ · ışık çizgisi
              soldan sağa · hedef (resifin öbür kenarı + iniç) SAĞ ÜÇTE
              BİRDE · kadın ekran-sağa hareket eder. Yön dönüşü 0 kare.
              ⭐ TASARLANMIŞ İSTİSNA: S1 · S7 · S12'de omuz üstünden
              çizgiye TEK saniyelik BAŞ dönüşü var; ayaklar yön
              değiştirmez. Bu Kart 9'un kinesik ayağıdır, ihlal değildir.
              ⭐ S10'da kadın 4 m GERİ (ekran-sola) yürür ama omuz hattı
              ekran-sağda kalır — bu ZORLANMA ÇAPASIDIR ve tasarımdır.
RENK          Filmde tam üç değer var: aydınlık metalin soğuk gümüşü,
              gölgenin mutlak siyahı, giysinin soluk kemik beyazı.
              Doygun renk 0 kare. ⭐ Tek spekülar vurgu avuç diskleri ve
              yamalardır — parlaklık bir SAYAÇTIR ve post'ta oynanmadı.
              ⛔ "Her şey aynı renk" bulgusu TASARIMDIR.
ANAHTAR       56 cm düz çelik, işaretsiz. S0'da bir levhaya DİK kaynamış;
              S10'da önkol manşeti ve dizle kurtarılır; S11'de son dikişe
              çakılır ve kaynar. ⛔ Avuçla 0 kare tutulur — "neden eliyle
              tutmuyor" bulgu değildir, filmin kuralıdır.
TEMAS         Kadın-nesne teması sayılıdır: avuç-metal 2 kez (S5 kaza ·
              S12 seçim) · manşet-anahtar 2 kez (S10 · S11) · bot-basamak
              1 kez (S11). Bunun dışında avuç hiçbir yüzeye değmez.
BİNİŞ         0 kare [D69]. Merdiven tırmanma, kapaktan girme, kalkış
              yok; film levhanın dibinde biter. "Final kesik" bulgusu
              DÜŞER — muğlak/genişleme finalidir.
KOŞU/ZIPLAMA  0 kare. Yürüyüş ölçülüdür. Koşu ve sıçrama TASARIM GEREĞİ
              yoktur (D23 + klon riski).
KONUŞMA       0 replik · ağız hiçbir karede konuşma için oynamaz. Radyo
              0 · AI sesi 0 · dış ses 0. "Diyalog yok" bulgusu TASARIMDIR
              [③ SES merceği için].
METİN         0 kare — gövde yazısı, logo, marka, numara, sembol, bayrak,
              arma, ölçü çentiği, gradasyon işareti, seri numarası, uyarı
              damgası hiçbir yüzeyde yok. ⭐ Bu filmin en yüksek metin
              riski METAL YÜZEYDİR [D138] ve karşı önlem POZİTİFTİR:
              bilgi taşıyan tek şey dikiş, perçin ve göktaşı çukurudur.
SU/ATEŞ       0 kare — su, buz, kırağı, buğu, sis, bulut, alev, duman,
              patlama, kıvılcım, motor jeti yok. İniç hiçbir karede
              çalışmaz.
CANLI         0 kare — hayvan, kuş, böcek, bitki, mikrobiyal örtü,
              organik hareket yok.
HASAR         0 kare — giysi yırtığı, çatlak vizör, sızıntı, buhar,
              kaçak gaz yok. Tek sonuç DİSKİN KALMASIDIR.
EŞ KADRAJ     S0 ↔ S14 (aynı kurulum A, aynı görsel iddia: bir metal
              yüzey ve üstünde ona kaynamış tek bir yabancı nesne —
              biri anahtar, öteki bir avuç diski)
```

---



Read out of the supplied SPEC before you watch:

```
A BLOĞU  → sahne haritası: hangi sahnede ne iş yapılıyor
C BLOĞU  → kilitler: kütle, mesafe, süre, ekipman, sayaçlar
```

Build a lock table BEFORE watching: one row per declared exertion — scene,
task, load or resistance, declared duration. You verify each on screen.

> 📌 **Eksik blok kaydı (dürüst not):** bu depoda SPEC'ler ⑧ için ayrılmış bir
> blok TAŞIMAZ. Bir film ileride **D BLOĞU — EFOR** yazarsa (sahne · iş · yük ·
> süre · beklenen bedel · toparlanma penceresi), bu mercek belgeli koşar.
> Bugün A + C bloklarından çıkarım MEŞRUDUR ama çıkarım olduğu YAZILIR.

---

## ⛔ STEP 0 — THE PREMISE GATE (both modes — run it before judging anything)

Write the register before you score anything:

```
PREMISE REGISTER
· gravity / medium        [0.12g contact steps, vacuum, water, 0.92g…]
· what the body wears     [suit, gloves, helmet, tether, pack — and its bulk]
· declared capability     [what the film says this person can do]
· declared limits         [air, heat, cold, time, injury already present]
· is the body human?      [augmented, remote-operated, synthetic → register it]
```

⛔ **NAMING THE MEDIUM IS NOT NAMING A RULE.** "Zero-g", "vacuum",
"weightless but mass and inertia remain intact" describe the SETTING and
restate ordinary physics. If the film is built on an impossibility — matter
that stops, weight that transfers, a body that cannot push off anything —
the register must state THAT, with the threshold the screen shows, because
it changes what counts as work. In a world where nothing can be pushed
against, throwing mass IS the exertion, and a body that throws and drifts
is paying a bill you will otherwise score as "no strain shown".

⛔ **LOW GRAVITY IS NOT LOW EFFORT.** A 0.12g environment reduces weight, not
mass and not inertia. Starting, stopping and turning a large mass costs the
same. A film where everything is effortless because "it's low gravity" has
made an error, and it is yours. Register the gravity; do not let it excuse
the body.

⛔ **A SUIT IS A COST, NOT A COSTUME.** Pressurised gloves resist closing.
Helmets restrict head rotation and peripheral vision. Packs move the centre
of mass. If the film dresses a body in equipment and then moves it as if
bare, that is a finding in category 7.

---

## STEP 1 — BUILD THE EFFORT LEDGER (before judging anything)

Watch once for work. An **exertion event** is any moment the body applies or
resists force in a way that should cost something. Write one row per event:

```
E<n> | in–out | task | load / resistance | duration | STRAIN SHOWN |
       RECOVERY SHOWN | debt after (0–9)
```

Rules for the ledger:

- `STRAIN SHOWN` is what you SAW, listed by channel: hands · arms · torso ·
  legs · neck/head · breath (visible) · face (if visible) · rate change.
  Write the channels you saw. **Write `none` if you saw none — that is the
  most important cell in this report.**
- `RECOVERY SHOWN` is what happens after: pause, lean, hands on knees, slow
  return to task, breath settling, or `none`.
- `debt after` is your running estimate of accumulated physical cost on a
  0–9 scale. It feeds the COST CURVE below.
- Environmental cost (cold, heat, thin air, pressure) counts as an exertion
  event even with no task: the body is working to stay alive.

### ⛔ THE BILL TEST — the only test this lens has

For each exertion event, answer in one sentence:

> *"What is different about this body AFTER, that the work caused?"*

If the honest answer is *"nothing"*, the event has `STRAIN SHOWN: none`,
`RECOVERY SHOWN: none`, and it is a finding. **Write the sentence.** A
deduction with no attempted sentence is not a finding.

⛔ In mode D, answer from the screen FIRST, then read the plan. The plan
will tell you the crate weighs 80 kg and you will start seeing strain that
is not there.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

```
① EFFORTLESS HEAVY — a mass is lifted, pushed or arrested with a straight
   back, relaxed hands, unchanged rate. Weight is stated, never performed.
② INFINITE STAMINA — sustained work produces no rate decay, no breath
   change, no posture change, however long it runs.
③ THE FRESH RESET — the next scene opens on a body that is unwinded,
   unmarked and upright, with no recovery shown between.
④ INJURY AS MAKEUP — a wound, burn or tear is visible but never alters
   reach, grip, gait or willingness. It is a texture, not a condition.
⑤ GRIP THAT NEVER FAILS — hanging, holding, or pulling with no forearm
   engagement, no re-grip, no slip, no shake. Hands are hooks.
⑥ THE SUIT THAT ISN'T THERE — gloved hands with bare-hand dexterity;
   a helmet with unrestricted head turn; a pack that never shifts balance.
⑦ PAIN WITHOUT DURATION — a wince that lasts one beat and vanishes with no
   guarding, no favouring, no changed movement afterward.
⑧ RECOVERY FASTER THAN EXERTION — forty seconds of maximal work, two
   seconds of recovery, back to baseline.
⑨ SYMMETRIC BODY UNDER ASYMMETRIC LOAD — a mass carried on one side, but
   posture, gait and arm swing stay mirror-symmetric.
⑩ BREATH THAT DOESN'T TRACK WORK — visible breathing (chest, visor fog,
   vapour) unchanged between rest and maximal effort, or fogging on a
   schedule unrelated to exertion.
⑪ THE UNEARNED SECOND WIND — capability returns with no rest, no food, no
   air, no stated reason. Often at the climax.
⑫ ENVIRONMENT WITHOUT BODILY COST — extreme cold, heat, thin air or
   pressure with no shiver, no stiffening, no slowed fine motor control.
⑬ THE UNTIRING HAND — delicate, precise fine-motor work performed
   immediately after exhausting gross-motor work, with no tremor.
⑭ COST WITHOUT SOURCE — the reverse error: exhaustion, injury or
   breathlessness arrives with no work shown to have caused it.
```

⛔ Pattern ⑭ scores exactly like the others. This lens is not "more suffering
is better". An unearned cost is as false as an unpaid one.

---

## YOUR TASK

Watch the film. Build the effort ledger. Run the bill test on every event.
Then score the categories below, deducting only from what your ledger holds.

## ═══ YOUR SCOPE ═══

```
✅ What physical work does to the body and whether the screen shows it:
   strain during, breath and recovery after, fatigue accumulating across the
   film, load expressed in posture and gait, injury persisting as a
   functional condition, grip and the price of holding on, the burden of
   worn equipment, the proportion of pain response, and the honesty of the
   recovery curve.
```

⛔ **You own the BILL, not the arithmetic, not the sameness, not the
readability.** Whether the mass is numerically right, whether the glove is
the same glove, whether the beat reads — none of these are yours. You ask
one question of every observation: **did the body pay, and can I see it?**

## ═══ NOT IN THIS PASS ═══

```
❌ Quantities: is this stride rate human, is this jump height possible at
   this gravity, is this mass consistent scene to scene — measured and
   computed                                              → the PHYSICS lens
   (their §9 asks "is the biomechanics PLAUSIBLE?"; you ask "did it COST?".
   A biomechanically perfect lift with no strain shown is yours, not theirs)
❌ Whether the wound is the SAME wound, whether the glove tear persists as
   an APPEARANCE                                     → the CONTINUITY lens
   (their question is "did it change?"; yours is "did it change what the
   body can DO?" A wound that stays visually identical and never affects
   function is a PASS for them and a finding for you)
❌ Whether the action READS: beat boundaries, contact legibility, geography,
   threat direction                                     → the ACTION lens
❌ Anatomy artifacts at rest, morphing, extra fingers, texture swimming
                                                          → the FRAME lens
❌ The SOUND of breathing, grunts, effort vocalisation, mix   → the SOUND lens
   (visible breath — chest rise, visor fog, vapour — is YOURS; audible
   breath is theirs; a film can fail one and pass the other)
❌ Emotional arc, whether the suffering means anything      → the STORY lens
❌ In mode V, anything you think the PLAN intended — FLAGS only.
```

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material takes `N/A` and leaves the mean.

### 1. 💪 STRAIN DURING THE WORK
```
□ Effort is visible in at least two channels while the work happens
□ Rate decays within a sustained effort — the tenth pull is slower
□ Bracing is present: the body sets itself before it applies force
□ Maximal effort looks different from routine effort (pattern ①)
```

### 2. 🌬️ BREATH & RECOVERY (visible only)
```
□ Visible breathing tracks work rate: chest, shoulders, visor fog, vapour
□ Breath elevates during and settles after, on a plausible curve
□ Recovery is proportional to exertion (pattern ⑧)
□ Fogging or vapour follows exertion, not a decorative schedule (⑩)
```

### 3. 📉 FATIGUE ACCUMULATION ACROSS THE FILM
```
□ Capability degrades across successive efforts (pattern ②)
□ The body in the last third differs from the body in the first
□ Recovery between scenes is shown or plausibly elapsed (pattern ③)
□ Any return of capability is earned and stated (pattern ⑪)
```

### 4. 🎒 LOAD IN THE BODY
```
□ Carried mass changes posture, gait and arm swing
□ Asymmetric loads produce asymmetric bodies (pattern ⑨)
□ Setting a load down produces a visible release
□ The same load produces the same body language every time it appears
```

### 5. 🩹 INJURY PERSISTENCE & FUNCTIONAL COST
```
□ An injury alters reach, grip, gait or willingness (pattern ④)
□ The alteration persists into later scenes, not just the scene of injury
□ Favouring and guarding are visible at the right side of the body
□ Where an injury is deliberately ignored by the character, the effort of
  ignoring it is visible
```

### 6. ✊ GRIP & THE PRICE OF HOLDING ON
```
□ Sustained grip shows forearm engagement, re-gripping, tremor (pattern ⑤)
□ Slipping is possible and sometimes happens
□ Fine motor control degrades after gross exertion (pattern ⑬)
□ Hands read as hands with a limit, not as attachment points
```

### 7. 🧤 EQUIPMENT BURDEN
```
□ Gloves resist: closing is slower, dexterity is reduced (pattern ⑥)
□ Helmets restrict head rotation and force whole-body turns
□ Packs, tethers and tools shift balance and catch on things
□ Any removal of equipment produces a visible change in capability
```

### 8. 😖 PAIN, RESTRAINT AND PROPORTION
```
□ Pain response is proportional to the event
□ It has duration and an aftermath (pattern ⑦)
□ Suppressed pain reads as suppression, not absence
□ No cost arrives without a cause shown (pattern ⑭)
```

### 9. 📈 THE RECOVERY CURVE'S HONESTY
```
□ The COST CURVE below only falls where recovery is shown or time elapsed
□ The film's hardest moment sits at or near the curve's peak
□ No scene resets the body to baseline without a reason
□ The ending's body is consistent with everything the film spent
```

---

## OUTPUT FORMAT — use this exact structure

```
INPUT MODE: [D / V]
FILM: [name as stated by the operator, or "(not supplied)"]
RUNTIME: [mm:ss — "measured" or "~mm:ss ESTIMATED"]
FRAME RATE ASSUMED: [n fps — every duration in this report uses it]
SCENES OBSERVED: [n] · CUTS COUNTED: [n]
NON-SCENE MATERIAL: [in-out + what it is, or "none"]
PRESENCE STRING: [see the section below — one character per scene]
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or "none"]
             When you write "none", say which none it is: "none — room tone
             present" or "none — nothing audible to me".
             ⛔ THIS LINE REPORTS WHAT YOU HEARD. It is never a statement
             about the file. You may not write that the file has no audio
             track: that is a property of the container, read with one
             ffprobe command, and no model can observe it. Write
             "none — nothing audible to me" and put the question in FLAGS.
EXERTION EVENTS: [n · from the ledger]
EVENTS WITH NO STRAIN SHOWN: [n]
BODY: [human / suited human / augmented / non-human — from the register]
PREMISE REGISTER: [each declared rule, one line — or "none"]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Report its in and out
timecode on that line, then EXCLUDE it from CUTS COUNTED, from the ledger,
from the cost curve and from every duration you report.

⛔ CUTS COUNTED is not optional and not a rounded impression: it is the
count you made in STEP 1, with its timecodes.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. When something this lens measures is
absent in EVERY scene without exception — no equipment is ever worn, no
injury ever occurs — that category takes `N/A`, stays out of the mean, and
the absence is named in one line. Score low only for an absence that is
scattered. A throughout-absence you suspect is deliberate goes to FLAGS as
a question, never to a score.

⛔ A FILM WITH NO EXERTION IS NOT A ZERO. If the ledger is empty, every
category is N/A, OVERALL SCORE reads `N/A — no exertion events`, and you
write one line saying so. A film of a person watching a sunrise does not
fail this lens; it is out of its reach.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [THE BODY PAYS / MINOR DEBT / FIXABLE IN EDIT / WEIGHTLESS WORK /
          NOBODY PAYS]
         One finding outranks every other score: if EVERY exertion event in
         the ledger has `STRAIN SHOWN: none`, the verdict is NOBODY PAYS,
         first line, regardless of the mean.
```

## EFFORT LEDGER
[the full STEP 1 ledger with the bill-test sentence for every event — this
is evidence, include it]

## PRESENCE STRING
One character per scene, in edit order, no spaces: `1` if a human figure is
visible anywhere in that scene, `-` if the scene has none. Cover only the
scenes you listed, excluding non-scene material. Never reorder it to match
what you expect a film to do — it is a fingerprint of the EDIT'S ORDER.

⛔ You write this even though it is not your subject. It is the ONE axis on
which every lens can be checked against every other lens: when six reports
of the same film print six strings, a disagreement locates the report that
misread the edit. A lens that skips it removes itself from that check.

⚠️ In a single-figure film this string is nearly constant (`1111…`) and
therefore proves very little on its own — a whole block of scenes can be
swapped without changing it [D163]. Write it anyway, and do not treat a
matching string as proof that the order is right.

## COST CURVE
```
One digit per scene, in order, length = SCENES OBSERVED:
  0 = baseline, rested        5 = heavily taxed
  9 = at the limit            (use the whole range, not just 0 and 1)
Example (15 scenes): 000122334445553
```
⛔ The curve's length must equal SCENES OBSERVED, which must equal
CUTS COUNTED + 1 when there is no card. If those three numbers disagree, say
so on this line — do not silently adjust one to fit another.

⛔ **EVERY FALL IN THE CURVE NEEDS A ROW IN THE RESET LOG.** A digit that
drops without a shown recovery or elapsed time is pattern ③ or ⑪ and is a
finding, not a smoothing.

## RESET LOG
| Between | Curve fell | Recovery shown? | Time elapsed? | Verdict |
One row per fall in the curve. Verdicts: EARNED / UNEARNED / UNCLEAR.

## EFFORT LOCK VERIFICATION — MODE D ONLY
| Declared exertion | Found at | Strain shown | Verdict |
One row per declared exertion. Verdicts: PASS / FAIL / UNMEASURABLE /
NOT PRESENT. A FAIL needs the ledger row it came from.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as ledger rows with
   timecodes: | Strain During the Work | 4/10 | -3 · E2 (0:41), E5 (1:52) |
   A deduction with no listed source is not applied; the category starts
   full.
② ONE OBSERVATION, ONE PLACE. An observation is EITHER a severity-tagged
   finding (it lowers ONE category's score) OR a question for the document
   (it lowers nothing). Never both, and never two categories at once — a
   grip failure that also reveals a glove problem picks its owning category
   by the root cause.
③ A category with material but no in-scope source keeps 10/10 and the Issue
   cell reads "no in-scope source". It never takes a silent deduction.
```

| # | Category | Score | Issue (with ledger rows and timecodes) |
|---|----------|-------|-----------------------------------------|
| 1 | Strain During the Work | /10 | |
| 2 | Breath & Recovery | /10 | |
| 3 | Fatigue Accumulation | /10 | |
| 4 | Load in the Body | /10 | |
| 5 | Injury Persistence & Cost | /10 | |
| 6 | Grip & the Price of Holding On | /10 | |
| 7 | Equipment Burden | /10 | |
| 8 | Pain, Restraint and Proportion | /10 | |
| 9 | Recovery Curve Honesty | /10 | |

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report.

## UNPAID WORK TABLE
| Timecode | The work | What should have shown | Which pattern (①–⑭) | Severity |
Every event with `STRAIN SHOWN: none` appears here. This is the table the
production line acts on.

## CONTRADICTION LOG
Every place where two things you observed cannot both be true, with both
timecodes. Write both; name the one you scored.

## THE THREE THAT MATTER
The three findings that most damage this film's physical credibility, in
order, each with its timecode and its one-line fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Two lists. Missing strain is almost never fixable in the edit — say so
plainly. An unearned curve reset sometimes is, by reordering or by removing
a scene.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, with the lens
named.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The bill test is the whole method.** Every finding traces to the
  question "what is different about this body afterward?"
- **Low gravity is not low effort.** Mass and inertia are unchanged.
- **A suit is a cost.** Gloves, helmets and packs must be honoured.
- **More suffering is not better.** Pattern ⑭ — cost with no cause — scores
  exactly like cost that never arrives.
- **Visible breath is yours; audible breath is the SOUND lens.**
- **In mode D, screen first, plan second.** Always.
