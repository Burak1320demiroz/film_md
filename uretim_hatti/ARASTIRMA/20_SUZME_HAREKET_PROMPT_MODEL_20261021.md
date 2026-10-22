# 20 · SÜZME — HAREKET, PROMPT, MODEL (eski kılavuzlardan hatta)

> **Ne:** Eski hattın prompt/hareket/model kılavuzlarının madde madde süzmesi; yöntem `18` ve `19` ile aynı (sahip kararı 21.10.2026).
> Çıktı: `uretim_hatti/HAREKET_VE_EFOR_KILAVUZU.md`.
> **Okunan (11 dosya · ~3.850 satır):** `PROMPT_HATA_ONLEME` (585; §2 ortam cümleleri küme 4'e) · `MIKRO_AKSIYON_VE_HALUSINASYON` (181) ·
> `FIZIKSEL_EFOR_VE_YERCEKIMI` (243) · `TEK_CEKIM_VE_GIZLI_GECIS` (480; §5-§6) · `SAHNE_ZINCIRI_VE_SINIR` (444; §1) · `COK_KLIPLI_SAHNE` (403; §3) ·
> `OMNI_1_1_FLASH_I2V` (422) · `VEO_3_1_FAST_DIYALOG` (228) · `IMAGE_VIDEO_PROMPT_TEMPLATES` (437) · `SAHNE_DEVAMLILIK` (386) · `KESINTISIZ_VIDEO` (37) —
> son beşi başlık + çekirdek okundu. `AI_FILMLERDE_10_SANIYELIK_KLIP_VE_RITIM` bugün uyarlandı, ayrıca süzülmedi.
> **Karşılaştırılan hat (en kalabalık küme):** `PROMPT_HATA_ATLASI` (A01-A14) · `GOSTERIM_COZUMLERI` · `GPT_IMAGE_OMNI_KILAVUZU` · `UZAY_FIZIGI_GORUNTU` ·
> `KIMLIK_VE_REFERANS` · `BILINEN_TUZAKLAR` · `goruntu-yonetmeni` (görsel/video kuralları, 8 soru) · `film_dogrula` DERS uyarıları.
> **Kanıt:** eski `PROMPT_HATA_ONLEME` §3b ölçümü (34 film, el kadrajda 617 sahne) · `03_PROMPT_HATA_SINIFLARI` (31 film) · DERSLER D175 D200 D206 ·
> GOZLEM_DEFTERI ADAY-95 · ADAY-98 · `ARASTIRMA/16` Y10.

Etiketler `18`'deki gibi.

---

## A · TEMAS

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| A1 | Temas anı gösterilmez: öncesi → kesme → sonrası; kurulu temas başlangıç karesinde | HATA §3b③ · MIKRO §3 · COK §3.6 | HATTA VAR | `GOSTERIM` ilke 1-2 · atlas A03 | — |
| A2 | **Temas ya ilk karede kurulu ya klibin ilk 2 saniyesinde** | HATA §3b① | **KANITLI** | 34 film: temas bulgusu 0-2 s %5,9 · 2-4 s %19,4 · 4-6 s %15,2 | kılavuz §1 |
| A3 | **Temas cümlesi yazmak kaynaşmayı azaltmıyor, artırdığı yönde** | HATA §1a · §3b | **KANITLI** | el kadrajda 617 sahne: cümle VAR %11,8 ↔ YOK %5,6 (RR 2,10, gözlemsel) · atlas A03 "önlemez" ile aynı yön, daha güçlü | kılavuz §1 |
| A4 | Durum cümlesi: `she is already gripping` (kurulu) ↔ `she grips` (uzanmayla açılır) | COK §3.4 | HİPOTEZ | A2 ölçümüyle aynı yön, kendisi sınanmadı | kılavuz §1 |
| A5 | **Nesne-nesne geçişi** (kayış metalden, halat abajurdan geçer) ayrı sınıf | HATA §3b④ | **KANITLI** | 81 geçiş bulgusunun 26'sı el karışmayan (DRY_ANCHOR · COUNTED_TURN · LEANING_ROOM · STILL_SWARM · LOOK_UP) · atlas A04'ü genişletir | kılavuz §1 |
| A6 | Pozitif ara katman: iki cismin arasına adlandırılmış, zıt renkli parça (halka, kılıf) | HATA §3b② | HİPOTEZ | ölçülmedi | kılavuz §1 |
| A7 | Alet tek rijit parça; parmakların alet üzerindeki hareketi tarif edilmez | MIKRO §3③ | HİPOTEZ | — | kılavuz §2 |
| A8 | İki yönlü temas cümlesi ("object-to-object … clear boundary") | HATA §3b④ | **RED** | A3 ölçümü: negatif temas cümlesi korumuyor; olumsuz blok hatta yazılmaz (atlas A14) | — |

## B · EYLEM SEÇİMİ

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| B1 | **Mikro → makro:** parmak ucu işi gövdenin yaptığı eyleme büyütülür (toka → iki elle kilit kolu · vida → levye · klavye → avuçla panel) | MIKRO §1 | **KANITLI** | el-nesne kaynaşması: atlas A03 9 film · `GOSTERIM` el-nesne satırı · STOLEN_SKY kalın eldivenle tuşlama · SLOW_RAIN toka | kılavuz §2 |
| B2 | **Yürüme platosu:** model zor işi yürümeye çevirir; zor iş çekiminde yürüme fiili yazılmaz, alt gövde zemine kilitli | MIKRO §2 | **KANITLI** | SLOW_RAIN S17-S24 (planda kesme, kazıma; ekranda yürüme) · ADAY-95 (TIMELINE kapıyı anlattı, beden boşta) · H03 yürüme dolgusu 24/52 | kılavuz §2 |
| B3 | Plato kırıcı duruşlar (omuzla yüklenme · levyeye asılma · diz çöküp tutunma) | MIKRO §2.2 | HİPOTEZ | — | kılavuz §2 |
| B4 | Makro nesne bedene göre boylanır (`a lever as long as her forearm`) | MIKRO §1 | HİPOTEZ | nesne-göreli ölçü (D138, eski) | kılavuz §2 |

## C · EFOR

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| C1 | Sabitlik sözcüğü eforu siler · zarf göstermez · efor kadraja sığar | — | HATTA VAR | atlas A01 (6 film) · A02 · `GOSTERIM` ağır iş satırı · ARIZA T02 | — |
| C2 | Efor dört parça: DESTEK (zemin, çerçeve) · GÖVDE (ağırlık yönü) · 2-3 aynı yöne İŞARET · DURAKSAMA (durur, gerilim kalır) | EFOR §1.2 · HATA §5b | HİPOTEZ | D206 (7 film) sorunu doğruluyor; çözüm biçimi A/B'siz | kılavuz §3 |
| C3 | Sonuç sayısı yazılmaz (`the lever moves 4 cm`) — pürüzsüz yörünge, ağırlıksız beden | HATA §5b · EFOR §1.1 | HİPOTEZ | TUR 22 mekanizması | kılavuz §3 |
| C4 | **Ağır çekim tuzağı:** `slowly` · `gradually` · `in slow motion` efor cümlesinde bütün sahneyi yavaşlatır | EFOR §1.6 | **KANITLI** | film_dogrula DERS Y10 "slow birikimi" (ARASTIRMA/16) · TUR 22 · EFOR §1.6 | kılavuz §3 |
| C5 | Direnç nesnede: `seized · jammed · bound by frost` ↔ zayıf `opens · slides · easily` | EFOR §1.4 | HİPOTEZ | — | kılavuz §3 |
| C6 | Asimetrik yük tutmaz (bir kol çeker, öteki gevşek → iki kol senkronlanır) | HATA §5b | HİPOTEZ | simetri önyargısı (rapor) | kılavuz §3 |
| C7 | Giysi sertliği yük: `working against the glove's own stiffness`; çevik parmak işi yok | EFOR §1.5 | HİPOTEZ | — | kılavuz §3 |
| C8 | Saydamlık tuzağı: `tendons through the glove` çıplak ön kol çizdirdi; efor giysi yüzeyinde (`sleeves pull tight`) | EFOR §1.5 | VAKA | D175 THE_UPWARD_FALL | kılavuz §3 |
| C9 | Efor anında vizörde nefes buğusu | EFOR §1.5 | **RED** | vizör buğusu 04.09.2026 sahip kararıyla reddedildi (`KARAKTER_VE_DUYGU` §4.2) | — |
| C10 | Ödenen bedel sonraki çekime taşınır | EFOR §1.7 | HATTA VAR | `KARAKTER_VE_DIYALOG` §3.1 (D207, KANITLI) | — |

## D · YERÇEKİMİ VE FİZİK

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| D1 | İki rejim aynı kadrajda: ayıran işaret görünür | HATA §2b | HATTA VAR | BILINEN_TUZAKLAR §B 7 · ARIZA T08 | — |
| D2 | İki rejimin ayrımı **mekanik sebebe** bağlanır (`locks each boot to the grating … while the loose tools drift`) | HATA §2b | **KANITLI** | LOOK_UP · GREEN_CEILING · PAYLOAD · LEANING_ROOM (2-3 🔴 her biri) | kılavuz §4 |
| D3 | Düşük g'de `falls fast · free fall · plummets · crashes down` 1 g çağırır; düşüşün şekli ve süresi yazılır | EFOR §2.1-§2.2 | VAKA | SLOW_RAIN (0,49 ↔ 4,27 m/s²) | kılavuz §4 |
| D4 | Yerçekimi g değeri + ad + insan ölçüsünde karşılaştırma | EFOR §2.2 · HATA §1b | HİPOTEZ (rakam kolu RED) | `UZAY_FIZIGI` §1 rakam yazılmaz · BILINEN_TUZAKLAR §B 7 sayının faydası gösterilemedi → yalnız insan ölçüsünde karşılaştırma | kılavuz §4 |
| D5 | Çarpışma üç evre (yaklaşma · temas · iz) ve iz ikincil nesne | EFOR §2.3 | HİPOTEZ | — | kılavuz §4 |
| D6 | Serbest parçacığa yön ver (`the frost settles back within a second`) | EFOR §2.4 | **RED** | atlas A12 (2 film): toz davranışı yazılınca model çizdi; toz kaldıran eylem taşıyıcı an olmaz | — |
| D7 | **Novumun taşıyıcı olgusu her promptta sayıyla kilitli** (`each panel drifts about one panel-width every four seconds`) | HATA §5 | **KANITLI** | STILL_SWARM 2/14 → 6 bulgu · RESONANT_STRAND 0/14 → 4 · STANDING_WIRE · UPWARD_FALL · HARD_DOCK: "filmin ana malzemesi kilitsiz" 5 film | kılavuz §4 |

## E · PROMPT DİLİ VE SIZINTI

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| E1 | Jeton sızıntısı (büyük harfli kısa etiket, sahne kodu) | HATA §6 | HATTA VAR | BILINEN_TUZAKLAR §C · film_dogrula M | — |
| E2 | **`tripod` kelimesi kadraja tripod çizdirir** → `a locked-off camera` | MIKRO §4.2 · HATA §6 | **KANITLI** | SLOW_RAIN S14 (96/96 promptta `tripod`) · STOLEN_SKY PART1 00:39 (94/192) — iki film; "tripod" 440 kez geçip çoğu filmde çıkmadı, değişiklik bedava | kılavuz §5 |
| E3 | Zaman bağlacı yok: `Next scene · After that · Following shot` dekoru yeniden kurar; `Suddenly` sarsıntı/parlama ekler | COK §3.4 | HİPOTEZ | rapor iddiası | kılavuz §5 |
| E4 | Filigran prompt değil araç işidir | MIKRO §4.1 | HATTA VAR | ARIZA T17 · BILINEN_TUZAKLAR §B 8 | — |
| E5 | Anakronik eşya yasak listesiyle değil pozitif envanterle (`the only equipment in frame is …`) | MIKRO §4.3 | HİPOTEZ | olumsuz cümle tutmuyor (atlas A14) ile aynı yön | kılavuz §5 |
| E6 | Kişi sayısı rakamla (`Exactly 2 human characters`), `no extra characters` tarif değildir | HATA §1a | HATTA VAR (kısmen) | goruntu-yonetmeni sayılabilir öğe rakamla · vaka KRONOS | — |
| E7 | Sabit nesnenin konumu prop cümlesinde (kızağın **yeri**, yalnız varlığı değil) | COK §3.5 | HİPOTEZ | vaka: SLOW_RAIN kızak S17 yerde · S20 sırtta · S22 yerde | kılavuz §5 |
| E8 | Sekiz cümlelik negatif çekirdek her promptta · `PHYSICS:` / `AUDIO:` satırları zorunlu | HATA §1 | **RED** | olumsuz blok hatta yazılmaz (atlas A14); ses tarifi model sesi kuralına bağlı (Y13) | — |
| E9 | On beş hata sınıfı tablosu | HATA §3 | HATTA VAR (çoğu) | 3a asimetrik işaret · 8 dünya cümlesi · 10 rakam · 11 arka plan · 12 iz (T14) hat dosyalarında | — |

## F · GEÇİŞ VE ÇEKİM SINIRI

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| F1 | Durum değişimi klip içinde yazılmaz, kesmede olur | ZINCIR §1 | HATTA VAR | `GOSTERIM` ilke 6 (T2V-CompBench) | — |
| F2 | Klip süren bir hareketin içinde biter; sonraki çekim aynı hareket sürerken başlar | COK §3.4 | HATTA VAR | `GECIS_VE_SES_SUREKLILIGI` §1 · goruntu-yonetmeni "ilk vuruş hareketle, kesme hareket üstüne" | — |
| F3 | Gizli geçiş: iki prompt birlikte tasarlanır — N'in son 0,5-1 s'si bir perdeyle kapanır, N+1 aynı perdeyle açılır; üç şart: ışık yönü, kir/doku, hareket hızı aynı | TEK_CEKIM §5-§6 | HİPOTEZ | `SECIM_VE_KURGU` §6 ③ "iki denemeyi gizli kesmeyle birleştirmek" için tasarım aracı; ölçülmedi | kılavuz §6 |
| F4 | Omurga lens, mekân-süre denklemi, 360° pratik ışık | TEK_CEKIM §3 §4 §7 | BAŞKA KÜME | küme 3 kamera | — |

## G · ESKİ ARAÇ VE ŞABLONLAR

| # | Madde | Kaynak | Etiket | Gerekçe |
|:--:|---|---|---|---|
| G1 | Omni I2V iskeleti, ses, iş akışı | OMNI_I2V | HATTA VAR / **RED** | `GPT_IMAGE_OMNI_KILAVUZU` (16.10, yeni araştırma) yerini aldı; tırnak/iki nokta sorusu `FLOW_GERCEKLERI` · SMOKE P9 |
| G2 | Veo 3.1 diyalog sentaksı, JSON iş akışı, ElevenLabs hibrit | VEO_3_1 | **RED** | araç ve diyalog yolu değişti (Omni · model sesi, 21.10.2026); "ton zarfla" Y13 ile çürüdü (`18` C10) |
| G3 | V2/V3 prompt şablonları (IN FRAME · START FRAME · NEGATIVE) | TEMPLATES | **RED** | hat şablonu `goruntu-yonetmeni` + `SABLON/PROMPTLAR/G01.md`; `IN FRAME:` etiketi film_dogrula M |
| G4 | Model seçimi, seed yönetimi, "kusurları kucaklamak" | SAHNE_DEVAMLILIK | **RED** | eski araç dönemi; kimlik `KIMLIK_VE_REFERANS` |
| G5 | Start/end frame zinciri (x. imaj + x+1. imaj = x. video) | KESINTISIZ · ZINCIR | HATTA VAR (⏸️) | zincir AGENTS F3b, yalnız zincir açıkken |
| G6 | Sahne 2-6 klip rejimi, `CONTINUOUS ACTION:` satırı, kapsama şablonları | COK §1-§2 | **RED** (biçim) | hat birimi 10 s çekim; özü (kalıntı) `KARAKTER_VE_DIYALOG` §3.1'de |

---

## Sayım

| Etiket | Madde |
|---|:--:|
| HATTA VAR (tam ya da kısmen) | 11 (A1 C1 C10 D1 E1 E4 E6 E9 F1 F2 G5) |
| **KANITLI (yeni)** | **9** (A2 A3 A5 B1 B2 C4 D2 D7 E2) |
| VAKA | 2 (C8 D3) |
| HİPOTEZ | 16 |
| RED | 9 (A8 C9 D6 E8 G1 G2 G3 G4 G6) |
| BAŞKA KÜME | 1 (F4) + `PROMPT_HATA_ONLEME` §2 ortam cümleleri (küme 4) |
| **Toplam** | **48** |

**Sonuç:** kümelerin en kanıtlısı. ~3.850 satırdan hatta yeni giren öz: 9 kanıtlı kural + 2 vakalı + 16 hipotez → tek kılavuz. Eski araç
belgelerinin (Veo, V2/V3 şablon, seed) hepsi düştü. İki eski öneri yeni ölçümle çürüdü: serbest parçacığa yön vermek (A12) ve iki yönlü temas
cümlesi (A3). En değerli tek ölçüm: **temas ilk 2 saniyede** (%5,9 ↔ %19,4).

**Ölçüm planı:** kılavuzla yazılan ilk filmin QA'sında — temas bulguları klibin hangi saniyesinde (A2) · zor iş çekimi yürümeye döndü mü (B2) ·
tripod çıktı mı (E2) · efor çekiminde sahne yavaşladı mı (C4).
