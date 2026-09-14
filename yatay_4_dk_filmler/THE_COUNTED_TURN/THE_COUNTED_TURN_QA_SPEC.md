# 📋 THE_COUNTED_TURN — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ **D165 · ÇALIŞMIYOR (3 vaka):** SPEC VE paket hazırken bile operatör çıplak
> rubriği yapıştırdı. Paket VAR olması mod D'yi GARANTİ ETMEZ — bu satır
> "adım gereksiz" diye okunmaz, "adım yeterli değil" der.
> Paketi betik üretir: `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>`

> ⛔ Dosya adı `*_QA_SPEC.md` KALIR (üç betik bu deseni arar).
> ⛔ Bu film YATAYDIR: `## 🎬 SAHNE SPESİFİKASYONU` başlığı BİLEREK YOKTUR.
> `rubrik_paketle.sh` çıktısında `aile: yatay` yazdığını GÖZLE doğrula.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]: EKRAN YÖNÜ · IŞIK
                   TAKVİMİ · ÜST GÜVERTE
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON    → B BLOĞU                          MOD D
⑧ 💪 EFOR       → C BLOĞU'nun EFOR satırları       MOD D
⑨ 🎯 KADRAJ     → B BLOĞU (KURULUM İSKELETİ)       MOD D  ⛔ mod V'de KOŞULMAZ [D190]
⑩ 🎭 OYUNCULUK  → A + C BLOĞU                      MOD D  ⛔ mod V'de KOŞULMAZ [D190]
⑪ 💡 IŞIK       → C BLOĞU (IŞIK TAKVİMİ)           MOD D  ⛔ mod V'de KOŞULMAZ [D190]
⑫ 🪝 HOOK       → A + B BLOĞU                      MOD D  ⛔ mod V'de KOŞULMAZ [D190]
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_COUNTED_TURN
FORMAT:            horizontal 16:9, 3-5 minute band
RUNTIME:           249.0 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       25
THEME:             the human-machine boundary — what the machine counts and
                   what the person counts are two measures of the same job,
                   and when one finishes the other is still running
THEME SCENES:      S3 · S11 · S20 · S24
INTENDED EMOTION:  awe and indifference, not threat — the ring does not care
ENDING TYPE:       TWIST + planted information. Seed at S3 (12% of runtime),
                   paid at S24. Exactly ONE question is left unanswered and it
                   is a THEME question, not a plot question: the plot resolves
                   (the run is finished).
PROTAGONIST:       an unnamed rigger, alone (no proper name anywhere [D34])
CENTRAL CHOICE:    S20 — she turns and walks WITH the spin, the heavy way,
                   because the light way cannot seat the band (starts 199.0 s)
COST:              S21 — she spends all four remaining clips on the final span
                   and has none left for the first pin (starts 209.0 s)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0 / RADIO 0
                   ⛔ THE FILM IS SILENT BY DESIGN. In the story rubric
                   DIALOGUE IS N/A, NOT a low score — the denominator drops to
                   9. Scoring a wordless film down for being wordless punishes
                   the design ("silence is not a gap").
                   ⛔ Likewise CHARACTER: the face is behind a visor in 25/25
                   scenes. "No face on screen" is a DECLARED absence here.
SILENT SCENES:     S22 is the music-free scene (219.0-229.0 s) with an absolute
                   silence window at 226.0-228.0 s
VIRAL INTERSTITIALS: S6 · S11 · S16 · S20  ⛔ THESE MAY NOT BE CUT
UNCUTTABLE:        S6 · S11 · S13 · S16 · S20 · S21 · S22 · S24
                   ⛔ In five separate films the FIRST item of a QA cut list
                   landed on a planned uncuttable scene [D94 pattern].
TITLE:             "THE COUNTED TURN" promises a turn that is being counted —
                   look at the turning and at the count.
LIBRARY CONTEXT:   the only film in this library using environment card 3.7
                   (vacuum + spin gravity) in long horizontal form, and the
                   second using the human-machine theme.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE · ⑦ AKSİYON · ⑨ KADRAJ · ⑫ HOOK)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri YOK)
ASL CURVE:       FLAT, by design.
                 ⛔ GEREKÇE SATIRI [D74]: bu film sabit 10 s ızgarada yazıldı
                 ve ASL eğrisi bilinçli olarak DÜZDÜR. Sebep tembellik değil
                 tasarım: filmin sayacı sahne SINIRINDA ilerler, dolayısıyla
                 sahne uzunluğunun kendisi bir ölçü birimidir. Ritmi ASL
                 değil KADRAJ İÇİ olay yoğunluğu taşır [YAYIN §7: "ilk 30
                 saniyede 19 görsel değişiklik" sabit ızgarada fiziksel olarak
                 imkânsızdır]. Hız kartı sona saklanmadı çünkü hiç açılmadı.
GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S1 = 9 · S6 = 59 · S12 = 119 · S13 = 129 · S18 = 179 ·
                 S20 = 199 · S21 = 209 · S22 = 219 · S23 = 229 · S24 = 239
                 ⛔ KLİP SÜRESİ ÜRETİMDEN ÖNCE ffprobe İLE ÖLÇÜLECEK [D124];
                 10.0 s'den saparsa bu bloktaki HER kod yeniden hesaplanır.
RUNTIME:         249.0 s
RAW FOOTAGE:     25 × 10.0 s = 250.0 s · TRIM BUDGET: 1.0 s (yalnız hook,
                 10.0 → 9.0 s; başka hiçbir klip kırpılmaz)
                 ⛔ Hook kırpılmazsa süre 250.0 s olur ve KAPI ① düşer.
                 Emsal: THE PAYLOAD ve THE FROST LINE'da hook kırpılmadı.
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı, filigran DÂHİL
CAMERA:          25/25 sabit lockoff · pan 0 · tilt 0 · dolly 0 · zoom 0
SETUP SEQUENCE:  A C G A C G F B E E B D H D G A G A E E C E A A A
KURULUM İSKELETİ: A C G A C G F B E E B D H D G A G A E E C E A A A
                 (PLAN'daki ile AYNI — ⑨ KADRAJ SETUP STRING'i buna okur)
KÜME:            3 · S8-S9 · S18-S19 · S22-S23-S24
DÖNÜŞ:           12 / 25 = %48 · S3 S4 S5 S9 S10 S13 S16 S17 S19 S21 S23 S24
ANGLE ARC:       4 açı tipi — high angle (A·E) · eye level (B·C·F) ·
                 low angle (D·G) · over-the-shoulder (H)
AZİMUT:          A 000° · B 045° · C 090° · E 135° · F 180° · D 225° ·
                 G 270° · H 315°
DORUK:           S22 → son klips kapanış pimine oturur (başlangıç 219.0 s)
                 ⭐ İkinci doruk beat'i S21 BEDEL (209.0 s)
BÖLÜM SINIRI:    S12 ↔ S13 · MCU→EWS 4 kademe · 90° · köprü EYLEM SÜREKLİLİĞİ

REPLİK ZAMANLARI: yok (replik 0). Formül yine de bütün zaman kodlarını üretti.

FİNAL VURUŞ KANITI [D141]:
   AÇIK KLİPS · 244.0 s · 1 adet · **BULUNAN**
   Kapanış piminde iki klips vardır: S22'de takılan yenisi KAPALI, S3'te
   takılan eskisi AÇIK ve bandı pimden kalkmış. Sayılabilir, adı konabilir.
   ffmpeg -ss 244 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: ilk kare (S0 · 0.0 s) ↔ son kare (S24 · 248.9 s)
   AYNI kurulum (A) · AYNI ölçek (ECU) · AYNI ışık yönü · AYNI kadraj.
   TEK değişken: kapanış pimi — S0'da BOŞ, S24'te İKİ klips ve biri AÇIK.
   ⭐ Bu bir KAFİYE'dir, LOOP değil: kurgu S24'ten S0'a dönmez.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111110111111111011111110
       (1 = insan var · 0 = insansız · sahne başına bir karakter)
       insansız yuvalar: S6 · S16 · S24
⛔ [D163] 25/25 insanlı bir filmde şerit SABİT olur ve SIRA eksenini ölçemez
   (THE OPEN CIRCUIT'te S2↔S3 yer değiştirmesi bu yüzden görülmedi). Bu filmde
   üç insansız yuva şeride BİLGİ koyuyor.
⭐ SIRA EKSENİNİN İKİNCİ ÇAPASI — SAYAÇ DEĞERİ (replik olmadığı için o kanal
   kapalı). Sahne başına sarkma değeri aşağıdaki C bloğunda; sıra ondan okunur.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤ ⑧ ⑩ ⑪'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         exactly 1 in 22 scenes, 0 in S6 · S16 · S24. No clones.
              Overhead deck: 0 people in 25/25 scenes.
KASK          vizör optik berrak, tint 0, ayna kaplama 0, yansıma 0 ·
              ön pencere DÜZ dikdörtgen 24 × 16 cm, GÖRÜNÜR fırçalanmış metal
              çerçeve (kubbe/bubble/seamless DEĞİL) · durum değişimi 0 kare ·
              sırt ünitesi YOK — düz, kesintisiz pozitif yüzey [D79 · D139]

⭐ PREMISE REGISTER — ⛔ ORTAM DEĞİL, KURAL YAZILIR [D166]:
   Weight in this ring comes ONLY from its rotation and it depends on
   DIRECTION. Walking with the spin makes a body heavier; walking against it
   makes it lighter. There is NO weightless frame anywhere in the film.
   A released object NEVER falls vertically and NEVER rises: it drifts to one
   side, always the same side, always the same distance.
   ⛔ Bu davranışın "imkânsızlığı" ASLA bir bulgu değildir; yalnız TUTARLILIĞI
     puanlanır. Emsal: THE LEANING ROOM'da üç mercek filmin novum'unu 🔴
     BLOCKER saydı çünkü register ORTAMI yazmıştı, kuralı değil.

NOVUM         kural: ağırlık yöne bağlıdır (yukarıda)
              ihlal: bırakılan cisim düz düşmez · aynı adım iki yönde iki
              farklı ağırlıkta iner · sarkma dönme hızıyla derinleşir
              SINIR [D183]: eksen boyunca hiçbir cisim ağırlık kazanmaz;
              eksene dik her cisim kazanır. Sıfır-g 0 kare.
YERÇEKİMİ     R = 12.00 m · T = 20.0 s → 12.0 s · 3.00 → 5.00 RPM
              a = 1.18 → 3.29 m/s² (0.121 g → 0.335 g)
              ⚠️ 1-2 RPM tasarım ölçütünün ÜSTÜNDE ve bu FİLMİN KONUSUDUR:
                bu ortamda kimse adapte olmuş sayılmaz (§3.7 · HEAVY SIDE emsali)
              BIRAKMA: h = 1.40 m · sapma 0.52 m ve DÖNME HIZINDAN BAĞIMSIZ
              SABİT · düşüş süresi 1.69 s (S0) → 1.03 s (S23)
              ⭐ Aynı yere, DAHA ERKEN. Sayaç SÜREDİR, mesafe değil.
ATMOSFER      hard vacuum · toz 0 kare · rüzgâr 0 · alev/kıvılcım/egzoz 0
              ses: dışarıda 0; yapı bir çandır, duyulan her şey TEMASTIR
EKRAN YÖNÜ    dönme yönü 25/25 sahnede AYNI ve İKİ nesneyle teyitli:
              ① yıldız alanı korkuluğun aynı ucundan çıkar
              ② güverte dikişi aynı yöne eğilir
              ⛔ Ters yönde akan tek kare = 🔴 [D174]
SAYAÇ         MONOTONİK · sarkma derinliği (cm), sahne sahne:
              S0 4.00 · S1 4.23 · S2 4.46 · S3 4.70 · S4 4.94 · S5 5.19
              S6 5.45 · S7 5.71 · S8 5.98 · S9 6.26 · S10 6.54 · S11 6.83
              S12 7.12 · S13 7.42 · S14 7.72 · S15 8.03 · S16 8.35 · S17 8.68
              S18 9.00 · S19 9.34 · S20 9.68 · S21 10.03 · S22 10.39
              S23 10.75 · S24 11.12
              ⛔ SAYAÇ TERSİNMESİ diğer bütün skorları EZER: geri giden sayaç
                bir devamlılık kayması değil ÖNERMENİN ÇÖKÜŞÜDÜR [T2 verdict].
              İKİNCİ KANAL [D78 çift kanal]: yıldız süpürme hızı
              S0 3.00 RPM → S12 4.00 → S24 5.00 (18 → 24 → 30 °/s)
              ⛔ Derece PROMPTA yazılmadı, SÜRE yazıldı [D138].
              ÜÇÜNCÜ KANAL (sayaç değil, iki vuruşluk kural kanıtı):
              düşüş süresi 1.69 s (S0) → 1.03 s (S23), iniş yeri SABİT.
              ⛔ [D134] Rapor "no counter present" derse bu sayaç yokluğu
                DEĞİL ÖLÇÜM BOŞLUĞUDUR; bulgu FLAGS'e taşınır, KAREYLE kapanır.
EŞ KADRAJ     S0 ↔ S24 (kafiye) · S2 ↔ S5 ↔ S14 ↔ S16 (sayaç) ·
              S11 ↔ S13 (üst güverte) · S8 ↔ S9 · S18 ↔ S19 · S22 ↔ S23 (küme)
YIPRANMA      sabit bölge 2: sol dizde çizik yama · sağ kalça rayında sığ ezik
              ⛔ YIPRANMA BU FİLMDE SAYAÇ DEĞİLDİR ve 25/25 sahnede AYNIDIR.
                Gerekçe: sayısal takvim bile tutmadı (Third Dune: 3 kademeli
                toz takvimi vardı, 2:29 kumlu suit 2:40'ta tertemiz) [D84].
IŞIK TAKVİMİ  ⭐ YAPISAL SABİT — MONOTONİK DEĞİL, HİÇ DEĞİŞMEZ.
              Işık dönme eksenine paraleldir; geometri halkanın dönüşüyle
              DEĞİŞMEZ [§3.7]. 25/25 sahnede anahtar ışık aynı saat konumunda,
              dolgu 0, gölge mutlak siyah.
              ⛔ [D193] Yazılan takvim ÖLÇÜLMEZSE tutmaz — E bloğu KAPI ⑤.
EFOR          efor sahneleri: S7 S8 S9 S18 S19 S21
              her birinde EN AZ İKİ beden kanalı yazılı: eldiven boğum
              sırtlarının derinleşmesi · manşet dikişinin gerilmesi · omuz
              hattının düşüp DÜŞÜK KALMASI · nefes ritminin ağırlaşması
              COST CURVE (0-9, sahne başına): 0 0 0 0 0 0 0 3 4 4 4 4 4 4 4 4
              4 4 6 6 6 8 8 8 8
              ⛔ Eğri HİÇ DÜŞMÜYOR — reset yok, gerekçe gerekmiyor.
              ⛔ DÜŞÜK YERÇEKİMİ DÜŞÜK EFOR DEĞİLDİR: ağırlık azalır, KÜTLE ve
                ATALET AZALMAZ. "0.12 g'de kolay olur" mazereti BULGUDUR.
SES REGISTER  HUMAN 0 · MACHINE 0 · RADIO 0 — film SESSİZDİR (tasarım).
              ③ SES için TESLİM DURUMU **B (sessiz, tasarımlı)**: Atıf ·
              Sentetik · Ses Kimliği · Aktarım · Sıra Alma sütunları `—`;
              yalnız Ambiyans · SFX · Miks · Müzik puanlanır.
KLİPS SAYIMI  kalça sırası: S0 12 · S15 6 · S17 4 · S18 4 (ikisi düşer) ·
              S19 4 (toplanır) · S21 0
              kapanış pimindeki klips: S0 0 · S3 1 · S22 2 · S24 2 (biri AÇIK)
              dikişteki cıvata: S0 2 · S23 3
PLANTED DETAIL [tohum]: S3 · pime TEK klips takılması · kadrajın merkezinde ·
              ödeme S24
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Aşağıdaki yedi kapının yedisi de 09.09.2026'da ffmpeg 8.1 ile FİİLEN kuru
> koşuldu; `vidstabdetect` KURULU DEĞİL ve o kapı YAZILMADI, ikame kondu.

```
KAPI ①        TESLİM SAYIMI — süre ve klip sayısı
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -c pts_time
DOĞRULANDI    ffprobe/ffmpeg 8.1 · 09.09.2026
BEKLENEN      249.0 ± 1.0 s · 25 klip · ızgara 9,19,29 … 239
İKAME         —  (temel araç, ikame gerekmiyor)

KAPI ②        EKRAN METNİ VE KUYRUK KARTI
KOMUT         ffmpeg -i "$M" -vf freezedetect=n=0.003:d=2 -map 0:v -f null - 2>&1 | grep freeze
              ffmpeg -sseof -3 -i "$M" -frames:v 1 son_kare.jpg
DOĞRULANDI    ffmpeg 8.1 · freezedetect MEVCUT · 09.09.2026
BEKLENEN      donma 0 · son kare S24'ün makrosu (kart YOK)
İKAME         blackdetect=d=0.5 (MEVCUT) — kartın siyah araya girmesi hâlinde

KAPI ③        PLANLI MUTLAK SESSİZLİK [D180]
KOMUT         ffmpeg -i "$M" -af silencedetect=noise=-50dB:d=1.0 -f null - 2>&1 | grep silence_
DOĞRULANDI    ffmpeg 8.1 · silencedetect MEVCUT · 09.09.2026
BEKLENEN      TAM BİR aralık: start ≈ 226.0 · end ≈ 228.0 · duration ≈ 2.0
              ⛔ Aralık YOKSA bıçak kurguda uygulanmamıştır → 🔴 TESLİM KUSURU
İKAME         astats ile saniyelik RMS (MEVCUT) — eşik altını elle okumak

KAPI ④        İHRAÇ SESİ
KOMUT         ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -14
DOĞRULANDI    ffmpeg 8.1 · ebur128 MEVCUT · 09.09.2026
BEKLENEN      I = −14.0 ± 1.0 LUFS · true peak ≤ −1.0 dBTP
İKAME         volumedetect (MEVCUT) — yalnız tepe için

KAPI ⑤        IŞIK TAKVİMİ İZİ [D193] — takvim YAPISAL SABİT olduğu için
              ölçüm de SABİT çıkmalı
KOMUT         ffmpeg -i "$M" -vf "select='not(mod(n,300))',signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
DOĞRULANDI    ffmpeg 8.1 · signalstats MEVCUT · 09.09.2026
BEKLENEN      YAVG örnekleri arasında sıçrama YOK; ışık geri yanmıyor.
              ⛔ THE OPEN CIRCUIT'te sönen şeritler aynı klibin sonunda geri
                yandı ve 12 merceğin 12'si kaçırdı.
İKAME         her 10 s'de bir kare çıkarıp gözle karşılaştırma

KAPI ⑥        KONTRAST — üst güvertedeki bant hattı okunuyor mu [🟡 uyarı 1]
KOMUT         ffmpeg -ss 119 -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX:key=lavfi.signalstats.YMIN" -frames:v 1 -f null - 2>&1 | grep Y
DOĞRULANDI    ffmpeg 8.1 · signalstats MEVCUT · 09.09.2026
BEKLENEN      S11 ve S13'te YMAX − YMIN ≥ 110
              (bant 24 m'de ~39 px; okunurluk BOYUTTAN değil KONTRASTTAN gelir)
İKAME         kare çıkarıp %25'e küçültüp gözle bakmak

KAPI ⑦        FİLİGRAN VE KÖŞE TESTİ [D150 · 6 vaka · ⛔ ÇALIŞMIYOR]
KOMUT         for t in 5 60 120 180 240; do ffmpeg -ss $t -i "$M" -vf "crop=iw/4:ih/4:iw*3/4:ih*3/4" -frames:v 1 kose_$t.png; done
DOĞRULANDI    ffmpeg 8.1 · crop MEVCUT · 09.09.2026
BEKLENEN      beş örnekte de sabit köşe işareti YOK
              ⛔ Filigranlı master MASTER DEĞİLDİR. İki filmde üretici
                filigranı 225/225 ve 230/230 saniyede durdu ve toplam yirmi
                mercek görmedi.
İKAME         —

⛔ YAZILMAYAN KAPI: KAMERA SABİTLİĞİ.
   `vidstabdetect` bu makinede KURULU DEĞİL (09.09.2026 · ffmpeg 8.1 ile
   doğrulandı). Kapı YAZILMADI — kurulu olmayan filtreye yazılan kapı
   sessizce hiç koşmaz [D142]. İKAME: S2 ve S20'nin ilk/son karesi çıkarılır
   ve kenarlar üst üste konur; kayma varsa lockoff 25/25 DEĞİLDİR.
   KOMUT: ffmpeg -ss 19 -i "$M" -frames:v 1 a.png ; ffmpeg -ss 28.9 -i "$M" -frames:v 1 b.png
```

## 🅵 F BLOĞU — GÖZ KAPILARI [D191] — hiçbir mercek bunları koşmuyor

> THE OPEN CIRCUIT'te SPEC'in göz kapılarının 12 maddesinden 5'i ihlal edildi
> ve on iki mercekte 0 bulgu çıktı. `rapor_kontrol.py` bu bloğu ⬜ listesi
> olarak basar; operatör KAREYE bakarak işaretler.

```
[ ] GÖZ ①  ekranda okunan konuşan ağız 0 kare (film sessiz)
[ ] GÖZ ②  kask: DÜZ dikdörtgen pencere + GÖRÜNÜR çerçeve · kubbe 0 kare
[ ] GÖZ ③  sırt: kesintisiz düz panel · çıkıntı 0 kare (özellikle S12)
[ ] GÖZ ④  dönme yönü 25/25 sahnede AYNI · ters akan kare 0
[ ] GÖZ ⑤  bırakılan cisim yana iner · düz düşen kare 0 (S0 · S18 · S19 · S23)
[ ] GÖZ ⑥  sarkma MONOTONİK · geri giden kare 0
[ ] GÖZ ⑦  kalça sırası 12 → 6 → 4 → 0 · geri dolan kare 0
[ ] GÖZ ⑧  üst güvertede insan 0 kare
[ ] GÖZ ⑨  yıldız alanı tek tek nokta · iz/çizgi 0 kare
[ ] GÖZ ⑩  toz · kıvılcım · alev 0 kare
[ ] GÖZ ⑪  çıplak deri 0 kare (yaka üstü · bilek · manşet)
[ ] GÖZ ⑫  hiçbir yüzeyde harf/rakam/işaret 0 kare (zemin ve pim DÂHİL)
[ ] GÖZ ⑬  S22'de ışık olayı 0 kare (şimşek/parlama/kıvılcım yok)
[ ] GÖZ ⑭  S24'te kapanış piminde İKİ klips ve biri AÇIK
```

## 🅶 G BLOĞU — PLAN ↔ KURGU SAYIMI [D156 · bulgu 8-9]

> ⛔ Planın "SIFIR" dediği her şey ayrı ölçüm satırıdır. THE PAYLOAD'da planın
> VAR dediği her şey geldi, SIFIR dediği her şey düştü — ve sıfırı kimse
> ölçmüyordu.

```
[ ] replik sayısı            plan 0   ↔ makara ___
[ ] ekran metni              plan 0.0 s ↔ makara ___
[ ] insan sayısı (tepe)      plan 1   ↔ makara ___
[ ] insansız sahne           plan 3   ↔ makara ___  (S6 · S16 · S24)
[ ] klip içi kesme           plan 0   ↔ makara ___
[ ] müziksiz sahne           plan 1   ↔ makara ___  (S22)
[ ] mutlak sessizlik         plan 2.0 s ↔ makara ___
[ ] SAHNE SAYISI [D188]      plan 25  ↔ makara ___
    ⛔ EŞİT DEĞİLSE hiçbir mercek koşulmaz, hiçbir T satırı yazılmaz.
      THE OPEN CIRCUIT'te iki sahne eksikti ve biri filmin DORUĞUYDU;
      ⑫ HOOK var olmayan doruğa 9/10 verdi.
[ ] PLANLI HER SAHNE KURGUDA MI — S0'dan S24'e tek tek işaretle
    ⛔ 11 teknik rapor kare İÇİNDEKİ hatayı arıyor; hiçbiri "planlanan sahne
      ekranda var mı" diye sormuyor [00_INDEX bulgu 8].
```
