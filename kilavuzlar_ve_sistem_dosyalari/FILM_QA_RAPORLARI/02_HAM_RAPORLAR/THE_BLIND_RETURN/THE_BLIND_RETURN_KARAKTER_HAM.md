# 🧍 THE BLIND RETURN — KARAKTER_QA HAM RAPORU

> Çalıştırma: 07.08.2026 · MOD V (rubrik zaten belgesiz çalışır)
> Rubrik: `../QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). Belge cevapları
> ve düzeltmeler: `../01_FILM_RAPORLARI/THE_BLIND_RETURN.md`
> ⚠️ Operatör yapıştırmasında tablo boru çizgileri kayboldu; satır içerikleri
> aynen korunmuştur.

---

FILM: (not supplied)
RUNTIME: 02:49 · SCENES OBSERVED: 12 · CHARACTERS TRACKED: 1
BASELINE: SELF-CONSISTENCY — this review measures whether each character agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 4/10
VERDICT: DRIFTS BUT RECOVERABLE
The core facial identity holds across cuts, but equipment state (helmet) and cross-cut action suffer major breaks.

## CHARACTER PASSPORT(S)

Label:            The Astronaut
First clear view: 00:00
Face:             Olive skin, prominent cheekbones, dark eyebrows.
Hair:             Dark, pulled back.
Eyes:             Dark, visible through visor.
Build:            Average height, athletic frame.
Costume:          Grey spacesuit, dark knee/elbow accents. Symmetrical piping.
Equipment:        Clear spherical helmet, dual headlamps. Backpack. Dark canister on right thigh.
Wear map:         Clean initially.
Voice:            (Silent character)

## APPEARANCE TABLE

Character | Scene | In-out | Face visible? | State notes
The Astronaut | 1 | 00:00-00:09 | Yes | Pristine suit, thigh canister attached.
The Astronaut | 2 | 00:09-00:40 | Yes | Running sequence, profile views.
The Astronaut | 3 | 00:40-00:50 | Yes | Crouching. Helmet clear.
The Astronaut | 4 | 00:50-01:00 | Yes | Headlamps on. Approaching marker.
The Astronaut | 5 | 01:00-01:10 | Yes | Falls. Visor cracks on her right side.
The Astronaut | 6 | 01:10-01:40 | Yes | Visor cracked. Canister on thigh.
The Astronaut | 7 | 01:40-01:50 | Yes | Removes canister from thigh.
The Astronaut | 8 | 01:50-01:55 | Yes | Sprays foam onto visor crack.
The Astronaut | 9 | 01:56-02:19 | No | Helmet transforms into solid opaque shell.
The Astronaut | 10 | 02:20-02:29 | Yes | Inside airlock. Removes opaque helmet.
The Astronaut | 11 | 02:30-02:39 | No | Climbing rocket ladder.
The Astronaut | 12 | 02:40-02:49 | Yes | Stepping out. Helmet pristine and clear again.

## SCORES SUMMARY

Category | Score | Critical Issue
Facial Identity | 6/10 | Consistent when visible.
Hair, Build & Proportions | 6/10 | Stable physical frame.
Costume Identity | 4/10 | Suit details hold, but helmet changes radically.
Wear, Damage & Injury | 3/10 | Visor crack vanishes by 02:40.
Equipment State | 3/10 | Opaque helmet swap; magically repaired later.
Cross-Cut Action | 3/10 | Severe location jumps at 02:20 and 02:30.
Count & Separation | N/A | Single character.
Voice & Performance | N/A | Silent character.

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 1

## IDENTITY DRIFT MAP — per character
Character | Element | First slip (timecode) | Undeniable by | Recovered?
The Astronaut | Helmet | 01:56 | 01:56 | Yes, at 02:40 (but breaks wear continuity).

## WEAR TIMELINE — per tracked mark
Mark | Acquired | Present at | Absent at ⚠️ | One-way?
Visor Crack | 01:03 | 01:10-01:55 | 02:40 | No.

## CONTRADICTION LOG
Timecode A | Timecode B | Character | Category | What contradicts what | Severity
01:50 | 01:56 | The Astronaut | Equipment State | Clear sprayed visor becomes solid opaque shell | Major
02:18 | 02:20 | The Astronaut | Cross-Cut Action | Enters dark silo hatch, cuts to kneeling in bright white room | Major
02:28 | 02:30 | The Astronaut | Cross-Cut Action | Kneeling in airlock, cuts to climbing exterior rocket ladder | Major
01:03 | 02:40 | The Astronaut | Wear/Damage | Cracked visor is pristine again | Minor

## THE THREE THAT MATTER
1. Helmet transformation (01:56): The clear, foam-sprayed helmet becomes a featureless opaque shell. Viewers will feel the prop swap. Fix: Regenerate 01:56-02:19 shots maintaining clear visor.
2. Airlock spatial jump (02:18-02:20): Character interacts with a dark ribbed silo, immediately cuts to kneeling calmly in a pristine white interior. The spatial flow is broken. Fix: Insert transition shot or re-cut.
3. Erased damage (02:40): The cracked visor returns to a pristine state. Violates linear time. Fix: Accept it as a spare helmet, or regenerate shot with damaged prop.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding | Fix | Cost
Opaque helmet swap | Regenerate 01:56-02:19 | High
Spatial jump at airlock | Insert transition | Low
Pristine helmet at end | Regenerate 02:40 | Medium

## FLAGS FOR DOCUMENT CHECK
Observation | Question the document must answer
Helmet becomes opaque at 01:56. | Is the helmet designed to polarize/turn solid in heavy dust?
Character climbs a rocket at 02:30. | Is the shelter a silo, a rocket, or a corrugated habitat tube?

## OUT-OF-SCOPE FLAGS
World logic break: The shelter exterior changes from a silo (02:10) to a rocket (02:30) to a corrugated tube (02:40) → MANTIK_QA.
