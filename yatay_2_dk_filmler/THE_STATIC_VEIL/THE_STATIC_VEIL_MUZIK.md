# 🎶 THE_STATIC_VEIL — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ:
   "İzleyici bu novum'u sessiz, kaçınılmaz bir körlük ve doğanın dielektrik yabancılığı olarak okumalı."

TEMPO:        72 BPM — 10.0 s sahne uzunluğuna tam hizalı (her sahne 12 vuruş = 3 ölçü)
SÜRE:         120.0 s = filmin RUNTIME'ı (12 sahne × 10.0 s)
MÜZİKSİZ SAHNE: S00 (0.0s-10.0s · açılış vakum sessizliği) ve S09 (80.0s-90.0s · doruk arkı ve batarya vuruşu)
SUB-BASS:     45 Hz temel frekans + 90 Hz ve 135 Hz harmonik eşlikçileri (telefon hoparlörü uyumlu)
VURUŞ NOKTASI: 3 vuruş:
              1. Vuruş: 20.0s (S02 başı · vizörün ilk çizilişi)
              2. Vuruş: 80.0s (S08 sonu / S09 başı · müziğin aniden kesilişi ve mutlak sessizlik)
              3. Vuruş: 100.0s (S10 sonu · fenerin kilitlenişi ve sıcak bas rezonansı)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow / Suno Audio Engine
GENRE: Cinematic Atmospheric Sci-Fi Drone / Minimalist Space Ambient Soundscape
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low bowed metallic cello drone (warm, non-melodic, continuous bowed texture)
  2. Deep 45 Hz sub-bass sine tone with 90 Hz harmonic overtones
  3. Cold crystalline glass drone (high-frequency bowed glass resonance at 4 kHz)
  4. Subtle granular electrostatic noise texture band-pass filtered between 2 kHz and 7 kHz
  5. Distant, rounded sub-bass pulse marking the 72 BPM grid

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0.0s - 10.0s (S00): MUTE. Absolute score silence. Only diegetic low-frequency seismic ground rumble.
  10.0s - 30.0s (S01-S02): Low 45 Hz drone and bowed cello fade in softly; high glass resonance enters at 20.0s.
  30.0s - 60.0s (S03-S05): Gradual claustrophobic build; granular electrostatic noise texture rises gently.
  60.0s - 80.0s (S06-S08): Mid-range thins out leaving a hollow, tense drone; bass pulse slows to a halt.
  80.0s - 90.0s (S09): MUTE. Sudden score cut to absolute zero; only diegetic vacuum impact and arc discharge.
  90.0s - 110.0s (S10): Deep, warm sub-bass swell re-enters smoothly as the beacon latch engages.
  110.0s - 120.0s (S11): Low resonant sustaining chord decaying slowly into cold vacuum silence.

SYNC RULE: Complete silence at 80.0s sharp; re-entry at 90.0s sharp on low sub swell.

MIX: Mono-compatible low end, 45 Hz centered with zero stereo widening below 120 Hz. Target −14 LUFS, peak −1.0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     Human 0 / Machine 0 (0 replik, tamamen diegetik ve fiziksel ses tasarımı)
KATMAN TAVANI: Sahne başına aktif katman ≤ 4 · oda tonu / kask içi solunum köprüsü ≥ 0.2 s
KATMAN TABLOSU:
  | sahne | katmanlar (ad) | sayı | köprü |
  |---|---|---|---|
  | S00 | Sismik zemin uğultusu, mikro toz sürtünmesi | 2 | 0.4s |
  | S01 | Kask içi regüle solunum, bot darbe titreşimi | 2 | 0.3s |
  | S02 | Kask içi solunum, kask camı çizilme gıcırtısı, bot sürtünmesi | 3 | 0.3s |
  | S03 | Hızlı solunum, zemin rayı eldiven temas tıkırtısı | 2 | 0.3s |
  | S04 | Kask içi solunum, pilon rüzgarsız zemin titreşimi | 2 | 0.3s |
  | S05 | Hızlı çalışan solunum, çelik tırnak sürtünmesi, eldiven gerilimi | 3 | 0.3s |
  | S06 | Kesik solunum, göğüs mandalı metalik açılış tıkırtısı | 2 | 0.3s |
  | S07 | Kask içi solunum, mikro kıvılcım çıtırtısı (0.1s) | 2 | 0.3s |
  | S08 | Derin tereddütlü soluk, batarya yuva tırnağı yay sesi | 2 | 0.3s |
  | S09 | Sert metalik şasi çarpması, 0.3s elektrik ark vızıltısı, telemetri sönüşü | 3 | 0.3s |
  | S10 | Ağır solunum, fener soketi döner kilit 'klik' sesi | 2 | 0.3s |
  | S11 | Yavaşlayan sakin solunum, düşük frekanslı fener güç uğultusu | 2 | 0.5s |
REPLİK SAYISI: 0
REPLİK ZAMANLARI: Yok (repliksiz dramaturji)
```
