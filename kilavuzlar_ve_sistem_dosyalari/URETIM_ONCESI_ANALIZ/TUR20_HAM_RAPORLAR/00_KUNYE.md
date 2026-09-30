# 🧾 TUR 20 — KÜNYE (16.09.2026 · OMNI 1.1 Flash · görüntüden-videoya)

```
PROMPT DOSYASI   23_OMNI_1_1_FLASH_I2V_ARASTIRMA_PROMPTLARI.md (dokuz prompt, altışar cümle)
KOŞU             16.09.2026 · sahip koştu, dokuz raporu TEK mesajda tırnaklı ve
                 virgülle ayrılmış dizi olarak yapıştırdı. Yapıştırma sırası
                 prompt sırası DEĞİL: 1 · 3 · 2 · 4 · 5 · 7 · 6 · 8 · 9.
                 Dosyalar PROMPT numarasıyla adlandırıldı; aşağıda "rapor n" =
                 prompt n.
GELEN            9/9 rapor — BİREBİR arşivlendi. Metin oturum kaydından
                 programla kesildi (181.661 karakter; dokuz parçanın toplamı +
                 ayırıcılar = yapıştırılan metin, fark 0), elle kopyalanmadı:
                   TUR20_1_KUNYE_HAM.md
                   TUR20_2_PROMPT_ANATOMISI_HAM.md
                   TUR20_3_BASLANGIC_KARESI_HAM.md
                   TUR20_4_HAREKET_ZAMAN_FIZIK_HAM.md
                   TUR20_5_KAMERA_DILI_HAM.md
                   TUR20_6_KIMLIK_SUREKLILIK_HAM.md
                   TUR20_7_SES_DIYALOG_HAM.md
                   TUR20_8_POLITIKA_RED_HAM.md
                   TUR20_9_IS_AKISI_VERIM_HAM.md
DOĞRULAMA        ⭐ İLK KEZ: süzmeden ÖNCE canlı kaynak kontrolü (aşağıda §🔎)
SÜZME            ../04_ARASTIRMA_BULGULARI.md §TUR 20
İNDİĞİ YER       ../../OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md (süzmeden SONRA)
                 + tek satırlık işaretçiler (04 §T20.7)
```

## ⚠️ Biçim ve kaynak kaydı — dürüst sınır

```
① BİÇİM: rapor 1 · 4 · 5 · 6 · 8 · 9 TEK SATIR geldi (başlıklar cümleye
   yapışık, tablo hücreleri ayırıcısız); rapor 2 · 3 · 7'de paragraf ve
   başlık kırılması var. Rapor 2 · 4 · 6 · 7'de `[cite: n]` artıkları.
   Rapor 1'de çoklu referans görseli etiketleri BOŞ geldi (araç açılı
   etiketleri yuttu: "` ,  biçiminde`"); rapor 8'in atlatma listesinde
   "(Kaynak ID:)" alanları boş. Ham dosyalarda OLDUĞU GİBİ bırakıldı.

② KAYNAK LİSTESİ: 6/9 raporda VAR (3 · 5 · 6 · 7 · 8 · 9; 7'ninki alan adı
   düzeyinde), 3/9'da yok (1 yalnız tablo sütununda alan adı · 2 · 4). TUR 15-19'un "kaynak listesi hiç
   gelmedi" profilinden İYİ — ama listelerin çoğu üçüncü taraf blog ve
   toplayıcıdır (promptslove.com 9 raporun 7'sinde · kie.ai ·
   morphic · mindstudio · segmind · wavespeed · layer3labs · "Invideo FAQ").

③ BAĞIMSIZLIK YOK. Dokuz rapor aynı araçtan, aynı oturumda geldi ve aynı
   bir avuç kaynağa dayanıyor. İki raporun aynı şeyi söylemesi İKİ
   BAĞIMSIZ UYGULAYICI DEĞİLDİR (04'ün "(b) iki bağımsız uygulayıcı"
   kuralı): tırnak/iki nokta kuralı rapor 2 · 5 · 7'de üç kez geçiyor;
   5 ve 7 promptslove.com'a, 2 künyesiz bir "Gemini Omni Prompting Guide"a
   dayanıyor, resmî belgede yok (§🔎 ⑫). Süzmede KAYNAK sayıldı, rapor değil.

④ ETİKET ENFLASYONU. Raporlar "ÖLÇÜLMÜŞ" etiketini SSS sayfalarına
   ("Invideo FAQ" — rapor 4'te 11 kez), prompt rehberlerine ve başka
   motorların belgelerine ("Hailuo AI Guide" · "Runway ML Guide" — rapor 3,
   sürüm sütununda gemini-omni-1.1-flash yazarak) verdi. MOTOR KARIŞMASI
   kapısı (23_) tam bunu yakalamak içindi; süzmede bu satırların etiketi
   düşürüldü.

⑤ SAYI KATMANI ÇÜRÜK — beşinci tur üst üste. Rapor 4'ün arıza sıklıkları
   (%65 · %50 · %40 · %35 · %45 · %60), eylem güvenilirlikleri (%30-75),
   "karmaşık fizik %50/50", "işleme sırasında 12-8 FPS dalgalanma"; rapor
   5'in kamera uyum yüzdeleri (%70-90+ — rapor kendisi "hipotez" dedi);
   rapor 6'nın saniye eşikleri (2,8 · 3,5 · 4,5 · 5,2 · 6,0 · 6,8 · 7,2 s ·
   "±8 yaş"); rapor 3'ün "%60 hero zone · %30 lead room · 0,5-2 cm · %80
   deformasyon"; rapor 9'un "%25-35 kabul · %20-40 varyasyon". Hiçbiri
   kaynağıyla eşleşmedi → İNMEDİ. Kılavuz SAYISIZ yazıldı; yalnız resmî
   belgedeki sayılar (çözünürlük basamakları · 10 s bağlam · 40 s uzatma ·
   3 × 3 s video referansı) künyede durur.

⑥ UYDURULMUŞ DOĞRULAMA. Üç rapor "thinking_level" parametresini
   "resmî belgelerle doğrulanmış" diye yazdı (rapor 2 · 3 · 4); resmî
   Gemini API Omni sayfasında YOK (§🔎). Rapor 6 bir red mesajını gerçek
   bir forum başlığına bağladı; başlıktaki mesaj, model ve yüzey FARKLI
   (§🔎 ⑱). Bu iki bulgu raporların "Doğrulanabilir Bulgular" listelerinin
   bütününü şüpheli yapar: her satır kaynağıyla ayrıca eşleştirildi.

⑦ RAPORLARIN KENDİ KISITINI İHLAL ETTİĞİ KALIPLAR (süzmede düşürüldü):
   rapor 2 şablonları — "a single glowing button" (glow yasağı D3 · D29) ·
   "thin condensation gradually forms along the lower edge of the outer
   visor" (klip içi DURUM DEĞİŞİMİ + buğu, T11.5④) · "pulsing white warning
   strobes" (ışık durumu değişimi) · "Kodak Vision3 500T" (marka); rapor 8
   ikame tablosu — "subtle internal glare obscuring central facial
   features" (yüzü gizleyerek filtreden geçirme = ATLATMA + D79 vizör
   berrak/yüz okunur kuralının tersi); rapor 4 — "falling … toward the
   regolith" (düşme = bedenin durum değişimi, kısıt dışı).

⑧ YANKI: dokuz raporun "elenen çözümler / hat dışı" bölümleri 23_'nin
   beşinci cümlesinin geri okunmasıdır; sayılmadı. Rapor 2'nin "120–300
   kelime (Hedef Band)" satırı kısıtın bulgu olarak geri dönmesidir —
   aynı raporun kendi tablosu düzyazıya 30-80 diyor.
```

## 🔎 CANLI KAYNAK KONTROLÜ — 16.09.2026 (süzmeden önce)

> Raporların taşıyıcı iddiaları birinci el kaynakla eşleştirildi. Bu tura
> kadar süzme yalnız rapor metnine bakıyordu (TUR 12: "üç sürüm künyesinin
> üçü de yanlış" ancak sonradan fark edildi). Kontrol edilen sayfalar:
> **G1** blog.google — *Gemini Omni 1.1 Flash lets you build with more control*
> (27.08.2026) · **G2** ai.google.dev/gemini-api/docs/omni — *Generate and edit
> videos with Gemini Omni Flash* · **G3** docs.cloud.google.com Agent Platform
> model sayfası (dizin sayfası çıktı, parametre içermiyor) · **D** the-decoder.com
> haberi (arama özeti) · **M** mindstudio.ai test yazısı · **S** blog.segmind.com
> karşılaştırması · **P** promptslove.com incelemesi · **F** discuss.ai.google.dev
> başlık #178261. Sayfalar bir özetleyici üzerinden okundu; alıntılar o
> özetleyicinin aktarımıdır — birebir tarayıcı kopyası değildir.

| # | Raporların iddiası | Birinci el | Sonuç |
|:--:|---|---|:--:|
| ① | Motorun adı **Gemini Omni 1.1 Flash**, Google; API kimliği `gemini-omni-1.1-flash`; 27.08.2026 | G1 başlık + tarih · G2 model kimliği `gemini-omni-1.1-flash` | ✅ — **04 §TUR 3 "Osmi = Gemini Omni" hipotezi KAPANDI** |
| ② | 360p · 720p (varsayılan) · 1080p · 4K | G1 · G2 `resolution: "360p", "720p" (default), "1080p", "4k"` | ✅ |
| ③ | 360p taslak ~%60 hızlı, maliyet ~⅓ | D (arama özeti) | ✅ yön (D) |
| ④ | 10 s önceki bağlam; 10 s adımlarla 40 s'ye uzatma; yalnız sona eklenir | G1 · G2 *"extend videos by 10s, up to a total length of 40s"* · *"limited to appending to the end"* | ✅ |
| ⑤ | **Başlangıç + bitiş karesi** interpolasyonu | G1 *"specify the starting and ending frames of a shot"* · G2 `<FIRST_FRAME> <LAST_FRAME>` etiketleri | ✅ API'de VAR — **23_ ÇELİŞKİ ① kapandı** (Flow arayüzünde görünürlüğü sınanmadı) |
| ⑥ | Video referansı 3 klip × 3 s; referanstaki ses yok sayılır | G2 | ✅ |
| ⑦ | Referans GÖRSEL sayısı 10 (rapor 1 · 6) | G2 özeti "3" · S "1 to 10" | ⬜ ÇELİŞKİLİ — hat dışı, kılavuza girmez |
| ⑧ | Tohum (seed) YOK (rapor 1) / seed ile iş akışı (rapor 6 · 9) | G2 seed'den söz etmiyor · P "Omni has no seed parameter" · S kendi uç noktasında seed alanı gösteriyor | ⬜ resmî API'de BELGESİZ — üçüncü taraf sarmalayıcı sunuyor olabilir; **iş akışı seed'e kurulamaz** |
| ⑨ | Ayrı negatif prompt alanı yok; olumsuzlar prompt gövdesine | G2 *"negative prompts are not supported (you can put your negatives in the regular prompt: e.g., 'Do not do X')"* | ✅ |
| ⑩ | Ses HER klipte üretilir; kapatma anahtarı yok | G2 *"generates a video with audio"*; kapatma belgelenmemiş | ✅ (kapatma: belgesiz) |
| ⑪ | Resmî prompt ipuçları: tek plan · olumsuzlar · zamanlama | G2 *"In a single unbroken scene" · "In a single continuous shot" · "No scene cuts" · "No dialogue" · "No embellishments" · "No extra sound effects" · "After 3 seconds, a woman enters the scene" · "[0-3s] A person is walking"* | ✅ — raporlardan DAHA net |
| ⑫ | **Tırnak = ekrana yazı, iki nokta = konuşma** (rapor 2 · 5 · 7) | G2'de YOK. G2: *"You can prompt to include text in your video and Gemini Omni will render in a way that is correct and readable."* · P kuralı yazıyor ama *"did not burn API credits rendering dozens of test clips"* (sınamadı) · başka bir üçüncü taraf rehber tersini yazıyor ("dialogue in quotation marks (for lip-sync)") | ⚠️ resmî değil, üçüncü taraflar ÇELİŞİYOR — yön deponun kendi ölçümüyle (D40, Veo hattı: tırnaklı replik → gömülü altyazı 2/2) uyumlu → **PROB şart** |
| ⑬ | Optimum prompt 30-80 kelime; 100 üstü "modelle kavga" (rapor 5 · 7) | P → roo.beehiiv.com (tek bağımsız deneyci); G2 yalnız DÜZENLEME için *"Simple prompts work best … Overly descriptive prompts can lead to unintended changes"* | ⚠️ tek kaynak — deponun 120-300 bandıyla ÇELİŞİR → PROB |
| ⑭ | `thinking_level` parametresi "resmî belgeyle doğrulandı" (rapor 2 · 3 · 4) | G2'de YOK | ❌ uydurulmuş doğrulama |
| ⑮ | 1080p/4K = 720p'nin büyütmesi (korelasyon ~0,999); 360p ↔ 720p 0,441-0,725 (rapor 6) | S: *"Pulled frames from all four clips at four timestamps and correlated them"* — değerler S'de VAR | ✅ tek bağımsız ölçüm, yöntemi yazılı → **360p taslak son klibi ÖNGÖRMEZ** |
| ⑯ | LMArena T2V 1515 Elo #1 · I2V 1488 #2 (rapor 6 · 9) | M: T2V 1., I2V 2. (Minimax'in arkasında), *"vote counts are still low"*; Elo değerleri M ve S'de YOK | ⚠️ sıra ✅ · Elo sayısı kaynaksız |
| ⑰ | Yüzde/animasyonda bozulma | M tek prompt testi: *"the robot's head detaches"* · *"the face is inconsistent when viewed from different angles"* · *"The castle and background elements held up fine"* | ✅ yön (tek test) |
| ⑱ | Red mesajı *"Failed This prompt may violate our policies regarding the generation of content that includes well-known people"* — `gemini-omni-1.1-flash` · Gemini App/Flow · 14.08.2026 · kaynak #178261 (rapor 6) | F #178261 (14.08.2026) GERÇEK başlık ama: model **`gemini-omni-flash-preview`**, yüzey **Gemini API**, mesaj *"Request blocked due to prohibited content guidelines. Unable to show the generated video. The video was filtered out because it violated Google's Generative AI Prohibited Use policy."*; girdi: kurgusal, yapay zekâ üretimi yetişkin sunucu PNG'si + ağız hareketi (M·B·P vizemleri); **kurgusal olduğu açıklandığı hâlde iki kez engellendi**; Google yanıtı yok | ❌ mesaj · model · yüzey YANLIŞ AKTARILDI · ✅ vaka gerçek ve ÇIKTI aşamasında |
| ⑲ | Tanınmış kişi / reşit olmayan yüklemeleri | G2 *"Uploading and editing images containing certain recognizable people is not supported"* · reşit olmayan: yalnız EEA · İsviçre · Birleşik Krallık · *"content safety filters to both input prompts and generated video (which vary by region)"* | ✅ |
| ⑳ | Türkiye EMEA grubunda, ALLOW_ADULT varsayılan (rapor 8) | G2'de bölge listesi yalnız EEA/CH/UK; Türkiye adı geçmiyor | ⬜ kaynaksız — 04 §TUR 3 ② açık kalır |
| ㉑ | Fiyat $0,03 / 0,10 / 0,15 / 0,30 saniye (360p/720p/1080p/4K) | D | ✅ (D) — kılavuza YAZILMAZ, burada tarihli durur |
| ㉒ | Yalnız İngilizce tam destekli | G2 *"English (EN) is fully supported, but other languages have not been evaluated"* | ✅ |

```
KONTROLÜN DERSİ (04 §T20.0 ①): dokuz raporun resmî belgeyle ÖRTÜŞEN
katmanı (künye, modlar, sınırlar) sağlam; resmî belgenin SUSTUĞU katman
(sözdizimi, uzunluk, seed, parametre, red mesajı, bütün yüzdeler)
üçüncü taraf bloglardan ya da raporun kendisinden geldi ve en az üç
yerde yanlış aktarıldı. Kural: resmî belgede olmayan hiçbir SÖZDİZİMİ
kuralı PROB koşulmadan kapı olmaz.
```
