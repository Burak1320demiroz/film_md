# 📋 THE STANDING WIRE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paket üretildi: `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/PAKET_1..8`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                   ATMOSFER · IŞIK TAKVİMİ · EKRAN YÖNÜ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🏃 AKSİYON     → B BLOĞU                          MOD D
⑧ 💪 EFOR        → C BLOĞU'nun ZORLANMA satırı      MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE STANDING WIRE
FORMAT:            yatay 16:9 · 3-5 dk bandı
RUNTIME:           249 seconds (title card: YOK — screen text lock 0 s)
SCENE COUNT:       25  (S0-S24)
THEME:             UMUT
THEME SCENES:      S11 · S17 · S19 · S24     (dört — eşik üç)
                   S11 kamera+ışık: soğuk kadraja yandan ince sıcak sızıntı
                   S17 kinesik: avucun savunmadan açılışa geçişi
                   S19 kinesik: başın ışığa dönüşü
                   S24 nesne+ışık: iç ışık açık ve boş eldivenin üstünde
INTENDED EMOTION:  HUŞU (ölçek kontrastıyla satın alınır: S6 ve S19)
ENDING TYPE:       TERSİNE DÖNÜŞ (twist) + TOHUM BİLGİ
                   twist S24: altı askı, beşi dolu, biri boş
                   tohum S2 (8,0-10,0 s): barakanın duvarında tek boş askı
PROTAGONIST:       hat bekçisi, kadın, 38 (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    halkayı bırakır — S17
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0 / TELSİZ 0
SILENT SCENES:     25 / 25 (film tamamen sessiz)
VIRAL INTERSTITIALS: S3 · S12 · S17 · S18   ⛔ THESE MAY NOT BE CUT
KESİLEMEZ (novum döngüsü): S0 · S3 · S9 · S16 · S17 · S24  [ONERME §5]
TITLE:             "THE STANDING WIRE" — başlık izleyiciyi TELE bakmaya
                   gönderir; vaat: düşmeyen, sarkmayan bir hat.
LIBRARY CONTEXT:   aynı raf (yatay 3-5 dk): THE PAYLOAD (gezegen→yanaşma,
                   ama roketle) · THE SKYLIGHT (aynı ortam kartı, yeraltı) ·
                   THE BLACK CRADLE · THE COLD BURN (yanaşma, iticili araç).
                   Bu film o dördünden AYRIŞIR: 0 motor · 0 egzoz · 0 kalkış ·
                   0 iki-gövdeli geniş kare.
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      25
SHOT COUNT:      25 · sahne içi kesme 0
SCENE COUNT:     25          (üç sayım da eşit — sahne = çekim = klip [D101])
TARGET ASL BAND: 10,0 s (sabit ızgara — ASL eğrisi yok)
ASL CURVE:       ①10,0 ②10,0 ③10,0 ④10,0 ⑤10,0
  ⛔ GEREKÇE SATIRI [D74 · KURGU_RITMI §1]: bu film sabit ızgaralıdır.
     Her sahne tek klip, her klip 10 s, tek istisna hook'un 10→9 s
     kırpması. Kırpma bütçesinin TAMAMI oraya harcanır; ASL eğrisi
     bu ızgarada uygulanamaz ve uygulanmadığı burada kayıtlıdır.

GRID:            sahne başlangıcı(n) = 9 s hook + (n−1) × 10 s klip
                 S0=0 · S1=9 · S2=19 · S3=29 · S9=89 · S12=119 ·
                 S17=169 · S18=179 · S21=209 · S22=219 · S23=229 · S24=239
RUNTIME:         249 s = 4:09
RAW FOOTAGE:     25 klip × 10 s = 250 s
TRIM BUDGET:     1 s  — tamamı S0'da (10,0 → 9,0). Diğer 24 klip TAM
                 uzunlukta kalır; hiçbir klip DÜŞÜRÜLMEZ [D100].
SCREEN TEXT:     0 saniye — filmde başlık kartı, jenerik ve altyazı yok
CAMERA:          25 / 25 sabit lockoff · kamera hareketi 0 kare

SETUP SEQUENCE:  A E F C F E D E F C F E F | D N F C F E G H I J K L
                 (S0 → S24 · dosya sınırı S12 ↔ S13)
                 A EWS aşırı alt · C CU üst/OTS · D EWS üst uzak ·
                 E WS alt · F MS göz hizası cephe · N WS göz hizası profil ·
                 G MS omuz/yukarı · H WS arkadan OTS · I MS yapı cephesi ·
                 J WS hedefte · K ECU makro · L CU iç
                 KURULUM SAYISI plan sözlüğü 12 / 25 · BETİK ÖLÇÜMÜ 14 / 25
                 ⚠️ ikisi de doğru, fark 2 ve yeri bilinir (PLAN 🎥 açı yayı);
                   betik kamera SATIRININ imzasından türetir. Betik ölçümü
                   bandın (13) 1 üstünde. Dosya başına 5 ve 11.
                   Gerekçe: BOLUM_2 ⑫ + PLAN [D74]
ANGLE ARC:       6 açı TİPİ (aşırı alt · alt · göz hizası · üst · OTS/sırt ·
                 makro)   §2 eşiği 3 ✅
BİLİNÇLİ ŞOK:    2 / 2   → S12↔S13 (2 kademe) · S22↔S23 (3 kademe)
                 ⭐ Doruk EN YÜKSEK kontrast sıçramasını taşıyor [B4]

DORUK:           S22 → TEMAS, sahne başlangıcı 219,0 s
                 ⛔ HESAPLATILDI [D122]: 9 + (22−1) × 10 = 219,0 s
                 TEMAS = 219,0 + 6,0 (prompt TIMELINE ofseti) = 225,0 s = 3:45,0

REPLİK ZAMANLARI: YOK — bu filmde 0 replik var, formül uygulanacak kayıt yok.
                 Formül yine de burada durur ve bir replik eklenirse koşar:
                 replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti

PLANLI SESSİZLİK [⛔ D180 — bıçak KURGUDADIR, video modelinde değil]:
                 KURGUDA HARD MUTE: sn 214,0 – 239,0  (25 s)
                 ⛔ Bu aralık ⑪ ölçüm kapısında ÜÇ eşikte doğrulanır:
                    rapor_kontrol.py --olcum-sessizlik 214-239
                    silencedetect −50 / −40 / −30 dB
                    Aralık yoksa 🔴 TESLİM KUSURU — master yeniden ihraç.

FİNAL VURUŞ KANITI [D141]:
                 nesne: ASKI · saniye: 244,0 · kaç tane: 6 (5 dolu + 1 BOŞ)
                 BULUNAN mı BULUNMAYAN mı: BULUNMAYAN — altıncı askı BOŞ
                 ⭐ Tek karede sayılabilir ve adı konabilir.
                 ffmpeg -ss 244 -i "$M" -frames:v 1 kanit_askilar.jpg  → BAK
                 İKİNCİ KANIT: nesne TEL · saniye 244,0 · tek kavis taşıyor mu

DÖNGÜ KANITI:    bu film DÖNGÜ değil KAFİYE'dir [ACILIS_KAPANIS §1].
                 ilk kare (6,0 s) ↔ son kare (247,0 s):
                 aynı KOMPOZİSYON (iki koyu kütle + ortada dar parlak açıklık
                 + içinde hat · figür/eldiven SOL ALT ÜÇTE BİR)
                 FARKLI ölçek, ışık ve jest — kasıtlı.
                 DEĞİŞEN TEK DEĞİŞKEN: telin çizgisi düz → tek kavis (foveal)
                 ffmpeg -ss 6 -i "$M" -frames:v 1 ilk.jpg
                 ffmpeg -ss 247 -i "$M" -frames:v 1 son.jpg   → YAN YANA KOY
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111111111111111111-1-1
       (S0…S24 · 1 = insan var · - = insansız)
       insansız sahne: S21 · S23  (toplam 2)
       ⛔ Şeritte iki insansız sahne YAN YANA DEĞİLDİR ve ikisi de
         yanaşma setinin zorunlu vuruşlarıdır (V1 · V6).
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤ ⑧'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 23 sahnede kadrajda (S21 ve S23 insansız)
              mürettebat 0 · pilot 0 · klon 0 · yansıma 0 · ikinci gölge 0
              istasyonda insan 0 (pencerede yüz yok, rıhtımda karşılayan yok)

KASK          25 / 25 sahnede KAPALI · açık 0 sahne
              vizör TEK DÜZ PANEL, görünür koyu çerçeve içinde — kubbe DEĞİL
              optik berrak: 0 ton · 0 ayna kaplaması · 0 çevre yansıması
              sırt ünitesi YOK — düz siluet [D79]
              ⭐ S20'de kamera ARKADA: pozitif yüzey cümlesi zorunlu [D139]

NOVUM         KURAL: bu telin gerilimi yukarıdandır ve nettir — ona bağlanan
              her şey sabit hızda YÜKSELİR.
              İHLAL: yerçekimi altında bir cismin düşmemesi ve yükselmesi.
              KANIT: S0/S3 tel · S9 bağlantı parçası · S16-S17 üzengi ·
              S24 gerilim biter, tel İLK KEZ sarkar.
              ⛔ İhlal sayısı 1. Tele bağlı OLMAYAN her şey normal düşer.

YERÇEKİMİ     0,42 g = 4,12 m/s²
              düşen cisim 1 s'de 2,06 m · 2 s'de 8,24 m
              S17'de halka iki saniyede kadraj dışına düşer
              ⭐ Yürüyüş GERÇEK ZAMANLI — ağır çekim, zıplama, süzülme 0 kare

ATMOSFER      S0-S18  ince atmosfer ~1,0 kPa · gölge zayıf ve YUMUŞAK
                      kenarlı (MEŞRU, hata değil) · dolgu ışığı VAR ·
                      ses boğuk ve tizsiz · rüzgâr hiçbir şeyi deviremez
              S19-S23 VAKUM · gölge MUTLAK SİYAH ve jilet kenarlı ·
                      dolgu ışığı YOK · DIŞ SES SIFIR · lens küresel
              S24     BASINÇLI İÇ HACİM ~1 atm · 0 g · gölge mutlak siyah
                      DEĞİL · dolgu VAR · fan yatağı duyulur
              ⛔ Geçiş SAHNE SINIRINDA: S18 ince atmosferde biter,
                S19 vakumda başlar. Klip içinde ortam değişmez.
              ⚠️ ⑤ ve ⑥ merceklerine: S13-S18'de yumuşak gölge KUSUR DEĞİLDİR;
                S19-S23'te mutlak siyah gölge KUSUR DEĞİLDİR. İkisi ayrı karttır.

EKRAN YÖNÜ    Hedef HER karede kadrajın ÜST yarısındadır.
              Tel HER karede kadının ekran-SAĞINDA ya da tam merkezdedir —
              hiçbir sahnede soluna geçmez.
              İlerleme HER sahnede YUKARI; 25 sahnenin 25'inde sabit.
              Güneş S12-S18'de ekran-SOLDA, S19-S23'te ekran-SOLDA (filtresiz).
              ⛔ Ters dönüş 0 kare · aşağı yönelim 0 kare.

TAŞIYICI      Tele KENETLİ, telin kesik ucundan 400 m yukarıda başlar.
              Kendi motoru YOKTUR; telle birlikte 0,30 m/s yükselir.
              Toplama hızı 0,30 m/s · kadının çıkması gereken 14.000 m ·
              taşıyıcının 13.600 m → eşik ortalama 0,309 m/s.
              Köprüde kalan fark: 0,45 m = 1,5 saniye.
              ⛔ Bu sayıların hiçbiri prompt gövdesinde YOKTUR [D138];
                ekranda hiçbir gösterge, kadran ya da rakam yoktur.
              ⭐ Tam gerekçe: PLAN ⚖️ YARIŞIN ARİTMETİĞİ.

SAYAÇ         METİNSİZ. Telin kesik alt ucu ile kadının GÖZ HİZASI arasındaki
              fark. MONOTONİK, hiç geri dönmez:
                S0  uç botlarının hizasında (0)
                S3  uç plakadan ayrılır, dizinin üstüne çıkar
                S6  uç iki teras aşağıda (kadın önde)
                S9  uç TAM GÖZ HİZASINDAN geçer  ⭐ dönüm
                S12 uç başının epey üstünde
                S16 üzengi tek elinin bir kol boyu üstünde
                S18 iki elle alır — sayaç durur
              ⛔ Kadrajda gösterge, kadran, çentik, skala, rakam: 0.
                Bu film KART 5'in ikinci yönünü (yasak anlatımı siler)
                gösterge KOYMAYARAK değil, gösterge GEREKTİRMEYEREK çözer.

EŞ KADRAJ     S0 ↔ S24   (açılış-kapanış çifti · KAFİYE)
              S3 ↔ S9 ↔ S16   (C kurulumu · el üçlemesi)
              S5 ↔ S7 ↔ S11   (E kurulumu · tırmanış)
              S2 ↔ S4 ↔ S8 ↔ S10 ↔ S12   (F kurulumu · cepheden)

YIPRANMA      MONOTONİK · sabit bölge sayısı [D42 · D147]
                S0-S3    2 bölge  (bot · diz)
                S4-S12   4 bölge  (+ kolların ön yüzü · dirsek)
                S13-S18  5 bölge  (+ göğsün alt yarısı)
                S19-S24  5 bölge  (vakum: eklenmez, silinmez)
              ⛔ Hiçbir sahnede AZALMAZ. Klip İÇİNDE sabittir.
              ⛔ Faz ETİKETİ hiçbir prompta yazılmadı [D155] — yalnız tarifi.

ZORLANMA      Kanal: ELDİVEN YÜZEYİ, deri değil [⛔ D175].
              ✅ "the glove's ribbed segments tighten and lift over the knuckles"
              ✅ "the sleeve's fabric draws taut along the forearm"
              ⛔ "through the glove" kalıbı hiçbir promptta YOK.
              Zorlanma sahneleri: S1 · S3 · S4 · S7 · S9 · S16 · S17 · S18 · S20
              ⛔ Çıplak deri 0 kare. Yaka üstü · bilek · ayak bileği: üçü de kapalı.

SES REGISTER  HUMAN 0 · MACHINE 0 · TELSİZ 0 — film TAMAMEN SESSİZ.
              Ses dokusu merdiveni (monotonik incelme):
                S0-S3   geniş alçak hava tonu + çakıl
                S4-S12  ince hava tonu + eldiven/kaya + nefes
                S13-S18 neredeyse yok — yalnız giysi ve nefes
                S19-S23 DIŞ SES SIFIR — yalnız kask içi (nefes, kumaş)
                S24     fan yatağı GİRER (hava taşır)
              ⛔ ③ SES merceğine: "nothing audible" bulgusu S19-S23 için
                KUSUR DEĞİLDİR, tasarımdır. Kask içi ses o sahnelerde
                tek kanaldır.

IŞIK TAKVİMİ  MONOTONİK ARTAR — hiçbir yerde parlak→karanlık→parlak yok
                S0-S3   −9.000 m · doğrudan güneş YOK · soğuk mavi-gri
                S4-S10  −7.000…−3.000 m · karşı duvarın TEPESİ aydınlanır
                S11     −1.500 m · ilk doğrudan güneş hizasının ÜSTÜNDE
                S12-S18 0…+5.000 m · tam doğrudan güneş · gök koyu çivit
                S19-S23 vakum · filtresiz tek güneş · gök SİYAH · dolgu YOK
                S24     iç · 4500 K nötr beyaz · dolgu VAR
              ⛔ Bu takvim aynı zamanda TEMANIN yayıdır.

YÜZEY RENGİ   TEK CÜMLE, TEK BLOK [⛔ D176]:
              "the rock is dark blue-grey basalt; the loose dust caught in
               its lees is pale gold"
              ⛔ Hiçbir promptun LIGHT bloğu bir yüzeye renk atamaz.
                Kontrast garantisi ÖZNEYİ tarif eder.

İSTASYON      SİLUET: TEK HAT · film boyu DEĞİŞMEZ
              MODÜL 3 · KANAT 2 · RADYATÖR 3 · PORT 1 (alt yüz) ·
              PENCERE 1 büyük + 2 küçük · KELEPÇE 4
              Kapak sınıfı: GENİŞ / YANAŞMA (giysili gövde dönmeden geçer)
              ⛔ Dar kenetlenme kapağı bilerek KULLANILMADI — sırt üniteli
                gövde geçemez, fizik hatası olurdu [UZAY_USSU §2.3]
              Yaşlanma: tek faz — örtü sararmış ve mat · yüzey çukurcuklu ·
              tutamaklarda boya kalkmış · İTİCİ KURUMU YOK (itici yok)
              ⛔ Motor · nozzle · egzoz · alev · plume: 25 sahnenin 25'inde 0

ÖLÇEK MERDİVENİ  aynı nesne (modül gövdesi), aynı eksen, MONOTONİK
                 S19 %0,58 → S20 %3,8 → S21 %73+taşma → S22 %52+taşma →
                 S23 taşma
                 Ölçek şahidi her yapı planında en az bir:
                 S19 ① ön planda eldiven · S20 ① sırttan tam boy ·
                 S21 ②+③ dört kelepçe + taşan kenar · S22 ① taşıyıcı+kadın ·
                 S23 doku
```

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Aşağıdaki beş filtrenin beşi de KURULU OLDUĞU DOĞRULANDI.

```
KAPI ①        KAMERA SABİTLİĞİ — 25/25 lockoff iddiası ölçülür
KOMUT         ffmpeg -i "$M" -vf cropdetect=limit=0:round=2:reset=0 -f null - 2>&1 \
                | grep crop= | sort -u | wc -l
              (tek benzersiz crop satırı = kadraj hiç kaymadı)
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · cropdetect KURULU
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: her sahnenin ilk ve son karesi çıkarılıp elle
              üst üste konur (ffmpeg -ss <n> -frames:v 1)

KAPI ②        PLANLI SESSİZLİK — 214,0-239,0 s aralığı GERÇEKTEN sessiz mi
KOMUT         for T in -50 -40 -30; do echo "== $T dB"; \
                ffmpeg -i "$M" -af "highpass=f=300,lowpass=f=3400,silencedetect=n=${T}dB:d=0.3" \
                -f null - 2>&1 | grep silence_; done
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · silencedetect KURULU
              ffmpeg -hide_banner -filters | grep -q " silencedetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: astats ile saniyelik RMS dökümü + elle okuma
              ⛔ D180: üç eşikte birden bakılır. −50'de aralık çıkmazsa
                −30'da da yoksa 🔴 TESLİM KUSURU, master yeniden ihraç.

KAPI ③        KONTRAST — mat koyu giysi karanlıkta kayboluyor mu
KOMUT         ffmpeg -i "$M" -vf signalstats,metadata=print:key=lavfi.signalstats.YMAX \
                -f null - 2>&1 | head -40
              (aynısı YMIN için; her sahnede YMAX − YMIN ≥ 110 beklenir)
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · signalstats KURULU
              ffmpeg -hide_banner -filters | grep -q " signalstats " || kapıyı yeniden yaz
İKAME         filtre yoksa: sahne başına tek kare + histogram bakışı
              ⚠️ D176: kontrast ÖLÇÜMLE koşulur; promptta yazılan kontrast
                garantisi bir ölçüm değil, bir renk atamasıdır.

KAPI ④        DONMUŞ KARE — sabit lockoff'ta klip gerçekten hareket ediyor mu
KOMUT         ffmpeg -i "$M" -vf "freezedetect=n=0.003:d=2" -f null - 2>&1 \
                | grep freeze
              (⛔ hiçbir sahnede 2 s'lik donma olmamalı — SAHNE_ZINCIRI §1:
               klibin içi boş bırakılamaz, tek sürekli hareket sürer)
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · freezedetect KURULU
              ffmpeg -hide_banner -filters | grep -q " freezedetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: her sahnenin 2. ve 8. saniyesi çıkarılıp
              yan yana konur

KAPI ⑤        SİYAH KARE / KART SIZINTISI — kapak ya da jenerik zincire karıştı mı
KOMUT         ffmpeg -i "$M" -vf "blackdetect=d=0.2:pic_th=0.98" -f null - 2>&1 \
                | grep black_start
              (⛔ beklenen sonuç: HİÇ SATIR YOK. Bu filmde başlık kartı,
               jenerik ve kapak çıktısı zincire GİRMEZ [D70/D72])
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · blackdetect KURULU
              ffmpeg -hide_banner -filters | grep -q " blackdetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: masterın ilk ve son 10 saniyesi tek tek bakılır

KAPI ⑥        SÜRE VE KLİP SAYISI — üç sayım eşit mi [D101]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              (beklenen: 249,0 ± 0,5 s · SCENE 25 = SHOT 25 = CLIP 25)
DOĞRULANDI    ffprobe 8.1 · 05.09.2026 · KURULU
İKAME         yok — ffprobe olmadan teslim ölçülemez

KAPI ⑦        FİLİGRAN / KÖŞE TESTİ [D150]
KOMUT         for T in 5 60 120 180 240; do \
                ffmpeg -ss $T -i "$M" -frames:v 1 kose_$T.jpg; done  → DÖRT KÖŞEYE BAK
              (⛔ üretici ikonu varsa master master değildir)
DOĞRULANDI    ffmpeg 8.1 · 05.09.2026 · KURULU
İKAME         yok — bu kapı gözle koşar, rubrik göremez (altı mercek görmedi)
```

---

## 🧾 SPEC BÜTÜNLÜK KAYDI

```
□ A bloğu dolu · tema üç sahneden fazla · merkezî seçim sahne numaralı
□ B bloğu dolu · doruk saati FORMÜLLE hesaplatıldı (219 + 6,0 = 225,0) [D122]
□ B bloğu ASL gerekçe satırı yazıldı (sabit ızgara) [D74]
□ B bloğu FİNAL VURUŞ KANITI sayılabilir ve adı konabilir [D141]
□ C bloğu SAYI taşıyor, tarif değil
□ E bloğu beş filtre + ffprobe · beşinin de DOĞRULANDI satırı gerçek koşuyla
  yazıldı (ffmpeg 8.1 · 05.09.2026)
□ Planlı sessizlik aralığı yazıldı ve ölçüm komutu verildi [D180]
□ QA PAKETİ üretildi: QA_PROMPTLARI/FILME_OZEL/THE_STANDING_WIRE/ [D165]
□ prompt_kontrol.py KLASÖR MODU koştu (05.09.2026): 0 BLOCK · film GO
  "📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik" satırı çıktıda VAR
□ Açık kalan 4 uyarı (S21/S23 negatif çekirdek) KART 10'un reçetesidir,
  kusur değil — gerekçe BOLUM_2 ⑭ ve PLAN 📏 kaydında
```
