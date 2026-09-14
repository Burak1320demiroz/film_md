# HAM RAPOR — THE KEPT LIGHT · ③ SES (T3)

```
KÜNYE: girdi "The Kept Light" (yol/çözünürlük yok · süre TAHMİN) [D160]
⛔ ① SPEC KAPISI: ③ tasarım gereği mod V koşar — bu mercek için mod V DOĞRUDUR.
⛔ ⑪ ÖLÇÜM: SES KANALI VAR ✅ (rapor AUDIO STATE B dedi ✅ — D136/D137 ikisi de
   temiz). AMA:
   · I = −16,4 LUFS (ihraç kilidi −14) · Peak = +0,9 dBFS (kilit −1,0 dBTP)
     → 🔴 TESLİM KUSURU, rapor bulgusu değil.
   · PLANLI MUTLAK SESSİZLİK 209,0-219,0 s TESLİM EDİLMEDİ. Üç eşikte
     (−50/−40/−30 dB) o bantta hiçbir sessizlik aralığı yok. Raporun kendi
     ambiyans haritası da orada "Deep Tunnel · High" yazıyor — yani rapor
     doğru DUYDU, ama SPEC'i görmediği için bunun bir TESLİM KUSURU olduğunu
     yazamadı. ⑤ BEŞİNCİ SATIR (SUSKUNLUK) bu koşuda ÖLÇÜMLE kapandı.
⛔ ⑪ ÖLÇÜM: kesme 20 → gerçek 24. Δ 4.
⛔ ARİTMETİK: 4 kategori · Σ 27,0 · 27,0÷4 = 6,75 → rapor 6,8 ✅
⛔ TALLY: 🟠3 🟡2 = 5; ambiance hole log + contradiction log'da yazılı 5 ✅
```

---

FILM: The Kept Light
RUNTIME: ~4:15 ESTIMATED
AUDIO STATE: B · SPOKEN LINES: 0 · CUTS COUNTED: 20
NON-SCENE MATERIAL: 4:10-4:15 title card
LINES HEARD: none — no dialogue present
DISTINCT VOICES: 0 · REGISTERS: 0 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY — this review measures whether the soundtrack agrees with itself and with the picture, not whether it matches a script.

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  4
SUM OF SCORES:      27.0
DIVISION:           27.0 ÷ 4 = 6.8      ← this is OVERALL SCORE

OVERALL SCORE: 6.8/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX
The film features no dialogue, relying entirely on SFX and ambience. The primary defect is the ambient bed dropping out at scene cuts and missing causality on heavy impacts. All issues can be resolved in a standard mix session.

## AUDIO LEDGER

### 1a. DIALOGUE LEDGER
(no dialogue)

### 1b. VOICE PASSPORT
(none - no voices present)

### 1c. AMBIENCE MAP

| Scene / location | In-out | Ambient bed (what you hear) | Level | Notes |
|---|---|---|---|---|
| Metal Room | 0:00-0:44 | Low mechanical hum, air hiss | Moderate | Drops abruptly at 0:10 cut |
| Rock Cavern | 0:44-0:49 | Deeper rumble, echo return | High | Hard cuts in, no crossfade |
| Metal Room | 0:49-1:40 | Low mechanical hum | Moderate | Drops at 0:49, 1:10, 1:20 |
| Space Void | 1:40-1:49 | Deep low-end drone | Moderate | - |
| Metal Room | 1:49-3:19 | Low mechanical hum | Moderate | Drops at 2:09, 2:39 |
| Deep Tunnel | 3:19-3:49 | Hollow wind rush, deep rumble | High | - |
| Metal Room | 3:49-4:10 | Low mechanical hum | Moderate | - |

### 1d. LAYER COUNT

| Timecode | Layers audible (name each) | Count | Dialogue intelligible? |
|---|---|---|---|
| 0:05 | SFX (tools), Ambience (room tone) | 2 | N/A |
| 1:25 | SFX (chain/box), Ambience (room) | 2 | N/A |
| 3:25 | SFX (falling cylinder), Ambience (tunnel drone) | 2 | N/A |

### 1e. MUSIC LEDGER

| Cue | In-out | Enters on | Exits on | Under dialogue? | Ducked? |
|---|---|---|---|---|---|
| Low Drone | 1:40-1:49 | Space exterior cut | Cut to interior | N/A | N/A |
| Deep Drone | 3:19-3:49 | Tunnel view | Cut to interior | N/A | N/A |

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|---|---|
| Speaker Attribution | — | no in-scope source |
| Synthetic Voice Tells | — | no in-scope source |
| Voice Identity Continuity | — | no in-scope source |
| Delivery vs Performance | — | no in-scope source |
| Turn-Taking & Acoustics | — | no in-scope source |
| Ambience Continuity | 5/10 | -5 · 0:10, 0:49, 1:20, 2:09, 2:39 (ambience drops at cuts) |
| SFX Causality & Sync | 6/10 | -4 · 1:50 (missing impact), 0:10-0:15 (sync drift) |
| Mix Hierarchy & Levels | 8/10 | -2 · 0:49 (SFX level jumps noticeably) |
| Music & Silence | 8/10 | -2 · 4:10 (hard cut-off at title card) |

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 2

## ATTRIBUTION MAP
(no lines)

## VOICE DRIFT COMPARISON
(no voices)

## SYNTHETIC TELL LOG
(no voices)

## AMBIENCE HOLE LOG

| Drops at | Returns at | Location | Absolute silence? | Severity |
|---|---|---|---|---|
| 0:10 | 0:11 | Metal Room | No, just floor drop | 🟠 MAJOR |
| 0:49 | 0:50 | Metal Room | No, just floor drop | 🟠 MAJOR |
| 1:20 | 1:21 | Metal Room | No, just floor drop | 🟡 MINOR |
| 2:09 | 2:10 | Metal Room | No, just floor drop | 🟡 MINOR |

## CONTRADICTION LOG

| Timecode A | Timecode B | Element | Category | What contradicts what | Severity |
|---|---|---|---|---|---|
| 0:44 | 0:49 | Ambience | 6 | Rock cavern tone vs metal room tone levels jump abruptly | 🟠 MAJOR |

## THE THREE THAT MATTER
Ambience Drops at Cuts: The room tone dies momentarily at almost every edit (e.g., 0:10, 0:49), exposing the generative clip boundaries. Fix: Lay down a continuous room tone stem under the entire edit.

Missing Causality on Impacts: At 1:50, a heavy metal cylinder is dropped but lacks a proportional impact sound or recoil clatter. Fix: Add a heavy metal foley impact.

Audio Hard Cut at Tail: The audio completely cuts off exactly at 4:10 when the title card appears, leaving dead air instead of a natural decay. Fix: Add a reverb tail or fade out to the room tone.

## FIXABLE IN THE MIX vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Ambience drops at cuts | Lay continuous room tone | Low |
| Missing cylinder impact | Add foley | Low |
| SFX sync drift at 0:10 | Slip audio or add footsteps | Low |
| Hard cut-off at title card | Add fade/reverb tail | Low |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Total lack of dialogue or breathing. | Was the astronaut intended to be completely silent (no comms, no breathing inside the helmet)? |

## OUT-OF-SCOPE FLAGS
none
