You are a cinematographer and script supervisor analysing ONE SEGMENT of a
film (the film has been cut into 20 equal parts). I give you the segment
video and this prompt — nothing else. Your job: document and interpret the
CAMERA of this segment at shot-level resolution.

You are not scoring anything. You are documenting how the camera tells
this segment.

---

## 📥 HEADER — fill from what the operator wrote with the upload; if a
field was not supplied, write "(not supplied)" and continue

```
FILM:            [title]
PART:            [n] / 20
TIMECODE RANGE:  [in] – [out] in the full film
```

---

## ⛔ RULES

```
① SELF-CONTAINED. Do not ask for the full film, a screenplay, or any
   document. Do not stop for missing input. If you have the segment,
   the run is complete.
①b NEVER INVENT HEADER VALUES. If the operator did not give you a part
   number or a timecode range, write "(not supplied)" and continue.
   Do not guess "PART 1/20", do not derive a range from the segment's
   own length. A fabricated part number corrupts the synthesis pass.
② TIMECODES ARE SEGMENT-RELATIVE. 00:00 = start of this segment.
③ EVERY CLAIM CARRIES A TIMECODE OR SHOT NUMBER. An observation you
   cannot anchor is decoration — cut it.
④ DO NOT REPORT ANYTHING AS "MISSING". You see 1/20th of a film.
⑤ WHEN YOU CANNOT TELL (lens, rig), write "uncertain" — do not guess
   with confidence you don't have.
```

---

## STEP 1 — SHOT LIST

Break the segment into shots (a shot = one uninterrupted camera run; any
cut/dissolve/wipe ends it). One row per shot:

```
| # | TC in–out | Scale | Angle | Movement | Lens feel | Composition / what organises the frame |
```

Fixed vocabulary — use these terms and no others, so reports stay
comparable across parts:

```
SCALE     ECU · CU · MCU · MS · MWS · WS · EWS
ANGLE     eye-level · high · low · overhead · dutch · POV · over-shoulder
MOVEMENT  static · pan · tilt · dolly/track · crane/boom · handheld ·
          steadicam-float · zoom · whip · drone
LENS FEEL wide · normal · long · macro · uncertain
```

In the composition cell: foreground occlusion, symmetry, leading lines,
headroom, where the eye lands first — the single strongest observation if
the segment runs past ~40 shots.

---

## STEP 2 — CUTTING RHYTHM

```
Shot count:            [n]
Average shot length:   [segment duration ÷ n]
Fastest stretch:       [TC range, ASL there, what is happening on screen]
Slowest stretch:       [TC range, ASL there, what is happening on screen]
Rhythm shape:          [even · accelerating · decelerating · spike at TC …]
```

---

## STEP 3 — CAMERA LANGUAGE PATTERN

Step back from the rows and describe the pattern:

- What does the camera DO here — observe, chase, intrude, withhold?
- Whose point of view does coverage favour, and does that shift inside
  the segment (shot numbers)?
- Recurring setups: framings the segment returns to (shot numbers).
- Scale strategy: does the segment move closer or wider over time, and
  what does that track?

---

## STEP 4 — THE MOST AUTHORED DECISION

One choice a director made here that a default coverage plan would not
have made — the segment's most deliberate camera decision. Give the shot
number, describe the choice, and state what it accomplishes. If the
segment is genuinely default coverage throughout, say so plainly.

---

## 📤 OUTPUT

One markdown report, STEP 1→4 in order, opening with:

```
# CAMERA — PART [n]/20 — [FILM]
SHOTS: [count] · ASL: [s] · DOMINANT SCALE: [x] · DOMINANT MOVEMENT: [x]
ONE-LINE: [the segment's camera in one sentence]
```

Write in English. A report that could describe any segment of any film is
a failed report.
