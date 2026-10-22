# AI Filmlerde 10 Saniyelik Klip ve Ritim Kılavuzu

**Odak:** Diyalog veya olay 6. saniyede bitince kalan 4 saniyenin amaçsız kalmasını önlemek — **10 s'yi keserek değil, tasarımla doldurarak**  
**İş akışı:** GPT Image ile başlangıç karesi → Omni / Veo veya seçilen image-to-video modeli → ses ve kurgu  
**Hazırlanma tarihi:** 21 Ekim 2026  
**Kullanım:** Hem yeni film planlarını yazarken hem üretilmiş videoları düzeltirken  
**Dil:** Türkçe açıklamalar, kopyalanabilir İngilizce video istemleri
**Hat uyarlaması:** 21.10.2026, sahip kararıyla hattın 10 s kuralına göre düzenlendi. Düzenlenmemiş ilk sürüm: `_ham_kilavuzlar/AI_FILMLERDE_10_SANIYELIK_KLIP_VE_RITIM_KILAVUZU.md`

> **HAT KURALI (SÖZLEŞME, sahip kararı 08.10.2026 · 10.10.2026) — bu kılavuzun her bölümü buna göre okunur**
> - Her çekim **10 s üretilir ve filmde 10 s kullanılır.** Çekim sayısı = hedef süre / 10 (2 dk 12 · 4 dk 24 · 8 dk 48 · 16 dk 96). `film_dogrula` ve `kurgu.py kontrol` denetler.
> - 10 s'lik aralık klibin kullanılabilir kısmından seçilir. Bozuk saniye klibi düşürür ya da yeniden ürettirir; **çekimi kısaltmaz.**
> - Temiz kısım 10 s'ye yetmezse sıra (`uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6): ① aynı çekimin başka denemesi → ② devam üretimi (temiz son kareden aynı açıyla ya da Omni uzatma) → ③ aynı çekimin iki denemesini gizli kesmeyle birleştirmek → ④ sonuç planı.
> - **Yok:** yavaşlatma, döngü, donmuş kare, bozuk görüntüyü bekletme.
> - Video promptu 10 s'nin planını yazar: **2-4 vuruş "a-b s", 0'dan 10'a boşluksuz, her vuruş ≥2 s, tek hareketin evreleri, son vuruş donmaz.** Saniye-altı mikro liste yok.
> - Ritim süreyle değil, çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
>
> Bu kılavuzda temel karar, her klibin sonuna rastgele hareket eklemek değildir. Planın işini hangi evrede tamamladığını belirlemek ve kalan saniyelere **aynı olayın** anlamlı devamını (tepki, sonuç, karar, sonraki adıma geçiş) yazmaktır. Boş kalan saniye kesilmez; çekim yeniden tasarlanır.

Bu belge hattın kılavuzlarına (`uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md`, `GPT_IMAGE_OMNI_KILAVUZU.md`, `ILK_30_SANIYE_KILAVUZU.md`) ek olarak kullanılır; çakışırsa hat kılavuzu geçerlidir. Kural türü: HİPOTEZ (AGENTS §1b). Film konularını tekrar etmez. İçindeki küçük sahne örnekleri, yalnız zamanlama ve kurgu tekniğini göstermek için hazırlanmıştır. Kullanıcıya ait gerçek bir video burada incelenmiş değildir; teşhisler anlatılan “6 saniye olay + 4 saniye boşluk” durumuna yönelik olasılıklardır.

## İçindekiler

1. En önemli düzeltme
2. Son dört saniye neden boş kalabilir?
3. Üretim süresi, plan süresi ve film süresi
4. Sessizlik ile boşluk arasındaki fark
5. Bir ana olayın aşamalarını tasarlamak
6. GPT Image karesini zamana hazırlamak
7. Diyalog süresini doğru hesaplamak
8. Kullanılabilir zamanlama düzenleri
9. Tam örnek: tek planda konuşma ve sonucu
10. Tam örnek: altı saniyelik iyi bölümü 10 s'ye tamamlamak
11. Aksiyon, manzara ve gerilim
12. Kopyalanabilir video istemleri
13. Üretilmiş boş klibi kurtarmak
14. Ses, J-cut ve L-cut
15. Dört, sekiz ve on altı dakikalık film hesabı (her çekim 10 s)
16. Altı çekimle tam 60 saniye: süre sabit, ritim değişken
17. Ek planlar ve üretim bütçesi
18. Gerçek çıktıyı ölçme yöntemi
19. Hata–neden–çözüm tablosu
20. Yeni klip kartı formatı
21. Yeni film hazırlayan asistana verilecek ana talimat
22. Mevcut planı veya videoyu inceleme talimatı
23. Uygulama sırası, kontrol listesi ve kısa cevaplar
24. Kaynaklar ve önerilerin sınırı

---

## 1. En önemli düzeltme

**10 saniyelik çekim, 10 saniyelik iş ister.**

Bir karakterin repliği 5. saniyede, anlamlı tepkisi 6. saniyede bitiyorsa sorun kalan dört saniyede değil, çekimin tasarımındadır. Hatta çekim kısalmaz; o dört saniyeye aynı olayın anlamlı devamı yazılır.

Böyle bir çekim için üç geçerli yol vardır:

1. **Olayı evrelerine yay:** Başlangıç karesini eylemin daha erken evresine çek (hazırlık, yaklaşma, tutuş). İş 6. saniyede değil, son vuruşta tamamlanır.
2. **Aynı olayın sonucunu ya da tepkisini son vuruşa koy:** Replikten sonra gerçekten gerekli bir karar, fiziksel sonuç veya algı değişimi varsa onu planla.
3. **Ayrı görüntü gerekiyorsa çekim listesinde çöz (F3):** Tepki ya da sonuç başka kadraj istiyorsa o, kendi 10 s'lik çekimidir. Çekim sayısı sabit olduğu için bu yeni çekim başka bir çekimin yerini alır ya da iki zayıf çekim birleşir.

İkinci ve üçüncü yolun işe yaraması için eklenen görüntünün bir anlamı olmalı. Rastgele kafa çevirme, kamera yaklaşması, kıvılcım veya uzun boş bakış kendi başına çözüm değildir.

### 1.1. Hattın varsayılanı

- 10 saniye hem **üretim birimi** hem **kurgu birimidir**: C01–C24, 24 çekim × 10 s.
- Bir çekimin içinde C01A / C01B gibi alt çekim yoktur. Bir çekim içindeki ritmi **vuruşlar** taşır (2-4 vuruş, her biri ≥2 s).
- Üretimde temiz kısım kısa kalırsa çekim kısaltılmaz; `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası uygulanır.

### 1.2. On saniyeyi tek planda taşımak

Birbirine bağlı aşamalar tasarla:

**Giriş durumu → ana girişim/replik → görünür sonuç → bu sonuca verilen tepki.**

Bunların hepsi her planda ayrı hareket olmak zorunda değil. Tek bir sürekli çaba veya yavaş gelişen bir keşif de on saniyeyi taşıyabilir. Vuruşlar bu aşamaların saniye aralıklarıdır; son vuruşta hareket sürer, donmaz.

## 2. Son dört saniye neden boş kalabilir?

Aşağıdaki nedenler olasılıktır. Hangisinin geçerli olduğu istem ve gerçek video birlikte incelenerek anlaşılır.

| Belirti | Olası neden | İlk düzeltme |
| --- | --- | --- |
| Tek replik bitince karakter donuyor. | Replikten sonra oynanacak bir niyet tanımlanmamış. | Repliğin karakterde veya ortamda yarattığı sonucu yaz. |
| Kapı açılıyor, sonra kamera boş alanı izliyor. | Eylemin sonucu erkenden tamamlanıyor. | Eylemi daha erken evreden başlat; sonucu ve gerçekten gerekli tepkiyi son vuruşlara yaz. |
| İstemde çok şey var ama hepsi ilk üç saniyeye sıkışıyor. | Olay sırası ve süreye uygunluk belirsiz; görev yoğun. | Ana eylemi seç, doğal aşamalarını vuruşlara dağıt; bağımsız olayları ayrı çekime taşı. |
| İlk kare zaten final pozunu gösteriyor. | Video için yapılacak iş kalmamış. | Başlangıç görselini eylem öncesi duruma çevir. |
| Son bölümde yalnız yavaş kamera yaklaşması var. | Kamera hareketi olayın yerine kullanılmış. | Yaklaşmanın neyi açığa çıkardığını belirle; yoksa son vuruşa öznenin bir sonraki davranışını yaz. |
| Uzun konuşma istemine rağmen replik çok hızlı bitiyor. | Performans temposu çıktı içinde değişmiş. | Gerçek ses süresini ölç; doğal konuşma isteğiyle tekrar dene; replikten sonraki vuruşa tepki ya da sonuç yaz. |
| Karakterler her klip sonunda seyirciye dönüp poz veriyor. | Son durum “heroic pose”, “hold”, “dramatic stare” gibi tanımlanmış olabilir. | Sonu hikâyedeki fiziksel/duygusal durumla tarif et. |
| Bütün klipler aynı ritimde: konuş, dur, kes. | Plan şablonu bütün sahnelere aynı uygulanmış. | Vuruş sayısını ve sınırlarını çekimden çekime değiştir; kadraj ve ölçek değişimi kullan (ARIZA H10). |

### 2.1. İstemde özellikle aranacak ifadeler

Şu ifadeler bağlama göre uzun ve amaçsız bir son yaratabilir:

- “Then he stands still.”
- “Hold the final pose.”
- “They look at each other.”
- “A long dramatic pause.”
- “The camera slowly pushes in.”
- “End on a cinematic freeze.”

Bu ifadeler yasak değildir. Sorun, neden gerekli oldukları belirlenmeden her klibe eklenmeleridir. Hatta son vuruş için ayrıca kural var: son vuruş donmaz (`holds still`, `freezes` yazılmaz), hareket 10. saniyede hâlâ sürer.

### 2.2. Süre ayarı ile olay dağılımı farklı kontrollerdir

Arayüzde 10 saniye seçmek dosyanın süresini belirleyebilir. Bu ayar, konuşmanın 6. saniyede bitmesini veya kapının 8. saniyede açılmasını tek başına garanti etmez.

Saniyeli istemler yönlendirme sağlar. Üretilen sonuçta olaylar yine erken, geç veya farklı sırada gerçekleşebilir. Gerçek zamanlama çıktı üzerinde ölçülür (`kareler.py`); 10 s'lik aralık klibin kullanılabilir kısmından seçilir, yetmezse `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası uygulanır.

## 3. Üretim süresi, plan süresi ve film süresi

### 3.1. Dört ayrı süre

| Kavram | Anlamı | Hatta |
| --- | --- | --- |
| Ham üretim süresi | Modelin verdiği kaynak dosyanın uzunluğu | Omni 10 s; uzatma ya da devam üretimiyle daha uzun olabilir. Veo 4/6/8 s verir (`FLOW_GERCEKLERI`). |
| Kullanılabilir bölüm | Kimlik, hareket, ses ve anlatı açısından işe yarayan aralık | Ölçülür (`kareler.py`, Gemini taraması, sahibin işaretlemesi). |
| Montajdaki çekim süresi | Zaman çizelgesinde kullanılan görüntü | **Her zaman 10,0 s.** |
| Film süresi | Montajın başlangıcından sonuna kadar geçen toplam zaman | Çekim sayısı × 10 s (24 × 10 = 240 s). |

Kullanılabilir bölüm 10 s'den uzunsa (örneğin uzatılmış 14 s'lik klipte 2,0–12,0) en iyi 10 s seçilir. Kısaysa (örneğin 0,4–6,6 = 6,2 s) çekim 6,2 s'ye inmez; eksik 3,8 s `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırasıyla tamamlanır.

### 3.2. Hattın tek çalışma modu

Kılavuzun ilk sürümü üç mod öneriyordu: değişken çekim süresi (Mod A), 10 s'lik bölüm içinde alt çekimler (Mod B) ve tek üretim = tek 10 s çekim (Mod C). **Hatta yalnız tek üretim = tek 10 s çekim geçerlidir.** Mod A ve Mod B uygulanmaz.

Bunun sonucu: eylem gerçekten 10 s'ye ihtiyaç duyacak şekilde tasarlanır. Altı saniyelik bir işi yavaşlatmak yerine sahnenin amacı ve başlangıç karesi yeniden düşünülür.

### 3.3. Aynı anda korunması gereken kısıtlar

Hat şu dört isteği birlikte korur:

- Çekim sayısı = hedef süre / 10.
- Her çekim filmde 10 s.
- Kaynak bozuk saniyesiyle kullanılmaz.
- Filmde amaçsız an olmaz.

Dördü her denemede kendiliğinden tutmaz. Bir denemede yalnız altı saniye işe yarıyorsa çekimi kısaltmak bir seçenek değildir. Yollar şunlardır: çekim tasarımını (vuruş planı, başlangıç karesi) düzeltmek, aynı çekimi yeniden üretmek, devam üretimi, iki denemeyi birleştirmek. Hiçbiri olmuyorsa çekim listesi F3'e geri döner.

## 4. Sessizlik ile boşluk arasındaki fark

**Konuşmanın bitmesi, planın bittiği anlamına gelmez.** İzleyici o sırada bir kararın oluşmasını, bir tehdidin yaklaşmasını veya yeni bilginin fark edilmesini izliyor olabilir.

| An | Değer taşıyor mu? | Neden? |
| --- | --- | --- |
| Karakter dört saniye aynı ifadeyle bekliyor; durum değişmiyor. | Çoğu bağlamda zayıf | İzleyiciye yeni bir şey vermiyor. |
| Karakterin uzattığı el, karşısındakinin tepkisiyle yavaşça geri çekiliyor. | Taşıyabilir | Güven veya karar değişimi görünür. |
| Kapı aralığı boyunca ışık çizgisi büyüyor; karakter bunu takip ediyor. | Taşıyabilir | Aynı olay ilerliyor ve beklenti sürüyor. |
| Geniş planda önemli engel yavaşça görünür oluyor. | Taşıyabilir | Mekânsal bilgi açılıyor. |
| Sadece parçacıklar uçuşuyor; ana olay değişmiyor. | Bağlama bağlı, çoğu kez yetersiz | Görsel hareket anlatısal işlev yerine geçmiyor. |
| Kayıptan sonra yüzün anlamını okumak için bekliyoruz. | Taşıyabilir | Duygusal karşılık için zaman veriliyor. |

### 4.1. Üç soruluk boşluk testi

Şüpheli aralığı düşüncede çıkar ve sor:

1. İzleyicinin anlaması gereken bilgi kayboldu mu?
2. Karakterin tepkisi veya kararının ağırlığı kayboldu mu?
3. Mekânı, hareketi veya yaklaşan sonucu okumak zorlaştı mı?

Üçüne de “hayır” diyorsan o aralık **boştur**. Hatta boş aralık kesilmez: planda yakalandıysa vuruş planı yeniden yazılır; üretimde yakalandıysa `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası uygulanır.

### 4.2. Hedef sürekli uyarım değildir

Her iki saniyede patlama, yeni nesne veya yeni sır eklemek gerekmez. Böyle bir kural hem sahneyi yorabilir hem üretim hatasını artırabilir.

Gerekli olan, plan devam ettiği sürece izleyicinin izleyecek anlamlı bir durumu olmasıdır. Bu durum sessiz ve çok küçük olabilir.

### 4.3. Bilinçli bekleyişi yazılabilir hâle getir

Zayıf:

~~~text
He looks worried for four seconds.
~~~

Daha somut:

~~~text
After hearing the answer, his eyes move from the other character to the object
in his hand. His grip loosens, but he does not release it. He chooses to keep it.
~~~

İkinci örnekte bir karar var. Gerçek performans iki saniyede okunuyorsa kalan süre aynı yüzde bekletilmez; kararın uygulanması (nesneyi cebine koyması, kapıya yönelmesi) sonraki vuruşa yazılır.

## 5. Bir ana olayın aşamalarını tasarlamak

### 5.1. Eylem sayısı ile aşama sayısı

“Tek ana eylem” demek bütün planda yalnız bir kıpırdama olacak demek değildir.

Bir nesneyi yerinden çıkarma girişimi şu aşamalara sahip olabilir:

- Tutuş ve hazırlık.
- Dirençle karşılaşma.
- Kuvvetin veya tutuşun ayarlanması.
- Nesnenin serbest kalması.
- Sonucun fark edilmesi.

Bunlar aynı hedefin aşamalarıdır. Araya yeni karakterin gelişi, ayrı bir konuşma ve mekân değişimi eklemek ise başka olaylar yüklemektir.

### 5.2. Her aşamanın üç alanı

~~~text
GÖRÜNÜR DAVRANIŞ: [Kamera ne kaydediyor?]
NEDEN: [Karakter bunu niçin yapıyor?]
SONUÇ: [Sonraki ana ne değişerek giriliyor?]
~~~

Yalnız “heyecan artar” yazmak görünür davranışı tarif etmez.

### 5.3. Son dört saniyede kullanılabilecek işlevler

| İşlev | Somut karşılık | Kullanım koşulu |
| --- | --- | --- |
| Tepki | Bakış hedefi, el veya beden kararı değişir. | Önceki söz/olay bu değişime sebep olmalı. |
| Fiziksel sonuç | Açılan yol, duran mekanizma veya yer değiştiren nesne görünür. | Sonuç, ana eylemden doğmalı. |
| Karar | Bir sonraki adım gerçekten başlatılır. | Sonraki klibin başlangıcıyla tutarlı olmalı. |
| Bilgi açılması | Kadraj veya bakış yeni bir ayrıntıyı görünür kılar. | Önceden kurulmuş sahnenin parçası olmalı. |
| Baskının sürmesi | Mesafe kapanır, yük artar veya kontrol zorlaşır. | Zamanın geçmesi anlamlı olmalı. |
| Duygusal karşılık | Karakter olanı kabul eder veya reddeder. | Yüz/beden performansı okunmalı. |
| Hareketle geçiş | Karakter kadrajdan çıkar veya hedefe yönelir. | Sonraki plan bunu devralmalı. |

Bunlar seçeneklerdir. Bir klibe yedisini birden ekleme.

### 5.4. Yanlış çözüm: her sonu yeni tehlikeye çevirmek

Her klibin sonunda alarm, gölge, patlama veya sürpriz kullanmak gerekmez. Olayın anlaşılması ve karakterin kararının görülmesi çoğu zaman daha değerlidir.

Final anını “bir sonraki görüntüyü gerektiren durum” olarak düşün. Bunun yüksek sesli olması şart değildir.

## 6. GPT Image karesini zamana hazırlamak

Video hareketinin başlayacağı durum ilk görselde kurulmalıdır.

Runway'in image-to-video rehberi, başlangıç görselinin kompozisyon ve görünümü belirlediğini; metnin ise hareketi ve zaman içindeki ilerlemeyi anlatması gerektiğini vurgular. Bu kılavuzdaki görsel/video ayrımı da bu yaklaşımdan yararlanır.[^runway]

### 6.1. İlk karede aranacaklar

- Yapılacak iş henüz tamamlanmamış mı?
- El veya nesne gereken başlangıç konumunda mı?
- Hareketin gideceği yönde kadrajda yer var mı?
- Sonucun görüleceği unsur görüntüde mi?
- Hem yüz hem el önemliyse kadraj ikisini de okuyabiliyor mu?
- Tepki başka karaktere aitse o karakterin planı veya referansı hazır mı?
- Sonraki hareket için gerekli nesne baştan mevcut mu?

### 6.2. Eylem öncesi ve eylem sonrası farkı

| Planlanan video | Uygun başlangıç | Sorun yaratabilecek başlangıç |
| --- | --- | --- |
| Nesneyi yerinden kaldırma | Nesne yerinde, el yaklaşmış veya temasta | Nesne zaten havada ve iş bitmiş |
| Bir geçidi açma | Geçit kapalı, açma yolu görünür | Geçit tamamen açık |
| Tepki ve karar | Karakter henüz sonucu görmemiş | Karakter zaten final ifadesinde |
| Çevreyi keşfetme | Bilginin bir kısmı örtülü veya kadraj dışında | Bütün bilgi ilk karede tüketilmiş |
| Sürekli çaba | İşin başı veya orta evresi | İşin tamamlanmış sunum pozu |

### 6.3. İngilizce başlangıç görseli eki

~~~text
Depict the moment immediately before the planned action.
[OBJECT] is still in [INITIAL_POSITION].
[SUBJECT] is ready to [MAIN_ACTION], but the result has not happened yet.
Keep [ACTION_PATH] and [RESULT_AREA] visible within the frame.
Preserve the approved character, costume and location references.
Create one still image showing one instant.
~~~

Görsel istemine “0–3 saniye bunu, 3–6 saniye şunu” yazılmaz. Bu zaman çizelgesi video içindir.

### 6.4. Kapanış karesi kullanılıyorsa

Araç ve seçilen mod destekliyorsa kapanış karesi hedef durumu belirlemeye yardım edebilir. Yine de iki uç kare arasındaki olayların tam zamanını garanti etmez.

Kapanış karesi yalnız güzel bir poster pozu olmamalı. Bir sonraki planın devralabileceği fiziksel durumu taşımalı.

## 7. Diyalog süresini doğru hesaplamak

### 7.1. Diyaloğu bütün on saniyeye yaymaya çalışma

Altı saniyede doğal söylenen cümleyi on saniyeye yaymak, oyunculuğu yapaylaştırabilir. Dört saniyelik açığı kelime ekleyerek kapatmak da gereksiz açıklama yaratabilir.

Önce repliğin gerçekten ne yaptığını belirle:

- Karar mı veriyor?
- Bilgi mi değiştiriyor?
- İlişkiyi mi etkiliyor?
- Karşıdaki kişiyi bir eyleme mi yönlendiriyor?

Repliğin görevi tamamlandıktan sonra kalan vuruşa tepki, sonuç ya da sonraki adıma geçiş yazılır. Kesme çekim sınırında, 10. saniyede olur.

### 7.2. Okuma provası

1. Repliği istenen duyguya yakın biçimde sesli oku.
2. İlk heceden son heceye kadar geçen süreyi ölç.
3. Nefes, bakış ve tepkiyi ayrıca prova et.
4. Görünür bir hareket konuşmayla aynı anda yapılabiliyorsa bunu açık yaz.
5. Üretilen gerçek ses geldiğinde süreyi yeniden ölç.

Metindeki kelime sayısı yalnız ön tahmindir.

### 7.3. Basit hesap

**Tahmini konuşma süresi = kelime sayısı × 60 / dakikadaki kelime sayısı.**

Örnek hesap için 150 kelime/dakika seçersek:

| Kelime | Matematiksel konuşma süresi |
| ---: | ---: |
| 8 | 3,2 saniye |
| 12 | 4,8 saniye |
| 15 | 6,0 saniye |
| 20 | 8,0 saniye |

150 kelime/dakika burada bir hesap varsayımıdır; doğal oyunculuk için zorunlu hız, araştırmayla belirlenmiş ideal veya modelin teknik sınırı değildir. Dil, vurgu, nefes, karakter ve duygu sonucu değiştirir.

On beş kelimelik replik kâğıt üzerinde altı saniyeye sığabilir. Tepki, eylem ve duraklamalar eklenince plan daha uzun sürebilir.

### 7.4. Eşzamanlı olanları iki kez sayma

Karakter üç saniye yürürken aynı üç saniyede konuşuyorsa bu, altı saniyelik malzeme değildir. Görüntü ve ses aynı zaman çizelgesinde örtüşür.

İş akışı:

~~~text
Konuşma: 0,7–5,5 saniye
Yavaş el hareketi: 2,0–5,5 saniye
Görünür sonuç: 5,5–8,0 saniye
Tepki: 8,0–9,6 saniye
~~~

Bu örnekte el hareketi konuşmanın bir bölümüne eşlik eder. Süre hesabı bütün satırları toplamakla yapılmaz.

Bu liste süre hesabı içindir. Video promptuna böyle saniye-altı bir liste yazılmaz; prompta en çok 4 vuruş, her biri ≥2 s olarak girer (örneğin 0-5 s replik, 5-8 s sonuç, 8-10 s tepki).

### 7.5. İki konuşmacı

İki karakterin her birine uzun cümle verip tepkiyi son saniyeye sıkıştırma. Gerekirse:

- Birinci repliği ana planda göster.
- İkinci repliği dinleyicinin veya tepki veren kişinin görüntüsüne taşı.
- Ayrı çekimler üretip (her biri 10 s) ses geçişini J/L ile kurguda kur.
- Aynı yüzü iki ayrı sesle konuşturma.
- Kadraj dışı sesi “offscreen” olarak açık belirt.

### 7.6. Ses modelden veya ayrı üretilirse

**Ses video modeli içindeyse (hatta "model sesi", FILM §5):** Replik video promptuna birebir yazılır; konuşmacı ve replik sonrası hareket aynı istemde açık olmalı. Gerçek çıktıdaki konuşma süresi esas alınır.

**Ses ayrı üretilirse:** Önce sesin gerçek süresine göre kurgu planlanabilir. Görünür ağızla senkron gerekecekse bunun ayrıca çözülmesi gerekir. Sesi sonradan eklemek kendiliğinden dudak uyumu sağlamaz.

## 8. Kullanılabilir zamanlama düzenleri

Bu tablolar vuruş planı için başlangıç taslaklarıdır: 0'dan 10'a boşluksuz, her vuruş ≥2 s. Saniyeler model garantisi değildir. Gerçek eylem daha kısa veya uzun sürerse 10 s'lik aralık klibin kullanılabilir kısmından seçilir; yetmezse `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6.

### 8.1. Diyalog + fiziksel sonuç

| Vuruş | İşlev |
| --- | --- |
| 0–5 s | Zaten süren küçük bir hareketle başlar; tek doğal replik. |
| 5–8 s | Repliğin ardından ana eylemin görünür sonucu. |
| 8–10 s | Sonucu fark etme ve sonraki davranışa yönelme; hareket sürer. |

Son vuruşun amacı yalnız “bakmak” değildir. Bakışın hedefi ve davranış üzerindeki etkisi tanımlanır.

### 8.2. Tek sürekli çaba

| Vuruş | İşlev |
| --- | --- |
| 0–2 s | Tutuş veya konum kurulmuş hâlde girişim başlar. |
| 2–7 s | Aynı çaba gerçek direnç veya mesafe boyunca sürer. |
| 7–10 s | Sonuç oluşur; beden yeni duruma uyum sağlar (denge, yön, tutuş). |

Direnç yalnız süre doldurmak için uydurulmamalı; sahnenin fiziksel koşullarıyla anlaşılmalı.

### 8.3. Bilgi açan geniş plan

| Vuruş | İşlev |
| --- | --- |
| 0–3 s | Konum ve ölçek okunur; özne ya da araç hareket hâlinde. |
| 3–7 s | Hareket veya örtünün açılması yeni bilgiyi gösterir. |
| 7–10 s | Yeni bilgi ile karakterin/araçların ilişkisi değişir. |

Yeni bilgi zaten ilk karede bütünüyle görünüyorsa on saniyeyi kamera hareketiyle değil, öznenin ilerlemesiyle taşı ya da bilginin bir kısmını başlangıç karesinde örtülü bırak.

### 8.4. Replik + tepki + sonuç, tek kadrajda

| Vuruş | Görüntü | Görev |
| --- | --- | --- |
| 0–6 s | İkili plan; konuşan önde | Replik veya girişim |
| 6–8 s | Aynı kadrajda dinleyen kıpırdar | Kararın etkisi |
| 8–10 s | Kamera tek yönelimle nesneye kayar ya da nesne kadraja girer | Olayın gerçekten değiştiğinin kanıtı |

Bu düzen tek üretimde, kesmesiz kurulur. Tepki ya da sonuç ayrı yakın plan istiyorsa o, kendi 10 s'lik çekimidir (§1, yol 3). Modelin tek üretimde kesme yapmasına güvenilmez.

### 8.5. İş altı saniyede bitiyorsa

Bu, çekimin tasarımının yeniden ele alınması gerektiği anlamına gelir. Altı saniyeden sonrası kullanılmaz diye bırakılmaz. Seçenekler:

| Seçenek | Ne yapılır |
| --- | --- |
| Daha erken başla | Başlangıç karesi eylemin hazırlık evresine çekilir (el yaklaşıyor, henüz temas yok). |
| Sonraki evreyi ekle | İşin sonucu ya da karakterin sonraki adıma geçişi son vuruşa yazılır. |
| Birleştir | İki komşu çekimin işi tek çekime toplanır; açılan çekim yeri sahnenin eksik bilgisine verilir (F3, yonetmen). |

### 8.6. Her klibi bu kalıplara sokma

Bir filmde bütün planların aynı dört aşamayla ilerlemesi mekanik ritim yaratabilir. 3-4-3 iskeleti ve donan bitiş zaten karantinada (PROMPT_HATA_ATLASI). Bazı planlar eylemin ortasında başlar; bazılarında sonuç bir sonraki çekime kalır; bazıları sessiz kalır. Vuruş sayısı ve sınırları çekimden çekime değişir. Kalıplar tanı koymak ve planlamak için vardır.

## 9. Tam örnek: tek planda konuşma ve sonucu

Bu örnek eski bir filmden alınmamıştır. Tek bir fiziksel olayın zamana nasıl dağıtılacağını gösterir.

### 9.1. Zayıf tasarım

~~~text
An adult alien says, "Stay behind me. I'm going to open this door slowly."
Cinematic lighting. Ten seconds.
~~~

Olası sonuç: Replik biter, kapı erkenden açılır ve karakter kalan süre boyunca bekler. Çünkü kapının ne zaman açıldığı, sonucun nasıl okunduğu ve karakterin ardından ne yaptığı belirsizdir.

### 9.2. Sahne amacı

Karakter kapıyı kontrollü açmak ister. Repliğini bitirdikten sonra açıklığı büyütür. İçeriden gelen ışık yüzüne ulaştığında, ilerlemeden önce içeriyi değerlendirdiğini görürüz.

Bu davranışta bir ana hedef vardır: kapıyı güvenle açmak. Son bölüm, aynı hedefin sonucudur.

### 9.3. İlk görselde olması gerekenler

- Onaylı yetişkin uzaylı karakter.
- Kapı kapalı.
- Bir el kapı kolunda, diğer el görünür ve boş.
- Karakterin yüzü, kapı kolu ve kapı aralığının oluşacağı bölge okunur.
- Kamera orta planda ve sabit.
- Açılma yönünde yeterli alan var.
- Kapı arkasında bir şey eklenecekse bu, ayrı plan ve referans kararıdır; örneğe kendiliğinden yeni yaratık eklenmez.

### 9.4. Saniye planı

| Vuruş | Görüntü | Ses | Değişim |
| --- | --- | --- | --- |
| 0–5 s | El kolun üzerinde; karakter kapıya doğru hafifçe eğilerek repliğini söyler, dikkat kapıda kalır. | Tek replik | Niyet anlaşılır. |
| 5–8 s | Kolu indirir ve kapıyı kontrollü aralar. | Kol ve menteşe sesi | Kapı durumu değişir. |
| 8–10 s | Işık yüzüne düşer; bakış aralığa geçer, beden içeri bakmak için yönelmeye devam eder. | Ortam sürer | Sonraki davranışa geçilir. |

Bu tablo yaklaşık hedef dağılımdır. Gerçek hareket 8,7 saniyede tamamlanır ve sonrası donarsa çekim kısaltılmaz: önce aynı çekimin başka denemesine, sonra devam üretimine bakılır (`uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6).

### 9.5. GPT Image istemi

~~~text
Create one cinematic 16:9 still using the attached approved character
and location references.

An adult alien stands beside a fully closed mechanical door.
One hand already rests on the door handle; the other hand is visible and empty.
The character has not yet turned the handle or opened the door.

Use a medium three-quarter composition that clearly shows the face,
the handle, the edge of the door and enough space for the door to open.
The character's attention is directed toward the door.

Preserve the exact anatomy, costume, door design and lighting from the references.
This is one starting instant before the action.
One image, no collage, no captions or watermark.
~~~

### 9.6. Kısa ve sıralı video istemi

~~~text
Use the supplied image as the starting frame.
One continuous medium shot with a locked camera.

The adult alien keeps one hand on the handle and says naturally:
"Stay behind me. I'm going to open this door slowly."

Immediately after finishing the line, the alien lowers the handle
and opens the door a short distance with controlled effort.
As light from the opening reaches the face, the alien shifts attention
into the gap and angles the body slightly to look inside.

The progression is speech, controlled opening, then assessment of the result.
Keep the same character identity, hand placement, anatomy and door geometry.

Audio: one visible speaker, the exact line above, subtle handle and hinge sounds,
and continuous room ambience.
~~~

### 9.7. Zaman işaretli sürüm (hat biçimi)

~~~text
Use the supplied image as the starting frame.
Target output: 10 seconds, one continuous medium shot, locked camera.

0-5 s: Holding the handle, the alien leans slightly toward the door and says naturally:
"Stay behind me. I'm going to open this door slowly."
5-8 s: After the line, the alien lowers the handle and opens the door slightly.
8-10 s: Light reaches the face. The alien looks through the gap and keeps
shifting body weight forward to assess the space beyond it.

Keep the action in that causal order.
Preserve the supplied identity, costume, anatomy and architectural geometry.
Audio: the exact line, matching mechanical sounds and continuous room ambience.
~~~

İki istemi üst üste eklemek gerekmez. **Hatta gönderilen istem zaman işaretli sürümdür** (vuruş planı zorunlu, sahip kararı 10.10.2026; `film_dogrula` M). Kısa ve sıralı sürüm (§9.6) yalnız olay sırasını düşünmek için taslaktır. Olay sırası doğru fakat tempo sorunluysa vuruş sınırları tek değişken olarak değiştirilir.

Runway'in rehberi zaman sıralamasını doğal dille veya yaklaşık zaman damgalarıyla belirtmeyi önerir; bu, farklı bir modelin aynı zamanlamayı eksiksiz uygulayacağına dair garanti değildir.[^runway]

### 9.8. Bu örneğin kabul ölçütü

- Replik anlaşılır mı?
- Kapı açma eylemi replikten sonra mı?
- Son bölümde kapı durumundaki değişim ve ona verilen tepki okunuyor mu?
- Yüz ve el yapısı korunmuş mu?
- Son vuruş donuyor mu; 10. saniyede hareket hâlâ sürüyor mu?
- Klibin temiz kısmı 10 s'yi karşılıyor mu? Karşılamıyorsa `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6.

Kabul ölçütü “son kare mutlaka 10,000 saniyede geldi” değildir. Dosya süresi ayrı, olayın ritmi ayrı kontrol edilir.

## 10. Tam örnek: altı saniyelik iyi bölümü 10 s'ye tamamlamak

Durum: C07'nin bir denemesinde 0,0–6,0 s iyi (karar repliği ve yüz performansı), 6,0–10,0 s boş. Çekim 6 s'ye inmez; iyi altı saniye korunarak 10 s tamamlanır.

### 10.1. Seçenekler, sırayla (`uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6)

| Sıra | Yol | Ne yapılır | Yeni üretim |
| --- | --- | --- | --- |
| ① | Başka deneme | Aynı çekimin diğer denemelerinde temiz 10 s var mı? | Gerekmez ya da bir deneme |
| ② | Devam üretimi | 6,0 s civarındaki temiz son kareden aynı açıyla devam (`GPT_IMAGE_OMNI_KILAVUZU` §8 A) ya da Omni uzatma; uzatılmış klipten 10 s seçilir | Bir üretim |
| ③ | İki denemeyi birleştirmek | Aynı çekimin iki denemesinin temiz kısımları, kadrajdan geçen nesne ya da hareketin arkasında gizli kesmeyle | Eldeki malzemeye bağlı |
| ④ | Sonuç planı | Tepki ya da sonuç ayrı kadraj istiyorsa: C07'nin vuruş planı yeniden yazılır (tek kadrajda, §8.4) ya da tepki çekim listesinde kendi 10 s çekimi olur | Bir üretim; çekim listesi değişir (F3) |

Sırf “dört saniye dolsun” diye ilgisiz bir görüntü eklenmez. Devam, ana plandaki kararın hemen sonrasına ait olmalıdır.

### 10.2. Devam üretimi istemi

~~~text
Use the supplied frame (the last clean frame of the previous take) as the starting frame.
Same camera position, same lens, same lighting.

0-4 s: Having just said the decision, the speaker keeps eye contact with the listener,
then lowers the object held near the chest.
4-10 s: The speaker turns toward the door and takes the first step,
the object now hanging at the side; the motion continues to the end of the shot.

Keep identity, costume, hand placement and object state exactly as in the starting frame.
Audio: room ambience and fabric movement; no new spoken line.
~~~

Birleşme noktası `kareler.py dikis` ile kontrol edilir: hız, bakış yönü, ışık ve el konumu tek kareyle kendiliğinden eşleşmez.

### 10.3. Tepki kendi çekimi olursa

~~~text
Use the approved listener and location references.
Frame the listener in a medium close-up with a consistent eyeline
toward the offscreen speaker.

0-4 s: Listening to the decision, the listener's grip on the object near the chest tightens.
4-7 s: The fingers relax; the listener glances at the object.
7-10 s: The listener lowers the object out of the way and steps aside,
still moving at the end of the shot.

Keep the mouth closed and the camera steady.
Audio: room ambience and a small fabric movement; no new spoken line.
~~~

Bu çekim 10 s'dir ve çekim listesinde bir yer alır. Çekim sayısı sabit olduğu için başka bir çekimin yerini alır; bu karar F3'te yonetmenindir. Kadraj dışı konuşma J/L ile tepki çekiminin üzerine taşınabilir.

### 10.4. Devamlılık tuzakları

- Devam ya da tepki planı, ana plandan önceki nesne durumunu yanlışlıkla geri getirmemeli.
- Görünür el ve tutuş aynı olmalı.
- Karakterin bakış yönü konuşmacının konumuna uymalı.
- Henüz gerçekleşmemiş sonuç erkenden gösterilmemeli.
- Aynı hareket iki kez yaşanmış gibi gösterilmemeli.
- Konuşma sesi tepki planına taşınırken görünür yanlış ağız hareketi olmamalı.
- Birleştirmede dikiş görünmemeli (`kareler.py dikis`).

### 10.5. Her boş son yeni üretim istemez

Ana denemede gerekli tepki zaten varsa ve temiz kısım 10 s'yi karşılıyorsa yalnız doğru 10 s aralığı seçilir. Yeni üretim, eksik saniyeler gerçekten boşsa açılır.

## 11. Aksiyon, manzara ve gerilim

### 11.1. Aksiyon

Kısa bir aksiyonun doğal sonu çoğu zaman fiziksel temasın hemen sonrası değildir. Sonucu anlamak için bir karşılık gerekebilir.

Kullanılabilecek yapı:

**Niyet okunur → hareket olur → temas/sonuç okunur → denge veya konum değişir.**

Amaçsız dört saniyeyi yeni bir çatışmayla doldurmak yerine mevcut hareketin sonucunu göster:

- Karakterin durduğu yeni yer.
- Nesnenin nereye gittiği.
- Bir yolun açılması veya kapanması.
- Karakterin dengeyi yeniden kazanması.
- Diğer kişinin yeni duruma uyum sağlaması.

Dengeyi toparlama hareketi sahnede zaten açıkça okunmuşsa onu uzatma.

### 11.2. “Aksiyon devam etsin” yerine ölçülebilir ilerleme

Zayıf:

~~~text
Keep the action intense for the full ten seconds.
~~~

Daha somut:

~~~text
The subject keeps pulling the same heavy object toward the marked opening.
The object advances in short visible increments.
Near the end of the shot, it clears the edge and the subject shifts weight
to control the sudden release.
~~~

Bu hareketin on saniye sürmesi fiziksel tasarıma uygunsa kullanılabilir. Küçük ve hafif bir nesneye yapay ağırlık ekleyerek süre yaratma.

### 11.3. Uzay ve manzara planları

Geniş görüntünün süresini şu işlevlerden biri gerekçelendirebilir:

- Ölçeğin yavaşça anlaşılması.
- Yolun veya engelin görünmesi.
- Araçla hedef arasındaki ilişkinin değişmesi.
- Bir örtünün arkasındaki bilginin açılması.
- Sonraki sahnenin yönünün kurulması.

Sadece “epic space, slow camera” yazılması, on saniyelik bir anlatı ilerlemesi tarif etmez.

~~~text
The camera makes one slow lateral move past the foreground structure.
As the foreground clears, the destination becomes visible in relation
to the small vehicle already in the frame.
The vehicle maintains a consistent trajectory toward that destination.
The vehicle keeps moving along that trajectory through the end of the shot.
~~~

Buradaki yeni bilgi hedef ile aracın ilişkisi. Aynı ilişki ilk karede zaten açıksa kamera hareketi gereksiz olabilir.

### 11.4. Gerilim

Gerilim planında beklemek işe yarayabilir; çünkü beklenen şey önemlidir.

Bekleyişi görünür kılan unsurlar:

- Azalan bir mesafe.
- Belirli bir yerden gelen ve karakterin takip ettiği ses.
- Açıklığı yavaşça değişen bir kapı.
- Yükü tutmakta zorlanan el.
- Kararını henüz verememiş ama davranışı değişen karakter.

Rastgele nefes, göz kırpma ve parçacık hareketi tek başına gerilim kurmaz.

### 11.5. Duygusal plan

Replikten sonraki yüz, hikâyenin asıl kısmı olabilir. Böyle bir planı “konuşma bitti” diye kesmek de hatadır.

Tepkiyi genel bir sıfat yerine oynanabilir değişimle tanımla:

- Gözler bir kişiden belirli bir nesneye geçer.
- Başta sıkılı duran çene gevşer.
- Uzanmış el geri çekilir.
- Karakter cevap verecek gibi olur, vazgeçer.
- Başını çok küçük bir hareketle onaylar ve eyleme geçer.

Hepsini aynı yüze yükleme. Bir veya iki okunabilir değişim seç.

### 11.6. Tek kamera ve timelapse

**Kesintisiz plan:** Süreyi bir görevin gerçek gelişimi taşır. Kamera sabit olsa da karakterin niyeti, mesafe, nesne konumu veya bilgi değişebilir.

**Timelapse:** İş altıncı saniyede tamamlanıyorsa son dört saniye final sunumu olabilir. Bitmiş mekânın okunmasına yarıyorsa boşluk değildir; sunumda kamera ya da ışık yine hareket eder. Ancak aynı final görüntüsü her çekimin sonunda dört saniye tekrar ediyorsa ara çekimlerde iş son vuruşa kadar sürdürülür, uzun sunum yalnız finalde bırakılır.

Timelapse'e anlatılı filmdeki konuşma–tepki şablonu otomatik uygulanmaz.

## 12. Kopyalanabilir video istemleri

### 12.1. Önce kısa ve nedensel sürüm

~~~text
Use the supplied image as the starting frame.
[CAMERA_SETUP].

[SUBJECT] begins [ONE_MAIN_ACTION] from [INITIAL_STATE].
The action progresses through [NATURAL_STAGE_OR_RESISTANCE].
Once [CAUSE] occurs, [VISIBLE_CONSEQUENCE] follows.
The subject responds by [ONE_RELEVANT_REACTION_OR_DECISION].

End with [OUTGOING_STATE] that the next shot can continue from.
Preserve [ESSENTIAL_IDENTITY_AND_GEOMETRY_ANCHORS].
Audio: [EXACT_DIALOGUE_IF_ANY] and [MATCHING_SOUNDS].
~~~

Görselde zaten açık olan bütün yüz, kıyafet ve mekân ayrıntılarını video isteminde tekrar tekrar tarif etmek yerine hareketin önceliği korunur. Kimlik için gerekli kısa sabitler tutulur.

### 12.2. Konuşma sonrası devam eki

~~~text
After finishing the line, [SUBJECT] immediately [RELEVANT_ACTION].
This causes [VISIBLE_RESULT].
The final part of the shot shows [SUBJECT] registering that result
and beginning [NEXT_LOGICAL_BEHAVIOR].
Keep the progression natural and in this order.
~~~

“Immediately” burada dört saniyelik gereksiz durmayı önlemek için kullanılır. Duygusal olarak bekleme gerekiyorsa “After a brief, readable hesitation” gibi doğru niyet yazılır.

### 12.3. Tek sürekli hareket eki

~~~text
The action remains in progress through most of the shot.
Show gradual, visible progress toward [CLEAR_GOAL].
The motion responds to [ESTABLISHED_PHYSICAL_CONDITION].
The result occurs in the last beat; the motion continues through it, with no frozen ending.
~~~

Bu şablon her hareketi yavaşlatma komutu değildir. Sahnede süre taşıyabilecek iş varsa kullanılır.

### 12.4. Yaklaşık zamanlamalı tam şablon

~~~text
START FRAME
Use [ACTUAL_START_IMAGE] as the starting frame.

SHOT
One continuous [SHOT_SIZE].
Camera: [LOCKED_OR_ONE_PURPOSEFUL_MOVE].
Target source duration: 10 seconds.

DRAMATIC PURPOSE
By the end of the shot, [ONE_CLEAR_CHANGE] must be readable.

BEATS (2-4, 0 to 10 with no gap, each ≥2 s)
[0-A s] — [INITIAL_ACTIVE_STATE, already in motion].
[A-B s] — [MAIN_LINE_OR_ACTION].
[B-C s] — [DIRECT_CONSEQUENCE].
[C-10 s] — [RESPONSE_OR_OUTGOING_BEHAVIOR, still moving].

DIALOGUE
[VISIBLE_SPEAKER]: "[EXACT_LINE]"
Delivery: [NATURAL_PERFORMANCE].
[OFFSCREEN_LINE_ONLY_IF_NEEDED].

AUDIO
[AMBIENCE].
[PHYSICAL_SOUNDS_MATCHING_THE_ACTION].
[MUSIC_PREFERENCE_IF_RELEVANT].

CONTINUITY
Preserve [IDENTITY], [OBJECT_OWNER], [HAND], [GEOMETRY] and [DAMAGE_STATE].

ENDING
[EXACT_OUTGOING_STATE], still in motion at 10 s.
~~~

Hattaki promptun tam biçimi (Reference anahtarı, ORTAK GÖRÜNÜM cümlesi, kimlik cümlesi) goruntu-yonetmeni ajanındadır; bu şablon yalnız 10 s'nin iç planını gösterir.

### 12.5. Kısa prompt ile ayrıntılı yönetmen notunu ayır

Üretim dosyasında ayrıntılı saniye tablosu bulunabilir. Video modeline verilen metin, bütün kontrol listelerinin tekrarlandığı bir sayfa olmak zorunda değildir.

**Plan kartı:** Neden, referans, süre hesabı, kurgu seçeneği, kontrol ölçütleri.  
**Üretim istemi:** Görselden başlayarak ne olacak, hangi sırayla olacak, kim konuşacak, nasıl bitecek.

Her denemede promptu biraz daha uzatmak yerine yanlış anlaşılan tek ilişkiyi düzelt.

## 13. Üretilmiş boş klibi kurtarmak

### 13.1. İlk tercih: iyi kısmı koru, çekimi kısaltma

1. Kaynağın kopyası üzerinde çalış (ham klip `~/film_medya/<FILM>/ham/` altında kalır).
2. Son anlamlı değişimin bittiği anı işaretle (`kareler.py kuyruk`).
3. Temiz kısım 10 s'yi karşılıyorsa en iyi 10 s'yi seç.
4. Karşılamıyorsa `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırasını uygula.
5. Bir sonraki çekimle birlikte izle.
6. Ses geçişini ayrıca dinle.
7. `kurgu.py kontrol` ile her parçanın 10 s olduğunu doğrula.

### 13.2. Kurtarma seçenekleri

| Elde ne var? | Yapılacak iş | Yeni üretim |
| --- | --- | --- |
| Temiz kısım ≥10 s | En iyi 10 s'yi seç | Gerekmez |
| İyi ana bölüm, boş son | Başka deneme → devam üretimi → iki denemeyi birleştirme | Çoğu kez bir |
| İyi ses, zayıf son görüntü | Sesi koru; görüntünün sorunlu bölümünü aynı çekimin başka denemesiyle gizli kesmeyle değiştir | Eldeki denemeye bağlı |
| İyi ana bölüm, gerekli sonuç eksik | Sonucu devam üretimiyle aynı çekime ekle; ayrı kadraj gerekiyorsa çekim listesine (F3) | Genellikle bir |
| Hareketin kendisi yanlış veya anlaşılmaz | Vuruş planını sadeleştirip yeniden üret | Gerekir |
| Son dört saniye anlamlı ama yavaş | Kullanılabilir; aynı çekimin daha canlı denemesi varsa o seçilir | Çoğu kez gerekmez |

### 13.3. İki denemeyi birleştirmek

Birleştirilen iki parça **aynı çekime** ait olmalı: aynı kadraj, aynı an, aynı nesne durumu. Gizli kesme şu yerlere düşer:

- Kadrajdan geçen bir nesne ya da kişinin arkası.
- Hızlı bir baş ya da beden hareketinin ortası.
- Kameranın kısa bir yönelimi.

Farklı sahneden alınmış güzel bir görüntü süreyi doldursa bile devamlılığı bozar; kullanılmaz.

### 13.4. İlk altı saniye iyi, son dört saniye kötü ise

Bütün 10 saniyeyi tekrar üretmek tek seçenek değildir. Kesip 6 s kullanmak ise seçenek değildir.

**Seçenek A:** Aynı çekimin başka denemesinde temiz 10 s ara.
**Seçenek B:** Ana planın uygun son karesinden, kimlik ve durum korunarak yalnız devamı üret ya da Omni uzatma kullan; gerçek birleşme noktasını kontrol et.
**Seçenek C:** Aynı çekimin iki denemesini gizli kesmeyle birleştir.
**Seçenek D:** Vuruş planını düzeltip çekimi yeniden üret (son vuruşa somut bir devam yaz).

Seçenek B, modelin desteklediği görüntü girişi veya uzatma moduna göre uygulanır (`FLOW_GERCEKLERI` Ek 2). Tek tek kareyle birleştirmek hareket hızını, bakış yönünü ve ışığı otomatik eşleştirmez.

### 13.5. Genellikle yanlış ilk çözümler (hatta yasak)

**Altı saniyeyi on saniyeye yavaşlatmak:** Hız yüzde 60 olur. Konuşma, yerçekimi, ağırlık ve yüz hareketi yapaylaşabilir. Bilinçli ağır çekim estetiği dışında varsayılan çözüm yapma.

**Son kareyi dört saniye dondurmak:** Filmde bilinçli bir donma etkisi yoksa hareketin kesildiği anlaşılır.

**Aynı hareketi ileri–geri oynatmak:** Yürüyüş, el ve mekanik yönleri bozabilir.

**Her boşluğa zoom eklemek:** Yaklaşma yeni bilgi göstermiyorsa sorun yalnızca hareketli boşluğa dönüşür.

**Rastgele efekt eklemek:** Sahneye yeni olay katmış gibi görünür ama anlam ve devamlılık yaratmayabilir.

**Müziği yükseltmek:** Görüntünün görevini değiştirmez.

### 13.6. Dijital kırpma ne zaman yardımcı olur?

Yüksek çözünürlüklü kaynakta zaten var olan anlamlı tepkiyi daha görünür kılmak için ölçülü kırpma kullanılabilir. Kaynakta olmayan tepkiyi yaratmaz. El, göz veya önemli nesne kırpma nedeniyle kaybolmamalıdır.

## 14. Ses, J-cut ve L-cut

Adobe'nin açıklamasına göre J-cut'ta sonraki planın sesi görüntüsünden önce gelir; L-cut'ta önceki planın sesi sonraki görüntü üzerinde sürer.[^adobe]

**J-cut örneği:** Dinleyen karakterin yüzünü görürken sonraki konuşmacının sesi başlar; sonra konuşmacıya kesilir.

**L-cut örneği:** İlk karakter konuşurken görüntü dinleyiciye geçer; ilk karakterin cümlesi dinleyici görüntüsü üzerinde biter.

Böylece konuşmayı bitiren yüzün üstünde gereksiz yere beklemek yerine sözün etkisi gösterilebilir. Ses geçişi, kendi başına anlamsız görüntüyü düzeltmez.

### 14.1. Uygulama notları

- Görünür ağız ile ses çelişmemeli.
- Aynı mekânın ortam sesi geçişte kopmamalı.
- Fiziksel temas sesi ilgili görüntüyle birlikte kalmalı.
- Kadraj dışı konuşma anlaşılır olmalı.
- Ses katmanları yeni görüntü süresi yaratmaz; film süresi zaman çizelgesinden ölçülür.
- Amaçsız son bölümü yalnız sesle örtme; çekimi yeniden tasarla ya da `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırasını uygula.

### 14.2. Konuşma bittikten sonra sessizlik

Sessizlikte işitilecek dünya tamamen yok olmak zorunda değildir. Odaya ait hava, kumaş, ayak veya mekanizma sesi sürdürülebilir. Bunlar sahnenin fiziksel sürekliliğini taşır; yeni olayın yerini tutmaz.

Sesin sonunu çok sert kesmek repliği yutabilir. Gereken nefes ve doğal sönüm korunur; görüntünün aynı yüzde kalması şart değildir.

## 15. Dört, sekiz ve on altı dakikalık film hesabı (her çekim 10 s)

### 15.1. Çekim sayısı sabittir

| Hedef | Çekim sayısı | Filmdeki süre |
| --- | ---: | --- |
| 2 dakika / 120 saniye | 12 | 12 × 10 = 120 s |
| 4 dakika / 240 saniye | 24 | 24 × 10 = 240 s |
| 8 dakika / 480 saniye | 48 | 48 × 10 = 480 s |
| 16 dakika / 960 saniye | 96 | 96 × 10 = 960 s |

Kılavuzun ilk sürümü "her klipten 6 s kullanılırsa 4 dakika 144 s'ye düşer" hesabını yapıyordu. Hatta bu hesap oluşmaz: çekim kısalmaz, eksik saniye üretimde tamamlanır.

### 15.2. Değişen şey deneme sayısıdır

Süre sabit olduğu için boş sonların bedeli **deneme ve devam üretimi** olarak ödenir:

| Durum | Bedel |
| --- | --- |
| Temiz 10 s ilk denemede | 1 üretim |
| Temiz kısım kısa, devam üretimi tuttu | 2 üretim |
| İki deneme birleştirildi | 2 üretim |
| Vuruş planı düzeltildi, yeniden üretildi | 2 ya da daha çok |

Bu yüzden boş sonu planda yakalamak (F3 metin animatiği, F5 vuruş planı, F7c kareli animatik) üretimde yakalamaktan ucuzdur. Bunlar kota tahmini değildir.

### 15.3. Dört dakikalık bir planın iç ritmi

24 çekimin hepsi 10 s'dir; ritim çekimlerin içinden gelir:

- Bazı çekimler 2 vuruşlu (0-6 / 6-10): uzun replik ve sonucu.
- Bazıları 3 vuruşlu (0-2 / 2-7 / 7-10): sürekli çaba.
- Bazıları 4 vuruşlu (0-2 / 2-5 / 5-8 / 8-10): hızlı aksiyon.
- Kadraj ve ölçek komşu çekimler arasında değişir; aynı mekânda ardışık iki çekim aynı ölçekte olmaz.

### 15.4. Gerçek montaj süresini kontrol et

- İlk 30 saniyede başlık kartı ve siyah ekran yok; başlık C03'ün üzerine yazı katmanıdır (`ILK_30_SANIYE_KILAVUZU`).
- Geçiş türü (kesme · karışım · karartma) toplam süreyi etkileyebilir; `kurgu.py gecis` hesaplar.
- Aynı kaynak parçanın iki kez kullanılması yeni bilgi yaratmaz.
- Nihai hesap `kurgu.py kontrol` ve dışa aktarılan dosyanın gerçek süresidir.

## 16. Altı çekimle tam 60 saniye: süre sabit, ritim değişken

Aşağıdaki tablo bir film konusu değildir. Altı adet 10 s'lik çekimin farklı iç ritimlerle nasıl birleşebileceğini gösterir.

| Çekim | Zaman çizelgesi | Vuruşlar | İşlev |
| --- | --- | --- | --- |
| C01 | 00:00–00:10 | 0-4 dikkat çeken durum (hareket hâlinde) · 4-10 durumun karakter üzerindeki etkisi | Sorun ve vaadin dünyası |
| C02 | 00:10–00:20 | 0-6 hedefi belirleyen kısa konuşma · 6-10 önemli nesneye yönelim | İnsan ve hedef |
| C03 | 00:20–00:30 | 0-2 hazırlık · 2-7 ilk girişim · 7-10 girişimin sonucu | Kapak anı ya da parçası |
| C04 | 00:30–00:40 | 0-3 yeni koşulu fark etme · 3-8 uyum sağlanan çaba · 8-10 kısa karar | Baskı artar |
| C05 | 00:40–00:50 | 0-5 kararın uygulanması · 5-10 mekân veya durum değişiminin okunması | Sonuç |
| C06 | 00:50–01:00 | 0-2 sonuçla yüzleşme · 2-5 tepki · 5-8 yeni durum · 8-10 sonraki bölüme yönelme | Geçiş |

**Toplam:** 60 saniye. **Çekim sayısı:** 6. Her çekimin vuruş sayısı ve sınırları farklı; ölçek komşu çekimler arasında değişir.

### 16.1. İlk 10/30/60 saniye hedefleri nasıl korunur?

İzleyicinin gördüğü montaj zamanına bak (C01-C03 = ilk 30 saniye, `ILK_30_SANIYE_KILAVUZU`):

- İlk on saniyede (C01) dikkat çeken olay ve ona verilen karşılık okunuyor mu?
- Otuzuncu saniyeye kadar (C03) hedef veya baskı netleşiyor mu?
- Altmışıncı saniyede (C06) ilk kararın bir sonucu görülüyor mu?

Bunlar anlatı tasarımı sorularıdır; platformun kesin izlenme kuralı değildir.

## 17. Ek planlar ve üretim bütçesi

### 17.1. Her konuşma için gerekli görüntüyü önceden düşün

Önemli bir sahnede şu dört görüntü türünün hepsi veya bazıları gerekebilir:

| Plan türü | Görevi | Ne zaman üret? |
| --- | --- | --- |
| Ana/genel plan | Kim nerede, olay ne? | Mekân ilişkisi belirsizse |
| Konuşmacı | Replik ve karakter niyeti | Yüz performansı önemliyse |
| Dinleyici | Sözün etkisi | Tepki kararı veya ilişkiyi değiştiriyorsa |
| Detay/sonuç | Olayın somut kanıtı | Ana planda sonuç okunmuyorsa |

Bütün sahnelere otomatik dört yeni üretim ekleme. Ana görüntü işini zaten yapıyorsa aynı bilgiyi çoğaltmak gerekmez. Çekim sayısı sabit olduğu için her ek plan ya mevcut çekimin bir vuruşudur (tek kadrajda) ya da başka bir çekimin yerini alır.

### 17.2. Kurguyu önce ucuz biçimde dene

Gerçek video üretiminden önce:

1. Onaylı başlangıç görsellerini zaman çizelgesine koy (hatta kareli animatik, F7c).
2. Replikleri geçici sesle veya kendi okumanla yerleştir.
3. Her kareyi 10 s tut; vuruş sınırlarını işaretle.
4. Altı saniyeden sonra izleyicinin ne göreceğini her çekim için tek cümleyle yaz.
5. Gerekli tepki ve sonuç görüntülerini işaretle.
6. Ancak sonra hareket üretimine geç.

Bu kaba deneme, hareket kalitesini test etmez; sahnenin zaman ve bilgi dağılımını test eder. Durağan bir taslakta bile dört saniyenin görevi açıklanamıyorsa video üretimi o boşluğu kendiliğinden çözmeyebilir.

### 17.3. Sınırlı deneme yaklaşımı

Bütün filmi üretmeden önce farklı işlevde birkaç plan seç:

- Konuşma sonrası fiziksel sonuç.
- Sessiz tepki.
- Sürekli aksiyon veya bilgi açan geniş plan.

Bir denemede tek bir değişkeni değiştir:

- Repliğin uzunluğu.
- Replik sonrası davranış.
- İlk görselin eylem öncesi konumu.
- Zaman işaretleri.
- Kamera hareketinin kaldırılması.

İki benzer denemede aynı bölüm hâlâ boş kalıyorsa yalnız daha uzun istem yazmak yerine vuruş planını değiştirmeyi, başlangıç karesini daha erken evreye çekmeyi ya da devam üretimini değerlendir. “İki deneme” bir bütçe disiplini önerisidir; teknik sınır değildir.

### 17.4. İyi altı saniyeyi çöpe atma

Yeni üretim yalnız gerekli eksik parçayı tamamlayabiliyorsa bütün planı tekrar üretmek zorunda değilsin. Bu yöntem mevcut iyi yüzü, sesi veya eylemi koruyabilir.

Devam üretiminin ilk durumu ana planın son durumuyla uyumlu olmalı. Birleştirme aynı çekimin içinde gizli kesmeyle yapılır; dikiş `kareler.py dikis` ile kontrol edilir.

### 17.5. Üretim günlüğü

| Kaynak | Amaç | Kaynak süresi | Temiz aralık | Temiz süre | Sorun | Sonraki karar |
| --- | --- | ---: | --- | ---: | --- | --- |
| C01_take01 | [İşlev] | [Gerçek] | [Giriş–çıkış] | [Hesap] | [Somut] | [10 s seç / başka deneme / devam üretimi / birleştir / yeniden üret] |
| C02_take01 | [İşlev] | [Gerçek] | [Giriş–çıkış] | [Hesap] | [Somut] | [Karar] |

Hatta bu günlük `medya.py al` ile tutulan DENEMELER kaydıdır. “Hep yarısı boş çıkıyor” hissini ölçülebilir hâle getirir. Birkaç örnekten bütün model hakkında kesin başarı oranı çıkarma.

## 18. Gerçek çıktıyı ölçme yöntemi

### 18.1. Dört izleme

**Birinci izleme — Normal seyir:** İzleyici gibi izle. Bekleme hissettiğin anı not et.

**İkinci izleme — Ses kapalı:** Görüntüde ne değişiyor? Karar veya sonuç konuşma olmadan da okunuyor mu? Diyaloğa dayalı sahnede her şeyin sessiz anlaşılması şart değildir; bu izleme görsel davranışı ayırmak içindir.

**Üçüncü izleme — Ses odaklı:** Konuşma doğal mı? Replik nerede bitiyor? Fiziksel ses hangi anda geliyor?

**Dördüncü izleme — Komşu planlarla:** Tek başına iyi olan bekleyiş, önceki ve sonraki görüntüler arasında gereksizleşebilir.

### 18.2. İşaretlenecek anlar

~~~text
KAYNAK: [FILENAME]
GERÇEK KAYNAK SÜRESİ: [SECONDS]

İLK GEREKLİ GÖRÜNTÜ: [TIME]
KONUŞMA BAŞLANGICI: [TIME_OR_NONE]
KONUŞMA BİTİŞİ: [TIME_OR_NONE]
ANA EYLEMİN TAMAMLANDIĞI AN: [TIME]
TEPKİNİN OKUNDUĞU AN: [TIME_OR_NONE]
SON GEREKLİ DEĞİŞİM: [TIME]

TEMİZ ARALIK: [IN–OUT] · TEMİZ SÜRE: [OUT_MINUS_IN]
SEÇİLEN 10 S ARALIK: [IN–IN+10] (temiz süre ≥10 ise)

BOŞ ARALIK VE ÇÖZÜM YOLU:
[Bilgi, duygu veya mekân açısından neyi tekrar ediyor?]
[Başka deneme / devam üretimi / birleştirme / sonuç planı]
~~~

### 18.3. Örnek ölçüm

Aşağıdaki değerler yöntemi göstermek için oluşturulmuş örnektir; gerçek videodan ölçülmüş değildir.

- Kaynak: 10 saniye.
- Replik: 0,4–5,4.
- Tepki: 5,4–6,4.
- Yeni anlam taşımayan bekleyiş: 6,4–10,0.
- Temiz aralık: 0,2–6,4.
- Temiz süre: 6,2 saniye; 10 s'ye 3,8 s eksik.
- Karar: aynı çekimin ikinci denemesine bakılır; yoksa 6,4 s'deki temiz kareden devam üretimi.

Yüzde 62 bir kalite puanı değildir. İyi altı saniye korunur; eksik kısım üretimde tamamlanır.

### 18.4. Son dört saniyenin işlev sorusu

Her 10 saniyelik kaynak için şu cümleyi tamamla:

> “6. saniyeden sonra izleyici ______ görerek/duyarak ______ anlıyor.”

Cümle yalnız “karakteri biraz daha görüyor” diye dolduruluyorsa son vuruş boştur: planda yakalandıysa vuruş planı yeniden yazılır, üretimde yakalandıysa `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6.

Fakat cevap “aldığı karardan vazgeçmediğini yüzünde okuyor” ise bekleyiş işlevli olabilir. Bunu gerçek oyunculuk göstermelidir; plan metninde yazması yeterli değildir.

### 18.5. Kontrol ölçütleri

| Ölçüt | Kabul sorusu |
| --- | --- |
| Amaç | Planın neden var olduğu tek cümlede açıklanabiliyor mu? |
| İlerleme | Giriş durumuyla çıkış durumu arasında gerekli değişim var mı? |
| Doğal tempo | Konuşma veya hareket sırf süre için uzatılmış mı? |
| Tepki | Gerekliyse okunuyor mu; gereksizse tekrar ediyor mu? |
| Bitiş | Son vuruş donuyor mu; 10. saniyede hareket sürüyor mu? |
| Süre | Seçilen aralık 10,0 s mi ve tamamı temiz mi? |
| Bağlantı | Sonraki plan bu durumu tutarlı devralıyor mu? |
| Ses | Söz, ağız, ortam ve fiziksel sesler uyumlu mu? |

## 19. Hata–neden–çözüm tablosu

| Hata | Önce bakılacak yer | Çözüm |
| --- | --- | --- |
| Replik 4 saniyede bitiyor, kalan 6 saniye boş. | Repliğin doğal süresi ve planın amacı | Gerçek sonuç/tepki vuruşu ekle ya da başlangıç karesini daha erken evreye çek; gereksiz kelime ekleme. |
| Replik 10 saniyeye sığmıyor. | Kelime, duraklama ve eşzamanlı hareket | Repliği sadeleştir veya iki çekime böl (J/L ile). |
| Eylem ilk saniyede tamamlanıyor. | Başlangıç görseli ve eylemin büyüklüğü | Eylem öncesi kare kur; eylemi evrelerine böl. |
| Karakter çok yavaş konuşuyor. | “Slow”, “dramatic pause”, süre doldurma talimatları | Doğal performans iste; açılan saniyeye sonraki evreyi yaz. |
| Her klipte kamera boş yere yaklaşıyor. | Otomatik kamera şablonu | Hareketi kaldır veya açığa çıkaracağı bilgiyi tanımla. |
| Üç olay bir anda gerçekleşiyor. | Aşırı dolu istem | Aynı hedefe ait aşamaları ayır; bağımsız olayları ayrı plan yap. |
| İkinci karakter yanlış repliği söylüyor. | Konuşmacı ataması | Görünür tek konuşmacı veya ayrı planlar. |
| Tepki sahnesi önceki durumu geri getiriyor. | Nesne sahibi, el, hasar ve zaman | Tepki referansını doğru ana göre hazırla. |
| Uzun bekleme sıkıcı ama hikâyede gerekli. | Beklemede görülen baskı/karar | Beklemede değişen bir şey yaz (mesafe, tutuş, ışık, ses kaynağı). |
| Yeni detay planı güzel ama ilgisiz. | Önceki eylemle neden-sonuç ilişkisi | Doğrudan sonucu gösteren detay seç. |
| Ses kesmelerde kopuyor. | Ortam ve replik sonu | Ortam sürekliliği kur; gereken ses kuyruğunu koru. |
| Temiz kısım 10 s'ye ulaşmıyor. | DENEMELER'deki temiz aralıklar | `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası; yavaşlatma, döngü, donma yok. |
| Zaman damgaları uygulanmıyor. | İstemin karmaşıklığı ve modun yeteneği | Vuruş sayısını azalt (2-3); 10 s'lik aralığı klibin kullanılabilir kısmından seç. |
| İlk plan iyi, devamı kimlik değiştiriyor. | Yanlış/eksik referans veya son kare | Doğru onaylı kareyi ve kimlik referansını kullan. |
| Her son “şok bakış” oluyor. | Tekrarlanan kapanış şablonu | Planın görevine göre karar, sonuç ya da sonraki adıma geçiş yaz. |

## 20. Yeni klip kartı formatı

C etiketleri hattın çekim numaralarıdır. Hatta bu bilgiler FILM.md §4 ve PROMPTLAR/ dosyalarında durur; kart düşünme aracıdır. Ham süre ile temiz süre ayrı alanlardır; montaj süresi her zaman 10 s'dir.

### 20.1. Doldurulabilir kart

~~~text
C[NN] — [PLAN_ADI]

TÜR:
[TEK ÇEKİM — 10 S]

FLOW:
[GERÇEK MODEL MODU]

EKLE:
- Başlangıç karesi: [GERÇEK DOSYA]
- Kimlik/mekân referansları: [GERÇEK DOSYALAR]
- Bitiş karesi: [YALNIZ DESTEKLENİYORSA VE VARSA]

HAM ÜRETİM SÜRESİ:
[10 S (OMNI) / UZATMA İLE DAHA UZUN]

MONTAJ KULLANIMI:
[10 S — SABİT]

FİLM İÇİNDEKİ ZAMAN:
[(NN−1)×10 – NN×10 S]

PLANIN GÖREVİ:
[Bu plan izleyicide neyi değiştirecek?]

GELEN DURUM:
[Kim, nerede, hangi nesne/hasar/konum?]

ANA EYLEM:
[Bir hedef]

DİYALOG:
[Konuşmacı + kesin replik]
[Tahmini süre + gerçek çıktıdan sonra ölçülecek alan]

VURUŞLAR (2-4, 0-10 boşluksuz, her biri ≥2 s):
[0-A s: başlangıç, hareket hâlinde]
[A-B s: ana girişim/replik]
[B-C s: sonuç]
[C-10 s: tepki ya da sonraki adım; donmaz]

REPLİK BİTİNCE:
[Ne olur? Boş bırakılmaz: tepki, sonuç ya da sonraki adım.]

6–10 SANİYEDEKİ İŞLEV:
[Anlamlı devam — boş aralık yazılmaz]

10. SANİYEDEKİ DURUM:
[Hareket sürüyor; sonraki çekimin devralacağı hâl]

KURTARMA YOLU (üretimde temiz kısım kısa kalırsa):
[Başka deneme / devam üretimi / birleştirme / sonuç planı]

EK KAYNAK GEREĞİ:
[0 / hangi plan; henüz üretilmedi]

GÖRSEL İSTEMİ:
[ENGLISH, TEK BAŞLANGIÇ ANI]

VİDEO İSTEMİ:
[ENGLISH, HAREKET + SIRA + SES + ÇIKIŞ]

GERÇEK ÇIKTI KAYDI:
[Kaynak süresi]
[Temiz aralık ve temiz süre]
[Seçilen 10 s aralık]
[Kontrol sonucu]
~~~

### 20.2. Tam film tablosuna eklenecek sütunlar

| Kimlik | Ham süre | Vuruşlar | Gerçek temiz süre | Son dört saniyenin görevi | 10. saniyedeki durum | Kurtarma |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | [s] | [0-a / a-b / b-10] | [üretim sonrası] | [İşlev] | [Hareket] | [Varsa] |
| C02 | [s] | [0-a / a-10] | [üretim sonrası] | [İşlev] | [Hareket] | [Varsa] |

Gerçek temiz süre sütunu üretimden önce doldurulmaz. Öngörü ile ölçüm birbirinden ayrılır.

## 21. Yeni film hazırlayan asistana verilecek ana talimat

Hatta bu iş `/yeni-film` içinde yonetmen (F3) ve goruntu-yonetmeni (F5) ajanlarınındır. Aşağıdaki metin hat dışında bir asistana verilecekse kullanılır:

~~~text
Bu filmi GPT Image başlangıç kareleri ve image-to-video üretimiyle yapacağım.
Kural: Her çekim 10 saniye üretilir ve filmde 10 saniye kullanılır.
Çekim sayısı = hedef süre / 10. Çekim kısaltılmaz.
En önemli sorun şu: Diyalog veya olay 5–6. saniyede bitiyor ve kalan süre
boş görünüyor. Planı bu sorunu önleyecek şekilde tasarla.

1. Her çekimin 10 saniyesini taşıyacak tek bir ana olay seç ve olayın
   doğal evrelerini (hazırlık, girişim, sonuç, tepki) 10 saniyeye yay.
   Süre doldurmak için ilgisiz hareket, rastgele alarm, gereksiz replik
   veya otomatik kamera yaklaşması ekleme.

2. Her çekim için şu alanları ver:
   - Gelen durum.
   - Ana eylem veya kesin replik.
   - Tahmini konuşma süresi; ölçülmüş gibi sunma.
   - Replikten sonra görülecek sonuç, tepki ya da sonraki adım.
   - Vuruş planı: 2-4 vuruş, "a-b s", 0'dan 10'a boşluksuz, her vuruş ≥2 s.
   - 10. saniyedeki durum (hareket sürüyor) ve sonraki çekimle bağlantı.

3. Sessizliği otomatik hata sayma. Sessiz bölümde bilgi, gerilim, duygu
   veya mekânsal anlama ilerliyorsa bunu somut olarak açıkla.
   Yalnız boş bakış varsa o vuruşu yeniden yaz.

4. Bütün çekimleri aynı vuruş kalıbına sokma. Vuruş sayısı ve sınırları
   çekimden çekime değişsin; komşu çekimlerde kadraj ve ölçek değişsin.

5. GPT Image istemi eylemden önceki tek anı kursun.
   Video istemi o görüntüden başlayan hareketi ve vuruşları anlatsın.
   Başlangıç görselinde iş zaten tamamlanmış olmasın.

6. Son vuruş donmasın: "holds still", "freezes", "final pose" yazma.

7. Tepki ya da sonuç ayrı kadraj istiyorsa onu kendi 10 saniyelik çekimi
   olarak öner ve hangi çekimin yerine geçeceğini yaz (çekim sayısı sabit).

8. Zaman damgalarını yönlendirme olarak yaz. Teknik özellikleri
   doğrulanmamış bir modele parametre uydurma.

9. Üretimde temiz kısım 10 saniyeye yetmezse sıra: aynı çekimin başka
   denemesi → temiz son kareden devam üretimi ya da uzatma → aynı çekimin
   iki denemesini gizli kesmeyle birleştirme → sonuç planı.
   Yavaşlatma, döngü, donmuş kare önerme.

10. Gerçek videoyu görmeden “boşluk yok”, “ritim düzeldi” veya
    “senkron tamam” deme. Planlanan ile doğrulananı ayrı göster.

Teslim:
A) Çekim listesi (çekim sayısı = hedef süre / 10).
B) Her çekimin vuruş planı.
C) İstenen kapsamdaki ayrı görsel ve video istemleri.
D) Ayrı kadraj gerektiren tepki/sonuç çekimleri ve yerine geçtikleri çekimler.
E) Üretim sonrası kontrol formu.

Proje bilgilerim:
[HEDEF_SÜRE]
[ORAN]
[MODEL_VE_MOD]
[DİYALOG_DİLİ]
[İSTENEN_TESLİM_KAPSAMI]
~~~

Bu talimat yeni içerik üretimini yönlendirir. Mevcut bir filmi yalnız ritim açısından düzeltmek istediğinde hikâyeyi baştan değiştirmesini istemeyen inceleme talimatını kullan.

## 22. Mevcut planı veya videoyu inceleme talimatı

### 22.1. Planı inceletmek için

~~~text
Aşağıdaki film planını yalnız çekim içi ritim açısından incele.
Mevcut olay örgüsünü, karakterleri ve dünya kurallarını koru.
Kural: her çekim 10 saniyedir ve kısaltılmaz; çekim sayısı sabittir.

Her çekimde:
- Diyalog/eylemin yaklaşık doğal süresini tahmin et.
- Sonuç veya tepki için hangi görüntünün gerekli olduğunu belirt.
- 10 saniyelik sürenin hangi bölümünün amaçsız kalma riski taşıdığını açıkla.
- O bölüm için anlamlı devamı öner (tepki, sonuç, sonraki adım) ve
  vuruş planını yeniden yaz (2-4 vuruş, her biri ≥2 s, son vuruş donmaz).
- Ayrı kadraj gerekiyorsa hangi çekimin yerine geçeceğini yaz.
- Önerinin önceki eylemle nedensel bağını yaz.

Tahminleri gerçek video ölçümü gibi sunma.
Her klibe yeni olay ekleme.
Tek çözüm olarak uzun diyalog veya ağır çekim önermeye çalışma.
Yeni görsel/video üretme; bu görev plan incelemesidir.

Çıktı tablosu:
Çekim | Süre riski | Gerekçe | Önerilen vuruş planı | 10. saniyedeki durum |
Ayrı çekim gereği | Devamlılık notu

Ardından:
1. En kritik düzeltmeler.
2. Düzeltilmiş video istemleri (vuruş planlı).
3. Değişen çekimler ve gereken yeni üretimler.

Plan:
[MEVCUT_PLAN]
~~~

### 22.2. Gerçek videoyu inceletmek için

~~~text
Eklediğim videonun klip ritmini incele.
Önce videoya ve sese gerçekten erişebildiğini belirt.
Erişemediğin bölümlerde izlenmiş gibi kesin zaman verme.

Gerçek çıktıda:
1. İlk gerekli görüntüyü işaretle.
2. Konuşma başlangıç ve bitişini işaretle.
3. Ana eylemin tamamlandığı anı işaretle.
4. Gerekli tepkinin sonunu işaretle.
5. Yeni anlam taşımayan aralıkları gerekçesiyle göster.
6. Temiz aralığı ve temiz süreyi yaz; ≥10 s ise en iyi 10 s'yi öner.
7. 10 s'ye yetmiyorsa önce mevcut malzemeyle (başka deneme, iki denemeyi
   gizli kesmeyle birleştirme) düzeltme öner.
8. Gerekirse yalnız devam üretimi ya da sonuç planı için istem ver.
   Çekimi kısaltmayı, yavaşlatmayı veya donmuş kareyi önerme.

Sessizliği otomatik boşluk kabul etme.
Görüntüde ölçtüğün şeyle senaryodan çıkardığın tahmini ayır.
Ses yoksa diyalog zamanını bildiğini varsayma.

Çıktı:
Gerçek süre | Konuşma aralığı | Son anlamlı değişim |
Temiz aralık | Temiz süre | Seçilen 10 s ya da kurtarma yolu |
Bir sonraki plan için gereken durum
~~~

Araç videoyu oynatamıyorsa yalnız tek bir ekran görüntüsünden gerçek konuşma süresi, hareket akışı veya ses senkronu çıkarılamaz.

## 23. Uygulama sırası, kontrol listesi ve kısa cevaplar

### 23.1. Bir sonraki filmde izlenecek sıra

1. **Hedef süreyi yaz:** Örneğin 240 saniye = 24 çekim.
2. **Her çekimin tek olayını seç:** 10 s'yi taşıyacak evreleri olan bir olay.
3. **Önce olay akışını kur:** Her plan neyi değiştiriyor?
4. **Replikleri prova et:** Tahmini süreyi kaydet.
5. **Her repliğin sonrasını yaz:** Sonuç, tepki, karar ya da sonraki adım; kalan vuruş boş kalmaz.
6. **Görseli buna göre kur:** İş bitmiş pozdan başlamasın.
7. **Kısa video istemini yaz:** Ana eylem, sıra, konuşmacı, sonuç.
8. **Gerekli ek planları belirle:** Her sahneye otomatik ekleme.
9. **Birkaç temsilî üretimle yöntemi dene:** Gerçek sonuçtan öğren (hatta pilot, F3p).
10. **Her çekimden temiz 10 s seç:** İyi kısmı koru; yetmezse başka deneme, devam üretimi, birleştirme.
11. **Bütün sahneyi sesli izle:** Tek tek klipten daha önemli olan akış.
12. **`kurgu.py kontrol` çalıştır:** Her parça 10 s, toplam = çekim sayısı × 10.

### 23.2. Üretim öncesi kontrol

- [ ] Klibin tek cümleyle açıklanabilen bir görevi var.
- [ ] İlk görsel eylemin başlangıcına uygun.
- [ ] Konuşma süresi prova veya açık varsayımla tahmin edilmiş.
- [ ] Replikten sonra ne olacağı belli (tepki, sonuç ya da sonraki adım).
- [ ] Son dört saniyeye yalnız dekoratif hareket eklenmemiş.
- [ ] Son durum sonraki klibe bağlanıyor.
- [ ] Saniye etiketleri kesin model garantisi gibi sunulmuyor.
- [ ] Tek üretimde gereksiz çok sayıda kesme ve bağımsız olay istenmiyor.
- [ ] Vuruş planı 2-4 vuruş, 0-10 boşluksuz, her vuruş ≥2 s; son vuruş donmuyor.
- [ ] Ayrı kadraj gerektiren tepki/sonuç çekim listesinde ve yerine geçtiği çekim belli.

### 23.3. Üretim sonrası kontrol

- [ ] Kaynağın gerçek süresi ölçüldü.
- [ ] Diyalog ve eylemin gerçek bitişi işaretlendi.
- [ ] Sessiz bölümün görevi görüntüde okunuyor.
- [ ] Seçilen 10 s aralığın tamamı temiz.
- [ ] Eksik saniyeler yavaşlatma, döngü ya da donmuş kareyle doldurulmadı.
- [ ] Ses ve görüntü bağlantısı dinlendi.
- [ ] Ek plan doğru zamana ve duruma ait.
- [ ] `kurgu.py kontrol` geçti.
- [ ] Yapılmayan üretim veya kontrol tamamlandı diye yazılmadı.

### 23.4. Sık sorular

**“Bütün replikler tam on saniye mi sürmeli?”**  
Hayır. Çekim 10 s'dir, replik değil. Repliğin görevine göre süre verilir; kalan vuruşlara tepki, sonuç ya da sonraki adım yazılır. Her boşluk konuşmayla kapatılmaz.

**“Her klibin sonuna iki saniye tepki ekleyeyim mi?”**  
Hayır. Tepki gerekiyorsa ve gerçekten yeni anlam taşıyorsa kullan. Zaten görünen sonucu tekrar etme.

**“Saniye saniye yazarsam sorun kesin çözülür mü?”**  
Hayır. Vuruş planı sıralama ve tempo yönlendirmesi sağlar; gerçek çıktı yine ölçülür ve 10 s'lik aralık temiz kısımdan seçilir.

**“Altı saniye iyi çıkması başarısızlık mı?”**  
Başarısızlık değil ama yetmez. İyi altı saniye korunur; eksik dört saniye başka deneme, devam üretimi ya da iki denemeyi birleştirmeyle tamamlanır. Çekim kısalmaz.

**“Görev gerçekten altı saniyelikse?”**  
Hatta her çekim 10 s olduğu için aynı hedefe ait doğal çaba, sonuç ve tepki tasarlanır; gerekirse ilk görsel daha erken evreye çekilir. Yine de altı saniyelikse iki komşu çekimin işi birleştirilir ve açılan yer sahnenin eksik bilgisine verilir (F3). Anlamsız dört saniye kalite diye sunulmaz.

**“Diyaloğu ayrı üretmek daha mı iyi?”**  
Bazı işlerde ses süresini önceden bilmek kurguyu kolaylaştırır. Görünür ağız varsa senkronu ayrıca çözmek gerekir. Her proje için otomatik daha iyi değildir.

**“Kamera hareketiyle kalan süreyi değerlendirebilir miyim?”**  
Kamera yeni bilgi veya mekânsal ilişki gösteriyorsa evet. Sadece kadrajı oynatıyorsa boşluğu çözmeyebilir.

**“Sinematik duraklamayı nasıl korurum?”**  
Duraklamayı bir vuruş olarak yaz (≥2 s) ve içinde neyin değiştiğini söyle: düşüncenin yüzde okunması, yaklaşan sonuç, izleyicinin anlaması gereken ayrıntı.

### 23.5. Tek ekranlık kısa kontrol

~~~text
REPLİK BİTTİ.

Sonuç veya gerekli tepki sürüyor mu?
- Evet: Onu görünür davranışla tarif et ve son vuruşa yaz.
- Hayır: Sonraki adımı (karar, yönelme, işin devamı) son vuruşa yaz.

Çekim 10 saniye. Kısalmaz.
- Vuruşlar 0'dan 10'a boşluksuz, her biri ≥2 s.
- Son vuruş donmaz; 10. saniyede hareket sürer.

Üretimde temiz kısım 10 saniyeye yetmedi mi?
- Başka deneme → devam üretimi → birleştirme → sonuç planı.
- Yavaşlatma, döngü, donmuş kare yok.
~~~

## 24. Kaynaklar ve önerilerin sınırı

Bu kılavuzdaki örnek sahneler, saniye dağılımları, üretim tabloları ve ana talimatlar bu çalışma için hazırlanmış editoryal önerilerdir. Model garantisi, ölçülmüş izleyici araştırması veya resmî platform kuralı değildir.

### 24.1. Doğrulanan teknik dayanak

**Gemini Omni 1.1 Flash:** 21 Ekim 2026 tarihinde kontrol edilen Google model sayfası, gemini-omni-1.1-flash-preview için görselden video, ilk/son kare, ses üretimi ve en fazla 10 saniyelik video desteğini listeliyor. Kullandığın arayüzün aynı sürümü ve modu sunduğu ayrıca kontrol edilmeli. Bir özelliğin desteklenmesi, iç zamanlamanın kusursuz olacağı anlamına gelmez.[^omni]

**Video isteminin parçaları:** Google'ın istem rehberi özne, eylem, kamera, zaman içindeki gelişim ve ses yönlendirmelerini ayrı öğeler olarak ele alıyor. Bu belge bunları kısa ve nedensel planlara dönüştürür.[^googleprompt]

**Image-to-video ve yaklaşık zamanlama:** Runway kaynağı kendi modellerine yönelik bir rehberdir. Burada hareket odaklı yazım ve yaklaşık olay sırası için yararlanılmıştır; aynı performansın Omni veya Veo'da garanti edildiği ileri sürülmez.[^runway]

**Sesli kurgu:** J-cut ve L-cut tanımları Adobe'nin resmî eğitiminden doğrulanmıştır.[^adobe]

### 24.2. Kaynak bağlantıları

[^omni]: Google Cloud, [Gemini Omni 1.1 Flash Preview](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/omni-1-1-flash). Erişim: 21 Ekim 2026. Bu belge yalnız görevle ilgili destek ve süre bilgilerini kullanır.

[^googleprompt]: Google Cloud, [Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide). Erişim: 21 Ekim 2026. Özellikle istem bileşenleri, temporal elements ve audio bölümleri.

[^runway]: Runway, [Image to Video Prompting Guide](https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide). Erişim: 21 Ekim 2026. Görselin rolü, hareket odaklı istem ve sequential prompting bölümleri.

[^adobe]: Adobe, [Perform J cuts and L cuts](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-j-cuts-and-l-cuts.html). Erişim: 21 Ekim 2026. Ses ve görüntü kesmelerinin farklı zamanlarda yapılması.

### 24.3. Bu kılavuzun uygulanmasında esas

Gerçek video ve ses, plan metninden daha belirleyicidir. İstemde “tepki var” yazıp çıktıda görünmeyen tepkiyi var sayma. İstemde “10 saniye” yazıp ölçülmemiş dosya süresini kesin kabul etme. En güçlü altı saniyeyi korumak ve çekimi kısaltmadan 10 s'ye tamamlamak (başka deneme, devam üretimi, birleştirme) bu iş akışının doğal parçasıdır.

