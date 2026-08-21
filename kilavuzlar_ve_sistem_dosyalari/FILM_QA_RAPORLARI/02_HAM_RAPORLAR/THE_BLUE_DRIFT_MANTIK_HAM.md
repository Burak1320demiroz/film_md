# 🧩 THE BLUE DRIFT — MANTIK_QA HAM RAPORU

> Çalıştırma: 20.08.2026 · yalnız video (dış model — Gemini) · TAM KURGU
> Rubrik: `../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> ⚠️ Beş mercekli partinin parçası; parti kapılardan geçmedi.
> ⭐ Bu raporun 15 blokluk sahne envanteri, planın 9 s + 24 × 10 s
> ızgarasının BİREBİR birleşimidir (blok 1 = 9 s hook) — ızgara geri
> alma tablosu: `../01_FILM_RAPORLARI/THE_BLUE_DRIFT.md` · KOŞU 2
> ⚠️ Üç bulgunun üçü de planda YAZILI tasarıma denk geliyor [D87 kapısı].
> ⛔ Skor satırı 04 tablosuna işlenmedi (ortak adım ⑤).
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

FILM: the blue drıft.mp4
RUNTIME: ~04:14 ESTIMATED
SCENES OBSERVED: 15
MATERIAL TYPE: FILM (undeclared)
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees with itself, not whether it matches its design.

OVERALL SCORE: 8/10
VERDICT: FIXABLE IN EDIT

SCENE INVENTORY
#    In-out    Location    Present    What happens    Dialogue
1    0:00-0:09    Ice Moon Surface    Male, Female    Wide shot of astronauts observing    No
2    0:10-0:29    Ice Moon Surface    Male, Female    Packing glowing core sample into case    No
3    0:30-0:49    Ice Moon Surface    Male, Female    Holding tripod, running to ship    No
4    0:50-1:09    Ship Cockpit    Male, Female    Pre-flight systems check    No
5    1:10-1:29    Ext. Ship    None visible    Vertical liftoff into space    No
6    1:30-1:59    Ship Cockpit    Male, Female    Flying in orbit    No
7    2:00-2:19    Ext. Ship    None visible    Cruising near gas giant    No
8    2:20-2:49    Ship Cockpit    Male, Female    Instrument monitoring    No
9    2:50-2:59    Ext. Station    None visible    Wide shot of space station    No
10    3:00-3:29    Ship Cockpit    Male, Female    Approaching station    No
11    3:30-3:39    Ext. Station    None visible    Ship entering internal docking bay    No
12    3:40-3:49    Ship Cockpit    Male, Female    Docked inside bay    No
13    3:50-3:59    Int. Station    Male, Female    Helmets off, glowing case on shelf    No
14    4:00-4:09    Ext. Station    None visible    Ship docked externally on hull    No
15    4:10-4:14    Title Card    Male    Poster shot with text    No

SCORES SUMMARY
Category    Score    Critical Issue
Physical Consistency    10/10    None
Counter Logic    N/A    No counter observed
Spatial Geography    4/10    −6 · 3:30 (S11) · 4:00 (S14)
Time & Light Logic    10/10    None
State, Costume & Props    6/10    −2 · 1:20 (S5) · 2:00 (S7) / −2 · 3:50 (S13) · 4:10 (S15)
Causality & Knowledge    10/10    None
Quantity Consistency    10/10    None
Setup & Abandonment    10/10    None

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 1

COUNTER CURVE
NONE

LOCATION MAP
Location (your name for it)    Scenes    Consistent?    Mismatch
Ice Moon Surface    1, 2, 3    Yes    None
Ship Cockpit    4, 6, 8, 10, 12    Yes    None
Ext. Ship    5, 7    No    Roof details shift mid-flight
Ext. Station    9, 11, 14    No    Docking port geography shifts
Int. Station    13    Yes    None

DRIFT MAP — where the film starts losing itself
Element    First slip (timecode)    Undeniable by    Recovered?
Ship Exterior Details    2:00    2:00    No
Docking Geography    4:00    4:00    No
Character Face State    4:10    4:10    No

CONTRADICTION LOG
Timecode A    Timecode B    Category    What contradicts what    Severity
3:30    4:00    Spatial Geography    The ship enters an enclosed, internal tunnel docking bay (3:30) but is later shown docked flat against the external outer hull of the station (4:00).    🟠 MAJOR
3:50    4:10    State, Costume & Props    The male character has a clean, unscarred face inside the station (3:50) but suddenly has a massive, fresh scar on his right cheek in the title card (4:10).    🟠 MAJOR
1:20    2:00    State, Costume & Props    The ship's roof is flat grey during ascent (1:20) but suddenly sprouts a bright orange dome sensor while cruising (2:00).    🟡 MINOR

OPEN THREADS
Object / setup    Introduced    Returned to?    Note
Tripod / Instrument    0:30    No    Carried to the ship during the escape, never seen or used again.

THE THREE THAT MATTER
Docking Bay Geography (3:30 & 4:00): The ship flies into a tunnel but is later seen stuck to the outside of the station. This breaks spatial reality at the climax of the journey. Fix: Re-cut to remove the 4:00 external shot.

Facial Scar Appearance (3:50 & 4:10): The male protagonist instantly acquires a massive facial scar at the end of the film. A viewer will assume they missed a crucial action scene. Fix: Regenerate the title card image to match the 3:50 face.

Ship Roof Dome (1:20 & 2:00): An orange dome appears on the ship mid-flight. Noticeable, but registers as a minor generation artifact rather than a story break. Fix: Accept it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Docking geography contradiction    Edit: Cut scene 14 (4:00)    Low
Facial scar contradiction    Regenerate: Re-roll the title card    Medium
Ship roof dome appearing    Accept it    Zero

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The tripod is carried to the ship but never deployed.    Was this prop intended to be used on the station, or is it just set dressing for the evacuation?
The title card is appended to a linear narrative film.    Was this project planned as a standalone short film or a promotional teaser trailer?

OUT-OF-SCOPE FLAGS
4:10: Burned-in text appears on screen during the title card → VIDEO_QA

3:50: Facial consistency wavers slightly compared to the surface visors → KARAKTER_QA
