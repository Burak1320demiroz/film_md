# 🌅 THE DAWN FRONT — Şafak Cephesi

## AI Production Bible — Full Format V3 (Self-Contained Prompts · Sahne İçi Kesme)

### 14 Sahne × 10 s = 140 s | 26 Segment · 12 Kesme | 16:9 Yatay | İnce Atmosfer | Bilimkurgu

### _"Burada gündoğumu bir ışık değil. Saatte kırk sekiz kilometre hızla gelen bir duvar."_

---

# 🧭 BÖLÜM 0 — PLAN

> Bu bölüm `KILAVUZ_REHBERI.md` §6 adım 1'dir ve üretimden önce yazıldı.
> Sıralama: PLAN → BIBLE → PLAN KONTROL → PROMPT.

## 0.1 DÖRT SORU

```
① YÖN?    yatay 16:9
② SÜRE?   2-4 dk  → 14 sahne × 10 s = 140 s (2:20)
③ TÜR?    bilimkurgu     → KILAVUZ_REHBERI §4.1 + UZAY_SENARYO_KILAVUZU
④ ORTAM?  ince atmosfer  → KILAVUZ_REHBERI §3.2 + Ders 39, 41
           referans film: LOW_POWER (aynı ortam kartı)
```

**Ortam neden ince atmosfer:** Filmin bütün görseli **süblimleşme** üzerine
kurulu — katı donun sıvıya uğramadan doğrudan gaza geçmesi. Bu ancak düşük
basınçta olur ve çıkan jetler ancak seyrek havada **keskin** kalır (kuyruklu
yıldız jetleri, Triton gayzerleri). Kalın atmosferde jet dağılır ve duvar
oluşmaz; vakumda toz hiç çökmez ve yerdeki iz okunmaz. Bu filmin fiziği tam
olarak §3.2 kartıdır.

---

## 0.2 ⭐ BU FİLMİN FARKI — KESME PROMPTUN İÇİNDE

> Bu deponun bugüne kadarki filmlerinin hepsi "tek kesintisiz çekim"
> kuralıyla yazıldı. Bu film aksiyonu hissettirmek için sahne içinde
> kesiyor **ve kesmeyi promptun içine yazıyor.** Gerekçesi ve riski
> burada, en başta duruyor.

### Neden bu Ders 1'i ihlal etmiyor

```
DERS 1 DİYOR Kİ    "AI video modelleri sahne içinde kesme yapıyor.
                    3 filmde de tekrarladı — EN YAYGIN HATA."
                    Gizli kesme 8/8 filmde tetiklendi.

YANİ              Model zaten kesiyor. Bugüne kadar yaptığımız şey,
                  kesmeyi YASAKLAMAK ve modelin bizim seçmediğimiz
                  yerlerden kesmesini izlemekti.

BU FİLM           Kesmeyi yasaklamıyor — TAKVİME BAĞLIYOR.
                  12 kesmenin 12'sinin saniyesi, lensi, mesafesi ve
                  yeni kadrajın içeriği promptun içinde yazılı.
                  Kontrolsüz bir hata, sayısal bir kilide dönüyor.
```

Kılavuz bunu zaten meşru sayıyor: `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU §11`
karar tablosu *"Bilinçli sert kesme → ✅"*, §5.3 *"⚠️ HEPSİNİ GİZLEME. Amaç
'hiç kesme yok' numarası yapmak değil."*

### ⛔ EN KRİTİK KURAL — "no cuts" bu promptlardan ÇIKARILDI

```
Kontrol listesi A1, deponun EN PAHALI HATASI olarak şunu yazıyor:
  "Aynı dosyada hem YASAK hem ANLATIM varsa → PLAN BOZUK.
   Model her zaman YASAĞI seçer, anlatım sessizce ölür."
  (Gerçek olay: Tidal Hunt · satır 285 `NEVER text` + satır 338
   `the countdown reads 6:00:00` → sayaç ekrana hiç çıkmadı.)

Bu filmde kesme İSTENİYOR. O hâlde "no cuts" cümlesi bir çelişkidir ve
çok çekimli sahnelerin negatif bloğundan ÇIKARILDI. Yerine sayısal bir
takvim kondu:

  ❌ ASLA YAZMA   "Single unbroken take: no cuts, no transitions"
                  (bir kesme isterken)
  ✅ YAZ          "CUT SCHEDULE: exactly two hard cuts, at 3.0s and
                   7.0s, and no others. Each of the three segments is
                   a single unbroken locked-off take with no camera
                   movement inside it. No dissolve, no fade, no wipe,
                   no morph, no speed ramp at either cut."

Yani yasak kalkmadı, YER DEĞİŞTİRDİ: artık "kesme yok" değil,
"yazılı kesmelerden BAŞKA kesme yok" diyoruz. Tek çekimli 7 sahnede
eski cümle aynen duruyor.
```

### 0.2.1 KESME GRAMERİ — yedi kural

```
① EKSEN KİLİDİ — 26 segmentin 26'sında geçerli
   Cephe her karede SOLDAN gelir. Kaçış her karede SAĞA doğrudur.
   Kamera hiçbir segmentte eksenin öbür yanına geçmez (180° kuralı).
   Bir tek segmentte eksen atlanırsa kovalamaca "karışıklık" olur.

② 30° / ÖLÇEK KURALI
   Ardışık iki segment ya en az 30 derece açı ya en az bir tam ölçek
   kademesi (çok geniş → geniş → orta → yakın) farkı taşır. İkisi de
   yoksa kesme "atlama" olarak okunur ve hata sanılır. Her sahnenin
   KESME PLANI bloğunda bu fark yazılıdır.

③ HAREKET ÜZERİNDE KES
   Kesme daima bir hareketin ORTASINDA olur, duruşta değil. Kesilen
   kare ile açılan kare aynı yöndeki hareketi sürdürür.

④ HER SEGMENT KENDİ KURULUMUNU TAM YAZAR
   ⭐ Bu, kesmeyi prompta koymanın bedelidir ve tek panzehiri budur.
   İmaj promptu yalnız A segmentinin ilk karesidir; B ve C'nin
   referans imajı YOKTUR. O yüzden video promptunda B ve C için
   lens + mesafe + açı + kadrajdaki her nesne YENİDEN yazılır.
   Eksik yazılan segmenti model uydurur ve kıyafet/ölçek kayar.

⑤ KESME SAYISI = GERİLİM EĞRİSİ
   Aksiyon sahnesi 3 segment (2 kesme) · nefes sahnesi 1 segment
   (0 kesme). Filmin en gergin sahnesi (S7) TEK ÇEKİMDİR: on iki
   kesmelik bir filmde kesmesiz on saniye, tehlikenin kendisidir.

⑥ SEGMENT SÜRELERİ SAYIYLA YAZILI
   3+4+3 · 5+5 · 4+6 · 10. Toplam her sahnede tam 10 saniye.
   Saniyeler hem MOTION bloğunda hem CUT SCHEDULE satırında geçer.

⑦ KAMERA SEGMENT İÇİNDE SABİT — 26/26 lockoff
   Risk Kartı 8: kamera projede çözülmüş TEK kategori (Low Power
   8/10, diğer 9 filmde 2-4).
   ⭐ Bu filmin tezi: AKSİYON KAMERA HAREKETİNDEN DEĞİL, KESMEDEN
     GELİR. Sabit kamera + kadrajı geçen hızlı kütle + sert kesme =
     klasik aksiyon grameri. Hareketli kamera bu depoda hem kesme
     uydurttu hem hızı sildi.
```

### 0.2.2 ⚠️ AÇIK RİSK — dürüst olmak gerekirse

```
Kesmeyi prompta yazmanın iki bilinen bedeli var ve ikisi de gerçek:

RİSK 1 — REFERANSSIZ SEGMENT
  İmaj promptu yalnız A'yı bağlar. B ve C'yi model yorumlar.
  Beklenen bozulma: kıyafet detayı, araç ölçeği ve yüz kaymaları
  ikinci ve üçüncü segmentte artar.
  KARŞI ÖNLEM: kural ④ — her segmentin kadraj içeriği tam yazılı;
  kıyafet bloğu ve araç kartı segment başına tekrarlanıyor.

RİSK 2 — KESMENİN GEÇİŞE DÖNÜŞMESİ
  Model "cut" kelimesini bazen çapraz bindirme veya morph olarak
  çiziyor. Bu bir Ders 1 türevi ve henüz ölçülmedi.
  KARŞI ÖNLEM: CUT SCHEDULE satırında beş ayrı yasak —
  "no dissolve, no fade, no wipe, no morph, no speed ramp".

📊 ÜRETİMDE ÖLÇÜLECEK TEK SORU
  Kesmeler yazıldığı saniyede ve yazıldığı kadrajla mı çıkıyor?
  Çıkmıyorsa çözüm §0.20'de: aynı film 26 ayrı klip olarak üretilip
  kurguda birleştirilir. Plan bu ihtimale hazır yazıldı — her
  segmentin kendi kurulumu zaten tam, ayrı prompt hâline gelmesi
  için ek yazı gerekmiyor.
```

## 0.3 NOVUM — tek cümle, ilk 3 saniyede görünür

> **Bu gezegende gündoğumu bir ışık değil bir cephedir: güneş donmuş
> zemine değdiği anda yer gaza dönüşüp altmış metrelik bir duvar hâlinde
> patlıyor — ve o duvar saatte kırk sekiz kilometre hızla ilerliyor.**

Novum bir **durum** değil, dünyanın **kuralı**dır ve olay örgüsünü zorunlu
kılar (UZAY_SENARYO_KILAVUZU §1'in ölçümle doğrulanmış şartı):

```
Kural saati başlatır  → film ilk karede başlamış bir kovalamacadır (S0)
Kural yolu çizer      → çıplak kayada patlama yok; rota kara lekeler
                        zinciridir (S3)
Kural tuzağa sokar    → beyaz ovada motoru kapatmak zorunda; hızını
                        veren şey aynı zamanda zemini patlatan şey (S6)
Kural direnir         → motoru açıp son 210 metreyi sürmeyi DENİYOR ve
                        zemin tekerleğin altında gaza dönüşüyor (S9)
Tek çıkış yolu        → aynı hatayı silah olarak kullanmak (S10)
```

**Bilim çapası:** Yavaş dönen bir gezegende terminatör ekvatorda 157 km/s
ilerler — kaçılmaz. **72. enlemde 157 × cos(72°) = 48 km/s.** Karakterin
hayatta olma ihtimali tek bir kosinüsün içindedir: *bu gezegende yalnız
kutuplara yakın yerlerde kaçabilirsin.*

## 0.4 KANCA — YER değil DURUM

```
0-3 s   ⭐ NOVUM      Karanlık ovada ufuk turuncuya dönüyor ve o çizgi
                     boyunca ZEMİN BEYAZA PATLIYOR — 60 m'lik bir duvar
3-7 s   ⭐ AKSİYON    Rover kadraja soldan tam hızda giriyor, dört
                     tekerlek don püskürtüyor, arkasında duvar
7-10 s  ⭐ SAYAÇ      Dikiz aynası: duvar aynanın sekizde birini
                     dolduruyor. Film buradan itibaren bir kronometre
```

Kanca bir YER göstermiyor: **ilk karede kovalamaca çoktan başlamış.**
Manzara kancası yasağı (UZAY_SENARYO_KILAVUZU §15) kapalı. Ve ilk 10
saniyede iki kesme var — ritim ilk saniyeden kuruluyor.

## 0.5 ANTAGONİST KANALI

```
Kanal 1 (çevre)        S0-S9    cephe: konuşmayan, yavaşlamayan, sabit
Kanal 4 (kendi seçimi) S10-S13  ⭐ asıl antagonist
```

Değer çatışması: **kaçmak için, kaçmasının sebebini yakmak zorunda.**
Kimse kötü değil. Cephe bir gündoğumudur; onu durdurmak imkânsızdır ve
zaten kimseye kızgın değildir.

## 0.6 ÇEHOV — dört halkalı zincir, dördü de görülüyor

```
HALKA 1  S3   Uzakta cephe çıplak kaya sırtına varıyor ve orada
              YÜKSELMİYOR — 40 metrelik bir çentik açılıp iki yanda
              devam ediyor. → İzleyici kuralı GÖRÜYOR: don yoksa duvar yok.

HALKA 2  S5   Roverin sol arka bacası 600 °C. Geçtiği yerde don 0.4
              saniyede gaza dönüşüyor ve arkasında 1.8 m genişliğinde
              ÇIPLAK kaya izi kalıyor. → Araç bir yakıcıdır.

HALKA 3  S9   Aynı baca beyaz ovada felakettir: zemin tekerleğin altında
              gaza dönüşüyor, tekerlek 0.4 m çukura giriyor.
              → Aynı özellik, ters sonuç. Silah önce onu vuruyor.

HALKA 4  S10  Üçü birleşiyor: roveri bacası tam açık hâlde CEPHEYE
              DOĞRU geri gönderiyor. Kurulum yeni bir alet getirmiyor;
              üç sahnede gösterilen tek özelliğin doğru kullanımı.
```

**Ters simetri:** S0'da rover cepheden kaçıyor. S10'da aynı rover cepheye
gidiyor. Aynı araç, ters yön, ters anlam.

## 0.7 ETKİNLİK ÇAPALARI (§9.1 — üç ölçümün de 4/10 aldığı kategori)

```
1. TERCİH ÇAPASI     S10, segment A. Eli güç kolunda 2 saniye duruyor,
                     sonra kolu sonuna kadar itip vitesi GERİ alıyor.
                     Doruk bir SAHNENİN, hatta bir SEGMENTİN içinde.

2. TEPKİ ÇAPASI      S4, segment B. Kırık arazide karot silindiri
                     kayışında zıplıyor; eli refleksle ona gidiyor,
                     kayışı sıkıyor, sonra direksiyona dönüyor.
                     (Ring Walker 1:12'de tam olarak bunu yapmadı.)

3. BAŞLANGIÇ AMACI   S0, segment B, 0. saniye. Rover zaten tam hızda ve
                     kadrajın sağına, gemiye doğru gidiyor.

4. ZORLANMA ÇAPASI   S7. Motoru kapalı süzülürken hiçbir şey yapamıyor.
                     Yetkinliğin işe yaramadığı 10 saniye.

5. 🆕 BAŞARISIZ DENEME  S9. Önce apaçık çözümü deniyor (motoru aç, son
                     210 metreyi sür) ve dünya hayır diyor. Yetkinlik
                     kuralı korunuyor: hata bilgi eksikliğinden değil,
                     seçeneksizlikten. Ve S10'un seçimi bu yüzden
                     zekice değil, ZORUNLU okunuyor.
```

**Kamera-taşıyıcı testi:** Karakteri drone ile değiştirirsem S10 kaybolur —
drone geldiği sebebi yakmayı seçmez. ✅ Test geçildi.

## 0.8 JEST TEKRARI DENETİMİ (Ring Walker Yapı 5/10)

```
Aynaya bakma          S0-C · S4-C · S8-B
                      → 3 kez, ama bu bir JEST DEĞİL, bir SAYAÇ.
                        Kadraj birebir aynı; değişen tek şey aynanın
                        içindeki duvarın boyu (§0.11 tablosu).
Güç koluna uzanma     S6-B (kapat) · S9-A (aç, dene) · S10-A (aç, feda et)
                      → 3 kez ama AYNI JEST DEĞİL: tırmanan bir karar
                        merdiveni — geri çekilme, deneme, vazgeçme.
                        Üçü de farklı bilgi taşıyor. ✅
Karot silindirine     S4-B (koruma) · S10-B (bırakma) → 2 kez, ters anlam ✅
dokunma
Yukarı bakma          0 kez — bilinçli. Bu filmde kimsenin yukarı
                      bakacak vakti yok.
```

## 0.9 RİSK SAYIMI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

```
□ KART 1  Su / sıvı .................. YOK    0 sahne   ✅ 🔴 kart elendi
□ KART 2  Canlı / hayvan ............. YOK    0 sahne   ✅ 🔴 kart elendi
□ KART 3  Kask / vizör ............... VAR    → HELMET STATE SCHEDULE
□ KART 4  İkinci figür ............... VAR    → HUMAN COUNT LOCK
□ KART 5  Ekran / sayaç / gösterge ... VAR    → metinsiz, DİKİZ AYNASI
□ KART 6  Parçacık / patlama ......... VAR    → 🔴 bu filmin en pahalı kartı
□ KART 6b Katmanlı dünya ............. YOK    → tek katman
□ KART 7  Diyalog .................... YOK    0 replik ✅ 🟡 kart elendi
□ KART 8  Kamera hareketi ............ YOK    26/26 segment sabit lockoff ✅

RİSK SAYISI: 4 / 9      ✅ eşiğin altında
🆕 KARTLARDA OLMAYAN RİSK: sahne içi kesme — §0.2.2
```

**Elenebilir üç kartın üçü de sıfırlandı** (su, canlı, diyalog) — üstelik
canlı kartı bir önceki filmde (THE HERD) açıktı ve orada risk 6/9'du.

```
⚠️ KART 6 bu filmin merkezinde ve kartın kanıtı kötü:
  Low Power Parçacık 2/10 — projenin en düşük tek skoru
  Kaleida patlama filmiydi ve parçacık HİÇ ölçülemedi
  → Karşı önlem §0.13'te SAYISAL: jet hızı 200 m/s, duvar 60 m,
    süblimleşme 0.4 s, toz çökme 40 s, hiçbir yerde sıvı yok.
    Ve "explosion / blast / smoke / flame" kökleri 28 promptun
    hiçbirinde pozitif betimlemede geçmiyor (Ders 56 + 59).
```

## 0.10 SAHNE HARİTASI — 14 sahne × 10 s = 140 s

| # | Sahne | İskelet | Segment | Kesme | Kesme saniyesi | Cephe |
|---|---|---|---|---|---|---|
| S0 | **HOOK** — ufuk patlıyor | novum + problem | **3** | 2 | 3.0 · 7.0 | 900 m |
| S1 | Aynı hız — kural | dünyanın kuralı | 1 | 0 | — | 880 m |
| S2 | ⭐ **VİRAL** — duvarın yüzeyi | saf görsel | 1 | 0 | — | — |
| S3 | ⭐ **ÇEHOV 1** — kayadaki çentik | kurulum | 1 | 0 | — | 840 m |
| S4 | **AKSİYON** — kırık arazi | ilk çatlak | **3** | 2 | 3.0 · 7.0 | 700 m |
| S5 | ⭐ **VİRAL + ÇEHOV 2** — baca | kurulum | 1 | 0 | — | 660 m |
| S6 | Beyaz ova — motoru kapat | kural direnir | **2** | 1 | 5.0 | 620 m |
| S7 | **Sessiz süzülme** | ⭐ nefes = tehlike | 1 | 0 | — | 480 m |
| S8 | Duruş — 210 m eksik | değer çatışması | **2** | 1 | 4.0 | 400 m |
| S9 | 🆕 **DENEME** — zemin çöküyor | kural İKİNCİ kez direnir | **3** | 2 | 3.0 · 7.0 | 330 m |
| S10 | ⭐ **DORUK** — roveri geri gönderme | **SEÇİM** | **3** | 2 | 3.0 · 7.0 | 260 m |
| S11 | **PATLAMA** — duvar kırılıyor | bedelin sonucu | **3** | 2 | 3.0 · 7.0 | 200→0 |
| S12 | **OVERVIEW** — 200 km'lik duvardaki çentik | ölçek · tema | 1 | 0 | — | — |
| S13 | **FİNAL** — iki duvarın arasında | held frame | 1 | 0 | — | geçti |

```
TOPLAM        14 sahne · 26 segment · 12 kesme · 140 saniye
              28 prompt (14 imaj + 14 video)
VİRAL ARA     S2 ve S5 — bunlar KESİLEMEZ
OVERVIEW      S12, tam olarak bir tane (§15: iki overview etkiyi yarıya indirir)
TEK ÇEKİMLİ   S1 · S2 · S3 · S5 · S7 · S12 · S13 — bu 7 sahnenin
              promptunda "single unbroken take, no cuts" cümlesi AYNEN durur
ÇOK ÇEKİMLİ   S0 · S4 · S6 · S8 · S9 · S10 · S11 — bu 7 sahnenin
              promptunda o cümle YOKTUR, yerine CUT SCHEDULE vardır (§0.2)
```

## 0.11 ⭐ İKİ SAYAÇ — ikisi de metinsiz

`Risk Kartı 5` iki yönlüdür: model ekrana anlamsız yazı ekler (Ders 13/34/45)
**ya da** "no text" yasağı anlatımı siler (Ders 50 — Tidal Hunt'ın sayacı hiç
ekrana çıkmadı). Bu filmde gösterge diye bir şey yok; sayaç **çevrede**.

### SAYAÇ A — DİKİZ AYNASI (birebir aynı kadraj, üç kez)

| Segment | Cephe mesafesi | Aynadaki duvarın doldurduğu alan |
|---|---|---|
| S0-C | 900 m | **1/8** — ince beyaz bir çizgi |
| S4-C | 700 m | **1/2** — aynanın yarısı |
| S8-B | 400 m | **tamamı** — aynada başka hiçbir şey yok |

```
75mm, sabit, 2.5 m, roll bar üstündeki 0.2 m'lik ayna kadrajın
merkezinde, sürücünün omzu sağ kenarda. Üç segmentte de AYNI kurulum.
Değişen tek şey aynanın içindeki beyaz. Rakam yok, doluluk var.
⚠️ Holding Field dersi: orada sayaç 9 küçük segmentti ve MANTIK
   raporunda hiç görünmedi (COUNTER CURVE: NONE) — telefonda
   okunmuyordu. Bu sayaç aynanın TAMAMI kadar büyük.
⚠️ Üçü de birer KESME SONRASI kadrajdır (S0'da 7.0s, S4'te 7.0s,
   S8'de 4.0s). Yani referans imajı yok — kural ④ gereği kadraj
   içeriği üç promptta da tam ve aynı kelimelerle yazılı.
```

### SAYAÇ B — GÜNEŞ

Cephe zaten terminatördür; yani **güneşin yüksekliği sayacın kendisidir.**

| Sahne | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 | S12 | S13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Güneş | −4.0° | −3.6° | −3.4° | −3.0° | −2.4° | −2.1° | −1.8° | −1.3° | −0.9° | −0.6° | −0.35° | −0.15° | +0.1° | **+0.4°** |

```
Monotonik ve geri dönüşsüz: film boyunca ışık ARTAR. S0'da güneş ufkun
altında ve tek ışık cephenin kendi parlaklığıdır; S13'te güneşin kenarı
yükselmiştir ve doğrudan yüze vurur.
⭐ IŞIK = TEMA. Filmin sonunda kazanılan şey ışıktır ve bedeli onu
  görmek için gerekli olan şeyi yakmak olmuştur.
KONTROL: dizi hiç geri dönmüyor (−4.0° → +0.4°).
```

## 0.12 SAYISAL KİLİTLER (§C — tarif kilidi %0 tuttu, sayısal kilit %100)

```
□ İNSAN SAYISI    HUMAN COUNT LOCK: tam 1 insan, 26 segmentin 26'sında.
                  Mürettebat yok, ikinci silüet yok, aynada ikinci
                  yansıma yok, vizörde ikinci yüz yok.
                  ⚠️ S10-B (araçtan iniş) Risk Kartı 4'ün tam hedefi —
                  Kaleida 1:25 ve Tidal Hunt 0:00/1:49 klonlarının üçü
                  de araca inme/binme anında çıktı. O segmentte gemi
                  kadrajda YOKTUR ve negatif blokta "koltuk BOŞ" ayrıca
                  yazılıdır.
                  ⭐ Gemiye biniş bu filmde HİÇ gösterilmez — film
                    gemiye 200 metre kala biter (held frame, S13).

□ KASK TAKVİMİ    HELMET STATE SCHEDULE: kapalı 26 segmentin 26'sında.
                  Açık: 0. Ara durum yok, geçiş yok.
                  Gerekçe fizikte: %1.2 basınç, solunamaz.

□ ÖLÇÜ            adam 1.78 m · rover 3.2 × 1.8 m · tekerlek çapı 0.9 m ·
                  ayna 0.2 m · karot silindiri 0.9 m / 40 kg · baca
                  ızgarası 0.5 m · gemi 16 m · don tabakası 0.40 m ·
                  duvar yüksekliği 60 m · çentik genişliği 40 m

□ YERÇEKİMİ       0.28 g (2.75 m/s²). Serbest düşüş: 1 saniyede 1.37 m,
                  2 saniyede 5.5 m. Ağır çekim panzehiri §0.14'te.

□ SIVI TEMASI     0 sahne. ⭐ BU FİLMDE HİÇ SIVI YOKTUR. Don katıdan
                  DOĞRUDAN gaza geçer; erime, ıslanma, damlama,
                  su birikintisi, buhar yoğuşması hiçbir karede yok.

□ CANLI ANATOMİSİ 0 canlı, 26 segmentin 26'sında.

□ HIZ             cephe 13.3 m/s (48 km/s) — 26 segmentin hepsinde aynı.
                  rover düz zeminde 14.4 m/s · kırık arazide 8.3 m/s ·
                  motorsuz süzülmede 14.4 → 0 (yavaşlama 0.15 m/s²) ·
                  geri viteste 6 m/s · koşan adam 5 m/s · jet 200 m/s

□ 🆕 KESME        CUT SCHEDULE: 12 kesme, 12 saniye değeri yazılı.
                  Yazılı kesmelerden BAŞKA kesme yok; bindirme, fade,
                  wipe, morph, hız rampası hiçbir sahnede yok.
                  Segment içinde kamera hareketi 0.
```

## 0.13 ⭐ CEPHE — filmin fizik sözleşmesi

```
GEZEGEN     yarıçap 2400 km · dönme süresi 96 saat · 0.28 g
            ince CO2/N2 atmosferi, deniz seviyesi basıncının %1.2'si

GECE YÜZÜ   96 saatlik gecede zemine 0.40 m kalınlığında katı azot-
            karbondioksit donu çöker. Mat, taneli, kemik beyazı, kuru.

CEPHE       Terminatör çizgisi. Doğrudan güneş ışığı dona değdiği anda
            don SIVIYA UĞRAMADAN gaza geçer — 0.4 saniyede. Genleşen
            gaz taneleri ve çakılı 200 m/s ile yukarı fırlatır. Sonuç:
            60 metre yüksekliğinde, ufuktan ufka, ilerleyen beyaz duvar.

HIZ         Ekvatorda 157 km/s — kaçılmaz. 72. enlemde 48 km/s = 13.3 m/s.

KURAL 1     DON YOKSA DUVAR YOK. Çıplak kaya sırtlarında don birikmez;
            cephe oraya vardığında hiçbir şey olmaz, sadece ışık geçer.
            → S3'te uzaktan, S11'de yakından görülür.

KURAL 2     ISI DA SÜBLİMLEŞTİRİR. 400 °C üstü her yüzey donu 0.4
            saniyede gaza çevirir ve arkasında çıplak kaya bırakır.
            Roverin 600 °C'lik baca ızgarası tam olarak budur.
            → S5'te avantaj, S9'da felaket, S10'da silah.

KURAL 3     BOŞLUK KALICI DEĞİL. Açılan çentik, iki yandaki gazın yanal
            yayılmasıyla 8 saniyede kapanır. Adamın geçmesi için 6
            saniye gerekir. Marj: 2 saniye.
```

### Beyaz ova tuzağı — filmin mekaniği

```
3 km'de rota 900 metrelik kesintisiz don ovasına giriyor. Tek bir
çıplak leke yok.

PROBLEM   Baca 600 °C. Ova boyunca açık kalırsa zemin ARACIN ALTINDA
          gaza dönüşür (Kural 2). Hızını veren şey, onu durduracak şey.
ÇÖZÜM     Motoru kapatıp süzülmek. Baca 40 saniyede griye iner.
BEDEL     0.15 m/s² yavaşlamayla 14.4 m/s'den menzil: 690 metre.
          Ova 900 metre. → 210 METRE EKSİK.
DENEME    S9: motoru yeniden açıp son 210 metreyi sürmeyi deniyor.
          Baca 600 °C'ye çıkıyor, zemin sol arka tekerleğin altında
          0.4 saniyede gaza dönüşüyor, tekerlek 0.4 m çukura giriyor,
          araç 30 metrede duruyor ve yana yatıyor.
          → Apaçık çözüm denendi ve dünya hayır dedi. S10 artık
            zekice bir fikir değil, TEK seçenek.
```

```
⚠️ NEGATİF ÇEKİRDEKLE İKİ ÇELİŞKİ — bilerek ve açıkça çözüldü

① "No water, no ice" — bu filmde zemin DONDUR.
   ÇÖZÜM: yasağın amacı su fiziğini engellemek. Don burada su değil,
   katı azot-karbondioksittir ve asla erimez. Promptlarda:
     "The frost is a dry granular solid that turns straight to gas —
      it never melts, never wets any surface, never drips, and there
      is no liquid, no puddle, no steam condensation anywhere."

② "no cuts" — §0.2'de çözüldü: çok çekimli 7 sahnede bu cümle
   promptta YOKTUR, yerine CUT SCHEDULE vardır. Tek çekimli 7
   sahnede aynen durur. A1 çelişkisi kapalı.

⚠️ İSİM TUZAĞI [Ders 56 + 59] — pozitif betimlemede yasaklı kökler
   Ders 59: "Model olumsuzlamayı değil İSMİ çiziyor."
   28 promptun hiçbirinde pozitif betimlemede geçmez:
     explosion · blast · fireball · shockwave · smoke · steam ·
     melt · splash · wave · flame
   Yerine ne yazılır:
     "a 60 m high advancing white wall of sublimating frost"
     "needle-fine vertical jets of gas at 200 m/s"
     "the frost turns straight to gas and the ground goes bare"
```

## 0.14 AĞIR ÇEKİM PANZEHİRİ [Ders 44]

0.28 g, "düşük-ama-yüksek yerçekimi ağır çekim okunuyor" tuzağının tam
ortası. Panzehir prompt cümlesi değil, **sahne tasarımı**:

```
① HIZ REFERANSI KADRAJIN İÇİNDE
   Rover 14.4 m/s ile kadrajı 3 saniyede geçiyor ve tekerlekleri don
   püskürtüyor. 3.2 metrelik bir cismin bu hızda kadrajı geçmesi ağır
   çekimle karıştırılamaz.

② ⭐ KESME HIZI — bu filmin ikinci ve daha güçlü panzehiri
   3 saniyelik bir segment ağır çekim olarak okunamaz; izleyicinin
   kareyi "yavaş" diye etiketleyecek vakti yok. Ders 44 bugüne kadar
   prompt cümlesiyle çözülmeye çalışıldı ve tutmadı.

③ DÜŞEN NESNE SAYISI YAZILI
   Fırlayan çakıl 0.28 g'ye uyar: 1 saniyede 1.37 m. Her promptta sayı.
```

## 0.15 ÜRETİM ÖNCESİ KONTROL — `03_PLAN_ONCESI_KONTROL_LISTESI.md`

```
ÜRETİM ÖNCESİ KONTROL — THE DAWN FRONT              tarih: 04.08.2026

A1 ✅ Yasak ↔ anlatım çelişkisi YOK — iki cephede birden denetlendi:
      · METİN: hiçbir göstergenin içeriği tarif edilmiyor. Sayaç A bir
        AYNA, sayaç B GÜNEŞ. İkisi de rakamsız.
      · ⭐ KESME: kesme İSTENEN 7 sahnenin promptunda "no cuts" cümlesi
        YOK; CUT SCHEDULE var. Kesme istenmeyen 7 sahnede cümle aynen
        duruyor. Tidal Hunt tuzağının kesme sürümü kapatıldı (§0.2).
A2 ✅ sahne sayısı: başlık 14 = blok 14 = "Scene N of 14" 14 promptta
      segment sayısı 26, kesme sayısı 12 (§0.10 tablosuyla birebir)
A3 ✅ süre: her sahnenin segment süreleri toplamı tam 10 s;
      14 × 10 = 140 s = iddia edilen 2:20
B1 ✅ doruk anı S10 segment A'nın İÇİNDE (tereddüt + kolu geri alma
      aynı 3 saniyede). İki sahne ARASINA da, iki segment ARASINA da
      düşmüyor.
      Kontrol: S10 → S11 geçişinde ekranda görülmeyen ama olması
      gereken bir şey var mı? Roverin cepheye varışı. → S11-A onu
      içeriyor: ilk karede rover şeridin ucunda.
B1b ✅ ışık takvimi §0.11'de tablo hâlinde, monotonik (−4.0° → +0.4°)
B2 ✅ bedelli seçim S10; kayıp S11-A'da (rover cepheye gidiyor) ve
      S13'te (eli boş, gemi hâlâ 200 m ötede) GÖRÜLÜYOR
C  ✅ 6 sayısal kilit + hız kilidi + kesme kilidi yazıldı — §0.12
D  ✅ risk sayımı yapıldı: 4/9, elenebilir üçü elendi — §0.9
      + kartlarda olmayan kesme riski ayrıca yazıldı — §0.2.2
E  ✅ QA SPEC bloğu yazıldı — §0.16
```

## 0.16 QA SPEC BLOĞU — üretimden sonra rubriklere BUNU kopyala

```
FILM:                 THE DAWN FRONT
FORMAT:               16:9 yatay · 2-4 dk · bilimkurgu · ince atmosfer
SCENE COUNT:          14
RUNTIME:              140 s       (14 × 10 s ile doğrulandı)
SEGMENT COUNT:        26          ⭐ sahne içi kesme — aşağıyı oku
PLANNED CUTS:         12
DIALOGUE LINES:       0           konuşmalı sahne: yok
SILENT SCENES:        14
VIRAL INTERSTITIALS:  2           S2, S5  — BUNLAR KESİLEMEZ
PROTAGONIST:          Dr. Kerem Aksoy · saha jeoloğu / sondaj mühendisi
CENTRAL CHOICE:       S10         bedelin görüldüğü sahne: S11-A ve S13
OVERVIEW SCENE:       S12         (tam olarak bir tane)
CAMERA:               26/26 segment sabit lockoff · segment içinde
                      hiçbir kamera hareketi yok

⛔ RUBRİĞE UYARI — bu film bilinçli olarak sahne içinde kesiyor.
   Sahne içi kesme bir ÜRETİM HATASI DEĞİL, tasarım kararıdır ve
   12 kesmenin 12'si aşağıda saniye olarak yazılıdır.
   Ders 1 ihlali olarak raporlanmamalıdır.
   ⚠️ ANCAK: aşağıdaki listede OLMAYAN her kesme gerçek bir ihlaldir.
     plana yazılı kesme         → tasarım
     plana yazılı OLMAYAN kesme → Ders 1 ihlali, raporlanır
     bindirme/fade/morph        → her durumda ihlal, hiçbiri planlı değil

   PLANLI KESME NOKTALARI (sahne başlangıcından itibaren, saniye):
     S0   3.0 · 7.0        S4   3.0 · 7.0       S6   5.0
     S8   4.0              S9   3.0 · 7.0       S10  3.0 · 7.0
     S11  3.0 · 7.0
   KESMESİZ SAHNELER (bunlarda TEK kesme bile ihlaldir):
     S1 · S2 · S3 · S5 · S7 · S12 · S13
```

## 0.17 FARKLILAŞMA — depodaki komşu filmlerle çakışma denetimi

```
THE HERD             en yakın komşu. Orada tehlike bir KÜTLE ve saat 40
                     dakika; kamera durgun, film durgun, 15/15 tek çekim.
                     Burada tehlike bir ÇİZGİ, saat 3.5 dakika, film
                     neredeyse gerçek zamanlı ve depodaki ilk sahne içi
                     kesme denemesi. Herd'de karakter bir şeyi ÇAĞIRIYOR,
                     burada bir şeyi YAKIYOR.

THE ETERNAL DUSK     terminatör çizgisi var · ama orada çizgi DURUYOR ve
                     film onun üzerinde yaşamayı anlatıyor. Burada çizgi
                     48 km/s ile GELİYOR. Aynı astronomi, ters dramaturji.

WHITE SILENCE        donmuş gezegen · ama orada don manzaradır ve film
                     sessizlik üzerinedir. Burada don YAKITTIR.

THE BURNING WORLD    ısı ve patlama · ama orada kaynak lav, yani sıvı ve
                     sürekli. Burada hiç sıvı yok ve olay tek seferlik
                     bir cephedir — geçince biter.

THE KALEIDA CRASH    araçlı felaket · ama orada kaza filmin başında olur
                     ve karakter yürür. Burada araç sona kadar yaşar ve
                     son sahnede bilerek feda edilir.

THE DEAD APPROACH    geri sayım · ama orada sayaç bir ekrandaydı ve
                     ekrana hiç çıkmadı (Ders 50). Burada sayaç bir AYNA
                     ve bir GÜNEŞ — ikisi de kadrajın yarısı.
```

## 0.18 📈 TUTUNDURMA HARİTASI — hangi saniyede ne tutuyor

| Saniye | Sahne | İzleyiciye ne veriyor | Kesme | Paylaşılabilir? |
|---|---|---|---|---|
| 0:00-0:10 | S0 | ⭐ **Kanca:** ufuk patlıyor → rover → ayna | **2** | ✅ 6 sn klip |
| 0:10-0:20 | S1 | **Kural:** mesafe 10 saniyede hiç değişmiyor | 0 | |
| 0:20-0:30 | S2 | ⭐ Duvarın yüzeyi: katıdan gaza, iğne jetler | 0 | ✅ 5 sn klip |
| 0:30-0:40 | S3 | ⭐ **Çehov:** kayada çentik — duvar orada yok | 0 | ✅ 4 sn klip |
| 0:40-0:50 | S4 | ⭐ **Aksiyon:** sıçrama → kayış → ayna | **2** | ✅ 6 sn klip |
| 0:50-1:00 | S5 | ⭐ Baca donu yiyor, arkada kara iz | 0 | ✅ 5 sn klip |
| 1:00-1:10 | S6 | **Tuzak:** beyaz ova → motoru kapatıyor | **1** | |
| 1:10-1:20 | S7 | ⭐ **Sessizlik:** motorsuz süzülme, 0 kesme | 0 | ⚠️ ölü bant riski |
| 1:20-1:30 | S8 | Araç duruyor → aynada başka hiçbir şey yok | **1** | |
| 1:30-1:40 | S9 | 🆕 **Deneme:** zemin tekerleğin altında çöküyor | **2** | ✅ 5 sn klip |
| 1:40-1:50 | S10 | 🎯 **Doruk:** vitesi geri alıyor → atlıyor → ters yönler | **2** | ✅ 6 sn klip |
| 1:50-2:00 | S11 | ⭐ **Duvar kırılıyor** — 60 m'den sıfıra | **2** | ✅ 5 sn klip |
| 2:00-2:10 | S12 | ⭐ **Overview:** 200 km duvarda tek çentik | 0 | ✅ kapak adayı |
| 2:10-2:20 | S13 | İki duvarın arasında ayakta. Held frame. | 0 | |

```
İLK 10 SANİYEDE  2 kesme · 1 imkânsızlık · kovalamaca çoktan başlamış
TOPLAM           10 paylaşılabilir an, en uzun boşluk 10 saniye
KESME YOĞUNLUĞU  ilk yarı 5 kesme · ikinci yarı 7 kesme → hızlanıyor
TEK CÜMLELİK ÖNCÜL — izleyicinin yoruma yazabileceği hâli:
  "Burada güneş doğduğunda yer patlıyor. Ve o adam onun önünde."

⚠️ ÖLÜ BANT RİSKİ: 1:10-1:20 (S7). Filmin tek kesmesiz, tek sessiz,
   hiçbir şeyin olmadığı sahnesi — ve bu BİLİNÇLİ. On iki kesmelik bir
   filmde kesmesiz on saniye gerilim üretir; ama ölçüm bunu "durdu"
   diye okursa suçlu S7'dir ve çözümü S7'yi 2 segmente bölmektir.
```

## 0.19 🎬 KURGU TALİMATI

> Kesme artık promptun içinde olduğu için montaj işi küçüldü — ama
> dördü hâlâ zorunlu. `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU §8` ile oku.

```
① TEK GRADE, TEK GREN  [§8]
   14 klip tek renk düzenlemesi altında toplanır ve gren TEK katman
   olarak en üste eklenir. Klip başına ayrı gren, sahne sınırlarını
   "iki farklı film" hâline getirir.
   ⚠️ Sahne İÇİNDEKİ kesmeler tek üretimden geldiği için bu sorundan
     doğal olarak muaf — bu, kesmeyi prompta koymanın tek net kazancı.

② SES KESİLMEZ  [§8, J-cut]
   Görüntü sahne içinde kesilse de ses akar: rover motoru, tekerlek
   gıcırtısı, cephenin alçak uğultusu ve nefes kesme boyunca devam eder.
   ⭐ S6'da bunun tersi bir kez kullanılır: motor sesi kesildiğinde
     kesme YOKTUR — ses kesilir, görüntü akar. Filmin en güçlü ses anı.

③ SAHNE SINIRLARI — hepsi düz sert kesme
   14 sahne arasında bindirme, fade, gizli geçiş YOKTUR. Kılavuz
   §5.2 ⑥'nın önerisi tek yerde uygulanır: S11 → S12 (Overview öncesi)
   kesmesi filmin en sert nefesidir ve ses de orada tamamen kesilir
   (§10 müziksiz sahne).

④ HİÇBİR KLİP HIZLANDIRILMAZ VE YAVAŞLATILMAZ
   Kılavuz §8'in "%2-4 hız ince ayarı" yalnız gizli geçiş içindir;
   bu filmde gizli geçiş yok. Hız rampası ağır çekim okunmasına yol
   açar (Ders 44) ve yasaktır.
```

## 0.20 ⏬ PLAN B — kesme prompt içinde tutmazsa

```
Üretimde 12 kesme yazıldığı saniyede ve yazıldığı kadrajla çıkmazsa
(bindirme/morph olarak çıkarsa veya kadraj uydurulursa), plan
DEĞİŞTİRİLMEDEN ikinci mimariye geçilir:

  Her segment AYRI üretilir → 26 klip → kurguda sert kesme
  Her segmentin lensi, mesafesi, açısı ve kadraj içeriği zaten video
  promptunun içinde tam yazılı (kural ④). Ayrı prompta dönüştürmek
  için yeni yazı gerekmiyor: segment bloğunu al, başına ortak kıyafet,
  fizik ve negatif bloklarını yapıştır.

  MALİYET  14 klip → 26 klip (+%86)
  KAZANÇ   kesme kare hassasiyetinde, kadraj kontrolü tam
  BEDEL    §0.19 ① gren/grade uyumu artık 26 klip için geçerli

⚠️ Bu karar İLK SAHNE üretildikten sonra verilir, filmin tamamı
  üretildikten sonra değil. Test sahnesi: S0 (iki kesme, üç farklı
  ölçek, biri referanssız ayna kadrajı). S0 temiz çıkarsa mimari
  tutuyor demektir.
```

---
# 📖 BÖLÜM 1 — THE BIBLES

---

## 🌍 WORLD BIBLE — GEZEGEN: SEVHAN

```
CORE CONCEPT: Sevhan is a slow-rotating world with a 96-hour day. Over
each 48-hour night a layer of solid nitrogen-carbon-dioxide frost 0.40
meters deep settles onto its dark basalt plains. When direct sunlight
first touches that frost it does not melt — it goes straight to gas in
about 0.4 seconds, and the expanding gas throws the grains and loose
gravel above it upward at 200 meters per second. The result is a wall
of white sublimating frost 60 meters high that runs from horizon to
horizon and advances with the sunrise.

CRITICAL WORLD RULE — SPEED BY LATITUDE: at the equator the terminator
crosses the ground at 157 km/h and nothing can outrun it. At 72 degrees
latitude that drops to 48 km/h — 13.3 meters per second. Everything in
this film happens at 72 degrees, and that is the only reason a human
being is still alive in it.

RULE ONE — NO FROST, NO WALL: wind-scoured bare basalt ridges collect
no frost. When the front reaches bare rock nothing happens there at
all: the wall drops from 60 meters to nothing across that width and
continues on both sides, and only the light passes.

RULE TWO — HEAT SUBLIMATES TOO: any surface above roughly 400 degrees
Celsius turns the frost under it straight to gas and leaves bare rock
behind. A rover's reactor vent grid at 600 degrees does exactly this —
which is an advantage on hard ground and a disaster on a deep frost
field, where the ground gives way under the wheel.

RULE THREE — A GAP DOES NOT LAST: a bare corridor cut through the frost
opens a gap in the advancing wall, but the wall spreads sideways into
it and closes a 40 meter gap in about 8 seconds.

GROUND: dark basalt plain under bone-white frost, flat to the horizon
with low scoured ridges of bare rock, fields of broken blocks, and long
shallow gravel washes. No water, no ice, no liquid of any kind, no
vegetation, no animal life. The frost is dry, matte and granular; it
never melts, never wets anything, never drips.

ATMOSPHERE & GRAVITY: 0.28 g. Thin carbon-dioxide/nitrogen atmosphere
at roughly 1.2% of Earth sea-level pressure. Sky is deep indigo-violet
overhead and pale orange at the horizon where the sun is coming.
Because the air is thin the gas jets stay needle-sharp and do not
billow, and thrown dust falls back and settles over about 40 seconds.

SOUND: thin and muffled. The front is a continuous low hiss felt more
than heard. Rover tyres on frost make a dry crunch. Nothing rings.
```

---

## 👤 CHARACTER BIBLE — DR. KEREM AKSOY

> ⚠️ **Ders 45:** Bu ad prompt gövdesine ASLA yazılmaz. Prompt'ta yalnız
> fiziksel tarif geçer; ad yalnız burada durur.

```
IDENTITY: 45-year-old field geologist and drilling engineer, nine years
of solo survey work. He landed on the night side to pull a single 0.9
meter core sample from a frost-buried lava tube — a four-hour job on a
48-hour night. The drill seized for six hours. That is the whole
backstory and none of it is spoken.

COMPETENCE RULE [UZAY_SENARYO_KILAVUZU §9]: He never panics and he
never improvises before he measures. His one error in this film is an
error of information, not of intelligence: he budgeted for the drill,
not for the drill failing. And when the obvious solution is available
he TRIES IT FIRST (Scene 9) — the world refuses, and only then does he
spend the vehicle.

⭐ SUIT IDENTITY LOCK [Ders 55] — yüzün okunduğu her segmentte (50mm,
75mm, 100mm) BİREBİR yazılır. 32mm geniş planlarda yüz zaten
çözünmediği için kısa biçim kullanılır; ölçü, renk ve dikiş bandı
orada da sayıyla verilir. Kısaltma dışında etiket yok, referans yok:

  A 45-year-old man, 1.78 meters tall, rangy and long-limbed. Pale
  weather-cracked skin with real visible pore texture, a long narrow
  nose broken once and set slightly crooked, deep-set grey eyes with
  heavy creases at the outer corners, thick greying eyebrows, a
  two-week salt-and-pepper beard, chapped lips. He wears a matte
  brick-red exploration suit with faded off-white seam tape along both
  forearms and across the chest, a scuffed dark grey hard-shell chest
  pack holding a flat integrated rebreather, and heavy ribbed boots.
  One fully transparent seamless visor, no tint, no coating, no mask
  or regulator beneath it, his whole face clearly readable through it.
  A narrow dark band on his right wrist shows a slow abstract amber
  pulse and nothing else. No back-mounted tank, no hose, no cable. His
  wear marks are fixed and never move: a pale grey dust smear across
  the left shoulder, a scuffed patch on the right forearm where the
  seam tape has lifted, and a film of frost dust across the top edge
  of the visor.

  This is the only suit in the film: 26 segments, 26 identical suits.

⭐ EQUIPMENT FRAME LOCK [Ders 57] — ve bu filmde İKİ KAT ÖNEMLİ:
  The suit and life-support configuration visible in the first frame
  is IDENTICAL in the last frame — AND IDENTICAL ACROSS EVERY CUT
  INSIDE THE SAME SCENE. Nothing is added, removed or reshaped at a
  cut. No tank appears. No mask appears. No hose appears. The visor
  never opens, closes, tints or clears. If any piece of equipment
  differs before and after a cut, the generation is an ERROR.
  ⚠️ Kesme, ekipman morphunun en olası anıdır — model yeni kadrajı
    yeniden icat ederken kıyafeti de yeniden icat ediyor. Bu yüzden
    her segment bloğunda kıyafet tarifi TEKRARLANIR.

HELMET STATE SCHEDULE [Ders 5, 37 · Risk Kartı 3]:
  Kapalı: 26 segmentin 26'sında. Açık: 0. Ara durum yok, geçiş yok.

HANDS: gloved, empty in every segment. He touches exactly three things
in this film and nothing else: the steering yoke, the power lever, and
the cargo strap.

MOVEMENT SIGNATURE (Motion Bible'dan her segmentte en az biri):
- direksiyonu bırakmadan başını 15 derece sola, cepheye çevirmek
- bir hareketten hemen önce kısa, kontrollü bir nefes vermek
- aynaya bakıp hemen öne dönmek
- sarsıntıda omzun seğirmesi ve elin kayışa gitmesi
- koşarken 0.28 g'de uzun, alçak, kontrollü adımlar atmak
```

---

## 🛻 ROVER BIBLE — SAHA ARACI

> Araç adı prompt gövdesine yazılmaz. Prompt'ta yalnız "the 3.2 meter
> open-frame four-wheel rover" geçer.

```
DIMENSIONS: 3.2 m long, 1.8 m wide, 1.6 m tall at the roll bar.

DESIGN LOGIC: an open, unglamorous, much-repaired field vehicle — no
cabin, no doors, no glass. A skeletal tube frame over a flat deck.

STRUCTURE (sayılabilir parçalar hâlinde, asla tek düz kütle değil):
- four open mesh wheels, each 0.9 m in diameter, on long travel arms
- an open tube roll bar over a single exposed seat
- ⭐ a 0.2 m rear-view mirror clamped to the LEFT side of the roll bar
  — bu filmin sayacı, üç segmentte birebir aynı kadrajda
- a rear cargo cradle holding one 0.9 m dark grey core cylinder,
  held by two off-white straps
- ⭐ a reactor vent grid 0.5 m across on the LEFT REAR of the deck.
  When the power lever is open the grid sits at 600 °C and reads dull
  orange with hard falloff over 1 meter and then nothing — never a
  halo. When the lever is closed it cools to grey over 40 seconds.
- matte brick-red frame with faded off-white markings, mismatched
  replacement tubes, pale frost dust packed into every joint

SCALE ANCHORS REQUIRED IN EVERY ROVER SEGMENT: at least one of — his
1.78 m figure in the seat, the 0.9 m wheel diameter, or the 0.9 m core
cylinder on the cradle.

MANDATORY QUALIFIER IN EVERY VEHICLE SEGMENT: "physically accurate
perspective, correct engineering proportions, realistic scale
relationships — the rover must never appear miniature or toy-like."

⭐ ROVER STATE SCHEDULE — hangi segmentte ne hâlde
  Baca TURUNCU (600 °C):  S0-A..C · S1 · S3 · S4-A..C · S5 · S6-A
  Baca SOĞUYOR (gri):      S6-B (40 s içinde) · S7 · S8-A · S8-B
  Baca YENİDEN TURUNCU:    S9-A..C · S10-A..C · S11-A
  Sol arka tekerlek ÇUKURDA ve gövde 8° YATIK:  S9-C'den sonra hep
  Karot silindiri KIZAKTA: 26 segmentin 26'sında — hiç indirilmiyor
  ⚠️ Bedel tam da budur: silindir hiçbir karede araçtan çıkmıyor.
```

---

## 🚀 SHIP BIBLE — İNİCİ

```
HULL: 16 meters long, three splayed legs, matte brick-red plating with
faded off-white markings, standing on a bare basalt outcrop with no
frost on it. Bu bir tercih değil, iniş kararıdır: çıplak kayaya indi.

IN FRAME: yalnız S6-A (ufukta küçük), S8-A (sağ kenarda), S12
(4 km'den bir nokta) ve S13 (200 m ötede, netsiz). Gemiye HİÇ varılmaz
ve gemiye biniş hiçbir segmentte yoktur. Film gemiye 200 metre kala
biter.

MANDATORY QUALIFIER: "physically accurate perspective, correct
engineering proportions — the ship must never appear miniature or
toy-like."
```

---

## 🗺️ RECURRING ENTITY BIBLE [Ders 58]

| Varlık | Segment | Sabit tanım (sayısal — asla değişmez) |
|---|---|---|
| **Rover** | 18 segment | 3.2 × 1.8 × 1.6 m, tuğla kırmızısı açık kafes, 4 × 0.9 m ağ tekerlek, roll bar solunda 0.2 m ayna, sol arkada 0.5 m baca ızgarası |
| **Cephe** | 22 segment | 60 m yüksek, ufuktan ufka, 13.3 m/s, iğne jetler 200 m/s, kemik beyazı, HER KAREDE SOLDAN |
| **Karot silindiri** | 10 segment | 0.9 m, koyu gri, iki kırık beyazı kayışla kızağa bağlı |
| **Ayna** | 3 segment | 0.2 m, roll barın solunda, 75mm / 2.5 m birebir aynı kadraj |
| **Çıplak kaya şeridi** | S3, S5, S11, S13 | koyu bazalt, mat, donsuz — cephenin üstünden geçtiği tek yer |
| **Gemi** | S6-A, S8-A, S12, S13 | 16 m, üç ayak, çıplak kaya çıkıntısı üstünde |

```
KURAL 1: Kartı olan varlığın geçtiği her SEGMENTTE kartın TAMAMI yazılır.
         Kesmeden sonraki segment de dâhil — orada özellikle.
KURAL 2: İki segmentten azında görünen prop üretilmez.
KURAL 3: İkinci gelişte "aynı yer" demek yetmez; sayı tekrarlanır.
```

---

## 🎥 CAMERA BIBLE

```
⭐ MOVEMENT: 26/26 SEGMENT FIXED LOCKOFF. Kamera hiçbir segmentin
   İÇİNDE hareket etmiyor. Zoom yok, pan yok, tilt yok, track yok,
   orbit yok, push-in yok. Kadraj yalnız KESMEYLE değişir.
   ⚠️ Bu bir aksiyon filmi ve kamera yine de sabit — gerekçe §0.2.1 ⑦.

LENS LOCK — segment başına tek lens, asla karıştırılmaz:
- ÇOK GENİŞ / CEPHE / OVA / OVERVIEW  → 32mm anamorphic
- GENİŞ-ORTA / ARAÇ / KOŞU            → 50mm
- ORTA-YAKIN / AYNA / EL / KARAR      → 75mm
- MAKRO (don yüzeyi, baca ızgarası)   → 100mm macro

DISTANCE LOCK: her segment kamera mesafesini metre cinsinden yazar.

⭐ AXIS LOCK: 26 segmentin 26'sında cephe kadrajın SOL tarafındadır
   veya soldan gelir; hareket SAĞA doğrudur. Kamera eksenin öbür
   yanına hiçbir segmentte geçmez. Kesmeden sonra da geçmez —
   bu, kesmeyi okunur kılan tek şeydir.

⭐ CUT GEOMETRY: ardışık iki segment ya ≥30° açı ya ≥1 ölçek kademesi
   farkı taşır (§0.2.1 ②). Her sahnenin KESME PLANI bloğunda yazılı.

⚠️ Ders 45 — KAMERA SATIRI CÜMLE OLARAK YAZILIR, künye gibi değil:
   ❌ CAMERA: 75mm, f/5.6, ISO 400, fixed at 2 meters
   ✅ Shot on a 75mm lens from a fixed position two meters away, f/5.6,
      physically accurate perspective.

CLIP LENGTH: her video prompt tam 10 saniyedir ve içinde 0, 1 veya 2
sert kesme taşır. Kesme saniyeleri MOTION ve CUT SCHEDULE bloklarında
iki kez yazılır.

CONTINUITY LOCK [Ders 1] — İKİ BİÇİMDE:
  Tek çekimli 7 sahnede : "single unbroken take, no cuts" (eski cümle)
  Çok çekimli 7 sahnede : "CUT SCHEDULE: exactly N hard cuts at [s],
                           and no others; each segment is a single
                           unbroken locked-off take" (§0.2)

MOTION SPEED [Ders 12, 44]: insan ve araç gerçek zamanlı hızda.
Ağır çekim YOK, hız rampası YOK — panzehir §0.14.
```

---

## 💡 LIGHTING BIBLE

> Faz adı her segmentte açıkça yazılır. **"cinematic lighting" ifadesi
> hiçbir prompt'ta geçmez** (Ders 33 — mumsu cilt ve bloom).
> ⚠️ Bir sahnenin üç segmenti AYNI ışık fazındadır; kesme ışığı
> değiştirmez. Kesmede renk sıcaklığı değişirse bu bir hatadır.

```
PRE-DAWN (S0-S3, güneş −4.0° ile −3.0°): the sun is still below the
horizon. The sky is deep indigo-violet overhead, pale orange low in the
east. The brightest thing in frame is the advancing white wall itself,
lit from behind and below by a sun that has not risen — a bright edge
with the plain in front of it nearly dark. Shadows are weak and
soft-edged, which is CORRECT for 1.2% pressure and is not an error and
not bloom [Ders 41].

FIRST RIM (S4-S6, güneş −2.4° ile −1.8°): the wall now carries a hard
orange rim along its crest while its face stays cold white. The plain
ahead of the rover is still in night; the frost reads pale blue-grey.

CLOSE LIGHT (S7-S10, güneş −1.3° ile −0.35°): the wall is close enough
to be the key light. It throws a cold white key from frame left across
the rover, the seat and one side of his face, with deep shadow on the
right side. The vent grid at 600 °C adds a dull orange edge low on the
left of frame with hard falloff over 1 meter and then nothing.

BREAK (S11, güneş −0.15°): where the wall collapses, a clean shaft of
direct orange sunlight comes through the 40 meter notch and lies along
the bare corridor — the first direct sunlight in the film.

FULL SUN (S12-S13, güneş +0.1° ile +0.4°): direct hard key across the
whole plain. Long defined shadows. The two walls on either side stay
cold white and are now backlit.

ANTI-BLOOM DIRECTIVE [Ders 3, 29]: 0% bloom on every light source.
High contrast between lit and unlit. Skin keeps visible pore texture
and real shadow under every condition. Yasak kelimeler hiçbir prompt'ta
geçmez: glowing, ethereal, radiant, shimmering, cinematic lighting.
```

---

## 🏃 MOTION BIBLE (Micro-Behavior Catalog)

```
Her segment bu katalogdan en az birini içerir:
- direksiyonu bırakmadan başını 15 derece sola çevirmek
- bir hareketten hemen önce kısa ve kontrollü bir nefes vermek
- aynaya bakıp hemen öne dönmek
- sarsıntıda omzun seğirmesi ve elin kayışa gitmesi
- 0.28 g'de uzun, alçak, kontrollü adımlarla koşmak
- eldivenli elin bir kola gitmeden önce bir an durması
- inişte dizlerin yükü emmesi ve gövdenin öne eğilmesi

⚠️ Bu katalogdaki hiçbir jest bir filmde ikiden fazla kullanılmaz
   (jest tekrarı kuralı — §0.8 denetimi). Aynaya bakma ve güç koluna
   uzanma üçer kez geçer; gerekçeleri §0.8'de yazılı.
```

---

## ⚙️ PHYSICS BIBLE

```
GRAVITY: 0.28 g (2.75 m/s²). Serbest düşüş — 1 saniyede 1.37 m,
2 saniyede 5.5 m, 3 saniyede 12.4 m. Fırlayan çakıl bu eğriyi izler.
Bu bir ağır çekim değildir; insan ve araç normal hızdadır.

SUBLIMATION PHYSICS — filmin çekirdeği:
  Frost layer          0.40 m solid nitrogen-CO2, dry, matte, granular
  Trigger              direct sunlight OR any surface above 400 °C
  Transition           solid straight to gas in about 0.4 seconds
                       ⛔ NEVER liquid. No melting, no wetting, no
                          dripping, no puddle, no steam condensation.
  Jet velocity         200 m/s, needle-fine and vertical, staying sharp
                       because the atmosphere is only 1.2% pressure
  Wall height          60 m, horizon to horizon
  Wall speed           13.3 m/s, constant, never accelerating
  Thrown gravel        follows 0.28 g exactly: 1.37 m in the first second
  Dust settling        thrown dust falls back and settles over 40 s

FRONT SPEED LOCK: 13.3 m/s in every single segment. The wall never
speeds up, never slows down, never surges and never lunges. It is a
sunrise.

ROVER PHYSICS:
  flat ground, power on     14.4 m/s
  broken ground, power on    8.3 m/s
  coasting, power off        deceleration 0.15 m/s² → 690 m from 14.4 m/s
  reverse, power on          6 m/s
  wheels                     4 × 0.9 m, always rotating in contact with
                             the ground, never sliding, never floating
  ⭐ deep frost + hot vent   the ground turns to gas under the wheel and
                             the wheel drops 0.4 m into loose gravel;
                             the vehicle stops within 30 m and settles
                             8 degrees over to the left (Scene 9)

PARTICLE GRAVITY LOCK [Ders 10, 30, 39]: All thrown frost grains and
gravel obey 0.28 g with continuous physical momentum. They rise, arc
over and fall back. Nothing hovers, nothing freezes in mid-air, nothing
flows like liquid. Ders 39'un yasak kelimesi 28 promptun hiçbirinde
geçmez; yasak, tetikleyici ismi hiç yazmadan kuruldu [Ders 39 + 59].

THIN ATMOSPHERE RULES [KILAVUZ_REHBERI §3.2]:
- Toz yavaş ama KESİN çöker ve yüzeye oturur (40 saniye).
- Gölge zayıf ve yumuşak kenarlı — MEŞRU, hata değil.
- Dolgu ışığı VAR ve motivelidir.
- Rüzgâr hiçbir şeyi deviremez.
- Gaz jetleri KESKİN ve dikey; kabarmaz, kıvrılmaz, mantar bulutu yapmaz.

CONTACT INTEGRITY [Ders 11, 43]: eldivenli el hiçbir yüzeye ERİMEZ.
Güç kolunu kavradığında parmaklarla metal arasında net sınır kalır.

COLLISION INTEGRITY [Ders 17]: hiçbir nesne bir diğerinin içinden
geçmez. Tekerlekler zemine basar; yalnız S9'da çukura girer ve orada
kalır. Düşen çakıl yere değer ve orada kalır.

ENVIRONMENT STABILITY [Ders 6]: zemin, kaya blokları ve gemi TAMAMEN
statiktir. Yalnız cephe ilerler ve yalnız yazılı hızda.

FACE LOCK [Ders 16] · SUIT CONTINUITY [Ders 8] · VISOR PERSISTENCE
[Ders 5]: Character Bible'daki blok her segmentte tekrarlanır.
```

---

## 🚫 NEGATIVE BIBLE — ⭐ İKİ ÇEKİRDEK

> ⚠️ **Bu filmde negatif çekirdek İKİ sürümlüdür ve hangisinin nereye
> gideceği §0.10 tablosunda yazılıdır. Karıştırmak A1 hatasıdır.**

### ÇEKİRDEK A — TEK ÇEKİMLİ SAHNELER (S1 · S2 · S3 · S5 · S7 · S12 · S13)

```
=== NEGATIVE CORE A — 14 prompt'ta birebir bu metin var ===

Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits, letters or symbols anywhere — no subtitles, no title
card, no credits, no watermark, no HUD, no lens data. 0% bloom, no
glow filter, no soft focus, no haze, no lens flare. Photorealistic skin
with pores and fatigue — no airbrushing, no waxy or plastic texture, no
face morphing, identical bone structure throughout. Suit and equipment
identical from first frame to last; dirt and wear stay fixed. THE FROST
IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — it never melts,
never wets any surface, never drips; there is no liquid, no puddle, no
steam condensation and no wet look anywhere. All thrown grains and
gravel obey 0.28 g with continuous momentum — never hovering, never
frozen in mid-air, never flowing like liquid. The advancing wall moves
at one constant speed and never surges, never lunges and never
accelerates. Hands keep a clear boundary at every contact — no merging,
no phasing, no extra fingers, rigid-body collision. Terrain static — no
melting terrain, no warping. No animal, no creature, no vegetation. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
===
```

### ÇEKİRDEK B — ÇOK ÇEKİMLİ SAHNELER (S0 · S4 · S6 · S8 · S9 · S10 · S11)

```
=== NEGATIVE CORE B — 14 prompt'ta birebir bu metin var ===
⭐ FARK: "single unbroken take / no cuts" cümlesi YOKTUR. Yerine CUT
SCHEDULE gelir ve o, her promptta sahnenin kendi kesme saniyeleriyle
yazılır. Geri kalan her cümle Çekirdek A ile aynıdır.

Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits, letters or symbols
anywhere — no subtitles, no title card, no credits, no watermark, no
HUD, no lens data. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Photorealistic skin with pores and fatigue — no
airbrushing, no waxy or plastic texture, no face morphing, identical
bone structure throughout. Suit and equipment identical before and
after every cut; dirt and wear stay fixed. THE FROST IS A DRY GRANULAR
SOLID THAT TURNS STRAIGHT TO GAS — it never melts, never wets any
surface, never drips; there is no liquid, no puddle, no steam
condensation and no wet look anywhere. All thrown grains and gravel
obey 0.28 g with continuous momentum — never hovering, never frozen in
mid-air, never flowing like liquid. The advancing wall moves at one
constant speed and never surges, never lunges and never accelerates.
Hands keep a clear boundary at every contact — no merging, no phasing,
no extra fingers, rigid-body collision. Terrain static — no melting
terrain, no warping. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain.
===
```

```
FİLME ÖZEL EK YASAKLAR (uygun segmentlerde vurgulanır)
- No fire, no flame, no burning, no ember, no ash — nothing is on
  fire in this film; the frost turns to gas and the gas is cold.
- No mushroom cloud, no billowing cloud, no rolling smoke bank — the
  jets are needle-fine and vertical in 1.2% pressure.
- No rain, no snowfall, no falling flakes from the sky — everything
  that is in the air was thrown up from the ground.
- No slow motion, no speed ramp: the rover crosses the frame at full
  real-world speed and no shot changes speed at a cut.
- Not miniature, not toy-like (rover, gemi ve cephe kadrajları).
- No second vehicle, no other tracks in the frost except the rover's
  own two wheel lines.
```

---
# 🎬 BÖLÜM 2 — SHOT-BY-SHOT PROMPTS (14 SAHNE × 10 s)

> **Kopyalama kuralı:** yalnız kod bloğunun içini kopyala. Türkçe başlık
> ekleme, iki promptu birleştirme (politika reddi alındı, doğrulandı).
>
> **Her sahne tek bir 10 saniyelik üretimdir.** Kesme varsa promptun
> içindedir: MOTION bloğunda segment segment yazılı, CUT SCHEDULE
> bloğunda saniyesiyle kilitli.
>
> **İmaj promptu yalnız A segmentinin ilk karesidir.** B ve C'nin
> referans imajı yoktur; o yüzden video promptunda her segmentin
> SETUP ve FRAME satırları tam yazılır (§0.2.1 kural ④).
>
> **İnsansız sahneler (S2, S11-A/B kısmen, S12):** negatif çekirdeğin
> insan cümlesi "No human in frame" biçiminde yazılır.

---

## 🎬 SAHNE 0 — HOOK: UFUK PATLIYOR

_Ufuk turuncuya dönüyor ve o çizgi boyunca zemin gaza dönüşüyor. Rover kadraja soldan giriyor. Aynada duvar._

```
⚙️ KESME PLANI — 3 segment · 2 kesme · 3+4+3 = 10.0 s
  A  0.0-3.0 s   32mm · 40 m · çok geniş, zemin seviyesi · İNSANSIZ
  ✂  3.0 s       ölçek: çok geniş → orta-geniş   (+40° açı farkı)
  B  3.0-7.0 s   50mm · 12 m · yandan, göğüs hizası
  ✂  7.0 s       ölçek: orta-geniş → yakın       (+90° açı farkı)
  C  7.0-10.0 s  75mm · 2.5 m · ayna · ⭐ SAYAÇ KADRAJI 1/3
  EKSEN   üçünde de cephe SOLDA, hareket SAĞA
  KES ANI ikisi de hareket üzerinde: duvarın yükselişi ve tekerlek dönüşü
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 0 of 14, opening frame. Across a dark frost plain the horizon
line is turning orange, and along that line the ground itself is
turning to gas and rising as a white wall.

ENVIRONMENT:
A flat dark basalt plain under a continuous layer of bone-white frost
0.40 meters deep, dry, matte and granular, running to the horizon on a
slow-rotating world at 0.28 g. Thin carbon-dioxide atmosphere at 1.2%
of Earth sea-level pressure. The sky is deep indigo-violet overhead and
pale orange low on the LEFT horizon. Low scoured ridges of bare dark
basalt break the frost here and there. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
The advancing front, filling the left two thirds of frame: a wall of
sublimating frost 60 meters high running from horizon to horizon,
bone-white, its face made of needle-fine vertical gas jets rising at
200 meters per second and carrying thrown grains and gravel with them.
The wall has a hard bright crest and a dark base where it meets the
plain. In front of it the untouched frost plain is still in night. Two
thin wheel lines cross the frost from left to right in the lower third
of frame.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 40 meters away,
f/5.6, very low at ground level so the frost surface fills the bottom
of frame and the 60-meter wall stands against the sky, physically
accurate perspective.

LIGHTING:
Pre-Dawn phase, sun 4.0 degrees BELOW the horizon. The brightest thing
in frame is the wall itself, lit from behind and below by a sun that
has not risen — a hard bright crest against a dark plain. Shadows are
weak and soft-edged, correct for 1.2% pressure. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The frost is a dry granular solid
that turns straight to gas in about 0.4 seconds — it never melts, never
wets anything, never drips. Gas jets stay needle-fine and vertical
because the air is thin. Thrown gravel obeys 0.28 g exactly: 1.37
meters in the first second, arcing over and falling back. The wall
advances at a constant 13.3 meters per second.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no crew, no
clone, no figure of any kind. No text, digits or symbols anywhere — no
subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. THE FROST IS A DRY
GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — it never melts, never wets
any surface, never drips; there is no liquid, no puddle, no steam
condensation and no wet look anywhere. All thrown grains and gravel
obey 0.28 g with continuous momentum — never hovering, never frozen in
mid-air, never flowing like liquid. The advancing wall moves at one
constant speed and never surges, never lunges and never accelerates.
Terrain static — no melting terrain, no warping. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain. Emphasis: nothing is on fire — no flame, no
ember, no ash, no smoke; the jets are needle-fine and vertical, never a
mushroom cloud and never a rolling smoke bank; nothing falls from the
sky, everything in the air was thrown up from the ground; no human
anywhere.
```

### 🎥 VIDEO PROMPT — 10 saniye, 2 kesme içinde

```
MOTION — 10 seconds, three fixed setups joined by two hard cuts:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 40 meters away, very low at
ground level.
FRAME: a bone-white frost plain 0.40 m deep over dark basalt; on the
left, an advancing wall of sublimating frost 60 m high running horizon
to horizon, its face made of needle-fine vertical gas jets at 200 m/s;
deep indigo-violet sky, pale orange at the left horizon. No human.
0.0s — The wall advances at a constant 13.3 m/s, jets rising along its
whole face; thrown gravel arcs up and falls back under 0.28 g.
2.8s — The wall is closer and taller in frame; the untouched frost in
the foreground has not moved.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 7.0 s
SETUP: 50mm lens, fixed lockoff 12 meters away, side-on at chest height.
No camera movement inside this segment.
FRAME: the same plain and the 60 m wall in the left third. Crossing left
to right at 14.4 m/s, the 3.2 m open-frame four-wheel rover: matte
brick-red tube frame, four 0.9 m mesh wheels, a 0.2 m mirror on the LEFT
of the roll bar, a 0.9 m core cylinder under two straps, a 0.5 m vent
grid at 600 °C dull orange on the LEFT REAR; in the seat the 45-year-old
man in a matte brick-red suit with off-white seam tape, a dark grey
chest pack and a fully transparent visor, both hands on the yoke.
3.0s — The rover is mid-frame at full speed, all four wheels throwing
frost sideways; the grains arc and settle within a meter.
5.0s — He turns his head fifteen degrees left toward the wall and
straight back to the front.
6.8s — The core cylinder jolts once against its straps.
✂ HARD CUT AT 7.0s

▸ SEGMENT C — 7.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff 2.5 meters away, level with the mirror.
No camera movement inside this segment.
FRAME: the 0.2 m mirror on the LEFT of the roll bar, dead centre and
sharply focused, its edge packed with frost dust. Inside it: the plain
running back and ONE thin white line on the reflected horizon filling
about ONE EIGHTH of the mirror's height, nothing else. At the right
edge, closer and soft, his shoulder and jaw — two-week salt-and-pepper
beard, fully transparent visor, pale grey dust smear on the left
shoulder.
7.0s — The reflected ground slides steadily through the mirror; the
white line holds its size.
8.5s — His eyes flick to the mirror without his head turning.
10.0s — He looks forward again. The line has not changed.

CUT SCHEDULE:
Exactly two hard cuts, at 3.0s and 7.0s, and no others. Each segment is one unbroken locked-off take with no camera movement inside it. No dissolve, no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle and lighting identical before and after every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Wall constant 13.3 m/s, rover
constant 14.4 m/s — full normal real-world speed, not slow motion.
Frost goes straight from solid to gas in 0.4 seconds with no liquid
stage. Wheels rotate in ground contact and never slide or float.
Thrown grains obey 0.28 g and settle within a meter.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: no dissolve and no morph at either cut — both are
instant hard cuts; no extra cut anywhere; no slow motion;
```

---

## 🎬 SAHNE 1 — AYNI HIZ: KURAL

_Rover soldan sağa kadrajı geçiyor, duvar arkasında. On saniyede aralarındaki mesafe hiç değişmiyor. Kural bu._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  Nefes sahnesi. Kesme YOK — çünkü anlatılan şey DEĞİŞMEMEKTİR.
  On saniye boyunca hiçbir şeyin değişmemesi, filmin kuralıdır.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 1 of 14. A wide side view: the rover on the left third of frame,
the 60-meter wall behind it, both moving right at almost the same
speed.

ENVIRONMENT:
A flat dark basalt plain under bone-white frost 0.40 meters deep, dry,
matte and granular, running to the horizon at 0.28 g under a thin
carbon-dioxide atmosphere at 1.2% of Earth sea-level pressure. Sky deep
indigo-violet overhead, pale orange low on the LEFT horizon. Low
scoured ridges of bare dark basalt break the frost in the middle
distance. Behind the rover and filling the left half of frame, an
advancing wall of sublimating frost 60 meters high running from horizon
to horizon, bone-white, its face made of needle-fine vertical gas jets
rising at 200 meters per second. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
A 3.2 meter long, 1.8 meter wide open-frame four-wheel rover: skeletal
matte brick-red tube frame over a flat deck, faded off-white markings,
mismatched replacement tubes, four open mesh wheels each 0.9 meters in
diameter, an open tube roll bar over a single exposed seat, a 0.2 meter
rear-view mirror on the LEFT of the roll bar, a rear cargo cradle
holding one 0.9 meter dark grey core cylinder under two off-white
straps, and a 0.5 meter reactor vent grid on the LEFT REAR of the deck
at 600 degrees Celsius reading dull orange with hard falloff over one
meter. In the seat, small at this distance, a 1.78 meter man in a matte
brick-red exploration suit with faded off-white seam tape and one fully
transparent seamless visor, both hands on the steering yoke. Two thin
wheel lines run back from the rover across the frost toward the wall.
Physically accurate perspective, correct engineering proportions,
realistic scale relationships — the rover must never appear miniature
or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 60 meters away,
f/8, side-on at chest height so the rover, the plain between it and the
wall, and the full 60-meter height of the wall are all in frame,
physically accurate perspective.

LIGHTING:
Pre-Dawn phase, sun 3.6 degrees BELOW the horizon. The wall is the
brightest thing in frame and lights the plain in front of it with a
cold white wash from frame left. The rover carries a hard cold rim on
its left side and deep shadow on its right. Shadows weak and
soft-edged, correct for 1.2% pressure. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The rover holds 14.4 m/s and the
wall holds 13.3 m/s, so over ten seconds the gap between them changes
by only about eleven meters out of 880 — visually it does not change at
all. Wheels rotate in ground contact. Frost is a dry granular solid
that turns straight to gas with no liquid stage.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no steam condensation, no wet look
anywhere. All thrown grains and gravel obey 0.28 g with continuous
momentum — never hovering, never frozen in mid-air, never flowing like
liquid. The advancing wall moves at one constant speed and never
surges, never lunges, never accelerates. Terrain static — no melting
terrain, no warping. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain. Emphasis:
no fire, no flame, no smoke, no ash, no mushroom cloud; the jets are
needle-fine and vertical; the gap between rover and wall must look
UNCHANGED across the whole shot; exactly one human; not miniature.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 32mm anamorphic lens,
fixed lockoff at 60 meters, side-on at chest height):
0s — The rover holds the left third of frame at 14.4 m/s, wheels
throwing frost. Behind it the 60-meter wall advances at 13.3 m/s.
3s — Both move steadily right. The gap between them does not visibly
change.
5s — The rover crosses a low bare basalt ridge; its wheels stop
throwing frost for a moment.
7s — Back onto frost. The wheels throw again. The gap is still the
same.
10s — Nothing has changed except position. The wall is exactly as far
behind as it was.
No cuts.

EQUIPMENT LOCK: rover and suit unchanged throughout — same four wheels,
same left-side mirror, same core cylinder under two straps, same dull
orange vent grid, first frame identical to last.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Rover 14.4 m/s, wall 13.3 m/s, both
constant for the whole shot. Wheels rotate in ground contact and never
slide. Frost goes straight from solid to gas with no liquid stage.
Thrown grains obey 0.28 g and fall back within a meter.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no wet look anywhere. All thrown grains
obey 0.28 g — never hovering, never frozen in mid-air, never flowing
like liquid. The wall moves at one constant speed and never surges,
never lunges, never accelerates. Terrain static. No animal, no
creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: no slow motion — full real-world speed; the wall
must NOT gain on the rover during this shot; no fire, no smoke, no
mushroom cloud; exactly one human; not miniature.
```

---

## 🎬 SAHNE 2 — ⭐ VİRAL ARA SAHNE: DUVARIN YÜZEYİ

_Katı, sıvıya uğramadan gaza dönüşüyor. İğne gibi, dimdik, saniyede iki yüz metre._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  Saf görsel. KESİLEMEZ (§0.10 viral ara sahne).
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 2 of 14. Macro on the base of the advancing wall: solid frost
turning straight into gas, needle-fine jets going vertically up.

ENVIRONMENT:
The lowest three meters of the advancing front, six meters from camera.
Dark basalt bedrock under a layer of bone-white frost exactly 0.40
meters deep, dry, matte and granular, with a visible cut edge where the
front is eating into it. Behind, the base of the wall rises out of the
top of frame. Thin carbon-dioxide atmosphere at 1.2% of Earth sea-level
pressure, 0.28 g. No water, no ice, no liquid, no vegetation, no animal
life, no human being anywhere.

SUBJECT:
The sublimation edge itself, filling the frame: a moving line where the
0.40 meter frost layer ends and bare dark basalt begins. At that line
the frost does not melt and does not slump — it goes straight to gas,
and hundreds of needle-fine vertical jets rise from it at 200 meters
per second, so thin and so straight that they read as white filaments
rather than as cloud. Loose grains and small gravel are carried up with
them, arc over and fall back. The bare basalt left behind is dark, dry,
matte and completely clean — no residue, no wet patch, no staining. The
edge advances steadily from left to right.

CAMERA:
Shot on a 100mm macro lens from a fixed position 6 meters away, f/4,
low and level with the frost surface so the cut edge runs across the
frame and the jets rise out of the top, physically accurate
perspective.

LIGHTING:
Pre-Dawn phase, sun 3.4 degrees BELOW the horizon. Hard cold white key
from frame left off the body of the wall above, raking across the frost
grains so every grain keeps sharp texture. The bare basalt behind the
edge falls into deep shadow. Shadows weak-edged but deep. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The frost is a dry granular solid
that turns straight to gas in about 0.4 seconds with no liquid stage —
it never melts, never wets the rock, never drips. The gas jets stay
needle-fine and vertical because the atmosphere is only 1.2% pressure;
they do not billow and do not curl. Carried grains obey 0.28 g exactly:
1.37 meters in the first second, arcing over and falling back onto the
bare rock. The edge advances at a constant 13.3 meters per second.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no crew, no
clone, no hand, no figure of any kind. No text, digits or symbols
anywhere — no subtitles, no title card, no watermark, no HUD. 0% bloom,
no glow filter, no soft focus, no haze, no lens flare. THE FROST IS A
DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — it never melts, never
wets any surface, never drips; there is no liquid, no puddle, no steam
condensation and no wet look anywhere. All carried grains and gravel
obey 0.28 g with continuous momentum — never hovering, never frozen in
mid-air, never flowing like liquid. Terrain static — no melting
terrain, no warping. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain. Emphasis:
the jets are needle-fine, vertical and separate — never a billowing
cloud, never rolling smoke, never a mushroom shape, never fog; nothing
is on fire, no flame, no ember, no ash; the rock left behind is
bone-dry and clean; no human, no hand anywhere.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 100mm macro lens, fixed
lockoff at 6 meters, low and level with the frost surface):
0s — The cut edge sits in the left third of frame. Needle-fine vertical
jets rise from it continuously.
3s — The edge advances steadily right at 13.3 m/s, eating into the 0.40
meter frost layer and leaving clean bare dark basalt behind it.
5s — A fist-sized piece of gravel is carried up by a jet, rises about
1.4 meters in the first second, arcs over and falls back onto the bare
rock, where it stays.
8s — The edge has crossed most of the frame; two thirds of what was
frost is now bare rock.
10s — The jets continue, unbroken, top to bottom of frame.
No cuts.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Solid straight to gas in 0.4 seconds
with no liquid stage. Jets stay needle-fine and vertical, never
billowing. Carried gravel obeys 0.28 g: 1.37 m in the first second,
arcing over and falling back. The edge advances at a constant 13.3 m/s.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no hand, no
figure of any kind. No text, digits or symbols anywhere — no subtitles,
no title card, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no haze, no lens flare. THE FROST IS A DRY GRANULAR SOLID THAT
TURNS STRAIGHT TO GAS — it never melts, never wets any surface, never
drips; no liquid, no puddle, no steam condensation, no wet look
anywhere. All carried grains obey 0.28 g — never hovering, never frozen
in mid-air, never flowing like liquid. Terrain static. No animal, no
creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: needle-fine vertical jets only — no billowing, no
rolling smoke, no mushroom cloud, no fog bank; no fire, no flame, no
ember; the edge advances smoothly and never surges toward camera; the
bare rock behind is dry and clean; no human anywhere.
```

---

## 🎬 SAHNE 3 — ⭐ ÇEHOV 1: KAYADAKİ ÇENTİK

_Uzakta duvar çıplak bir kaya sırtına varıyor. Ve orada yükselmiyor. Kırk metrelik bir çentik açılıp iki yanda devam ediyor._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  Kurulum sahnesi. Kesme YOK — izleyicinin kuralı fark etmesi için
  aynı kadrajda hem "duvar var" hem "duvar yok" aynı anda durmalı.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 3 of 14. In the distance the wall reaches a bare basalt ridge,
and across that width it simply is not there: a 40-meter notch, with
the 60-meter wall continuing on both sides.

ENVIRONMENT:
A dark basalt plain under bone-white frost 0.40 meters deep, dry, matte
and granular, at 0.28 g under a thin carbon-dioxide atmosphere at 1.2%
of Earth sea-level pressure. Sky deep indigo-violet overhead, pale
orange low on the LEFT horizon. Running across the middle distance, a
wind-scoured ridge of bare dark basalt about 40 meters wide with no
frost on it at all. On the left, the advancing wall of sublimating
frost 60 meters high, bone-white, its face made of needle-fine vertical
gas jets rising at 200 meters per second. Where the wall meets the bare
ridge it drops to nothing: a clean 40-meter gap in a wall that runs
from horizon to horizon. No water, no ice, no liquid, no vegetation, no
animal life.

SUBJECT:
The notch itself, at frame centre: on either side of it the wall stands
its full 60 meters, and between them there is only open air and the
pale orange sky beyond. The bare ridge under the notch is dark, dry and
clean. In the lower right foreground, small, the 3.2 meter long, 1.8
meter wide open-frame four-wheel rover moving away from camera: matte
brick-red tube frame, four open mesh wheels each 0.9 meters in
diameter, an open roll bar with a 0.2 meter mirror on its LEFT, a rear
cargo cradle with one 0.9 meter dark grey core cylinder under two
off-white straps, a 0.5 meter vent grid on the LEFT REAR at 600 degrees
Celsius reading dull orange with hard falloff over one meter, and a
1.78 meter man in a matte brick-red exploration suit with faded
off-white seam tape and one fully transparent seamless visor in the
seat. Physically accurate perspective, correct engineering proportions,
realistic scale relationships — the rover must never appear miniature
or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 25 meters behind
the rover, f/8, at chest height looking along the plain so the rover is
small in the lower right and the notch in the wall sits at frame
centre, physically accurate perspective.

LIGHTING:
Pre-Dawn phase, sun 3.0 degrees BELOW the horizon. The wall is the
brightest thing in frame; through the 40-meter notch a band of pale
orange horizon sky is visible, and it is the only warm colour in the
image. The plain in front is nearly dark. Shadows weak and soft-edged.
0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Where there is no frost there is
nothing to turn to gas, so the wall has no height at all across the
bare ridge — it is not thinner there, it is absent. The wall advances
at a constant 13.3 m/s and the notch travels with it. Frost is a dry
granular solid that turns straight to gas with no liquid stage.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no steam condensation, no wet look
anywhere. All thrown grains obey 0.28 g with continuous momentum —
never hovering, never frozen in mid-air, never flowing like liquid. The
advancing wall moves at one constant speed and never surges, never
lunges, never accelerates. Terrain static — no melting terrain, no
warping. No animal, no creature, no vegetation. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain. Emphasis: the notch
is EMPTY AIR — not a thinner section, not a lower section, not a gap
filled with mist; the wall's two edges at the notch are clean and
vertical; no fire, no flame, no smoke, no mushroom cloud; exactly one
human; not miniature.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 32mm anamorphic lens,
fixed lockoff at 25 meters, chest height):
0s — The wall runs unbroken across the background at its full 60
meters, advancing at 13.3 m/s. The bare basalt ridge lies ahead of it.
3s — The wall's leading edge reaches the bare ridge. Across those 40
meters the wall simply stops existing — the jets end and there is open
sky between two vertical white edges.
6s — The notch travels forward with the wall, holding its width, the
pale orange horizon visible through it.
8s — In the lower right the rover keeps moving away from camera at 14.4
m/s; the man's head turns fifteen degrees to the left, toward the
notch, and back to the front.
10s — The notch is still open, the wall still 60 meters on both sides.
No cuts.

EQUIPMENT LOCK: rover and suit unchanged throughout — same four wheels,
same left-side mirror, same core cylinder under two straps, first frame
identical to last.

PHYSICS:
0.28 g, thin air at 1.2% pressure. No frost means nothing to sublimate,
so the wall has zero height over the bare ridge. Wall speed constant at
13.3 m/s. Rover constant at 14.4 m/s. Frost goes straight to gas with
no liquid stage.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no wet look anywhere. All thrown grains
obey 0.28 g — never hovering, never frozen in mid-air, never flowing
like liquid. The wall moves at one constant speed and never surges.
Terrain static. No animal, no creature. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: the notch must read as
EMPTY AIR with the sky visible through it — not mist, not a thinner
wall, not a dip; the notch keeps its width for the whole shot; no fire,
no smoke; exactly one human.
```

---
## 🎬 SAHNE 4 — AKSİYON: KIRIK ARAZİ

_Kaya blokları. Rover sıçrıyor, karot kayışında zıplıyor, aynada duvar iki katına çıkıyor._

```
⚙️ KESME PLANI — 3 segment · 2 kesme · 3+4+3 = 10.0 s
  A  0.0-3.0 s   32mm · 30 m · geniş, alçak yandan
  ✂  3.0 s       ölçek: geniş → orta-yakın      (+70° açı farkı)
  B  3.0-7.0 s   50mm · 5 m · araç üstünde, yüksek üç-çeyrek
  ✂  7.0 s       ölçek: orta-yakın → yakın      (+60° açı farkı)
  C  7.0-10.0 s  75mm · 2.5 m · ayna · ⭐ SAYAÇ KADRAJI 2/3
  EKSEN   üçünde de cephe SOLDA, hareket SAĞA
  KES ANI ikisi de hareket üzerinde: sıçramanın iniş anı ve elin kayışa gidişi
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 4 of 14, opening frame. The rover crosses a field of broken
basalt blocks at speed, airborne off a block.

ENVIRONMENT:
A field of broken dark basalt blocks between 0.3 and 1.5 meters across,
half buried in bone-white frost 0.40 meters deep, dry, matte and
granular, at 0.28 g under a thin carbon-dioxide atmosphere at 1.2% of
Earth sea-level pressure. Sky deep indigo-violet overhead, pale orange
low on the LEFT horizon. Filling the left third and the background, an
advancing wall of sublimating frost 60 meters high, bone-white, its
face made of needle-fine vertical gas jets rising at 200 meters per
second. No water, no ice, no liquid, no vegetation, no animal life.

SUBJECT:
The 3.2 meter long, 1.8 meter wide open-frame four-wheel rover crossing
the block field left to right at 8.3 meters per second: skeletal matte
brick-red tube frame over a flat deck, faded off-white markings,
mismatched replacement tubes, four open mesh wheels each 0.9 meters in
diameter on long travel arms, an open tube roll bar with a 0.2 meter
mirror on its LEFT, a rear cargo cradle holding one 0.9 meter dark grey
core cylinder under two off-white straps, a 0.5 meter reactor vent grid
on the LEFT REAR at 600 degrees Celsius reading dull orange with hard
falloff over one meter. Its front wheels have just come off a block and
the whole 3.2 meter frame is airborne by about 1.2 meters, nose
slightly up. In the seat, a 1.78 meter man in a matte brick-red
exploration suit with faded off-white seam tape along both forearms and
across the chest, a scuffed dark grey hard-shell chest pack and one
fully transparent seamless visor, both hands locked on the steering
yoke, his body braced. Physically accurate perspective, correct
engineering proportions, realistic scale relationships — the rover must
never appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 30 meters away,
f/5.6, low and side-on so the block field runs across the bottom of
frame and the wall stands behind, physically accurate perspective.

LIGHTING:
First Rim phase, sun 2.4 degrees BELOW the horizon. The wall now
carries a hard orange rim along its crest while its face stays cold
white. Cold white key from frame left across the rover; deep shadow on
its right side. Shadows weak and soft-edged. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The airborne rover follows a 0.28 g
ballistic arc: from 1.2 meters it takes about 0.93 seconds to come
down. It is moving at 8.3 m/s at full normal real-world speed, not slow
motion. Wheels keep rotating while airborne and meet the ground without
sliding. Thrown frost grains obey 0.28 g and fall back. The wall
advances at a constant 13.3 m/s.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no wet look anywhere. All thrown grains and
gravel obey 0.28 g with continuous momentum — never hovering, never
frozen in mid-air, never flowing like liquid. The advancing wall moves
at one constant speed and never surges. Hands keep a clear boundary at
every contact — no merging, no phasing, no extra fingers. Terrain
static — no melting terrain, no warping. No animal, no creature. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
Emphasis: no slow motion — the jump reads at full real-world speed on a
0.28 g arc, never floating and never hanging; the rover does not roll,
does not flip and does not break apart; no fire, no smoke, no sparks;
exactly one human; not miniature.
```

### 🎥 VIDEO PROMPT — 10 saniye, 2 kesme içinde

```
MOTION — 10 seconds, three fixed setups joined by two hard cuts:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 30 meters away, low and side-
on.
FRAME: a field of broken dark basalt blocks 0.3-1.5 m across under 0.40
m bone-white frost; on the left and behind, the 60 m wall with needle-
fine vertical jets and a hard orange rim. Crossing left to right, the
3.2 m open-frame four-wheel rover: matte brick-red tube frame, four 0.9
m mesh wheels on long travel arms, a 0.2 m mirror on the LEFT of the
roll bar, a 0.9 m core cylinder under two straps, a 0.5 m vent grid at
600 °C dull orange; in the seat the 45-year-old man in a matte brick-red
suit with off-white seam tape and a fully transparent visor.
0.0s — The rover is airborne about 1.2 meters over the blocks, nose
slightly up, moving right at 8.3 m/s, wheels still turning.
0.9s — All four wheels meet the ground together; the travel arms
compress and the frame drops about 0.3 meters and comes back up.
2.8s — Frost sprays from under the wheels, arcs and settles.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 7.0 s
SETUP: 50mm lens, fixed lockoff 5 meters away, high three-quarter angle
from behind and above the seat.
FRAME: the open rover deck — matte brick-red tube frame, frost dust in
every joint. In the rear cradle a 0.9 m dark grey core cylinder under
two off-white straps. Reaching back to it, the gloved right hand and
forearm of the 45-year-old man; his face above — two-week salt-and-
pepper beard, fully transparent visor, pale grey dust smear on the left
shoulder. His left hand stays on the yoke at the edge of frame.
3.0s — The rover lands from a block; the cylinder jumps about 0.15 m
against its straps and drops back into the cradle.
4.0s — His shoulder twitches; his right hand comes off the yoke and goes
back to the cylinder.
5.0s — His glove closes on the strap and pulls it tight, one hard
motion, a clear boundary between glove and webbing.
6.8s — He looks at the cylinder for half a second, then his hand starts
back toward the yoke.
✂ HARD CUT AT 7.0s

▸ SEGMENT C — 7.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff 2.5 meters away, level with the mirror.
No camera movement inside this segment.
FRAME: the 0.2 m mirror on the LEFT of the roll bar, dead centre and
sharply focused. Inside it: the block field running back and the wall
behind it, bone-white with a hard orange rim, now filling HALF the
mirror's height, nothing else. At the right edge, soft, his shoulder and
jaw with the fully transparent visor.
7.0s — The reflected block field jolts through the mirror; the wall
holds its size at half the glass.
8.0s — The rover hits a block; the whole mirror shakes once and settles.
The wall is still exactly where it was.
10.0s — His eyes flick to the mirror and hold there, then forward.

CUT SCHEDULE:
Exactly two hard cuts, at 3.0s and 7.0s, and no others. Each segment is one unbroken locked-off take with no camera movement inside it. No dissolve, no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle and lighting identical before and after every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Ballistic arc is 0.28 g: 1.2 m of
drop takes about 0.93 s. Rover 8.3 m/s over broken ground, full normal
real-world speed.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: both cuts are instant hard cuts — no dissolve, no
morph, no extra cut anywhere; no slow motion and no floating;
```

---

## 🎬 SAHNE 5 — ⭐ VİRAL ARA + ÇEHOV 2: BACA

_Altı yüz derecelik ızgara donu yiyor. Aracın arkasında bir seksen genişliğinde çıplak kaya izi kalıyor._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  Saf görsel + kurulum. KESİLEMEZ (§0.10 viral ara sahne).
  Bu on saniye izlenmeden S9'un felaketi ve S10'un doruğu anlaşılmaz.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 5 of 14. Macro under the rover's left rear: a 600 degree Celsius
vent grid passing over frost, turning it straight to gas and leaving a
bare rock track behind.

ENVIRONMENT:
The underside rear quarter of a moving field rover, 1.2 meters from
camera: skeletal matte brick-red tube frame, faded off-white markings,
pale frost dust packed into every joint, one open mesh wheel 0.9 meters
in diameter turning at the right of frame. Below it, bone-white frost
0.40 meters deep, dry, matte and granular, over dark basalt bedrock.
Thin carbon-dioxide atmosphere at 1.2% of Earth sea-level pressure,
0.28 g. No water, no ice, no liquid, no vegetation, no animal life, no
human being in frame.

SUBJECT:
A 0.5 meter reactor vent grid on the LEFT REAR of the rover deck: a
flat rectangular grid of heavy metal bars sitting at 600 degrees
Celsius, reading dull orange with hard falloff over one meter and then
nothing — never a halo, never a light that fills the air. Directly
under and behind it, the frost is turning straight to gas: a dense band
of needle-fine vertical jets rising at 200 meters per second from a
1.8 meter wide strip. Behind the vehicle that strip is bare dark
basalt, dry, matte and completely clean, running back out of frame — a
1.8 meter wide black track cut through a white plain, with the two
0.9 meter wheel lines pressed into the frost on either side of it.

CAMERA:
Shot on a 100mm macro lens from a fixed position 1.2 meters away, f/4,
very low and angled slightly back so the hot grid is in the upper left,
the jets fill the centre and the bare track runs away to the lower
right, physically accurate perspective.

LIGHTING:
First Rim phase, sun 2.1 degrees BELOW the horizon. Two sources only:
the dull orange 600 degree grid lighting the jets from above with hard
falloff over one meter, and a cold white wash from frame left off the
distant wall. The bare rock track falls into deep shadow. Every frost
grain keeps sharp texture. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Any surface above 400 degrees
Celsius turns the frost under it straight to gas in about 0.4 seconds —
it never melts, never wets the rock, never drips. The jets stay
needle-fine and vertical because the atmosphere is only 1.2% pressure.
Carried grains obey 0.28 g exactly: 1.37 meters in the first second,
arcing over and falling back. The wheel rotates in ground contact and
never slides.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no hand, no
crew, no clone, no figure of any kind. No text, digits or symbols
anywhere — no subtitles, no title card, no watermark, no HUD. 0% bloom,
no glow filter, no soft focus, no haze, no lens flare. THE FROST IS A
DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — it never melts, never
wets any surface, never drips; there is no liquid, no puddle, no steam
condensation and no wet look anywhere. All carried grains and gravel
obey 0.28 g with continuous momentum — never hovering, never frozen in
mid-air, never flowing like liquid. Terrain static — no melting
terrain, no warping. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain. Emphasis:
the grid is hot metal reading dull orange with hard falloff — no halo,
no bloom, no light filling the air; nothing is on fire, no flame, no
ember, no ash, no smoke; the jets are needle-fine and vertical, never
billowing; the bare track behind is dry and clean; no human, no hand.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 100mm macro lens, fixed
lockoff at 1.2 meters, very low and angled slightly back):
0s — The rover is moving; the 0.5 m grid passes over untouched frost
and a dense band of needle-fine vertical jets rises from under it.
3s — The camera position holds while the vehicle moves through frame:
frost enters the bottom of frame white and leaves the top of frame as
bare dark basalt. The change takes about 0.4 seconds each time.
5s — Grains carried up by the jets rise about 1.4 meters in the first
second, arc over and fall back onto the bare rock, where they stay.
8s — The 1.8 meter bare track runs away behind the vehicle, black
against white, straight and clean, with a wheel line on each side.
10s — The jets continue at the grid, the track continues behind.
No cuts.

EQUIPMENT LOCK: rover unchanged throughout — same 0.5 m grid, same
0.9 m mesh wheel, same brick-red tube frame, first frame identical to
last.

PHYSICS:
0.28 g, thin air at 1.2% pressure. 600 °C turns frost straight to gas
in 0.4 seconds with no liquid stage. Jets needle-fine and vertical.
Carried grains obey 0.28 g and fall back. The wheel rotates in ground
contact and never slides.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no hand, no
figure of any kind. No text, digits or symbols anywhere — no subtitles,
no title card, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no haze, no lens flare. THE FROST IS A DRY GRANULAR SOLID THAT
TURNS STRAIGHT TO GAS — it never melts, never wets any surface, never
drips; no liquid, no puddle, no steam condensation, no wet look
anywhere. All carried grains obey 0.28 g — never hovering, never frozen
in mid-air, never flowing like liquid. Terrain static. No animal, no
creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: no fire, no flame, no ember, no ash, no smoke —
the grid is hot metal and the gas is cold; no halo, no bloom around the
grid; the jets are needle-fine and vertical, never billowing; the bare
track is dry and clean and stays bare; no human, no hand anywhere.
```

---

## 🎬 SAHNE 6 — BEYAZ OVA: MOTORU KAPAT

_Ufka kadar tek bir kara leke yok. Ve baca altı yüz derece. Hızını veren şey, zemini patlatacak olan şey._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 5+5 = 10.0 s
  A  0.0-5.0 s   32mm · 80 m · çok geniş, hafif yüksek
  ✂  5.0 s       ölçek: çok geniş → yakın        (+80° açı farkı)
  B  5.0-10.0 s  50mm · 3 m · sürücü ve güç kolu
  EKSEN   ikisinde de cephe SOLDA, hareket SAĞA
  KES ANI elin güç koluna gitmeye başladığı hareket üzerinde
  ⭐ SES: motor sesinin kesildiği an segment B'nin İÇİNDE (7.5 s),
    kesmede DEĞİL. Ses kesilir, görüntü akar (§0.19 ②).
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 6 of 14, opening frame. A 900-meter plain of unbroken frost with
no bare rock anywhere in it, the rover entering at the left, the ship a
speck on the far side.

ENVIRONMENT:
A completely flat dark basalt plain under an unbroken sheet of
bone-white frost 0.40 meters deep, dry, matte and granular, 900 meters
across and running to the horizon left and right, at 0.28 g under a
thin carbon-dioxide atmosphere at 1.2% of Earth sea-level pressure.
There is not a single patch of bare rock in it. Sky deep indigo-violet
overhead, pale orange low on the LEFT horizon. Filling the left of
frame, an advancing wall of sublimating frost 60 meters high with a
hard orange rim on its crest, its face made of needle-fine vertical gas
jets rising at 200 meters per second. Far across the white field on the
right, a dark bare basalt outcrop with a 16 meter three-legged lander
standing on it, matte brick-red with faded off-white markings, small at
this distance. No water, no ice, no liquid, no vegetation, no animal
life.

SUBJECT:
The 3.2 meter long, 1.8 meter wide open-frame four-wheel rover entering
the white field from the left at 14.4 meters per second: skeletal matte
brick-red tube frame, four open mesh wheels each 0.9 meters in
diameter, an open roll bar with a 0.2 meter mirror on its LEFT, a rear
cargo cradle with one 0.9 meter dark grey core cylinder under two
off-white straps, a 0.5 meter reactor vent grid on the LEFT REAR at 600
degrees Celsius reading dull orange with hard falloff over one meter,
and a 1.78 meter man in a matte brick-red exploration suit with faded
off-white seam tape and one fully transparent seamless visor in the
seat. Behind the rover, a 1.8 meter wide bare rock track and two wheel
lines run back across the frost. Physically accurate perspective,
correct engineering proportions, realistic scale relationships —
neither the rover nor the ship must ever appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 80 meters away,
f/11, slightly elevated so the whole width of the white field, the wall
on the left and the distant outcrop on the right are all in frame,
physically accurate perspective.

LIGHTING:
First Rim phase, sun 1.8 degrees BELOW the horizon. The wall on the
left is the key and washes the white field with cold light; the field
itself is the brightest large surface in the film so far. The distant
outcrop and lander read as a dark notch on the right. Shadows weak and
soft-edged. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The rover holds 14.4 m/s, the wall
holds 13.3 m/s. The frost is a dry granular solid that turns straight
to gas at either direct sunlight or any surface above 400 °C — and the
rover's vent grid is at 600 °C, which is the problem this shot states
without a word. Thrown grains obey 0.28 g.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure at the ship. No text, digits or
symbols anywhere — no subtitles, no title card, no watermark, no HUD.
0% bloom, no glow filter, no soft focus, no haze, no lens flare. Suit
and equipment identical from first frame to last; wear stays fixed. THE
FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — no liquid,
no puddle, no steam condensation, no wet look anywhere. All thrown
grains obey 0.28 g with continuous momentum — never hovering, never
frozen in mid-air, never flowing like liquid. The advancing wall moves
at one constant speed and never surges. Terrain static — no melting
terrain, no warping. No animal, no creature. No Unreal Engine or video
game aesthetic. Photorealistic, 35mm grain. Emphasis: the white field
must be COMPLETELY unbroken — not one patch of bare rock, not one dark
stone in it; no fire, no smoke, no mushroom cloud; exactly one human
and nobody at the distant ship; not miniature, not toy-like.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 5.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 80 meters away, slightly
elevated.
FRAME: a 900 m wide unbroken sheet of bone-white frost 0.40 m deep with
no bare rock in it; on the left a 60 m wall of sublimating frost with a
hard orange rim; far right, a dark basalt outcrop with a 16 m three-
legged matte brick-red lander on it. Entering from the left, the 3.2 m
open-frame four-wheel rover with four 0.9 m mesh wheels, a 0.2 m mirror
on the LEFT of its roll bar, a 0.9 m core cylinder under two straps and
a 0.5 m vent grid at 600 °C reading dull orange, one 1.78 m man in a
matte brick-red suit in the seat.
0.0s — The rover crosses the last bare ridge and rolls out onto the
unbroken white field at 14.4 m/s.
2.0s — Under its left rear a thin dense band of needle-fine jets starts
up where the 600 °C grid meets fresh frost — and it does not stop.
3.5s — The band thickens; the vehicle rocks slightly as the ground under
its left rear gives way.
✂ HARD CUT AT 5.0s

▸ SEGMENT B — 5.0 to 10.0 s
SETUP: 50mm lens, fixed lockoff 3 meters away, three-quarter angle from
the front right.
FRAME: the single exposed seat of the moving rover — skeletal matte
brick-red tube frame, faded off-white markings, frost dust in every
joint, a bare metal power lever 0.3 m long at his right hand. In the
seat, the same 45-year-old man 1.78 m tall: pale weather-cracked skin
with visible pore texture, a long narrow nose broken once and set
crooked, deep-set grey eyes, a two-week salt-and-pepper beard, a matte
brick-red suit with faded off-white seam tape, a scuffed dark grey chest
pack, one fully transparent seamless visor with his face readable
through it, a pale grey dust smear on the left shoulder. Behind him,
soft, the white field and the wall on the left.
5.0s — His right hand is already moving to the 0.3 m power lever; his
left stays on the yoke.
6.0s — His hand closes on the lever and stops there for half a second —
a clear boundary between glove and metal.
7.0s — He pulls it fully closed in one motion.
7.5s — ⭐ The engine noise stops. Nothing in frame changes visually at
all: the plain still slides past behind him, his hands do not move. Only
the sound is gone.
10.0s — He puts his right hand back on the yoke. His expression has not
changed.

CUT SCHEDULE:
Exactly one hard cut, at 5.0s, and no others. Each segment is one unbroken locked-off take with no camera movement inside it. No dissolve, no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle and lighting identical before and after every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Rover 14.4 m/s, wall 13.3 m/s. The
600 °C grid sublimates frost under the vehicle in about 0.4 seconds,
with no liquid stage. After the lever closes the grid begins cooling
toward grey over about 40 seconds and the vehicle coasts, losing speed
at 0.15 m/s². His hand moves at full normal real-time human speed.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: the cut is an instant hard cut — no dissolve, no
morph, and no second cut anywhere; nothing flickers or flashes when the
sound stops; the ground under the rover does not crater or collapse, it
turns to gas in a thin band;
```

---

## 🎬 SAHNE 7 — SESSİZ SÜZÜLME

_Motor kapalı. Yapabileceği hiçbir şey yok. Filmin tek kesmesiz, tek sessiz on saniyesi — ve en gergin olanı._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  ⭐ BİLİNÇLİ RİTİM KIRILMASI. On iki kesmelik bir filmde kesmesiz on
  saniye, gerilimin kendisidir. Karakter hiçbir şey yapamıyor; kamera
  da yapmıyor. Bu sahne KESİLEMEZ ve BÖLÜNEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 7 of 14. The rover coasting silently across the white field with
its vent grid gone grey, the wall closing behind it.

ENVIRONMENT:
A completely flat dark basalt plain under an unbroken sheet of
bone-white frost 0.40 meters deep, dry, matte and granular, at 0.28 g
under a thin carbon-dioxide atmosphere at 1.2% of Earth sea-level
pressure. Not one patch of bare rock anywhere in frame. Sky deep
indigo-violet overhead, pale orange low on the LEFT horizon. Filling
the left half of frame and much closer than before, the advancing wall
of sublimating frost 60 meters high with a hard orange rim on its
crest, its face made of needle-fine vertical gas jets rising at 200
meters per second. No water, no ice, no liquid, no vegetation, no
animal life.

SUBJECT:
The 3.2 meter long, 1.8 meter wide open-frame four-wheel rover coasting
left to right: skeletal matte brick-red tube frame over a flat deck,
faded off-white markings, mismatched replacement tubes, four open mesh
wheels each 0.9 meters in diameter still turning but no longer driven,
an open tube roll bar with a 0.2 meter mirror on its LEFT, a rear cargo
cradle holding one 0.9 meter dark grey core cylinder under two
off-white straps, and a 0.5 meter reactor vent grid on the LEFT REAR
that has cooled to plain grey metal — no orange anywhere on the
vehicle. Behind the rover there is now NO bare rock track, only two
0.9 meter wheel lines pressed into unbroken frost. In the seat, a 1.78
meter man in a matte brick-red exploration suit with faded off-white
seam tape and one fully transparent seamless visor, both hands resting
on the yoke, not steering, doing nothing. Physically accurate
perspective, correct engineering proportions, realistic scale
relationships — the rover must never appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 15 meters away,
f/5.6, side-on and low so the rover crosses the lower third of frame
and the wall fills the height behind it, physically accurate
perspective.

LIGHTING:
Close Light phase, sun 1.3 degrees BELOW the horizon. The wall is now
close enough to be the key light: a cold white key from frame left
across the rover and one side of the man's face, deep shadow on the
right. Nothing on the vehicle is warm any more. Shadows weak-edged but
deep. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The rover is coasting with no drive:
it decelerates at 0.15 m/s², so over these ten seconds it slows from
about 11.5 to 10.0 m/s while the wall holds a constant 13.3 m/s — the
gap closes visibly for the first time in the film. The wheels turn
freely in ground contact and throw almost nothing. No jets rise from
under the vehicle because the grid is cold.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no steam condensation, no wet look
anywhere. All thrown grains obey 0.28 g with continuous momentum —
never hovering, never frozen in mid-air, never flowing like liquid. The
advancing wall moves at one constant speed and never surges, never
lunges, never accelerates. Terrain static — no melting terrain, no
warping. No animal, no creature. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: NO ORANGE ANYWHERE ON
THE VEHICLE — the vent grid is cold grey metal in every frame; no jets
under the rover; no bare rock track behind it; no fire, no smoke; the
wall closes steadily and never lunges; exactly one human; not
miniature.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 32mm anamorphic lens,
fixed lockoff at 15 meters, side-on and low):
0s — The rover coasts into frame from the left, wheels turning freely,
vent grid cold grey, no jets under it.
3s — It crosses frame centre, slowing. The man's hands rest on the yoke
and do not move. He does not look back.
5s — Behind him the wall is visibly closer at the end of this second
than at the start — the first time in the film that the gap has changed.
7s — He lets out one short controlled breath; the bottom edge of the
visor fogs a centimetre and clears.
10s — The rover is still moving, slower, toward the right of frame. The
wall is closer. Nothing else has happened.
No cuts.

EQUIPMENT LOCK: rover and suit unchanged throughout — same four wheels,
same core cylinder under two straps, vent grid cold grey in the first
frame and cold grey in the last, first frame identical to last.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The rover coasts and decelerates at
0.15 m/s² from about 11.5 m/s. The wall holds a constant 13.3 m/s and
therefore gains steadily. Wheels turn freely in ground contact. No jets
anywhere under the vehicle.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no wet look anywhere. All thrown grains
obey 0.28 g — never hovering, never frozen in mid-air, never flowing
like liquid. The wall moves at one constant speed and never surges,
never lunges, never accelerates. Terrain static. No animal, no
creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: the vent grid is cold grey in every single frame
— no orange, no heat, no jets under the vehicle; the man does nothing
and does not turn around; the wall gains steadily and smoothly; no
fire, no smoke; exactly one human.
```

---
## 🎬 SAHNE 8 — DURUŞ: İKİ YÜZ ON METRE EKSİK

_Rover duruyor. Gemi hâlâ ötede. Ve aynada başka hiçbir şey yok._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 4+6 = 10.0 s
  A  0.0-4.0 s   32mm · 20 m · geniş, alçak yandan
  ✂  4.0 s       ölçek: geniş → yakın            (+75° açı farkı)
  B  4.0-10.0 s  75mm · 2.5 m · ayna · ⭐ SAYAÇ KADRAJI 3/3
  EKSEN   ikisinde de cephe SOLDA
  KES ANI aracın son yuvarlanışı üzerinde — hareket biterken kesilir
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 8 of 14, opening frame. The rover rolls its last meters to a stop
in the middle of the white field, the outcrop and the ship still 210
meters ahead.

ENVIRONMENT:
A completely flat dark basalt plain under an unbroken sheet of
bone-white frost 0.40 meters deep, dry, matte and granular, at 0.28 g
under a thin carbon-dioxide atmosphere at 1.2% of Earth sea-level
pressure. Sky deep indigo-violet overhead, pale orange low on the LEFT
horizon. Filling the left half of frame, the advancing wall of
sublimating frost 60 meters high with a hard orange rim, its face made
of needle-fine vertical gas jets rising at 200 meters per second. On
the right edge of frame, a dark bare basalt outcrop with a 16 meter
three-legged matte brick-red lander standing on it, separated from the
rover by an unbroken stretch of white. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
The 3.2 meter long, 1.8 meter wide open-frame four-wheel rover in its
last meters of travel: skeletal matte brick-red tube frame, four open
mesh wheels each 0.9 meters in diameter turning slower and slower, an
open roll bar with a 0.2 meter mirror on its LEFT, a rear cargo cradle
holding one 0.9 meter dark grey core cylinder under two off-white
straps, and a 0.5 meter reactor vent grid on the LEFT REAR that is cold
grey metal with no orange anywhere. Two wheel lines run back from it
across the frost toward the wall. In the seat, a 1.78 meter man in a
matte brick-red exploration suit with faded off-white seam tape and one
fully transparent seamless visor, sitting still. Physically accurate
perspective, correct engineering proportions, realistic scale
relationships — neither the rover nor the ship must appear miniature or
toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 20 meters away,
f/8, low and side-on so the rover is left of centre, the unbroken white
gap runs across the frame and the outcrop with the lander sits at the
right edge, physically accurate perspective.

LIGHTING:
Close Light phase, sun 0.9 degrees BELOW the horizon. The wall is the
key: cold white from frame left across the rover and the field, deep
shadow on the right side of everything. The distant outcrop reads as a
dark shape. Shadows weak-edged but deep. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The rover has been coasting at 0.15
m/s² deceleration and is about to stop; the wheels slow evenly and stop
turning without locking or skidding. The wall continues at a constant
13.3 m/s, 400 meters back. Nothing on the vehicle is hot.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure at the ship or in any mirror. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. Suit and equipment identical from first frame to last; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no wet look anywhere. All thrown grains
obey 0.28 g — never hovering, never frozen in mid-air, never flowing
like liquid. The advancing wall moves at one constant speed and never
surges. Terrain static — no melting terrain, no warping. No animal, no
creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: NO ORANGE ANYWHERE ON THE VEHICLE — the grid is
cold grey; the rover coasts to a stop smoothly and never skids, never
locks a wheel, never crashes; the white gap between the rover and the
outcrop is completely unbroken; exactly one human and nobody at the
ship; not miniature.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 4.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 20 meters away, low and side-
on.
FRAME: an unbroken white frost field; on the left a 60 m wall of
sublimating frost with a hard orange rim; on the right edge a bare
basalt outcrop with a 16 m three-legged matte brick-red lander. Left of
centre, the 3.2 m open-frame four-wheel rover with four 0.9 m mesh
wheels, a 0.2 m mirror on the LEFT of its roll bar, a 0.9 m core
cylinder under two straps, a 0.5 m vent grid that is COLD GREY, and a
1.78 m man in a matte brick-red suit in the seat.
0.0s — The rover is still rolling slowly, wheels barely turning, no
drive, no jets, no orange anywhere on it.
2.0s — It slows to walking pace; the frost stops moving under the
wheels.
3.0s — It stops completely. The wheels make one last quarter turn and
hold. Nothing skids.
✂ HARD CUT AT 4.0s

▸ SEGMENT B — 4.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff 2.5 meters away, level with the mirror.
No camera movement inside this segment.
FRAME: the 0.2 m rear-view mirror on the LEFT of the roll bar, dead
centre and sharply focused, glass scratched, edge packed with frost
dust. Inside the mirror there is now only ONE thing: the advancing wall
of sublimating frost, bone-white with a hard orange rim and a face of
needle-fine vertical jets, filling the mirror EDGE TO EDGE — no horizon,
no ground in front of it, nothing else. At the right edge of frame,
closer and slightly soft, his shoulder and jaw: pale weather-cracked
skin with visible pore texture, a long narrow nose broken once and set
crooked, deep-set grey eyes, a two-week salt-and-pepper beard, a matte
brick-red suit with faded off-white seam tape, a scuffed dark grey chest
pack, a fully transparent seamless visor, a pale grey dust smear on the
left shoulder.
4.0s — Nothing slides through the mirror; the vehicle is stopped.
6.0s — He looks into the mirror and this time he does not look away.
8.0s — He turns his head forward, away from the mirror, toward the
outcrop 210 meters ahead — out of frame right.
9.0s — He lets out one short controlled breath; the bottom edge of the
visor fogs a centimetre and clears.
10.0s — He is still, looking forward, the mirror still full behind him.

CUT SCHEDULE:
Exactly one hard cut, at 4.0s, and no others. Each segment is one unbroken locked-off take with no camera movement inside it. No dissolve, no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle and lighting identical before and after every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Even deceleration to a full stop, no
skid, no wheel lock. The wall continues at a constant 13.3 m/s and
gains the whole time; in the mirror it grows only very slightly across
six seconds.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: the cut is an instant hard cut — no dissolve, no
morph, no second cut anywhere; the mirror is filled EDGE TO EDGE by the
wall with no horizon and no face in it; no orange anywhere on the
vehicle;
```

---

## 🎬 SAHNE 9 — 🆕 DENEME: ZEMİN TEKERLEĞİN ALTINDA ÇÖKÜYOR

_Apaçık çözümü deniyor: motoru aç, son iki yüz on metreyi sür. Ve gezegen hayır diyor._

```
⚙️ KESME PLANI — 3 segment · 2 kesme · 3+4+3 = 10.0 s
  A  0.0-3.0 s   75mm · 1.5 m · el ve güç kolu
  ✂  3.0 s       ölçek: yakın → makro            (+50° açı farkı)
  B  3.0-7.0 s   100mm makro · 1.2 m · sol arka tekerleğin altı
  ✂  7.0 s       ölçek: makro → geniş            (+85° açı farkı)
  C  7.0-10.0 s  32mm · 20 m · geniş, yandan
  EKSEN   üçünde de cephe SOLDA
  KES ANI ikisi de hareket üzerinde: kolun itilişi ve tekerleğin çöküşü
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 9 of 14, opening frame. A gloved hand on the power lever of the
stopped rover, about to open it.

ENVIRONMENT:
The seat area of a stopped field rover: skeletal matte brick-red tube
frame, faded off-white markings, pale frost dust packed into every
joint, a bare metal power lever 0.3 meters long. Beyond and thrown soft
by shallow depth of field, an unbroken white frost field and, on the
left, the advancing wall of sublimating frost, close now and very
bright. Thin carbon-dioxide atmosphere at 1.2% of Earth sea-level
pressure, 0.28 g.

SUBJECT:
The gloved right hand and forearm of a 45-year-old man, filling the
lower two thirds of frame, closing on the 0.3 meter power lever. Above
and behind it, in the upper right of frame and sharply lit, his face: a
45-year-old man, 1.78 meters tall, rangy and long-limbed, with pale
weather-cracked skin with real visible pore texture, a long narrow nose
broken once and set slightly crooked, deep-set grey eyes with heavy
creases at the outer corners, thick greying eyebrows, a two-week
salt-and-pepper beard, chapped lips. He wears a matte brick-red
exploration suit with faded off-white seam tape along both forearms and
across the chest, a scuffed dark grey hard-shell chest pack holding a
flat integrated rebreather, and heavy ribbed boots. One fully
transparent seamless visor, no tint, no coating, no mask or regulator
beneath it, his whole face clearly readable through it. A narrow dark
band on his right wrist shows a slow abstract amber pulse and nothing
else. His wear marks are fixed and never move: a pale grey dust smear
across the left shoulder, a scuffed patch on the right forearm where
the seam tape has lifted, and a film of frost dust across the top edge
of the visor. He is looking forward, toward the outcrop, not at his
hand.

CAMERA:
Shot on a 75mm lens from a fixed position 1.5 meters away, f/2, low and
tight on the lever with his face in the upper right of frame,
physically accurate perspective.

LIGHTING:
Close Light phase, sun 0.6 degrees BELOW the horizon. The wall is the
only key: hard cold white from frame left across his knuckles, his
forearm and the left side of his face, with deep unlit shadow on the
right. Skin keeps visible pore texture and real shadow. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. His hand moves at full normal
real-time human speed. The glove keeps a clear structural boundary
against the lever — rigid-body collision throughout, no merging, no
sinking in. Opening the lever restarts the reactor and the 0.5 meter
vent grid begins heating from grey back to 600 degrees Celsius.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD, no marking on the lever. 0% bloom, no glow filter,
no soft focus beyond the stated shallow depth of field, no haze, no
lens flare. Photorealistic skin with pores and fatigue — no
airbrushing, no waxy texture, no face morphing, identical bone
structure throughout. Suit and equipment identical from first frame to
last; wear stays fixed. Hands keep a clear boundary at every contact —
no merging, no phasing, no extra fingers, rigid-body collision. No
liquid, no wet look anywhere. Terrain static. No animal, no creature.
No Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
Emphasis: no readable text, number, icon or gauge anywhere on the lever
or the frame; no indicator light, no screen content; his mouth stays
closed, he does not speak; the visor stays closed and fully
transparent; exactly one human, exactly ten fingers.
```

### 🎥 VIDEO PROMPT — 10 saniye, 2 kesme içinde

```
MOTION — 10 seconds, three fixed setups joined by two hard cuts:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 75mm lens, fixed lockoff 1.5 meters away, low and tight on the
power lever with his face in the upper right. No camera movement inside
this segment.
FRAME: the gloved right hand and forearm of the 45-year-old man on a 0.3
m bare metal power lever; his face above right — pale weather-cracked
skin with visible pore texture, a two-week salt-and-pepper beard, deep-
set grey eyes, a matte brick-red suit with faded off-white seam tape, a
fully transparent seamless visor, a pale grey dust smear on the left
shoulder. Behind, soft, the white field and the wall on the left.
0.0s — His hand closes on the lever.
1.5s — He pushes it fully open in one motion, a clear boundary between
glove and metal.
2.8s — His eyes go forward to the outcrop. His hand returns to the yoke.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 7.0 s
SETUP: 100mm macro lens, fixed lockoff 1.2 meters away, very low,
looking under the rover's left rear. No camera movement inside this
segment.
FRAME: the 0.5 m reactor vent grid on the LEFT REAR of the deck, heavy
metal bars now back at 600 °C reading dull orange with hard falloff over
one meter; beside it one open mesh wheel 0.9 m in diameter; below, bone-
white frost 0.40 m deep over dark basalt.
3.0s — The grid is orange again. A dense band of needle-fine vertical
jets erupts from the frost directly beneath it at 200 m/s.
4.5s — The 0.40 m frost layer under the wheel turns to gas and the
surface gives way; the wheel drops about 0.4 meters into loose gravel
and bare rock.
6.0s — The wheel spins in the pit, throwing gravel that arcs and falls
back under 0.28 g. It does not climb out.
✂ HARD CUT AT 7.0s

▸ SEGMENT C — 7.0 to 10.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 20 meters away, low and side-
on.
FRAME: the unbroken white field; on the left the 60 m wall with its hard
orange rim; on the right edge the bare outcrop with the 16 m three-
legged lander. The 3.2 m rover stands about 30 meters further on than
before, tilted 8 degrees over to the left with its left rear wheel sunk
in a shallow pit, a ragged burned patch of bare rock around it, the 0.9
m core cylinder still strapped in the cradle, the 1.78 m man in the
seat.
7.0s — The rover is stopped and tilted; jets still rising from the
burned patch under its left rear.
8.5s — He reaches down and pulls the power lever closed. The jets stop.
10.0s — Stillness. The wall is closer. The outcrop is still far away.

CUT SCHEDULE:
Exactly two hard cuts, at 3.0s and 7.0s, and no others. Each segment is one unbroken locked-off take with no camera movement inside it. No dissolve, no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle and lighting identical before and after every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. 600 °C turns the 0.40 m frost layer
straight to gas in about 0.4 seconds with no liquid stage; the ground
under the wheel is removed, not melted, and the wheel drops 0.4 m into
loose gravel. Thrown gravel obeys 0.28 g: 1.37 m in the first second.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: both cuts are instant hard cuts — no dissolve, no
morph, no extra cut anywhere; the ground does not crater, does not
collapse into a hole and does not swallow the vehicle — one wheel drops
0.4 m and stops;
```

---

## 🎬 SAHNE 10 — ⭐ DORUK: ROVERİ GERİ GÖNDERMEK

_Aynı kolu üçüncü kez tutuyor. Bu kez vitesi geri alıyor ve iniyor._

```
⚙️ KESME PLANI — 3 segment · 2 kesme · 3+4+3 = 10.0 s
  A  0.0-3.0 s   75mm · 1.5 m · el ve kol · ⭐ TEREDDÜT + KARAR
  ✂  3.0 s       ölçek: yakın → orta-geniş       (+100° açı farkı)
  B  3.0-7.0 s   50mm · 6 m · araçtan iniş · ⚠️ KART 4 segmenti
  ✂  7.0 s       ölçek: orta-geniş → geniş       (+45° açı farkı)
  C  7.0-10.0 s  32mm · 25 m · ters yönler
  EKSEN   üçünde de cephe SOLDA; ⭐ ADAM sağa, ROVER sola gidiyor
  KES ANI ikisi de hareket üzerinde: kolun itilişi ve iniş anı
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 10 of 14, opening frame. The same gloved hand on the same power
lever — and this time it is not moving.

ENVIRONMENT:
The seat area of a stopped and slightly tilted field rover: skeletal
matte brick-red tube frame, faded off-white markings, pale frost dust
packed into every joint, a bare metal power lever 0.3 meters long and a
short bare metal drive selector beside it. Beyond and thrown soft by
shallow depth of field, an unbroken white frost field and, on the left,
the advancing wall of sublimating frost, very close and very bright.
Thin carbon-dioxide atmosphere at 1.2% of Earth sea-level pressure,
0.28 g.

SUBJECT:
The gloved right hand and forearm of a 45-year-old man, filling the
lower two thirds of frame, resting on the 0.3 meter power lever and
completely still. Above and behind it, in the upper right of frame and
sharply lit, his face: a 45-year-old man, 1.78 meters tall, rangy and
long-limbed, with pale weather-cracked skin with real visible pore
texture, a long narrow nose broken once and set slightly crooked,
deep-set grey eyes with heavy creases at the outer corners, thick
greying eyebrows, a two-week salt-and-pepper beard, chapped lips. He
wears a matte brick-red exploration suit with faded off-white seam tape
along both forearms and across the chest, a scuffed dark grey
hard-shell chest pack holding a flat integrated rebreather, and heavy
ribbed boots. One fully transparent seamless visor, no tint, no
coating, no mask or regulator beneath it, his whole face clearly
readable through it. A narrow dark band on his right wrist shows a slow
abstract amber pulse and nothing else. His wear marks are fixed and
never move: a pale grey dust smear across the left shoulder, a scuffed
patch on the right forearm where the seam tape has lifted, and a film
of frost dust across the top edge of the visor. He is not looking at
his hand; he is looking back over his left shoulder, out of frame, at
the wall.

CAMERA:
Shot on a 75mm lens from a fixed position 1.5 meters away, f/2, low and
tight on the lever with his face in the upper right of frame — the
identical setup used earlier in this film, physically accurate
perspective.

LIGHTING:
Close Light phase, sun 0.35 degrees BELOW the horizon. The wall is the
only key: hard cold white from frame left across his knuckles, his
forearm and the left side of his face, with deep unlit shadow on the
right. Skin keeps visible pore texture and real shadow. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Nothing in frame moves in this
opening moment. The glove keeps a clear structural boundary against the
lever — rigid-body collision throughout.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any mirror or reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD, no marking on the lever or selector. 0% bloom, no
glow filter, no soft focus beyond the stated shallow depth of field, no
haze, no lens flare. Photorealistic skin with pores and fatigue — no
airbrushing, no waxy texture, no face morphing, identical bone
structure throughout. Suit and equipment identical from first frame to
last; wear stays fixed. Hands keep a clear boundary at every contact —
no merging, no phasing, no extra fingers, rigid-body collision. No
liquid, no wet look anywhere. Terrain static. No animal, no creature.
No Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
Emphasis: the hand is COMPLETELY STILL in this frame — no motion blur
on it, no tremor; no readable text, number or gauge anywhere; his mouth
stays closed; the visor stays closed and fully transparent; exactly one
human, exactly ten fingers.
```

### 🎥 VIDEO PROMPT — 10 saniye, 2 kesme içinde

```
MOTION — 10 seconds, three fixed setups joined by two hard cuts:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 75mm lens, fixed lockoff 1.5 meters away, low and tight on the
power lever with his face in the upper right. No camera movement inside
this segment.
FRAME: the gloved right hand and forearm of the 45-year-old man resting
on a 0.3 m bare metal power lever, a short bare metal drive selector
beside it; his face above right — two-week salt-and-pepper beard, deep-
set grey eyes, fully transparent visor, pale grey dust smear on the left
shoulder. He is looking back over his left shoulder, out of frame.
0.0s — His hand rests on the lever and does not move.
1.0s — Still nothing. His jaw tightens once. The hand has not moved.
2.0s — He turns his head forward and in the same motion pushes the lever
fully open — one hard, committed push.
2.5s — His hand drops to the drive selector and pulls it back into
REVERSE. A clear boundary between glove and metal throughout.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 7.0 s
SETUP: 50mm lens, fixed lockoff 6 meters away, chest height, side-on. No
camera movement inside this segment.
FRAME: an unbroken white frost field with the 60 m wall filling the left
third, very close. The 3.2 m open-frame four-wheel rover fills the right
half, already rolling BACKWARDS to the LEFT at about 6 m/s: four 0.9 m
mesh wheels turning in reverse, a 0.2 m mirror on the LEFT of the roll
bar, the 0.9 m core cylinder still under two straps, the 0.5 m vent grid
at 600 °C dull orange with needle-fine jets under it. Stepping off the
deck, the 45-year-old man in a matte brick-red suit with off-white seam
tape, heavy ribbed boots and a fully transparent visor. NO SHIP IN
FRAME.
3.0s — He steps off the deck; the drop of about 0.9 m takes roughly 0.8
seconds at 0.28 g.
3.8s — His boots hit the frost; his knees bend deeply to absorb it, his
body angles right. The frost compacts and does not give way.
5.0s — The rover continues away to the left, UNMANNED, the seat empty,
leaving a widening band of bare dark rock behind it.
6.8s — He straightens and takes his first step to the right.
✂ HARD CUT AT 7.0s

▸ SEGMENT C — 7.0 to 10.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 25 meters away, chest height,
side-on.
FRAME: one frame, two directions. On the right, the 1.78 m man in the
matte brick-red suit running RIGHT with long low strides. On the left,
the 3.2 m rover reversing LEFT at about 6 m/s with an EMPTY SEAT, the
core cylinder still strapped in, its 0.5 m vent grid dull orange.
Between them, a strip of bare dark basalt about 40 m wide burned through
the frost, growing longer every second. Behind, the 60 m wall with its
hard orange rim.
7.0s — He runs right at about 5 m/s; the rover reverses left; the gap
between them opens fast.
8.5s — The black strip lengthens continuously between them.
10.0s — He is near the right edge, the rover near the left, the strip
running the whole width between them.

CUT SCHEDULE:
Exactly two hard cuts, at 3.0s and 7.0s, and no others. Each segment is
one unbroken locked-off take, no camera movement inside it. No dissolve,
no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle
and light identical across every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The step down is a 0.28 g fall: 0.9 m
in about 0.8 seconds, not slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: both cuts are instant hard cuts — no dissolve, no
morph, no extra cut anywhere;
```

---
## 🎬 SAHNE 11 — PATLAMA: DUVAR KIRILIYOR

_Şerit yanıp bitiyor. Cephe oraya varıyor ve altmış metreden sıfıra düşüyor. Arkasında sadece ışık kalıyor._

```
⚙️ KESME PLANI — 3 segment · 2 kesme · 3+4+3 = 10.0 s
  A  0.0-3.0 s   32mm · 60 m · geniş, alçak · İNSANSIZ
  ✂  3.0 s       ölçek: geniş → çok geniş        (+35° açı farkı)
  B  3.0-7.0 s   32mm · 120 m · çok geniş, duvara dik · İNSANSIZ
  ✂  7.0 s       ölçek: çok geniş → orta         (+90° açı farkı)
  C  7.0-10.0 s  50mm · 8 m · koşan adam, arkadan ışık
  EKSEN   üçünde de cephe SOLDA, kaçış SAĞA
  KES ANI ikisi de hareket üzerinde: duvarın çökme anı ve adımın ortası
  ⚠️ A ve B insansız, C'de tek insan var — negatif cümlesi segment
    bazında değil, sahne bazında "exactly one human" olarak yazılır
    ve A/B'de kimsenin OLMADIĞI ayrıca vurgulanır.
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 11 of 14, opening frame. The unmanned rover has reached the foot
of the wall at the end of a 40-meter strip of bare rock it burned
through the frost.

ENVIRONMENT:
A dark basalt plain under bone-white frost 0.40 meters deep, dry, matte
and granular, at 0.28 g under a thin carbon-dioxide atmosphere at 1.2%
of Earth sea-level pressure. Sky deep indigo-violet overhead, pale
orange low on the LEFT horizon. Filling the left two thirds of frame,
the advancing wall of sublimating frost 60 meters high with a hard
orange rim, its face made of needle-fine vertical gas jets rising at
200 meters per second, its base only meters from the vehicle. Running
from the lower right to the vehicle, a strip of bare dark basalt about
40 meters wide and 200 meters long, burned clean through the white
field, dry and matte with no residue. No human being anywhere in frame.
No water, no ice, no liquid, no vegetation, no animal life.

SUBJECT:
The 3.2 meter long, 1.8 meter wide open-frame four-wheel rover at the
end of the strip, still reversing: skeletal matte brick-red tube frame,
four open mesh wheels each 0.9 meters in diameter, an open roll bar
with a 0.2 meter mirror on its LEFT, an EMPTY SEAT, the 0.9 meter dark
grey core cylinder still strapped in the rear cradle under two
off-white straps, and a 0.5 meter reactor vent grid on the LEFT REAR at
600 degrees Celsius reading dull orange with hard falloff over one
meter, throwing a dense band of needle-fine jets from the last frost
under it. Physically accurate perspective, correct engineering
proportions, realistic scale relationships — the rover must never
appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 60 meters away,
f/8, low and side-on so the burned strip runs from the lower right to
the vehicle and the full 60-meter height of the wall stands behind,
physically accurate perspective.

LIGHTING:
Break phase, sun 0.15 degrees BELOW the horizon. The wall is the key,
hard cold white from frame left, with a hard orange rim along its
crest. The bare strip reads almost black. The vent grid is a small dull
orange point. 0% bloom.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The strip is bare rock with no frost
left on it at all — there is nothing there to turn to gas. The wall
advances at a constant 13.3 m/s toward the strip. Frost is a dry
granular solid with no liquid stage. Thrown grains obey 0.28 g.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no crew, no
clone, no driver in the seat, no figure of any kind anywhere. No text,
digits or symbols anywhere — no subtitles, no title card, no watermark,
no HUD. 0% bloom, no glow filter, no soft focus, no haze, no lens
flare. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS —
no liquid, no puddle, no steam condensation, no wet look anywhere. All
thrown grains obey 0.28 g with continuous momentum — never hovering,
never frozen in mid-air, never flowing like liquid. The advancing wall
moves at one constant speed and never surges, never lunges. Terrain
static — no melting terrain, no warping. No animal, no creature. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
Emphasis: the seat is EMPTY and there is no human being anywhere in
this image; the rover does not explode, does not burn and does not
catch fire; no fireball, no flame, no smoke, no shockwave; the burned
strip is bare dry rock; not miniature.
```

### 🎥 VIDEO PROMPT — 10 saniye, 2 kesme içinde

```
MOTION — 10 seconds, three fixed setups joined by two hard cuts:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 60 meters away, low and side-
on. No human in frame.
FRAME: a bone-white frost plain with a 40 m wide strip of bare dark
basalt running from the lower right to the base of the wall; on the left
the 60 m wall with a hard orange rim; at the end of the strip the 3.2 m
open-frame four-wheel rover, EMPTY SEAT, four 0.9 m mesh wheels turning
in reverse, the 0.9 m core cylinder under two straps, the 0.5 m vent
grid at 600 °C dull orange.
0.0s — The unmanned rover reverses the last meters toward the base of
the wall, jets rising from the last frost under its hot grid.
1.5s — The final patch of frost under the vehicle turns to gas and the
strip is complete: 40 meters wide, bare rock end to end.
2.8s — The wall's leading edge reaches the vehicle; the rover is covered
by the white face — no fire, no flash, simply gone from view.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 7.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 120 meters away, low and
square on to the wall. No human in frame.
FRAME: the wall running from horizon to horizon across the whole frame,
60 m high, bone-white, needle-fine vertical jets, a hard orange rim
along its crest; crossing the plain toward camera, the 40 m wide strip
of bare dark basalt.
3.0s — The wall advances at its full 60 meters, the burned strip lying
ahead of it.
4.5s — The leading edge reaches the strip. Across those 40 meters the
jets stop and the wall drops from 60 meters to nothing in about half a
second — a clean notch of empty air opens in it, vertical-sided.
5.5s — A hard shaft of direct orange sunlight comes through the notch
and lies along the bare rock — the first direct sunlight in the film.
6.8s — The wall keeps advancing on both sides; the notch travels with
it, already narrowing very slightly from both edges.
✂ HARD CUT AT 7.0s

▸ SEGMENT C — 7.0 to 10.0 s
SETUP: 50mm lens, fixed lockoff 8 meters away, side-on at chest height.
No camera movement inside this segment.
FRAME: the 40 m wide strip of bare dark basalt in full backlight;
running RIGHT along it, the 45-year-old man 1.78 m tall in a matte
brick-red suit with off-white seam tape, a dark grey chest pack, heavy
ribbed boots, a fully transparent visor and a pale grey dust smear on
the left shoulder. Behind him on the left, the notch: open air with a
hard shaft of orange sunlight through it; far out on both sides, the
wall still 60 m high.
7.0s — He runs right at about 5 m/s with long, low, controlled strides,
backlit by the shaft through the notch.
8.5s — He crosses frame centre. Behind him nothing rises from the bare
rock — no jets, no wall, only light.
10.0s — He reaches the right edge of frame, still running, still
backlit.

CUT SCHEDULE:
Exactly two hard cuts, at 3.0s and 7.0s, and no others. Each segment is
one unbroken locked-off take, no camera movement inside it. No dissolve,
no fade, no wipe, no morph and no speed ramp at any cut. Suit, vehicle
and light identical across every cut.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Where there is no frost there is
nothing to turn to gas, so the wall's height across the strip is zero —
it is absent, not thinner. Wall speed constant at 13.3 m/s.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any mirror or reflection. No text, digits or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no haze, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical across every cut; wear
stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no wet look anywhere. All thrown grains obey 0.28 g —
never hovering, never frozen in mid-air, never flowing like liquid. The
wall moves at one constant speed and never surges. Hands keep a clear
boundary at every contact — no extra fingers. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: both cuts are instant hard cuts — no dissolve, no
morph, no extra cut anywhere;
```

---

## 🎬 SAHNE 12 — OVERVIEW: İKİ YÜZ KİLOMETRELİK DUVARDAKİ TEK ÇENTİK

_Yukarıdan bakınca ölçek görünüyor: ufuktan ufka bir duvar, ve içinde kırk metrelik tek bir delik._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  ⭐ Filmin TEK Overview sahnesi (§15: iki overview etkiyi yarıya indirir).
  ⭐ MÜZİKSİZ SAHNE (GOOGLE_FLOW §10). En yüksek görsel, en düşük ses.
  ⚠️ Kılavuz §5.2 ⑥: "Overview sahnesinden ÖNCE bilinçli sert kesme
    doğrudur." S11 → S12 geçişi filmin en sert kesmesidir.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 12 of 14. From four kilometers up: a white wall running from
horizon to horizon across a whole world, with one 40-meter notch in it.

ENVIRONMENT:
A dark basalt plain seen from 4 kilometers above, flat to the horizon
under bone-white frost, at 0.28 g with a thin carbon-dioxide atmosphere
at 1.2% of Earth sea-level pressure. The sky above the horizon is deep
indigo-violet grading to pale orange where the sun is rising. On the
night side of the line the plain is white with frost; on the day side
it is bare dark basalt, swept clean. No water, no ice, no liquid, no
vegetation, no animal life, no human being visible at this scale.

SUBJECT:
The terminator front itself, running edge to edge across the frame as a
single continuous line perhaps 200 kilometers long: a wall of
sublimating frost 60 meters high, bone-white, advancing, dividing the
white night side from the dark day side. At one point near frame centre
there is a single clean interruption in it, 40 meters wide — a notch,
insignificantly small against the length of the wall, with a thin
finger of bare dark rock running away from it. At the far end of that
finger, a bare basalt outcrop with a 16 meter three-legged matte
brick-red lander standing on it. Physically accurate perspective,
correct engineering proportions, realistic scale relationships — the
ship must never appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 4 kilometers above
the plain, f/16, looking down at a steep angle so the full length of
the front runs from one edge of frame to the other, physically accurate
perspective.

LIGHTING:
Full Sun phase, sun 0.1 degrees ABOVE the horizon. Hard low direct
sunlight across the whole plain from the left. The frost side is
brilliant; the swept side is dark. The wall throws a long shadow onto
the frost ahead of it. Deep contrast, sharp texture. 0% bloom, no lens
flare.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The whole front advances at a
constant 13.3 meters per second — at this scale that is barely
perceptible, which is the point. The notch is 40 meters wide in a
200-kilometer line: a ratio of one to five thousand. Frost is a dry
granular solid with no liquid stage.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no crew, no
clone, no figure of any kind. No text, digits or symbols anywhere — no
subtitles, no title card, no watermark, no HUD, no map marking, no
grid, no reticle. 0% bloom, no glow filter, no soft focus, no haze, no
lens flare. THE FROST IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO
GAS — no liquid, no puddle, no steam condensation, no wet look
anywhere. All thrown grains obey 0.28 g. The advancing wall moves at
one constant speed and never surges. Terrain static — no melting
terrain, no warping. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain. Emphasis:
the front is one continuous straight line across the entire frame with
exactly ONE small interruption in it; no clouds, no weather, no storm
system, no other structures; not a satellite image look and no map
overlay of any kind; not miniature.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 32mm anamorphic lens,
fixed lockoff 4 kilometers above the plain, steep downward angle):
0s — The front runs edge to edge across the frame, advancing so slowly
at this scale that it is barely readable as motion.
4s — The single 40-meter notch is visible near frame centre, holding
its position in the line as the whole front moves.
7s — The notch narrows very slightly from both sides and the finger of
bare rock behind it stays dark.
10s — The front continues. Nothing else in the frame changes at all.
No cuts.

PHYSICS:
0.28 g, thin air at 1.2% pressure. Constant 13.3 m/s across the whole
length of the front. The notch closes from both sides at about 5 m/s,
which at this scale is a very slow narrowing.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no figure of
any kind. No text, digits or symbols anywhere — no subtitles, no title
card, no watermark, no HUD, no map marking, no grid, no reticle. 0%
bloom, no glow filter, no soft focus, no haze, no lens flare. THE FROST
IS A DRY GRANULAR SOLID THAT TURNS STRAIGHT TO GAS — no liquid, no wet
look anywhere. The wall moves at one constant speed and never surges.
Terrain static. No animal, no creature. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: the line stays
straight and continuous with exactly one small interruption; no clouds,
no weather, no storm; no map overlay, no satellite-image look; nothing
else moves in the frame.
```

---

## 🎬 SAHNE 13 — FİNAL: İKİ DUVARIN ARASINDA

_Duruyor. Sağında ve solunda altmış metrelik duvarlar geçiyor. Üstüne güneş vuruyor. Gemi iki yüz metre ötede ve film ona varmadan bitiyor._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  Held frame. Kapanış YOK (§15: seri held frame ile biter).
  Gemiye varış, biniş ve kalkış bu filmde hiç gösterilmez.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 13 of 14. He stands still on bare rock in full sunlight while
60-meter walls of sublimating frost pass on both sides of him.

ENVIRONMENT:
A strip of bare dark basalt 40 meters wide, dry and matte, in full low
sunlight, at 0.28 g under a thin carbon-dioxide atmosphere at 1.2% of
Earth sea-level pressure. On the LEFT and on the RIGHT, receding away
from him, two sections of the advancing wall of sublimating frost, each
60 meters high, bone-white, their faces made of needle-fine vertical
gas jets rising at 200 meters per second — they have already passed his
position and are moving on. Between them, along the strip, open air and
direct sunlight. Sky deep indigo-violet overhead, orange low on the
LEFT horizon. Roughly 200 meters ahead of him and slightly out of
focus, a bare basalt outcrop with a 16 meter three-legged matte
brick-red lander standing on it. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
A 45-year-old man, 1.78 meters tall, rangy and long-limbed, standing
still at the centre of frame, turned back toward camera, not moving.
Pale weather-cracked skin with real visible pore texture, a long narrow
nose broken once and set slightly crooked, deep-set grey eyes with
heavy creases at the outer corners, thick greying eyebrows, a two-week
salt-and-pepper beard, chapped lips. He wears a matte brick-red
exploration suit with faded off-white seam tape along both forearms and
across the chest, a scuffed dark grey hard-shell chest pack holding a
flat integrated rebreather, and heavy ribbed boots. One fully
transparent seamless visor, no tint, no coating, no mask or regulator
beneath it, his whole face clearly readable through it, catching full
direct sunlight. A narrow dark band on his right wrist shows a slow
abstract amber pulse and nothing else. His wear marks are fixed and
never move: a pale grey dust smear across the left shoulder, a scuffed
patch on the right forearm where the seam tape has lifted, and a film
of frost dust across the top edge of the visor. Both hands hang empty
at his sides. Physically accurate perspective, correct engineering
proportions — the ship must never appear miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 30 meters away,
f/8, low and square on so he stands small at frame centre with a
60-meter wall filling the frame on each side of him, physically
accurate perspective.

LIGHTING:
Full Sun phase, sun 0.4 degrees ABOVE the horizon. ⭐ Hard direct low
sunlight from the LEFT full on his visor and chest, throwing a long
defined shadow to the right across the bare rock. The two walls are
backlit and read cold white against the sky. This is the first time in
the film that a human face is in direct sunlight. Deep contrast, sharp
texture. 0% bloom, no lens flare.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The two wall sections continue at a
constant 13.3 m/s away from him and never turn back. Nothing rises from
the bare rock he is standing on. He does not move at all.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure at the ship. No text, digits or
symbols anywhere — no subtitles, no title card, no credits, no end
card, no watermark, no HUD. 0% bloom, no glow filter, no soft focus, no
haze, no lens flare. Photorealistic skin with pores and fatigue — no
airbrushing, no waxy texture, no face morphing, identical bone
structure throughout. Suit and equipment identical from first frame to
last; wear stays fixed. THE FROST IS A DRY GRANULAR SOLID THAT TURNS
STRAIGHT TO GAS — no liquid, no puddle, no wet look anywhere. All
thrown grains obey 0.28 g — never hovering, never frozen in mid-air,
never flowing like liquid. The walls move at one constant speed and
never surge, never lunge, never turn back. Terrain static. No animal,
no creature. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain. Emphasis: nothing rises from the bare rock he stands on;
the rover is gone and does not appear; his hands are empty; he does not
walk toward the ship and the ship is never reached; exactly one human
and nobody at the lander; no fire, no smoke; not miniature.
```

### 🎥 VIDEO PROMPT

```
MOTION (10 seconds, one fixed setup, no cuts — 32mm anamorphic lens,
fixed lockoff at 30 meters, low and square on):
0s — He stands still at frame centre in full direct sunlight, turned
back toward camera, the two 60-meter walls passing on either side of
him and receding.
3s — He does not move. The walls continue at 13.3 m/s; their
needle-fine jets keep rising; nothing rises from the bare rock under
his boots.
5s — He lets out one short controlled breath; the bottom edge of the
visor fogs a centimetre and clears.
7s — Nothing else happens. He does not turn toward the ship.
10s — The frame holds exactly as it is to the last frame.
No cuts.

EQUIPMENT LOCK: suit unchanged throughout — same closed transparent
visor, same chest pack, same wrist band, same dust smear on the left
shoulder, both hands empty, first frame identical to last.

PHYSICS:
0.28 g, thin air at 1.2% pressure. The two wall sections hold a
constant 13.3 m/s and recede. Nothing sublimates on the bare strip. He
is motionless except for one breath.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure at the ship. No text, digits or
symbols anywhere — no subtitles, no title card, no credits, no end
card, no watermark, no HUD. 0% bloom, no glow filter, no soft focus, no
haze, no lens flare. Photorealistic skin with pores and fatigue — no
airbrushing, no waxy texture, no face morphing. Suit and equipment
identical from first frame to last; wear stays fixed. No liquid, no wet
look anywhere. All thrown grains obey 0.28 g. The walls move at one
constant speed and never surge, never lunge, never turn back. Terrain
static. No animal, no creature. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: he does not walk, does
not turn to the ship and does not raise his hands; nothing rises from
the ground he stands on; no fade, no dissolve, no title card and no end
card at the last frame — the shot simply ends; exactly one human.
```

---

# 🎶 BÖLÜM 3 — MÜZİK PROMPTU

> `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` akışına göre: önce §17 künyesi,
> sonra §14 tempo hizalaması, §15.1 sub-bass oktav eşlikçisi, §10
> müziksiz sahne.

```
§17 KÜNYE — bu cümle yazılmadan müzik promptu yazılmaz:
"İzleyici bu novum'u, kızgın olmayan bir tehlike olarak okumalı —
 kovalayan şey bir gündoğumudur ve kimseye kızgın değildir."
→ Müzik bu yüzden tehdit değil, SAAT tonunda. Vurgu ritimde; melodi
  neredeyse yok. Cephenin kendi teması YOKTUR — cephenin müziği
  nabzın kendisidir.

§10 MÜZİKSİZ SAHNE: S12 (Overview). Tam sessizlik — yalnız boğuk ortam
     ve alçak bir uğultu. En yüksek görsel, en düşük ses.

§14 TEMPO — 10 saniyelik sahne ızgarasına hizalı (96/120/144 BPM)
⭐ EK KURAL — bu filme özel: müzik KESMEYE hizalanır.
   Vuruş, planlı kesme saniyelerine (3.0 · 4.0 · 5.0 · 7.0) düşer.
   Kesme ile vuruş çakışırsa kesme "montaj hatası" değil "ritim"
   olarak okunur. Sahne içi kesmenin en ucuz sigortası budur.
```

```
Genre: Lean, percussive electronic-orchestral score for a chase whose
pursuer is a sunrise. A clock, not a monster.

Instrumentation: A single dry low pulse — one struck damped string per
beat — running almost the whole film, never resolving, never changing
key. Close hand percussion and short bowed bass stabs for the cut
scenes (0, 4, 9, 10, 11), landing exactly on the cut points. One high
thin sustained tone with no vibrato for the macro shots of the
sublimation edge (Scenes 2 and 5). At the moment the engine is switched
off (Scene 6, at 7.5 s) every instrument drops out except the low
pulse, which continues alone through the whole silent coast (Scene 7) —
the most exposed twenty seconds in the film. One struck piano note left
to decay across the failed attempt (Scene 9). One more, harder, across
the decision (Scene 10). The pulse doubles in speed for the first and
only time as the wall collapses (Scene 11). NOTHING at all for the
Overview (Scene 12). One low sustained note that does not resolve for
the final frame (Scene 13).

Mood: Physical, dry, forward-leaning. Not frightening, not heroic. The
score never treats the front as a villain; it treats it as a schedule.

Tempo: 120 BPM through Scenes 0-5. 96 BPM through Scenes 6-9 as the
vehicle slows — the tempo drops exactly when the rover does. 120 BPM at
Scene 10. 144 BPM for Scene 11, the only fast music in the film.
Silence at Scene 12. Unmetered at Scene 13.

Low-end rule: every sub-bass element below 90 Hz is doubled by an
octave companion between 90 and 160 Hz so the low end survives phone
speakers.

Dynamic arc: hard start (0) — steady clock (1-5) — everything falling
away as the engine dies (6) — one pulse alone (7-8) — a struck note and
a refusal (9) — a harder struck note and a decision (10) — the only
acceleration in the score (11) — total silence (12) — one unresolved
note (13).

Reference feel: the dry mechanical patience of a heist countdown cue
crossed with the low physical pressure of a documentary score for
avalanche footage. No lyrics. One continuous evolving piece, roughly
2 minutes 20 seconds, mapped to the 14-scene arc above.
```

---

# 📋 BÖLÜM 4 — ÜRETİM NOTLARI

```
DURUM              ✍️ YAZILDI (04.08.2026) · ÜRETİLMEDİ
                   Plan: 140 s / 14 sahne / 26 segment / 12 kesme
                   28 prompt (14 imaj + 14 video)

⛔ ÜRETİM SIRASI — bu filmde iki kapı var

   KAPI 1 — MİMARİ TESTİ: ÖNCE S0 ÜRETİLİR. Tek başına.
      S0 iki kesme ve üç farklı ölçek taşıyor, üstelik üçüncü segmenti
      referanssız bir ayna kadrajı. Bu tek klip, kesmeyi prompta
      koymanın işe yarayıp yaramadığını söyler.
      Kabul ölçütü:
        · Kesmeler 3.0 ve 7.0 saniyede mi?
        · İkisi de SERT kesme mi — bindirme, fade, morph var mı?
        · Segment B ve C'nin kadrajı yazıldığı gibi mi?
        · Kıyafet ve araç kesmeden sonra aynı mı?
      Bunlar tutmuyorsa → §0.20 Plan B: 26 ayrı klip, kurguda kesme.
      Karar burada verilir, filmin tamamı üretildikten sonra değil.

   KAPI 2 — FİZİK TESTİ: sonra S5 ve S2 (süblimleşme makroları).
      Filmin bütün görsel iddiası bunların doğru çıkmasına bağlı.
      Kabul ölçütü: jetler İĞNE GİBİ ve DİKEY mi · hiçbir yerde sıvı,
      ıslaklık, buhar yoğuşması, alev veya duman var mı · geride kalan
      kaya kuru ve temiz mi.
      Tutmazsa film üretilmez; 22 segmentte cephe kadrajda ve başka
      hiçbir sahne bu hatayı kurtaramaz.

   Sonra kalan 11 sahne. Onaylanmamış imajdan video üretilmez.

⭐ SAYAÇ KADRAJI — üç segment aynı kurulumla
   S0-C, S4-C ve S8-B birebir aynı lens, mesafe, yükseklik ve açıyla
   yazıldı. Üçü de KESME SONRASI segmentlerdir, yani referans imajı
   yoktur. S0 onaylandıktan sonra o klibin ayna karesi dondurulup
   S4 ve S8 üretilirken referans olarak açık tutulur.
   Kadraj kayarsa filmin sayacı ölür.

PROMPT UZUNLUK KONTROLÜ — üretimden önce ölçülecek
  ⚠️ 4.300 karakter Veo'da hata veriyor (KILAVUZ_REHBERI §7).
  ⚠️ Prompt'lar SELF-CONTAINED: kıyafet, araç kartı, fizik ve negatif
     bloklar her promptta tam metin. Çok çekimli sahnelerde kadraj
     tarifi SEGMENT BAŞINA tekrarlanıyor (§0.2.1 kural ④).

🆕 BU FİLMDE İLK KEZ DENENEN BEŞ ŞEY — üretimden sonra ölçülecek
  1. 🆕 KESME PROMPTUN İÇİNDE. Depoda ilk kez. Ders 1 yasağı
     kaldırılmadı, TAKVİME çevrildi. Ölçülecek soru: kesmeler
     yazıldığı saniyede ve kadrajda mı çıkıyor?
  2. 🆕 İKİ NEGATİF ÇEKİRDEK. Tek çekimli 7 sahnede "no cuts",
     çok çekimli 7 sahnede CUT SCHEDULE. A1 çelişkisini kesme
     ekseninde kapatan ilk plan.
  3. 🆕 SÜBLİMLEŞME FİZİĞİ. Katıdan doğrudan gaza geçen bir zemin
     depoda hiç denenmedi. "no ice / no water" yasağının içinden
     don anlatmanın yolu §0.13'te yazılı.
  4. 🆕 NEREDEYSE GERÇEK ZAMAN. Önceki filmler 40 dakikalık hikâye
     zamanını 2 dakikaya sıkıştırıyordu; bu film 3.5 dakikayı
     2:20'ye sıkıştırıyor.
  5. 🆕 KESMEYE HİZALI MÜZİK (Bölüm 3). Vuruş, planlı kesme
     saniyelerine düşüyor.

⚠️ ÜRETİMDE İZLENECEK DÖRT AÇIK RİSK
  · Kesmenin geçişe dönüşmesi. Model "cut"ı bindirme veya morph
    olarak çizebilir. CUT SCHEDULE satırında beş ayrı yasak yazılı.
  · Referanssız segment. B ve C kadrajlarında kıyafet/ölçek kayması
    beklenir. Karşı önlem: segment başına tam kadraj tarifi.
  · Jet şekli. Model süblimleşmeyi DUMAN olarak çizmeye eğilimli.
    "needle-fine, vertical, never billowing, no smoke, no fire"
    her promptta yazılı.
  · Klon. S10 segment B (araçtan iniş) deponun ölçülmüş en riskli
    çekim tipi. Negatif blokta "THE SEAT IS EMPTY" vurgulu.

SONRAKİ ADIM       KILAVUZ_REHBERI §6 adım 3.5 — prompt QA (elle)
KAPAK              ✅ BÖLÜM 5'te hazır — A sürümü + Plan B + tipografi
PAKETLEME          VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
```

---

# 🖼️ BÖLÜM 5 — KAPAK FOTOĞRAFI

> **Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`
> **Ev kuralı:** kapak **metinsiz** üretilir, tipografi post'ta eklenir.

## 5.1 ✅ PALET — filmden çıkıyor, uydurulmuyor

```
Filmin paleti:  kemik beyazı (don ve duvar) + koyu bazalt + derin
                indigo-mor gökyüzü
Tek doygun kırılma: ŞAFAK TURUNCUSU — duvarın tepesindeki sert kenar
                    ve S11'de çentikten geçen doğrudan güneş ışığı

→ "Derin indigo-mor zemin üzerine sıcak turuncu" — kılavuzun başarılı
  kombinasyon listesindeki "Lacivert zemin üzerine Canlı Turuncu"nun
  bu filmdeki fiziksel olarak meşru karşılığı. 120 pikselde ayrışır.
```

## 5.2 🎯 MİKRO-HİKAYE — kapak neyi soruyor

```
ÖLÇEK       Kadrajın %70'i beyaz bir duvar — tepesi kadrajın dışında
ÖZNE        Duvarın önünde, alt sağ üçte birde, minicik bir araç
NESNE       Araçtan geriye uzanan iki tekerlek izi — nereden geldiği
BAKIŞ       İzleyicinin gözü önce duvara, sonra araca gider
DUYGU       "O şey neyin önünde kaçıyor?"

İZLEYİCİNİN SORUSU: "Bu beyaz duvar ne — ve neden ilerliyor?"
```

Kapak S0 segment B'nin tek karelik hâli ve film ilk 7 saniyede o vaadi
ödüyor → `PROMISE VS PAYLOAD: HONEST`.

## 5.3 📸 KAPAK PROMPTU — A SÜRÜMÜ (ÖNERİLEN, metinsiz)

> Başlık için **üst-sol** dörtte birlik alan boş bırakıldı.
> **Sağ alt köşe** tamamen boş — YouTube süre rozeti orayı kapatır.

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels,
16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE.
YouTube thumbnail optimized — maximum impact at 120 pixels wide.

SUBJECT — THE SHOCK, FILLS THE FRAME:
A wall of sublimating frost 60 meters high runs across the entire frame
from left to right, occupying roughly 70% of the image, its crest going
out of the top of frame. Its face is made of hundreds of needle-fine
vertical gas jets — white filaments, not cloud, not smoke, not fog.
Along its crest runs a hard warm ORANGE rim from a sun that has not yet
risen. At its base, a clean dark line where it is eating into a
bone-white frost plain.

THE SCALE ANCHOR — SMALL AND HOT:
In the LOWER RIGHT THIRD, tiny against the wall, a 3.2 meter open-frame
four-wheel rover races to the right: a skeletal matte brick-red tube
frame over a flat deck, four open mesh wheels each 0.9 meters across
throwing frost sideways, an open roll bar over a single seat with one
small human figure in a matte brick-red suit and a fully transparent
visor in it, and a small 0.5 meter vent grid at its left rear reading
dull ORANGE with hard falloff. Two thin wheel lines run back from it
across the frost toward the wall. It is no more than one twelfth of the
frame width. Physically accurate perspective, correct engineering
proportions — the rover must never appear miniature or toy-like.

LIGHTING — TWO SOURCES ONLY:
1. The wall itself as a cold WHITE key from frame left, washing the
   frost plain and rim-lighting the rover's left side.
2. A hard warm ORANGE edge along the wall's crest and a matching
   orange point at the rover's vent grid.
Sharp directional light with clear falloff. Deep shadows on the right
side of everything. 0% bloom, 0% glow filter, 0% soft focus, no lens
flare, no halo around any light source.

BACKGROUND:
Above the wall, a deep indigo-violet sky grading to pale orange at the
lower left horizon. The UPPER LEFT QUADRANT is kept clean, dark and
uncluttered — open negative space reserved for the title added later
in post.

COLOR — TWO COLORS ONLY:
- COLD WHITE and deep indigo-violet: the wall, the frost, the sky
- WARM ORANGE: the crest rim and the vent grid
No green, no purple beyond the sky, no teal, no red. Two-value
contrast: cold mass against a warm edge. Increase final saturation by
20% so the orange survives at thumbnail scale.

COMPOSITION:
- The wall occupies 70% of the frame and runs edge to edge
- The rover in the lower right third, sharply in focus
- 30% of the frame is clean negative space (upper left)
- LOWER-RIGHT CORNER completely empty — no detail of any kind

TECHNICAL:
- No text, no letters, no numbers, no digits, no logo, no watermark,
  no subtitles, no name label, no HUD, no lens data
- Exactly one human being — no second person, no crew, no figure
  standing on the plain, no reflection of another person
- Photorealistic, 35mm film grain
- Sharp focus on the rover and on the wall's base — they are the two
  sharpest things in the image
- The wall is made of needle-fine vertical jets — NOT smoke, NOT fog,
  NOT a dust storm, NOT a wave of water, NOT a cloud bank
- Nothing is on fire: no flame, no ember, no ash, no smoke
- No liquid, no wet surface, no melting, no steam condensation
- No Unreal Engine look, no CGI aesthetic, no video game aesthetic
```

## 5.4 📸 KAPAK PROMPTU — B SÜRÜMÜ (PLAN B, 48 saat kuralı)

> Kılavuz §7: yayından **48 saat** sonra CTR %4'ün altındaysa hazır
> bekleyen alternatif kapak devreye alınır. A sürümü ölçek odaklı;
> B sürümü **soru odaklı** — S11 segment B'nin kapak hâli.

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels,
16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE.
YouTube thumbnail optimized — maximum impact at 120 pixels wide.

SUBJECT — THE QUESTION:
A wall of sublimating frost 60 meters high runs across the frame from
left to right, its face made of needle-fine vertical white gas jets
with a hard warm ORANGE rim along its crest. At frame centre there is
a single clean NOTCH in it, 40 meters wide, with vertical sides — a
gap of empty air in a wall that otherwise runs unbroken to both edges
of frame. Through that notch comes a hard shaft of direct ORANGE
sunlight, lying along a strip of bare dark basalt that runs toward
camera.

THE SCALE ANCHOR:
Standing in the middle of that lit strip in the LOWER RIGHT THIRD, one
small human figure in a matte brick-red exploration suit with faded
off-white seam tape and a fully transparent visor, seen from behind,
motionless, no more than one fifteenth of the frame height. Exactly one
human being in the image. His long shadow runs toward camera.

LIGHTING:
The shaft of direct orange sunlight through the notch is the only warm
source and the only direct light; everything else is cold white off the
wall's face. Deep hard contrast between the lit strip and the unlit
frost. 0% bloom, no glow filter, no soft focus, no lens flare, no halo.

COLOR — TWO COLORS ONLY:
- COLD WHITE and deep indigo-violet: the wall and the sky
- WARM ORANGE: the shaft of sunlight and the crest rim
Increase final saturation by 20% so the orange survives at thumbnail
scale.

COMPOSITION:
- The notch at frame centre, the wall filling the rest edge to edge
- The lit strip running from the notch toward the lower right
- The small figure in the lower right third
- UPPER LEFT QUADRANT kept clean for a title added later in post
- LOWER-RIGHT CORNER completely empty of detail

TECHNICAL:
- No text, no letters, no numbers, no logo, no watermark, no HUD
- Exactly one human being — no second person, no vehicle, no crew
- Photorealistic, 35mm film grain
- The notch is EMPTY AIR with sunlight through it — not mist, not a
  tunnel, not a thinner section of wall, not a doorway
- The wall is needle-fine vertical jets — NOT smoke, NOT fog, NOT a
  wave of water, NOT a cloud bank
- Nothing is on fire: no flame, no ember, no smoke
- No liquid, no wet surface, no melting
- No Unreal Engine look, no CGI aesthetic, no video game aesthetic
```

## 5.5 ✍️ TİPOGRAFİ — post'ta eklenir, prompt'a ASLA girmez

```
KONUM        üst-sol dörtte birlik alan (her iki sürümde boş bırakıldı)
BAŞLIK       THE DAWN FRONT     — ağır grotesk, tümü büyük harf
ALT SATIR    "Burada güneş doğduğunda yer patlıyor."  — ince, %60 opaklık
RENK         kemik beyazı; turuncu ASLA kullanılmaz (tek doygun renk
             görüntüde zaten var, ikincisi onu öldürür)
ÖLÇÜ TESTİ   120 piksel genişliğe küçült — başlık hâlâ okunuyor mu
YASAK        kapak promptunun içine tek harf bile yazılmaz
```

## 5.6 ✅ ÜRETİM ÖNCESİ KAPAK KONTROLÜ

```
□ Görüntüde tek bir harf, rakam veya sembol var mı?        → varsa yeniden üret
□ Tek insan mı? Arkada ikinci figür var mı?                → varsa yeniden üret
□ Duvar DUMAN gibi mi görünüyor?                           → öyleyse yeniden üret
□ Herhangi bir yerde alev, kıvılcım, ıslaklık var mı?      → varsa yeniden üret
□ Turuncu kenar sert mi, yoksa hale mi yapmış?             → hale varsa yeniden üret
□ Üst-sol çeyrek başlık için boş mu?                       → değilse yeniden üret
□ Sağ alt köşe boş mu (süre rozeti)?                       → değilse yeniden üret
□ 120 piksele küçülttüğünde araç/figür hâlâ seçiliyor mu?
□ Kapağın vaadi filmde ödeniyor mu? (A → S0-B · B → S11-B) → PROMISE VS PAYLOAD
```

---

# THE DAWN FRONT

### _"Burada güneş doğduğunda yer patlıyor. Ve o adam onun önünde."_





