# 🎚️ KURGU, SES VE MÜZİK KILAVUZU — montaj planı tutar, müzik kesmeyi bilir

> **Ne için:** montajda final ve doruk düştü (D62 · D72), on klip sessizce eksildi ama süre "yaklaşık tuttu" (D100), jenerik ve başlık kartı altı filmde zincire
> geri girdi (D70). Bu kılavuz `SECIM_VE_KURGU` ve `besteci`'nin üstüne yalnız eklenenleri verir: montaj kapısının iki kanıtlı maddesi, tempo hizası, müziğin
> az kullanılan araçları, vakum sesi ve ihraç.
> **Kim okur:** kurgucu (F8) · besteci (F4 · F8) · ses-tasarimcisi (F4) · Fable · sahip (montaj, ihraç).
> **Kaynak:** eski 3 kılavuz (~1.130 satır) → `ARASTIRMA/23_SUZME_KURGU_SES_MUZIK_20261021.md` (29 madde). Sahip kararı 21.10.2026.
> Tamamlayıcı (burada tekrarlanmaz): `SECIM_VE_KURGU_KILAVUZU` (iş sırası, beş karar, 10 s doldurma, taslak kapısı) · `GECIS_VE_SES_SUREKLILIGI` (yatak, J/L,
> geçiş türü) · `REPLIK_VE_KLIP_SESI_KILAVUZU` · `besteci` kuralları · `HIKAYE_YAPISI_KILAVUZU` §4 (doruk ve final kurgudan düşmez).
> **Tarih:** 21.10.2026.

**Kural türü (AGENTS §1b):** **KANITLI** satırlar en az iki kayıtlı vakaya dayanır; uygulanır. **HİPOTEZ** satırlar ölçülmedi; uygulanır ya da gerekçe yazılır.
Her çekim 10 s'dir; eski kılavuzların kırpma bütçesi, ASL eğrisi ve hız ayarı bu yüzden yoktur.

---

## 1 · Montaj kapısına eklenenler

- **Plan ↔ kurgu eşlemesi çekim çekim — KANITLI** (D100 LAST SHIFT: on klip düştü, süre tuttu · D81 · D118: bozulan blok her vakada final bloğuydu).
  Süre ve çekim sayısı tek başına aldatır. Her plan çekiminin karşısına kurgudaki zaman kodu yazılır (`kurgu.py liste --zaman`); **son üç çekimin sırası
  elle** doğrulanır. Hat dışı montajda bu eşleme `medya.py bol` ile geri kurulur.
- **Başlık kartı, jenerik ve kapak görseli zincire girmez — KANITLI** (D70 · altı film: UNBROKEN CITY · BANDED DEEP · LAST SHIFT …). Başlık yalnız bir çekimin
  üstünde yazı katmanıdır (`ILK_30_SANIYE` §2); siyah kart, jenerik kartı ve kapak dosyası timeline'da video parçası olmaz.
- Çehov halkasının kurulum çekimi kurguda var mı (ödemesi olup kurulumu olmayan halka) — HİPOTEZ.
- Ardışık iki çekimde ölçek, palet ve ses dokusunun **üçü birden** aynıysa dikkat sıfırlanmaz; en az biri değişir — HİPOTEZ (ölçek kolu `GECIS` §1-5'te kural).
- Sert kesme (ses ve görüntü aynı karede) yalnız bilinçli şok için, filmde en çok üç kez ve planda yazılı; gerisi J/L — HİPOTEZ.
- Bütün filmin üstünde tek renk düzeltmesi ve tek gren katmanı; klip başına ayrı gren yok (iki kesme arasında gren farkı hissedilir) — HİPOTEZ.

---

## 2 · Müzik — besteciye eklenenler (HİPOTEZ)

Okuma cümlesi, müziksiz an, fade-out yok, çözülme sayısı, alt basın oktav eşi, mickey-mousing yasağı ve miks `besteci`'de. Eklenenler:

- **Tempo kesmelere hizalanır.** Çekim 10 s olduğu için tempo hesapla seçilebilir: **BPM = 240 × ölçü ÷ 10** → 48 (2 ölçü) · 72 (3) · 96 (4) · 120 (5) · 144 (6).
  Bu tempolardan biriyle her kesme bir ölçü başına düşer; vurgu yine olaya oturur (besteci kural 4). Eski iki filmde tempo hizasızdı (130 · 58 BPM); 120 ya da 144,
  48 ya da 72 aynı duyguyu korur. Müzik promptuna tempo sayıyla yazılır.
- **Müzik vuruşuna kesme** yalnız açılışta ve doruktan hemen önce; geneli harekette kesilir. Her yerde vuruşa kesmek kurguyu mekanikleştirir.
- **Anempatik müzik:** olay büyürken müziğin **değişmemesi**; evrenin insanı umursamadığını söyler (silinen kayıt, kırılan tarla aynı sakin nabızla).
  Neşeli müzik değil, tepkisiz müzik.
- **Karşıt ruh hali:** keşif anında müziğin soğuk kalması bedelin ipucudur; genel bakış anında müziğin yükselmemesi huşuyu zaferden ayırır.
- **Söz verip tutmama:** yükselen bir cümle doruğa varmadan kesilir (`the line stops mid-phrase and does not continue`), daha sonra tamamlanır.
- Sonsuz yükseliş (Shepard tonu) istenmez: model güvenilir üretmez, tona uymaz.

---

## 3 · Ses — vakum ve replik altı (HİPOTEZ)

- Model sesi filmlerinde klip sesi replik aralığında açıktır (sahip kararı 21.10.2026). Vakum sahnesinde o aralıktaki klip sesinin **tizi kesilir** (alçak geçiren
  filtre ~300-400 Hz) ve eşik kapısı yüksek tutulur: çarpma ve patlama tizi gider, kalan boğuk alt uç gövdeden iletilen sese oturur. Ne duyulur, ne duyulmaz:
  `REPLIK_VE_KLIP_SESI` §4.
- Replik altında yatak kısılır (duck); anlık katman sayısı üç-dördü geçiyorsa önce yatak kısılır. Doruk ve temas bölgesi teslimden önce kulakla dinlenir.

---

## 4 · İhraç ve yayın sonrası ses kontrolü (HİPOTEZ, dış kaynak, çatışmasız)

| Parametre | Değer | Neden |
|---|---|---|
| Çözünürlük | 2560×1440 ya da 3840×2160 (kaynak 1080p olsa da büyütülerek) | platform 1440p ve üstünü daha iyi kodekle sıkıştırır; ince gren ve doku korunur |
| Kare hızı | kaynağa sadık, aradeğerleme yok | — |
| Kodek | MP4 · H.264 ya da H.265 · yüksek bit hızı (yatayda 45-60 Mbps) | yeniden sıkıştırmaya tampon |
| Renk | BT.709 | soluklaşma ve renk kayması |
| Ses | AAC · 48 kHz · stereo 384 kbps · −14 LUFS · ≤ −1 dBTP (`kurgu.py yukseklik`) | — |

Yayından sonra videoda **Stats for nerds → Content loudness** −1 ile 0 dB arasında olmalı; artıysa miks yüksek, çok eksiyse düşük. Ses düşük teslim edilmez:
platform yüksek sesi kısar, düşüğü yükseltmez.

---

## 5 · Kim, ne zaman

| Faz | Kim | Bu kılavuzdan |
|---|---|---|
| F4 | besteci · ses-tasarimcisi | §2 tempo hizası, anempatik ve karşıt ruh hali kararları · §3 vakumda klip sesi |
| F8 | kurgucu | §1 plan ↔ kurgu eşlemesi, son üç çekimin sırası, başlık kartı zincirde mi · §3 |
| F8 | besteci | §2 kesin promptta tempo kesmelere hizalı mı |
| F9 | Fable · sahip | §4 ihraç ve yayın sonrası ses kontrolü |

---

> **Ölçüm:** bu kılavuzla kurgulanan ilk filmde — montajda düşen ya da sırası bozulan çekim var mı (§1) · başlık ya da jenerik kartı zincire girdi mi (§1) · seçilen
> tempo kesmelere oturdu mu (§2). **Bu dosya ne zaman değişir:** yalnız yeni kayıtlı vakayla ya da sahip kararıyla.
