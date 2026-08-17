# THE LAST SHIFT — KARAKTER_QA HAM RAPOR

> **Tarih:** 16.08.2026 · **Rubrik:** `QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (rubrik zaten yalnız video) · **Malzeme:** 02:54 kurgu · 2 karakter
> ⛔ Model çıktısı olduğu gibi. Belge cevapları film kaydında:
> `../01_FILM_RAPORLARI/THE_LAST_SHIFT.md`
> ✅ DERS 95 ve DERS 97 bu koşuda TUTTU: mühürlü kask kanıtla yazıldı, yüz
> sütunu kanıt tabanı ölçülerek ⚠️ UNVERIFIABLE bırakıldı.

---

```
INPUT MODE: V
BASELINE: SELF-CONSISTENCY
This review answers "does each character agree with themselves?"
It does NOT answer "does the character match their design sheet?"

FILM: Adsız tasarım (22).mp4
RUNTIME: 02:54 · SCENES OBSERVED: 14 · CHARACTERS TRACKED: 2

OVERALL SCORE: 6/10
VERDICT: IDENTITY BREAK

CHARACTER PASSPORT — Female Investigator
Label:            Female Investigator
First clear view: Scene 3, 0:20
Face:             Unreadable — opaque helmet visor in all appearances.
Hair:             Unreadable.
Eyes:             Unreadable.
Build:            Average height, slim frame.
Costume:          White jumpsuit. Orange stripe on LEFT arm. Orange stripe on LEFT leg.
                  Smooth white moon-style boots. Silver collar ring.
Equipment:        Helmet (sealed — evidence: solid visor pane and collar lock visible).
                  Carries a grey box with cyan light (starting S6).
Wear map:         Clean initially; heavy grey dust on lower boots from 2:10 onwards.
Voice:            N/A (does not speak).

⭐ EVIDENCE BASE
FACE-VISIBLE:     0 s of 174 s total   ·  0 of 14 scenes
COSTUME-VISIBLE:  9 of 14 scenes
MOUTH ON SCREEN:  no

CHARACTER PASSPORT — Male Investigator
Label:            Male Investigator
First clear view: Scene 3, 0:20
Face:             Caucasian, dark stubble, sharp jawline (partially visible through visor
                  at 0:34 and 2:00).
Hair:             Dark, short.
Eyes:             Unreadable.
Build:            Tall, broad shoulders.
Costume:          Olive green jumpsuit. Orange stripe on LEFT arm. Orange stripe on RIGHT
                  leg. Dark grey boots and gloves.
Equipment:        Helmet (sealed — evidence: glass reflections and voice muffling).
                  Metal crowbar held in right hand.
Wear map:         Clean initially; grey dust accumulates on right glove at 0:40.
Voice:            N/A (does not speak on screen; voiceover only).

⭐ EVIDENCE BASE
FACE-VISIBLE:     ~10 s of 174 s total   ·  2 of 14 scenes
COSTUME-VISIBLE:  8 of 14 scenes
MOUTH ON SCREEN:  no

APPEARANCE TABLE
Character   Scene   In-out       Face visible?   State notes
Both        S3      0:20-0:29    Male partial    Walking. Male holds crowbar right hand. Female empty-handed.
Both        S4      0:30-0:49    Male partial    Male pulls door with both hands.
Both        S5      0:50-0:59    No              Walking away. Both visibly empty-handed.
Both        S6      1:00-1:19    No              Male holds crowbar. Female crouches near cyan box on ground.
Both        S7      1:20-1:39    No              Standing. Box is on the ground.
Male        S8      1:40-1:49    No              Right hand (gloved) touches dust in wall cavity.
Both        S10     2:00-2:09    Male partial    Male removes right glove to touch scanner. Crowbar absent.
Female      S11     2:10-2:19    No              Walking away carrying cyan box in right hand. Dusty boots.
Female      S12     2:20-2:29    No              Walking in orange desert. Complete costume identity break.

SCORES SUMMARY
Category                    Score            Critical Issue
Facial Identity             ⚠️ UNVERIFIABLE   Faces obscured by visors or angle for >80% of runtime.
Hair, Build & Proportions   7/10             Build holds, though the suit bulk shifts drastically at 2:20.
Costume Identity            2/10             Female suit completely changes design, details, and side-mapping.
Wear, Damage & Injury       9/10             Dust accumulation on boots and gloves is consistent and one-way.
Equipment State             3/10             Box appears from nowhere; crowbar vanishes without being dropped.
Cross-Cut Action            8/10             General screen direction and positioning hold across cuts.
Count & Separation          10/10            Two distinct characters, no duplicates, no trait merging.
Voice & Performance         N/A              No on-screen speaking mouths.

SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 0

IDENTITY DRIFT MAP — per character
Character   Element     First slip   Undeniable by   Recovered?
Female      Costume     2:20         2:21            No
Male        Equipment   2:00         2:01            No (Character exits film)

WEAR TIMELINE — per tracked mark
Mark                        Acquired   Present at    Absent at ⚠️   One-way?
Dust on Male right glove    0:40       1:40, 2:00    -              Yes
Dust on Female boots        2:10       2:20          -              Yes

CONTRADICTION LOG
Timecode A   Timecode B   Character   Category    What contradicts what                                                                       Severity
0:20         2:20         Female      Costume     Left arm orange band and smooth boots vs. Right arm orange patch, ribbed knees, ribbed boots. 🔴 BLOCKER
0:50         1:00         Female      Equipment   Both characters visibly empty-handed vs. Cyan-lit box suddenly present on the ground.         🟠 MAJOR
1:00         2:00         Male        Equipment   Holds crowbar in right hand vs. reaches with both hands, crowbar completely absent.           🟠 MAJOR

THE THREE THAT MATTER
1. Female Costume Break (2:20): The female character in the orange desert wears a
   completely different suit model, boot model, and mirrored insignia from her scenes in
   the grey outpost. The viewer immediately reads this as footage of a different person or
   from a different project. Cheapest fix: Cut the 2:20 scene entirely.
2. The Teleporting Box (0:50 vs 1:00): The characters walk away from the door with
   explicitly empty hands. In the very next scene, a highly specific grey box with a cyan
   light is sitting on the ground next to them, which they then carry for the rest of the
   film. Cheapest fix: Accept it as a time-jump/off-screen discovery, though it feels jarring.
3. The Vanishing Crowbar (1:00 vs 2:00): The male uses the crowbar as his primary prop, but
   when he needs two hands to remove his glove for the climax, the crowbar vanishes from
   existence rather than being placed on the ground. Cheapest fix: Accept it / crop tighter.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding                      Fix                                                       Cost
Female suit change at 2:20   Cut S12 (orange desert walk) entirely.                    Loss of 10 seconds.
Box appearing at 1:00        None without regeneration or inserting a discovery shot.  Acceptable error.
Crowbar vanishing at 2:00    None without regeneration.                                Acceptable error.

FLAGS FOR DOCUMENT CHECK
Observation                                          Question the document must answer
Female suit completely redesigns at 2:20.            Was this scene generated from an older/different prompt,
                                                     or is this an intentional "flash forward" with a new suit?
Helmet visors appear dark but lack distinct pane     Does the character design specify transparent visors,
reflections in S6 and S7.                            or completely opaque helmets?

OUT-OF-SCOPE FLAGS
2:09: Male investigator's bare fingers merge and melt into the metal scanner plate. → VIDEO_QA
0:20-2:54: Voiceover audio consistency, character attribution, and lip-sync absence. → SES_QA
2:54: The narrative halts on a text card before the scanner action resolves. → SENARYO_QA
```
