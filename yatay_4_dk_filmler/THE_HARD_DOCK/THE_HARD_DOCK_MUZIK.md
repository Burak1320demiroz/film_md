# 🎶 THE_HARD_DOCK — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
İzleyici bu novum'u "yalpalayan istasyona yumuşak kenet imkânsız; halka bir daha açılmamak üzere porta sürülür — röle yaşar, gemi kalır" olarak okumalı.

TEMPO:        96 BPM (10s sahne ile 16 barlık mükemmel ölçü eşleşmesi)
SÜRE:         240 s (04:00)
MÜZİKSİZ SAHNE: S22 · S23 · S24 — müzik DORUKTAN ÖNCE, S21'in sonunda (3:30) susar [YANASMA §2.1 · müzik §10];
              temas (S22 6,0 s) yalnız telsiz yatağı + tutulan nefesle; S24 çözülme akoru YOK — insan sahnesi sessiz biter
SESSİZLİK GEREKÇESİ: diegetik — makine "guidance withdrawn" dedikten sonra kalan tek şey telsiz taşıyıcısı ve nefes
SUB-BASS:     40 Hz + 120 Hz oktav eşlikçisi (Telefon ve hoparlör uyumlu)
VURUŞ NOKTASI: 3 — S06 oran karesi (0:50) · S14 gezegen (2:10) · S19 karar (3:00); temas (S22) müziksizdir
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: MusicFX / Suno v3.5
GENRE: Cinematic Industrial Sci-Fi Tension / Space Dark Ambient
TEMPO: 96 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low analog synth drone with rhythmic sub-bass pulse (40Hz + 120Hz octave)
  2. Cold metallic resonant synthesizer pads with slow pitch bend modulation
  3. Staccato industrial pulses mimicking mechanical pressure gauges

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  00:00-00:40 s (S01-S04): low drone with metallic resonance, no pulse yet
  00:40-01:20 s (S05-S08): the 96 BPM sub-bass pulse enters at 0:50 (S06 wide shot), builds
  01:20-02:00 s (S09-S12): pulse plus staccato pressure-gauge pulses; falls away at 1:55 (wave-off)
  02:00-03:00 s (S13-S18): drone only, slowly darkening; pulse returns thin at 2:40 (abort line)
  03:00-03:30 s (S19-S21): pulse and bassline rise to the loudest point of the piece
  03:30 s (end of S21): COMPLETE CUT — the piece ends here; S22-S24 carry no music at all

SYNC RULE: Musical bar lines match 10-second scene transitions exactly at 96 BPM (16 bars per scene). Total music length 210 s; hard stop at 3:30, no tail, no reverb ring-out.

MIX: Mono compatible, low end centered. Target -14 LUFS, -1.0 dBTP.

NO vocals, NO lyrics, NO acoustic drums, NO EDM drop, NO braam, NO reversed cymbal.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     MACHINE (MIRA gemi bilgisayarı — akuzmatik, kabin hoparlörü/telsiz; bedenleştirme YOK)
REPLİK SAYISI: 8 (HUMAN 0)
REPLİK ZAMANLARI (formül: (n−1)×10 + klip ofseti [D122]):
   S02: 00:13   "Station wobble confirmed. One full cycle every forty-eight seconds."
   S03: 00:23   "Relay carrier lost."
   S06: 00:53   "Coronal flux rising. Sensor confidence fifty percent."
   S10: 01:33   "Capture window six seconds per cycle."
   S15: 02:23   "Sensor confidence zero. Guidance withdrawn."
   S17: 02:43   "Abort approach. Return burn available for ninety seconds."
   S24: 03:52   "Hard capture confirmed. Release struts destroyed."
   S24: 03:57   "Relay carrier restored."
YATAK ENVANTERİ [D83]: kabin fanı (iç sahneler) · telsiz taşıyıcı hışırtısı (tüm film, tek parça serilir) ·
   kabin uyarı tonu iki tonlu, 2 s'de bir (S01-S23; S24'te yok) · nefes kaskın içinde · vakumda dış ses 0
   ⛔ Temas bölgesi (3:36) kulakla dinlenir: mutlak dijital sıfır YOK — taşıyıcı hışırtısı sürer
```

