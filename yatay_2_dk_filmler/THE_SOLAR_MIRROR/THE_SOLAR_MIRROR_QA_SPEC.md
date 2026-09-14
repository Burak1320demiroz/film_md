# 📊 THE_SOLAR_MIRROR — QA SPECIFICATION

> **Kaynak:** `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §1 · `DERSLER/08_QA_SURECI.md`

---

## BLOCK A — AUDIENCES AND METRICS

- **TARGET FORMAT:** `yatay_2_dk_filmler` (16:9)
- **TARGET RUNTIME:** 160.0 s (120.0 s scenes + 40.0 s title/credits)
- **TARGET ASL BAND:** 8.0 s – 12.0 s
- **TARGET ASL CURVE:** Linear baseline (10.0 s average per scene)
- **CLIP COUNT:** 12 clips
- **SHOT COUNT:** 12 shots

---

## BLOCK B — STORY AND DIALOGUE TIMELINES

- **FORMULA VERIFIED:** `T_event = S0_duration + sum(S_i)` [D122]
  - S00 Dialogue (Telsiz): 00:05.0 s
  - S03 Dialogue (Parazit): 00:55.0 s
  - S05 Doruk Saat: 01:13.0 s (RCS crossfeed lever pull)
  - S06 Real-Time T-00: 01:22.0 s (Thermal ray hit)
  - S07 Dialogue (Telsiz): 01:25.0 s
  - S10 Fan Stop: 02:10.0 s (Breathing ceases)

- **FINAL VURUŞ KANITI [D141]:**
  - S11 final karesinde (02:25.0–02:40.0 s) mutlak kask içi sessizlik (0.0 dB audio stream), suit fanının ve nefes ritminin tamamen sıfırlanması, EWS kadrajında serbest süzülen 1 adet tekil astronot silueti.

---

## BLOCK C — VISUAL AND OPTICAL SPECIFICATIONS

- **ASPECT RATIO:** 16:9 (1920×1080)
- **LENS SYSTEM:** 35mm anamorphic prime lens profile
- **BLOOM LIMIT:** 0% bloom, zero soft focus glow filter
- **VISOR TRANSPARENCY:** 100% optically clear zero-tint glass across all 12 scenes (D197)
- **PHYSICS ENGINE:** Vacuum microgravity, zero-g continuous linear momentum (D198)

---

## BLOCK E — MACHINE GATES AND DRY RUN VERIFICATION

```bash
# Gate 1: Aspect ratio verification
ffmpeg -hide_banner -i video.mp4 -vf "cropdetect" -frames:v 100 -f null - 2>&1 | grep -q "crop=1920:1080"
# DOĞRULANDI (ffmpeg 6.1.1 2026-09-10)
# İKAME: ffprobe -v error -select_streams v:0 -show_entries stream=width,height

# Gate 2: Audio silence verification on final scene (S11)
ffmpeg -hide_banner -ss 02:25 -to 02:40 -i video.mp4 -af "volumedetect" -f null - 2>&1 | grep -q "max_volume: -91.0 dB"
# DOĞRULANDI (ffmpeg 6.1.1 2026-09-10)
# İKAME: silencedetect filter
```
