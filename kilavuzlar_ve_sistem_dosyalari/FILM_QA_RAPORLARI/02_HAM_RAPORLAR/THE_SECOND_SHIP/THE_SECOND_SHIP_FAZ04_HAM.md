# THE SECOND SHIP — FAZ 4 / TARLA · HAM QA ÇIKTISI

> Model: Gemini · Tarih: 09.08.2026 · Rubrik: `FAZ_04_TARLA/FAZ_04_QA_PROMPT.md`
> Girdi: tek reel (ölçüm 93 s, 10 segment: 6×10.0 s + 3×8.0 s + 1×9.0 s) · MODE R
> ⚠️ Rubrik MODE T'yi (10 ayrı dosya) TERCİH EDİLEN mod ilan etmişti;
> koşu yine reel ile yapıldı ve S32↔S33 segmentleri takas çıktı.
> ⚠️ FAZ ölçümüdür — film tablolarına ve 00_INDEX sayacına GİRMEZ.
> ⚠️ Skor 5.2 KISMEN KİRLİDİR: iki segment (S32/S33) çapraz-kirli,
> kalan sekizi kendi satırına karşı ölçüldü. Ayrıntı ve aksiyonlar:
> `FAZ_04_TARLA/FAZ_04_QA_DERSLER.md`
> Bu dosya modelin ham çıktısıdır, düzenlenmez.

---

MATERIAL
Mode R (ONE REEL), 1 file received, measured duration 93 seconds. Passed gate.

SEGMENT MAP
S31: 0:00-0:08 (8 s) - short.
S32: 0:08-0:18 (10 s) - segment mapped to S32 plainly contradicts its row (content shows a man testing the leg, matching S33).
S33: 0:18-0:28 (10 s) - segment mapped to S33 plainly contradicts its row (content shows leg alone with pouring sand, matching S32).
S34: 0:28-0:36 (8 s) - short.
S35: 0:36-0:44 (8 s) - short.
S36: 0:44-0:54 (10 s) - 10.0 s.
S37: 0:54-1:04 (10 s) - 10.0 s.
S38: 1:04-1:14 (10 s) - 10.0 s.
S39: 1:14-1:24 (10 s) - 10.0 s.
S40: 1:24-1:33 (9 s) - short.

COPY MATERIAL TABLE

Matte bone-grey single tone: S32 (fails - rendered as metallic/plastic leg), S34 (pass), S35 (fails - rendered as a real steel cargo ship with rust/paint), S37 (pass), S38 (pass), S39 (pass).

No markings: S32 (pass), S34 (pass), S35 (fails - clear windows, radar masts, and vents visible at 0:40), S37 (pass), S38 (pass), S39 (pass).

No light of its own: S32 (pass), S34 (pass), S35 (pass), S37 (pass), S38 (pass), S39 (pass).

Rooted with no base line: S32 (pass), S34 (pass), S35 (fails - distinct base line where sand meets the hull; looks buried, not grown), S38 (pass), S39 (pass).

Never moves: S33 (mapped segment fails - continuous waterfall of sand pouring from the leg at 0:20), S34 (pass), S35 (pass), S37 (pass), S38 (pass), S39 (pass).

Root veins (S33): Not visible in mapped segment.

WHITE FIGURE LEDGER
S31: No.
S32: No.
S33: No.
S34: No.
S35: No.
S36: No.
S37: No.
S38: No.
S39: No.
S40:

Height: Normal human proportions, not distinctly taller (2.10m).

Dustlessness: Fails. Suit is visibly scuffed and carries dirt/shadows in seams.

Arm length: Standard, not elongated.

Finger count: Unverifiable (hands out of clear view).

Visor opacity: Opaque, but white/light grey instead of dark grey-green.

Rooted-or-standing: Standing on dust.

Turn: Yes, one continuous incomplete rotation.

Deviation: Figure has a bulky backpack and corrugated hoses; back is not flat.

PASSPORTS AS SEEN

The woman: Dark hair, pale skin. Suit is dark grey with faded orange/brown accents. Wears a helmet. Has a visible scar on her RIGHT eyebrow (viewer's left).

The man: Short dark hair, stubble. Suit is dark with muted/teal accents. Taller than the woman.

The stone copies: The leg (S33 content) looks metallic/plastic. The giant ships in S34 look like metal wrecks. The ship in S35 is a highly detailed, realistic steel cargo ship with windows. The suits in S38 and S39 are solid matte grey stone.

The ground: Dry, cracked basalt and dust.

The light: S31 features a warm dawn sun frame left. S32-S40 maintain soft 4400K daylight, key light from frame left.

The Watcher: Appears only in S40. White suit with panel lines, dirt, and a backpack. Opaque white visor.

SCORES

COPY MATERIAL DISCIPLINE: 3 - S35 fails completely (ship is real metal with windows).

NO REAL-TIME GROWTH: 7 - Continuous sand pouring in S33 segment; ghosting morphs in S31.

THE WHITE FIGURE LOCK: 4 - Kept out until S40, but the S40 Watcher fails the flat-back and pristine specifications entirely.

IDENTITY CONTINUITY: 5 - Woman's scar is mapped to the wrong side of her face in S36.

COSTUME, EQUIPMENT & FIGURE COUNT: 6 - Orange/teal accents present but subdued; S40 Watcher has forbidden backpack.

CAMERA DISCIPLINE: 3 - S34 tracks from behind instead of side-on; segments S32 and S33 are completely swapped in the render.

PHYSICS & MATERIALS: 7 - Dust and gravity look acceptable, but S35 ship looks buried rather than grown.

LIGHT DISCIPLINE: 9 - Dawn to locked daylight transition is highly successful and holds direction.

PHASE CHAIN: 3 - S32 and S33 contents are swapped, breaking the sequence of the timeline.

DELIVERY HYGIENE: 5 - Four out of ten segments failed to meet the 10.0s requirement.
MEAN SCORE: 5.2

TOP 5 CRITICAL

0:08 / S32 & S33 - SEVERITY RED: Segments S32 and S33 are physically swapped in the reel. S32 shows the man kicking the leg; S33 shows the leg alone. This destroys the phase chain.

0:38 / S35 - SEVERITY RED: The cargo ship is rendered as real steel with windows, radar, and rust, sitting on a base line. It completely violates the Copy Material Law (must be solid bone-grey stone, unmarked, rooted).

1:20 / S39 - SEVERITY RED: A fully sculpted, detailed stone human face (eyes closed, nose, lips) is visible inside the visor recess. The spec explicitly demands blind, faceless stone.

1:26 / S40 - SEVERITY RED: The Watcher has a bulky backpack, visible seams, and dirt. Spec demands a seamless, dustless, flat back.

0:28 / S34 - SEVERITY RED: The camera tracks the walkers from behind, looking down the lane. Spec strictly demands a lateral, side-on track to establish the pairing law across the frame.

SCENE-BY-SCENE FINDINGS
S31: Verified dawn, warm left key, two walkers.

0:04 (S31) - RED: Bizarre temporal ghosting artifact. Transparent duplicates of the walkers split off and overlay the frame.
S32: (Mapped 0:08-0:18)

0:08 (S32) - RED: 1 figure present (man testing leg). Content belongs to S33. Audited against S32, this is a blocker.
S33: (Mapped 0:18-0:28)

0:18 (S33) - RED: 0 figures present. Content belongs to S32.

0:20 (S33) - YELLOW: Continuous waterfall of sand pours from the leg, implying motion/growth.
S34: Verified deep focus, wrecks paired.

0:28 (S34) - RED: Camera tracks from behind, completely missing the lateral side-on framing.
S35: Verified slow push-in.

0:38 (S35) - RED: Ship is metal, rusty, has windows and radar masts, and sits on a distinct sand baseline instead of being grown from continuous stone.
S36: Verified tight close-up, lack of emotion, 0 speech.

0:46 (S36) - RED: The scar is on her RIGHT eyebrow. Spec demands LEFT eyebrow.
S37: Verified hand touching stone, no deformation.

0:54 (S37) - RED: The background blurred orange stripe is entirely missing. There is no original behind the copy to teach the limit of the rule.
S38: Verified lane, stone figure standing from behind.

1:04 (S38) - YELLOW: The woman is mostly in frame from behind, rather than just a soft foreground shoulder.
S39: Verified 0 living figures, push-in.

1:20 (S39) - RED: A distinctly sculpted face occupies the visor recess instead of an empty hollow.
S40: Verified Watcher rotation, incomplete turn.

1:25 (S40) - RED: Watcher has a backpack, corrugated hoses, seams, and dirt. Visor is opaque white, not dark grey-green.

PHASE CHAIN
The light discipline successfully anchors the phase—dawn in S31 correctly snaps to a locked daylight that holds its left key through S40. However, the physical swapping of S32 and S33 destroys the narrative chain (we see him test the leg before it is established). S34 breaks the spatial continuity by shooting from behind instead of side-on.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION

Edit: The reel can be chopped and segments 2 and 3 reordered to fix the S32/S33 swap, assuming the native clips can be rearranged.

Regeneration: S31 (ghosting morph), S34 (wrong camera angle), S35 (metal ship instead of stone), S36 (wrong scar placement), S37 (missing background original), S39 (stone face in visor), S40 (Watcher backpack/seams).

FLAGS FOR DOCUMENT CHECK

Were the F4 clips uploaded in the wrong order, causing the S32/S33 swap, or did the generation batch output them with reversed filenames?

The model actively resisted making S35 matte stone and populated it with ship logic (windows, radar). Is the prompt for S35 adequately suppressing standard ship keywords?

The model hallucinated a face in S39's visor. Does the prompt include negative weight for "face, skull, features"?

WHAT WORKED

0:00 (S31): The lighting transition into this phase is beautiful; the soft-edged dawn shadows and pale moon perfectly match the spec.

1:04 (S38): The stone suit from behind is a flawless execution of the Copy Material Law—solid, matte, dusty, and perfectly still.

1:25 (S40): The fluid, continuous rotation of the Watcher carries excellent weight and obeys the movement lock beautifully, despite the costume failures.
