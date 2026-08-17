# 🧩 THE COLD BURN — MANTIK_QA HAM RAPORU

> Çalıştırma: 09.08.2026 · MOD V (rubrik zaten belgesiz çalışır — Gemini)
> Rubrik: `../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> Ölçülen malzeme: 225 s kurgu / 12 sahne. Belge cevapları:
> `../01_FILM_RAPORLARI/THE_COLD_BURN.md`
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④). DERS 65 TUTTU.
> ✅ Rubrik uyum notu: `COUNTER: NONE` satırı DERS 78 gereği FLAGS'e SORU
> olarak taşındı — dipnot kuralının İLK uygulanışı (Blind Return'de
> atlanmıştı). Belge cevabı: planda sayaç kanalı VAR (duruş küresi +
> 10 segmentlik rezerv göstergesi) → D78'in 3. vakası.

---

FILM: (not supplied)
RUNTIME: 03:45 · SCENES OBSERVED: 12
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees
with itself, not whether it matches its design.

OVERALL SCORE: 7/10
VERDICT: FIXABLE IN EDIT

SCENE INVENTORY
#    In-out    Location    Present    What happens    Dialogue
S1    0:00-0:10    Ice Planet Ext    None    Ship resting on the ice.    No
S2    0:10-0:20    Ice Planet Ext    2 Astronauts    Collecting a blue sample into a metal case.    Yes
S3    0:20-0:40    Ice Planet Ext    2 Astronauts    Observing massive storm front approaching.    Yes
S4    0:40-0:50    Ice Planet Ext    2 Astronauts    Running to the ship carrying the case.    Yes
S5    0:50-1:20    Ship Cockpit    2 Astronauts    Taking off as the storm hits.    Yes
S6    1:20-1:40    Space Orbit    Ship    Ship approaching the orbital station.    No
S7    1:40-2:20    Space Orbit    Station    Station module suddenly explodes.    Yes
S8    2:20-2:50    Space Orbit    Ship/Station    Ship docks with the damaged station hub.    Yes
S9    2:50-3:10    Hub Interior    2 Astronauts    Entering zero-g; fire breaks out in module.    Yes
S10    3:10-3:30    Hub Interior    2 Astronauts    Evacuating back to the ship.    Yes
S11    3:30-3:40    Space Orbit    Ship    Undocking and jumping to hyperspace.    No
S12    3:40-3:45    Space    Woman    Title card appears over character.    No

SCORES SUMMARY
Category    Score    Critical Issue
Physical Consistency    7/10    Gravity shift from planet to space is coherent; fire propagation contradicts its lighting.
Counter Logic    N/A    NONE
Spatial Geography    6/10    Docking port scale shifts severely between approach and contact.
Time & Light Logic    7/10    Interior lighting contradicts the presence of the fire in reverse angles.
State, Costume & Props    7/10    Suit wear resets from the planet surface to the cockpit.
Causality & Knowledge    8/10    Characters react to visible threats coherently.
Quantity Consistency    10/10    No numbering or quantity mismatches observed.
Setup & Abandonment    5/10    The blue sample is the inciting object and is completely abandoned.

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 1

COUNTER CURVE
NONE

LOCATION MAP
Location (your name for it)    Scenes    Consistent?    Mismatch
Ice Planet Ext    S1, S2, S3, S4    Yes    None
Ship Cockpit    S5    Yes    None
Space Orbit (Station)    S6, S7, S8, S11    No    Docking port scale shifts.
Hub Interior    S9, S10    Yes    None

DRIFT MAP — where the film starts losing itself
Element    First slip (timecode)    Undeniable by    Recovered?
Docking Scale    2:20 (S8)    2:40 (S8)    No, scene ends.
Fire Lighting    2:50 (S9)    3:10 (S10)    No.

CONTRADICTION LOG
Timecode A    Timecode B    Category    What contradicts what    Severity
0:18    0:50    State, Costume & Props    The man kneels on the ice in S2, accumulating snow/wear on his knees. In S5 (cockpit), the suit is pristine with no cleaning shown.    🟡 MINOR
2:20    2:40    Spatial Geography    The station docking port appears massive relative to the ship in the wide approach, but shrinks considerably in the close-up lock sequence.    🟠 MAJOR
3:00    3:15    Time & Light Logic    The hub is bathed in orange light from the fire in S9. In S10, the reverse shot shows the astronauts fleeing under cool blue LEDs, contradicting the active fire behind them.    🟠 MAJOR

OPEN THREADS
Object / setup    Introduced    Returned to?    Note
Blue sample / metal case    S2 (0:10)    No    Placed in the case and carried to the ship. It is never seen in the cockpit or during the station evacuation.

THE THREE THAT MATTER
Docking port scale mismatch (2:20 vs 2:40)
Why: It breaks spatial geography at a critical tension moment, making the ship feel like a toy.
Fix: Re-cut to hide the direct contact point, relying on interior sound/reaction.
Interior lighting contradiction (3:00 vs 3:15)
Why: The absence of fire-light in the reverse shot makes the two angles feel like they belong to different scenes, killing the urgency of the evacuation.
Fix: Regenerate the S10 shot to include motivated orange/flickering light, or apply a heavy color grade in edit.
Suit wear regeneration (0:18 vs 0:50)
Why: A classic AI artifact where dirt fails to persist between environments.
Fix: Accept it. The pacing of the takeoff sequence makes it a minor distraction.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Docking scale shift    Trim the close-up docking shot.    Cheap
Lighting mismatch during fire    Regenerate S10 with correct motivated lighting.    Expensive
Suit regeneration    None (accept).    Zero

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
There is no environmental counter tracked across the scenes.    Is there an environmental counter planned (e.g., storm proximity distance) that requires a specific visual tracker, or is "approaching storm" sufficient?
The blue sample is collected and forgotten.    Was the blue sample intended to be used, referenced, or lost during the station disaster, or is it a deliberate open thread?

OUT-OF-SCOPE FLAGS
Rigid zero-g models and static fire behavior (0g physics) → VIDEO_QA
Lack of a Central Choice regarding the sample during the climax → SENARYO_QA
Burned-in text visible on the final title card → VIDEO_QA
