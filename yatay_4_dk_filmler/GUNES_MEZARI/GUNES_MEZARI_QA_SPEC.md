# 📋 GUNES_MEZARI — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `GUNES_MEZARI_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
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
FILM:              GUNES_MEZARI
FORMAT:            horizontal 16:9 · 4 minutes · 24 clips × 10.0 s · 2 part files
RUNTIME:           240 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       7        ⛔ SCENE COUNT ≠ CLIP COUNT — see B BLOCK SCENE PLAN
PART GRID:         — (2 part files are a WRITING split, not a QA split: this film is
                   measured as ONE 240 s master. The 4-minute line has no PART QA.)
THEME:             SACRIFICE — "the one who gives something back waits in front of
                   what she cannot give back"
THEME SCENES:      S01 · S02 · S03 · S05 · S06 · S07
INTENDED EMOTION:  atonement, then a loss confirmed in daylight (a double feeling)
ENDING TYPE:       ENDS — she finishes the work, pays for it, and the answer to the
                   film's question arrives and is negative; one living thing remains
PROTAGONIST:       an unnamed former fleet captain, alone, sealed suit (no proper name
                   appears in any prompt [D34])
CENTRAL CHOICE:    K16 — she lets go of the launch lever and does not leave (S05)
                   SECOND CHOICE: K20 — she spends the ship's one key bar (S06)
DIALOGUE LINES:    2 · register: HUMAN 0 / MACHINE 0 / RECORDED HUMAN 2
                   ⭐ Both are the SAME one-sentence recording, heard in K03 (24.0 s)
                   and K10 (90.0 s). No character speaks on camera in any clip.
SILENT SCENES:     22 of 24 clips carry no speech at all
VIRAL INTERSTITIALS: 2 — K12 · K17  ⛔ THESE MAY NOT BE CUT
TITLE:             "A Straight Question: can a light be given back?" — the released
                   title is in the release package; the film promises a return and
                   delivers it, and then shows what a return does not fix
LIBRARY CONTEXT:   nearest shelf-mates: THE_KEPT_LIGHT (a light kept, 4 min) and
                   THE_SOLAR_MIRROR (a sun redirected). Both KEEP or AIM the light;
                   this one GIVES IT BACK and spends its carrier doing it.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 17   (SHOT = CLIP; every cut is a scene-internal
                 or scene-boundary cut, there are no cuts inside a clip)
SCENE PLAN:      SAHNE PLANI 3 6 3 2 3 4 3 = 24
                 S01 = K01-K03 · S02 = K04-K09 · S03 = K10-K12 · S04 = K13-K14 ·
                 S05 = K15-K17 · S06 = K18-K21 · S07 = K22-K24
                 ⛔ SCENE COUNT 7 ≠ CLIP COUNT 24
INTRA-SCENE CUTS: K01|K02 · K02|K03 · K04|K05 · K05|K06 · K06|K07 · K07|K08 · K08|K09 ·
                 K10|K11 · K11|K12 · K13|K14 · K15|K16 · K16|K17 · K18|K19 · K19|K20 ·
                 K20|K21 · K22|K23 · K23|K24 — these cuts are INSIDE one scene:
                 location, light, sound bed, frost rime, held object and body pose MUST
                 match across them; a reset here is a ② CONTINUITY defect, not a scene
                 change. SCENE BOUNDARIES (a change here is legitimate): K03|K04 ·
                 K09|K10 · K12|K13 · K14|K15 · K17|K18 · K21|K22
TARGET ASL BAND: 10.0 s (fixed grid — no curve)   ASL CURVE: —
                 ⛔ GEREKÇE [D74]: this line is a 24 × 10.0 s module (§2.3). The grid is
                 a PRODUCTION plan, not the final edit rhythm: the cut may hold or trim
                 a clip and that decision is measured at the edit gate, not here.
GRID:            clip(n) start = (n−1) × 10.0 s   (no hook offset — K01 starts at 0.0 s)
RUNTIME:         240.0 s
RAW FOOTAGE:     24 clips × 10.0 s = 240 s · TRIM BUDGET: 0 s (fixed grid)
SCREEN TEXT:     0.0 saniye — title card, end card and cover output INCLUDED
CAMERA:          24 / 24 sabit lockoff — zero camera movement in every clip
SETUP SEQUENCE:  C I C · I F G F D C · A C D · C D · F H F · H F D I · C A C
KURULUM İSKELETİ: C I C I F G F D C A C D C D F H F H F D I C A C   (PLAN ile AYNI)
KÜME:            — (ÇOK KLİPLİ SAHNE rejiminde küme YOKTUR · ACI_YAYI §4b · 22.09.2026)
DÖNÜŞ:           10 / 24 = %41.7 (≥%40 ✅) — K03 K04 K07 K11 K13 K14 K17 K18 K19 K24
ANGLE ARC:       5 angle TYPES — eye level (A·D·I) · high angle (C) · low angle (F) ·
                 over-the-shoulder (G) · profile (H)
DORUK:           K21 → S06 4/4 (clip start 200.0 s) · the single deliberate SHOCK cut
                 in the film is K20|K21 (CU → WS, two scale steps)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   line(K_n) = (n−1) × 10.0 + TIMELINE offset
   K03: (3−1) × 10.0 + 4.0 = 24.0 s      K10: (10−1) × 10.0 + 0.0 = 90.0 s
   Doğrulandı: iki kayıt da formülle üretildi; sapma 0.

FİNAL VURUŞ KANITI [D141]:
   one dark maroon shoot with three leaves, inside the rock hollow · 236.0 s ·
   1 adet · BULUNAN
   ffmpeg -ss 236 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: K01 (0.0-10.0 s) ↔ K24 (230.0-240.0 s) — SAME setup C, same lens,
   distance, height and angle; the camera sentence is copied verbatim. The ONE
   variable that changes is what is in the frame: a caged dimmed sphere ↔ a lit
   living shoot in stone.
   ffmpeg -ss 5 -i "$M" -frames:v 1 ilk.jpg ; ffmpeg -ss 235 -i "$M" -frames:v 1 son.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  --1-111111-111111111-11-
       (1 = human in frame · - = no human · ONE CHARACTER PER CLIP, 24 characters)
       ⛔ K01 · K02 · K04 · K11 · K21 · K24 carry NO human and that is BY DESIGN —
         see the FALSE-POSITIVE WALL. 18 of 24 clips carry exactly one human, 6 carry
         none. ⚙️ MEASURED from the prompt bodies on 25.09.2026, not typed by hand:
         every one of those six has `IN FRAME: none` in both its image and its video
         prompt, and a shortened NEGATIVE block (KART 10 · refusal register #2).

DAVRANIŞ ŞERİDİ (klip başına bir harf · KARAKTER_KARTI §4):
       --RGGGTTSG-RDGTKBGDKRSS-
       G = task · T = hesitation · D = failed attempt · K = choice · B = cost ·
       R = reaction · S = stillness · - = no human
       G share of human clips: 6/20 = 30% (ceiling 50%)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         exactly 1 in 18 clips · exactly 0 in 6 clips (K01 · K02 · K04 · K11 · K21 · K24)
KASK          worn and sealed in 24/24 clips, opened in 0 clips · the visor is ONE
              FLAT front pane inside a THICK dark rim, optically clear, zero tint,
              zero mirror, face fully readable through it · back is one continuous
              ribbed surface, no back-mounted unit — flat back silhouette [D79]
              ⛔ the words seamless / bubble / dome / sphere never describe the helmet
NOVUM         A sun can be carried: a POWERED cage compresses and holds it, and if
              the cage changes hands the sun changes hands. Three rings under the
              ship are a portable cradle; the city's three stone arches are the fixed
              one. THE VIOLATION: a star-like body the size of a small building is
              clamped, carried and handed over like cargo.
              BOUNDARY: the rule applies ONLY to the sphere. Nothing else in this film
              stays up in the air; anything she lets go reaches the ground in about a
              second. A lens that reads THAT as "two gravities" is reading the design.
YERÇEKİMİ     0.38 g — single value, 24/24 prompts
              fall table: 1.0 m → 0.73 s · 1.7 m → 0.96 s · 6.0 m → 1.80 s
ATMOSFER      dense cryogenic atmosphere, 0.90 bar, 95 K, NO haze (the long night
              rained the photochemical haze out) → shadows HARD, fill WEAK, absolute
              shadow legitimate; lifted frost settles within 0.5 s; wind 1-2 m/s never
              moves cloth
EKRAN YÖNÜ    the cradle is always beyond the rooftops on the same side; the ship's
              bow is to SCREEN LEFT in all four clips it appears (K02 · K04 · K18 ·
              K21 · K23); she never crosses the 180° line inside a scene — 24/24 fixed
HAREKET KİLİDİ one gesture per clip; the lower body is locked to the ground in 14 of
              the 20 human clips (knee down, boots braced, shoulder into a surface);
              exactly ONE walking clip in the film (K05)
SAYAÇ         three textless counters, all monotonic:
              ① ship lamps 6 (K15) → 3 (K17) → 1 (K18) → 0 (K21+)
              ② frost rime none (K01-K03) → thin (K04-K14) → heavier (K15-K24)
              ③ lit area of the city 0 (K01-K18) → socket (K19) → wall and paving
                (K22) → whole street (K23-K24)
EŞ KADRAJ     K01 ↔ K24 (setup C, verbatim camera sentence) · K02 ↔ K18 (the same
              one lit window on the hull, lit then dark)
DÜNYA ÇAPASI  3/3 — sky (a black sky thick with stars and one shattered moon low over
              the rooftops, its ring a thin arc) · horizon (a flat line of black basalt
              towers to a straight horizon, no haze) · landmark (the release cradle at
              the city's edge, three stone arches, its open socket facing the sky);
              copied VERBATIM into every exterior prompt, zero drift [D209]
YIPRANMA      one global finish, three steps, never reset: pale frost rime along the
              cloak hem and the shoulder caps; plus ONE permanent mark — a crescent
              scorch the width of two fingers across the knuckles on the back of the
              LEFT glove, present in all 20 human clips [D42 · D91]
KİMLİK DİZİSİ kask K K K K K K K K K K K K K K K K K K K K (20 human clips, all K) ·
              amblem NONE ANYWHERE (no badge, no patch, no rank mark — the empire is
              read as SHAPE, not as a sign) · giysi matte graphite (never "black") ·
              kir frost rime from K04 onward · hasar none · key bar carried K15-K20,
              absent from K21 onward (does not come back) [D208]
IŞIK TAKVİMİ  monotonic and FLAT for S01-S05 (one lamp + one shattered moon, no sky
              body), then RISING: S06 adds the socket light at K19 and the release at
              K21, S07 is the new sun. THE RISE IS A DECLARED EVENT, not a drift [D193]
              ⚠️ FALSE-POSITIVE: the key light is a LAMP SHE CARRIES; it moves with her
              body. Its direction is locked by SOURCE, not by clock face.
SES REGISTER  HUMAN 0 · MACHINE 0 · RECORDED HUMAN 2 (the same sentence twice)
              room tone: one continuous bed for the full 240 s, never cut
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
E1 · KUYRUK KART / DONMUŞ KARE
KAPI          teslimin sonunda 1 s'den uzun donmuş kare var mı (başlık kartı şüphesi)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=-60dB:d=1" -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · filtre VAR
İKAME         filtre yoksa son 6 s'den 0,5 s aralıkla 12 kare çıkarılır ve göz sınavı
BEKLENEN      0 donma · ekran metni 0,0 s · süre 240,0 ±2 s

E2 · IŞIK TAKVİMİ İZİ  (artış İLAN EDİLMİŞ — düşüş değil artış aranır)
KAPI          klip başına ortalama parlaklık serisi; K01-K18 düz, K19'dan sonra ARTAN
KOMUT         ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · signalstats VE metadata VAR
İKAME         her klibin ortasından kare + histogram gözle
BEKLENEN      K01-K18 arasında %20'den büyük ARTIŞ YOK · K19 < K21 < K22 ≤ K23 ·
              klip İÇİNDE geri sönme 0 (⟳ işareti 0)

E3 · PLANLI SESSİZLİK  (K12'nin sonu — kurguda HARD MUTE)
KAPI          118,0-120,0 s aralığında kesintisiz sessizlik var mı
KOMUT         ffmpeg -hide_banner -i "$M" -af "highpass=f=300,lowpass=f=3400,silencedetect=n=-50dB:d=0.3" -f null - 2>&1 | grep silence
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · silencedetect VAR
İKAME         üç eşikte koşulur: -50 / -40 / -30 dB; hiçbirinde aralık yoksa TESLİM KUSURU
BEKLENEN      118,0-120,0 s tek aralık · filmin başka hiçbir yerinde mutlak sıfır 0 s

E4 · İHRAÇ SESİ
KAPI          integrated loudness ve true peak
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · ebur128 VAR
İKAME         yok — bu kapı ikamesizdir, ölçüm yapılmadan teslim edilmez
BEKLENEN      -14 LUFS (kabul -14 … -15) · true peak ≤ -1,0 dBTP
              ⛔ KEPT_LIGHT -16,4 LUFS / +0,9 dBTP teslim etti ve hiçbir mercek görmedi

E5 · IZGARA (kesme saniyeleri 10,0'ın katı mı)
KAPI          kesmelerin 10,0 s ızgarasına oturması · klip sayısı 24
KOMUT         ffmpeg -hide_banner -i "$M" -vf "select='gt(scene,0.3)',metadata=print" -f null - 2>&1 | grep pts_time
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · select VE metadata VAR
İKAME         karanlık kesmeler görünmezse 5, 15, 25 … 235 s karelerinden 24'lük döşeme
BEKLENEN      tespit edilen her kesme 10,0'ın katı (±0,15 s) · toplam 23 kesme

E6 · FİLİGRAN KÖŞE TESTİ
KAPI          sağ alt çeyrekte tekrar eden bir işaret var mı
KOMUT         for t in 20 60 100 140 180 220; do ffmpeg -hide_banner -ss $t -i "$M" -vf "crop=iw/2:ih/2:iw/2:ih/2" -frames:v 1 kose_$t.png -y; done
DOĞRULANDI    ffmpeg 8.1 · 25.09.2026 · crop VAR
İKAME         yok — göz sınavı
BEKLENEN      altı örneğin altısında aynı yerde aynı şekil YOK (0 filigran)
```

---

## 👁️ GÖZ KAPILARI — beş soru, beşi de KAREYLE cevaplanır

> Betik bunları ölçmez; operatör bakar. Her satır bir SAYI sorar.

```
G1 · KÜRE (filmin 1 numaralı riski) — kare 5,0 s · 15,0 s · 205,0 s
   □ kürenin kenarı tek karede takip edilebiliyor mu (keskin mi)
   □ çevresinde korona / ışın / lens parlaması: 0 kare mi
   □ küre ile kamera arasındaki hava pus ve hale taşımıyor mu
   □ yüzeydeki parlak hücreler ~4 saniyede bir genişlik mi
   ⛔ Üç denemede de ateş topu geliyorsa İPTAL KAPISI devreye girer (PLAN B)

G2 · VİZÖR BİÇİMİ — kare 25,0 s · 115,0 s · 165,0 s
   □ ön pane TEK ve DÜZ mü · çerçeve kalın ve koyu mu
   □ kubbe / balon / çerçevesiz sarma: 0 klip mi
   □ yüz panenin içinden okunuyor mu (yansıma yalnız üst kenarda tek çizgi)
   ⛔ İkinci üretilen klipte kubbe görülürse ÜRETİM DURUR ve karar sahibe döner

G3 · KÜRENİN KADRAJI TERKİ — kare 205,0 · 206,0 · 207,0 · 208,0 s
   □ 206,0 s'de kürenin alt kenarı üst kadraj çizgisini geçmiş mi
   □ 208,0 s'de küre kadrajda YOK mu · geri dönüyor mu (dönmemeli)
   □ kendi genişliğini ~2 saniyede geçiyor mu

G4 · HİLAL YANIK İZİ — kare 75,0 s · 105,0 s · 115,0 s
   □ iz SOL eldivenin SIRTINDA, parmak eklemlerinin üstünde mi
   □ iki parmak genişliğinde mi · giysinin başka yerinde iz VAR mı (olmamalı)
   □ K11'in levhasındaki resimdeki eldivende AYNI iz okunuyor mu
   ⛔ Bu üç kare filmin kanıt zincirinin tamamıdır; biri düşerse K11 anlamsızlaşır

G5 · SON KARE — kare 236,0 s · 239,9 s
   □ oyuğun içinde TEK filiz var mı (1 adet · üç yaprak · bir parmak boyu)
   □ oyuğun kenarındaki kırağı yerinde mi (erimemiş, çekilmemiş)
   □ 239,9 s'den sonra kart / yazı / siyah: 0 kare mi
```

---

## 🧱 YANLIŞ-POZİTİF DUVARI — burada İLAN EDİLEN karar ihlal olarak yazılamaz

> ⑬ UYUM ve ② ③ ⑤ ⑨-⑫ merceklerinin FLAGS soruları buradan cevaplanır.
> Her satır bir TASARIM KARARIDIR ve ölçülmüş bir kayda dayanır.

```
① 6 KLİPTE İNSAN YOK (K01 · K02 · K04 · K11 · K21 · K24) ve o altı klibin NEGATIVE bloğu
   KISALTILMIŞTIR; insan sayısı cümlesi bilerek YAZILMAMIŞTIR.
   Kayıt: üretim red defteri satır 2 — "insansız sahne + uzun NEGATIVE +
   Exactly 0 human figures" deponun tek ölçülmüş YAPISAL REDDİ; geçen çözüm
   "NEGATIVE tek pozitif satıra indi" idi. ⛔ Bu bir eksik değil, o çözümdür.

② ANA IŞIK ELDE TAŞINIR ve kadının hareketiyle döner (S02-S06). ⑪ IŞIK merceği
   bunu "KEY WALKS" diye yazarsa bulgu DÜŞER: yön SAATLE değil KAYNAKLA
   kilitlendi ("her own lamp, at her own chest height").

③ IŞIK TAKVİMİ MONOTONİK DEĞİL — S07'de ARTAR. Artış filmin OLAYIDIR ve
   PLAN'ın Lighting Bible'ında ilan edilmiştir. "Işık geri yandı" bulgusu ancak
   K01-K18 arasında geçerlidir.

④ KÜRE HAVADA DURUR ve bu filmin TEK kurmaca kuralıdır (C bloğu NOVUM).
   Küre DIŞINDA hiçbir şey havada durmaz. "Two gravities" hükmü ancak küre
   DIŞINDAKİ bir nesne için yazılabilir.

⑤ "still" kelimesi pozitif gövdede 42 kez geçer; 24'ü ŞABLONUN KENDİ ifadesi
   ("the approved still" = onaylı KARE, bir isim), 18'i zarf ("hâlâ"). Yasak
   olan DURUM kelimesi ("holds still", "motionless") 0 kez geçer.

⑥ 0 REPLİKLİ SAHNE 22 KLİP · tek replik iki klipte duyulur ve bir CİHAZDAN
   gelir. Kadrajda konuşan ağız 0 klip. "Karakter neden konuşmuyor" bir bulgu
   değildir: sesin ağzı bu dünyada kalmadı (bedenleşme yapısal olarak imkânsız).

⑦ SABİT 10,0 s IZGARA ve 0 kırpma bilinçli sapmadır [D74] — §2.3 modülü.
   ASL eğrisi UYGULANAMAZ. "Tempo düz" bulgusu ızgaranın kendisine yazılamaz;
   yazılacaksa kadraj İÇİ değişkenlere yazılır (ölçek · kurulum · beden).

⑧ GEMİ 40 m ve K02/K21'de kadrajın (37,5 m) DIŞINA taşar. "Gemi kadraja
   sığmıyor" bir ölçek hatası değil, kasıtlı bir okunurluk kararıdır.

⑨ K06'da kamera ARKADADIR ve sırt pozitif cümlesiyle yazılmıştır. Filmde
   sırtı gören BAŞKA klip yoktur; "sırt hiç görünmüyor" bir bulgu değildir.

⑩ AMBLEM/ARMA HİÇBİR YÜZEYDE YOK. İmparatorluk yalnız BİÇİM olarak var
   (kaburga + üç halka). "Kimlik işareti eksik" bulgusu D138 ve üretim red
   defteri satır 3 gereği DÜŞER.
```

---

## ⛔ OPERATÖRE TEK SATIR

```
Bu dosya rubriğin BAŞINA yapıştırılır. Yapıştırılmadıysa koşu MOD V'dir ve
T tablolarına GİREMEZ [D129]. Depoda SPEC yazılmış olduğu hâlde mod V koşulan
film sayısı 13'tür; ikisi bu filmin okuma listesindeydi.
```
