```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_STANDING_WIRE
mercek    : ⑧ EFOR
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_STANDING_WIRE_QA_SPEC.md  (aile: yatay)
üretildi  : 05.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_3_5_dk_filmler/THE_STANDING_WIRE
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

### ⬇️ OPERATÖR DOLDURDU — THE_STANDING_WIRE_QA_SPEC.md'den A + C · MODE D

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE STANDING WIRE
FORMAT:            yatay 16:9 · 3-5 dk bandı
RUNTIME:           249 seconds (title card: YOK — screen text lock 0 s)
SCENE COUNT:       25  (S0-S24)
THEME:             UMUT
THEME SCENES:      S11 · S17 · S19 · S24     (dört — eşik üç)
                   S11 kamera+ışık: soğuk kadraja yandan ince sıcak sızıntı
                   S17 kinesik: avucun savunmadan açılışa geçişi
                   S19 kinesik: başın ışığa dönüşü
                   S24 nesne+ışık: iç ışık açık ve boş eldivenin üstünde
INTENDED EMOTION:  HUŞU (ölçek kontrastıyla satın alınır: S6 ve S19)
ENDING TYPE:       TERSİNE DÖNÜŞ (twist) + TOHUM BİLGİ
                   twist S24: altı askı, beşi dolu, biri boş
                   tohum S2 (8,0-10,0 s): barakanın duvarında tek boş askı
PROTAGONIST:       hat bekçisi, kadın, 38 (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    halkayı bırakır — S17
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0 / TELSİZ 0
SILENT SCENES:     25 / 25 (film tamamen sessiz)
VIRAL INTERSTITIALS: S3 · S12 · S17 · S18   ⛔ THESE MAY NOT BE CUT
KESİLEMEZ (novum döngüsü): S0 · S3 · S9 · S16 · S17 · S24  [ONERME §5]
TITLE:             "THE STANDING WIRE" — başlık izleyiciyi TELE bakmaya
                   gönderir; vaat: düşmeyen, sarkmayan bir hat.
LIBRARY CONTEXT:   aynı raf (yatay 3-5 dk): THE PAYLOAD (gezegen→yanaşma,
                   ama roketle) · THE SKYLIGHT (aynı ortam kartı, yeraltı) ·
                   THE BLACK CRADLE · THE COLD BURN (yanaşma, iticili araç).
                   Bu film o dördünden AYRIŞIR: 0 motor · 0 egzoz · 0 kalkış ·
                   0 iki-gövdeli geniş kare.
```


## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤ ⑧'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 23 sahnede kadrajda (S21 ve S23 insansız)
              mürettebat 0 · pilot 0 · klon 0 · yansıma 0 · ikinci gölge 0
              istasyonda insan 0 (pencerede yüz yok, rıhtımda karşılayan yok)

KASK          25 / 25 sahnede KAPALI · açık 0 sahne
              vizör TEK DÜZ PANEL, görünür koyu çerçeve içinde — kubbe DEĞİL
              optik berrak: 0 ton · 0 ayna kaplaması · 0 çevre yansıması
              sırt ünitesi YOK — düz siluet [D79]
              ⭐ S20'de kamera ARKADA: pozitif yüzey cümlesi zorunlu [D139]

NOVUM         KURAL: bu telin gerilimi yukarıdandır ve nettir — ona bağlanan
              her şey sabit hızda YÜKSELİR.
              İHLAL: yerçekimi altında bir cismin düşmemesi ve yükselmesi.
              KANIT: S0/S3 tel · S9 bağlantı parçası · S16-S17 üzengi ·
              S24 gerilim biter, tel İLK KEZ sarkar.
              ⛔ İhlal sayısı 1. Tele bağlı OLMAYAN her şey normal düşer.

YERÇEKİMİ     0,42 g = 4,12 m/s²
              düşen cisim 1 s'de 2,06 m · 2 s'de 8,24 m
              S17'de halka iki saniyede kadraj dışına düşer
              ⭐ Yürüyüş GERÇEK ZAMANLI — ağır çekim, zıplama, süzülme 0 kare

ATMOSFER      S0-S18  ince atmosfer ~1,0 kPa · gölge zayıf ve YUMUŞAK
                      kenarlı (MEŞRU, hata değil) · dolgu ışığı VAR ·
                      ses boğuk ve tizsiz · rüzgâr hiçbir şeyi deviremez
              S19-S23 VAKUM · gölge MUTLAK SİYAH ve jilet kenarlı ·
                      dolgu ışığı YOK · DIŞ SES SIFIR · lens küresel
              S24     BASINÇLI İÇ HACİM ~1 atm · 0 g · gölge mutlak siyah
                      DEĞİL · dolgu VAR · fan yatağı duyulur
              ⛔ Geçiş SAHNE SINIRINDA: S18 ince atmosferde biter,
                S19 vakumda başlar. Klip içinde ortam değişmez.
              ⚠️ ⑤ ve ⑥ merceklerine: S13-S18'de yumuşak gölge KUSUR DEĞİLDİR;
                S19-S23'te mutlak siyah gölge KUSUR DEĞİLDİR. İkisi ayrı karttır.

EKRAN YÖNÜ    Hedef HER karede kadrajın ÜST yarısındadır.
              Tel HER karede kadının ekran-SAĞINDA ya da tam merkezdedir —
              hiçbir sahnede soluna geçmez.
              İlerleme HER sahnede YUKARI; 25 sahnenin 25'inde sabit.
              Güneş S12-S18'de ekran-SOLDA, S19-S23'te ekran-SOLDA (filtresiz).
              ⛔ Ters dönüş 0 kare · aşağı yönelim 0 kare.

TAŞIYICI      Tele KENETLİ, telin kesik ucundan 400 m yukarıda başlar.
              Kendi motoru YOKTUR; telle birlikte 0,30 m/s yükselir.
              Toplama hızı 0,30 m/s · kadının çıkması gereken 14.000 m ·
              taşıyıcının 13.600 m → eşik ortalama 0,309 m/s.
              Köprüde kalan fark: 0,45 m = 1,5 saniye.
              ⛔ Bu sayıların hiçbiri prompt gövdesinde YOKTUR [D138];
                ekranda hiçbir gösterge, kadran ya da rakam yoktur.
              ⭐ Tam gerekçe: PLAN ⚖️ YARIŞIN ARİTMETİĞİ.

SAYAÇ         METİNSİZ. Telin kesik alt ucu ile kadının GÖZ HİZASI arasındaki
              fark. MONOTONİK, hiç geri dönmez:
                S0  uç botlarının hizasında (0)
                S3  uç plakadan ayrılır, dizinin üstüne çıkar
                S6  uç iki teras aşağıda (kadın önde)
                S9  uç TAM GÖZ HİZASINDAN geçer  ⭐ dönüm
                S12 uç başının epey üstünde
                S16 üzengi tek elinin bir kol boyu üstünde
                S18 iki elle alır — sayaç durur
              ⛔ Kadrajda gösterge, kadran, çentik, skala, rakam: 0.
                Bu film KART 5'in ikinci yönünü (yasak anlatımı siler)
                gösterge KOYMAYARAK değil, gösterge GEREKTİRMEYEREK çözer.

EŞ KADRAJ     S0 ↔ S24   (açılış-kapanış çifti · KAFİYE)
              S3 ↔ S9 ↔ S16   (C kurulumu · el üçlemesi)
              S5 ↔ S7 ↔ S11   (E kurulumu · tırmanış)
              S2 ↔ S4 ↔ S8 ↔ S10 ↔ S12   (F kurulumu · cepheden)

YIPRANMA      MONOTONİK · sabit bölge sayısı [D42 · D147]
                S0-S3    2 bölge  (bot · diz)
                S4-S12   4 bölge  (+ kolların ön yüzü · dirsek)
                S13-S18  5 bölge  (+ göğsün alt yarısı)
                S19-S24  5 bölge  (vakum: eklenmez, silinmez)
              ⛔ Hiçbir sahnede AZALMAZ. Klip İÇİNDE sabittir.
              ⛔ Faz ETİKETİ hiçbir prompta yazılmadı [D155] — yalnız tarifi.

ZORLANMA      Kanal: ELDİVEN YÜZEYİ, deri değil [⛔ D175].
              ✅ "the glove's ribbed segments tighten and lift over the knuckles"
              ✅ "the sleeve's fabric draws taut along the forearm"
              ⛔ "through the glove" kalıbı hiçbir promptta YOK.
              Zorlanma sahneleri: S1 · S3 · S4 · S7 · S9 · S16 · S17 · S18 · S20
              ⛔ Çıplak deri 0 kare. Yaka üstü · bilek · ayak bileği: üçü de kapalı.

SES REGISTER  HUMAN 0 · MACHINE 0 · TELSİZ 0 — film TAMAMEN SESSİZ.
              Ses dokusu merdiveni (monotonik incelme):
                S0-S3   geniş alçak hava tonu + çakıl
                S4-S12  ince hava tonu + eldiven/kaya + nefes
                S13-S18 neredeyse yok — yalnız giysi ve nefes
                S19-S23 DIŞ SES SIFIR — yalnız kask içi (nefes, kumaş)
                S24     fan yatağı GİRER (hava taşır)
              ⛔ ③ SES merceğine: "nothing audible" bulgusu S19-S23 için
                KUSUR DEĞİLDİR, tasarımdır. Kask içi ses o sahnelerde
                tek kanaldır.

IŞIK TAKVİMİ  MONOTONİK ARTAR — hiçbir yerde parlak→karanlık→parlak yok
                S0-S3   −9.000 m · doğrudan güneş YOK · soğuk mavi-gri
                S4-S10  −7.000…−3.000 m · karşı duvarın TEPESİ aydınlanır
                S11     −1.500 m · ilk doğrudan güneş hizasının ÜSTÜNDE
                S12-S18 0…+5.000 m · tam doğrudan güneş · gök koyu çivit
                S19-S23 vakum · filtresiz tek güneş · gök SİYAH · dolgu YOK
                S24     iç · 4500 K nötr beyaz · dolgu VAR
              ⛔ Bu takvim aynı zamanda TEMANIN yayıdır.

YÜZEY RENGİ   TEK CÜMLE, TEK BLOK [⛔ D176]:
              "the rock is dark blue-grey basalt; the loose dust caught in
               its lees is pale gold"
              ⛔ Hiçbir promptun LIGHT bloğu bir yüzeye renk atamaz.
                Kontrast garantisi ÖZNEYİ tarif eder.

İSTASYON      SİLUET: TEK HAT · film boyu DEĞİŞMEZ
              MODÜL 3 · KANAT 2 · RADYATÖR 3 · PORT 1 (alt yüz) ·
              PENCERE 1 büyük + 2 küçük · KELEPÇE 4
              Kapak sınıfı: GENİŞ / YANAŞMA (giysili gövde dönmeden geçer)
              ⛔ Dar kenetlenme kapağı bilerek KULLANILMADI — sırt üniteli
                gövde geçemez, fizik hatası olurdu [UZAY_USSU §2.3]
              Yaşlanma: tek faz — örtü sararmış ve mat · yüzey çukurcuklu ·
              tutamaklarda boya kalkmış · İTİCİ KURUMU YOK (itici yok)
              ⛔ Motor · nozzle · egzoz · alev · plume: 25 sahnenin 25'inde 0

ÖLÇEK MERDİVENİ  aynı nesne (modül gövdesi), aynı eksen, MONOTONİK
                 S19 %0,58 → S20 %3,8 → S21 %73+taşma → S22 %52+taşma →
                 S23 taşma
                 Ölçek şahidi her yapı planında en az bir:
                 S19 ① ön planda eldiven · S20 ① sırttan tam boy ·
                 S21 ②+③ dört kelepçe + taşan kenar · S22 ① taşıyıcı+kadın ·
                 S23 doku
```



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
