# THE LAST SHIFT — VIDEO_QA (TEKNİK) HAM RAPOR

> **Tarih:** 16.08.2026 · **Rubrik:** `QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> **Mod:** V ⛔ **ÖN KOŞU** — SPEC bloğu planın §0.15'inde HAZIRDI, yapıştırılmadı [DERS 94]
> **Malzeme:** 176 s (rapor ölçümü) kurgu · dosya adı `Adsız tasarım (22).mp4`
> ⛔ Model çıktısı olduğu gibi. Belge cevapları ve kilit çelişkileri film kaydında:
> `../01_FILM_RAPORLARI/THE_LAST_SHIFT.md`

---

```
INPUT MODE: V

BASELINE: SELF-CONSISTENCY + PHYSICS
This review answers "is this clip internally consistent and physically
believable?"  It does NOT answer "does this clip match its design document."

FILM: (not supplied)
FORMAT: (not supplied)
SCENE: (not supplied)
VIDEO DURATION: 176s
SPEC BLOCK PROVIDED: no — mode V

OVERALL SCORE: 5/10 (mean of 7 scored categories. 3 categories excluded as UNVERIFIABLE)
VERDICT: REGENERATE

SCORES SUMMARY
Category                Score          Critical Issues
Character               3/10           Hand fusion at contact point.
Scale & Physics         5/10           General scale holds; dust impacts lack density.
Camera                  UNVERIFIABLE   Cuts present; scene boundaries unverified.
Lighting                6/10           Overcast, consistent diffuse lighting.
Environment             5/10           Radical environment shift mid-video.
Creatures               UNVERIFIABLE   No biological creatures present.
Particles & Materials   4/10           Dust clouds behave as flat 2D assets.
Dialogue & Audio        6/10           Voiceover matches; character consistency → SES_QA.
Frame Anchor Fidelity   UNVERIFIABLE   No anchor images provided.
Negative Violations     2 count        NEGATIVE BOX COUNT: 2 · LINKED FINDINGS: 2 · UNLINKED: 0
Motion Quality          5/10           Generally stable but slightly rigid motion.

SCENE INVENTORY — mode V only
MATERIAL
What you were given:  compilation edit · duration 176s
Cuts you can see:     Multiple cuts (e.g., 0:09, 0:29, 0:49, 1:09, 1:19, 1:49, 1:59, 2:29, 2:49)
Aspect ratio:         16:9

THE CHARACTER — as first clearly seen
Face / hair / marks:  Visors down, faces obscured. First frame fully visible: 0:20
Suit / wardrobe:      Female in white suit with orange armbands; Male in green suit with
                      orange armbands. Helmets with visors.
Wear / dirt:          Mild scuffing on boots and lower legs.
Equipment:            Metallic carrying box, crowbar.

THE WORLD — as the footage shows it
Gravity read:         1g (normal Earth-like step weight).
Atmosphere read:      Dense (dust hangs heavily, sound carries).
Light sources:        Overcast/diffuse skylight. Directional shadows are soft. Traceable.
Location:             Brutalist desert outpost / checkerboard terrain.

MOTION
Camera:               Mix of static lockoffs, slow tracking shots, and aerial pushes.
Subject:              Slow, deliberate walking and basic physical interaction.

SEVERITY TALLY
🔴 BLOCKER: 2    🟠 MAJOR: 2    🟡 MINOR: 1

TOP 3 CRITICAL ERRORS (most impactful)
2:50 — 🔴 BLOCKER — Burned-in text and subtitles appear on screen.
2:09 — 🔴 BLOCKER — Bare hand fuses with the metallic scanner plate upon contact.
2:20 — 🟠 MAJOR  — Character's suit radically changes design, patches, and armband
                   configuration between shots.

DETAILED ERROR LOG
2:50 — 🔴 BLOCKER — Category 10 — On-screen text ("THE LAST SHIFT") and burned-in
                    subtitles appear.
2:09 — 🔴 BLOCKER — Category 1 — Hand geometry breakdown; index finger melts into the
                    metal plate.
2:20 — 🟠 MAJOR   — Category 1 — Suit drift; female character's suit completely changes
                    design and detailing.
1:52 — 🟠 MAJOR   — Category 7 — Low-density particle physics; massive dust cloud moves
                    uniformly like a 2D fluid simulation.
0:41 — 🟡 MINOR   — Category 1 — Glove touching door handle is stiff, lacking natural
                    articulation.

WHAT WORKED WELL (keep these in future prompts)
- The brutalist, overcast lighting is highly consistent and avoids typical AI bloom.
- The color grading remains remarkably stable across disparate environments.

PROMPT IMPROVEMENT SUGGESTIONS
1. ADD to video prompt: "Clean framing, absolutely no text, subtitles, or watermarks."
   → prevents burned-in training text.
2. ADD to image prompt: "Fingers maintaining sharp, distinct separation from the metal
   surface." → prevents contact hand morphing.
3. REMOVE from image prompt: "Epic dust storm" → causes 2D fluid-like particle behavior;
   replace with "Heavy, physically dense particulate matter settling naturally."

NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [11, 28, 31, 33].

FLAGS FOR DOCUMENT CHECK — mode V only
0:09 — multiple hard cuts observed — QUESTION: what are the planned scene boundaries for
       this compilation?
2:20 — sudden shift to an orange Mars-like atmosphere — QUESTION: is this a scripted scene
       location change?
2:30 — landscape changes to a distinct checkerboard pattern — QUESTION: was this specific
       aerial topography documented?

QUALITY TABLE ROW (paste into LESSONS_LEARNED.md)
| (not supplied) Ⓥ | (not supplied) | 3 | 5 | UNV | 6 | 5 | UNV | 5 | 5/10 |
```
