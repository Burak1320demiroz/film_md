# 🔬 09 — KARAKTER DONANIM ARAŞTIRMA PROMPTLARI (TUR 5 girdisi · 03.09.2026)

> **Ne bu dosya:** filmlerdeki astronot karakterlerin giysi donanımını
> (rozet/amblem · kişisel eşya · saat/bilek · yaşam destek ünitesi)
> derinleştirmek için yazılmış dört derin araştırma promptu. Her biri
> **altı cümledir** ve **salt prompt** çalışır — kopyala, araştırma
> aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı
> prompt ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki
> turun sonucu karşılaştırılamaz (07 ve 08'in gerekçesiyle aynı).
>
> **KOŞU KAYDI:** dört prompt 03.09.2026'da koşuldu → dört rapor geldi.
> Ham metinler: `TUR5_HAM_RAPORLAR/` (TAM metin — Tur 4'ün "iddia
> düzeyinde arşiv" kısayolu bu turda ALINMADI).
> Süzme: `04_ARASTIRMA_BULGULARI.md` §TUR 5.
> Kural indiği yer: `../ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md`.

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md (süzme kaydı) →
         ancak oradan ilgili kılavuza.
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ SAYI KILAVUZA YAZILMADAN ÖNCE ETİKETLENİR.
   Bu turun raporları tarihsel ÖLÇÜ (belgeli donanım boyutu) ile
   kurgusal TASARIM ÖNERİSİNİ (raporun kendi icadı) aynı tabloda verdi.
   İkisi aynı şey değildir; süzme kaydında ayrı etiket taşır.

⛔ RAPORLAR ÇAPRAZ OKUNUR.
   Aynı donanım iki raporda farklı sayıyla geçiyorsa (Tur 5'te geçti:
   bilek kontrol listesi sayfa boyutu) sayı kılavuza İNMEZ, çelişki
   kayda geçer.
```

---

# 1️⃣ ROZET, YAMA VE AMBLEM SİSTEMİ

```
Gerçek uzay giysilerindeki rozet, yama ve amblem sistemini görsel referans düzeyinde çıkar: Apollo A7L'den NASA EMU ve xEMU'ya, Rus Orlan ve Sokol'dan SpaceX ile Axiom giysilerine kadar görev yamaları, isim şeritleri, ajans amblemleri, bayraklar ve komutanı ayıran kırmızı şerit geleneği hangi gövde bölgesinde, hangi boyutta, hangi malzeme ve tutturma yöntemiyle (beta cloth, cırt bant, dikiş) duruyor, tek tek belgele. Her öğe için konumu (sol göğüs, sağ omuz, kol), çapını veya kenar uzunluğunu santimetre olarak, renk paletini ve kenar dokusunu (kabartma nakış, baskı) ver; uçuş fotoğrafları, müze arşivleri ve NASA/ESA teknik dokümanları gibi birincil kaynaklara dayan. Görev yaması sembolojisinin geleneklerini ayrıca çıkar: araç silueti, yörünge çizgisi, mürettebat sayısı kadar yıldız gibi SAYILABİLİR konvansiyonlar hangi görevlerde nasıl kullanılmış. Kritik kısıt: AI video üretimi küçük metni bozar ve bizim sistemimizde kadraj içi okunur yazı zaten yasak — hangi yama tipleri tamamen metinsiz, salt geometri ve renkle çalışır, gerçek örnekleriyle ayır. İkinci kısıt: gerçek bayrak, ülke adı ve ajans logosu hem telif hem politika riski taşıdığından kullanılamaz — ülke-nötr, kurgusal bir amblem dili için tasarım ilkeleri (iki-üç renk, sayılabilir öğe, asimetrik yerleşim) ve 2-4 kişilik bir ekipte rolü (komutan, mühendis, tıbbi) uzak ölçekten ayırt ettiren işaret sistemleri öner. Çıktıyı tablo olarak ver: öğe adı, konum, boyut, renk/malzeme, tek satırlık İngilizce prompt ifadesi, kimlik çapası değeri (uzak ölçekte okunurluk) ve üretimde bozulma riski sütunları.
```

---

# 2️⃣ KARAKTERE ÖZEL KİŞİSEL EŞYALAR

```
Gerçek astronotların uzaya taşıdığı kişisel eşyaların belgelenmiş envanterini çıkar: Personal Preference Kit içerikleri, Soyuz kabinine asılan ve yerçekimi göstergesi işlevi gören peluş oyuncak geleneği, aile fotoğrafları, yüzükler, dini ve uğur objeleri, müzik aletleri gibi somut vakaları isim ve görev numarasıyla listele. Giysi ve kask ÜZERİNDE görünür kişiselleştirmeyi ayrıca araştır: kask içi iletişim başlığı varyasyonları, eldiven üstü kalem, bilek kontrol listesine iliştirilen kişisel notlar, alet halkasına (D-ring) asılan objeler ve mürettebatın kendi ekipmanını işaretleme gelenekleri. Her eşya için basınçlı EVA eldiveniyle tutulup tutulamayacağını, giysinin neresine bağlandığını (cırt bant, kordon, göğüs cebi) ve yerçekimsiz ortamda nasıl davrandığını (süzülme, dönme, yüzeye yapışma) belirt. Amaç dramaturjik: tek kâşifli 10-20 dakikalık uzay filmlerinde eşya sahnesi bütçesi ayrılıyor — hangi eşyalar aşırı yakın çekim gerektirmeden tek karede okunur, hangi duygu vuruşunu (bağ, kayıp, umut, veda) taşır, gerçek anlatı örnekleriyle eşle. Aynı üniformayı giyen iki-üç karakteri yalnız kişisel eşyayla ayırt etmenin sinema ve gerçek görev örneklerini topla; sayılabilir, yüksek kontrastlı ve asimetrik konumlu eşya tasarım ilkelerini çıkar. Çıktıyı tablo olarak ver: eşya, belgelenmiş kaynağı, görsel tanımı (boyut, renk, malzeme), giysideki konumu, tek satırlık İngilizce prompt ifadesi ve hizmet ettiği duygu vuruşu.
```

---

# 3️⃣ SAAT VE BİLEK DÜZENİ

```
Uzay saatçiliğinin tam envanterini çıkar: Apollo'daki Omega Speedmaster kullanımı ve NASA sertifikasyon testleri, Bulova istisnası, Rus uçuşlarındaki Strela ve Poljot geleneği, ISS döneminde dijital saat kullanımı ve EVA sırasında saatin giysi kolunun ÜZERİNE uzatılmış cırt kayışla takılması pratiği. Bilekteki diğer donanımı da kapsa: ayna yazılı bilek kontrol listesi (cuff checklist), göğüs modülündeki ters basılmış etiketleri okumak için kullanılan bilek aynası ve bileğe takılan gösterge-sayaç türleri. İşlevi belgele: EVA'da saat gerçekte neyi zamanlar (yörünge gündoğumu-günbatımı döngüsü, oksijen ve görev süresi takibi) ve mürettebat kalan süreyi hangi göstergeden, hangi aralıklarla okur. Görsel düzeyde her saat tipi için kadran rengi ve deseni, kasa çapı, kayış malzemesi ve hangi bileğe takıldığını ver; orta ve uzak kamera ölçeğinde saatin hangi özelliği (kadran kontrastı, kayış rengi, boyut) hâlâ okunur, ayır. Kısıtlar: marka adı telif nedeniyle prompta yazılamaz, bu yüzden her modelin jenerik ama karakteristik İngilizce tanımını üret; ayrıca durmuş saat gibi anlatı yükü taşıyan varyantların gerçek karşılıklarını (mekanik ve elektronik saatlerin vakumda, aşırı sıcaklık farkında ve darbede durma nedenleri) açıkla. Çıktıyı üç parça ver: model→jenerik İngilizce tanım eşleme tablosu, sol-sağ bilek yerleşim şeması (saat, kontrol listesi, ayna, gösterge üst üste nasıl dizilir) ve öğe başına tek satırlık İngilizce prompt ifadesi.
```

---

# 4️⃣ HAVA/YAŞAM DESTEK ÜNİTESİ VE GÖĞÜS MODÜLÜ

```
EVA giysisinin yaşam destek donanımının DIŞTAN GÖRÜNÜR anatomisini çıkar: NASA EMU'nun sırt ünitesi (PLSS) boyutları ve silueti, yedek oksijen paketi, göğüsteki kontrol modülünün (DCM) düğme-gösterge düzeni, renk kodlu bağlantı soketleri, hortum güzergâhları, kask lambaları ve kamerası ile SAFER acil itki paketi. Karşılaştırmalı sök: Rus Orlan'ın sırttan kapılı tek parça tasarımı, Artemis xEMU'nun farkları ve Sokol tipi kabin-içi giysinin hortum-bağımlı yapısı — her siluetin hangi hikâye durumuna (uzun EVA, acil çıkış, kabin sahnesi) uyduğunu değerlendir. Sayısal göstergeleri belgele: oksijen basıncı ve kalan süre gerçek panellerde nasıl gösterilir (analog ibre, segmentli gösterge, rakam), uyarı renk ve ses konvansiyonları nedir, mürettebat hangi eşikte hangi alarmı duyar. Arıza görselliğini ayrıca çıkar: düşük oksijen, karbondioksit birikimi ve soğutma arızası dış kameradan nasıl görünür (vizör buğusu, kırağı, buhar jeti, yanıp sönen uyarı ışığı) — Gemini 4 vizör buğusu ve Parmitano'nun kaskında su birikmesi gibi belgelenmiş vakaları kullan. Kritik kısıt: AI video üretiminde sırt donanımı sahneden sahneye kayar, bu yüzden hangi öğelerin büyük, geometrik ve SAYILABİLİR olduğu için devamlılık çapası olarak güvenilir, hangilerinin (ince hortum ağı, küçük etiketler) kayma riski taşıdığını önceliklendirilmiş liste hâlinde ver. Çıktıyı tablo olarak ver: dıştan görünür her modül için konum, boyut, renk, işlev ve tek satırlık İngilizce prompt ifadesi, artı iki-üç karakteri yalnız sırt siluetiyle ayırt ettirecek varyant önerileri.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TUR5_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil).
2. 04_ARASTIRMA_BULGULARI.md'ye tur bölümü açılır ve İKİ liste yazılır:
   GİRDİ (hangi bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
3. ⛔ Raporlar ÇAPRAZ OKUNUR: aynı donanımın iki raporda geçen her
   sayısı yan yana konur; tutmayan sayı kılavuza İNMEZ.
4. Ancak ondan sonra kılavuz düzenlenir. Tarihsel ÖLÇÜ ile raporun kendi
   TASARIM ÖNERİSİ kılavuzda ayrı etiket taşır; kaynaksız satır girmez.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir ve
bu turun kaynakları ağırlıkla ansiklopedik/ikincildir (müze, arşiv,
meraklı siteleri) — hakemli değil. Tarihsel donanım görselliği için bu
kabul edilebilir bir taban; **sayısal iddialar bağlayıcı değildir.**
Kılavuza inen hiçbir çapa henüz üretimde test edilmedi; ilk uygulamada
① KARE ve ② DEVAMLILIK skorlarıyla sınanır.
