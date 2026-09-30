# 📋 THE_SIGNAL_KEEPERS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_SIGNAL_KEEPERS_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ⚠️ **DİKEY FİLMDE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI — artık MAKİNE KAPISI
> DEĞİL.** Bu başlığı yalnız `rubrik_paketle.sh` okuyordu (aile: yatay/dikey) ve
> o betik 11.09.2026'da silindi. Başlık yazım geleneği olarak KALABİLİR; hiçbir
> betik ona bakmaz, yokluğu artık sessiz bir arıza üretmez.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri (hedef dilimi · hareket yönü · eksen) + A  MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⭐ 14.09.2026: ⑭/⑮ için C bloğuna yazılacak satırlar — `HAREKET KİLİDİ:` (eller/ayaklar/baş ne
   yapar, "tek jest" kuralı) ve `EKRAN YÖNÜ:` (hedef hangi dilimde · figür hangi yöne · eksen
   çizgisi — screen-left/right, pusula yok). Yoksa iki mercek çıkarımla koşar ve bunu yazar.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_SIGNAL_KEEPERS
FORMAT:            horizontal 16:9 · 4 minutes · 24 clips × 10.0 s · 2 part files
RUNTIME:           240 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       6        ⛔ SCENE COUNT ≠ CLIP COUNT — see B BLOCK SCENE PLAN
PART GRID:         — (2 part files are a WRITING split, not a QA split: this film is
                   measured as ONE 240 s master. The 4-minute line has no PART QA.)
THEME:             HOPE — "what you send without expecting an answer finds its answer
                   even if you never see it"
THEME SCENES:      S01 · S02 · S03 · S05 · S06
INTENDED EMOTION:  being heard, and a loss paid for it in the same frame (a double
                   feeling: gratitude and bereavement)
ENDING TYPE:       ENDS — she finishes the work, pays for it with the recording, and
                   sends an answer she will not live to see received
PROTAGONIST:       an unnamed lone explorer, sealed suit (no proper name appears in
                   any prompt [D34])
CENTRAL CHOICE:    K19 — her hand stops in the air in front of the panel and she does
                   not withdraw (S05); she carries it out in K20
                   SECOND CHOICE: K23 — she spends the one object she brought from home
DIALOGUE LINES:    2 · register: HUMAN 0 / MACHINE 0 / RECORDED HUMAN 2
                   ⭐ Both are the SAME one-sentence recording, heard broken in K02
                   (12.0 s) and clean in K18 (173.0 s). No character speaks on camera
                   in any clip; the mouth that made the line is 41 years gone.
SILENT SCENES:     22 of 24 clips carry no speech at all
VIRAL INTERSTITIALS: 3 — K11 · K20 · K22  ⛔ THESE MAY NOT BE CUT
TITLE:             "The Signal Keepers" — the title promises someone has been keeping
                   a signal alive; the film shows who, and what keeping it cost when
                   it was finally answered
LIBRARY CONTEXT:   nearest shelf-mates: THE_STILL_SWARM (first contact, being 0 frames)
                   and THE_LAST_SHIFT (dead colony, creature 1 shot). Both KEEP THE
                   BEING OFF SCREEN; this one brings it in on a staged ladder and gives
                   it a choice of its own.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 18   (SHOT = CLIP; every cut is a scene-internal
                 or scene-boundary cut, there are no cuts inside a clip)
SCENE PLAN:      SAHNE PLANI 3 4 5 3 5 4 = 24
                 S01 = K01-K03 · S02 = K04-K07 · S03 = K08-K12 · S04 = K13-K15 ·
                 S05 = K16-K20 · S06 = K21-K24
                 ⛔ SCENE COUNT 6 ≠ CLIP COUNT 24
INTRA-SCENE CUTS: K01|K02 · K02|K03 · K04|K05 · K05|K06 · K06|K07 · K08|K09 · K09|K10 ·
                 K10|K11 · K11|K12 · K13|K14 · K14|K15 · K16|K17 · K17|K18 · K18|K19 ·
                 K19|K20 · K21|K22 · K22|K23 · K23|K24 — these cuts are INSIDE one
                 scene: location, light, sound bed, suit grit, held object and body pose
                 MUST match across them; a reset here is a ② CONTINUITY defect, not a
                 scene change. SCENE BOUNDARIES (a change here is legitimate):
                 K03|K04 · K07|K08 · K12|K13 · K15|K16 · K20|K21
TARGET ASL BAND: 10.0 s (fixed grid — no curve)   ASL CURVE: —
                 ⛔ GEREKÇE [D74]: this line is a 24 × 10.0 s module (§2.3). The grid is
                 a PRODUCTION plan, not the final edit rhythm: the cut may hold or trim
                 a clip and that decision is measured at the edit gate, not here.
GRID:            clip(n) start = (n−1) × 10.0 s   (no hook offset — K01 starts at 0.0 s)
RUNTIME:         240.0 s
RAW FOOTAGE:     24 clips × 10.0 s = 240 s · TRIM BUDGET: 0 s (fixed grid)
SCREEN TEXT:     0.0 saniye — title card, end card and cover output INCLUDED
                 ⭐ This world has NO WRITING AT ALL: no letter, digit, badge or emblem
                 on any surface, in any clip. It is the novum, not only a lock [D138].
CAMERA:          24 / 24 sabit lockoff — zero camera movement in every clip
SETUP SEQUENCE:  A B A · C D C D · E F G F E · H I H · J K E K E · K E L G
KURULUM İSKELETİ: A B A C D C D E F G F E H I H J K E K E K E L G   (PLAN ile AYNI)
KÜME:            — (ÇOK KLİPLİ SAHNE rejiminde küme YOKTUR · ACI_YAYI §4b · 22.09.2026)
DÖNÜŞ:           10 / 24 = %41.7 (≥%40 ✅) — K03 K06 K07 K11 K12 K15 K19 K20 K21 K22
                 NOT counted (interval > 3, re-introduction not return): K18 (E, gap 6)
                 and K24 (G, gap 14 — the deliberate loop closure onto the novum frame)
ANGLE ARC:       4 angle TYPES — eye level (A·B·E·F·H·J·L) · low angle (C·K) ·
                 high angle (D·G) · ground level (I)
DORUK:           K21 → S06 1/4 (clip start 200.0 s)
                 ⚡ DELIBERATE SHOCK CUTS: 0 (ceiling 2). All 23 adjacent pairs are
                 EXACTLY one scale step. The film's break is in the SOUND channel at
                 K20; an optical smash cut on top of it would shrink both. The one
                 legitimate shock (K20|K21, MS→EWS) was MEASURED AND NOT TAKEN — see
                 00_ANALIZ/03_SAHNE_SIRALAMASI.md §3.

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   line(K_n) = (n−1) × 10.0 + TIMELINE offset
   K02: (2−1) × 10.0 + 2.0 = 12.0 s      K18: (18−1) × 10.0 + 3.0 = 173.0 s
   CUT (no quoted text in the prompt): (20−1) × 10.0 + 2.6 = 192.6 s
   Doğrulandı: iki kayıt da formülle üretildi; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   one sphere of dark blue glass seated in the round seat on the probe's face, plus
   ONE mark of dark blue on the black stone floor · 236.0 s · 1 + 1 adet · BULUNAN
   ⛔ sayılabilir ve adı konabilir: a sphere, and one stain the size of a hand
   ffmpeg -ss 236 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: K10 (90.0-100.0 s) ↔ K24 (230.0-240.0 s) — SAME setup G, same lens,
   distance, height and angle; the camera sentence is copied verbatim and carries
   "— the same position, height and lens as Clip 10." The ONE variable that changes is
   what is in the frame and what it sounds like: a BROKEN piece of blue glass with a
   DULL tone ↔ a WHOLE blue sphere with a CLEAR tone.
   ⭐ K01 ↔ K24 is a BEHAVIOURAL rhyme, not a camera rhyme: hands close to the body
   with one on the sphere (LISTENING) ↔ hands open and empty (ANSWERING).
   ffmpeg -ss 95 -i "$M" -frames:v 1 novum.jpg ; ffmpeg -ss 235 -i "$M" -frames:v 1 son.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111-11-111111-1111111
       (1 = human in frame · - = no human · ONE CHARACTER PER CLIP, 24 characters)
       ⛔ K07 · K10 · K17 carry NO human and that is BY DESIGN — see the FALSE-POSITIVE
         WALL. 21 of 24 clips carry exactly one human, 3 carry none. ⚙️ MEASURED from
         the prompt bodies on 28.09.2026, not typed by hand: each of those three has
         `IN FRAME: none` in both its image and its video prompt, and a shortened
         NEGATIVE block (KART 10 · refusal register #2).

DAVRANIŞ ŞERİDİ (klip başına bir harf · KARAKTER_KARTI §4):
       SGRGDR-TR-KRGSGG-TKBRSBR
       G = task · T = hesitation · D = failed attempt · K = choice · B = cost ·
       R = reaction · S = stillness · - = no human
       G share of human clips: 5/21 = 23.8% (ceiling 50%) · T 2 · D 1 · K 2 · B 2 ·
       R 6 · S 3 · first letter (S) ≠ last letter (R)

TEMPO ŞERİDİ (Y slow · N normal · H fast):
       YNY NYNY NNYNN YYN YNYNH NYNY
       17 changes · no three identical in a row · the central choice (K19 = N) differs
       from both neighbours (K18 Y · K20 H) · after the cost (K20 H) it slows (K21 N)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         exactly 1 in 21 clips · exactly 0 in 3 clips (K07 · K10 · K17)
KASK          worn and sealed in 24/24 clips, opened in 0 clips · the visor is ONE
              FLAT front pane inside a THICK dark-grey rim, optically clear, zero tint,
              zero mirror, face fully readable through it · back is one continuous
              sculpted surface from collar to hip, no back-mounted unit — flat back
              silhouette [D79]
              ⛔ the words seamless / bubble / dome / sphere never describe the helmet
              FACE IS THE SUBJECT in 6 clips (K02 K08 K09 K11 K18 K20 K22 → 7); in the
              rest the visor sentence stands and says nothing more
NOVUM         Nobody writes on this world: they hear and they keep. A human probe that
              fell 41 years ago has been REPAIRED and its voice kept alive ever since.
              THE VIOLATION: a human-made object is being cared for, precisely and for
              four decades, by something that has no use for it.
              BOUNDARY: the rule lives in the SOUND and the OBJECT. Nothing hangs in
              the air, nothing changes shape, nothing is written anywhere. The
              recognition is carried by TWO TONES on the same material — the BROKEN
              piece is DULL, the WHOLE sphere is CLEAR — and by nothing else.
YERÇEKİMİ     0.42 g — single value, 24/24 prompts
              fall table: 1.0 m → 0.70 s · 1.70 m → 0.91 s · 3.20 m → 1.25 s
ATMOSFER      dense cold atmosphere, 3.1 bar, 240 K, unbreathable → visor 100% closed
              in 24/24 · fill VERY STRONG but motivated (a ringed giant planet, a large
              soft source), shadow edges soft and the shadows DEEP inside · lifted dust
              settles again within 3 s and CLUMPS as it lands · NO suspended dust
              curtain in any clip · low mist is CONDENSATE: it SITS in the hollows and
              never rises · the slow wind moves only fine dust along the ground
              ⛔ mist and dust are never mixed in one sentence: mist SITS, dust LIFTS
              AND SETTLES. Two different substances, two different rules.
EKRAN YÖNÜ    KONUM KİLİDİ: the woman is in the RIGHT third and the standing figure in
              the LEFT third in every clip that holds both bodies (K13 · K15 · K16 ·
              K19); the centre line between them is crossed in 0 clips. The ringed
              giant planet is over the same horizon in all 6 exterior clips that show
              it. She never crosses the 180° line inside a scene — 24/24 fixed.
HAREKET KİLİDİ one gesture per clip; the fingertip TAPS, the palm SEATS, and no hand
              grips-and-turns anything except the two ring turns (K20 two hands, K23
              two fingertips). Walking clips: 3 in the whole film (K04 · K12 · K16).
              ⛔ CONTACT BETWEEN THE TWO BODIES: 0 frames, 24/24 clips. In K19 the
              mineral hand is ALREADY flat on the panel and her hand stops in the air
              a hand's width short; refusal delay 0.8 s (≥0.7 s).
SAYAÇ         four textless counters, all monotonic, none of them a dial or a display:
              ① TONE (the object's counter): DULL K10 → CLEAR K11 → CLEAR from the
                probe's own seat K24 — never reverses
              ② the ringed giant's height above the horizon, 6 steps: K01 → K03 → K04
                → K13 → K14 → K15; the counter ENDS at the hall door by design and
                hands over to ③
              ③ darkened plants behind her: 2 (K04) → 3 (K05, one by her own finger)
                → 5 (K06) → the whole row, UNTOUCHED (K07) ⭐ the counter CHANGES HANDS
              ④ waking cradle rings: the nearest three (K21) → the row tilting upward
                and the light leaving the top of frame (K22)
EŞ KADRAJ     K10 ↔ K24 (setup G, verbatim camera sentence, the film's rhyme pair) ·
              K17 ↔ K21 (setup K, the same empty socket dead then alive) ·
              K18 ↔ K20 and K20 ↔ K22 (setup E: the frame that HEARS, SILENCES, SENDS)
DÜNYA ÇAPASI  3/3 — sky (a dark sky with a ringed giant planet low over the horizon,
              its ring a thin bright line, the planet as wide as a palm held at arm's
              length) · horizon (black stone valleys to a straight horizon, low mist
              sitting in the hollows) · landmark (the towers of the city beyond the rock
              passage, taller than the mountains they stand among); copied into every
              exterior prompt, zero drift [D209]
YIPRANMA      one global finish, never reset: an even matte dusting of pale grey grit
              over the whole suit, heavier at the knees from S02 onward, plus scuffed
              edges at the wrist rings. Damage: none. The blue glass sphere is chipped
              at one edge and scratched from the first clip — that is the OBJECT's
              history, not the suit's wear [D42]
KİMLİK DİZİSİ 4 attributes, SAME ORDER in every prompt [D208 · D167]:
              ① off-white thick creased multilayer nylon ② dark-grey segmented joint
              guards ③ a faded burnt-orange band on the left upper arm ④ a round
              brushed-steel seat on the left shoulder holding a sphere of dark blue
              glass · amblem NONE ANYWHERE (no badge, no patch, no rank mark) · kir
              pale grey grit from K01 onward · hasar none · the shoulder sphere is
              carried K01-K23 and is in the PROBE's seat from K24 on (does not come
              back) · height / skin tone / hair / age appear in 0 prompts (red #15)
IŞIK TAKVİMİ  6 scene lines, hard-locked per scene (㉜⑥ verified). S01 one source
              (reflected only) · S02 adds the plants' own light · S03 reflected only ·
              S04 adds the city's orange-gold band · S05 is the film's DARKEST scene
              (cold grey points over the nearest cradles, the hall depth UNLIT) ·
              S06 RISES — the cradle rings come on at K21 and the row leaves the top of
              frame at K22. THE RISE IS A DECLARED EVENT [D193], the only one.
              ⚠️ The exterior sky counter and the interior ring counter are TWO
              counters that hand over at the hall door; this is not a reset.
SES REGISTER  HUMAN 0 · MACHINE 0 · RECORDED HUMAN 2 (the same sentence twice, once
              broken and once clean) · the being's only "word" is ONE tapped tone
              (organic source: breath and sliding mineral texture; synthetic and
              theremin sources: 0 clips) · room tone: one continuous bed for the full
              240 s, cut ONCE — the hard mute at 192.6-194.0 s [D180]
              ⛔ Exactly TWO treble events in the whole film and both are meaningful:
                the consonants of the recording, and the tone off the glass.
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
E1 · KUYRUK KART / DONMUŞ KARE
KAPI          teslimin sonunda 1 s'den uzun donmuş kare var mı (başlık kartı şüphesi)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=-60dB:d=1" -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · filtre VAR
İKAME         filtre yoksa son 6 s'den 0,5 s aralıkla 12 kare çıkarılır ve göz sınavı
BEKLENEN      0 donma · ekran metni 0,0 s · süre 240,0 ±2 s

E2 · IŞIK TAKVİMİ İZİ  (artış İLAN EDİLMİŞ — S06'da ARTIŞ aranır)
KAPI          klip başına ortalama parlaklık serisi; K16-K20 en düşük düzey, K21'den
              sonra ARTAN
KOMUT         ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · signalstats VE metadata VAR
İKAME         her klibin ortasından kare + histogram gözle
BEKLENEN      K16-K20 filmin en karanlık beşlisi · K20 < K21 < K22 · klip İÇİNDE geri
              sönme 0 · K01-K15 arasında %20'den büyük ani ARTIŞ YOK

E3 · PLANLI SESSİZLİK  (K20'nin kesilmesi — kurguda HARD MUTE)
KAPI          192,6-194,0 s aralığında kesintisiz sessizlik var mı
KOMUT         ffmpeg -hide_banner -i "$M" -af "highpass=f=300,lowpass=f=3400,silencedetect=n=-50dB:d=0.3" -f null - 2>&1 | grep silence
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · silencedetect VAR
İKAME         üç eşikte koşulur: -50 / -40 / -30 dB; hiçbirinde aralık yoksa TESLİM KUSURU
BEKLENEN      192,6-194,0 s tek aralık · filmin başka hiçbir yerinde mutlak sıfır 0 s

E4 · İHRAÇ SESİ
KAPI          integrated loudness ve true peak
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · ebur128 VAR
İKAME         yok — bu kapı ikamesizdir, ölçüm yapılmadan teslim edilmez
BEKLENEN      -14 LUFS (kabul -14 … -15) · true peak ≤ -1,0 dBTP

E5 · IZGARA (kesme saniyeleri 10,0'ın katı mı)
KAPI          kesmelerin 10,0 s ızgarasına oturması · klip sayısı 24
KOMUT         ffmpeg -hide_banner -i "$M" -vf "select='gt(scene,0.3)',metadata=print" -f null - 2>&1 | grep pts_time
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · select VE metadata VAR
İKAME         karanlık kesmeler görünmezse 5, 15, 25 … 235 s karelerinden 24'lük döşeme
BEKLENEN      tespit edilen her kesme 10,0'ın katı (±0,15 s) · toplam 23 kesme
              ⚠️ Bu filmde ardışık çiftlerin HEPSİ tek ölçek kademesi; sahne algılayıcı
              eşiği 0,3'te bazı kesmeleri kaçırabilir. İkame döşeme ZORUNLU sayılır.

E6 · FİLİGRAN KÖŞE TESTİ
KAPI          sağ alt çeyrekte tekrar eden bir işaret var mı
KOMUT         for t in 20 60 100 140 180 220; do ffmpeg -hide_banner -ss $t -i "$M" -vf "crop=iw/2:ih/2:iw/2:ih/2" -frames:v 1 kose_$t.png -y; done
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · crop VAR
İKAME         yok — göz sınavı
BEKLENEN      altı örneğin altısında aynı yerde aynı şekil YOK (0 filigran)
```

---

## 👁️ GÖZ KAPILARI — beş soru, beşi de KAREYLE cevaplanır

> Betik bunları ölçmez; operatör bakar. Her satır bir SAYI sorar.

```
G1 · VARLIĞIN BİÇİMİ (filmin 1 numaralı riski) — kare 125,0 s · 145,0 s · 155,0 s
   □ tek eksen · 2 bacak · 2 ön kol · 1 omuz levhası · o levhada 1 çatlak — sayılar tutuyor mu
   □ boyu kadrajdaki taş kemer ağzının 3/4'ü mü (sabit şahit her üç karede aynı mı)
   □ başın ön yüzü TEK düz mineral zar mı · GÖZ: 0 kare mi (hiçbir karede olmamalı)
   □ ikinci bir uzuv çifti · kubbe/plaka kask: 0 kare mi
   ⛔ Kubbe, ikinci uzuv çifti ya da HERHANGİ bir göz çıkarsa ÜRETİM DURUR ve karar
     sahibe döner; HAZIR DÜŞÜŞ (tam form → siluet) devreye girer

G2 · VİZÖR BİÇİMİ — kare 15,0 s · 95,0 s · 175,0 s
   □ ön pane TEK ve DÜZ mü · çerçeve kalın ve koyu gri mi
   □ kubbe / balon / çerçevesiz sarma / aynalı kaplama: 0 klip mi
   □ yüz panenin içinden okunuyor mu (yansıma yalnız üst kenarda tek çizgi)
   ⛔ İkinci üretilen klipte kubbe görülürse ÜRETİM DURUR [D146 · referans paketi RK2]

G3 · TON KANALI (novum kapısı) — kare 95,0 s · 105,0 s · 233,0 s
   □ K10'da kırık parça avuçta OKUNUYOR mu (kadrajın ~1/4'ü, bir kenarı keskin)
   □ K11'de parmak ucunun teması ve camın titremesi KADRAJDA mı
   □ K24'te aynı kadraj, aynı lens, aynı yükseklik mi — değişen tek şey içindeki nesne mi
   ⛔ Donuk/berrak ayrımı üç denemede de kadrajda okunur bir HAREKET olarak gelmezse
     taşıyıcı DEĞİŞİR: kırık parça sondanın boş cam yuvasının yanında durur, tanıma
     K17'ye taşınır (Plan B — bedel ve doruk yerinde kalır)

G4 · TEMAS SIFIR (politika + ayrılık kapısı) — kare 181,0 s · 183,0 s · 185,0 s
   □ mineral avuç panelin üstünde ÖNCEDEN duruyor mu (kadının eli sonra gelmeli)
   □ iki el arasında her üç karede de AÇIK bir hava boşluğu var mı
   □ ret gecikmesi: avuç indikten ~0,8 s sonra el duruyor mu (sıra tersine DÖNMEMELİ)
   ⛔ Sıra tersine dönerse ret değil ÇARPIŞMA okunur ve sahnenin anlamı tersine döner

G5 · SON KARE — kare 236,0 s · 239,9 s
   □ sondanın cam yuvasında TEK mavi küre var mı (1 adet, sonuna kadar oturmuş)
   □ siyah taşta TEK mavi leke var mı (1 adet, bir avuç genişliği)
   □ eldiven kadrajdan BOŞ ve AÇIK çıkıyor mu
   □ 239,9 s'den sonra kart / yazı / siyah: 0 kare mi
```

---

## 🧱 YANLIŞ-POZİTİF DUVARI — burada İLAN EDİLEN karar ihlal olarak yazılamaz

> ⑬ UYUM ve ② ③ ⑤ ⑨-⑫ merceklerinin FLAGS soruları buradan cevaplanır.
> Her satır bir TASARIM KARARIDIR ve ölçülmüş bir kayda dayanır.

```
① 3 KLİPTE İNSAN YOK (K07 · K10 · K17) ve o üç klibin NEGATIVE bloğu KISALTILMIŞTIR;
   insan sayısı cümlesi bilerek YAZILMAMIŞTIR. Kayıt: üretim red defteri satır 2 —
   "insansız sahne + uzun NEGATIVE + Exactly 0 human figures" deponun tek ölçülmüş
   YAPISAL REDDİ; geçen çözüm NEGATIVE'i kısaltmaktı. ⛔ Bu bir eksik değil, o çözümdür.

② VARLIĞIN GÖZÜ YOKTUR ve göz hiçbir promptta ANILMAZ — ne pozitif ne negatif olarak.
   "no eyes" yazmak yasağın kendisini prompta sokar [D123]. Yazılan şey pozitiftir:
   başın ön yüzü tek düz mineral zar. "Varlığın gözleri okunmuyor" bir bulgu DEĞİLDİR.
   Empati kanalı GÖZ değil ELDİR (avuç açılır K10 · avuç panele iner K19 · avuç kalkar
   K20); bu, uzaylı kılavuzu §1'in birinci tercihinden bilinçli sapmadır [D74] ve
   sahip ayrı bir soruyla onayladı.

③ TEMAS 0 KARE, 24/24. Ayrılık anı (K19) bir RET'tir ve mesafeyle okunur. "İki gövde
   hiç dokunmuyor" bir devamlılık kusuru değil, KART 12 + D196 karşılığıdır.

④ BİTKİLER ve CAM KENDİ IŞIK KAYNAKLARIDIR, ve `0% bloom, no glow` satırı KALKMAZ.
   Çelişki değil, §3.4'ün Arşimet kalıbıdır: yasak HÂLE için, pozitif kural KAYNAK
   için — "the low plants are themselves the source, like lit lamps, not spreading
   past their edges". ⑪ merceği bunu çelişki yazarsa bulgu DÜŞER.

⑤ IŞIK S05'TE DÜŞER, S06'DA ARTAR. Düşüş mekândır (dışarıdan ışıksız bir salona
   girilir), artış OLAYDIR (K21). "Işık takvimi monotonik değil" hükmü ancak SAHNE
   İÇİNDE geçerlidir; sahne içi LIGHT satırları makineyle birebir doğrulandı (㉜⑥).

⑥ "YÜZLERCE SONDA" HİÇBİR PROMPTTA YAZILMAZ. Salonun derinliği IŞIKSIZDIR ve çokluk
   izleyicinin çıkarımıdır. "Medeniyetin ölçeği gösterilmemiş" bulgusu KART 13 gereği
   DÜŞER: model saymaz, doldurur.

⑦ AMBLEM/ARMA/HARF HİÇBİR YÜZEYDE YOK — ne giyside, ne şehirde, ne sondada. Bu bir
   yasak değil DÜNYANIN KURALIDIR (novum: bu medeniyet yazmaz). "Kimlik işareti
   eksik" bulgusu D138 ve üretim red defteri satır 3 gereği DÜŞER.

⑧ SABİT 10,0 s IZGARA ve 0 kırpma bilinçli sapmadır [D74] — §2.3 modülü. ASL eğrisi
   UYGULANAMAZ. "Tempo düz" bulgusu ızgaraya yazılamaz; yazılacaksa kadraj İÇİ
   değişkenlere (ölçek · kurulum · beden) yazılır.

⑨ ⚡ŞOK KESME 0 (tavan 2) ve bu bir EKSİKLİK DEĞİL TERCİHTİR: filmin kopuşu SES
   kanalındadır (K20, 192,6 s). Ölçülüp ALINMAYAN şok K20|K21'dir ve gerekçesi
   00_ANALIZ/03_SAHNE_SIRALAMASI.md §3'te yazılıdır.

⑩ K19'DA VARLIĞIN ÖN KOLU "in a shell of dark mineral plates" diye yazılmıştır. Bu bir
   giysi değildir; varlığın kendi yüzeyidir. ㉑ merceği bunu "örtü adı" olarak okur ve
   doğru okur: mineral kabuk bu gövdenin örtüsüdür.

⑪ SIRT 6 KLİPTE KADRAJDA (K01 · K03 · K06 · K12 · K13 · K15 · K16) ve hepsinde POZİTİF
   yüzey cümlesiyle yazılmıştır ("one continuous sculpted surface from collar to hip").
   Sırt ünitesi / sırt çantası / tank: 0 klip [D79 · D139].

⑫ "still" kelimesi pozitif gövdede çoğunlukla ŞABLONUN KENDİ ifadesidir ("the approved
   still" = onaylı KARE, bir isim) ya da zarftır ("hâlâ"). Yasak olan DURUM kalıbı
   ("holds still" · "motionless" · "frozen" tek başına) 0 kez geçer; durağanlık her
   yerde nefes + sabit bakış hedefi + tek mikro ayarla yazıldı [D79].
```

---

## ⛔ OPERATÖRE TEK SATIR

```
Bu dosya rubriğin BAŞINA yapıştırılır. Yapıştırılmadıysa koşu MOD V'dir ve
T tablolarına GİREMEZ [D129]. Depoda SPEC yazılmış olduğu hâlde mod V koşulan
film sayısı 13'tür; ikisi bu filmin okuma listesindeydi.
```
