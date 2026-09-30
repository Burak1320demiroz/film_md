# 📚 FAZ 8 / TIRMANIŞ — QA DERSLERİ VE AKSİYON RAPORU (1. KOŞU)

> Koşu: 12.08.2026 · Girdi: **1 birleşik reel (~100 s) · MODE R —
> KARAR 5 ⑨'a RAĞMEN** · Rubrik: `FAZ_08_QA_PROMPT.md` · Ham çıktı:
> `../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP/THE_SECOND_SHIP_FAZ08_HAM.md`
>
> **SKOR YOK — ve bu kez bu bir BAŞARIDIR.** MAPPING COLLAPSE kapısı
> [DERS 92, F7 koşusundan sonra yazıldı] ilk sahasında çalıştı: rapor
> 6/10 çelişkiyi ilan etti, yalnız beş kategoriye puan verdi, üçüne
> UNVERIFIABLE yazdı ve **"NO SCORE" yayımladı.** F7'nin zehirli 1.9
> ortalaması tekrarlanmadı. Bu koşu bir **bulgu koşusudur**; skor
> tablosuna hiçbir satır yazılmaz.
>
> ⚠️ Üç koşu üst üste (F6 · F7 · F8) teslimat yüzünden taban üretemedi.

---

## 1. KÖK NEDEN #1 — TESLİMAT: sekizinci fazda YEDİNCİ sapma, ikinci kez sıra kaydı

KARAR 5 ⑨ mekanik kapıyı yazmıştı: `s71.mp4 … s80.mp4` boş yuva
şablonu, MODE T, kurguya ADA GÖRE alma. Yine reel gitti, yine sıra
bozuktu. **Ama bu kez karışmanın deseni okunabilir.**

| Yuva | İçerik | Kayma |
|---|---|---|
| 71 · 72 | S71 · S72 | ✅ yerinde |
| 73 · 74 · 75 | **S74 · S75 · S73** | 3'lü döngü |
| 76 · 77 | S76 · S77 | ✅ yerinde |
| 78 · 79 · 80 | **S79 · S80 · S78** | 3'lü döngü |

```
PERMÜTASYON:  71 72 · [74 75 73] · 76 77 · [79 80 78]
İki AYNI 3'lü döngü. Her üçlüde grubun İLK dosyası (s73 ve s78) sona
düşmüş, diğer ikisi birer öne kaymış. Bu, alfabetik sıralamanın DEĞİL,
DEĞİŞİKLİK TARİHİNE göre sıralamanın imzasıdır — s73 ve s78 kendi
üçlülerinin EN YENİ dosyalarıdır, yani o iki sahne komşularından SONRA
yeniden üretilmiştir.

⭐ F7'de aynı imza vardı (S62 grubun sonuna düşmüştü, "en çok yeniden
üretilen kare" olduğu için). SINIF ARTIK İKİ VAKALI VE İSPATLI:
yeniden üretilen her klip, kurguya mtime sırasıyla alındığında kendi
grubunun SONUNA düşer.

DOĞRULAMA (operatör, 10 saniye):  ls -lT <üretim klasörü>/s7*.mp4
  → s73 ve s78 en yeni tarihliyse kök neden kesinleşir.
```

**Bedeli:** on kategoriden BEŞİ (EVENT DELIVERY · IDENTITY · COSTUME ·
CAMERA · PHASE CHAIN) ölçülemedi. S73'ün ÇEHOV 4 ateşlemesi, S75'in
konuşma penceresi ve S80'in ÇEHOV 7'si kendi satırlarına karşı hiç
denetlenmedi — yalnız içerik çapasıyla dolaylı okundu.

---

## 2. İÇERİK ÇAPASI — bulgular gerçek sahneye göre yeniden yazıldı

Rapor her segmentin içeriğini tarif etti; eşleme tektir ve şüphesizdir
(üç ışık durumu ayırt ediciydi — CLIP MAP'e eklenen "gözlenen ışık
durumu" sütunu bu koşuda tam olarak bunun için işe yaradı).

**Aşağıdaki tüm bulgular GERÇEK sahne numarasına göre yazılmıştır.**
Rapordaki yuva numaraları ham dosyada durur.

---

## 3. ⛔ KİLİT ÇELİŞKİSİ DEFTERİ [AGENTS.md C/D/E ortak adım ②]

> Planda YAZILI bir kilide aykırı her bulgu buraya alınır. Çözüm eylemi
> master'ın o saniyesini izlemektir (~10 sn iş). ⬜ AÇIK madde varken o
> bulgudan **global ders yazılmaz ve yeniden üretim siparişi verilmez.**

| # | Rapor ne dedi | Hangi kilit | Çözüm eylemi | Sonuç |
|---|---|---|---|---|
| 1 | S77'de mühürlü eldivende **5 hane** | GLOVE DIGIT LAW · dört hane | Master 1:00–1:10 · figür 13–18 m'de; hane sayılabiliyor mu? | ⬜ AÇIK |
| 2 | S80'de **sol el de çıplak** | ONE-SEAL LAW · tek mühür | Master 1:20–1:30 · halkayı çeviren elde eldiven var mı? | ⬜ AÇIK |
| 3 | S71'de kamera **pan yapıyor** | S71 = fixed lockoff | Master 0:00–0:10 · kadraj kayıyor mu? | ⬜ AÇIK |
| 4 | S71'de kadının izi **sağ yanakta** | SEPARATION LOCK · sol kaşın kılı | Master 0:00–0:10 · tek kare dondur, ize bak | ⬜ AÇIK |
| 5 | S75'te adam **4s'de konuşuyor** | SPEECH LOCK · ~9s penceresi | Master 0:30–0:40 · dudak ne zaman kıpırdıyor | ⬜ AÇIK |
| 6 | S76 konsolunda **"60" · "3w"** | TEXT · mutlak yasak | Master 0:50–1:00 · sol panele bak | ⬜ AÇIK |
| 7 | S78'de gökte **ikinci nesne + iz** | tek nesne · kuyruksuz | Master 1:30–1:40 · gökyüzüne bak | ⬜ AÇIK |
| 8 | S72'de turuncu figür **hiç yok** | S72 satırı · 0–2s'de var | Master 0:10–0:20 · ilk iki saniye | ⬜ AÇIK |

⚠️ **Madde 1 özel:** rubrik "figür bu ölçekte çözülemiyorsa *not
resolvable at this scale* yaz, tahmin etme" diyordu; rapor bu kaçışı
KULLANMADI ve 32mm'de 13 m mesafeden kesin sayı verdi. Sınıf yedi
vakada yedi kez battığı için bulgu inandırıcıdır, ama **rapor tek
başına bunu kanıtlayamaz.** Aynı rapor S77 vizörünü PASS verdi — yani
aynı figürü hem çözebilmiş hem çözememiş olamaz; ikisinden biri
tahmindir.

---

## 4. KÖK NEDEN #2 — ÜRETİM: dersler (numaralar F7'den devam)

### D-AX 🔴 PAN YASAĞI FAZIN HİÇBİR PROMPTUNDA YOK — depo kanıtlı boşluk

S71 bir lockoff sahnesidir ve rapor kameranın figürleri takip ettiğini
söylüyor. Bulgu ⬜ AÇIK, **ama promptun boşluğu açık değil — kanıtlı:**

```
grep -c "no pan" FAZ_08_TIRMANIS.md
→ 2 — ve ikisi de "no pane" (S74'ün deliği: "no glass, no pane").
  KAMERA anlamında "no pan" fazda SIFIR KEZ geçiyor.

On sahnenin kamera negatifi şunları yasaklıyor:
  no cuts · no transitions · no shake · no zoom · no push-in
  · no zoom snap · no speed change
PAN hiçbirinde yok. Kamera kilidi sekiz fazdır eksik yazılıyor ve bu
ilk kez saha bulgusuna dönüştü.
```

```
YAMA — on sahnenin de kamera negatifine, tek dize:
  no pan, no tilt, no camera rotation of any kind, no reframing to
  follow a subject
S72 (yanal takip) ve dört hareketli sahne için:
  ...beyond the single move described above.
```

⚠️ F9 S87'de aynı yasak YAZILI ("no pan following the ship") ve orada
da battı → sınıf iki katmanlı: eksik yazım (F8) + yazıldığı hâlde
tutmama (F9). Plan katmanı çözümü D-BJ'de (F9 dosyası).

### D-AY 🔴 YARA İZİ: DÖRDÜNCÜ FAZ, VE İLK KEZ ÇAPRAZ BULAŞMA

F7 D-AP'nin yaması S71'e eksiksiz yazıldı — özellik + ölçü + "yüzün
geri kalanı işaretsiz":

```
"a 2 cm white line splitting THE HAIR OF HER LEFT EYEBROW"
"her scar stays IN her LEFT brow hair ... with no mark anywhere else
 on either face"
```

Rapor kadının izini **SAĞ YANAKTA** gördü — yani izin gittiği yer,
aynı karedeki ADAMIN iz konumu (sağ elmacık kemiği). Bu artık bir
TARAF hatası değil, **iki pasaport arasında çapraz bulaşma**.

```
DERS ADAYI [→ ⬜ AÇIK madde 4'e bağlı]: iki yüz aynı karedeyken
işaretler pasaportlar arasında GEÇİŞ yapıyor. Tarif kilidi (özellik +
ölçü + "başka iz yok") üç fazdır ölçülebilir şekilde işe yaramadı.

Çözüm artık PROMPT KATMANINDA DEĞİL:
  · S71 iki ayrı render + kompozit olarak üretilir (F9 KARAR 1'in
    imza çekim için ayırdığı yedek plan, iki-yüz karesine de uygulanır)
  · ya da onaylı R1/R2 yüz kareleri start-frame verilir ve tek kare
    insan gözüyle taranır [KARAR 5 ⑤ üretim öncesi kapısı — bu
    koşuda uygulanmadığı anlaşılıyor]
```

### D-AZ 🔴 KADRAJ KENARINDA DOĞUP ÖLEN BEAT ÜRETİLMİYOR

S72'nin ilk beat'i: sağ kenarda, sırtı dönük, yarı kadraj dışında bir
turuncu figür — 2s'de kayıp gidiyor ve bir daha gelmiyor. Rapor figürü
**hiç görmedi.**

```
Sınıf: F7 D-AN'nin (2-3 mm zemin kabarması hiç üretilmedi) kadraj-kenarı
versiyonu. Model, kadrajın kenarında yarım görünen ve kısa yaşayan bir
özneyi "gürültü" sayıp atıyor.

ÇÖZÜM — beat prompttan çıkar, START FRAME'e taşınır:
S72 zaten END FRAME imajı alıyor; START FRAME imajı da alır ve o imaj
turuncu figürü sağ kenarda YARI KADRAJDA içerir. Video promptu artık
figürü YARATMAZ, sadece ÇIKARIR:
  "the orange figure already at the right edge leaves frame by 2s and
   never returns"
```

### D-BA 🔴 METİN: ÜÇ NEGASYON BİR KONSOLU DURDURAMADI

S76'nın promptunda metin yasağı **üç ayrı yerde** yazılı (IMAGE
NEGATIVE + VIDEO gövde + VIDEO kapanış). Rapor sol panelde okunabilir
rakamlar gördü: "60", "3w".

```
DERS ADAYI [→ ⬜ AÇIK madde 6'ya bağlı]: bir yüzeyin metinsiz kalması
NEGASYON SAYISIYLA sağlanamıyor. Model "yuvalı konsol paneli" önselini
çiziyor ve yasak listesi o önseli iptal etmiyor.

POZİTİF SAYISAL KİLİT [AGENTS.md §8 · tarif değil sayı]:
  "The panel around the socket carries EXACTLY SIX oval segments of
   flat colour, each 8 mm across, arranged in one straight row, and
   NOTHING ELSE: the rest of the panel is bare matte metal."
Yasak listesi kalır; ama artık yüzeyin ne OLDUĞU sayıyla yazılıdır.
```

⭐ Rubriğin TEXT LEDGER'ı bu bulguyu üretti. Sahne sahne "evet/hayır"
sorulmasaydı, genel izlenimde kaçardı.

### D-BB 🔴 DÖRT HANE — SEKİZİNCİ VAKA (⬜ AÇIK)

Rapor S77'de 5 hane saydı. Sınıf F1'den beri ölçülen her koşuda battı.
KARAR 5 ③ üretim kapısını yazmıştı: "R3 BEKÇİ MASTER'da parmak SAYILDI
mı · onaylı el karesi start-frame". Kapının uygulanmadığı anlaşılıyor.

```
⛔ AKSİYON KAPININ KENDİSİNDE, bulgunun doğrulanmasını BEKLEMEZ:
S77 ve F9'un üç Bekçi sahnesi (S85 S86 S90) onaylı R3 EL karesi
start-frame verilmeden üretilmez. Prompt cümlesi bu sınıfı sekiz
vakada bir kez bile kurtarmadı.
```

### D-BC 🟡 SANTİMETRİK OLAY DA ÜRETİLMİYOR — eşik artık ölçülü

S80'de eldiven yere düşüyor ve **bir kez ~1 cm sekmesi** gerekiyor.
Rapor: düştü, durdu, sekmedi.

```
SINIF İKİ VAKALI:
  F7 S68 · 2–3 mm zemin kabarması → hiç üretilmedi [D-AN]
  F8 S80 · 1 cm sekme            → hiç üretilmedi [bu ders]

F8 KARAR 5 ④ "sayı korunur, OKUNURLUK KANCASI eklenir" demişti;
kanca S80 promptuna YAZILMADI (grep: "bounces once about a centimeter"
dışında hiçbir okunurluk desteği yok).

DERS ADAYI: ~2 cm'in altındaki tek seferlik hareket beat'i bu modelde
ÜRETİLMİYOR. Üç seçenek var, dördüncüsü yok:
  ① ölçeği büyüt (1 cm → 4-5 cm sekme; 100mm makro kadrajda hâlâ
     ölçülü görünür)
  ② beat'i kaldır (eldiven düşer ve durur — sekme dramatik yük
     taşımıyor)
  ③ kurguda çöz (ses tasarımı sekmeyi zaten veriyor)
```

### D-BD 🔴 ZAMAN KİLİDİ ("X. saniyeden önce olmasın") TUTMUYOR

S75'in konuşma kilidi saniyeye bağlanmıştı — F7 D-AR'nin yaması buydu:

```
"His mouth is NEVER visible while he speaks: it stays closed for the
 first nine seconds, and the reply only begins after his head has
 turned three quarters away."
```

Rapor: 4s'de konuşuyor, ağız hattı okunuyor. Kilit hem saniyeyi hem
baş yönünü kaybetti.

```
DERS ADAYI [→ ⬜ AÇIK madde 5'e bağlı]: on saniyelik tek çekimde
"şu saniyeden önce OLMASIN" biçimindeki negatif zaman kilitleri
tutmuyor. Model olayı sahnenin ortasına yayıyor.

⭐ BU BİR PROMPT SORUNU DEĞİL, PLAN SORUNU [AGENTS.md §8]:
S75'te KONUŞAN KİŞİ ZATEN KADRAJDA DEĞİL. Sahnenin işi dinlemek.
Cevabın görüntüde başlamasına hiç gerek yok — replik post'ta, bir
sonraki sahnenin üstüne binebilir.
  → S75'in son beat'i (9s: cevap başlar) SİLİNİR.
  → Sahne baştan sona kapalı ağızlı bir dinleme sahnesi olur.
  → Konuşma penceresi sayısı bu fazda BİRDEN SIFIRA iner ve fazın
    en kırılgan kilidi tamamen ortadan kalkar.
```

### D-BE 🔴 TEK MÜHÜR YAYILDI: çıplaklık ELLERE GENELLENDİ (⬜ AÇIK)

ONE-SEAL LAW'ın ilk saha testi. F7'de model hedef değiştirmişti (eldiven
yerine kask); burada hedef doğru ama **kapsam yayıldı**: rapor sol elin
de çıplak olduğunu söylüyor.

```
S80'in promptu şunu diyor:
  "EXACTLY ONE SEAL OPENS IN THIS SHOT AND IT IS THE RIGHT WRIST RING:
   no helmet, collar ring or second glove is touched, opened or
   removed at any second"
Cümle SOL ELDİVENİN ÇIKARILMASINI yasaklıyor — ama sol elin
ELDİVENLİ OLDUĞUNU hiç söylemiyor. Model eldiveni çıkarmadı;
sahneye baştan eldivensiz bir sol el çizdi. Yasak ihlal edilmedi,
ATLANDI.

YAMA — pozitif durum cümlesi, IMAGE + VIDEO SUBJECT'e:
  "Her LEFT hand is GLOVED throughout: a dark grey-blue pressure
   glove with a worn ORANGE cuff panel, sealed at the wrist, covering
   every finger. No skin of the left hand is visible at any second."
```

⭐ Bu, D-BA ile aynı kök: **negasyon bir durumu kurmaz, sadece bir
değişimi yasaklar.** Modelin baştan yanlış kurduğu durumu ancak pozitif
tarif düzeltir.

### D-BF 🔴 BİÇİM VERİLEN GÖK NESNESİ KUYRUK TAKIYOR (⬜ AÇIK)

F7 S70'te gökteki şey bir NOKTAYDI ve o koşuda sınıf tertemiz geçti
(F7 raporunun WHAT WORKED'ünde yazılı: kuyruk yok, alev yok, iz yok,
ikinci nesne yok). F8 S78'de aynı şey artık "elongated hull shape" —
ve rapor hem iz hem ikinci nesne bildiriyor.

```
DEĞİŞEN TEK ŞEY: nesneye BİÇİM verilmesi.
  nokta   → temiz (F7 S70)
  gövde   → kuyruk + ikinci nesne (F8 S78)
F9'da aynı sınıf üç sahnede daha battı (S82 · S87 alev, S88 ikinci
gemi) → sınıf toplam DÖRT VAKALI. Ortak ders F9 dosyasında D-BK.
```

---

## 5. TUTAN TARAF — bu koşunun gerçek kazanımları

| Ne | Kanıt |
|---|---|
| **MAPPING COLLAPSE KAPISI [DERS 92]** | İlk sahada çalıştı: 6/10 çelişki ilan edildi, yalnız 1·2·3·7·9 puanlandı, 4·8·10 UNVERIFIABLE yazıldı, **NO SCORE yayımlandı.** F7'nin zehirli ortalaması tekrarlanmadı. Bu, F7 koşusunun tek somut çıktısıydı ve bir fazda geri ödedi. |
| **İÇERİK ÇELİŞKİ KURALI** | Altı segmentin altısı da yakalandı ve hangi satıra benzediği yazıldı. Kayma iki temiz 3'lü döngü olarak okunabildi — kök neden (mtime sıralaması) bu sayede ikinci kez ispatlandı. |
| **IŞIK DURUMU SÜTUNU** (F8'de eklendi) | Üç ışık durumu eşlemeyi tek bakışta çözdü; "beyaz kule içi" damgası taşıyan bir segmentin dış sahne satırına düştüğü anında görüldü. Yeni rubriğin en ucuz ve en verimli eklentisi. |
| **DOLU VİZÖR — D-AL YAMASI GENİŞ KADRAJDA TUTTU** | Raporun WHAT WORKED'ü: "The S77 visor plate remained flush, dark, and non-reflective **even in a wide frame**." F7'de plaka tam olarak geniş kadrajda cama dönmüştü; "THE DARKEST VALUE IN THE FRAME" dili ilk denemede geçti. ⚠️ Aynı rapor aynı figürde hane sayamamış olabilir → defter madde 1. |
| **KOPYA MALZEME DİLİ 10/10** | Dört sahnede (S72 S73 S74 S76) tek tonlu mat kemik grisi; sıfır renk sızması, sıfır işaret, sıfır ışıma. KARAR 3'ün "biçim var, renk yok" dili cansız nesnede tamamen tuttu. ⚠️ F9'da aynı dil GİYSİLİ BEDENDE battı (D-BH). |
| **DURAĞAN DÜNYA** | Zemin kotası kapalı kuralı on segmentte de tuttu; S74'te kabuk dokunuşa cevap vermedi — fazın çapa beat'i doğru çalıştı. Girdap 8→11 hızlanması görüntüye hiç sızmadı [KARAR 2]. |
| **TEXT LEDGER** | İlk koşuda karşılığını verdi: S76'daki iki rakam sahne sahne sorulan bir tabloyla yakalandı. |

---

## 6. RUBRİĞİN BATAN TARAFI → YAMALANACAK

```
① LEDGER SATIRLARI HÂLÂ YUVA NUMARASIYLA YAZILDI
   F7 D-AU'nun kapanış notu "sonraki faz rubriğinde ledger satırlarına
   İÇERİK sütunu eklenmeli" diyordu. F8 rubriğinde sütun yalnız CLIP
   MAP'e eklendi; SEAL & SKIN, STATIC WORLD, TEXT, LIGHT ledger'ları
   yuva numarasıyla yazıldı ve içerik parantez içinde kaldı. Kayma
   altında bu tablolar okunamıyor.
   → YAMA: her ledger'ın ilk sütunu "SLOT / CONTENT" ikilisi olur.

② MAPPING COLLAPSE KAPISI FAZLA GENİŞ KESİYOR
   Kapı 4·8·10'u komple UNVERIFIABLE yaptı. Oysa S71 S72 S76 S77
   YERİNDEYDİ — S71'in pan bulgusu ve S72'nin eksik figürü gerçek
   kamera/olay bulgularıdır ve puanlanabilirdi.
   → YAMA: "score only 1,2,3,7,9" yerine → "kayan segmentler için
     UNVERIFIABLE; YERİNDE KALAN segmentler üzerinden kısmi puan,
     paydası yazılarak (örn. CAMERA 6/10 · 4 segment üzerinden)".

③ COPY-MATERIAL LEDGER KENDİ HARİTASIYLA ÇELİŞTİ
   Harita "yuva 74 = S75 içeriği" diyor; ledger aynı satırda "shows
   S73 component" yazıyor. Rapor içi tutarsızlık.
   → YAMA: ledger satırlarının içerik etiketi SEGMENT MAP'ten
     kopyalanır, yeniden türetilmez.

④ "SEKMEDİ" YANLIŞ LEDGER'A YAZILDI
   Eldivenin sekmemesi STATIC WORLD LEDGER'a "otonom hareket: YES"
   olarak girdi ve kategori 3'ü 9'a düşürdü. Sekmeme bir dünya
   hareketi değil, bir DÜŞEN NESNE FİZİĞİ olayıdır.
   → YAMA: ledger'a ayrı satır: "OBJECT PHYSICS (S80): fell / landed /
     bounced once / rested — yes-no each".
```

---

## 7. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ ⛔ MASTER TARAMASI (8 madde · ~2 dakika) — §3 defteri
     Sekiz ⬜ AÇIK maddenin sekizi de tek bir izlemede kapanır.
     Bu yapılmadan: yeniden üretim siparişi VERİLMEZ, global ders
     YAZILMAZ. [AGENTS.md C/D/E ortak adım ②]

2. □ DOSYA SIRASI KAPISI — artık kök nedeni bilinen bir hata
     a) ls -lT ile s73/s78'in en yeni olduğunu doğrula (10 sn)
     b) NLE'ye alma kuralı: ASLA "değişiklik tarihi", HER ZAMAN "ad"
     c) kurgudan sonra 10 başlıklı içerik kontrolü — üç ışık durumu
        bunu 30 saniyeye indiriyor
     ⚠️ Bu, sekiz fazda yedinci sapma. Yazılı kural yedi kez tutmadı.

3. □ PROMPT YAMALARI — sırayla (hepsi ⬜ AÇIK'tan bağımsız, çünkü
     ikisi depo kanıtlı boşluk, biri kapı):
     a) ON SAHNEYE PAN YASAĞI [D-AX] — depo kanıtlı, hemen
     b) S80'e SOL ELDİVEN POZİTİF CÜMLESİ [D-BE] — depo kanıtlı
     c) S76'ya POZİTİF SEGMENT SAYIMI [D-BA]
     d) S72'ye START FRAME imajı + "çıkarır, yaratmaz" dili [D-AZ]
     e) S75'in son beat'i SİLİNİR — konuşma penceresi kapanır [D-BD]
     f) S80'in sekmesi 4-5 cm'e çıkarılır ya da kaldırılır [D-BC]
     g) S71 iki ayrı render + kompozit yoluna alınır [D-AY]

4. □ ⛔ TETİK KAPISI [D-BB]: R3 BEKÇİ MASTER'da parmak SAYILMADAN
     S77 yeniden üretilmez. Onaylı el karesi start-frame ZORUNLU.
     Aynı kapı F9'un S85 · S86 · S90'ı için de geçerlidir.

5. □ RUBRİK YAMALARI [§6 ① ② ③ ④] — 2. koşudan önce.

6. □ 2. KOŞU: MODE T, 10 ayrı dosya. Bu faz henüz TABAN ÜRETMEDİ.
```

---

## 8. FLAGS — dokümandan/operatörden cevaplanacak

```
· Raporun sorusu: "S77 için 4 haneyi ezen global bir 5-parmak anatomi
  kısıtı uygulandı mı?" → REFERANS_PAKETI'ndeki R3 plakasının kendisi
  kaç haneli? Sekiz vakalık sınıfın kaynağı prompt değil REFERANS
  olabilir; bu hiç kontrol edilmedi.
· s73 ve s78 komşularından sonra mı yeniden üretildi? (mtime)
· S71 tek render'da mı üretildi, kompozit mi? (D-AY'nin çözümü buna
  bağlı)
· S76'nın konsol imajı hangi referanstan geldi — referans karede rakam
  var mıydı?
```

---

## 9. F9+ VE SİSTEME TAŞINANLAR

> ⛔ Global DERS numarası (100+) HENÜZ AÇILMADI: §3'teki sekiz madde
> ⬜ AÇIK. Master taraması sonrası aşağıdaki üç aday LESSONS_LEARNED'a
> yazılır. F9'un koşusu aynı sınıfların üçünü de bağımsız olarak
> tekrarladı — bu, adayları güçlendiriyor ama doğrulamanın yerine
> geçmiyor.

```
ADAY DERS 100 · NEGASYON DURUM KURMAZ, SADECE DEĞİŞİM YASAKLAR
  [D-BA · D-BE · F9 D-BG]  Model bir durumu BAŞTAN yanlış kurduğunda
  yasak listesi devreye girmiyor: "eldiveni çıkarma" cümlesi baştan
  eldivensiz çizilmiş bir eli engellemiyor; "metin yok" cümlesi baştan
  rakamla çizilmiş bir paneli engellemiyor. Yasak KALIR, ama yanına
  pozitif ve SAYISAL durum tarifi yazılır.

ADAY DERS 101 · ~2 CM ALTINDAKİ HAREKET BEAT'İ ÜRETİLMEZ
  [F7 D-AN 2-3 mm · F8 D-BC 1 cm]  İki vaka, iki kez sıfır. Ölçeği
  büyüt, beat'i kaldır ya da kurguya devret — dördüncü seçenek yok.

ADAY DERS 102 · BİÇİM VERİLEN UÇAN NESNE KUYRUK/EGZOZ/İKİNCİ NESNE ÜRETİR
  [F8 D-BF · F9 D-BK]  Nokta güvenli, gövde güvensiz. Dört vaka.

⭐ KAMERA KİLİDİ (D-AX) DEPO KANITLI OLDUĞU İÇİN BEKLEMEZ:
  "no pan / no tilt / no camera rotation" negatif çekirdeğe girmeli.
  grep -rl "no camera teleportation" --include="*.md" .
  → çekirdeği taşıyan 9 dosyanın hepsine aynı dize eklenir
  [AGENTS.md kart G madde 4].
```
