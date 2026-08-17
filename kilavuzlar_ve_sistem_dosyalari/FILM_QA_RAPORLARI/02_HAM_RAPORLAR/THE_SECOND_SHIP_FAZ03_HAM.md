# THE SECOND SHIP — FAZ 3 / İMDAT · HAM QA ÇIKTISI

> Model: Gemini · Tarih: 08.08.2026 · Rubrik: `FAZ_03_IMDAT/FAZ_03_QA_PROMPT.md`
> Girdi: tek reel ("faz 3", 10 segment: 8×10.0 s + 2×8.0 s) · MODE R
> Not: ilk deneme ESKİ kapıda düştü (ölçüm "87s", kapı 100±3 istiyordu);
> kapı 75–105 s bandına genişletilip segment haritası ölçümlü hâle
> getirildi, ikinci koşu geçti. İki koşunun süre ölçümü tutmuyor
> (87 s vs 96 s) — modelin süre ölçümü tek başına güvenilir değil.
> ⚠️ FAZ ölçümüdür — film tablolarına ve 00_INDEX sayacına GİRMEZ.
> ⚠️ Skor 3.7 KİRLİDİR: reel yanlış sırada kurulmuş (5 slot kayık),
> 0:10–0:30 ve 0:50–1:20 verdiktleri çapraz-kirli. Ayrıntı ve aksiyonlar:
> `FAZ_03_IMDAT/FAZ_03_QA_DERSLER.md`
> Bu dosya modelin ham çıktısıdır, düzenlenmez.

---

MATERIAL GATE FAILED - wait, no, the gate passed.
MODE R (ONE REEL) - received 1 video file, measured duration 1:36 (96 seconds).

SEGMENT MAP
S21 | 0:00 - 0:10 | 10.0 s | Pass
S22 | 0:10 - 0:20 | 10.0 s | Pass (Content heavily contradicts mapped row - resembles S23)
S23 | 0:20 - 0:30 | 10.0 s | Pass (Content heavily contradicts mapped row - resembles S22)
S24 | 0:30 - 0:40 | 10.0 s | Pass
S25 | 0:40 - 0:50 | 10.0 s | Pass
S26 | 0:50 - 1:00 | 10.0 s | Pass (Content heavily contradicts mapped row - resembles S27)
S27 | 1:00 - 1:10 | 10.0 s | Pass (Content heavily contradicts mapped row - resembles S28)
S28 | 1:10 - 1:20 | 10.0 s | Pass (Content heavily contradicts mapped row - resembles S26)
S29 | 1:20 - 1:28 | 8.0 s  | Short (Delivery Hygiene finding)
S30 | 1:28 - 1:36 | 8.0 s  | Short (Delivery Hygiene finding)

DAMAGE FREEZE TABLE

THE HOLE | S21: Missing. | S23 (0:20): Missing (panel work). | S24 (0:30): Missing. | S26 (0:50): Not visible. | S28 (1:10): Missing. | S30 (1:28): Missing. -> FAILED. (Note: Segment at 0:10 features a glass-paned circular window, not an open glassy hole).

THE ROLL | S21: Missing (ship is level). | S23 (0:20): Not visible. | S24 (0:30): Not visible. | S28 (1:10): Missing (level). | S30 (1:28): Missing. -> FAILED.

THE LEG  | S21: Missing (resting flat). | S23 (0:20): Not visible. | S28 (1:10): Not visible. | S30 (1:28): Missing (skid visible on left). -> FAILED.

THE GROOVE | S21: Missing. | S30 (1:28): Missing. -> FAILED.

THE MAST | Born S24 (0:30). | S26 (0:50, ground shot): Not visible. | S28 (1:10, two sitting): Missing from background. -> FAILED.

PASSPORTS AS SEEN

The woman: Dark brown hair worn in a tight bun. Suit is dark grey-blue with orange accents. Face has light skin, but her scar is positioned on her RIGHT eyebrow/forehead, not her left. She wears fully sealed gloves at all times.

The man: Very short dark hair, dark stubble. Broad build, taller than the woman. Suit is dark grey-blue with green/teal accents. No prominent shiny 2 cm burn scar is visible on his right cheekbone.

The ship: Boxy, rusty orange/brown, heavily weathered with paneled sections. It lacks the required 4-degree tilt and rests flat on its belly rather than on a collapsed leg. It features a glowing yellow doorway rather than a dark open hatch.

The ground: Dark grey, cracked dust and small rocks. A distinct swelling is visible and interacted with in segment 0:10-1:10.

The light: A prominent, pale moon positioned in the upper left of the sky in nearly every wide shot. Helmet lamps emit hard white light. The ship emits an amber glow from its open doorway and various external panels.

SCORES

DAMAGE FREEZE - 1 (None of the four permanent damage marks are present or maintained; the hole is a glass window, the ship is level, no leg is collapsed, no groove exists.)

IDENTITY CONTINUITY - 5 (Faces remain relatively stable, but the woman's scar is baked onto the wrong side [right instead of left], and the man's scar is absent.)

COSTUME & EQUIPMENT - 2 (The bare skin rule is entirely ignored; gloves never come off. The arm panel displays forbidden waveform graphics. The mast is heavily lit, not skeletal.)

FIGURE COUNT & CLONE CONTROL - 1 (Massive failure due to file misordering causing incorrect figure counts in 5 of 10 slots, plus the fatal spawn of a third white figure in S30.)

CAMERA DISCIPLINE - 8 (Movements are generally stable, constant-rate, and avoid internal cuts, though S21 lacks the specified push-in.)

PHYSICS & MATERIALS - 6 (Dust and ground interactions look solid, but the flattened ground occurs in the wrong scene due to misordering.)

NIGHT & LIGHT DISCIPLINE - 7 (Moon position is disciplined [upper left], night holds, but the ship hatch emits an unauthorized bright yellow glow.)

GROUND & SILHOUETTE DISCIPLINE - 1 (The single tremor is entirely missing from the reel. The horizon silhouette is a cylindrical rocket, not a twin boxy ship.)

PHASE CHAIN - 2 (The narrative chain is shattered by misfiled clips. The mast disappears after being raised, and footprint trails do not accumulate.)

DELIVERY HYGIENE - 4 (Multiple scenes misfiled and out of order. S29 and S30 are short [8s]. S25 contains forbidden readable text/waveform UI.)
MEAN: 3.7

TOP 5 CRITICAL

0:10 (Mapped S22) - RED (Blocker) - The Bare Skin Rule is completely failed. Gloves are never removed in the entire reel. This destroys the setup for the film's ending.

1:34 (Mapped S30) - RED (Blocker) - A third figure (the tall sealed white figure) spawns on the right side of the frame in the distance. The locked spec expressly forbids this figure from appearing in this phase.

0:00 (Mapped S21) - RED (Blocker) - The ship's damage state is ignored. The ship rests level on its belly without a collapsed leg, no 4-degree roll, no drag groove, and the hatch is glowing yellow instead of an empty dark mouth.

1:24 (Mapped S29) - RED (Blocker) - The silhouette on the horizon is a detailed cylindrical rocket with a nosecone, not the matte bone-grey twin of their boxy cargo ship.

0:45 (Mapped S25) - RED (Blocker) - The forearm panel clearly displays a readable audio waveform and digital text/UI. All readable text/graphics are forbidden.

SCENE-BY-SCENE FINDINGS

S21 (0:00-0:10)
Verified: 2 figures, night plain, moon upper left.

0:00 | RED | Ship is fully visible and small, collapsing the scale rule (must be a towering wall past both edges).

0:00 | RED | Hatch is not dark and empty; it emits a bright yellow glow and appears to have a door pane.

0:00 | RED | Both figures are walking at 0s, not standing still.

0:00 | RED | Damage freeze failed (no roll, no collapsed leg, no groove).

S22 (0:10-0:20)
Verified: Nothing matches the S22 spec.

0:10 | RED | Segment content contradicts mapped row (shows 2 figures, man touching ship). Audited as mapped.

0:10 | RED | 2 figures present instead of 1.

0:10 | RED | The bare skin rule is failed. Gloves are on for the entire duration.

0:10 | RED | No macro close-up on hands; shot is a medium wide of both figures.

S23 (0:20-0:30)
Verified: Nothing matches the S23 spec.

0:20 | RED | Segment content contradicts mapped row (shows 1 figure working on panel). Audited as mapped.

0:20 | RED | 1 figure present instead of 2.

0:20 | RED | The man is missing, and the specified speech/nod beat does not occur.

0:20 | RED | The 1.2m circular hole is missing.

S24 (0:30-0:40)
Verified: 1 figure (woman), upward unfolding of a mast structure.

0:34 | YELLOW | The mast is not a dark spare skeletal column; it features large glowing rectangular slots.

0:37 | YELLOW | The second amber point waking beat is missing.

S25 (0:40-0:50)
Verified: 1 figure (woman), tight close-up, hand raised to chest at 0:47.

0:40 | RED | The woman's scar is on her RIGHT eyebrow, not the left.

0:43 | YELLOW | She speaks with wide mouth amplitude, not small and bowed.

0:45 | RED | The arm panel displays an active audio waveform graphic and UI dots, violating the TEXT rule.

0:47 | YELLOW | She presses her RIGHT hand to her chest, not her left.

S26 (0:50-1:00)
Verified: Nothing matches the S26 spec.

0:50 | RED | Segment content contradicts mapped row (shows ground macro). Audited as mapped.

0:50 | RED | 0 figures present instead of 2.

0:50 | RED | Helmet lamps/lighting is bright on the ground; this is not the darkest frame.

S27 (1:00-1:10)
Verified: Nothing matches the S27 spec.

1:00 | RED | Segment content contradicts mapped row (shows boot crushing ground). Audited as mapped.

1:00 | RED | 1 partial figure present instead of 0 figures.

1:04 | RED | The required single tremor of dust is missing; the scene shows a boot step instead.

S28 (1:10-1:20)
Verified: Nothing matches the S28 spec.

1:10 | RED | Segment content contradicts mapped row (shows 2 figures sitting). Audited as mapped.

1:10 | RED | 2 figures present instead of 1 partial figure (boot).

1:10 | RED | No ground swelling or flattening occurs.

S29 (1:20-1:28)
Verified: 1 figure (woman), upward tilt from boots, moon upper left.

1:20 | YELLOW | Short clip duration (8.0s instead of 10.0s).

1:24 | RED | The silhouette on the horizon is a cylindrical rocket, not a twin boxy cargo ship.

1:26 | YELLOW | The woman's suit has an incorrect orange accent stripe on the lower back/legs.

S30 (1:28-1:36)
Verified: 2 figures, walking away from camera.

1:28 | YELLOW | Short clip duration (8.0s instead of 10.0s).

1:28 | RED | Damage freeze failed (no 4-degree tilt, skid visible instead of collapsed right leg).

1:34 | RED | A third figure (tall sealed white figure) appears in the distant right background.

PHASE CHAIN
Severely broken. The file misordering (S22/S23 swapped, S26/S27/S28 swapped) shatters the timeline of events. The ship's damage state is ignored globally. The mast, raised in S24, does not persist in the background of the scene showing the two sitting figures (1:10). The environment fails to accumulate boot prints. The night lighting is the only element that holds continuously.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Fixable in the edit:

Misfiled segments (0:10-0:30 and 0:50-1:20) can be reordered on the timeline to match their intended slots, which would resolve the gross content mismatches.

Requires Regeneration (all scenes due to hard bakes):

S21: Hatch is glowing yellow; ship scale is too small; damage state missing.

S22 (Content at 0:20): Bare skin rule completely failed (gloves never come off).

S23 (Content at 0:10): Hole is rendered as a glass window.

S25: Waveform text/UI on panel; scar on wrong side of face.

S27 (Content at 0:50): Single tremor beat is missing.

S29: Silhouette is a rocket instead of a boxy twin ship.

S30: Third white figure spawned in the background.

FLAGS FOR DOCUMENT CHECK

Is there an automated file naming pipeline issue? Clips 2/3 and 6/7/8 were plainly generated correctly for their respective prompts but assembled/uploaded in the wrong order.

The woman's scar is consistently rendering on the right eyebrow instead of the left. Has her character Lora/seed been trained with a mirrored image?

WHAT WORKED

0:30 - The upward unfolding motion of the mast is mechanically smooth and distinct.

0:40 - The push-in and lighting on the woman's face during the dialogue scene are highly cinematic and steady.

1:00 - The physical interaction of the boot crushing the ground swelling reads perfectly with appropriate weight and dust displacement.
