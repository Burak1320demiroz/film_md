```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_COLD_WELD
mercek    : ⑦ AKSİYON
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_COLD_WELD_QA_SPEC.md  (aile: yatay)
üretildi  : 02.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_2_4_dk_filmler_uzay/THE_COLD_WELD
belge: A (sahne haritası) + C (kilitler). ⛔ Rubriğin kuralı: ANLATIM CÜMLESİ önce EKRANDAN yazılır, sonra plana bakılır — ters sıra sahte PASS üretir
```

# ⑦ AKSİYON QA — ACTION LEGIBILITY CRITIQUE PROMPT

> Yapıştırılacak tek dosya. Mercek ⑦. Kardeş mercekler: ① KARE · ② DEVAMLILIK ·
> ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑧ EFOR.
> Ortak adımlar `AGENTS.md` §3'ten, kayıt zinciri `qa-isle` skill'inden okunur.

## WHAT THIS REVIEW IS

You are reviewing an AI-generated film for **ACTION LEGIBILITY** — whether a
first-time viewer can narrate what physically happened, in order, without
guessing.

This is not a physics review and not a story review. The physics lens asks
whether the numbers survive checking. The story lens asks whether the film
means anything. **You ask one question, of every moment where something
physical happens to someone: could a viewer describe it?**

An action beat that is physically perfect and dramatically motivated can
still fail here — because the contact happened behind an elbow, because the
threat arrived from a direction the frame never established, because the cut
landed on the wind-up and resumed on the aftermath and the beat itself was
never rendered.

⛔ **Legibility is not the same as beauty, speed, or intensity.** A calm,
slow, well-framed grapple can be perfectly legible. A fast, loud, shaking
sequence can be illegible. Rate your findings on what a viewer can RECOVER
from the screen, never on how exciting it felt.

---

## ⛔ STEP −2 — MEDIA GATE: IS THERE A PLAYABLE VIDEO?

Before anything else, answer in one line:

```
MEDIA: [video played / stills only / nothing played]
```

If no video played, you may not report timecodes, cuts, scene counts,
durations, or motion of any kind. Write `MEDIA: nothing played`, put every
question in FLAGS, and stop. **A run that invents a timeline is worse than
a run never made.**

---

## ⛔ STEP −1 — INPUT MODE (declare this in the first line of your report)

```
INPUT MODE: D   → a written SPEC was supplied with the video
INPUT MODE: V   → video only, no document
```

⛔ If a SPEC was supplied and you write `INPUT MODE: V`, the run is void and
must be repeated. If you were given a document, you are in mode D — read it.

**MODE D** — you verify the film against its own declared plan. Every beat
the plan declares must be found on screen or reported missing by name.

**MODE V** — you have no plan. You may never report that something is
MISSING; you have no way to know what was intended. An absence becomes a
question in FLAGS, never a deduction.

---

## 📋 BEAT LOCK LIST — MODE D ONLY

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



Read these out of the supplied SPEC before you watch:

```
A BLOĞU  → sahne haritası: her sahnenin ne yaptığı, doruk sahnesi
C BLOĞU  → kilitler: sayaçlar, ekran yönü, mesafeler, nesne konumları
```

From those, build a lock table BEFORE watching. One row per action beat the
plan declares: which scene, what the actor is trying to do, what resists,
what the outcome is. You will verify each row on screen.

> 📌 **Eksik blok kaydı (dürüst not):** bu depoda SPEC'ler ⑦ için ayrılmış bir
> blok TAŞIMAZ; A + C bloklarından çıkarım yaparsın. Bir film ileride
> **D BLOĞU — AKSİYON** yazarsa (beat listesi: sahne · niyet · direnç · temas ·
> sonuç · tehdit yönü), bu mercek belgeli koşar ve çıkarım gerekmez.
> Bugün çıkarım MEŞRUDUR ama çıkarım olduğu YAZILIR.

---

## ⛔ STEP 0 — THE PREMISE GATE (both modes — run it before judging anything)

The film may have declared rules that make an "error" correct. Before you
score anything, write the register:

```
PREMISE REGISTER
· gravity / medium         [e.g. vacuum, 0.12g contact steps]
· what the actor can do    [suit limits, tools, established capability]
· what resists them        [the antagonist force: matter, time, machine, person]
· established screen rules [is the camera ever handheld? does it ever cut mid-beat?]
```

A beat that violates ordinary expectation but obeys the film's declared
rules is **NOT a finding**. Write it in the register and move on.

⛔ NAMING THE MEDIUM IS NOT NAMING A RULE. "Zero-g", "vacuum", "motion is
continuous until arrested" describe the SETTING and restate ordinary
physics. If the film is built on an impossibility — matter that stops,
weight that transfers, a force that only works one way — the register must
state THAT, with the threshold the screen shows, and the beat that carries
it is then the film's MOST important beat, not a scene with no beat in it.
Before you write `-` in the beat string for any scene, ask whether that
scene is where the film's rule is demonstrated.

⛔ Absence of an antagonist figure is not absence of action. In this repo
most films have no second person: the resisting force is vacuum, cold,
a countdown, a mass, a mechanism. **Those are action beats and they are
yours.** A film where a lone figure fights a stuck coupling for 40 seconds
is an action film for this lens.

---

## STEP 1 — BUILD THE ACTION BEAT LEDGER (before judging anything)

Watch once for beats. A **beat** is one attempt at one physical problem. It
has a boundary you can name. Write one row per beat:

```
B<n> | in–out | ACTOR does WHAT | resisted by WHAT | contact? | outcome |
       threat/force direction on screen | readable? Y / PARTIAL / N
```

Rules for the ledger:

- A beat may span scenes. A scene may hold several beats. **Beats are not
  scenes** — do not force them to align.
- `contact?` is what you SAW: contact / near-miss / occluded / none.
- `outcome` is the state change: what is different after the beat that was
  not different before. If nothing is different, write `no state change` —
  that is itself a major finding.
- `readable?` is your verdict on that single beat, decided by the narration
  test below. Decide it BEFORE you look at your category scores.

### ⛔ THE NARRATION TEST — the only test this lens has

For each beat, write the sentence a first-time viewer would say:

> *"He braces his boot on the strut, pulls the lever twice, it doesn't move,
> then the third pull tears his glove."*

If you cannot write that sentence without using the SPEC, without guessing,
and without the words *"probably"*, *"seems to"*, or *"I think"* — the beat
is `N` (unreadable). If you can write it but one clause is uncertain, it is
`PARTIAL`. **Write the sentence in the ledger.** The sentence is the
evidence; a `readable? N` with no attempted sentence is not a finding.

⛔ In mode D you must write the narration sentence FROM THE SCREEN FIRST,
then compare it with the plan. Reading the plan first contaminates the test
— you will "see" what you were told is there. This is the single most common
way this lens produces a false PASS.

---

## KNOWN AI FAILURE PATTERNS (watch for these specifically)

These are the ways generated video breaks action. Each is a real, repeated
failure in this repo's material.

```
① CONTACT WITHOUT OCCLUSION — the hand reaches the surface but never
   deforms it, never occludes it, never stops on it. Contact is asserted by
   proximity alone.
② REACTION BEFORE CAUSE — the struck body, the dust, the cloth begins to
   move one or more frames BEFORE the thing that moved it arrives.
③ THE RESET POSE — after a violent motion the body returns to neutral
   standing. Nobody stays where the force left them.
④ THE ACTION ELLIPSIS — the cut lands on the wind-up and resumes on the
   aftermath. The beat itself was never rendered; the edit hides what the
   generator could not produce. Look for this specifically at every cut
   adjacent to a beat.
⑤ MOMENTUM EVAPORATION — a run, a fall, a swing ends without deceleration.
   Motion stops rather than slows.
⑥ THE FLOATING HIT — force lands and the world does not answer: no debris,
   no dust displacement, no cloth ripple, no camera answer, no settle.
⑦ GEOGRAPHY TELEPORT UNDER MOTION — the threat that was at screen-left is
   at screen-right mid-beat, with no move that put it there.
⑧ UNMOTIVATED CAMERA VIOLENCE — shake, whip, or blur with no in-world cause,
   arriving exactly where the action should be legible. Cover, not coverage.
⑨ LIMB MULTIPLICATION UNDER SPEED — an extra arm, a doubled hand, a leg
   that leaves and re-enters during fast motion.
⑩ THE ONE-SPEED FILM — every action at the same rate. No burst, no sustain,
   no hesitation. Effort has no tempo.
⑪ INTENT INVISIBLE — the body moves but you cannot tell what it is TRYING
   to do. Motion without a goal reads as animation, not action.
⑫ STAKES OBJECT OFF-SCREEN AT THE DECISIVE MOMENT — the thing the beat is
   about leaves the frame exactly when it resolves.
⑬ THREAT WITH NO APPROACH — the danger appears already at contact distance.
   It never travelled; therefore it was never coming.
⑭ SLOW-MOTION WITHOUT A SLOWED WORLD — the subject slows, the dust and the
   background do not.
```

---

## YOUR TASK

Watch the film. Build the beat ledger. Run the narration test on every beat.
Then score the categories below, deducting only from what your ledger holds.

## ═══ YOUR SCOPE ═══

```
✅ Whether physical events READ: beat boundaries, intent, spatial geography
   under motion, threat direction and approach, contact and its occlusion,
   consequence visibility, the camera's contract with the action, the tempo
   of effort, and whether the edit renders the beat or hides it.
```

⛔ **You own READABILITY, not correctness, not sameness, not meaning.**
Whether the momentum is numerically right, whether the glove is the same
glove, whether the scene earns its place in the story — none of these are
yours. You ask one question of every observation: **can a viewer recover
what happened?**

## ═══ NOT IN THIS PASS ═══

```
❌ Quantities: momentum, mass, speeds, stride rates, gravity, distances
   measured and computed                                  → the PHYSICS lens
   (the moment your finding needs a NUMBER to stand, it is theirs; the
   moment theirs needs a VIEWER to stand, it is yours)
❌ Artifacts read off one frame or one shot: morphing, melting, anatomy at
   rest, texture swimming, bloom, on-screen text        → the FRAME lens
   (limb multiplication DURING motion is yours when it destroys the beat's
   readability, and theirs as an artifact — both may write, each its kind)
❌ Whether a thing is the SAME across a cut: costume, prop, counter,
   established screen direction as a continuity value   → the CONTINUITY lens
   (their question is "did it change?"; yours is "could you follow it?"
   A perfectly consistent geography can still be unreadable, and that is
   yours alone)
❌ Whether the body shows strain, fatigue, injury cost, breath, load
                                                          → the EFFORT lens
❌ Dramatic escalation, pacing, whether the beat deserved its screen time,
   stakes as a story value                                → the STORY lens
❌ Anything in the non-subject field with no bearing on the beat
                                                      → the BACKGROUND lens
❌ Sound of impacts, mix, whether a hit is audible          → the SOUND lens
❌ In mode V, anything you think is MISSING — you have no plan. FLAGS only.
```

The boundary with the CONTINUITY lens, precisely: **they own "the threat was
at screen-left in S4 and screen-right in S5" — a comparison. You own "in S5
I could not tell where the threat was" — a reading.** The same cut can
produce both findings; each lens writes its own kind and neither writes the
other's.

---

## CRITIQUE CATEGORIES

Score each 1–10. A category with no material in the film takes `N/A` and
leaves the mean (see DECLARED ABSENCE).

### 1. 🎯 BEAT ANATOMY
```
□ Each beat has a readable setup → commitment → contact → consequence
□ The beat's boundary is visible: you can say when it starts and ends
□ No beat is elided by a cut (pattern ④) — the attempt itself is on screen
□ A failed attempt reads as a FAILED ATTEMPT, not as an absent one
```

### 2. 🗺️ SPATIAL GEOGRAPHY UNDER MOTION
```
□ Actor, obstacle and goal have positions you could sketch during the beat
□ Movement between positions is shown or clearly implied, never teleported
□ Screen direction survives the beat's own cuts (pattern ⑦)
□ Frame scale lets you see the relationship the beat is about
```

### 3. ⚠️ THREAT VECTOR & APPROACH
```
□ The resisting force — figure, mass, mechanism, time — has a direction
□ It arrives from somewhere the frame established (pattern ⑬)
□ Its proximity is legible: you know how close it is to mattering
□ Where the threat is a countdown or a state, its progress is on screen
```

### 4. 👊 CONTACT LEGIBILITY
```
□ Contact occludes, deforms, or arrests — it is not asserted by proximity
□ Contact and reaction are in the right order (pattern ②)
□ The contact point is visible or its concealment is deliberate and covered
□ Near-misses read as near-misses, not as ambiguous contacts
```

### 5. 💢 CONSEQUENCE VISIBILITY
```
□ Every beat produces a visible state change (or is legibly a null attempt)
□ Force lands on a world that answers: debris, dust, ripple, settle
□ The body ends where the force left it (pattern ③)
□ Consequence persists at least into the following shot
```

### 6. 🎥 THE CAMERA'S CONTRACT WITH THE ACTION
```
□ Camera movement serves legibility — it does not hide the beat (pattern ⑧)
□ Shake, blur and whip have in-world causes
□ Cut rate does not outrun comprehension at the decisive moment
□ The lens distance at contact lets contact be seen
```

### 7. 🧭 AGENCY & INTENT
```
□ You can state what the actor is TRYING to do, at every beat (pattern ⑪)
□ The attempt has a method you can name, not generic exertion
□ Changes of plan mid-beat are visible as decisions
□ Where intent is deliberately hidden, the hiding is legible as hiding
```

### 8. 🎯 THE STAKES OBJECT
```
□ The object the beat is about is in frame when the beat resolves (⑫)
□ Its state is readable at the moment it changes
□ If it leaves frame, it returns in a state consistent with what happened
□ The viewer never has to be told what mattered
```

### 9. 📈 PHYSICAL TEMPO & ESCALATION
```
□ Beats differ in rate: burst, sustain, hesitation (pattern ⑩)
□ Successive attempts at the same problem escalate in method or cost
□ Slow motion, where used, slows the world with the subject (pattern ⑭)
□ The film's hardest physical moment is its most legible, not its blurriest
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
BEATS COUNTED: [n · from the ledger]
BEATS READABLE: [n readable · n partial · n unreadable]
PREMISE REGISTER: [each declared rule, one line — or "none"]

⛔ NON-SCENE MATERIAL is not a scene at ANY duration. Material that carries
burned-in text, or is static, or bears no scene fingerprint, is a card.
Report its in and out timecode on that line, then EXCLUDE it from CUTS
COUNTED, from the ledger, from the beat string and from every duration you
report. Its text is never the film's name.

⛔ CUTS COUNTED is not optional and not a rounded impression: it is the
count you made in STEP 1, with its timecodes.

⛔ DECLARED ABSENCE IS NOT A DEFICIT. When something this lens measures is
absent in EVERY scene without exception — no beat ever has a stakes object,
no threat is ever a figure — that category takes `N/A`, stays out of the
mean, and the absence is named in one line. Score low only for an absence
that is scattered. A throughout-absence you suspect is deliberate goes to
FLAGS as a question, never to a score.

⛔ A FILM WITH NO ACTION BEATS IS NOT A ZERO. If the ledger is empty, every
category is N/A, the OVERALL SCORE line reads `N/A — no action beats`, and
you write one line saying so. This lens does not punish a contemplative
film for being contemplative.

ARITHMETIC GATE — write these three numbers BEFORE the score
  SCORED CATEGORIES:  __        (UNVERIFIABLE, N/A and ⚠️ PARTIAL excluded,
                                 never 0)
  SUM OF SCORES:      __._
  DIVISION:           __._ ÷ __ = __._      ← this is OVERALL SCORE

OVERALL SCORE: __/10
VERDICT: [ACTION READS / MINOR BLUR / FIXABLE IN EDIT / BEATS ILLEGIBLE /
          ACTION NEVER RENDERED]
         One finding outranks every other score: if any beat's core attempt
         is elided by a cut (pattern ④) and never shown, the verdict is
         ACTION NEVER RENDERED, first line, regardless of the mean.
```

## ACTION BEAT LEDGER
[the full STEP 1 ledger with the narration sentence for every beat — this is
evidence, include it]

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

## BEAT STRING
```
One character per scene, in order, length = SCENES OBSERVED:
  A = a beat runs in this scene and reads
  p = a beat runs and is PARTIALLY readable
  x = a beat runs and does NOT read
  - = no beat in this scene
Example (15 scenes): --A-ApxA--x-AA-
```
⛔ The string's length must equal SCENES OBSERVED, which must equal
CUTS COUNTED + 1 when there is no card. If those three numbers disagree,
say so on this line — do not silently adjust one to fit another.

## BEAT LOCK VERIFICATION — MODE D ONLY
| Beat the plan declares | Found at | Narration from screen | Verdict |
One row per declared beat. Verdicts: PASS / FAIL / UNREADABLE / NOT PRESENT.
A FAIL needs the ledger row it came from. This table is the reason mode D
exists — never omit a declared beat from it.

## SCORES SUMMARY

⛔ **EVERY SCORE CELL CARRIES ITS SOURCE, AND NO OBSERVATION IS BILLED TWICE.**

```
① Write the deduction's source in the Issue cell, as ledger rows with
   timecodes: | Contact Legibility | 4/10 | -3 · B3 (1:20), B7 (2:41) |
   A deduction with no listed source is not applied; the category starts
   full.
② ONE OBSERVATION, ONE PLACE. An observation is EITHER a severity-tagged
   finding (it lowers ONE category's score) OR a question for the document
   (it lowers nothing). Never both, and never two categories at once — a
   contact that also broke the geography picks its owning category by the
   root cause, and the other category is not touched.
③ A category with material but no in-scope source keeps 10/10 and the Issue
   cell reads "no in-scope source". It never takes a silent deduction.
```

| # | Category | Score | Issue (with ledger rows and timecodes) |
|---|----------|-------|-----------------------------------------|
| 1 | Beat Anatomy | /10 | |
| 2 | Spatial Geography Under Motion | /10 | |
| 3 | Threat Vector & Approach | /10 | |
| 4 | Contact Legibility | /10 | |
| 5 | Consequence Visibility | /10 | |
| 6 | Camera's Contract with the Action | /10 | |
| 7 | Agency & Intent | /10 | |
| 8 | The Stakes Object | /10 | |
| 9 | Physical Tempo & Escalation | /10 | |

## SEVERITY TALLY
🔴 BLOCKER: __   🟠 MAJOR: __   🟡 MINOR: __
⛔ The tally must equal the number of 🔴/🟠/🟡 tags actually written in this
report. If they disagree, the report is not internally consistent and the
gate will say so.

## UNREADABLE MOMENTS TABLE
| Timecode | What I could not recover | Which pattern (①–⑭) | Severity |
Every `N` and `PARTIAL` from the ledger appears here. This is the table the
production line acts on.

## CONTRADICTION LOG
Every place where two things you observed cannot both be true, with both
timecodes. Do not resolve them silently — write both and name the one you
scored.

## THE THREE THAT MATTER
The three findings that most damage this film's legibility, in order, each
with its timecode and its one-line fix.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Two lists. A beat elided by a cut is almost never fixable in the edit — say
so plainly. A geography break at a single cut often is.

## FLAGS FOR DOCUMENT CHECK
Questions for the plan, not deductions. In mode V, every suspicion of a
missing beat lands here.

## OUT-OF-SCOPE FLAGS
What you noticed that belongs to another lens, one line each, with the lens
named. You do not score these and you do not argue them.

---

## IMPORTANT NOTES FOR THE REVIEWER

- **The narration sentence is the whole method.** Every finding in this
  report traces to a sentence you tried to write and could not finish.
- **Do not reward intensity.** Loud, fast and shaking is not legible.
- **Do not punish stillness.** A film with two beats in 150 seconds can
  score 10/10 here if both beats read.
- **Most films in this repo have no antagonist figure.** The resisting force
  is matter, cold, vacuum, a countdown, a stuck mechanism. Score those beats
  exactly as you would a fight.
- **In mode D, screen first, plan second.** Always.
