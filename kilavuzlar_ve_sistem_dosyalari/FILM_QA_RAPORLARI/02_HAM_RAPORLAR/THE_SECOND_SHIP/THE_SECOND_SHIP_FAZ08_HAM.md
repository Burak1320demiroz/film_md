# THE SECOND SHIP — FAZ 8 / TIRMANIŞ · HAM QA ÇIKTISI (1. KOŞU)

> Koşu: 12.08.2026 · Rubrik: `../../../yatay_10_20_dk_filmler/THE_SECOND_SHIP/FAZ_08_TIRMANIS/FAZ_08_QA_PROMPT.md`
> Model: Gemini · Girdi: 1 birleşik reel (~100 s) — **MODE R** (protokol: 10 ayrı klip / MODE T)
> İşlenmiş hâli: `../../../yatay_10_20_dk_filmler/THE_SECOND_SHIP/FAZ_08_TIRMANIS/FAZ_08_QA_DERSLER.md`
>
> ⛔ Bu dosya modelin ham çıktısıdır — DÜZENLENMEZ. Yorum, düzeltme ve
> içerik-çapalı yeniden eşleme ders dosyasında yapılır.

---

PROTOCOL DEVIATION - phase 8 QA is specified to run on ten separate named clips; a merged reel was delivered. Mapping confidence is reduced.

MAPPING COLLAPSE - 6 of 10 segments contradict their mapped rows.

MATERIAL
Mode selected: MODE R
File count: 1
Measured duration: 100 s
Material Gate: Passed (with protocol deviation).
Segment Map: MEASURED

SEGMENT MAP

Scene    Start    End    Length    Observed Light State    10.0 s (+/- 0.3)
S71    0:00    0:10    10.0 s    Exterior Day    Yes
S72    0:10    0:20    10.0 s    Exterior Day    Yes
S73    0:20    0:30    10.0 s    Exterior Day    Yes (Shows S74 content)
S74    0:30    0:40    10.0 s    Exterior Day    Yes (Shows S75 content)
S75    0:40    0:50    10.0 s    Exterior Day    Yes (Shows S73 content)
S76    0:50    1:00    10.0 s    Amber Cockpit    Yes
S77    1:00    1:10    10.0 s    White Tower    Yes
S78    1:10    1:20    10.0 s    White Tower    Yes (Shows S79 content)
S79    1:20    1:30    10.0 s    White Tower    Yes (Shows S80 content)
S80    1:30    1:40    10.0 s    Exterior Day    Yes (Shows S78 content)

SEAL & SKIN LEDGER

Scene    Helmet    Collar Ring    Left Glove    Right Glove    Wrist Ring    Bare Skin
S71    ON    CLOSED    ON    ON    CLOSED    NO
S72    ON    CLOSED    ON    ON    CLOSED    NO
S73    ON    CLOSED    ON    ON    CLOSED    NO (Shows S74 content)
S74    ON    CLOSED    ON    ON    CLOSED    NO (Shows S75 content)
S75    ON    CLOSED    ON    ON    CLOSED    NO (Shows S73 content)
S76    ON    CLOSED    ON    ON    CLOSED    NO
S77    ON    CLOSED    ON    ON    CLOSED    NO
S78    ON    CLOSED    ON    ON    CLOSED    NO (Shows S79 content)
S79    N/A    N/A    OFF    OFF (at ~4s)    OPEN (at ~2s)    YES - Left hand bare from 0s; Right hand bare from ~4s (Shows S80 content)
S80    N/A    N/A    N/A    N/A    N/A    NO (Shows S78 content)

COPY-MATERIAL LEDGER

Scene    Tone / Single-Toned    Markings / Paint    Glow / Shimmer    Movement / Growth
S72    Matte bone-grey, single-toned    None    None    None
S73    Matte bone-grey, single-toned    None    None    None (Segment shows S74 crust)
S74    Matte bone-grey, single-toned    None    None    None (Segment shows S73 component)
S76    Matte bone-grey, single-toned    None    None    None

STATIC WORLD LEDGER

Scene    Autonomous Movement (Ground, Crust, Wall, Dust)    Specifics
S71    NO    Dust is static.
S72    NO    Dust falls normally, no hovering.
S73    NO    (Shows S74) Crust does NOT respond to touch at 8s.
S74    NO    (Shows S75) Background is static.
S75    NO    (Shows S73) Dust and chips fall naturally.
S76    NO    Surfaces are static.
S77    NO    Floor and walls static.
S78    NO    (Shows S79) Walls are static.
S79    YES    (Shows S80) The fallen glove lands and stops completely; it fails to bounce once.
S80    NO    (Shows S78) Tower is static.

SPEECH LEDGER

Scene    Lip Movement / Open Mouth    Details
S71    NO    Mouths closed.
S72    NO    No speech.
S73    NO    (Shows S74) No speech.
S74    YES    (Shows S75) Man speaks at ~4s. Mouth line reads clearly.
S75    NO    (Shows S73) No speech.
S76    NO    No speech.
S77    NO    No speech.
S78    NO    (Shows S79) Mouth closed.
S79    NO    (Shows S80) No face in frame.
S80    NO    (Shows S78) No person in frame.

SEALED FIGURE CHECK (S77)

Height: 2.10 m, clearly taller than the woman.

Back: Flat and bare.

Shell: Flawless, dustless pearl-white.

Glove digit count: 5 digits counted on the visible right glove.

Arm length: Long.

Visor plate: Filled flush, darkest value in frame, imaging nothing.

Motion continuity: One slow continuous head tip.

TEXT LEDGER

Scene    Readable Text / Characters    Details
S71    NO    None.
S72    NO    None.
S73    NO    (Shows S74) None.
S74    NO    (Shows S75) None.
S75    NO    (Shows S73) None.
S76    YES    Readable numerals ("60", "3w") visible on the left console screen at ~8s.
S77    NO    None.
S78    NO    (Shows S79) None on chest indicators.
S79    NO    (Shows S80) None.
S80    NO    (Shows S78) None.

LIGHT LEDGER

Scene    Light State    Visible Source / Emitter    Directional Shadow    Two States Mixed
S71    Ext Day (4400K)    None    Soft-edged shadows present    NO
S72    Ext Day (4400K)    None    Soft-edged shadows present    NO
S73    Ext Day (4400K)    None (Shows S74)    Soft-edged shadows present    NO
S74    Ext Day (4400K)    None (Shows S75)    Soft-edged shadows present    NO
S75    Ext Day (4400K)    None (Shows S73)    Soft-edged shadows present    NO
S76    Amber Cockpit (2800K)    Indicator segments    None    NO
S77    White Tower (5600K)    None    Almost absent    NO
S78    White Tower (5600K)    Chest indicators (Shows S79)    Almost absent    NO
S79    White Tower (5600K)    None (Shows S80)    Almost absent    NO
S80    Ext Day (4400K)    None (Shows S78)    Soft-edged shadows present    NO

PASSPORTS AS SEEN

The Woman: Dark brown hair in low bun. Dark grey-blue suit with orange panels. Her scar is located on her RIGHT cheek (not in her left eyebrow).

The Man: Athletic, short black hair and stubble. Dark grey-blue suit with teal green panels. Burn scar located on his RIGHT cheekbone.

The Sealed Figure: Tall, white seamless shell, flush dark visor plate, 5 digits on the right glove.

The Stone/Crust/Component: Matte bone-grey, single-toned, crisply formed with no markings or paint.

The Ship: Grounded, holed, swallowed by crust above landing gear. Sits flat (no clear 4-degree tilt).

The Ground/Walls: Basalt plain outside; smooth, seamless, featureless white walls inside the tower.

The Light: 4400K orange daylight exterior; 2800K warm amber cockpit interior; flat sourceless 5600K white tower interior.

SCORES

SEAL & SKIN DISCIPLINE: 0 (The left hand in the mapped S79 clip is completely bare - phase blocker)

BONE-GREY COPY DISCIPLINE: 10 (Stone is single-toned, matte, and free of paint across all copies)

STATIC WORLD: 9 (Crust and ground remain perfectly static; deduction for the fallen glove failing to bounce once)

EVENT DELIVERY: UNVERIFIABLE

IDENTITY CONTINUITY & SCAR ANCHORING: UNVERIFIABLE

COSTUME, EQUIPMENT & FIGURE COUNT: UNVERIFIABLE

THE SEALED FIGURE (S77): 2 (Five digits rendered on the sealed glove - critical failure)

CAMERA DISCIPLINE: UNVERIFIABLE

LIGHT, BLANK SURFACE & TEXT DISCIPLINE: 2 (Readable text on the S76 console breaks the absolute text ban)

PHASE CHAIN & DELIVERY HYGIENE: UNVERIFIABLE

MEAN SCORE: NO SCORE - mapping collapsed, this is not a baseline run.

TOP 5 CRITICAL

0:20-1:40 (Across phase) - RED - Mapping Collapse: Six of the ten segments contradict their mapped rows. Makes event delivery and continuity unverifiable.

1:21 (Segment 9, showing S80) - RED - Left Hand Bare: The hand turning the wrist ring has no glove and bare skin is visible. Violates the One-Seal Law.

1:08 (Segment 7, S77) - RED - Sealed Figure Digits: The sealed figure has 5 digits on its right glove instead of 4.

0:58 (Segment 6, S76) - RED - Text on Console: Readable numerals appear on the left screen inside the cockpit.

0:34 (Segment 4, showing S75) - RED - Early Speech: The man begins speaking at ~4s instead of waiting for the ~9s window.

SCENE-BY-SCENE FINDINGS

S71: Verified: Two figures, orange and teal separation. Deviations: The camera pans to follow the figures instead of remaining locked off (RED). The woman's scar is on her right cheek instead of her left brow (RED).

S72: Verified: Lateral track left, stone field on horizon. Deviations: The woman (orange figure) is entirely absent from the start of the shot (RED).

S73: The segment showing the ship (mapped S73) contradicts its row (RED). Audited against S73: Complete content mismatch.

S74: The segment showing the radio (mapped S74) contradicts its row (RED). Audited against S74: Complete content mismatch.

S75: The segment showing the grey twin (mapped S75) contradicts its row (RED). Audited against S75: Complete content mismatch.

S76: Verified: Seating the component, amber lights illuminating, stone is purely grey. Deviations: Readable text visible on the left-hand panel (RED).

S77: Verified: White room, figure heights, plate untouched. Deviations: 5 digits on the tall figure's glove (RED).

S78: The segment showing the count (mapped S78) contradicts its row (RED). Audited against S78: Complete content mismatch.

S79: The segment showing the falling glove (mapped S79) contradicts its row (RED). Audited against S79: Complete content mismatch. Content deviation: Left hand is bare (RED). Glove hits the floor and stops without a bounce (YELLOW).

S80: The segment showing the sky (mapped S80) contradicts its row (RED). Audited against S80: Complete content mismatch. Content deviation: A second object appears trailing behind the first object in the sky at 1:36 (RED).

PHASE CHAIN
UNVERIFIABLE due to Mapping Collapse.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION

Edit:

S74 (showing S75): Crop or trim the beginning to remove the early lip movement, though it will break the 10-second duration constraint.

Regeneration:

The entire reel must be regenerated to fix the Mapping Collapse (delivery of clips in the wrong order/slots).

S71: Regenerate to enforce fixed lockoff and correct scar placement.

S72: Regenerate to include the orange figure in the first 2 seconds.

S76: Regenerate to clear the text from the UI panel.

S77: Regenerate to restrict the sealed figure to 4 digits.

S79 (showing S80 content): Regenerate to cover the left hand; it must be gloved.

S80 (showing S78 content): Regenerate to remove the second sky object.

FLAGS FOR DOCUMENT CHECK

Does the prompt pipeline currently lack a negative prompt for "text, numbers, interface" for S76, given a console was heavily detailed?

Was a global "5 fingers" anatomical constraint applied that overrode the 4-digit lock for S77?

Was the file-naming script scrambled prior to rendering, resulting in the 6-slot mapping shuffle?

WHAT WORKED

The bone-grey copy material logic held beautifully across the phase (0:20-1:00); the component in the cockpit was perfectly matched and single-toned.

The crust in the ship shot (0:28) did absolutely nothing when touched, perfectly fulfilling the Static World law.

The S77 visor plate remained flush, dark, and non-reflective even in a wide frame.
