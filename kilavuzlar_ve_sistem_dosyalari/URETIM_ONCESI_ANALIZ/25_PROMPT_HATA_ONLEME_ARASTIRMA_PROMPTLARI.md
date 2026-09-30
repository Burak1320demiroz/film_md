# 🔬 25 — PROMPT HATA ÖNLEME · ÜÇ DERİN ARAŞTIRMA PROMPTU (19.09.2026)

> ✅ **KOŞULDU — 19.09.2026.** Ham: `TUR22_HAM_RAPORLAR/` (3 rapor) ·
> Süzgeç: `04_ARASTIRMA_BULGULARI.md` §TUR 22 · İndiği yer:
> `../PROMPT_HATA_ONLEME_KILAVUZU.md` §1a · §2 · §2b · §3b · §4 · §5b.
> ⭐ Turun ayırt edici yanı: raporun her sınanabilir iddiası deponun **771
> bulgusuna** karşı koşuldu. Bir tez doğrulandı (negatif temas cümlesi korumuyor),
> bir tez çürütüldü (ortam adı sayıdan kritiktir), ÖLÇÜLMÜŞ etiketlerin yaklaşık
> üçte biri sözleşme ihlali nedeniyle düşürüldü.

> **Ne bu dosya:** `PROMPT_HATA_ONLEME_KILAVUZU.md`'nin **cevabı olmayan üç
> sınıfı** için ÜÇ derin araştırma promptu. Her biri **altı cümledir**, her cümle
> **tek satırdır** ve **salt prompt** çalışır — kopyala, araştırma aracına yapıştır,
> başka hiçbir şey verme.
>
> | # | konu | ölçülen ağırlık | kılavuzun hangi bölümünü kapatır |
> |:--:|---|---|---|
> | 1 | **KATI CİSİM SINIRI** — el–nesne füzyonu, nesne–nesne geçişi, fazla parmak | ~50 bulgu · **20+ 🔴** · 7 film | §3 sınıf 2 · §4 "temas füzyonu" satırı |
> | 2 | **BEDENİN YÜKÜ** — efor, oran düşüşü, biriken yorgunluk, eldiven inceliği, sıfır-g hareket | **99 bulgu** (⑧ EFOR · deponun en üretken ikinci merceği) · 29 film | §3 sınıf 5 · `prompt_kontrol` ⑳'nin sertleşmesi |
> | 3 | **ORTAM YASASI** — vakumda ses, parçacık momentumu, tek yerçekimi rejimi | ~64 bulgu · 12 🔴 | §2 ortam cümleleri · §4 "vakumda ses" satırı |
>
> **Kaynak ölçüm:** `FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/` — **34 filmin 392 ham
> QA raporu, 750 tekil bulgu**, her bulgu o sahnenin prompt metnine karşı okundu
> (19.09.2026: ızgarası belgesiz üç film raporların kendi künyesinden ÖLÇÜLEREK eklendi).
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz; aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı, yoksa iki turun sonucu
> karşılaştırılamaz (07-24'ün gerekçesiyle aynı).

---

## ⭐ NEDEN BU ÜÇÜ — ve neden ötekiler DEĞİL

Kılavuzun on beş hata sınıfından üçü seçildi. Seçim gerekçesi ölçüm **ve** deponun
neyi zaten sorduğudur:

| sınıf | ağırlık | daha önce soruldu mu | bu turda |
|---|---|---|---|
| temas / katı cisim sınırı | 20+ 🔴 | ⛔ **hiç sorulmadı** (`23_` "temas" kelimesini 0 kez geçiriyor) | ✅ **1** |
| efor / bedenin yükü | **99 bulgu** | ⛔ **hiç sorulmadı** (`23_` "efor" 0 kez) | ✅ **2** |
| ortam yasası: ses | 12 🔴 | ⚠️ `23_` §7 sordu, **TUR 20 koştu** — ama çıkan kural yalnız *"AUDIO satırı her klipte + No dialogue. No music."*; dış ses yasasının TUTUP TUTMADIĞI cevapsız | ✅ **3** (daraltılmış yeniden soru) |
| ortam yasası: parçacık · yerçekimi | ~37 bulgu | ⛔ **hiç sorulmadı** (`23_` "parçacık" 0 kez) | ✅ **3** |
| jeton sızıntısı (`PHASE 1` · `EVA` · `rose` · **`S04`** · **`ORION`**) | 7 bulgu · **4 film** | ⚠️ **`24_` §1 cümle 3'te YAZILI, koşulmadı** | ⛔ yeniden yazılmaz — ⭐ ama **öncelik yükseldi**: 19.09 genişletmesi sınıfı 2 filmden 4 filme çıkardı ve SAHNE ETİKETİNİN (`S04`) basıldığını ölçtü |
| kimlik · giysi · nesne sürekliliği | ~38 bulgu | ⚠️ **`24_` §3'te YAZILI, koşulmadı** | ⛔ yeniden yazılmaz — `24_` koşulsun |
| metin yasağı × ekranlı tasarım | 8 🔴 | ⚠️ `24_` §1 + D50/D78 | ⛔ bu turda değil |

⛔ **Aynı soruyu iki dosyada iki kez sormak, iki turu karşılaştırılamaz yapar.**
`24_`'ün dört promptu koşulmadan bu üçü koşulabilir; sıra bağımsızdır.

---

## ⚠️ ARAŞTIRMAYA VERİLMEYEN ŞEY — ve neden

Promptlar **salt** çalışır: araştırma aracına bu deponun dosyaları, film adları,
ham raporları ya da ölçüm tabloları **verilmez**. Gerekçe `07-24` ile aynı:
araç depoyu görürse deponun dilini tekrar eder ve dışarıdan bilgi getirmez.
Deponun vakaları promptun **beşinci cümlesine** (kritik kısıt) soyutlanarak girer;
ham hâlleriyle aşağıdaki **SINAMA SETİ** bloklarında durur ve **cevap geldikten
sonra** ona karşı okunur.

---

# 1️⃣ KATI CİSİM SINIRI — el nesneye değince geometri neden çöküyor

```
Görüntüden-videoya çalışan güncel video üretim modellerinde (Google Veo 3.1 ve Gemini Omni 1.1 Flash öncelikli, ayrıca Kling, Runway Gen-4, Luma Ray, Pika, Hailuo, Wan ve Sora sürümleri karşılaştırma için) bir elin ya da eldivenin katı bir nesneye değdiği anda ortaya çıkan geometri bozulmasını araştır: parmakların nesneye erimesi ve kaynaması, nesnenin elin içinden geçmesi, fazla ya da eksik parmak, tutulan aletin biçim değiştirmesi ve iki katı cismin (kayış ile pim, egzoz ile iniş ayağı, halat ile kiriş) birbirinin içinden geçmesi — bu arızaların yayımlanmış teknik açıklamaları, model kartlarındaki bilinen sınır maddeleri, hakemli çalışmalar ve yöntemi yazılı bağımsız testler; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: arızanın üretim zincirinin neresinde doğduğu (ilk karedeki el pozu mu, hareket kestirimi mi, örtüşme ve derinlik sırası mı, kodlayıcının ince yapıyı koruyamaması mı), temas anının klipte nerede olmasının (0-2 saniye, ortada, son saniye) arıza oranını değiştirip değiştirmediği, temasın kadrajdaki ölçeğinin (el kare yüksekliğinin %10'u mu %60'ı mı) ve çözünürlüğün etkisi, elin hareket hızının ve kamera hareketinin etkisi, eldiven gibi kalın ve tek parça bir yüzeyin çıplak ele göre daha kolay mı yoksa daha zor mu tutulduğu, nesnenin biçiminin (ince uzun çubuk, halka, kumaş kayış, düz levha) ve tutuş tipinin (kavrama, iki parmak, avuç içi baskı, sürtünerek kaydırma) fark yaratıp yaratmadığı — iki yönlü, tutan ve çöken vakalar birlikte.
Sözcükle çözülüp çözülmediğini ayrıca sor: "no merging, no phasing, no extra fingers, hand-to-surface contact keeps a clear boundary" gibi olumsuz cümlelerin bu arızayı ölçülebilir biçimde azaltıp azaltmadığı, olumsuz cümlenin tersine o kavramı çağırıp çağırmadığı, aynı işi pozitif cümleyle yazmanın (görünür ara katman, tutamak kılıfı, halka, kemer tokası, iki parmak arasında görünen boşluk) sonucu değiştirip değiştirmediği, temas anının kasten perdelenmesinin (elin nesnenin arkasında kalması, kadrajın temastan hemen önce ya da sonra başlaması, aletin gövdeyle örtülmesi) belgelenmiş bir teknik olup olmadığı ve izleyici okunurluğuna bedeli.
Kadraj ve iş akışı tarafını topla: yapay zekâ film ekiplerinin el ve nesne temasını çekmek için kullandığı belgelenmiş kadraj kararları (temas öncesi ve sonrası iki ayrı klip, temasın kadraj dışında bırakılması, eli sabit tutup nesneyi hareket ettirme, teması tek bir statik yakın planda dondurma), ilk kareye temas hâlinde başlamak ile temassız başlayıp klip içinde temas kurmak arasındaki fark, ilk karenin temas noktasını ne kadar iyi kilitlediği, aynı promptun birkaç kez üretilip en iyisinin seçilmesinin (red-üret-seç) gerçek maliyeti ve kaç denemede bir temiz temas çıktığına dair sayısal veri.
Kritik kısıt: kullanım yeri, on saniyelik, kesmesiz, varsayılan olarak sabit kameralı, tek İngilizce promptla üretilen fotogerçekçi uzay bilimkurgu klipleridir; her klip ayrı üretilir ve kliplerin arası kurguda kesilir; karakter basınç giysili ve neredeyse her sahnede eldivenlidir; filmin olayı çoğu zaman elle yapılan bir iştir (kemer halkası, karabina, kayış, vana, kol, çekiç, halat) ve bu yüzden temas kadraj dışına atılamaz; prompt tek metindir, pozitif gövde 120-300 kelime ve ardından en çok on bir cümlelik olumsuz blok gelir, kadrajda olmayan hiçbir şey tarif edilmez; VFX kompozit, rotoskop, maske ve elle rötuş YOKTUR, yalnız kesme ve ses miksi vardır — bu yüzden 3B takip, el modeli, sonradan düzeltme ve kare kare rötuş öneren çözümleri "hat dışı" diye işaretle ama silme, tek prompt ve kadraj kararıyla uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) ARIZA tablosu — arıza biçimi (parmak erimesi, nesne geçişi, fazla parmak, alet morfu, iki cisim geçişi), doğduğu aşama, tetikleyen koşul, ölçülmüş oran varsa oranı, model ve sürüm, kaynak ve etiket; (b) ÖNLEM tablosu — önlem (olumsuz cümle, pozitif ara katman cümlesi, kadraj kararı, ilk kare kararı, tekrar üretim), İngilizce tam kalıp, ölçülmüş etkisi, yan etkisi ve okunurluk bedeli, model, kaynak ve etiket; (c) KARAR AĞACI — "sahnede el bir nesneye değiyor" girdisinden başlayıp hangi koşulda hangi önlemin seçileceğini söyleyen evet/hayır adımları, her adımın kaynağı ve etiketi; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bu çelişkiyi AÇIKLAMALI

```
Aynı cümle, iki zıt sonuç — cevabın açıklaması gereken şey budur:

  THE_COUNTED_TURN   temas cümlesi 22/25 promptta YAZILI  →  7 🔴 temas arızası
  THE_DRY_ANCHOR     temas cümlesi 14/14 promptta YAZILI  →  6 🔴 temas arızası
  BENI_HATIRLAMA     temas cümlesi 48/48 promptta YAZILI  →  2 🔴
  THE_FALLING_WORLD  temas cümlesi 46/48 promptta YAZILI  →  2 🟠
  THE_LEANING_ROOM   temas cümlesi 12/12 promptta YAZILI  →  1 🔴

  THE_FROST_LINE     temas cümlesi bulgunun düştüğü BEŞ sahnede YOK → 5 🔴

⛔ Cümlenin VARLIĞI arızayı durdurmuyor: yazılıyken de 🔴 çıkıyor.
   İlk iki filmin ortak özelliği: filmin OLAYI elle yapılan bir iş
   (kayış–karabina · çekiç–kazık). Cevap "hangi koşulda cümle tutmaz"ı
   söylemiyorsa kılavuz §4'ün "kadraj kararı" satırı hipotez kalır.

DEPONUN SINANMAMIŞ HİPOTEZİ: temas anı kadrajda TUTULAMAZ; ya perdelenir,
ya araya görünür bir katman (halka · sap kılıfı) konur, ya da temasın
öncesi ve sonrası gösterilip anı atlanır.
```

---

# 2️⃣ BEDENİN YÜKÜ — ağır iş neden bedene yazılmıyor, yorgunluk neden birikmiyor

```
Güncel video üretim modellerinde (Google Veo 3.1 ve Gemini Omni 1.1 Flash öncelikli, ayrıca Kling, Runway Gen-4, Luma Ray, Hailuo, Wan ve Sora sürümleri karşılaştırma için) insan bedeninin bir yükü taşıdığının görünmemesi arızasını araştır: ağır bir cismi kaldıran ya da çeken figürün sırtının bükülmemesi, omzunun düşmemesi, bacağının destek almaması, kavrayışın hiç gevşememesi, nefesin değişmemesi, hareket hızının iş boyunca hiç yavaşlamaması ve kalın basınçlı eldivenin çıplak el inceliğiyle hareket etmesi — bu arızaların yayımlanmış açıklamaları, model kartlarındaki sınır maddeleri, insan hareketi ve biyomekanik sadakatini ölçen değerlendirme çalışmaları (hareket gerçekçiliği ölçütleri, fizik sadakati kıyaslamaları) ve yöntemi yazılı bağımsız testler; model, sürüm, tarih ve bağlantıyla.
Mekanizmayı sök: modelin yükü nereden çıkardığı (nesnenin adı mı, boyutu mu, malzemesi mi, fiilin kendisi mi, ilk karedeki duruş mu), ağırlığı sayıyla yazmanın ("a 40 kg case") sıfatla yazmaya ("a heavy case") göre ölçülebilir bir fark yaratıp yaratmadığı, eforu SONUÇLA yazmanın ("the lever moves four centimetres in the first second and one in the last") beden tarifiyle yazmaya ("his forearm tightens, his shoulders drop") göre farkı, hareket hızının prompttan kontrol edilip edilemediği ve yavaşlamanın ağır çekime dönüşme riski, kamera ölçeğinin (yakın plan önkol, orta plan gövde, geniş plan tüm figür) efor okunurluğuna etkisi, on saniyelik bir klipte kaç ayrı beden işaretinin güvenle üretilebildiği — iki yönlü, tutan ve tutmayan kalıplar birlikte.
Yorgunluğun BİRİKMESİNİ ayrıca sor: birbirinden bağımsız üretilen ardışık kliplerde bir karakterin yorgunluk durumunun (nefes nefese kalma, duruşun gevşemesi, adımın kısalması, kirlenme, terleme, titreme) taşınmasının belgelenmiş yolları, ilk kare olarak verilen görüntünün yorgunluk durumunu ne kadar taşıdığı, durumun metinle numaralı bir merdiven olarak yazılmasının ("wear state three of four") işe yarayıp yaramadığı, bir kliptekiefordan sonraki klipte hiçbir iz kalmamasının (anlık sıfırlanma) bilinen bir sınır olup olmadığı ve bunu ölçen bir çalışma bulunup bulunmadığı.
Serbest uzuv ve temassız hareket tarafını topla: yerçekimsiz ya da düşük yerçekimli ortamda figürün havada yürüyor gibi bacak çırpması, gövdenin itilmeden dönmesi, ayakların zemine basmadan kayması, kolların dengelemek için havada açılması ve elin havada bir şeye uzanıp boşluğu kavraması gibi arızaların tetikleyicileri; hareketi bir TEMAS NOKTASINA bağlayarak yazmanın ("he pulls himself along the rail with his right hand, his boots never touch the deck") bu arızaları azaltıp azaltmadığı, itme ve tepki çiftinin promptta açıkça yazılmasının etkisi, ve bu ailenin arızalarının efor arızalarıyla aynı kökten gelip gelmediği.
Kritik kısıt: kullanım yeri, on saniyelik, kesmesiz, varsayılan olarak sabit kameralı, tek İngilizce promptla üretilen fotogerçekçi uzay bilimkurgu klipleridir; her klip ayrı üretilir ve bir filmde 12 ile 48 klip vardır, yani yorgunluk yalnız metinle ve ilk kareyle taşınabilir; karakter basınç giysili ve kasklıdır, çoğu filmde vizör berraktır ama bazılarında tamamen opaktır ve o filmlerde yüz hiçbir karede görünmez, yani efor yalnız gövdeyle okunur; prompt tek metindir, pozitif gövde 120-300 kelime ve ardından en çok on bir cümlelik olumsuz blok gelir; ağır çekim, hız rampası, VFX kompozit ve elle rötuş YOKTUR — bu yüzden hareket yakalama, 3B iskelet, fiziksel simülasyon ve sonradan hız ayarı öneren çözümleri "hat dışı" diye işaretle ama silme, tek prompt ve ilk kareyle uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) EFOR İŞARETİ tablosu — beden işareti (sırt eğrisi, omuz düşüşü, bacak desteği, kavrayış gevşemesi, nefes, hız düşüşü, titreme, duruş bozulması), promptta yazılışı (İngilizce tam kalıp), modelin uyma oranı varsa oranı, hangi kamera ölçeğinde okunur, model, kaynak ve etiket; (b) BİRİKEN BEDEL tablosu — durum (yorgunluk, kir, hasar, nefes), klipler arası taşıma yöntemi (metin merdiveni, ilk kare, referans görseli), ölçülmüş tutuş, kopma noktası, model, kaynak ve etiket; (c) TEMASSIZ HAREKET tablosu — arıza (havada yürüme, itmesiz dönme, kayan ayak, boşluğu kavrama), tetikleyici, önleyen İngilizce kalıp, model, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bu sınırı AÇIKLAMALI

```
Deponun en kalabalık bulgu kaynağı: ⑧ EFOR merceği tek başına **99 bulgu** yazdı (① KARE'den sonra deponun en
üretken merceği), 29 filmde efor cümlesi KISMİ.

  cümle HİÇ YOK   KRONOS_SON_SINYAL  96 promptta efor sözlüğü toplam 10 kelime  → 11 bulgu
                  THE_RESONANT_STRAND  efor cümlesi 5/14                        →  8 bulgu
  cümle VAR       SUSMAYAN_NOBETCI   ⑳ kapısı 0 BLOCK verdi, cümle yazılı       →  9 bulgu
                  THE_COUNTED_TURN   efor cümlesi 24/25                         →  6 🔴
                  THE_LOCKED_PULSE   efor cümlesi 24/25                         →  9 bulgu

⛔ ÖLÇÜLMÜŞ KAPI SINIRI: `prompt_kontrol.py` ⑳ kapısı cümlenin VARLIĞINI
   sayıyor, ŞİDDETİNİ ölçmüyor. "his forearm tightens" yazmak kapıdan
   geçiriyor ve ekranda hiçbir şey değiştirmiyor.

BİRİKME ARIZASI, birebir rapor cümleleri:
  "scene 24'teki kapasite scene 2 ile aynı"            (KRONOS · ⑧ 1/10)
  "physical state remains 100% rested across runtime"  (RESONANT_STRAND)
  "maximal strain instantly disappears into a completely relaxed posture" (STILL_SWARM)
  "Recovery Curve Honesty 2/10 — reset between Scene 7 and Scene 8" (DRY_ANCHOR)

TEMASSIZ HAREKET (⑭ merceği): "legs pedal in a walking cadence while suspended
in mid-air" (KRONOS S05 🔴) · "hands close on empty air 10 cm away" (LOOK_UP S05 🔴)
· "boots skate across deck plating without stepping weight" (KRONOS S14 · S24).

ARANAN CEVAP: efor cümlesi hangi BİÇİMDE yazılırsa tutar — beden tarifi mi,
sonucun sayısı mı, ikisi birden mi; ve yorgunluk klipler arası metinle
taşınabiliyor mu, taşınamıyorsa ne taşır.
```

---

# 3️⃣ ORTAM YASASI — vakumda ses, parçacık momentumu ve tek yerçekimi rejimi

```
Güncel video üretim modellerinde (Google Veo 3.1 ve Gemini Omni 1.1 Flash öncelikli, ayrıca Kling, Runway Gen-4, Luma Ray, Hailuo, Wan ve Sora sürümleri karşılaştırma için) kadrajın fiziksel ortam yasasına uymaması arızasını araştır: havasız ortamda hava yoluyla ses üretilmesi, parçacık ve enkazın momentum taşımadan havada donması ya da sıvı gibi kıvrılması, aynı kadrajda iki farklı yerçekimi rejiminin (biri yüzerken öteki yürüyor, yağmur gerçek zamanlı düşerken nesne ağır çekimde süzülüyor) aynı anda görünmesi ve düşen cisimlerin sahneden sahneye farklı ivmeyle düşmesi — bu arızaların yayımlanmış açıklamaları, model kartlarındaki sınır maddeleri, fizik sadakatini ölçen kıyaslama çalışmaları ve yöntemi yazılı bağımsız testler; model, sürüm, tarih ve bağlantıyla.
Sesi ayrı ve derinlemesine sök: yerel ses üretiminin promptun metninden mi yoksa üretilen görüntünün anlamından mı türediği, "no exterior sound", "silent", "vacuum carries no sound", "only suit-borne sound" gibi cümlelerin ölçülebilir biçimde tutup tutmadığı, olumsuz ses cümlesinin tersine o sesi çağırıp çağırmadığı, sesi tamamen kapatan ya da sessiz klip üreten bir anahtar, parametre veya yüzey bulunup bulunmadığı, üretilen sesin ayrı bir kanal olarak alınıp alınamadığı ve alınamıyorsa dış ses katmanının kurguda güvenilir biçimde ayıklanmasının bilinen yolları, ayrıca aynı promptun tekrar üretiminde ses davranışının ne kadar kararlı olduğu — iki yönlü, tutan ve tutmayan vakalarla.
Parçacık ve serbest cisim tarafını sor: toz, kıvılcım, buhar, enkaz, sıvı ve kumaşın promptla ne ölçüde yönlendirilebildiği, davranışı sayıyla yazmanın ("dust settles within three seconds", "the plume expands in a straight cone and is gone in one and a half seconds") sıfatla yazmaya göre farkı, parçacığın kadrajda donması ile düzlemsel iki boyutlu davranmasının ayrı arızalar olup olmadığı, dönme (açısal momentum) ile doğrusal momentumun ayrı ayrı yazılmasının gerekip gerekmediği, ve ilk karede görünen parçacık dağılımının videodaki davranışı ne kadar belirlediği.
Yerçekimini ve rejim tutarlılığını topla: ortamın yerçekimini sayıyla yazmanın ("gravity is 0.30 g") sıfatla yazmaya ("low gravity", "about two thirds of Earth's weight") göre ölçülebilir faydası, aynı sayının bir filmin bütün kliplerinde tekrarlanmasının klipler arası tutarlılığa etkisi, aynı kadrajda iki rejimin çıkmasını önleyen tarif biçimleri (ayıran işaretin adlandırılması: manyetik bot, el tutamağı, kemer, mıknatıs), ortam adının (vakum, ince atmosfer, basınçlı iç hacim) yazılmasının sayı kadar gerekli olup olmadığı, ve bir filmin bütün kliplerinde aynı fizik rejimini tutturmak için belgelenmiş bir yöntem bulunup bulunmadığı.
Kritik kısıt: kullanım yeri, on saniyelik, kesmesiz, varsayılan olarak sabit kameralı, tek İngilizce promptla üretilen fotogerçekçi uzay bilimkurgu klipleridir ve bir filmde 12 ile 48 klip vardır; ortamlar vakum, ince atmosfer (Mars benzeri), kalın atmosfer, dönme yerçekimi ve basınçlı iç hacimdir ve bir film bunlardan ikisini birden kullanabilir; prompt tek metindir, pozitif gövde 120-300 kelime, ardından en çok on bir cümlelik olumsuz blok gelir ve promptta `PHYSICS:` ile `AUDIO:` diye iki ayrı satır zaten vardır; kurguda kesme ve ses miksi yapılır ama VFX kompozit, parçacık simülasyonu, rotoskop ve elle rötuş YOKTUR — bu yüzden ayrı parçacık katmanı üretip birleştirmeyi, ses tasarımını sıfırdan kurmayı ve fizik simülasyonu öneren çözümleri "hat dışı" diye işaretle ama silme, tek prompt, ilk kare ve kurgu adımıyla uygulanabilir olanları öne al.
Çıktıyı üç tablo ve iki liste olarak ver: (a) SES tablosu — istenen ses durumu (tam sessizlik, yalnız gövdeden iletilen ses, boğuk dış ses, normal ses), İngilizce tam kalıp, modelin uyum oranı varsa oranı, kapatma ya da ayıklama yolu, model, kaynak ve etiket; (b) PARÇACIK ve YERÇEKİMİ tablosu — olgu (toz, buhar, kıvılcım, enkaz, düşen cisim, dönen parça), sayıyla yazılışı (İngilizce tam kalıp), ölçülmüş tutuş, tipik arıza biçimi, model, kaynak ve etiket; (c) REJİM TUTARLILIĞI tablosu — arıza (aynı kadrajda iki rejim, klipler arası farklı ivme, rejimin sahne ortasında değişmesi), tetikleyici, önleyen tarif biçimi, model, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, ÖLÇÜLMÜŞ dediğin her satır için birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre, sürüm adı ya da sayı uydurma.
```

### 🧪 SINAMA SETİ — gelen cevap bu üç ölçümü AÇIKLAMALI

```
① VAKUMDA SES — kilit ne kadar açık yazılırsa yazılsın tutmuyor

   KRONOS_SON_SINYAL   AUDIO satırı 0/96 promptta            → 4 🔴
   SUSMAYAN_NOBETCI    AUDIO satırı 96/96, cümleler birebir:  → 4 🔴
        "no exterior sound at all, the hull parts in silence"
        "faint radio carrier hiss only; no exterior sound at all, the pod separates in silence"

   ⛔ TUR 20 (OMNI) bu konuyu sordu ve çıkan tek kural şu oldu:
      "AUDIO satırı HER klipte + sessiz klipte No dialogue. No music."
      Dış ses yasasının TUTUP TUTMADIĞI cevapsız kaldı ve yukarıdaki
      dört BLOCKER o kuraldan SONRA yazılan filmde çıktı.

   ARANAN CEVAP: dış ses prompttan kontrol edilebiliyor mu? Edilemiyorsa
   üretilen sesin kanal olarak ayrılıp ayıklanması mümkün mü? İkisi de
   hayırsa kılavuz §4'ün "kurgu masası" satırı ÖLÇÜLMÜŞ olur.

② YERÇEKİMİ — sayı yarıya indiriyor ama sıfırlamıyor

   BENI_HATIRLAMA     TARİFLE: "about two thirds of Earth's weight"
                      + çekirdekte "particles obey the stated gravity"
                      → ekranda 0,39 · 1,11 · 1,13 · 2,48 m/s² ölçüldü
                      → 2,9× tutarsızlık · 2 🔴
   THE_FALLING_WORLD  SAYIYLA: "Gravity is 0.30 g" · 48/48 promptta
                      → ekranda 4,4 ↔ 2,2 m/s² · 1 🔴

   ARANAN CEVAP: sayının faydası bağımsız olarak ölçülmüş mü, ve aynı
   sayıyı bütün kliplerde tekrarlamak klipler arası tutarlılığı artırıyor mu?

③ PARÇACIK — cümle var, ortam yok

   THE_STILL_SWARM    parçacık cümlesi 2/14 · film YÜZEN PANEL filmi
                      → "background debris entirely static/frozen" 🔴
                      → "gas emission freezes into static 2D plane" 🔴
   THE_SHATTERED_BREATH  parçacık cümlesi 12/12 AMA ortam adı 1/12
                      → "steam drifts upward linearly despite the vacuum background"

   ARANAN CEVAP: parçacık cümlesi ortam adı olmadan anlamlı mı, ve
   açısal momentum (dönme) ayrıca yazılmalı mı?
```

---

## 📥 SONUÇ GELDİĞİNDE — kayıt zinciri

```
1. Ham rapor OLDUĞU GİBİ → URETIM_ONCESI_ANALIZ/TUR22_HAM_RAPORLAR/
   (⚠️ 24_'ün turu koşulmadı; koşulursa o TUR 21 olur ve bu tur 22 kalır.
    Sıra bozulursa klasör adı koşu tarihine göre düzeltilir, rapor değil.)
2. 04_ARASTIRMA_BULGULARI.md → § TUR 22: neyin girdiği · neyin GİRMEDİĞİ · neden
3. PROMPT_HATA_ONLEME_KILAVUZU.md → §3 sınıf 2 · §3 sınıf 5 · §2 · §4 güncellenir
4. ⛔ Kılavuza yalnız ÖLÇÜLMÜŞ etiketli satırlar iner. UYGULAMA ve ÖNERİ
   satırları 04'te kalır ve kılavuzda "⬜ sınanmalı" olarak anılır.
5. Sonra: ham QA raporları × sahne promptları YENİDEN okunur —
   cevabın öngördüğü koşul 10_PROMPT_QA_ANALIZI'nin 688 bulgusunda
   doğrulanıyor mu? Doğrulanmıyorsa cevap kılavuza İNMEZ.
```
