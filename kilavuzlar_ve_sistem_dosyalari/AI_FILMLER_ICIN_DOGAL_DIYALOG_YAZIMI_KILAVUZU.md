# AI Filmler İçin Doğal Diyalog Yazımı Kılavuzu

**Odak:** Açıklama okur gibi konuşan karakterleri düzeltmek; her karaktere ayırt edilebilir bir konuşma biçimi vermek  
**Kullanım:** Bilimkurgu, fantastik, korku, aksiyon ve dram; kısa film ve seri bölümleri  
**Üretim bağlamı:** GPT Image ile başlangıç karesi hazırlanan, image-to-video ile hareketlendirilen sahneler; 8–10 saniyelik kaynak kliplerle kurgu  
**Dil:** Türkçe anlatım, özgün İngilizce diyalog örnekleri, Türkçe uyarlamalar ve kopyalanabilir çalışma promptları  
**Hazırlanma:** 21 Ekim 2026

> **HAT KURALI (SÖZLEŞME, sahip kararı 08.10.2026):** Her çekim 10 s üretilir ve filmde 10 s kullanılır; çekim sayısı = hedef süre / 10; çekim kısaltılmaz. Temiz kısım 10 s'ye yetmezse `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası (başka deneme → devam üretimi → iki denemeyi birleştirme → sonuç planı). Bu kılavuzdaki süre önerileri buna göre düzenlendi (21.10.2026). Düzenlenmemiş ilk sürüm: `_ham_kilavuzlar/AI_FILMLER_ICIN_DOGAL_DIYALOG_YAZIMI_KILAVUZU.md`.

Bu kılavuzun hedefi, karakterin söylediği sözün hem o kişiye hem de o ana ait olmasıdır. Karakter bir şeyi anlatırken, saklarken, isterken veya reddederken karşısındaki kişiyi de duymalıdır.

Örnekler bu belge için yazılmış kısa alıştırmalardır; mevcut filmlerinin konularını veya karakterlerini değiştirme talimatı değildir. Süreler kurgu taslağıdır. Ses kaydı ya da video üretilerek doğrulanmış sonuçlar değildir; seçtiğin gerçek sesle ölçülmelidir. Belirli bir video modelinin kesin süre, ses veya dudak eşleme desteği varsayılmaz.

## İçindekiler

1. Doğal diyalogla neyi hedefliyoruz?
2. Açıklama okuyan diyalogu teşhis etme
3. Replikten önce sahnenin ihtiyacını yazma
4. Karakterin konuşma profilini oluşturma
5. Dört karakteri aynı konuda farklı konuşturma
6. Aynı karakterin farklı ilişkilerde değişmesi
7. Kim ne biliyor: bilgi dağılımı
8. Açıklamayı doğal konuşmaya dönüştürme
9. Alt metin ve açık konuşmanın dengesi
10. Dinleme, cevap ve konuşmanın akışı
11. Güç ilişkileri ve duygunun değişmesi
12. Kısa cümle, uzun cümle ve ritim
13. Doğal İngilizce ve Türkçe uyarlama
14. Türlere ve uzaylı karakterlere uyarlama
15. Yapay hissettiren tekrarları temizleme
16. Diyaloğu 8–10 saniyelik kliplere yerleştirme
17. Reaksiyon, sessizlik ve boş klip sonları
18. Konuşmayı planlara bölme
19. Senaryoyu görsel, video ve ses talimatına çevirme
20. Baştan sona çalışılmış altı çekimlik örnek (60 saniye)
21. On iki kısa yeniden yazım örneği
22. Yedi geçişte diyalog revizyonu
23. Doldurulabilir çalışma kartları
24. Kopyalanabilir ana promptlar
25. Alıştırmalar ve değerlendirme
26. Son kontrol, kullanım sırası ve kaynaklar

---

## 1. Doğal diyalogla neyi hedefliyoruz?

Doğal film diyaloğu, karakterin durumuna inanabileceğimiz konuşmadır. Günlük konuşmadaki her duraksamayı, tekrarı ve yarım cümleyi taşımak zorunda değildir. Sade, düzgün kurulmuş bir cümle de doğal olabilir.

Bir repliği şu dört noktadan değerlendir:

- **Kişi:** Bu karakter böyle bir kelime seçer mi?
- **Muhatap:** Bu bilgiyi karşısındaki kişiye söylemesi anlamlı mı?
- **An:** Şu tehlikenin, ilişkinin ve duygunun içinde böyle konuşur mu?
- **Etki:** Sözü, karşısındakinin düşüncesini veya davranışını nasıl etkiliyor?

### 1.1. Sadece kelimeleri düzeltmek yetmeyebilir

~~~text
ZAYIF
ADA: As you already know, our only remaining escape route is the
maintenance passage on the lower level.
~~~

Sorun yalnızca cümlenin uzunluğu değildir. Ada'nın neden bu anda, bunu zaten bilen birine anlattığı belli değildir.

~~~text
DAHA İŞLEVSEL
LEON: Is there another way out?
ADA: Only through the maintenance passage. Lower level.
~~~

İkinci örnekte aynı bilgi, çıkış arayışına cevap olarak söylenir. “Tek kalan yol”, “bakım geçidi” ve “alt kat” korunur. Bilgi konuşmanın ihtiyacına bağlanmıştır.

### 1.2. Üç ayrı iş

**Diyalog yazımı:** Karakter ne söylüyor, neden söylüyor?

**Oyunculuk/ses yönetimi:** Bunu hangi niyetle, hangi vurgu ve hızla söylüyor?

**Kurgu:** Sözü ve karşılığını hangi görüntülerde, ne kadar süreyle izliyoruz?

Kötü yazılmış bir repliği yalnızca “daha duygulu söyle” talimatıyla düzeltmeye çalışma. Önce karakterin ihtiyacını ve cümlenin işlevini netleştir.

### 1.3. Doğal olmak sıradanlaşmak değildir

Hatırlanabilir bir cümle, törensel bir konuşma veya uzun itiraf kullanılabilir. Bunların gücü, karaktere ve sahneye ait olmalarından gelir. Herkesin her konuşmada kusursuz bir slogan üretmesi ise sesleri birbirine benzetir.

## 2. Açıklama okuyan diyalogu teşhis etme

Aşağıdaki belirtilerden birini görmek otomatik olarak repliğin kötü olduğu anlamına gelmez. Birkaçının birlikte görünmesi, yeniden yazım için güçlü bir işarettir.

| Belirti | Neden yapay hissedebilir? | İlk düzeltme |
| --- | --- | --- |
| “Bildiğin gibi…” ile ortak geçmişi anlatmak | Karakter, muhataptan çok seyirciye konuşuyor olabilir. | Bu geçmişin bugünkü karar üzerindeki etkisini yaz. |
| Kendi duygusunu raporlamak | Sözü ve davranışı arasında keşfedilecek alan kalmayabilir. | Duygunun karaktere yaptırdığı isteği bul. |
| Herkesin eşit uzunlukta konuşması | Konuşma sıra beklenen bir sunuma dönüşebilir. | Kimin sözü almak, kimin bitirmek istediğini belirle. |
| Her cevabın yeni bilgi paketi olması | Dinleme yerine sırayla açıklama yapılır. | Cevabı önceki sözdeki bir ayrıntıya bağla. |
| Sürekli isimle hitap etmek | Yakın ilişkide gereksiz tanıtım hissi yaratabilir. | İsmi dikkat, mesafe veya yakınlık gerektiğinde kullan. |
| Aynı olayı görüntü, anlatıcı ve diyalogla yinelemek | İzleyici aynı bilgiyi üç kez alır. | Her anlatım kanalına ayrı görev ver. |
| Tehlike sırasında kusursuz tarih anlatısı | O anki önceliklerle konuşma uyuşmayabilir. | Hemen gerekli eylemi söyle; geçmişi uygun ana taşı. |
| Herkesin aynı benzetmeleri yapması | Yazarın sesi bütün karakterleri kaplar. | Her karakterin dikkat ettiği ayrıntıyı değiştir. |
| Her sahnenin bilmeceyle bitmesi | Açık bilgi sürekli ertelenir. | Gerekli cevabı ver; yeni soruyu sonucundan çıkar. |
| Sürekli “Actually”, “However”, “Therefore” kullanımı | Konuşma bir makale gibi bağlanabilir. | Bağı doğal cevap, düzeltme veya eylemle kur. |
| Her replikte üç farklı duygu talimatı | Oyuncunun oynayacağı esas niyet kaybolur. | Bir baskın niyet ve gerekirse bir değişim seç. |
| Repliğin sonunda herkesin aynı uzunlukta beklemesi | Klip uzunluğu konuşmanın ritmini yönetir. | Kesme noktasını gerçek eylem ve tepkiye göre seç. |

### 2.1. Bir repliğe “açıklama” demeden önce sor

- Dinleyenin bu bilgiyi gerçekten bilmediği bir durum var mı?
- Aynı bilgiyi bilseler bile anlamı veya sonucu konusunda anlaşmazlık var mı?
- Karakter hatırlatarak suçluyor, uyarıyor veya sözünü tutturmaya mı çalışıyor?
- Bu açık anlatımın bir meslek, ilişki veya durum gerekçesi var mı?

Bir eğitim, sorgu, brifing veya acil durum talimatında doğrudan bilgi vermek doğru olabilir. Ama brifingin bile bir hedefi, öncelik sırası ve dinleyicisi vardır.

## 3. Replikten önce sahnenin ihtiyacını yazma

Bir sahneyi önce konuşmasız olarak bir paragrafta anlat:

> Ada çıkışı açmak için yardım istiyor. Leon daha hızlı başka bir yol olduğuna inanıyor. Ada o yolun kapandığını biliyor. Konuşma sonunda Leon kaçmayı tartışmayı bırakıp Ada'ya yardım etmeli.

Bu paragraf, repliklerin ne yapacağını belirler. Cümleleri henüz süslemeye gerek yoktur.

### 3.1. Karakter başına altı alan

~~~text
KARAKTER:
Şu anda karşısındakinden istediği:
İsteğini doğrudan söylemesini zorlaştıran şey:
Kaybetmek istemediği şey:
Kullandığı ilk yöntem:
İlk yöntem işe yaramazsa değiştireceği yaklaşım:
Sahne sonunda yaptığı görünür seçim:
~~~

“Üzgün” bir durumdur. “Karşısındakini gitmekten vazgeçirmeye çalışıyor” oynanabilir bir amaçtır.

### 3.2. Konuşma yöntemi seç

Karakter şu yollardan birine başvurabilir:

- Rica eder.
- İkna etmeye çalışır.
- Pazarlık yapar.
- Sınır koyar.
- Güvence verir.
- Konuyu değiştirir.
- Bir ayrıntıyı doğrulatır.
- Kendi sorumluluğunu azaltmaya çalışır.
- Özür diler.
- Açıkça yardım ister.

Her konuşma kavga olmak zorunda değildir. Aynı hedefe çalışan iki kişinin farklı bilgiye veya önceliğe sahip olması yeterli bir hareket yaratabilir.

### 3.3. Her repliğin büyük olay yaratması gerekmez

“Thanks”, “Here”, “All right” gibi küçük sözler ilişkiyi, iş birliğini veya bir eylemin tamamlandığını duyurabilir. Bütün repliklere aynı anda olay, geçmiş, tema ve sürpriz yüklemek konuşmayı ağırlaştırır.

## 4. Karakterin konuşma profilini oluşturma

Karakter sesini yalnızca kalın/ince ses, aksan veya konuşma hızı olarak düşünme. Aynı ses oyuncusuyla okunduğunda bile kelime seçimleri ve düşünme biçimleri ayrılabilmelidir.

### 4.1. Sekiz karar alanı

| Alan | Doldurulacak soru | İşe yarayan ayrım |
| --- | --- | --- |
| Dikkat | İlk olarak neyi fark eder? | İnsan, risk, eşya, zaman, yetki, tutarsızlık |
| Kesinlik | Bilmediği şeyi nasıl ifade eder? | Açıkça belirsizlik söyler; tahminini gerçek gibi sunar; soruyla yoklar |
| İstek | Bir şeyi nasıl ister? | Doğrudan rica, açıklamalı talep, emir, pazarlık |
| Saklama | Hangi duyguyu veya gerçeği gizler? | Korku, hata, ihtiyaç, kırgınlık, cehalet |
| Cümle yapısı | Düşünceyi nasıl kurar? | Önce sonuç; önce gerekçe; konuşurken düzeltme; soru üzerinden ilerleme |
| Kelime alanı | Hangi sözcükler ona yakın? | Somut gündelik kelimeler, mesleki terimler, ilişkisel ifadeler |
| Baskı | Stres altında ne değişir? | Cümleleri kısalır, fazla ayrıntı verir, nezaketi bırakır, sesi sakinleşir |
| Yakınlık | Güvendiği kişiye neyi farklı söyler? | Yardım ister, şaka yapar, daha az açıklar, özel bir hitap kullanır |

Her alanı aşırı belirginleştirme. İki veya üç güçlü ayrım çoğu kısa film için yeterli bir başlangıçtır.

### 4.2. Meslek ve kimlik tek başına ses değildir

Mühendislerin hepsi teknik, komutanların hepsi kısa, yaşlıların hepsi bilge konuşmaz. Meslek erişebildikleri bilgiyi etkileyebilir; o bilgiyi kullanma biçimini kişilik ve ilişki belirler.

Cinsiyet, ülke veya uzaylı türünden otomatik konuşma kalıbı çıkarma. Karakterin deneyimine ve o anki isteğine dayan.

### 4.3. Bir karaktere yasak kelime listesi vermek

“Bu kişi asla şu sözcüğü söylemez” gibi katı kurallar sınırlı kullanılmalı. Daha işlevsel örnek:

> Ada normalde kesin olmayan bir sonuca “kesin” demez. Panik sırasında bunu söylerse, bu değişimin hikâyede bir nedeni olmalıdır.

Bu, karakteri yaşayan bir kişi olarak korur; bir kelime filtresine dönüştürmez.

## 5. Dört karakteri aynı konuda farklı konuşturma

Aşağıdaki kişiler yalnızca çalışma örneğidir.

| Karakter | Konuşurken önceliği | Tipik tercih | Baskı altında değişimi |
| --- | --- | --- | --- |
| **Ada** | Yanlış bir işlemi önlemek | Somut ayrıntı ve uygulanabilir talep | Açıklamasını kısaltır; yardım istemekte zorlanır. |
| **Leon** | Beklemeyi bitirmek | Hızlı seçenek ve doğrudan soru | Belirsizliği itirazla örter; güvendiğinde destek olur. |
| **Nil** | İnsanların neye ihtiyacı olduğunu anlamak | Kişiye dönük soru, açık sınır | Nazik dolaylılığı bırakıp netleşir. |
| **Oren** | Verilen sözün kapsamını bilmek | Koşulu, sorumluyu ve sonucu açıklığa kavuşturma | Resmî dili azalır; kişisel bedeli söyler. |

### 5.1. Ortak durum: Bir kapı açılmıyor

~~~text
ADA:
The hinge is bent. Hold the door while I check the bottom.

LEON:
Can you open it, or should I find another way?

NIL:
Can the person on the other side hear us?

OREN:
Who told you this door would be open?
~~~

Aynı kapıya bakıyorlar; farklı sorunları görüyorlar. Farkı üretmek için dört ayrı aksan veya dört slogan gerekmiyor.

### 5.2. Ortak ihtiyaç: Karşısındaki kişiyi kalmaya ikna etmek

~~~text
ADA:
I can't keep this level on my own. Stay until I get the bolt in.

LEON:
Give me a minute. If it doesn't work, we go.

NIL:
Stay with me. I don't want to wait here alone.

OREN:
If you leave now, who answers for the people still inside?
~~~

Bunlar karakterlere sonsuza dek yapıştırılacak kalıplar değildir. Ada da açık bir duygusal yardım isteyebilir; böyle bir an önceki davranışıyla anlam kazanır.

### 5.3. İsimleri kapatma denemesi

Karakter adlarını kaldırıp replikleri oku. Ayırt etmek mümkün değilse şu üç alandan birini güçlendir:

1. Dikkat ettiği şey.
2. Karşısındakinden istediği davranış.
3. İsteğini ifade etme biçimi.

John August ve Craig Mazin de karakterlerin repliklerinin birbirine aktarılabilir olup olmadığını, ses ayrımı için yararlı bir kontrol olarak öneriyor.[^voice]

Her “Yes” repliğinden konuşanı tanımak zorunda değilsin. Denemeyi birkaç repliklik bir bölüm üzerinde yap.

## 6. Aynı karakterin farklı ilişkilerde değişmesi

Ses tutarlılığı, karakterin herkese aynı konuşması demek değildir.

Ada'nın ortak bilgisi: İşin güvenli biçimde bitmesi için daha fazla zamana ihtiyacı var.

~~~text
YÖNETİCİSİNE:
I need another minute. The lower bracket isn't secure.

YAKIN ARKADAŞINA:
Hold on. I haven't fixed the bottom yet.

ONA GÜVENMEYEN BİRİNE:
You can check it yourself. That bracket is still loose.

KENDİSİNDEN YARDIM BEKLEYEN BİRİNE:
Stay where you are. I'm fixing it.
~~~

Bilgi korunur; ilişki, kelime seçimini ve açıklama miktarını değiştirir.

### 6.1. Özel ve kamusal konuşma

Bir karakter kalabalık önünde hatasını kabul etmek istemeyebilir; yalnız kaldığında daha açık konuşabilir. Bu değişimi “iki farklı karakter sesi” diye düzeltme.

~~~text
KALABALIK ÖNÜNDE:
We're checking the route.

YALNIZKEN:
I sent them the wrong way.
~~~

### 6.2. Karakter gelişimini konuşmada göster

Başlangıçta yardım isteyemeyen biri, finalde “I need you” diyebilir. Cümlenin etkisi, önceki davranışlardan gelir.

Her gelişimi bir konuşmayla açıklama. “Artık insanlara güvenmeyi öğrendim” yerine, gerçekten güvenerek bir işi devretmesi ve buna uygun kısa bir söz yeterli olabilir.

## 7. Kim ne biliyor: bilgi dağılımı

Açıklama sorununu çözmenin en güçlü yollarından biri, bilginin kime ait olduğunu yazmaktır.

| Bilgi | Konuşan biliyor mu? | Dinleyen biliyor mu? | İzleyici biliyor mu? | Şimdi gerekli mi? |
| --- | --- | --- | --- | --- |
| Merdivenlerin su altında kaldığı | Ada biliyor. | Leon bilmiyor. | Henüz bilmiyor. | Evet; Leon o yolu öneriyor. |
| Kapının yıllar önce yenilendiği | İkisi de biliyor. | Evet. | Bilmiyor. | Açma yöntemini değiştirmiyorsa hayır. |
| Ada'nın eli titriyor | Ada hissediyor. | Leon henüz fark etmedi. | Yakın planda görebilir. | İlişkinin değişimi için yararlı olabilir. |
| Leon'un geçmişte birini beklediği | Leon biliyor. | Ada bilmiyor. | Bilmiyor. | Bu sahnede zorunlu değil. |

### 7.1. Bilgiyi karakterin ihtiyacına bağla

Leon “Merdivenleri kullanalım” dediğinde Ada'nın su bilgisini söylemek için doğal bir nedeni vardır.

Ada'nın merdiven tarihini kendiliğinden anlatmasının ise aynı gerekliliği yoktur.

### 7.2. Görüntüdeki bilgiyi sözle tekrar etme

Görüntü kapının kapalı olduğunu açıkça gösteriyorsa “The door is closed” gereksiz olabilir. Ama biri açık olduğunu iddia etmişse aynı cümle suçlama veya düzeltme işlevi kazanır.

Tekrarın değeri bağlama bağlıdır. Tek başına “görünen şeyi söylemek yasaktır” kuralı koyma.

### 7.3. Açıklamayı silerken anlamı koru

Metinden teknik sözcükleri çıkardıktan sonra şu soruları kontrol et:

- Hangi nesne?
- Hangi kişi?
- Hangi yön?
- Hangi işlem?
- Başarısız olursa ne olacak?

Hepsi “it”, “that” ve “there” olmuşsa izleyici yanlış şeyi takip edebilir. İlk kullanımda nesneyi adlandır; ortak referans kurulduktan sonra zamir kullan.

## 8. Açıklamayı doğal konuşmaya dönüştürme

Aşağıdaki beş yöntemden duruma uyanı seç. Hepsini aynı sahneye koymak gerekmez.

### 8.1. Yanlış planı düzelt

~~~text
ZAYIF
ADA: The east corridor is no longer usable because the ceiling collapsed.

DÜZELTİLMİŞ
LEON: East corridor. It's closer.
ADA: The ceiling came down. We have to go around.
~~~

Bilgi bir kararı değiştirir. Leon bilmediği bir şeyi öğrenir.

### 8.2. Bilgiyi talebin gerekçesi yap

~~~text
ZAYIF
ADA: This panel is sensitive to movement and could detach if disturbed.

DÜZELTİLMİŞ
ADA: Keep the panel steady. It could come loose.
~~~

İkinci replik hâlâ açıklamadır. Doğal olmasını sağlayan şey, o anki eyleme hizmet etmesidir.

### 8.3. Geçmişi bugünkü hesaplaşmaya bağla

~~~text
ZAYIF
LEON: Three years ago, during the station evacuation, you promised
to wait for me but left before I arrived.

DÜZELTİLMİŞ
LEON: You said you'd wait.
ADA: I did.
LEON: You left before I got there.
~~~

“Üç yıl önce”, “istasyon” ve “tahliye” ayrıntıları çıkarıldı. Hikâyeyi anlamak için gerekiyorsa görüntüde, daha önceki sahnede veya uygun bir devam repliğinde kurulmalıdır. Daha doğal yazmak, önemli olay bilgisini kaybetme izni vermez.

### 8.4. Bilgiyi sorunun gereken kadarına indir

~~~text
LEON:
Will it hold both of us?

ADA:
One at a time.
~~~

Bu, yük kapasitesi tartışmasının yeterli olduğu bir sahnede çalışır. İzleyicinin neden böyle bir sınır olduğunu bilmesi gerekiyorsa kısa bir kanıt ekle: bağlantının eğilmesi, gevşek bir bağlantı noktası veya bunun söylenmesi.

### 8.5. Açık bilgiyi açıkça ver

~~~text
NIL:
The water's rising. We need to leave this room.
~~~

Acil bir durumda bu cümle yeterince doğaldır. Alt metin veya espri eklemek için mesajı bulandırma.

### 8.6. Dönüştürme sırası

1. Replikteki bütün bilgileri ayrı maddelere ayır.
2. Şimdi gereken bilgiyi işaretle.
3. Konuşanın bunu söyleme nedenini yaz.
4. Dinleyenin hangi kısmı bilmediğini belirle.
5. Bir gerçek soru, yanlış varsayım veya talep kur.
6. Cevabı bu ihtiyaca göre yaz.
7. Çıkardığın bilgilerin sonraki sahneleri bozmadığını kontrol et.

John August'ın yaklaşımında da bilginin seyirciye aktarılması ile karakterin karşısındakine konuşma nedeni birlikte düşünülür. Buradaki kartlar ve örnekler bu ayrımı üretimde kontrol etmek için hazırlanmıştır.[^dialogue]



## 9. Alt metin ve açık konuşmanın dengesi

Alt metin, söylenen cümlenin ilişkide taşıdığı ikinci anlamdır. Karakterin gizli bir mesajı şifrelemesi gerekmez. Bazen karşısındakini incitmemek, yardım istediğini belli etmemek veya cevabı duymaktan korkmak yeterlidir.

| Söylenen | Görünür bağlam | Karakterin ilişki içinde istediği |
|---|---|---|
| “Do you want me to leave the light on?” | Nil, yalnız kalmak istemeyen Ada'nın odasından çıkıyor. | Yakınlık teklif etmek; Ada'yı itirafa zorlamamak. |
| “You can take the other seat.” | Leon, tartıştığı kişinin yanındaki yeri boş bırakmış. | Uzak durma hakkı tanıyarak barışmaya alan açmak. |
| “I kept your tools.” | Ada, uzun süre dönmeyen arkadaşının çantasını uzatıyor. | Dönmesini beklediğini söylemek. |
| “Call me when you get there.” | Oren, güvenmediği bir güzergâha giden yakınıyla konuşuyor. | Kaygısını denetim talebi gibi göstermeden bağlantıyı korumak. |

Bu cümlelerin anlamını sahne oluşturur. Aynı cümle başka bir bağlamda yalnızca ışık, koltuk, alet veya telefon hakkındadır. Yazarın açıklama notunda “burada aslında seni seviyorum diyor” yazması, seyircinin bunu göreceği anlamına gelmez. Önceki davranış, oyunculuk ve karşı tarafın cevabı ikinci anlamı taşımalıdır.

### 9.1. İki katmanı birlikte yaz

~~~text
GÖRÜNÜR KONU: Leon eski odasının anahtarını geri veriyor.
ADA'NIN İSTEĞİ: Leon'un bir daha gelmeyeceğini öğrenmek.
ADA'NIN SÖYLEMEKTEN KAÇINDIĞI: Burada kalmanı istiyorum.

LEON: I found the spare key.
ADA: You can keep it.
LEON: I won't need it.
ADA: Right.
~~~

Burada Ada'nın son sözü kısa olduğu için değil, beklentisi değiştiği için anlam taşır. Son “Right”ın ardından anahtarı alması veya elini bir an uzatmaması sahneyi tamamlayabilir. Her ikisini ve bir açıklama repliğini birden eklemek gerekmez.

### 9.2. Ne zaman doğrudan konuşmalı?

- Yanlış anlaşılma birinin o an ne yapacağını belirsiz bırakıyorsa.
- Karakter sonunda sakladığı şeyi söylemeye karar veriyorsa.
- İlişki, ima kurmaya ihtiyaç duymayacak kadar güvenliyse.
- Bir talimat, sınır veya özür açık olmalıysa.

“I don't want you to go” cümlesi doğal olabilir. Onu mutlaka “The room gets cold when you're away” gibi bir mecaza çevirmek gerekmez. Karakterin duygusunu söylemesi sorun değildir; sahnenin zaten anlattığı duyguyu yalnızca seyirci için tekrar raporlaması sorun olabilir.

## 10. Dinleme, cevap ve konuşmanın akışı

Diyaloğu iki kişinin sırayla kendi metnini okumasından kurtaran şey, önceki sözün sonraki sözü değiştirmesidir.

### 10.1. Cevabın bağını kontrol et

~~~text
KOPUK
NIL: Did you tell her we were leaving?
LEON: We have to reach the crossing before dark.
NIL: The road is dangerous.

BAĞLI
NIL: Did you tell her we were leaving?
LEON: I left a message.
NIL: That's not what I asked.
LEON: No. I didn't speak to her.
~~~

İkinci konuşmada yeni bir mekanik bilgi eklenmez; Nil, cevaptaki kaçamağı fark eder. Leon da buna cevap verir. Bu alışveriş, ilişkide neyin zor olduğunu gösterir.

Her dolaylı cevap kopuk değildir. “We have to reach the crossing before dark” bilinçli bir kaçışsa Nil bunu fark edebilir: “You haven't told her.” Kaçınmayı yazmakla soruyu unutmak farklı sonuçlar doğurur.

### 10.2. Doğal cevap çeşitleri

| Cevap hareketi | Örnek | Kullanım |
|---|---|---|
| Düz cevap | “Yes. I spoke to her.” | Hız ve açıklık gerektiğinde. |
| Daraltma | “I spoke to her assistant.” | İlk cevabın kapsamını değiştirirken. |
| Düzeltme | “Yesterday. Not this morning.” | Önemli bir varsayımı düzeltirken. |
| Karşı soru | “What did she tell you?” | Cevaptan önce karşı tarafın bilgisini ölçerken. |
| Sınır koyma | “I'll explain when we're alone.” | Konuşmanın koşulunu değiştirirken. |
| Fikri değiştirme | “Wait. Take mine instead.” | Yeni bir şeyi fark edip karar değiştirirken. |

Bütün repliklere karşı soru veya kaçamak koyarsan kimse işbirliği yapmıyormuş gibi görünür. Birçok konuşmanın temeli gerçekten cevap vermektir.

### 10.3. Duraksama, tekrar ve söz kesme

Bir tekrarın anlamı değişebilir:

~~~text
ADA: It's open.
LEON: Open?
ADA: Someone got here first.
~~~

Leon duyduğu kelimenin sonucunu kavramaya çalışır. Buna karşılık her cümlenin başına “Well”, “Look”, “Listen”, “Um” eklemek kendiliğinden doğallık sağlamaz.

Söz kesme, diğer kişinin nereye gittiğini anladığında veya bekleyemediğinde çalışır. Her konuşmayı üst üste bindirmek anlaşılabilirliği zayıflatabilir. Kullandığın video aracının birden fazla sesi nasıl işlediği doğrulanmadıysa, örtüşmeyi ayrı ses kayıtları ve kurgu üzerinden planla.

Yeniden başlayan cümleleri amaçla kullan:

~~~text
OREN:
I thought you were— I didn't know you were still here.
~~~

Bu yarım kalış bir düzeltmedir. Bir sonraki cümlede tekrar kullanman gerekmez.

## 11. Güç ilişkileri ve duygunun değişmesi

Konuşmadaki güç yalnızca rütbeden gelmez. Bir kişi cevabı biliyor, diğeri bekliyor olabilir. Biri gitmekte özgürken diğeri ondan yardım istemek zorunda kalabilir.

Şunları izle:

- Konuyu kim açıyor?
- Kim soruya cevap vermeyebiliyor?
- Kimin susması diğerini konuşmaya zorluyor?
- Kim sonradan talepte bulunmak zorunda kalıyor?
- Konuşmanın sonunda bu düzen değişiyor mu?

### 11.1. Gücü ses yükseltmeden değiştir

~~~text
OREN: I need the report by morning.
NIL: Then I need the original recordings.
OREN: You have the summary.
NIL: I can't sign a summary I didn't prepare.
OREN: I'll have them sent over.
~~~

Nil bağırmaz. Yapacağı işin koşulunu belirler. Oren'in son cümlesi bu koşulu kabul ettiğini gösterir. Böyle bir değişim, iki kişinin birbirine daha sert hakaret etmesinden daha belirgin olabilir.

### 11.2. Duyguyu oynanabilir bir niyete çevir

| Genel duygu notu | Daha kullanışlı niyet | Görülebilecek sonuç |
|---|---|---|
| “Korkmuş” | Korktuğunu belli etmeden birini yanında tutmaya çalışır. | Yeni bir küçük görev teklif eder. |
| “Öfkeli” | Diğer kişinin konuyu değiştirmesine izin vermez. | Aynı soruya geri döner. |
| “Üzgün” | Karşı tarafı suçlamadan bir açıklama ister. | Cümleyi yumuşatır ama sorudan vazgeçmez. |
| “Suçlu” | Olayı anlatmadan önce zarar gören şeyi düzeltmeye çalışır. | Yardım teklif eder; teklifi geri çevrilince konuşur. |
| “Rahatlamış” | Kontrol etmeyi bırakıp işin bir kısmını devreder. | İlk kez açıkça yardım ister. |

Bunlar olası tercihlerdir; bütün korkan insanlar aynı davranmaz. Duyguyu yalnızca tek bir belirtiye bağlama: öfke her zaman bağırmak, korku her zaman kekelemek değildir.

### 11.3. Değişimi adım adım göster

Bir karakter düşmanca başlayıp tek replikte içten bir dosta dönüşüyorsa aradaki neden eksik olabilir. Küçük bir bilgi, fark edilen çaba veya kabul edilen hata konuşma biçimini değiştirsin.

Örneğin Leon önce acele ettirir. Ada'nın beceriksiz olmadığı, elinin yaralı olduğu anlaşılınca tonu değişir. “You're doing fine” o zaman genel bir teselli değil, gördüğü şeye verilmiş bir cevaptır. Görüntüde yaralanma kurulmuyorsa senaryoda varmış gibi davranma; yorgunluk, titreme veya başka bir gözlenebilir neden seç.

## 12. Kısa cümle, uzun cümle ve ritim

Doğal diyalog bütün cümleleri kısa yapmak değildir. Karakter bir şeyi ilk kez dürüstçe söyleyebilir, düşüncesini konuşurken bulabilir veya yanlış anlaşılmamak için açıklamasını uzatabilir.

~~~text
NIL:
I can stay tonight, but I need you to tell me if you want company.
I can't keep guessing whether I'm helping or getting in your way.
~~~

Bu replik uzundur; aynı ihtiyacı birkaç ayrı açıdan kurar. Karakterin ilişki sorununa uygunsa işlevlidir. Onu “Want me here or not?” cümlesine indirgemek, Nil'in özenini ve kırılganlığını kaybettirebilir.

### 12.1. Ritim için üç soru

1. Bu kişi cevabı zaten biliyor mu, konuşurken mi buluyor?
2. Karşı taraf sabırla mı dinliyor, araya girmek mi istiyor?
3. Cümlenin sonunda başlayan yere göre yeni bir anlam var mı?

Uzun cümle aynı bilgiyi tekrarlıyorsa kısalt. Gerekli bir düşünce ilerliyorsa alan aç veya uygun bir yerden başka plana geçir.

### 12.2. Nazik sözleri otomatik silme

“Please”, “if you can”, “I think” ve “sorry” bazen dolgu, bazen karakterin ilişki kurma biçimidir.

- “Move.”: Yetki, yakınlık veya aciliyet taşıyabilir.
- “Could you move a little?”: Ortak alanı nazikçe müzakere eder.
- “Please. I need to get through.”: Bir engeli yardım isteyerek aşmaya çalışır.

Aynı eylemi istemelerine rağmen aynı karakter anını anlatmazlar. Revizyonda sadece kelime sayısını değil, ilişkiyi de koru.

### 12.3. Sahnenin sesini tekdüzeleştirme

Arka arkaya sekiz kısa emir yazdıysan araya sırf çeşitlilik için bir monolog koyma. Önce durumun değişip değişmediğine bak. Herkes bilgi veriyorsa birinin o bilgiye ne yaptığı eksik olabilir. Herkes şakalaşıyorsa şakanın işe yaramadığı bir an sahneye ağırlık kazandırabilir.

## 13. Doğal İngilizce ve Türkçe uyarlama

İngilizce yayınlayacağın filmde hedef, Türkçe cümleyi aynı sırayla İngilizceye taşımak değildir. Anlamı, niyeti, ilişkinin mesafesini ve gereken bilgiyi koruyarak yeniden söylemektir.

### 13.1. İşlevi çevir

| Türkçedeki niyet | İngilizce seçenek | Dikkat |
|---|---|---|
| “Seni burada bırakıp gidemem.” | “I can't leave you here.” | Kısa ve doğrudan bir karşılık yeterli. |
| “Bana bir şey olursa…” | “If something happens to me…” | Devamı ve bağlamı cümleyi taşımalı. |
| “Kendini suçlama.” | “This wasn't your fault.” | Sorumluluğu reddeder. “Don't blame yourself” ise kişinin tepkisine seslenir. |
| “Sen bilirsin.” | “It's your call.” / “Do what you want.” | İlki karar yetkisi verir; ikincisi bağlama göre kırgın veya sert duyulabilir. |
| “Yanlış anladın.” | “That's not what I meant.” | Kendi anlatımını düzeltir; “You misunderstood” karşı tarafı daha açık sorumlu tutabilir. |
| “Bir dakika, öyle demedim.” | “Wait. I didn't say that.” | Konuşmanın akışına müdahale eder. |

Bu seçenekler evrensel eşanlamlılar değildir. Önce sahnedeki işlevi seç, sonra karşılığı seç.

### 13.2. İngilizce doğallık kontrolü

- Karakterin üslubuna uygunsa “I'm”, “don't”, “we've” gibi kısaltmalar kullan.
- Teknik terimden önce dinleyenin neyi bilmesi gerektiğini belirle.
- Birden fazla nesne varken art arda “it” ve “that” kullanıp referansı kaybetme.
- Her karakteri aynı Amerikan argosuyla konuşturma.
- “Daha sinematik” diye sıradan bir isteği mecaza çevirme.
- Basit İngilizceyi eksik veya bozuk dilbilgisiyle karıştırma.
- Aksanı kişilik yerine kullanma; kelime seçimi, dikkat ve niyet önce gelsin.

~~~text
AŞIRI YAZILI
I am unable to provide you with an answer at this particular moment.

DURUMA UYGUN SEÇENEKLER
I don't know yet.
I can't answer that here.
Give me a minute.
~~~

Bu üç kısa seçenek aynı şeyi söylemez: bilgi eksikliği, konuşma ortamı ve zaman talebi farklıdır. Hangisinin doğru olduğuna hikâye karar verir.

### 13.3. Türkçe sürümü ayrıca dinle

İngilizce repliğin kelime sayısı Türkçe seslendirme süresini belirlemez. Ekler, sözcük uzunluğu, vurgu ve oyuncunun nefesi süreyi değiştirir. Türkçe uyarlamayı ayrı bir oyunculuk metni gibi oku.

Karakter adının veya kurmaca bir terimin telaffuzu gerekiyorsa bunu ayrı ses notuna koy:

~~~text
SPOKEN LINE:
Oren knows the route.

PRONUNCIATION NOTE — NOT SPOKEN:
Oren: use the pronunciation established in the character reference.
~~~

Gerçek telaffuz henüz seçilmediyse uydurup bütün üretime dağıtma; projede bir kez belirle ve kaydet.

## 14. Türlere ve uzaylı karakterlere uyarlama

Tür değiştiğinde doğallığın ölçüsü değişmez: bu kişi, bu kişiye, bu koşulda neden böyle konuşuyor?

| Tür / durum | Diyalog için yararlı odak | Sık sorun |
|---|---|---|
| Bilimkurgu | Teknolojinin mevcut karar üzerindeki sonucu | Her repliğin kullanım kılavuzuna dönüşmesi |
| Fantastik | Toplumun hitapları, yükümlülükleri ve değerleri | Bütün karakterlerin aynı ağır üslupla konuşması |
| Korku | Karakterin gerçekten duyduğu, gördüğü ve bildiği | Seyirciden önce tehdidin bütün kurallarını açıklamak |
| Aksiyon | Açık hedef, engel ve işbirliği | Her hareketin sözle tekrar edilmesi |
| Dram | Yakınlık, kaçınma, ihtiyaç ve yanlış anlaşılma | Duyguların sürekli isimlendirilmesi |
| Komedi | Karakterin ciddi ihtiyacı ile durum arasındaki uyumsuzluk | Her karakterin aynı şakacı yazara dönüşmesi |

### 14.1. Uzaylıyı anlaşılmaz konuşarak farklılaştırma

Bir uzaylının konuşması düzgün, gündelik ve açık olabilir. Farklılık, hangi bilgiyi önce sorduğunda ortaya çıkabilir.

Özgün bir kurmaca tercih yapalım: Bir topluluk, bir yere girişte mekânın sahibinden çok içeridekinin davetini önemser.

~~~text
LEON: The building's empty. We can go in.
SERA: Did anyone invite us?
LEON: There's nobody to ask.
SERA: Then we should leave a message before we enter.
~~~

Sera'nın değerini davranışın içinden anlarız. Hemen ardından kendi türünün bin yıllık geleneklerini açıklaması gerekmez. Ancak filmde bu gelenek bir kararın sonucunu belirleyecekse yeterli açıklıkla kurulmalıdır.

Bu, bütün uzaylılar için önerilen bir özellik değildir. Aynı türden başka biri geleneği esnetebilir, dalga geçebilir veya daha sıkı uygulayabilir. Tür kimliği ile kişilik aynı şey değildir.

### 14.2. Teknik bilgi için önce sonuç

~~~text
YOĞUN AÇIKLAMA
The propulsion regulator can no longer maintain the required output.

KARAR ODAKLI
We can keep the engines on, or we can keep the lights on.
Not both.
~~~

İkinci sürüm ancak senin kurmaca sisteminde böyle bir tercih gerçekten varsa doğrudur. Doğal replik uğruna teknik kural icat edip olay örgüsünü değiştirme. Gereken gerçek bilgi “motor gücü düşüyor ama ışıklar bağımsız” ise bu yeniden yazım kullanılamaz.

## 15. Yapay hissettiren tekrarları temizleme

Bir kalıp tek başına yasak değildir. Aynı filmde herkesin aynı kalıba tekrar tekrar dönmesi dikkat çeker.

| Kontrol edilecek örüntü | Ne zaman sorun olur? | Revizyon sorusu |
|---|---|---|
| Her replikte karşıtlık: “It isn't X. It's Y.” | Bütün karakterler aynı retorikle konuşuyorsa. | Karakter doğrudan ne istiyor? |
| “You don't understand.” | Ardından anlamayı sağlayacak hiçbir şey gelmiyorsa. | Hangi yanlış varsayımı düzeltebilir? |
| “There's no time.” | Karar vermeyi veya bilgi aktarmayı sürekli erteliyorsa. | Şimdi yapılacak tek işi söyleyebilir mi? |
| “It's worse than you think.” | Gerilim sadece bilgi saklamaya dayanıyorsa. | Seyirciye hangi somut sonuç gösterilebilir? |
| Sürekli kader, karanlık, umut benzetmeleri | Konuşmanın bağlamı bu dili taşımıyorsa. | Bu kişinin gündelik sözcükleri neler? |
| Her cevabın espri olması | Korku, kayıp veya gerçek dinleme için yer kalmıyorsa. | Bu şaka kimin savunması, kimin rahatsızlığı? |
| Birbirine sık sık isimle seslenme | Hitap hiçbir yön değiştirmiyorsa. | Kimin konuştuğu zaten açık mı? |
| Bütün cümlelerin aynı uzunlukta olması | Konuşma hazırlanmış karşılıklı sunuma benziyorsa. | Kimin düşünmeye, kimin hızlı cevaba ihtiyacı var? |
| Sürekli “…”, “uh”, “well” ekleme | Dolgu bir niyet veya düşünce değişimi taşımıyorsa. | Buradaki duraksama neyi değiştiriyor? |

### 15.1. Doğallık için küfür ekleme zorunluluğu yok

Argo, küfür, ağız özelliği veya bozuk cümle ancak karakterin koşullarına hizmet ediyorsa kullanışlıdır. Birbirinden farklı dört karakter aynı sert argo paketini kullanıyorsa sesleri yine birbirine yaklaşır.

### 15.2. Yazarın sevdiği repliği sahneye karşı kontrol et

Çok güzel bir cümle yazmış olabilirsin. Şunları sor:

- Bu kişi normalde böyle bir benzetme kurar mı?
- Şu an bunu düşünecek zamanı ve dikkati var mı?
- Karşısındaki bu cümleye gerçekten cevap veriyor mu?
- Repliği çıkarınca yalnızca bir alıntı mı kayboluyor, sahnenin bir hareketi mi?

Replik karaktere aitse koru. Yalnızca yazarın kendini göstermesine yarıyorsa başka bir sahneye taşı veya çıkar.


## 16. Diyaloğu 8–10 saniyelik kliplere yerleştirme

Üretim süresi ile filmde kullandığın süreyi ayrı kaydet.

| Süre | Anlamı |
|---|---|
| Kaynak klip süresi | Araçtan çıkan toplam video süresi. |
| Konuşma süresi | Repliğin gerçek ses kaydında sürdüğü zaman. |
| Duraklama ve tepki | Düşünme, dinleme veya bir anlam değişiminin süresi. |
| Eylem süresi | Replik dışında gerçekleşmesi gereken görünür iş. |
| Kurguda kullanılan süre | Film zaman çizelgesine koyduğun bölüm. Hatta her çekim için 10 s, klibin temiz kısmından seçilir. |

Konuşma ile eylem aynı anda gerçekleşebilir. Bir karakter cümlesini söylerken kapıya yürüyorsa bu iki süreyi otomatik olarak birbirine ekleme. Ardışık mı, örtüşen mi olduklarını belirt.

### 16.1. Kelime hesabı yalnızca ilk tahmindir

Örnek hesap için dakikada **150 kelime** seçelim. Bu, burada kullanılan varsayımsal bir planlama hızıdır; bütün oyuncular, diller veya sahneler için önerilen standart değildir.

~~~text
150 kelime / 60 saniye = saniyede 2,5 kelime

18 kelimelik replik / 2,5 = yaklaşık 7,2 saniye konuşma
Ardından 1 saniye duraklama + 1 saniye tepki = yaklaşık 9,2 saniye
~~~

Bu örnek 10 saniyelik bir kaynağa kâğıt üzerinde sığar. Ses kaydı 8,8 saniye çıkarsa aynı plan sığmayabilir.

~~~text
17 kelimelik replik / 2,5 = yaklaşık 6,8 saniye konuşma
Ardından 0,7 saniye duraklama + 1 saniye tepki = yaklaşık 8,5 saniye
~~~

Bu plan 8 saniyelik bir kaynak için uzundur. Çözüm sesi otomatik hızlandırmak değildir. Repliği anlamı koruyarak kısaltabilir, tepkiyi sonraki çekime taşıyabilir veya konuşmayı J/L ile sonraki çekimin üzerinde sürdürebilirsin.

| Bu varsayımsal hızla ayrılan konuşma alanı | Yaklaşık kelime karşılığı |
|---|---:|
| 3 saniye | 7–8 kelime |
| 4 saniye | 10 kelime |
| 5 saniye | 12–13 kelime |
| 6 saniye | 15 kelime |

Bu tabloya bakıp her 10 saniyelik çekime 15 kelime yazma. Önce sahnede gereken konuşma alanını belirle; çekimin kalan saniyeleri tepki, sonuç ya da sonraki adım vuruşudur. Özel ad, zor telaffuz, fısıltı, nefes ve duygusal değişim hesabı etkiler. Türkçe ve İngilizceyi ayrı ölç.

### 16.2. Gerçek süreyi nasıl kontrol edeceksin?

1. Repliği hedeflenen duyguyla sesli oku veya taslak seslendirmeyi üret.
2. Konuşmanın ilk duyulan sesinden son sesine kadar ölç.
3. Gerekli sessizliği ve ardışık eylemi ayrıca işaretle.
4. Video ve sesin birlikte ilerleyebildiği kısımları belirle.
5. Klip sınırında kelime, nefes veya anlam kesiliyor mu dinle.
6. Sonra görsel üretim planını kesinleştir.

Buradaki örnekler için gerçek seslendirme üretilmedi; belirtilen sahne süreleri kurgu taslağıdır.

### 16.3. Dört dakikalık filmin hesabını koru

24 çekim × 10 saniye = 240 saniye. Hatta bu sabittir: her çekim 10 s üretilir ve 10 s kullanılır.

Repliğin doğal süresi 6 s ise çekim 6 s'ye inmez. Kalan 4 s'yi boş beklemeyle ya da yavaş konuşmayla doldurma. Repliğin yarattığı sonucu, dinleyenin tepkisini ya da sonraki adımı vuruş olarak yaz:

~~~text
0-6 s: replik (konuşan, küçük eşlik eden hareketle)
6-10 s: dinleyenin kararı görünür olur (eli geri çekilir, kapıya yönelir)
~~~

Konuşma bütün sahnede sürekli kısa kalıyorsa sahnenin eksik kalan olayına, coğrafyasına, seçimine ya da ilişki gelişimine bak; iki konuşma tek çekimde toplanabilir ve açılan çekim o eksiğe verilir (F3).

## 17. Reaksiyon, sessizlik ve boş klip sonları

Bir replik altıncı saniyede bittiğinde kalan dört saniyenin tek doğru kullanımı yoktur.

| Sonraki ihtiyaç | Uygun tercih |
|---|---|
| Cevabı hemen duymak | Cevap bir sonraki çekimdedir; bu çekimin son vuruşunda dinleyen cevaba hazırlanır ya da cevabın ilk sözü J-cut ile erken başlar. |
| Söylenenin etkisini görmek | Dinleyenin kararını veya değişen davranışını göster. |
| Talebin uygulanmasını görmek | Karakterin istenen işe başladığını göster. |
| Bir sonucun ortaya çıkmasını beklemek | Kapının açılması, cevabın gelmesi gibi kurulmuş sonucu izle. |
| Yeni bir şey olmuyor | Vuruş planını yeniden yaz: sonraki adımı ekle ya da iki konuşmayı tek çekimde topla (F3). Çekim kısalmaz. |

### 17.1. Dolu sessizlik nasıl anlaşılır?

~~~text
ADA: You can keep the key.
~~~

Ardından Leon'un anahtarı masaya bırakması yeni bir bilgi verir: teklifi kabul etmiyor. Anahtara bakıp hiçbir değişim olmadan dört saniye beklemesi boş vuruştur; bırakma hareketi o dört saniyeye yazılır.

Sessizliğin değeri uzunluğunda değil, seyircinin o sırada neyi gözlediğindedir. Her saniyeye ayrı hareket yazmak da gerekmez. Bir kişinin cevap vermemeyi seçmesi, bağlam yeterince kurulmuşsa tek başına anlamlıdır.

### 17.2. Video talimatına yalnızca “emotional reaction” yazma

Daha uygulanabilir bir talimat:

~~~text
After the line, Leon stops reaching for the key.
He leaves his hand on the table and waits for Ada to answer.
~~~

Burada davranış belirli, sonucu okunabilir. Aynı dört saniyeye gözyaşı, yumruk sıkma, geriye dönme, gülümseme ve kapıyı çarpma yükleme.

### 17.3. Her klibi aynı yapıya sokma

Bütün çekimleri “ilk iki saniye bakış, sonraki dört saniye replik, son dört saniye tepki” olarak tasarlamak mekanik bir ritim yaratabilir. Vuruş sayısı ve sınırları çekimden çekime değişir.

Bazı planlar konuşmanın ortasında başlar. Bazılarında önce hareket, sonra replik vardır. Bir cevap, önceki planın sonunda ses olarak başlayabilir. Seçimi konuşmanın akışı belirlesin.

## 18. Konuşmayı planlara bölme

Önce sahneyi kesintisiz yaz. Sonra kimin neyi duyduğunu ve neyin görülmesi gerektiğini belirleyerek planlara ayır.

### 18.1. Planın merkezi her zaman konuşan kişi değildir

| Görüntü tercihi | Diyalog açısından işlevi |
|---|---|
| Konuşanın yakın planı | Söylemenin bedelini, tereddüdü veya kararı gösterir. |
| Dinleyenin yakın planı | Bilginin etkisini gösterir. |
| İkili plan | İki kişinin mesafesini ve ortak işini anlaşılır tutar. |
| El, nesne veya sonuç detayı | Sözün hangi somut işe bağlı olduğunu gösterir. |
| Konuşan kadraj dışında | Görünmesi daha önemli olan tepkiye veya eyleme alan açar. |

Yalnızca ağız hareketini göstermeye çalışmak, dinleyeni filmden silebilir. Tersine, sürekli nesne detayı kullanmak da karakterin duygusal anından kaçışa dönüşebilir.

### 18.2. Bir konuşmayı iki kaynak klibe bölerken

Doğal bir düşünce veya eylem dönümünü bul:

~~~text
NIL:
I can stay tonight, but I need you to tell me if you want company.

[Karşı tarafın tepkisi veya uygun devam planı]

NIL:
I can't keep guessing whether I'm helping or getting in your way.
~~~

İki parçayı ayrı ses kayıtları olarak üretirsen ton, hız, ortam ve nefes devamını kontrol et. Kesintisiz bir ses kaydını iki görüntünün üzerinde kullanmak da bir seçenektir; kullanılan araçların ve kurgunun buna uygun olması gerekir.

Yalnızca kaynak süre sınırına uymak için özne ile yüklemi, olumsuzluk ile anlamı veya özel adın iki hecesini ayırma.

### 18.3. Görsel devamlılık konuşmayı da etkiler

- Karakter kime baktığını koruyor mu?
- Konuşma sırasında kullandığı el sonraki planda başka işte mi?
- Bir önceki planda eline aldığı nesne hâlâ onda mı?
- Son sözü duymadan cevap veriyor gibi mi görünüyor?
- Aynı soru iki kaynak klibin başında tekrar mı edilmiş?

Tek görünür konuşmacı, bazı çekimleri planlamayı kolaylaştırabilir. Bunu bütün video modelleri için zorunlu teknik kural gibi kullanma. Önce kullandığın aracın gerçek çıktısını değerlendir.

## 19. Senaryoyu görsel, video ve ses talimatına çevirme

Dört ayrı bilgi katmanı tut:

1. **Senaryo:** Kimin tam olarak ne söylediği.
2. **Oyunculuk niyeti:** Bu sözle karşısındaki kişiden ne istediği.
3. **Başlangıç görseli:** Hareket başlamadan önce tek bir görünür an.
4. **Video ve ses talimatı:** Bu andan sonra gerçekleşecek eylem, konuşma ve sonuç.

Görsel promptuna hem konuşma öncesini hem konuşma sonrasını aynı resimde anlatma. “Kapalı kapı, ardından açılmış kapı” tek başlangıç karesinin tanımı değildir.

### 19.1. Oyunculuk notunu kısa ve kullanılabilir tut

~~~text
SPOKEN LINE:
The lower stairs are flooded. I checked. Hold this plate.

INTENTION:
Ada corrects Leon's escape plan and asks him to help with the door.

DELIVERY:
Practical and focused. A small emphasis on "I checked".
~~~

“Nefesli, korkmuş, üzgün, öfkeli, umutlu, titrek, sinematik, fısıltılı” gibi birbiriyle yarışan etiketler yerine bir niyet ve gerekiyorsa tek değişim yaz.

Kısa oyunculuk notları anlamı veya ritmi açıklayabilir; her bakışı ve küçük hareketi paranteze doldurmak gerekmez.[^parentheticals]

### 19.2. Örnek başlangıç görseli promptu

Aşağıdaki prompt, 20. bölümdeki örnek sahnenin D02 planına aittir. Köşeli parantezli alanlara üretimde gerçekten kullandığın referansları ekle.

~~~text
Create one horizontal 16:9 cinematic still for the opening frame
of a dialogue shot. Use [ADA_REFERENCE] and [LOCATION_REFERENCE]
to preserve the established character and room.

Medium close-up of Ada beside a closed maintenance door.
She holds a screwdriver in her right hand, paused near a loose
metal latch plate. The plate's upper screw is visibly loose.
Ada looks toward Leon, who stands just outside the frame to camera right.
Her mouth is at rest, immediately before speaking.

Soft overhead work light. Consistent clothing, face, tool and door design.
Show this single moment only. No collage, captions or written dialogue.
~~~

Bu bir **görsel tasviridir**. Repliği resmin üzerine yazmak veya birkaç zaman anını birleştirmek amaçlanmaz.

### 19.3. Aynı plan için image-to-video talimatı

~~~text
Continue from the supplied opening frame.
Keep Ada's identity, clothing, the door and the screwdriver consistent.
Use a steady medium close-up.

Ada looks toward Leon and says:
"The lower stairs are flooded. I checked. Hold this plate."

She corrects his assumption in a practical, focused tone.
While asking for help, she indicates the loose latch plate
with a small movement of the screwdriver, then keeps the tool clear.
Leon remains off screen and does not speak in this shot.

After the line, Ada looks back at the plate, ready for Leon to help.
Do not add extra dialogue, new characters, captions or an unrelated event.
Target source duration: 10 seconds, if supported by the selected tool.
~~~

Saniye hedefi bir talimattır; aracın kesin zamanlama garantisi değildir. Çıktıda replik, telaffuz, konuşmacı ve hareketi kontrol et.

### 19.4. Ses desteğine göre üretim yolu

**Araç konuşma sesi üretiyorsa:** Tam repliği ve konuşmacıyı belirt. Üretilen sesi dinle; kelime ekleme, atlama, isim değiştirme veya yanlış kişiye ses verme ihtimalini çıktı üzerinden kontrol et.

**Araç yalnızca video üretiyorsa:** Diyaloğu ayrı ses kaydı olarak hazırla. Görüntü süresini bu kayda göre planla. Dudak eşleme gerekiyorsa, kullandığın araç ve iş akışının bunu desteklediğini ayrıca doğrula. Kadraj dışı konuşma ve dinleyenin görüntüsü bazı sahnelerde uygun anlatım tercihleri olabilir.

**Ses başka bir araçtan geliyorsa:** Konuşmacı kimliği, telaffuz, kayıt seviyesi ve ortam devamlılığını sahne boyunca tutarlı tut.

Bu kılavuz, GPT Image'ın video veya ses ürettiğini varsaymaz; görsel hazırlama aşaması için prompt örneği verir. İsimleri benzer video modellerinin aynı özellikleri taşıdığını da varsayma.

### 19.5. Replik sürümünü kilitle

~~~text
SCENE: S03
SHOT: D02
DIALOGUE VERSION: v03

EXACT SPOKEN TEXT:
The lower stairs are flooded. I checked. Hold this plate.

VOICE / PRONUNCIATION REFERENCE:
[Established Ada voice and pronunciation reference]

STATUS:
Text approved for production.
Audio duration not yet measured.
~~~

Repliği değiştirdiğinde ses dosyasını, video promptunu ve altyazıyı birlikte güncelle. Birindeki eski sürüm, doğru üretilmiş diğer parçaların uyumsuz görünmesine yol açabilir.

## 20. Baştan sona çalışılmış altı çekimlik örnek (60 saniye)

Bu bölüm yeni bir film fikri değil, yöntemi gösteren özgün bir diyalog alıştırmasıdır.

### 20.1. Sahne koşulları

- Ada ve Leon kapalı bir bakım kapısının önündedir.
- Kapının gevşemiş metal mandal plakası hizadan çıkmıştır; Ada yerine oturtup vidasını sıkmaya çalışır.
- Alt merdivenler suyla dolmuştur. Ada bunu kontrol etmiştir; Leon henüz bilmiyordur.
- Leon kapıda zaman kaybettiklerini düşünür.
- Ada işi tek başına yapmakta zorlanır; birinin plakayı sabit tutması gerekir.
- Sahne sonunda kapı açılır. Leon'un tavrı acele ettirmekten destek olmaya döner.

**Gerekli bilgi:** Merdiven yolu kullanılamaz; kapı birlikte çalışarak açılabilir.  
**İlişki hareketi:** Leon varsayımını bırakır ve Ada'ya yardım eder.  
**Gereksiz bilgi:** Binanın tarihi, kapının üreticisi, önceki bütün kaçış girişimleri.

### 20.2. Açıklama okuyan ilk taslak

~~~text
LEON:
Ada, we are trapped because this maintenance door has a loose
latch plate. I believe the lower stairs are our alternative route.

ADA:
Leon, I previously inspected those stairs and discovered that
they are flooded. I am currently repairing the plate, but I
require another person to hold it in position.

LEON:
I understand. I will assist you, although I am anxious about
how long the repair is taking.

ADA:
I am also anxious, but your support will make the repair easier.
~~~

Bilgi mevcut; fakat replikler insanların birbirini değiştirmesinden çok sahnenin raporunu sunuyor. İsimler işlevsiz tekrar ediliyor; duygu davranışın yerine açıklanıyor.

### 20.3. Yeniden yazılmış sahne

~~~text
LEON kapıya, ardından geldikleri yöne bakar.

D01 — LEON
Leave it. We can use the stairs.

ADA yaptığı işi bırakmadan kısa bir bakış atar.

D02 — ADA
The lower stairs are flooded. I checked. Hold this plate.

LEON yaklaşır. Elini gevşek mandal plakasına götürür.

D03 — LEON
This one?

ADA tornavidayı temas noktasından uzak tutarak plakayı işaret eder.

D04 — ADA
A little higher. There. Keep it still.

LEON plakayı yerine bastırır. ADA vidayı sıkmaya başlar.
LEON onun elindeki hafif titremeyi fark eder; baskısını sabit tutar.

D05 — LEON
I've got it. You're doing fine.

ADA vidayı sıkmayı bitirir. Mandalı kontrol eder.

D06 — ADA
That's it. Let go.

LEON plakanın üzerinden elini çeker.
ADA kapı kolunu indirip kapıyı iter. Kapı açılır.
~~~

Buradaki hareketler üretim taslağıdır. Araç aynı plan içinde gerekli el ve nesne devamlılığını sağlayamıyorsa planı basitleştir veya ayrı bir detay planı üret. Hatalı hareketi açıklama repliği ekleyerek gizlemeye çalışma.

### 20.4. Konuşma neden daha doğal?

- Leon bir alternatif önerir; Ada bu öneriye cevap verir.
- “I checked” Ada'nın bilgisine dayanak sunar ve tartışmayı kısaltır.
- “Hold this plate” açıklamayı yapılacak işe bağlar.
- “This one?” Leon'un söyleneni uyguladığını gösterir.
- Ada'nın kısa yönlendirmeleri ortak işe bağlıdır.
- Leon'un tesellisi, Ada'nın zorlandığını gördükten sonra gelir.
- Son replik onarımın bittiğini bildirir; kapının açılması bunu doğrular.

“Flooded” gibi gerekli bilgi korunmuştur. Diyalog kısalmıştır ama olayın nedeni kaybolmamıştır.

### 20.5. Kaynak ve kurgu planı

Aşağıdaki süreler **taslak hedeflerdir; sesle veya üretilmiş videoyla test edilmemiştir**. Hatta her çekim 10 s'dir; konuşmanın bittiği yerden sonrası tepki, sonuç ya da sonraki adım vuruşudur. Gerçek çıktıda cümlenin başlangıcı ve sonu korunacak biçimde 10 s'lik aralık seçilir.

| Çekim | Filmdeki zaman | Konuşma (taslak) | Vuruşlar | Görsel merkez |
|---|---|---|---|---|
| D01 | 00:00–00:10 | ~0-7 s | 0-7 öneri · 7-10 yönünü belli eder, yürümeye başlar | Leon alternatif yolu önerir. |
| D02 | 00:10–00:20 | ~0-8 s | 0-8 düzeltme · 8-10 plakayı gösterir | Ada yanlış varsayımı düzeltir. |
| D03 | 00:20–00:30 | ~2-4 s | 0-2 yaklaşır · 2-6 parçayı bulur ve sorar · 6-10 parçayı yerinden çıkarmaya başlar | Leon doğru parçayı bulur. |
| D04 | 00:30–00:40 | ~0-8 s | 0-8 hiza tarifi · 8-10 Leon plakayı sabitler | Ada hizayı tarif eder. |
| D05 | 00:40–00:50 | ~0-7 s | 0-4 zorlanma · 4-7 fark eder · 7-10 tavrı değişir, tutuşu bırakır | Leon zorlanmayı fark eder. |
| D06 | 00:50–01:00 | ~0-6 s | 0-6 onarım biter · 6-10 el çekilir, kapı açılır | Onarım biter. |
| **Toplam** | **60 saniye** | — | **6 çekim × 10 s** | — |

D03'te iki kelimeyi altı saniye söylemek hedeflenmiyor. Yaklaşma, doğru parçayı bulma ve sorunun bağlamı süreyi oluşturuyor. Bu eylemler gerçek çıktıda iki saniyede tamamlanıyorsa konuşmayı uzatma ve görüntüyü yavaşlatma; temiz kısım 10 s'ye yetmezse `uretim_hatti/SECIM_VE_KURGU_KILAVUZU.md` §6 sırası uygulanır.

### 20.6. D05 için görsel ve hareket ayrımı

**Başlangıç görseli:**

~~~text
One horizontal 16:9 cinematic still.
Use [LEON_REFERENCE], [ADA_REFERENCE] and [LOCATION_REFERENCE].

Medium close-up of Leon beside the same closed maintenance door.
His left hand holds the loose latch plate steady.
Ada's tool hand is visible at the lower edge of the frame,
positioned near the plate without overlapping Leon's fingers.
Leon looks down toward her hand. His mouth is at rest.

Preserve the established lighting, wardrobe and tool positions.
One moment only. No text or collage.
~~~

**Video talimatı:**

~~~text
Continue from the opening frame with a steady camera.
Leon keeps his left hand in place on the latch plate.
He notices a slight tremor in Ada's tool hand and looks toward her.

Leon says:
"I've got it. You're doing fine."

His tone is quiet and practical, without teasing.
Ada does not speak. Leon maintains steady pressure while she continues.
End on their shared task, with no additional dialogue or new event.
Target source duration: 10 seconds, if supported.
~~~

“Quiet” burada ses tonu için kullanılıyor; fısıltı zorunluluğu değildir. Amaç Leon'un Ada'yı acele ettirmekten vazgeçmesini duyurmaktır.

### 20.7. Türkçe diyalog uyarlaması

~~~text
D01 — LEON
Bırak. Merdivenlerden gideriz.

D02 — ADA
Alt merdivenler su altında. Baktım. Şu plakayı tut.

D03 — LEON
Bunu mu?

D04 — ADA
Biraz yukarı. Tamam. Oynatma.

D05 — LEON
Tuttum. İyi gidiyorsun.

D06 — ADA
Tamamdır. Bırakabilirsin.
~~~

Bu sürümün süresi ayrıca ölçülmelidir. “Plaka” sözcüğü görüntüde doğru nesneyi göstermiyorsa “şu parçayı” gibi daha gündelik bir karşılık seçilebilir; hangi parçanın kastedildiği yine anlaşılır olmalıdır.


## 21. On iki kısa yeniden yazım örneği

Aşağıdaki “zayıf” sürümler, belirtilen bağlam için zayıftır. Aynı cümle başka bir sahnede işlevli olabilir. Her değişiklikte bilgi ve ilişki kaybını ayrıca kontrol et.

### 21.1. Karakterin mesleğini herkese anlatması

**Bağlam:** Nil'in doktor olduğunu yanındaki herkes biliyor. Yaralı bir arkadaşının eline bakacak.

~~~text
ÖNCE
NIL: As a doctor, I have the medical knowledge to examine your injury.

SONRA
NIL: Let me see your hand.
~~~

Meslek bilgisi zaten kurulmuş olduğu için repliğin görevi izin istemektir. Seyirci Nil'in doktor olduğunu henüz bilmiyorsa bunu başka uygun bir kanıtla kur.

### 21.2. Her replikte isimle seslenme

**Bağlam:** Ada ve Leon yalnız. Dikkatleri zaten birbirinde.

~~~text
ÖNCE
ADA: Leon, did you bring it?
LEON: Yes, Ada, it's in my bag.
ADA: Leon, take it out.

SONRA
ADA: Did you bring it?
LEON: In my bag.
ADA: Get it out.
~~~

İsimler bir dikkat değişimi yaratmıyor. Kalabalıkta doğru kişiyi çağırmak, birini kendine getirmek veya yakınlık kurmak için isim kullanmak hâlâ anlamlı olabilir.

### 21.3. Ortak geçmişi özetleme

**Bağlam:** İki kişi hastanede verilmiş aynı sözü hatırlıyor; biri sözün tutulmadığını düşünüyor.

~~~text
ÖNCE
ADA: When we were at the hospital, you promised that you would
never make this decision without me again.

SONRA
ADA: You promised me at the hospital.
LEON: I meant it.
ADA: Then why am I hearing about this from someone else?
~~~

Sözün tam içeriği sahnenin önceki konuşmasında kurulmuş olmalı. Kurulmadıysa ilk cümleye “You said we'd decide together” eklemek gerekebilir. Kısa sürüm, kendi başına bütün bağlamı taşımıyor.

### 21.4. Duyguyu raporlamak

**Bağlam:** Nil yalnız kalmak istemiyor; henüz bunu açıkça söyleyemiyor.

~~~text
ÖNCE
NIL: I am experiencing anxiety about being left alone.

SONRA
NIL: Are you leaving now?
OREN: In a minute.
NIL: Could you wait until she gets here?
~~~

Duygu bir talep üzerinden görünür. Nil'in açık konuşabildiği bir anda “I'm scared to be here alone” da gayet uygun olabilir.

### 21.5. İçeriği olmayan tehdit

**Bağlam:** Leon vardiyasını yine Ada'ya bırakmaya çalışıyor.

~~~text
ÖNCE
ADA: If you leave, there will be consequences you cannot imagine.

SONRA
ADA: If you walk out, I won't cover your shift again.
~~~

Somut sınır, bu sahnedeki gerçek çatışmayı taşır. İlk sürümün belirsiz büyük tehdidi karakterin koşuluna uymuyor.

### 21.6. Her duyguyu şiirle anlatmak

**Bağlam:** Oren, yakınını hayal kırıklığına uğratmış; konuşma gündelik ve özel.

~~~text
ÖNCE
OREN: My heart is a ruined house in which your trust no longer lives.

SONRA
OREN: I know an apology won't fix it. Tell me what I can do today.
~~~

İkinci replik onarım girişimidir. Oren sürekli mecazlarla konuşan bir şairse ilk üslup farklı değerlendirilebilir; yine de karşı tarafın tepkisini düşün.

### 21.7. Teknik açıklamanın anlamı örtmesi

**Bağlam:** Bir alıcı tam güçte iki, düşük güçte altı saat çalışabiliyor. Karakter kullanım kararı verecek.

~~~text
ÖNCE
ADA: The device's operational endurance varies according to the
selected power configuration, with values of two and six hours.

SONRA
ADA: Two hours at full power. Six if we turn it down.
LEON: Will we still hear the signal?
~~~

Süreler korunur. Leon'un sorusu bir sonraki gerekli bilgiyi açar. Cevap, kurmaca cihazın önceden belirlenmiş kuralına uymalıdır.

### 21.8. Görüntünün anlattığını tekrar etmek

**Bağlam:** Nil elindeki kırık kupaya bakıyor; kupayı Oren'in kullandığını biliyor.

~~~text
ÖNCE
NIL: My cup is broken, and I can see that this makes me sad.

SONRA
NIL: You could've told me.
OREN: I was going to replace it.
NIL: It was my mother's.
~~~

Söz, görünen kırığı tarif etmek yerine neden önem taşıdığını ekler. “Annesinin kupası” yeni bir örnek hikâye bilgisidir; gerçek bir senaryoyu revize ederken izin verilmeden böyle bir geçmiş eklenmemelidir.

### 21.9. Aciliyete uymayan resmiyet

**Bağlam:** İki yakın arkadaşın geçişi kapanmak üzere.

~~~text
ÖNCE
LEON: Would you perhaps consider moving to this side of the doorway?

SONRA
LEON: This side. Now.
~~~

Kısa emir burada işlevlidir. Aynı cümleyi sakin bir toplantıda kullanmak ilişkiyi gereksiz sertleştirebilir.

### 21.10. Önceki repliği duymayan cevap

**Bağlam:** Ada birinin hâlâ içeride olduğunu söylemiştir.

~~~text
ÖNCE
ADA: Nil's still inside.
LEON: The vehicle is ready for departure.

SONRA
ADA: Nil's still inside.
LEON: Where?
ADA: The room behind the stairs.
LEON: Keep the door open.
~~~

Yeni konuşma duyulan bilgi üzerine gelişir. Ada'nın konumu bilmesi hikâyede kurulmalı; bilmiyorsa dürüstçe “I don't know” demesi gerekir. Araç hazır bilgisinin bu anda gerekli olup olmadığını ayrıca kontrol et; gerekiyorsa uygun bir sonraki replikte koru.

### 21.11. Herkesin aynı şakayı sürdürmesi

**Bağlam:** Leon gerilimi espriyle yönetir; Nil'in dikkati kayıp arkadaşındadır.

~~~text
ÖNCE
LEON: Great. Another door that hates us.
NIL: Maybe it read our reviews.
ADA: Tough crowd.

SONRA
LEON: Great. Another door that hates us.
NIL: Can you open it?
LEON: I'm trying.
~~~

Espri tamamen silinmez; herkes aynı mizah ritmine katılmaz. Nil'in gerçek ihtiyacı konuşmanın yönünü belirler.

### 21.12. Savunmaya geçen kişiyi tek kelimeye indirmek

**Bağlam:** Oren bir kararı geciktirmiştir. Yalan söylemiyor; kararının makul olduğuna inanıyor.

~~~text
ÖNCE
NIL: You waited.
OREN: No.

SONRA
NIL: You waited.
OREN: I waited for a reply. You asked me not to make the call
until we heard from them.
NIL: I asked you to wait until morning.
~~~

Oren'in daha uzun cevabı kendi gerekçesini ortaya koyar. Nil aynı olayın sınırını farklı anladığını gösterir. Konuşmayı tek kelimelik karşılıklara indirmek burada çatışmayı zayıflatır.

## 22. Yedi geçişte diyalog revizyonu

Bütün sorunları aynı anda düzeltmeye çalışmak, iyi bir ayrıntıyı yanlışlıkla silmene neden olabilir. Her geçişin ayrı bir sorusu olsun.

| Geçiş | Ana soru | Somut çıktı |
|---|---|---|
| 1. Hikâye doğruluğu | Gerekli bilgi ve neden-sonuç korunuyor mu? | Değiştirilmeyecek gerçekler listesi |
| 2. Niyet | Her konuşmacı burada ne elde etmeye çalışıyor? | Kişi başına bir sahne amacı |
| 3. Karakter sesi | Dikkat, yaklaşım ve dil karaktere ait mi? | Konuşma profiline göre işaretlenmiş replikler |
| 4. Dinleme | Cevap önceki sözü duyuyor mu? | Kopuk cevapların düzeltilmesi |
| 5. Açıklık ve alt metin | Seyirci gerekeni anlıyor mu; ilişki de okunuyor mu? | Eksik veya fazla açıklamaların dengelenmesi |
| 6. Sesli okuma | Ağza takılan, yapay veya nefessiz kalan yer var mı? | Konuşularak düzeltilmiş sürüm |
| 7. Süre ve üretim | Gerçek ses, eylem ve plan sınırı uyumlu mu? | Ölçülmüş ses ve kurgu planı |

### 22.1. Revizyondan sonra değişiklik kaydı tut

~~~text
DEĞİŞİKLİK:
Ada'nın iki açıklama cümlesi bir bilgi ve bir talebe dönüştürüldü.

KORUNAN:
Alt merdivenlerin suyla dolu olması.
Ada'nın bunu önceden kontrol etmiş olması.
Leon'un plakayı tutmasının gerekmesi.

ÇIKARILAN:
Kapının görünür arızasının sözle tekrar edilmesi.

YENİDEN KONTROL:
Sonraki sahnede merdivenlerin kullanılmadığından emin ol.
Repliğin yeni ses süresini ölç.
~~~

“Daha doğal oldu” yeterli bir kalite kaydı değildir. Ne değiştiğini ve neyin korunması gerektiğini bil.

### 22.2. Ne zaman yeniden yazmayı bırakmalı?

- Karakterin amacı anlaşılıyorsa.
- Dinleyenin cevabı önceki söze bağlıysa.
- Gerekli bilgi kaybolmamışsa.
- Konuşma profili birkaç replik boyunca hissediliyorsa.
- Sesli okumada hedeflenen oyunculukla söylenebiliyorsa.
- Süre, anlamı bozmadan üretim planına yerleşiyorsa.

Bir repliğin daha kısa başka bir sürümünün bulunabilmesi, mevcut sürümün yanlış olduğu anlamına gelmez.

## 23. Doldurulabilir çalışma kartları

### 23.1. Karakter konuşma profili

~~~text
KARAKTER:
Hikâyedeki görevi:
Bu sahnede istediği:
Söylemekten kaçındığı:

İlk dikkat ettiği şey:
Belirsizlik karşısındaki tavrı:
Yardım isteme biçimi:
İtiraz etme biçimi:
Bilgi verirken seçtiği ayrıntı:
Tipik cümle ritmi:
Gerçekten bildiği kelime alanı:

Baskı altında ne değişir?
Güvendiği kişinin yanında ne değişir?
Otorite karşısında ne değişir?

Sık kullanabileceği ama zorunlu olmayan 2 özellik:
1.
2.

Bu karakteri tek tipe indirmemek için istisna:
Örnek gündelik replik:
Örnek zor bir şey isteme repliği:
Örnek özür veya itiraf repliği:
~~~

### 23.2. Sahne ve bilgi kartı

~~~text
SAHNE:
Görünür eylem:
Sahne başındaki durum:
Sahne sonundaki değişim:

A'nın istediği:
B'nin istediği:
İşbirliği / çatışma noktası:

SEYİRCİNİN ŞİMDİ BİLMESİ GEREKEN:
1.
2.

A ne biliyor?
B ne biliyor?
Seyirci ne biliyor?

Hangi bilgi görüntüde açık?
Hangi bilgi konuşmayla verilmeli?
Hangi bilgi şimdilik gereksiz?
Hangi belirsizlik kasıtlı?
Hangi belirsizlik yanlış anlaşılmaya yol açıyor?
~~~

### 23.3. Replik ve klip kartı

~~~text
SAHNE / PLAN:
REPLİK SÜRÜMÜ:
KONUŞMACI:
KARŞISINDAKİ:
TAM SÖYLENECEK METİN:

Bu sözle istediği:
Önceki repliğe bağlantısı:
Gerekli bilgi:
Alt metin varsa:

KAYNAK KLİP HEDEFİ: 10 s
ÇEKİM SÜRESİ: 10 s (sabit)
VURUŞLAR:
KELİME SAYISI:
TAHMİNİ SES SÜRESİ:
ÖLÇÜLMÜŞ SES SÜRESİ: [henüz ölçülmedi / süre]

Konuşmayla aynı anda olan eylem:
Konuşmadan sonra gereken eylem veya tepki:
Başlangıç görselindeki durum:
Plan sonunda değişen durum:

Ses üretim yolu:
Ses / telaffuz referansı:
Görsel referanslar:
Devamlılık notu:

KURGUDAN SONRA
Seçilen 10 s'lik kaynak aralığı:
Temiz kısım 10 s'ye yetti mi? (yetmediyse kurtarma yolu)
Replik tam duyuluyor mu?
Sonraki plana geçiş anlaşılır mı?
~~~

### 23.4. Diyalog revizyon denetimi

~~~text
ÖNCEKİ REPLİK:
YENİ REPLİK:

Sorun:
Yaptığım değişiklik:
Korunan gerçekler:
Çıkardığım bilgiler:
Yeni eklenen bilgi varsa:
Bu yeni bilgi için senaryo onayı var mı?

Karakterin ilişkideki tavrı değişti mi?
Amaçlanan anlam hâlâ aynı mı?
İzleyicinin bilmesi gereken bir şey kayboldu mu?
İngilizce ve Türkçe aynı niyeti taşıyor mu?
Ses / video / altyazı sürümleri güncellendi mi?
~~~


## 24. Kopyalanabilir ana promptlar

Bu promptlar bir metin modeliyle senaryo çalışmak içindir. Dosya eklemek veya görsel/video üretimini başlatmak için otomatik yetki vermezler. Köşeli parantezleri kendi sahnenle doldur.

### 24.1. Açıklama okuyan diyalogu yeniden yaz

~~~text
Bir film senaryosu diyalog editörü olarak çalış.

AMAÇ
Aşağıdaki sahnede karakterlerin seyirciye bilgi anlatır gibi
konuşmasını azalt. Konuşmayı, karakterlerin birbirinden bir şey
istemesi ve duyduklarına cevap vermesi üzerinden yeniden yaz.

ÇIKTI DİLİ
Diyalog: [İngilizce / Türkçe]
Açıklama ve değişiklik kaydı: Türkçe

SAHNE BAĞLAMI
[Mekân, önce olan olay, görünür eylem, sahnenin sonucu]

DEĞİŞMEMESİ GEREKEN GERÇEKLER
[Olaylar, isimler, ilişkiler, dünya kuralları, gereken bilgiler]

KARAKTERLER
[A: amacı, bildikleri, konuşma profili]
[B: amacı, bildikleri, konuşma profili]

MEVCUT SAHNE
[Metni yapıştır]

KURALLAR
- Yeni geçmiş, teknoloji kuralı veya olay uydurma.
- Herkesin bildiği bilgiyi neden söylediklerini kontrol et.
- Dinleyenin bilmediği gerekli bilgiyi sırf kısa olsun diye silme.
- Bütün cümleleri kısa, sert, gizemli veya esprili yapma.
- Uzun bir cümle karakterin düşüncesini ilerletiyorsa koru.
- Gerekli açık anlatımı koru; her şeyi alt metne çevirme.
- Karakterler önceki repliği gerçekten duymuş gibi cevap versin.
- Senaryo ile oyunculuk notunu ayır.
- Eksik bağlam yüzünden kesin karar veremiyorsan varsayımı belirt.

ÇIKTI
1. En önemli 3–5 somut sorun.
2. Yeniden yazılmış tek sahne.
3. Korunan / çıkarılan / yeni eklenmesi önerilen bilgi tablosu.
4. En fazla 3 yerde kısa revizyon gerekçesi.
5. Hikâye sahibinin karar vermesi gereken gerçek belirsizlikler.

Yalnızca daha süslü sözcükler seçerek revizyon yapma.
~~~

### 24.2. Karakterlerin sesini birbirinden ayır

~~~text
Aşağıdaki karakterler aynı yazarın aynı sesiyle konuşuyormuş gibi
hissediliyor. Her biri için tutarlı ama esnek bir konuşma profili
hazırla ve verilen sahneyi bu profillere göre düzelt.

KARAKTER BİLGİLERİ
[Her biri için: amaç, korku, ilişki, bilgi alanı, baskı altındaki tavır]

SAHNE
[Metin]

İNCELEME EKSENLERİ
- İlk dikkat ettiği şey
- Belirsizliğe yaklaşımı
- Yardım isteme ve itiraz etme biçimi
- Bilgi verirken seçtiği ayrıntı
- Cümle ritmi
- Güvendiği kişiyle ve otoriteyle konuşurken değişimi

KISITLAR
- Aksan, cinsiyet, milliyet veya tür klişelerini kişilik yerine kullanma.
- Herkese ayrı bir slogan veya yapay kelime yasağı verme.
- Her repliğin kimliğini tek başına ilan etmesini bekleme.
- Yaşanan olayları ve sahnenin sonucunu değiştirme.
- Bir karakteri doğal yapmak için diğerlerini karikatürleştirme.
- Ünlü bir oyuncunun veya yaşayan bir kişinin taklidini hedefleme;
  özgün karakter özellikleri üzerinden çalış.

ÇIKTI
1. Karakter başına 2–3 belirgin konuşma özelliği.
2. Her karakterin bir ilişkiye göre nasıl esneyebileceği.
3. Yeniden yazılmış sahne.
4. Konuşmacı isimleri silindiğinde ayırt etmeye yardımcı olan
   üç somut fark ve hâlâ birbirine benzeyen yerler.
~~~

### 24.3. Türkçeden doğal İngilizce diyaloğa uyarla

~~~text
Aşağıdaki Türkçe film diyaloğunu İngilizceye uyarlayacaksın.

HEDEF
Kelime sırasını kopyalamak yerine anlamı, niyeti, ilişki mesafesini,
gereken bilgiyi ve bilinçli alt metni koruyan konuşma İngilizcesi.

BAĞLAM
[Mekân, durum, karakterlerin ilişkisi]

KARAKTER ÜSLUPLARI
[Karakter başına kısa konuşma profili]

METİN
[Türkçe sahne]

KURALLAR
- İngilizceyi gereksiz resmîleştirme veya argoyla doldurma.
- Gündelik kısaltmaları karaktere uygunsa kullan.
- Özel adları ve dünya kurallarını koru.
- Belirsiz bir Türkçe cümlenin niyetini uydurma; olası anlamları
  kısaca belirt ve seçtiğin varsayımı açıkla.
- Bütün karakterleri aynı sert, kısa cümlelerle konuşturma.
- Doğal uyarlama adına yeni olay veya geçmiş ekleme.
- Süreyi kelime sayısından kesin olarak bildiğini iddia etme.

ÇIKTI
1. İngilizce sahne.
2. Anlamı veya tavrı belirgin biçimde etkileyen çeviri kararları.
3. Zor telaffuz / referansı belirsiz zamir / sesli okumada
   kontrol edilmesi gereken yerler.
4. İstenirse: İngilizce sürümün niyetini Türkçe tek cümleyle açıkla;
   otomatik olarak ikinci bir tam senaryo yazma.
~~~

### 24.4. Diyaloğu klip ve ses planına dönüştür

~~~text
Aşağıdaki onaylı diyaloğu AI film üretim planına dönüştür.

VERİLER
Çekim süresi: 10 saniye (sabit; kısaltılmaz)
Filmin hedef süresi: [süre] → çekim sayısı = süre / 10
Diyalog dili: [dil]
Video aracının doğrulanmış ses özelliği: [bilgi / bilinmiyor]
Ölçülmüş ses süreleri: [plan ve süre listesi / henüz yok]
Karakter ve mekân referansları: [referanslar]
Sahne metni: [metin]

ÖNCELİK
Konuşmanın anlamını ve karakterlerin tepkisini koru.

KURALLAR
- Her çekim 10 saniyedir; konuşma bittikten sonraki saniyelere tepki,
  sonuç ya da sonraki adım yaz (vuruş: 2-4, her biri ≥2 s, son vuruş donmaz).
- Ses ölçülmediyse süreleri tahmin diye etiketle.
- Kullandığın konuşma hızı varsayımını açıkça belirt.
- Konuşmayla eşzamanlı eylemi, sonradan gelen eylemden ayır.
- Replik erken bittiğinde otomatik bekleme veya yavaş hareket ekleme.
- Cümleyi süreye sığdırmak için anlamını kesme.
- Gerekirse uygun başka plana devam ettir veya yeniden yazım öner;
  onaylı metni değiştirdiğini açıkça işaretle.
- Tek başlangıç görseli promptunda tek bir an anlat.
- Söylenecek sözleri, oyunculuk notlarını ve kamera notlarını ayır.
- Modelin desteklediği doğrulanmamış ses, süre veya dudak eşleme
  özelliklerini varmış gibi kullanma.
- Çekim sayısı × 10 = hedef süre olduğunu kontrol et.

ÇIKTI
1. Çekim tablosu: konuşmacı, tam replik, görünür iş, ses süresi
   tahmini/ölçümü, 10 s'nin vuruş planı.
2. Her planın başlangıç durumu ve sonunda değişen durum.
3. Seçilen bir plan için başlangıç görseli promptu ve ayrı
   image-to-video talimatı.
4. Ölçülmesi veya gerçek çıktıdan kontrol edilmesi gerekenler.
5. Repliği 10 s'ye sığmayan ya da 10 s'yi taşıyamayan çekimler
   ve önerilen çözüm (bölme, birleştirme, tepki vuruşu).

Şimdilik yalnızca metin planı üret; görsel veya video oluşturma.
~~~

### 24.5. Kısa son kontrol promptu

~~~text
Bu sahneyi yeniden yazmadan önce denetle.

Yalnızca somut kanıt göstererek şu beş soruyu yanıtla:
1. Kim hangi replikte seyirciye açıklama okur gibi konuşuyor?
2. Hangi karakterlerin dikkat, niyet ve cümle ritmi birbirine benziyor?
3. Hangi cevap önceki repliği duymamış gibi?
4. Nerede gerekli bilgi eksik, nerede gereksiz tekrar var?
5. Hangi replik hedef oyunculukla süreye sığmayabilir?

Her bulgu için metinden kısa bir bölüm, nedeni ve tek düzeltme yönü ver.
Sorun olmayan yeri zorla sorun ilan etme.
Duyulmayan sesin süresini ölçmüş gibi davranma.

SAHNE:
[Metin]
~~~

## 25. Alıştırmalar ve değerlendirme

### 25.1. Karakteri filmin dışında konuştur

Ana olaydan bağımsız, küçük bir gündelik durum seç: ödünç aldığı bir aleti geç iade etmek, yanlış gelen yemeği değiştirmek veya sessiz bir yerde birinden yardım istemek.

Aynı durumu dört karakterle ayrı ayrı, 6–8 repliklik kısa konuşmalar halinde yaz. Kimin neye dikkat ettiğine ve talebini nasıl kurduğuna bak. Bu yaklaşım, John August'ın karakter sesini ana senaryonun dışında deneme önerisiyle uyumludur; buradaki alıştırma konuları özgün örneklerdir.[^offpage]

**Başarı ölçütü:** Dört ayrı aksan değil, dört ayrı yaklaşım görmek.

### 25.2. İsimleri gizle

Bir sahnede konuşmacı isimlerini geçici olarak A ve B yap. Birkaç replik boyunca kimin kim olduğunu hangi tercihlerden anladığını yaz.

“Evet”, “Tamam”, “Burada” gibi ortak kısa sözlerin ayırt edilememesi sorun değildir. Bütün sahnenin aynı düşünme ve cevap verme biçimine sahip olması daha anlamlı bir uyarıdır.

**Başarı ölçütü:** Dikkat, tavır veya ritim üzerinden en az birkaç somut fark tarif edebilmek; her repliği tahmin etmek zorunlu değil.

### 25.3. Cevap bağını sök

Bir karakterin cevabını başka bir sorunun altına taşı. Cevap hâlâ hiçbir değişiklik gerektirmeden çalışıyorsa nedenini incele.

~~~text
SORU 1: Did you tell her?
SORU 2: Are you staying?
GENEL CEVAP: We have to keep moving.
~~~

Bu cevap bilinçli bir kaçış olabilir. Ama her sorunun altında aynı işlevle duruyorsa karakterin dinlemesi zayıf yazılmış olabilir.

**Başarı ölçütü:** Cevabın önceki sözden hangi bilgi, duygu veya talebi aldığını gösterebilmek.

### 25.4. Aynı ihtiyacı iki biçimde yaz

İhtiyaç: “Gitmeni istemiyorum.”

- Bir sürümde kişi açıkça söylesin.
- Diğerinde doğrudan söylemekten kaçınsın.
- Her sürümde karşı tarafın cevabını da yaz.

Sonra hangi ilişkinin ve sahne anının hangi sürümü taşıdığını belirt. Alt metinli sürümü otomatik olarak daha iyi sayma.

**Başarı ölçütü:** İki sürümün farklı ilişki koşulları gerektirdiğini açıklayabilmek.

### 25.5. Sesli okuma ve süre

Aynı repliği önce gerçek niyetle, sonra yalnızca süreye yetişmeye çalışarak oku. İkincisinde hangi kelimelerin ve tepkilerin kaybolduğunu dinle.

Kayıt alabiliyorsan şunları işaretle:

- Düşüncenin değiştiği yer.
- Gerçek nefes ihtiyacı.
- Doğal vurgu.
- Fazla açıklamanın başladığı yer.
- Karşı tarafın cevabına alan açan an.

**Başarı ölçütü:** Süre sorununu sadece daha hızlı konuşarak çözmemek.

### 25.6. Bilgiyi koruma deneyi

Açıklama dolu bir paragraftan üç gerekli gerçeği çıkar. Diyaloğu yeniden yaz. Ardından yalnızca yeni sahneyi okuyarak o üç gerçeği geri bulmaya çalış.

**Başarı ölçütü:** Doğallık artarken gereken bilgi hâlâ anlaşılabiliyor. Bir bilgi yalnızca yazarın notlarında kaldıysa sahnede kurulmuş sayılmaz.

### 25.7. Değerlendirme tablosu

Her maddeyi “hazır”, “revizyon gerekli” veya “ses/çıktı testi bekliyor” olarak işaretle. Tek bir toplam puan, önemli bir bilgi hatasını örtemesin.

| Ölçüt | Kanıt olarak neye bakacaksın? |
|---|---|
| Sahne amacı | Konuşmanın sonunda değişen durum |
| Karakter ayrımı | Dikkat, talep ve cevap biçimindeki somut farklar |
| Bilgi açıklığı | İzleyicinin şimdi bilmesi gerekenlerin sahnede bulunması |
| Dinleme | Önceki söze bağlı cevaplar |
| İlişki | Söylenenin karşı tarafta yaptığı değişim |
| Konuşulabilirlik | Hedef oyunculukla sesli okuma |
| Süre | Tahmin değil, ölçülmüş ses ve gerçek kurgu aralığı |
| Üretim tutarlılığı | Aynı replik sürümünün ses, video ve altyazıda kullanılması |

Bu değerlendirme, görüntülenme veya başarı tahmini değildir. Senaryonun ve üretim planının belirli sorunlarını bulmak için bir araçtır.

## 26. Son kontrol, kullanım sırası ve kaynaklar

### 26.1. Üretim öncesi son kontrol

- [ ] Her karakterin bu sahnede istediği şey belli.
- [ ] Kimin ne bildiği kaydedildi.
- [ ] Karakterler birbirlerine konuşuyor; gerekli açıklamanın sahne içi nedeni var.
- [ ] Herkes aynı sözcük, ritim ve benzetmelerle konuşmuyor.
- [ ] Karakterler önceki sözlere cevap veriyor.
- [ ] Açık bilgi gereken yerde anlaşılır biçimde veriliyor.
- [ ] Alt metin yalnızca yazarın açıklamasında kalmıyor.
- [ ] Kısaltırken olay, ilişki veya dünya kuralı değiştirilmedi.
- [ ] Uzun replikler sırf uzun oldukları için silinmedi.
- [ ] İngilizce uyarlamanın anlamı ve tavrı kontrol edildi.
- [ ] Oyunculuk notları söylenecek sözlerden ayrıldı.
- [ ] Sesli okuma yapıldı; yapılmadıysa bekleyen iş olarak işaretlendi.
- [ ] Süreler “tahmin” ve “ölçülmüş” diye ayrıldı.
- [ ] Başlangıç görseli tek bir anı tanımlıyor.
- [ ] Her çekim 10 s; replik çekimin vuruşuna sığıyor.
- [ ] Konuşma bittikten sonra kalan sürenin anlatı işlevi var (tepki, sonuç ya da sonraki adım).
- [ ] Ses, video promptu ve altyazı aynı replik sürümünü kullanıyor.

### 26.2. İlk uygulamada izleyeceğin sıra

1. Mevcut filminden yapay hissettiren **tek bir sahne** seç.
2. 23. bölümdeki sahne ve bilgi kartını doldur.
3. Konuşan iki karakter için kısa konuşma profili çıkar.
4. 24.1'deki promptla revizyon al; değişen bilgileri kendin kontrol et.
5. Sesli oku veya taslak ses üret; ardından 24.4 ile klip planına çevir.
6. İlk gerçek çıktıyı dinleyip izle; yalnızca gördüğün soruna yönelik düzeltme yap.

Bir sahnede işe yarayan her tercihi bütün filme yayma. Aynı karakter farklı ilişkilerde, farklı baskı altında ve hikâyenin farklı aşamalarında esneyebilir.

### 26.3. Kaynaklar ve kullanım notu

Bu dosyadaki karakterler, sahneler, örnek replikler, çalışma kartları, promptlar ve süre planları bu kılavuz için hazırlanmıştır. Aşağıdaki birincil kaynaklar belirli senaryo yazımı ilkelerine dayanak sağlar. Dosya bir modelin teknik kullanım belgesi değildir; özellikleri doğrulanmamış bir üretim aracına kesin yetenek atfetmez.

[^dialogue]: John August, [How to write dialogue](https://johnaugust.com/2007/how-to-write-dialogue), 2007. Konuşmanın amacı, gerçek konuşmayı dinleme ve yazılan diyaloğu değerlendirme üzerine birincil senaryo yazımı kaynağı.

[^voice]: John August ve Craig Mazin, Scriptnotes, [Dialogue — Episode 37](https://johnaugust.com/2012/dialogue), 2012. Karakterlerin diyalog içinde ayrışması ve konuşmanın sahnedeki işlevi üzerine tartışma.

[^offpage]: John August, [Writing off the page](https://johnaugust.com/2010/writing-off-the-page), 2010. Karakteri ana senaryonun dışında yazarak sesini keşfetme alıştırması.

[^parentheticals]: John August, [Using parentheticals](https://johnaugust.com/2003/using-parentheticals), 2003. Senaryoda kısa oyunculuk ve söyleyiş açıklamalarının kullanımı.

**Son üretim notu:** Bu belgede gerçek ses veya video çıktısı test edilmemiştir. Örnek planların kesin süreleri, seçtiğin ses performansı ve üretilen görüntü üzerinden belirlenmelidir.

