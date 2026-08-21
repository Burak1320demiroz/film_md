# 🧍 THE BLUE DRIFT — KARAKTER_QA HAM RAPORU

> Çalıştırma: 20.08.2026 · yalnız video (dış model — Gemini) · TAM KURGU
> Rubrik: `../QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> ⚠️ Beş mercekli partinin parçası; parti kapılardan geçmedi.
> ⚠️ Sahne envanteri MANTIK raporuyla BİREBİR aynı (15 blok, aynı zaman
> kodları, aynı bulgular) — aynı oturumda koşuldu [D110: ortak defter,
> bağımsız ölçüm değil].
> ⚠️ İki 🔴'nin biri (4:10) filmin sahnesi olmayan başlık kartındadır.
> ⛔ Skor satırı 06 tablosuna işlenmedi (ortak adım ⑤).
> Model çıktısı aşağıda OLDUĞU GİBİ korunmuştur (kural ④).

---

FILM: the blue drıft.mp4
RUNTIME: ~04:14 ESTIMATED
SCENES OBSERVED: 15 · CHARACTERS TRACKED: 2
BASELINE: SELF-CONSISTENCY — this review measures whether each character agrees with themselves, not whether they match a design sheet.

OVERALL SCORE: 5/10
VERDICT: IDENTITY BREAK
An on-screen duplicate and a total facial identity break at the finale require critical regeneration.

CHARACTER PASSPORT(S)
CHARACTER A (Female Astronaut)
Label: Female Astronaut
First clear view: Scene 2, 0:10
Face: Fair skin, no visible scars.
Hair: Auburn, pulled back into a tight bun.
Eyes: Dark.
Build: Average height, athletic frame.
Costume: Blue spacesuit, gold/orange accent panels on chest and arms.
Equipment: Clear helmet sealed. Carrying glowing core sample.
Wear map: Clean throughout.
Voice: Mid-pitch, narrow range.

⭐ EVIDENCE BASE
FACE-VISIBLE: ~20s of ~254s total · 3 of 15 scenes
COSTUME-VISIBLE: 10 of 15 scenes
MOUTH ON SCREEN: yes

CHARACTER B (Male Astronaut)
Label: Male Astronaut
First clear view: Scene 2, 0:10
Face: Rugged, clean-shaven, no facial scars.
Hair: Dark brown, short.
Eyes: Dark.
Build: Taller, broad shoulders.
Costume: Blue spacesuit, teal accent panels on chest.
Equipment: Clear helmet sealed. Holding case.
Wear map: Clean.
Voice: Low-mid pitch.

⭐ EVIDENCE BASE
FACE-VISIBLE: ~25s of ~254s total · 4 of 15 scenes
COSTUME-VISIBLE: 10 of 15 scenes
MOUTH ON SCREEN: yes

APPEARANCE TABLE
Character    Scene    In-out    Face visible?    State notes
Female Ast.    S2    0:10-0:29    Yes    Packing sample. Visor state unreadable (no specular line).
Male Ast.    S2    0:10-0:29    Yes    Holding case. Visor state unreadable.
Both    S3    0:30-0:49    No    Running. Male carrying tripod. Duplicate glitch at 0:43.
Both    S4-S12    0:50-3:49    Partial    Cockpit. Helmets on, faces partially obscured by angle.
Both    S13    3:50-3:59    Yes    Helmets off. Clean faces.
Male Ast.    S15    4:10-4:14    Yes    Title card. Massive facial scar appears. Total face morph.

SCORES SUMMARY
Category    Score    Critical Issue
Facial Identity    3/10    −4 · 3:50 (clean) · 4:10 (scarred morph)
Hair, Build & Proportions    7/10    −1 · 4:10 (Male build shifts heavier)
Costume Identity    7/10    −1 · 3:50 (Suit paneling shifts slightly)
Wear, Damage & Injury    3/10    −4 · 3:50 (clean) · 4:10 (fresh scar with no cause)
Equipment State    4/10    −3 · 0:30 (held) · 0:50 (vanished)
Cross-Cut Action    7/10    −1 · 1:30 (Eyelines drift in reverse coverage)
Count & Separation    3/10    −4 · 0:40 (solo) · 0:43 (duplicate)
Voice & Performance    → SES_QA    [delegated to audio lens]

SEVERITY TALLY
🔴 BLOCKER: 2   🟠 MAJOR: 1   🟡 MINOR: 2

IDENTITY DRIFT MAP — per character
Character    Element    First slip (timecode)    Undeniable by    Recovered?
Male Ast.    Facial Identity / Scar    4:10    4:10    No
Female Ast.    Silhouette / Count    0:43    0:43    Yes

WEAR TIMELINE — per tracked mark
Mark    Acquired    Present at    Absent at ⚠️    One-way?
Right Cheek Scar (Male)    4:10    4:10    3:50    No (Appears spontaneously)

CONTRADICTION LOG
Timecode A    Timecode B    Character    Category    What contradicts what    Severity
3:50    4:10    Male Ast.    Facial Identity    Character has a clean, unblemished face at 3:50, but morphs into a different facial structure with a massive cheek scar at 4:10.    🔴 BLOCKER
0:40    0:43    Female Ast.    Count & Separation    Only one female astronaut is running, but a transparent duplicate silhouette suddenly overlays the frame.    🔴 BLOCKER
0:30    0:50    Male Ast.    Equipment State    Character picks up and carries a tripod at 0:30, but is seated in the cockpit at 0:50 with empty hands and no drop shown.    🟠 MAJOR

THE THREE THAT MATTER
Title Card Identity Break (3:50 & 4:10): The male astronaut completely morphs faces and acquires a severe scar. Fix: Regenerate the title card to match the established actor.

Duplicate Silhouette (0:40 & 0:43): A phantom character appears over the running sequence. Fix: Re-cut or trim the shot right before the glitch.

Vanishing Tripod (0:30 & 0:50): A carried object teleports out of existence between scenes. Fix: Accept it, as it happens during an implied time jump.

FIXABLE IN THE EDIT vs REQUIRES REGENERATION
Finding    Fix    Cost
Duplicate silhouette (0:43)    Edit: Trim the final 3 seconds of the shot    Low
Vanishing tripod    Accept it    Zero
Facial morph & scar (4:10)    Regenerate: Re-roll the final title card    Medium

FLAGS FOR DOCUMENT CHECK
Observation    Question the document must answer
Visor states are completely unreadable in S2 due to a lack of specular reflections.    Are the visors intended to be SEALED or OPEN during the surface walk?

OUT-OF-SCOPE FLAGS
0:12: Fingers merge into the glowing core sample → VIDEO_QA

4:10: Burned-in subtitles/text on the title card → VIDEO_QA

3:30: The ship docks inside a tunnel but is later seen outside → MANTIK_QA
