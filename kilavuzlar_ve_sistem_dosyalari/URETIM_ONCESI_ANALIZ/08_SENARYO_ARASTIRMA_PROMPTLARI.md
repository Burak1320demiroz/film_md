# 🔬 08 — SENARYO ARAŞTIRMA PROMPTLARI (TUR 4 girdisi · 02.09.2026)

> **Ne bu dosya:** hikâye tarafını araştırmak için yazılmış dört derin
> araştırma promptu. Her biri **altı cümledir** ve **salt prompt** çalışır —
> kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> üç ay sonra yeniden koşulacak ve **aynı metin** koşulmalı; yoksa iki
> turun sonucu karşılaştırılamaz. (07'nin gerekçesiyle aynı.)
>
> **Neden ŞİMDİ:** `06_HIKAYE_HATTI_TESHISI.md` deponun hikâye arızasını
> ölçtü ve çözüm maddelerini kapıya indirdi — ama §5'in dürüst kaydı
> duruyor: **maddelerin hiçbiri denenmedi ve depoda tek bir gerçek
> izlenme eğrisi yok.** Bu dört prompt o boşluğun DIŞ bilgi tarafını
> doldurur; iç tarafını `PROB_KOSUSU.md`'nin iki probu dolduracak.

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md TUR 4 (süzme kaydı) →
         ancak oradan ilgili kılavuza.
   Süzme kaydı iki liste tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.
   Tur 1'de bu elek beş iddiayı elemişti — biri kendi raporuyla 35 puan
   çelişiyordu, biri içerik toplayıcıya dayanıyordu. AYNI ELEK KOŞULUR.

⛔ BU ARAŞTIRMA "NASIL VİRAL OLUNUR" ARAŞTIRMASI DEĞİLDİR.
   Aranan şey taktik değil MEKANİZMA: bir anın ya da bir kararın neden
   işe yaradığının açıklaması. Bir kaynak "şu formülü uygula" diyor ama
   mekanizmayı söylemiyorsa, bulgu süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI KILAVUZA YAZILMAZ, ÖNCE SÜZME KAYDINA YAZILIR.
   Tur 1'in en pahalı dersi: aynı "+%85" üç ayrı mekanizmaya iliştirilmişti
   ve tek kaynağın yankısıydı. Mekanizmalar alındı, sayı alınmadı.

⛔ DEPONUN KENDİ VERİSİ SIFIRDIR VE BU PROMPTLARA YAZILMAZ.
   Yayınlanmış film sayısı 0 (08_YAYIN_PERFORMANS_TABLOSU). Araştırma
   deponun hipotezini doğrulamak için değil, hipotezi SINAMAK için
   koşuluyor. Prompta "bizim serimizde şöyle" cümlesi eklenmez —
   eklenirse model onaylamaya çalışır.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Çıkarılabilir an** | Planlarda `⭐VİRAL #1-4` işaretli sahneler var ve neyin viral yaptığı **hiç ölçülmedi** | `SENARYO_VE_VIRAL_KAMERA` §2 · `FRAGMAN` · `PAKETLEME_VE_VAAT` |
| 2 | **İstek ve hasım, sözsüz** | `06` §4①: HASIM satırı yeni kondu, **kanıtı yok** — ORTAM'ın hasım olamayacağı bir OKUMADIR | `06` §4① · `KARAKTER_VE_DUYGU` · `03_PLAN_ONCESI` B5 |
| 3 | **Az replikli senaryo** | `06` §4b: diyalog merdiveni kuruldu, **basamakların hiçbiri ölçülmedi** | `SES_VE_DIYALOG_URETIM` · `02_RISK_KARTLARI` KART 7 |
| 4 | **Uzay kısa film rakip seti** | `ONERME_VE_NOVUM` §1: İLİŞKİ satırının thumb-stop sütunu ⬜ **BOŞ** | `ONERME_VE_NOVUM` §1 · `SERI_VE_KANAL_STRATEJI` |

> ⚠️ **2 ve 4 birbirini denetler.** 2 mekanizmayı sorar ("nasıl kuruluyor"),
> 4 dağılımı sorar ("hangisi tutuyor"). İkisi çelişirse süzme kaydına
> **çelişki olarak** yazılır ve hiçbiri kılavuza inmez — Tur 1'de tek
> raporun kendi içindeki 35 puanlık çelişki bu yüzden yakalandı.

---

# 1️⃣ ÇIKARILABİLİR AN — bir filmin tek sahnesinin tek başına dolaşması

```
Uzun bir filmden ya da diziden koparılıp tek başına dolaşan iki ile beş saniyelik
anların hangi ortak yapısal özellikleri taşıdığını araştır: belgelenmiş vakalarda o
an eserin hangi dakikasındaydı, koparıldığında yanına hiçbir bağlam almadan mı
yayıldı, ve anı tek başına anlaşılır kılan şey tek bir nesnenin durum değiştirmesi
mi, bir yüz ifadesi mi, ölçek şoku mu, yoksa bir beklenti ihlali mi? "Çıkarılabilirlik"
üzerine akademik, platform kaynaklı ya da stüdyo kaynaklı herhangi bir ölçüm var mı,
ve bu ölçümler bir anın koparılabilirliğini önceden kestirebilen bir özellik listesi
veriyor mu? Repliksiz ve sessiz anların konuşmalı anlara göre daha çok mu yoksa daha
az mı koparıldığını gösteren veri ara, ve bunu sesi kapalı izleme oranlarıyla birlikte
ver; ayrıca koparılan anın altına yazı eklenmesinin yayılmayı değiştirip
değiştirmediğini araştır. Bir anın yayılmasıyla kaynak esere dönüş arasındaki oranı
belgeleyen vaka var mı — klip çok yüksek izlenme alırken kaynağa dönen izleyici
yüzdesi ölçülmüş mü, ve ölçülmediyse bunu kim, hangi gerekçeyle ölçemediğini söylüyor?
Her iddia için kaynağı, tarihini ve türünü ayrı ayrı yaz — hakemli çalışma, platform
şeffaflık raporu, stüdyo veya dağıtımcı açıklaması, gazetecilik, içerik toplayıcı,
tek kullanıcı anekdotu — ve hiçbir sayıyı kaynağından koparma. Sonunda iki liste ver:
doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız
iddialar; ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ İSTEK VE HASIM — sözsüz anlatıda dramatik motor

```
Hiç replik kullanmayan ya da toplam beşten az replik kullanan kısa filmlerde bir
karakterin İSTEĞİNİN ve karşısındaki İRADENİN ilk kaç saniyede ve hangi kanaldan
kurulduğunu araştır: taşınan bir nesne mi, engellenmiş bir eylem mi, bakış yönü mü,
bir başkasının bıraktığı iz mi, yoksa karakterin reddettiği bir şey mi? Karşı gücün
bir doğa olayı ya da fiziksel koşul olduğu filmlerle karşı gücün bir insan ya da
irade sahibi bir varlık olduğu filmleri karşılaştıran herhangi bir ölçüm var mı —
izleyici tutundurması, duygusal tepki, hatırlanma ya da yeniden izlenme açısından
ikisi arasında belgelenmiş bir fark bulunuyor mu, yoksa bu ayrım yalnız senaryo
kuramında mı yaşıyor? Kadrajda hiç görünmeyen ikinci bir kişinin bir ses, bir iz, bir
eşya, bir kayıt ya da boş bırakılmış bir yer üzerinden hasım veya istek muhatabı
olarak kurulmasının kanonik teknikleri neler, hangi filmlerde bu teknik adlandırılmış
ve kısa formatta etkisi hiç ölçülmüş mü? Tek karakterli sessiz kısa filmlerin
izleyici ya da eleştirmen tarafından "hiçbir şey olmuyor" veya "umursamadım" biçiminde
eleştirildiği vakaları topla ve eleştirinin gerekçesini üçe ayır: karakterin isteği mi
yoktu, bedeli mi yoktu, yoksa isteğin muhatabı mı yoktu? Her iddia için kaynağı,
tarihini ve türünü ayrı ayrı yaz — hakemli çalışma, senaryo kuramı kitabı, festival
veya jüri raporu, yönetmen söyleşisi, eleştiri yazısı, izleyici yorumu — ve hiçbir
sayıyı kaynağından koparma. Sonunda iki liste ver: doğrulanabilir kaynağa dayanan
bulgular, ve mekanik olarak makul ama kaynaksız iddialar; ikincisini "hipotez" diye
işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ AZ REPLİKLİ SENARYO — tek repliğin yaptığı iş

```
Toplamda beşten az replik kullanan kısa filmlerde tek bir repliğin hangi işi yaptığını
araştır — bilgi mi veriyor, bir ilişki mi kuruyor, bir yalan mı söylüyor, bir isteği
mi dile getiriyor, yoksa yalnız sessizliği mi kırıyor — ve belgelenmiş vakalarda
repliğin filmin hangi yüzdesinde geldiğini, kaç saniye sürdüğünü ve öncesindeki
sessizliğin ne kadar olduğunu ver. İlk konuşulan repliğin zamanlamasının izleyici
tutundurmasına etkisini ölçen veri var mı, ve uzun bir sessizlikten sonra gelen ilk
insan sesinin izleyici davranışını değiştirdiğini gösteren platform ya da akademik bir
ölçüm bulunuyor mu? Kadraj dışı ses, telsiz, kayıt, anons ve makine sesi gibi konuşan
ağzı ekranda göstermeyen biçimlerin dramatik gücü ve sınırları üzerine ne yazılmış, bu
biçimler izleyicide bir tür konvansiyonu olarak mı yoksa bütçe kısıtının işareti olarak
mı okunuyor, ve ikisini ayıran şey nedir? Yapay zekâ ile üretilmiş videolarda konuşan
yüz içeren kliplerle konuşmanın kadraj dışında kaldığı kliplerin izleyici tarafından
algılanma farkını ölçen bir çalışma ya da yayıncı raporu var mı, ve "yapay zekâ yapımı"
algısı repliğin varlığıyla mı, dudak senkronu kalitesiyle mi, yoksa sesin tınısıyla mı
ilişkilendirilmiş? Her iddia için kaynağı, tarihini ve türünü ayrı ayrı yaz — hakemli
çalışma, platform raporu, ses veya post prodüksiyon sektör kaynağı, yönetmen söyleşisi,
eleştiri, izleyici yorumu — ve hiçbir sayıyı kaynağından koparma. Sonunda iki liste
ver: doğrulanabilir kaynağa dayanan bulgular, ve mekanik olarak makul ama kaynaksız
iddialar; ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 4️⃣ UZAY KISA FİLM — rakip set ve önerme tipi  ⭐ İLİŞKİ satırının boş sütunu burada

```
Son üç yılda çevrimiçi olarak en çok izlenen uzay ve bilimkurgu temalı kısa filmleri,
iki ile on dakika bandında ve varsa bunların dikey kısa video uyarlamalarıyla birlikte
topla; her biri için önermesini tek cümleyle yaz ve önermenin bir FİZİK VEYA ORTAM
KURALINA mı, yoksa İKİ İNSAN ARASINDAKİ BİR ŞEYE mi dayandığını açıkça işaretle. Bu iki
önerme tipinin izlenme, tamamlanma, paylaşılma ve yorum yoğunluğu açısından farklılaşıp
farklılaşmadığını gösteren veri var mı, yoksa fark yalnız yorumların içeriğinde mi
görünüyor, ve görünüyorsa yorumlar tam olarak ne diyor? Aynı kümede tekrar eden anlatı
kalıplarını çıkar: kaç tanesi bir keşifle, kaç tanesi bir kayıpla, kaç tanesi bir
kararla bitiyor, kaç tanesinde kadrajda birden fazla insan var, kaç tanesinde replik
var, ve bu özellikler ile paylaşılma arasında görünür bir ilişki bulunuyor mu? Bu
filmlerin izleyici yorumlarında en çok tekrar eden ŞİKÂYETİ ve en çok tekrar eden
ÖVGÜYÜ ayrı ayrı topla, ve özellikle "hiçbir şey olmuyor", "çok yavaş", "yapay zekâ
işi", "güzel ama boş" gibi kalıpların hangi film özellikleriyle birlikte göründüğünü
ara. Her iddia için kaynağı, tarihini ve türünü ayrı ayrı yaz — platform sayfasının
kendisi, festival veya yayıncı verisi, hakemli çalışma, sektör raporu, gazetecilik,
içerik toplayıcı, tek kullanıcı anekdotu — ve hiçbir izlenme sayısını kaynağından
koparma, ölçüldüğü tarihi de yaz. Sonunda iki liste ver: doğrulanabilir kaynağa
dayanan bulgular, ve mekanik olarak makul ama kaynaksız iddialar; ikincisini "hipotez"
diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır (düzeltilmez, kısaltılmaz).
2. 04_ARASTIRMA_BULGULARI.md'ye TUR 4 bölümü açılır ve İKİ liste yazılır:
   GİRDİ (hangi bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
3. ⛔ 2 ile 4 numaralı raporlar ÇAPRAZ OKUNUR. 2 "insan hasım daha güçlü"
   derken 4'ün dağılımı bunu göstermiyorsa, ikisi de kılavuza İNMEZ ve
   çelişki kayda geçer. Tek raporun kendi içinde çeliştiği vaka
   Tur 1'de yaşandı (35 puan) ve ancak çapraz okumayla yakalandı.
4. Ancak ondan sonra kılavuz düzenlenir. Kılavuza inen her satırın
   yanında kaynağı durur; kaynaksız satır girmez.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Dış bilgi bu serinin ölçümü değildir ve `04`'ün en önemli kaydı hâlâ
geçerli — **depoda yayınlanmış film sayısı sıfır.** Bu turdan çıkacak
her şey, ilk gerçek yayında yeniden sınanacak bir hipotezdir.
İç ölçüm tarafı ayrı ve daha ucuzdur: `PROB_KOSUSU.md` · iki klip.
