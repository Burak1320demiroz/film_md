# ③ 🔊 SES — HAM RAPOR · THE LAST SPAN · 25.08.2026

> ⛔ Model çıktısı OLDUĞU GİBİ. Düzenlenmedi, kısaltılmadı [AGENTS kural ④].
> İşleme, kapı sonuçları ve geçerlilik kararı:
> `../01_FILM_RAPORLARI/THE_LAST_SPAN.md`
>
> ⚠️ Bu koşu bir ÖN KOŞU'dur — kurgu kapısı 3/3 ihlal + D110 oturum
> bulaşması. Skorları hiçbir tabloya işlenmedi.

---

```
FILM: the last stand.mp4
RUNTIME: 1:54 measured
AUDIO STATE: B · SPOKEN LINES: 0 · CUTS COUNTED: 10
NON-SCENE MATERIAL: 1:50-1:54 title card
LINES HEARD: none
DISTINCT VOICES: 0 · REGISTERS: 0 human / 0 machine / 0 unclear
BASELINE: SELF-CONSISTENCY

ARITHMETIC GATE
SCORED CATEGORIES: 4 · SUM: 26.0 · DIVISION: 26.0 / 4 = 6.5
OVERALL SCORE: 6.5/10
VERDICT: AUDIBLE DRIFT, FIXABLE IN THE MIX

AUDIO LEDGER
1a. DIALOGUE LEDGER — none (no dialogue present)
1b. VOICE PASSPORT — none (no dialogue present)
1c. AMBIENCE MAP
| Scene / location | In-out | Ambient bed | Level | Notes |
| S1-S6 / Packed Bridge | 0:00-0:59 | Low wind, metallic creaking, distant dust rustle | Mid | Bed drops out entirely at 0:19 and 0:50 cuts |
| S7-S11 / Empty Lane | 0:59-1:50 | Low wind | Low | Missing the metallic creaking from S1-S6 |
1d. LAYER COUNT
| Timecode | Layers audible | Count | Dialogue intelligible? |
| 0:15 | Wind, metal creak, footsteps, drone | 4 | N/A |
| 1:05 | Wind, footsteps, drone | 3 | N/A |
| 1:45 | Wind, drone swelling | 2 | N/A |
1e. MUSIC LEDGER
| Cue | In-out | Enters on | Exits on | Under dialogue? | Ducked? |
| Synth Drone | 0:00-1:50 | S1 start | S11 end | N/A | N/A |

SCORES SUMMARY
| Category | Score | Critical Issue |
| Speaker Attribution | N/A | no dialogue present |
| Synthetic Voice Tells | N/A | no dialogue present |
| Voice Identity Continuity | N/A | no dialogue present |
| Delivery vs Performance | N/A | no dialogue present |
| Turn-Taking & Acoustics | N/A | no dialogue present |
| Ambience Continuity | 5/10 | -5 · 0:19 (F1) · 0:50 (F2) |
| SFX Causality & Sync | 6/10 | -4 · 1:18 (F1) |
| Mix Hierarchy & Levels | 8/10 | -2 · 0:59 (F1) |
| Music & Silence | 7/10 | -3 · 1:40 (F1) |

SEVERITY TALLY
BLOCKER: 2 · MAJOR: 2 · MINOR: 0

ATTRIBUTION MAP — none (no dialogue present)
VOICE DRIFT COMPARISON — none (no dialogue present)
SYNTHETIC TELL LOG — none (no dialogue present)

AMBIENCE HOLE LOG
| Drops at | Returns at | Location | Absolute silence? | Severity |
| 0:19 | 0:20 | Packed Bridge | Yes | BLOCKER |
| 0:50 | 0:51 | Packed Bridge | Yes | BLOCKER |

CONTRADICTION LOG
| A | B | Element | Cat | What contradicts what | Sev |
| 0:10 | 1:18 | SFX | 7 | Footsteps on metal cars (0:10) have SFX, but setting the metal jerrycan down (1:18) makes no sound | MAJOR |
| 0:50 | 0:59 | Ambience | 6 | Dense metallic creaking bed (0:50) vanishes entirely in the empty lane (0:59) | MAJOR |

THE THREE THAT MATTER
1. Ambience Holes (0:19, 0:50): the absolute digital silence between cuts
   causes the world to momentarily vanish. This reads as a broken file rather
   than a stylistic choice. Cheapest fix: re-level and extend the ambient bed
   across cuts.
2. Missing Jerrycan SFX (1:18): the character sets down a heavy metal object
   in a quiet environment with zero impact sound, breaking physical
   causality. Cheapest fix: add an SFX impact in the mix.
3. Wall-to-Wall Drone (0:00-1:50): the synth drone never breathes or dips,
   leaving no dynamic range for the climax of the edit at 1:50. Cheapest fix:
   re-level and duck the music slightly during the empty lane sequence.

FIXABLE IN THE MIX vs REQUIRES REGENERATION
| Finding | Fix | Cost |
| Ambience dropping at cuts | Extend bed across edits | Low |
| Missing jerrycan impact | Add SFX | Low |
| Wall-to-wall drone | Re-level music | Low |

FLAGS FOR DOCUMENT CHECK
| Observation | Question the document must answer |
| No dialogue present | Was this edit intended to be silent by design, or is the dialogue track missing? |
| Missing metallic ambience in S7-S11 | Was the empty lane intentionally designed to sound dead, or did the model drop the environment layer? |

OUT-OF-SCOPE FLAGS
0:59 - Geography changes drastically from packed bridge to empty lane.
  -> CONTINUITY lens.
```
