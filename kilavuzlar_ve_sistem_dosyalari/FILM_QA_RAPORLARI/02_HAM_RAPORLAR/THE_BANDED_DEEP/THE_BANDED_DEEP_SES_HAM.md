# 🔊 THE BANDED DEEP — SES QA HAM RAPORU

> **Tarih:** 14.08.2026 · **Model:** Gemini · **Rubrik:** SES_VE_DIYALOG_QA_CRITIQUE_PROMPT.md
> **Girdi:** 186 s TAM KURGU (kapı ① ✅) · **AUDIO STATE: B** (kapı ② ✅ — geçerli koşu)
> Model çıktısı aşağıda olduğu gibi.

---

FILM: THE BANDED DEEP
RUNTIME: 03:06 · AUDIO STATE: STATE B — NO VOICES, SOUND ONLY · SPOKEN LINES: 0
DISTINCT VOICES: 0 · REGISTERS: 0 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY

OVERALL SCORE: 6.2/10
VERDICT: SOUNDTRACK HOLDS
Note: No dialogue present. Categories 1–5 N/A per protocol.

## AUDIO LEDGER
1a. DIALOGUE LEDGER — NO DIALOGUE PRESENT.
1b. VOICE PASSPORTS — NO VOICES PRESENT.
1c. AMBIENCE MAP
Canyon Sky/Landing   00:00–00:29  Engine thruster rumble, low wind rush, desert air hum — Mid-High — Hard acoustic shift at 00:29 cut
Canyon Floor Walk    00:30–01:42  Open desert wind, gravel scuffs, suit servo whirrs — Mid — Bed drops slightly in density at shot changes
Cliffside Rappel     01:43–02:01  High-altitude canyon wind, rope tension, piton clicks — Mid — Consistent wind texture
Cliff Base & Wall    02:02–03:06  Deep cavernous rumble, soft wind, tactile brushing — Low-Mid — Fades toward title card
1d. LAYER COUNT
00:24 Thruster jet blast, dust impact rumble, low wind, musical drone — 4
01:45 Anchor impact click, rope friction, gusting wind, score bed — 4
02:02 Wall brush rustle, low room tone, musical pad — 3
1e. MUSIC LEDGER
Cue 1 (Atmospheric Drone) 00:00–03:06 — Enters on ship entry, exits on title fadeout, ducked under thruster landing at 00:24

## SCORES SUMMARY
Speaker Attribution N/A · Synthetic Voice Tells N/A · Voice Identity N/A ·
Delivery vs Performance N/A · Turn-Taking N/A ·
Ambience Continuity 6/10 — beds drop/shift abruptly across visual edits ·
SFX Causality & Sync 5/10 — thruster SFX misaligned with solid dust stream visual at 00:24 ·
Mix Hierarchy & Levels 7/10 — balanced, no clipping ·
Music & Silence 7/10 — score subordinated to action

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 1   🟡 MINOR: 2

## AMBIENCE HOLE LOG
00:29→00:30 landing→walk transition — abrupt tone drop — 🟡 MINOR
01:42→01:43 floor→rappel transition — wind texture hard-cut — 🟡 MINOR

## CONTRADICTION LOG
00:24 ↔ 02:02 — Thruster SFX vs dust visuals — heavy pressurized blast over solid rope-like dust physics at 00:24; soft brushing at 02:02 lacks tactile contact Foley — 🟠 MAJOR

## THE THREE THAT MATTER
1. Abrupt ambient bed cuts at shot boundaries (00:29, 01:42) — crossfade fix.
2. Thruster SFX vs visual physics mismatch (00:24) — AI generation artifact.
3. Missing tactile Foley on surface touch (02:02) — layer in granular contact.

## FIXABLE IN THE MIX vs REQUIRES REGENERATION
Ambient tone jumps 00:29/01:42 — 12-frame crossfades — MIX
Missing glove brush Foley 02:02 — layer granular sand Foley — MIX
Thruster sound mismatch 00:24 — swap blast for softer rumble — MIX

## FLAGS FOR DOCUMENT CHECK
Astronaut completes exploration without vocalizing — is this intended fully silent, or were suit AI logs planned?

## OUT-OF-SCOPE FLAGS
Visual dust anomaly (solid string physics) 00:24 → VIDEO_QA
Glove boundary softening on contact 00:55 / 02:02 → VIDEO_QA / KARAKTER_QA
On-screen title text "THE BANDED DEEP" 03:00 → VIDEO_QA
