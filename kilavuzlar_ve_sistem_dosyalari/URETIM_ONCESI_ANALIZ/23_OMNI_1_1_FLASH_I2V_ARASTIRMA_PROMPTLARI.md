# 🔬 23 — OMNI 1.1 FLASH · GÖRÜNTÜDEN-VİDEOYA ARAŞTIRMA PROMPTLARI (16.09.2026)

> **Ne bu dosya:** OMNI 1.1 Flash ile image-to-video (I2V) üretiminin
> "nasıl yazılır · nasıl hazırlanır · nasıl daha iyi çalışır" tarafı için
> DOKUZ derin araştırma promptu. Her biri **altı cümledir**, her cümle
> **tek satırdır** ve **salt prompt** çalışır — kopyala, araştırma aracına
> yapıştır, başka hiçbir şey verme.
>
> | # | konu | kurulacak kılavuzun bölümü (çalışma adı `OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md`) |
> |:--:|---|---|
> | 1 | **KİMLİK ve YETENEK KÜNYESİ** — resmî ad, sürüm, girdi modları, parametreler, sıralamadaki yeri | §0 KÜNYE · motor kartı satırı |
> | 2 | **PROMPT ANATOMİSİ** — kare varken prompt neyi yönetir: biçim, sıra, uzunluk, şablon | §1 YAZIM KURALLARI · §2 ŞABLONLAR |
> | 3 | **BAŞLANGIÇ KARESİ** — videoyu iyi yapan görüntü: kompozisyon, teknik nitelik, zincir kaybı | §3 KARE KURALLARI (görüntü promptuna iner) |
> | 4 | **HAREKET · ZAMAN · FİZİK** — on saniyeye dağılım, tarif biçimi, beden arızaları | §4 HAREKET |
> | 5 | **KAMERA DİLİ** — kapalı listenin bu modelde uyumu, tek kareden paralaks, sabit kamera | §5 KAMERA |
> | 6 | **KİMLİK ve SÜREKLİLİK** — klip içi kayma, klipler arası zincir, yüz × politika | §6 SÜREKLİLİK |
> | 7 | **SES ve DİYALOG** — replik sözdizimi, dudak senkronu, altyazı riski, katmanlar | §7 SES |
> | 8 | **POLİTİKA ve RED YÜZEYİ** — hangi aşama reddeder, birebir mesaj, uyumlu ikame | `POLITIKA` §6 motor satırı · §8 RED |
> | 9 | **İŞ AKIŞI ve VERİM** — deneme sayısı, teşhis, Flash ödünleşimi, model seçimi | §9 İŞ AKIŞI · `POLITIKA` §6.1 seçim kuralı |
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-22'nin gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin isteği (16.09.2026) — *"omni 1.1 flash video
> modeli için image to video yapmayla ilgili birbirinden farklı 6 satırlık
> derin araştırma promptu: promptlar nasıl olmalı, örnek şablonlar, model
> nasıl daha iyi çalışır."* Motor, depoda en az dört filmin planında adıyla
> geçiyor (THE_SCOURED_GLASS 180 sahne OMNI I2V; LOCKED_PULSE referans
> paketinde imaj motoru adayı). Ama **Veo'nun kılavuzu var, Omni'nin yok**:
> Omni bilgisi beş dosyaya dağılmış tek satırlardan ibaret ve bunların
> çoğu tek kaynaklı ya da sınanmamış:
>
> | depoda bilinen | kaynak | durum |
> |---|---|---|
> | "Osmi" = Gemini Omni (Flash / 1.1 Flash) | 04 §TUR 3 · `POLITIKA` §6 | ⚠️ hipotez — tek tur |
> | "ünlü kişi" yanlış-pozitifi Veo'dan AĞIR; tek pencerede kimlik ≤3-4 öznitelik | red defteri #15 (OMNI **image**) · 04 §TUR 3 · D167 · ⑲ | 1 vaka + tek kaynak |
> | düzenleme odaklı · V2V + ilk/son kare | `POLITIKA` §6 (dış kaynak) | ⚠️ hipotez |
> | replik sözdizimi `Character speaks the line: "..."` | 04 §T13 #11 | KAYNAK (tek rapor) |
> | argo · çığlık · ağlama krizi politika reddi üretebiliyor | 04 §T13 #12 | KAYNAK (tek rapor) |
> | tırnaklı replik → gömülü altyazı 2/2 → `heard only — never shown as text` | YERCEKIMI F4/F5 · D40 | ÖLÇÜLMÜŞ (motor Omni değil) |
> | I2V'de görünüm yeniden tarif edilmez, yalnız hareket/kamera/ışık/ses | `VEO_3_1_FAST` §6B | Veo için yazıldı, Omni'de sınanmadı |
> | eylem öne yığılıyor, son saniyeler boş | TUR 19 → `SAHNE_DOLULUGU_KILAVUZU` | çok motorlu; Omni'ye özgü satır yok |
>
> **AÇIK ÇELİŞKİLER — bu tur kapatmalı:**
> ① **Bitiş karesi:** `POLITIKA` §6 "V2V + ilk/son kare → kesintisiz zincir
>    OMNI" diyor; `THE_SCOURED_GLASS/00_PLAN` "end frame yok (OMNI)" diyor
>    ve 180 sahnelik zinciri buna göre kurdu. İkisi aynı anda doğru olamaz
>    (belki yüzeye/sürüme bağlı) → prompt 1.
> ② **İki nokta üst üste:** 04 §T13 #11 "iki nokta üst üste kullanılmaz —
>    model yazı sanıyor" diyor, ama önerdiği kalıbın kendisi
>    `speaks the line:` iki nokta taşıyor → prompt 7.
> ③ **Seed alanı:** `THE_SCOURED_GLASS_REFERANS_PAKETI` "alanın VAR OLDUĞU
>    önce sınanır [D142]"; referans çağırma söz dizimi ⚙️ SINANMAMIŞ →
>    prompt 1 (var mı) + prompt 9 (işe yarıyor mu).
> ④ **Motor seçim kuralı** (`POLITIKA` §6.1: yüzlü I2V → VEO, zincir →
>    OMNI) iki hipotezin üstüne kurulu: yüz yanlış-pozitifi ve ilk/son kare.
>    İkisi de bu turda sorulur → prompt 6 · 8 · 9.
> ⑤ **Klip süresi** 10,0 s "araçtan ölçülür" [D124]; Omni'nin teslim ettiği
>    gerçek süre hiçbir yerde yazılı değil → prompt 1.
>
> **KOŞU KAYDI:** ✅ **TUR 20 koşuldu — 16.09.2026, aynı gün.** 9/9 rapor
> `TUR20_HAM_RAPORLAR/` (birebir, oturum kaydından programla kesildi) +
> `00_KUNYE.md` §🔎 **canlı kaynak kontrolü** (resmî Google blog + Gemini API
> Omni sayfası) → `04_ARASTIRMA_BULGULARI.md` §TUR 20 (süzme) →
> `../OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md` (sayısız). Çelişki ① bitiş karesi
> VAR · ② sorun iki nokta değil TIRNAK (PROB) · ③ seed resmî API'de belgesiz ·
> ④ §6.1 yarım · ⑤ süre açık. Aşağıdaki ⬜ adaylar 04 §T20.8'e taşındı.
> *(İlk hâli: ⏳ 16.09.2026 yazıldı, koşulmadı.)*
> ⚠️ Kaynak listesi İSTENİR; gelmezse `00_KUNYE.md`'ye yazılır (TUR 15/17
> dersi). Motor adı, sürümü ve tarihi olmayan satır İNMEZ (TUR 12 dersi:
> "Kling 3.0 Omni" bulgusu bu motora karışmıştı — 04 §T12).

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → TUR20_HAM_RAPORLAR/ (birebir) →
         04_ARASTIRMA_BULGULARI.md §TUR 20 (süzme kaydı) →
         OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md (çalışma adı; VEO_3_1_FAST
         kılavuzunun kardeşi) → dokunduğu yerler:
         POLITIKA §6 motor tablosu + §6.1 seçim kuralı (hipotez etiketi
         ya düşer ya kural çöpe gider) ·
         09_URETIM_RED_DEFTERI MOTOR lejandı (resmî ad) ·
         KILAVUZ_REHBERI motor kartı satırı (zincir modu: start / start+end) ·
         REFERANS_PAKETI_KILAVUZU motor satırı (seed · referans çağırma) ·
         IMAGE_VIDEO_PROMPT_TEMPLATES I2V video şablonu (Omni satırı) ·
         SES_VE_DIYALOG §3 motor sözdizimi ·
         prompt_kontrol kapı adayları (Omni sözdizimi · kimlik öznitelik sayısı).
   Süzme kaydı ÜÇ liste tutar: GİRDİ · GİRMEDİ + NEDEN · GEOMETRİYE ÇEVRİLDİ.

⛔ BU ARAŞTIRMA "PROMPT HİLESİ" DEĞİLDİR.
   Aranan şey: bu motorda neyin ÖLÇÜLMÜŞ olarak çalıştığı, neyin
   çöktüğü ve hangi koşulda. "Şu kelimeyi ekle, video sinematik olur"
   diyen ama motor sürümü, tarih, deneme sayısı ve karşı örnek vermeyen
   kaynak süzme kaydına "GİRMEDİ" yazılır. Filtre atlatma tavsiyesi
   (prompt 8) her koşulda GİRMEDİ'dir — aranan politika uyumlu tarif.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — resmî belge · bağımsız benchmark · sistematik test
   (b) UYGULAMA — yapay zekâ film yapımcısı, prompt mühendisi, kullanıcı raporu
   (c) ÖNERİ    — raporun kendi çıkarımı
   Kaynaksız (a) düşer; (b) ancak iki bağımsız uygulayıcı aynı şeyi
   söylüyorsa iner; (c) yalnız ⬜ HİPOTEZ etiketiyle iner.
   TUR 17/19'un dersi: sayı katmanı çürük gelirse kılavuz SAYISIZ yazılır.
   Sürüm tarihi yazılmaz (04 §T12: üç sürüm künyesinin üçü de yanlıştı);
   yalnız sahibin üretim günü arayüzde gördüğü sürüm yazılır.

⛔ MOTOR KARIŞMASI — "Omni" adı en az üç modelde geçiyor.
   Kling (O1 / 3.0 Omni), ByteDance OmniHuman ve benzerlerinin bulgusu
   bu motora YAZILMAZ. Her prompt motor sütunu ister; motor sütunu boş
   ya da başka model olan satır Omni kılavuzuna inmez, en fazla
   "karşılaştırma" sütununa girer. Resmî ad doğrulanamazsa 04 §TUR 3
   hipotezi KALIR ve kılavuzun başlığına yazılır.

⛔ ÖNCEKİ TURLARLA VE MEVCUT KILAVUZLARLA ÇAKIŞMA ("ZATEN VAR").
   • I2V'de görünümün yeniden tarif edilmemesi → VEO §6B · REFERANS §5.2.
     2 bunu KURAL olarak değil SORU olarak sorar (Omni'de sınanmadı);
     iki yönlü: yeniden tarifin işe yaradığı vaka da istenir.
   • Eylemin öne yığılması, fiil sınıfı, 10 s iskeleti, dolgu kaynakları
     → TUR 19 · SAHNE_DOLULUGU_KILAVUZU. 4 yalnız OMNI'YE ÖZGÜ davranışı
     sorar; genel zanaat ve senaryo birimi sorulmaz.
   • Kamera hareketi kapalı listesi → TEMPLATES. 5 listeyi değiştirmeyi
     değil listenin bu motorda nasıl yazıldığını sorar.
   • Kimlik ≤3-4 öznitelik [D167 · ⑲] · FACE LOCK · SINGLE CHARACTER ·
     vizör optik berrak [D79] → prompt_kontrol. 6 ve 8 eşiğin Omni'de
     DOĞRULANMASINI sorar, yeniden tanımlamasını değil.
   • Replik azlığı · tek insan · kapalı vizörde replik post'ta · MCU
     lip-sync tabanı · 20-25 kelime / 10 s → SES_VE_DIYALOG · 04 §T13.
     7 bunları KISIT olarak verir, sözdizimini ve senkron eşiğini sorar.
   • Politika yüzeyinin genel haritası, milliyet reddi, tehlike çerçevesi
     kelimeleri → TUR 3 · POLITIKA §1-§5. 8 yalnız I2V AŞAMASINI (girdi
     görseli / prompt / çıktı) ve Omni ↔ Veo farkını sorar.
   • Deponun ölçülmüş KARARLARI promptlarda kısıt olarak durur: tek sahne
     tek kilit, SAYIYLA · pozitif gövde 120-300 kelime · yüzeyde okunur
     yazı yok [D34 · D45] · "glow/bloom" yasak [D3 · D29] · klip içinde
     durum değişimi yok (KILAVUZ_REHBERI §7) · "still / motionless /
     frozen" tek başına yasak (OYUNCULUK §4).
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Omni yüzde Veo'dan katı", "Omni'de ilk/son kare var", "tohum aynı
   sonucu verir", "maintain the subject… çapası kaymayı azaltır",
   "kamera cümlesi başta daha iyi tutar", "iki nokta yazı üretir" bu
   deponun ADAYLARIDIR — dokuz prompt da İKİ YÖNLÜ yazıldı (çalıştığı ve
   çöktüğü vakalar birlikte istenir). Üretim kısıtları hipotez değil
   FİLTREDİR ve her promptun beşinci cümlesinde açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — altı çift.
   1 ↔ 9 : 9'un iş akışı 1'in "yok / belirsiz" dediği bir özelliği
           (seed, bitiş karesi, extend) kullanıyorsa o adım inmez.
   2 ↔ 3 : aynı kural hem prompta hem kareye yazılabiliyorsa (ışık,
           kompozisyon) 3 kazanır — kare onaylıdır, video promptu kareyi
           değiştiremez; 2'deki karşılığı "çelişme yasağı"na döner.
   4 ↔ 5 : 5'in "sabit kamera tekniği" 4'e göre özneyi de donduruyorsa
           teknik "yan etkili" etiketiyle iner; tek başına kural olmaz.
   6 ↔ 8 : yüz yanlış-pozitifi eşiği ikisinde de aynıysa iner; farklıysa
           ⬜ HİPOTEZ kalır ve POLITIKA §6.1 değişmez.
   7 ↔ 8 : 7'nin önerdiği ses tarifi 8'e göre red tetikliyorsa (çığlık,
           ağlama) tarif iner ama "red riskli" etiketiyle.
   2 ↔ 7 : tırnak ve iki nokta kuralı ikisinden aynı gelmezse ÇELİŞKİ ②
           açık kalır ve karar PROB koşusuna gider (2 kliplik A/B).
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Künye** — resmî ad, sürüm, modlar, parametreler, sıralama | "Osmi" kimliği tek tur hipotez; bitiş karesi var mı (ÇELİŞKİ ①); seed alanı var mı (③); gerçek klip süresi (⑤) | Kılavuz §0 · POLITIKA §6 · red defteri lejandı · KILAVUZ_REHBERI motor kartı |
| 2 | **Prompt anatomisi** — yeniden tarif, biçim, sıra, uzunluk, şablon | VEO §6B kuralları Omni'de sınanmadı; Omni için şablon yok; 120-300 kelime bandının Omni'de karşılığı bilinmiyor | Kılavuz §1-§2 · TEMPLATES I2V Omni satırı |
| 3 | **Başlangıç karesi** — kompozisyon, teknik nitelik, gelecek bilgisi, zincir kaybı | Kare kuralları imaj kılavuzlarında motor-bağımsız; I2V'yi bozan kare özelliği ölçülmedi; son kareden devam zincirinin nesil kaybı bilinmiyor | Kılavuz §3 · imaj promptu şablonu · REFERANS_PAKETI |
| 4 | **Hareket · zaman · fizik** | TUR 19 çok motorlu; Omni'nin damga uyumu ve düşük yerçekimi/giysi içinde beden arızası bilinmiyor | Kılavuz §4 · SAHNE_DOLULUGU motor satırı |
| 5 | **Kamera** | Kapalı listenin Omni uyumu ölçülmedi; sabit kameranın yan etkisi bilinmiyor | Kılavuz §5 · TEMPLATES kamera satırı |
| 6 | **Kimlik ve süreklilik** | 180 klipli zincirde yüz/giysi kayması; kimlik eşiği ≤3-4 Omni'de tek vaka | Kılavuz §6 · ⑲ eşiği · REFERANS_PAKETI |
| 7 | **Ses ve diyalog** | ÇELİŞKİ ②; Omni lip-sync eşiği; kapalı vizörde ne üretir; ses sürekliliği | Kılavuz §7 · SES_VE_DIYALOG §3 · DIALOGUE_CRITIQUE |
| 8 | **Politika ve red** | Red hangi aşamada (görsel / prompt / çıktı); Omni ↔ Veo farkı tek kaynak; bölge ayarı (04 §TUR 3 ②) | POLITIKA §6 · §6.1 · red defteri |
| 9 | **İş akışı ve verim** | Deneme başına kabul oranı, teşhis sırası, Flash ↔ Veo seçim kuralı (ÇELİŞKİ ④) | Kılavuz §9 · POLITIKA §6.1 · FAZ şablonu üretim notu |

---

# 1️⃣ KİMLİK ve YETENEK KÜNYESİ — Omni 1.1 Flash tam olarak nedir, I2V'de neyi destekler

```
Google'ın Flow ve Gemini ortamında Veo'nun yanında sunulan, arayüzde "Omni 1.1 Flash" adıyla seçilen video modelinin (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretim künyesini çıkar: resmî ad ve model ailesi, 1.0 / 1.1 ve Flash / daha büyük kardeş sürümler arasındaki farklar, hangi yüzeylerden erişildiği (Flow, Gemini uygulaması, Gemini API, Vertex AI) ve yüzeye göre değişen özellikler — resmî model kartı, sürüm notları, geliştirici belgeleri ve Google / DeepMind duyuruları öncelikli, bağlantı ve tarihle.
Görüntü girdisinin kabul edildiği bütün modları ayrı ayrı sök: yalnız başlangıç karesi, başlangıç ve bitiş karesi (interpolasyon), çoklu referans görseli (karakter, nesne, mekân — kaç görsel, hangi rolle, promptta nasıl çağrıldığı), videodan-videoya düzenleme, uzatma (extend) ve son kareden devam — her modun hangi yüzeyde ve sürümde bulunduğunu, bulunmadığını ve kullanıcı raporlarında birbiriyle çelişen iddiaları (özellikle bitiş karesinin bu sürümde olup olmadığı) açıkça yaz.
Üretim parametrelerini topla: seçilebilen klip süreleri ve gerçekte teslim edilen süre, çözünürlük ve kare hızı, en-boy oranları (16:9, 9:16) ve girdi görselinin oranı farklıysa ne olduğu (kırpma, dolgu, dış boyama), yerel ses üretimi ve kapatılıp kapatılamadığı, tohum (seed) alanının var olup olmadığı ve aynı tohumun aynı sonucu verip vermediği, negatif prompt alanı, prompt uzunluk sınırı, istek başına varyasyon sayısı, kredi ya da ücret bedeli ve kotalar.
Modeli bağımsız ölçümlerle konumlandır: Artificial Analysis Video Arena (görüntüden-videoya), VBench-I2V ve benzeri benchmark ve kör karşılaştırma sıralamalarında Veo 3.1, Veo 3.1 Fast, Kling, Sora 2, Runway, Hailuo ve Seedance'e göre yeri; resmî belgenin güçlü dediği alanlar ile kullanıcıların sistematik olarak bildirdiği zayıf alanlar (düzenleme mi üretim mi, hareket mi görünüş sadakati mi, ses mi görüntü mü) — iki yönlü, övgü ve şikâyet ayrı sütunlarda.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır (2 ile 30 dakika arası filmler, 12 ile 180 klip) — bu yüzden hatta kullanılmayan yetenekleri (metinden-videoya, stil aktarımı, çok çekimli üretim) silme ama "hat dışı" diye işaretle, ve yalnız denemeyle ölçülebilecek iddiaları (tohumun tekrar üretilebilirliği, gerçek klip süresi, bitiş karesi desteği) "sınanmalı" diye ayır.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KÜNYE tablosu — özellik, değer, sürüm, yüzey, kaynak bağlantısı, etiket (ÖLÇÜLMÜŞ: resmî belge ya da bağımsız ölçüm · UYGULAMA: kullanıcı ya da uygulayıcı raporu · ÖNERİ: senin çıkarımın); (b) GİRDİ MODU tablosu — mod, var / yok / belirsiz, sınırı, promptta çağrılış biçimi (İngilizce), kaynak ve etiket; (c) KARŞILAŞTIRMA tablosu — ölçüt, Omni 1.1 Flash, Veo 3.1 Fast, en güçlü rakip, kaynak; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — resmî adı doğrulayamazsan bunu açıkça yaz, en yakın adayları gerekçeyle sırala, sürüm adı uydurma ve adında "Omni" geçen başka modellerin (Kling Omni, OmniHuman ve benzerleri) bulgusunu bu modele yazma.
```

---

# 2️⃣ PROMPT ANATOMİSİ — başlangıç karesi varken prompt neyi yönetir, hangi biçimde yazılır

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde promptun nasıl yazılması gerektiğini araştır: Google'ın resmî prompt rehberleri (Flow, Gemini API ve Vertex AI video prompt kılavuzları, model kartı örnekleri), Google'ın yayınladığı örnek promptlar, sistematik test yapan prompt mühendislerinin ve yapay zekâ film yapımcılarının belgelenmiş karşılaştırmaları — model sürümü, tarih ve kaynakla.
Başlangıç karesi varken promptun görevini sök: karede zaten görünen öğeleri (özne görünüşü, giysi, mekân, ışık) yeniden tarif etmenin kimliği güçlendirip güçlendirmediği ya da yeniden üretimi tetikleyip kaymaya yol açtığı, yalnız hareket + kamera + ışık değişimi + ses yazmanın sonucu, "the scene begins exactly as the provided image" ya da "maintain the subject from the first frame" türü çapa cümlelerinin etkisi, prompt ile kare çeliştiğinde modelin hangisine uyduğu ve çelişkinin kaçıncı saniyede görünür hâle geldiği — iki yönlü, yeniden tarifin işe yaradığı vakalar dâhil.
Biçimi ve sırayı karşılaştır: akıcı düz paragraf, etiketli bölümler (Camera: / Action: / Audio:), JSON ya da yapılandırılmış prompt, zaman damgalı satırlar, madde işaretleri; cümle sırası (kamera cümlesi başta mı sonda mı, özne mi eylem mi önce), prompt uzunluğunun (yaklaşık 30, 80, 150, 300 kelime) uyuma ve artefakta etkisi ve modelin uzun promptun sonunu okuyup okumadığı, olumsuz cümlelerin ("no", "without", "avoid") prompt içinde mi ayrı alanda mı işe yaradığı, tırnak işaretinin ve iki nokta üst üstenin ekranda yazı üretme riski.
Hazır şablonları topla ve sına: resmî ya da yaygın görüntüden-videoya kalıpları (örneğin kamera + özne eylemi + ortam hareketi + ışık değişimi + ses sırası), "cinematic, 8k, masterpiece, highly detailed" türü nitelik yığınlarının bu modelde işe yarayıp yaramadığı ya da zarar verip vermediği, lens, film stoku, renk derecelendirme ve yönetmen ya da film adı gibi film dili kelimelerinin etkisi; her şablonun hangi sahne tipinde (sessiz eylem, konuşma, manzara, yakın plan, nesne) denendiği ve sonucu, iki yönlü.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır; pozitif metin bandı yaklaşık 120-300 kelimedir, her prompt başka belgeye atıf yapmadan tek başına okunur, her sahnede tek bir sayılı hareket kilidi vardır, kadrajda okunur yazı ve arayüz öğesi olamaz, "still / motionless / frozen" tek başına yazılmaz — bu yüzden sonradan düzenleme, maske, çoklu çekim ya da bant dışı uzunluk gerektiren önerileri işaretleyip ele, tek promptla uygulanabilir yazım kurallarını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) YAZIM KURALI tablosu — kural, mekanizma, bozulunca ne olur, İngilizce doğru ve yanlış örnek çifti, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) BİÇİM tablosu — biçim (düzyazı / etiketli / JSON / damgalı), uyum, artefakt, uygun uzunluk aralığı, kaynak ve etiket; (c) ŞABLON tablosu — sahne tipi, köşeli parantezli yuvalarla İngilizce tam şablon, doldurulmuş tek örnek, denendiği sürüm, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin (Veo, Kling Omni ve benzerleri) bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 3️⃣ BAŞLANGIÇ KARESİ — videoyu iyi yapan görüntü nasıl hazırlanır

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde BAŞLANGIÇ KARESİNİN kendisinin videonun kalitesini nasıl belirlediğini araştır: hangi görüntü özelliklerinin hareketi, kimlik korumasını ve fizik tutarlılığını iyileştirdiği ya da bozduğu — resmî belgeler, girdi karesinin çıktıya etkisini ölçen görüntüden-videoya araştırmaları, storyboard'dan video üreten ekiplerin ve yapay zekâ film yapımcılarının sistematik testleri; sürüm, tarih ve kaynakla.
Kompozisyonu sök: öznenin kadrajdaki yeri ve hareket yönündeki boş alan, kadraj kenarına yakın ya da kırpılmış uzuvların ve nesnelerin videoda nasıl tamamlandığı, pozun eylemin ortasından mı durağan anından mı seçilmesi gerektiği, çekim ölçeği (geniş, orta, yakın, makro) ile artefakt arasındaki ilişki, arka plandaki ince ve tekrarlayan ayrıntıların (kablo, panel, ızgara, perçin) hareketle erimesi, alan derinliğinin ve bulanık arka planın etkisi.
Görüntünün teknik niteliğini sök: çözünürlük ve en-boy oranının çıkış oranıyla uyuşmaması, sıkıştırma artefaktı, aşırı keskinleştirme ve aşırı ayrıntı, pozlama ve dinamik aralık (patlamış parlak alanlar, ezilmiş gölgeler, yansıtıcı kask vizörü), fotoğraf görünümlü ile render görünümlü karenin farkı, karenin aynı aileden bir görüntü modeliyle (Nano Banana Pro, Nano Banana 2) mi başka bir modelle mi üretildiğinin videoya etkisi, karede görünmez filigran bulunmasının davranışa etkisi, karedeki metin ve logoların videoda bozulması.
Karenin taşıdığı "gelecek" bilgisini sor: videoda olacak eylemin başlangıç karesinde nasıl hazırlanması gerektiği (elin nesneye mesafesi, bakış yönü, gövde ağırlığının dağılımı), karede görünmeyen bir şeyin (kadraj dışı nesne, arkası dönük yüz, kapalı bir kapak) video sırasında ortaya çıkarılmasının güvenilirliği, iki klip zincirlenirken önceki klibin son karesini yeni başlangıç karesi yapmanın nesiller boyunca kalite kaybı (renk kayması, keskinlik düşüşü, yüz sürüklenmesi) ve onu önleme yolları — iki yönlü, işe yarayan ve çöken vakalarla.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde üretilip onaylanan tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır; video promptu kareyi değiştiremez ve kare kuralları görüntü promptuna yazılır, kask vizörü optik olarak berrak ve yüz okunur olmak zorundadır, kadrajda okunur yazı, gösterge ekranı ve logo yoktur, klip içinde durum değişimi (kapak açılır, lamba yanar) güvenilmezdir ve kesmeye yazılır — bu yüzden videoda maske, sonradan kompozit, bitiş karesi ya da el ile rötuşla çözülen önerileri işaretleyip ele, görüntü promptuna yazılabilecek kare kurallarını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KARE ÖZELLİĞİ tablosu — özellik, videoya etkisi (hareket / kimlik / fizik / artefakt), iyi değer ya da kural, kötü değer, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) ÇEKİM ÖLÇEĞİ tablosu — ölçek, artefakt riski, yüz ve el sadakati, bu ölçeğe uygun eylem tipi, kaynak ve etiket; (c) KARE KONTROL LİSTESİ — kareyi videoya göndermeden önce sorulacak evet / hayır soruları ve "hayır" cevabının öngördüğü arıza, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 4️⃣ HAREKET · ZAMAN · FİZİK — on saniyelik klipte eylem bu modelde nasıl yazılır

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde hareketin, zamanlamanın ve fiziğin promptla ne ölçüde yönetilebildiğini araştır: eylemin klip süresine dağılımı (ilk saniyelere yığılma, erken bitip donma, döngüye girme, uydurulmuş yeni eylem), hız ve tempo kelimelerinin etkisi, bir klipte kaç ardışık eylemin güvenle yapılabildiği — bu modele özgü testler, bağımsız değerlendirmeler ve sistematik kullanıcı raporları; sürüm, tarih ve kaynakla, başka modellerin bulgusu ayrı sütunda.
Tarif biçimlerini bu modelde karşılaştır: zaman damgalı satırlar ("0-3s … 3-7s … 7-10s"), "first … then … finally" sıralaması, süre ve oran beyanı ("over the full ten seconds", "one step every two seconds"), süreç fiilleri ("keeps hauling", "works the latch loose") ile noktasal fiiller ("grabs", "turns"), "slowly / gradually / steadily" gibi hız zarfları, ikincil hareket cümleleri (nefes, kumaş, kablo, toz, gölge) — her birinin klibin 5-10. saniyelerine uyumu ve artefakt bedeli, ölçülmüş ya da sistematik gözlemlenmiş.
Fizik ve beden arızalarını sök: ayak kayması, yere değmeyen yürüme ve süzülme, el ve parmak bozulması, tutan elin nesneden geçmesi, nesnenin belirip kaybolması, ağırlık ve momentum hissi, kumaş, kablo ve toz davranışı, düşük yerçekimi ya da ağırlıksızlık istendiğinde ne üretildiği, kalın eldiven ve sert giysi içinde beden hareketinin inandırıcılığı; hangi prompt biçiminin hangi arızayı artırdığı ya da azalttığı ve fiziği tarif eden kelimelere ("heavy", "braced", "momentum", "low gravity", "slow arc") modelin verdiği tepki.
İki yönlü uygulayıcı çözümlerini topla: eylemin ortasından seçilen başlangıç karesi, tek eylemi yavaşlatıp bütün klibe yaymak, klibe ikinci bir sürekli süreç eklemek, negatif cümlelerin harekete etkisi ("no sudden movements", "no morphing"), aynı promptla çoklu deneme alıp seçmek, uzatma zinciri; hangisinin bu modelde işe yaradığı, hangisinin donmuş özne ya da aşırı ve amaçsız hareket ürettiği, ve "hiçbir şey olmayan" tutulmuş bir planın bu modelde canlı kalıp kalmadığı.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli uzay bilimkurgu planlarıdır; karakter basınç giysisi, kask, eldiven ve bot içinde hareket eder, sahneler vakumda, ince atmosferde ya da düşük yerçekiminde geçer, her sahnede tek bir sayılı hareket kilidi vardır, klip süresi sabittir, klip içinde durum değişimi (kapak açılır, lamba yanar) güvenilmezdir ve kesmeye yazılır, "still / motionless / frozen" tek başına yazılmaz — bu yüzden klibi kısaltan, ara kesme ekleyen, ikinci karakter getiren ya da klip içi durum değişimi öneren çözümleri işaretleyip ele.
Çıktıyı üç tablo ve iki liste olarak ver: (a) HAREKET BİÇİMİ tablosu — biçim, 0-3 / 3-7 / 7-10 saniye uyumu, artefakt bedeli, İngilizce tek satırlık kalıp, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) FİZİK ARIZASI tablosu — arıza, tetikleyen tarif ya da kare özelliği, önleyen tarif (İngilizce), bu modeldeki sıklığı, kaynak ve etiket; (c) EYLEM KAPASİTESİ tablosu — eylem tipi (yürüme, uzanma, alet kullanma, dönme, çömelme, düşme, ağırlıksız süzülme), güvenilirlik, önerilen yazım, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 5️⃣ KAMERA DİLİ — hareket listesi bu modelde nasıl yazılır, sabit kamera nasıl sabit kalır

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde kamera dilinin promptla ne ölçüde yönetilebildiğini araştır: kamera hareketi terimlerinin (locked-off tripod, slow push-in, pull-back, orbit / arc, tilt, pan, lateral track, crane rise, vertical track, dolly zoom, handheld) uyum oranı ve istenmeyen kamera hareketinin (kilitli kamera istenirken süzülme, zoom, titreme) sıklığı — resmî belgelerde ve arayüzde listelenen kamera kontrolleri, bağımsız testler ve kullanıcı raporları; sürüm, tarih ve kaynakla.
Tek görüntüden kamera hareketinin geometrisini sök: push-in, orbit ve lateral track sırasında paralaksın ve derinliğin nasıl uydurulduğu, başlangıç karesinde görünmeyen alanlar (öznenin arkası, kadraj dışı mekân) açıldığında tutarlılık, hareketin büyüklüğü ile artefakt arasındaki ilişki, kamera hareketi ile özne hareketi aynı anda istendiğinde hangisinin kaybolduğu, hareketin hızını ve mesafesini tarif eden kelimelerin ("slow", "subtle", "half a metre", "over the full ten seconds") etkisi.
Optik ve çekim dili kelimelerini sına: odak uzunluğu ("24mm", "35mm", "85mm"), alan derinliği ve odak kaydırma, çekim ölçeği ve açı (low angle, eye level, overhead, Dutch angle), lens kusurları ve film estetiği (lens flare, anamorphic, film grain) ve bunların istenmeden ışıma, parlama ya da yazı gibi artefakt üretip üretmediği; kamera cümlesinin promptun başında mı sonunda mı daha iyi uyulduğu ve kamera cümlesi hiç yazılmazsa modelin varsayılan davranışı.
İki yönlü uygulayıcı bulgularını topla: sabit kamerayı gerçekten sabit tutmanın belgelenmiş yolları (tekrarlanan beyan, "the camera does not move", tripod ya da güvenlik kamerası çerçevesi, negatif cümle) ve bunların özne hareketini de dondurma yan etkisi; push-in ve orbit'in kimliği ve arka planı bozduğu ya da koruduğu vakalar; yavaş bir kamera hareketinin eylemi biten klibi canlı tutup tutmadığı ve bunun bedeli.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu planlarıdır; kamera hareketi kapalı bir listeden seçilir (fixed lockoff, push-in, pull-back, slow orbit, tilt, lateral track, crane rise, vertical track), varsayılan kilitli tripoddur, bir klipte en fazla tek kamera hareketi vardır, zoom ve klip içi kesme yoktur, kadraj değişimi kesmeye yazılır, "glow / bloom" türü ışıma kelimeleri yasaktır — bu yüzden el kamerası, hızlı kurgu, çoklu çekim ve listede olmayan hareket öneren çözümleri işaretleyip ele, listeyi bu modelde en güvenli yazan kalıpları öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KAMERA HAREKETİ tablosu — terim, uyum, artefakt riski, özne hareketine etkisi, bu modelde en iyi çalışan İngilizce kalıp, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) OPTİK KELİME tablosu — kelime, beklenen etki, gözlenen etki, yan etki, kaynak ve etiket; (c) SABİT KAMERA tablosu — yöntem, sabitlik, özne hareketine yan etkisi, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 6️⃣ KİMLİK ve SÜREKLİLİK — karedeki kişi, giysi ve mekân klip boyunca ve klipler arasında nasıl korunur

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde başlangıç karesindeki kimliğin ve görünüşün klip boyunca ve ardışık klipler arasında ne kadar korunduğunu araştır: yüz, saç, ten, yaş okuması, giysi rengi ve parçaları, kask ve vizör, küçük aksesuarlar, nesne sayısı ve mekân öğelerinin kaç saniye sonra ve hangi koşulda kaydığı — kimlik tutarlılığı benchmark'ları, bağımsız testler ve çok klipli film üreten ekiplerin raporları; sürüm, tarih ve kaynakla.
Klip içi kaymayı tetikleyenleri sök: yüzün dönmesi ya da kadrajdan çıkıp geri girmesi, yüzün el, kask ya da nesneyle kapanması, ışık değişimi, kamera hareketi, hızlı eylem, geniş planda küçük kalan yüz, yansıtıcı yüzeyler (vizör, cam, metal) ve yansımada uydurulan içerik, simetrik ve tekrarlayan desenler; hangi prompt cümlelerinin (kimlik çapası, kısa görünüş özeti, "the same person throughout") kaymayı azalttığı ya da artırdığı, iki yönlü.
Klipler arası sürekliliği sor: aynı karakterin farklı başlangıç karelerinden üretilen kliplerde aynı kalması için referans görseli ya da karakter girdisi modlarının bu modelde nasıl çalıştığı ve kaç referansı kaldırdığı, son kareden devam zincirinde nesil nesil kayma (renk, pozlama, keskinlik, yüz), tutarlılığı artıran metin kalıpları (her klipte aynı tanımlayıcı cümle, sayılabilir öznitelikler, renk adı + malzeme) ve metin tekrarının kaymayı artırdığı vakalar.
Yüz ile politikanın kesişimini ayrıca sor: fotogerçekçi kurgusal bir yüz içeren başlangıç karesinin bu modelde "tanınmış kişi / gerçek kişi" gerekçesiyle reddedilme koşulları ve aynı karenin Veo 3.1'deki sonucu, tek karakterde üst üste yazılan kimlik özniteliği sayısının (boy, ten, saç rengi, saç biçimi, yaş, yüz işareti) hem reddi hem kaymayı nasıl etkilediği, kimliği kareye bırakıp metinde kaç özniteliğin güvenli kaldığı — geçen ve reddedilen vakalar birebir red mesajıyla.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi uzay bilimkurgu planlarıdır; karakter çoğunlukla tek kişidir, basınç giysisi ve kask giyer, vizör optik olarak berrak ve yüz okunur olmak zorundadır, film 12 ile 180 klipten kurulur ve her klip ayrı onaylı kareden üretilir, milliyet, bayrak, kurum işareti, logo ve okunur yazı yoktur — bu yüzden yüz değiştirme, sonradan yüz düzeltme, LoRA ya da ince ayar eğitimi gerektiren ve kimliği yazıyla, isimle ya da amblemle taşıyan çözümleri işaretleyip ele.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KAYMA tablosu — öğe (yüz, saç, giysi rengi, kask, vizör, aksesuar, nesne sayısı, mekân), kaç saniyede ve hangi tetikleyiciyle kayar, önleyen İngilizce tarif, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) ZİNCİR tablosu — yöntem (yeni başlangıç karesi / son kareden devam / referans görseli), kaç klip sonra ne bozulur, önlem, kaynak ve etiket; (c) YÜZ ve POLİTİKA tablosu — kare ve prompt özelliği, geçti ya da reddedildi, birebir mesaj metni, model ve tarih, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 7️⃣ SES ve DİYALOG — yerel ses, replik sözdizimi, dudak senkronu ve altyazı riski

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modelinin (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde yerel ses üretimini araştır: ses efekti, ortam sesi, müzik ve konuşmanın promptla nasıl istendiği ve ne kadar uyulduğu, ses ile görüntü eşzamanlılığı, sesin kapatılabilmesi ya da sessiz klip istenebilmesi — resmî belgeler ve örnek promptlar, bağımsız testler ve sistematik kullanıcı raporları; sürüm, tarih ve kaynakla.
Konuşma sözdizimini birebir sök: repliğin tırnak içinde mi yazılacağı, "says:", "speaks the line", "says in a low voice" gibi kalıplar arasındaki fark, iki nokta üst üstenin ve tırnağın ekrana gömülü altyazı ya da yazı üretme riski ve bunu önleyen cümleler ("no subtitles", "heard only, never shown as text"), on saniyeye sığan kelime sayısı, konuşma hızı ve duraklama tarifi, duygu ve vurgu kelimelerinin etkisi, konuşmanın klibin hangi saniyesinde başlayacağının yönetilebilmesi — iki yönlü, işe yarayan ve yazı üreten örneklerle.
Dudak senkronunu ve sesin sahibini sor: senkronun hangi çekim ölçeğinde (yakın, orta yakın, orta, geniş) ve hangi yüz açısında çöktüğü, kapalı kask, maske ya da görünmeyen ağızla konuşma istenirse ne üretildiği, sesin kadrajdaki doğru kişiye bağlanması, telsiz, kayıt cihazı ya da kadraj dışı ses gibi kaynağı görünmeyen sesin tarifi, aynı karakterin sesinin ardışık kliplerde aynı kalıp kalmadığı ve sesi sabitlemenin belgelenmiş yolu.
Ortam ve efekt katmanını sor: "Audio:", "SFX:", "Ambient:" gibi etiketlerin etkisi, kaç ses katmanının güvenle üretildiği, eylem ile sesi bağlayan cümle biçimleri ("as the latch clicks"), istenmeden eklenen müziği kapatmanın yolu, vakum ya da ince atmosfer gibi sesi taşımayan ortamların tarifi (boğuk dış ses, yalnız giysi içi nefes ve fan) ve modelin buna uyup uymadığı; ayrıca çığlık, ağlama, argo ve sert sesin politika reddi ürettiği ve üretmediği vakalar, birebir mesaj metniyle.
Kritik kısıt: kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, kesmesiz, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli uzay bilimkurgu planlarıdır; karakter çoğu klipte konuşmaz, replik yalnız basınçlı iç mekânda, kasksız ve orta yakın planda klip içinde üretilir, kapalı vizörde replik klip içinde üretilmez ve sesi sonradan eklenir, tek konuşmacı ve replik başına beş saniyeden kısa, kadrajda hiçbir yazı ve altyazı olamaz, dış ses anlatıcı yoktur — bu yüzden altyazıya, çok konuşmacılı diyaloğa, dış sese ya da sonradan dudak senkronu aracına dayanan çözümleri işaretleyip ele.
Çıktıyı üç tablo ve iki liste olarak ver: (a) SÖZDİZİMİ tablosu — İngilizce birebir kalıp, dudak senkronu sonucu, altyazı ya da ekran yazısı riski, kelime sınırı, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) SENKRON tablosu — çekim ölçeği ve yüz durumu (açık, profil, kasklı, kapalı vizör), senkron sonucu, arıza biçimi, kaynak ve etiket; (c) SES KATMANI tablosu — katman (konuşma, efekt, ortam, müzik, sessizlik), İngilizce kalıp, uyum, istenmeyen yan etki, kaynak ve etiket; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin (özellikle Veo 3.1) bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 8️⃣ POLİTİKA ve RED YÜZEYİ — I2V'de hangi aşama reddeder, uyumlu tarif nasıl yazılır

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modelinin (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya modunda hangi girdilerin reddedildiğini araştır: reddin girdi görseli denetiminde mi, prompt metninde mi, üretilen çıktıda mı gerçekleştiği ve kullanıcının bu üç aşamayı nasıl ayırt edebileceği, her aşamanın birebir red mesaj metinleri, reddedilen üretimde kredinin düşüp düşmediği — resmî kullanım politikası, model kartının güvenlik bölümü, Google'ın üretken yapay zekâ yasaklı kullanım politikası ve kullanıcı raporları; sürüm, tarih ve kaynakla.
Kişi ve yüz yüzeyini sök: fotogerçekçi kurgusal insan içeren başlangıç karesinin "tanınmış kişi" yanlış pozitifi ürettiği koşullar, kişi üretimi ayarının (person generation ve benzeri) bölgeye göre varsayılanı ve Türkiye'nin hangi bölge grubunda olduğu, çocuk görünümlü yüzlerin kuralı, gerçek bir kişinin fotoğrafını başlangıç karesi yapmanın kuralı, aynı kare ve promptun bu modelde reddedilip Veo 3.1'de geçtiği ya da tersinin olduğu belgelenmiş vakalar.
İçerik ve kelime yüzeyini sök: tehlike, yaralanma, ölüm, boğulma, basınç kaybı, yangın, patlama ve alet gibi hayatta kalma draması kelimelerinin red tetikleme durumu ve politika uyumlu betimleme ikameleri, milliyet, bayrak, kurum ve marka adlarının etkisi, olumsuz cümle ya da yasak listesi içinde geçen hassas kelimenin denetime yine takılıp takılmadığı, uzun olumsuz blokların red riskine etkisi, aynı promptun tekrar gönderilince geçtiği rastlantısal redlerin sıklığı.
Yayın tarafını ekle: bu modelin ürettiği videolardaki görünür ve görünmez işaretler (SynthID, C2PA, görünür filigran), ticari kullanım ve YouTube'da yayın hakları, platformların yapay zekâ içerik etiketi zorunluluğu; ve iki yönlü vakalar — sözlük temizlenince geçen, temizlendiği hâlde reddedilen ve kare değiştirilince geçen üretimler, tarih ve birebir mesajla.
Kritik kısıt: bu araştırma filtre atlatma araştırması DEĞİLDİR — aranan, meşru kurgusal bilimkurgu içeriğinde yanlış pozitifleri düşüren politika uyumlu tarif kalitesidir, "filtreyi şöyle aş" diyen kaynakları ayrı listede işaretle ve tavsiye olarak kullanma; kullanım yeri, ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretilen on saniyelik, fotogerçekçi, çoğunlukla tek karakterli uzay hayatta kalma draması planlarıdır, yüz berrak kask vizöründen görünür, tehlike, arıza ve yalnızlık anlatılır ama kan, yara, ceset ve silah gösterilmez, milliyet, bayrak, kurum ve marka yoktur.
Çıktıyı üç tablo ve iki liste olarak ver: (a) RED AŞAMASI tablosu — aşama (girdi görseli / prompt / çıktı), birebir mesaj metni, tipik tetikleyici, aşamayı ayırt etme yöntemi, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) TETİKLEYİCİ tablosu — kelime ya da kare özelliği, red riski, politika uyumlu İngilizce ikame, Veo 3.1 ile farkı, kaynak ve etiket; (c) YAYIN tablosu — işaret ya da hak, durum, koşul, kaynak; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle), ayrı bir "atlatma önerisi — kullanılmadı" listesi ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

# 9️⃣ İŞ AKIŞI ve VERİM — kaç deneme, hangi sırayla düzeltme, Flash ne zaman doğru model

```
Google'ın Flow ve Gemini ortamında "Omni 1.1 Flash" adıyla sunulan video modeliyle (resmî adının Gemini Omni Flash olduğu varsayılıyor, doğrulanmadı) görüntüden-videoya üretimde en yüksek isabet oranına ulaşmak için uygulayıcıların iş akışını araştır: bir sahne için kaç deneme alındığı ve kabul oranı, iyi klibin nasıl seçildiği, kötü klibin promptu değiştirerek mi, tohumu değiştirerek mi, başlangıç karesini değiştirerek mi düzeltildiği ve hangisinin daha az denemeyle sonuç verdiği — yapay zekâ ile kısa ve uzun film üreten ekiplerin belgelenmiş süreçleri, topluluk ölçümleri ve resmî ipuçları; sürüm, tarih ve kaynakla.
Hata teşhisini sistematikleştir: çıktı bozukluğunun (donma, kimlik kayması, fizik hatası, istenmeyen kamera hareketi, ekranda yazı, kötü ses, prompttan sapma) kök nedeninin kareden mi prompttan mı modelden mi geldiğini ayırmanın yöntemi, tek değişken değiştiren A/B deneme düzeni, aynı kare ve promptun tekrar üretiminde sonuçların ne kadar değiştiği, promptu kısaltmanın ya da sadeleştirmenin isabeti yükselttiği vakalar ile çok deneme almanın kaliteyi artırmadığı vakalar — iki yönlü.
Flash sürümünün ödünleşimini ve model seçimini sor: Flash ile daha yüksek kaliteli kardeş sürüm ve Veo 3.1 / Veo 3.1 Fast arasında hangi sahne tiplerinde (konuşma, yüz yakın planı, geniş manzara, hızlı eylem, tutulmuş sabit plan, nesne yakın planı) hangisinin tercih edildiği ve neden, kabul edilen klip başına kredi bedeli, üretim süresi, aynı filmde iki modeli karıştırmanın renk, grenlilik, hareket karakteri ve ses açısından görünür dikiş bırakıp bırakmadığı.
Üretim sonrası ve ölçeklemeyi ekle: klibin ilk ve son karelerindeki artefakt yüzünden kırpma ihtiyacı, büyütme (upscale) ve kare hızı artırmanın bu modelin çıktısına etkisi, klipler arası renk eşleme, yüzlerce klipli bir filmde prompt, tohum, sürüm ve tarih kaydı tutmanın pratikleri, model sürümü sessizce güncellendiğinde önceki kliplerle tutarsızlığın nasıl yakalandığı ve önlendiği.
Kritik kısıt: kullanım yeri, 2 ile 30 dakika arası filmleri kuran 12 ile 180 on saniyelik klipten her birinin ayrı bir görüntü modelinde onaylanmış tek başlangıç karesinden İngilizce tek promptla üretildiği, varsayılan sabit kameralı, fotogerçekçi, çoğunlukla tek karakterli ve basınç giysili uzay bilimkurgu hattıdır; tek kişi üretir, bütçe krediyle sınırlıdır, her üretimin modeli, sürümü ve tarihi kaydedilir, klip süresi sabittir ve kurgu klibi kısaltmak yerine tam kullanır — bu yüzden büyük ekip, özel eğitim (LoRA, ince ayar), yerel açık kaynak model ya da klip başına onlarca deneme gerektiren çözümleri işaretleyip ele, tek kişinin kredi bütçesinde uygulanabilir yöntemleri öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) İŞ AKIŞI tablosu — adım, yöntem, deneme sayısı ya da kabul oranı, kredi ve zaman bedeli, sürüm, kaynak ve etiket (ÖLÇÜLMÜŞ · UYGULAMA · ÖNERİ); (b) TEŞHİS tablosu — belirti, olası kök neden (kare / prompt / model), ilk denenecek düzeltme, ikinci düzeltme, kaynak ve etiket; (c) MODEL SEÇİMİ tablosu — sahne tipi, Omni 1.1 Flash uygun mu, alternatif model, tercih gerekçesi, bedel farkı, kaynak; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve tam kaynak listesi — başka modelin bulgusunu motor sütununda ayır, sürüm adı uydurma.
```

---

## ⬜ ARAŞTIRMA BEKLEMEDEN YAPILABİLECEKLER — sahip kararı, hiçbiri yapılmadı

> Aşağıdakiler TUR 20'nin cevabına bağlı DEĞİL; açık çelişkilerin ikisi
> arayüze bir kez bakmakla kapanır. Sahip "yap" demeden hiçbiri depoya girmez.

```
1. ARAYÜZ KÜNYESİ (5 dakika, 0 kredi)  ⬜
   Flow'da Omni 1.1 Flash seçiliyken ekran görüntüsü: bitiş karesi alanı
   var mı · seed alanı var mı · süre seçenekleri · en-boy · ses anahtarı.
   ÇELİŞKİ ① ③ ⑤'i araştırmadan önce kapatır; rapor 1 bununla sınanır.

2. SÜRE ÖLÇÜMÜ (1 klip)  ⬜
   İlk Omni klibinde ffprobe süresi → D124 satırı. 10,0 s varsayımı
   ölçülmedi; 48 × 10 s ızgarası buna yaslanıyor.

3. İKİ NOKTA PROB'u (2 klip, A/B)  ⬜
   Aynı kare, aynı replik: A `speaks the line: "…"` · B `speaks the line "…"`
   (iki noktasız) — ikisinde de `heard only, never shown as text`.
   Ekranda yazı çıkan kol kaybeder. ÇELİŞKİ ②'yi rapor 7 gelmeden kapatır.

4. RED DEFTERİ MOTOR SÜTUNU  ⬜
   POLITIKA §6.1 seçim kuralı "3 vaka biriktirince" kesinleşecekti;
   14 vakanın 13'ünde motor yazılmamış. Omni üretim günü satır açılırsa
   rapor 6 ↔ 8'in eşiği deponun kendi vakalarıyla çaprazlanır.
```
