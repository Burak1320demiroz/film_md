# 📋 BENI_HATIRLAMA — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar ve BU dosyayı rubriğin BAŞINA yapıştırır.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `BENI_HATIRLAMA_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (klipte 0 replik · post-dub kayıt sesi ·
> sabit lockoff · tasarımlı sessizlik · metinsiz sayaç · yarı saydam figür) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → C BLOĞU İNSAN · KASK · NOVUM · ATKI · CANLI satırları (tasarım duvarı)   MOD D
③ 🔊 SES         → A BLOĞU DIALOGUE/POST-DUB + C SES REGISTER (post kayıt sesi bant-geçiren, MACHINE)
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]: DÜNYA ÇAPASI · IŞIK TAKVİMİ · EKRAN YÖNÜ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C HAREKET KİLİDİ  MOD D
⑮ 🧭 YÖN         → C BLOĞU EKRAN YÖNÜ + A  MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              BENI_HATIRLAMA
FORMAT:            horizontal 8 min · 48 scenes · written in 4 files of 12 (BOLUM_1-4)
RUNTIME:           480 seconds ASSUMED (48 × 10 s clip — clip length not yet measured with ffprobe) (title card: none — screen text lock 0 s)
SCENE COUNT:       48
PART GRID:         K1 PROPOSAL (owner decision pending) — QA unit = QUARTER, `rapor_kontrol.py --bolum n/4`:
                   B1 = S00-S11 · 12 clips · 0-120 s  |  B2 = S12-S23 · 12 clips · 120-240 s
                   B3 = S24-S35 · 12 clips · 240-360 s  |  B4 = S36-S47 · 12 clips · 360-480 s
                   Rubric gets "THIS FILE IS PART n OF 4 — scenes Sx-Sy" pasted with this SPEC.
                   BOUNDARY PAIRS S11↔S12 · S23↔S24 · S35↔S36 are closed by hand with frames.
                   (If the owner picks halves instead: B1 = S00-S23 · 0-240 s | B2 = S24-S47 · 240-480 s, --bolum n/2.)
THEME:             IDENTITY
THEME SENTENCE:    loving someone means not dressing someone else in their face
THEME SCENES:      S9 · S15 · S28 · S30 · S37 · S39 · S47
INTENDED EMOTION:  grief turning to awe (quiet sorrow → wonder at S32 and S46-S47)
ENDING TYPE:       AMBIGUOUS with an early twist (the woman is the creature's projection, S10-S11); ONE open question:
                   will the recorded voice ever be played again? (S45 the device goes into the pocket, unplayed)
PROTAGONIST:       unnamed suited man — bone-white pressure suit, no personal name anywhere
CENTRAL CHOICE:    S36 — he plays the first recorded line himself and this time closes his eyes
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0   (no speech is generated inside any clip)
POST-DUB LINES:    6 · MACHINE 6/6 — one recorded adult female voice, band-limited like a small speaker:
                   S2 0:22.0 · S8 1:21.5 + 1:23.3 · S12 2:03.0 · S36 6:03.0 · S38 6:22.0 (Turkish; subtitle language per YAYIN_PAKETI)
                   ⛔ no mouth is ever on screen for these lines — voice from the device or from the figure's direction
SILENT SCENES:     all clips carry no speech; S37 is music-less (breath + cave hum stay; no digital silence)
VIRAL INTERSTITIALS: S1 · S44  ⛔ THESE MAY NOT BE CUT (also uncuttable: S0 hook · S15 novum still · S30 · S36 · S37 · S47)
TITLE:             "Close Your Eyes, Dad" — promises the father's eyes and the game: refused at S8, done at S36
LIBRARY CONTEXT:   MARS_SON_CIKIS (8-min format, part-grid friction) · THE_HERD (thick atmosphere, helmet drift) ·
                   THE_COUNTED_TURN (face gender drift) · THE_HEALING_GROUND (cost image froze the after-state) ·
                   THE_ROSE_COAT (forbidden ladder climb, undeclared novum flagged) · LOW_POWER · THE_HARD_DOCK (rhyme broke)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      48 (+3 standby versions for S37 — exactly ONE S37 clip enters the cut)
SHOT COUNT:      48 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s   ASL CURVE: flat
                 GEREKÇE [D74]: 48 tek-klip I2V lockoff; ritmi kesme sıklığı değil kurulum iskeleti (3 küme · %48 dönüş)
                 ve ses köprüleri taşır. Sert kesme yalnız S10→S11 (lens tık) · S37→S38 (sessizlik→kayıt) · S43→S44.
GRID:            scene start(n) = n × clip · clip = 10 s assumed · S0 is the hook and sits INSIDE the grid
                 ⛔ clip length ffprobe ile ölçülmedi (⬜ D124) — ölçüm gelince bütün saniyeler aynı formülle yeniden
RUNTIME:         480 s assumed
RAW FOOTAGE:     48 accepted clips · TRIM BUDGET: 0 s (fixed grid)
SCREEN TEXT:     0 seconds
CAMERA:          48 / 48 fixed lockoff (in-clip camera movement 0)
SETUP SEQUENCE:  21 setups — A 35mm MLS low · B 24mm WS eye · C 50mm MCU eye · D 50mm CU high · E 35mm MS OTS · I heat POV WS ·
                 J heat POV MS · Y heat POV CU · L 24mm WS eye · M 35mm MS profile · Q 24mm WS low · S 50mm CU eye ·
                 Z 24mm EWS low · P 50mm MCU eye · X 35mm MS eye · N 50mm CU eye · T 24mm WS high · U 85mm MS OTS ·
                 V 50mm MCU profile · W 50mm ECU high · F 50mm CU low
KURULUM İSKELETİ: A C E D D E C E C E I J B E Y E B E B E L L M Q M L M S M S M L Z L M P X X P M N M T U V W F A
KÜME:            3 · S3-S4 · S20-S21 · S36-S37 (each second clip carries the "continues the previous clip" line)
DÖNÜŞ:           23/48 = %48 (S4 S5 S7 S8 S9 S13 S15 S16 S17 S18 S19 S21 S24 S25 S26 S28 S29 S30 S33 S34 S37 S38 S41)
ANGLE ARC:       6 types — low · eye level · high · over-the-shoulder · profile · POV (heat view)
DORUK:           S37 → the figure thins away (scene start 370 s) · ACTION PEAK S44 (440 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = n × klip + promptun TIMELINE ofseti   (hook S0 ızgaranın içinde)
   S2 = 20 + 2,0 = 22,0 · S8a = 80 + 1,5 = 81,5 · S8b = 80 + 3,3 = 83,3 · S12 = 120 + 3,0 = 123,0 · S36 = 360 + 3,0 = 363,0 · S38 = 380 + 2,0 = 382,0
   (post-dub konum saniyeleri; klipte replik yok — klip ölçülünce formül yeniden koşar)

FİNAL VURUŞ KANITI [D141]:
   yellow wool scarf ×1 + amber lights ×2 · at 476 s (S47 + 6 s) · BULUNAN (present) · human 0 · woman figure 0
   ffmpeg -ss 476 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: first frame S0 ↔ last frame S47 — same setup A (35mm · 0.5 m · 4 m · MLS · low angle) · same scale ·
   light DELIBERATELY different (grey day ↔ amber cave) · the scarf in the right third in both · jest: scarf end lifting in both
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  -111111111--11-1111111111111111111111111111111--
       (1 = suited man in frame · - = no human: S0 figure only · S10 · S11 · S14 heat POV · S46 · S47)
GÖRÜNTÜ ŞERİDİ (ayrı şerit — figür İNSAN ŞERİDİNE SAYILMAZ · THE_ROSE_COAT dersi):
       1-1--1-1-11111-1111---------1----11-11----------
       (1 = semi-transparent woman figure or her heat outline in frame · after S37 always -)
VARLIK ŞERİDİ (K0-K4): 000000000024022313111132333231331331331443010023
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         exactly 1 suited man (İNSAN ŞERİDİ) · woman figure ≤1 (GÖRÜNTÜ ŞERİDİ) · third figure 0 in every clip
KASK          closed 48/48 · hard off-white shell, ONE flat front pane in a thick dark-grey rim, deep brushed-steel collar ring,
              2 small square brow lamps + 1 small dark round heat lens · visor optically clear · back one continuous sculpted
              surface, flat silhouette, no back unit [D79] · no reference package (owner decision) → any helmet shape drift is a
              REAL fault (R2), not a design choice
NOVUM         NOT A FAULT — a semi-transparent, helmetless woman figure in her late twenties (rock/sand visible through her at about
              half strength · no footprints · no contact shadow · wind-blown sand passes through her · pale colourless outline in
              the heat view) is the injured young creature's projection of the man's memory; holding it drains the creature's
              light. It thins away from the edges at S37 and is ABSENT from S38 on. Violated: opacity and physics, ONLY for her.
              ⛔ may NOT be written as clone / second human / ghost effect / glitch · ⛔ a figure visible after S37 IS a fault ·
              ⛔ her face is never shown (0 frames) — a visible face IS a fault
YERÇEKİMİ     ≈0.7 g ("about two thirds of Earth's weight") · dropped case ≈0.5 s to the sand (S1)
ATMOSFER      ≈3 atm, thick · wind slow but pushing · sand in low streaks, settles in 2-3 s, never hangs · no long shadows (diffuse)
EKRAN YÖNÜ    lander always screen-LEFT · rock outcrop / crack always screen-RIGHT · man LEFT, figure RIGHT in 15/15 two-figure
              scenes · wind and sand streaks left→right · S12 man walks BACKWARD toward screen-left facing right · S16 turns
              left-right-left then walks right · S42 walks right→left toward the lander lamps · cave: shaft mouth upper-left,
              creature lower-right in 22/22 cave scenes · cockpit window screen-left
HAREKET KİLİDİ  S1 the case slips and drops — one gesture · S5/S16/S19 "His right palm presses flat on the chest pocket flap twice."
              · S17 glove stops a palm short, no touch · S29 palm rises to the flap WITHOUT pressing · S30 fingers open one at a
              time · S36 slow press + helmet bows + shoulders drop and stay down · S41 second pull slower than the first ·
              S45 palm flat on the pocket flap
SAYAÇ         right-wrist lamps 5 (S0-S5) → 4 (S6) → 3 (S26) → 1 (S35) → 0 (S44) · monotonic · changes ONLY at cuts · device has no screen
EŞ KADRAJ     S0↔S47 (A, rhyme) · S3↔S4 · S20↔S21 · S36↔S37 (split single shots)
DÜNYA ÇAPASI  3/3 — sky "a low, still cloud deck" · horizon "a long dark storm wall on screen-left behind the lander, rock outcrop
              screen-right" · ground "a dark sand plain, fist-sized dark stones half-sunk in the sand" [D209] · storm wall grows
              ONLY at cuts (S6 · S16 · S42)
YIPRANMA      suit grit global in 3 steps: F1 light (S0-S17) → F2 heavier at knees (S18-S41) → F3 helmet to boots (S42-S45) · never goes back [D42]
KİMLİK DİZİSİ helmet closed in every man scene · slate-blue band LEFT upper arm + LEFT thigh · suit bone-white · grit F2 from S18 ·
              damage none · right wrist lamp ring · left wrist round device (S3-S34), in hand S34-S45, in pocket S45 [D208]
IŞIK TAKVİMİ  surface MONOTONIC darkening S0 → S6 → S12 → S16 → S19 → S42-S43 darkest ✅ · cave declared CURVE (not a fault):
              L1 brow lamps on, veins dark S20-S24 · L2 lamps off, creature's low amber only S25-S30 · L3 veins lit and staying lit,
              creature light varying S31-S41 · L4 + one soft pale daylight patch S46-S47 · creature light level curve in 03 §2b
SES REGISTER  HUMAN 0 · MACHINE 6 (post-dub) · wordless warble S6 · S26 · S35 (MACHINE) · creature: organic pitched seal-pup breath
ATKI          yellow wool scarf: on the figure S0-S28 · in his pocket S4 / S29 · on the creature S30-S47 · ≤1 scarf in frame always ·
              figure WITHOUT scarf from S33
CANLI         anatomy counts (6 legs · 2 eyes · 3 membranes) only S11 (heat) · S39 · S40 · dark patch on its LEFT flank (mirroring = fault)
              · large creature S46 = light + two limbs only, two full forms never together
İNSANSIZ      S14 · S46 · S47 — Style line instead of a long negative list (red log YR)
```

### 👁️ F — GÖZ KAPILARI (elle kare · makine ölçemez)

```
F1 FACE      S1 = S6 = S8 = S35 = S38 = S44 — same man, late fifties, grey stubble; a smooth or female face IS a fault (COUNTED_TURN ②)
F2 FIGURE    woman figure face 0 frames · head above frame top in M/X cave setups · figure count ≤1 · none after S37
F3 S37       she thins edge-first, NO fragments/dust/particles, the rock appears through her · single figure throughout
F4 SCARF     count ≤1 in every frame (S28-S37 checked frame by frame)
F5 HELMET    one flat pane in a thick dark rim in S1 · S36 · S38 · S44 (no dome, no bubble)
F6 ORIENT    creature patch on the LEFT flank in S11 · S14 · S15 · S39 (mirror check)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Filtre varlığı 17.09.2026'da bu makinede ölçüldü (ffmpeg 8.1 · `ffmpeg -hide_banner -filters`).
> ⚠️ `vidstabdetect` KURULU DEĞİL — kamera sabitliği ona yazılmadı.

```
KAPI          clip length / grid (D124) — every accepted clip's duration; the GRID and every post-dub second depend on it
KOMUT         for f in S*.mp4; do printf "%s " "$f"; ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"; done
DOĞRULANDI    ffprobe 8.1 · 17.09.2026 (tool present; no clip yet)
İKAME         —

KAPI          cut grid — cuts in the master fall only on n × clip (48 scenes → 47 cuts)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "scdet=threshold=10,metadata=print" -f null - 2>&1 | grep -o "lavfi.scd.time=[0-9.]*"
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filter scdet present
İKAME         -vf "select='gt(scene,0.3)',showinfo" (select + showinfo present)

KAPI          light calendar — mean luma per scene midpoint; surface S0-S19 must fall monotonically, cave follows declared L1-L4 curve
KOMUT         for n in $(seq 0 47); do t=$((n*10+5)); ffmpeg -v error -ss $t -i "$M" -frames:v 1 -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | tail -1; done
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filter signalstats present
İKAME         —

KAPI          loudness and the S37 music-less window — master −14 LUFS / −1 dBTP; 370-380 s no music, breath bed stays above digital silence
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12 ; ffmpeg -ss 370 -t 10 -i "$M" -af silencedetect=n=-60dB:d=0.5 -f null - 2>&1 | grep silence_
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filters ebur128 + silencedetect present
İKAME         astats (present)

KAPI          frozen clip — a held-stillness scene must not freeze (S15 · S22 · S31 · S32 · S39 · S47 keep breath/light/scarf motion)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=0.003:d=4" -map 0:v -f null - 2>&1 | grep freeze_
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filter freezedetect present
İKAME         mpdecimate (present)

KAPI          black frames — black allowed only after S47 (cut to black at the end)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.2:pix_th=0.10" -an -f null - 2>&1 | grep black_start
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filter blackdetect present
İKAME         —

KAPI          in-clip camera stillness (lockoff) — frame difference inside a clip comes only from the subject
KOMUT         ffmpeg -v error -ss 25 -t 10 -i "$M" -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | tail -3
DOĞRULANDI    ffmpeg 8.1 · 17.09.2026 · filters tblend + signalstats present (vidstabdetect NOT installed — not used)
İKAME         hand check of first/last frame edges on the rock/horizon lines
```
