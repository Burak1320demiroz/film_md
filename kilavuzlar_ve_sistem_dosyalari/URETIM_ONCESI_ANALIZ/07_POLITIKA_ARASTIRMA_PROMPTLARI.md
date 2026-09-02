# 🔬 07 — POLİTİKA ARAŞTIRMA PROMPTLARI (TUR 3 girdisi · 01.09.2026)

> **Ne bu dosya:** dört motorun içerik politikası yüzeyini araştırmak için
> yazılmış dört derin araştırma promptu. Her biri **altı cümledir** ve
> **salt prompt** çalışır — kopyala, araştırma aracına yapıştır, başka
> hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz (KULE 7).
> Aynı prompt üç ay sonra yeniden koşulacak ve **aynı metin** koşulmalı;
> yoksa iki turun sonucu karşılaştırılamaz.

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md TUR 3 (süzme kaydı) →
         ancak oradan POLITIKA_VE_URETILEBILIRLIK_KILAVUZU / prompt_kontrol
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.
   Tur 1'de bu kayıt beş iddiayı elemişti (biri kendi raporuyla 35 puan
   çelişiyordu, biri içerik toplayıcıya dayanıyordu). Aynı elek koşulur.

⛔ SAYI KILAVUZA YAZILMAZ. Red sayıları tek yerde:
   FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md

⛔ BU ARAŞTIRMA FİLTRE ATLATMA ARAŞTIRMASI DEĞİLDİR.
   Aranan şey: yanlış-pozitifleri düşüren POLİTİKA UYUMLU TARİF kalitesi.
   Depo bunu iki kez ölçtü — sözlük temizlenince görüntü aynı kaldı ve
   kilit GÜÇLENDİ (SLOW STONE S4). Bir kaynak "filtreyi şöyle atlat"
   diyorsa o bulgu süzme kaydına "GİRMEDİ" olarak yazılır.
```

**Hangi prompt nereyi besler:**

| # | motor | besleyeceği yer |
|:--:|---|---|
| 1 | Nano Banana Pro | POLİTİKA §6 · §3 (kompozisyon ekseni — deponun tek kaydı var) |
| 2 | Nano Banana 2 | POLİTİKA §6 · defter §4② (motor farkı sorusu) |
| 3 | Veo | POLİTİKA §1 (mesaj tablosu) · §2 · defter §4③ (I2V↔T2V) |
| 4 | Osmi | POLİTİKA §6 · önce KİMLİK tespiti |

---

# 1️⃣ NANO BANANA PRO — görsel

```
Google'ın "Nano Banana Pro" olarak bilinen Gemini görsel üretim modelinin içerik
politikası yüzeyini araştır: hangi resmî belge hangi kategorileri yasaklıyor, bu
kategoriler API tarafında hangi parametrelerle (person generation, safety filter
level) kontrol ediliyor ve tüketici arayüzlerinde (Gemini uygulaması, Google Flow,
Whisk) bu parametreler kullanıcıya açık mı? Reddin kullanıcıya nasıl göründüğünü
topla — sessizce üretmeme, kısmi üretim, hata mesajı — ve bunların hangisinin
PROMPT reddi, hangisinin ÇIKTI reddi olduğunu ayır; mesajların birebir metnini ver.
Fotogerçekçi, tek insanlı, bilimkurgu ve uzay içerikli görsellerde bildirilmiş
YANLIŞ-POZİTİF vakalarını ara: yakın plan uzuv, yüzü kadraj dışında bırakan kadraj,
tepeden makro, koruyucu ekipman ve kısıtlanmış görünen duruş gibi masum tariflerin
hangileri reddedilmiş ve bunu kim raporlamış? Aynı görüntüyü geçiren yeniden yazım
kalıplarını topla — filtre atlatma tekniği olarak değil, POLİTİKA UYUMLU TARİF
kalitesi olarak: hangi somut cümle biçimleri (pozitif malzeme tarifi, nesne göreli
ölçek, yasak listesi yerine olumlu betimleme) red oranını düşürüyor? Her iddia için
kaynağı, tarihini ve türünü ayrı ayrı yaz — resmî belge, model kartı, sağlayıcı
blogu, geliştirici forumu, tek kullanıcı anekdotu — ve hiçbir sayıyı kaynağından
koparma. Sonunda iki liste ver: doğrulanabilir kaynağa dayanan bulgular, ve mekanik
olarak makul ama kaynaksız iddialar; ikincisini "hipotez" diye işaretle ve neden
doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ NANO BANANA 2 — görsel

```
"Nano Banana 2" adıyla bilinen Gemini görsel üretim modelinin resmî kimliğini
netleştir: hangi model ailesinin hangi sürümü, ne zaman yayınlandı, Nano Banana
Pro'dan hangi yönlerden ayrılıyor ve iki model aynı içerik politikasına mı tabi?
İki model arasında POLİTİKA DAVRANIŞI farkı bildiren bir kaynak var mı — aynı
promptun birinde geçip ötekinde reddedildiğini belgeleyen vaka, ya da sağlayıcının
açıkça "filtreler sıkılaştı veya gevşedi" dediği bir sürüm notu? Kullanıcı hangi
modelin isteği karşıladığını nasıl anlıyor: arayüzde model seçimi var mı, çıktı
meta verisinde (SynthID, C2PA, EXIF) model adı yazıyor mu ve bu bilgi bir red
günlüğü tutmaya yetecek kesinlikte mi? Modelin insan üretimi kısıtlarını ayrıntılandır
— çocuk görünümlü figür, gerçek kişi benzerliği, milliyet ve etnisite ifadeleri,
üniforma ve kurum sembolleri hangi eşiklerde reddediliyor, ve bu kısıtlar promptun
METNİNDEN mi yoksa üretilen GÖRÜNTÜDEN mi ölçülüyor? Her bulguyu kaynak, tarih ve
tür etiketiyle ver; sürüm numarası ya da tarih taşımayan hiçbir davranış iddiasını
kesin dille yazma. Kapanışta tek bir tablo çıkar: satırlar politika kategorisi,
sütunlar Nano Banana Pro ve Nano Banana 2, hücreler yalnız üç değerden biri —
"belgelenmiş", "bildirilmiş", "bilinmiyor".
```

---

# 3️⃣ VEO — video  ⭐ deponun açık sorusu burada

```
Google Veo'nun (3.x sürümleri; Gemini uygulaması ve Google Flow üzerinden) video
üretimindeki içerik politikası yüzeyini araştır: resmî yasak kategorileri, person
generation ayarları, gerçek kişi ve ünlü benzerliği kuralları, ve bunların bölgeye,
hesap tipine veya abonelik kademesine göre değişip değişmediği. Red mesajlarının
birebir metinlerini topla ve sınıflandır: "I can't generate that video", "I can't
make videos that could relate to dangerous situations", "I'm having a hard time
fulfilling your request", "I encountered an error" gibi ifadelerden hangisi içerik
politikası reddi, hangisi istem sınıflandırıcısı reddi, hangisi teknik hata? En
kritik soru şu ve ayrı bir bölüm hak ediyor: aynı sahnenin metinden-videoya (T2V)
ve görselden-videoya (I2V, başlangıç karesi verilerek) üretiminde red oranı farklı
mı, başlangıç karesi vermek politika denetimini değiştiriyor mu, ve bu konuda
ölçüm ya da geliştirici raporu var mı? Video tarafına özgü tetikleyicileri
ayrıntılandır: şiddet ima eden fiiller, düşme-çarpma-patlama sözcükleri, diyalog
ve dudak senkronu talebi, ses üretimi, kalabalık sahneler, ve süre ile çözünürlüğün
redle ilişkisi. Promptun uzunluğunun, yapısının (etiketli bloklar, uzun negatif
listeler) ve dilinin reddi etkilediğini bildiren kaynak var mı — özellikle
"yokluk listesi" biçiminde yazılmış negatif blokların istem reddine yol açtığına
dair? Her bulguya kaynak, tarih ve tür etiketi koy, ölçülmüş oran veren hiçbir
sayıyı örneklem büyüklüğü olmadan aktarma, ve sonucu "doğrulanmış / bildirilmiş /
bilinmiyor" üçlü ayrımıyla özetle.
```

---

# 4️⃣ OSMI — Flow'un ikinci video modeli  ⛔ önce KİMLİK

```
Google Flow içinde Veo'nun yanında sunulan ikinci video üretim modelinin resmî
kimliğini tespit et: kullanıcıların "Osmi" dediği bu seçenek hangi resmî model
adına karşılık geliyor, arayüzde hangi adla görünüyor, ne zaman eklendi ve hangi
model ailesinden geliyor? Kimlik netleştikten sonra bu modelin içerik politikasının
Veo'nunkinden ayrılıp ayrılmadığını araştır: aynı Google politika belgesine mi tabi,
ayrı bir model kartı var mı, ve red mesajları Veo'nunkiyle birebir aynı metinleri
mi veriyor? Modelin üretim karakterini ve kısıtlarını topla — klip süresi, çözünürlük,
ses üretimi, görselden-videoya desteği, insan üretimi kuralları — ve hangi sahne
tiplerinde Veo'dan daha kısıtlı ya da daha serbest olduğunun bildirildiğini yaz.
Aynı promptun iki modelde farklı sonuç verdiğini belgeleyen bir karşılaştırma var
mı, özellikle politika reddi ekseninde birinde geçip ötekinde reddedilen vaka
raporları? Bu modelle üretilen içeriğin işaretlenmesi (SynthID, C2PA, görünür
filigran) ve kullanım hakları Veo'dan farklı mı — bu fark yalnız üretimi değil
yayın tarafını da bağlar. Eğer "Osmi" adına karşılık gelen resmî bir model
bulamazsan bunu açıkça yaz, en yakın üç adayı gerekçeleriyle sırala, ve kesinlikle
uydurma bir model adı üretme.
```

---

# 🧾 TUR 3 SÜZME KAYDI — dört koşu bittiğinde doldurulacak

`04_ARASTIRMA_BULGULARI.md`'ye şu başlıkla eklenir: **TUR 3 — POLİTİKA YÜZEYİ**

```
T3.1 DÖRT SORU, DÖRT HÜKÜM
     ① Motorların politika yüzeyi farklı mı?          ⬜
     ② I2V, T2V'den daha az mı reddediliyor?          ⬜  ← defter §4③
     ③ Deponun mesaj sınıflandırması doğru mu?        ⬜  ← POLİTİKA §1
     ④ Sözlüğümüzde eksik/yanlış tetikleyici var mı?  ⬜  ← POLITIKA_T1/T2

T3.2 DEPOYA GİRMEYENLER — dürüst kayıt (bulgu | neden girmedi)
T3.3 BULGU → HANGİ DOSYA (bulgu | işlendiği yer | tip: ⭐yeni ✅düzeltme ⚠️hipotez)
T3.4 AÇIK KALAN ÇELİŞKİLER — karar proje sahibinde
```

⛔ **Bir bulgunun kılavuza girmesi için kapı:** kaynağı resmî belge ya da
birden çok bağımsız rapor olacak. Tek anekdot **hipotez** etiketiyle girer
ve kural olarak yazılmaz — Tur 1'in "%130 CR" vakası bu kapıdan döndü.

⚠️ **Ve eşik sayıları dışarıdan gelmez.** Hiçbir resmî belge "kaç tetikleyici
redde yol açar" demiyor; o sayı yalnız `09_URETIM_RED_DEFTERI`'nden çıkar.
Araştırma KATEGORİ verir, defter EŞİK verir.
