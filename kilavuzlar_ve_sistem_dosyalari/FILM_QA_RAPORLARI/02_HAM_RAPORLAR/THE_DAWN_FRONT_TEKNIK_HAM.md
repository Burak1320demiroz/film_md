# 🔧 THE DAWN FRONT — TEKNİK QA HAM RAPORU

> **Tarih:** 05.08.2026 · **Model:** Gemini
> **Girdi:** video + `QA_PROMPTLARI/THE_DAWN_FRONT_VIDEO_QA_TEK_DOSYA.md`
> (SPEC plan dosyasından gömülü — projenin ilk dolu-SPEC'li dış model koşusu)
> **Video süresi:** 141 s (plan: 140 s + opsiyonel kapanış kartı)
> ⚠️ Aynı gün gelen MANTIK raporunun videosu 145 s / "_2.mp4" idi —
> iki koşunun aynı kurgu sürümü olup olmadığı belirsiz.
>
> Aşağıısı model çıktısının olduğu gibi kopyasıdır — düzenlenmez.

---

FILM: THE DAWN FRONT
SCENE: Compilation
VIDEO DURATION: 141s
SPEC SOURCE: embedded in prompt (plan §0.10/§0.16 + bibles) — VERIFIED

OVERALL SCORE: 4/10
VERDICT: REGENERATE

## SCORES SUMMARY

| Category | Score | Critical issues |
|----------|:-----:|-----------------|
| Character | 4/10 | Severe face morphing; unscheduled back tank appears. |
| Scale & Physics | 3/10 | Heavy gravity (~1g) on debris; no 8° tilt persistence. |
| Camera & Cuts | 3/10 | Widespread camera tracking; unplanned cuts in S1/S2. |
| Lighting | 4/10 | Fire illumination present; sun counter not monotonic. |
| Environment | 4/10 | Massive liquid hallucination on the front (waterfall). |
| Particles & Materials | 3/10 | Fire in vent/exhaust; dry gas rule completely broken. |
| Audio | 5/10 | Muffled acoustics lost; timing misaligned with visual cuts. |
| Story-Beat Presence | 4/10 | Scenes severely out of sync; S3/S12 missing/skipped. |
| Negative Violations | 8 count | Fire, liquid, face morph, text mid-scene, bad cuts. |
| Motion Quality | 5/10 | Standard AI jello/warp; run cycle lacks 0.28g stride. |

## SEVERITY TALLY
🔴 BLOCKER: 8   🟠 MAJOR: 4   🟡 MINOR: 2

## SCENE PRESENCE TABLE

| S# | Present? | On time? | Key beat readable? | Note |
|----|----------|----------|--------------------|------|
| S0 | Yes | Yes | Yes | Camera drifts instead of lockoff. |
| S1 | Yes | No | No | Contains unplanned in-scene cut. |
| S2 | Yes | No | No | Wall exhibits severe liquid flow. |
| S3 | No | No | No | Notch opens prematurely in S2. |
| S4 | Yes | No | No | Cargo strap touch missing. |
| S5 | Yes | No | No | Vent emits literal flames. |
| S6 | No | No | No | Engine off/trap beat skipped. |
| S7 | No | No | No | Coasting missed; rover driving. |
| S8 | Yes | No | No | Full mirror shot missing. |
| S9 | No | No | No | Wheel drop and 8° tilt absent. |
| S10 | No | No | No | Reverse gear beat missing. |
| S11 | Yes | No | Yes | Sun shaft occurs out of sequence. |
| S12 | No | No | No | 4km overview completely missing. |
| S13 | Yes | No | No | Text overlays before end card. |

## COUNTER CHECK
Mirror: [1/8 at 0:07 · 1/2 at 0:40 · full at N/A — monotonic? no]
Sun:    [monotonic brightening? no — reversals with timestamps at 1:52]

## TOP 3 CRITICAL ERRORS
1. 0:20 — 🔴 BLOCKER — Massive liquid hallucination; the front behaves like a waterfall, breaking the strict zero-liquid/dry-gas physics contract.
2. 0:48 — 🔴 BLOCKER — Identity drift; character's face drastically ages and bone structure morphs during close-up.
3. 1:42 — 🔴 BLOCKER — Equipment hallucination; character runs with an unscheduled back tank, violating suit spec.

## DETAILED ERROR LOG
0:02.5 — 🟠 MAJOR — Camera — Camera tracks rover; violates fixed lockoff rule.
0:06.0 — 🔴 BLOCKER — Particles — Fire hallucination from rover exhaust.
0:15.0 — 🔴 BLOCKER — Camera — Unplanned in-scene cut during restricted S1.
0:20.0 — 🔴 BLOCKER — Environment — Wall exhibits severe waterfall effect.
0:23.0 — 🔴 BLOCKER — Camera — Unplanned cut; notch beat occurs early.
0:33.0 — 🟠 MAJOR — Physics — Thrown rocks fall too fast (~1g, not 0.28g).
0:48.0 — 🔴 BLOCKER — Character — Severe face morphing/aging.
1:06.0 — 🔴 BLOCKER — Particles — Visible flames inside rover vent grid.
1:35.0 — 🔴 BLOCKER — Lighting — Wall crest illuminated by fire, not rim light.
1:42.0 — 🔴 BLOCKER — Character — Unscheduled back tank appears on suit.
2:04.0 — 🔴 BLOCKER — Negative — Burned-in text overlay appears over live action.

## WHAT WORKED WELL
- The initial 16:9 framing and overall color palette attempt to match the matte brick-red and pale visual aesthetic.
- The 1/8 mirror counter at S0 was executed well before timing degraded.

## PROMPT IMPROVEMENT SUGGESTIONS
1. ADD: "dry granular dust avalanche, zero water, zero liquid" → prevents [waterfall hallucination].
2. REMOVE: "exhaust, thruster, engine burn" → causes [fire hallucinations in vent/wheels].
3. REPLACE "cinematic tracking shot" with "locked-off tripod camera, static frame" → prevents [unplanned camera drift].

## NEW LESSON CANDIDATE
No new lesson — all errors map to existing failure patterns 1, 2, 3, 5, 6, 7, and 11.

## QUALITY TABLE ROW
| THE DAWN FRONT | Compilation | 4 | 3 | 3 | 4 | 4 | N/A | 5 | 4/10 |

---

> ⚠️ **Arşiv notu (raporun kendisine ait değil):** Raporda iç çelişki var —
> süre 141 s (plan ±1 s) bildiriliyor, ama sahne tablosu 6 sahneyi
> "Present: No" işaretliyor. 14 slotluk bir kurguda 6 sahne gerçekten yoksa
> süre ~80 s olurdu. Muhtemel okuma: slotlar dolu ama İÇERİK planla
> eşleşmiyor (beat kaybı), "yok" ifadesi sahne değil beat düzeyinde.
> Sahne-varlık bulguları kurgu elle doğrulanmadan kesin sayılmaz.
> "REMOVE: exhaust, thruster, engine burn" önerisi de yanlış hedefe atıyor —
> bu kelimeler 28 promptun hiçbirinde yok (plan §0.9, Ders 56+59 uygulandı).
> Model yine de ateş üretti → Ders 67'nin kanıtı.
