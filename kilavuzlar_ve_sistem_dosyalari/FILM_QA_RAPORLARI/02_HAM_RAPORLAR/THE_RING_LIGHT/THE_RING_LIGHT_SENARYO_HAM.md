# THE RING LIGHT — SENARYO_QA (HİKAYE) HAM RAPOR

> **Tarih:** 12.08.2026 · **Rubrik:** `QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> **Mod:** V (plan dosyası verilmedi — §0.15 SPEC bloğu HAZIRDI)
> **Malzeme:** 144 s tam kurgu · rapor 15 sahne saydı (14 sahne + jenerik kartı)
> ⛔ Model çıktısı olduğu gibi. Belge cevapları film kaydında.
> ⚠️ Raporun kesme listesinin 1. ve 2. sırası planın **KESİLEMEZ viral ara**
> sahnesine (S2) ve onun devamına giriyor → uygulanmaz, gerekçe film kaydında.

---

```
MEASURED RUNTIME: 144 s        CUTS COUNTED: 14

INPUT MODE: V
BASELINE: THE FILM AS SCREENED
FILM: (not supplied)
FORMAT: (not supplied)
RUNTIME: 144
SCENE COUNT: 15 (counted, not from a document)
SPEC BLOCK PROVIDED: no — mode V

ENDS OR STOPS: stops — the film cuts to a title card immediately after a
  cliffhanger line ("There is something out there"), leaving the narrative
  unresolved.
PEAK LOCATED AT: 1:56 (S12) — the violent docking collision, followed by the
  emotional quiet beat at 2:00 (S13).

OVERALL STORY SCORE: 6.0/10
VERDICT: REVISE STRUCTURE
```

## THE FILM IN ONE SENTENCE (as a first-time viewer would say it)

"A spacecraft crew must manually eject an unbalanced payload to survive a
perilous orbital docking, only to discover an unknown anomaly inside the
station."

## SCORES SUMMARY

| Category | Score | Core Issue |
|---|:--:|---|
| Hook | 6/10 | Visually grand but takes 10s to introduce tension. |
| Premise & Clarity | 7/10 | Excellent hard-sci-fi focus on kinematic path-tracking and mass imbalance. |
| Structure & Pacing | 6/10 | Pacing drags early with redundant establishing exterior shots. |
| Character | 7/10 | High professional competence; quiet hand-hold is a strong human anchor. |
| Theme | 6/10 | Sacrifice for survival is clear, but undercut by the sudden cliffhanger. |
| Dialogue | 6/10 | Clinical and grounded, though the final tunnel line narrates the visible. |
| Emotional Arc | 7/10 | Steady escalation of pressure to a solid climax, followed by a necessary breathing space. |
| Ending | 4/10 | Fails to resolve; operates purely as a teaser for a next installment. |
| Originality | 6/10 | Evokes standard hard-sci-fi orbital peril but elevates it via precise control-logic dialogue. |
| Retention Risk | 5/10 | High drop-off risk between 0:20–0:40 due to lack of new information. |

## THE THREE THINGS THAT MOST HURT THIS FILM

1. 0:20-0:40 (S3-S4) — Redundant establishing shots — Stalls narrative momentum
   just as the central conflict is introduced.
2. 1:56 (S12) — Low-density impact physics — The collision visually reads as
   lightweight CGI rather than heavy metal shearing, dampening the climax.
3. 2:10 (S14) — Narrating the visible — "We are entering the transfer tunnel
   now" explicitly states what the cinematic framing already demonstrates.

## THE THREE THINGS WORTH PROTECTING

1. 1:10-1:30 (S8-S9) — The payload ejection — Dramatizes the solution to the
   center-of-mass control anomaly through physical action.
2. 2:00 (S13) — The hand-hold — Provides breathing room and emotional grounding
   after the violent docking sequence.
3. 0:10 (S2) — The initial control logic dialogue — Instantly establishes the
   crew's professional competence and the specific kinematic problem.

## THE ONE THING NOTHING ELSE DOES

It grounds its primary conflict entirely in highly specific autonomous
path-tracking control errors (pitch drift caused by asymmetric payload mass),
making the sci-fi feel functionally realistic.

## SCENE MAP — mode V (numbering is the reviewer's own)

| # | Timecode | Where | Who | What happens | Dialogue? | Function |
|---|---|---|---|---|:--:|---|
| S1 | 0:00-0:10 | Ext. Orbit | None | Station approach | Yes | Establish |
| S2 | 0:10-0:20 | Cockpit | Crew | Payload center of mass error identified | Yes | Inciting |
| S3 | 0:20-0:30 | Ext. Space | None | Station rotates slowly | No | Pace/Stall |
| S4 | 0:30-0:40 | Int. Window | None | View of station structure | No | Pace/Stall |
| S5 | 0:40-0:50 | Cockpit | Crew | Warning signals escalate | Yes | Escalate |
| S6 | 0:50-1:00 | Ext. Orbit | None | Comm check, shadow entry | Yes | Trans. |
| S7 | 1:00-1:10 | Ext. Dock | None | Thruster alignment | No | Build |
| S8 | 1:10-1:20 | Cockpit | Crew | Analyze pitch translation error | Yes | Choice |
| S9 | 1:20-1:30 | Ext. Hull | None | Payload canister is ejected manually | Yes | Action |
| S10 | 1:30-1:40 | Ext. Orbit | None | Final approach vector | Yes | Build |
| S11 | 1:40-1:50 | Cockpit | Crew | Distance/speed countdown | Yes | Tension |
| S12 | 1:50-2:00 | Ext. Dock | None | Violent collision upon docking | Yes | Climax |
| S13 | 2:00-2:10 | Cockpit | Crew | Visors up, a quiet hand-hold | No | Quiet Beat |
| S14 | 2:10-2:20 | Int. Tunnel | Crew | Floating into tunnel; anomaly spotted | Yes | Cliffhanger |
| S15 | 2:20-2:24 | Ext. Space | None | Static title card displayed | No | Outro |

```
RUNTIME (measured): 144
SCENE COUNT (counted): 15
SPEAKING SCENES: 9 — "Sekiz darbe..." / "Yük beşikte..." / "İptal edildi..." /
  "Shadow entry..." / "Her ötelemede..." / "Beşik boş..." / "Sonic warning..." /
  "20 metre..." / "We are entering..."
THE FILM'S QUESTION: Will the crew overcome the asymmetric payload error to
  safely complete the docking sequence?
THE READ: The crew survives the physical docking hazard by sacrificing their
  payload, only to face an unknown anomaly on the station.
```

## SCENE-BY-SCENE VERDICT

| # | Timecode | Function | Verdict | Note |
|---|---|---|---|---|
| S1 | 0:00-0:10 | Establish | KEEP | Good initial cinematic framing. |
| S2 | 0:10-0:20 | Inciting | KEEP | Crucial technical setup. |
| S3 | 0:20-0:30 | Pace/Stall | CUT | Redundant wide shot; stalls pacing. |
| S4 | 0:30-0:40 | Pace/Stall | CUT | Provides no new narrative information. |
| S5 | 0:40-0:50 | Escalate | KEEP | Solidifies stakes. |
| S6 | 0:50-1:00 | Trans. | KEEP | Bridges the gap smoothly. |
| S7 | 1:00-1:10 | Build | KEEP | Good visual tension. |
| S8 | 1:10-1:20 | Choice | KEEP | Grounds the anomaly in control logic. |
| S9 | 1:20-1:30 | Action | KEEP | Necessary physical payoff. |
| S10 | 1:30-1:40 | Build | TIGHTEN | Trim by 5s to hasten the climax. |
| S11 | 1:40-1:50 | Tension | KEEP | Excellent countdown rhythm. |
| S12 | 1:50-2:00 | Climax | KEEP | Core narrative peak. |
| S13 | 2:00-2:10 | Quiet Beat | KEEP | Vital emotional release. |
| S14 | 2:10-2:20 | Cliffhanger | REWRITE | Remove the expositional first line. |
| S15 | 2:20-2:24 | Outro | KEEP | Standard wrap. |

## RANKED CUT LIST (to lose 30 seconds)

resulting runtime: 119s — BELOW FORMAT FLOOR (assuming 2-4dk format),
replace don't remove.

1. S3 (0:20-0:30) — 10s — pure atmospheric stall lost; no story impact.
2. S4 (0:30-0:40) — 10s — redundant interior window view lost.
3. S10 (1:30-1:40) — 5s — lingering approach trimmed for tighter pacing.
4. S14 (2:10-2:15) — 5s — redundant spoken exposition lost.

## RETENTION DROP-OFF FORECAST

- 0:35 — Viewers leave due to 20 straight seconds (S3+S4) of static station
  views with no narrative progression. Fix: Cut S3 and S4 directly to the
  warning in S5.
- 2:20 — Viewers who wanted a contained story leave frustrated by a sudden
  cliffhanger stop. Fix: Ensure the ending provides thematic closure even if
  the plot continues.

## SHAREABLE MOMENT

2:00 — The transition from the violent external docking crunch immediately into
the dead-silent cockpit where the crew raises their visors and holds hands.

## REWRITE PRESCRIPTIONS

1. SCENE 14: cut the line "We are entering the transfer tunnel now" → it
   narrates what we already see. Start the dialogue directly at "Wait."
2. SCENE 3 & 4: replace with a single compressed 3-second establishing cut →
   fixes the early retention-killing pacing drag.

## FLAGS FOR DOCUMENT CHECK

- QUESTION: Is the film intended to act strictly as a pilot/teaser rather than
  a standalone short? I read the ending as an abrupt stop rather than a
  thematic close.
- QUESTION: Are scenes S3 and S4 designed as intended viral interstitials? If
  not, they act as severe pacing stalls.

## STORY TRACKING ROW

| Ⓥ (not supplied) | (not supplied) | 6 | 7 | 6 | 7 | 6 | 6 | 7 | 4 | 6 | 5 | 6.0/10 | ⚠️ ŞARTLI |
