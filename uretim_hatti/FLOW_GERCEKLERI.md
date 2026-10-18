# 🎬 FLOW GERÇEKLERİ — Google Flow olgu sayfası

> **Ne için:** Flow'da hangi model hangi modu, kaç saniyeyle, kaç krediyle yapar; ne bilinmiyor.
> **Kim okur:** goruntu-yonetmeni · teknik-danisman · yonetmen · ses-tasarimcisi · besteci · kurgucu · kapak-tasarimcisi · Fable.
> **Ne değildir:** kural değil, araç gerçeği. Ajanlar araç bilgisini araştırma raporundan değil buradan alır.
> Satır davranış kuralı doğurmaz (AGENTS.md §1 ④). Hat kuralları kendi dosyalarında durur; burada yalnız "hat bağlamı" diye anılır.
> **Son doğrulama:** 07.10.2026. §4 sessiz ayarı, §3 model kredisi ve Ek (Gemini) 06.10.2026'da doğrulandı.
> **Kaynak:** `ARASTIRMA/04_SUZME_20261007.md` (R8 + §F Google) · `ARASTIRMA/02_SUZME_20261006.md` §A.
> Ham rapor (`ARASTIRMA/ham/08_…`) kanıt sayılmaz; yalnız süzmede KABUL edilen satır buradadır.

**Durum etiketi:** **RESMİ** = resmî Google sayfasında birebir cümle (süzmede ✅) · **ÖLÇÜLECEK** = sahibin Flow denemesiyle
görülür, SMOKE P# yazılı (P yoksa "P yok") · **BİLİNMİYOR** = resmî kaynakta yok ya da süzmede açılmadı ·
**ÇÜRÜTÜLDÜ** = kaynak tersini söylüyor ya da kaynak yok, yeniden önerilmez · **◐** = süzmede kısmen tuttu; RESMİ sayılmaz, neyin tuttuğu satırda yazar.

**Kaynak kısaltmaları** (parantezde sayfanın tarihi; tarihsiz sayfa: `G#` `Y#` 07.10.2026'da, `A#` 06.10.2026'da görüldü — "gör.")
`fl/N` = support.google.com/flow/answer/N · `yt/N` = support.google.com/youtube/answer/N · `blog` = blog.google ·
`vx` = docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice · `api` = ai.google.dev/gemini-api/docs/veo ·
`pol` = policies.google.com/terms · `G#` `Y#` = 04 §F satırı · `A#` = 02 §A satırı

> SMOKE: P9-P13 `SMOKE_TEST.md` "Araştırma denemeleri" bölümünde (sahip onayı 07.10.2026). P1-P8'in tanımı 02 §E'de; sahip onayı bekliyor. "Zincir testi" dosyada yazılı.

**Kim neye bakar:** goruntu-yonetmeni §1 §2 §4 §5 · teknik-danisman §1 §4 §9 §10 · yonetmen §1 §3 · ses-tasarimcisi §4 §6 ·
besteci §6 · kurgucu §2 §4 §9 Ek · kapak-tasarimcisi §5 §7 · Fable hepsi (`FLOW_KREDI` için §3).

## 1 · Modeller × modlar

| Mod | Veo 3.1 Lite | Veo 3.1 Fast | Veo 3.1 Quality | Gemini Omni Flash 1.1 |
|---|:--:|:--:|:--:|:--:|
| Metinden video (Text to Video) | 4 · 6 · 8 s | 4 · 6 · 8 s | 4 · 6 · 8 s ⚠ | ? |
| Karelerden video (Frames to Video, ilk + son kare) | 4 · 6 · 8 s | 4 · 6 · 8 s | 4 · 6 · 8 s ⚠ | var, yalnız Flow web · süre ? |
| Malzemeden video (Ingredients / References) | yalnız 8 s | yalnız 8 s | **yok** | 4 · 6 · 8 · 10 s |
| Uzatma (Extend) | **uzatmayı yalnız Lite yapar** | yok · klibi Lite uzatır | yok · klibi Lite uzatır | Omni videosu uzatılamaz |
| Videodan videoya (Video to Video editing) | ? | ? | **yok** | ? |

| Hücre | Durum | Kaynak |
|---|---|---|
| Veo metinden ve karelerden video 4/6/8 s · metinden video satırında "Both aspect ratios" (16:9 ve 9:16) | RESMİ | G1 · fl/16352836 |
| ⚠ Quality süresi: 06.10'da iki Flow sayfası çelişiyordu. 07.10'da G1 Quality'yi 4/6/8 s'e katıyor; çelişki ayrıca açılmadı | ÖLÇÜLECEK P6 | A2 · G1 |
| Malzemeden video Lite/Fast "8s videos only" | RESMİ | G1 · fl/16352836 |
| Quality: "Unsupported features in Veo 3.1 - Quality Ingredients/References to Video Video to Video editing Extend videos" | RESMİ | G2 · fl/16352836 |
| Omni Flash 1.1 malzemeden video 4/6/8/10 s | RESMİ | G1 notu · fl/16352836 |
| Omni başlangıç + bitiş karesi: "Add start & end frames … only available at Google Flow on web." | RESMİ · kullanımı ÖLÇÜLECEK P11 | G5 · fl/16352836 |
| "All Veo 3.1 8s videos can be extended, but you must use Veo 3.1 Lite to extend them." · "You can currently only extend Veo generated videos." | RESMİ | G3 · fl/16935718 |
| Uzatmanın eklediği süre · uzatılan klibin kalitesi | BİLİNMİYOR · P yok | süzmede yok |
| Videodan videoya Lite / Fast / Omni'de var mı, kaç s | BİLİNMİYOR | ham "Up to 10s" diyor; süzmede doğrulanmadı |
| Omni'de metinden video var mı, kaç s · Omni karelerden video kaç s | BİLİNMİYOR → ÖLÇÜLECEK P6 | süzmede yok |

**Okuma:**
- Malzemeden video ya da uzatma isteyen çekimde model Lite ya da Fast'tır. Quality bu modları açmaz.
- Quality klibi uzatılırsa devamını Lite üretir.
- Zincir halkası (gerçek ilk + son kare) = Frames to Video; üç Veo modelinde de var. Davranışı ölçülmedi (§9).

## 2 · Çözünürlük ve büyütme

> **Sahibin sorusu (07.10.2026), "4K diye süre belirlemem gerekiyor mu?":** Flow yardımına göre hayır; 4K üretimde seçilen bir şey değil, üretilmiş klibe Ultra planda 50 krediyle yapılan bir büyütmedir ve "yalnız 8 s" şartı yalnız API belgesinde yazıyor, Flow yardımında süre şartı yok.

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Büyütme nerede | "Upscaling to 1080p and 4K is only available in Flow, the Gemini API and Vertex AI" | RESMİ | G4a · blog …/veo-3-1-ingredients-to-video/ (13.01.2026) |
| 1080p büyütme | bütün modeller · Plus, Pro, Ultra: **0 kredi** | RESMİ | G4b · fl/16526234 |
| 4K büyütme | yalnız Ultra: **50 kredi** (klip başına) · Ultra dışı: "Not available" | RESMİ | G4b · fl/16526234 |
| API'de büyütme süresi | "1080p (8s length only), 4k (8s length only)". API'de birebir, Flow yardımında süre yazmıyor | ◐ | G4c · api (17.09.2026) |
| Flow'da büyütmenin süre sınırı | yazmıyor | BİLİNMİYOR → §9 | G4c |
| Omni 360p taslak | "Pro and Ultra subscribers can upscale their Omni 360p video generations to 720p for 0 credits." | RESMİ | G5 · fl/16352836 |
| Büyütmesiz üretim çözünürlüğü (Veo) | Flow için birebir cümle yok; 720p/1080p/4K değerleri yalnız API belgesinde | ÖLÇÜLECEK P6 (ffprobe) | A2 |
| İndirme biçimi | video .mp4 · GIF 270p. G11 grubunda; tek başına işaretlenmemiş | ÖLÇÜLECEK P6 | G11 |

## 3 · Kredi

| Kalem | Değer | Durum | Kaynak |
|---|---|---|---|
| Günlük | 50 kredi, aboneli ve abonesiz herkese | RESMİ | G8 |
| Aylık ek | Plus 200 · Pro 1.000 · Ultra ($100) 10.000 · Ultra ($200) 25.000 | RESMİ | G8 · fl/16526234 |
| Devir | "Unused monthly Google Flow credits do not roll over" | RESMİ | G8 |
| Başarısız üretim | "You are not charged any credits for failed generations." | RESMİ | G8 · fl/16353333 |
| Klip kredisi | Lite **10** · Fast **20** · Quality **100** | RESMİ (02 §A2 satırı ◐; ◐ kısmı fps ve 1080p/4K, kredi kısmı resmî Flow) | A2 · gör. 06.10 · URL süzmede yok |
| Büyütme | 1080p 0 · 4K 50 (yalnız Ultra) · Omni 360p → 720p 0 (Pro/Ultra) | RESMİ | §2 |
| Kredi süreye göre değişir mi (4 s = 8 s?) | yazmıyor | BİLİNMİYOR → P6 · P7 kredi kaydı | — |
| Omni Flash 1.1 kredisi | süzmede yok | BİLİNMİYOR → P11 | — |
| Politika reddi "failed" sayılır mı | süzmede açılmadı | BİLİNMİYOR · P yok | — |

Hat bağlamı: her deneme kredisiyle `NOTLAR.md`'ye yazılır (AGENTS §4); toplam `ODA/DURUM.md` → `FLOW_KREDI`.

## 4 · Ses

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Sessiz çıktı ayarı | "Return silent videos": "all video generations are silent" | RESMİ | A1 · Flow yardımı · gör. 06.10 · URL süzmede yok |
| Ses üretimde mi kapanıyor, sonradan mı atılıyor | yazmıyor | BİLİNMİYOR → P1 | A1 |
| Sessiz üretim ağız ve beden "konuşma izini" kaldırır mı | — | ÖLÇÜLECEK P1 | 02 R4 |
| Ses ve video birlikte mi üretiliyor | model kartı ikisinin de difüzyondan geçtiğini yazıyor; "jointly" kelimesi yok | ◐ | A3 |
| Konuşma biçimi · Vertex | "use a colon ( : ) after the speaker's action to denote speech and avoid using quotation marks" (amaç: ekrana yazı basılmasın) | RESMİ | G9 · vx (06.10.2026) |
| Konuşma biçimi · Gemini API | "Dialogue: Use quotes for specific speech." | RESMİ | G9 · api (17.09.2026) |
| İki resmî belge çelişiyor | hat bugün `she says, "<line>"` yazıyor ve iki noktayı yasaklıyor (yalnız ağız kadrajdaki replik) | ÖLÇÜLECEK P9 | 04 R8 |

Hat bağlamı:
- Model sesi taslakta atılır (AGENTS §2). İş emrine "Return silent videos AÇIK" 02 §D 2'de önerildi.
- İstisna (sahip kararı 12.10.2026, THE_MAYDAY_SEA): FILM.md §5 Kaynak = **model sesi** olan filmde replikler video promptunda, Omni konuşmayı videoda üretir →
  o filmde "Return silent videos" **KAPALI**; klibin sesi `kurgu.py` `klip_sesi` ile yalnız replik için filme girer, ortam yatağı yine kurgudan. Omni'nin aynı sesi
  başka klipte tekrar verip veremediği ÖLÇÜLMEDİ → SMOKE P18.
- 04 §D 2 önerisi: P9'a kadar `film_dogrula.py` iki biçimi de kabul etsin (`says, "<line>"` · `says: <line>`).
- BILINEN_TUZAKLAR §C (prompt kelimesi kadraja basılıyor) Vertex'in uyarısıyla aynı yönde.

## 5 · Görsel

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Varsayılan görsel model | Nano Banana 2 Lite · Ultra'da Nano Banana Pro | ◐ (doğrulayıcı Google sayfasında gördü; birebir cümle süzmede yok) | G12c · 04 R8 |
| Karakter | "Upload or generate 1 or 2 images that show the visual appearance of your character." · promptta çağrılır | RESMİ | G7 · fl/16935308 |
| Karakter kask, vizör ve giysi kimliğini malzemeden iyi tutar mı | — | ÖLÇÜLECEK P10 | 04 §C |
| Başlangıç karesinin en-boyu videodan farklıysa Flow ne yapar (kırpar mı, doldurur mu) | süzmede resmî cümle yok. "16:9 + 9:16 kırpar/doldurur" alıntısı üçüncü taraf blogdan | BİLİNMİYOR · P yok | A12 |

Hat bağlamı:
- Başlangıç karesi videoyla aynı en-boy ve çözünürlükte üretilir (02 R3 KABUL, şablonda yazılı).
- Hangi görsel modelinin seçili olduğu ilk üretimde `NOTLAR.md`'ye yazılır. Referans karesi modeli sahibin planına göre seçilir (04 R8).

## 6 · Müzik ve efekt

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Google Flow Music | gerçek ürün: "my bandmates and I started Google Flow Music (formerly ProducerAI)" | RESMİ | G6a · blog …/believe-flow-music-partnership/ (06.05.2026) · fl/17083868 |
| Lyria 3.5 | Flow Music'te 29.07.2026'dan beri | ◐ | G12f |
| SynthID (müzik) | "All Lyria 3 and Lyria 3 Pro outputs are embedded with SynthID". Cümle Lyria 3 ve 3 Pro'yu sayıyor, 3.5'i anmıyor | RESMİ | G6c · blog …/lyria-3-pro/ |
| Parça süresi | "30-second clips to three-minute tracks". Cümle Google Vids yazısında, Lyria 3 Pro yazısında değil | ◐ | G6b · blog (Vids, 02.04.2026) |
| Mondo Sónico | ortam, foley ve bağlamsal efekti ayrı izler hâlinde üreten Flow aracı (23.09.2026) | RESMİ (varlığı) · kullanımı ÖLÇÜLECEK P12 | G12g · URL süzmede yok |
| Ticari kullanım (Flow ve Flow Music çıktısı) | **açık izin cümlesi yok**; yalnız "Google won't claim ownership over that content." | BİLİNMİYOR | G6d ∅ · pol |
| ses-muzik skill'indeki "ticari kullanım: ücretli plan gerekir · 14 gün içinde silinebilir" | resmî kaynakta bulunamadı | BİLİNMİYOR | 04 §D 4 |

Hat bağlamı: ticari koşul Google Hizmet Şartları'na bağlı. Haklar satırı `apexaic/POLITIKA_VE_RISK.md` §4'te, sahibin kontrolünde (04 §D 4).

## 7 · Filigran ve köken

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Görünür filigran | Hindistan, Güney Kore, Vietnam'da otomatik; başka yerde isteğe bağlı anahtar | ◐ | G11a |
| SynthID | her Flow çıktısında | ◐ | G11a (04 R8 satırı) |
| C2PA → YouTube | C2PA metadatası varsa YouTube etiketi kendisi koyar; değiştirilemez | RESMİ | Y4 · yt/14328491 |
| YouTube bildirimi | "Disclosing AI content won't limit a video's audience or impact its eligibility to earn money." | RESMİ | Y4 · yt/14328491 |
| Fotogerçekçi yapay zekâ içeriği bildirilir | "disclose … photorealistic content" | RESMİ | A5 · YouTube yardımı · gör. 06.10 |
| Flow dosyası C2PA taşıyor mu | `apexaic/CAPRAZ_YAYIN.md` §2 "gömer" diyor; süzmede resmî cümle yok | BİLİNMİYOR · P yok | — |

Hat bağlamı:
- Filigran promptla çözülmez → ARAÇ AYARI + yeniden dışa aktarma (ARIZA_LISTESI T17). İş emrine "Visible watermarking KAPALI" 04 §D 3'te önerildi.
- C2PA temizlenmez (`apexaic/CAPRAZ_YAYIN.md` §2).

## 8 · Veri

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| İnsan incelemesi | "up to 18 months" | RESMİ | G11c |
| "Help improve Google Flow" | kapatılabilir | RESMİ | G11d · fl/17025472 |

Açık ya da kapalı olması sahibin tercihidir (04 R8 NOT).

## 9 · Bilinmeyenler — ölçülene kadar varsayım yazılmaz

| Soru | Bilinen | Nasıl görülür |
|---|---|---|
| Kare hızı | Flow'da yazmıyor; API'de Veo 3.1 "24fps" (G13 ∅) | ÖLÇÜLECEK P6 · `ffprobe … r_frame_rate` |
| Gerçek klip süresi (`KLIP_SURESI`) · Quality süre çelişkisi (§1 ⚠) · büyütmesiz çözünürlük | resmî 4/6/8 s; dosya süresi ve çözünürlük ölçülmedi, şablon künyesi "ölçülmedi" | ÖLÇÜLECEK P6 + Zincir testi 1 · `ffprobe … width,height … format=duration` |
| Büyütmede süre sınırı | Flow'da yazmıyor; API'de yalnız 8 s (G4c ◐) | P yok. P6 sırasında 4 ya da 6 s'lik bir klipte 1080p büyütme (0 kredi) denenebilir |
| Frames to Video bitiş karesini tutuyor mu, hangi modelde | resmî: ilk + son kare üç Veo modelinde var | Zincir testi 1-5. Sonuç yazılmadan zincirli üretim yok (AGENTS §0) |
| Dikişte ease-in/out var mı | kaynaksız | ÖLÇÜLECEK P5 |
| 10 s'lik çekim nasıl üretilir (hat kuralı: her çekim 10 s, sahip kararı 08.10.2026) | Veo 4/6/8 s (§1); 10 s yalnız Omni Flash Ingredients; uzatma yalnız Lite | ÖLÇÜLECEK P14 · `ffprobe … format=duration` + `kareler.py kuyruk` |
| El işinde Frames mı, Ingredients mi | ölçülmedi | ÖLÇÜLECEK P3 |
| Sessiz ayar: ses nerede kapanıyor, konuşma izi kalıyor mu | A1 | ÖLÇÜLECEK P1 |
| Flow kısa promptu yeniden yazıyor mu | Vertex'te kısa promptlar için "prompt rewriter" var; Flow için resmî bilgi yok (A16) | ÖLÇÜLECEK P2 |
| Konuşma: tırnak mı, iki nokta mı | G9 çelişkisi (§4) | ÖLÇÜLECEK P9 |
| Karakter kask ve giysiyi tutuyor mu | G7 (§5) | ÖLÇÜLECEK P10 |
| Omni taslağı hareket ve kadraj denemesine yeter mi; 10 s işe yarar mı | G5 (§1, §2) | ÖLÇÜLECEK P11 |
| Mondo Sónico ayrı iz veriyor mu, vakum kuralına uyuyor mu, ticari koşulu | G12g (§6) | ÖLÇÜLECEK P12 |
| Olumsuz ifade Veo'da ters etki yapıyor mu | Runway ve Luma'da resmî; Veo için resmî cümle yok | ÖLÇÜLECEK P13 |
| Kredi süreye bağlı mı · kullanılabilir deneme oranı | §3 | ÖLÇÜLECEK P6 · P7 |
| Uzatmanın eklediği süre | §1 | BİLİNMİYOR · P yok |

## 10 · Çürütülenler — yeniden önerilmesin

| İddia | Neden | Durum | Kaynak |
|---|---|---|---|
| "Aracın verdiği 10 s klip" (eski hat) | Veo 3.1 Flow'da 4/6/8 s. 10 s yalnız Omni Flash 1.1'in malzemeden video seçeneğinde var | ÇÜRÜTÜLDÜ | A2 · G1 · 03 SINAMA SETİ |
| YouTube hedefi −16 LUFS / −1.5 dBTP | YouTube resmî sayı yayımlamıyor, yalnız sesi kısıyor. Hat −14 LUFS / ≤ −1 dBTP (yaygın değer; `kurgu.py yukseklik`) | ÇÜRÜTÜLDÜ | A6 |
| Ünlü yüz filtresini metinle ya da tek pikseli değiştirerek aşmak | politika atlatma; kanal sağlığı riski. Yanlış ret olursa kare yeniden tasarlanır (kask, vizör, açı); filtre aşılmaz | ÇÜRÜTÜLDÜ · **RED: politika atlatma** | 04 R8 · `apexaic/POLITIKA_VE_RISK.md` |
| Nano Banana 2 Flow'da varsayılan | 26.02.2026'da öyleydi; bugün değil (§5) | ÇÜRÜTÜLDÜ (eskidi) | G12c |
| Görsel maliyeti "1.000 görsel 0,034 $" | açıkça yanlış sayı | ÇÜRÜTÜLDÜ | 02 R3 |
| "Zincir 4. halkada kopar" | sayfa gövdesi açılmıyor, yöntem yok. ≤4 halka tavanı hipotez olarak kalır | ÇÜRÜTÜLDÜ (kanıt olarak) | A10 |

Hat dışı (API forum raporları, doğrulanmadı): 9:16 isteğinin 16:9'a zorlanması · `generateAudio:false` hatası. Hat API kullanmıyor (04 R8 NOT).

## Ek · Gemini (tarama aracı, Flow değil)

| Olgu | Durum | Kaynak |
|---|---|---|
| Gemini videoyu varsayılan 1 fps örnekler | RESMİ (API belgesi) | A4 · gör. 06.10 |
| API'de `videoMetadata fps` ile özel fps var; Gemini uygulamasında fps ayarı yok | RESMİ (API) · uygulama: A4 gözlemi | A4 |

Hat bağlamı: 1 s'den kısa kusur (parmak erimesi, tek karelik sıçrama) taramada kaçabilir (02 R5 KABUL).

## Ek 2 · Gemini uygulaması — Omni (üretim aracı, Flow değil) · 16.10.2026

> Kaynak: `ARASTIRMA/11_SUZME_20261016.md` §A (V1-V10). `gm` = gemini.google/overview/video-generation (tr) · `gh/16126339` = support.google.com/gemini/answer/16126339.
> THE_SKY_CATCH bu yolla üretildi (GPT Image → Gemini). Yöntem: `GPT_IMAGE_OMNI_KILAVUZU.md`.

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Model | Gemini Omni, Gemini uygulamasında Veo 3.1'in yerini alıyor | RESMİ | V1 · gm |
| Süre | "10 saniyelik videolar oluşturun" | RESMİ · dosya süresi ÖLÇÜLECEK (ffprobe) | V2 · gm |
| Ses | "Doğal ses üretme" · "You can also ask Gemini to generate audio with your video." | RESMİ | V2 · gm · gh/16126339 |
| Görsel girdi | "You can upload one video and up to 5 images." · "Referans fotoğraflar kullanarak (5 adede kadar)" | RESMİ | V3 |
| Oran | "If you upload a reference image or video, the aspect ratio will match your uploaded content." | RESMİ | V5 · gh/16126339 |
| Uzatma · videodan videoya · etkileşimli düzenleme | var; "Özellikler katmana ve coğrafi konuma göre değişir." | RESMİ (varlığı) · hesapta ÖLÇÜLECEK | V4 · gm |
| Ayrı başlangıç + bitiş karesi | Gemini uygulamasında resmî cümle yok (Flow web'de var, §1). Geliştirici blogu (API): "specifying the starting and ending frames of a shot" | uygulamada BİLİNMİYOR · API RESMİ | V6 · `13` V12 |
| Sahne uzatma süresi (API) | "You can extend videos in 10-second increments up to a total cumulative length of 40 seconds." · çıkış 27.08.2026 | RESMİ (API) · uygulamada ÖLÇÜLECEK | `13` V11 · blog …/build-with-gemini-omni-1-1-flash |
| Video referansı (API) | "Reference up to three seconds of video when crafting your scene." | RESMİ (API) | `13` V13 |
| Veo 3.1 referans görseli (karşılaştırma) | "Veo 3.1 now accepts up to 3 reference images" — Veo için; Omni değil | RESMİ | `13` V19 · api |
| fps · çözünürlük · seed · günlük kota · kredi | yazmıyor | BİLİNMİYOR | — |

Hat bağlamı:
- Zincir (AGENTS §0) yalnız Flow web'de kurulur; Gemini uygulamasında devamlılık `GPT_IMAGE_OMNI_KILAVUZU.md` §8.
- 5 görsel = 5 referans; 5 zaman anahtarı ya da 5 sabit kamera açısı değildir.
- Oran karenin pikselinden gelir: 1536×1024 (3:2) kare 16:9 video vermez → `GPT_IMAGE_OMNI_KILAVUZU.md` §13.

## Ek 3 · GPT Image (OpenAI) — başlangıç karesi aracı · 16.10.2026

> Kaynak: `ARASTIRMA/15_SUZME_20261016.md` §A (V25-V40). `oai/guide` = developers.openai.com/api/docs/guides/image-generation ·
> `oai/sb` = …/models/gpt-image-2.5-sunburst · `oai/d3` = …/models/dall-e-3 · `oai/forum` = community.openai.com duyurusu (08.09.2026).
> help.openai.com "Images in ChatGPT" 403 verdi; ChatGPT satırları ◐.

| Olgu | Değer | Durum | Kaynak |
|---|---|---|---|
| Güncel modeller (API) | `gpt-image-2.5-sunburst` ("Our most capable model for image generation and editing"; hassas düzenleme, daha yavaş; snapshot `…-2026-09-08`) · `gpt-image-2.5-flare` (hızlı) | RESMİ | oai/sb · oai/guide · oai/forum |
| ChatGPT | "ChatGPT Images 2.5", 08.09.2026'dan beri bütün ChatGPT kullanıcılarına; hangi API modelini kullandığı yazmıyor | RESMİ (duyuru) · model eşlemesi BİLİNMİYOR | oai/forum |
| DALL·E 3 | "deprecated and removed from the API" | RESMİ | oai/d3 |
| Boyut (API) | hazır: 1024×1024 · 1536×1024 · 1024×1536; özel `WIDTHxHEIGHT` ("such as 1536x864"): kenarlar 16'nın katı, oran 1:3-3:1, en uzun kenar ≤3840 | RESMİ | oai/guide |
| 16:9 (API) | 1280×720 · 1536×864 · 2048×1152 · 2560×1440 · 3840×2160 (1920×1080 olmaz: 1080 16'nın katı değil) | RESMİ kurala göre hesap | 15 V28 |
| Oran (ChatGPT) | "any aspect ratio", oran seçici ya da promptta oran | ◐ · indirilen dosyanın pikseli ÖLÇÜLECEK | 15 V29 |
| Kalite | low · medium · high · xhigh · max · auto (xhigh/max yalnız 2.5) | RESMİ | oai/guide |
| Girdi görseli | örnekte 4; en çok sayı yazmıyor | BİLİNMİYOR → ÖLÇÜLECEK | oai/guide |
| `input_fidelity` | "controls how strongly a model preserves details from input images during edits"; gpt-image-2'de değiştirilemez; 2.5 değerleri açılmadı | RESMİ (varlığı) · ÖLÇÜLECEK | oai/guide |
| Maske | alfa kanallı; çok görselde ilk görsele uygulanır | RESMİ | oai/guide |
| Çok turlu | `previous_response_id` · `action: "edit"` | RESMİ (API) | oai/guide |
| Biçim · şeffaflık | png (varsayılan) · jpeg · webp · `background: "transparent"` | RESMİ | oai/guide |
| Fiyat (Sunburst) | 1M token: metin girdi $5 · görsel girdi $8 · görsel çıktı $30 (Batch $15) | RESMİ (16.10.2026) | oai/sb |
| Olumsuz ifade | ayrı parametre yok; resmî örneklerde "No logos" · "No watermarks" · "No text" satırları | RESMİ | 13 V17 |

Hat bağlamı: başlangıç karesi **16:9 piksel** üretilir (API'de özel boyut, ChatGPT'de oran seçici + ölçüm); olmazsa kırpılır (`GPT_IMAGE_OMNI_KILAVUZU` §13).
Kullanılan model ve arayüz her denemede NOTLAR'a yazılır.

> **Bu sayfa ne zaman değişir:** SMOKE sonucu gelince satır ÖLÇÜLECEK'ten "ölçüldü (tarih · film · değer)"e geçer.
> Resmî sayfa değişirse satır yeni tarih ve kaynakla yazılır; eski değer §10'a taşınır, silinmez.
> Kaynaksız ya da tarihsiz satır girmez. Değişiklik sahibin kararıyla.
