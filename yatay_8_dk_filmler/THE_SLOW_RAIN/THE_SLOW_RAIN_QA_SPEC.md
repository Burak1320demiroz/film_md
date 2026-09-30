# 📋 THE_SLOW_RAIN — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_SLOW_RAIN_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
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
FILM:              THE_SLOW_RAIN
FORMAT:            YATAY 16:9 · 8 dk · 48 sahne × 10 s · yazım 4 × 12 bölüm dosyası · QA birimi BÖLÜM (2 yarım)
RUNTIME:           480 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       48 (S0-S47)
PART GRID:         B1 = S00-S23 · 24 clips · 0-240 s · B2 = S24-S47 · 24 clips · 240-480 s. QA her yarıma AYRI koşar;
                   rubriğe SPEC'le birlikte "THIS FILE IS PART n OF 2 — S00-S23 / S24-S47" beyanı yapıştırılır;
                   BOUNDARY PAIR S23 ↔ S24 = 🕰️ KÜME (aynı kurulum R, işaretli devam klibi — sınırda sıçrama
                   BİLİNÇLİ olarak yoktur; ② bunu ihlal yazamaz), elle kareyle kapanır.
                   ⚠️ yazım dosyası 4 × 12 (sahip) — `sahne_kapisi.sh <yarım master> 10 24`, `rapor_kontrol.py --bolum n/2`.
                   (yalnız 6/8/16 dk hattı [§2.6/§2.7/§2.8]: n PART satırı — B1 = S00-S17 · 18 clips ·
                   0-180 s · B2 = S18-S35 · 18 clips · 180-360 s (6 dk) … 16 dk: B1-B4 × 24 clips ×
                   240 s + FULL = S00-S95 · 96 clips · 0-960 s. QA her parçaya AYRI koşar; rubriğe
                   SPEC'le birlikte "THIS FILE IS PART n OF m — …" beyanı yapıştırılır;
                   BOUNDARY PAIR(lar) elle kareyle kapanır. Diğer formatlarda "—" kalır)
THEME:             IDENTITY — "someone who exists by flying is still the same person when she walks home: the wing rack empty, the strap cut, her hand at her side"
THEME SCENES:      S1 · S10 · S15 · S19 · S25 · S29 · S45 · S47     ⛔ en az üç (yazılmayan tema dekoratif)
INTENDED EMOTION:  bittersweet pride (buruk gurur) — she brought the core home; she will never fly again
ENDING TYPE:       AMBIGUOUS · last shot returns to the first setup (RHYME, not loop): S0 glove raised to the drop ↔ S47 gloves at her sides; no title card, the take ends on the held frame
PROTAGONIST:       FLYER (rol etiketi, ad yok) — a lone heat-line maintenance worker on a cryogenic moon, wing rig on her back (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S15 (lays the wings flat, straps the core onto them — walks instead of flies) · COST S29 (cuts the core free, leaves the sunk wing rig in the pool)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0 — designed silent film; AUDIO line in every prompt is the environment's sound law
SILENT SCENES:     48 / 48 (no speech; sound design = dense-air ambience + drop ticks + contact thuds)
VIRAL INTERSTITIALS: S0 · S2 · S24 · S25 · S29 · S35 · S45 · S47  ⛔ THESE MAY NOT BE CUT (each carries FACE + MOTION lines in 00_SAHNE_TABLOSU)
TITLE:             THE SLOW RAIN — promises rain that falls slowly enough to watch, and a clock that hangs in the sky
LIBRARY CONTEXT:   yatay_8_dk_filmler: BENI_HATIRLAMA (identity via memory) · SUSMAYAN_NOBETCI · THE_FALLING_WORLD (güven, iki kişili) · KRONOS_SON_SINYAL; same environment card §3.9: THE_HEALING_GROUND (2 dk); same clock shape: THE_PAYLOAD (storm front)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      48
SHOT COUNT:      48 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, bilinçli sapma)   ASL CURVE: —
                 GEREKÇE [D74]: sahne = çekim = klip; ritim kadraj içinden (ölçek sıçraması · palet · ses dokusu · 7 küme) gelir, kırpmadan değil
GRID:            sahne başlangıcı(n) = 0 hook + n × 10 s klip (hook S0 klibin İÇİNDE, ayrı değil; S0 = 0-10 s, S47 = 470-480 s) ⛔ klip süresi ARAÇTAN ölçülür [D124] — ölçülen değer 10 s'den saparsa ızgara yeniden hesaplatılır
RUNTIME:         480 s ± 2 s (kurgu kapısı TAM masterda; yarım masterlar 240 s ± 1 s)
RAW FOOTAGE:     48 clips × 10 s = 480 s · TRIM BUDGET: 0 s (klip kırpılmaz, klip DÜŞÜRÜLMEZ)
SCREEN TEXT:     0.0 saniye (başlık kartı DAHİL; S47 promptu "the take ends on the held frame")
CAMERA:          48 / 48 sabit lockoff — klip içi kamera hareketi 0; sahneler arası 22 kurulum
SETUP SEQUENCE:  A C R J R B B G G I K I G G N O P O P O Q O N R R S T T T Y T V V V O Y O Z E Z F H L L L M L A
KURULUM İSKELETİ: A C R J R B B G G I K I G G N O P O P O Q O N R R S T T T Y T V V V O Y O Z E Z F H L L L M L A
KÜME:            7 küme · S5-S6 · S7-S8 · S12-S13 · S23-S24 · S26-S27-S28 · S31-S32-S33 · S42-S43-S44 (10 devam klibi, her biri "continues the previous clip from its exact last frame — the same position, height and lens as Scene N")
DÖNÜŞ:           20/48 = %42 (≥%40; dönüş = kaynağından ≤3 sahne sonra; S47 = S0 yeniden tanıtım/kafiye, dönüş sayılmadı)
ANGLE ARC:       6 açı tipi — göz hizası · alt açı · üst açı · profil · dörtte üç ön · dörtte üç arka/sırt · şok 1 (S0→S1 CU→WS)
DORUK:           S43 → çekirdek yuvaya oturur, gösterge sönükken klip biter; gösterge S44 ilk karesinde yanık (sahne başlangıcı 430 s; oturma 433,0 s)
DÖNGÜ KANITI:    RHYME — ilk kare S0 (A · 75mm · 1.6 m · h 1.55 · CU frontal, glove raised) ↔ son kare S47 (aynı A, gloves at sides, rime on rim); aynı kurulum · ölçek · ışık; jest TERS (tek değişken el)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Yazılan her kayıt formülle DOĞRULANIR; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   ① SOKET LAMBASI (tek yuvarlak ışık noktası) · 440,0 s (S44 ilk kare) · 1 adet · BULUNAN — yanık; 439,9 s'de (S43 son kare) BULUNMAYAN — sönük
   ② KESİK KAYIŞ UCU askıda · 456,0 s (S45 · 6,0 s) · 1 adet · BULUNAN — iki açık klipsli askıda tek kayış, başka nesne yok
   ③ KANAT kadrajda YOK · 470-480 s (S47) · 0 adet · BULUNMAYAN — sırt kadraj dışı, kask çerçevesinde beyaz puf 1 adet
   ffmpeg -ss 440.0 -i "$M" -frames:v 1 kanit_lamba.jpg · ffmpeg -ss 456.0 -i "$M" -frames:v 1 kanit_kayis.jpg → BAK
   ⛔ tek karede sayılabilir ve adı konabilir olmalı; "final duygusu" değil
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: yukarıda (RHYME) — S0 ↔ S47 aynı kurulum · ölçek · ışık; jest ters (el kalkık ↔ el belde)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
DAVRANIŞ ŞERİDİ (KARAKTER_KARTI §4 · ⑩ ledger'ı ile karşılaştırılır):
GGRTKRGGRGTGGDRKRRDKRGRGGRRDGBRGGKRRGGDKRGGKRBSS
G 17 · T 2 · D 4 (S13 · S18 · S27 · S38) · K 6 (S4 · S15 · S19 · S33 · S39 · S43) · B 2 (S29 · S45) · R 15 · S 2 (S46 · S47)
```

### ⚓ ÇAPA ÜÇLÜSÜ (OYUNCULUK_YAZIM §2 — ⑩ mod D "CHOICE at · COST at · FINAL at")

```
CHOICE  S15 · 153,0 s   BEFORE: both gloves on the strap, shoulders high, the hand stops a palm's width off the buckle for two seconds
                        AFTER:  gloves cinch the buckle, shoulders drop into each pull; the empty back harness stays on the frost beside the rig
COST    S29 · 292,0 s   BEFORE: left glove at the buckle, two fingers straightened a finger's width short, shoulders high
                        AFTER:  both arms closed around the core against her chest, the cut strap-end hanging from the buckle, shoulders down and staying down; the wing spar under the liquid stays in frame
FINAL   S47 · 471,0 s   BEFORE (S0 · 1,0 s): right glove raised to chest height, brows lift as the drop lands
                        AFTER  (S47 · 1,0 s): both gloves at her sides, brows level as the drop lands on the helmet rim — same channel (hand + brow), same setup A
```

### 🎬 KARAR MİMARİSİ · BAŞARISIZ DENEMELER (⑩ · ⑭ · KARAKTER_KARTI §3)

```
FAILED ATTEMPTS:  S13 (flight with the core — drops at twice the glide rate) · S18 (scraping the crust — fresh drops land where cleared) ·
                  S27 (hauling the sunk sled — three pulls, the third shorter) · S38 (rolling the core up the slope — it slides back to her boot)
CHOICES AFTER:    S15 (wings laid flat as a sled) · S19 (cuts the crusted wing-tip off) · S29 (cuts the core free, leaves the wing) ·
                  S33 (turns onto the narrowing dry strip) · S39 (climbs on her knees) · S43 (seats the core)
REJECTED OBJECT IN FRAME: S15 empty back harness beside the rig · S21 cut wing section stays in the lower third · S29-S30 wing spar under the liquid stays at frame edge
HABIT:            right glove tugs the chest buckle twice — S6 · S12 (· S15 hesitates a palm's width off) · BROKEN S29 (two fingers stop a finger's width short, then the cutter)
```

```
PLAN:  111111111111111111111111111111111111111111111111     (1 = insan var · - = insansız · sahne başına bir karakter — 48/48 insanlı, insansız sahne 0)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 × 48 sahne (HUMAN COUNT LOCK 1 × 48); ikinci figür 0; batan kanat (S30) ikinci figür DEĞİLDİR — koyu füme membran + pale spar
KASK          48 × K (kapalı) · açık 0 · vizör TEK DÜZ PANE, KALIN KOYU ÇERÇEVE, 0 ton · 0 ayna · yüz okunur (10 yüz sahnesi: S0 · S2 · S4 · S23 · S24 · S25 · S29 · S35 · S45 · S47) ·
              sırt: KANAT TAKIMI S0-S14 (tek nesne, iki membran + çubuk + tek toka) · S15-S28 kızak yerde, sırt DÜZ · S29-S47 sırt DÜZ — sırt ünitesi/hortum/kablo 0 [D79]
              kask çerçevesi beyaz kuru-kar tortusu S24'ten itibaren (geri dönmez; S25'te silinir ve geri gelir)
NOVUM         SLOW RAIN — iri (bilye boyu), seyrek, sayılabilir damlalar Dünya yağmurunun ~1/3 hızıyla (yavaş koşu temposu, ~3 m/s) iner; bulut tabanından
              yere dakikalar sürer, cephe gökte görünür (S5 yarı yol → S14 baş üstü → S24 omuz → S32 yerde); sıcak yüzeye değen damla anında buharlaşıp
              beyaz puf (diz boyu · 2 s) → kuru kar olarak geri düşer; soğuk yüzeyi ıslatır. Neyin ihlali: Dünya yağmuru hızının/görünümünün — çizgi YOK, asılı perde YOK.
              İkinci sonuç (ihlal değil, ortam): 0,38 g + ~3 kg/m³ hava → insan iki kol boyu kanatla SÜZÜLÜR (çırpma 0), çekirdekle süzülemez (S13)
              KANIT SAHNELERİ: S0 eldiven · S7 kanat · S17 kızak · S24 kask · S32 zemin (≥3 sahne · ≥2 nesne)
YERÇEKİMİ     0,38 g — DÜŞÜŞ TABLOSU: damla sürüklenme sınırı ~3 m/s SABİT (bilye boyu, kalın hava) · bırakılan katı nesne serbest düşüş: eldiven boyu 0,3 m → 0,4 s ·
              diz boyu 0,5 m → 0,5 s · çakılma S13: çatıdan (3 H ≈ 5,7 m) süzülemeyen kanatlarla ~1,7 s · çekirdek yamaçta kayış ivmeli (S38) ·
              iç mekân su damlası (S44) serbest düşüş — ⑥ merceği: aynı kadrajda damla YAVAŞ + katı nesne HIZLI = TASARIM, ihlal değil (PHYSICS satırı ikisini adlandırır)
ATMOSFER      §3.9 kriyojenik: 0,90 bar N₂+CH₄ · 95 K · yoğunluk ~3 kg/m³ · rüzgâr 0-2 m/s (kumaş kıpırdamaz) · pus dolgusu, güneş diski 0, gölge sığ · ses 199 m/s ağır ·
              sıvı metan yüzeyde (SIVI BANDI — bu film kartı açar): durgun, koyu, mat, akmaz · SIVI TEMASI 5 sahne (S22 · S26 · S27 · S28 · S29-30) gerisi arka plan
              İÇ HACİM (§3.10): üs ~1 atm, soğuk (kırağı), kask KAPALI; istasyon ısıtılmamış
EKRAN YÖNÜ    hedef ÜS hep SAĞ üçte bir (S14-S47, 22 dış sahnede sabit) · İSTASYON hep SOL üçte bir (S5-S13) · gidiş S6-S7 ekran SOLUNA · dönüş S16-S40 ekran SAĞINA ·
              yağmur cephesi soldan (istasyon tarafından) iner/yere değer (S20) · FLIP 0 · HAREKET KİLİDİ: sahne başına TEK baskın jest (S0 eldiven kalkık · S6/S12 toka ×2 ·
              S15 kayış · S19/S29 kesici · S25 silme · S35 sarma · S45 asma · S47 eller belde); baş/bakış hedefi NESNE (damla · perde · toka · lamba · askı)
SAYAÇ         ① KIRAĞI ÇİZGİSİ (üs içi duvar): S2 çentiğin bir parmak üstü → S3 yuva hizası → S42 tavana bir el → S44 erir (monotonik yükselir; S44 OLAY) — a/b S3 ↔ S42
              ② DAMLA PERDESİ yüksekliği: S5 haze↔ridge yarı yol → S9 alçak → S11 daha alçak → S14 baş üstü → S24 omuz → S32 yerde (monotonik iner) — a/b S5 ↔ S24
              ③ VENT TÜYÜ (kuru kar): S1 kısa · S16 orta · S28 uzun · S35 kısa (ısı bütçesi)  ⛔ hiçbiri rakam/ekran değil
EŞ KADRAJ     S0 ↔ S47 (A) · S3 ↔ S42/S43 (J ↔ L: aynı yuva) · S5 ↔ S24 (perde a/b)
DÜNYA ÇAPASI  3/3 — gök: "An unbroken amber haze sky, no sun disc, no horizon glow." · ufuk: "A flat dark lakebed of pale-dusted ice to a soft horizon at eye level." · yer imi: "the base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window." (dönüş) / "the old station in the left third, a low dark module barely taller than she is, one door, a flat roof." (gidiş) — dış-mekân promptlarında BİREBİR [D209]
YIPRANMA      5 sabit bölge: kanat ucu çatlak S8+ · kızak/kanat ıslak halka + kuru kar S17+ · sağ bacak ıslak koyu + kar S22+ · kask çerçevesi tortusu S24+ · giysi göğüs/bel ıslak + kabuk S28+ (S35'te ÖN kabuk dökülür — yazılı olay; sırt/bacak kabuğu kalır) [D42]
KİMLİK DİZİSİ kask KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK · amblem YOK — tek aksan: TEAL BANT göğüs üstü (her MS/CU'da yazılı) · giysi PALE GREY ribbed, scuffed composite plates, brushed-steel neck ring ·
              sırt: KANAT S0-S14 / DÜZ S15-S47 · kesik kayış ucu tokada S29-S45 · kir/kabuk bölgeleri yukarıda · hasar: kanat ucu çatlak S8 (geri dönmez, S30'da batar) [D208]
IŞIK TAKVİMİ  monotonik değil, SABİT: dış = pus dolgusu tepe, ~5000 K amber-gri, gölge sığ, saat yönü yok (S0-S2 · S5-S9 · S11-S41 · S47) · iç üs = 3200 K tek tavan paneli (S3-S4 · S42-S46) ·
              istasyon içi = loş gri-mavi + kapıdan amber (S10) · geçişler OLAY (S2/3 · S4/5 · S9/10 · S10/11 · S41/42 · S46/47); ↑/⟳ işareti dış sahnelerde 0 beklenir
SES REGISTER  HUMAN 0 · MACHINE 0 — replik yok; AUDIO yasası: alçak frekans ağır ve yakın, tizler ölü, damla 'tok', temas 'thud'; iç: kırağı çıtırtısı + nefes; müzik S0'da 0, S1'den alçak katman
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI          ① KLİP/KESME SAYISI — yarım master 24 klip, kesme 23, ızgara 10,0 s (küme sınırlarında kesme de sayılır; S23↔S24 küme yarım sınırında)
KOMUT         bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh "$M" 10 24
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 (betik ffmpeg select/scene kullanır; ffprobe 8.1)
İKAME         ffprobe -show_frames -select_streams v -show_entries frame=pts_time,pict_type "$M" | grep -c "I" (I-kare sayımı)

KAPI          ② KUYRUK/BAŞ KART ŞÜPHESİ — ilk 10 s ve son 10 s'de donmuş kare / siyah (D70 · D211)
KOMUT         ffmpeg -i "$M" -vf "freezedetect=n=-60dB:d=1" -an -f null - 2>&1 | grep freeze_start ; ffmpeg -i "$M" -vf blackdetect=d=0.5 -an -f null - 2>&1 | grep black_start
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 — freezedetect OK · blackdetect OK
İKAME         ffmpeg -sseof -1 -i "$M" -frames:v 1 son_kare.jpg → gözle (kart var mı)

KAPI          ③ LOUDNESS / TRUE PEAK — −14 LUFS · −1,0 dBTP (HEALING GROUND −0,4 dBTP vakası)
KOMUT         ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 — ebur128 OK
İKAME         ffmpeg -i "$M" -af volumedetect -f null - 2>&1 | grep max_volume

KAPI          ④ SESSİZLİK / DİJİTAL SIFIR — planlı sessizlik YOK; kesmede dijital sıfır 0 kare olmalı (D216)
KOMUT         ffmpeg -i "$M" -af silencedetect=n=-50dB:d=0.3 -f null - 2>&1 | grep silence_start
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 — silencedetect OK
İKAME         ffmpeg -i "$M" -af astats=metadata=1:reset=1 -f null - | grep RMS_level (saniyelik RMS)

KAPI          ⑤ DAMLA HIZI (1 NUMARALI RİSK · D192) — novum sahnelerinde (S0 · S24 · S32 · S47) iki ardışık kare arasında aynı damlanın yol aldığı kesir: 10 kare/s'de yaklaşık kadraj yüksekliğinin 1/20'si (WS) — çizgi 0 · asılı damla 0
KOMUT         ffmpeg -ss 242.0 -i "$M" -frames:v 10 -vf "fps=10" s24_%02d.jpg → ardışık kareler yan yana; ffmpeg -ss 242.0 -i "$M" -frames:v 1 -vf "tblend=all_mode=difference" fark.jpg
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 — tblend OK
İKAME         ffmpeg -ss 242.0 -i "$M" -frames:v 3 -vf "fps=2" s24_%d.jpg → gözle: damla üç karede üç ayrı konumda mı

KAPI          ⑥ FİLİGRAN / KÖŞE TESTİ (D150 · D215) — 5·60·120·180·240 s sağ-alt montaj
KOMUT         for t in 5 60 120 180 240; do ffmpeg -ss $t -i "$M" -frames:v 1 -vf "crop=480:270:iw-480:ih-270" kose_$t.jpg; done
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026 — crop OK
İKAME         ffmpeg -ss 5 -i "$M" -frames:v 1 tam_5.jpg → gözle sağ alt köşe

KAPI          ⑦ FİNAL VURUŞ KANITI (D141) — 439,9 s lamba sönük · 440,0 s lamba yanık · 456,0 s kayış askıda
KOMUT         ffmpeg -ss 439.9 -i "$M" -frames:v 1 k1.jpg; ffmpeg -ss 440.0 -i "$M" -frames:v 1 k2.jpg; ffmpeg -ss 456.0 -i "$M" -frames:v 1 k3.jpg
DOĞRULANDI    ffmpeg 8.1 · 22.09.2026
İKAME         — (kare çıkarma her ffmpeg'de var)

⬜ HAREKET PROFİLİ (SAHNE_DOLULUGU §5 adayı — sahip kararı): ffmpeg -i "$M" -vf "select='gte(scene,0)',metadata=print" … saniye başına kare farkı → ölü saniye sayısı; eşik bu filmde KALİBRE edilir, elle yazılmaz
```
