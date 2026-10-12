# 📈 İZLEYİCİ VERİSİ — yayından sonra YouTube'dan ne alınır, nasıl okunur

> **Ne için:** yayından sonra hangi ölçütün, hangi gün, hangi yoldan alınacağını; nereye yazılacağını; düşüşün nasıl
> çekime çevrileceğini ve yayın öncesi tahminle nasıl karşılaştırılacağını söyler. `paketleme` §F10'un ayrıntısıdır.
> **Kim kullanır:** **sahip** veriyi alır (Studio ya da API; ajanların YouTube erişimi yok) · **Fable** faz 10'da düşüşü
> çekime çevirip `NOTLAR.md`'ye yazar · **yayin** faz 6 ve 9'da önceki filmlerin CTR ve A/B satırlarını okur.
> **Ne değildir:** hedef ya da "iyi oran" tablosu değil (kaynaklı aralık yok, §9) · algoritma tavsiyesi değil · betik değil
> (§2 yalnız sorgu alanlarını verir) · kural kaynağı değil (§8).
> **Tarih:** 07.10.2026. **Kaynak:** `ARASTIRMA/04_SUZME_20261007.md` R10 + §F Y1-Y9; bu dosya yazılırken açılan resmî
> sayfalar ("gör. 07.10"). Ham rapor (`ARASTIRMA/ham/10_…`) kanıt sayılmaz. Sayıların tek kaynağı `apexaic/DIS_SAYILAR.md` §1'dir;
> burada yalnız bu işin gerektirdiği satırlar anılır.

`yt/N` = support.google.com/youtube/answer/N · `api/…` = developers.google.com/youtube/analytics/{metrics · dimensions ·
channel_reports} · `Y#` = 04 §F satırı · ◐ = kısmen doğrulandı · ∅ = bu turda bulunmadı

---

## 1 · Ölçütler

| Ölçüt | Resmî tanım (birebir) | Studio'da | API adı | En düşük eşik | Uzun video ↔ Shorts |
|---|---|---|---|---|---|
| Gösterim | "How many times your thumbnails were shown to viewers on YouTube through registered thumbnail impressions." · "Impressions are counted if the thumbnail is shown for more than 1 second and at least 50% of the thumbnail is visible" (yt/7577430 · Y5) | Analytics → Content sekmesi | **yok**: API ölçütlerinde küçük resim gösterimi yok (api/metrics, gör. 07.10) → Studio | eşik yok; sayım kuralı tanımda | Shorts → son satır |
| CTR | "How often viewers watched a video after seeing a thumbnail." (yt/7577430) | aynı | **yok** (aynı sebep). `annotationClickThroughRate` CTR değildir (§9) | evrensel eşik yok → DIS_SAYILAR §1 "CTR" | Shorts → son satır |
| Ortalama izleme süresi | "The average length, in seconds, of video playbacks." (api/metrics, gör. 07.10) | video → Analytics → Overview · Engagement | `averageViewDuration` | ∅ | ∅ |
| Ortalama izlenme yüzdesi | "The average percentage of a video watched during a video playback." (aynı) | aynı | `averageViewPercentage` | ∅ | ∅ |
| Mutlak tutma | "The absolute ratio of viewers watching the video at the given point in the video." Tekrar izlenen kısımda 1'i geçebilir (Y2) | Content → video → Analytics → Overview ya da Engagement (yt/9314415) | boyut `elapsedVideoTimeRatio` + ölçüt `audienceWatchRatio` | işlenme → DIS_SAYILAR §1 "Tutma verisi" · görüntülenme eşiği ∅ | ∅ |
| Göreli tutma | "A measurement that shows how well a video retains viewers during playbacks in comparison to all YouTube videos of similar length." 0-1 · "A median value of 0.5…" (Y2) | aynı kart → SEE MORE: "how your video compares to all YouTube videos of similar length" | `relativeRetentionPerformance` | aynı | ∅ |
| Kilit anlar | "Intro tells you what percentage of your audience still watched your video after the first 30 seconds." · Dips: "…either skipped or moments where viewers stopped watching your video completely." (yt/9314415 · Y1) | tutma kartı | doğrudan karşılığı yok. Intro ≈ 30. saniyeyi kapsayan noktanın `audienceWatchRatio`'su (öneri, §2.3) | **≥60 s ve ≥100 görüntülenme:** "Your video should also be at least 60 seconds long and have at least 100 views." | 60 s altındaki dikey kesimde kilit an çıkmaz (eşik gereği) |
| Shorts seçimi | "How many chose to view" (yt/12942217, Shorts sürümü · Y6 ◐) | Shorts'un Analytics'i | ∅ | ∅ | yalnız Shorts. Uzun videoda karşılığı gösterim + CTR. Görüntülenme sayımı → DIS_SAYILAR §1 |

---

## 2 · Dışa aktarma

### 2.1 Studio (elle, CSV)
```
1. Studio → Content → video → Analytics                                   (yt/9314415)
2. "Under a report, click ADVANCED MODE or SEE MORE."                      (yt/9717005, gör. 07.10)
3. "At the top, select Export current view and choose your preferred file format." → CSV
   ⚠ "Downloaded reports are limited to 500 rows."
4. Üç dosya: (a) özet: gösterim · CTR · ort. süre · ort. %   (b) trafik kaynağı   (c) tutma eğrisi
5. Ad: <GG.AA>_<48s|7g|28g>_<a|b|c>.csv → ~/film_medya/<FILM>/analiz/youtube/
   (öneri; README § Medya'da bu alt klasör yok. Ham dosya ve ekran görüntüsü repoya girmez, repoya yalnız NOTLAR satırı girer)
```
⚠ Tutma eğrisi dışa aktarılan dosyaya nokta nokta geliyor mu, doğrulanmadı. Gelmezse iki yol var: API (§2.2) ya da
ekran görüntüsü + düşüş saniyeleri (`paketleme` §F10.1).

### 2.2 API — betik yok, yalnız alanlar (api/dimensions · metrics · channel_reports, Y2)
```
uç          reports.query (YouTube Analytics API)
ids         channel==MINE           startDate  yayın günü      endDate  ölçüm günü (48 s · 7 g · 28 g)
dimensions  elapsedVideoTimeRatio
metrics     audienceWatchRatio,relativeRetentionPerformance
filters     video==<VIDEO_ID>       ⛔ zorunlu, tek video: "the value must specify a single video ID"
            isteğe bağlı: ;subscribedStatus==SUBSCRIBED  ya da  UNSUBSCRIBED   (abone ayrımı, §4)
yetki       https://www.googleapis.com/auth/yt-analytics.readonly  (gelir için yt-analytics-monetary.readonly; burada gerekmez)

özet        metrics=views,averageViewDuration,averageViewPercentage            filters=video==<VIDEO_ID>
trafik      dimensions=insightTrafficSourceType  metrics=views,estimatedMinutesWatched  filters=video==<VIDEO_ID>
```
⚠ Tutma raporunun isteğe bağlı süzgeçleri yalnız `audienceType` · `subscribedStatus` · `youtubeProduct`'tır
(api/channel_reports, gör. 07.10). Trafik kaynağına göre süzülmez. Gösterim ve CTR API'de yok, Studio'dan alınır.

### 2.3 Çözünürlük — bir nokta kaç saniye
API her video için 100 eşit nokta verir: "ratio values ranging from 0.01 to 1.0" ve "The dimension's value denotes the
exclusive end of the interval." Yani r değerli satır [r − 0,01 ; r) × süre aralığını kapsar. Bir nokta = süre / 100.
```
 4 dk (240 s)   2,4 s   çekimin dörtte biri (çekim 10 s, SABLON/FILM.md §4)          → düşüş ÇEKİME çevrilebilir
 8 dk (480 s)   4,8 s   bir çekim boyu                                               → çekim ya da komşu iki çekimden biri
16 dk (960 s)   9,6 s   birkaç çekimi kapsar                                         → ancak SAHNEYE çevrilir
```
**Örnek (4 dk):** r = 0.25 → [0,24 ; 0,25) × 240 = 57,6–60,0 s → `kurgu.py liste <timeline> --zaman 00:57.6` ve `--zaman 00:59.9`; ikisi aynı çekimi verirse düşüş o çekimdedir.

- `kurgu.py liste --zaman` çıktısı: `MM:SS.s → <çekim> · <dosya> içinde <kaynak saniyesi> s`. Film dışında kalan saniyede ⛔ verir.
- Çekimin sahnesi FILM.md §2/§4'ten okunur.
- Süre olarak `kurgu.py liste` son satırındaki toplam alınır. Videoya timeline dışında bir şey eklendiyse (örn. logo introsu), önce onun süresi çıkarılır.

---

## 3 · Kayıt — film başına tek satır

**Yer:** `<FORMAT>_filmler/<FILM>/NOTLAR.md`. Önerilen bölüm adı `## İZLEYİCİ VERİSİ (YouTube · uretim_hatti/IZLEYICI_VERISI.md)`,
İZLEME ile KARARLAR arasında. `SABLON/NOTLAR.md` bu dosyayla değişmez; bölümü eklemek sahibin kararıdır. Kimlik (başlık,
kapak, yayın saati) yayından önce KARARLAR'a yazılır (`paketleme` §F9.6); burada tekrarlanmaz.

| Video ID | Format | Süre | Gösterim 48s / 7g / 28g | CTR 48s / 7g / 28g | Ort. izlenme % 48s / 7g / 28g | İlk 30 s (Intro) 48s / 7g / 28g | Kritik düşüş → `kurgu.py liste --zaman` → çekim | A/B sonucu | Trafik karışımı 28g (ilk 3 · pay) |
|---|---|--:|---|---|---|---|---|---|---|
| `<id>` | yatay 4 dk | MM:SS.s | __ / __ / __ | __ / __ / __ | __ / __ / __ | __ / __ / __ | MM:SS.s–MM:SS.s → Cnn · … | kazanan A/B/C · aynı · sonuçsuz · test yok | <kaynak> __ % · … |

- 48 saat, 7 gün ve 28 gün sonra aynı satır doldurulur. Satır yeniden yazılmaz, yalnız boş hücre dolar.
- Düşüş satırı 48-72 saatte açılır (F10) ve 28 günde yeniden okunur. Kayan ya da kaybolan düşüş "(28g: yok)" diye işaretlenir.
- Görüntülenme 100'ün altındaysa (§1 kilit an eşiği) düşüş hücresine "n<100" yazılır ve okunmaz.
- A/B testi sürerken CTR hücresine "(test)" eklenir.

### 3b · Açılış deney satırı (12.10.2026, `uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §8)

Aynı bölümde, kayıt satırının altında. F9'da açılır (KABUL F9.7), Giriş hücreleri yukarıdaki satırdan okunur.

| Test edilen tek açılış değişkeni | H1 kapak anı ilk 30 s'de (saniye) | H2 insan ilk kez (saniye · beden/el/yüz) | H3 ilk 30 s'de görünen kusur yok | Başlık saniyesi | İlk replik saniyesi | Ana sayfa + önerilen payı 28g | Yorum (28g) |
|---|---|---|---|---|---|---|---|
| <örn. "insan C01'de"> | evet · 00:24 | 00:08 · beden | evet | 00:27 | 00:12 | __ % | <tipik bandın üstü/içi/altı> |

- Filmler yalnız aynı trafik kaynağı içinde karşılaştırılır. Bir değişken iki filmde aynı yönde sonuç verirse sahibe kural önerilir (AGENTS §1 ④).

### 3c · Kapak ve başlık değişikliği kaydı (12.10.2026, `uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §9)

Eski videoda ya da yeni filmde her paket değişikliği bir satır. Aynı videoda bir değişiklikten sonra 14 gün başka değişiklik yapılmaz.

| Tarih | Video ID | Ne değişti (kapak · başlık · ikisi; tek değişken) | Yol (Test & Compare · elle) | Önce 14 g: gösterim · tıklama oranı · ort. izlenme (aynı trafik kaynağı) | Sonra 14 g: aynı üçü | Test sonucu (kazanan · aynı · sonuçsuz) | Karar |
|---|---|---|---|---|---|---|---|
| 12.10.2026 | `<id>` | kapak: kalabalık uzay → tek figür + turuncu vurgu | Test & Compare (mevcut ilk sırada) | 99.000 · %1,07 · __ | __ · __ · __ | __ | kalıcı · geri al · yeniden dene |

- İki kapak arasındaki farkın gerçek olup olmadığı kılavuz §8'deki hata payıyla okunur.

**Kanal düzeyi: sahibe öneri** (bu dosya hiçbir tablo açmaz):
- Eski `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` eski hattadır, düzenlenmez (AGENTS §1 ③).
- Öneri: `apexaic/` altında tek dosya (ad önerisi `YAYIN_PERFORMANSI.md`). Film başına bu satırın 28g hücreleri + NOTLAR bağlantısı; ayrı bölümde taban olarak eski videolar (§4).
- ⚠ `apexaic/YAYIN_PLANI.md` §6 hâlâ 08'e işaret ediyor ve iki yerde bu dosyadan ayrılıyor: "24 / 48 / 72 saat" (burada 48s / 7g / 28g) ve "ÜÇ AYRI FİLMDE" (burada AGENTS §1 ④: iki film → sahibe sor). Uyum sahibin kararıdır.

---

## 4 · Okuma — düşüş içten mi, dıştan mı (öneri · R10 KABUL; ölçülmüş değil)

| Düşüş türü | Olası iç neden | Olası dış neden | Ayırt etme yolu |
|---|---|---|---|
| İlk 30 s'de keskin düşüş (Intro düşük) | açılış, kapak ve başlığın vaadini vermiyor · yavaş açılış | ilgisiz kitleye gösterim · yerleşik oynatıcı (`NO_LINK_EMBEDDED`) | abonelere ya da "Göz atma"ya süz. Düşüş sürüyorsa iç → `KAPAK_VE_YAYIN.md` vaadi + ANLATIM A2 |
| Ortada tek noktada keskin düşüş (Dip) | o çekimde anlatım kopuyor · ses boşluğu · görsel hata | kitle aradığını alıp çıkıyor | saniye → çekim (§2.3) → o çekimin NOTLAR TARAMA / ANLATIM / İZLEME satırları. Abone olmayan eğride de aynı yerdeyse iç |
| Kademeli eğim | ritim · uzayan sahne | kitle genişliyor (48 s → 28 g) | 48 s ve 28 g eğrisi aynı noktada karşılaştırılır. Eğim yalnız 28 g'de dikse dış |
| Sıçrama (Spike) | anlaşılmayan an geri sarılıyor ya da beğenilen an tekrar izleniyor | zaman damgalı dış paylaşım | aynı günlerde trafikte `EXT_URL` artışı varsa dış. Yoksa ANLATIM A1 (karışıklık) ile karşılaştırılır |
| Son saniyelerde düşüş | bitiş anlaşılmadı ya da "bitti" sanıldı | bitiş ekranı (→ DIS_SAYILAR §1 "Bitiş ekranı") | düşüş bitiş ekranı aralığında mı · ANLATIM 6 (ENDING) cevabı |

**Süzme nasıl yapılır:**
1. **Abone ayrımı resmîdir:** "You can compare new viewers vs returning viewers, subscribers vs non-subscribers…" (yt/9314415, gör. 07.10) · API'de `subscribedStatus`.
2. **"Göz atma"ya süzmek R10'un önerisidir.** Tutma eğrisine trafik süzgeci Studio'da uygulanabiliyor mu, doğrulanmadı; API'de yok. İlk filmde sahip bakar, NOTLAR'a yazar.
3. ⚠ API'deki `SUBSCRIBER` trafik türü abone demek değildir: "The video views were referred from feeds on the YouTube homepage or from YouTube subscription features." (api/dimensions). Studio'daki "Göz atma"ya yakındır.

**İlk 48 saat:** kitle abonelere yaslı olabilir (ham raporun iddiası; kanalda ölçülmedi). Abone payı 48 s'de ve 28 g'de
karşılaştırılarak sınanır. Doğrulanana kadar bir filmin 48s hücresi başka filmin 28g hücresiyle yan yana konmaz.

**Karşılaştırma ne zaman anlam kazanır** (öneri):
```
YAŞ     yalnız aynı yaş: 7 g ↔ 7 g, 28 g ↔ 28 g. Karar hücresi 28 g'dir.
TABAN   "karşılaştırma kendi benzer videoların" (DIS_SAYILAR §1 "CTR"): aynı süre bandı (4 · 8 · 16 dk), aynı biçim (yatay ↔ Shorts).
        Kanaldaki 225 eski video taban olabilir. 28 g+ ölçütleri Studio'da var, ama timeline'ları yok:
        düşüşleri çekime çevrilmez, yalnız CTR ve ort. % tabanı olarak kullanılır.
        Geriye dönük kimlik satırı açılmaz (00_KANAL_DENETIMI §0 ③).
SAYI    kaynaklı bir "kaç video" eşiği bulunamadı (§9). Hattın tek sayısı AGENTS §1 ④: iki film.
```

---

## 5 · Tahmin ↔ gerçek — QA da böyle sınanır

Yayın öncesinde üç tahmin vardır. Hepsi yayından önce tarihli olarak yazılmıştır:
1. **ANLATIM_TESTI:** tablo satırları A2 WOULD STOP (en çok iki) ve A1 CONFUSED → NOTLAR ANLATIM.
2. **izleyici ajanı:** 7 KOPTUĞUM ve 8 BIRAKIRDIM (metin animatiği faz 3 · kareli animatik faz 7 · kareler faz 8) → `ODA/`.
3. **IZLEME_FORMU:** A7 "Sıkıldığım an" · B6 "Nerede kafan karıştı?" · B7 "Nerede bırakmak istedin?" → NOTLAR İZLEME.

Bunlar gerçek düşüş saniyeleriyle aynı tabloda, NOTLAR İZLEYİCİ VERİSİ bölümünde, §3 satırının altında yan yana yazılır:

| Kaynak | Sürüm | Tahmin (zaman ya da an) | Çekim | Gerçek düşüş 28g | Çekim | Eşleşme |
|---|---|---|:--:|---|:--:|---|
| ANLATIM A2 · izleyici 8 · İZLEME B7 … | taslak_xx | MM:SS ya da "kare 07" | Cnn | MM:SS.s–MM:SS.s | Cnn | aynı çekim · komşu · aynı sahne · yok |
| — (tahmin yok) | — | — | — | MM:SS.s–MM:SS.s | Cnn | **KAÇIRILAN** |
| <kaynak> | taslak_xx | MM:SS | Cnn | — | — | **YANLIŞ ALARM** |

- **Ortak anahtar çekimdir, saniye değil:** taslakla final arasında kurgu değişmiş olabilir, izleyici ajanı da an verir. 16 dk'da en ince düzey sahnedir (§2.3).
- **Yalnız yer karşılaştırılır, yüzde karşılaştırılmaz.** "Ön gösterim kopmayı bulur, yüzdeyi tahmin edemez" bir hipotezdir (R10 NOT).
- **Tahmin yayından sonra yazılamaz.** Kaynak, NOTLAR ya da ODA'daki tarihli satırdır.
- **QA'nın sınaması:** her kaynak için film başına isabet (eşleşen / tahmin) ve kaçırılan sayısı tutulur. Bir kaynak iki filmde
  aynı yönde kaçırıyorsa ya da yanlış alarm veriyorsa → §8.

---

## 6 · Kapak ve başlık A/B — Test & Compare (resmî · yt/16391400 · Y3)

```
≤3 seçenek    "up to 3 different titles and thumbnails"
kazanan       "based on watch time share": CTR ile değil, izlenme süresi payıyla
görsel        her biri ≥1280×720: "lower than 720p (1280 x 720), all experiment thumbnails will be downscaled to 480p"
dokunma       "If a video's title or thumbnail is changed during the test, the test will automatically stop."
yer · süre    → DIS_SAYILAR §1 "Başlık/kapak testi" (masaüstü Studio · Shorts'ta yok)
```
**Hat bağlamı:** konsept faz 6'da tek değişkenle kurulur (`KAPAK_VE_YAYIN.md` §1); görsel ölçüsünü kapak-tasarimcisi tutar.
Test bitmeden başlık ya da kapak elle değişmez (`apexaic/YAYIN_PLANI.md` §4 tek değişken kilidi). Sonuç §3 "A/B sonucu" hücresine.

---

## 7 · Yapay zekâ bildirimi (resmî · yt/14328491 · Y4)

> "Disclosing AI content won't limit a video's audience or impact its eligibility to earn money."

- **Bildirmemenin yaptırımı:** "manual application of a label, or penalties … removal of content or suspension from the YouTube Partner Program."
- **C2PA:** dosyada C2PA metadatası varsa YouTube etiketi kendisi koyar ve bu etiket değiştirilemez. C2PA temizlenmez (`apexaic/CAPRAZ_YAYIN.md` §2).
- **Bildirimi SAHİP yapar** (`paketleme` §F9.2). Resmî cümle gereği bildirim, veri okumasında düşüş nedeni sayılmaz.
- ⚠ Sayfanın adı artık "Disclosing use of GenAI content", ayarın adı "AI use" (Y4). Ama `apexaic/POLITIKA_VE_RISK.md` §3 ve
  `SABLON/YAYIN_PAKETI.md` hâlâ "Altered or synthetic content" yazıyor. Bu, sahibe not.

---

## 8 · Kural

- ⛔ **Tek filmin verisi kural olmaz** (AGENTS §1 ④). NOTLAR'a satır olur, o kadar.
- **İki ayrı filmde aynı yön** görülürse (aynı tür düşüş aynı tür çekimde, ya da aynı tahmin kaynağı sürekli kaçırıyor),
  sahibe sorulur: "ARIZA_LISTESI'ne / BILINEN_TUZAKLAR'a girsin mi?" (`paketleme` §F10.4).
- **Dış bulgu** önce "sınanacak" diye yazılır (`apexaic/YAYIN_PLANI.md` §6.1 biçimi). Kendi verimiz iki filmde aynı yönü
  göstermeden kural olmaz.

---

## 9 · Çürütülenler — yeniden önerilmez

| İddia | Neden çürük | Kaynak |
|---|---|---|
| Kısa film için tutma ve izlenme yüzdesi aralıkları (ort. izlenme %35-45 · ilk 30 s %60-70 · Shorts'ta izlenen >%50-60) | örneklem yazılı değil (ajans analizleri); %35-45 için ham rapor kendisi "sayı ve örneklem büyüklüğü belirsizdir" diyor | R10 RED |
| Senaryo metninden tutma tahmini (R² 0,742) | ölçülen şey tutma değil, tahmin edilen bölüm izlenmesi; tek dizi (Better Call Saul); başka dizide eksi | Y9 ◐ · R10 RED |
| CTR'ın API adı `annotationClickThroughRate` | bu bir ek açıklama (annotation) ölçütüdür; API'de küçük resim gösterimi ve CTR ölçütü yok | api/metrics, gör. 07.10 |
| "En az 5-10 video, binlerce gösterim" karşılaştırma eşiği · "yüksek CTR + düşük süre = gösterim kısılır" | ikisi de kaynaksız | ham §"Tek Videonun Yetersizliği" · §"Gösterim ve CTR" |
