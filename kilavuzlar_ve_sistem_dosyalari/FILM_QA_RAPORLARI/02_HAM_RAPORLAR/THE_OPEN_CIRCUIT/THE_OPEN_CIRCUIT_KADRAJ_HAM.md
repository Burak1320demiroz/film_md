# THE OPEN CIRCUIT — ⑨ KADRAJ QA (HAM)

> ⛔ HAM ÇIKTI — DÜZENLENMEDİ (AGENTS §2 kural ④)
> girdi: `/Users/dai/Downloads/the open cırcuıt (1).mp4` · **235,14 s** · 3840x2160 · 30 fps · AAC
>   ikiz: `the open cırcuıt.mp4` — AYNI SÜRE (235,14 s), 1280x720 · ⑪.0 kimliği 4K'dan alındı
> model: tek sağlayıcı, on iki mercek arka arkaya · tarih: 08.09.2026
> ⛔ **SPEC KAPISI [D129]:** `THE_OPEN_CIRCUIT_QA_SPEC.md` **VAR** *ve* paket
>   `QA_PROMPTLARI/FILME_OZEL/THE_OPEN_CIRCUIT/PAKET_1..12` **VAR** — rapor yine `INPUT MODE: V`.
>   → koşu YAPILMAMIŞ sayılır: T tablosuna satır YAZILMAZ, kesme listesi / REMOVE reçetesi /
>     yeniden üretim siparişi UYGULANMAZ. Ham çıktı kanıt olarak burada durur.
> ⛔ **TESLİM SINIFI: 🚨 HAM ZİNCİR** [D181] — filigran (23/23 klip) + kuyruk kartı (230,13→son)
>   + plan 25 sahne / makara 23 klip. HAM ZİNCİR'de mercek koşulmaz, rapor okunmaz, satır yazılmaz.
> ⛔ **⑤/⑦ notu [D110]:** on iki mercek üç künye grubuna ayrılıyor (25 replik / 22 replik /
>   16 replik) — grup içi künyeler BİREBİR aynı. Bağımsız ölçüm sayısı en fazla **3**, 12 değil.

---

INPUT MODE: V
FILM: The Open Circuit
RUNTIME: 03:55 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 22 · CUTS COUNTED: 21 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 03:50–03:55 title card
PRESENCE STRING: 1111111111111111111111
LINES HEARD: 16
00:21 "Second lugs under the coil."
00:25 "Fronts early."
00:52 "Then we're quick."
01:31 "Mass line is holding potential."
01:36 "It won't bite through that."
01:51 "Cutters."
01:55 "Not for that line."
02:11 "Bay pressure is nominal."
02:14 "Seal? Wait it out."
02:16 "Wait it out with what stat?"
02:24 "Two left."
02:31 "Module two is open to outside."
02:41 "Third rib from the seam. Count it."
03:32 "It's holding."
03:34 "It'll be cold by four."
03:37 "It'll be cold by four."
SETUPS REGISTERED: 22 distinct camera positions
LOCKOFF HELD: 22 / 22 clips

ARITHMETIC GATE
SCORED CATEGORIES:  2
SUM OF SCORES:      10.0
DIVISION:           10.0 ÷ 2 = 5.0

OVERALL SCORE: 5.0/10
VERDICT: RHYME BROKEN

## SETUP LEDGER

S1 | 00:00 | - | ECU / low / normal / ground front | A | MATCH | plate seam | 0
S2 | 00:20 | - | WS / eye / wide / front | B | MATCH | metal plate | 0
S3 | 00:29 | - | MCU / low / normal / ground side | C | MATCH | mast base | 0
S4 | 00:39 | - | MCU / eye / normal / ground side | D | MATCH | dirt mound | 0
S5 | 00:49 | - | WS / eye / wide / behind | E | MATCH | horizon | 0
S6 | 01:00 | - | WS / high / wide / above behind | F | MATCH | base module | 0
S7 | 01:09 | - | WS / eye / wide / behind | G | MATCH | glowing box | 0
S8 | 01:20 | - | WS / eye / wide / behind | H | MATCH | lit base | 0
S9 | 01:30 | - | MS / low / normal / front | I | MATCH | circular port | 0
S10 | 01:40 | - | CU / low / normal / ground side | J | MATCH | metal plate | 0
S11 | 01:50 | - | MS / eye / normal / side | K | MATCH | base modules | 0
S12 | 02:00 | - | CU / eye / long / side | L | MATCH | belt tool | 0
S13 | 02:10 | - | WS / eye / wide / front | M | MATCH | interior door | 0
S14 | 02:20 | - | MCU / eye / normal / side | N | MATCH | door frame | 0
S15 | 02:30 | - | WS / eye / wide / profile | O | MATCH | corridor wall | 0
S16 | 02:40 | - | MCU / low / normal / front | P | MATCH | corridor window | 0
S17 | 02:49 | - | WS / high / wide / behind | Q | MATCH | base module | 0
S18 | 02:59 | - | MS / low / normal / front | R | MATCH | cable | 0
S19 | 03:09 | - | MCU / low / normal / front | S | MATCH | plate | 0
S20 | 03:19 | - | CU / low / normal / front | T | MATCH | clamp | 0
S21 | 03:29 | - | MS / eye / wide / behind | U | MATCH | base module | 0
S22 | 03:40 | - | WS / high / wide / behind | V | MATCH | mast base | 0

## SETUP STRING

OBSERVED:   ABCDEFGHIJKLMNOPQRSTUV
PLAN:       none (mode V)
DIFFERS AT: none

## PRESENCE STRING

1111111111111111111111

## RHYME PAIR

|  | First frame | Last frame | Same? |
| --- | --- | --- | --- |
| setup letter / size / angle / anchor position / the one variable | A / ECU / low / plate seam / N/A | V / WS / high / mast base / N/A | No |

PAIR FAILS — The film shifts from an extreme close-up of a clamp to a wide shot of a mast, changing all variables instead of holding the setup.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| all held |  |  |  |  |

## SCORES SUMMARY

No returning setups exist (every scene is a new camera); categories 4 and 7 have no material and are excluded.

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | Mode V |
| 2 | Lockoff Integrity | 7/10 | No in-scope source |
| 3 | Rhyme Pair | 3/10 | S1 00:00 vs S22 03:40: Complete setup mismatch |
| 4 | Return Consistency | N/A | No returning setups |
| 5 | Cluster Seams | N/A | Mode V |
| 6 | Angle Arc & Deliberate Shocks | N/A | Mode V |
| 7 | Screen Geometry | N/A | No returning setups |

## SEVERITY TALLY

🔴 BLOCKER: 1   🟠 MAJOR: 0   🟡 MINOR: 0

## THE THREE THAT MATTER

1. 🔴 00:00 / 03:40 (S1/S22) Rhyme Pair Fail: Regenerate the final scene to share the exact setup as S1.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

The rhyme pair failure requires a complete regeneration of the final shot, as missing setups cannot be recovered in the edit. Lockoffs are stable and require no post-stabilization.

## FLAGS FOR DOCUMENT CHECK

Does the plan intentionally request 22 entirely unique setups without a single returning camera angle?

## OUT-OF-SCOPE FLAGS

* (BACKGROUND) Base module geography and surrounding terrain features shift significantly between wide exterior shots.
* (CONTINUITY) Suit wear, dirt accumulation, and lighting conditions fluctuate noticeably between cuts.
