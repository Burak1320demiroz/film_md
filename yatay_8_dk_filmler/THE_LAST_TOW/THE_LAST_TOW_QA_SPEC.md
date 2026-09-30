# 📋 THE_LAST_TOW — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_LAST_TOW_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
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
FILM:              THE_LAST_TOW
FORMAT:            16:9 horizontal · 8:00 · 48 clips × 10.0 s · 2 parts · science
                   fiction (salvage) · VACUUM + BARE METAL, cold welding
                   (0.30 g · no atmosphere · shadows absolute black · one grazing star
                   fixed at 2.3 degrees elevation)
RUNTIME:           480 seconds (title card: none — screen text lock 0.0 s)
SCENE COUNT:       12        ⛔ SCENE COUNT ≠ CLIP COUNT (multi-clip scene regime)
PART GRID:         B1 = K01-K24 · 24 clips · 0-240 s · S01-S06
                   B2 = K25-K48 · 24 clips · 240-480 s · S07-S12
                   QA runs on each part SEPARATELY; paste with the SPEC:
                   "THIS FILE IS PART 1 OF 2 — clips K01-K24 — the film's ending is NOT in this file."
                   "THIS FILE IS PART 2 OF 2 — clips K25-K48 — the film's opening is NOT in this file."
                   BOUNDARY PAIR: K24 | K25 — closed by hand with two frames (see E BLOCK gate 6)
THEME:             LONELINESS
THEME SCENES:      S01 · S04 · S06 · S09 · S11 · S12
INTENDED EMOTION:  peaceful imprisonment — at last not alone, and never able to leave
ENDING TYPE:       CLOSED. She sends the only other thing here away and stays.
PROTAGONIST:       — (isimsiz · rol etiketi "salvager" yalnız burada; özel ad hiçbir
                   promptta geçmez [D34])
CENTRAL CHOICE:    S11 · K43 — she sets her cutter head into the closing gap and leaves it there
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S01 · S03 (no music; sound bed and contact only)
VIRAL INTERSTITIALS: 3 — K16 · K27 · K40   ⛔ THESE MAY NOT BE CUT
FOUR PROOF CLIPS:  K03 · K25 · K37 · K44   ⛔ THESE MAY NOT BE CUT — each one is the
                   film's rule proved by a positive CHANGE, not by an absence
TITLE:             "THE LAST TOW" promises a final departure and a thing carried away.
LIBRARY CONTEXT:   THE_COLD_WELD (same environment card, 2 min, light is the THREAT there)
                   · THE_BORROWED_WEIGHT (carrying salvage) · THE_SLOW_RAIN (8 min line)

⭐ FALSE-POSITIVE WALL — these are DESIGN, not defects:
  ① 0 dialogue in 48 clips. The environment card says there is no sound outside and
    everything heard is contact; a speaking human would break the rule in one second.
  ② The camera never moves. 48 locked-off setups, no pan, no push, no handheld.
  ③ Shadows are absolutely black with no fill. There is no atmosphere to scatter light.
  ④ The metal carries NO numbers, no serials, no gauge marks. Only weld seams, rivet
    lines and meteorite pits carry information.
  ⑤ Nothing on the metal is loose and nothing lies flat. A tool standing upright on a
    plate is not a physics error — it is the film's rule.
  ⑥ A cut that closes behind the blade is not a render glitch (K15 · K35).
  ⑦ The second pressure suit is an OBJECT. It never moves on its own, its front pane
    is dark, and the human count stays exactly one in all 48 clips.
  ⑧ No dust on the metal. Micrometeorite strikes swept it; dust lies only on regolith.
  ⑨ The star's elevation never changes (2.3°). What moves is the SHADOW EDGE, 2.0 cm
    per second — one direction, never back.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      48
SHOT COUNT:      48 · sahne içi kesme 36 (SHOT COUNT = CLIP COUNT; klip içi kesme 0)
SCENE PLAN:      4 3 5 4 4 4 4 5 3 4 5 3
                 S01 = K01-K04 · S02 = K05-K07 · S03 = K08-K12 · S04 = K13-K16 ·
                 S05 = K17-K20 · S06 = K21-K24 · S07 = K25-K28 · S08 = K29-K33 ·
                 S09 = K34-K36 · S10 = K37-K40 · S11 = K41-K45 · S12 = K46-K48
INTRA-SCENE CUTS: K01|K02 K02|K03 K03|K04 · K05|K06 K06|K07 · K08|K09 K09|K10 K10|K11
                 K11|K12 · K13|K14 K14|K15 K15|K16 · K17|K18 K18|K19 K19|K20 ·
                 K21|K22 K22|K23 K23|K24 · K25|K26 K26|K27 K27|K28 · K29|K30 K30|K31
                 K31|K32 K32|K33 · K34|K35 K35|K36 · K37|K38 K38|K39 K39|K40 ·
                 K41|K42 K42|K43 K43|K44 K44|K45 · K46|K47 K47|K48
                 → these cuts are INSIDE one scene: location, light, sound bed, costume
                 dirt, held object and body pose MUST match across them; a reset here is
                 a ② CONTINUITY defect, not a scene change.
                 SCENE BOUNDARIES (11): K04|K05 K07|K08 K12|K13 K16|K17 K20|K21
                 K24|K25 K28|K29 K33|K34 K36|K37 K40|K41 K45|K46
TARGET ASL BAND: 10.0 s flat   ASL CURVE: flat — no curve
                 ⛔ GEREKÇE SATIRI [D74]: the 10 s grid is a PRODUCTION plan, not an
                 editing rhythm. Every clip is a separate single take and is not trimmed
                 (owner decision 22.09.2026, edit gate ±0). Rhythm is carried by scale
                 walk and palette, not by clip length.
GRID:            klip başlangıcı(n) = (n−1) × 10.0 s   (hook 48'in İÇİNDE, ayrı klip değil)
RUNTIME:         480 s
RAW FOOTAGE:     48 × 10.0 s = 480 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0.0 s
CAMERA:          48 / 48 sabit lockoff — 0 pan, 0 push, 0 handheld
SETUP SEQUENCE:  C A B A · B C D · C E H E F · E F G K · G I J A · J I D I |
                 D K D F · B F G F G · F G K · G I G I · J I D K D · C B A
KURULUM İSKELETİ: C A B A  B C D  C E H E F  E F G K  G I J A  J I D I | D K D F  B F G F G  F G K  G I G I  J I D K D  C B A
KÜME:            — (bu rejimde ARANMAZ: zincir kalktı, SAHNE PLANI beyan edildi)
DÖNÜŞ:           21 · %43,8  (≥%40 · dönüş = kaynağından ≤3 klip sonra)
ANGLE ARC:       3 açı tipi (eye-level B·C·D·E·H·K · low-angle A·F·J · high-angle G·I)
DORUK:           S10 · K37-K40 (klip başlangıcı 360-400 s) → S11 · K43 (420 s) merkezî seçim

REPLİK ZAMANLARI: YOK. 0 replik · 0 kayıt. ㉓ envanteri promptlarda 0 tırnak sayar.

FİNAL VURUŞ KANITI [D141]:
   nesne: kesici kafası (46 cm, sapı 19 mm) · saniye: 470-480 s · kaç tane: 1 ·
   BULUNAN — filmin başında sahada olmayan, sonunda duran tek nesne
   ⛔ tek karede sayılabilir ve adı konabilir
   ffmpeg -ss 475 -i "$M" -frames:v 1 kanit.jpg   → dikişte duran kesici kafası VAR mı
DÖNGÜ KANITI: K02 (10-20 s) ↔ K48 (470-480 s) — aynı kurulum A (18 mm · 9,0 m · 0,30 m),
   aynı ölçek EWS, aynı yer. DEĞİŞEN: ışık (gölge → tam ışık) ve dikişte duran kesici.
   ⛔ Bu bir LOOP DEĞİL, KAFİYEDİR: film kapanır, 0:00'a bağlanmaz.
   ffmpeg -ss 15 -i "$M" -frames:v 1 kafiye_a.jpg ; ffmpeg -ss 475 -i "$M" -frames:v 1 kafiye_b.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  --1111111111111111111111111111111111111111111111
       (1 = insan var · - = insansız · KLİP başına bir karakter)
       K01 ve K02 insansız (46/48). ⛔ O iki klipte insan SAYIMI kurulmaz;
       "No people, no figures, no silhouettes of people." yazılır [red defteri #2 YR].
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         1 canlı insan 46/48 klipte · K01-K02'de 0 · ikinci basınç giysisi bir
              NESNEdir (14 klipte), insan sayısına GİRMEZ
KASK          vizör tek düz ön pane 22 × 14 cm, kalın koyu gri çerçeve içinde, optik
              berrak · sırt ünitesi YOK — düz siluet, tek sürekli yüzey [D79 · D139]
              ⛔ "seamless" · "bubble" · "dome" · "wraparound" 0 kez [D146]
NOVUM         Oksitsiz iki metal yüzey değdiği anda ısı olmadan atomik olarak BİRLEŞİR.
              İhlal ettiği şey: bu ortamda gevşek parça olamaz — düşen alet düştüğü
              yerde DİK kalır. Sonucu: ayıran tek güç ısı farkıdır.
              Kanıt klipleri: K03 (tekmelenen anahtar kaymaz) · K25 (dikiş kopar) ·
              K37 (botlar kopar) · K44 (kesici kafası değer ve kalır)
YERÇEKİMİ     0.30 g · düşüş 1,40 m → 0,97 s · 0,60 m → 0,64 s · 0,35 m → 0,49 s
ATMOSFER      yok (hard vakum) · dışarıda 0 ses · rüzgâr 0 · pas 0 · kıvılcım 0
              metalin üstünde 0 kare toz; toz yalnız metal DIŞINDAKİ regolitte
EKRAN YÖNÜ    hedef (kapak) hep kadrajın SAĞ yarısında · ilerleme ışık kenarı SOLDAN
              SAĞA · 48/48 klipte sabit · 180° çizgisi hiçbir sahnenin içinde aşılmaz
HAREKET KİLİDİ eldiven film boyu yüzeylere SIRTIYLA değer, avuçla değmez (11 klipte
              görünür sakınma) · tek klipte TEK jest · baş yalnız bir kez döner (K07 ·
              K11 · K19) · K43'te avuç bilerek bastırır — filmin tek ters kararı
SAYAÇ         3 kanal, üçü de MONOTONİK ve ekranda SAYI yazmaz:
              ① ışık kenarının dikişe mesafesi 4,80 → 4,00 → 3,40 → 2,40 → 1,60 →
                0,80 → 0,00 m (K04 · K07 · K12 · K16 · K20 · K25)
              ② kesicinin durumu: yuvada keskin (K01-K15) → yuvada ağzı gitmiş
                (K16-K42) → dikişte kaynamış (K43-K48) → yuva BOŞ (K44-K48)
              ③ açıklığın genişliği 20 mm (K29) → 12 mm (K37) → 4 mm (K41) →
                kama 19 mm'de kilitlenir (K44)
              ⛔ cihaz ekranı · kadran · gösterge · sayaç filmde HİÇ YOK
EŞ KADRAJ     K02 ↔ K48 (kurulum A) — kafiye çifti · K24 ↔ K25 bölüm sınırı çifti
DÜNYA ÇAPASI  3/3 — SKY: flat black, no stars, no gradient · HORIZON: a low regolith
              ridge forty metres high with a sharp top edge · LANDMARK: the welded spine
              of the reef crossing the frame. Üç cümle dış-mekân promptlarında BİREBİR [D209]
YIPRANMA      2 sabit bölge: bilek halkalarında çizik + giysinin tamamında eşit mat
              pas grisi toz. Artış YOK — klip içinde sabit, sahne SINIRINA yazılır [D42 · D84]
KİMLİK DİZİSİ 4 öznitelik, 48/48 promptta AYNI SIRADA [D167 · D208]:
              ① pale sand-grey thick creased multilayer nylon
              ② a rib of four raised segments across each shoulder of the suit
              ③ a wide utility belt with two sockets
              ④ heavy dark-grey ceramic-coated gloves and boots
              ⛔ 0 promptta: boy · ten rengi · saç · yaş · yüz işareti (red #15)
              AYIRT ETME GEOMETRİDE: omuz kaburgası + kemerdeki iki yuva
IŞIK TAKVİMİ  MONOTONİK ✅ — yıldız yüksekliği 2,3°'de SABİT, azimut sabit; hareket eden
              yalnız gölge kenarı ve saniyede 2,0 cm tek yönde. Palet GÖLGE (S01-S02) →
              KENAR (S03-S06) → IŞIK (S07-S12), geri dönüş YOK
SICAKLIK      yıldıza bakan DİKEY çıplak metal 370 K · YATAY zemin 180 K → 190 K fark;
              genleşme metrede 1,3 mm; 18 m'lik çerçeve dizisi 23 mm büyür > 20 mm boşluk
SES REGISTER  HUMAN 0 · MACHINE 0 — duyulan her şey TEMASTIR, gövdeden iletilir,
              kuru ve kısa, yankı yok. Müziksiz sahne: S01 · S03
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> ⛔ Aşağıdaki altı kapının altısı da `ffmpeg 8.1` ile KURU KOŞUYLA doğrulandı
> (28.09.2026): filtrenin varlığı `ffmpeg -hide_banner -filters` çıktısından
> teyit edildi. Master yok — kapılar master geldiğinde koşacak.

```
KAPI 1        SÜRE VE IZGARA — 480 s ± 2 s ve kesmelerin 10 s ızgaraya oturması
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -oE "pts_time:[0-9.]+"
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · showinfo + select VAR
İKAME         filtre yoksa kesmeler elle sayılır (kare kare) ve sayı SPEC'e yazılır

KAPI 2        SES KANALI VARLIĞI — "duydum/duymadım" bir ölçüm DEĞİLDİR [D136]
KOMUT         ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 "$M"
DOĞRULANDI    ffprobe 8.1 · 28.09.2026 · çıktı BOŞSA dosyada ses kanalı YOKTUR = teslim kusuru
İKAME         yok — bu kapı ikame kabul etmez

KAPI 3        GÖLGE SİYAHI — bu filmde gölge MUTLAK siyah olmak ZORUNDA (dolgu 0)
KOMUT         ffmpeg -ss <s> -i "$M" -vf "crop=iw/4:ih/4:0:ih*3/4,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -frames:v 1 -f null -
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · signalstats VAR
İKAME         kare çıkarılır ve histogramı elle okunur
⭐ EŞİK        gölge içi YAVG < 12/255 olmalı. ⚠️ Bu §3.2'nin TERSİ bir eşiktir
              (orada saçılma yüzünden YAVG > 18 aranıyordu) — vakumda dolgu yok.

KAPI 4        FİLİGRAN / KÖŞE TESTİ — KRONOS'ta 4 kollu yıldız 0:00-4:00 tüm sahnelerdeydi
KOMUT         for t in 5 120 240 360 475; do ffmpeg -ss $t -i "$M" -vf "crop=320:180:iw-320:ih-180" -frames:v 1 kose_$t.png; done
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · crop VAR
İKAME         yok — beş köşe karesi gözle okunur

KAPI 5        KUYRUK KARTI — iki filmde teslim adımının VARSAYILANI olarak eklendi [D70/D72]
KOMUT         ffmpeg -sseof -6 -i "$M" -vf "blackdetect=d=0.5:pix_th=0.10" -f null - 2>&1 | grep black_start
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · blackdetect VAR
İKAME         son 6 saniye kare kare okunur
⭐ BEKLENEN    çıktı BOŞ — ekran metni 0,0 s, kart YOK

KAPI 6        BÖLÜM SINIRI ÇİFTİ — ② hiçbir yarım masterda K24 ↔ K25'i yan yana GÖREMEZ
KOMUT         ffmpeg -sseof -1 -i "<B1.mp4>" -frames:v 1 sinir_a.jpg
              ffmpeg -ss 0.2 -i "<B2.mp4>" -frames:v 1 sinir_b.jpg
DOĞRULANDI    ffmpeg 8.1 · 28.09.2026 · -sseof VAR
İKAME         yok — iki kare yan yana konur ve dört şey karşılaştırılır:
              gövde duruşu · ışık kenarının yeri · kir/hasar · kesicinin kemerdeki durumu
```

---

## 👁️ GÖZ KAPILARI — makinenin ölçemediği dördü

```
G1  İKİ GÖVDE AYRIMI (K32 · K38 · K39 · K40 · K46)
    Kadının omzunda kaburga hattı ve kemerinde iki yuva VAR; ikinci giysinin omzu
    DÜZ, kemeri YOK, ön paneli KOYU. ⛔ Ayrım RENKLE kurulmadı — renkle kurulan
    ayrım gece sahnesinde çöküyor [BLIND BERTH].

G2  ATOMİK SINIR (K25 · K26 · K33 · K37 · K44)
    İki yüzey ayrı ayrı görünüyor ve aralarında NET sınır var mı? Eriyorsa,
    birbirine geçiyorsa ya da sınır bulanıksa bu bir ÜRETİM HATASIDIR [D24],
    kartın kuralı değil. ⛔ K44 bu filmin İPTAL KAPISIDIR.

G3  İKİNCİ GİYSİNİN PANELİ (K31 · K32 · K38 · K39 · K40 · K46)
    Panel koyu ve hiçbir şey vermiyor mu? Arkasında bir YÜZ belirirse ÜRETİM DURUR
    ve giysi yalnız yandan/arkadan çerçevelenir (HAZIR DÜŞÜŞ).

G4  VİZÖR BİÇİMİ (48/48, özellikle K21 ve K43'ten önce)
    Tek DÜZ pane mi, kalın koyu gri çerçeve içinde mi? Kubbe/balon görülürse
    ÜRETİM DURUR ve biçim kararı sahibe geri gider [D146].
    ⚠️ Referans paketi YAZILMADIĞI için bu kapı bu filmde tek savunmadır.

G5  METALDE METİN (48/48)
    Yüzeyde numara, seri işareti, ölçü çentiği ya da damga var mı? Bilgi taşıyan
    tek üç şey: 8 mm dikiş · 40 mm perçin aralığı · 1-20 cm göktaşı çukuru [D138].
```
