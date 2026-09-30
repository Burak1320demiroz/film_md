# 🔬 24 — NANO BANANA 2 · GÖRSEL ÜRETİM ARAŞTIRMA PROMPTLARI (16.09.2026)

> **Ne bu dosya:** Nano Banana 2 (NB2 · Gemini 3.1 Flash Image) ile film karesi
> üretiminin "nasıl yazılır · kare videoya nasıl hazırlanır · kimlik nasıl
> tutulur · red ve iş akışı" tarafı için DÖRT derin araştırma promptu. Her biri
> **altı cümledir**, her cümle **tek satırdır** ve **salt prompt** çalışır —
> kopyala, araştırma aracına yapıştır, başka hiçbir şey verme. `23_`'ün (OMNI)
> görüntü tarafındaki kardeşidir.
>
> | # | konu | kurulacak kılavuzun bölümü (çalışma adı `NANO_BANANA_2_GORSEL_URETIM_KILAVUZU.md`) |
> |:--:|---|---|
> | 1 | **KÜNYE ve PROMPT OKUMA** — resmî kimlik, parametreler, promptun okunuşu, yazı eğilimi, şablon | §1 KÜNYE · §2 YAZIM KURALLARI · §8 ŞABLONLAR |
> | 2 | **VİDEOYA HAZIR KARE** — I2V ilk karesi olarak kompozisyon, fotogerçekçilik, video modeline uyum | §3 KARE KURALLARI · OMNI kılavuzu §3 ile çift |
> | 3 | **KİMLİK · REFERANS · SÜREKLİLİK** — referans görseli biçimi, kayma tetikleyicileri, yüz × politika | §4 SÜREKLİLİK · REFERANS_PAKETI motor satırı |
> | 4 | **POLİTİKA · RED · İŞ AKIŞI** — red aşamaları, NB2 ↔ Pro filtre farkı, deneme/seçim/kayıt | `POLITIKA` §6 · §6.1 · §5 İŞ AKIŞI |
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-23'ün gerekçesiyle aynı).
>
> **Neden ŞİMDİ:** sahibin isteği (16.09.2026) — *"aynı mantıkta nano banana 2
> için 4 tane hazırla"* — TUR 20'nin (OMNI) bittiği gün. Depo hattı iki
> motorludur: kare NB2/NBP'de, video OMNI/Veo'da. TUR 20 video tarafının
> kılavuzunu yazdı; kare tarafında motorun kendi kılavuzu yok. NB2 bilgisi
> dağınık ve çoğu doğrulanmamış:
>
> | depoda bilinen | kaynak | durum |
> |---|---|---|
> | NB2 = **Gemini 3.1 Flash Image**; ayrı bir **NB2 Lite = Gemini 3.1 Flash-Lite Image** var; NBP = Gemini 3 Pro Image | POLİTİKA §6 · red defteri lejandı · ⭐ 16.09.2026 ön kontrol: Google Cloud belge başlığı *"Gemini 3.1 Flash Image (Nano Banana 2)"* · DeepMind *"Gemini 3.1 Flash Image – Nano Banana 2"* · Workspace Updates 02.2026 *"Introducing Nano Banana 2 in the Gemini app"* · VentureBeat *"Nano Banana 2 Lite aka Gemini 3.1 Flash-Lite"* | ✅ kimlik (arama sonucu başlıkları; sayfa içerikleri okunmadı) |
> | **NB2 filtreleri NBP'den ESNEK** → "red alan image promptunda ÖNCE NB2 dene" (POLİTİKA §6.1 kuralı) | 04 §TUR 3 — "Firebase dokümanından alıntı", alıntının bağlantısı depoda YOK | ⚠️ hipotez — tek kaynak |
> | Referans görseli sınırları: "NB2 14 / 4 kişi" ↔ "NB2 10 nesne / 4 karakter, Lite 14" | 04 §T3.2 (iki rapor çelişti) ↔ `.claude/skills/image/references/nano-banana.md` (üçüncü taraf beceri, CC BY) | ⛔ çelişkili |
> | Sayısal lens değerleri (50mm · f/2.8) NB tarafından yok sayılır, nitel yaz | image becerisi (üçüncü taraf) | ⚠️ doğrulanmamış — V3 CAMERA satırı lensi SAYIYLA yazıyor |
> | NB2'ye özgü: web/görsel temellendirme (grounding) · uç oranlar · `thinking_level` · 512px | image becerisi | ⚠️ doğrulanmamış (TUR 20'de OMNI için `thinking_level` uydurma çıktı) |
> | Kadrajda olmayanı tarif etmek onu kadraja sokar | D214 | ÖLÇÜLMÜŞ (depo) |
> | Vizör biçimi sayıyla yazılmazsa bir filmde üç kask çıkar | D146 | ÖLÇÜLMÜŞ (depo) |
> | Metin yasağı kostüme yazıldı, ölçü zemine basıldı | D138 | ÖLÇÜLMÜŞ (depo) |
> | Referans sayfası değil kırpılmış panel yüklenir; panel oluğu/etiket çıktıya sızar | REFERANS_PAKETI §4.3 | yarı ölçülmüş; "sayfanın tamamını yükle" diyen dört paketle ⬜ A/B |
> | Kare kuralları (oran = çıkış oranı · eylemin ortası AMA dengede · ince tekrarlayan ayrıntı ikincil · görünmeyeni açma yok) | OMNI kılavuzu §3 (TUR 20) | video tarafından yazıldı; NB2'nin bunu üretip üretemediği sorulmadı |
> | Image pozitif gövde bandı 100-250 kelime | `prompt_kontrol.py` `KELIME_BANDI` | ⬜ kalibrasyon açık |
> | NB2 red vakası | `09_URETIM_RED_DEFTERI` | ❌ YOK — defterin tek image-motor satırı (#15) OMNI'dir |
>
> **AÇIK SORULAR — bu tur kapatmalı:**
> ① **"NB2 esnek" cümlesinin kendisi:** birebir metin, bağlantı, hangi yüzey için
>    yazıldığı; ve aynı promptun iki modelde farklı sonuç verdiği vaka var mı.
>    POLİTİKA §6.1'in kuralı buna dayanıyor → prompt 4.
> ② **Referans sınırları ve biçimi:** kaç görsel, nesne/karakter ayrımı; sayfa mı
>    kırpılmış panel mi → prompt 1 (sayı) + prompt 3 (biçim).
> ③ **Lens sayısı:** NB2 "24mm" okuyor mu? Okumuyorsa V3 CAMERA satırı image
>    promptta boşuna kelime yiyor; okuyorsa beceri dosyası yanlış → prompt 1.
> ④ **Seed:** alan var mı, tekrar üretim veriyor mu [D142 · REFERANS §5.4] → prompt 1 + 4.
> ⑤ **Uzunluk:** 100-250 kelimelik bandın NB2'deki karşılığı; uzun promptun sonu
>    okunuyor mu (image bandı kalibrasyonu açık) → prompt 1.
> ⑥ **Yazı eğilimi:** NB2 güçlü metin çizer — depo yazı istemez; ölçü, rozet,
>    panel tarifi yazıya dönüyor mu [D138] → prompt 1.
>
> **KOŞU KAYDI:** ⏳ **16.09.2026 yazıldı, KOŞULMADI.** TUR 21 numarası bu
> dosyaya rezerve (numara koşuya verilir — TUR 8 usulü). Koşulunca:
> `TUR21_HAM_RAPORLAR/` (4 dosya, birebir, her birinin başında koşulan prompt)
> → `00_KUNYE.md` §🔎 **canlı kaynak kontrolü** (TUR 20 usulü — süzmeden ÖNCE)
> → `04_ARASTIRMA_BULGULARI.md` §TUR 21 (süzme) → kılavuz.

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA GİRMEZ.
   Sıra: araştırma → TUR21_HAM_RAPORLAR/ (birebir) → 00_KUNYE §🔎 canlı kontrol →
         04_ARASTIRMA_BULGULARI.md §TUR 21 (süzme kaydı) →
         NANO_BANANA_2_GORSEL_URETIM_KILAVUZU.md (çalışma adı; OMNI kılavuzunun
         görüntü tarafındaki kardeşi) → dokunduğu yerler:
         POLITIKA §6 NB2 satırı + §6.1 "red gelirse önce NB2" kuralı ·
         IMAGE_VIDEO_PROMPT_TEMPLATES V3 IMAGE (CAMERA lens satırı · Output satırı) ·
         prompt_kontrol KELIME_BANDI["image"] (kalibrasyon) ·
         REFERANS_PAKETI §4.3 yükleme kuralı · §5.4 seed · motor satırı ·
         OMNI kılavuzu §3 (kare kuralları → NB2 yazım karşılığı) ·
         09_URETIM_RED_DEFTERI (NB2 satırı · AŞAMA sütunu).
   Süzme kaydı ÜÇ liste tutar: GİRDİ · GİRMEDİ + NEDEN · GEOMETRİYE ÇEVRİLDİ.

⛔ TUR 20'NİN DERSİ PROMPTLARIN İÇİNDE.
   TUR 20'de raporlar üç yerde "resmî belgeyle doğrulandı" yazıp uydurdu
   (thinking_level · forum red mesajı · Elo), SSS sayfalarını ÖLÇÜLMÜŞ
   etiketledi ve aynı bloga dayanan iddiaları üç kanıt gibi sundu. Bu yüzden
   dört promptun altıncı cümlesi şunları ZORUNLU ister: resmî satır için
   belgeden birebir kısa alıntı + bağlantı (yoksa ÖLÇÜLMÜŞ yazılamaz) · SSS,
   prompt blogu ve başka modelin belgesi ÖLÇÜLMÜŞ değildir · aynı kaynağa
   dayanan iki iddia iki kanıt sayılmaz · belgede olmayan parametre ya da
   sürüm adı uydurulmaz. Süzmede canlı kontrol yine yapılır — prompt bunu
   kolaylaştırır, yerine geçmez.

⛔ BU ARAŞTIRMA "PROMPT HİLESİ" DE "FİLTRE ATLATMA" DA DEĞİLDİR.
   Aranan: bu modelde neyin çalıştığı, neyin çöktüğü, hangi koşulda.
   Motor sürümü, tarih ve karşı örnek vermeyen "şu kelimeyi ekle" kaynağı
   GİRMEDİ'dir. Filtre atlatma tavsiyesi (prompt 4) her koşulda GİRMEDİ'dir.

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) ÖLÇÜLMÜŞ — resmî belge (birebir alıntıyla) · yöntemi yazılı bağımsız ölçüm
   (b) UYGULAMA — uygulayıcı, prompt mühendisi, kullanıcı raporu
   (c) ÖNERİ    — raporun kendi çıkarımı
   Kaynaksız (a) düşer; (b) ancak iki BAĞIMSIZ kaynak aynı şeyi söylüyorsa iner;
   (c) yalnız ⬜ HİPOTEZ etiketiyle iner. Sayı katmanı çürük gelirse kılavuz
   SAYISIZ yazılır (TUR 17-20). Fiyat kılavuza yazılmaz.

⛔ MOTOR KARIŞMASI — "Nano Banana" dört modelde geçiyor.
   Nano Banana (Gemini 2.5 Flash Image) · Nano Banana Pro (Gemini 3 Pro Image) ·
   Nano Banana 2 (Gemini 3.1 Flash Image) · Nano Banana 2 Lite (Gemini 3.1
   Flash-Lite Image). Her prompt motor sütunu ister; NB2 dışındaki satır NB2
   kılavuzuna inmez, en fazla "karşılaştırma" sütununa girer. NBP satırları
   ayrıca değerlidir — depo iki modeli birlikte kullanıyor.

⛔ ÖNCEKİ TURLARLA VE MEVCUT KILAVUZLARLA ÇAKIŞMA ("ZATEN VAR").
   • Kare kuralları (oran · dengeli eylem ortası · ince ayrıntı · görünmeyeni
     açma yok) → OMNI kılavuzu §3 (TUR 20). 2 bunları KURAL olarak değil
     "NB2 bunu nasıl yazdırır" diye sorar.
   • Kadrajda olmayan tarif edilmez [D214] · IN FRAME satırı → V3. 2 bunu
     NB2'de SINAR (iki yönlü), yeniden tanımlamaz.
   • İmaj promptu değişimin ÖNCESİNİ yazar, I2V'de imaj t=0'dır [D179] ·
     klip içinde durum değişimi yok → REHBER §7. Kısıt olarak verilir.
   • Vizör biçimi sayıyla [D146] · vizör optik berrak [D79] · kimlik dizisi
     [D208] · kimlik ≤3-4 öznitelik [D167 · ⑲] → 3 bunları kısıt olarak verir,
     NB2'deki kayma MEKANİZMASINI sorar.
   • Metin yasağı ve ölçünün zemine basılması [D34 · D45 · D138] → 1 NB2'nin
     yazı EĞİLİMİNİ sorar.
   • Referans sayfası kanonu, yükleme kuralı, yaşam döngüsü → REFERANS_PAKETI
     (TUR 12). 3 biçimi NB2 özelinde sorar; paket mimarisini sormaz.
   • Yüz sözlüğü, ışık senaryosu, dünya görünüşü, araç → TUR 18 (21_). Sorulmaz.
   • Giysi silueti, malzeme ve renk dili → UZAY_GIYSISI (TUR 17). Sorulmaz.
   • Politika sözlüğü, olasılık ≠ şiddet, red basamakları, kredi iade edilmez
     → POLITIKA §1-§5 (TUR 3). 4 yalnız NB2 AŞAMA ve NB2 ↔ NBP FARKINI sorar.
   • Deponun ölçülmüş KARARLARI promptlarda kısıt olarak durur: fotogerçekçi ·
     tek sahne tek kilit · pozitif gövde 100-250 kelime · okunur yazı yok ·
     "glow/bloom" yasak · milliyet/kurum/marka yok.
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "NB2 filtreleri NBP'den esnek", "lens sayısı yok sayılır", "sayfa değil
   panel yükle", "NBP yüzde NB2'den zayıf", "uzun promptun sonu okunmaz"
   deponun ya da üçüncü taraf becerinin ADAYLARIDIR — dört prompt da İKİ
   YÖNLÜ yazıldı (tutan ve tutmayan vaka birlikte istenir). Üretim kısıtları
   hipotez değil FİLTREDİR ve her promptun beşinci cümlesinde açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — dört çift.
   1 ↔ 2 : 1'in yazım kuralı (lens sayısı · uzunluk · olumsuz cümle) 2'nin kare
           kuralını yazdıramıyorsa kural "NB2'de yazılamaz" etiketiyle iner.
   2 ↔ 3 : 2'nin kompozisyon önerisi (geniş plan · sığ alan derinliği) 3'e göre
           kimliği kaydırıyorsa kimlik kazanır; öneri sahne tipine bağlanır.
   3 ↔ 4 : kimlik özniteliği ve fotogerçekçi yüz eşiği ikisinde aynıysa iner;
           farklıysa ⬜ HİPOTEZ kalır, D167 değişmez.
   1 ↔ 4 : 4'ün iş akışı 1'in "yok / belirsiz" dediği bir özelliğe (seed ·
           düşük çözünürlük taslağının yüksek çözünürlükte aynı kalması ·
           temellendirme) dayanıyorsa o adım inmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Künye ve prompt okuma** | Referans sınırları çelişkili (②); lens sayısı okunuyor mu (③); seed (④); 100-250 bandı (⑤); yazı eğilimi (⑥); `thinking_level` ve grounding gerçekten var mı | Kılavuz §1-§2 · §8 · TEMPLATES V3 IMAGE · `KELIME_BANDI` |
| 2 | **Videoya hazır kare** | OMNI kılavuzu §3'ün kare kuralları NB2'de nasıl yazdırılır; yapay görünüm (HDR · plastik cilt · oyun görünümü) videoya nasıl taşınır; D214 NB2'de de geçerli mi | Kılavuz §3 · OMNI §3 çift satırı · IMAGE şablonu |
| 3 | **Kimlik · referans · süreklilik** | Sayfa mı panel mi (REFERANS §4.3 ↔ dört paket); asimetri aynalanması, sayılabilir öğe, kask biçimi kayması NB2'de nasıl önlenir; yüz × red eşiği NB2'de | Kılavuz §4 · REFERANS_PAKETI §4.3/§5.4 · D146/D208 gerekçesi |
| 4 | **Politika · red · iş akışı** | "NB2 esnek" alıntısı (①) ve §6.1 kuralı; NB2 red defterinde hiç yok; taslak → son kare akışı; seed; kayıt | POLITIKA §6/§6.1 · red defteri · kılavuz §5 İŞ AKIŞI |

> ⚠️ **Dört rapor birbirini denetler** (yukarıdaki çapraz okuma). Bir raporun
> getirdiği kural ötekinde tutmuyorsa kılavuza ancak ⬜ HİPOTEZ etiketiyle iner.

---

# 1️⃣ KÜNYE ve PROMPT OKUMA — Nano Banana 2 promptu nasıl okur, nasıl yazılır

```
Google'ın Nano Banana 2 adıyla sunduğu Gemini 3.1 Flash Image görsel modelinin (Nano Banana 2 Lite = Gemini 3.1 Flash-Lite Image, Nano Banana Pro = Gemini 3 Pro Image ve Nano Banana = Gemini 2.5 Flash Image ayrı modellerdir) üretim künyesini ve prompt okuma biçimini araştır: resmî model kimlikleri ve sürüm geçmişi, erişim yüzeyleri (Gemini uygulaması, Flow, AI Studio, Gemini API, Vertex AI / Agent Platform) ve yüzeye göre değişen özellikler, en-boy oranları ve çözünürlük basamakları, referans görseli sınırları (nesne ve karakter için ayrı ayrı), çok turlu düzenleme, düşünme (thinking) ve web ya da görsel aramayla temellendirme seçenekleri, seed ve negatif prompt alanının var olup olmadığı — Google model kartı, geliştirici belgeleri, resmî prompt rehberleri ve duyurular öncelikli; bağlantı ve tarihle.
Modelin promptu nasıl okuduğunu sök: akıcı paragraf, etiketli bölümler, JSON ve madde listesi arasındaki fark, cümle sırasının (özne, eylem, mekân, kompozisyon, ışık, kamera, stil) sonuca etkisi, prompt uzunluğunun (yaklaşık 50, 150, 250, 400 kelime) uyuma ve sürüklenmeye etkisi ve uzun promptun sonundaki cümlelerin okunup okunmadığı, sayısal lens ve kamera değerlerinin ("24mm", "f/2.8", "camera height 1.2 m") nitel tariflerden ("wide-angle", "shallow depth of field", "eye level") farklı işlenip işlenmediği, olumsuz cümlelerin ("no …", "without …") ne kadar tuttuğu ve tersine o nesneyi çağırıp çağırmadığı — iki yönlü, tutan ve tutmayan vakalar birlikte.
Yazı eğilimini ayrıca sor: modelin güçlü metin çizme yeteneğinin istenmeyen yazıya nasıl dönüştüğü (tırnak içindeki kelimeler, ölçü ve sayı ifadeleri, marka ve kurum adları, ekran ve kontrol paneli tarifleri, rozet, yama ve şerit tarifleri), yazıyı güvenilir biçimde önleyen tarif kalıpları ve "no text, no letters, no numbers" türü olumsuz cümlelerin bu konuda işe yarayıp yaramadığı, tırnak işaretinin ve iki nokta üst üstenin etkisi, sayı ve ölçünün prompta yazılmasının görüntüde basılı rakama dönüşme riski; belgelenmiş örneklerle.
Hazır şablonları topla ve sına: Google'ın resmî prompt rehberlerindeki fotogerçekçi sahne şablonları, "cinematic, 8k, masterpiece, highly detailed" türü nitelik yığınlarının bu modelde işe yarayıp yaramadığı ya da zarar verip vermediği, film dili kelimelerinin (film grain, lens tipi, renk derecelendirme) ve marka ya da film adının etkisi, düşünme ya da temellendirme açıldığında aynı promptun sonucunun nasıl değiştiği; her şablonun hangi sahne tipinde (tek karakter orta plan, geniş manzara, iç mekân, nesne ya da el yakın planı) denendiği ve sonucu, iki yönlü.
Kritik kısıt: kullanım yeri, fotogerçekçi uzay bilimkurgu filmlerinin kareleridir — her kare tek İngilizce prompttan (gerekirse onaylı birkaç referans görseliyle) 16:9 ya da 9:16 oranında üretilir ve sonra bir video modelinde (Gemini Omni 1.1 Flash ya da Veo 3.1) görüntüden-videoya ilk kare olur; film 12 ile 180 kareden kurulur; pozitif metin 100-250 kelimedir, ardından en fazla on cümlelik bir olumsuz blok gelir; her prompt başka belgeye atıf yapmadan tek başına okunur; kadrajda olmayan hiçbir şey tarif edilmez; okunur yazı, rakam, logo, bayrak, milliyet ve kurum adı yoktur; "glow / bloom" yasaktır — bu yüzden stilize, illüstrasyon, infografik, metinli tasarım ve bant dışı uzunluk gerektiren özellikleri silme ama "hat dışı" diye işaretle, yalnız denemeyle ölçülebilecek iddiaları (seed'in tekrar üretilebilirliği, lens sayısının okunması, uzun promptun sonunun okunması) "sınanmalı" diye ayır.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KÜNYE tablosu — özellik, değer, model (NB2 · NB2 Lite · Nano Banana Pro · Nano Banana), yüzey, belgeden birebir kısa alıntı ve bağlantı, etiket; (b) YAZIM KURALI tablosu — kural, mekanizma, bozulunca ne olur, İngilizce doğru ve yanlış örnek çifti, model, kaynak ve etiket; (c) ŞABLON tablosu — sahne tipi, köşeli parantezli yuvalarla İngilizce tam şablon, doldurulmuş tek örnek, denendiği model ve tarih, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, resmî diye etiketlediğin her satır için belgeden birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, SSS sayfasını, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre ya da sürüm adı uydurma.
```

---

# 2️⃣ VİDEOYA HAZIR KARE — görüntüden-videoya ilk karesini Nano Banana 2'ye nasıl yazdırırsın

```
Nano Banana 2 (Gemini 3.1 Flash Image) ile, sonradan bir video modeline görüntüden-videoya ilk kare olarak verilecek fotogerçekçi film kareleri üretmenin yöntemini araştır: Google'ın kendi "Nano Banana karesi → Veo ya da Gemini Omni Flash videosu" hattı için yayınladığı rehberler ve örnekler, storyboard ve anahtar kare (keyframe) üreten yapay zekâ film ekiplerinin belgelenmiş iş akışları, görüntüden-videoya girdi karesinin videonun hareketine, kimliğine ve fiziğine etkisini inceleyen çalışmalar; görüntü modeli, video modeli, sürüm, tarih ve kaynakla.
Karenin kompozisyonunu videoya göre sök ve her birinin bu modele nasıl yazdırıldığını sor: öznenin kadrajdaki yeri ve hareket yönündeki boş alan, pozun eylemin ortasından ama dengede seçilmesi (iki destek noktası yerde) ile adım ortası, sıçrama ya da düşüş anı arasındaki fark, kırpılmış uzuvlar, arka planda ince tekrarlayan ayrıntının (ızgara, kablo demeti, perçin sırası) yoğunluğu, alan derinliği, ışık yönünün ve gölgelerin sonraki karede korunabilecek biçimde tarifi, karenin doğrudan hedef oranda (16:9, 9:16) üretilmesi ile sonradan kırpılması arasındaki fark — modelin bu tarifleri ne ölçüde uyguladığı, iki yönlü.
Fotogerçekçilik ve "yapay zekâ görünümü"nü ayrıca sor: bu modelin aşırı HDR, aşırı doygunluk, plastik ya da mum gibi cilt, fazla temiz yüzey, oyun ve render görünümü eğilimleri, bunları azaltan tarif kalıpları (doğal kontrast, film greni, gerçek malzeme dokusu, kir ve aşınma, optik kusur), bu kalıpların videoya taşındığında titreme ya da doku kaynaması üretip üretmediği, ve kadrajda olmayanı tarif etmenin (örneğin el yakın planında yüz ya da giysinin tamamını tarif etmek) modele o şeyi kadraja soktup soktmadığı — belgelenmiş örneklerle, iki yönlü.
Video modeline uyumu sor: aynı aileden video modellerinin (Veo 3.1, Gemini Omni Flash) Nano Banana 2 karelerini başka görüntü modellerinin karelerinden farklı işleyip işlemediğine dair kanıt, kareye gömülü görünmez filigranın (SynthID) ve C2PA verisinin video girdisi olarak etkisi, karenin çözünürlüğünün (1K, 2K, 4K) video çıktısına etkisi, karede görünen durumun (açık kapak, yanan lamba, kask açık ya da kapalı) videoda değiştirilmeyip sonraki sahnenin karesine bırakılmasının pratiği, ve video promptu kareyi yeniden tarif etmediğinde karenin hangi özelliklerinin videoda en çok kaydığı.
Kritik kısıt: kullanım yeri, ayrı onaylanan her karenin bir video modelinde kesmesiz, on saniyelik, varsayılan sabit kameralı bir planın ilk karesi olduğu fotogerçekçi uzay bilimkurgu hattıdır; video promptu karedeki görünümü yeniden tarif etmez; karakter çoğunlukla tek, basınç giysili ve kasklıdır, vizör optik olarak berrak ve yüz okunurdur; klip içinde durum değişimi yapılmaz, değişim bir sonraki karede görünür; okunur yazı, gösterge ekranı, logo ve bayrak yoktur; "glow / bloom" yasaktır; görüntü promptunun pozitif metni 100-250 kelimedir — bu yüzden sonradan rötuş, kompozit, maske, bitiş karesi, stilize görünüm ya da harici büyütme aracı öneren çözümleri işaretleyip ele, tek İngilizce görüntü promptuna yazılabilecek kare kurallarını öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KARE ÖZELLİĞİ tablosu — özellik, videoya etkisi (hareket / kimlik / fizik / artefakt), bu modele yazdıran İngilizce kalıp, kötü değer, model, kaynak ve etiket; (b) YAPAY GÖRÜNÜM tablosu — eğilim, tetikleyen tarif, azaltan İngilizce kalıp, videoya taşındığında yan etkisi, model, kaynak ve etiket; (c) KARE KONTROL LİSTESİ — kareyi videoya göndermeden önce sorulacak evet / hayır soruları ve "hayır"ın öngördüğü arıza, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, resmî diye etiketlediğin her satır için belgeden birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, SSS sayfasını, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre ya da sürüm adı uydurma.
```

---

# 3️⃣ KİMLİK · REFERANS · SÜREKLİLİK — yüzlerce karede aynı karakter, giysi, kask ve araç

```
Nano Banana 2 (Gemini 3.1 Flash Image) ile yüzlerce karelik bir film boyunca aynı karakterin, giysinin, kaskın, aracın ve mekânın tutarlı kalmasının yollarını araştır: referans görseli modu (kaç görsel, nesne ve karakter için ayrı sınırlar, görsellere rol atama biçimi), çok turlu düzenleme ile tutarlılık, metinle tarif edilen kimliğin ardışık üretimlerde hangi özelliklerinin sabit kalıp hangilerinin kaydığı — resmî belgeler, yöntemi yazılı bağımsız testler ve karakter tutarlılığı ölçen değerlendirmeler; sürüm, tarih ve kaynakla, Nano Banana Pro ve Nano Banana 2 Lite bulguları ayrı sütunda.
Referans görselinin biçimini sök: tek varlığın kırpılmış kareye yakın görseli ile birden fazla paneli olan karakter sayfasının (model sheet, turnaround) yüklenmesi arasındaki fark, panel oluklarının, etiketlerin, okların ve ölçü çizgilerinin çıktıya sızması, referansın ışığının, arka planının ve pozunun yeni kareye taşınması, zıt ışıklı iki referansın birlikte verilmesi, referansın boyutu ve çözünürlüğü, referans ile metin çeliştiğinde modelin hangisine uyduğu ve metinde referansı nasıl çağırmak gerektiği — iki yönlü, belgelenmiş örneklerle.
Kayma tetikleyicilerini sor: sol-sağ asimetrik giysi öğelerinin (tek koldaki şerit, tek taraftaki hortum ya da ünite) ayna görüntüsüne dönmesi, sayılabilir öğelerin (şerit, lamba, kablo, düğme) sayısının değişmesi, kask ve vizör biçiminin (kubbe, yüz plakası, çerçeve, yaka halkası) kareden kareye başka bir kaska dönüşmesi, geniş planda küçük kalan yüzün jenerik bir yüze dönmesi, açı ve ışık değişince yüzün kayması, tekrarlanan düzenlemelerde (düzenlemenin düzenlemesi) kalite ve kimlik kaybı; hangi tarif biçimlerinin (sayıyla yazılmış öznitelik, renk + malzeme kalıbı, tek asimetri işareti, her karede aynı kalan kısa tanımlayıcı cümle) kaymayı azalttığı ve hangilerinin (uzun sıfat yığını, her karede tekrarlanan tam tarif) artırdığı.
Kimlik ile politikayı kesiştir: tek karakterde üst üste yazılan kimlik özniteliklerinin (boy, ten rengi, saç rengi ve biçimi, yaş, yüz işareti) "tanınmış kişi / gerçek kişi" reddi ile ilişkisi, fotogerçekçi kurgusal bir yüzün referans görseli olarak yüklenmesinin red koşulları, milliyet belirtmeyen yüz tarifinin kimliği ardışık karelerde taşıyıp taşımadığı; geçen ve reddedilen vakalar birebir red mesajı, yüzey ve tarihle ve aynı durumun Nano Banana Pro'daki sonucuyla.
Kritik kısıt: kullanım yeri, 12 ile 180 karelik fotogerçekçi uzay bilimkurgu filmleridir ve her kare ayrı üretilir; filmin başında onaylanan küçük bir referans paketi (karakter, giysi, kask, araç panelleri) vardır ve sahnelere o paketten kırpılmış paneller verilir; karakter çoğunlukla tek, basınç giysili ve kasklıdır, vizör optik olarak berrak ve yüz okunurdur; kimlik yazı, isim, amblem, bayrak ya da milliyetle taşınmaz; referans sayfasına etiket, ok ve ölçü yazılmaz; her kare görüntüden-videoya ilk kare olur — bu yüzden LoRA ya da ince ayar eğitimi, yüz değiştirme, sonradan rötuş ve kimliği metin ya da amblemle taşıyan çözümleri işaretleyip ele, tek İngilizce prompt ve birkaç kırpılmış referansla uygulanabilir yöntemleri öncelikle.
Çıktıyı üç tablo ve iki liste olarak ver: (a) KAYMA tablosu — öğe (yüz, saç, giysi rengi, asimetrik öğe, sayılabilir öğe, kask ve vizör biçimi, araç, mekân), tetikleyici, önleyen İngilizce tarif, model, kaynak ve etiket; (b) REFERANS tablosu — referans biçimi (kırpılmış tek varlık / karakter sayfası / çoklu referans / çok turlu düzenleme), sınırı, sızma ve kayma riski, promptta çağrılış biçimi (İngilizce), model, kaynak ve etiket; (c) YÜZ ve POLİTİKA tablosu — kare ve prompt özelliği, geçti ya da reddedildi, birebir mesaj, model, yüzey ve tarih, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, resmî diye etiketlediğin her satır için belgeden birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, SSS sayfasını, prompt rehberi blogunu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma, red mesajını ancak bağlantısını verdiğin sayfada birebir geçiyorsa yaz; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle) ve bağlantılı tam kaynak listesi — belgede olmayan parametre ya da sürüm adı uydurma.
```

---

# 4️⃣ POLİTİKA · RED · İŞ AKIŞI — neyi reddeder, Pro'dan farkı ne, üretim nasıl yürütülür

```
Nano Banana 2 (Gemini 3.1 Flash Image) görsel üretiminde hangi isteklerin reddedildiğini ve üretimin nasıl verimli yürütüleceğini araştır: reddin prompt metninde mi, yüklenen referans görselinde mi, üretilen görüntüde mi gerçekleştiği ve bu aşamaların kullanıcı tarafından nasıl ayırt edileceği, her aşamanın birebir red mesajları, Gemini uygulaması, Flow, AI Studio ve API arasında mesaj ve eşik farkları, reddedilen isteğin kredi ya da ücret tüketip tüketmediği — resmî kullanım politikası, model kartının güvenlik bölümü, geliştirici belgeleri ve bağlantısı verilebilen forum kayıtları; sürüm, tarih ve bağlantıyla.
Nano Banana 2 ile Nano Banana Pro'nun filtre farkını belgele: Google belgelerinde Nano Banana 2 için geçtiği bildirilen "daha esnek, daha az kısıtlayıcı güvenlik filtreleri" türü ifadenin birebir metni, bağlantısı ve hangi yüzey ya da ürün (örneğin Firebase, Vertex, Gemini API) için yazıldığı, aynı promptun iki modelde farklı sonuç verdiği belgelenmiş vakalar ve böyle bir fark bulunamıyorsa bunun açık kaydı; kişi üretimi ayarlarının bölgeye göre varsayılanı (Türkiye'nin hangi grupta olduğu dâhil, yalnız belgede adı geçiyorsa), hayatta kalma draması kelimelerinin (tehlike, yaralanma, basınç kaybı, yangın, ölüm) ve kırmızı acil ışığı, kalabalık, yüzü kapatan ekipman gibi görsel malzemenin red riski ve politika uyumlu betimleme ikameleri.
İş akışını sor: bir kare için kaç deneme alındığı ve varyasyonların nasıl seçildiği, düşük çözünürlükte ya da Nano Banana 2 Lite'ta taslak alıp beğenileni yüksek çözünürlükte ya da başka modelde yeniden üretmenin aynı görüntüyü verip vermediği ve büyütmenin (upscale) ne zaman gerektiği, seed alanı varsa aynı seed ile tekrar üretilebilirliği, kötü karenin promptu değiştirerek mi, referansı değiştirerek mi, çok turlu düzenlemeyle mi daha az denemede düzeldiği ve düzenlemenin karede başka yerleri de değiştirip değiştirmediği — iki yönlü, çok deneme almanın ya da düzenlemenin işe yaramadığı vakalar dâhil.
Kayıt ve izlenebilirliği ekle: üretilen her karede görünmez filigranın (SynthID) ve C2PA verisinin varlığı ve görünür filigranın hangi yüzeylerde bulunduğu, ticari kullanım ve YouTube'da yayın koşulları, model sürümü sessizce güncellendiğinde önceki karelerle tutarsızlığın nasıl fark edildiği, yüzlerce karelik bir üretimde prompt, referans, model, sürüm, çözünürlük, tarih ve red kaydı tutmanın pratiği.
Kritik kısıt: bu araştırma filtre atlatma araştırması DEĞİLDİR — aranan, meşru kurgusal bilimkurgu içeriğinde yanlış pozitifleri düşüren politika uyumlu tarif kalitesi ve verimli, kayıtlı bir üretim düzenidir, "filtreyi şöyle aş" diyen kaynakları ayrı listede işaretle ve tavsiye olarak kullanma; kullanım yeri, tek kişinin kredi bütçesiyle ürettiği 12 ile 180 karelik, fotogerçekçi, çoğunlukla tek ve basınç giysili karakterli, yüzü berrak vizörden görünen uzay hayatta kalma draması kareleridir; tehlike, arıza ve yalnızlık anlatılır ama kan, yara, ceset ve silah gösterilmez, milliyet, bayrak, kurum ve marka yoktur; kareler sonra görüntüden-videoya ilk kare olur — bu yüzden fotogerçekçiliği bırakıp stilize ya da animasyon görünümüne geçmeyi, yüzü gizlemeyi ve büyük ekip ya da yerel açık kaynak model gerektiren çözümleri işaretleyip ele.
Çıktıyı üç tablo ve üç liste olarak ver: (a) RED AŞAMASI tablosu — aşama (prompt / referans görseli / üretilen görüntü), birebir mesaj metni, yüzey, tipik tetikleyici, aşamayı ayırt etme yöntemi, model ve tarih, bağlantı ve etiket; (b) TETİKLEYİCİ tablosu — kelime ya da görsel malzeme, red riski, politika uyumlu İngilizce ikame, Nano Banana Pro ile farkı, kaynak ve etiket; (c) İŞ AKIŞI tablosu — adım, yöntem, deneme sayısı ya da kabul oranı, bedel, tekrar üretilebilirlik, model, kaynak ve etiket; etiketler ÖLÇÜLMÜŞ (resmî belge ya da yöntemi yazılı bağımsız ölçüm) · UYGULAMA (uygulayıcı ya da kullanıcı raporu) · ÖNERİ (senin çıkarımın) olsun, resmî diye etiketlediğin her satır için belgeden birebir alıntı ve bağlantı ver ve veremiyorsan o satırı ÖLÇÜLMÜŞ yazma, red mesajını ancak bağlantısını verdiğin sayfada birebir geçiyorsa yaz, SSS sayfasını, blogu ve başka modelin belgesini ÖLÇÜLMÜŞ sayma, aynı kaynağa dayanan iki iddiayı iki kanıt sayma; sonunda doğrulanabilir bulgular ile kaynaksız iddialar ("hipotez", neden doğrulanamadığı tek cümle), ayrı bir "atlatma önerisi — kullanılmadı" listesi ve bağlantılı tam kaynak listesi — belgede olmayan parametre ya da sürüm adı uydurma.
```

---

## ⬜ ARAŞTIRMA BEKLEMEDEN YAPILABİLECEKLER — sahip kararı, hiçbiri yapılmadı

> Aşağıdakiler TUR 21'in cevabına bağlı DEĞİL; dördü de bir ekran ya da iki
> kareyle kapanır. Sahip "yap" demeden hiçbiri depoya girmez.

```
1. ARAYÜZ KÜNYESİ (5 dakika, 0 kredi)  ⬜
   Flow ve Gemini uygulamasında NB2 seçiliyken ekran görüntüsü: oran ve
   çözünürlük seçenekleri · seed alanı · referans görseli kutusu sayısı ·
   düşünme/temellendirme anahtarı. Açık soru ② ③ ④'ün yarısını kapatır;
   rapor 1 bununla sınanır.

2. LENS SAYISI PROB'u (2 kare, A/B)  ⬜
   Aynı IMAGE promptu: A "24mm lens … camera height 1.20 m" · B "wide-angle
   lens … camera at chest height". Ölçüt: perspektif ve kadraj farkı var mı.
   Fark yoksa V3 IMAGE CAMERA satırı kelime yemeye devam etmez (açık soru ③).

3. REFERANS BİÇİMİ PROB'u (2 kare, A/B)  ⬜
   Aynı sahne: A kırpılmış tek panel · B referans sayfasının tamamı.
   Ölçüt: kask/giysi biçimi tuttu mu + oluk/etiket sızdı mı.
   REFERANS_PAKETI §4.3 ↔ dört paket çelişkisini kapatır (açık soru ②).

4. "NB2 ESNEK" ALINTISININ BAĞLANTISI  ⬜
   04 §TUR 3 ham metni arşivde yok; cümle Firebase belgelerinde aranır,
   bağlantı POLİTİKA §6'ya yazılır. Bulunamazsa §6.1 kuralı ⬜ HİPOTEZ'den
   düşer (açık soru ①).
```
