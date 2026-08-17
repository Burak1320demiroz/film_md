# THE KALEIDA CRASH — MANTIK VE DEVAMLILIK QA · HAM RAPOR

```
QA TARİHİ:     31 Temmuz 2026
QA MODELİ:     Gemini (video analiz)
QA PROMPTU:    QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md
GİRDİ:         tam kurgu · 02:05 · yalnızca video (rubrik gereği doküman yok)
SPEC BLOĞU:    YOK — bu rubrik SPEC istemez, taban çizgisini videodan kurar
BASELINE:      SELF-CONSISTENCY
```

> ⚠️ Değiştirilmedi, düzeltilmedi, kısaltılmadı. Doğrulama ve plan
> karşılaştırması `../01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md` içindedir.

---

FILM: The Kaleida Crash
RUNTIME: 02:05 · SCENES OBSERVED: 12
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees
          with itself, not whether it matches its design.

OVERALL SCORE: 4.0/10
VERDICT: FIXABLE IN EDIT

## SCENE INVENTORY
| # | In-out | Location | Present | What happens | Dialogue |
|---|---|---|---|---|---|
| S1 | 0:00–0:09 | Impact Crater | Protagonist | Pod crashes in crystal field; door opens | None |
| S2 | 0:10–0:19 | Impact Crater | Protagonist | Crawls out, touches glowing ground, kneels | None |
| S3 | 0:20–0:29 | Archway Plain | Protagonist | Walks through crystal arch, checks wrist, steps glow | None |
| S4 | 0:30–0:39 | Crystal Forest | Protagonist | Walks through crystal woods; lightning cracks crystal | None |
| S5 | 0:40–0:49 | Prism Hall | Protagonist | Walks down crystal corridor, checks wrist device | None |
| S6 | 0:50–0:59 | Crystal Glade | Protagonist, Crystal Cat | Encounters translucent feline beast in clearing | None |
| S7 | 1:00–1:09 | Mirror Stream | Protagonist | Crosses water stepping stones; touches wall | None |
| S8 | 1:10–1:19 | Crystal Chasm | Protagonist | Leaps across gorge, lands on knees, checks ground | None |
| S9 | 1:20–1:29 | Wreckage Field | Protagonist (x2) | Approaches crashed ship; duplicate protagonist appears | None |
| S10 | 1:30–1:39 | Ship Exterior | Protagonist | Climbs burning metal hull of crashed ship | None |
| S11 | 1:40–1:49 | Transmitting Deck | Protagonist | Activates beacon panel; light beam shoots to sky | None |
| S12 | 1:50–2:05 | Hull Crest | Protagonist | Sits on wreckage looking out at twin suns sunset | None |

---

### THE CHARACTER — as first clearly seen
*   **Face:** Female, dark hair tied in a high bun, clean skin with slight smudges, dark eyes.
*   **Suit:** Dark grey/black tactical flight suit with orange piping, shoulder guards, collar ring. Left shoulder strap has a tear exposing grey under-layer.
*   **Wear/dirt:** Smudges on suit knees and elbows; tear on left shoulder visible from S2 onward.
*   **Equipment:** Clear hemispherical bubble helmet with neck seal. Wrist unit on left forearm with glowing interface.
*   **First scene this is fully visible:** S1 (0:08) / S2 (0:10).

---

### THE WORLD — as the film shows it
*   **Gravity read:** Earth-standard to slightly floaty (long air-time during leap at 1:12).
*   **Atmosphere read:** Hazy, dust particles hang and drift in light beams; smoke rises vertically from fires.
*   **Light source:** Variable between scenes — direct golden sunlight, overcast cool ambient, and dark night/dusk.
*   **Locations:**
    *   *Impact Crater:* Open plain littered with giant clear quartz-like crystals and crash debris.
    *   *Archway Plain:* Desert-like terrain framed by a natural crystal arch, smoke column in background.
    *   *Crystal Forest:* Dense woodland intermingled with tall vertical crystal pillars.
    *   *Prism Hall:* Tunnel-like formation of giant angled crystals with reflective floor.
    *   *Crystal Glade:* Sunlit earth glade surrounded by crystal trees.
    *   *Mirror Stream:* Shallow water corridor lined with crystal columns and floating ice/stone slabs.
    *   *Crystal Chasm:* Deep rocky canyon surrounded by pine forest and crystal spikes.
    *   *Wreckage Field:* Dark plain dominated by a massive crashed freighter hull emitting electrical arcs.
    *   *Transmitting Deck / Hull Crest:* Metal top exterior of the crashed vessel.

---

### THE COUNTER — does the film track a changing quantity?
*   **TRACKED ITEM:** Purple Energy Footprint Trail (appears wherever the character walks or touches ground).
*   **Observed values:**
    *   S2 (0:12): Ground glows purple on hand contact.
    *   S3 (0:27): Footprints leave glowing purple marks behind her.
    *   S5 (0:41): Footprints continue leaving purple trail.
    *   S7 (1:02): Footprints glow purple on water stepping stones.
    *   S8 (1:19): Hand contact creates glowing purple starburst pattern.
    *   S9 (1:25): Footprints glow purple on approach to ship.
*   **Behavior:** Consistent visual logic across scenes.

---

### NUMBERS SPOKEN OR SHOWN
*   *None observed in audio or environment.*

---

### OBJECTS THAT GET ATTENTION
*   **Wrist Device:** First seen S2 (0:17), used S3 (0:24), S5 (0:46), S11 (1:41).
*   **Beacon Transmitter:** First seen S10 (1:38), activated S11 (1:45).

---

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|:---:|---|
| Physical Consistency | 6/10 | Jump flight time at 1:12 exceeds ground gravity rules shown earlier |
| Counter Logic | 8/10 | Purple step-tracking remains visually coherent throughout |
| Spatial Geography | 4/10 | Rapid terrain shifting from crystal plains to pine forest to dark wreckage |
| Time & Light Logic | 3/10 | Chaotic day/night/dusk jumps between adjacent walking steps |
| State, Costume & Props | 2/10 | Helmet repeatedly disappears and reappears on bare head in vacuum/alien air |
| Causality & Knowledge | 2/10 | Duplicate protagonist clone appears at 1:26 walking alongside original |
| Quantity Consistency | 8/10 | Character count is 1 throughout except the glitch at 1:26 |
| Setup & Abandonment | 6/10 | Crystal beast introduced at 0:50 is immediately abandoned |

---

## SEVERITY TALLY
🔴 **BLOCKER:** 2 | 🟠 **MAJOR:** 4 | 🟡 **MINOR:** 3

---

## COUNTER CURVE
`S2 (Hand touch active) → S3 (Steps active) → S5 (Steps active) → S7 (Steps active) → S8 (Hand touch active) → S9 (Steps active)` — *Counter operates consistently.*

---

## LOCATION MAP

| Location | Scenes | Consistent? | Mismatch |
|---|---|:---:|---|
| Impact Crater | S1, S2 | Yes | Environment holds spatial context between pod exit and standing. |
| Archway Plain | S3 | No | Smoke column direction shifts between wide shot and medium step. |
| Crystal Forest | S4 | No | Background transforms from desert plain to dense evergreen woodland. |
| Prism Hall | S5 | Yes | Enclosed crystal corridor geometry remains consistent within scene. |
| Crystal Glade | S6 | No | Lighting shifts from cool internal corridor to warm direct sun. |
| Mirror Stream | S7 | No | Terrain shifts to shallow water channel not visible from Glade. |
| Crystal Chasm | S8 | No | Earth pine tree forest appears on chasm edge; absent in previous scenes. |
| Wreckage Field | S9, S10, S11, S12 | No | Lighting flips to pitch dark night (S9-S11) then twin suns sunset (S12). |

---

## DRIFT MAP — where the film starts losing itself

| Element | First slip (timecode) | Undeniable by | Recovered? |
|---|---|---|---|
| Helmet Continuity | 0:20 (Helmet disappears) | 0:30 (Helmet reappears) | No (oscillates continuously) |
| Environment / Sky Lighting | 0:30 (Dark forest) | 1:20 (Night wreckage) | No (jumps to sunset at 1:50) |
| Character Integrity | 1:25 (Clone spawns) | 1:27 (Two characters walking) | Yes (returns to 1 character at 1:30) |

---

## CONTRADICTION LOG

| Timecode A | Timecode B | Category | What contradicts what | Severity |
|---|---|---|---|---|
| 0:15 | 0:22 | State, Costume & Props | Helmet is fully sealed around head at 0:15; at 0:22 character is walking in open air with bare head and no helmet present, with no suit removal shown. | 🔴 BLOCKER |
| 0:22 | 0:32 | State, Costume & Props | Character has bare head with no helmet at 0:22; sealed glass bubble helmet reappears on head at 0:32. | 🔴 BLOCKER |
| 0:52 | 1:02 | State, Costume & Props | Helmet is sealed on head during creature encounter at 0:52; helmet vanishes and head is bare while crossing stream at 1:02. | 🟠 MAJOR |
| 1:02 | 1:12 | State, Costume & Props | Bare head during stream walk at 1:02; full glass bubble helmet reappears during chasm leap at 1:12. | 🟠 MAJOR |
| 1:15 | 1:22 | Time & Light Logic | Environment at 1:15 is bright daylight in pine canyon; environment at 1:22 is pitch-black night illuminated by electrical sparks. | 🟠 MAJOR |
| 1:24 | 1:26 | Causality & Knowledge | Single protagonist stands looking at ship at 1:24; at 1:26 a duplicate second protagonist enters frame walking identically alongside her. | 🔴 BLOCKER |
| 1:44 | 1:52 | Time & Light Logic | Sky is pitch-black night during beacon launch at 1:44; sky instantly transforms to bright twin-sun dusk sunset at 1:52 on same hull location. | 🟠 MAJOR |
| 0:10 | 1:12 | Physical Consistency | Character moves with heavy grounded weight while crawling at 0:10; character floats across a 30-foot chasm with extended airtime at 1:12. | 🟡 MINOR |
| 0:28 | 1:28 | State, Costume & Props | Suit fabric tear on left shoulder is present at 0:28, vanishes/repairs on climbing suit at 1:28, and reappears torn at 1:52. | 🟡 MINOR |

---

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
|---|---|:---:|---|
| Crystal Cat Creature | 0:50 | No | Creature appears, stares at character, walks past, and never impacts plot again. |
| Wrist Device Ping | 0:24 | Yes | Activated twice in field, used finally to activate ship beacon. |
| Purple Footprint Trail | 0:27 | Yes | Persists throughout walking beats across all terrain types. |

---

## THE THREE THAT MATTER

1.  **Oscillating Helmet State (0:15 vs 0:22 / 0:22 vs 0:32 / 1:02 vs 1:12):** The character alternates between wearing a sealed space helmet and walking with an uncovered bare head every 10–15 seconds without taking it off on screen.
    *   *Viewer Impact:* Completely destroys environmental believability and rules of the alien atmosphere.
    *   *Cheapest Fix:* Edit out shots where head is bare (S3: 0:20–0:29, S7: 1:00–1:09) or crop framing to hide the head area.
2.  **Duplicate Protagonist Clone Glitch (1:24 vs 1:26):** Two identical versions of the main character appear walking side-by-side toward the ship wreckage.
    *   *Viewer Impact:* Instantly breaks narrative immersion; reads as an AI visual error rather than a narrative event.
    *   *Cheapest Fix:* Trim timestamp 1:25–1:28 out of the sequence and cut directly from wide arrival (1:23) to hull climb (1:30).
3.  **Erratic Day-to-Night Time Jumps (1:15 vs 1:22 / 1:44 vs 1:52):** Scene lighting shifts violently from daylight to pitch night and back to twin suns sunset in consecutive steps.
    *   *Viewer Impact:* Disorients spatial and temporal progression.
    *   *Cheapest Fix:* Apply color grade/exposure adjustment to harmonize night shots, or trim S9/S11 to reduce night-to-dusk contrast.

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Duplicate Clone (1:26) | Cut 1:25–1:28 from timeline | 0 USD (3 seconds runtime loss) |
| Bare-head helmet toggles (0:20, 1:00) | Cut Scene S3 (0:20–0:29) and Scene S7 (1:00–1:09) | 0 USD (20 seconds runtime loss) |
| Abrupt Night-to-Sunset Jump (1:44 to 1:52) | Apply color match/tint dissolve across beacon activation | 0 USD (Post-processing time) |
| Extreme environment shifts (Forest to Canyon) | Re-generate S4 or S8 to keep terrain consistent | Requires AI video regeneration |

---

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Character breathes without helmet in S3 and S7, but wears helmet in S1, S2, S4, S5, S6, S8, S9, S10, S11. | Is the alien atmosphere designed to be breathable, or is the helmet mandatory for survival? |
| Two identical characters appear walking together at 1:26. | Is there a cloning/hallucination narrative beat in the script, or is this a generation glitch? |
| Environmental sky shifts from golden day to dark night within 1 minute of screen time. | What is the intended time scale of the hike from pod to ship? |

---

## OUT-OF-SCOPE FLAGS
*   *TECHNICAL (VIDEO_QA):* High AI bloom and chromatic aberration haloing present around crystal structures at 1:45.
*   *DRAMATIC (SENARYO_QA):* Middle traversal section (0:30–1:15) lacks active dramatic conflict or goal escalation.
