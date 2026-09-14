# 🎶 LOOK_UP — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
İzleyici bu novum'u basınçlı yörünge istasyonunda mikro yerçekimi kuşatması ve klostrofobik kurtarma gerilimi olarak okumalı.

TEMPO:        96 BPM (10 saniye sahne süresi = 4 ölçü / 16 vuruş at 96 BPM)
SÜRE:         120 s
MÜZİKSİZ SAHNE: S01 (00:00–00:04 sn açılışta yalnızca ortam fanı, kask nefesi ve pençe tıkırtısı)
SUB-BASS:     45 Hz + 90 Hz oktav eşlikçisi (telefon ve kulaklık uyumluluğu için)
VURUŞ NOKTASI: 3 vuruş noktası — 00:10 (S02 ilk darbe), 01:00 (S07 Mara'nın kapı kararı), 01:30 (S10 kapı kapanışı)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google MusicFX / Suno V4 / Udio
GENRE: Cinematic Sci-Fi Atmospheric Tension & Suspense
TEMPO: 96 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low industrial station drone and metallic pulse
  2. Staccato dark cello ostinato
  3. Sub-bass pulse (45 Hz with 90 Hz octave harmonic)
  4. Metallic percussive ticks and rhythmic tension pads

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  00:00-00:10 s (S01): Minimal ambient drone, focus on dialogue and claw click
  00:10-00:30 s (S02-S03): Metallic percussive pulse enters, driving tension
  00:30-00:50 s (S04-S05): Slower rhythmic hits build as flanking occurs
  00:50-01:00 s (S06): High tension drone sustained during snagged line
  01:00-01:10 s (S07): Music thins down, emotional low bass note for Mara's decision
  01:10-01:30 s (S08-S09): Rhythmic drive returns building to elevator entry
  01:30-01:40 s (S10): Peak percussive intensity climax on door slam
  01:40-01:50 s (S11): Soft resolving ambient texture, breathing space
  01:50-02:00 s (S12): Music fades out on overhead metallic clicks, ending in silence

SYNC RULE: Every 10-second scene boundary aligns with a 4-bar measure boundary at 96 BPM.

MIX: Mono-compatible low end, center panned bass. Target -14 LUFS, -1.0 dBTP.

NO vocals, NO lyrics, NO brass fanfares, NO braam, NO reversed cymbal, NO whoosh.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     H (Human helmet comms with mild Band-Pass filter)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare · diyalog altında müzik −6 dB
KATMAN TABLOSU:
  S01: Ortam fanı | Kask nefesi | Pençe tıkırtısı | Replik (3 katman)
  S02: Ortam fanı | Çarpma ve kilit kopması | Carbine atışı | Replik (4 katman)
  S03: Ortam fanı | Pençe tıklamaları | C10 şaft motifi | Replik (4 katman)
  S04: Ortam fanı | Carbine atışı | Kordon kilit sesi | Replik (4 katman)
  S05: Ortam fanı | Stereo pençe sesleri | Kalkan darbesi | Replik (4 katman)
  S06: Ortam fanı | Bot kilit mekanizması | Kordon gerilimi | Replik (4 katman)
  S07: Ortam fanı | Kapı motoru | Makara kilitleme | Replik (4 katman)
  S08: Ortam fanı | Kalkan saptırma darbesi | Tether carabiner tıkırtısı | Replik (4 katman)
  S09: Ortam fanı | Kordon kesici sesi | Makara çekişi | Replik (4 katman)
  S10: Ortam fanı | Kapı motoru | Kalkan sürtünmesi | Replik (4 katman)
  S11: Kabin yükselme motoru | Kabin fanı | Kask nefesi | Replik (4 katman)
  S12: Kabin fanı | Üç dikey çatı tıkırtısı | Kask fısıltısı | Replik (3 katman)

REPLİK SAYISI: 12 replik (Sahne başına kesin 1 replik)
REPLİK ZAMANLARI:
  S01: 00:05s — Noah: "Above us!"
  S02: 00:14s — Mara: "Lock your boots!"
  S03: 00:22s — Mara: "Get the lift open."
  S04: 00:36s — Mara: "Together. Move."
  S05: 00:44s — Cole: "They're flanking us."
  S06: 00:57s — Noah: "I'm caught!"
  S07: 01:05s — Mara: "Hold my line."
  S08: 01:14s — Mara: "Eyes on me."
  S09: 01:27s — Eren: "All five. Close it!"
  S10: 01:34s — Mara: "Push!"
  S11: 01:47s — Noah: "We made it."
  S12: 01:52s — Mara: "Nobody move."
```
