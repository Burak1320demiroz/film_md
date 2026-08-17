# THE SECOND SHIP — FAZ 1 / TRANSİT · HAM QA ÇIKTISI

> Model: Gemini · Tarih: 07.08.2026 · Rubrik: `FAZ_01_TRANSIT/FAZ_01_QA_PROMPT.md`
> Girdi: 10 sahnelik derleme reel (S1–S10, 100 s)
> ⚠️ FAZ ölçümüdür — film tablolarına ve 00_INDEX sayacına GİRMEZ.
> Bu dosya modelin ham çıktısıdır, düzenlenmez. Yorum ve aksiyonlar:
> `FAZ_01_TRANSIT/FAZ_01_QA_DERSLER.md`

---

MATERIAL
measured total duration = 100 seconds
number of distinct scene-length segments you can count = 10
Gate passed.

SEGMENT MAP
S1  0:00  0:10  10.0s  Y
S2  0:10  0:20  10.0s  Y
S3  0:20  0:30  10.0s  Y
S4  0:30  0:40  10.0s  Y
S5  0:40  0:50  10.0s  Y
S6  0:50  1:00  10.0s  Y
S7  1:00  1:10  10.0s  Y
S8  1:10  1:20  10.0s  Y
S9  1:20  1:30  10.0s  Y
S10 1:30  1:40  10.0s  Y

PASSPORTS AS SEEN

The woman: Slim build, symmetrical face, brown hair. Dark suit, orange panels. Visible scar on RIGHT eyebrow (deviation). Chest carries cross and horizontal bar indicators.

The man: Athletic, light brown skin, short dark hair, stubble. Dark suit, teal green panels. Burn scar on right cheek. Oversized back module present.

The cockpit: Utilitarian, dark grey/brown. Lit by warm amber console lighting.

The exterior: Dark night environments. Giant moon in S1. Scattered ground wrecks in S2. Planet limb with a bright expanding shockwave in S10.

SCORES

IDENTITY CONTINUITY: 4/10 - Scar flipped on woman; S9 features a bare head.
COSTUME & EQUIPMENT: 4/10 - Bare head in S9 violates helmet lock; scenes S4/S7 swapped.
FIGURE COUNT & CLONE CONTROL: 7/10 - Counts match per frame, no clones.
CAMERA DISCIPLINE: 7/10 - Takes unbroken, no internal cuts.
LIGHT & COLOUR: 6/10 - Correct palettes, but severe bloom in S10.
PHYSICS & MATERIALS: 6/10 - Mostly stable; S10 blooms like a shockwave.
TEXT & SYMBOL DISCIPLINE: 7/10 - No readable text detected.
PHASE CHAIN: 3/10 - Severe scene sequence mix-up (S4-S7 content shifted).
NOVUM DISCIPLINE: 3/10 - S1 moon gives scale; S10 reads as an explosion.
DELIVERY HYGIENE: 7/10 - No watermarks, timing is correct.
Mean: 5.4/10

TOP 5 CRITICAL

1:20 S9 RED: Bare head. Helmet removed entirely; violates absolute phase lock.
0:30 S4 RED: Content swap. Displays S7 man at console instead of S4 corridor.
0:00 S1 RED: Giant moon present. Violates strict rule against scale-giving objects.
1:30 S10 RED: Expanding light blooms with a shockwave effect. Violates "not an explosion".
0:20 S3 YELLOW: Woman's scar is on her right eyebrow. Spec demands left.

SCENE-BY-SCENE FINDINGS
S1: Verified 0 figures, dark plain.
0:00 S1 RED: Giant moon provides scale.

S2: Verified lateral track, wrecks present.
0:10 S2 YELLOW: Wreck pairs lack strict identical symmetry.

S3: Verified 1 figure, amber light.
0:20 S3 YELLOW: Scar is on the right eyebrow instead of the left.

S4: Verified 1 figure present.
0:30 S4 RED: Incorrect content; displays S7 console sequence instead of S4 corridor.

S5: Verified equipment interactions.
0:40 S5 RED: Incorrect content; displays S4 corridor sequence instead of S5 cockpit 2-shot.

S6: Verified seated figures.
0:50 S6 RED: Incorrect content; displays S5 cockpit sequence instead of S6 macro amber strip.

S7: Verified macro console elements.
1:00 S7 RED: Incorrect content; displays S6 amber strip instead of S7 man at side display.

S8: Verified 2 figures in profile, correct layout. Clean.

S9: Verified woman at console.
1:20 S9 RED: Bare head; helmet lock violated.

S10: Verified planet limb.
1:30 S10 RED: Light bursts as a blooming shockwave, failing the non-explosion rule.

PHASE CHAIN
Sequence is fatally broken. S4, S5, S6, and S7 are out of order, destroying continuity. S8 to S9 link fails due to S9's bare head. Planted questions fail due to scale (S1) and explosion visuals (S10).

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Fixable:
S2: Crop or re-frame to isolate identical pairs.
S3: Flip horizontally to correct scar placement.
Requires Regeneration:
S1: Regenerate to remove moon.
S4, S5, S6, S7: Assembly error; requires proper scene slotting.
S9: Regenerate with helmet on.
S10: Regenerate to remove shockwave and bloom.

FLAGS FOR DOCUMENT CHECK
Was the S4-S7 sequence incorrectly assembled in the NLE, or were the prompts misnumbered during generation?
Does the woman's character model have the scar permanently baked onto the right eyebrow?

WHAT WORKED
1:10 S8 composition holds the required layout and separation locks effectively.
0:50 S6 (S5 content) correctly establishes the two-person spatial relationship without cloning.

---

## EK — FAZ 2 KOŞUSU (aynı gün, başarısız)

Faz 2 rubriği tam reel bekliyordu; operatör sahneleri tek tek veriyor.
Modelin tam çıktısı:

MATERIAL GATE FAILED - measured 0 s, 0 segments for faz 2 .mp4. Not the phase reel.

→ Kapı tasarlandığı gibi çalıştı (Ders 75 sınıfı: yetersiz malzeme
puanlanmadı). Rubrik 07.08.2026'da tek-sahne moduna genişletildi.
