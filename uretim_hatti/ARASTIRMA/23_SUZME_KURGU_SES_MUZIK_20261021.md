# 23 · SÜZME — KURGU, SES, MÜZİK (eski kılavuzlardan hatta)

> **Ne:** Eski hattın kurgu, ihraç ve müzik kılavuzlarının madde madde süzmesi; yöntem `18`-`22` ile aynı (sahip kararı 21.10.2026).
> Çıktı: `uretim_hatti/KURGU_SES_VE_MUZIK_KILAVUZU.md`.
> **Okunan (3 dosya · ~1.130 satır + devralınan):** `KURGU_RITMI_VE_IHRAC` (324) · `KURGU_VE_TESLIM` (230) · `GOOGLE_FLOW_MUSIC_URETIM` (580; §7-§17) ·
> devralınan: `PROMPT_HATA_ONLEME` §4 vakum sesi reçetesi (`20`).
> **Karşılaştırılan hat:** `SECIM_VE_KURGU_KILAVUZU` (iş sırası, beş karar, 10 s doldurma, mekanik kontroller, taslak kapısı) · `GECIS_VE_SES_SUREKLILIGI`
> (yatak, J/L, geçiş türü) · `REPLIK_VE_KLIP_SESI` (klip sesi, vakum, telsiz) · `besteci` (okuma cümlesi, müziksiz an, bitiş, alt bas, miks, prompt biçimi) ·
> `kurgu.py` (kontrol · taslak · yukseklik) · `HIKAYE_YAPISI` §4 (doruk ve final kurgudan düşmez, KANITLI).
> **Kanıt:** eski D70 D72 D81 D83 D100 D118 · `KURGU_VE_TESLIM` §1 (başlık kartı / kapak zincire karıştı, 6 vaka).

Etiketler `18`'deki gibi.

---

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| **KURGU** | | | | | |
| 1 | Mekân başına tek kesintisiz ortam yatağı; mutlak dijital sıfır yok | RITIM §3① · TESLIM §4 | HATTA VAR | `GECIS` §2 · `SECIM` §5 · `REPLIK` §4 (D83) | — |
| 2 | J-cut / L-cut; kesmede ses köprüsü | RITIM §3②③ | HATTA VAR | `GECIS` §2 "J/L zorunlu" | — |
| 3 | Sert kesme (ses ve görüntü aynı karede) yalnız bilinçli şok için, filmde en çok üç, planda yazılı | RITIM §3④ | HİPOTEZ | — | kılavuz §1 |
| 4 | Doruk, seçim, bedel ve final kurgudan düşmez | TESLIM §1 ④⑦ | HATTA VAR | `HIKAYE_YAPISI` §4 (KANITLI, D62 D72) | — |
| 5 | **Süre tek başına aldatır: plan ↔ kurgu eşlemesi çekim çekim yapılır; son üç çekimin sırası elle doğrulanır** | TESLIM §1 ②⑧⑨ | **KANITLI** | D100 LAST SHIFT (10 klip düştü, süre "yaklaşık tuttu") · D81 · D118 (bozulan blok her vakada final bloğu) | kılavuz §1 |
| 6 | **Başlık kartı, jenerik ve kapak görseli çekim zincirine karışmaz; başlık yalnız yazı katmanı** | TESLIM §1 ③ | **KANITLI** | D70 (jenerik kartı geri geldi) · 6 vaka (UNBROKEN CITY · BANDED DEEP · LAST SHIFT …) · INVERSION planlanmamış jenerik kartı | kılavuz §1 |
| 7 | Kurulumu olmayan ödeme: Çehov halkasının kurulum çekimi kurguda var mı | TESLIM §1 ⑩ | HİPOTEZ | `HIKAYE_YAPISI` §2 kurulum-ödeme (HİPOTEZ) | kılavuz §1 |
| 8 | Örüntü kırıcı: ardışık iki çekimde ölçek + palet + ses dokusu üçü birden aynıysa dikkat sıfırlanmaz | RITIM §2 | HİPOTEZ | ölçek/açı kolu HATTA VAR (`GECIS` §1-5) | kılavuz §1 |
| 9 | Müzik vuruşuna kesme yalnız açılışta ve doruk öncesi son saniyelerde; geneli harekette kesilir | RITIM §4 | HİPOTEZ | — | kılavuz §2 |
| 10 | Tek renk düzeltmesi ve tek gren katmanı bütün filmin üstünde; klip başına ayrı gren yok | TESLIM §3 | HİPOTEZ | `GECIS` §1 ortak görünüm cümlesinin kurgu karşılığı | kılavuz §1 |
| 11 | ASL eğrisi, kırpma bütçesi, doruk öncesi 0,5 s'lik rampa kesmeleri | RITIM §1 §5 · TESLIM §2 | **RED** | her çekim 10 s sözleşmesi | — |
| 12 | Hız ince ayarı %2-4 | TESLIM §3 | **RED** | `SECIM` §6 yavaşlatma yok | — |
| **SES** | | | | | |
| 13 | Vakumda klip sesinin tizi kesilir (alçak geçiren filtre ~300-400 Hz), kalan boğuk alt uç gövdeden iletilen sese oturur | HATA_ONLEME §4 | HİPOTEZ | model sesi filmlerinde klip sesi replik aralığında açık (21.10.2026); `REPLIK` §4 vakum tablosu HATTA VAR | kılavuz §3 |
| 14 | Replik altında yatak duck edilir; anlık katman 3-4'ü geçerse önce yatak kısılır | TESLIM §4 | HATTA VAR (kısmen) | `besteci` replik altında müzik −6…−9 dB | kılavuz §3 |
| 15 | Ses düşük teslim edilmez (platform yükseği kısar, düşüğü yükseltmez); −14 LUFS · −1 dBTP | RITIM §6.2 | HATTA VAR | `kurgu.py yukseklik` | — |
| 16 | Yayından sonra "Stats for nerds" → Content loudness −1…0 dB arasında mı | RITIM §6.2 | HİPOTEZ | dış (platform davranışı) | kılavuz §4 |
| **İHRAÇ** | | | | | |
| 17 | 1440p ya da 4K yüklemek platformu daha iyi kodeğe zorlar; 48 kHz · AAC · BT.709 · kaynağa sadık kare hızı · yüksek bit hızı | RITIM §6.1 | HİPOTEZ | dış (çatışmasız) | kılavuz §4 |
| **MÜZİK** | | | | | |
| 18 | Okuma cümlesi · müziksiz an (doruktan 1-2 s önce susar, tek notayla döner) · fade-out yok · en çok 1-2 çözülme · alt basın oktav eşi · mickey-mousing yok · melodi alıntılanmaz | MUSIC §7-§13 §15 | HATTA VAR | `besteci` kural 1-8 | — |
| 19 | **Tempo kesmelere hizalanır:** 10 s çekimde 48 · 72 · 96 · 120 · 144 BPM her kesmeyi bir ölçü başına düşürür (BPM = 240 × ölçü ÷ 10) | MUSIC §14 | HİPOTEZ | matematik; eski iki filmde hizasız tempo (130 · 58 BPM); besteci "vuruş olaya oturur" ile çelişmez: tempo kesmeye, vurgu olaya | kılavuz §2 |
| 20 | Müzik tek parça üretilir, çekim çekim değil | MUSIC §14① | HATTA VAR | `besteci` F8 tek prompt + KESME NOKTALARI | — |
| 21 | Vuruş tutmuyorsa müzik değil görüntü kaydırılır | MUSIC §14③ | HATTA VAR | `besteci` kural 6 | — |
| 22 | Anempatik müzik: olay büyürken müziğin **değişmemesi** (evrenin kayıtsızlığı) | MUSIC §9 | HİPOTEZ | Chion (dış) | kılavuz §2 |
| 23 | Karşıt ruh hali: keşif anında müziğin soğuk kalması; genel bakış anında yükselmemesi | MUSIC §7.1 | HİPOTEZ | Copland (dış) | kılavuz §2 |
| 24 | Söz verip tutmama: yükselen cümle doruğa varmadan kesilir (`the line stops mid-phrase`), sonra tamamlanır | MUSIC §11② | HİPOTEZ | Huron (dış) | kılavuz §2 |
| 25 | "Müzik duyulmaz olmalı" ilkesi bu kanalda geçersiz: müzik anlatının ikinci sesi | MUSIC §8 | **RED** (eski gerekçe) | replik artık varsayılan (06.10.2026) ve model sesi; müzik replik altında kısılır (`besteci` 7) | — |
| 26 | Shepard tonu (sonsuz yükseliş) | MUSIC §11③ | **RED** | modelin güvenilir üretmediği yazılı; tona uymaz | — |
| 27 | Müzik "kapanmaz", çünkü "seri held frame ile biter" | MUSIC §7 | **RED** (gerekçe) | H02 film biter (`19` D2); "fade-out yok, çözülmemiş akor" `besteci`'de kendi gerekçesiyle durur | — |
| 28 | Lisans, telif, kök ayrıştırma (stem) | MUSIC §3 §5 | HATTA VAR | `FLOW_GERCEKLERI` §6 (bilinmiyor) · `REPLIK` §4 (Demucs PROB) | — |
| 29 | Film müziği künyesi şablonu | MUSIC §17 | **RED** (biçim) | `FILM.md` §7 + MÜZİK PROMPTU bloğu | — |

---

## Sayım

| Etiket | Madde |
|---|:--:|
| HATTA VAR (tam ya da kısmen) | 9 (1 2 4 14 15 18 20 21 28) |
| **KANITLI (yeni)** | **2** (5 · 6) |
| HİPOTEZ | 12 (3 7 8 9 10 13 16 17 19 22 23 24) |
| RED | 6 (11 12 25 26 27 29) |
| **Toplam** | **29** |

**Sonuç:** en küçük ve en çakışık küme. Hat `SECIM_VE_KURGU`, `GECIS`, `REPLIK` ve `besteci` ile bu konuyu zaten taşıyor; eski kılavuzların kırpma ve
ASL bölümleri 10 s sözleşmesiyle düştü. Yeni giren öz: 2 kanıtlı (plan ↔ kurgu eşlemesi · başlık kartı zincire girmez) + bir avuç hipotez
(tempo hizası, anempatik müzik, ihraç sayıları) → kısa bir kılavuz.

**Ölçüm planı:** kılavuzla kurgulanan ilk filmde — montajda düşen ya da sırası bozulan çekim var mı (5) · başlık ya da jenerik kartı zincire girdi mi (6) ·
seçilen tempo kesmelere oturdu mu (19).
