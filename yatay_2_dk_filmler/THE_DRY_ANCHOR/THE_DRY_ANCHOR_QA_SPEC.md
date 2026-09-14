# 📋 THE_DRY_ANCHOR — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET kaldırıldı. Operatör `QA_PROMPTLARI/_KAYNAK/`
> rubriğini açar ve BU dosyayı rubriğin BAŞINA yapıştırır; mod D'nin tek koşulu budur.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ✅ **BU FİLM YATAYDIR** — `## 🎬 SAHNE SPESİFİKASYONU` başlığı yoktur.
> (O başlığı yalnız `rubrik_paketle.sh` okuyordu; betik 11.09.2026'da silindi,
> başlık artık hiçbir makine kapısını beslemiyor.)

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⑨-⑫ → B + F BLOĞU (mod V bu dörtlüde GEÇERSİZ'dir [D184 · D189])
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_DRY_ANCHOR
FORMAT:            yatay 16:9 · 2-4 dk kartı (KILAVUZ_REHBERI §2.2)
RUNTIME:           140,0 seconds (title card: YOK — screen text lock 0,0 s)
SCENE COUNT:       14  (14 × 10,0 s · sabit ızgara · hook da 10,0 s)
THEME:             İNSAN-MAKİNE SINIRI — "insan zemini OKUR, zemin okunduğu
                   için DEĞİŞMEZ." (TANIM cümlesi · takas kalıbı değil)
THEME SCENES:      S3 · S4 · S9 · S11 · S13   ⛔ en az üç (yazılmayan tema dekoratif)
                   ⭐ S9 = BEDEL sahnesi; B3'ün çapraz kapısı bunu ister
INTENDED EMOTION:  önce HUŞU (S4), sonra SOĞUK KABUL (S11-S13) — korku değil,
                   panik hiç değil. Hiçbir sahnede kurtarma yoktur.
ENDING TYPE:       ÇÖZÜLMEMİŞ DENGE — gemi kurtulur, gelinme sebebi (kasa)
                   kaybedilir; son kare tutulur, müzik çözülmeden kesilir.
PROTAGONIST:       isimsiz saha mühendisi (özel ad promptta geçmez [D34])
CENTRAL CHOICE:    kasa kayışını hatta eklemek — S9 (90-100 s)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
                   ⛔ SIFIR replik: filmde konuşan ağız, telsiz, suit AI ve
                   kayıt YOKTUR. Transkript eden mercek UYDURMUŞTUR [D188].
SILENT SCENES:     müziksiz: S0 · S10 · S11 (§10 en az bir ister — burada üç)
                   MUTLAK sessizlik: 118,0-120,0 s (S11'in son 2 s'si)
VIRAL INTERSTITIALS: S11 (⭐VİRAL · YÜZ + HAREKET) · S4 (PAYLAŞIM · HUŞU)
                   ⛔ THESE MAY NOT BE CUT
TITLE:             "This Dust Has No Bottom" — KURALI söz veriyor, sonucu değil
LIBRARY CONTEXT:   deponun İKİNCİ ince-atmosfer filmi ve BİRİNCİ yatay olanı;
                   kardeş: THE THIN ROOF (dikey shorts · §3.2 kartı · 27.08.2026)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      14
SHOT COUNT:      14 · sahne içi kesme 0   (sahne = çekim = klip)
TARGET ASL BAND: 10,0 s SABİT (bant değil TEK DEĞER: 140,0 ÷ 14)
ASL CURVE:       UYGULANAMAZ
                 ⛔ GEREKÇE SATIRI [D74 · KURGU_RITMI §0②]: sabit ızgaralı
                 filmde ASL matematiksel olarak sabittir ve §1 eğrisi kırpma
                 bütçesi ister — bu filmde kırpma bütçesi 0,0 s'dir. Ritmi
                 taşıyan şey §2'nin KADRAJ İÇİ değişkenleridir: ölçek
                 (EWS→CU→WS→MS), açı tipi (3), ses dokusu ve müziğin
                 çekilmesi. Örüntü kırıcı ardışık çift denetimi 03_SAHNE
                 SIRALAMASI'nda sahne sahne koşuldu.
GRID:            sahne başlangıcı(n) = hook 10,0 s + (n−1) × 10,0 s klip
                 n = 1..14 → S0 0,0 · S1 10,0 · S2 20,0 · S3 30,0 · S4 40,0 ·
                 S5 50,0 · S6 60,0 · S7 70,0 · S8 80,0 · S9 90,0 · S10 100,0 ·
                 S11 110,0 · S12 120,0 · S13 130,0 → bitiş 140,0
                 (hook klip uzunluğuna EŞİT olduğu için formül n×10,0'a indirgenir)
RUNTIME:         140,0 s
RAW FOOTAGE:     14 × (Veo 8 s + 2 s extend) = 140,0 s · TRIM BUDGET: 0,0 s
SCREEN TEXT:     0,0 saniye (başlık kartı yok · alt yazı yok · son kart yok)
CAMERA:          14 / 14 sabit lockoff — pan · tilt · dolly · zoom SIFIR
SETUP SEQUENCE:  sahne sahne kurulum imzası (mesafe · yükseklik · lens · açı):
                 S0  A 24mm · 110 m · 1,50 m · el +2°  · EWS
                 S1  A (küme · S0'ın devamı)
                 S2  B 35mm · 4,5 m · 3,20 m · el −55° · MS (üst açı)
                 S3  C 35mm · 1,2 m · 0,26 m · el −12° · CU
                 S4  A (dönüş · S0)
                 S5  B (dönüş · S2)
                 S6  D 35mm · 22,0 m · 1,50 m · el +12° · WS (alt açı)
                 S7  C (dönüş · S3)
                 S8  D (dönüş · S6)
                 S9  D (küme · S8'in devamı)
                 S10 E 35mm · 3,0 m · 0,53 m · el −10° · MS
                 S11 E (küme · S10'un devamı)
                 S12 D (dönüş · S6)
                 S13 A (dönüş · S0 · KAFİYE)
KURULUM İSKELETİ: A A B C A B D C D D E E D A   (PLAN'daki ile AYNI)
KÜME:            3 küme — S0-S1 · S8-S9 · S10-S11 (12+ sahnede ≥2 · ACI_YAYI §4b)
                 ⛔ hiçbir küme bölüm sınırını çaprazlamaz; S6→S7 GERÇEK kesmedir
DÖNÜŞ:           7 / 14 = %50 (≥%40) — S4 · S5 · S7 · S8 · S12 · S13 + küme dönüşleri
                 hepsi kaynağından ≤3 sahne sonra ya da işaretli KAFİYE (S13→S0)
ANGLE ARC:       3 açı TİPİ (§2 en az 3 ister): göz hizası (A) · üst açı (B) ·
                 alt açı (D) — ayrıca iki alçak-kamera-aşağı varyantı (C · E)
DORUK:           S11 → 110,0-120,0 s (sahne başlangıcı 110,0 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   → BU FİLMDE KOŞMAZ: 0 replik. Formül ileride replik eklenirse koşar;
     boş bırakılmaz, çünkü boş alan uydurma transkripti davet ediyor.

FİNAL VURUŞ KANITI [D141]:
   nesne: ÖRNEK KASASI (kapalı dikdörtgen kasa, düz geniş tabanlı)
   saniye: 132,0 s   ·   kaç tane: BİR (1)   ·   BULUNAN
   yanında sayılabilir ikinci kanıt: gergin hat 1 (tek) · yüzeyde görünen
   pabuç 3 / 4 (dördüncü bacakta pabuç YOK)
   ⛔ tek karede sayılabilir ve adı konabilir: "final duygusu" değil
   ffmpeg -ss 132.0 -i "$M" -frames:v 1 "${TMPDIR:-/tmp}/kanit.jpg"   → BAK
   ⛔ kanıt karesi DEPO DIŞINA yazılır: bu repoda image/video bulunmaz
DÖNGÜ KANITI: ilk kare (0,0 s · A) ↔ son kare (140,0 s · A)
   AYNI: kurulum · lens · yükseklik · mesafe · ölçek (EWS) · güneş yönü
   DEĞİŞEN (kafiyenin kendisi): eller BOŞ (S0'da kızak yüklü) · kelepçeler
   BOŞ (S0'da dolu) · kadrajı çaprazlayan gergin hat VAR (S0'da yok) ·
   gölgeler UZUN (S0'da kısa) · kasa YERDE (S0'da kızakta)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  11111111111111     (1 = insan var · - = insansız · sahne başına bir karakter)
       14/14 sahnede TEK insan; hiçbir sahnede ikinci gövde, hiçbir sahnede
       insansız kadraj yok. S2 · S3 · S5 · S7'de insan KISMİDİR (el · kol ·
       botun altı) ama kadrajdadır — bu satır "kadrajda insan var mı" sorusunu
       cevaplar, "tam boy mu" sorusunu değil.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         1 — tam olarak bir insan, 14/14 sahnede; klon/ikiz/ikinci kişi 0
KASK          çerçeveli DÜZ dikdörtgen ön pencere · vizör optik berrak (0 renk
              tonu · 0 ayna kaplaması · 0 çevre yansıması) · sırt ünitesi YOK —
              düz siluet, yaka-kalça arası tek panel, üstünde hiçbir şey [D79]
              kask içi tek cyan lamba yüzü ALTTAN aydınlatır (14/14)
TOZ (1 NO'LU RİSK) halka 2 gövde genişliği · yükseklik ≤ pabuç · düşüş yürüyüş
              temposunda ve DÜZ · 20,0 s'de asılı zerre 0 · oturan katman 1 parmak
              — biçim POZİTİF ve SAYILI yazıldı, negatif cümleye bırakılmadı [D192]
NOVUM         KURAL: yağmur görmemiş toz sıkışmaz — taban basıncı yüksek olan
              her şey iner ve DURMAZ (dar taban batar, geniş düz taban durur).
              İHLAL: S11 — rüzgârın süpürdüğü çıplak taş, yağmurun yapmadığını
              yapar; kazık ilk kez DURUR ve sürücü geri seker.
              TAŞIYICI: ÇELİK KAZIK (geniş bilezikli, kısa saplı) — S3 · S10 · S11
YERÇEKİMİ     3,721 m/s² = 0,379 g · yavaş çekim 0 kare
ATMOSFER      610 Pa · %95 CO₂ · 243 K · gün ışığı Dünya'nın %43'ü ·
              toz ~1,5 µm · 30 m/s rüzgâr = 9 Pa dinamik basınç (hiçbir şeyi
              devirmez, kumaş uçurmaz) · gölgeler YUMUŞAK KENARLI ve İÇİ DOLU
              (saçılma) — mutlak siyah gölge REDDİR
EKRAN YÖNÜ    hedef hep SOLDA (gemi · batı · alçak güneş) · ilerleme hep
              SOLDAN SAĞA (gemi → sahte koyu kabuk → süpürülmüş gerçek taş);
              dönüş hareketi SAĞDAN SOLA (S8) · gölgeler 14/14 karede
              SOLDAN SAĞA · alçak koyu sırt 14/14 karede ufkun SAĞ yarısında
              — 14 sahnenin 14'ünde sabit
SAYAÇ         METİNSİZ, MONOTONİK, iki kanal:
              ① bacak gövdesindeki toz yakası: S1 ince yaka → S6 bir el eni
                (tek çizgi) → S8 önceki izin ÜSTÜNDE (iki çizgi görünür) →
                S12 iki çizgi BİRLEŞİR ve durur (S13'te aynı)
              ② kalça kelepçesi: S0-S2 ikisi DOLU → S3-S10 üst yuva BOŞ →
                S11-S13 ikisi BOŞ
              ⛔ ikisi de yalnız KESMELER ARASINDA ilerler; klip İÇİNDE hiçbir
                sayaç değeri değişmez (T2V-CompBench 0,0687 ekseni kapatıldı)
EŞ KADRAJ     S0↔S1↔S4↔S13 (A) · S2↔S5 (B) · S3↔S7 (C) · S6↔S8↔S9↔S12 (D) ·
              S10↔S11 (E)
YIPRANMA      3 sabit bölge (sağ diz · sol önkol · sağ baldır) [D42]
              ⚠️ AÇIK: promptlar bölgeleri ADLANDIRMAZ, "dirt and wear staining
              stays fixed" kilidini taşır. İlk KABUL EDİLEN kare referanstır;
              ② DEVAMLILIK bu üç bölgeyi o kareye göre sayar.
IŞIK TAKVİMİ  MONOTONİK — tek alçak güneş batıda (kadrajın solunda), 14/14;
              gölge boyu yalnız UZAR (S13'te açıkça daha uzun), hiçbir sahnede
              kısalmaz · ikinci ışık yalnız kask içi cyan lamba · dolgu GERÇEK
SES REGISTER  HUMAN 0 · MACHINE 0 — ses yatağı: ince rüzgâr · giysi fanı ·
              nefes · tanelerin giysiye çarpması · kuyruksuz metal vuruşu
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı. Aşağıdaki beş kapının beşi de 10.09.2026'da
> `ffmpeg -hide_banner -filters` ile KURU KOŞULDU.

```
KAPI 1        KLİP İÇİ KESME YOK — her klip tek çekim (negatif çekirdeğin
              "single unbroken take" iddiası makinede ölçülür)
KOMUT         ffmpeg -hide_banner -i "$K" -vf "scdet=threshold=10,metadata=print:file=-" -f null - 2>&1 | grep -c "lavfi.scd.time"
              → 0 olmalı. >0 ise o klip REDDEDİLİR, yeniden üretilir.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · scdet VAR
              ffmpeg -hide_banner -filters | grep -q " scdet " || kapıyı yeniden yaz
İKAME         scdet yoksa: -vf "select='gt(scene,0.10)',showinfo" ve basılan
              kare sayısı 0 olmalı.

KAPI 2        GÖLGE İÇİ DOLGU — Mars saçılması; "mutlak siyah gölge" REDDİR (§3.2)
KOMUT         ffmpeg -hide_banner -ss <sn> -i "$M" -frames:v 1 -vf "signalstats,metadata=print" -f null - 2>&1 | grep -E "YMIN|YAVG"
              → kare YAVG ≥ 18/255 VE YMIN ≥ 10/255. Altındaysa sahne REDDEDİLİR.
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · signalstats VAR
              ffmpeg -hide_banner -filters | grep -q " signalstats " || kapıyı yeniden yaz
İKAME         signalstats yoksa: blackframe=amount=0:threshold=24 — hiçbir kare
              basılmamalı.

KAPI 3        MUTLAK SESSİZLİK 118,0-120,0 s (S11'in son iki saniyesi)
KOMUT         ffmpeg -hide_banner -i "$M" -af "silencedetect=noise=-60dB:d=1.8" -f null - 2>&1 | grep silence_
              → silence_start ≈ 118,0 (±0,2) ve silence_duration ≥ 1,9 s
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · silencedetect VAR
              ffmpeg -hide_banner -filters | grep -q " silencedetect " || kapıyı yeniden yaz
İKAME         astats=metadata=1:reset=1 ile 0,5 s'lik pencerelerde RMS_level
              ölçülür; 118,0-120,0 penceresi ≤ −70 dB olmalı.

KAPI 4        TESLİM SESİ — −14 LUFS · −1,0 dBTP (KURGU_RITMI §6)
KOMUT         ffmpeg -hide_banner -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -12
              → I ≈ −14 (±0,5) LUFS · Peak ≤ −1,0 dBTP
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · ebur128 VAR
              ffmpeg -hide_banner -filters | grep -q " ebur128 " || kapıyı yeniden yaz
İKAME         astats ile Peak_level (dBFS) + loudnorm=print_format=json kuru koşusu.

KAPI 5        KAMERA SABİTLİĞİ (14/14 lockoff)  ⚠️ ANA FİLTRE YOK
KOMUT         ⛔ vidstabdetect BU KURULUMDA YOK — kapı İKAME ile koşar (aşağıda).
DOĞRULANDI    ffmpeg 8.1 · 10.09.2026 · vidstabdetect YOK (kuru koşu ile ölçüldü)
              ffmpeg -hide_banner -filters | grep -q " vidstabdetect " → BOŞ
İKAME         ① ffmpeg -hide_banner -i "$K" -vf "scdet=threshold=3,metadata=print:file=-" -f null - 2>&1 | grep -c lavfi.scd.time
                 → 0 olmalı: lockoff klipte kare-arası fark eşiği geçmez.
              ② ffmpeg -hide_banner -i "$K" -vf "freezedetect=n=-60dB:d=2" -f null - 2>&1 | grep freeze
                 → S4 ve S13'te freeze BASILMAMALI: kadraj sabittir ama
                   yüzey tozu sürüklenir; basılıyorsa klip DONMUŞ demektir.
              ⚠️ Bu bir stabilizasyon ölçümü DEĞİL, vekildir; kapı bunu
                açıkça söyler [D142'nin dürüst kayıt kuralı].

KAPI 6        IZGARA — her klip tam 10,0 s
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$K"
              → 10.0 ± 0,04 (bir kare). Sapan klip yeniden üretilir, kırpılmaz.
DOĞRULANDI    ffprobe 8.1 · 10.09.2026 · mevcut (which ffprobe)
İKAME         ffmpeg -i "$K" 2>&1 | grep Duration
```

## 🅵 F BLOĞU — GÖZ KAPILARI [Ders 191]

> Bu maddeler makineye inmez: her biri **TEK KAREYLE** kapanır
> (`ffmpeg -ss <sn> -i "$M" -frames:v 1 "${TMPDIR:-/tmp}/kare.jpg"` → BAK —
> kare depo DIŞINA yazılır; repoya yalnız ÖLÇÜM girer).
> `rapor_kontrol.py --film` bu listeyi her koşuda ekrana basar. Açık □ madde
> varken parti KAPANMAZ; kapanmayan madde [D96] kilit defterine `⬜ AÇIK`
> girer ve o eksende skor SAYI TAŞIMAZ.

```
□ ① SIRT — hiçbir karede sırt ünitesi yok (sırt kadrajda: 22,0 · 82,0 · 134,0 s)
□ ② VİZÖR — düz dikdörtgen pencere + görünür metal çerçeve; kubbe/kavisli
     pencere YOK, ayna/çevre yansıması YOK, yüz okunuyor (36,0 · 106,0 · 118,0 s)
□ ③ BACAK SAYIMI — dört bacak; üçünde pabuç yüzeyde, dördüncüde (kadrajın
     solunda) pabuç HİÇ görünmüyor (14,0 · 44,0 · 134,0 s)
□ ④ TOZ — 1 NUMARALI RİSK, SAYIYLA ÖLÇÜLÜR [A5 · D192]:
     7,0 s'de halka çapı = 2 gövde genişliği · halkanın hiçbir noktası pabuç
     yüksekliğini AŞMIYOR · zerre yörüngesi DÜZ ve AŞAĞI (yatay sapma 0) ·
     20,0 s'de havada asılı zerre SIFIR · oturan katman BİR PARMAK kalınlığında
     ve 24,0 · 44,0 · 104,0 · 134,0 s'de aynı yerde duruyor (bir daha kalkmıyor)
     ⛔ toz perdesi / toz duvarı / yukarı savrulan toz: 0 kare
□ ⑤ KAZIK BAŞI — 38,0 s'de yerin üstünde vurulacak hiçbir şey kalmamış
     (bilezik yüzeyin ALTINDA, toz üstünü kapatmış)
□ ⑥ SAYAÇ ÇİZGİSİ — bacak gövdesinde toz yakası: 64,0 s'de BİR çizgi ·
     84,0 s'de İKİ çizgi (ikisi de görünür) · 124,0 s'de çizgiler BİRLEŞMİŞ
□ ⑦ KELEPÇE — 4,0 s iki dolu · 34,0 s üst yuva boş · 134,0 s iki boş
□ ⑧ METİN — hiçbir yüzeyde harf, rakam, işaret yok: giysi · gövde · zemin ·
     kaya · kasa (14/14 sahne · üretici filigranı da yok)
□ ⑨ HAT — 124,0 ve 134,0 s'de kadrajı çaprazlayan TEK gergin hat; ikinci
     ip, ikinci kayış, ikinci hat yok
□ ⑩ KASA — 134,0 s'de kasa YERDE ve kızak BOŞ (kasa kızakta DEĞİL)
□ ⑪ SESSİZLİK — 118,0-120,0 s dalga formunda mutlak sıfır (müzik · efekt ·
     oda tonu üçü de yok)
□ ⑫ GÖLGE YÖNÜ — 14/14 karede gölgeler SOLDAN SAĞA ve gölgelerin İÇİ DOLU
     (mutlak siyah leke yok)
```
