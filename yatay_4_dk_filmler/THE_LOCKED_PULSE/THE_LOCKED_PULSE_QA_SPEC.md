# 📋 THE_LOCKED_PULSE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI. Operatör `QA_PROMPTLARI/_KAYNAK/`
> rubriğini açar ve **BU DOSYAYI RUBRİĞİN BAŞINA YAPIŞTIRIR.** Mod D'yi taşıyan tek şey budur.
> ⛔ Her mercek TEMİZ oturumda, AYNI master dosyasıyla koşulur [D110 · 6 vaka].

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_LOCKED_PULSE_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (6 MAKİNE repliği · 0 insan repliği ·
> sabit lockoff · tasarımlı sessizlik S20 · metinsiz sayaç · S13 insansız dış · S22+ çıplak sağ el)
> ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V   (Ⓥ satırı geçerlidir — 11.09.2026 politikası)
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]: İNSAN · EKRAN YÖNÜ · SAYAÇ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D   (NUMERIC LOCK LIST aşağıda)
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C (BEAT/COST STRING)  MOD D
⑨ 🎯 KADRAJ · ⑩ 🎭 OYUNCULUK · ⑪ 💡 IŞIK · ⑫ 🪝 HOOK → A + B + C (kurulum iskeleti · çapa üçlüsü · ışık takvimi · hook tipi)  MOD D
⑬ 🧩 UYUM       → bu SPEC + URETIM_DEFTERI + sahne_kapisi.sh + bölüm promptları BİREBİR
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_LOCKED_PULSE
FORMAT:            16:9 horizontal · 3-5 min band · 25 scenes
RUNTIME:           249.0 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       25  (S0 hook 9 s + S1-S24 × 10 s)
THEME:             İNSAN-MAKİNE (HUMAN–MACHINE BOUNDARY: the point where a machine's correct calculation counts the human as a part)
THEME SCENES:      S2 · S10 · S12 · S18 · S22 · S24     ⛔ en az üç (yazılmayan tema dekoratif)
INTENDED EMOTION:  controlled dread → weight → a quiet, costly refusal → the machine's ledger closes on him
ENDING TYPE:       TWIST + planted seed — S2 seed (seven lamp sockets, six lit) pays at S23 233.0 s (seventh lamp lights: the machine counts
                   his abandoned glove as the seventh sealed pod); final frame rhymes S0 (same setup A); one open question: will anyone come
PROTAGONIST:       an unnamed maintenance engineer, alone (no proper name anywhere [D34]); man, forties, medium olive-brown skin,
                   heavy brow ridge; slate-grey quilted industrial pressure suit, one amber band LEFT upper arm + LEFT thigh; helmet ON 25/25
CENTRAL CHOICE:    S20 · 199.0-209.0 s — his left hand stops a palm's width short of the small yellow-and-black wheel (ring brake), holds two
                   seconds, opens, withdraws: he does NOT brake the ring (braking would free his wrist and warm the six pods)
DIALOGUE LINES:    6 · register: HUMAN 0 / MACHINE 6 (ceiling speaker ×5, radio ×1) — all off-screen; mouth never in frame while a line plays
                   #1 S1 11.0 s · #2 S6 61.0 s · #3 S9 92.0 s · #4 S12 125.0 s · #5 S13 132.0 s · #6 S18 181.0 s (last line; S19-S24 silent)
                   cevaplı/cevapsız: 6/6 CEVAPLI — cevap kanalı BEDEN (dinleyen kadrajı: S1 sırt · S6 WS · S9 alt açı kask · S12 insert omuz · S13 — · S18 sırt)
SILENT SCENES:     S0 S2 S3 S4 S5 S7 S8 S10 S11 S14 S15 S16 S17 S19 S20 S21 S22 S23 S24 (19) — no voice; bed + SFX + breath only
VIRAL INTERSTITIALS: S4 · S10 · S17 · S22  ⛔ THESE MAY NOT BE CUT
MAY NOT BE CUT (all): S0 · S2 · S4 · S10 · S12 · S13 · S17 · S20 · S22 · S24
TITLE:             THE LOCKED PULSE — promises a lock (wrist ring / port collar) and a pulse (the alarm, the ring's spin)
LIBRARY CONTEXT:   same shelf: THE_COUNTED_TURN (§3.7 ring, 3-5 min) · THE_HARD_DOCK (machine voice, 3-5 min) · THE_HEAVY_SIDE (ring, shorts) ·
                   THE_STATIC_SHADOW (machine voice + cost, 2-4 min)
HOOK TYPE:         in medias res — hands already on the wheel; S0 question: "why does the floor curve up, and why can't he turn that wheel?"
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s   ASL CURVE: flat (9 s hook + 24 × 10.0 s)
                 GEREKÇE [D74]: sabit ızgara — 25/25 lockoff, her sahne kendi onaylı imajından I2V; kurgu planı aşmaz;
                 tempo değişimi kesme sıklığıyla değil sahne İÇİ tempoyla (TEMPO sütunu Y/N/H) kurulur
GRID:            sahne başlangıcı(n) = 9 hook + (n−1) × 10 klip     (S1 = 9.0 · S12 = 119.0 · S13 = 129.0 · S20 = 199.0 · S24 = 239.0)
RUNTIME:         249.0 s ± 2
RAW FOOTAGE:     25 × 10.0 s = 250.0 s · TRIM BUDGET: 1.0 s (hook S0 10 → 9 s)
SCREEN TEXT:     0.0 saniye (jenerik kartı DÂHİL · filigran 0)
CAMERA:          25 / 25 sabit lockoff (S13: hub'a kilitli dış kamera, yapıya göre sabit)
SETUP SEQUENCE:  A B C D C E E C D H C G D X D G G J B J M A C C A
KURULUM İSKELETİ: A B C D C E E C D H C G D X D G G J B J M A C C A   (PLAN'daki ile AYNI)
KÜME:            3 · S5-S6 (E) · S15-S16 (G) · S22-S23 (C) — her biri 2 klip
DÖNÜŞ:           11 / 25 = %44 (12+ sahnede ≥%40; dönüş = kaynağından ≤3 sahne sonra)
ANGLE ARC:       6 açı TİPİ (eye-level · over-the-shoulder · side-on insert · low · high · dutch)
DORUK:           S20 → el fren çarkının bir avuç önünde durur, geri döner (sahne başlangıcı 199.0 s; duruş 203.0-205.0 s)
CHAPTER SPLIT:   S12 | S13 (BOLUM_1 13 sahne · BOLUM_2 12 sahne) — bölüm sınırı bilinçli ŞOK #1 (CU insert → EWS dış)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti
   #1 S1: 9+0+2.0 = 11.0 · #2 S6: 9+50+2.0 = 61.0 · #3 S9: 9+80+3.0 = 92.0 · #4 S12: 9+110+6.0 = 125.0 · #5 S13: 9+120+3.0 = 132.0 · #6 S18: 9+170+2.0 = 181.0
   doruk duruşu: 9 + 190 + 4.0 = 203.0 → 205.0 · kilit: 9 + 110 + 4.0 = 123.0 · mühür: 9 + 210 + 5.0 = 224.0 · 7. lamba: 9 + 220 + 4.0 = 233.0

FİNAL VURUŞ KANITI [D141]:
   BULUNAN: seven lit lamps in the horizontal row above the hand-wheel · 249.0 s (any frame 233.0-249.0) · TAM 7 (S0-S22: 6 lit + 1 dark)
   BULUNAN: one empty right glove seated in the port collar · 249.0 s · TAM 1 (its cuff open; no hand in it)
   BULUNMAYAN: no glove on the hand-wheel · 249.0 s · 0   (S0: two gloves on the wheel)
   ffmpeg -ss 248 -i "$M" -frames:v 1 kanit.jpg   → BAK: lamba say (7) · yakada eldiven (1) · çarkta el (0)
DÖNGÜ KANITI (3-5 dk = KAFİYE, döngü değil): ilk kare ↔ son kare — aynı kurulum A · aynı ölçek WS · aynı ışık yönü · TEK değişken nesne
   (eldiven yakada + 7 lamba) + gerekçeli ikincil (kayış 4.0 → 2.0 s · diz çökmüş → oturmuş). Arkasına eklenen her kare kafiyeyi öldürür.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111-11111111111     (1 = insan var · - = insansız · sahne başına bir karakter; S13 = '-' bilinçli dış Overview)
       ⚠️ tek figürlü filmde şerit SIRA kontrolü için KÖRDÜR [D163] — sıra kontrolü replik ekseni (6 anons) + durum ekseni ile:
       jet VAR S3-S8 · jet YOK S10+ · eldiven YAKADA S22+ · lamba 7 S23+
DAVRANIŞ ŞERİDİ:  G R G D T G G G G R G G R - D D S T R S K R B R B   (G görev · T tereddüt · D deneme · K karar · B bedel · R tepki · S sükûnet)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 (S13: 0) · klon 0 · yansıtıcı yüzey 0 (paneller mat, vizör yansımasız) · biniş/iniş/kapı geçişi 0 kare
KASK          KAPALI 25/25 · vizör OPTİK BERRAK 25/25 (zero tint, zero mirror) · görünür kalın koyu çerçeve + bronz yaka halkası ·
              sırt ünitesi YOK — sırt "one continuous ribbed surface from collar to hip, closed and smooth, carrying nothing" [D79/D139]
              ELDİVEN: iki eldiven S0-S21 · S22 224.0 s sağ bilek halkası açılır, sağ eldiven PORT YAKASINDA KALIR · S22-S24 sağ el ÇIPLAK (planlı)
NOVUM         kural: bu halkada ağırlık dönüş hızıdır; makine basıncı korumak için hızı artırır (2.0 → 4.0 RPM), her şey ağırlaşır ve
              bırakılan hiçbir şey düz düşmez (yana iner — ekran-SOL, film boyu tek yön). İhlali: düz düşen / süzülen / sağa inen nesne.
              ⛔ SINIR: kural yalnız SERBEST BIRAKILAN nesneye uygulanır — duran kayış RADYAL sarkar (eğik DEĞİL), zemindeki nesne KAYMAZ,
              yürüyen adam savrulmaz (yalnız adım genişliği), halka içi duvarlar sabit. "Kayış eğik değil" veya "adam düz yürüyor" bulgu DEĞİLDİR.
              ⛔ Bilek kilidi ihlal DEĞİL, sonuçtur (port yakasının basınç kilidi, mekanik).
YERÇEKİMİ     dönme g · R 56.0 m · 2.0 RPM 0.25 g (S0-S1) · 2.5 RPM 0.39 g (S2-S5) · 3.0 RPM 0.56 g (S6-S8) · 3.5 RPM 0.77 g (S9-S12) ·
              4.0 RPM 1.00 g (S13-S24, SPIN HOLD) — monotonik ↑, yalnız sahne SINIRINDA; tek karede tek g [D200]; S13 dış vakum, yapı rijit
ATMOSFER      iç: basınçlı, ses taşır (fan yatağı) · dış S13: vakum, ses 0, gölge mutlak siyah, süzülen parçacık 0, gezegen 0
EKRAN YÖNÜ    hedef (vana istasyonu) hep +Y duvarında: A'da SAĞ üçte bir · E'de sol-uzak · B/C/G/J'de karşıda (sol yarı) · kamera tarafı film
              boyu koridorun −Y (kayış) tarafı — 24/24 iç sahnede sabit · düşen nesne ekran-SOL 2/2 (S2 · S15)
SAYAÇ         monotonik, metinsiz: ① kayış salınım periyodu 4.0 s (S0) → 2.0 s (S21/S24) ↓ · ② alarm periyodu 2.0 (S0-S5) → 1.5 (S6-S12) → 1.0 s (S14-S24) ↓
              · ③ lamba dizisi 7 yuva: 6 yanık + 1 sönük (S0-S22) → 7 yanık (S23 4.0 s = 233.0 s +) — tek geçiş ↑ · ④ jet 0.20 m (S3) → 0.10 (S8) → 0 (S10 6.0 s)
              · ⑤ düşüş süresi anahtar ~0.7 s (S2) → levye ~0.4 s (S15) ↓ · ⑥ RPM/g ↑ (yukarıda)
EŞ KADRAJ     S0 ↔ S24 (kurulum A, kamera cümlesi birebir; değişen: eldiven yakada · 7 lamba · kayış hızı · duruş) · S1 ↔ S18 (B) · S17 ↔ S19 (J)
              · S3 ↔ S8 ↔ S12 ↔ S14 (D) · S11 ↔ S15 (G)
YIPRANMA      kir GLOBAL sabit ("even matte dusting of grey grit") · takvim YOK · sabit bölge 0 (özel iz yazılmadı) [D42/D147]
IŞIK TAKVİMİ  alarm periyodu 2.0 → 1.5 → 1.0 s monotonik ↓ (değişim S5|S6 · S13|S14) · tavan paneli nötr sabit · kask içi fill sabit ·
              KEY DIRECTION STRING (kuruluma bağlı): A/C/D/J/M üst-sol · B üst-arka · G tepeden · H kaynak kadrajda · E üst sıra · X güneş sağ üst
              ⛔ ⑪ IŞIK: aynı kurulum harfinde ışık yönü değişimi BULGU; farklı kurulumlarda yön farkı TASARIM
SES REGISTER  HUMAN 0 · MACHINE 6 (düz sentetik, tavan hoparlörü ×5 + telsiz ×1) — sentetik düzlük TASARIMDIR, ceza değil · yatak: fan+pompa uğultusu
              24/24 iç sahne kesintisiz (dijital sıfır 0 s) · S13 dış: yatak YOK (vakum), yalnız telsiz · S20: HARD MUTE 203.0-205.0 (kurguda) ·
              müzik: yok S0-S1 · anempatik nabız 72 BPM 19.0-197.5 · yok 197.5-241.0 · çözülmemiş akor 241.0-249.0
PROP          çark Ø ~0.30 m (helmet-wide) · port yakası Ø 0.15 m (= bilek halkası) · fren çarkı Ø 0.25 m zemin, sarı-siyah bant · lamba Ø 0.12 m × 7 ·
              kayış L 1.0 m · anahtar 0.30 m · levye 0.50 m · alarm lambası 1 · dolap 1 · pencere 0 (iç) · halka 1 · spoke 4 · hub 1
```

### 🔢 NUMERIC LOCK LIST — ⑥ FİZİK mod D (PASS / FAIL / UNMEASURABLE / NOT EXERCISED)

```
L1  S2  anahtar bırakma→zemin süresi ≤ 1.0 s (plan 0.68 s · h 0.90 m · 2.5 RPM)         tolerans ±%20 → 0.55-0.82 PASS bandı, ≤1.0 kabul
L2  S2  anahtar iniş noktası bırakma noktasının ≥ 0.05 m ekran-SOLU (plan 0.11 m)        yön SAĞ = FAIL · sapma 0 = FAIL
L3  S15 levye bırakma→zemin süresi ≤ 0.5 s (plan 0.39 s · h 0.75 m · 4.0 RPM)
L4  S15 levye iniş noktası ≥ 0.05 m ekran-SOL (plan 0.08 m)
L5  S0  kayış tam salınım periyodu 4.0 s ± %25 (3.0-5.0)                                 kayış tek düz çizgi (dalgalanma = ① KARE bulgusu, ⑥ değil)
L6  S21/S24 kayış periyodu 2.0 s ± %25 (1.5-2.5) — L5'in en az %30 altında
L7  S13 yıldız alanı kadrajı 3.1 s ± %20'de geçer, tek yön, ters dönmez; halka/spoke 0 px hareket
L8  S5  adım kadansı 8 ± 1 / 7.5 s · yürüyüş "real time" (yavaş çekim = FAIL)
L9  S10 jet bitişi tek anlık (≤ 0.3 s), 6.0 ± 1.0 s'de; sonrasında sıfır kalıntı
L10 S12 yaka dış halkası çeyrek tur + tek tık 4.0 ± 1.0 s; sonrasında 0 hareket
L11 S23 yedinci lamba 4.0 ± 1.0 s'de tek anda yanar (≤ 0.2 s), titreme 0
L12 Zemindeki nesneler (anahtar S4-S24 · levye S16-S24) 0 px hareket — kayma = NOVUM SINIRI ihlali
```

### 🧍 ÇAPA ÜÇLÜSÜ — ⑩ OYUNCULUK "ANCHOR BEATS" / "THE CHOICE ON THE BODY" (`OYUNCULUK_YAZIM` §2)

```
CHOICE  S20 · 203.0-205.0 s · BEFORE: left glove's fingers a palm's width short of the small wheel's rim, still · AFTER: fingers open, hand drawn back
        out of frame; the wheel 0 movement — kanal EL (aynı kanal)
COST    S22 · 224.0 s · BEFORE: gloved right hand in the collar, wrist ring latched · AFTER: bare right hand on the chest plate, empty glove seated in the collar — kanal EL
FINAL   S24 · 239.0-249.0 s · BEFORE (S0 0.0 s): kneeling upright, two gloves on the wheel · AFTER: sitting on the deck, back to the wall, one glove, bare hand on chest — kanal DURUŞ + EL
GAZE STRING (25): O O O O A O O O O U O D O - O D A A D A - D D D D   (O nesne/çark · A yaka-lamba-fren (başka nesneye kayış) · D aşağı/bilek · U yukarı/tavan · - yok)
TEMPO: N Y N H Y N N N N Y N Y H Y H H Y Y N Y Y N H Y Y
COST CURVE (⑧ EFOR): 1 1 2 2 3 2 2 3 3 3 4 5 6 - 6 7 7 7 8 8 8 8 9 9 9 — RESET LOG: S5 3→2 (yük koldan indi, yürüyüş) — tek reset, gerekçeli
BEAT STRING (⑦, sahne başına 1 hane): S S R F T W W L L R S H C - P L S T R S K R O R S
        (S sabit iş · R tepki · F başarısız · T tereddüt · W yürüyüş · L levye · H tutuş · C kilit · P çekiş · K karar · O mühür açılır · - insansız)
```

### 🪝 HOOK / PAYLAŞIM — ⑫

```
HOOK TİPİ: in medias res · S0 SORUSU yukarıda · İLK 2 SN SESİ: fan/pompa uğultusu (tek diegetik) · müzik 0:00'da YOK
PAYLAŞIM ANLARI: S4 (0:39) · S10 (1:39) · S17 (2:49) · S22 (3:39) — her biri tek başına okunur (viral)
PLATO KONTROLÜ: aynı kurulumda ≥3 ardışık sahne 0 · aynı mekân/ölçekte ≥3 ardışık 0 (küme ≤2)
ÇIKIŞ: son kare S0'a döner (kafiye), kart 0, fade 0 · doruk yerleşimi %80-84
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142] — ffmpeg 8.1 · 13.09.2026 kuru koşu

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Kuru koşu: `ffmpeg -hide_banner -filters | grep -q " <filtre> "` — 13.09.2026, ffmpeg 8.1: silencedetect ✅ · freezedetect ✅ · signalstats ✅ ·
> ebur128 ✅ · select ✅ · showinfo ✅ · astats ✅ · hue ✅ · tile ✅ · blackdetect ✅ · **vidstabdetect ❌ (kurulu değil)** · scdetect ❌

```
KAPI ①       KURGU IZGARASI — 25 klip · sınırlar 9.0 + 10.0k
KOMUT        ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (select · showinfo)
İKAME        karanlık kesmede: silencedetect delikleri + kart başı; ayrıca ffprobe format=duration = 249.0 ± 2

KAPI ②       SÜRE / SAHNE SAYISI (⑤ SÜRE ekseni [D205] · ①.9 teslim [D188])
KOMUT        ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"  ·  bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh "$M" 10 25
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (ffprobe)
İKAME        —

KAPI ③       EKRAN METNİ / KUYRUK KARTI 0.0 s [D70/D72] · freezedetect ile kart şüphesi
KOMUT        ffmpeg -i "$M" -vf "freezedetect=n=0.003:d=2" -f null - 2>&1 | grep freeze_start  ·  ffmpeg -ss 248.5 -i "$M" -frames:v 1 son_kare.jpg → BAK
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (freezedetect)
İKAME        son 6 s'den 3 kare çıkar (tile=3x1), gözle: yazı/kart var mı — ⚠️ S24 held frame planlıdır: freeze S24 içinde (239-249) BULGU DEĞİL, 249'dan SONRA bulgudur

KAPI ④       FİLİGRAN köşe testi [D150] — 4 köşe × 6 örnek
KOMUT        for t in 5 60 120 180 230 245; do ffmpeg -ss $t -i "$M" -frames:v 1 -vf "crop=iw/5:ih/5:iw*4/5:ih*4/5" kose_SA_$t.png; done → aynı ikon ⇒ 🔴
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (crop)
İKAME        —

KAPI ⑤       SES KANALI + YATAK SÜREKLİLİĞİ [D83 · D136] — dijital sıfır 0 s (S20 hard mute hariç)
KOMUT        ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M"  ·  ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (silencedetect)
İKAME        astats RMS saniyelik eğri — ⚠️ 203.0-205.0 s PLANLI HARD MUTE: silencedetect burada bir aralık BULMALIDIR (bulmazsa 🔴 doruk teslim edilmedi [D180]);
             S13 (129-139) dış: yatak yok ama telsiz taşıyıcı hışırtısı var → mutlak sıfır beklenmez

KAPI ⑥       LOUDNESS −14 LUFS / −1.0 dBTP [KURGU_RITMI §6]
KOMUT        ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (ebur128)
İKAME        loudnorm print_format=summary

KAPI ⑦       KAMERA SABİTLİĞİ 25/25 lockoff [ADAY-40 · IRON SLOPE S2]
KOMUT        vidstabdetect ❌ KURULU DEĞİL → kapı İKAME ile yazıldı
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 — vidstabdetect YOK (grep sonucu boş); ikame filtreleri (select · tile · signalstats) ✅
İKAME        her klibin 0.5 s ve 9.5 s kareleri: ffmpeg -ss <t> -i "$M" -frames:v 1 -vf "hue=s=0" k.png → iki karede DUVAR PANEL KENARLARI ve ÇARK MERKEZİ
             piksel farkı ≤ 8 px (1080p); sapan klip 🔴 (kamera kaydı)

KAPI ⑧       IŞIK TAKVİMİ [D193] — alarm periyodu monotonik ↓ (2.0 → 1.5 → 1.0 s) · kırmızı kanal nabzı
KOMUT        ffmpeg -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=-" -f null - | awk üzerinden sahne ort/min/son-2s;
             kırmızı nabız: crop=bay bölgesi + signalstats (RAVG*) saniyelik eğri → tepe aralığı 2.0/1.5/1.0
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (signalstats · metadata)
İKAME        her sahnenin 5.0 s karesi tile=5x5 → gözle: takvim geri sardı mı (↑ = 🔴)

KAPI ⑨       FİGÜR ↔ ZEMİN KONTRASTI (A/C kurulumları) — YMAX−YMIN ≥ 110
KOMUT        ffmpeg -ss <t> -i "$M" -frames:v 1 -vf "signalstats,metadata=print" -f null - 2>&1 | grep -E "YMIN|YMAX"
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (signalstats)
İKAME        hue=s=0 gri ton karesi → silüet gözle ayrılıyor mu

KAPI ⑩       FİNAL VURUŞ KANITI + KİLİT KARELERİ [D141 · D125]
KOMUT        for t in 24 123 205 224 233 248; do ffmpeg -ss $t -i "$M" -frames:v 1 kanit_$t.jpg; done → BAK (anahtar solda · kilit · el geri · eldiven yakada · 7 lamba · final)
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026
İKAME        tile=3x2 tek levha

KAPI ⑪       DÜŞÜŞ ÖLÇÜMÜ L1-L4 (⑥ mod D)
KOMUT        ffmpeg -ss 22.5 -t 3 -i "$M" -vf "fps=10,tile=6x5" s2_dusus.png  ·  ffmpeg -ss 153.5 -t 2 -i "$M" -vf "fps=10,tile=5x4" s15_dusus.png → kare say (süre) + iniş noktası (yön/sapma)
DOĞRULANDI   ffmpeg 8.1 · 13.09.2026 (fps · tile)
İKAME        showinfo pts ile kare zamanı
```

## 🆗 F BLOĞU — GÖZ KAPILARI [D191] — her biri TEK KAREYLE kapanır

```
□ F1  S2  anahtar bırakıldığı noktanın SOLUNA indi (sağa/düz = 🔴 novum) — kare 24.0-25.0
□ F2  S3  jet DÜZ tek çizgi, bir karış, girdap 0 — kare 33.0
□ F3  S10 jet 6.0 s'de tek anda bitti, kalıntı 0 — kare 105.0 / 106.0
□ F4  S12 yaka dış halkası bilek halkasının ÜSTÜNE kapalı; tek bilek; iki ön kol yan yana 0; tepeden makro 0 — kare 123.5
□ F5  S13 halka + 4 spoke + hub; gezegen 0; yıldız tek yön; maket okuması 0 — kare 134.0
□ F6  S15 levye SOLA indi, zeminde kaldı — kare 155.0
□ F7  S17 · S20 el fren çarkına DEĞMEDİ; çark 0 hareket — kare 173.0 / 204.0
□ F8  S22 sağ eldiven YAKADA kaldı, çıplak sağ el göğüste, sol eldiven giyili, kask kapalı — kare 227.0
□ F9  S23/S24 lamba dizisi 7/7 yanık (S0-S22'de 6+1 sönük) — kare 233.5 · 248.0
□ F10 vizör 25/25 berrak + görünür çerçeve (kubbe 0) · sırt B/G/E kadrajlarında düz kapalı yüzey (ünite 0) — kare 15.0 · 65.0 · 115.0 · 185.0
□ F11 kayış: tek düz çizgi, salınım S0 ~4 s / S24 ~2 s; dalgalanma 0 — S0 · S24 tile
□ F12 ekran metni/kart/filigran 0 · S13 dışında pencere/yıldız 0 · ikinci insan 0 — kuyruk + köşe + rastgele 6 kare
□ F13 alarm periyodu S0 (2.0) > S6 (1.5) > S14 (1.0) — üç kısa klip sayımı
□ F14 çıplak deri yalnız S22-S24 sağ el; başka hiçbir karede (yaka · sol bilek · bilek-ayak) 0 — kare 100 · 150 · 227
```

## 🧾 KÜNYE — ölçüm kimliği [D160]

```
MASTER DOSYA ADI (beklenen):  the locked pulse.mp4   (⑪.0: ad kimlik değildir — orta kare çıkarılıp SPEC C'ye karşı BAKILIR)
KİMLİK ÇAPALARI (metin olmayan ≥2): ① S0/S24 kafiye kadrajı (kayış solda, bay sağda, sarı-siyah bantlı küçük çark zeminde) · ② 7 yuvalı lamba dizisi
  · ③ S13 halka + 4 spoke · ④ amber şerit SOL pazu · ⑤ eldiven yakada (S22+)
SPEC YAZIM: 13.09.2026 · yeni-film akışı · ffmpeg 8.1 kuru koşu aynı gün
```
