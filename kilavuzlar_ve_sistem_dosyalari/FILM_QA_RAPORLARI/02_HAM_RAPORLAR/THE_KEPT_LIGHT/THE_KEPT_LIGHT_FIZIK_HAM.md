# HAM RAPOR — THE KEPT LIGHT · ⑥ FİZİK (T6)

```
KÜNYE: girdi "The Kept Light" (yol/çözünürlük yok · süre TAHMİN) [D160]
⛔ ① SPEC KAPISI: SPEC VAR + PAKET_6_FIZIK.md (C bloğunun sayısal kilitleri
   gömülü) VAR, rapor `INPUT MODE: V` → koşu TEKRARLANIR [D129].
⛔ ⑩ ÖNERME KAPISI — BU RAPORUN BAŞLIK BULGUSU DÜŞER [D166]:
   raporun PREMISE REGISTER'ı "none" yazıyor. SPEC C bloğu NOVUM'u yazılı:
   "Kapağın altına bırakılan hiçbir şey düşmesini bitirmez… indikçe daha az
   iner." SPEC'in kendi satırı: "Bir mercek bu davranışı 'yerçekimine aykırı'
   diye 🔴 yazarsa bulgu ⑩'da DÜŞER — filmin kuralı budur."
   → L5 (1,0 m/s²) · L7 (2,0 m/s²) · "TWO GRAVITIES" verdict'i DÜŞER.
   AYAKTA KALAN: L3 "released, drift UP" — novum "aşağı giden yukarı gelmez"
   diyor. Bu bir İHLALDİR ve ⬜ AÇIK (kareyle çözülecek).
⛔ CETVEL: "4.5m (hatch scale)" · "25m (tunnel width)" — ikisinin de cetveli
   adlandırılmamış (Kart F2: cetvelsiz FAIL DÜŞER).
⛔ ⑪ ÖLÇÜM: sahne 20 / kesme 20 → gerçek 25 / 24. Δ 5.
⛔ ARİTMETİK: 7 kategori · Σ 36,0 · 36,0÷7 = 5,142 → rapor 5,1 ✅
⛔ TALLY: 🔴1 🟠2 🟡1 = 4; SCORES SUMMARY + contradiction log'da yazılı 4 ✅
```

---

INPUT MODE: V
FILM: The Kept Light
RUNTIME: ~4:15 ESTIMATED
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 20 · CUTS COUNTED: 20
NON-SCENE MATERIAL: 4:10-4:15 title card
LINES HEARD: none — nothing audible to me
GRAVITY: 1.0 m/s² – 2.0 m/s² (based on dropped cylinder), contradicted by 9.8 m/s² human walk cycles and 0 m/s² floating tools.
PREMISE REGISTER: none — localized zero-gravity for tools is not established as a world rule; it behaves as a generation artifact against normal-gravity human motion.

ARITHMETIC GATE
SCORED CATEGORIES:  7
SUM OF SCORES:      36.0
DIVISION:           36.0 ÷ 7 = 5.1

OVERALL SCORE: 5.1/10
VERDICT: TWO GRAVITIES
The film features real-time, normal-gravity human walk cycles occupying the same frame as zero-gravity floating tools and slow-falling objects, implying multiple conflicting physical laws without a covering premise.

## PHYSICS LEDGER

| # | Timecode | Event | Duration | Distance (est. + RULER) | Implied value | Consistent with? |
|---|---|---|---|---|---|---|
| L1 | 0:02-0:08 | Pliers float mid-air | 6.0 s | ~0.0m (static) | g = 0 m/s² | Nothing |
| L2 | 0:10-0:15 | Astronaut walking | 5.0 s | ~3m (stride ≈ 0.6m) | g ≈ 9.8 m/s² | Earth normal |
| L3 | 1:06-1:09 | Pliers released, drift up | 3.0 s | -0.2m (hatch rim) | g < 0 m/s² | Nothing |
| L4 | 1:24-1:28 | Hoisted box swings | 4.0 s | ~0.5m arc | Heavy mass | L2 gait |
| L5 | 1:50-1:53 | Cylinder dropped | 3.0 s | ~4.5m (hatch depth) | g = 1.0 m/s² | Nothing |
| L6 | 2:10-2:15 | Box lowered by rope | 5.0 s | ~4m (rope length) | Controlled | N/A |
| L7 | 3:20-3:25 | Cylinder falls in well | 5.0 s | ~25m (tunnel scale) | g = 2.0 m/s² | Nothing |

## NUMERIC LOCK VERIFICATION — MODE D ONLY

| Lock | Stated | Measured on screen | Δ | Verdict |
|---|---|---|---|---|
| N/A | N/A | N/A | N/A | NOT EXERCISED |

## SCORES SUMMARY

| # | Category | Score | Critical Issue |
|---|---|---|---|
| 1 | Gravity & Free Fall | 3/10 | 🔴 L1, L2, L5 show 0G, 1G, and 0.1G simultaneously. |
| 2 | Ballistics & Trajectories | 4/10 | 🟠 L3 objects float upward when dropped. |
| 3 | Impact & Momentum | 5/10 | 🟡 L4 box has momentum; L1 tools lack mass. |
| 4 | Material Behaviour | 6/10 | Rope in L6 stays taut under tension. |
| 5 | Particles & Atmosphere | — | no in-scope source |
| 6 | Scale & Measurement | 7/10 | Box and tools maintain relative size. |
| 7 | Rates & Timing | — | no in-scope source |
| 8 | Light & Shadow Physics | 7/10 | Shadows agree with overhead lamps. |
| 9 | Human Biomechanics | 4/10 | 🟠 L2 normal gait contradicts 0G environment. |

## PRESENCE STRING
11111111111111111111

## SEVERITY TALLY
🔴 BLOCKER: 1   🟠 MAJOR: 2   🟡 MINOR: 1

## GRAVITY TABLE

| Ledger row | Timecode | Height (est. + ruler) | Time | Implied g | vs film's g |
|---|---|---|---|---|---|
| L5 | 1:50 | 4.5m (hatch scale) | 3.0s | 4.5 = 0.5·g·3² ⟹ g = 1.0 m/s² | vs 9.8 m/s² |
| L7 | 3:20 | 25.0m (tunnel width) | 5.0s | 25.0 = 0.5·g·5² ⟹ g = 2.0 m/s² | vs 9.8 m/s² |

## RATE TABLE

| Rate | First measure (timecode) | Second measure (timecode) | Verdict |
|---|---|---|---|
| N/A | N/A | N/A | N/A |

## CONTRADICTION LOG

| Ledger rows | Timecodes | Cat. | What contradicts what | Severity |
|---|---|---|---|---|
| L1 vs L2 | 0:02 vs 0:10 | 1 | Floating objects (0G) vs normal human walking gait (1G). | 🔴 BLOCKER |
| L3 vs L5 | 1:06 vs 1:50 | 2 | Released objects float upward vs dropping slowly downward. | 🟠 MAJOR |

## THE THREE THAT MATTER
Split-Frame Gravity: Humans walk in 1G while tools float in 0G. Breaks fundamental physics. Fix: Accept it as surrealism or regenerate walking shots to zero-g wirework style.

Upward Float: Dropped tools drift upwards. Confuses mass expectations. Fix: Trim shot before tools drift.

Inconsistent Fall Rates: Cylinder drops at 1.0 m/s² then 2.0 m/s². Fix: Speed ramp the L5 descent in edit.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Inconsistent fall times (L5/L7) | Speed ramp the descent clips | Low |
| Tools floating upwards (L3) | Trim tail of the clip | Low |
| Walking gait in 0G room (L2) | Regenerate with low-g motion prompts | High |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| The astronaut walks normally but tools float. | Does the plan call for localized gravity boots, or is this a zero-g environment? |

## OUT-OF-SCOPE FLAGS
Suit textures shift during the rope pull (CONTINUITY lens).
