# 🔬 21 — DÜNYA · IŞIK · YÜZ · ARAÇ GÖRÜNÜŞ ARAŞTIRMA PROMPTLARI (12.09.2026)

> **Ne bu dosya:** kurulacak DÖRT kılavuz için dört derin araştırma promptu.
> Her biri **altı cümledir**, her cümle **tek satırdır** ve **salt prompt**
> çalışır — kopyala, araştırma aracına yapıştır, başka hiçbir şey verme.
>
> | # | kurulacak kılavuz (çalışma adı) | hangi Bible'ın görünüş katmanı |
> |:--:|---|---|
> | 1 | `DUNYA_GORUNUSU_KILAVUZU.md` | World Bible — gökyüzü · ufuk · arazi · gök cisimleri |
> | 2 | `ISIK_SENARYOSU_KILAVUZU.md` | Lighting Bible — film boyu ışık planı (çevre yarısı) |
> | 3 | `YUZ_VE_KAST_KILAVUZU.md` | Character Bible'ın YÜZ yarısı (giysi yarısı: TUR 17) |
> | 4 | `ARAC_VE_IC_HACIM_TASARIM_KILAVUZU.md` | Vehicle Bible (⬜ şablona girer mi: sahip kararı) + kabin/kokpit/koridor |
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-20'nin gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin sorusu (12.09.2026) — *"sence kılavuz olarak
> başka eksik ne var"* — ve TUR 17'nin bittiği gün yapılan tarama. Teşhis
> dört satır, dördü de depodan ölçüldü (12.09.2026 kesiti; komutlar
> `yatay_*/*/*.md dikey_shorts_filmler/*/*.md` üzerinde):
> ① `FILM_KLASOR_SABLONU/FILM_PLAN.md` ALTI Bible tanımlıyor; dördünün
>    kılavuzu var (Character → DONANIM + UZAY_GIYSISI · Negative → REHBERİ
>    §5 · Physics → REHBERİ §3 · Camera → KAMERA_ACISI + ACI_YAYI).
>    **World ve Lighting Bible için "nasıl yazılır" kılavuzu YOK**; ikisi
>    de `SINEMATOGRAFIK_TEKNIK` §1/§8'in beş satırlık tablosuna yaslanıyor.
> ② Gökyüzü ve arazi deponun EN SIK görsel öznesi ve giysideki hastalığı
>    taşıyor — tek sıfat + isim (`grep -ohiE "[a-z-]+ [a-z-]+ sky\b" … |
>    sort | uniq -c | sort -rn` → *flat black sky* · *pale x-beige sky*
>    ilk sıralarda). Gözlem defterinde kapısız beş aday (31 · 32 · 50 ·
>    70 · 71) ve D6 · D48 · D145 buna vuruyor.
> ③ Işık sürekliliği defterin EN BÜYÜK kapısız kümesi (17 · 27 · 42 · 43 ·
>    56 · 86 · 87 · 88) + D47 · D104 · D193 · D201. ⑪ merceği ölçüyor,
>    yazım tarafı yok; son üç film güneş yönü ve ışık takvimini kendi
>    başına icat etti (BENT GRASS · DRY ANCHOR · COUNTED TURN).
> ④ Yüz tek kalıba çökmüş (`grep -ohiE "[a-z-]+ [a-z-]+ (eyes|hair)\b"` →
>    *dark brown eyes* ve *dark brown hair* açık ara ilk; yaş kalıbı *woman
>    in her late thirties*). D79 vizörü berrak yaptı: yüz artık en açık
>    kimlik yüzeyi. ⑯'nın MİLLİYET tetiklerinin sebebi bir yüz sözlüğü
>    olmaması — `POLITIKA` §2 tek ikame satırı veriyor. Araç için aynı:
>    `grep -ohiE "[a-z-]+ hull\b"` → sıfatlar konumsal (*low · upper ·
>    torn*), malzeme yok; `UZAY_USSU` gemi/gezici için yalnız iki ölçek
>    satırı taşıyor ve §9 ① "iç mekân cetveli yok" diyor.
>
> **KOŞU KAYDI:** ⏳ **henüz koşulmadı** (12.09.2026 yazıldı). Koşulunca:
> `TUR18_HAM_RAPORLAR/` (her dosyanın başında koşulan prompt birebir) →
> `04_ARASTIRMA_BULGULARI.md` §TUR 18 → dört kılavuz. ⚠️ Kaynak listesi
> İSTENİR; gelmezse `00_KUNYE.md`'ye yazılır (TUR 15/17 dersi). Rapor
> motor tablosu getirirse motor adı ve tarihi olmayan satır inmez.

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR 18 (süzme kaydı) →
         ancak oradan dört kılavuza ve dokunduğu yerlere
         (FILM_KLASOR_SABLONU World/Lighting/Character bible blokları ·
         KILAVUZ_REHBERI §1 tür satırı + §3 ortam kartlarına işaretçi ·
         SINEMATOGRAFIK_TEKNIK §1 işaretçi · SAHNE_DEVAMLILIK §2.1 yüz
         satırı · POLITIKA §2 milliyet ikame satırı · UZAY_USSU §4 ve §9 ①
         · ⑪ IŞIK rubriği [D201 kapısı] · prompt_kontrol kapı adayları).
         Süzme kaydı ÜÇ liste tutar: GİRDİ · GİRMEDİ + NEDEN ·
         GEOMETRİYE ÇEVRİLDİ.

⛔ BU ARAŞTIRMA "GÜZEL MANZARA / GÜZEL GEMİ GALERİSİ" DEĞİLDİR.
   Aranan şey hayranlık değil MEKANİZMA + EŞİK + TEST: bir gökyüzünün
   neden "gerçek yer" değil "fon levhası" okunduğu, ışık yönü değişince
   izleyicinin neyi ne zaman fark ettiği, bir yüzün kaskta hangi
   özellikle tanındığı, bir gövdenin neden "oyun gemisi" okunduğu.
   "Şu film güzeldi" diyen ama hangi geometri/neden/ne kadar demeyen
   kaynak süzme kaydına "GİRMEDİ" yazılır.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — deneysel / korpus / benchmark / hakemli ölçüm
   (b) UYGULAMA — yapım tasarımcısı, görüntü yönetmeni, kast yönetmeni,
       VFX süpervizörü, devamlılık süpervizörü, tasarım kuramı kitabı
   (c) ÖNERİ    — raporun kendi tasarım önerisi
   Kaynaksız (a) düşer; (b) ancak iki bağımsız uygulayıcı aynı şeyi
   söylüyorsa iner; (c) yalnız ⬜ HİPOTEZ etiketiyle iner.
   TUR 17'nin dersi: sayı katmanı çürük gelirse kılavuz SAYISIZ yazılır.

⛔ KOPYA SINIRI — film adı ARAŞTIRMA promptunda OLUR, ÜRETİM promptuna
   İNMEZ [MESHUR_SAHNE_KALIPLARI §4 · 17_ ve 20_'nin usulü].
   Raporlar film ve tasarımcı adıyla konuşabilir; süzmede her bulgu
   GEOMETRİYE ve MEKANİZMAYA çevrilir ve 04 §TUR 18 "GEOMETRİYE
   ÇEVRİLDİ" listesini tutar. Kılavuza film adı, karakter adı, oyuncu
   adı, tescilli tasarım adı ve marka girmez — bu yüzden 1 ve 4 numaralı
   promptlar tabloyu "film adı silinince de okunur" biçimde ister.
   ⛔ 3 numaralı prompt için ek sınır: GERÇEK KİŞİ yüzü referans olarak
   kılavuza girmez; yalnız sözlük ve mekanizma iner [POLİTİKA §2 · D123].

⛔ ÖNCEKİ TURLARLA VE MEVCUT KILAVUZLARLA ÇAKIŞMA ("ZATEN VAR").
   • Ortam FİZİĞİ (toz, gölge kenarı, dolgu, ses, rüzgar, gökyüzü tek
     satırı) → KILAVUZ_REHBERI §3 kartları. 1 ve 2 fiziği yeniden
     SORMAZ; görünüşü ve klipler arası sürekliliği sorar.
   • Işık psikolojisi tablosu, renk sıcaklığı haritası, LOG/ACES, sensör
     ve lens karakteri → SINEMATOGRAFIK_TEKNIK §1 · §9-15. 2 sormaz.
   • Kask İÇİ yüz ışığı (üç düzenek + kalıp), malzeme sözlüğü, kir global
     bitiş, sert kabuk üç kelime kuralı → TUR 17. 2 kask içini sormaz;
     4 sözlüğü yeniden istemez, yalnız ARACA taşınabilirliğini sorar.
   • Ölçek birimi 1H, istasyon/üs anatomisi, sayılabilir çapa, ölçek
     şahidi merdiveni, maket etkisi (bulanıklık gradyanı), iki negatif
     blok, dönen yapı, ISS iç metrikleri → TUR 9. 4 bunları sormaz;
     yalnız §9 ①'in AÇIK bıraktığı iç hacim görünüşünü ve dış yüzey
     dilini sorar.
   • Aracın iniş/kalkış/yanaşma HAREKETİ ve fren yönü → UZAMSAL_HARITA §5
     + YANASMA_VE_KENETLENME. 4 hareket sormaz.
   • Referans paketi kanonu, panel sayısı, seed → TUR 12. Sorulmaz.
   • Milliyet · gerçek kurum · gerçek kişi yasağı ve ünlü benzerliği reddi
     → TUR 3 + POLİTİKA §2. 3 bunu KISIT olarak verir, doğru mu SORMAZ.
   • Rol şeridi, amblem, eşya, saat → TUR 5. 3 ve 4 sormaz.
   • Deponun ölçülmüş KARARLARI promptlarda kısıt olarak durur, sorgu
     değil: derece/metre gövde cümlesine yazılmaz [D138] · güneş yönü
     kadran+yükseklikle SPEC'te kilitlenir [D201] · en parlak ışık yön
     mıknatısıdır [D104] · alçak açıda ufuk kilidi [D145] · biyom ve ışık
     sahneler arası sıçramaz [D47 · D48] · vizör berrak, yüz okunur [D79 ·
     T11.5③] · karakter adı prompta girmez [D45] · yüz bloğu kelimesi
     kelimesine kopyalanır [SAHNE_DEVAMLILIK §2.1] · "glow/bloom" yasak
     [D3 · D29] · yüzeyde okunur yazı yok [D34 · D45].
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Tek sıfatlı gökyüzü düz çıkıyor", "kadran kilidi ışığı tutar", "yüz
   çeşitliliği kanal kimliği için şart", "araç arketipi giysi arketipi
   gibi çalışır", "kalabalık iç hacim = yaşanmış" bu deponun TASARIM
   ADAYLARIDIR, kanıtlanmış yasa değil — dört prompt da İKİ YÖNLÜ yazıldı
   (sade dünyanın güçlü okunduğu, steril beyaz kabinin bilerek seçildiği,
   ortalama yüzün işe yaradığı, derece yazmanın kadrajda sayı bastığı
   vakalar da istenir). Üretim kısıtları hipotez değil FİLTREDİR ve her
   promptun beşinci cümlesinde açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — dört çift.
   1 ↔ 2 : gökyüzü rengi, güneş konumu ve renk sıcaklığı AYNI fizikten
           çıkar; 1'in gökyüzü tablosu 2'nin ışık takvimiyle çelişirse
           iki satır da ⬜ HİPOTEZ, sayısız iner.
   1 ↔ 4 : arazi doku ölçeği (yakın taş boyu) aracın boyutunu okutur;
           1'in doku hiyerarşisi 4'ün "oyuncak okuma" eşiğiyle
           uyuşmuyorsa ölçek satırı UZAY_USSU §5'e işaretle iner, yeni
           kural yazılmaz.
   2 ↔ 4 : 4'ün "güvenilir" dediği gövde yüzeyi (mat/parlak) 2'nin tek
           sert kaynak altında "patlar/erir" dediği yüzeyse iki rapor da
           o satırı ⬜ HİPOTEZ taşır.
   2 ↔ 3 : 3'ün "kaskta tanımayı taşıyan bölge" satırı 2'nin dış ışık
           yönü tablosuyla okunur — hangi yönde o bölge gölgede kalıyorsa
           kılavuza "yüz okunurluğu için ışık yönü" satırı iner; yoksa
           inmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Dünya görünüşü** — gökyüzü gradyanı, ufuk, arazi doku hiyerarşisi, gök cisimleri, atmosferik perspektif, paralaks | World Bible'ın yazım kılavuzu yok; ortam kartı fizik yazıyor, görünüş tek satır; gökyüzü tek sıfatla yazılıyor; gök cismi ve biyom kayması defterde beş aday (31·32·50·70·71) + D48 · D145; "fon levhası" okumasının değişkeni hiç sorulmadı | Yeni kılavuz §1 DÜNYA ARKETİPİ · §2 gökyüzü/ufuk/arazi kalıpları · §3 sürüklenme · REHBERİ §3 kartlarına işaretçi · şablon World Bible bloğu |
| 2 | **Işık senaryosu** — film boyu ışık planı belgesi, güneş yönü ve takvim kilidi, kesmeler arası ışık algısı, vakum ışığı, motorlarda ışık tarifi | Lighting Bible'ın yazım kılavuzu yok; SINEMATOGRAFIK §1 psikoloji tablosu; ⑪ ölçüyor ama yazım tarafı yok; defterin en büyük kümesi (8 aday) + D47 · D104 · D193 · D201; ışık takvimi son üç filmde üç kez yeniden icat edildi | Yeni kılavuz §1 IŞIK PLANI satırları · §2 gölge yönü/boyu kalıpları · §3 vakum ışığı · §4 motor tarifi · ⑪ rubriğine işaretçi · şablon Lighting Bible bloğu |
| 3 | **Yüz ve kast** — milliyetsiz yüz sözlüğü, kaskta tanımayı taşıyan bölge, kanal boyu çeşitlilik, motorlarda kimlik sürüklenmesi | Yüz tarifi tek kalıp; milliyet ⑯'da BLOCK ama ikame sözlüğü tek satır; D79 yüzü en açık kimlik yüzeyi yaptı; ADAY-16 (kimlik/cinsiyet değişimi) · ADAY-61 (işaret atlaması) · D16 kapısız; hangi yüz özelliğinin motorda önce kaydığı hiç ölçülmedi | Yeni kılavuz §1 YÜZ SÖZLÜĞÜ · §2 kask penceresi kuralı · §3 kast çeşitliliği · §4 sürüklenme · SAHNE_DEVAMLILIK §2.1 + POLİTİKA §2'ye işaretçi · şablon Character Bible bloğu (yüz satırı) |
| 4 | **Araç ve iç hacim** — gemi/gezici/iniş aracı dış yüzey dili ve arketipleri, kabin/kokpit/koridor "yaşanmış" okuması, iç-dış tutarlılık, motorlarda oyun-görünümü | Vehicle Bible yok; hull sıfatları konumsal, malzeme yok; UZAY_USSU gemi için iki ölçek satırı, §9 ① iç cetvel açık; UZAY_SENARYO §5 dramaturji; ADAY-54 (gemi modeli morph) · ADAY-69 (kule morph) · D32; "sleek/futuristic" kelimelerinin maliyeti ölçülmedi | Yeni kılavuz §1 ARAÇ ARKETİPİ · §2 dış yüzey dili · §3 İÇ HACİM tablosu · §4 sürüklenme · UZAY_USSU §4/§9 ①'e işaretçi · ⬜ şablona Vehicle Bible satırı (sahip kararı) |

> ⚠️ **1 ile 2, 1 ile 4, 2 ile 4, 2 ile 3 birbirini denetler** (yukarıdaki
> çapraz okuma). Bir raporun getirdiği eşik ötekinde tutmuyorsa kılavuza
> ancak ⬜ HİPOTEZ etiketiyle iner, sayısız iner.

---

# 1️⃣ DÜNYA GÖRÜNÜŞÜ — gökyüzü, ufuk, arazi ve gök cisimleri nasıl "gerçek yer" okunur, nasıl sabit kalır

```
1968'den bugüne sinema ve prestij dizilerinde TASARLANMIŞ gezegen yüzeyi ve gökyüzü dünyalarının (2001: A Space Odyssey, Alien, Dune 1984 ve 2021, Prometheus, Interstellar, The Martian, Arrival, Ad Astra, Moon, Oblivion, Blade Runner 2049'un dış mekânları, The Expanse, For All Mankind, Foundation, Star Wars'un çöl ve buz gezegenleri ve benzerleri) yapım tasarımcısı, VFX süpervizörü, matte painting sanatçısı ve görüntü yönetmeni tanıklıklarını topla: her dünya için belgelenmiş NİYET (hangi hikâye tonu), gökyüzünün rengi ve gradyanı, ufuk yüksekliği ve eğriliği, gök cisimlerinin (güneş, ikinci güneş, ay, halka, gezegen diski) sayısı, boyutu ve konumu, arazi doku hiyerarşisi (yakın taş, orta kum, uzak sırt), atmosferik perspektifin var ya da yok kararı ve bilerek yapılan fiziksel sapmalar — kaynak, tarih ve tür ile; tablo film adı silinince de okunabilsin.
İzleyicinin bir manzarayı "gerçek yer" ile "fon levhası, oyun haritası, stok render" olarak ayırmasını hangi görsel değişkenlerin belirlediğini araştır — derinlik katmanı sayısı, paralaks, atmosferik perspektif gradyanı, ufuk çizgisinin kadrajdaki yüksekliği, gök cismi ölçeği, yakın plandaki doku ölçeği (görünen taş boyu), tekrar eden doku ("tiling"), gökyüzü ile zemin arasındaki değer kontrastı — algı psikolojisi, VFX ve matte painting pratiği ile varsa ölçüm; her iddiaya kaynak ve etiket.
Devamlılık pratiğini sök: film ve dizi yapımlarında gökyüzü, güneş konumu, gök cisimleri ve arazi biyomunun sahneden sahneye sabit tutulması için tutulan belgeler (sky chart, sun path, horizon lock, biome map, matte painting bible), hangi öğelerin devamlılık hatasına en açık olduğu, izleyicinin gökyüzü ya da arazi değişimini fark etme oranına dair çalışma; iki yönlü sor — bilerek değiştirilen gökyüzünün anlatı aracı olduğu belgelenmiş vakalar ile istemsiz değişimin "sahte" okunduğu eleştiri vakaları, eleştirinin kendi sözcükleriyle.
Yapay zekâ görüntü ve video motorlarına (Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzerleri) geç: gökyüzü, ufuk, arazi ve gök cismi tarifinde hangi kelime ve cümle biçimlerinin ("flat black sky", "pale beige sky", "one small moon high on the right", "fine grey regolith with fist-sized rocks", "no haze") ardışık üretimler arasında sabit tuttuğu, hangilerinin her üretimde değiştiği (gök cismi sayısı ve konumu, biyom, ufuk yüksekliği, atmosferik pus, gökyüzü gradyanı), ölçülmüş ya da sistematik gözlemlenmiş sürüklenme davranışı motor sürümü ve tarihiyle; tek sıfatlı gökyüzü tarifi ile çok katmanlı tarifin karşılaştırmalı tutarlılığı ve iki yönlü: sade tek sıfatın daha iyi tuttuğu vakalar da istenir.
Kritik kısıt: hedef filmler on saniyelik kesmesiz sabit kamera planlarıdır, her klip başka belgeye atıf yapmayan tek prompttan üretilir ve dünya tarifi o promptun dar bandından pay alır, ortam fiziği (vakum, ince atmosfer, kalın atmosfer, kriyojenik) ayrı kartlarda zaten kilitlidir ve sorulmuyor, gökyüzünde okunur yazı, HUD ve gerçek Dünya coğrafyası adı bulunamaz, derece ve metre sayısı prompt gövdesine yazılmaz, güneş ekranın soluna ya da sağına kilitlenir ve film boyunca geri dönmez, biyom sahneler arasında değişmez — bu yüzden yıldız haritası, aurora, çok cisimli gösteriş ya da her sahnede farklı biyom öneren çözümleri işaretleyip ele; az öğeyle uzun klip dizisinde sabit kalan dünyaları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) DÜNYA ARKETİPİ tablosu — arketip, film adsız gökyüzü tarifi (gradyan, cisimler), ufuk ve arazi tarifi, atmosferik perspektif kararı, eşlendiği hikâye tonu, tasarımcı gerekçesi, izleyici okuması, İngilizce tek satırlık World Bible kalıbı, kaynak ve etiket; (b) "GERÇEK YER" değişken tablosu — değişken, gerçek yöndeki değeri, levha yöndeki değeri, devrildiği eşik, kaynak ve etiket; (c) SÜRÜKLENME tablosu — dünya öğesi, kayma sırası ve oranı, motor, önleyen tarif biçimi, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 2️⃣ IŞIK SENARYOSU — film boyu ışık planı nasıl yazılır, kesmeler arası ışık nasıl tutulur

```
Görüntü yönetmenlerinin ve gaffer'ların bir filmin tamamı için tuttuğu ışık planı belgelerini araştır (lighting plot, sun path chart, key direction log, color script ve renk sıcaklığı takvimi, practicals envanteri, pozlama planı): hangi bilgilerin sahne başına zorunlu tutulduğu, tek sert kaynaklı filmlerde (uzay, çöl, kutup, gece dış) ana ışık yönünün kesmeler arasında nasıl korunduğu, zamanın geçişini gösteren ışık takviminin (güneş yüksekliği, gölge boyu, renk sıcaklığı kayması) nasıl planlandığı ve set ile post arasında nasıl devredildiği — 2001: A Space Odyssey, Gravity, Interstellar, The Martian, First Man, Ad Astra, Moon, Sunshine, Dune, Mad Max: Fury Road ve benzerlerinin belgelenmiş uygulamaları, kaynak, tarih ve tür ile.
Kesmeler arası ışık sürekliliğinin algısını ölç: izleyicinin ana ışık yönü değişimini (örneğin saat 10'dan saat 2'ye), renk sıcaklığı ve pozlama sıçramasını, kaybolan pratik kaynağı (sönen lamba, biten şerit) fark etme eşiği, ışık sürekliliği hatasının "sahte, kolaj, yapay zekâ" okumasına katkısı, değişim körlüğü literatürünün ışık ve gölgeye uygulanmış deneyleri — hakemli ölçüm ile devamlılık süpervizörü pratiği ayrı sütunlarda, örneklem ve etki büyüklüğüyle.
Vakum ve ince atmosfer ışığını ayrıca sök: havasız ortamda tek güneşin ürettiği keskin terminatör, albedo dolgusu (yüzeyden ve gövdeden yansıyan ikincil ışık), volumetrik saçılmanın yokluğu, gölgede detayın kalıp kalmadığı, Dünya-parıltısı ve gezegen ışığı gibi ikincil kaynakların rengi ve gücü — Apollo, ISS ve sonda fotoğrafçılığındaki ölçülmüş değerler ile sinemanın bilerek yaptığı sapmalar (gölgeye dolgu, yüzü açan gizli kaynaklar, yıldız alanının pozlanması), uzman ve genel izleyicinin hangisini fark etmediği hangisini "sahte" okuduğu.
Yapay zekâ görüntü ve video motorlarına (Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzerleri) geç: ışık yönünü, gölge yönünü, renk sıcaklığını ve pozlamayı ardışık kliplerde sabit tutan tarif biçimleri (saat kadranı, "shadows fall from left to right", Kelvin değeri, gölge boyunun gövdeye oranı, "no fill in the shadow side", pratik kaynak sayısı) ile hangi biçimin ölçülmüş ya da sistematik gözlemlenmiş tutarlılık verdiği, referans karesinin ışığı ile metnin ışığı çeliştiğinde hangisinin kazandığı, "volumetric", "god rays", "glow", "cinematic lighting", "dramatic lighting" gibi kelimelerin havasız sahnede ürettiği arıza — motor sürümü ve tarihiyle, iki yönlü: derece ve Kelvin yazmanın kadrajda sayı ya da HUD bastığı vakalar ile sayının hiç sorun çıkarmadığı vakalar.
Kritik kısıt: hedef filmler on saniyelik kesmesiz sabit planlardır, her prompt tek başına çalışır ve ışık cümlesi dar bir metin bandından pay alır, derece ve Kelvin sayısı plan belgesinde durur ama prompt gövdesi gölge yönü ve gölge boyuyla yazılır, kask içi yüz ışığı ayrı bir kılavuzda zaten çözülmüştür ve sorulmuyor, ışık psikolojisi tablosu ve renk sıcaklığı haritası zaten vardır ve sorulmuyor, "glow" ve "bloom" kelimeleri yasaktır, en parlak kaynak figürün yönünü çeker ve bu bilinmektedir, ışık yalnız planlı sahne sınırında değişebilir — bu yüzden sahne başına yeniden tasarlanan atmosferik ışık, çok kaynaklı stüdyo düzenleri ve renk sıçramasını stil sayan çözümleri işaretleyip ele; tek kaynak ve monoton takvimle uzun klip dizisini tutanları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) IŞIK PLANI tablosu — belge ya da satır adı, sahne başına tutulan bilgi, tek kaynaklı filmde nasıl kilitlendiği, İngilizce tek satırlık Lighting Bible kalıbı, kaynak ve etiket; (b) SÜREKLİLİK ALGISI tablosu — değişken (yön, sıcaklık, pozlama, pratik kaynak), fark edilme eşiği, "sahte" okumaya katkısı, kaynak ve etiket; (c) MOTOR tablosu — tarif biçimi, tutarlılık, kadrajda sayı basma riski, havasız sahne arızası, motor, kaynak; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 3️⃣ YÜZ VE KAST — milliyetsiz ve ünlüsüz yüz sözlüğü, kaskta tanımayı taşıyan bölge, kanal boyu çeşitlilik

```
Kast yönetmenleri, karakter tasarımcıları, adli portre (composite) uzmanları ve yüz tanıma araştırmacılarının bir yüzü milliyet, etnik köken ve ünlü benzerliği kullanmadan tarif etmek için kullandığı sözlükleri topla: yaş belirteçleri (deri dokusu, kırışıklık bölgeleri, saç grileşmesi), yüz biçimi ve oranları, ten tonu ölçekleri (Monk, Fitzpatrick, Pantone SkinTone ve benzerleri) ile bunların metinsel karşılıkları, göz-kaş bölgesi, burun ve çene tarifleri, saç ve tekil işaretler (yara, ben, leke, asimetri) — hangi sistem hangi alanda standarttır, kaynak, tarih ve tür ile.
Yüz tanıma ve bellek araştırmasından ölç: insanların bir yüzü tanımasında iç özelliklerin (göz, kaş, burun, ağız dizilimi) dış özelliklere (saç, yüz dış hattı) göre ağırlığı, saçın güçlü ama kararsız bir ipucu olduğu bulgular, yüz belleğinde "ayırt edici, hatırlanır" yüzü ortalama yüzden ayıran ölçülmüş değişkenler, kask, bere ya da şapka ile saç ve dış hat kapatıldığında tanımanın hangi özelliklere kaydığı, aynı yüzün farklı ışık yönlerinde tanınma kaybı — hakemli çalışmalar, örneklem ve etki büyüklüğüyle.
Sinema ve dizi kast pratiğini iki yönlü sor: uzun seriler ve çok karakterli yapımlarda yüzlerin birbirine karışmaması için kast ve makyaj departmanlarının uyguladığı ayırt etme ilkeleri (siluet, yaş bandı, ten değeri, saç kütlesi, tekil işaret dağılımı), kask ya da vizör ardında oynayan oyuncuların yüzünü okunur ve tanınır tutmak için alınan tasarım kararları (Gravity, Interstellar, The Martian, First Man, Ad Astra, Moon, For All Mankind, The Expanse ve benzerleri), benzer yüzlü kastın izleyiciyi karıştırdığı belgelenmiş eleştiri vakaları ile sade, ortalama yüzün bilerek seçildiği ve işe yaradığı vakalar.
Yapay zekâ görüntü ve video motorlarına (Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzerleri) geç: metinle tarif edilen bir yüzün ardışık üretimlerde hangi özelliklerinin sabit kaldığı hangilerinin kaydığı (yaş, ten tonu, göz rengi, yüz biçimi, saç, tekil işaret, cinsiyet okuması), kimlik tutarlılığını ölçen benchmark ve değerlendirme çalışmaları, tarif uzunluğu ile tutarlılık ilişkisi, referans karesi ile metnin iş bölümü, milliyet ve ünlü adı kullanmadan ayırt edici yüz üretmenin belgelenmiş tarif biçimleri ve hangi kelimelerin (etnik köken çağrışımlı sıfatlar, ünlü benzerliği, bazı ten tarifleri) güvenlik filtresini tetiklediği — motor sürümü ve tarihiyle, iki yönlü: zengin yüz tarifinin kaymayı artırdığı vakalar ile sade tarifin yine de kaydığı vakalar.
Kritik kısıt: karakter her karede kapalı kask ve berrak düz vizör ardındadır, saç kask içinde büyük ölçüde kapalıdır, yüz tarifi bir kez yazılır ve her prompta kelimesi kelimesine kopyalanır, prompt gövdesinde karakter adı, milliyet, etnik köken, gerçek kişi ve kurum adı bulunamaz, yüz tarifi giysi tarifiyle aynı dar metin bandını paylaşır, filmler çoğunlukla tek kişiliktir ve aynı kanalda onlarca farklı film yayınlanır — bu yüzden saça, kıyafete, aksesuara ya da etnik etikete dayanan ayırt etme çözümlerini işaretleyip ele; kask penceresinin gösterdiği bölgede (kaş, göz, burun, ağız, çene, deri) az kelimeyle ayırt edici ve tutarlı kalan yüzleri öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) YÜZ SÖZLÜĞÜ tablosu — özellik, İngilizce kelime seçenekleri, kaskta görünürlüğü, tanımada ağırlığı, motorlarda tutarlılığı, filtre riski, kaynak ve etiket; (b) KAST ÇEŞİTLİLİĞİ tablosu — ayırt etme ekseni (yaş bandı, ten değeri, yüz biçimi, tekil işaret ve benzeri), bir kanaldaki filmler arasında nasıl dağıtılacağı, kaynak ve etiket; (c) SÜRÜKLENME tablosu — yüz özelliği, kayma sırası ve oranı, motor, önleyen tarif biçimi, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 4️⃣ ARAÇ VE İÇ HACİM — gemi, gezici ve iniş aracının dış yüzey dili; kabin, kokpit ve koridorun "yaşanmış" okuması

```
1968'den bugüne sinema ve prestij dizilerinde TASARLANMIŞ uzay araçlarının, gezicilerin ve iniş araçlarının (2001: A Space Odyssey, Silent Running, Alien, Outland, Moon, Sunshine, Prometheus, Gravity, Interstellar, The Martian, Ad Astra, First Man, Stowaway, The Expanse, For All Mankind ve benzerleri) yapım tasarımcısı, konsept sanatçısı ve model/VFX ekibi tanıklıklarını topla: her araç için belgelenmiş NİYET (endüstriyel yük, bilimsel sonda, askerî, iniş modülü, basınçlı gezici), alınan gerçek referans (Apollo LM, Soyuz, ISS modülü, petrol platformu, denizaltı, kamyon) ve bilerek sapılan yerler, dış yüzey dili (panel çizgisi yoğunluğu, "greeble" tutumu, mat ya da parlak, kir ve yıpranma kararı, tek ayırt edici siluet öğesi) — tablo film adı silinince de okunur biçimde, kaynak, tarih ve tür ile.
İç hacmi ayrı sök: kabin, kokpit, koridor ve hava kilidinin "yaşanmış, kullanılmış gelecek" ile "steril, plastik, oyun menüsü" okumasını hangi değişkenlerin belirlediği (yüzey malzemesi, panel ve düğme yoğunluğu, kablo ve boru görünürlüğü, kişisel eşya ve kir, renk kodlu yerel dikey, ışık kaynağı sayısı ve yerleşimi, pencere sayısı ve biçimi, hacmin dar tutulması), tasarımcı beyanı ile izleyici ve eleştiri okuması ayrı sütunlarda; iki yönlü — steril beyaz iç hacmin bilerek seçildiği ve güçlü okunduğu vakalar ile aşırı kalabalık iç hacmin siluet ve okunurluğu yuttuğu vakalar, eleştirinin kendi sözcükleriyle.
Araç ve iç hacim devamlılık pratiğini araştır: sanat departmanının araç için tuttuğu belgeler (dört görünüş çizimi, panel ve pencere haritası, iç-dış tutarlılık planı — dıştan görülen pencere içten görülenle uyuşur mu), hangi öğelerin devamlılık hatasına en açık olduğu (anten, kapak, panel sayısı, renk, kir), izleyicinin araç biçimi ve iç mekân değişimini fark etme oranına dair çalışma, ve maketin "oyuncak" okunmasını engelleyen yüzey ve ayrıntı kararları — ölçek şahidi ve odak gradyanı dışında kalanlar.
Yapay zekâ görüntü ve video motorlarına (Nano Banana Pro, Nano Banana 2, Veo 3.1, Gemini Omni ve benzerleri) geç: bir aracın dış biçimini ve iç hacmini ardışık kliplerde sabit tutan tarif biçimleri (sayılabilir büyük öğe, tek asimetrik siluet işareti, malzeme + renk kalıbı, "no greebles" türü olumsuz cümle, pencere sayısı, ışık kaynağı sayısı) ile hangi biçimin ölçülmüş ya da sistematik gözlemlenmiş tutarlılık verdiği, "sleek", "futuristic", "sci-fi spaceship", "high-tech cockpit", "holographic" gibi kelimelerin oyun ya da CGI görünümü üretme eğilimi ve hangi kelimelerin (kumaş, kir, boya aşınması, perçin, mat kompozit, kablo kanalı) geri çektiği, tek referans karesiyle çoklu görünüş setinin karşılaştırmalı tutarlılığı — motor sürümü ve tarihiyle, iki yönlü: temiz ve parlak aracın fotogerçekçi tuttuğu vakalar da istenir.
Kritik kısıt: hedef filmler on saniyelik kesmesiz sabit planlardır, her prompt tek başına çalışır ve araç tarifi dar bir metin bandından pay alır, ölçek birimi kasklı gövde boyudur ve metre sayısı prompt gövdesine yazılmaz, istasyon ve üs anatomisi, sayılabilir çapa kuralı, ölçek şahidi merdiveni, maket etkisi ve iç hacmin fiziği ayrı kılavuzlarda zaten kilitlidir ve sorulmuyor, aracın iniş, kalkış ve yanaşma hareketi ayrı kılavuzda çözülmüştür ve sorulmuyor, araç üzerinde okunur yazı, bayrak, logo ve marka bulunamaz, gövdede ve kabinde ekran ile HUD metni yasaktır, giysi için yazılmış malzeme sözlüğü ve global kir kuralı zaten vardır ve yalnız araca taşınıp taşınamayacağı sorulur — bu yüzden neon şeritli, hologramlı, çok ekranlı ve "sleek" çözümleri işaretleyip ele; az ama büyük öğeyle uzun klip dizisini tutan dış ve iç tasarımları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) ARAÇ ARKETİPİ tablosu — arketip, film adsız dış geometri (siluet, panel dili, yüzey, ayırt edici tek öğe), eşlendiği hikâye tonu, tasarımcı gerekçesi, izleyici okuması, İngilizce tek satırlık Vehicle Bible kalıbı, kaynak ve etiket; (b) İÇ HACİM tablosu — hacim tipi (kabin, kokpit, koridor, hava kilidi), malzeme ve yoğunluk kararı, ışık ve pencere düzeni, yerel dikey çözümü, İngilizce tek satırlık kalıp, kaynak ve etiket; (c) SÜRÜKLENME tablosu — araç ya da iç hacim öğesi, kayma sırası ve oranı, motor, önleyen tarif biçimi, oyun-görünümü riski, kaynak ve etiket; ve sonunda iki liste: doğrulanabilir kaynağa dayanan bulgular ile mekanik olarak makul ama kaynaksız iddialar — ikincisini "hipotez" diye işaretle ve neden doğrulanamadığını tek cümleyle yaz.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TUR18_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil; araç kaynak listesini boş
   verirse 00_KUNYE.md'ye yazılır ve yeniden koşuda İSTENİR — TUR 15/17
   dersi). Prompt metinleri her ham dosyanın başına birebir kopyalanır.
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR 18 açılır ve ÜÇ liste yazılır:
   GİRDİ (bulgu · hangi dosyaya · tipi) · GİRMEDİ (bulgu · NEDEN) ·
   GEOMETRİYE ÇEVRİLDİ (film/oyuncu adlı bulgu → adsız geometri ve
   sözlük). Her sayı ÜÇ etiketten birini taşır: ÖLÇÜLMÜŞ · UYGULAMA ·
   ÖNERİ. TUR 3/5/9/12/17'de ve REHBERİ §3, SINEMATOGRAFIK §1'de zaten
   olan bulgular "ZATEN VAR" etiketiyle geçer.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔2 · 1↔4 · 2↔4 · 2↔3). Tutmayan eşik
   kılavuza İNMEZ, çelişki kayda geçer. Özellikle 1↔2: gökyüzü rengi
   ile güneş konumu/renk sıcaklığı tek fizikten çıkmıyorsa iki satır
   da ⬜ HİPOTEZ.
4. Ancak ondan sonra DÖRT kılavuz yazılır (çalışma adları yukarıdaki
   tabloda; her biri TUR 17 kılavuzunun iskeletiyle: değişmeyen
   kararlar · teşhis · arketip/sözlük · kalıplar · sürüklenme · kısaltma
   sırası · reçete + örnek İngilizce blok · ⬜ sınır). Dokunulan yerler
   AYRI iştir ve kart G/P usulüyle işlenir: FILM_KLASOR_SABLONU üç bible
   bloğu (+ ⬜ Vehicle Bible satırı: SAHİP KARARI) · KILAVUZ_REHBERI §1
   tür satırı ve §3 kartlarına işaretçi · SINEMATOGRAFIK §1 ·
   SAHNE_DEVAMLILIK §2.1 · POLITIKA §2 · UZAY_USSU §4/§9 ① · ⑪ IŞIK
   rubriği (D201 kapısı) · yeni-film skill adım 8 · prompt_kontrol
   kapı adayları (TODO'ya).
   ⛔ D47 · D48 · D79 · D104 · D138 · D145 · D201 KARARLARI değişmez;
   kılavuzlar yalnız TARİF BİÇİMİ ve YAZIM SIRASI önerir ve ilk filmde
   ① KARE · ② DEVAMLILIK · ⑪ IŞIK ile sınar.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Yapım tasarımcısı ve görüntü yönetmeni tanıklıkları UYGULAMA
düzeyindedir, hakemli değil; "gerçek yer / yaşanmış hacim" okumasının
izleyici ölçümü muhtemelen seyrektir ve raporlar boşluğu kendi önerisiyle
dolduracaktır — o satırlar ⬜ HİPOTEZ etiketiyle iner. Yüz tanıma
literatürü (2 numaralı cümle) bu turun en sağlam ÖLÇÜLMÜŞ damarıdır ama
kask penceresi koşulu için doğrudan deney beklenmez; oradaki çıkarım
etiketlenir. AI motor ölçümleri topluluk gözlemi ağırlıklı olacaktır;
motor sürümü ve tarih yazılmayan ölçüm inmez. Kılavuza inen hiçbir kalıp
henüz üretimde test edilmedi; ilk uygulamada referans paneli + ① KARE ·
② DEVAMLILIK · ⑪ IŞIK skorlarıyla sınanır.
