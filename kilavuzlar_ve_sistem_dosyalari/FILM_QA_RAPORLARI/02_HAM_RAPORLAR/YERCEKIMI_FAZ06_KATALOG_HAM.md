# YERÇEKİMİ — FAZ 6 · GEÇİŞ B (KATALOG) · HAM QA RAPORU

```
KÜNYE
  Film   YERÇEKİMİ · FAZ 6 makarası · 10 parça · 100 s (beyan)
  ⛔ IZGARA 10,0 s — F4 · F5 · F6. F1-F3 = 8,0 s. → D124 · 6. vaka
  Rubrik FAZ_06_KAPSUL/FAZ_06_QA_PROMPT.md — 🅱️ PROMPT B (KATALOG)
  Motor  Gemini · ⭐ KÖR GEÇİŞTEN AYRI SOHBET · 02.09.2026 · Mod ⚠️ V
⭐⭐ EKSİK-İKİ TESTİ: denetçiye hangi iki girdinin iptal edildiği
   SÖYLENMEDİ. MISSING listesine tam olarak "I, J" yazdı ve UNMATCHED
   sıfır çıktı → DOĞRU İKİ KLİP DÜŞMÜŞ. (F2'de yanlış klip atlanmıştı.)
```
⛔ Aşağısı raporun BİREBİR kendisidir [AGENTS kural ④].

---

MATERIAL
measured total duration = 100 seconds
number of distinct shot segments = 10
measured shot length = total / segment count = 10.0 seconds
are all segments the same length within 0.3 s? yes

SEGMENT MAP
Segment 1 | 0:00-0:10 · Segment 2 | 0:10-0:20 · Segment 3 | 0:20-0:30
Segment 4 | 0:30-0:40 · Segment 5 | 0:40-0:50 · Segment 6 | 0:50-1:00
Segment 7 | 1:00-1:10 · Segment 8 | 1:10-1:20 · Segment 9 | 1:20-1:30
Segment 10 | 1:30-1:40

IDENTIFICATION TABLE
Segment 1 | 0:00-0:10 | A | High | Hand only, green dominant. Fingertip touches a black circular panel ring.
Segment 2 | 0:10-0:20 | B | High | Hands and chest only, green dominant. Bare forearms float in front of chest.
Segment 3 | 0:20-0:30 | C | High | Medium shot from behind. Screen-left window with a structure sliding past.
Segment 4 | 0:30-0:40 | D | High | Seat only (shoulder edge). Empty seat with drifting straps.
Segment 5 | 0:40-0:50 | E | High | Hand only, white dominant. Fingers turn a knurled tuning dial.
Segment 6 | 0:50-1:00 | F | High | Face only, head-on. Lit cool green from below, eyes open.
Segment 7 | 1:00-1:10 | G | High | Face only, profile. Eyes close and reopen.
Segment 8 | 1:10-1:20 | H | High | Wide shot from behind. Blue-white light pouring through a window filled with Earth.
Segment 9 | 1:20-1:30 | K | High | Hand only. Fingers turn a textured valve wheel on a panel.
Segment 10 | 1:30-1:40 | L | High | Face only, head-on. Lights physically die in sequence.

MATCHED · A, B, C, D, E, F, G, H, K, L
MISSING · I, J
UNMATCHED · None

HER FACE - OBSERVATION ONLY
Her face features an oval structure, a defined soft jawline, and straight cheekbones. Her apparent age is in her 30s. Her skin tone is light/wheat with visible pores and slight fatigue. Her nose is straight, eyes are brown, and brows are dark. Hair is dark brown, cut chin-length, and behaves flawlessly in zero gravity, lifting away from her head and holding shape without hanging. It is NOT the exact same face in every entry: in Segment 6 (0:50, F) and Segment 7 (1:00, G), the forehead is completely clean. However, in Segment 10 (1:30, L), a fresh, bright red vertical scratch is visible on her right forehead. No vertical pale scar is visible on her left temple in any segment.

THE CAPSULE - OBSERVATION ONLY
The capsule is a cylindrical/conical space, roughly 8 to 10 feet across, heavily lined with off-white padded/quilted walls. It contains large, white, high-backed seats equipped with 5-point grey harnesses. Control panels feature small circular green lights, dials, and switches. The window is a circular port with a thick metal rim. It does NOT look like the exact same capsule in all entries. In Segment 3 (0:20, C) and Segment 4 (0:30, D), a seat is positioned immediately against a screen-left window. In Segment 8 (1:10, H), the cabin layout changes drastically: the window is perfectly centered, and two identical seats are positioned on the far left and right, both facing away from the window, breaking the layout established in the other segments.

THE TWO CONFUSABLE PAIRS
F vs L: Segment 6 (0:50) is assigned to F because the green light from below holds steady at one level, and her eyes remain open. Segment 10 (1:30) is assigned to L because the green light source physically dies in sequential stages, and her eyes close for good.
A vs K: Segment 1 (0:00) is assigned to A because the object being touched is a large, flat, segmented black ring set into the console, and its segments remain dark. Segment 9 (1:20) is assigned to K because the object turned is a raised, textured valve wheel, and a segmented ring is visible on the wrist cuff.

SCORES
COVERAGE: 10 (All expected 10 segments definitively matched)
FACE CONTINUITY: 2 (Red scratch appears on right forehead in L)
SOLITUDE AND FIGURE COUNT: 10 (One person exclusively, empty seats remain empty)
COSTUME AND HANDS: 4 (Wristband teleports to right wrist in K, hand injured in E)
THE TWO RINGS AND THE WATCH: 1 (Wrist ring wrong count and wrong arm in K, watch unverifiable)
CAMERA DISCIPLINE: 8 (All locked off correctly, but push-in missing in H)
LIGHT: 3 (Hard shadows in E and K; missing amber lamp in L)
ZERO-G WITH AIR: 2 (Floating mid-air rather than seated in H; forearms do not rise in B)
STILLNESS IN H: 1 (Figure is floating rigidly in the center of the room)
THE SINGLE ACTIONS: 1 (Action mechanics fail completely in A, B, and K)
THE PLACE: 2 (Severe layout contradiction in H)
TEXT DISCIPLINE: 1 (Subtitles/characters present in A, E, F, K)
DELIVERY HYGIENE: 3 (Subtitles baked into rendering in multiple segments)
OVERALL SCORE: 3.7

TOP 5 CRITICAL
TEXT / SUBTITLES: Generative subtitles are baked onto the screen in Segment 1 (0:00, A), Segment 6 (0:50, F), and Segment 9 (1:20, K), violating the strict zero-character lock.
POSTURE / SEATING: In Segment 8 (1:10, H), the astronaut is floating rigidly cross-legged in the center of the cabin mid-air, directly violating the requirement of a seated, still figure.
ACTION FAILURE: In Segment 2 (0:10, B), the core physical action fails entirely. Her hands simply hover and twitch; she never presses them down, meaning they cannot rise on their own as specified.
CAPSULE LAYOUT: Segment 8 (1:10, H) features a totally contradictory cabin layout with a centered window and seats facing away from it.
FACE INJURY: In Segment 10 (1:30, L), a new red vertical scratch appears on her right forehead that is completely absent in prior face close-ups.

FINDINGS BY SEGMENT
Segment 1 (0:00, A): Subtitle text reads "Main propellant, empty. Orbital burn unavailable." on screen (maximum severity). The fingertip presses the center pad and taps the inner rim rather than tracing an arc along the outer edge.
Segment 2 (0:10, B): The forearms are never pressed down into the lap; they only hover and twitch, failing the required zero-g demonstration (maximum severity). The wrist ring is present on the left wrist but no action utilizes it.
Segment 3 (0:20, C): The object passing the window is a satellite/solar array moving right-to-left, rather than a turning torn blue fragment.
Segment 4 (0:30, D): No faults found. Zero-G straps drift perfectly without touching the cushion.
Segment 5 (0:40, E): Readable tiny tick marks/numbers are generated on the silver dial face (maximum severity). The right thumb webbing bears an unexplained red cut. Shadows cast by the fingers are hard-edged.
Segment 6 (0:50, F): Subtitle text reads "Contact confirmed. Please maintain trajectory." on screen (maximum severity).
Segment 7 (1:00, G): The unfastened strap fails to drift across her chest and touch her shoulder as required.
Segment 8 (1:10, H): The astronaut is floating rigidly cross-legged in mid-air rather than being seated with hands on armrests (maximum severity). The window is centered in the wall, not screen-left. The camera is completely locked off, lacking the specified 20cm push-in.
Segment 9 (1:20, K): Subtitle text reads "Oxygen 11%. Warning." on screen (maximum severity). The wrist ring is generated on the RIGHT wrist instead of the LEFT. The wrist ring displays 4 lit segments, not 2 dropping to 1. The hand does not execute a continuous quarter turn. Shadows are hard-edged.
Segment 10 (1:30, L): A fresh red vertical scratch appears on the right forehead (high severity). The sequence ends in total darkness rather than leaving one small amber lamp illuminated.

CROSS-SHOT CHECKS
1. IS SHE THE SAME PERSON? No. Segment 6 (F) and Segment 7 (G) feature a clean forehead. Segment 10 (L) features a fresh red scratch on the right forehead. The specified left temple scar is absent in all three.
2. IS SHE ALONE? Yes. One person in all available segments.
3. HEAD AND HANDS BARE? Yes, in all segments.
4. IS HER BACK FLAT in C and H? In C the back is flat/normal, though a chest pack with ports is visible on the front. In H the back is flat.
5. THE TWO RINGS: In A, the large panel ring is perfectly dark. In K, the small wrist ring is on the wrong (right) wrist and has FOUR segments lit instead of two dropping to one.
6. THE WATCH: UNVERIFIABLE. Due to the intentional absence of entries I and J, the stopped watch does not appear in this reel.
7. THE LIGHT, ENTRY BY ENTRY: A white/green, white dominant; B flat white; C white; D white pools; E white; F white/green; G white; H blue-white from window; K white; L green before dropping to zero. Amber is missing from L. Nothing flashes.
8. HARD SHADOWS / BEAMS: Hard-edged shadows are present in E around the dial and K around the valve.
9. ZERO-G BEHAVIOR: Hair holds perfectly in C, F, G, L. Straps drift beautifully in D. EXCEPTIONS: In B, forearms hover but do not push down and rise. In H, the astronaut sits cross-legged rigidly floating in mid-air, violating the seated requirement.
10. EARTH-BOUND BODY LANGUAGE: None found.
11. THE WINDOW: In C it is screen-left showing a moving satellite. In G it is background-left showing static stars. In H it is centered showing the Earth. The layout in H is incorrect.
12. TEXT: A subtitle; E tick marks on dial; F subtitle; K subtitle.
13. SPEECH: Lips remain firmly closed in all face segments.
14. CAMERA: Locked off in all segments. H is incorrectly locked off, lacking its specified push-in.
15. THE TWO CONFUSABLE PAIRS: F assigned to Segment 6 because eyes stay open; L to Segment 10 because the light dies. A assigned to Segment 1 because it's a flat console pad; K to Segment 9 because it features a raised valve and wrist ring.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
FIXABLE: C and G are structurally sound, though missing the exact debris/strap interactions, they can likely be used as-is. D is perfect.
REQUIRES REGENERATION: A, F and K must be regenerated to remove baked-in subtitles. B must be regenerated to capture the mechanical action of pushing the arms down. H must be completely regenerated to seat the astronaut and fix the capsule layout. E must be regenerated to remove dial text and hand injury. L must be regenerated to fix the face scratch and add the amber lamp.

FLAGS FOR DOCUMENT CHECK
The reference manual calls for a left temple scar; the generation tools seem to be missing this entirely across all face close-ups. Check the facial model LoRA weight.
Subtitle generation tools appear to have been left active in the pipeline for shots A, F, and K.

WHAT WORKED
The zero-gravity hair simulation in F (0:50) and L (1:30) lifts and holds in a highly convincing manner. The floating harness straps in D (0:30) effectively communicate weightlessness without resting on the cushion. The three-stage physical light death in L (1:30) is dramatically effective and strictly respects the one-way progression.
