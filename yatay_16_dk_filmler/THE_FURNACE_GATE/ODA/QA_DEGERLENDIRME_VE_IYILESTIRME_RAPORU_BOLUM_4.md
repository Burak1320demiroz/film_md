# 📊 THE_FURNACE_GATE — QA Değerlendirme ve İyileştirme Raporu · Bölüm 4 (C73–C96)

> **Video:** `taslak_01` 4. parça · 04:00 · 24 çekim · film içinde 12:00–16:00
> **Tarih:** 18.10.2026 · **Yazan:** Fable (ana ajan; alt ajan çağrısı yok)
> **Kaynak:** `ODA/HAM_QA_RAPORU_BOLUM_4.md` (Anlatım Testi · İzleme Formu · Süreklilik · Tarama, sahibin ilettiği hâliyle)
> **Dayanak:** `AGENTS.md` §3 · `uretim_hatti/QA_OKUMA_KILAVUZU.md` (sözleşme v1.0) · `SECIM_VE_KURGU_KILAVUZU.md` · `KIMLIK_VE_REFERANS_KILAVUZU.md` · `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` · FILM.md §3-§6 · PROMPTLAR/G07-G08
> **Kayıt:** `NOTLAR.md` TARAMA · SÜREKLİLİK · ANLATIM · İZLEME · KARARLAR ("P4" satırları) · yeniden test paketi `ODA/QA_YENIDEN_TEST_BOLUM_4.md`

---

## 0 · Bu rapor neye dayanıyor

**Kaynakların geçerliliği** (QA_OKUMA §4: geçersiz kaynak atılmaz, ağırlığı düşer; ret nedeni insan doğrulamasıyla olur):

| Rapor | Durum | Neden | Ne yapıldı |
|---|:--:|---|---|
| ANLATIM | geçerli | sesli, plansız; ama yalnız 4. parça izlendi | 1-8 → çekim çekim "planlanan ↔ anlaşılan"; çekirdeğin feda edildiği C69 görülmediği için "çekirdek nerede" sorusunun bir kısmı parça kesiminden |
| İZLEME A | ? | model çıktısı biçiminde geldi | sahibin kendi izlemesi mi, sahip söyler (§6 K3) |
| İZLEME B | **dış izleyici sayılmaz** | kendini "simülasyon" diye adlandırıyor | kaydedildi, yayın onayına sayılmaz (AGENTS §1 ⑤) |
| SÜREKLİLİK | geçersiz | `>90 s` · "ne olmalı" ve kesme listesi verilmedi (SAME/NEW modelin tahmini) · Türkçe çıktı | 26 satır okundu, kesmeler film numarasına çevrildi (+72) |
| TARAMA | geçersiz | `>90 s` · "ne olmalı" verilmedi · Türkçe çıktı | 25 satır okundu |

**Zaman → çekim eşlemesi:** `timeline.json` hâlâ şablon, `~/film_medya/THE_FURNACE_GATE` boş (`medya.py durum`: ref 0/15 · kare 0/96 · ham 0).
`kurgu.py liste --zaman` koşulamadı. Eşleme **içerik çapasıyla** yapıldı (QA_OKUMA §2 adım 4):
- parça başı 12:00 = C73;
- 22 repliğin (R74–R95) duyulduğu saniye FILM §5'teki planlı saniyeyle örtüşüyor (örn. R78 3,5 s → 00:53 · R82 6,0 s → 01:56 · R83 6,0 s → 02:07);
- her 10 s penceresinin içeriği o çekimin §4 satırına uyuyor.

Medya hatta girince `kurgu.py liste --zaman` ile doğrulanır (TEST 0).

**Sınıf geçicidir.** Hiçbir kare ya da klip görülmedi. Hata türünü (S1: "videoda var mı?") insan kesinleştirir. "Doğduğu yer" de rapordaki tariften çıkarıldı: kusur çekimin ilk saniyesinden beri varsa "kare", çekim içinde beliriyorsa "hareket" yazıldı.

---

## 1 · Özet

**Tutan:**
- **Hikâyenin omurgası okundu.** Planı bilmeyen izleyici dört dakikayı tek paragrafta doğru anlattı: geri dönüş → kurtarma → ark kapıdan çıkar → bedel ödenir.
- **24 çekimin 16'sı** planlanan bilgiyi taşıdı.
- **§5'teki 22 replik** duyuldu; metin sapması yok.
- **Final duygusu geçti.** C95–C96'daki kimya, tebessüm ve fedakârlık hem izleme formunda hem anlatım testinde ayrı ayrı övüldü. Teknik olarak en temiz pencere de burası (03:40–03:59).

**Kırılan:**
1. **Üç anlatım kopuşu:** görüntü repliği desteklemiyor ya da onunla çelişiyor.
   - **Köprü (C74 · C81):** "The bridge is gone" deniyor, ama köprü iki dış planda da sağlam görünüyor.
   - **Ayrılma (C80):** tug ark'tan ayrılmak yerine yaklaşıyor gibi okunuyor.
   - **Çekirdek (C73 · C94):** başta "koyu küre" görülüyor, sonda açılıp boş çıkan beyaz bir kutu. Aynı çekirdeğe yapılan geri çağrı kurulmuyor.
2. **Tug kimliği:** 8 dış çekimde (C80 C81 C84 C85 C87 C89 C92 C96) üç-dört ayrı araç görünüyor. Bunlar küt + 4 turuncu itici · sivri + kanatlı + mavi itici · köşeli + eğik kanopi · üçgen kama + tek mavi itici.
3. **Kostüm işaretleri:**
   - rozet göğüs ↔ omuz ↔ ikisi birden: 9 kesmede ve 6 klip içinde;
   - C83'te ABD bayrağı;
   - C86'da Rhea'nın göğsünde Leon'un kuş rozeti;
   - kol bantları tek kolda.
4. **Ses:**
   - klip sesi replik penceresine kısılmamış: vakumda metal çarpması ve patlama sesi duyuluyor (C82 C84 C85);
   - model iki repliği tekrarladı (R76, R86), birini yanlış sesle verdi (R82).
5. **Vakumda ateş:** C91 ve C92'nin son vuruşunda vakumda kabaran alev ve duman var.
6. **Ölü zaman:** C74 ve C80'de 10'ar s neredeyse donuk dış plan. İki yerde "bırakırdım" dendi.

**Sayılar (geçici, insan doğrulaması öncesi):**
- Ham satırlar: anlatım 9 · süreklilik 26 · tarama 25 · izleme A'da 8 soru. Birleşince 60 bulgu.
- Sınıf dağılımı: 🅐 27 · 🅑 14 · 🅑+ 3 (biri aday) · 🅒 11 · ? 5.
- Payda, sözleşme v1.0'a göre 🅐+🅑+🅑+ = 44'tür. Yüzde yazılmadı: hiçbir bulgu insanca doğrulanmadı.

---

## 2 · Anlatım — planlanan bilgi ↔ izleyicinin anladığı

16 ✅ · 5 ⚠️ · 3 ❌ (çekim çekim tablo: `NOTLAR.md` ANLATIM, P4).

| Çekim | Planlanan | Anlaşılan | Neden | Doğduğu yer |
|:--:|---|---|---|---|
| **C74** ❌ | yükleme köprüsü geri çekilir | köprü 10 s sapasağlam, hiçbir şey olmuyor (A1 SURE · A2) | hareket görünmüyor; uzak geniş planda yavaş kayma okunmaz | hareket (kare?) |
| **C80** ❌ | tug ark'tan ayrılır | mekik port önünde donuk, **yaklaşıyor** gibi (A2) | arka iticiler ateşliyken geri gitmek okunmuyor; port ark gövdesinde değil koyu duvarda | hareket + kare |
| **C81** ❌ | köprünün altından kurtarma uçuşu | ayrı an olarak anlatılmadı; köprü hâlâ yerinde (A1) | referans paneli köprüyü sağlam gösteriyor, metin "geri çekilmiş" diyor (🅑+) | kare |
| C75 ⚠️ | Rhea karşıda kalır | "köprü gitti" der, mahsur görünür — ama C74 ile çelişir | C74'e bağlı | — |
| C77 ⚠️ | Rhea acil iskelede bekler | "bu pozisyonu tutamam" derken gevşek kablo, zorlanma yok (A3) | replik süre baskısı ("burada uzun kalamam"), imge fiziksel tutuş gösteriyor | anlatım (🅑) |
| C82 ⚠️ | güvenlik ateşinden geçer | "küçük cisim patladı", ne olduğu belirsiz (A5) | drone uzak ve küçük; atım yerine drone'un kendisi parlayıp yok oluyor | hareket |
| C90 ⚠️ | tug ark'ın ardından hızlanır | ayrı an olarak anlatılmadı | kokpit içi, kanopiden ark — okunur ama iz bırakmıyor | — (kabul) |
| C94 ⚠️ | bedel: çekirdek yok, kazanç yok | kutu açılıp boş; çekirdeğin akıbeti yalnız diyalogdan (A9) | yanlış nesne (beyaz çanta) + morph; C73'ün "küresi"yle eşleşmiyor | kare + hareket |

- **Parça kesimi uyarısı:** çekirdeğin feda edilişi (C69, 3. parça) bu izlemede yoktu. Bu yüzden "çekirdeğe ne oldu" sorusu, düzeltilmiş C94'te de tek parçalık izlemede kısmen kalır. Doğru ölçüm, 3. ve 4. parçanın birlikte izlenmesidir (TEST 4).
- **"Ark" kelimesi:** izleyici "Ark"ın dev gemi olduğunu 02:40'ta (C89) çözdü. Tam filmde ark C01'de gösterildiği için bu da büyük ölçüde parça kesiminden.

---

## 3 · Birleşik bulgu tablosu (çekim çekim)

Kaynak kısaltmaları:
- **A#** — anlatım tablosu satırı;
- **İA-n** — izleme formu A, soru n;
- **B-n** — izleme simülasyonu, soru n;
- **S#** — süreklilik bulgusu (rapordaki numara);
- **T#** — tarama bulgusu.

Prompt alıntısı gönderilen sürümden değil, **güncel** dosyadan alındı. DENEMELER boş olduğu için hangi sürümün gönderildiği bilinmiyor; QA_OKUMA §2 adım 5 bunu bekler.

| # | Çekim | Zaman (parça · film) | Bulgu | Kaynak | Sınıf | Doğduğu yer | Prompt (birebir \| YOK) | Karar |
|:--:|:--:|---|---|---|:--:|---|---|---|
| 1 | C73 | 00:01–00:08 · 12:01 | itişte uyarı lambası ve kollar biçim değiştiriyor | T1 KESİN | 🅐 | hareket | "one round red bridge-warning lamp sits dark" · "the three lowered levers and the hatch window stay in place" | yan öğe → kabul adayı (insan) |
| 2 | C73 | 00:02–00:09 · 12:02 | kaskta gösterge, sol omuzda yıldız arma | T2 OLASI · S2 | 🅑 | kare | KİMLİK TABANI "a blue-gold geometric-sun badge" (konum YOK) | örüntü P2 |
| 3 | C73 | 00:00 · 12:00 | çekirdek "koyu küre" okundu | A9 · İA-1 | ? | kare? | "the single spent core, latched, its casing heat-scored but intact and its glass centre dark" | kare ↔ ref 10 `core spent panel` (insan); C94'ün geri çağrısı buna bağlı |
| 4 | C74 | 00:10–00:19 · 12:10 | köprü 10 s sağlam ve hareketsiz | A1 SURE · A2 · S3 · İA-1 · İA-7 · B-6 | 🅐 (🅑+ adayı) | hareket (kare?) | Video "slides to the right into its foundry housing … the dark gap opening wider" · Görsel "using the exterior intact panel" + "a narrow dark vacuum gap has opened" | **yeniden üret (öncelik 2)** |
| 5 | C74 | 00:10–00:19 · 12:10 | vakum planında alçak uğultu; kesmede kabin uğultusu sürüyor | T3 OLASI · S1 LIKELY | 🅒 | — | Y1 "low steady non-diegetic pressure tone" · §6 Y6→Y1 çapraz 1 s | kabul (çapraz ≤1 s mi, insan) |
| 6 | C75 | 00:20 · 12:20 | güneş arması göğüsten sol omza, eldiven parçası beyaz | S2 · T4 KESİN | 🅑 | kare | konum YOK | P2 |
| 7 | C75 | 00:24–00:27 · 12:24 | pencere ve dış yapı yer değiştiriyor | T5 KESİN | 🅐 | hareket | "the push-in carries the camera nearer to the hatch window and the distant ivory hull framed in it" | insan; temiz 00:20–00:24 |
| 8 | C76 | 00:33–00:35 · 12:33 | sol kumanda kolu eriyor | T6 KESİN | 🅐 | hareket | "his gloved hands on the console controls" | KARE MODU (TEST 1) → doğrulanırsa yeniden üret, eller kadraj dışında |
| 9 | C76 | 00:37–00:38 · 12:37 | "I'm coming back" ikinci kez | anlatım 7 · İA-5 | 🅐 | kurgu | replik yalnız 0-5 s; 5-10 s "he draws a slow breath and his jaw tightens" | klip sesi penceresi; 85 mm'de sessiz dudak görünüyor mu (insan) |
| 10 | C76 | 00:30 · 12:30 | kuş arması sağ omuzda, göğüste plaka; turuncu bant tek kolda | S5 | 🅑 (konum) · 🅐 (bant) | kare | "orange upper-arm bands" | P2 |
| 11 | C77 | 00:40 · 12:40 | arma göğüste ve sağ omuzda aynı anda | T7 · S4 | 🅑 | kare | konum YOK | P2 |
| 12 | C77 | 00:43–00:49 · 12:43 | tether ucu beyaz başlıklı sert çubuğa dönüşüp havada duruyor | T8 KESİN | 🅐 | hareket | "a navy safety tether … floating in a loose curve" · "The tether floats taut and steady" | **yeniden üret** |
| 13 | C77 | 00:40–00:49 · 12:40 | "tutamam" derken zorlanma yok | A3 SURE · İA-4 | 🅑 | anlatım | "her right glove draws back one short length along the tether" (süre baskısı YOK) | yeniden tasarım: baskı bakışla |
| 14 | C78 | 00:50 · 12:50 | arma göğüs ortasına, sol kola bant | T9 · S5 | 🅑 | kare | konum YOK | P2 |
| 15 | C78 | 00:50 · 12:50 | kabin C76'dan farklı | S6 | 🅒 | — | "the camera facing aft from the canopy side" (ters açı) | kabul |
| 16 | C78 | 00:53–00:57 · 12:53 | yüz donuk, dudak senkronu yapay; "Ark on hold" bağlamsız | İA-4 · İA-5 | 🅑 (tercih) | anlatım | "His gaze stays on the module's cyan light" | kullan; dış izleyiciye sorulur |
| 17 | C79 | 01:06–01:08 · 13:06 | iki kol gaz koluyla birleşiyor | T10 KESİN | 🅐 | hareket | "His glove lifts away from the toggle and settles on the control stick beside it" | KARE MODU → kırp + SECIM §6 (ikinci deneme / devam) |
| 18 | C79 | 01:00 · 13:00 | arma sağ omuza; kaskta menteşe | S7 | 🅑 | kare | konum YOK | P2 |
| 19 | C79 | 01:00 · 13:00 | farklı kabin, kanopi, beyaz gövde | S8 | 🅒 | — | mekân değişimi (ark komutası → tug, §6 Y8→Y2) | kabul |
| 20 | C80 | 01:10–01:19 · 13:10 | 10 s donuk; arka iticiler ateşliyken ilerleme yok; yaklaşıyor gibi | A4 · T11 · İA-7 · B-7 | 🅐 + 🅑 | hareket | "The tug keeps drifting leftward … the gap opening to about the length of the tug's hull" · itici durumu YOK | **yeniden üret (öncelik 3)** |
| 21 | C80 | 01:10 · 13:10 | 4 turuncu itici (referans: 2) | S10 | 🅐 | kare | "two rear thrusters and four radiator fins" | P1 |
| 22 | C80 | 01:10 · 13:10 | port düz, koyu duvarda | S9 | 🅐 | kare | "the ark's small round starboard maintenance port, which sits in the pale ivory hull wall" | #20 ile |
| 23 | C81 | 01:20 · 13:20 | tug sivri, kanatlı, mavi itici | T12 · S10 · İA-2 | 🅐 | kare | "Reference 3 (tug) … using the three-quarter panel" | P1 |
| 24 | C81 | 01:23–01:29 · 13:23 | ileri itkiyle geri-aşağı kayma | T12 KESİN | 🅐 | hareket | "starts a single curved flight path toward the emergency socket" | **yeniden üret (öncelik 4)** |
| 25 | C81 | 01:20 · 13:20 | köprü sağlam, geri çekilmiş değil | A1 · İA-1 · B-6 | 🅑+ | kare | "using the bridge and socket panel" (not: "köprüyü sağlam gösterir") ↔ "in its retracted state" | 9.KOPRU `exterior retracted panel` eklenir |
| 26 | C81 | 01:20 · 13:20 | tug geride, ark ve köprü kadraja girmiş | S11 | 🅒 | — | yeni konum, kompozisyon gereği | kabul |
| 27 | C82 | 01:34–01:36 · 13:34 | drone parlayıp iz bırakmadan yok oluyor; ne olduğu belirsiz | A5 SURE · T13 | 🅐 | hareket | "one brief blue-white pulse streaks across the dark outside the canopy and passes beyond the glass" | yeniden üret (orta) |
| 28 | C82 | 01:35 · 13:35 | keskin patlama sesi | T13 · İA-6 | 🅐 | kurgu | "The only ambient sound is soft cabin ventilation and close, calm breathing" | klip sesi yalnız R80 penceresi |
| 29 | C82 | 01:34–01:36 · 13:34 | Leon tepkisiz | İA-4 | 🅑 | anlatım | "He makes one small restrained input" (bakış YOK) | yeniden üretimde gözler atımı izler |
| 30 | C82 | 01:30 · 13:30 | arma göğüste ve omuzda | S12 | 🅑 | kare | konum YOK | P2 |
| 31 | C82 | 01:30 · 13:30 | kanopiden açık uzay ve drone | S13 | 🅒 | — | "Beyond the canopy glass lies open space" | kabul |
| 32 | C83 | 01:40–01:49 · 13:40 | ABD bayrağı · kare çerçeveli arma · bant tek kolda | S14 · T14 · İA-2 | 🅑 | kare | "the only marking on the suit" YOK | **kareyi düzelt → yeniden üret** |
| 33 | C83 | 01:48–01:49 · 13:48 | yuvarlatılmış siyah çerçeve, film şeridi lekeleri | T15 · İA-3 | 🅑+ adayı | seçim | "fine 35 mm film texture" (her promptta; yalnız burada çıktı) | yeniden üretimde düşer; yoksa ölçekli kırpma |
| 34 | C84 | 01:56–01:59 · 13:56 | "Contact. Contact." kadın "sistem" sesiyle | anlatım 7 · İA-5 | 🅐 | kurgu | "a low, dry adult man's voice … softened by a light suit-radio filter … says: Contact." | R82 yedek kayıt (§5 Kayıt HUMAN) |
| 35 | C84 | 01:56 · 01:58 · 13:56 | vakumda kuru metal çarpması | T16 · İA-6 | 🅐 | kurgu | Y1 cümlesi | klip sesi kapalı; tasarım efekti (§6) |
| 36 | C84 | 01:50 · 13:50 | menteşeli kapak tug'da değil soket yakasında | T16 · S15 | 🅒 | — | "the socket's single broad hinged clamp stands open on the socket collar" (iki yakada da kelepçe: ref 3 + ref 14) | kabul |
| 37 | C84→C85 | 01:58–02:00 · 13:58 | kapak C84 sonunda yarı kapanıyor, C85 baştan kapatıyor | S16 SURE | 🅐 | hareket | "the hinged clamp still standing open on the socket collar" | YEDEK ile yeniden üret (orta) ya da kabul (§6 K5) |
| 38 | C85 | 02:00–02:09 · 14:00 | yüksek motor ve kilit sesleri | T17 · İA-6 | 🅐 | kurgu | Y1 cümlesi | R83 penceresi dışında sessiz |
| 39 | C85 | 02:07 · 14:07 | "Hard seal" otomatik sistem sanıldı | anlatım 7 | ? | — | RHEA telsiz | Rhea'nın sesi mi (insan) |
| 40 | C86 | 02:10 · 14:10 | Rhea'nın göğsünde Leon'un kuş rozeti | S17 SURE | 🅐 | kare | KİMLİK TABANI "a blue-gold geometric-sun badge" | görünürse **kareyi düzelt → yeniden üret** (duygusal merkez) |
| 41 | C86 | 02:10 · 14:10 | hava kilidi geçişi görülmeden kokpitte | A6 | 🅒 | — | FILM §4 Risk "Rhea'nın geçişi kesmede" | dış izleyiciye sorulur |
| 42 | C86 C88 C90 C93 C95 | 02:10–03:49 | koltuklar "yer değiştiriyor" | A8 SURE | 🅒 | — | F5 KOKPİT YÖNÜ: önden Leon kare sağında, arkadan solda | dış izleyiciye sorulur (okuma sinyali) |
| 43 | C87 | 02:28–02:29 · 14:28 | burun halkası kopup boşlukta kalıyor | T18 · İA-3 · A7 | 🅑+ | hareket | "its unlatched collar sliding away so that the thin gap starts to widen" | yeniden üret (orta) |
| 44 | C87 | 02:21–02:28 · 14:21 | R86 iki sese bölündü, "We're clear" tekrar | anlatım 7 | 🅐 | kurgu | "a clear, quick adult woman's voice … says: We're clear. I still have the ark link." | tek "We're clear." |
| 45 | C87 | 02:20 · 14:20 | soket kapağı yok | S18 | 🅑 | kare | soket kelepçesi YOK | yeniden üretimde |
| 46 | C88 | 02:30 · 14:30 | Rhea'nın eli altında beyaz kutu | T19 | 🅒 adayı | — | "Rhea glove already on the same wrist-link's broad hold toggle" | bilek bağlantı yuvası mı (insan) |
| 47 | C89 | 02:40 · 14:40 | tug sivri, mavi itici | S20 | 🅐 | kare | 3.KESTREL `side view panel` | P1 |
| 48 | C90 | 02:50 · 14:50 | ark motor bloğunda köşeli podlar | T20 OLASI | ? | kare | — | kabul adayı |
| 49 | C90 | 02:50 · 14:50 | halkanın yanında küçük uydu | S21 | 🅑 | kare | "başka gemi yok" kilidi YOK | kabul adayı |
| 50 | C91 | 03:07–03:09 · 15:07 | vakumda kabaran alev/duman | T21 KESİN | 🅐 (🅑+ adayı) | hareket | "the warm orange furnace glow at frame-left swells slowly behind the heavy blast ribs" | yeniden üret (son vuruşta ışık olayı yok) |
| 51 | C90→C91 | 03:00 · 15:00 | ark birden neredeyse tamamen geçmiş | S22 | 🅒 | — | "only the stern engine section … still inside the aperture" (zaman atlaması) | kabul |
| 52 | C91 | 03:08 · 15:08 | patlamada ses yok | İA-6 | 🅒 | — | vakum · §6 "dış ses yok … efektler tasarım, gövdeden ya da kaskın içinden" | tasarım efekti serbest (§6 K2) |
| 53 | C92 | 03:10 · 15:10 | ark ters yöne bakıyor | S23 SURE | 🅐 | kare | "Far ahead at frame-right the long ivory ark travels away" | **yeniden üret (öncelik 5)** |
| 54 | C92 | 03:10 · 15:10 | tug üçüncü tasarım | S23 | 🅐 | kare | 3.KESTREL `three-quarter panel` | P1 |
| 55 | C92 | 03:15–03:19 · 15:15 | yanan tünel ağzı, kabaran duman | S23 · T22 | 🅐 (🅑+ adayı) | hareket | "the orange furnace light starts to swell in one contained pulse, far from both ships" | #53 ile |
| 56 | C93 | 03:20–03:22 · 15:20 | bileklik hangi bilekte, sönük ↔ parlak | S24 · T23 | ? | kare | FILM §3: Rhea'nın bilek bağlantısı SAĞ bilek | raporlar çelişiyor → insan |
| 57 | C93 | 03:20 · 15:20 | ark uzak, motorlar sönük | S24 | ? | — | — | kabul adayı |
| 58 | C94 | 03:30–03:39 · 15:30 | beyaz çanta tipi kutu; parlayıp ikiye bölünüyor, yeni modül türüyor | T24 · İA-3 · A9 · B-6 | 🅐 | kare + hareket | "the spent portable core sits latched in its input cradle … its graphite casing heat-scored dark" · "the casing, the latch and the three levers stay rigid" | **yeniden üret (öncelik 1)** |
| 59 | C95 | 03:40 · 15:40 | bant tek kolda, omuz arması yok | S25 | 🅑 | kare | konum YOK | yakın plan; kabul adayı |
| 60 | C96 | 03:50 · 15:50 | tug kama gövdeli, tek mavi itici | T25 · S26 | 🅐 | kare | "the small wedge-shaped tug" + 3.KESTREL | P1 kararına bağlı (§6 K4) |

---

## 4 · Film düzeyi örüntüler

### P1 · Tug kimliği — 8 dış çekimde üç-dört araç

- **Ne görüldü:**
  - C80: küt gövde, 4 turuncu itici, kanatçık var.
  - C81 ve C89: sivri, kanatlı, mavi itici.
  - C84, C85 ve C87: küt.
  - C92: köşeli gövde, eğik kanopi.
  - C96: üçgen kama, tek mavi itici.
  - Ref 3'ün tarifi: "geniş kısa fildişi kama · koyu grafit alt gövde · burunda tek dar turuncu bant · geniş füme-mavi kanopi · **yan yana iki gömme yuvarlak arka itici** · **dört kısa rijit radyatör kanatçığı**".
- **Neden (geçici):**
  - itici sayısı ve kanatçıklar yalnız C80 ve C84 metninde yazıyor;
  - itici rengi hiçbir promptta yok (🅑);
  - panel her çekimde farklı: `side view` · `three-quarter`.
- **Düzeltme:**
  1. Sahip, hangi çekimdeki tug'ın `ref/3.KESTREL_v1.png` ile aynı olduğunu söyler (§6 K4). O çekimin karesi kare-referansı olur.
  2. Yeniden üretilen her tug karesi aynı sayfadan, aynı tarif cümlesiyle üretilir: "two flush round rear thrusters and four short rigid radiator fins". İtici rengi bir kez seçilip her promptta yazılır.
  3. Geri giden tug'da arka iticiler sönük olur, burunda kısa soluk "puf"lar görünür (UZAY_FIZIGI §2 örnek cümlesi: `Two brief pale puffs from the forward thrusters, gone almost as soon as they appear.`).
- **Kural ④:** araç kimliği kayması kayıtlı ikinci filmdir: THE_PLANET_THIEF C05–C08'de mekik kanatlı kamadan mermi silindirine dönüşmüştü (`yatay_4_dk_filmler/THE_PLANET_THIEF/ODA/QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU.md` §3.1). `BILINEN_TUZAKLAR`'da araç kaydı yok. Sahibe soru: §6 K6.

### P2 · Kostüm işaretleri — rozet konumu, bayrak, bant

- **Ne görüldü:**
  - rozet göğüs ortası ↔ omuz ↔ ikisi birden: 9 kesmede (S2 S4 S5 S7 S12 S14 S17 S19 S25) ve 6 klip içinde (T2 T4 T7 T9 T14 T19), iki karakterde;
  - C83'te ABD bayrağı;
  - C86'da Rhea'da Leon'un kuş rozeti;
  - bantlar tek kolda: C76, C83, C95.
  - 2. parçada da aynı aile görüldü (NOTLAR SÜREKLİLİK P2: 2.RHEA / 1.LEON arma satırları).
- **Neden:** FILM §3 KİMLİK TABANI rozetin türünü yazıyor ("a blue-gold hawk badge"), ama konumunu ("sol göğüste", ref 1-2) yazmıyor. "The only marking on the suit" kilidi de yok (🅑). Promptlar 14-15.10'da yazıldı; `KIMLIK_VE_REFERANS_KILAVUZU` 16.10'da geldi. Bugün `film_dogrula` aynı boşluğu DERS Y1 uyarısıyla 56 çekimde işaretliyor: "işaret var, tarafı yok — sayı + taraf + konum + 'the only marking'". Bu uyarı F5 kapandıktan sonra eklendi, o yüzden cevapsız kaldı.
- **Düzeltme (mevcut kılavuz, yeni kural değil):** yeniden üretilecek çekimlerde KİMLİK TABANI'ndan sonra tek ek cümle. KIMLIK §5 biçimi şöyle:
  `The blue-gold hawk badge sits on the left chest and is the only marking on the suit.`
  `The blue-gold geometric-sun badge sits on the left chest above the core-carry harness and is the only marking on the suit.`
  KİMLİK TABANI cümlesinin kendisi birebir kalır. Bayrak bulunan C83 karesi için KIMLIK §6'daki düzenleme yolu kullanılır: `Edit the supplied frame. Remove only the flag …`. Karar: §6 K1.
- Kılavuzda zaten kayıtlı (KIMLIK §1: dört filmde bayrak ve arma). Kural ④ sorusu gerekmez.

### P3 · Klip sesi replik penceresine kısılmamış

- C82 (patlama), C84 ve C85 (metal çarpma, motor, kilit) — prompt üçünde de yalnız ortam istedi (🅐).
- FILM §6 bunu zaten çözüyor: "Y1 dış kliplerde klip_sesi AÇILMAZ; replik varsa klibin sesi yalnız replik penceresinde (±0,5 s, solma 0,1)".
- SECIM §3: "Vakuma aykırı ya da istenmeyen ses → kurguda değiştir; görüntü yeniden üretilmez." → **yeniden üretim gerekmez.**

### P4 · Model sesi replik kusurları — 22'de 4

| Replik | Sorun | Karar |
|---|---|---|
| R76 | sonradan tekrarlandı | pencereyle kısılır |
| R82 | yanlış ses (kadın) + tekrar | yedek kayıt |
| R83 | ses kimliği belirsiz | insan doğrulaması |
| R86 | iki sese bölündü + tekrar | tek "We're clear" kalır |

Aynı aile 2. parçada da var: R28, R49, R50. Hepsi kurguda çözülür. Aynı film içinde olduğu için kural ④ sorusu doğmaz.

### P5 · Vakumda ateş ve duman

- C91 ve C92'nin son vuruşu. İki prompt da "glow … swells" / "starts to swell in one contained pulse" diyor; aynı ifade iki çekimde aynı kusuru verdi → 🅑+ adayı.
- 2. parçada C44'te de aynı aile (NOTLAR TARAMA P2).
- `UZAY_FIZIGI §2` zaten kayıtlı ("vakumda patlama ateş topu yapmaz → kısa ışık parlaması").
- **Düzeltme:** yeniden üretimde son vuruşta ışık olayı yazılmaz (kamera kilitli, gemi süzülür). Purge gerekiyorsa "one brief pale flash on the inner edges of the ribs, gone at once" biçiminde yazılır.

### P6 · Donuk dış plan

- C74 ve C80'de 10'ar s dış plan neredeyse hareketsiz; iki ayrı yerde "bırakırdım" dendi.
- **Kısaltma yapılmaz.** 10 s sözleşmesi (SÖZLEŞME, sahip 08.10) kısaltmayı yasaklar; SECIM §6 da "yavaşlatma, döngü, donmuş kare uzatma yok" der.
- Çözüm, 10 s'yi taşıyan görünür hareket: daha yakın ölçek, hareketin ilk 6 s'de bitmesi, boşluğun kadrajın ortasında açılması. İzleme formunun "3-4 s'ye indir" önerisi: §6 K1.

---

## 5 · Eylem planı

### 5.1 Kurguda hemen — yeniden üretim yok

Klip sesi yalnız replik penceresinde. Zamanlar parça içi; kurgu.py'ye girerken klip içi saniyeye çevrilir. Kalan süre o mekânın yatağıdır (FILM §6 Y1/Y2/Y5/Y6/Y8/Y9; mekân değişiminde çapraz 1 s + J 1 s).

| Çekim | Pencere | Not |
|:--:|---|---|
| C73 | 00:01.5–00:05.5 | R74 |
| C75 | 00:20.5–00:22.5 | R75 |
| C76 | 00:30.5–00:34.5 | R76; **00:36.5–00:38.5 tekrarı dışarıda** |
| C77 | 00:39.5–00:44.5 | R77 |
| C78 | 00:52.5–00:56.5 | R78 |
| C79 | 00:59.5–01:02.5 | R79 |
| C82 | 01:30.5–01:33.5 | R80; **01:35 patlaması dışarıda** |
| C83 | 01:41.5–01:43.5 | R81 |
| C84 | — | klip sesi kapalı; **R82 yedek kayıttan** 01:56.0'da, Leon sesi, telsiz filtresi |
| C85 | 02:06.5–02:08.5 | R83; 02:04–02:06 kilit sesi dışarıda |
| C86 | 02:10.5–02:15.5 | R84 R85 |
| C87 | 02:20.5–02:22.5 + 02:25.5–02:28.5 | ilk "We're clear." ve "I still have the Ark link."; ikinci "We're clear." dışarıda |
| C88 | 02:29.5–02:34.5 | R87 R88 |
| C90 | 02:49.5–02:52.5 | R89 |
| C93 | 03:21.5–03:24.5 | R90 |
| C94 | 03:32.5–03:36.5 | R91 (VO) |
| C95 | 03:40.5–03:46.5 | R92 R93 |
| C96 | 03:51.5–03:56.5 | R94 R95 |

**Tasarım efektleri** (FILM §6: "efektler tasarım, gövdeden ya da kaskın içinden"). İzleme formunun önerisi plana uyuyor:
- **01:56 · C84 temas:** boğuk, alçak geçirgen bir gövde vuruşu. Kuru metal çarpması değil; tug'ın içinden duyulan.
- **02:06 · C85 kelepçe:** aynı biçimde.
- **03:07–03:10 · purge:** gövdeden gelen alçak bir sarsıntı ya da müziğin altında kısa bir bas kabarması. Hangisi olacağı tercih (§6 K2). Görüntüde ateş topu kalmaz (5.2).

**Ara çözüm (C83 yeniden üretilene kadar):** 01:47.5–01:50 arasında kenar çerçevesi görünmeyene kadar ölçekli kırpma.

### 5.2 Yeniden üretim — öncelik sırası

Her çekim için 2 deneme (AGENTS §4). Aynı sebeple iki deneme bozulursa yaklaşım değişir. Yeniden tasarımı goruntu-yonetmeni yazar (F7); aşağıdakiler yalnız yöndür.

| Öncelik | Çekim | Neden | Yön |
|:--:|:--:|---|---|
| 1 | **C94** | finalin bedel anı; yanlış nesne + morph | kare: 10.CEKIRDEK `core spent panel` + 12.KONTROL_ODASI `levers down panel`. Çekirdek C73'teki **aynı nesne**: dikdörtgen, grafit, yanık, camı karanlık. Video yalnız yavaş itiş, hiçbir şey ışımaz. Konum okunsun diye kare biraz geniş başlayabilir (boş oda, üç kol aşağıda) |
| 1b | C73 | çekirdek "küre" okunduysa C94'ün geri çağrısı kurulmaz | insan doğrulaması: kare ↔ ref 10. Yanlışsa kareyi düzelt → yeniden üret. Kamera itişi arka plan nesnelerini oynatıyor (#1): kilitli kamera düşünülebilir |
| 2 | **C74** | "köprü gitti" görünmüyor; 10 s donuk | (a) daha yakın ölçek: orta bölüm ve ark tarafı platform kadrajı doldurur, kayma 0-6 s'de biter, boşluk kadraj ortasında açılır; (b) YEDEK (G07 C74 notu): kare `exterior retracted panel` ile geniş boşluğu gösterir, kamera kilitli. Anlam garanti, ama durağanlık kalır |
| 3 | **C80** | ayrılma "yaklaşma" okunuyor; donuk; yanlış itici ve port | port ark'ın fildişi gövdesinde (6.ARK `stern panel`); arka iticiler sönük, burunda iki kısa soluk puf (UZAY_FIZIGI §2); aralık 0-7 s'de tug boyu kadar açılır |
| 4 | **C81** | köprü sağlam (🅑+); farklı tug; ters itki | 9.KOPRU `exterior retracted panel` dördüncü referans (ya da 5.FOUNDRY yerine köprü için); tug P1'e göre; itici ileri yönde ateşlenir |
| 5 | **C92** | ark ters yöne bakıyor + üçüncü tug + vakumda duman | ark sağda, burnu sağa; tug P1; son vuruşta purge yerine kısa soluk parlama ya da hiç ışık olayı (P5) |
| 6 | C77 | tether morph + replik ↔ imge çelişkisi | kadraj: eldiven korkulukta, tether kemerden çapaya gergin, elde değil. Süre baskısı bakışla verilir: kaburgaların ardında fırın ışığı atar, o dönüp boş sokete bakar |
| 7 | C83 | ABD bayrağı + kenar çerçevesi | kareyi düzelt (KIMLIK §6 düzenleme) + P2 ek cümlesi → yeniden üret |
| 8 | C86 | Rhea'da Leon'un rozeti (duygusal merkez) | insan: iki kişilik genişte okunuyor mu → okunuyorsa kareyi düzelt + yeniden üret |
| 9 | C87 | burun halkası kopuyor (🅑+) | "the tug, its collar fixed to its bow, draws straight back"; soket kelepçesi açık ve görünür |
| 10 | C91 | vakumda alev, son 3 s | son vuruşta ışık olayı yok; temiz 03:00–03:06 + SECIM §6 (devam üretimi) de olur |
| 11 | C76 | kol erimesi (KARE MODU doğrularsa) + sessiz dudak | kadraj: yüz, kask, kanopi; eller kadraj dışında |
| 12 | C84 | kelepçe yarı kapanıyor (C85 baştan) | YEDEK (G07 C84 notu): halkalar temas hâlinde, kelepçe açık, kamera kilitli + lambalar + telsiz |
| 13 | C82 | drone ve atım okunmuyor | drone okunur ölçekte, kırmızı şerit görünür; atım drone'dan çıkar, drone yerinde kalır; Leon'un gözü atımı izler |
| 14 | C89 · C96 | tug kimliği | P1 kararından sonra; C96 ref'le aynıysa C96 kalır |
| 15 | C79 | son 3 s'de kol birleşmesi | SECIM §6: ikinci deneme ya da 01:06 karesinden devam |

**Toplam:** 13-16 çekim × 2 deneme ≈ 26-32 video, artı 4-6 kare düzenlemesi. Kesin sayı insan doğrulamasından sonra.

### 5.3 Kullanılır (kurgu düzeltmesiyle)

C75 · C78 · C85 · C88 · C90 · C93 · C95. C95 ve C96 parçanın en güçlü penceresi.
Kabul adayları (insan bakar):
- #1 · C73 lamba;
- #48 · C90 podlar;
- #49 · C90 uydu;
- #57 · C93 ark;
- #59 · C95 bant.

---

## 6 · Sahibin kararları

| # | Soru | Fable önerisi |
|:--:|---|---|
| K1 | İzleme formu C74 ve C80'i "3-4 s'ye indir" diyor; 10 s sözleşmesi buna izin vermiyor | 10 s kalsın, hareketle çözülsün (5.2 öncelik 2-3). Kısaltmayı yalnız sen açabilirsin |
| K2 | Purge anında (03:07) ses | gövdeden gelen kısa alçak sarsıntı; müziğe bas kabarması eklenmesin, çünkü finalde müzik açılıyor. İkisi de plana uygun |
| K3 | İzleme formu A senin kendi izlemen mi? B bir simülasyon | A seninse olduğu gibi kalır. Yayın onayı için hikâyeyi bilmeyen 2-3 gerçek kişi gerekir (TEST 6) |
| K4 | Hangi tug `ref/3.KESTREL_v1.png` ile aynı: C80 · C81 · C84 · C92 · C96? | o çekim kare-referansı olur, kalanlar ona göre üretilir |
| K5 | C84'teki yarı kapanan kelepçe | YEDEK ile yeniden üret (ucuz, tek deneme yeterli olabilir); istersen kabul |
| K6 | Kural ④: araç kimliği kayması iki filmde görüldü (PLANET_THIEF C05–C08 · FURNACE P4). `BILINEN_TUZAKLAR`'a ya da `ARIZA_LISTESI`'ne girsin mi? | evet, KİMLİK kaydının araç karşılığı olarak (referans sayfası + itici/kanatçık sayısı her promptta). Karar senin |
| K1b | P2 ek cümlesi ("… on the left chest … the only marking on the suit") yalnız yeniden üretilecek çekimlere mi, yoksa kalan bütün çekimlere mi? | yalnız yeniden üretilecekler; KİMLİK TABANI birebir kalır |

---

## 7 · Testler

Yapıştırmaya hazır test paketi: `ODA/QA_YENIDEN_TEST_BOLUM_4.md`.

| Test | Ne | Ne zaman |
|:--:|---|---|
| 0 | medyayı hatta al (`/medya-denetle`), timeline'ı kur, bu raporun eşlemesini `kurgu.py liste --zaman` ile doğrula | şimdi |
| 1 | KARE MODU, 8 pencere: C73 · C76 (×2) · C77 · C79 · C83 · C87 · C94 | şimdi (mevcut taslakla) |
| 2 | TARAMA, ≤90 s × 3 parça, "ne olmalı" bloğu dolu, çıktı İngilizce | yeniden üretimden sonra |
| 3 | SÜREKLİLİK, aynı 3 parça, SAME/NEW kesme listesiyle | yeniden üretimden sonra |
| 4 | ANLATIM, 3. ve 4. parça birlikte (08:00–16:00), yeni sohbet, nötr dosya adı | yeniden üretimden sonra |
| 5 | kimlik kontak sayfası: tug × 8 · Rhea × 8 · Leon × 7 kare + ref 1 · 2 · 3 → devamlilik (kare modu, 1 çağrı) | şimdi |
| 6 | İZLEME B: hikâyeyi bilmeyen 2-3 kişi, sesli, baştan sona | final öncesi |
| 7 | mekanik: `kurgu.py kontrol` · `kurgu.py yukseklik` (−14 LUFS · ≤ −1 dBTP) · `kareler.py dikis` (SAME kesmeleri C80→C81 · C84→C85 · C91→C92) | her yeni taslakta |

Sahip TEST 0-1'i doğrulayınca (✅ var / ❌ yok) güven kalibrasyonu (QA_OKUMA §3) bu parçanın satırlarıyla başlar.
