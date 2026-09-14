# 🔬 20 — SİNEMATİK UZAY GİYSİSİ ARAŞTIRMA PROMPTLARI (12.09.2026)

> **Ne bu dosya:** kurulacak `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md`
> (astronot giysisinin *görünüş* katmanı — mevcut `ASTRONOT_DONANIM` yalnız
> *kimlik* katmanıdır) yazılmadan ÖNCE kapatılması gereken üç açık soru
> için üç derin araştırma promptu. Her biri **on cümledir**, her cümle
> **tek satırdır** ve **salt prompt** çalışır — kopyala, araştırma aracına
> yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-19'un gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin isteği (12.09.2026) — *"filmlerdeki karakterlerin
> astronot kıyafetleri çok kötü, daha film tarzı havalı kıyafetler için
> kılavuz."* Depo içi teşhis dört satır:
> ① Bible sözlüğü tek sıfat + "pressure suit": film klasörlerinde en sık
>    giysi cümlesi `white pressure suit` (ölç: `grep -rhoiE
>    "(white|grey|navy|orange)[a-z -]{0,40}(pressure|eva|space) suit"
>    yatay_* dikey_* | sort | uniq -c | sort -rn`) — biçim hiçbir bible'da
>    yazılı değil, modelin varsayılanı doluyor.
> ② Ders 79/139 bloğu (*flat back · carrying nothing · zero tint, zero
>    mirror, zero reflection*) devamlılık ve yüz okunurluğu için kondu;
>    yan etkisi, bir film giysisini film giysisi yapan hacim, halka ve
>    yansımanın yasak listesine düşmesi. Bu bloğun KARARLARI (vizör berrak
>    [T11.5③] · sırt kaymaz) sorgulanmıyor; TARİF BİÇİMİ sorgulanıyor.
> ③ TUR 5 (03.09.2026) "daha detaylı olsun: rozet, eşya, saat, hava
>    ünitesi" isteğiyle koştu ve kaynağı Apollo/EMU/Orlan tarihiydi —
>    ayırt ettirmeyi öğretti, iyi göstermeyi sormadı.
> ④ Hiçbir QA merceği "tasarım kalitesi" ölçmüyor: ①/② devamlılık ölçer,
>    Kostüm-Prop hücresi "sabit kaldı mı" der. Sistem giysinin kötü
>    olduğuna dair hiç sinyal almadı; ilk ölçüm sahibin gözü.
>
> **KOŞU KAYDI:** ✅ **12.09.2026 koşuldu → 3/3 rapor geldi, BİREBİR arşivlendi:**
> `TUR17_HAM_RAPORLAR/` (her dosyanın başında koşulan prompt; tek satır, tablolar
> çökmüş, kaynak listesi YOK — `00_KUNYE.md`). Süzme: `04_ARASTIRMA_BULGULARI.md`
> §TUR 17 (25 giren · üçüncü liste GEOMETRİYE ÇEVRİLDİ · sayı katmanı çürük).
> ✅ Süzmeden sonra kılavuz yazıldı (aynı gün): `../UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md`.
> ⚠️ Yeniden koşulacaksa kaynak listesi İSTENİR; rapor 3'ün motor tabloları depo
> motorlarını ölçmüyor — yeniden koşuda motor adları promptun 9. cümlesine yazılır.

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR 17 (süzme kaydı) →
         ancak oradan yeni kılavuza ve dokunduğu yerlere
         (ASTRONOT_DONANIM işaretçi · KILAVUZ_REHBERI §1 tür satırı ·
         REFERANS_PAKETI §4.1 kask içi ışık satırı · FILM_KLASOR_SABLONU
         bible bloğu · prompt_kontrol kapı adayı). Süzme kaydı İKİ liste
         tutar: NEYİN GİRDİĞİ ve NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "GÜZEL KOSTÜM GALERİSİ" DEĞİLDİR.
   Aranan şey hayranlık değil MEKANİZMA + EŞİK + TEST: bir giysinin neden
   "film giysisi" okunduğu, hangi değişken devrilince "oyuncak" ya da
   "stok NASA" okunduğu, tasarımın klipler arasında neye mal olduğu.
   "Şu film güzeldi" diyen ama hangi geometri/neden/ne kadar demeyen
   kaynak süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — deneysel / korpus / benchmark / hakemli ölçüm
   (b) UYGULAMA — kostüm tasarımcısı, görüntü yönetmeni, yapım notu,
       tasarım kuramı kitabı
   (c) ÖNERİ    — raporun kendi tasarım önerisi
   Kaynaksız (a) düşer; (b) ancak iki bağımsız uygulayıcı aynı şeyi
   söylüyorsa iner; (c) yalnız ⬜ HİPOTEZ etiketiyle iner.

⛔ KOPYA SINIRI — film adı ARAŞTIRMA promptunda OLUR, ÜRETİM promptuna
   İNMEZ [MESHUR_SAHNE_KALIPLARI §4 · 17_'nin usulü].
   Raporlar film ve tasarımcı adıyla konuşabilir; süzmede her bulgu
   GEOMETRİYE ve MEKANİZMAYA çevrilir ve 04 §TUR 17 "GEOMETRİYE ÇEVRİLDİ"
   listesini tutar. Kılavuza film adı, karakter adı, tescilli tasarım adı
   ve marka girmez — bu yüzden 1 numaralı prompt tabloyu "film adı
   silinince de okunur" biçimde ister.

⛔ ÖNCEKİ TURLARLA ÇAKIŞMA — yeniden istenmeyenler ("ZATEN VAR").
   • Rol şeridi (renk · LEFT/RIGHT konum), metinsiz amblem seti, kişisel
     eşya sistemi, saat/bilek düzeni, yaşam destek DIŞ ANATOMİSİ (PLSS ·
     SAFER · DCM ölçüleri), arıza görselliği, AI risk sınıfları → TUR 5.
     Hiçbir prompt bunları sormaz; rapor getirirse "ZATEN VAR".
   • Referans paketinin SAYFA KANONU (görünüm sayısı · zemin · ışık),
     yükleme kuralı, "sayılabilen BELGEDE / dokunsal GÖRSELDE" iş bölümü
     ilkesi, kod kanonu → TUR 12. 3 numaralı prompt ilkeyi yeniden
     İSTEMEZ; onu KOSTÜM için ÖLÇÜMLE sorar (hangi giysi öğesi önce kayar).
   • Motorların politika yüzeyi, red sınıfları, kelime sözlüğü → TUR 3.
   • Metin yasağı ve kapsamı [D34 · D45 · D138], vizör berrak kararı
     [D79 · D95 · T11.5③], sırt yokluk-kilidi ve pozitif yüzey cümlesi
     [D139] deponun KARARLARIDIR — promptlar bunları "kısıt" olarak
     dokuzuncu cümlede verir, doğru mu diye SORMAZ.
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Düz sırt çirkinliğin sebebi", "sert gövde + yumuşak uzuv = sinematik",
   "beyaz = belgesel", "az öğe daha iyi tutar", "kask içi ışık heybeti
   geri verir" bu deponun TASARIM ADAYLARIDIR, kanıtlanmış yasa değil —
   üç prompt da İKİ YÖNLÜ yazıldı (sade giysinin güçlü okunduğu vakalar,
   şık giysinin oyuncak okunduğu vakalar, zengin tasarımın tutarlı kaldığı
   hatlar da istenir). Üretim kısıtları hipotez değil FİLTREDİR ve her
   promptun dokuzuncu cümlesinde açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 2 : 1'in her arketipi 2'nin malzeme sözlüğüyle YAZILABİLMELİ;
           2 "sert kabuk kelimeleri oyun görünümü üretir" diyorsa 1'in
           sert kabuklu arketipi kılavuza risk etiketiyle iner, etiketsiz
           inmez.
   2 ↔ 3 : 2'nin "güvenilir" dediği malzeme/renk kelimesi 3'ün
           sürüklenme tablosunda "önce kayan" çıkıyorsa iki rapor da o
           satırı ⬜ HİPOTEZ taşır.
   1 ↔ 3 : 1'in arketip öğe sayısı 3'ün metin bütçesine sığmıyorsa
           arketip kılavuza "kısaltma sırası" satırıyla iner; sırasız
           arketip inmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Silüet ve tasarım dili** — giysiyi "film giysisi" okutan değişkenler, arketipler, kask mimarisi | Bible'da biçim yok (tek sıfat + "pressure suit"); DONANIM §4 siluet tablosu dört satır ve gerçek-donanım kökenli; "havalı"nın hangi değişkenden çıktığı hiç sorulmadı | Yeni kılavuz §1 ARKETİP tablosu · §3 kask mimarisi · DONANIM §4'e işaretçi |
| 2 | **Yüzey, renk ve ışık** — kamerada ve AI motorunda malzeme/renk/kir/kask içi ışık | Malzeme sözlüğü yok; negatif çekirdek "no CGI / no game" ile sert kabuk tarifi çekişiyor, ölçülmedi; kask içi ışık REFERANS_PAKETI §4.1'de tek satır, gerekçesiz; renk adı kayması bir vaka (oxblood → deep maroon), sistematik değil | Yeni kılavuz §2 MALZEME SÖZLÜĞÜ · §4 renk bloğu · §5 kask içi ışık kalıbı · negatif çekirdek notu |
| 3 | **Giysi kilidi ve bütçe** — tasarımı klipler boyunca tutmak, metin maliyeti, ölçüm | D139 pozitif yüzey cümlesi tek vakaya dayanır; giysi tarifinin bant içindeki payı hiç ölçülmedi; hangi giysi öğesinin önce kaydığı deponun ders kayıtlarında dağınık (D42 · D58 · D79 · D139); "tasarlandığı gibi mi" ölçen mercek yok | Yeni kılavuz §6 SÜRÜKLENME tablosu · §7 bütçe ve kısaltma sırası · §8 bible reçetesi · QA mercek adayı (kart G) |

> ⚠️ **1 ile 2, 2 ile 3, 1 ile 3 birbirini denetler** (yukarıdaki çapraz
> okuma). Bir raporun getirdiği eşik ötekinde tutmuyorsa kılavuza ancak
> ⬜ HİPOTEZ etiketiyle iner, sayısız iner.

---

# 1️⃣ SİLÜET VE TASARIM DİLİ — giysiyi "film giysisi" okutan ne, hangi arketip hangi hikâye

```
1968'den bugüne sinema ve prestij dizilerinde TASARLANMIŞ uzay giysilerinin (2001: A Space Odyssey, Alien, Sunshine, Moon, Prometheus, Gravity, Interstellar, The Martian, Ad Astra, First Man, Passengers, Europa Report, Stowaway, For All Mankind, The Expanse ve benzerleri) kostüm tasarımcısı, yapım tasarımcısı ve konsept sanatçısı tanıklıklarını topla: her giysi için tasarımcının belgelenmiş NİYETİ (hangi hikâye tonu, hangi karakter bilgisi), aldığı gerçek referans (hangi ajans giysisi, hangi dalış, askerî ya da spor ekipmanı) ve bilerek SAPTIĞI yerler — kaynak, tarih ve tür ile.
Her giysiyi film adından bağımsız GEOMETRİYE indir: gövde ve uzuvlarda sertlik dağılımı (sert kabuk nerede, yumuşak kumaş nerede), omuz genişliği ile bel daralması oranı, kask-gövde bağlantı biçimi (yaka halkası görünür mü, kask gövdeye gömülü mü), sırt hacmi ve profili, eldiven ve bot kütlesi, eklem çözümü (körük, bilezik, segment) — tablo film adı silinince de okunabilsin.
Bir giysinin izleyicide "sinematik / ikonik" ile "belgesel / stok ajans giysisi" okuması üretmesini hangi görsel değişkenlerin belirlediğini araştır — siluet okunurluğu, oran, sertlik kontrastı, renk bloğu, yüzey parlaklığı, kask biçimi, parça sayısı — bunu ölçen, sistematik karşılaştıran ya da kuramlaştıran çalışma, eleştiri korpusu veya tasarım kuramı var mı; her iddiaya kaynak ve etiket.
İki yönlü sor: sade, gerçekçi, belgesel görünümlü giysinin tam da o yüzden güçlü okunduğu belgelenmiş vakalar ile şık, ince, sert kabuklu tasarımın "oyuncak", "video oyunu", "kostüm partisi" okunup eleştiri aldığı vakalar — hangi değişken hangi yönde devrildi, eleştirinin kendi sözcükleriyle.
Siluet ARKETİPLERİNİ çıkar ve her birini hikâye durumuna eşle: hangi arketip yalnızlık, hangisi kurumsal ekip, hangisi endüstriyel emek, hangisi keşif, hangisi tehdit ya da yas okutuyor — tasarımcı beyanı (UYGULAMA) ile izleyici algısı (ÖLÇÜLMÜŞ) ayrı sütunlarda.
Kask ve vizör mimarisini ayrıca sök: kubbe, düz pane, çok yüzlü, dar pencere; çerçeve kalınlığı ve görünürlüğü; kask içi ışık düzeni ve görüntü yönetmenlerinin yüzü kask içinden aydınlatma gerekçeleri; yüzün okunması ile giysinin heybeti arasındaki takasın tasarımda nasıl çözüldüğü — berrak vizörle güçlü siluet kuran vakalar özellikle.
Renk ve malzeme kararlarının gerekçesini topla: giysi rengi ile ortam rengi (siyah uzay, turuncu-kırmızı toprak, beyaz buz, gri istasyon) arasındaki kontrast ilkesi, tek aksan rengi pratiği, mat, saten ya da parlak yüzey seçiminin kamera gerekçesi, kir ve yıpranma katmanının hangi filmde neden eklendiği ya da bilerek eklenmediği.
Tarihsel sapmaları belgele: gerçek basınç giysisinin fiziksel olarak izin vermediği ama sinemanın rutin yaptığı şeyler (ince bel, dar omuz, esnek eklem, sırt ünitesiz tasarım, kask içinden gelen yüz ışığı) — hangi sapmanın izleyici tarafından hiç fark edilmediği, hangisinin "sahte" okunduğu, uzman ve genel izleyici tepkisi ayrı ayrı.
Kritik kısıt: hedef filmler on saniyelik kesmesiz sabit kamera planlarıyla kurulur, giysi metinle ve dört ile altı karelik referans paneliyle yapay zekâ görüntü ve video motorlarına (Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzerleri) tarif edilir, vizör her karede berrak ve yüz okunur olmak zorundadır, giysi üzerinde okunur yazı, bayrak, logo ve marka bulunamaz, serbest hortum ve kablo devamlılık nedeniyle yasaktır, sırt her sahnede aynı biçimde tarif edilebilen tek yüzey olmalıdır — bu yüzden çok parçalı, çok kablolu, aynalı ya da opak vizörlü, yazı taşıyan tasarımları işaretleyip ele; az parçayla güçlü siluet kuranları öncelikle.
Çıktıyı iki tablo ve iki liste olarak ver: (a) ARKETİP tablosu — arketip adı, film adsız geometri tarifi, sertlik dağılımı, kask tipi, renk mantığı, eşlendiği hikâye tonu, tasarımcı gerekçesi, izleyici okuması, İngilizce tek satırlık gövde kalıbı, kaynak ve etiket; (b) SİNEMATİK OKUMA değişken tablosu — değişken, sinematik yöndeki değeri, belgesel yöndeki değeri, devrildiği eşik, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ YÜZEY, RENK VE IŞIK — giysi kamerada ve yapay zekâ motorunda nasıl görünür

```
Kostüm yüzeyinin kamerada nasıl okunduğunu araştır: mat, saten, parlak ve metalik yüzeylerin sert ve yumuşak ışık altında ölçülmüş ya da belgelenmiş davranışı (parlama, doku kaybı, kütle hissi), kapitone, nervürlü, örgü ve düz kumaşın hangi kamera ölçeğinde doku olarak okunup hangi ölçekte düz renge çöktüğü — görüntü yönetmeni, kostüm ve dijital doku kaynakları ile varsa ölçüm, her biri kaynak, tarih ve türle.
Renk bloğu kurallarını çıkar: bir giysi üzerinde kaç renk ve hangi oranlarda (ana, ikincil, aksan) kullanıldığında siluet bütünlüğü korunuyor, aksan rengin gövdenin neresine konması uzak ölçekte okunurluk sağlıyor, açık ve koyu değer kontrastının ortam zeminine (siyah uzay, kırmızı-turuncu toprak, beyaz buz, gri metal) göre nasıl seçildiği — tasarım kuramı, yapım notu ve algı çalışması ayrı ayrı.
Kirlenme ve yıpranmayı ölç: yeni-temiz giysi ile yıpranmış giysinin izleyicide ürettiği okuma (steril, oyuncak, yaşanmış, tehlikeli), kirin hangi bölgelere ve hangi yoğunlukta uygulandığı, kirin karakter bilgisi taşıdığı belgelenmiş vakalar ve kirin fazla olduğunda siluet ile rengi yuttuğu eşik.
Kask içi ışığı sök: sinemada yüzü kask içinden aydınlatma konvansiyonunun (halka, üst-alt çift kaynak, gizli LED şerit) teknik uygulaması, renk sıcaklığı ve yönü, bu ışığın fiziksel gerçekçilikle çelişmesine rağmen neden kabul gördüğü, vizördeki yansıma (kamera, ekip, ortam) probleminin set ve post çözümleri ve berrak vizörün heybet kaybını neyle telafi ettikleri.
Yapay zekâ görüntü ve video motorlarına geç: Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzer motorlarda malzeme ve doku kelimelerinin ("matte", "satin", "brushed", "quilted", "ribbed", "hard composite shell", "anodized", "ballistic nylon", "worn" gibi) çıktıda ölçülmüş ya da sistematik gözlemlenmiş etkisi, hangi kelimelerin güvenilir hangilerinin gürültü olduğu, model sürümleri arasındaki farklar ve kaynağı.
"Oyun / CGI görünümü" arızasını araştır: sert kabuklu, panelli, ışıklı giysi tariflerinin fotogerçekçi promptta bile oyun karakteri estetiği üretme eğilimi belgelenmiş mi, bunu hangi kelimeler tetikliyor, hangi kelimeler (film grain, lens, kumaş fiziği, yıpranma, ter, nefes buğusu) geri çekiyor ve "no CGI look" türü olumsuz cümlelerin ölçülmüş etkisi ne — iki yönlü: sert kabuğun fotogerçekçi tuttuğu belgelenmiş vakalar da istenir.
Renk adı ve palet kilidini ölç: motorların renk adlarını (safety orange, slate grey, deep maroon vb.) ne kadar tutarlı ürettiği, aynı renk adının klipler arasında kayma oranı, iki tonlu giysinin hangi tonunun önce kaydığı ve çıplak renk adı yerine malzeme + renk kalıbının ("matte brick-red polymer plate") tutarlılığa ölçülmüş etkisi.
Işık ile giysi etkileşimini ölç: tek sert güneş ışığı, kabin içi yumuşak ışık ve kask içi lokal ışık altında aynı giysi tarifinin çıktıda nasıl değiştiği, beyaz giysinin patlaması ve koyu giysinin siyah zeminde erimesi arızalarının belgelenmiş çözümleri, pozlama ve dinamik aralık kelimelerinin etkisi.
Kritik kısıt: hedef klipler on saniyelik tek plandır, yüz kask içinde ve berrak vizör ardında her karede okunur olmalıdır, negatif çekirdekte "no CGI aesthetic, no video game aesthetic, photorealistic with 35mm film grain" cümlesi sabittir, giysi üzerinde okunur yazı ve marka yoktur, HEX kodu prompta girmez ve renk her zaman malzemeyle birlikte adlandırılır — bu yüzden parlak zırh, gövde üstü ekran ve neon şerit ağırlıklı çözümleri işaretleyip ele; kumaş, kabuk, kir ve tek aksan rengiyle çalışanları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) MALZEME SÖZLÜĞÜ — İngilizce kelime, kamerada okunma ölçeği, motorlarda güvenilirlik, oyun-görünümü riski, kaynak ve etiket; (b) RENK BLOĞU tablosu — kural, oran, aksan konumu, zemin uyumu, kaynak ve etiket; (c) KASK İÇİ IŞIK tablosu — düzen, yön, sıcaklık, gerekçe, İngilizce tek satırlık kalıp, kaynak; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ GİYSİ KİLİDİ VE BÜTÇE — tasarımı klipler boyunca tutmak, neye mal olur, nasıl ölçülür

```
Film kostüm departmanlarının devamlılık pratiğini araştır: kostüm devamlılık sayfaları, kostüm kitabı ve döner-görünüm çizimlerinde hangi bilgilerin zorunlu tutulduğu, giysinin hangi bölgelerinin devamlılık hatasına en açık olduğu (kayış, kapak, kir, aksesuar konumu), ve bu hataların izleyici tarafından fark edilme oranına dair çalışma — kaynak, tarih ve tür ile.
Yapay zekâ görüntü-video hattında kostüm sürüklenmesini ölç: referans görsel ve metinle tarif edilen bir giysinin ardışık kliplerde hangi öğelerinin önce kaydığı (sırt, eldiven, kask halkası, şerit konumu, panel sayısı, renk tonu, kir dağılımı), sürüklenme oranlarını raporlayan benchmark, değerlendirme çalışması ya da sistematik topluluk ölçümü, motorlar arası fark.
Karmaşıklık ile tutarlılık arasındaki takası ölç: giysi tarifindeki öğe sayısı arttıkça devamlılık hatasının artıp artmadığı, "az ama büyük" öğelerle "çok ama küçük" öğelerin karşılaştırmalı ölçümü, ve iki yönlü sor — zengin tasarımın buna rağmen tutarlı kaldığı belgelenmiş hatlar ile sade tasarımın yine de kaydığı vakalar.
Sırt ve arka görünüm problemini ayrıca sor: kamera figürün arkasına geçtiğinde modelin boş sırtı doldurma eğilimi belgelenmiş mi, yokluk tarifi ("no backpack") ile pozitif yüzey tarifi ("one continuous panel") ve heykelsi pozitif tarif ("low-profile sculpted back plate with two recessed panels, no hose") arasında tutarlılık farkı ölçülmüş mü, sırt için hangi tarif biçimi hem sinematik hacim hem klipler arası sabitlik veriyor.
Metin bütçesini ölç: bir karakter giysisi tarifinin prompt içinde kaç kelime ya da karakter aldığında sahne, ışık ve eylem tarifinin zarar görmeye başladığı, uzun promptun sonundaki cümlelerin ihmal edilme eğilimi (konum etkisi) ölçülmüş mü, ve giysi tarifini kısaltırken hangi katmanın (siluet, malzeme, renk, aksesuar, kir) son çıkarılması gerektiğine dair kanıt.
Referans paneli ile metnin iş bölümünü KOSTÜM için ölç: giysinin hangi bilgisi görselde, hangisi metinde daha iyi tutuluyor (biçim mi, renk mi, doku mu, sayı mı), referans karesinin ışığı ve pozu ile sahne ışığı çeliştiğinde kostümün hangi yönde bozulduğu, ve tek kimlik karesi ile çoklu görünüm setinin karşılaştırmalı tutarlılığı.
Kimlik ile giysiyi ayır: aynı giysiyi giyen iki karakteri ayırt eden en küçük tasarım farkının klipler arası kayma davranışı, farkın asimetrik konumda olmasının ölçülmüş etkisi ve iki figürün kostümünün birbirine bulaşması (renk, şerit, aksesuar sızması) arızasının oranı ve belgelenmiş çözümleri.
Ölçüm tarafını kur: üretilmiş bir klipte giysinin "tasarlandığı gibi" olup olmadığını puanlayan yayınlanmış bir rubrik, kontrol listesi ya da otomatik ölçüm (siluet karşılaştırma, renk histogramı, öğe sayımı, referansa benzerlik skoru) var mı, maddeleri neler, insan hakemler arası uyuşması ölçülmüş mü ve bu ölçüm "devamlılık" ile "tasarım kalitesi"ni ayrı puanlıyor mu.
Kritik kısıt: hedef filmler yirmi ile yüz seksen arası on saniyelik kliptir, her klip kendi başına çalışan tek bir prompttan üretilir ve başka belgeye atıf yapamaz, video promptunun toplam uzunluğu dar bir banda kilitlidir ve giysi tarifi o bandın içinden pay alır, karakter tarifi her sahnede kelimesi kelimesine aynı kopyalanır, referans paketi film başına dört ile altı karelik kimlik panelleri içerir, sırt her sahnede tek yüzey olarak tarif edilir ve serbest hortum, kablo, okunur yazı yasaktır — bu yüzden çok belgeli, çok panelli, sahne başına yeniden tasarlanan çözümleri işaretleyip ele; tek blok metin ve az panelle uzun klip dizisini tutanları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) SÜRÜKLENME tablosu — giysi öğesi, kayma sırası ve oranı, motor, önleyen tarif biçimi, kaynak ve etiket; (b) BÜTÇE tablosu — tarif katmanı, kelime ya da karakter maliyeti, çıkarılma sırası, kanıt; (c) ÖLÇÜM tablosu — rubrik ya da araç, maddeleri, hakem uyuşması, devamlılık/tasarım ayrımı, kaynak; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Üç rapor HAM hâliyle saklanır: TUR17_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil; araştırma aracı kaynak listesini
   boş verirse 00_KUNYE.md'ye yazılır ve yeniden koşuda İSTENİR — TUR 15
   dersi). Prompt metinleri her ham dosyanın başına birebir kopyalanır
   (Tur 7 usulü).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR 17 açılır ve ÜÇ liste yazılır:
   GİRDİ (bulgu · hangi dosyaya · tipi) · GİRMEDİ (bulgu · NEDEN) ·
   GEOMETRİYE ÇEVRİLDİ (film adlı bulgu → adsız geometri; 17_'nin usulü).
   Her sayı ÜÇ etiketten birini taşır: ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ.
   TUR 3/5/12'de zaten inen bulgular "ZATEN VAR" etiketiyle geçer.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔2 · 2↔3 · 1↔3). Tutmayan eşik kılavuza
   İNMEZ, çelişki kayda geçer. Özellikle 1↔2: sert kabuklu arketip ile
   oyun-görünümü riski TEK satırda buluşmuyorsa arketip ⬜ HİPOTEZ iner.
4. Ancak ondan sonra kılavuz yazılır: UZAY_GIYSISI_SINEMATIK_TASARIM_
   KILAVUZU.md (§1 arketip · §2 malzeme sözlüğü · §3 kask mimarisi · §4
   renk bloğu · §5 kask içi ışık · §6 sürüklenme · §7 bütçe ve kısaltma
   sırası · §8 bible reçetesi + örnek İngilizce bloklar). Dokunduğu yerler
   AYRI iştir ve kart G/P usulüyle işlenir: ASTRONOT_DONANIM §4'e işaretçi
   · KILAVUZ_REHBERI §1 Bilimkurgu satırı · REFERANS_PAKETI §4.1 kask içi
   ışık satırı · FILM_KLASOR_SABLONU bible bloğu · negatif çekirdek notu ·
   "tasarlandığı gibi mi" QA mercek adayı (varsa kart G).
   ⛔ Ders 79/139 bloğunun KARARI değişmez; kılavuz yalnız sırt ve vizör
   için pozitif TARİF BİÇİMİ önerir ve ilk filmde ①/② ile sınar.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** üç prompt da DIŞ bilgi getirir.
Tasarımcı ve görüntü yönetmeni tanıklıkları UYGULAMA düzeyindedir, hakemli
değil; "sinematik okuma" değişkenlerinin izleyici ölçümü muhtemelen
seyrektir ve raporlar boşluğu kendi önerisiyle dolduracaktır — o satırlar
⭐ öneri etiketiyle iner. AI motor ölçümleri topluluk gözlemi ağırlıklı
olacaktır; motor sürümü ve tarih yazılmayan ölçüm inmez. Kılavuza inen
hiçbir arketip henüz üretimde test edilmedi; ilk uygulamada referans
paneli (R1 arka görünüm dâhil) + ① KARE ve ② DEVAMLILIK skorlarıyla sınanır.
