# 🛰️ THE QUIET IMPACT — Sessiz Çarpışma

Dikey YouTube Shorts / Reels Production Document
Format: **9:16 (DİKEY)** | Sahne: 6 (Hook + 5 Ana Sahne) | Süre: Her sahne 8 saniye, toplam 48 saniye
Prompt yapısı: Her sahne için **1 görsel promptu + 1 video promptu** (tek versiyon, T2V)
Kaynak: **özgün konsept** — kaynak film yok
Zaman ve yer: **Vakum · alçak yörünge**, pas kahvesi bir gezegenin gece tarafı (promptlarda yer adı geçmez)
_"İki gemi yürüme hızında çarpıştı. Kimse duymadı."_

---

## 🎯 BU SHORTS'UN TEK İŞİ

Kullanıcı talebi: **bol aksiyonlu, uzayda iki geminin çarpışması ve sonraki
sessizlik.** Bu dosya talebi küçültmüyor — **aksiyonu modelin gerçekten
çizebildiği kanala taşıyor.** Depoda ölçülmüş gerçek şu: bu sistemin en
düşük tek skoru (Parçacık 2/10, Low Power) ve en düşük çevre skorlarından
biri (Kaleida 4.5/10, "patlama boyama gibi duruyor") aynı malzemeden geldi
— **ateş, duman, patlama.** Aynı kadranda taş kadar sağlam duran şey ise
büyük katı gövdedir.

```
KLASİK "UZAY ÇARPIŞMASI"              BU FİLM
─────────────────────────────         ─────────────────────────────
ateş topu, saniyelerce yanan alev  →  ATEŞ 1,0 SANİYE. Sonra yok. Oksijen yok.
gövde paramparça, enkaz bulutu     →  SERBEST KALAN NESNE SAYISI: TAM 6 panel
kamera sarsılıyor                  →  kamera gövdeye vidalı — 6/6 sahnede sıfır sarsıntı
ışık hızında bir kaza              →  temas hızı 12 m/s: koşan bir insanın hızı
gürültü                            →  vakum. Tek ses, botların altından gelen.
```

Filmin bütün aksiyonu **iki büyük katı gövdenin birbirine değmesinde**:
160 metrelik ölü bir tanker, 240 metrelik bir yük gemisinin burnuna oturur;
sekiz ezilme silindirinden yapılmış 12 metrelik tampon halkası 1,5 saniyede
3 metreye çöker; tam 6 gövde paneli düz çizgilerde uzaklaşır; ve **her şey
biter.** Geriye kalan 8 saniye filmin asıl vaadidir: sessizlik.

> ⚠️ **İKİ BİLİNÇLİ SAPMA — dürüst kayıt (SHORTS_SISTEM_PROMPTU §2).**
>
> **① "Fiziksel imkansızlık = kanca" (DNA 3).** Bu filmde imkansızlık YOK.
> Novum **algısal**: göz "dev cisim = hızlı ve gürültülü" diye okur, ekranda
> yürüme hızında ve sessiz bir çarpışma görür. Seride ilk kez novum
> tamamen gerçek fiziktir. Bu, Ders 73/76'nın doğrudan sonucudur —
> **taşıyıcı birincil, çizilebilir bir nesnedir (iki gövde)**, türetilmiş
> fenomen ya da yokluk değil. Wrong Shadow gölgeye, Starless Circle yokluğa
> yüklendi; ikisi de ekrana hiç girmedi.
>
> **② "Tehlike yoktur, huşu vardır" (DNA 5).** Bu filmde tehlike var.
> Karşılığı: **panik yok, kaçış yok, çığlık yok.** Karakter bir mühendis
> gibi davranır — bakar, sayar, karar verir, kaldıracı çeker, çarpmayı
> bekler. Depoda aksiyon kulvarı zaten var (Dawn Front, Stone Sky);
> dikey hatta ilk kez giriyor.

**RİSK SAYIMI: 4 / 9** — kask (Kart 3) · ikinci figür (Kart 4, her filmde) ·
sayaç (Kart 5, **metinsiz/çevresel**) · parçacık-patlama (Kart 6).
Su yok · canlı yok · diyalog yok · katmanlı dünya yok · kamera 6 sahnenin
5'inde tamamen sabit.

> 🚨 **DÜRÜST KAYIT [THE LOW MOON · THE WRONG SHADOW emsali]: bu filmin
> gerçek 1 numaralı riski kartlarda yok — İKİ BÜYÜK GÖVDENİN KATI-CİSİM
> TEMASI.** Ders 17 (nesneler birbirinden geçiyor) bu depoda en düşük fizik
> skorunun kaynağı; Ders 38 (model "hasarlı"yı "parçalanmış" okuyor) gemi
> ölçek kilidini de beraberinde çökertti. Karşı önlem tarif değil sayıdır:
> ezilme mesafesi 9 m (12 m → 3 m) · ezilme süresi 1,5 sn · serbest kalan
> nesne TAM 6 · ateş süresi 1,0 sn · gövde bütünlüğü "damaged" sıfatıyla
> DEĞİL, sağlam kalan yüzeylerin sayımıyla yazılır.

---

## ⚠️ Genel Prodüksiyon Kuralları

1. **SIFIR KESME** — Her video 8 saniyelik, kesintisiz tek çekim. Her sahne
   AYRI üretilir. **Çekim başına TEK sürekli hareket** ve bu filmde 6
   sahnenin **5'i tamamen sabittir (lockoff)**; yalnız S5 pull-back taşır.
   [Ders 1 · Kart 8 — deponun ölçülmüş tek çözülmüş kategorisi]
2. **DİKEY SADAKAT (9:16) + GÜVENLİ ALAN** — Karakter **her karede alt
   1/4'ün dışında**. 1080×1920 karede alt 484 px platform arayüzüyle kapalı;
   `y=1436`'nın altı görünmez. Bkz. **📱 GÜVENLİ ALAN HARİTASI**.

   > **Bu konseptin dikeyde olmasının sebebi:** Filmin ekseni **yukarıdır**
   > ve bu kez yukarısı dolmaktadır. Karakter ayaklarını bastığı metal
   > düzlükle birlikte alt 1/3'te durur; üst 2/3 önce yıldız alanı ve
   > gezegen kavsi, sonra sırayla 1/5 → 1/4 → 1/2 → 3/4 → **hepsi** gövdedir.
   > 16:9'da bir silindir yandan geçer ve "gemi" olur; 9:16'da aynı silindir
   > **tavana dönüşür.** THE HALF SKY'ın tam tersi: orada yukarı bakınca
   > hiçbir şey yoktu, burada yukarı bakınca 160 metre var.
3. **İKİ LENS KİLİDİ — HEPSİ KÜRESEL** — Geniş/ölçek: **32mm** (S0, S2, S3,
   S4, S5). Yakın/duygusal: **75mm** (yalnız S1). ⚠️ **Anamorfik lens ve
   yatay parlama YASAK** — vakumda atmosferik saçılma yoktur
   (`KILAVUZ_REHBERI` §3.1). Kamera mesafesi ve yüksekliği her promptta
   **metre** olarak yazılır.

   > **Filmde TEK yakın plan vardır (S1).** Bilinçli karar: yüzü son kez
   > okuyabildiğimiz kare, gökyüzü kapanmadan önceki karedir.
4. **GÖSTER, ANLATMA** — Yönetmen notu yok. Hiçbir promptta "nefes kesici",
   "izleyici anlar", "dramatik" geçmez. Ölçek sayıyla gelir: panel 2,0 m,
   kuşak arası 24 m, insan 1,68 m.
5. **RENK DİLİ** — **Pas kahvesi gezegen ışığı + soğuk beyaz lamba havuzları
   (kenarları jilet keskin) + vakum mavi-siyahı ve yoğun yıldız alanı +
   grafit gri suit + tankerin üç sönük kırmızı bekleme feneri + güvenlik
   sarısı tek kaldıraç.**

   > ⚠️ **Palet çakışma denetimi — dürüst kayıt.** Vakum + keskin gölge
   > fiziği THE HALF SKY ile aynıdır (aynı ortam kartı, kaçınılmaz). İki
   > ayırt edici karar var: **(a)** Half Sky'ın kadranının çoğunluğu
   > **sinyal yokluğudur** (0 IRE); bu filmin kadranının çoğunluğu **ışık
   > alan metaldir** — dominant yüzey pas kahvesiyle yıkanmış gövde
   > kaplaması. **(b)** Half Sky'ın tek doygun rengi oksit kırmızısı
   > suittir; burada suit **grafit gri**, yani kadranın en nötr nesnesi, ve
   > tek doygun renk kadranın %1'inden azını kaplayan **güvenlik sarısı
   > kaldıraçtır** — filmin tek seçiminin rengi. Amber/altın bu filmde
   > hiç yok. Diğer paletler: Wrong Shadow (kireç beyazı/haki/gölge grisi) ·
   > Sinking Hour (gül-bej/is siyahı/çivit) · Slow Stone (bazalt/kemik
   > beyazı/hardal) · Nine Minutes (metan mavi-beyazı/bakır turuncusu) ·
   > Walking Day (pirinç altını/petrol siyahı/jade).
6. **KARAKTER SADAKATİ** — 6 görsel promptunun **6'sında da** aynı karakter
   bloğu birebir, kısaltmasız tekrarlanır. Köşeli parantez referansı
   kullanılmaz [Ders 45]. Kask 6/6 kapalı; vizör **optik olarak berrak**,
   sırt silueti **düz** — ikisi de negatif çekirdeğe pozitif cümleyle
   girer [Ders 79].
7. **VİRAL ZAMANLAMA (Hook)** — 0-2sn merak (grafit gri bir figür, 26 metre
   genişliğinde ışıklı bir metal düzlükte tek başına duruyor; gezegen kavsi
   sol üstte) → 2-5sn ipuçları (sol üstte, pas rengi gezegenin önünde ÜÇ
   KIRMIZI IŞIK; yıldızlar arasında değil, bir siluetin üstünde) → 5-7sn tam
   reveal (üç ışık tek bir gövdenin üstünde: 160 metrelik bir silindir
   gezegenin önünden geçmiyor — **büyüyor**) → 7-8sn tek güçlü görüntü
   (figür başını kaldırmış, gövde yıldız alanının beşte birini kapatmış,
   hiçbir itki alevi yok — o şey manevra yapmıyor).
8. **TEK VİDEO PROMPTU** — Her sahnenin tek video promptu vardır ve T2V
   olarak yazılmıştır. Referans görselden üretim (I2V) yapacaksan: promptun
   başındaki teknik satırı ve `At 0s` beat'ini sil, yerine
   `"The scene begins exactly as the provided image."` yaz, kalan beat'leri
   düz nesre çevir. Karakteri/ortamı asla yeniden tarif etme.
9. **ELLER 5/6 BOŞ — TEK SAPMA S3'TE VE FİLMİN BEDELİDİR** — Hiçbir sahnede
   elde taşınan alet, cihaz, çanta yok; **halat/tether de yok** [Ders 26
   riski konseptten çıkarıldı — botlar manyetik]. Tek istisna: S3'te iki
   eldivenli el **gövdeye sabit** bir kaldıracı kavrar. Kaldıraç taşınmaz,
   sökülmez, kadraja elde girmez. Sapma bilinçlidir, gizlenmemiştir ve
   kontrol listesinde işaretlenmemiş kutu olarak durur [THE SLOW STONE
   emsali].
10. **⛔ EKRANDA METİN SÜRESİ = 0,0 SANİYE [Ders 61]** — 6 sahnenin 6'sı
    canlı çekimdir. **Her iki gövdede de hiçbir yazı, rakam, seri numarası,
    bayrak, amblem yoktur** — gemi gövdesi modelin yazı yazmak için en çok
    zorladığı yüzeydir. Kapak ayrı üretilir ve **videoya girmez**.
11. **⛔ ATEŞ SÜRESİ = 1,0 SANİYE · İTKİ ALEVİ = 0 KARE — BU FİLMİN 1
    NUMARALI KURALI** — Vakumda oksitleyici yoktur: metal kesme kıvılcımı
    kızgın parçacıktır, **alev değildir**, ve 1,0 saniyede beyazdan sönük
    turuncuya geçip kaybolur. Ateş topu, alev, yangın, duman, duman izi,
    egzoz konisi, itki parlaması **filmin hiçbir karesinde yoktur**
    [Ders 21 · 36 · Kart 6]. Bu tek kural, kartlardaki en pahalı riski
    tek bir saniyeye hapseder.
12. **⛔ SERBEST KALAN NESNE SAYISI = TAM 6 [Ders 38]** — Çarpışmada tam 6
    adet 2,0 m × 2,0 m gövde paneli kopar ve düz çizgilerde uzaklaşır.
    Gövdeler **bütün kalır**: parçalanma yok, sürekli enkaz dökülmesi yok,
    genişleyen enkaz bulutu yok. Sağlam kalan yüzeyler promptta ayrıca
    yazılır — model neyin BOZULMAYACAĞINI bilmezse hepsini bozar.

---

## 🧬 VİRAL MEKANİK — "ÖLÇEK-HIZ UYUŞMAZLIĞI"

```
Bu shorts'un mekaniği bir imkansızlık değil, bir YANLIŞ BEKLENTİ.

İzleyicinin gözü şunu bilir: büyük şey hızlı çarpar, gürültü çıkarır,
alev alır. Ekranda gördüğü şey ise:

 · 400 metrelik toplam gövde, temas hızı 12 m/s — koşan bir insan.
 · Temastan itibaren 1,5 saniye süren, ölçülebilir bir EZİLME:
   12 metrelik tampon halkası 3 metreye iner. 9 metre. Sayılabilir.
 · Gövdenin ivmesi 0,25 g, 1,5 saniye — sert bir otobüs freni.
   Karakter 25 derece öne yatar ve doğrulur. Fırlamaz, savrulmaz.
 · 1,0 saniyelik beyaz kıvılcım. Sonra hiçbir ışık. Oksijen yok.
 · Ses YOK. Vakum ses taşımaz. Karakterin duyduğu tek şey,
   botlarının altından gövdeye yayılan derin metal uğultusudur —
   ses katı cisimden geçer. Bu, filmin ses tasarımının tamamıdır.

İzleyicinin gözü ilk 2 saniyede "uzay yürüyüşü" der. 4. saniyede sol
üstteki üç kırmızı ışığın bir GÖVDEYE ait olduğunu görür ve düzeltir.
6. saniyede o gövdenin hiç manevra yapmadığını görür — itki alevi yok,
demek ki ölü — ve bir kez daha düzeltir: bu bir geçiş değil, bir
BULUŞMA. 34. saniyede iki gövde birbirine değer ve hiçbir ses çıkmaz.
Geriye tek soru kalır: bu kadar büyük bir şey nasıl bu kadar sessiz
olabilir?

Serinin önceki mekaniklerinden ayrı: sinyal yokluğu değil (Half Sky),
süreksizlik değil (Winter Line), zaman kaybı değil (First Morning),
yörünge değil (Low Moon), eksik neden değil (Wrong Shadow).
Buradaki mekanik ÖLÇEK-HIZ UYUŞMAZLIĞI: fizik doğru, sezgi yanlış.
```

### Mekaniğin insani karşılığı

```
Kadın kurtarma mühendisi. Yakıt aktarımı sürdüğü için yük gemisinin
motorları soğuk — manevra yapamaz. Karşıdaki tanker saatlerdir ölü ve
sürükleniyor; kimse yok, kurtarma yok, radyo yok. Vardiyası boyunca
yaptığı tek iş mesafeyi ÖLÇMEK oldu ve ölçtüğü şeyi durduramıyor.
Filmin bedeli S3'te ödenir: çarpma protokolü T-20 saniyede bütün
kapakları mühürler. Dört metre gerisinde açık, aydınlık bir kapak
duruyor — tek sığınağı. Kapağa gitmez; altı metre İLERİ gider ve
tampon kaldıracını çeker. Böylece çarpışma bir yırtılma değil, bir
EZİLME olur; iki gemi paramparça olmak yerine tek parça hâlinde
sürüklenir. Kapak arkasında sönerken elleri kaldıracın üstündedir —
bedel ve seçim AYNI KAREDE.
```

---

## 📱 GÜVENLİ ALAN HARİTASI (9:16 · 1080×1920)

Kaynak: `kilavuzlar_ve_sistem_dosyalari/KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §5
evrensel matrisi · denetleyen rubrik: `QA_PROMPTLARI/SHORTS_QA_CRITIQUE_PROMPT.md` §B

```
┌──────────────────────────────┐ y=0
│  ÜST KÖR NOKTA  200-254 px   │      sekmeler, profil
├──────────────────────────────┤ y=254
│                          │S │
│                          │A │
│        GÜVENLİ ALAN      │Ğ │      sağ 242 px: beğen/paylaş/yorum
│                          │  │
│                          │242
├──────────────────────────────┤ y=1436   ⛔ BURADAN AŞAĞISI GÖRÜNMEZ
│  ALT KÖR NOKTA    484 px     │      açıklama, müzik, CTA
└──────────────────────────────┘ y=1920
```

### ✅ BU FİLMİN GÜVENLİ ALAN AVANTAJI

```
Reveal nesnesi GÖKYÜZÜNDE — yani zaten üst 2/3'te yaşıyor.
```

Wrong Shadow ve Sinking Hour'un yapısal çelişkisi (reveal yerde, güvenli
alan altı yasaklıyor) bu filmde **yok**. Tek dikkat noktası tersine döner:
karakterin ayakları alt çeyreğe düşmemeli. Çözüm sayısaldır — **kamera
gövde kaplamasının 1,0-1,6 m üstünde tutulur ve düz bakar**; bu yükseklikte
metal düzlük kadranın alt üçte birini doldurur, figür onun üstünde durur,
ayaklar hiçbir sahnede %75'in altına inmez.

### Sahne sahne denetim

| Sahne | Reveal nesnesi | Doğal yeri | Karara bağlanan çözüm |
|:--:|---|:--:|---|
| S0 | üç kırmızı fener + uzak silindir | ✅ üstte | kamera 9 m / 1,6 m; figür y980-1400; tanker y300-560 (sol üst) |
| S1 | tankerin altı kuşağı ayrışıyor | ✅ üstte | kamera 2,5 m / 1,5 m; yüz y420-900; tanker yumuşak koyu bant y150-420 |
| S2 | gövde gökyüzünün yarısı | ✅ üstte | kamera 12 m / 1,2 m; figür y1050-1420; tanker y254-950 |
| S3 | kaldıraç + sönen kapak + açılan tampon | ⚠️ karışık | kamera 5 m / 1,2 m; figür y820-1400; kapak sol y1000-1300; burun+tampon y480-700 |
| S4 | **TEMAS** | ✅ üstte | kamera 9 m / 1,0 m; figür y1000-1400; temas noktası y500-700; tanker y254-620 |
| S5 | iki gövde tek siluet | ✅ üstte | kamera 7→22 m / 1,4 m; figür y1080-1420; birleşik siluet y254-900 |

**Her görsel promptun COMPOSITION satırına eklenen zorunlu cümle:**

```
No part of the figure falls into the bottom quarter of the frame.
```

---

## 📖 Sabit Referanslar (Bibles)

### 👤 Character Bible

**Kimlik (yalnızca bu dosyada):** DENİZ ARAL, 34, kurtarma mühendisi.
Sekiz yıldır yörünge çekicilerinde; mesafeyi aletle değil, gövdedeki
kuşaklara bakarak okuyan cinsten.

> ⚠️ **ÜRETİM UYARISI [Ders 34 / 45]:** Karakter Türk, ama promptlarda
> **milliyet ifadesi KULLANILMAZ** — geçmişte üretim reddine yol açtı.
> Karakterin adı hiçbir promptta yazılmaz. Gerçek bir kurum, ülke, ajans,
> bayrak ya da marka hiçbir promptta geçmez.

**Tam tarif — 6 GÖRSEL promptun 6'sında da birebir, kısaltmasız tekrarlanır:**

```
A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles.
```

**Hareket imzası (konsepte özgü):** Manyetik bot yürüyüşü — her adım hafif
bir yapışma gecikmesiyle kalkar, tabanı düz basar, gövdesi yatay kalır.
Vakumda hiçbir şey sallanmaz; kolları yürürken sarkaç yapmaz. Bir şeyi
ölçerken **başını değil, gözünü çevirir**; tankerin kuşaklarını saymak için
2-3 saniye tamamen hareketsiz kalır. Şaşkınlığı hızlanma değil
**doğrulamadır**. Durduğunda iki botunu da düz basar ve dizlerini 5 derece
kırar — çarpmaya hazırlanan bir insanın duruşu.

### 🚀 Ship Bible — İKİ GÖVDE, İKİSİ DE İNSANSIZ

> ⚠️ **HUMAN COUNT LOCK'un yarısı buraya yazılır [Kart 4 · Ders 20]:**
> Her iki gemi de **otomatik yük taşıyıcıdır**. Mürettebat yok, pilot yok,
> aydınlık kokpit yok, **hiçbir gövdede pencere yok**. Kart 4'ün ölçülmüş
> sıcak noktası (gemi iniş/kalkış anında beliren ikinci insan) bu filmde
> konsept düzeyinde kapatıldı: iniş yok, kalkış yok, biniş yok.

```
① AYAKLARININ ALTINDAKİ GÖVDE — YÜK GEMİSİ (240 m)
   Sırt omurgası: 26 m genişliğinde düz metal yürüme düzlüğü
   Kaplama:       TAM 2,0 m × 2,0 m kare paneller (kadrandaki tek cetvel)
   Korkuluk:      1,1 m yüksekliğinde, omurganın iki kenarı boyunca
   Lamba direği:  3 m boyunda, HER 20 METREDE BİR — kaplamaya
                  kenarları jilet keskin soğuk beyaz ışık havuzu düşürür
   Burun tamponu: 8 ezilme silindirinden halka.
                  Kapalı: gövdeye gömülü.  Açık: 12 m ileri, 9 m çap.
                  Ezilme sonrası: 3 m.  (12 → 3 = 9 m, 1,5 saniyede)
   Motorlar:      SOĞUK. Film boyunca tek bir itki alevi yok.
   Yazı:          YOK. Gövdede rakam, harf, seri no, amblem, bayrak yok.

② YAKLAŞAN GÖVDE — ÖLÜ TANKER (160 m)
   Biçim:         34 m çapında düz silindir, oksitlenmiş gri, mat
   Kuşaklar:      TAM 6 kaburga bandı, aralarında 24 m — İZLEYİCİNİN CETVELİ
   Işık:          TAM 3 sönük kırmızı bekleme feneri, aralarında 40 m
                  (haleleri yok, parlamıyorlar, sadece yanıp sönüyorlar)
   Pencere:       YOK.  Kokpit ışığı: YOK.  Yazı: YOK.
   İtki:          YOK — ölü olduğunun tek kanıtı budur ve her promptta yazılır

③ ÖLÇEK KİLİDİ [Ders 32] — her promptta aynı sayılar:
   insan 1,68 m · panel 2,0 m · omurga 26 m · korkuluk 1,1 m ·
   lamba direği 3 m / 20 m arayla · tanker çapı 34 m · kuşak arası 24 m
   Bu oranlar hiçbir sahnede değişmez. Kapı, merdiven, rampa yok —
   değişebilecek geometri konseptten çıkarıldı.
```

### 🌍 World Bible — VAKUM, GEZEGENİN GECE TARAFI

```
YER:       Alçak yörünge. Aşağıda/sol üstte pas kahvesi bir gezegenin
           kavsi. Gezegen adı promptlarda geçmez.
YERÇEKİMİ: Serbest düşüş (0 g). Karakter yüzmüyor — botları manyetik.
           Bu, Ders 23'ün (rijit süzülen gövde) tetiklenmediği tek duruş.
ATMOSFER:  YOK. Duman yok, pus yok, saçılma yok, egzoz yok, alev yok.
           Gölgeler mutlak keskin ve DOLGUSUZ. Yıldız alanı yoğun ve
           titremiyor (vakumda yıldızlar kırpışmaz).
GÜNEŞ:     Kadrajda YOK — gemiler gezegenin gölgesinde. Bu bir estetik
           tercih değil, iki riskin birden kapatılmasıdır: parlama/bloom
           [Ders 3/29/41] ve altın/aynalı vizör zorunluluğu [Ders 79].
SES:       Vakum ses taşımaz. Karakterin duyduğu tek şey botlarından
           gövdeye yayılan yapısal uğultudur (katı cisim iletimi).
SU:        YOK. Buz yok, sıvı yok, buhar yok. [Kart 1 konseptte yok]
CANLI:     YOK. [Kart 2 konseptte yok]

⚠️ MERKEZİ OLAY — ÇARPIŞMA TAKVİMİ (ana saat, T = temas anı):
Yaklaşma hızı sabit: 12 m/s. Film bu 67 saniyeden altı pencere alır.

  S0   T-66 → T-58 s   mesafe 792 → 696 m   tanker kadranın ~1/5'i
  S1   T-52 → T-44 s   mesafe 624 → 528 m   kuşaklar ayrışmaya başlıyor
  S2   T-38 → T-30 s   mesafe 456 → 360 m   tanker kadranın ~1/2'si
  S3   T-24 → T-16 s   mesafe 288 → 192 m   ⭐ MERKEZ SEÇİM (kaldıraç)
  S4   T-2  → T+6 s    mesafe 24 → 0 m      ⭐ TEMAS (çekimin 2,0. sn'si)
  S5   T+120 → T+128 s mesafe 0 (kilitli)   sessizlik, iki dakika sonra

Görsel promptlara **pencerenin orta değeri** yazılır (yaklaşık): S0 750 m ·
S1 575 m · S2 400 m · S3 220 m. S0-S3'ün zorunlu satırı:
"the gap between the two hulls is approximately [X] metres and closing at
a steady 12 metres per second — the closing speed of a running person"
S4'te mesafe sıfırlanır ("the gap is zero — this is the contact instant,
closing speed twelve metres per second at first touch"), S5'te gövdeler
kilitlidir ve mesafe satırı yazılmaz.

S4'ün zorunlu ezilme satırı:
"the twelve-metre crush ring collapses to three metres over one and a half
seconds; the hulls decelerate at about a quarter of one g; both hulls stay
whole and exactly six 2.0-metre hull panels break free"
```

### 🎥 Camera Bible

```
LENS KİLİDİ — çekim başına tam olarak bir lens, hepsi küresel:
  32mm → S0, S2, S3, S4, S5      75mm → S1 (filmin TEK yakın planı)
  ⛔ Anamorfik lens ve yatay parlama yasak (vakumda fiziksel olarak yanlış)
MESAFE + YÜKSEKLİK KİLİDİ: her promptta metre cinsinden yazılır.
  Kamera hiçbir sahnede kaplamanın 1,6 metresinden yüksek değildir.
HAREKET SÖZLÜĞÜ (çekim başına TEK sürekli hareket):
  S0 sabit lockoff · S1 sabit lockoff · S2 sabit lockoff ·
  S3 sabit lockoff · S4 sabit lockoff (⭐ temas karesi — KIPIRDAMAZ) ·
  S5 yavaş pull-back 7 m → 22 m
  → 6 sahnenin 5'i tamamen sabit. Deponun bir shorts'ta ulaştığı en yüksek
    lockoff oranı. Gerekçe: Kart 8, Kamera 2/10 → 8/10 sıçramasının tek
    sebebi talebin kaldırılmasıydı.
⭐ KAMERA GÖVDEYE VİDALIDIR: çarpma anında kamera da 0,25 g ivmelenir,
  yani kadrajda görece hareket YOKTUR. "Aksiyon = sarsıntı" refleksi bu
  cümleyle kapatılır; her video promptunda "no camera shake" ayrıca durur.
SABİT KLİP SÜRESİ: her video promptu tam 8 saniye, tek kesintisiz çekim.
GÜNEŞ KADRAJI: hiçbir sahnede güneş yok — flare riski sıfır [Ders 3].
```

### 💡 Lighting Bible — ÜÇ KAYNAK, HEPSİ SAYILI

```
KAYNAKLAR (adıyla yazılır, asla "cinematic lighting" denmez) [Ders 33]:
  · GEZEGEN IŞIĞI (planetshine): sol üstteki pas kahvesi kavisten gelen
    yumuşak, sıcak-kahve dolgu ışığı. Zayıf ama geniş.
  · LAMBA HAVUZLARI: her 20 metrede bir, 3 m'lik direklerden aşağı
    vuran soğuk beyaz ışık. Vakumda hava saçılması olmadığı için
    havuzların kenarı JİLET KESKİNDİR ve aradaki kaplama koyu kalır.
    Işık huzmesi GÖRÜNMEZ — havada tutunacak toz yok.
  · ÜÇ KIRMIZI FENER: tankerin gövdesinde, sönük, halesiz, yanıp sönen.
  · (yalnız S4, 1,0 saniye) KIVILCIM IŞIĞI: beyaz, sert, kısa.

⚠️ [Ders 3/29/41] Metal + nokta kaynak = bloom riski. Kaplama MATtır,
   "glowing / radiant / shining" hiçbir promptta geçmez, hale ve flare
   negatif bloktadır.

IŞIK TAKVİMİ — tek yönlü ve fiziksel (tanker gezegeni kapatıyor):
  S0 gezegen kavsi %100 açık · S1 %85 · S2 %60 · S3 %30 · S4 %10 →
  temastan sonra %0 · S5 %0 — filmin son 8 saniyesinde tek ışık,
  geminin kendi lamba havuzlarıdır.
  Zorunlu satır: "approximately [X] percent of the planet limb is still
  open at upper left; the rest is blocked by the tanker's hull."
ZEMİN KİLİDİ [Ders 48]: "the hull plating, panel size, rail height and
lamp mast spacing are identical to the previous scene; only the light and
the distance have changed."
```

### 🚫 Negative Bible

```
Kesme yok. Sarsıntı yok. Ağır çekim yok. Minyatür/oyuncak görünüm yok.
CGI havası yok. Hava fırçasız cilt yok. İkinci insan yok, mürettebat yok,
insan yansıması yok. Elde taşınan alet yok. Metin yok. Filigran yok.

KONSEPTE ÖZGÜ EKLER:
ATEŞ YOK: ateş topu yok, alev yok, yangın yok, yanan gövde yok, duman yok,
duman izi yok, egzoz konisi yok, itki parlaması yok, kıvrılan gaz yok.
(Tek istisna: S4'te 1,0 saniyelik kızgın metal kıvılcımı — alev değil.)
PARÇALANMA YOK: enkaz bulutu yok, sürekli enkaz dökülmesi yok, gövde
parçalanması yok, dağılan kaplama yok. Serbest kalan nesne TAM 6.
GEÇME YOK: hiçbir gövde bir diğerinin içinden geçmez, kaynaşmaz, erimez.
ÜÇÜNCÜ GEMİ YOK. Pencere yok, kokpit ışığı yok, uydu yok, istasyon yok.
Vakumda toz bulutu yok, pus yok, görünür ışık huzmesi yok.
Yıldızlar kırpışmaz. Gezegende bulut animasyonu yok.
```

**Negatif bloklara eklenecek kuyruk (her görsel promptun sonuna):**

```
no second person, no crew, no figure in any window, no human reflection, no
third ship, no satellite, no station, no fireball, no flame, no fire, no
burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no
thruster flash, no visible light beam, no lens flare, no bloom, no glow
filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no
fragmenting hull, no structural disintegration, no hull passing through
another hull, no slow motion, no camera shake, no miniature look, no toy
look, no CGI look, no waxy skin, no text, no letters, no digits, no serial
numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark
```

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

```
🔴 EN YÜKSEK RİSK — kartlarda yok, bu dosyada tanımlandı

KATI-CİSİM TEMASI (İKİ BÜYÜK GÖVDE)
        Ders 17: nesneler birbirinden geçiyor (deponun en düşük fizik
        skorunun kaynağı). Ders 38: model "hasarlı"yı "parçalanmış"
        okuyor ve ölçek kilidini de beraberinde çökertiyor.
        Kilitler: ezilme 12 m → 3 m / 1,5 sn · ivme 0,25 g ·
        serbest nesne TAM 6 · "both hulls stay whole" + sağlam kalan
        yüzeylerin sayımı · "no hull passes through another hull" 6/6.
        ÜRETİM SIRASI: S4 (temas) ÖNCE üretilir. Karede ateş topu,
        parçalanan gövde, üçüncü cisim ya da ağır çekim çıkarsa
        film üretilmez [THE LOW MOON · WRONG SHADOW emsali].

DERS 12 / 44  AĞIR ÇEKİM — bu filmin en olası bozulması. "Çarpışma"
        kelimesi modeli doğrudan slow-motion'a çeker; üstüne 0 g
        beklentisi biner. Karşı önlem: "real-time motion at normal
        playback speed" + "no slow motion" 6 video promptunun 6'sında,
        ve hareketin sayısal hızı ("12 metres per second", "1.5 seconds").

DERS 21 / 36 / 31  ATEŞ VE PARÇACIK — patlama 1,0 saniyeye hapsedildi,
        itki alevi ve duman konseptten tamamen çıkarıldı. Kıvılcım
        "cooling from white to dull orange to nothing within 1.0
        second, in straight lines, no flame" olarak yazılır.

🟡 ORTA RİSK

KART 4 / DERS 20  İKİNCİ FİGÜR — "exactly one human" 6/6 promptta;
                  iki gemi de insansız ve PENCERESİZ (sıcak nokta kapalı)
DERS 79 / 5 / 16 / 37  SUIT VE VİZÖR — sırt düz + vizör berrak,
                  ikisi de negatif çekirdekte POZİTİF cümleyle
                  (bible'da kalan yasak iki filmde üst üste tutmadı)
DERS 32           GEMİ ÖLÇEĞİ — 8 sayı 6 promptta birebir tekrarlanır
DERS 23           SIFIR-G — karakter manyetik botlu (rijitlik riski
                  düşük); mikro hareket YÜKÜ serbest 6 panele ve
                  çarpma anındaki 25 derecelik gövde yatışına verildi
DERS 47 / 48      IŞIK VE ZEMİN İLERLEMESİ — gezegen kavsi tek yönde
                  kapanır (%100→0), kaplama 6 sahnede birebir aynı
DERS 6 / 42       ARKA PLAN VE YIPRANMA — lamba direği aralığı, korkuluk,
                  suit toz izleri 6 sahnede sabit
DERS 71           ANALOG PERDE YOK — reveal mesafeyle değil, KADRAJ İÇİ
                  büyümeyle gelir; sis/flu/karanlık perde kullanılmadı

⬛ HER PROMPTTA

DERS 9 · 13 · 34 · 45 · 61   EKRANDA METİN YOK — iki gövdede de yazı,
        rakam, seri no, amblem yok; ekran/gösterge/HUD hiç yok;
        jenerik kartı yok; isim hiçbir promptta geçmez.
DERS 73 / 76      NOVUM TAŞIYICISI BİRİNCİL VE POZİTİF — taşıyıcı iki
        katı gövdedir. "Sessizlik" bir yokluk olarak DEĞİL, ölçülebilir
        pozitif olgularla render edilir: ateş 0 kare, duman 0 kare,
        enkaz düz çizgide, kırmızı fenerler yanıp sönmeye devam ediyor.
DERS 70 / 72      KURGU KAPISI — 6 klip × 8,000 s = 48,000 s. Jenerik
        kartı, başlık karesi, kapak karesi kurguya GİRMEZ.
```

---

## 🎬 SAHNE 0 — KANCA: ÜÇ KIRMIZI IŞIK

_"Yıldızların arasında yıldız olmayan üç nokta."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 0 of 6. Solo female salvage engineer orbital collision film. MAXIMUM VIRAL SCALE SHOCK.
Lens: 32mm, f/8, ISO 400.
Camera Distance: Approximately 9 metres, camera height 1.6 metres above the hull plating, held level, hard-mounted to the hull.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. She stands alone at the forward guard rail, side-on to camera, head just beginning to turn up and to the left.

ENVIRONMENT / BACKGROUND: The hull under her boots is the dorsal spine of a 240-metre automated bulk hauler: a flat metal walkway 26 metres wide, plated in exactly 2.0-metre square panels, with a 1.1-metre guard rail down both edges and a 3-metre lamp mast every 20 metres throwing a hard-edged pool of cold white light onto the plating. The hauler has no windows, no lit cockpit, no markings and no engine plume — its engines are cold. Beyond the bow the star field is dense, steady and unblinking, and the rust-brown limb of a planet fills the upper left; approximately 100 percent of the planet limb is still open at upper left. Crossing that rust glow at upper left is a distant dark cylinder: an automated tanker, 160 metres long and 34 metres in diameter, plain oxidised grey with six rib bands and exactly three dim red standby beacons spaced 40 metres apart along its side — no windows, no lit cockpit, no markings, and no engine plume of any kind. The gap between the two hulls is approximately 750 metres and closing at a steady 12 metres per second — the closing speed of a running person.

THE VIRAL MOMENT / REVEAL: Three dim red points hang in the upper left where there should only be stars — and they are not separate. They belong to one long dark body silhouetted against the planet, and that body is not crossing the sky; it is growing in it. Nothing on it is firing. There is no thruster flash anywhere.

COMPOSITION: Vertical 9:16. The lit metal plain fills the bottom third of the frame, its panel grid receding toward the bow at roughly thirty-two percent of frame height. She stands left of centre between roughly fifty-one and seventy-three percent of frame height, clear of the outer right eighth. The tanker sits in the upper left between roughly sixteen and twenty-nine percent of frame height and reads about one fifth of the frame width. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only lit hull plating.

LIGHTING: Cold white lamp pools on matte grey plating, their edges knife-sharp with no atmospheric falloff and no visible beam. Soft rust-brown planetshine from upper left fills her left side. Three dim red beacons, no halo, no bloom, no lens flare. Shadows are absolutely sharp and unfilled.

PHYSICS: Hard vacuum and free fall — no smoke, no haze, no atmospheric scattering, no fire, no engine plume. Nothing sways or flutters. Her boots are magnetically locked flat to the plating; her body does not float. The star field does not twinkle.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, locked off at 9 metres, camera height 1.6 metres above the hull plating, dead level, hard-mounted to the hull. The camera does not move at all. Real-time motion at normal playback speed.

At 0s — A woman in a matte graphite-grey EVA suit stands alone at the guard rail of a wide lit metal walkway that runs away from camera into black. Hard-edged pools of cold white light repeat down the plating. A rust-brown planet limb fills the upper left. An ordinary shift.
At 2s — Three dim red points blink in the upper left, out among the stars. They blink together, in step, at the same slow rate.
At 3.5s — The red points resolve: they sit along one long dark body silhouetted against the planet — a plain grey cylinder with six rib bands, growing steadily larger frame by frame.
At 5s — She turns her head up and left and holds absolutely still, reading it. Nothing on that hull fires. No flash, no plume, no manoeuvre.
At 6.5s — The cylinder is measurably bigger than it was at 2s and now covers about a fifth of the sky. Her breath fogs a faint crescent on the inside of her visor and clears.
By 8s — She is still watching it. It is still growing. No cuts within the shot.

Exactly one human in this shot. Exactly two ships, both without windows, crew or engine plume. Nothing burns and nothing smokes. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 1 — ALTI KUŞAK

_"Kuşakların arası yirmi dört metre. Saymaya başladı."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 1 of 6. Solo female salvage engineer orbital collision film.
Lens: 75mm, f/4, ISO 800.
Camera Distance: Approximately 2.5 metres, camera height 1.5 metres above the hull plating, held level, hard-mounted to the hull.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. Head and shoulders, three-quarter angle, chin slightly lifted, eyes moving in small steps from left to right as she counts something in the distance.

ENVIRONMENT / BACKGROUND: Behind her, softly out of focus, the wide lit spine of the 240-metre hauler with its 2.0-metre panel grid, 1.1-metre rail and 3-metre lamp masts every 20 metres. Across the top of the frame, also soft, the dark bar of the approaching tanker against the rust-brown planet limb; approximately 85 percent of the planet limb is still open at upper left. Three dim red beacons read as three soft red points along that bar. The tanker is 160 metres long, 34 metres in diameter, with six rib bands spaced 24 metres apart — the bands have just become separately readable. No windows, no lit cockpit, no markings, no engine plume on either hull. The gap between the two hulls is approximately 575 metres and closing at a steady 12 metres per second — the closing speed of a running person. The hull plating, panel size, rail height and lamp mast spacing are identical to the previous scene; only the light and the distance have changed.

THE VIRAL MOMENT / REVEAL: Her face is doing arithmetic. The rib bands are 24 metres apart and she is using them as a ruler; her eyes step left to right, six times, and stop. Whatever the answer is, she does not look away from it.

COMPOSITION: Vertical 9:16. Her face occupies roughly twenty-two to forty-seven percent of frame height, her shoulders reaching seventy percent, positioned slightly left of centre and clear of the outer right eighth. The soft dark bar of the tanker crosses the top of the frame between roughly eight and twenty-two percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only defocused lit plating.

LIGHTING: Cold white lamp light from below-frame-right rakes up across her jaw and visor; soft rust-brown planetshine from upper left fills the other side of her face. The clear visor throws no reflection and no mirror sheen; her whole face is readable. No bloom, no halo, no lens flare.

PHYSICS: Hard vacuum and free fall — no haze, no smoke, no scattering. Her boots are magnetically locked; her body is steady, only her eyes and a small head tilt move. Breath haze forms and clears on the inside of the visor.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm, locked off at 2.5 metres, camera height 1.5 metres above the hull plating, dead level, hard-mounted to the hull. The camera does not move at all. Real-time motion at normal playback speed.

At 0s — Close on a woman's face behind optically clear helmet glass, lit hard from below by cold white lamp light and softly from upper left by rust-brown planetshine. Behind her, out of focus, a wide lit metal walkway and a dark bar across the top of the frame.
At 2s — Her eyes step left to right in six small movements, counting the rib bands of the approaching hull, then return to the start and count again.
At 3.5s — She stops. Her jaw sets. Nothing theatrical: a professional receiving an answer she already suspected.
At 5s — Her breath fogs a crescent on the inside of the visor and slowly clears. The three soft red points behind her blink once, together.
At 6.5s — She lifts her chin a few degrees and holds, still watching. The dark bar behind her has grown slightly thicker across the top of the frame.
By 8s — She has not looked away. No cuts within the shot.

Exactly one human in this shot. The visor never mirrors or tints; her face stays fully readable. Nothing burns and nothing smokes; no engine plume anywhere. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 2 — GÖKYÜZÜ KAPANIYOR

_"Yıldızlar bitiyor. Yerlerine gri geliyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 2 of 6. Solo female salvage engineer orbital collision film.
Lens: 32mm, f/8, ISO 400.
Camera Distance: Approximately 12 metres, camera height 1.2 metres above the hull plating, held level, hard-mounted to the hull.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. She stands small and centred on the walkway, feet apart, knees very slightly bent, looking up.

ENVIRONMENT / BACKGROUND: The full width of the hauler's 26-metre dorsal spine, plated in exactly 2.0-metre squares, 1.1-metre guard rails down both edges, 3-metre lamp masts every 20 metres laying hard-edged pools of cold white light along it. Four metres behind her, set into the plating, an open circular hatch throws a warm white rectangle of interior light onto the deck — the only warm light in the frame. Above and ahead, the tanker now fills the upper half of the sky: a plain oxidised-grey cylinder 160 metres long and 34 metres in diameter with six rib bands spaced 24 metres apart and exactly three dim red standby beacons spaced 40 metres apart, no windows, no lit cockpit, no markings, no engine plume. Approximately 60 percent of the rust-brown planet limb is still open at upper left; the rest is blocked by the tanker's hull. The gap between the two hulls is approximately 400 metres and closing at a steady 12 metres per second — the closing speed of a running person. The hull plating, panel size, rail height and lamp mast spacing are identical to the previous scene; only the light and the distance have changed.

THE VIRAL MOMENT / REVEAL: The star field is disappearing from the top down. Where there were stars there is now a grey wall with ribs on it, and the wall has an end — you can see both ends of a 160-metre object in one frame, and it is still coming.

COMPOSITION: Vertical 9:16. The lit walkway fills the bottom third, its rails converging toward the bow. She stands centred and small between roughly fifty-five and seventy-four percent of frame height, the open hatch glowing warm behind her at roughly seventy percent, both clear of the outer right eighth. The tanker occupies the frame between roughly thirteen and fifty percent of frame height and about half the frame width. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only lit hull plating.

LIGHTING: Cold white lamp pools with knife-sharp edges, one warm white rectangle from the open hatch, weakening rust-brown planetshine from upper left, three dim red beacons above. The tanker's underside is unlit and reads as flat oxidised grey. No bloom, no halo, no lens flare, no visible light beam.

PHYSICS: Hard vacuum and free fall — no haze, no smoke, no scattering, no fire, no plume. Both hulls are rigid, whole and undamaged; the tanker is not rotating and not manoeuvring. Her boots are magnetically locked flat to the plating.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, locked off at 12 metres, camera height 1.2 metres above the hull plating, dead level, hard-mounted to the hull. The camera does not move at all. Real-time motion at normal playback speed.

At 0s — Wide and low along a 26-metre lit metal walkway. A small graphite-grey figure stands centred on it, a warm-lit open hatch four metres behind her. Above, a ribbed grey cylinder already covers the upper half of the sky.
At 2s — The cylinder grows visibly against the star field; stars vanish behind its leading edge, row by row, from the top down.
At 3.5s — She tips her head back to follow it and her knees bend very slightly, a bracing posture, boots staying flat on the plating.
At 5s — The three red beacons blink together, closer and brighter than before. Still no thruster flash anywhere on that hull.
At 6.5s — The rust-brown planet limb at upper left is being covered; the light on the walkway cools as the warm fill disappears.
By 8s — More sky is grey than black. She has not moved her feet. No cuts within the shot.

Exactly one human in this shot. Exactly two ships, both windowless and unlit except three red beacons. Both hulls stay whole and rigid. Nothing burns and nothing smokes. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 3 — MERKEZ SEÇİM: SIĞINAK MI, TAMPON MU

_"Kapak arkasında söndü. Elleri kaldıraçtaydı."_

> ⭐ **CENTRAL CHOICE — vuruş haritası §2.1.** Seçim bu çekimin İÇİNDE
> tamamlanır ve bedeli AYNI KAREDE görünür: kapağın ışığı 4,0. saniyede
> söner, eller 5,0-6,5 arasında kaldıracı 90 derece çevirir [Ders 78 ①].

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 3 of 6. Solo female salvage engineer orbital collision film.
Lens: 32mm, f/8, ISO 400.
Camera Distance: Approximately 5 metres, camera height 1.2 metres above the hull plating, held level, hard-mounted to the hull.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. Both of her gloved hands are closed around a hull-mounted lever: a 1.2-metre safety-yellow bar with black diagonal stripes, fixed to a rail post and pulled from vertical toward horizontal, her weight low and her elbows bent.

ENVIRONMENT / BACKGROUND: The forward end of the hauler's 26-metre dorsal spine, plated in exactly 2.0-metre squares, 1.1-metre guard rail, 3-metre lamp masts every 20 metres. Behind her at frame left, four metres away, the circular hatch is closing: its warm white interior light is shrinking to a thin seam. Thirty metres ahead, at the bow, a ring of eight crush cylinders is telescoping forward — extended nine metres of its full twelve, nine metres in diameter. Filling the upper frame, the tanker: a plain oxidised-grey cylinder 160 metres long and 34 metres in diameter with six rib bands spaced 24 metres apart and exactly three dim red standby beacons spaced 40 metres apart, no windows, no lit cockpit, no markings, no engine plume. Approximately 30 percent of the rust-brown planet limb is still open at upper left; the rest is blocked by the tanker's hull. The gap between the two hulls is approximately 220 metres and closing at a steady 12 metres per second — the closing speed of a running person. The hull plating, panel size, rail height and lamp mast spacing are identical to the previous scene; only the light and the distance have changed.

THE VIRAL MOMENT / REVEAL: One frame holds the whole decision: behind her the last warm light of the only shelter narrowing to a seam, ahead of her a twelve-metre ring pushing out to meet a hundred and sixty metres of dead ship, and between them two gloved hands finishing a ninety-degree pull.

COMPOSITION: Vertical 9:16. She stands right of centre between roughly forty-three and seventy-three percent of frame height, the yellow lever crossing her body at roughly sixty percent, clear of the outer right eighth. The closing hatch sits at frame left between roughly fifty-two and sixty-eight percent. The bow and its extending crush ring read between roughly twenty-five and thirty-six percent. The tanker fills the frame above them between roughly thirteen and twenty-eight percent, its underside now the ceiling of the shot. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only lit hull plating.

LIGHTING: Cold white lamp pools with knife-sharp edges; a narrowing warm white seam from the closing hatch at frame left; the last weak rust-brown planetshine at upper left; three dim red beacons overhead. The safety-yellow lever is the only saturated colour in the frame and covers less than one percent of it. No bloom, no halo, no lens flare, no visible light beam.

PHYSICS: Hard vacuum and free fall — no haze, no smoke, no scattering, no fire, no plume. The lever is a rigid part of the ship: it rotates on its pivot, does not bend, does not detach, and is never carried. The crush ring extends smoothly on eight straight cylinders. Both hulls are whole and rigid. Her boots are magnetically locked flat to the plating.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships. Exactly one lever, fixed to the ship and never carried. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, locked off at 5 metres, camera height 1.2 metres above the hull plating, dead level, hard-mounted to the hull. The camera does not move at all. Real-time motion at normal playback speed.

At 0s — She walks six steps forward along the lit plating, away from an open hatch that throws warm white light onto the deck four metres behind her. Each magnetic step lifts with a small sticky delay and plants flat. Above her, a ribbed grey hull fills the top of the frame.
At 2s — She reaches a rail post and closes both gloved hands around a 1.2-metre safety-yellow lever, setting her feet, knees bent.
At 4s — Behind her the hatch seals. The warm rectangle of light narrows to a seam and goes out; the deck around her turns cold white. She does not look back.
At 5s — She pulls. The lever swings ninety degrees, from vertical to horizontal, in one steady movement — no strain theatre, no jerk.
At 6.5s — Thirty metres ahead at the bow, a ring of eight crush cylinders telescopes forward and locks, extended twelve metres.
By 8s — She keeps both hands on the lever and looks up at the hull coming down. No cuts within the shot.

Exactly one human in this shot. The lever is part of the ship: it rotates, never bends, never detaches, and is never carried. Both hulls stay whole. Nothing burns and nothing smokes; no engine plume anywhere. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 4 — VİRAL DORUK: TEMAS

_"Yüz altmış metre, yürüme hızında geldi ve hiç ses çıkarmadı."_

> ⭐ **ÜRETİM BURADAN BAŞLAR.** Filmin en pahalı karesi ve katı-cisim
> temasının tek sınavı. Karede **ateş topu, yanan gövde, parçalanan
> kaplama, üçüncü cisim, ağır çekim ya da birbirinin içinden geçen iki
> gövde** çıkarsa **film üretilmez** — prompt iyileştirmeye dönmeden önce
> `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` oku ve sonucu
> **KAPI KAYDI** tablosuna yaz [Ders 74].

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 4 of 6. Solo female salvage engineer orbital collision film. MAXIMUM VIRAL CONTACT SHOCK.
Lens: 32mm, f/8, ISO 400.
Camera Distance: Approximately 9 metres, camera height 1.0 metres above the hull plating, held level, hard-mounted to the hull.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. She stands braced thirty metres back from the bow, feet wide, knees bent, torso leaning about twenty-five degrees forward into a slow shove, one gloved hand on the guard rail.

ENVIRONMENT / BACKGROUND: The forward spine of the 240-metre hauler — 26 metres wide, exactly 2.0-metre plating, 1.1-metre rail, 3-metre lamp masts every 20 metres. At the bow, the ring of eight crush cylinders, deployed twelve metres forward and nine metres in diameter, is being compressed: the cylinders have folded to about six metres and are still shortening. Pressed against them, filling the entire upper frame, the flank of the tanker: plain oxidised grey, 34 metres in diameter, its six rib bands spaced 24 metres apart now enormous, three dim red standby beacons still blinking, no windows, no lit cockpit, no markings, no engine plume. Approximately 10 percent of the rust-brown planet limb is still open at upper left; the rest is blocked by the tanker's hull. The gap between the two hulls is zero — this is the contact instant, closing speed twelve metres per second at first touch. The hull plating, panel size, rail height and lamp mast spacing are identical to the previous scene; only the light and the distance have changed.

THE VIRAL MOMENT / REVEAL: Two enormous hulls are touching at the speed of a running person. The twelve-metre crush ring is collapsing toward three metres over one and a half seconds; a single one-second burst of white-hot metal particles sprays outward from the contact line in straight lines, cooling to dull orange and vanishing — no flame, no fireball, no smoke, because there is no oxygen. Exactly six 2.0-metre hull panels have broken free of the crush zone and are tumbling away in straight lines. Everything else on both ships is intact: the spine, the rails, the lamp masts, the tanker's rib bands and beacons are all whole and undamaged.

COMPOSITION: Vertical 9:16. She stands left of centre between roughly fifty-two and seventy-three percent of frame height, clear of the outer right eighth. The compressing crush ring and the contact line sit between roughly twenty-six and thirty-six percent — the brightest event in the frame and the only saturated light. The tanker's flank fills everything between roughly thirteen and twenty-six percent and reads as a ceiling. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only lit hull plating.

LIGHTING: Cold white lamp pools on matte plating, plus one short-lived hard white light from the shearing metal at the contact line, throwing sharp unfilled shadows back down the walkway for one second only. Three dim red beacons above. No bloom, no halo, no lens flare, no glow, no fire light.

PHYSICS: Hard vacuum and free fall. RIGID BODY COLLISION: the two hulls meet surface to surface and neither passes through, phases through or merges with the other. The crush cylinders absorb the closing speed by folding, not by exploding. Both hulls decelerate together at about a quarter of one g for one and a half seconds — a firm shove, not a jolt; the camera is bolted to the same hull and therefore does not shake. Exactly six panels are freed and they travel in dead straight lines at walking pace, tumbling slowly, never arcing and never slowing. There is no fire, no smoke and no sound.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships. Exactly six freed panels. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, locked off at 9 metres, camera height 1.0 metres above the hull plating, dead level, bolted to the hull. The camera does not move at all and does not shake at any point. Real-time motion at normal playback speed.

At 0s — Low and wide down the lit walkway. A braced graphite-grey figure stands thirty metres back from the bow, one hand on the rail. The whole top of the frame is the flank of a grey ribbed hull, twenty-four metres away and closing at twelve metres per second.
At 2s — CONTACT. The bow's twelve-metre ring of eight crush cylinders meets the tanker's flank. No flash of flame, no fireball: a one-second spray of white-hot metal particles fires outward from the contact line in straight lines and cools through dull orange to nothing.
At 2.5s — The cylinders fold. Twelve metres becomes nine, then six, the deformation smooth and enormous, both hulls staying whole.
At 3.5s — The crush finishes at three metres. Exactly six 2.0-metre hull panels tear free of the crush zone and tumble away in dead straight lines, slowly rotating, never slowing.
At 4s — The shove reaches her: the deck accelerates under her boots at about a quarter of one g and she leans twenty-five degrees into it, magnetic soles holding, one hand tight on the rail. The camera, bolted to the same deck, does not move relative to her.
At 5.5s — The push ends. She straightens. Nothing is burning; there is no smoke anywhere; the sparks are already gone.
By 8s — The two hulls rest against each other, still and locked, the six panels still receding. No cuts within the shot.

Exactly one human in this shot. Exactly two ships and exactly six freed panels; both hulls stay whole and neither passes through the other. No fire beyond the one-second spark burst, no smoke at any time, no engine plume. Everything moves at normal speed — the collision is not slowed down. No slow motion. No camera shake.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 5 — İKİ DAKİKA SONRA

_"Artık iki gemi yok. Tek bir şey var ve hiçbir yere gitmiyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 5 of 6. Solo female salvage engineer orbital collision film.
Lens: 32mm, f/5.6, ISO 800.
Camera Distance: Approximately 7 metres, camera height 1.4 metres above the hull plating, held level, hard-mounted to the hull, pulling back.

SUBJECT: A 34-YEAR-OLD WOMAN salvage engineer in a matte graphite-grey hard-shell EVA suit — warm olive skin with clearly visible pore texture, a small pale scar through her right eyebrow, dark brown eyes, thick dark eyebrows, a chapped lower lip, faint tiredness under her eyes, natural facial asymmetry, black hair pulled back flat under a soft white skullcap. Photographed as a real person, not CGI. She is 1.68 metres tall. Her helmet is one piece of optically clear glass with zero tint, zero mirror coating and zero reflection of the environment; her whole face is fully readable through it at every head angle, with a faint crescent of breath haze along the lower inside edge. The suit is matte graphite grey with two dull safety-yellow bands at the shoulders, scuffed pale dust marks on both knees and forearms, and a blank faded chest patch carrying no letters, digits or symbols. The suit has NO back-mounted unit: no backpack, no tank, no hose, no cable, no rear housing of any kind — her back silhouette is flat. Her gloved hands carry no tool, no instrument, no bag, no tether and no line of any kind — she never carries anything that is not a fixed part of the ship. Her boots are locked flat to the hull plating by magnetic soles. She stands still and upright near the sealed hatch, arms loose at her sides, head tipped back, calm.

ENVIRONMENT / BACKGROUND: Two minutes after contact. The hauler's spine — 26 metres wide, exactly 2.0-metre plating, 1.1-metre rail, 3-metre lamp masts every 20 metres — with the circular hatch at frame left now sealed: a flat unlit plate with a visible seam ring where a warm rectangle of light used to be. At the bow, thirty metres ahead, the crush ring is a compressed three-metre stub of folded cylinders, and resting against it, motionless, the flank of the tanker: 34 metres in diameter, six rib bands 24 metres apart, three dim red standby beacons still blinking in sequence, no windows, no lit cockpit, no markings, no engine plume. The two hulls now read as ONE joined silhouette against the star field. Six 2.0-metre hull panels are far away and still receding in straight lines, small tumbling squares against the stars. Zero percent of the rust-brown planet limb is open — it is fully behind the tanker now, and the only light left is the hauler's own. The hull plating, panel size, rail height and lamp mast spacing are identical to the previous scene; only the light and the distance have changed.

THE VIRAL MOMENT / REVEAL: Nothing is burning. Nothing is falling. Nothing is making a sound. Four hundred metres of ship met at running speed and the aftermath is a single dark shape, three red lights blinking on schedule, and six squares drifting away forever in perfectly straight lines.

COMPOSITION: Vertical 9:16. She stands right of centre between roughly fifty-six and seventy-four percent of frame height, clear of the outer right eighth; the sealed hatch sits at frame left at roughly sixty-five percent. The joined silhouette of the two hulls fills the frame between roughly thirteen and forty-seven percent. The six receding panels are small and scattered in the star field between roughly fifteen and thirty percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only lit hull plating.

LIGHTING: Only the hauler's cold white lamp pools, hard-edged on matte plating, and the three dim red beacons. No planetshine, no warm light anywhere, no fire light, no bloom, no halo, no lens flare. The shadows are absolutely sharp and unfilled.

PHYSICS: Hard vacuum and free fall — no smoke, no haze, no scattering, no fire. The two hulls are in rigid contact and travelling together; neither is deforming any further. The six freed panels move in dead straight lines and tumble at a constant slow rate; they never arc, never slow and never stop.

NEGATIVE: Exactly one human in the entire frame. Exactly two ships, joined. Exactly six freed panels. no second person, no crew, no figure in any window, no human reflection, no third ship, no satellite, no station, no fireball, no flame, no fire, no burning hull, no smoke, no smoke trail, no engine plume, no exhaust, no thruster flash, no visible light beam, no lens flare, no bloom, no glow filter, no halo, no atmospheric haze, no dust cloud, no debris cloud, no fragmenting hull, no structural disintegration, no hull passing through another hull, no slow motion, no camera shake, no miniature look, no toy look, no CGI look, no waxy skin, no text, no letters, no digits, no serial numbers, no hull markings, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, one slow continuous pull-back from 7 metres to 22 metres, camera height 1.4 metres above the hull plating, level, hard-mounted to the hull. Real-time motion at normal playback speed.

At 0s — The lit walkway, a sealed circular hatch at frame left with a visible seam ring and no light behind it, and a woman standing upright beside it with her arms loose and her head tipped back. Ahead, the two hulls rest against each other, motionless.
At 2s — The camera begins pulling slowly back. Nothing is burning. There is no smoke. The compressed three-metre stub of the crush ring holds the two ships together.
At 4s — Far out in the star field, six small tumbling squares recede in dead straight lines, slowly rotating, never slowing.
At 5.5s — The tanker's three red beacons blink in sequence, exactly as they did before contact. The dead ship has not noticed anything.
At 7s — The pull-back opens the frame: one joined silhouette of four hundred metres of ship, one small figure standing on it, six panels leaving, and a dense unblinking star field behind everything.
By 8s — The panels are still receding and the beacons still blinking. Nothing settles. No cuts within the shot.

Exactly one human in this shot. The two hulls stay whole and joined; exactly six panels are drifting and no new debris appears. Nothing burns, nothing smokes, no engine plume anywhere. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🔁 LOOP SATIRI (0:48 → 0:00)

Kaynak: `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §5

```
① KADRAJ EŞLEŞMESİ: S5'in son beat'i (32mm, geniş, figür alt üçte bir,
   üstünde bir kütle) ile S0'ın ilk beat'i (32mm, geniş, figür alt üçte
   bir, üstünde boş yıldız alanı) aynı kadraj ailesindendir. Aynı lens,
   aynı figür yerleşimi, aynı yön.
② DEĞİŞEN TEK ŞEY GÖKYÜZÜ: S0'da üstü boş, S5'te üstü dolu. İki imaj yan
   yana konduğunda filmin tamamı okunur — açılış-kapanış çifti tek karar
   olarak verildi [§2.3 ③].
③ HAREKET DURMAZ: son karede altı panel hâlâ uzaklaşıyor, üç fener hâlâ
   yanıp sönüyor. Poz yok, donma yok.
④ IŞIK SÜREKLİLİĞİ ÇELİŞKİSİ VE ÇÖZÜMÜ [§5 ⑤]: S0'da gezegen ışığı %100,
   S5'te %0. Loop kadrajla değil KOMPOZİSYONLA kurulur; renk farkı kesmeyi
   "aynı yörüngenin yeni turu" gibi okutur. Bu bir tasarım kararıdır ve
   burada yazılıdır.
⑤ SES: müzik 48. saniyede çözülmez; S5'in düşük dronu S0'ın açılış
   dronuyla aynı perdededir (bkz. müzik promptu).
```

---

## 🎶 MÜZİK PROMPTU (Tek Global Tema — 48 sn)

Araç: Suno / Udio · tek parça · 48 saniye · söz yok, geleneksel melodi yok.

```
48-second minimalist score for a scene with no air, no vocals, no lyrics, no traditional melody. TWO SOUND WORLDS, never mixed: 1. AIRBORNE — a very low sub-bass drone, wide and clean, standing for what the camera sees. 2. STRUCTURE-BORNE — dry, close, metallic resonance conducted through solid steel: creaks, low bar-like tones and a deep hull groan, with no reverb tail and no air around them, standing for what the character actually hears through her boots.

Dynamic arc: 0-8s the sub-bass drone alone, steady and patient, with one faint metallic tick every four seconds. 8-16s the drone gains a slow second harmonic; the metallic ticks come slightly closer together. 16-24s a rising sub-bass pressure with no percussion and no riser effect — the low end simply gets wider and heavier. 24-32s the pressure thins to a single sustained low note; everything else drops away. 32-34s the note continues, then AT 34.0 SECONDS EVERYTHING STOPS: one and a half seconds of absolute digital silence, no tail, no reverb, no fade — the collision is silent. 35.5-40s the structure-borne world takes over alone: one deep conducted hull groan, dry and close, low metal resonance settling and ticking as it cools, no air, no reverb. 40-48s a slow wide low drone returns at the same pitch as the opening drone, with one soft sub-bass pulse every two seconds matching a blinking beacon, and the track ends without any cadence or resolution — it must be able to run straight back into its own beginning.

Mood: patient, enormous, unhurried, matter-of-fact. Reference feel: the sustained low patience of Éliane Radigue and the dry structural writing of Jóhann Jóhannsson. Do not quote, sample or reproduce any melody, motif or lyric from either.

NO vocals, NO lyrics, NO choir, NO melody, NO drums, NO percussion, NO braam, NO riser, NO impact hit at the collision, NO reversed cymbal, NO whoosh, NO orchestral swell, NO explosion sound, NO air-based ambience.
```

> ⭐ **Filmin tek ses kararı 34,0. saniyededir:** izleyicinin bütün hayatı
> boyunca öğrendiği şey, o boyutta bir çarpışmanın bir SES çıkarmasıdır.
> Parça tam o anda 1,5 saniye mutlak sessizliğe geçer. Depoda "vuruş
> anında hit koymamak" ilk kez bilinçli bir tasarım kararı olarak yazıldı.
> Ayrıntı: `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 (spotting §14).

---

## 🖼️ KAPAK PROMPTU (1080×1920)

⚠️ **Bu görsel videoya GİRMEZ** — yalnızca thumbnail [Ders 61].

> **Kaynak an: S4.** Kapağın tek sınavı 120 px testidir. Bu karede 120
> px'te okunan şey bir KARŞITLIKTIR: altta ince, aydınlık bir metal şerit
> ve üstünde onu ezen kocaman koyu bir kütle; ikisinin değdiği yerde tek
> bir beyaz çizgi. İnsan figürü 120 px'te yalnız bir nokta olarak okunur
> ve ölçeği o nokta verir.

```
Cinematic photorealistic vertical cover image, 1080x1920, 9:16. Hard vacuum, low orbit,
night side of a planet. No sun in frame.

A flat lit metal walkway 26 metres wide, plated in exactly 2.0-metre squares with a
1.1-metre guard rail and 3-metre lamp masts every 20 metres, runs away from the viewer
into black. A single 34-year-old woman salvage engineer in a matte graphite-grey
hard-shell EVA suit with two dull safety-yellow shoulder bands stands braced on it,
small, leaning about twenty-five degrees forward, one gloved hand on the rail, her
helmet a single piece of optically clear glass with zero tint and zero mirror coating
so her face is fully readable. Her back silhouette is flat: no backpack, no tank, no
hose, no cable. Photographed as a real person, not CGI.

Filling the entire upper two thirds of the frame, pressing down like a ceiling, is the
flank of an automated tanker: a plain oxidised-grey cylinder 34 metres in diameter with
six rib bands spaced 24 metres apart and three dim red standby beacons, no windows, no
lit cockpit, no markings, no engine plume. At the bow, thirty metres ahead of her, a
ring of eight crush cylinders is folding under the contact, and along the contact line
a single one-second spray of white-hot metal particles fires outward in straight lines.
No flame, no fireball, no smoke — there is no oxygen. Both hulls are whole; exactly six
2.0-metre panels have broken free and tumble away in straight lines.

COMPOSITION: The tanker's flank occupies the frame between roughly thirteen and thirty
percent of frame height; the white contact line sits at roughly thirty-two percent, dead
centre horizontally; the woman stands left of centre between roughly fifty-two and
seventy-three percent. A dense unblinking star field fills the remaining sky. Nothing
story-critical falls in the top 254 pixels, the bottom 484 pixels, or the right 242
pixels; those bands are covered by platform UI.

LIGHTING: Cold white lamp pools with knife-sharp edges on matte plating, one short hard
white light at the contact line, three dim red beacons. No bloom, no glow filter, no
lens flare, no halo, no fire light, no visible light beam.

NEGATIVE: Exactly one human, no second person, no crew, no figure in any window, no
human reflection. Exactly two ships, no third ship, no satellite, no station. No
fireball, no flame, no fire, no smoke, no engine plume, no exhaust, no thruster flash.
No debris cloud, no fragmenting hull, no structural disintegration. Not miniature, no
toy look, no CGI look, no waxy skin. No text, no letters, no digits, no hull markings,
no flag, no logo, no HUD overlay, no watermark.

Output: 9:16, 1080x1920, no text, no watermark.
```

**120 px testi:** küçültüldüğünde okunması gereken tek şey → *aydınlık ince
bir şerit, onu ezen kocaman koyu bir kütle, değme noktasında tek beyaz
çizgi.* Yüz ve kuşaklar okunmazsa sorun değil; **kütle bir "gemi" gibi
okunmaya başlıyorsa ya da kadranda alev/duman belirmişse kapak
başarısızdır, yeniden üret.**

> Kapak denetimi 120 px posta pulu testiyle elle yapılır (KAPAK_QA rubriği 12.08.2026'da kaldırıldı).

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ

**Başlık alternatifleri (≤40 karakter):**

```
1. Uzayda çarpışma neden sessizdir?
2. 400 metre, yürüme hızında çarpıştı
3. Duyacağın en büyük ses hiç çıkmadı
```

**Açıklama (ilk satır kancadır):**

```
İki gemi saniyede 12 metreyle buluştu — koşan bir insanın hızıyla.
Ateş bir saniye sürdü, ses hiç çıkmadı. Vakumda çarpışma böyle görünür.
#uzay #fizik #bilimkurgu #shorts #ai
```

**Sabitlenecek yorum:** "Yörüngede iki büyük yapı genelde saniyede birkaç
metre hızla buluşur; vakumda oksijen olmadığı için alev bir saniyeden fazla
yaşamaz ve ses hiç yayılmaz. Çarpışmayı duyan tek şey, gövdeye değen
botlardır. 🛰️"

---

## 🔒 Master Cinema Lock

```
Photorealistic live-action cinematography, Kodak Vision3 color science,
natural film grain, no digital sharpening. Vertical 9:16 native framing.
One spherical lens per shot (32mm or 75mm), no anamorphic, no horizontal
flare; camera distance and height stated in metres, camera never higher
than 1.6 metres above the hull plating, hard-mounted to the hull. Single
continuous 8-second takes, 0 cuts, one camera move maximum per shot and
five of the six shots fully locked off. Real-time motion at normal
playback speed — no slow motion ever, including the collision. Hard
vacuum: no smoke, no haze, no atmospheric scattering, no engine plume, no
fire beyond one 1.0-second spark burst in one shot. Rigid body collision:
no hull passes through another hull; both hulls stay whole and exactly six
2.0-metre panels are freed in the whole film. Exactly one human in every
frame; both ships are automated, windowless and crewless. The suit has no
back-mounted unit and the visor is optically clear with zero mirror
coating. No text of any kind on screen or on any hull at any moment.
```

---

## 📋 QA SPEC BLOĞU — üretim bitince QA promptlarına kopyalanır

```
FILM: THE QUIET IMPACT (dikey shorts)
FORMAT: 9:16 · 6 sahne × 8 s = 48 s · sahne başına 1 kesintisiz çekim, 0 kesme
İNSAN SAYISI: 1 (6/6 sahne) · iki gemi de insansız, penceresiz
DIALOGUE LINES: 0 · SILENT SCENES: 6
CANLI: yok · SU: yok · DİYALOG: yok
GEMİ: 2 — yük gemisi 240 m (omurga 26 m, panel 2,0 m, korkuluk 1,1 m,
      lamba direği 3 m / 20 m arayla) · ölü tanker 160 m (çap 34 m,
      6 kuşak / 24 m, 3 kırmızı fener / 40 m)
ÇARPIŞMA: yaklaşma 12 m/s sabit · temas S4'ün 2,0. saniyesinde ·
      tampon 12 m → 3 m / 1,5 sn · ivme 0,25 g / 1,5 sn ·
      serbest kalan nesne TAM 6 panel, düz çizgide
ATEŞ: TAM 1,0 saniye (yalnız S4) · duman 0 kare · itki alevi 0 kare
MESAFE TAKVİMİ: S0 750 m → S1 575 → S2 400 → S3 220 → S4 0 → S5 0 (kilitli)
IŞIK: gezegen kavsi %100 → 85 → 60 → 30 → 10 → 0 (tek yönde kapanır);
      lamba havuzları 6/6 sabit; güneş hiçbir karede yok
LENS: 32mm (S0,S2,S3,S4,S5) · 75mm (yalnız S1)
KAMERA: S0-S4 lockoff · S5 pull-back 7→22 m · yükseklik ≤1,6 m ·
      gövdeye vidalı, çarpma anında dahil sıfır sarsıntı
CENTRAL CHOICE: S3 — kaldıraç 90° (5,0-6,5 sn); bedel AYNI KAREDE
      (kapak 4,0. saniyede mühürleniyor)
VIRAL INTERSTITIALS: yok (6 sahnenin 6'sı anlatı) — KESİLEMEZ sahne: S4
YASAKLAR: ateş topu · duman · itki alevi · parçalanma · enkaz bulutu ·
      üçüncü gemi · mürettebat · ağır çekim · kamera sarsıntısı · metin
```

---

## ✅ Tutarlılık Kontrol Listesi

```
□ Karakter bloğu 6 görsel promptta birebir aynı mı?
□ "no back-mounted unit … back silhouette is flat" 6/6 promptta var mı? [D79]
□ "optically clear … zero mirror coating … fully readable" 6/6 var mı? [D79]
□ Mesafe takvimi 750 → 575 → 400 → 220 → 0 → 0 sırasını izliyor mu?
□ "closing at a steady 12 metres per second" S0-S3'ün 4 görsel promptunda
  var mı; S4 temas satırını, S5 kilitli gövdeyi mi taşıyor?
□ Gezegen kavsi yüzdesi tek yönde kapanıyor mu? (100→85→60→30→10→0)
□ Gemi ölçek sayıları (1,68 / 2,0 / 26 / 1,1 / 3 / 20 / 34 / 24) her
  görsel promptta AYNI mı? [D32]
□ "no slow motion" 6 video promptunun 6'sında var mı? [D12/44 — 1 numaralı tuzak]
□ "no camera shake" S4 dahil 6/6 var mı? Kamera "gövdeye vidalı" yazıyor mu?
□ Ateş yalnız S4'te ve tam 1,0 saniye mi? Başka hiçbir sahnede alev/duman
  /itki alevi geçiyor mu? [Kural 11]
□ "exactly six" panel sayısı S4 ve S5'te aynı mı; başka enkaz var mı? [D38]
□ "no hull passing through another hull" S4'te var mı? [D17]
□ "Exactly one human" 6/6 promptta var mı; iki gemi de penceresiz mi? [Kart 4]
□ Hiçbir promptta su, canlı, bulut, rüzgar, toz bulutu var mı?
□ Hiçbir figür alt 1/4'e ya da sağ şeride giriyor mu?
□ Ekranda metin süresi 0,0 saniye mi? Gövdelerde rakam/harf/seri no var mı?
□ Loop satırı yazıldı mı; S5 son beat ↔ S0 ilk beat kadraj ailesi aynı mı?
□ Üretim S4'ten (temas) başladı mı? S4 temiz çıkmadan diğer sahneler
  üretilmedi mi? Sonuç KAPI KAYDI'na yazıldı mı? [D74]
■ ELLER: 6 sahnenin 5'inde boş — S3'te iki el gövdeye sabit kaldıraçta.
  ⚠️ Bu kutu BİLEREK işaretsiz bırakıldı: sistem promptunun "eller her
  zaman boş" kuralından bilinçli sapmadır, gerekçesi filmin bedelli
  seçimidir [Ders 78 ② · THE SLOW STONE emsali].
```

---

## 🧪 ÜRETİM ÖNCESİ KONTROL — 03_PLAN_ONCESI_KONTROL_LISTESI.md

```
ÜRETİM ÖNCESİ KONTROL — THE QUIET IMPACT              tarih: 06.08.2026

A1 ✅ "no text" ile ekran içeriği aynı dosyada YOK — bu filmde hiç ekran,
      gösterge, sayaç arayüzü yok; sayaç ÇEVRESEL (mesafe + kuşak sayısı +
      gezegen kavsinin kapanma yüzdesi), üçü de metinsiz [Kart 5]
A2 ✅ sahne sayısı: başlık 6 = blok 6 = "Scene N of 6" 6
A3 ✅ süre: 6 sahne × 8 s = 48 s = iddia edilen süre
A4 ✅ yasaklı sahne tipi taraması yapıldı:
      · biniş/iniş/airlock geçişi → S3'te kapak KADRAJDA ama eşik hiç
        geçilmiyor, biniş hareketi hiçbir sahnede kadraja alınmıyor
        — D69 ① gereği (06.08)
      · loş iç mekâna giriş → yok, film 6/6 dış mekân
      · aynalı-yansıtıcı yüzey → yok; vizör berrak, iki gövde de MAT ve
        yansıtmıyor (promptta yazılı) [D20 · D69]
      · türetilmiş optik fenomen novum → yok; taşıyıcı iki katı gövde [D73]
      · yokluk novum → "sessizlik" pozitif olgularla render ediliyor
        (ateş 0 kare, duman 0 kare, düz çizgide enkaz, yanıp sönen fener) [D76]
      · jenerik/başlık kartı → yok, kapak videoya girmez [D34 · D70 · D72]
B1 ✅ doruk anı S4'ün İÇİNDE, 2,0. saniyede tarif edildi — sahne arasına
      düşmüyor (Tidal Hunt hatası)
B1b —  katmanlı dünya değil; yine de IŞIK TAKVİMİ yazıldı (%100→0, monotonik)
B2 ✅ bedelli seçim S3 (kaldıraç), kayıp AYNI SAHNEDE görülüyor (kapak
      4,0. saniyede mühürleniyor) ve S5'te sonucu duruyor (sönük kapak)
C  ✅ sayısal kilitler: insan 1×6 · kask 6/6 kapalı · ölçü 8 sayı ·
      yerçekimi 0 g + manyetik bot · sıvı yok · canlı yok ·
      + bu filme özel: 12 m/s · 12→3 m · 1,5 sn · 0,25 g · 6 panel · 1,0 sn ateş
D  ✅ risk sayımı: 4/9 (kask · ikinci figür · sayaç · parçacık-patlama)
      → "en riskli malzemeyi bir sahneye hapset" uygulandı: ateş yalnız
        S4'te ve 1,0 saniye
E  ✅ QA SPEC bloğu yazıldı (yukarıda)
```

---

## 🚪 KAPI KAYDI [DERS 74]

> Kapı koşulmadan bir sonraki adıma geçilmez ve **sonuç bu tabloya
> yazılmadan kapı koşulmuş sayılmaz.** Wrong Shadow'da bu tablonun ilk iki
> satırı boş kaldı ve novumsuz 64 saniye iki QA merceğine kadar geldi.

| # | Kapı | Ne ölçülür | Batma ölçütü | Durum |
|:--:|---|---|---|:--:|
| 1 | **Tek-kare fizibilite** [D73 ②] | S4 GÖRSEL promptu tek başına koşulur | karede ateş topu · yanan gövde · parçalanan kaplama · üçüncü cisim · birbirinin içinden geçen gövde · 6'dan fazla serbest panel | ⛔ KOŞULMADI |
| 2 | **Ölçek kapısı** [D32] | S0 ve S4 karelerinde panel 2,0 m ↔ insan 1,68 m oranı | oran iki karede farklıysa | ⛔ KOŞULMADI |
| 3 | **S4 video kapısı** | S4 video promptu, 8 s | ağır çekim · kamera sarsıntısı · 1 sn'den uzun ateş · duman | ⛔ KOŞULMADI |
| 4 | **Kurgu kapısı** [D70/72] | kurgu süresi ve klip sayısı | 6 klipten farklı · 48,000 s'den sapma · jenerik kartı · doruk kurguda yok | ⛔ KOŞULMADI |

**Kapı 1 batarsa Plan B:** temas anı I2V start-frame kilidine alınır — S4'ün
kabul edilmiş TEK görseli başlangıç karesi olarak verilir ve video yalnız
ezilme + kıvılcım + 6 panel hareketini ekler. Plan B'yi çalıştırmak opsiyon
değil, kapının çıktısıdır [D76 ③].

---

## 🎥 ÜRETİM NOTLARI

```
DURUM: yazıldı, üretilmedi (06.08.2026).
Üretim sırası: S4 → (temiz çıkarsa) S3 → S0 → S2 → S5 → S1.
Gerekçe: en pahalı ve en kırılgan kare önce; S4 batarsa kalan 5 sahne
hiç üretilmez ve Plan B'ye geçilir.
```

---

**🛰️ THE QUIET IMPACT — Sessiz Çarpışma**
_"İki gemi yürüme hızında çarpıştı. Kimse duymadı."_
