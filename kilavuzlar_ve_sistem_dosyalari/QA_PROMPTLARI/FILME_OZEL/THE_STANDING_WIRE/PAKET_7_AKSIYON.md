```
OPERATÖR KÜNYESİ — bu dosyanın TAMAMI tek parça yapıştırılır (rubrik + belge)
film      : THE_STANDING_WIRE
mercek    : ⑦ AKSİYON
mod       : D
girdi     : ____ (master yolu · süre · çözünürlük — koşudan ÖNCE doldur, D160)
SPEC      : THE_STANDING_WIRE_QA_SPEC.md  (aile: yatay)
üretildi  : 05.09.2026 · rubrik_paketle.sh — elle düzenlenmez, SPEC değişince yeniden üret
koşu sonrası: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <rapor.md> --film yatay_3_5_dk_filmler/THE_STANDING_WIRE
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
