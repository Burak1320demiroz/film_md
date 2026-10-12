# 📒 THE_MAYDAY_SEA — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|
| <GG.AA> | C01 | d1 | Frames to Video | p1 | ✅ kullanılabilir 01.2–04.6 | |
| <GG.AA> | C01 | d2 | Frames to Video | p1 | ❌ el tokaya eriyor 03.1 → hareket | |

```
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

## RED (üretim reddi)

| Tarih | Çekim | Mesajın BİREBİR metni | İlerleyip sonda mı düştü | Değişen şey | Sonuç |
|---|:--:|---|:--:|---|:--:|

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

| Tarih | Video / kare modu | Zaman | Çekim (`kurgu.py liste`) | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması |
|---|---|---|:--:|---|---|:--:|:--:|

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|

## İZLEME (insan · `IZLEME_FORMU.md`)

| Tarih | Kim | Sürüm | Cevaplar |
|---|---|---|---|

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 12.10.2026 | Film sahibin hazır planından kurulur; plan `ODA/SAHIP_PLANI.md`'de birebir, FILM.md §1-§7 oradan yerleşti; faz 1-4 ajan turu açılmadı (DURUM AŞILAN KAPILAR). Fable'ın türettikleri: referans numaraları (1.MARA · 2.KAPSUL · 3.KOKPIT · 4.OKYANUS · 5.ISTASYON · 6.KORIDOR · 7.GOZLEM_ODASI · 8.AKSESUARLAR · 9.CANLI_SU), grup bölümü (G01 C01-08 · G02 C09-16 · G03 C17-24), replik saniye/süre tahmini, AI repliği MACHINE varsayımı, FIZIK_IDDIASI yok, §6 yatak (Y1-Y5) ve geçiş tablosu (karışım 3 · karartma 1), §3 ORTAK GÖRÜNÜM / MEKÂN IŞIĞI / ORTAM SESİ cümleleri. | Sahip talimatı "bunu bozmadan aynı şekilde hazırla" (THE_PLANET_THIEF yolu). Plan araçları (GPT Image · Gemini Omni 10 s) hat araçlarından (Flow) farklı; promptlar F5'te hat biçimine çevrilir, içerik planın kendisidir. |
| 12.10.2026 | **Plandan tek bilinçli sapma (sahibin talimatı):** bütün replikler §5 Kaynak = model sesi (…), video promptlarında birebir; Omni konuşmayı videoda üretir; Flow'da ses AÇIK; timeline'da replik taşıyan parçalar `klip_sesi: true`. Planın "Mara'nın K02 cümlesini bir kez kaydet, K12/K23'te aynı dosyayı kullan" ve "K02 erkek çağrısını K07'de yeniden kullan" yöntemi **kurguda yedek**: Omni aynı sesi başka klipte garanti etmez. F7'de SMOKE P18 ölçer; tutmazsa C02 klibinin sesi `ses` parçası olarak C07/C12/C23'e yerleşir ve o parçalarda klip_sesi kapanır. | Sahip: "dialogları video promptuna ekle, Omni modeli video promptuya eklesin." Ses taklidi hikâyenin dönüm noktası (K12/K23); risk sahibe açık yazıldı (DURUM SAHİP CEVAPLARI). |
| 12.10.2026 | C02'de Mara'nın repliği "ağız kadrajda" sayılır (vizör şeffaf, yüz yakın): tavan 5 s, dudak senkronu riski; C08 · C13 · C18 aynı. C12 ve C23'te OCEAN sesi alıcıdan gelir, Mara'nın ağzı kapalı yazılır (C23'te Mara kadrajda). C06'da AI konuşurken Mara kadrajda, ağzı kapalı. | Model sesi AÇIK olduğu için kadrajdaki kişinin konuşup konuşmadığı promptta açık olmalı (teknik-danisman maddesi 12.10.2026). |
| 12.10.2026 | Plan promptlarının hat kurallarıyla çatışan kalıpları F5 çevirisinde kalkar: olumsuz blok ("No readable text…", "No cuts, new characters…"), zincir dili ("first frame", "uploaded scene still"), araç/süre etiketi ("10 seconds", "16:9", "Animate the uploaded…"), "All spoken lines will be added in the edit" (bu filmde tersi), çekim atfı ("established earlier", "the same … as before"). Yerine: `Reference <No> (<rol>)` anahtarı, 10 s vuruş planı (ilk vuruş hareketli), pozitif tarif, ortak görünüm cümlesi, (video) mekân ortam ses cümlesi + model sesi replikleri. Planın "Audio:" satırları §6'ya katman olarak taşındı; efektler kurguda. | film_dogrula M (meta · atıf · zincir dili · konuşma) ve PROMPT_HATA_ATLASI (olumsuz blok ters etki); GECIS_VE_SES_SUREKLILIGI §1. |
| 12.10.2026 | F5 birleştirme geçişi (§2c, tur açılmadı; ÖLÜMCÜL 0/2 eleştirmen, CİDDİ 9+8, KÜÇÜK 6+7). Fable kararları K1-K19 (ODA/F5_goruntu-yonetmeni_2_G0x.md §K): K1 kimlik tabanı = C02 cümlesi + modüler ekler (bant · eldiven · rozet · bot) aynı kelimelerle; K2 kokpit yanları: ekran düzeni korunur, beden-göreli taraf düzeltilir (C18 sağ omuz · C20 sağ eldiven · C23 sol eldiven), yara cümlesi C23'e; K3 sayfa 2 "her panelde halka" cümlesi durum bazlı, yeni paneller `side view after separation panel` · `lever pulled, receiver on panel`, C22 burun cümlesi silinir; K4 G02'de her referansa tek panel adı; K5 sayfa 7 kask lacivert kenar, sayfa 4 mekik kısa kanat; K6 replik vuruşun SON cümlesi (G01 C02 C06 C07 C08); K7 ses tarifleri sabit (Mara `warm and low` + tek sıfat · AI `calm adult man's voice, even and unhurried, over the comms` · CALLER `tired man's voice, softened by a light radio filter` · OCEAN = Mara + radyo filtresi); K8 gök cümlesi birebir, C24 lens 18 mm; K9 iskelet ≤3 tekrar, C24 0-3·3-8·8-10; K10 C04 son vuruş durmaz; K11 C05 temas kesmede; K12 C19/C21 kelepçe soket ucu / su orta bant, "tighten" → parlaklaşma; K13 C24 halka kapalı kelepçede; K14 C08 görsel bakış aşağıda, ses kaynağı alıcı statiği; K15 C22 sabit hız, itici biçimini korur; K16 KISMEN: sayfa 1 yaş + ten kalır (plan; PLANET_THIEF kararı), eldiven paneli tek eldiven `glove panel`; K17 "lever" ≤2; K18 C18 nefes çelişkisi; K19 G02 EKLE/ışık/"Render" biçimi. T8 klip sesi penceresi → FILM §6 (dış kliplerde `ses` parçası). T6(2) → SMOKE P18 ek karşılaştırma. | Plan olayları korunur; değişenler ölçülmüş tuzaklar (T01 çift temas, T11 yön, T05/T09 durum paneli, T13 vakum sesi, A10 replik sonrası betimleme, A05 çelişki) ve çok panelli sayfa kuralı (10.10.2026). |
| 12.10.2026 | **F5 KAPANDI** (Fable). Denetçi 1 KAPANAMAZ (Ö7 · Ö4 · F5.8) → üçü de kapatıldı (DURUM, FILM §4 C18/C19, G03 C18/C23 taban, devamlilik 1b) → denetçi 2 KAPANABİLİR, ❌ yok. §4 Durum 24/24 ✍️. F6 açılmadı: plan üç kapak adayı A/B/C KAPAK_VE_YAYIN §1'de, final F9'da gerçek kareden. FAZ 7 sahipte: Flow ses AÇIK, SMOKE P14 + P18 önce, 9 referans sayfası, öncelikli C01/C10/C14/C21. 7 plan sapması sahip onayı bekliyor (DURUM SAHİP CEVAPLARI). 7 çağrı. | Plan hazır olduğu için eleştiri yalnız biçim çevirisinin (F5) olduğu yere kondu; bütçe 7/50. Denetçi ikinci kez çağrıldı (PLANET_THIEF'te çağrılmamıştı): bütçe bol, kanıt izi tam olsun. |
| 12.10.2026 | Geçiş taslağı (§6): karartma yalnız C05→C06 (plan "metal sesi, kısa sessizlik", içeri giriş kesmede); karışım C13→C14 (iç → su altı açılma) ve C23→C24 (sessizlikten okyanusa kapanış); kalan 20 kesme kesme, yataklar mekân değişiminde 1-1,5 s çapraz. F8'de kurgucu `kareler.py dikis` ile kesinleştirir. | GECIS_VE_SES_SUREKLILIGI §3 oranları (karışım ≤ ¼, karartma ≤ 2); planın geçiş notları (K05 sessizlik, K17→K18 kesme). |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 12.10.2026 | F5/1 | goruntu-yonetmeni (G01) | sonnet | FILM §3 §4 §5 + SAHIP_PLANI R01-R09 + K01-K08 (biçim çevirisi görevi) | PROMPTLAR/G01.md | ✅ 9 referans sayfası (Mara 5 panel: önden · arkadan · portre · ¾ portre · eldivenler; kapsül 5, halkalı/halkasız; kokpit 5, kol dik/çekilmiş, anahtar açık/kapalı; okyanus 4, alttan dahil; istasyon 3; koridor 4; gözlem 3; aksesuarlar 3 nesne; canlı su 5; KAYNAK zinciri 3←2, 5←4, 7←6) + 8 çekim + iş emri 25 satır; replikler videoda `says:` biçiminde, alıcıdan gelen seste ağız kapalı; ORTAK GÖRÜNÜM ve ortam sesi birebir · sapma: karakter adı promptta yok ("the woman"); C05←C04 bağımlılığı kaldırıldı; kapsül sayfasına "ayrılma sonrası" paneli (plan söylemiyor, C21-C22 için gerekli) · risk: C02 iki replik (ağız erken oynayabilir); C05 temas kadrajda (ek donanım riski); plan yön tutarsızlığı (kokpitte kol solda/alıcı sağda/yüz görünür; C17 su sağda ↔ koridorun ters görünüşü) G03'e; videolar P11/P14/P18 ölçümüne kadar iş emrinde bekler |
| 12.10.2026 | F5/1 | goruntu-yonetmeni (G02) | sonnet | FILM §3 §4 §5 + SAHIP_PLANI K09-K16 (biçim çevirisi görevi) | PROMPTLAR/G02.md | ✅ 8 çekim, hepsi Frames to Video; ORTAK GÖRÜNÜM 16 blokta, MEKÂN IŞIĞI 8 görselde, ORTAM SESİ 8 videoda birebir; 5 replik `says:` biçiminde (ilgili vuruşun son cümlesi); iş emri 8 kare + 8 video, C10/C14 öncelikli · sapma: plan kalıpları çıktı, olumsuzlar pozitife; C11 mekiğe kısa kanat (kapsüle benzemesin); C16←C11 kaynak kare bağımlılığı kaldırıldı (metinle taşındı) · risk: panel adları G01'e bağlı (C13 ¾ profil ve C14 alt görünüş paneli sayfalarda yok); kimlik ve gök cümleleri dosya başında, G01/G03 aynı kelimelerle yazmalı; C12 aynı ses riski (P18) |
| 12.10.2026 | F5/1 | goruntu-yonetmeni (G03) | sonnet | FILM §3 §4 §5 + SAHIP_PLANI K17-K24 (biçim çevirisi görevi) | PROMPTLAR/G03.md | ✅ 8 çekim, iş emri 8 kare + 8 video, C21 öncelikli; 5 replik `says:` biçiminde, R17'de "mouth stays closed" iki kez; panel adları, kimlik cümlesi ve ses kalıpları G01'le hizalı; "the woman" · sapma: kaynak kare bağımlılıkları kaldırıldı (C19←C05 · C21←C19 · C22←C21; FILM §3 notu ve §4 Risk eskidi → Fable güncelleyecek); C17 AYNALANDI (kamera hava kilidine bakar → su kanalı solda, dolap sağda; plan "right floor channel"); C23 eldiven anahtarın ÜSTÜNDE başlar (plan "yanında"); C22 burun uçuş yönüne (sağa); C24 R18 ≈8,5 s'ye uzanır · risk: kokpit yerleşimi (kol solda · alıcı sağda · yüz görünür) C18/C23'te F7'de gözle; sağ elmacık yarası bu açılarda yazılmadı |
| 12.10.2026 | F5/1 | Fable (mekanik) | — | PROMPTLAR/G01-G03 (⛔ önceki sürüm ODA/F5_goruntu-yonetmeni_1_G0x.md'ye kopyalandı) | — | `film_dogrula --bolum cekim sahneleme prompt` ✅ (24/24 prompt, referans anahtarı, 10 s planı, model sesi replikleri birebir) |
| 12.10.2026 | F5/1 | devamlilik (grup içi + gruplar arası tek çağrı) | sonnet | G01-G03 + FILM §3 §4 §5 | ODA/F5_devamlilik_1.md | ÖLÜMCÜL 0 · CİDDİ 9 (kimlik cümlesi 4 sürüm · kokpit sol/sağ · kapsül sayfası halka çelişkisi · G02 panel adları yok · C16 yanlış panel · G01 replik son cümle değil · C08 görsel sonucu gösteriyor · iskelet 3 kalıp · C05 kamera cümlesi) · KÜÇÜK 6 (gök cümlesi/lens · C04 duruyor · C24 halka · kask kenarı/mekik kanadı · ses tarifleri · G02 biçimi) · KORU: ORTAK GÖRÜNÜM 48/48, ORTAM SESİ 24/24, R01-R18 birebir, referans rolleri sabit, C17 aynalama tutuyor · KAPANABİLİR |
| 12.10.2026 | F5/1 | teknik-danisman | sonnet | G01-G03 risk sütunu dolu çekimler + 9 sayfa | ODA/F5_teknik-danisman_1.md | ÖLÜMCÜL 0 · CİDDİ 8 (C05 iki temas · G02 panel anahtarları · kokpit yanları · durum panelleri C21/C22/C23 · G01 replik sırası · ses kimliği 6+8 klip · C19/C21 kelepçe-su bandı · vakumda klip sesi 7 dış klip) · KÜÇÜK 7 (C04 duruyor · C22 burun arkadan · sayfa 1 kimlik yığını + iki eldiven · "lever" ×7 · C18 nefes çelişkisi · C24 replik 8,5 s · G02 EKLE) · KORU C20/C23 temas ilk karede, C10 yerçekimi işareti · KAPANABİLİR |
| 12.10.2026 | F5/1b | goruntu-yonetmeni G01 (birleştirme geçişi, SendMessage devamı — çağrı sayılmaz) | sonnet | F5_devamlilik_1 + F5_teknik-danisman_1 + Fable kararları K1-K19 | PROMPTLAR/G01.md (güncel) · ODA/F5_goruntu-yonetmeni_2_G01.md (§K) | ✅ KABUL 14 · KISMEN 3 (D10 gök cümlesi C05'e girmedi, yakın planda uzay yok · T8 klip sesi penceresi iş emrine F8 notu · T11 yaş+ten kaldı, eldiven tek) · RED 0 · kapsam dışı 13; yeni paneller `glove panel` · `side view after separation panel` · `lever pulled, receiver on panel`; sayfa 2 halka durumu panel bazlı; sayfa 4 mekik kanat, sayfa 7 kask kenarı; iskelet tekrarı ≤2 (C06=C07); C06/C08'de rozet yok (göğüs kadraj dışı, yazar kararı); C04'e gök cümlesi |
| 12.10.2026 | F5/1b | goruntu-yonetmeni G02 (birleştirme geçişi, SendMessage devamı — sayılmaz) | sonnet | aynı girdiler | PROMPTLAR/G02.md (güncel) · ODA/F5_goruntu-yonetmeni_2_G02.md (§K) | ✅ KABUL 10 · KISMEN 1 (T8: C15'te itici/metal yok, klip sesi penceresi Not'a) · RED 1 (T2b: C13'e "white gloves" yok — eller kadraj dışı, K1 modüler kural; Fable KABUL eder) · panel adları G01 ile birebir, EKLE G01 biçimi, "Render…" kalktı; C13 kimlik tabanı + ¾ portre paneli; C16 yalnız wreck-cord; 8 çekimde 8 ayrı iskelet; yazar kendi düzeltmesi: C14 kamera `underside panel` geometrisine (aşağıdan yukarı), C10 ref 9 `wall-climb panel`, C15 ref cümlesi · risk (kapandı): sayfa 7 kask kenarı ve sayfa 4 mekik kanadı G01 son sürümünde var |
| 12.10.2026 | F5/1b | goruntu-yonetmeni G03 (birleştirme geçişi, SendMessage devamı — sayılmaz) | sonnet | aynı girdiler | PROMPTLAR/G03.md (güncel) · ODA/F5_goruntu-yonetmeni_2_G03.md (§K) | ✅ KABUL 15 · KISMEN 1 (D8: C24 0-3·3-8·8-10, C17 0-2·2-5·5-10, C18 0-4·4-6·6-10; C19 0-3·3-7·7-10 kaldı, R15 oturuyor) · RED 0 · KORU 3 (C17 aynalı · C23 eldiven anahtar üstünde · C20 el ilk karede) · kokpit yanları K2, bantlar K12, C22 K15, "lever" ≤2, nefes K18; Fable: FILM §5 R18 saniye 4.0 → 3.0 (yapıldı), §4 C20/C23 (yapıldı); G01 panel adları çapraz kontrol: `side view after separation panel` · `lever pulled, receiver on panel` · `glove panel` G01'de var |
| 12.10.2026 | F5 kapı | denetci | opus | KABUL Ö + F5 · ODA F5 dosyaları · G01-G03 (+ ODA _1_ sürümleri) · FILM §3-§6 · DURUM · NOTLAR | ODA/F5_denetci_1.md | KAPANAMAZ · mekanik ❌ Ö7 (DURUM SIRADAKI açılış adımında kalmış) · yargı ❌ Ö4 (G03 C18/C23 kimlik tabanı bölünmüş; FILM §4 C18 "aceleci nefes" ve C19 "sıkılaşır" KABUL sonrası eski) · F5.8 (devamlilik "ilk vuruş hareketli" ve "aynı-mekân ölçek/açı" denetimine kanıt yok) · ✅ 14 madde (F5.1 M, F5.4 M, F5.9 M dahil) · gözlem: G03 C19 notu eski C05 boşluğunu anıyor; G02'nin kendi değişiklikleri eleştirmen görmedi; teknik NOTLAR/DURUM okudu (bağımsızlık) |
| 12.10.2026 | F5 kapı sonrası | Fable (düzeltme) | — | denetçi Ö7 · Ö4(2) | DURUM SIRADAKI · FILM §4 C18 (kontrollü nefes) · C19 (taban toplanma + parlaklaşma, boyut sabit) | ✅ yapıldı; Ö4(1) G03'e, F5.8 devamlilik'e SendMessage devamıyla (sayılmaz) |
| 12.10.2026 | F5/1c | goruntu-yonetmeni G03 (denetçi Ö4 düzeltmesi, SendMessage devamı — sayılmaz) | sonnet | F5_denetci_1 Ö4(1) | PROMPTLAR/G03.md · ODA/F5_goruntu-yonetmeni_2_G03.md (§K +2) | ✅ C18/C23 kimlik tabanı tek parça, ekler (rozet · bant · eldiven) tabandan sonra ayrı cümle; C19 notu K11'e göre (C05 halka oturmuş, kelepçe açık ↔ C19 kelepçe kapalı + su); KABUL 17 |
| 12.10.2026 | F5/1b | devamlilik (F5.8 ek geçişi, SendMessage devamı — sayılmaz) | sonnet | G01-G03 yeni sürüm; yalnız (1) ilk vuruş hareketli (2) aynı-mekân ölçek/açı (3) G02/G03 değişiklikleri | ODA/F5_devamlilik_1b.md | ÖLÜMCÜL 0 · CİDDİ 0 · KÜÇÜK 2: B16 C15 ilk vuruş yalnız ışık (→ G02 yazarına, Fable KABUL) · B17 C14 kamera vakumda, yatak "su altı" (→ FILM §6 Y5 "heard from outside the water", tasarım; prompt cümlesi değişmez) · (1) 23/24 hareketli, tablo · (2) BULGU YOK, 5 çift lens/açı tablosu · (3) yeni ÖLÜMCÜL yok; C14 geometri `underside panel` ile uyumlu, C10 `wall-climb panel` ve C15 ref cümlesi tutuyor, G03 C18/C23 kimlik tabanı birebir, kokpit yönü tutarlı · KAPSAM DIŞI: C24 `living network panel` yanaşık kapsül taşıyor ↔ C24 kapsül yok → F7 kare denetiminde bakılacak (Fable notu) |
| 12.10.2026 | F5/1c | goruntu-yonetmeni G02 (B16 düzeltmesi, SendMessage devamı — sayılmaz) | sonnet | F5_devamlilik_1b B16 | PROMPTLAR/G02.md C15 · ODA/F5_goruntu-yonetmeni_2_G02.md (§K +1) | ✅ C15 0-3 s'e yüzey dalgacıkları (`the surface ripples drift slowly rightward …`), kamera sabit, ortam/görünüm cümleleri aynı; §K KABUL 11 · KISMEN 1 · RED 1 |
| 12.10.2026 | F5 kapı 2 | denetci | opus | F5_denetci_1 + düzeltmeler · ODA F5 dosyaları (1b dahil) · G01-G03 · FILM · DURUM · NOTLAR | ODA/F5_denetci_2.md | **KAPANABİLİR** · mekanik ❌ yok · yargı ❌ yok · önceki 4 Ö4 kalıntısı + F5.8 kapandı (kanıtlı) · 16/16 madde ✅ · gözlem: DURUM SIRADAKI/FAZ GÜNLÜĞÜ kapanışta güncellenecek (yapıldı); G03 C24 notu "R18 4.0→3.0 Fable'ın işi" eski (yapıldı, not kod bloğu dışı, dokunulmadı); C15 B16 değişikliğine eleştirmen bakmadı (KÜÇÜK, tek vuruş) |
