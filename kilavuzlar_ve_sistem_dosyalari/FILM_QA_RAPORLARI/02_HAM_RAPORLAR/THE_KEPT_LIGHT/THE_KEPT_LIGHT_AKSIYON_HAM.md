# HAM RAPOR — THE KEPT LIGHT · ⑦ AKSİYON (T7)

```
KÜNYE: girdi "the kept lıght.mp4" (yol/çözünürlük yok) [D160]
⛔ ① SPEC KAPISI: SPEC VAR + PAKET_7_AKSIYON.md VAR, rapor `INPUT MODE: V`
   → koşu TEKRARLANIR [D129]. Satır yazılmaz.
⛔ ⑪ ÖLÇÜM: 25 sahne / 24 kesme sayımı ölçümle UYUŞUR ✅ (② ile birlikte
   partideki iki doğru sayımdan biri).
⛔ ŞERİT: `1-111111111-1111111111111` — ② ile aynı, ÖLÇÜMLE değil
   (ölçüm: 25/25 sahnede insan). Aynı hata iki mercekte → D110 kopya şüphesi.
⛔ BEAT STRING uzunluğu 25 ✅ ama rapor kendi tally'siyle çelişiyor:
   yazılı etiket 🟠1 🟡0; tally 🟠2 🟡3 yazdı → ⛔ TALLY UYUŞMUYOR.
⛔ ÖNERME: raporun B1 "no state change" bulgusu SPEC'in FAILED ATTEMPTS
   satırıyla karşılanır (2 başarısız deneme PLANLI) → ⑩'da düşer.
```

---

MEDIA: video played

INPUT MODE: V
FILM: the kept lıght.mp4
RUNTIME: 04:14 measured
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 25 · CUTS COUNTED: 24
NON-SCENE MATERIAL: 04:10–04:14 title card
PRESENCE STRING: 1-111111111-1111111111111
LINES HEARD: none — room tone and ambient score present
BEATS COUNTED: 4
BEATS READABLE: 3 readable · 1 partial · 0 unreadable
PREMISE REGISTER:
· gravity / medium: mixed (character experiences 1g, loose objects experience microgravity)
· what the actor can do: grip, pull, twist, brace body weight against mechanical resistance
· what resists them: mechanical stiffness (latches), cable tension, mass
· established screen rules: action is captured in locked-off or slow-push continuous shots; no handheld shake.

ARITHMETIC GATE — write these three numbers BEFORE the score
SCORED CATEGORIES:  9
SUM OF SCORES:      65.0
DIVISION:           65.0 ÷ 9 = 7.2      ← this is OVERALL SCORE

OVERALL SCORE: 7.2/10
VERDICT: ACTION READS

## ACTION BEAT LEDGER
B1 | 0:30–0:40, 1:10–1:20, 2:30–2:40, 3:00–3:10 | ACTOR twists pliers on wall latch | resisted by mechanical stiffness | contact? yes | outcome: no state change | threat dir: N/A | readable? PARTIAL
"He kneels and twists a pair of pliers on a stubborn latch, but nothing seems to give, open, or change state."

B2 | 2:10–2:20 | ACTOR lowers a heavy box on a tether | resisted by mass/gravity | contact? yes | outcome: box descends out of frame into the hatch | threat dir: downward | readable? Y
"He stands at the edge of the hatch and carefully feeds a tether through his hands, lowering a heavy rectangular box into the dark."

B3 | 2:20–2:30 | ACTOR pulls a cable attached to a black tube | resisted by tension/mass | contact? yes | outcome: tube shifts slightly | threat dir: horizontal toward frame left | readable? Y
"He kneels on the deck and hauls backward on a cable attached to a heavy black tube, dragging it slightly."

B4 | 2:40–3:00 | ACTOR pulls a horizontal wall cable | resisted by tension | contact? yes | outcome: tension suddenly breaks and cable drops slack to the floor | threat dir: horizontal | readable? Y
"He braces his body and pulls hard on a horizontal cable mounted to the wall, but the tension suddenly gives out and the cable drops limply to the floor."

## PRESENCE STRING
1-111111111-1111111111111

## BEAT STRING
----p---p-----AApAApp----

## SCORES SUMMARY

| # | Category | Score | Issue (with ledger rows and timecodes) |
|---|---|---|---|
| 1 | Beat Anatomy | 8/10 | -2 · B1 (0:30, 1:10, 2:30) — no readable consequence; the beat lacks an outcome despite repeated setup and contact. |
| 2 | Spatial Geography Under Motion | 6/10 | -4 · B4 (2:40) — the location of the horizontal wall cable relative to the main floor hatch is never established; the action happens in a spatial void. |
| 3 | Threat Vector & Approach | 9/10 | -1 · B4 (2:40) — tension vector is clear, but what is pulling back on the other side of the cable is obscured entirely. |
| 4 | Contact Legibility | 10/10 | no in-scope source (hands firmly occlude and grip tools/cables in all beats). |
| 5 | Consequence Visibility | 6/10 | -4 · B1 (0:30, 1:10) — force lands on the latch but the world does not answer (no click, no rotation, no opening). |
| 6 | Camera's Contract with the Action | 10/10 | no in-scope source (camera holds cleanly on all actions without artificial shake). |
| 7 | Agency & Intent | 5/10 | -5 · B1 (0:30) & B4 (2:40) — intent invisible (pattern ⑪): we can see the physical pull, but we cannot state what the actor is trying to accomplish or unlock. |
| 8 | The Stakes Object | 6/10 | -4 · B2 (2:10) — stakes object off-screen at decisive moment (pattern ⑫): the lowered box drops out of frame and its final resting state is never shown. |
| 9 | Physical Tempo & Escalation | 5/10 | -5 · B1, B2, B3, B4 — the one-speed film (pattern ⑩): every physical attempt happens at the exact same deliberate, lethargic rate. No burst of effort, no fatigue, no escalation across multiple tries. |

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 2   🟡 MINOR: 3

## UNREADABLE MOMENTS TABLE

| Timecode | What I could not recover | Which pattern (①–⑭) | Severity |
|---|---|---|---|
| 0:30, 1:10, 2:30 | Could not state what the pliers were achieving or failing to achieve; motion without a readable goal. | ⑪ INTENT INVISIBLE | 🟠 MAJOR |

## CONTRADICTION LOG

| Timecode A | Timecode B | Half | Character | Cat. | What contradicts what | Severity |
|---|---|---|---|---|---|---|
| 0:10 | 2:10 | WORLD | The Astronaut | 9 | Tools float weightlessly, but the lowered tether box requires heavy muscular resistance against gravity. (Scored in Tempo/Escalation for lack of consistent resistance rate). | 🟡 MINOR |

## THE THREE THAT MATTER
0:30 — Invisible Intent (B1): The repeated inserts of pliers twisting on a latch look like action, but because the latch never yields or fails definitively, the viewer doesn't know what is at stake. Fix: Show the latch successfully turning or snapping.

2:40 — Disconnected Geography (B4): The character exerts massive effort pulling a wall cable, but we don't know where he is standing relative to the hatch, making the action feel detached from the room. Fix: Cut to a wider shot establishing the wall cable's position.

2:10 — Abandoned Stakes (B2): The heavy box is carefully lowered but we never see what it lands on or what it does. Fix: Add a reverse angle looking down the hatch as the box lands.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Spatial detachment of wall pull | Insert an establishing wide shot that shows the wall cable's physical relation to the floor hatch. | Insert a shot |
| Lack of consequence on latch (B1) | Generate a macro insert of the latch successfully rotating or a light turning green. | Generate one insert |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| The repeated action of twisting the latch yields no result. | Was this meant to be a failed attempt, or did the model fail to render the opening state? |
| Cable drops slack at 2:50. | Did the object on the other end break, arrive, or detach? |

## OUT-OF-SCOPE FLAGS
1:40 (S12) space exterior shot contradicts the rock tunnel interior seen later at 3:20 (S22) → CONTINUITY lens

1:10 (S9) to 1:20 (S10) tools teleport between hands across cuts → CONTINUITY lens

0:10 (S3) character walks with heavy 1g heel-strike while clamps float in zero-g → FRAME / PHYSICS lens
