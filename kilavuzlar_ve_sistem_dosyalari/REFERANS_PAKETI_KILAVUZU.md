## 🎫 KAPI KARTI — REFERANS PAKETİ        (06.09.2026 · gövde aşağıda, ek'tir)
```
NE ZAMAN:   PLAN bitti, PROMPT yazılıyor · İLK KARE ÜRETİLMEDEN ÖNCE (KAPI 0)
KURAL 1:    Altı tetikleyiciden BİRİ doğruysa paket ZORUNLU. Eski sayım
            kuralı ("ikiden fazla insan ya da araç") ÖLDÜ: onu hiç tetikleme-
            yen THE STANDING WIRE biçim kilidini kaybetti [D146].
              → KAPI: LİSTE paket §0 — altı kutudan biri işaretlenmeden paket
                yazılmaz · AGENTS Kart A
KURAL 2:    Paket AYRI DOSYADIR: <FILM>_REFERANS_PAKETI.md. Planın İÇİNDEKİ
            blok koşulmaz [D117]; ad film önde [D160/⑪.0].
              → KAPI: LİSTE AGENTS Kart A "yazımı tamam" satırı
KURAL 3:    Bir varlığın referansı ONAYLANIP seed'i yazılmadan o varlığın
            geçtiği hiçbir sahne üretilmez. Sıra: PAKET → doruk → merkezî
            seçim → hook [D168].       → KAPI: LİSTE paket §2 · §7 ⑪
KURAL 4:    Modele SAYFA yüklenmez, KIRPILMIŞ TEK VARLIK yüklenir; sayfa
            insan gözü ve arşiv içindir. ⚠️ DEPO TERSİNİ YAZDI, ölçüm yok
                                       → KAPI: LİSTE paket §5 KIRPIM sütunu
KURAL 5:    Başlangıç karesi varken video promptu GÖRÜNÜŞÜ yeniden yazmaz;
            kamera·eylem·çevre yazar. Negatif çekirdek (D79) istisnadır.
              → KAPI: BETİK ⑳b — yalnız DEĞİŞİM yarısını ölçer · gerisi GÖZ
KURAL 6:    Kimlik metne YIĞILMAZ, görselde kilitlenir: tek pencerede en çok
            3 kişi özniteliği [D167].     → KAPI: BETİK ⑲ (⚠️ FIX verir,
              BLOCK değil — 06.09'da referans promptunda fiilen koşuldu)
OKUMA:      Gövdeyi AÇ eğer: ① yeni film yazıyorsan · ② bir varlığın biçimi
            iki klipte farklı çıktıysa · ③ üretim ortasında tasarım
            değiştiyse · ④ insan dışı canlı ya da tekrar eden olay varsa.
BİLİNEN YANLIŞ: ⛔ Paketin VARLIĞINI ölçen BETİK kapısı YOKTUR — üçüncü
            prompt tipi yazılmadı [T12.4①]; bugün kapı LİSTE ve GÖZDÜR.
            §4.1 kare bantları depo ölçümüdür, OPTİMUM sınanmadı (⚙️).
            §4.3'ün yükleme kuralı dört pakete AYKIRIDIR ve ölçülmedi.
            §5.3 dış çizelgesi ve §6.2 makine eşikleri TUR 12'de DÜŞTÜ.
```

---

# 🧷 REFERANS PAKETİ KILAVUZU

> **Bu dosya tek bir ders yüzünden var: D146 — biçim kilidi metinle
> tutulmuyor.** Üç ölçülmüş vaka: **THE SKYLIGHT** (bible optiği ve sırtı
> kilitledi → 1 filmde 3 farklı kask) · **YERÇEKİMİ F2** (vizör geometrisi
> dokuz promptta ÖLÇÜYLE yazılı → kubbe çıkan 6 klibin 5'inde tam tarif
> vardı; ⭐ kilidin OPTİK yarısı 6/6 tuttu, GEOMETRİ yarısı 0/6) · **THE
> STANDING WIRE** (SPEC "kubbe DEĞİL", betik GO verdi → 24 klibin ezici
> çoğunluğunda kubbe; dersin kendi satırı ölçtü: *referans paketi yoktu,
> üretilmiş panel 0*). D146'nın borcu "cümleden ARACA" yazılı; **araç bu
> dosyadır.**
>
> **Bedel ölçüldü.** THE SINKING STAKE'in QA kaydında iki satır yan yana:
> *"② SIRA · referans paketi HİÇ ÜRETİLMEDİ → çapa yok"* ve *"🟠 DEVAMLILIK ·
> göğüs paketi tasarımı S13'te değişiyor."* Filmi kapatan olay bu değildi
> (kapatan politika reddiydi [D167]); ekranda kaybedilen devamlılık buydu.
>
> ⛔ Bu kılavuz nasıl ÇİZİLECEĞİNİ değil, **neyin KİLİTLENECEĞİNİ** anlatır.
> Prompt iskeleti `IMAGE_VIDEO_PROMPT_TEMPLATES.md` · kapak `KAPAK_...` ·
> seed `SAHNE_DEVAMLILIK` §6 · ölçü dili `UZAY_USSU` §1 · giysi kimliği
> `ASTRONOT_DONANIM`. Hiçbiri burada tekrar anlatılmaz.

**Sayı yok.** Kaç filmin paketi olduğu tek yerde durur —
`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh` · ⬜ sayaç bu satırı **henüz
vermiyor**. Dış kaynak **TUR 12** (`URETIM_ONCESI_ANALIZ/15_...` →
`TUR12_HAM_RAPORLAR/`); ⚠️ o turun sayı katmanı çürüktü — aşağıda yalnız
**depoda ölçülmüş** ya da ⚙️ damgalı satır vardır.

---

# 1. 🚦 TETİKLEYİCİ — paket ne zaman zorunlu

| # | TETİKLEYİCİ | Bu depoda ölçülen karşılığı | Kayda giren |
|:--:|---|---|---|
| **T1** | Ayırt etme kanalı KAPALI: kask · vizör · basınç giysisi | D79 · D146 — yüz kanalı kapanınca kimlik siluete ve donanıma düşer | RK1… |
| **T2** | Biçim kilidi metinle tutulmayan varlık | D146'nın üç vakası (vizör geometrisi · kask kabuğu) | ilgili varlık |
| **T3** | Oranı sözle yazılamayan nesne: araç · istasyon · mimari | ölçek birimi **1H** → `UZAY_USSU` §1 · §5.3 | RA · RB · RI |
| **T4** | İnsan dışı canlı | `UZAYLI_VARLIK_TASARIM` §4 zaten zorunlu tutuyor (HEALING GROUND uyguladı: 3 referans / 7 panel) | RV |
| **T5** | Tekrar eden insan dışı olay: toz cephesi · kırağı · gaz sütunu | D147 kir merdiveni metinle tutmadı · SINKING STAKE gaz sütununu VARLIK saydı (RG) | RO |
| **T6** | Bir varlık kadrajda tekrar tekrar dönüyor ve iki klipte farklı çıktı | D84 — üç çapa da 42/42 promptta yazılıydı, üçü de kırıldı | ilgili varlık |

```
⭐ SONUÇ, DÜRÜSTÇE: T1 bu deponun neredeyse her filminde doğrudur → PAKET
   İSTİSNA DEĞİL, VARSAYILANDIR. Soru "paket yazılacak mı" değil, "HANGİ
   VARLIK kayda girecek"tir. Kod atama §2 kanonundadır.
⛔ ÖLEN KURAL: KILAVUZ_REHBERI'nin iki yerindeki "(+ REFERANS_PAKETI — iki
   insandan veya iki araçtan fazlası varsa)" satırı bu tabloyla DEĞİŞİR.
   İki ölçüm: STANDING WIRE tek insanlıydı, kuralı hiç tetiklemiyordu ve
   D146'nın 3. vakası oldu · SINKING STAKE tam iki insan / tam iki araç
   taşıyordu, kural harfiyen tetiklenmiyordu, paketi YİNE yazdı (gerekçe o
   paketin §0'ında: "ayırt etme kanalı renk değil GEOMETRİ").
⛔ T6'ya SAYI YAZILMADI: dış raporun "4-5 klip"i kaynaksızdı → §5.3.
⭐ MİNİMUM SET — dördü de ölçülmüş bir arızayı kapatır: ① sahne→referans
   eşleme tablosu [D84] · ② varlık sayfaları + seed [D146] · ③ palet ve
   malzeme kilidi · ④ durum merdiveni [D147]. ⛔ "ŞUNLAR ATLANABİLİR" listesi
   yazılmadı: dış raporun saydıkları (çağrı kâğıdı · lojistik formu · dikiş
   dosyası · storyboard) bu depoda hiç var olmadı (T12.1).
```

# 2. 📦 VARLIK ENVANTERİ — kim kendi kaydını hak eder

| Varlık sınıfı | Kod | Kayıt? | BELGEDE metin olarak kalır | Yalnız GÖRSELDE kilitlenir | Önlediği arıza |
|---|:--:|:--:|---|---|---|
| Kasklı insan | `RK1·RK2` | ✅ | gövde oranı · rol şeridi rengi ve YERİ · sayılabilir öğe adedi · vizör en-boy | kumaş dokusu · dikiş · mikro valf · yıpranma dağılımı | kasklı figürler arası kimlik kaybı |
| Araç | `RA·RB` | ✅ | 1H cinsinden oran · lüle/kapı/pencere ADEDİ · amblem yeri | kaplama malzemesi · panel çizgileri | kütle dalgalanması |
| İç mekân | `RI1·RI2` | ✅ | tavan yüksekliği (1H) · armatür adedi · kapı yeri | yüzey dokusu · pratik ışık sıcaklığı | aynı kabinin daralıp genişlemesi |
| Dış mekân | `RD` | ✅ | ufuk yüksekliği · TEK ışığın azimut/yükseklik değeri | zemin dokusu · gök gradyanı | sahne başına başka gezegen |
| Tekrar eden olay | `RO` | ✅ | yön · kademe sayısı · süre | yoğunluk · saydamlık · düşüş izi | aynı dünyada iki fizik |
| İnsan dışı canlı | `RV` | ✅ | uzuv SAYISI · insana göre boy oranı | kabuk dokusu · renk | kütle kayması, uzuv sayısı oynaması |
| El aleti / prop | `RP` | ⚠️ | eldiven ölçeğine göre oran | biçim | yalnız INSERT'te taşıyıcıysa kendi kaydını alır |

```
⭐ AYRIMIN KURALI (T12.3): SAYILABİLEN ve YER BELİRTEN bilgi BELGEDE kalır ve
   prompta iner · DOKUNSAL ve SÜREKLİ bilgi yalnız GÖRSELDE kilitlenir. "Üç
   dairesel valf" sayıdır, model sayar; "fırçalanmış titanyumun iplik yönü"
   anlamsal gürültüdür ve sapar.
⛔ METRE PROMPTA İNMEZ: ölçü SPEC/PLAN'da metre, prompt gövdesinde GÖVDE BOYU
   — `UZAY_USSU` §1 [D45 · D138]. Bu kılavuz o kuralı tekrarlamaz, uyar.
⛔ PALET prompta HEX inmez: belgede kod, promptta MALZEME + RENK ADI ("mat
   kiremit kırmızısı polimer plaka"). ⛔ RENK SAYISINA TAVAN YAZILMADI —
   "3 ana + 2 vurgu" kaynaksızdı (T12.1). Depo emsali SAYIYA değil BAĞA
   dayanır: THE UPHILL DARK turuncuyu TAM ÜÇ YERE bağladı (iki skafandr ·
   yük kayışı · atma kolu) ve S19'dan sonra kadrajdaki tek turuncu iki insan.
⛔ ROL ŞERİDİ · METİNSİZ AMBLEM · SIRT SİLUETİ burada tarif edilmez:
   `ASTRONOT_DONANIM`. Burası yalnız KAYDA girişini yazar.
⭐ Kod kanonu (COLD BURN şeması): panel `RA p4` · durum `RA-K2`. ⛔ Kod yerine
   ÖZEL AD yazılmaz — ne dosyada, ne kartta, ne promptta [D34]. ❌ Kapak
   envantere girmez: ayrı dosya, RK onaylandıktan SONRA.
```

# 3. 🪜 DURUM MİMARİSİ — çift mi, merdiven mi

| Tip | Ölçüt | Birim | Kademe | Yazım | Örnek |
|---|---|---|:--:|---|---|
| **DURUM ÇİFTİ** | değişim ANLIK bir anahtarsa | ikili | 2 | `_ACIK/_KAPALI` | `RK1_KASK_KAPALI` |
| **DURUM MERDİVENİ** | değişim BİRİKİYORSA, geri dönmüyorsa | kaplanan alan yüzdesi | 3 (K0·K1·K2) | `-K0/-K1/-K2` | `RK1-K2` (sırt tozlu) |
| **SAYAÇ** | değer sayısal ve okunuyorsa | filmin kendi birimi | — | kademelenmez, **metne devredilir** | teleskopik kademe 3→2→1 |

```
① MERDİVEN TEK YÖNLÜDÜR — K2'den K1'e dönüş yok; model kabinde bible'a
   dönüp kiri sıfırlıyor [D147 · D84: "2:29 kumlu → 2:40 tertemiz"].
② HER KADEMENİN KENDİ PANELİ ⚙️ SINANMAMIŞ: tek panelde iki durum özne
   karışması üretir (dış gerekçe). ⚠️ Depo TERSİNİ yazdı — BLUE DRIFT üç
   durum çiftini, UPHILL DARK ikisini bilerek aynı sayfaya koydu (gerekçe ve
   bedel o dosyaların §0'ında); iki film de ÜRETİLMEDİ, sonuç ÖLÇÜLMEDİ.
   ⬜ Ölçülene kadar DEPO PRATİĞİ geçerlidir.
③ FAZ IŞIĞI AYRI SATIRDIR: aynı kabinin "beyaz" ve "kırmızı alarm" hâli iki
   kayıttır (`THE_SLOW_STONE` RI p2 karanlık ↔ p3 tavan paneli).
④ KADEMENİN DEĞİŞTİĞİ SAHNE I2V ÜRETİLİR [D84 ①]. ⛔ İKİ DEPO KURALI
   ÇELİŞİYOR ve ölçüm yok: D84 ① / D42 ① / `KESINTISIZ_VIDEO_URETIM_TEKNIGI`
   klibin SON karesini sonrakinin başlangıcı yapar; `YERCEKIMI` paketi "her
   faz MASTER'dan" der. Bu kılavuzun aldığı taraf: kademe İÇİNDE zincir,
   kademe DEĞİŞİRKEN master (§7.1). ⬜ ölçüm borcu.
```

# 4. 🖼️ SAYFA KANONU
## 4.1 Reçete tablosu — bantlar depo ölçümü, OPTİMUM ⚙️ sınanmadı

| Varlık | Kare | Görünümler | Zemin | Işık |
|---|:--:|---|---|---|
| Kasklı insan | 4-6 | ön · 3/4 · profil · **arka** · (kask makro) · (vizör ardı yüz CU) | nötr mid-grey seamless | eşit nötr key + yumuşak dolgu + **kask içi lokal ışık** |
| Araç | 4-5 | ön · profil · tepe · 3/4 üst · (lüle/temas makro) | nötr mid-grey düz | yumuşak tepe + alttan yansıma |
| İç mekân | 4 | merkezden dört ana yön | yok (kapalı geometri) | ⭐ **sahnenin kendi ışığı** · her faz AYRI PANEL |
| Dış mekân | 3 | geniş kurulum · orta bağlam · zemin dokusu | gök/ufuk | ⭐ **filmin TEK ışığı** |
| Kahraman prop | 3 | ön · 3/4 · eldivenle arayüz makro | nötr mid-grey | ürün ışığı, net dolgu |
| Tekrar eden olay | 3-4 | biçim · kadans · **tek düşüş davranışı** | saf siyah | yönlü sert ışık |
| İnsan dışı canlı | 3-7 | ön · 3/4 · profil · arka · (tepe) · (alt) · uzuv | nötr mid-grey | düşük açılı yüzey ışığı |

```
⭐ SAYILARIN KAYNAĞI DEPODUR: UPHILL DARK 5 sayfa × TAM 4 panel · BLUE DRIFT
   5 × 4 · COLD BURN 6 / 28 · SINKING STAKE 6 / 24 · YERÇEKİMİ 6 × 4 ·
   HEALING GROUND 3 / 7. Dış raporun sabit "6·5·4·3·3·3·7" tablosu kişisel
   bir blogdan çıkmıştı (T12.1) ve ALINMADI. Parantezli görünümler KOŞULLU —
   yalnız sahne listesinde o açı varsa üretilir (kamera ağırlıkla sabit).
⭐ REÇETENİN EKLEDİĞİ İKİ KARE DEPONUN ARIZA YERİDİR: ARKA GÖRÜNÜM [D79 ·
   D139] ve VİZÖR ARDI YÜZ CU [D146'nın tek aday aracı].
⭐ IŞIK VARLIK SINIFINA BAĞLIDIR (T12.3 · BELGELENMİŞ): kimlik varlığı nötr
   mid-grey + eşit key; MEKÂN varlığı sahnenin kendi ışığında. ⛔ Kelvin ve
   %gri DEĞERİ YAZILMADI — sekiz paketin dördü 5000K yazıyor, dördü
   yazmıyor; paket kendi değerini künyesine yazar.
⛔ DIŞ MEKÂN NEDEN İSTİSNA: gezegenin TEK ışığı kimliğin kendisidir (SINKING
   STAKE 000° azimut / 34° yükseklik, 25/25 sahnede aynı); nötr stüdyo ışığı
   o kimliği siler.
⛔ D79 SAYFAYA DA İŞLER: opak/altın/aynalı vizör YASAK, yüz HER KAFA AÇISINDA
   okunur; kask içi lokal ışık bunun aracıdır ve dış ortam ne kadar karanlık
   olursa olsun kareye YAZILIR. ⛔ "seamless visor" yazılmaz — çerçevesizlik
   kubbe davetiyesidir [D146]. Marka/tescilli tasarım adı girmez, biçim
   GEOMETRİYE çevrilir (`MESHUR_SAHNE_KALIPLARI` §4).
```

## 4.2 Tek sayfa mı, ayrı kare mi — karar ÇİZİMDEN ÖNCE verilir
```
1) Kareyi kim okuyacak? İNSAN (onay·arşiv) → TEK SAYFA · MODEL → 2
2) Yüksek frekanslı ince detay (mikro valf, örgü)? EVET → AYRI TAM KARE;
   panelde çözünürlük düşer (`YERCEKIMI` §0 "panel sayfasının bedeli")
3) İki figür benziyor mu? boy kıyaslaması yan yana TEK sayfa · KİLİTLEME için
   AYRI kare (yan yana kilitlemek doku bulaştırır)
4) SAYFANIN EN-BOY ORANI FİLMİN ORANINA EŞİTLENİR — dikey hatta paket yok.
⛔ "kamera yayı 60° dilim" KURALI YAZILMADI: dış raporun kendi açı tablosu
   45°'lik adım kullanıyordu, ikisi çeliştiği için sayı düştü (T12.1).
```

## 4.3 ⭐ YÜKLEME KURALI — paketin ölçülmemiş tek büyük kararı
```
KURAL: MODELE YÜKLENEN ŞEY SAYFA DEĞİLDİR: tek varlık, kırpılmış, kareye
yakın. Sayfa onay ve arşiv belgesidir.
① Sayfa üretilir → paneller KIRPILIP ayrı dosya olur → sahneye kırpılmış
  panel yüklenir. ② Sayfaya YAZI yazılmaz (etiket·ölçü·başlık·ok = 0); panel
  adı DOSYA ADINDA durur. ③ Zıt ışıklı iki referans aynı üretime verilmez.

DEPODA ÖLÇÜLEN YARI: panel oluğu ve her etiket/ok/ölçü çizgisi çıktıya SIZIYOR
(`YERCEKIMI` §0 üç önlem · `THE_BLUE_DRIFT` · `THE_UPHILL_DARK`); nötr zemin
bir SIZINTI ÖNLEMİDİR ve sekiz paketin altısında uygulanmış.
⚙️ DIŞ MEKANİZMA, BU HATTA DOĞRULANMADI: açık kaynak görüntü kodlayıcıları
girdiyi merkezden kırpıp 224 px'e (bir varyantta 336) indiriyor; konu kadrajın
küçük bir kesrindeyse kimlik ön işlemede kayboluyor. ⛔ Veo/Flow'un ön işleme
çözünürlüğü HİÇBİR resmî belgede yok; "64×64 altında kimlik çöker" eşiği atıf
verilen çalışmada geçmiyor (o çalışma YAŞ TAHMİNİ hatası ölçüyor) — sayı
KAPIYA YAZILAMAZ [T12.1 · D142].

⚠️ DEPO TERSİNİ YAZDI — DÖRT PAKETTE: COLD BURN · UPHILL DARK · BLUE DRIFT
   ve SLOW STONE *"sayfanın TAMAMINI yükle — tek panelden güçlü çapa"*
   diyor. Dördü de ÜRETİLMEDİ, iddia ÖLÇÜLMEDİ. ⬜ Bu çelişki sayıyla değil,
   tek A/B koşusuyla kapanır (§AÇIK İŞLER). Kural o güne kadar ÖNERİDİR.
```

# 5. 🔗 KULLANIM KONTRATI
## 5.1 Sahne → referans eşleme tablosu (zorunlu kolonlar)

| Sahne | İç/Dış + ışık fazı | Yüklenecek KIRPIM (+panel) | Görünüm | Durum kademesi | Metne devredilen |
|---|---|---|---|---|---|
| S12 | İÇ · kırmızı alarm | `RA p5` · `RK1 p6` | 3/4 ön | `RA-K1` | jest · kumaş dalgalanması · kıvılcım |

```
· "Metne devredilen" kolonu BOŞ BIRAKILAMAZ: referansın taşıyamadığı her şey
  (anlık eylem, geçici yansıma, hareket) buraya yazılır. Bölüm dosyalarındaki
  `📎 REFERANS` satırı bu tablonun kopyasıdır.
· Bir sahnede EN ÇOK 3 KAYIT yüklenir — `VEO` §6 md.2. ⛔ "kapalı sistemlerde
  varlık tavanı 2-3" satırı ALINMADI: kaynaksızdı ve bir sağlayıcı tersini
  söylüyor (T12.1). Dördüncü varlık kadraj dışına alınır ya da metne
  devredilir — PLAN kararıdır, üretimde çözülmez.
· Flow'da referans `@ETİKET` ile çağrılır, etiket D34 gereği KOD olur
  (@RA · @RK1). ⚙️ SINANMAMIŞ — bu hatta hiç denenmedi.
```

## 5.2 Başlangıç karesi kontratı

| Prompta GİRER | Prompta GİRMEZ | Gerekçe |
|---|---|---|
| kamera satırı (I2V'de zorunlu) | öznenin görünümü: renk · kumaş · yüz · kask biçimi | görsel çapa piksel düzeyinde kısıtlıyor; tekrar tarif özne karışması üretir |
| öznenin eylemi (fiil) | *"ilk karedeki özneyi koru"* türü cümleler ⚙️ | iki taraf da ölçmedi — `VEO` §6B bunu çekirdek sayıyor; PROB konusudur |
| çevresel dinamik (toz·buhar·titreşim) | referansla ÇELİŞEN atmosfer/ışık | çelişki kumlanma ve yanma üretir |
| durum kademesi ADI (`-K2`) | kademenin GÖRSEL tarifi | kademe zaten panelin kendisidir |

```
⛔ İKİ İSTİSNA — depoda ölçüldü, dış kaynak bunları bilmez: ① NEGATİF
   ÇEKİRDEK KALIR — D79'un pozitif cümleleri ("flat back silhouette" · "face
   fully readable at every head angle") her promptta durur; YERÇEKİMİ'nde
   OPTİK yarı 6/6 tuttu, tutan yarı budur. ② Depo kimlik çapası bloklarını
   60 promptta birebir taşıdı (COLD BURN); ⚙️ kısaltmanın etkisi ölçülmedi
   ve ölçülmeden blok silinmez.
⭐ DEĞİŞİM KURALI: değişim içeren sahnenin başlangıç karesi değişimin
   ÖNCESİDİR — model sağlamı bozar, bozuğu geri kuramaz. KAPI ⑳b [D179];
   dış rapor bunu bağımsız DOĞRULADI, yeni bilgi getirmedi.
⭐ VEO §6 ↔ §6B ÇELİŞKİSİ §6B LEHİNE KAPANIR: "kimlik özniteliklerini metne
   TEKRAR yaz" yalnız çoklu-referans (ingredients) modundadır; onaylı ilk
   kare varken geçersiz. Yan kazanç: D167 red yüzeyi düşer.
```

## 5.3 ⛔ YENİDEN ÇAPALAMA ÇİZELGESİ — YAZILMADI · 5.4 SEED
```
Dış rapor "kasklı sabit kamerada 4-5 klip · dinamik eylem 1-2 · araç 3-4 ·
açık yüz 2-3 · grup 1" çizelgesi verdi; ALINMADI (T12.1): tek sayının kaynağı
yok, rapor kendi tahmin damgasını bu tabloda vurmadı, ve çizelge KLİP-ZİNCİRLİ
bir hattı varsayıyor — burada her sahne KENDİ onaylı imajından üretilir,
sürüklenme klipten klibe birikmez. ✅ Yerine koşan: faz başı kimlik yenileme
(`YERCEKIMI`: her faz master'dan) + §6.1 ⑨ kare çıkarma göz kapısı.
SEED: aynı seed + aynı metin + aynı referans aynı gürültü kalıbını verir,
piksel kopyası DEĞİL; metin değişince biçim yeni metne bükülür. ⛔ "%99"
oranı ALINMADI, kaynaksızdı. ⚙️ Flow'da seed arayüzde gizli ve ALANIN VARLIĞI
ÖNCE SINANIR — yoksa "seed dolu" kapısı doldurulamaz bir alanı zorunlu kılar
[D142]. Alan varsa SEED kolonu doldurulur; boş kolon "üretilmedi" demektir.
⬜ `SAHNE_DEVAMLILIK` §6.1'in "piksel düzeyinde devamlılık" satırı değişmeli.
```

# 6. ✅ KABUL KAPISI
## 6.1 BUGÜN koşabilenler (python3 · bash · ffmpeg 8.1 · göz)
```
① DOSYA KAPISI      <FILM>_REFERANS_PAKETI.md var mı · film klasöründe mi
② ÇAPRAZ BAĞ ⚙️     her kod envanterde var mı · her kayıt en az bir sahnede
                    çağrılıyor mu (çağrılmayan = YETİM: silinir ya da
                    gerekçelenir). python3 + markdown, ML yok — betiği YOK
③ SEED KOLONU       🔴 ZORUNLU işaretli her satırda seed dolu mu (§5.3 ön koşulu)
④ PANEL ARİTMETİĞİ  künye toplamı = tablo toplamı (sapma varsa GEREKÇE yazılı)
⑤ SIFIR YAZI        sayfada etiket/ok/ölçü çizgisi/başlık: göz sınavı, 0
⑥ KAPALI UÇLU SINAV her sayfa için TEK KELİMEYLE cevaplanan 3 soru yazılıp
                    cevaplanır: "vizör kaç panel?" · "göğüste kaç modül?" ·
                    "şerit hangi kol?"  ⛔ "kask güzel mi" sınav değildir
                    [D144: KABUL · RET · YABANCI GÖZ · SONUÇ]
⑦ İKİ FİGÜR         benzeyen iki sayfa YAN YANA bakılır; ayırt edilemiyorsa
                    İKİSİ DE reddedilir [D69 · COLD BURN · YERCEKIMI RC p3]
⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — ayrım yalnız renge
                    dayanıyorsa panel reddedilir. Kapı olarak yazılmadan
                    ÖNCE mevcut bir panelde fiilen koşulur [D142]
⑧ 120 px TESTİ      posta pulu boyunda amblem/rol şeridi ayırt ediliyor mu
                    [`KAPAK_...`]. ⛔ Dış raporun "%10 · 64×64 px · 3:1 luma"
                    değerleri atıf verdiği kaynakta YOK (o kaynak testi NİTEL
                    veriyor) — depoda ölçülmüş tek eşik 120 px'tir
⑧b KRİTİK AYRINTI ⚠️ şerit/göğüs paneli teslim karesinde ≥12-14 px sürüyor mu;
                    sürmüyorsa devamlılık kanıtı değildir, yük siluete geçer.
                    BELGELENMİŞ ama AKTARIM (Johnson 1958 · 6,4 ±1,5 çizgi
                    çifti · termal optik) → katı ret olmadan SINANIR [D142]
⑧c BAŞPARMAK/ÖLÇEK  iki benzer figür filmin EN GENİŞ kadrajının ölçeğinde
                    ayrılıyor mu · araç/mimari yanında 1H şahidi var mı
⑨ KARE ÇIKARMA      `ffmpeg -i <klip> -vf fps=1` → kare onaylı panelle YAN
                    YANA bakılır (üretim sonrası göz kapısı)
⑩ BAYT AYNILIĞI ⚙️  paketteki kimlik bloğu ile onu taşıyan sahne promptu
                    `shasum -a 256` + `diff` ile karşılaştırılır; paketler
                    "kelimesi kelimesine aynıdır" yazıyor, kimse ölçmedi
⑪ GÖRSEL ÖZETİ ⚙️   onaylanan her referans görselinin SHA-256'sı seed
                    tablosuna yazılır, üretimden önce yeniden hesaplanır
```

## 6.2 ⛔ MAKİNE EŞİKLERİ — İKİ AYRI SEBEPLE DÜŞTÜ
```
Dış raporun tablosu (ArcFace >0,65 · LightGlue >%85 · SAM 2 IoU >0,88 ·
LPIPS <0,15 · ΔE <2,5 · YOLO "text"=0 · DINOv2 >0,80) ÖNERİ olarak da
yazılmaz:
① EŞİKLER UYDURMA — altısı da atıf verilen çalışmalarda geçmiyor; ArcFace ve
   LPIPS kabul eşiği yayımlamaz, YOLO'nun stok 80 sınıfında `text` YOK (komut
   olduğu gibi koşulsa kapı HER ZAMAN geçer) [T12.1]. ② KOŞMAZ — bu makinede
   ArcFace/SAM2/LightGlue/YOLO/LPIPS yok, ffmpeg'in vidstabdetect'i bile
   kurulu değil [D142]. Yerine §6.1 ⑥ · ⑦b · ⑨ koşar.
```

# 7. ♻️ YAŞAM DÖNGÜSÜ VE GEÇERSİZLİK

| Durum | Giriş | Çıkış | Bloke olan |
|---|---|---|---|
| TASLAK | kod atandı, prompt yazıldı | §6.1 kapılarından geçti | o kodu çağıran TÜM sahneler |
| ONAYLI | kapılar geçildi, seed yazıldı | geçersiz kılan olay (§7.2) | yok |
| GEÇERSİZ | §7.2'den bir olay | yeni sürüm ONAYLI olur | o kodu çağıran tüm sahneler |

```
ÜRETİM SIRASI: PAKET (KAPI 0) → doruk → merkezî seçim → hook → gerisi;
dramatik sıra üretim sırası değildir [D168].
⛔ FAZ/KADEME DEĞİŞİRKEN üretilmiş kare YENİ ÇAPA olarak geri verilmez —
   `YERCEKIMI` paketi bunu yazılı kural yapıyor ("çapa imajı bir önceki fazın
   çıktısından DEĞİL, bu dosyadaki master'dan"). Kaç döngüde koptuğuna SAYI
   YAZILMADI, dış tahmindi (T12.1). ⭐ AYNI kademe içinde D84 ①'in zinciri
   geçerlidir (§3 ④).
KÜNYE: pakete "üreten sistem + sürüm + tarih" yazılır; sürüm değişimi
   aşağıdaki geçersizlik olayıdır, o alanların KENDİSİ doğru envanterdir.
```

**GEÇERSİZLİK OLAYLARI** — biri olursa sayfa TASLAK'a düşer ve o kodu
çağıran sahneler kilitlenir: ① tasarım revizyonu (sahip geri bildirimi) ·
② model/araç sürümü değişti (onaylı çapalar göz kapısından yeniden geçer) ·
③ oran/çözünürlük değişti 16:9 ↔ 9:16 (paket reddedilir) · ④ sağlayıcı
varlığı düştü (yerel kopya devreye girer — paket YEREL saklanır).

**Emsal:** THE SINKING STAKE revizyon 1 (02.09.2026) — araç değişti, `RA`
4→5 panel yeniden yazıldı, `RB` 1→2 ve öncelik 🟡→🟠, *"RA/RB onaylanmadan
S4 üretilmez"* satırı kondu; bedel sıfır oldu, çünkü üretilmiş dört sahnede
(S0-S3) araç yoktu. **Doğru yapılmış tek geçersizlik vakası budur.**

## 7.3 Üstünlük kuralı
```
BİÇİM çeliştiğinde ONAYLI GÖRSEL > paket metni > sahne prompt metni;
gerekçe dış eşik değil D146'nın üç ölçümüdür. SAYI ve OLAY çeliştiğinde
PLAN üstündür (aritmetik planda yaşar).
⛔ Çelişki AYNI GÜN kapatılır: iki belge birlikte yaşarsa üçüncü bir gerçek
   doğar ve promptlar ikisini de kaybeder.
⛔ AMORTİSMAN SAYISI YAZILMADI ("15-20 iterasyon · 4-5 sahnede öder"):
   raporun kendi tahmin damgasını taşıyordu ve depo bunu kendi sekiz
   paketinden ÖLÇEBİLİR (T12.4⑤).
```

# 8. 🛡️ KİMLİK YAZIMI VE POLİTİKA
```
⭐ TEK TEZ: PAKET POLİTİKA RİSKİNİ DÜŞÜREN BİR ARAÇTIR. THE SINKING STAKE 25
   imaj promptunun 25'inde kişi başına YEDİ öznitelik taşıyordu (boy·gövde·
   ten·saç rengi·saç biçimi·yüz işareti·yaş); OMNI *"can't depict some public
   figures"* diyerek reddetti [D167 · red defteri 15]. O yedi öznitelik
   promptta, çünkü kilitlenecek GÖRSEL yoktu.
KURAL: tek pencerede EN ÇOK 3 kişi özniteliği → KAPI ⑲. ⚠️ Betik ≥4'te
       FIX verir, BLOCK değil — 06.09.2026'da referans promptu üzerinde
       fiilen koşuldu ve altı öznitelik saydı.
KURAL: ayırt etme BİYOMETRİDEN GEOMETRİYE taşınır — gövde oranı · sırt
       teçhizatı · rol şeridinin KOLU · vizör en-boy · göğüs paketi.
       (SINKING STAKE'in doğrusu: boy 188↔165 · göğüs boyunduruk↔düz ·
       kalça dört cep↔sarılı halat; üçü de o paketin §0'ında.)
KURAL: gerçek kişi · milliyet · kurum · marka: sıfır → `POLITIKA_...` §2 ·
       yasak yazma MALZEMEYİ TARİF ET [D123]; referans promptu da ⑯'dan geçer.
KURAL: belirsiz sıfat GÖVDE-GÖRELİ yazılır — "büyük tank" değil, "a cylinder
       about as wide as her shoulders". ⛔ Rakam/birim prompt gövdesine
       girmez [`UZAY_USSU` §1 · D45 · D138].
```

# ⬜ AÇIK İŞLER
```
⬜ "iki insandan/araçtan fazlası" kuralı §1 tablosuyla değişecek:
   KILAVUZ_REHBERI satır 165 · 345 + `.claude/skills/yeni-film/SKILL.md` 34.
⬜ sayac.sh'ye "paketi olan film · seed dolu" satırı — sayı elle yazılmaz.
⬜ prompt_kontrol.py'de paketin VARLIĞINI ölçen kapı yok. ⭐ 06.09.2026'da
   ÖLÇÜLDÜ: `### 📸 IMAGE PROMPT` başlıklı referans sayfası DOSYA modunda
   normal imaj promptu gibi denetleniyor (⑯ ⑮ ⑲ D79 uzunluk) ve `## SAHNE n`
   taşımadığı için DİZİ kapılarına (⑩ ⑪ ⑬) GİRMİYOR — istenen davranış budur.
   ⛔ TEK KOŞUL: İngilizce prompt başlıktan sonraki İLK çitli blok olmalı;
   künye bloğu araya girerse betik YANLIŞ bloğu ölçer ve BLOCK verir.
   §6.1 ② çapraz bağ ile ⑩ bayt aynılığı hâlâ yazılmadı — D146'nın borcu.
⬜ 10-20 dk hattındaki üç paket `REFERANS_PAKETI.md` adıyla duruyor —
   D160/⑪.0 gereği `<FILM>_REFERANS_PAKETI.md` olacak.
⬜ ÖLÇÜM BORCU — tek A/B koşusu iki soruyu kapatır: (a) sayfanın tamamı mı,
   kırpılmış panel mi (§4.3; dört paket tersini yazıyor)? (b) aynı sayfada
   iki durum bulaşıyor mu (§3 ②)? Aynı sahne, iki yükleme biçimi, göz kapısı.
⬜ DÖRT KAPI YAZILMADAN ÖNCE FİİLEN SINANACAK [D142]: hex kapısı (prompt
   gövdesinde altı haneli renk kodu → BLOCK) · gri ton basamağı ⑦b · Flow
   arayüzünde seed alanının varlığı · @ETİKET söz dizimi.
⬜ İNSAN DIŞI VARLIĞIN KİMLİK MEKANİZMASI sorulmadı: dört araştırma da kimliği
   İNSAN üzerinden sordu. Bir ARACIN kimliği kartla mı, saf görsel çapayla mı,
   salt geometriyle mi tutulur — bilinmiyor; bu deponun bir kısım filminde baş
   varlık ARAÇTIR. ⬜ PANEL MALİYETİ de ölçülmedi (kademe başına panel · ışık
   fazı başına panel · dikey hatta ikinci sayfa); ölçüm sekiz paket üzerinden.
```
