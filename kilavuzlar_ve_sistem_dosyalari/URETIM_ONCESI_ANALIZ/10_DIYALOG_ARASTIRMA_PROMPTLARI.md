# 🔬 10 — DİYALOG ARAŞTIRMA PROMPTLARI (TUR 6 girdisi · 03.09.2026)

> **KOŞU KAYDI:** dört prompt 03.09.2026'da koşuldu → dört rapor geldi.
> Ham: `TUR6_HAM_RAPORLAR/` · süzme: `04_ARASTIRMA_BULGULARI.md` §TUR 6 ·
> indiği yerler: `../PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md` (yeni
> kapı) + `../SES_VE_DIYALOG_URETIM_KILAVUZU.md` §2a +
> `../FILM_KLASOR_SABLONU/FILM_PLAN.md` (replik tablosu + B5 bloğu).
>
> **Ne bu dosya:** diyalog tarafını araştırmak için yazılmış dört derin
> araştırma promptu. Her biri **altı cümledir** ve **salt prompt** çalışır —
> kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacak ve **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz. (07/08/09'un gerekçesiyle aynı.)
>
> **Neden ŞİMDİ:** sahip kararı (03.09.2026) — filmlere hikâyeyle uyumlu,
> **tamamen İngilizce, planlı diyalog** istendi. `SES_VE_DIYALOG_URETIM`
> yazıldı ve hiç kullanılmadı (replikli üretilmiş film yok); TUR 4'ün
> 3 numaralı promptu repliğin VARLIĞINI ve YERİNİ araştırdı (kaç replik,
> hangi saniyede, ağız ekranda mı). Bu tur repliğin **İÇERİĞİNİ ve
> ÖLÇÜMÜNÜ** araştırır: iyi replik neyle ayrışır, hikâyeye nasıl bağlanır,
> doğal İngilizce nasıl yazılır, eleştiren hakem nasıl güvenilir kılınır.
> Çıktısı `PROMPT_KONTROL/`'e kurulacak **DIALOGUE_CRITIQUE rubriğini**
> besleyecek — ⛔ rubrik bu tur süzülmeden YAZILMAZ.

```
⛔ ÇIKTI DOĞRUDAN RUBRİĞE/KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md TUR 6 (süzme kaydı) →
         ancak oradan DIALOGUE_CRITIQUE rubriğine ve SES_VE_DIYALOG'a.
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "İYİ DİYALOG ÖRNEKLERİ" DERLEMESİ DEĞİLDİR.
   Aranan şey alıntı değil MEKANİZMA ve ÖLÇÜT: bir repliğin neden
   çalıştığının açıklaması ve çalışmayanı yakalayan test. Bir kaynak
   "şöyle yazın" diyor ama neden/nasıl ölçüldüğünü söylemiyorsa,
   bulgu süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI KILAVUZA YAZILMAZ, ÖNCE SÜZME KAYDINA YAZILIR.
   (Tur 1'in dersi: aynı sayı üç mekanizmaya iliştirilmişti ve tek
   kaynağın yankısıydı. Mekanizma alınır, sayı elenebilir.)

⛔ DEPONUN KENDİ KURALLARI PROMPTLARA YAZILMAZ.
   D35/D82 gibi mevcut kurallar sorulara gömülmez — model onaylamaya
   çalışır. Sınanacak kural tarafsız soru olarak sorulur (3 numaralı
   promptta "sayı taşıyan replik insana mı makineye mi veriliyor"
   böyle sorulmuştur). Deponun ölçülmüş diyalog verisi SIFIRDIR ve
   promptlara "bizde şöyle" cümlesi eklenmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Replik kalitesi ölçütleri** | "İyi replik" depoda tanımsız — eleştiri rubriğinin kategorileri ve eşikleri yok | `PROMPT_KONTROL/DIALOGUE_CRITIQUE` (kurulacak) · `SES_VE_DIYALOG` §7 |
| 2 | **Alt metin ve bilgi yükü** | B5 omurgası (İSTEK/ENGEL/BEDEL/MUHATAP) ile replik arasındaki bağın mekanizması yazılı değil | `SES_VE_DIYALOG` · `03_PLAN_ONCESI` B5 çaprazı · `TEMA_MUHENDISLIGI` §6 |
| 3 | **Konuşma İngilizcesi + telsiz söz dağarcığı** | Register haritası HUMAN/MACHINE'i ayırıyor ama SÖZCÜK düzeyinde ne yazılacağını söylemiyor; "doğal İngilizce" hiç tanımlanmadı | `SES_VE_DIYALOG` §1/§3 · `VEO` kılavuzu §3-4 |
| 4 | **Hakem güvenilirliği** | Kural ⑥: aynı rubrik aynı filme 2 puana kadar oynadı — diyalog gibi öznel eksende eleştiri nasıl çapalanır? | DIALOGUE_CRITIQUE çıktı formatı · çapa örnekleri · koşu protokolü |

> ⚠️ **1 ile 4 birbirini denetler:** 1 ölçüt listesi getirir, 4 o ölçütlerde
> hakemlerin uyuşup uyuşmadığını. 1'in getirdiği bir ölçüt 4'te "uyuşma yok"
> çıkıyorsa rubriğe ancak çapa örneğiyle girer, sayısız girmez.
> **2 ile 3 kesişir:** 2 alt metin ve az bilgi ister, 3'ün telsiz registerı
> kısalık dayatır. Çelişki çıkarsa süzme kaydına çelişki olarak yazılır ve
> hiçbiri kılavuza inmez.

---

# 1️⃣ REPLİK KALİTESİ ÖLÇÜTLERİ — profesyoneller diyaloğu neyle puanlıyor

```
Profesyonel senaryo değerlendirme pratiğinde — stüdyo script coverage formları,
senaryo yarışmalarının jüri kılavuzları, senaryo danışmanlarının yayınlanmış
ölçütleri — DİYALOG kalitesinin hangi adlandırılmış ölçütlerle değerlendirildiğini
araştır ve her ölçütün tam tanımını, varsa puanlama ölçeğini ve hangi kurumdan
geldiğini ayrı ayrı yaz. "On-the-nose" (duyguyu ya da niyeti doğrudan söyleyen
replik) kusurunun kanonik tanımını, bu kusuru yakalamak için önerilmiş somut
testleri (repliği silince sahnenin ne kaybettiği testi, duygu adlandıran kelime
taraması gibi) ve bu testlerin herhangi bir yerde sistematik uygulanıp
uygulanmadığını bul. Ödüllü ya da kanonik kabul edilen filmlerin senaryoları
üzerinde yapılmış korpus analizleri var mı — replik başına kelime sayısı, konuşma
sırası uzunluğu, sahne başına replik sayısı, karakterler arası söz dağılımı gibi
SAYISAL dağılımlar çıkarılmış mı, ve övülen diyalogla eleştirilen diyalog bu
sayılarda gerçekten ayrışıyor mu? Masabaşı okuma (table read) ve sesli okuma
pratiğinin diyalog revizyonunda ne yakaladığı belgelenmiş mi — yazıda geçen ama
sesli okununca düşen replik tiplerinin bir sınıflandırması var mı, ve bu pratik
yalnız metin üzerinde çalışan bir değerlendirmeciye hangi vekil testlerle
taşınabilir? Her iddia için kaynağı, tarihini ve türünü ayrı ayrı yaz — hakemli
çalışma, senaryo kuramı kitabı, stüdyo veya yarışma kılavuzu, senaryo danışmanı
yayını, yönetmen/yazar söyleşisi, eleştiri yazısı — ve hiçbir sayıyı kaynağından
koparma. Sonunda iki liste ver: doğrulanabilir kaynağa dayanan bulgular, ve
mekanik olarak makul ama kaynaksız iddialar; ikincisini "hipotez" diye işaretle
ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ ALT METİN VE BİLGİ YÜKÜ — replik hikâyeye nasıl bağlanır

```
Alt metnin (karakterin söylediği ile istediğinin ayrışması) izleyici tarafından
nasıl çıkarımlandığını araştır: hangi anlatı koşulları kurulduğunda izleyici
söylenmeyeni okuyor, ve alt metinli sahnelerle düz anlamlı sahneleri izleyici
tepkisi (hatırlama, duygusal tepki, göz izleme ya da nörolojik ölçüm) açısından
karşılaştıran herhangi bir çalışma var mı? Sinema ve dizi yazımında bilgi
aktarımı (exposition) yönetiminin adlandırılmış teknikleri neler — bilginin
çatışmanın içine gömülmesi, dikkat çeken bir eylemle aynı anda verilmesi,
bilginin saklanıp doğru anda silah gibi kullanılması — ve bu tekniklerin
izleyicinin bilgi yükü algısını değiştirdiğini gösteren ölçüm yapılmış mı?
Bir repliğin taşıdığı YENİ bilgi miktarı üzerine ne yazılmış: "replik başına tek
yeni bilgi" gibi pratik kurallar hangi kaynaktan geliyor, hiç ölçüldü mü, ve
söylenen bilginin görsel kanalda aynı anda tekrarlanması (söyleneni ekranda da
göstermek) izleyicide pekiştirme mi bıkkınlık mı üretiyor? Karakterin sözü ile
eylemi çeliştiğinde (yalan, inkâr, kendini kandırma) izleyici bağlanmasının
değiştiğini gösteren veri var mı, ve izleyicinin karakterden fazla bildiği
sahnelerde (dramatik ironi) replik yazımının nasıl değiştiği kuramsal ya da
ampirik bir kaynakta işlenmiş mi? Her iddia için kaynağı, tarihini ve türünü
ayrı ayrı yaz — hakemli çalışma, senaryo kuramı kitabı, anlatıbilim/psikoloji
literatürü, yönetmen/yazar söyleşisi, eleştiri yazısı — ve hiçbir sayıyı
kaynağından koparma. Sonunda iki liste ver: doğrulanabilir kaynağa dayanan
bulgular, ve mekanik olarak makul ama kaynaksız iddialar; ikincisini "hipotez"
diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ KONUŞMA İNGİLİZCESİ VE TELSİZ SÖZ DAĞARCIĞI — replikler hangi dille yazılır

```
Doğal konuşma İngilizcesini yazı İngilizcesinden ayıran, korpus çalışmalarıyla
belgelenmiş özellikleri topla — kısaltma (contraction) oranı, ortalama söz
uzunluğu, yarım bırakılan cümle oranı, kelime sıklığı profili — ve ana dili
İngilizce olmayan yazarların İngilizce diyalog yazarken en sık ürettiği "çeviri
kokusu" kalıplarının adlandırılmış bir listesi ya da çalışması var mı? Gerçek
uzay görevi telsiz konuşmalarının (görev kontrol kayıtları, uçuş transkriptleri)
dilsel yapısını araştır: ortalama söz kaç kelime, hangi standart kısalık kodları
ve okuma-geri okuma (readback) düzeni kullanılıyor, duygu bu registera hangi
anlarda ve nasıl sızıyor, ve bu gerçek konuşmalar kurmaca uzay filmlerindeki
telsiz diyaloglarından ölçülebilir olarak nasıl ayrışıyor? Kurmacada makine ve
bilgisayar sesi yazımının konvansiyonları neler — sentetik ses insan sesinden
SÖZCÜK SEÇİMİ ve SÖZDİZİMİ düzeyinde nasıl ayrıştırılıyor, hangi kalıplar
izleyicide "bu bir makine" okuması üretiyor — ve sayı, birim ya da zaman bilgisi
taşıyan replikler yerleşik pratikte insana mı makineye mi veriliyor? Yapay zekâ
ses üretiminde (metin-konuşma sistemleri ve konuşma üreten video modelleri)
yazılı metnin hangi özelliklerinin çıktı doğallığını ölçülebilir biçimde
etkilediğini araştır: noktalama, cümle uzunluğu, sayının rakamla ya da yazıyla
yazılması, ünlem ve duraklama işaretleri prosodiyi nasıl değiştiriyor ve hangi
yazım tercihi dinleyicide sentetik damga üretiyor? Her iddia için kaynağı,
tarihini ve türünü ayrı ayrı yaz — hakemli korpus/dilbilim çalışması, görev
transkripti veya arşiv, ses/post-prodüksiyon sektör kaynağı, model sağlayıcı
dokümantasyonu, eleştiri — ve hiçbir sayıyı kaynağından koparma. Sonunda iki
liste ver: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama
kaynaksız iddialar; ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını
tek cümleyle yaz.
```

---

# 4️⃣ HAKEM GÜVENİLİRLİĞİ — diyaloğu eleştiren aletin kendisi

```
Yaratıcı metinleri (senaryo, diyalog, kurmaca) değerlendiren İNSAN hakemlerin
kendi aralarındaki tutarlılığını ölçen çalışmaları topla: senaryo yarışmalarında
ve benzeri değerlendirmelerde hakemler arası güvenilirlik (inter-rater
reliability) sayıları ne, ve diyalog gibi öznel eksenlerde uyuşma yapı ya da
format gibi eksenlere göre daha mı düşük? Büyük dil modellerinin metin kalitesi
hakemi olarak kullanıldığı durumlarda belgelenmiş sistematik yanlılıkları
araştır — uzunluk/ayrıntı yanlılığı, konum yanlılığı, kendi üslubuna benzeyeni
yüksek puanlama, üslubu içeriğe tercih etme, aynı metne iki koşuda farklı puan
verme — ve her yanlılığın ölçülmüş büyüklüğünü ayrı ayrı yaz. Bu yanlılıkları
azaltmak için sınanmış yöntemlerden hangileri ne kadar işe yaradı: çapa örnekli
rubrik, mutlak puan yerine ikili karşılaştırma, birden çok koşunun ortalaması,
gerekçeyi puandan önce yazdırmak, kör yeniden koşu — her yöntemin hangi koşulda
ne kadar iyileştirme sağladığını sayıyla ver. Diyalog ya da senaryo
değerlendirmesi için maddeleri ve ölçekleri açık, yayınlanmış bir değerlendirme
aracı var mı — varsa maddelerini aynen aktar, güvenilirlik ya da geçerlilik
ölçümü yapılmış mı, ve otomatik değerlendirmeyle insan değerlendirmesinin en çok
ayrıştığı madde hangisi? Her iddia için kaynağı, tarihini ve türünü ayrı ayrı
yaz — hakemli çalışma, ölçme-değerlendirme literatürü, model sağlayıcı teknik
raporu, yarışma/kurum kılavuzu, ikincil derleme — ve hiçbir sayıyı kaynağından
koparma. Sonunda iki liste ver: doğrulanabilir kaynağa dayanan bulgular, ve
mekanik olarak makul ama kaynaksız iddialar; ikincisini "hipotez" diye işaretle
ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır (düzeltilmez, kısaltılmaz).
2. 04_ARASTIRMA_BULGULARI.md'ye TUR 6 bölümü açılır ve İKİ liste yazılır:
   GİRDİ (hangi bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
3. ⛔ 1 ile 4 ve 2 ile 3 numaralı raporlar ÇAPRAZ OKUNUR.
   1'in ölçütü 4'te "hakemler uyuşmuyor" çıkıyorsa rubriğe ancak çapa
   örneğiyle iner; 2'nin alt metin talebi 3'ün telsiz kısalığıyla
   çelişiyorsa ikisi de inmez, çelişki kayda geçer.
4. Ancak ondan sonra PROMPT_KONTROL/DIALOGUE_CRITIQUE rubriği yazılır ve
   SES_VE_DIYALOG_URETIM güncellenir. Rubriğe inen her ölçütün yanında
   kaynağı durur; kaynaksız ölçüt inmez.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Depoda replikli üretilmiş film yok; bu turdan çıkacak her şey, ilk
replikli üretim ve ilk gerçek yayında yeniden sınanacak bir hipotezdir.
İç ölçüm tarafı ayrı ve daha ucuzdur: `PROB_KOSUSU.md` PROB B (ekranda
tek replik) — merdivenin 3. basamağı o koşulmadan açılmaz.
