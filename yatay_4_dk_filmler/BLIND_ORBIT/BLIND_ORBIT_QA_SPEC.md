# 📋 BLIND_ORBIT — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar ve BU dosyayı rubriğin BAŞINA yapıştırır.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `BLIND_ORBIT_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (konuşan ağız 0 · sabit
> lockoff · 9 insansız klip · kara ekran) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → B BLOĞU sahne içi kesmeler + C  MOD D
③ 🔊 SES         → A (DIALOGUE LINES) + C SES REGISTER   MOD D
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi (DÜNYA ÇAPASI · IŞIK TAKVİMİ · EKRAN YÖNÜ) [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + bölüm promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A + C HAREKET KİLİDİ             MOD D
⑮ 🧭 YÖN         → C EKRAN YÖNÜ + A                 MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              BLIND_ORBIT
FORMAT:            horizontal 16:9 · 4 minutes · 24 clips × 10.0 s · 2 part files
RUNTIME:           240 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       6        ⛔ SCENE COUNT ≠ CLIP COUNT — see B BLOCK SCENE PLAN
PART GRID:         — (2 part files are a WRITING split, not a QA split: this film is
                   measured as ONE 240 s master. The 4-minute line has no PART QA.)
THEME:             TRUST — "in the last metres you cannot see, someone else's eye becomes
                   your eye"
THEME SCENES:      S02 · S03 · S04 · S05 · S06
INTENDED EMOTION:  held breath released into relief — the pilot gives up her own eyes
                   and the ship docks on a voice
ENDING TYPE:       ENDS — the small ship is joined to the station, carried home with it,
                   and the pilot's hand opens
PROTAGONIST:       an unnamed pilot, sealed suit, left seat (no proper name appears in
                   any prompt [D34]); SECOND HUMAN: an unnamed flight engineer, right
                   seat, then alone in the optical bay — mostly off screen as a voice
CENTRAL CHOICE:    K18 — her thumb stops short of its habitual double press, her glove
                   loosens and she steers on his voice instead of her eyes (S04)
                   FIRST SPLIT: K08 — he offers to shut the damaged bank; she holds the
                   grip for a full second before "Do it." (S02)
DIALOGUE LINES:    17 · register: HUMAN 13 / MACHINE 2 / RECORDED HUMAN 2
                   ⭐ No character speaks on camera in any clip: every line comes over a
                   helmet radio, a flight recording or a cabin speaker, from a speaker
                   who is off screen, seen from behind, or in another compartment.
                   Numbers are spoken ONLY by the machine voice (K04 · K22) [D82].
SILENT SCENES:     12 of 24 clips carry no speech at all
VIRAL INTERSTITIALS: 1 — K18  ⛔ MAY NOT BE CUT
UNCUTTABLE:        K01 · K15 · K18 · K20 · K21 · K23 · K24 [D62]
TITLE:             "Blind Orbit" — the title promises a docking done without sight; the
                   film shows the display going black and the gap closing on a voice
LIBRARY CONTEXT:   nearest shelf-mates: THE_HARD_DOCK (docking, visor clear, one pilot)
                   and THE_LAST_GATE (two suited people, microgravity, one PHYSICS
                   line). Both dock BY SIGHT; this one removes sight at K16 and gives the
                   last 20 metres to a second person's eye.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 18   (SHOT = CLIP; no cuts inside a clip)
SCENE PLAN:      SAHNE PLANI 2 6 4 6 4 2 = 24
                 S01 = K01-K02 · S02 = K03-K08 · S03 = K09-K12 · S04 = K13-K18 ·
                 S05 = K19-K22 · S06 = K23-K24
                 ⛔ SCENE COUNT 6 ≠ CLIP COUNT 24
INTRA-SCENE CUTS: K01|K02 · K03|K04 · K04|K05 · K05|K06 · K06|K07 · K07|K08 · K09|K10 ·
                 K10|K11 · K11|K12 · K13|K14 · K14|K15 · K15|K16 · K16|K17 · K17|K18 ·
                 K19|K20 · K20|K21 · K21|K22 · K23|K24 — these cuts are INSIDE one
                 scene and often cross between outside and inside the ship: the LIGHT
                 line, the PHYSICS line and the first AUDIO sentence are identical across
                 them; ship damage, seat positions, display state and latch state MUST
                 match. A reset here is a ② CONTINUITY defect, not a scene change.
                 SCENE BOUNDARIES (a change here is legitimate):
                 K02|K03 · K08|K09 · K12|K13 · K18|K19 · K22|K23
TARGET ASL BAND: 10.0 s (fixed grid — no curve)   ASL CURVE: —
                 ⛔ GEREKÇE [D74]: 24 × 10.0 s module (§2.3); the cut may hold or trim and
                 that is measured at the edit gate, not here.
GRID:            clip(n) start = (n−1) × 10.0 s   (no hook offset — K01 starts at 0.0 s)
RUNTIME:         240.0 s
RAW FOOTAGE:     24 clips × 10.0 s = 240 s · TRIM BUDGET: 0 s (fixed grid)
SCREEN TEXT:     0.0 saniye — title card, end card and cover output INCLUDED
                 ⭐ Every display is abstract: one thin amber line for the reserve, a flat
                 grey or flat black rectangle for the docking display, a plain needle
                 dial on the wrist gauge, two etched cross-hair lines on the window.
CAMERA:          24 / 24 sabit lockoff — zero camera movement in every clip
                 (K15: the camera is the small ship's own hull camera — locked to the
                 ship, it turns with it; this is the novum shot, not a camera move)
KURULUM İSKELETİ: A B A C D C A C E F C F A C G C B H B I J B H A   (PLAN ile AYNI)
KÜME:            — (ÇOK KLİPLİ SAHNE rejiminde küme YOKTUR · ACI_YAYI §4b)
DÖNÜŞ:           10 / 24 = %41.7 (≥%40 ✅) — K03 K06 K07 K08 K11 K12 K14 K16 K19 K22
ANGLE ARC:       5 angle TYPES — eye level (A·G·H·I) · side-on profile (A) ·
                 over-the-shoulder (B·F) · high angle (C·J) · low angle (D·E)
DORUK:           K20 → K21 · S05 2/4 + 3/4 (clip starts 190.0 s · 200.0 s)
                 ⚡ DELIBERATE SHOCK CUTS: 1 (ceiling 2) — K20 (WS) → K21 (CU), the second
                 beat of the climax. Bölüm sınırı K12 (F · CU · inside) → K13 (A · EWS ·
                 outside): 3 steps + location.

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   line(K_n) = (n−1) × 10.0 + TIMELINE offset
   R1 K01 1.0 → 1.0 s       R2 K02 2.0 → 12.0 s      R3 K04 1.5 → 31.5 s
   R4 K04 5.0 → 35.0 s      R5 K06 6.0 → 56.0 s      R6 K08 1.0 → 71.0 s
   R7 K08 4.5 → 74.5 s      R8 K12 2.0 → 112.0 s     R9 K12 6.0 → 116.0 s
   R10 K16 4.0 → 154.0 s    R11 K17 7.0 → 167.0 s    R12 K18 1.0 → 171.0 s
   R13 K18 5.0 → 175.0 s    R14 K19 1.0 → 181.0 s    R15 K19 5.0 → 185.0 s
   R16 K22 0.5 → 210.5 s    R17 K24 3.0 → 233.0 s
   Doğrulandı: 17 tırnaklı replik, prompt TIMELINE ofsetleriyle formülden üretildi; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   four hook-shaped latches closed over the joined docking ring · 208.0 s · 4 adet · BULUNAN
   ⛔ sayılabilir ve adı konabilir: four latches, all closed, two separate rims
   ffmpeg -ss 208 -i "$M" -frames:v 1 kanit.jpg   → BAK
   + İLK↔SON (beden): K23 · 226.0 s — the pilot's right glove lies open on her thigh
   ffmpeg -ss 226 -i "$M" -frames:v 1 el.jpg
DÖNGÜ KANITI: K01 (0.0-10.0 s) ↔ K24 (230.0-240.0 s) — SAME setup A, same lens, distance,
   height and angle; the camera sentence carries "— the same position, height and lens as
   Clip 1." The ONE variable that changes: two hulls TOUCHING (K01, flash-forward) ↔ ONE
   joined body carried along under the station's engine light (K24).
   ffmpeg -ss 8 -i "$M" -frames:v 1 ilk.jpg ; ffmpeg -ss 238 -i "$M" -frames:v 1 son.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  -1-2-2-21111-1-1111--11-
       (1 = one human in frame · 2 = two humans · - = no human)
       ⚙️ MEASURED from the prompt bodies on 05.10.2026, not typed by hand.
       9 clips carry no human (K01 K03 K05 K07 K13 K15 K20 K21 K24) and that is BY
       DESIGN — see the FALSE-POSITIVE WALL. 12 clips carry exactly one human, 3 clips
       carry exactly two (K04 · K06 · K08 — the only shared cockpit frames).
       WHO: pilot only K11 K14 K16 K18 K23 · engineer only K02 K09 K10 K12 K17 K19 K22 ·
       both K04 K06 K08.

DAVRANIŞ ŞERİDİ (klip başına bir harf · KARAKTER_KARTI §4):
       G S G G D D B T G B R K R G S T G K R R R S R S
       G = task · T = hesitation · D = failed attempt · K = choice · B = cost ·
       R = reaction · S = stillness   (insansız klipler olay şeridiyle harflendi)
       G 6/24 · K'dan önce D/T · K'dan sonra R · ilk (G) ≠ son (S)

TEMPO ŞERİDİ (Y slow · N normal · H fast):
       Y Y N N Y H H Y N H N N Y N Y H H Y N Y H N N Y
       no three identical in a row · CHOICE K18 = Y between H (K17) and N (K19)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME KAPISI'nı besler:
> kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         exactly 1 in 12 clips · exactly 2 in 3 clips (K04 K06 K08) · exactly 0 in
              9 clips · body contact between the two: 0 frames
KASK          worn and sealed in 24/24 clips, opened in 0 clips · the visor is ONE FLAT
              front pane inside a THICK dark-grey rim, optically clear, zero tint, zero
              mirror, face fully readable through it (face on screen: K18 · K23 only) ·
              back is one continuous sculpted surface from collar to hip, no back-mounted
              unit — flat back silhouette [D79 · D139] — back in frame in 13 clips
              ⛔ the words seamless / bubble / dome never describe the helmet
NOVUM         RELATIONSHIP novum (no physics is broken): in the last metres the hand that
              steers the ship cannot see, and the eye that sees cannot steer — docking
              happens only when the two act as one.
              CARRIER: the docking collar in the cross-hairs of the small round window ×
              the engineer's visor at the glass and his two raised fingers ↔ the pilot
              turning from the black docking display and loosening her glove on the grip
              → the gap between collar and latches closes (K17-K20).
              THE STATION'S SPIN (1 numaralı risk): one full turn every 40 s = a quarter
              turn per 10 s clip. K15 is the proof frame: the station's face and fins
              HOLD STILL while the black hole behind them turns a quarter of the way
              round, in one direction, never reversing.
YERÇEKİMİ     0 g — orbital free fall inside and outside, one PHYSICS line in 24/24 video
              prompts. Nobody walks: the engineer moves hand over hand on rails (K09).
              Thruster gas is a short straight cone that is gone within a hull-length;
              no gas after K10 except short manoeuvring puffs (K13 K14).
ATMOSFER      hard vacuum outside: no sound through it, no haze, no light shafts, hard
              black shadows · pressurised cabin inside: suits sealed anyway (24/24)
EKRAN YÖNÜ    exterior (A): station ALWAYS screen-left, small ship ALWAYS screen-right,
              approach ALWAYS right → left, black hole upper left behind the station ·
              cockpit from behind (C): pilot LEFT seat, engineer RIGHT seat, 24/24 ·
              the damaged nozzle cluster is on the ship's LEFT (port) side, film-long ·
              "port" (R13) = the ship's left = the damaged side
HAREKET KİLİDİ one gesture per clip. Pilot's habit: right glove squeezes the grip twice,
              short, before a correction (K04 K06 K14) → BROKEN in K18 (thumb stops a
              palm short). Engineer's habit: tugs his strap twice (K09) → ONE pull only
              in K17. Refusal/delay beat: K08, 1.2 s with the forearm locked on the grip.
SAYAÇ         three textless counters, all monotonic:
              ① RESERVE: one thin amber line beside the display — long (K04 K06) → short
                (K08 K11) → very short (K14 K16); never grows back
              ② SPIN MATCH: the station's fins sweep through the cockpit window fast
                (K13) → slower (K14) → still (K15)
              ③ MACHINE CLOCK: "Station burn in three minutes." (K04) → "ten seconds."
                (K22) — the only spoken numbers in the film
EŞ KADRAJ     K01 ↔ K24 (setup A, verbatim camera sentence) · K02 ↔ K17 ↔ K19 ↔ K22
              (setup B: the window that sees) · K18 ↔ K23 (setup H: the glove tight →
              the glove open)
DÜNYA ÇAPASI  3/3 — sky (a black hole: a black disc wrapped in a thin sharp band of hot
              amber light, a fainter bent arc above and below it) · horizon (no horizon
              and no ground — black space and a few faint stars) · landmark (a long dark
              cylinder with three dark flat radiator fins at equal angles and one round
              docking collar at the centre of its front face); copied into every exterior
              prompt, zero drift [D209]
YIPRANMA      ship: on its LEFT side by the nozzle cluster the hull is opened along one
              seam, edges cold and torn — from K01 (flash-forward) to K24, never repaired ·
              suits: scuffed composite plates, worn rubber edges — no dirt, no damage ·
              cockpit display: lit pale grey (K11) → flat black from K16 to the end
KİMLİK DİZİSİ PILOT, same order in every prompt [D208 · D167]: ① close-fitting pearl-white
              suit of matte textile ② scuffed composite shoulder/chest plate ③ dark-gold
              neck ring ④ dark-gold band on the RIGHT forearm · badge: swept wings,
              textless (reference page only) · face (K18 K23): mid-thirties, dark hair
              pulled back, steady dark eyes
              ENGINEER: ① close-fitting white suit of ribbed textile ② cobalt-blue elbow
              panels ③ steel neck ring ④ cobalt-blue band on the LEFT upper arm · left
              wrist: round analogue gauge, single needle, plain dial · face never on
              screen · height / skin tone appear in 0 prompts (red #15)
              ⛔ The two are told apart by SIDE (right ↔ left band), COLOUR (gold ↔
              cobalt), SURFACE (composite plate ↔ ribbed textile) and SEAT (left ↔ right)
IŞIK TAKVİMİ  6 scene lines, hard-locked per scene (㉜⑥ verified). One key, always from
              the UPPER LEFT (the black hole's amber band, ~2700 K) · interiors cold
              5600 K · S04 the cabin is dimmest (amber window light across the seats) ·
              S05 bay dim and cold; K22 the ceiling panel comes on steady white (a
              declared event — power from the station) · S06 ADDS hard blue-white engine
              light from the station's far end (DECLARED EVENT, K22|K23 boundary [D193])
SES REGISTER  HUMAN 13 (helmet radio, band-limited) · MACHINE 2 (flat synthetic ship
              voice, cabin speaker) · RECORDED HUMAN 2 (flight recording, K01 K02) ·
              exterior sound through vacuum: 0 — every sound is carried by a hull, a
              seat or a suit · four separate latch knocks in K21 (through the hull) ·
              deep tremor from K22 to the end · music: none in any prompt (score is
              added in the edit — see MUZIK)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Kuru koşu: 05.10.2026, ffmpeg 8.1, `lavfi testsrc + sine` 4 s sentetik klip üzerinde —
> her filtre çalıştı ve çıktı satırı üretti.

```
E1 · KUYRUK KART / DONMUŞ KARE
KAPI          teslimin sonunda 1 s'den uzun donmuş kare var mı (başlık kartı şüphesi)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=-60dB:d=1" -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · freezedetect VAR (kuru koşu: 0 donma, beklenen)
İKAME         son 6 s'den 0,5 s aralıkla 12 kare çıkarılır ve göz sınavı
BEKLENEN      ⚠️ K15 ve K24'te yapı kadrajda DURUR ama arka plan döner — donma DEĞİL.
              0 donma > 1 s · ekran metni 0,0 s · süre 240,0 ±2 s

E2 · IŞIK TAKVİMİ İZİ  (S06'da motor ışığı ARTIŞI ilan edildi)
KAPI          klip başına ortalama parlaklık serisi
KOMUT         ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · signalstats VE metadata VAR (kuru koşu: 100 satır)
İKAME         her klibin ortasından kare + histogram gözle
BEKLENEN      S04 (K13-K18) iç klipleri filmin en loş iç klipleri · K23-K24 ortalaması
              K13-K22 dış kliplerinden yüksek · klip İÇİNDE ani sönme 0

E3 · KARA EKRAN SÜREKLİLİĞİ  (yanaşma ekranı K16'dan itibaren siyah)
KAPI          K16 (150-160 s) karesinde konsol ekranı siyah mı, K11 (100-110 s) karesinde açık mı
KOMUT         for t in 105 155 165; do ffmpeg -hide_banner -ss $t -i "$M" -frames:v 1 ekran_$t.png -y; done
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · tek kare çıkarımı VAR (kuru koşu: kare yazıldı)
İKAME         yok — göz sınavı
BEKLENEN      105 s ekran AÇIK (soluk gri) · 155 s ekran SİYAH · ekranda harf/rakam 0

E4 · İHRAÇ SESİ
KAPI          integrated loudness ve true peak
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · ebur128 VAR (kuru koşu: "I:" satırı üretildi)
İKAME         yok — bu kapı ikamesizdir, ölçüm yapılmadan teslim edilmez
BEKLENEN      -14 LUFS (kabul -14 … -15) · true peak ≤ -1,0 dBTP

E5 · IZGARA (kesme saniyeleri 10,0'ın katı mı)
KAPI          kesmelerin 10,0 s ızgarasına oturması · klip sayısı 24
KOMUT         ffmpeg -hide_banner -i "$M" -vf "select='gt(scene,0.3)',metadata=print" -f null - 2>&1 | grep pts_time
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · select VE metadata VAR (kuru koşu: 0 kesme, beklenen)
İKAME         karanlık kesmeler görünmezse 5, 15, 25 … 235 s karelerinden 24'lük döşeme
BEKLENEN      tespit edilen her kesme 10,0'ın katı (±0,15 s) · toplam 23 kesme
              ⚠️ dış→dış aynı-kurulum kesmeleri (K01|K02 değil; K03→K04 iç) görünmeyebilir;
              ikame döşeme ZORUNLU sayılır

E6 · FİLİGRAN KÖŞE TESTİ
KAPI          sağ alt çeyrekte tekrar eden bir işaret var mı
KOMUT         for t in 20 60 100 140 180 220; do ffmpeg -hide_banner -ss $t -i "$M" -vf "crop=iw/2:ih/2:iw/2:ih/2" -frames:v 1 kose_$t.png -y; done
DOĞRULANDI    ffmpeg 8.1 · 05.10.2026 · crop VAR (kuru koşu: kose.png yazıldı)
İKAME         yok — göz sınavı
BEKLENEN      altı örneğin altısında aynı yerde aynı şekil YOK (0 filigran)
```

---

## 👁️ GÖZ KAPILARI — beş soru, beşi de KAREYLE cevaplanır

```
G1 · DÖNÜŞ EŞLEMESİ (filmin 1 numaralı riski) — kare 140,5 s · 145,0 s · 149,5 s
   □ istasyonun ön yüzü, kenet halkası ve üç kanat üç karede de AYNI yerde mi
   □ kara deliğin kehribar bandı 140,5 → 149,5 s arasında ~çeyrek tur döndü mü
   □ dönüş TEK yönde mi (geri dönüş 0)
   ⛔ İPTAL KAPISI: iki üretimde tutmazsa üçüncü yeniden yazım yok — kamera A'ya
     taşınır (imza "birlikte dönen ikili" olur), karar sahibe döner

G2 · VİZÖR BİÇİMİ — kare 35,0 s · 175,0 s · 226,0 s
   □ ön pane TEK ve DÜZ mü · çerçeve kalın ve koyu gri mi
   □ kubbe / balon / aynalı kaplama: 0 klip mi
   □ K18 · K23'te yüz panenin içinden okunuyor mu
   ⛔ İkinci üretilen klipte kubbe görülürse ÜRETİM DURUR [D146 · RK1/RK2]

G3 · KENETLENME (doruk) — kare 192,0 s · 194,0 s · 208,0 s
   □ 192 s: iki halka ARALIKLI · 194 s: halkalar temas etmiş, yumuşak halka bir parmak esnemiş
   □ 208 s: dört kanca kapalı — adet 4 (3 ya da 5 değil)
   □ iki halka iki ayrı kenar olarak kalıyor mu (tek yüzeye erime 0 · kıvılcım 0)
   ⛔ K20 + K21 iki üretimde temas/dört kilit göstermezse film ÜRETİLMEZ (PLAN İPTAL KAPISI)

G4 · KONUŞAN AĞIZ SIFIR — replik saniyeleri (R1-R17, B BLOĞU)
   □ her replik anında konuşan kişinin yüzü kadrajda DEĞİL (arkadan / kadraj dışı / başka bölme)
   □ K18'de pilotun dudakları KAPALI (dinleyen) · K23'te dudaklar kapalı
   □ ekranda altyazı/yazı 0 kare
   ⛔ Kadrajda konuşan ağız görülürse klip yeniden üretilir — üretim defteri üç kutusu

G5 · SON KARE — kare 236,0 s · 239,9 s
   □ gemi istasyonun ön yüzüne burnundan BAĞLI mı (tek gövde)
   □ sol kenardan sert beyaz-mavi motor ışığı giriyor mu
   □ gemide sol yandaki yırtık dikiş hâlâ görünüyor mu (onarım 0)
   □ 239,9 s'den sonra kart / yazı / siyah: 0 kare mi
```

---

## 🧱 YANLIŞ-POZİTİF DUVARI — burada İLAN EDİLEN karar ihlal olarak yazılamaz

```
① 9 KLİPTE İNSAN YOK (K01 K03 K05 K07 K13 K15 K20 K21 K24) ve o klipler NEGATIVE bloğu
   KISALTILMIŞTIR; insan sayısı cümlesi bilerek YAZILMAMIŞTIR. Kayıt: üretim red defteri
   satır 2 — "insansız sahne + uzun NEGATIVE + Exactly 0 human figures" deponun tek
   ölçülmüş YAPISAL REDDİ. ⛔ Bu bir eksik değil, o çözümdür.

② KONUŞAN AĞIZ 0 KLİP. 17 replik telsizden, kayıttan ya da kabin hoparlöründen gelir;
   konuşan kişi kameraya sırtını döner, kadraj dışındadır ya da başka bölmededir. "Lip
   sync yok" ya da "kimin konuştuğu görünmüyor" bulgusu DÜŞER — film sesi bedensiz
   tutar (SES_VE_DIYALOG §1a.1).

③ YANAŞMA EKRANI K16'DAN SONRA SİYAHTIR ve siyah KALIR. Bu bir render hatası değil,
   filmin kaybıdır (görüntü kanalı). Siyah ekran K18'de kadrajda — reddedilen nesne.
   K11'de ekranın bir kez kararıp geri gelmesi DRAMATİK İRONİDİR (izleyici pilottan önce görür).

④ K01 VE K02 İLERİ SIÇRAMADIR (K20/K19'un önceden gösterimi). Hikâye sırasıyla
   "çelişki" yazılamaz; ileri sıçramanın sesi uçuş KAYDIDIR (band-pass).

⑤ K15'TE YAPI DURUR, EVREN DÖNER. Kamera geminin gövde kamerasıdır ve gemiyle birlikte
   döner; "arka plan kayıyor, kamera sabit değil" bulgusu DÜŞER — sabit olan gemiye göre
   kameradır, filmin novum karesi budur.

⑥ IŞIK TEK YÖNDEN (sol üst) VE SERTTİR. Vakumda dolgu yoktur; siyah gölgeler kusur
   değil ortam kartıdır (§3.1). S06'daki beyaz-mavi ışık İLAN EDİLMİŞ bir olaydır (motor).

⑦ GEMİNİN SOL YANINDAKİ YIRTIK DİKİŞ FİLM BOYU DURUR (K01 dahil). "Hasar ileri sıçramada
   da var" bir devamlılık hatası değil, ileri sıçramanın doğruluğudur.

⑧ DÖRT KANCA KURMACADIR (gerçek bir yanaşma standardının donanım sayısı değildir);
   istasyon boyutu/dönüşü ve son yaklaşmanın hızı da kurmaca kabullerdir (PLAN).

⑨ SABİT 10,0 s IZGARA ve 0 kırpma bilinçli sapmadır [D74] — §2.3 modülü.

⑩ AMBLEM/ARMA/HARF HİÇBİR YÜZEYDE YOK — rozetler yazısız kabartmadır (kanat · altıgen),
   gösterge kadranı yazısızdır, retikülde ölçek çizgisi yoktur [D138].

⑪ SIRT 13 KLİPTE KADRAJDA ve hepsinde POZİTİF yüzey cümlesiyle yazılmıştır ("one
   continuous ... surface from collar to hip"). Sırt ünitesi / tank: 0 klip [D79 · D139].
```

---

## ⛔ OPERATÖRE TEK SATIR

```
Bu dosya rubriğin BAŞINA yapıştırılır. Yapıştırılmadıysa koşu MOD V'dir ve
T tablolarına GİREMEZ [D129].
```
