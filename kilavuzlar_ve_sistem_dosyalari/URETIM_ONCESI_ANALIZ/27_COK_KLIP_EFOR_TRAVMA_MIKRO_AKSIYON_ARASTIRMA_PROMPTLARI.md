# 🔬 27 — ÇOK KLİPLİ SAHNE · EFOR/YERÇEKİMİ · TRAVMA · MİKRO-AKSİYON · ALTI DERİN ARAŞTIRMA PROMPTU (22.09.2026)

> ✅ **KOŞULDU — 22.09.2026.** Ham: `TUR24_HAM_RAPORLAR/` (6 rapor) ·
> Süzgeç: `04_ARASTIRMA_BULGULARI.md` §TUR 24 · İndiği yer:
> `../COK_KLIPLI_SAHNE_KILAVUZU.md` §3.4-§3.6 · `../FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` ·
> `../POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md` · `../MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md`.
> ⭐ Turun ayırt edici yanı: altı raporun hiçbiri ÖLÇÜLMÜŞ etiketine bağlantı vermedi
> (`[cite: 5, 19]` biçiminde çıplak numaralar). TUR 22 sözleşmesi gereği **hiçbir
> satır ölçülmüş olarak inmedi**; dört rapor önerisi deponun kendi ölçümüyle çeliştiği
> için **reddedildi** (ayrıntı §TUR 24 ②).

> **Ne bu dosya:** 22.09.2026 ÇOK KLİPLİ SAHNE kararından (son kare zinciri kalktı)
> sonra açılan dört kılavuz için altı derin araştırma promptu. Sahip tarafından
> yazıldı ve dış araştırma aracında koşuldu; buraya **aynı metinle** arşivlendi ki
> tur yeniden koşulursa sonuçlar karşılaştırılabilsin (07-26'nın gerekçesi).
>
> | # | kılavuz (önerilen ad → deponun verdiği ad) | prompt |
> |:--:|---|---|
> | 1A | `COKLU_KLIP_SAHNE_KAPSAMA` → **`COK_KLIPLI_SAHNE_KILAVUZU`'na katıldı** (aynı konu, 22.09 kuruldu) | kapsama hiyerarşisi · kesme noktası · ses köprüsü · tempo |
> | 1B | aynı | sahne içi pozisyon ve mekân kilidi |
> | 2A | `FIZIKSEL_EFOR_VE_KAS_GERILIMI` → **`FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU`** (2B de içinde) | biyomekanik efor [D206] |
> | 2B | aynı | yerçekimi tutarlılığı ve çarpışma kinetiği [D200] |
> | 3 | **`POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU`** | travma merdiveni · hasar hafızası · kadro kilidi [D207] |
> | 4 | `MIKRO_AKSIYON_LIMITI_VE_HALUSINASYON` → **`MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU`** | mikro→makro eylem · yürüme platosu · filigran · anakronizm |

## ⚠️ Promptlardaki depo iddiaları — kayda karşı düzeltme (22.09.2026)

Promptların altındaki "Sınama Seti" satırları QA kayıtlarıyla karşılaştırıldı.
Sayıların çoğu doğru; üç düzeltme var:

| prompt | iddia | kayıttaki hâli |
|---|---|---|
| 1A | SLOW_RAIN "QA raporu: *Tempo Platosu 4.0/10*" | böyle bir puan YOK. ④ HİKAYE ⛔ TEKRAR (mod V · düzeltilmiş 5.0) "S17–S24 tempo platosu" · ⑫ HOOK 🚨 GEÇERSİZ "02:30–03:30 plateau" |
| 1B | SLOW_RAIN "② DEVAMLILIK 7.0/10 🔴 Blocker" | ② ⚠️ ŞARTLI 7.0; kızak bulgusu 🔴 Blocker (doğru) |
| 3 | "D42 Anti-Reset / Physical Amnesia" | **D42 = kir ve toz deseni sürüklenmesi.** Beden sıfırlanmasının dersi **D207**'dir (4 film). Hasar hafızası D42 + D84'e düşer |
| 2B · 3 · 4 | SLOW_RAIN fizik/oyunculuk bulguları | ⑥ ⛔ TEKRAR · ⑩ 🚨 GEÇERSİZ (mod V, T tablosuna girmez [D129 · D190]) — vaka olarak geçerli, SAYI olarak değil |

`THE_STOLEN_SKY` ⑧ EFOR 1.0/10 (PART 4) ve S13'te vurulan askerin S24'te hasarsız
dönmesi (PART 3 ② STRUCTURAL PROBLEM) kayıtta **birebir** var.

---

# 1️⃣ ÇOK KLİPLİ SAHNE İÇİN

### 🔬 PROMPT 1A: ÇOKLU KLİP SAHNE DİZİLİMİ VE KAMERA KAPSAMA HİYERARŞİSİ (Coverage & Shot Grammar)

```text
Güncel üretken video modellerinde (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling 1.5, Runway Gen-4 ve Sora) tek bir dramatik olayın (sahnenin), her biri bağımsız üretilen 10'ar saniyelik 3 ila 5 ardışık klibe (toplam 30-50 saniye) yayılarak sinematik kapsama (coverage) teknikleriyle bölünmesi mimarisini araştır: bir olayın 10 saniyede bitip yeni bir olaya zıplamasının yarattığı slayt gösterisi hissini kırmak için geniş (establishing), orta (action/interaction) ve yakın (detail/reaction) planların ardışık klipler arasında hangi hiyerarşiyle dizilmesi gerektiği, modellerin "aynı sahnenin farklı açısı" algısını koruyabilme kapasitesi, sahne içi ölçek atlama kuralları ve bu konuda yayımlanmış akademik/endüstriyel yönergeler; model, sürüm ve test bağlantılarıyla.
Mekanizmayı sök: modelin bir sahneyi baştan başlatmak (reset) yerine önceki klibin uzantısı olarak görmesini sağlayan prompt kalıpları, sahne içi kurgusal kesme (cut) anlarının hareketin neresine (eylem başlangıcı, eylem ortası, eylem sonucu) denk getirilmesinin görsel sürekliliği maksimize ettiği, izleyicinin 3 klip boyunca aynı zaman diliminde kaldığını hissettiren zamansal bağlaçlar ("meanwhile in the same second", "continuing the same breath") ve ölçek sıçramalarında (örn. genişten aşırı yakına) modelin karakter kimliğini veya arka plan coğrafyasını kaybetme eşikleri; tutan ve tutmayan yapılarla.
Akustik ve montaj sürekliliğini analiz et: ardışık 3 klipte görsel açı ve ölçek değişirken arka plan ambiyansının (oda tonu, rüzgar uğultusu, motor hum) ve ses efektlerinin (J-cut ve L-cut köprüleri) görsel sıçramaları maskeleme gücü, bağımsız üretilen kliplerde diyalogların tek klibe yığılması yerine 30 saniyelik sahneye (1. klip sessiz eylem, 2. klip tek net replik, 3. klip dinleme/reaksiyon) yayılmasının anlaşılırlığa etkisi.
Ritim ve tempo platosunu sorgula: 30-50 saniyelik çoklu klip sahnelerinin film geneline yerleştirilmesinde tekdüze 10'ar saniyelik klip metronomunun izleyicide yarattığı bilişsel yorgunluğu önlemek için sahne içindeki mikro-tempo değişimlerinin (eylem hızlanması, duraklama, nefes alma) prompt düzeyinde nasıl yönetilebileceği.
Kritik kısıt: kullanım yeri, her biri tam 10,000 saniye süren, kesmesiz tek plan olarak üretilen, varsayılan olarak sabit kameralı, tek İngilizce promptla çalışan fotogerçekçi uzay bilimkurgu klipleridir; klipler arası son kare zinciri (I2V frame chain) KULLANILMAMAKTADIR, her klip bağımsız text-to-video veya statik referans görseliyle üretilir ve kurgu masasında sert kesmeyle (hard cut) birleştirilir; karakter basınç giysili ve kasklıdır; VFX kompozit, 3B kamera eşleme ve ek kurgu efektleri YOKTUR, çözüm yalnız prompt dili, sahne kurgusu ve ses miksiyle sağlanmalıdır.
Çıktıyı üç tablo ve bir karar ağacı olarak ver: (a) 3-5 KLİP KAPSAMA ŞABLONU tablosu — sahne türü (keşif, kriz, tamir, yüzleşme), klip sayısı, her klibin kamera ölçeği/açısı, sahne içi dramatik görevi; (b) SAHNE İÇİ BAĞLAÇ tablosu — zaman/mekân tutarlılığı sağlayan İngilizce prompt cümle kalıpları, etki alanı, model uyumu; (c) KESME VE RİTİM tablosu — sahne içi geçiş tipi, eylem noktası (action match), beklenen hata ve çözümü; (d) KARAR AĞACI — "yazılacak sahnenin süresi > 10 saniye" girdisinden başlayıp kaç klip ve hangi açı diziliminin seçileceğini belirleyen akış; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ olsun ve kaynak bağlantıları eksiksiz verilsin.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_SLOW_RAIN` filminde S17–S24 arası tam 8 klip boyunca (80 saniye) aynı açıdan kızak çekme yürüyüşü üretildi (QA raporu: *Tempo Platosu 4.0/10*). Bu promptun cevabı, 80 saniyelik bir intikal eyleminin 3-4 farklı kapsama açısıyla (geniş zemin → kızak bağı detayı → vizör içi yorgunluk → ufuk hedefi) monotonlaşmadan nasıl yazılacağını açıklamalıdır.

### 🔬 PROMPT 1B: SAHNE İÇİ POZİSYON VE MEKÂN KİLİDİ (Intra-Scene Pose & Spatial Anchor)

```text
Üretken video yapay zeka modellerinde, son kare zinciri (I2V continuity) kullanılmaksızın bağımsız üretilen ve aynı 30 saniyelik sahnenin parçası olan ardışık 10 saniyelik klipler arasında karakterin mikromekanik pozisyonunu, el-ayak duruşunu ve mekânsal koordinatlarını koruma yöntemlerini araştır: Klip 1'in sonunda sol eliyle bir konsol kolunu tutarak bitiren karakterin, Klip 2 farklı bir kamera açısından başladığında kolu hiç tutmamış gibi odanın ortasında serbest durmasını engelleyen prompt mimarisi, "eylem ortası başlangıç" (mid-action initialization) başarımı ve modelin mekân içi çapalama kapasitesi; Veo, Omni, Kling ve Runway verileriyle.
Mekanizmayı sök: prompt metnine karakterin o anki statik pozisyonunu mutlak fiziksel koordinatlarla yazmanın ("character is already anchored with left hand gripping the latch, right foot braced 40 cm back") eylem fiiliyle yazmaya ("character grips the latch") kıyasla ilk 2 saniyedeki duruş sapmasını önleme oranı, modelin "already in progress" (zaten devam etmekte olan eylem) direktifine itaati, kamera açısı değiştiğinde (örn. 3/4 profilden karşı cepheye geçildiğinde) sağ/sol el simetrisinin ters yüz olmasını (mirroring artifact) engelleyen çapa cümleleri.
Mekânsal coğrafya ve prop sürekliliğini incele: sahne içindeki sabit nesnelerin (hava kilidi kapağı, alet çantası, sızdıran boru) ardışık kliplerde yer değiştirmesini, şekil değiştirmesini (kare kapaktan yuvarlak kapağa morflama) veya yok olmasını önleyen "sahne içi dünya çapası" (scene-level spatial anchor) formülleri; sahneye ait değişmez unsurların promptun pozitif bloğunda hangi sırada ve hangi kelime yoğunluğuyla yazılması gerektiği.
Açı sıçraması ve 180 derece kuralı entegrasyonu: sahne içi 3 klip arasında kamera ekseni değiştirilirken modelin mekân yönünü şaşırmasını (karakterin aniden ters yöne bakması, arka plan duvarının yer değiştirmesi) engelleyen ekran yönü (screen direction) kilitleri ve pusula/kadraj yönü ("facing screen-left throughout the scene") komutlarının etkinliği.
Kritik kısıt: kullanım yeri, her klip tam 10 saniye olan fotogerçekçi uzay bilimkurgu sahneleridir; klipler arası son kare referansı veya video-to-video beslemesi YOKTUR; karakter kapalı kasklı, uzay giysilidir; tüm mekânlar kurgusal uzay istasyonu, hava kilidi veya yabancı gezegen yüzeyidir; kompozitleme veya 3B ortam taraması yoktur; çözüm yalnızca İngilizce prompt gövdesi ve negatif prompt bloklarıyla elde edilmelidir.
Çıktıyı üç tablo olarak ver: (a) POZİSYON BAŞLANGIÇ KALIPLARI tablosu — eylem durumu (tutunma, çökme, alet kullanma, uzanma), Klip 2 başlangıç prompt şablonu, model itaat düzeyi, hata riski; (b) MEKÂNSAL ÇAPA SÖZLÜĞÜ tablosu — nesne tipi, yön/konum kilitleme cümlesi, aynalanmayı önleme formülü; (c) SAHNE İÇİ DEVAMLILIK KONTROL LİSTESİ — Klip 1'den Klip 2'ye geçerken kontrol edilecek 5 zorunlu parametre; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ formatında kaynaklarıyla sunulsun.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_SLOW_RAIN` S17'de yerde çekilen kızak, S20'de aniden astronotun sırtına monte edilmiş olarak belirdi; S22'de tekrar yere düştü (QA: *② DEVAMLILIK 7.0/10 🔴 Blocker*). Bu promptun cevabı, aynı sahnenin klipleri arasında eşyanın konumunun nasıl sabitleneceğini kesinleştirmelidir.

---

# 2️⃣ FİZİKSEL EFOR VE YERÇEKİMİ İÇİN

### 🔬 PROMPT 2A: BİYOMEKANİK KAS EFORU, TORK VE BEDENSEL DİRENÇ (Body Torque & Weighted Effort - D206)

```text
Yapay zeka video üretim modellerinde (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4 ve Sora) insan bedeninin mekanik dirence, ağır kütleye ve fiziksel efora karşı gösterdiği biyomekanik gerilimin üretilememesi sorununu (D206 "Nobody Pays / Weightless Work") araştır: tonlarca ağırlıktaki bir hava kilidi kolunu çeken veya ağır bir yükü sürükleyen karakterin sırtının eğilmemesi, bacaklarıyla zemine baskı uygulamaması (bracing), kolların kasılmaması, hareketin sıfır dirençle tereyağı gibi akması ve kalın basınçlı uzay eldivenlerinin çıplak el hassasiyetiyle hareket etmesi arızalarının nedenleri ve çözümleri; biyomekanik gerçekçilik değerlendirmeleri ve model sınırları.
Mekanizmayı sök: modelin bir eylemi "zahmetli ve ağır" üretmesini tetikleyen temel prompt unsurları nelerdir; sadece eylemi tarif etmenin ("pulls the lever") neden sıfır direnç ürettiği, buna karşılık karşıt kuvvet ve gövde torku tarif etmenin ("braces both boots against the metal frame, leans full body weight backward at a 45-degree angle, forearms trembling under isometric tension") fiziksel gerilimi ne kadar tetiklediği, hareket hızının promptta açıkça sınırlandırılmasının ("the frozen wheel rotates only two inches over eight seconds of sustained strain") efor hissine katkısı.
Eforun görsel ve fizyolojik kanıtlarını analiz et: yüzü tamamen kapalı olan kasklı astronotlarda eforun yalnızca gövde ve kıyafet üzerinden okunmasını sağlayan somut fiziksel işaretler; kask vizörünün iç yüzeyinde yoğunlaşan nefes buğusu (condensation fogging curve), göğüs kafesinin hızlı ve derin inip kalkması (hyperventilation/chest heave), aşırı gerilim altındaki parmak eklemlerinde ve tendonlarda mikro-titremeler (isometric tremors), kumaş ve dikiş hatlarındaki gerilme çizgileri; bu işaretlerin promptta yazım kalıpları.
Alet ve mekanizma direnci sözlüğü: donmuş valf, paslı çark, sıkışmış kızak ve ağır kapak gibi nesnelerin "direnç katsayısını" modele aktaran sıfat ve fiil öbekleri; nesnenin aniden açılmasını önleyen, "kademeli ve zorlu ilerleme" tanımları; modelin aşırı eforu ağır çekim (slow-motion) sanmasını engelleyen tempo koruma direktifleri.
Kritik kısıt: kullanım yeri, 10 saniyelik fotogerçekçi uzay bilimkurgu klipleridir; karakter kalın basınç eldivenli, ağır uzay giysilidir ve çoğu sahnede yüzü kaskın arkasında görünmez; filmlerde CGI parçacık simülasyonu, sonradan hız yavaşlatma/hızlandırma veya görsel efekt yoktur; tüm efor yalnızca tek bir İngilizce metin promptu ile modelin difüzyon katmanından doğal hareket olarak çıkarılmalıdır.
Çıktıyı üç tablo ve bir kılavuz kural seti olarak ver: (a) BİYOMEKANİK GERİLİM SÖZLÜĞÜ tablosu — eylem tipi (çekme, itme, kaldırma, çevirme), bedensel destek (ayak/bacak duruşu), gövde açısı ve prompt İngilizce tam kalıbı; (b) EFORUN TEK KARE KANITLARI tablosu — görsel kanıt (vizör buğusu, göğüs hareketi, titreme), uygulanabilirlik derecesi, kamera ölçeği, model uyumu; (c) DİRENÇLİ MEKANİZMA SÖZLÜĞÜ — donmuş/sıkışmış nesnelerin hareket kısıtını belirten İngilizce ifadeler ve kaçınılması gereken zayıf kelimeler; (d) D206 ÖNLEME KONTROL KURALLARI; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ formatında kaynaklarıyla sunulsun.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_STOLEN_SKY` filminde ⑧ EFOR merceği **1.0/10 ⛔** aldı (D206: *"Karakter kalın basınç eldiveniyle klavyede çıplak elle yazar gibi narin tuşlama yapıyor, ağır kargo kapağını çekerken sıfır kas gerilimi"*). Bu promptun çıktısı, kalın eldivenin hantallığını ve kapak çekerken vücut torkunu modele zorla çizdiren kalıpları vermelidir.

### 🔬 PROMPT 2B: YERÇEKİMİ TUTARLILIĞI, İVME VE ÇARPIŞMA KİNETİĞİ (Anti-Two Gravities - D200)

```text
Video üretim yapay zekalarında (Veo 3.1, Omni 1.1 Flash, Kling, Sora, Runway), bilimkurgu sahnelerinde yerçekimi ivmesinin (g) sahneler arasında veya aynı klip içinde 5 ila 10 kat dalgalanması sorununu (D200 "Two Gravities") ve kütlesiz çarpışma arızalarını araştır: bir klipte Ay yerçekiminde (0.16g) gibi yavaş süzülen bir nesnenin veya bedenin, kaza düşüşünde aniden Dünya yerçekiminde (1.0g) gibi sert çakılması, düşen ağır nesnelerin zeminde sıfır sarsıntı ve toz kaldırması, katı nesnelerin birbirine çarptığında kinetik momentum aktarmaksızın hayalet gibi durması veya çarpışma anında kütlesiz morflaması arızalarının nedenleri; video difüzyon modellerinde fizik sadakati kıyaslamaları.
Mekanizmayı sök: modelin yerçekimi hızını neye göre belirlediği (ortamın adı örn. "lunar/alien surface" mı, görsel arka plan mı, yoksa prompttaki hareket fiili mi), metne net sayısal fizik değeri yazmanın ("gravity is 0.38g, objects fall at 3.7 m/s²") modele etki edip etmediği, yoksa modelin hız algısını "fall speed", "descent rate", "terminal velocity" gibi kinematik niteleyicilerle mi kontrol ettiği; serbest düşüş ile süzülüş arasındaki ivme farkının promptta nasıl ayrıştırılacağı.
Kütle, çarpışma ve zemin etkileşimi: iki katı cisim (örn. kaza yapan astronot ve zemin, çarpışan iki araç veya kayaya çarpan kızak) temas ettiğinde modelin katı cisim geçişi (solid passing through solid) yapmasını engelleyen prompt komutları; çarpmanın büyüklüğünü kanıtlayan ikincil fiziksel unsurların (zeminden fırlayan donmuş toz, sekme açısı, savrulan kar kütlesi) ana çarpışma kinetiğini doğrulamadaki rolü.
Havada asılı kalma (hovering) ve serbest parçacık arızaları: yerçekimli bir ortamda sıvı damlalarının, tozların veya ekipmanların itkisiz şekilde havada düz çizgiler halinde asılı kalması (causeless floating) veya tersine yukarı doğru yükselmesi arızalarını engelleyen çevre fiziği kilitleri; atmosfer basıncı ve rüzgar direncinin yerçekimiyle tutarlı birleşik tarifleri.
Kritik kısıt: kullanım yeri, 10 saniyelik fotogerçekçi bilimkurgu filmleridir; filmlerde yerçekimi rejimleri bellidir (0g vakum, 0.38g kriyojenik yüzey, 1g istasyon içi); her sahne tek promptla üretilir; fizik motoru veya post-prodüksiyon simülasyonu YOKTUR; çözüm sadece prompt içi fiziksel çevre kuralları ve negatif prompt bloklarıyla elde edilmelidir.
Çıktıyı üç tablo olarak ver: (a) YERÇEKİMİ SEVİYESİ PROMPT FORMÜLLERİ tablosu — rejim (Mikro-g, Mars-g 0.38, Dünya-g 1.0), düşüş hızı tanımı, adım ve zıplama dinamiği, modelin itaat ettiği İngilizce tam kalıplar; (b) ÇARPIŞMA VE KÜTLE KİNETİĞİ tablosu — çarpma tipi (sert zemin çakılması, nesne çarpışması), kütlesizliği ve faz geçişini engelleyen darbe tarifleri; (c) ÇEVRESEL FİZİK KİLİTLERİ — havada asılı kalmayı ve yerçekimi dalgalanmasını önleyen negatif blok kelimeleri; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ formatında verilsin.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_SLOW_RAIN`'de pencereden inişte g = 0.49 m/s² ölçülürken, kaza düşüşünde g = 4.27 m/s² ölçüldü (8.7 kat yerçekimi zıplaması · QA: *⑥ FİZİK TWO GRAVITIES ⛔*). Bu promptun cevabı, aynı film boyunca yerçekimi düşüş hızının nasıl sabit bir oranda kilitleneceğini vermelidir.

---

# 3️⃣ POST-TRAVMA VE DURUM HAFIZASI İÇİN

### 🔬 PROMPT 3: POST-IMPACT TRAVMA MERDİVENİ, KOSTÜM HASARI VE ÖLÜM KALICILIĞI (Trauma Continuity & Anti-Reset - D42)

```text
Yapay zeka video üretim modellerinde (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4 ve Sora), bağımsız üretilen ardışık sahneler arasında karakterin travma durumunun, yaralanmasının, fiziksel acısının ve kıyafet hasarının bir sonraki klipte anında sıfırlanması arızasını (D42 "Anti-Reset / Physical Amnesia") ve ölen/vurulan karakterlerin sonraki sahnelerde arka planda hasarsız yeniden belirmesini araştır: şiddetli bir kaza, patlama veya darbe geçiren bir figürün bir sonraki klipte sanki hiçbir şey olmamış gibi nötr, dinlenmiş ve dimdik bir beden diliyle başlamasını engelleyen prompt ve süreklilik stratejileri; modellerin durum hafızası sınırları.
Post-Impact (Darbe Sonrası) toparlanma eğrisini modelle: sinematik dramaturjide ve gerçekçi fizikte sert bir travmadan sonraki ilk 30-40 saniyenin (3-4 bağımsız klip) aşamalı toparlanma kinetiği; Klip 1 (çarpma anı ve hareketsizlik), Klip 2 (şok, nefes darlığı, kalkamama, zeminde acıyla kıvranma), Klip 3 (kusurlu doğrulma, topallama, hasarlı uzvu göğse bastırma, ağırlık verememe); modelin bu aşamalı zayıflık ve acı durumunu prompt metninden ne kadar yansıtabildiği, hangi kelimelerin bedensel sakatlığı ve sendelemeyi güvenle ürettiği.
Kostüm ve ekipman hasarının kilitlenmesi: yırtılan basınç giysisi, çatlayan kask vizörü, göğüs plakasındaki yanık/çizik izleri, çamura/kaza sıvısına batmış botlar gibi kalıcı hasar unsurlarının sonraki 10-20 klip boyunca temizlenmeden taşınması; durum merdiveni ("damage state: cracked right visor corner with spiderweb fracture, heavy mud encrusted up to mid-calf") şeklinde metin standardizasyonunun difüzyon modellerinde tutarlılık sağlama başarımı; referans görseli kullanımının hasar detaylarını aktarmadaki sınırları.
Ölüm, kayıp ve sahne dışı kalma kontrolü: bir sahnede vurulan, düşen, sedyeyle taşınan veya gruptan ayrılan figürlerin sonraki kalabalık sahnelerde arka planda canlı, yürürken veya hasarsız şekilde duplike olarak halüsinasyonla belirmesini (zombi dirilişi hatası) prompt düzeyinde kesin olarak engelleyen negatif kompozisyon ve kadro dondurma kuralları.
Kritik kısıt: kullanım yeri, 10 saniyelik fotogerçekçi uzay bilimkurgu klipleridir; filmlerde VFX makyajı, CGI dikiş veya 3B karakter modeli yoktur; her klip bağımsız promptla üretilir; karakter basınç giysili ve kasklıdır; çözüm tamamen prompt yazım standardı, SPEC durum parametreleri ve negatif kilitlerle sağlanmalıdır.
Çıktıyı üç tablo ve bir durum protokolü olarak ver: (a) 4 AŞAMALI TRAVMA MERDİVENİ tablosu — kaza sonrası klip sırası (0s, +10s, +20s, +30s), zorunlu beden dili, hareket kısıtı, prompt İngilizce tam kalıbı; (b) KOSTÜM HASAR TAKVİMİ tablosu — hasar tipi (çatlak, yırtık, ezik, kir), promptta kalıcı yazım formatı, modelin koruma başarımı; (c) KADRO DONDURMA VE ELENEN FİGÜR tablosu — sahneden çıkan/ölen karakterin sonraki kliplerde belirmesini engelleyen negatif blok cümleleri; (d) ANTI-RESET PROTOKOLÜ kuralları; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ formatında kaynaklarıyla sunulsun.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_SLOW_RAIN` S14'te sert kaza inişi yapan astronot, S15'te sıfır sarsıntı ve sıfır acıyla karda rahatça otururken başladı (QA: *⑩ OYUNCULUK 🚨 GEÇERSİZ Desen ⑧ Beden Sıfırlanması*). `THE_STOLEN_SKY` S13'te vurulan asker, S24'te hasarsız geri döndü. Bu promptun çıktısı bu iki hatayı birden yasaklayan kuralları getirmelidir.

---

# 4️⃣ MİKRO-AKSİYON VE HALÜSİNASYON İÇİN

### 🔬 PROMPT 4: MİKRO-AKSİYON SINIRI, YÜRÜME PLATOSU VE HALÜSİNASYON PROP ENGELLEME (Feasible Actions & Watermark Cleansing)

```text
Güncel difüzyon video üretim modellerinde (Google Veo 3.1, Gemini Omni 1.1 Flash, Kling, Runway Gen-4, Wan ve Sora), modelin fiziksel olarak üretemediği mikro-manuel eylemlerin el-nesne erimesine (hand-surface fusion) ve katı cisim geçişine yol açması sınırını, karmaşık eylemleri üretemeyip jenerik "yürüme platosuna" kaçmasını ve bilimkurgu sahnelerinde modern eşya/filigran halüsinasyonlarını araştır: parmaklarla küçük bir tokayı açma, vida sıkma, aletle buz kazıma, ince kablo bağlama gibi mikro-el işlerinin modellerdeki başarısızlık oranı ve bu eylemlerin yerini alabilecek "makro-biyomekanik eylem" alternatifleri; modellerin nesne etkileşimi sınırları.
Yürüme platosu ve eylem kaçınma mekanizması: prompta karmaşık hayatta kalma görevleri yazıldığında (örn. aletle kanadı sökmek, tüpü bağlamak, paneli onarmak) difüzyon modellerinin bu karmaşık hareket tensörlerini çözemeyerek sahneyi varsayılan olarak "astronotun kameraya doğru yürümesi" veya "boş boş etrafa bakması" çıktısına indirgemesinin (action degradation) teknik nedenleri; modelin yürüyüşe kaçmasını engelleyen ve net görsel dinamizm sağlayan makro-eylem şablonları (tüm gövdeyle paneli devirme, omuzla kapağa yüklenme, iki elle levyeye asılma, diz çöküp yere tutunma).
Katı cisim sınırları ve erimeyi (fusion/clipping) önleme: modelin eldiven parmaklarını tuttuğu aletin metaline kaynatmasını veya nesnelerin zemin/duvar içinden hayalet gibi geçmesini önleyen kadrajlama ve kompozisyon kuralları; temas anını doğrudan göstermek yerine "temas öncesi hazırlık" ve "temas sonrası sonuç" olarak ikiye bölmenin (occlusion / implied interaction) uygulanabilirliği.
Yapay zeka filigranı ve anakronik halüsinasyon temizliği: modellerin eğitim verilerinden sızan sabit köşe parıltıları/filigranları (özellikle sağ alt köşede 4 kollu yıldız/sparkle watermark kalıntıları) ve yabancı gezegen/uzay üssü ortamlarında beliren anakronik eşyalar (günümüz kamera tripodları, sivil modern kıyafetler, çağdaş çantalar); bu görsel sızıntıları prompt düzeyinde ve negatif bloklarla %100 oranında temizleyen doğrulanmış negatif sözlükler.
Kritik kısıt: kullanım yeri, her biri tam 10 saniye olan fotogerçekçi uzay bilimkurgu klipleridir; filmlerde kompozit temizleme, boyama (paint-out) veya rotoskop kullanılmaz; karakter uzay giysilidir; tüm sorunlar prompt metni, negatif bloklar ve sahne eylem tasarımı ile çekim anında (in-generation) çözülmelidir.
Çıktıyı üç tablo ve bir eylem rehberi olarak ver: (a) MİKRO VS MAKRO EYLEM DÖNÜŞÜM tablosu — yasak mikro-eylem (modelin erittiği/yapamadığı), güvenli makro-eylem karşılığı (tüm gövdeyle yapılan), model güvenilirlik skoru; (b) YÜRÜME PLATOSU KIRICI HAREKETLER tablosu — yürüyüşü kesen 10 saniyelik net statik/dinamik duruş eylemleri; (c) FİLİGRAN VE HALÜSİNASYON TEMİZLEME tablosu — köşe parıltılarını (sparkle) ve anakronik eşyaları (tripod, modern kıyafet) kesin engelleyen İngilizce negatif blok terimleri; (d) SAHNE EYLEM YAZIM KURALLARI; etiketler ÖLÇÜLMÜŞ, UYGULAMA, ÖNERİ formatında kaynaklarıyla sunulsun.
```

* **🧪 Sınama Seti (Depo Kanıtı):** `THE_SLOW_RAIN`'de tokayı ayarlarken eldiven metalle eridi, kanat karın içinden hayalet gibi geçti, 24 sahnenin 19'unda sağ alt köşede AI sparkle filigranı çıktı ve zemin ortasında modern kamera tripodu belirdi! Bu promptun cevabı, modeli eritmeyecek makro-eylemleri ve köşe filigranlarını yok eden negatif filtreyi vermelidir.
