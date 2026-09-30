# 📋 SUSMAYAN_NOBETCI — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `SUSMAYAN_NOBETCI_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
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
FILM:              SUSMAYAN_NOBETCI
FORMAT:            16:9 · yatay 8 dk · 48 scenes × 10 s
RUNTIME:           480 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       48
PART GRID:         ⬜ OWNER DECISION (K1). Proposal — four quarters, `--bolum n/4`:
                   P1 = S0-S11 · 12 clips · 0-120 s · P2 = S12-S23 · 12 clips · 120-240 s ·
                   P3 = S24-S35 · 12 clips · 240-360 s · P4 = S36-S47 · 12 clips · 360-480 s
                   (alternative: two halves S0-S23 / S24-S47, `--bolum n/2`).
                   Paste with the rubric: "THIS FILE IS PART n OF 4 — judge only these clips."
                   BOUNDARY PAIRS closed by hand frames: S11↔S12 · S23↔S24 · S35↔S36.
THEME:             IDENTITY OF THE MACHINE — war goes on inside machines after the people who started it are gone.
THEME SCENES:      S3 · S17 · S31 · S44 · S47
INTENDED EMOTION:  cold dread that turns into steady resolve; relief paid for in the open at the end
ENDING TYPE:       ambiguous — the people are safe, the machine keeps scanning
PROTAGONIST:       unnamed tug pilot — a woman in her mid-forties, off-white industrial pressure suit, orange band on the left arm
CENTRAL CHOICE:    S29 — she pulls the release lever and sends her own escape capsule out as a decoy
DIALOGUE LINES:    0 in the clips · POST-DUB LINES: 8 · register: HUMAN 8 / MACHINE 0
                   (radio 7 · in-helmet 1; every line is added after the cut, no quotes in any prompt)
SILENT SCENES:     S0 · S3-S6 · S8 · S10-S13 · S15-S26 · S28-S45 · S47 (no spoken line; room tone and breath always present)
VIRAL INTERSTITIALS: S44  ⛔ THESE MAY NOT BE CUT
UNCUTTABLE:        S0 · S3 · S4 · S15 · S16 · S29 · S30 · S36 · S37 · S44 · S45 · S46 · S47
TITLE:             "Don't Light the Engine" — promises that the engine is the danger, and the first ten seconds deliver it
LIBRARY CONTEXT:   same shelf as THE_HARD_DOCK (docking, 24 × 10 s) and KRONOS_SON_SINYAL (8 min, orbital station)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      48 (+0 standby)
SHOT COUNT:      48 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s fixed grid · ASL CURVE: none
                 ⛔ GEREKÇE [D74]: sahne = çekim = klip sabit ızgara; kırpma bütçesi yok, ritim
                 kadraj içinden gelir (KURGU_RITMI §0 ②). Değişken süre yazılmadı.
GRID:            sahne başlangıcı(n) = 0 s hook + n × 10 s klip   (hook S0'ın İÇİNDE)
RUNTIME:         480 s (±2 s)
RAW FOOTAGE:     48 clips × 10 s = 480 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0.0 saniye (jenerik · başlık kartı · kapak çıktısı dâhil)
CAMERA:          48 / 48 sabit lockoff · klip içi kamera hareketi 0
SETUP SEQUENCE:  A B I C C A C I Y F C I C F C J J C I G I C E C I Q Q F H E T E T A B I K K A L M N M Z E Z R Z
KURULUM İSKELETİ: A B I C C A C I Y F C I C F C J J C I G I C E C I Q Q F H E T E T A B I K K A L M N M Z E Z R Z
KÜME:            4 küme — S3-S4 (C) · S15-S16 (J) · S25-S26 (Q) · S36-S37 (K) · ≥2 ✅
DÖNÜŞ:           20/48 = %42 ≥%40 ✅ (S4 S6 S10 S11 S12 S13 S14 S16 S17 S20 S21 S23 S24 S26 S31 S32 S37 S42 S45 S47)
ANGLE ARC:       7 açı tipi — OTS · profil · üst açı · göz hizası · alt açı (≥3 ✅)
DORUK:           S36 → S37 (sahne başlangıcı 360 s · temas 364,0 s) · bedel S45 (450-453 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 0 s hook + n × 10 s + promptun TIMELINE ofseti
   R1 S1 12,0 · R2 S2 25,0 · R3 S7 73,0 · R4 S9 94,0 · R5 S14 141,5 · R6 S14 144,0 · R7 S27 272,0 · R8 S46 465,0
   ⚠️ Klip süresi ffprobe ile ölçülünce (K3) hepsi yeniden hesaplanır.

FİNAL VURUŞ KANITI [D141]:
   empty capsule cradle on the tug's left flank · 474,0 s · 1 tane · BULUNAN
   rescue ship's burning engine cone, far left · 474,0 s · 1 tane · BULUNAN (and never struck)
   satellite's white light sitting on the planet's edge, half cut off · 474,0 s · 1 tane · BULUNAN
   ffmpeg -ss 474 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: RHYME PAIR = event, not setup — S0 (a burning engine is struck) ↔ S47 (a burning engine is not struck);
   kurulum dönüşü S43 ↔ S45 ↔ S47 (Z, birebir aynı kamera cümlesi). ⚠️ SAHİP KARARI: açılış A (kokpit),
   kapanış Z (dış geniş) — aynı kamera DEĞİL [D74 ③].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  11111111--111-1--11-1111111-11-1-111111-111-1-2-
       (1 = insan var · - = insansız · 2 = S46: pilot + ikinci insanın eldiveni ve ön kolu · sahne başına bir karakter)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         1 (S46'da 2: pilot + kadraj kenarından giren tek eldiven ve ön kol) · 48/48 sahnede ilan edildi
KASK          vizör optik berrak, tek düz ön pane kalın koyu çerçeve içinde, yüz her karede okunur · sırt ünitesi YOK,
              sırt tek sürekli nervürlü yüzey [D79] · kask kapalı S0-S45, AÇIK yalnız S46 (sahneye açık girer)
NOVUM         a war-era satellite strikes anything that lights an engine within 3.0 s; it cannot fire while its two
              radiator wings are folded out (≈15 s window). İhlali: motor ateşleyen gövde vurulur, kanatlar açıkken vurulmaz.
YERÇEKİMİ     0 g · film boyu tek değer; ateşleme sırasında kabinde tek yön (kıça doğru)
ATMOSFER      yok (vakum) · dış ses 0; iç hacimlerde kabin havası var
EKRAN YÖNÜ    hedef (tahliye gemisi) hep ekran SAĞINDA, çekici SOLDA · uydu ışığı SAĞ ÜST · gezegen kenarı ALT ·
              48 sahnenin 48'inde sabit; S36-S37 kamera eksende (nötr çekim, çekici kameraya gelir)
HAREKET KİLİDİ eller: tek jest (kol · kapak · kelepçe) · ayaklar 0 g'de yere basmaz, tutamak kullanılır ·
              baş: bakış nesneye kilitlenir, kameraya dönmez
SAYAÇ         K1 uydu kanatları AÇIK/KAPALI (S3 açık · S4 kapanır · S5 açık · S17 açılır-kapanır · S31 açık · S32 kapalı · S44 kapalı)
              K2 soğuk gaz ibresi ¾ (S6) → ½ (S12) → dibe bir parmak (S21) → dip (S33) · monotonik
              K3 tahliye penceresinde yanan fener 3 (S1) → 2 (S23) → 1 (S26) → 0 (S38) · monotonik · yalnız sınırda değişir
              K4 uydu ışığının gezegen kenarına yüksekliği ¼ (S8) → 1/12 (S43) → 1/20 (S45) → 0, yarısı kesik (S47) · monotonik
              K5 kapsül yuvası DOLU (S0-S29) → BOŞ (S30-S47) · geri dolmaz
EŞ KADRAJ     S43 ↔ S45 ↔ S47 (Z) · S0 ↔ S5 ↔ S33 ↔ S38 (A) · S36 ↔ S37 (K küme)
DÜNYA ÇAPASI  3/3 — "A flat black sky with no stars." · "The curved bright edge of a large rust-and-grey planet crosses
              the lower part of the frame." · "One small steady white light hangs above that edge on the right and blinks
              once every two seconds." (World Bible'daki üç cümle BİREBİR; dış promptlarda sıfır sapma) [D209]
YIPRANMA      1 sabit bölge — sağ eldiven avucunda parlak sürtünme izi, başlangıç S42, geri temizlenmez [D42]
KİMLİK DİZİSİ kask K×46 + A×1 (S46) + K×1 (S47 insansız, kask kadrajda yok → -) →
              KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKAK
              amblem: turuncu bant SOL pazu + SOL uyluk (48/48) · giysi rengi kırık beyaz kanvas ·
              kir: global mat toz sabit · hasar: eldiven sürtünme izi S42'den sonra (geri dönmez) [D208]
IŞIK TAKVİMİ  sabit — güneş kadraj dışı sol üstte, film boyu tek yön; iç mekân 4500K; takvim yok (gerçek zaman ~8 dk).
              Pratik ışıklar yalnız sayaç K3 ile değişir; monotonik ✅
SES REGISTER  HUMAN 8 (7 telsiz band-pass + 1 kask içi) · MACHINE 0 · replikler post-dub, klipte üretilmez
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Filtre varlığı 18.09.2026'da bu makinede ölçüldü (ffmpeg 8.1 · `ffmpeg -hide_banner -filters`).
> ⚠️ `vidstabdetect` KURULU DEĞİL — kamera sabitliği ona yazılmadı.

```
KAPI          clip length / grid [D124] — every accepted clip's duration; the GRID and all eight post-dub seconds depend on it
KOMUT         for f in S*.mp4; do printf "%s " "$f"; ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"; done
DOĞRULANDI    ffprobe 8.1 · 18.09.2026 (tool present; no clip produced yet)
İKAME         —

KAPI          cut grid — cuts in the master fall only on n × clip (48 scenes → 47 cuts)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "scdet=threshold=10,metadata=print" -f null - 2>&1 | grep -o "lavfi.scd.time=[0-9.]*"
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filter scdet present
İKAME         -vf "select='gt(scene,0.3)',showinfo" (select + showinfo present)

KAPI          hit form [D192 · film's number one risk] — each strike is one flash under 0.25 s with no afterglow;
              luma peak at 3.0 s of S0 · S4 · S15 · S30 · S45 must last ≤6 frames and return to the pre-flash level
KOMUT         for t in 3 33 153 303 453; do ffmpeg -v error -ss $t -t 2 -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX" -f null - 2>&1 | tail -20; done
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filter signalstats present
İKAME         frame-by-frame export: ffmpeg -ss <t> -t 1 -i "$M" -vf fps=25 kare_%03d.jpg → count bright frames by eye

KAPI          exterior silence — in vacuum scenes the only audio is the radio bed; a hit must add no exterior sound
KOMUT         ffmpeg -ss 150 -t 20 -i "$M" -af astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filter astats present
İKAME         ebur128 (present) short-term loudness around the hit seconds

KAPI          loudness and the post-hit silence window — master −14 LUFS / −1 dBTP; 453-455 s carries the cut's 2 s of
              designed silence, and the cabin bed stays above digital zero
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12 ; ffmpeg -ss 450 -t 10 -i "$M" -af silencedetect=n=-60dB:d=0.3 -f null - 2>&1 | grep silence_
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filters ebur128 + silencedetect present
İKAME         astats (present)

KAPI          frozen clip — held scenes (S3 · S8 · S9 · S32 · S43 · S47) must keep motion (blinking light, swinging lamp, drift)
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=0.003:d=4" -map 0:v -f null - 2>&1 | grep freeze_
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filter freezedetect present
İKAME         mpdecimate (present)

KAPI          black frames and screen text — black allowed only after S47; no title card anywhere
KOMUT         ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.2:pix_th=0.10" -an -f null - 2>&1 | grep black_start
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filter blackdetect present
İKAME         —

KAPI          in-clip camera stillness (lockoff) — frame difference inside a clip comes only from the subject
KOMUT         ffmpeg -v error -ss 365 -t 10 -i "$M" -vf "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | tail -3
DOĞRULANDI    ffmpeg 8.1 · 18.09.2026 · filters tblend + signalstats present (vidstabdetect NOT installed — not used)
İKAME         hand check of the first and last frame against the planet's edge line
```

## 🅵 F BLOĞU — GÖZ KAPILARI (insan gözüyle, koşudan sonra)

```
F1  VURUŞ BİÇİMİ   5 vuruşun 5'inde: ışın/mermi 0 kare · çakma ≤6 kare · ayrılan parça dönüşünü sürdürüyor ·
                   buz kristali konisi düz ve ≤2 s · alev/duman 0 kare        (S0 · S4 · S15 · S30 · S45)
F2  TEMAS          S36'da iki halka çarpışıyor ve çekici geri sekiyor; hiçbir gövde diğerinin içinden geçmiyor
F3  SAYAÇLAR       fener 3→2→1→0 ve uydu ışığının kenara yüksekliği ¼→1/12→1/20→0: değerler yalnız kesmede değişiyor
F4  KAPSÜL YUVASI  S29'da dolu, S31 · S32 · S44 · S47'de boş — aynı kadrajda okunuyor
F5  KASK BİÇİMİ    46 klibin hepsinde tek düz ön pane + kalın koyu çerçeve; kubbe/balon 0 kare (referans paketi YOK)
F6  İKİNCİ İNSAN   yalnız S46'da bir eldiven ve ön kol; başka hiçbir karede ikinci gövde, gölge ya da yansıma yok
```
