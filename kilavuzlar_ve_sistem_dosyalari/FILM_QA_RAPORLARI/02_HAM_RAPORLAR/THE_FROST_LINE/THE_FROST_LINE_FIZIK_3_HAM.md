# THE FROST LINE — ⑥ FİZİK HAM RAPORU (2. PARTİ · 3. koşu · mod V)

> Operatör künyesi: sahip 01.09.2026 mesajıyla teslim etti · model bilinmiyor
> (dış model, sahip koştu) · girdi: 235,201 s'lik kurgu + rubrik.
> Önceki koşular: `THE_FROST_LINE_FIZIK_HAM.md` · `..._FIZIK_2_HAM.md` (1. parti).
> Aşağısı model çıktısıdır, düzenlenmemiştir.
>
> ⛔ **MOD KAPISI DÜŞTÜ [kart F2]:** plan sayısal kilit taşıyor (0,38 g ·
> tünel 32×4,5×3,2 m · jet ~4 m · yama ≤1 s · sarkma takvimi · kırağı
> hattı) → koşu MOD D olmalıydı; NUMERIC LOCK LIST boş.
> ⛔ **FRAME RATE ASSUMED: 24 fps — ölçüm 30 fps der.** Rubriğin kendi
> kuralı ("state your frame rate once and use it everywhere") ihlal:
> süre türevli her sayı (implied g dâhil) bu eksende ŞARTLI. Üç koşunun
> üçü de 24 fps varsaydı.
>
> ⭐ Yine de iki gerçek PASS var ve ikisi de planı DOĞRULUYOR: L1 jeti
> g≈3,2 m/s² ve L6 toprak düşüşü g≈4,4 m/s² — SPEC 0,38 g = 3,72 m/s².
> ⑥, üç mercekten planın sayısal kilidine oturan tek ölçümü üretti.
> ⚠️ `Impact & Momentum: — no in-scope source` hücresi doğru uygulanmış
> (sayı taşımıyor, ortalamadan çıkmış) — ① ve ⑤ aynı kuralı ihlal etti.

---

INPUT MODE: V
FILM: (not supplied)
RUNTIME: 235 s measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 23 · CUTS COUNTED: 22
NON-SCENE MATERIAL: 3:50-3:55 Title Card
LINES HEARD: none — room tone present
GRAVITY: 3.2 – 4.4 m/s² (Geyser fall L1, soil drop L6)
PREMISE REGISTER:

Low-gravity environment (falls take roughly 1.5x longer than Earth-normal, consistent with Mars).

ARITHMETIC GATE
SCORED CATEGORIES:  8
SUM OF SCORES:      55.0
DIVISION:           55.0 ÷ 8 = 6.9

OVERALL SCORE: 6.9/10
VERDICT: INCONSISTENT WORLD

PHYSICS LEDGER
#    Timecode    Event    Duration (measured)    Distance (est. + RULER)    Implied value    Consistent with?
L1    0:02-0:10    Geyser spray falling    ~2.5 s    ~10 m (≈3x greenhouse height)    g ≈ 3.2 m/s²    Premise (Low-G)
L2    0:29-0:39    Gas spray from tear    Continuous    drops ~1 m over ~3 m travel    Ballistic arc    Premise (Low-G)
L3    1:00-1:04    Greenhouse roof collapses    ~2.0 s    ~3 m (≈1.5x astronaut)    Material has no structural rigidity    Unresisting cloth
L4    1:59-2:09    Astronaut pulls plastic sheet    ~1.5 s    ~2 m (≈1x astronaut)    g ≈ 1.7 m/s² (slowed by air resistance)    Plausible for plastic sheet
L5    3:10-3:20    Astronaut pushes metal bar    ~2.0 s    Bends >30 degrees    Metal acts elastically beyond yield strength    Rubber
L6    3:30-3:35    Astronaut drops soil/seeds    ~0.3 s    ~0.2 m (≈hand to ground)    g ≈ 4.4 m/s²    Premise (Low-G)
L7    0:00 (S1)    Exterior shadows    Static    Cast right-to-left    Light source on right    Itself
L8    3:39 (S23)    Exterior shadows    Static    Cast left-to-right    Light source on left    180° shift from L7
L9    0:00 (S1)    Greenhouse exterior scale    Static    Height ≈ 3 m (≈1.5x astronaut)    Exterior diameter    Itself
L10    1:39 (S11)    Greenhouse interior scale    Static    Height ≈ 4.5 m+ (≈2.5x astronaut)    Interior height    1.5x larger than L9

SCORES SUMMARY
#    Category    Score    Critical Issue
1    Gravity & Free Fall    8/10    -2 · L1, L6 variance
2    Ballistics & Trajectories    9/10    -1 · L2 slight float
3    Impact & Momentum    —    no in-scope source
4    Material Behaviour    2/10    -4 · L3 (1:00) · -4 · L5 (3:15)
5    Particles & Atmosphere    8/10    -2 · L2 gas spray hangs slightly
6    Scale & Measurement    6/10    -4 · L9 (0:00) vs L10 (1:39)
7    Rates & Timing    9/10    -1 · L4 slight cinematic slow-mo
8    Light & Shadow Physics    4/10    -6 · L7 (0:00) vs L8 (3:39)
9    Human Biomechanics    9/10    -1 · Astronaut gait slightly heavy for low-G

PRESENCE STRING
11111111111111111111111

SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 3

GRAVITY TABLE
Ledger row    Timecode    Height (est. + ruler)    Time    Implied g    vs film's g
L1    0:02    ~10 m (≈3x greenhouse)    ~2.5 s    ~3.2 m/s²    Matches Premise
L6    3:30    ~0.2 m (≈hand to ground)    ~0.3 s    ~4.4 m/s²    Matches Premise

RATE TABLE
Rate    First measure (timecode)    Second measure (timecode)    Verdict
Astronaut walking speed    1:29    1:50    PASS (~1.2 m/s consistent)

CONTRADICTION LOG
Ledger rows    Timecodes    Cat.    What contradicts what    Severity
L9, L10    0:00, 1:39    6    Exterior greenhouse height (~3m) contradicts interior aisle height (~4.5m).    🟠 MAJOR
L7, L8    0:00, 3:39    8    Shadows cast right-to-left at 0:00, then left-to-right at 3:39, reversing the sun's position.    🟠 MAJOR

THE THREE THAT MATTER
Material Amnesia (Metal Bar): At 3:15, the rigid metal crossbar bends like a rubber tube when the astronaut pushes it. Viewers instantly feel this because human intuition for metal rigidity is absolute; it makes the prop look like a cheap toy. Fix: Regenerate the shot or cut just before the bend becomes extreme.

Material Amnesia (Greenhouse Collapse): At 1:00, the pressurized, thick polymer greenhouse deflates and collapses exactly like a thin cotton bedsheet, displaying zero structural resistance or material memory. Fix: Regenerate the clip prompting for rigid panels buckling, or accept it as a limitation of the model.

Sun Split (Shadow Reversal): The exterior shadows flip 180 degrees between the opening wide shot (0:00) and the closing wide shot (3:39), implying the sun crossed the entire sky instantly. Fix: Flip the S23 clip horizontally in the edit if no text/asymmetry prevents it.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Metal bar bends like rubber (3:15)    Trim the tail of the clip before the bend exceeds plausible metal flex.    Low (Edit)
Sun split/shadow reversal (3:39)    Mirror the clip horizontally (assuming no asymmetric suit decals are visible).    Low (Edit)
Scale inflation (Interior vs Exterior)    Unfixable in edit.    High (Regenerate)

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
The greenhouse deflates like soft cloth.    Does the design document specify the greenhouse as a soft inflatable tent, or a rigid/semi-rigid structure?

OUT-OF-SCOPE FLAGS
1:00 — Exterior greenhouse collapses entirely, but interior is shown fully structured in S9 → CONTINUITY lens.
3:23 — Fingers phase directly through the glass visor of the helmet → FRAME lens.
