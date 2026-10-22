# 21 · SÜZME — KAMERA VE SAHNELEME (eski kılavuzlardan hatta)

> **Ne:** Eski hattın kamera, açı, mekân, ışık ve doluluk kılavuzlarının madde madde süzmesi; yöntem `18`-`20` ile aynı (sahip kararı 21.10.2026).
> Çıktı: `uretim_hatti/KAMERA_VE_MEKAN_KILAVUZU.md`.
> **Okunan (7 dosya · ~3.630 satır + devralınanlar):** `UZAMSAL_HARITA_VE_EKRAN_YONU` (1.269; §0.2 §1 §2 §4 §7-§9) · `SINEMATOGRAFIK_TEKNIK` (759; §10-§13) ·
> `ACI_YAYI_VE_SEKANS` (396; §1-§4b) · `KAMERA_ACISI_PSIKOLOJISI` (205) · `SAHNE_DOLULUGU` (444; §0-§3) · `ISIK_SENARYOSU` (322; §0-§7) ·
> `SENARYO_VE_VIRAL_KAMERA` (239; §2.4) · devralınan: `MESHUR_SAHNE_KALIPLARI` 20 kalıp (`19` F2) · `IKI_KISI_VE_AYRILIK` §5-§6 (`19` E5-E6) ·
> `TEK_CEKIM_VE_GIZLI_GECIS` §3-§4 · §7 (`20` F4).
> **Karşılaştırılan hat:** `yonetmen` çekim listesi kuralları (taraf/yön · ölçek/açı · tek bilgi) · `GECIS_VE_SES_SUREKLILIGI` §1 (ortak görünüm, mekân ışık cümlesi,
> ölçek/açı farkı) · `GOSTERIM_COZUMLERI` · `GPT_IMAGE_OMNI` §5 (mekân bir kez kurulur) · `PROMPT_HATA_ATLASI` A05 A12 A13 A14 · `ILK_30_SANIYE` §6 · ARIZA T04 T07 T11 T18.
> **Kanıt:** ARIZA (49 tam film) · eski coğrafya bulguları (UZAMSAL §1: 9 sınıf, film adlarıyla) · `MOONMOTHER/ODA/QA_DERSLER.md` D4 D6 · atlas A13 A14 · eski D3 D29 D33 D86 D193 · ADAY-86.

Etiketler `18`'deki gibi.

---

## A · COĞRAFYA VE EKRAN YÖNÜ

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| A1 | Taraf/yön çekimden çekime tutarlı; ışık ve sabit nesnenin ekran tarafı her promptta aynı kelimelerle | UZAMSAL §2 | HATTA VAR | `yonetmen` kural 7 (T11) · atlas A13 | — |
| A2 | Ekran-uzayı dili (`in the right third of the frame`, `screen-left to screen-right`); dünya-uzayı ve çapasız `toward the ship` yok | UZAMSAL §2 İlke 1 · §4.0 | VAKA (olumlu) | THIRD DUNE: sayılı konum dört sabit 25/25 sahnede tuttu; çapasız "toward" ile figür dizilimi kaydı (D86) | kılavuz §1 |
| A3 | **Konum, yönelim ve hareket ayrı yazılır; yönelim yazılmazsa model rastgele seçer** (araç burnu, gövde açısı) | UZAMSAL §2 İlke 4 · §4.2 | **KANITLI** (sorun) | LAST ARCHIVE · HERD ("ışınlanan gemi") · THIRD DUNE kalkış çanağı — araç yönelimi 3 film; çözüm biçimi (saat kadranı) sınanmadı | kılavuz §1 |
| A4 | **Yön taşıyıcıları (rüzgâr, toz, duman, enkaz, gölge) film boyu tek ekran yönünde** | UZAMSAL §7 kural 5 | **KANITLI** | KALEIDA duman · HOLDING FIELD enkaz · STONE SKY gölge — 3 film "mekân döndü" | kılavuz §1 |
| A5 | **Mekân değişimi geçişle kazanılır:** kısa geçiş çekimi ya da yeni mekânın ilk çekimi geniş ve eskisini arka planda gösterir | UZAMSAL §7 kural 4 | **KANITLI** | BLIND RETURN · CANOPY WORLD · HOLDING FIELD "ışınlanma" — 3 film · ARIZA H05 mekân sıçraması | kılavuz §1 |
| A6 | **Ölçek çapası:** büyük nesnenin boyu her çekimde neyin yanında ne kadar olduğuyla aynı cümle; yaklaşırken monoton büyür | UZAMSAL §4.6 · §7 kural 2 | **KANITLI** | COLD BURN dok kapısı dev ↔ oyuncak · MOONMOTHER D4 dev yaratık ay boyu ↔ normal boy | kılavuz §1 |
| A7 | **Kalıcı mekân hâli** (yüksek teras, kopuk uç) alçak kamerada da aynı cümleyle | — | VAKA | MOONMOTHER D6 kıyı coğrafyası değişti | kılavuz §1 |
| A8 | Giriş-çıkış eşlemesi (sağdan çıkan soldan girer); kameraya doğru/uzağa çekim nötrdür, taraf orada değişir; kesme matrisi | UZAMSAL §7 kural 6 · §7.1 | HİPOTEZ | klasik kurgu pratiği; depoda ölçülmedi | kılavuz §1 |
| A9 | Oryantasyon devri: dikey tırmanış sonraki çekimde yatay zeminde ayakta başlamaz | UZAMSAL §7 kural 3 | VAKA | BLIND RETURN 02:38; özü `KARAKTER_VE_DIYALOG` §3.1 kalıntı (KANITLI) | — |
| A10 | Kim solda film boyu kilit; iki figür konum kilidi (`the tall figure stays in the left third … neither crosses the centre`) | IKI_KISI §5 §6 | **KANITLI** (sorun) · HİPOTEZ (cümle) | D86 THIRD DUNE erkek/kadın taraf değiştirdi · T11 · cümle sınanmadı | kılavuz §1 |
| A11 | Kuşbakışı harita planda, prompta yalnız o çekimin ekran-uzayı çevirisi | UZAMSAL §3 | HİPOTEZ | `SAHNELEME.md` ⏸️ (zincir açıkken); çekim listesinde "Taraf / yön" sütunu yeterli | kılavuz §1 (tek satır) |
| A12 | Master geniş kare: coğrafya bir kez görselde kurulur, sonrakiler ona bağlanır | UZAMSAL §8 | HATTA VAR | `GPT_IMAGE_OMNI` §5 · mekân referans sayfası (§3) | — |
| A13 | Kurtarma: yanlış yönlü çekim kurguda yatay çevrilir — ayna kapısı (metin, asimetrik işaret, hangi el, araç asimetrisi, görünür yönlü ışık yoksa) | UZAMSAL §9 | HİPOTEZ | STONE SKY rapor önerisi; çevirme uygulanıp ölçülmedi | kılavuz §6 |
| A14 | Kesirli koordinat (x=0,72) · saat kadranı + derece kademeleri | UZAMSAL §4.0 | HİPOTEZ | kademe 2-3 hiç denenmedi | kılavuz §1 (tek satır) |
| A15 | Refleks çatışması: en parlak kaynak ve kamera figürün yönünü çeker; kilit iki denemede yenilirse kadraj değişir | UZAMSAL §1.1 Kanıt C | VAKA | BLACK CRADLE S4 iki deneme · eski D104 | kılavuz §2 |

## B · IŞIK

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| B1 | Mekân başına ışık cümlesi birebir; dünya ve gök cümlesi her dış çekimde aynı | ISIK §0 | HATTA VAR | `GECIS` §1-2 · `goruntu-yonetmeni` T18 | — |
| B2 | Işık değişimi (pratik söner, güneş batar) çekim içinde değil, çekim sınırında | ISIK §0⑩ | HATTA VAR | `GOSTERIM` ilke 6 | — |
| B3 | **Işığı çağıran tetik kelimeleri yazılmaz:** `volumetric · god rays · light shafts · glow · bloom · cinematic/dramatic lighting · lens flare` | ISIK §5 · SINEMA §11 | **KANITLI** | bloom yasak yazılıyken 6 filmde (atlas A14) · vakumda pus konisi (atlas A05) · eski D3 D29 D33; atlas "çağıran pozitif sözcük çıkarılır" ilkesinin listesi | kılavuz §2 |
| B4 | **Pratik ışık kaynakları sayılı ve konumlu, durumu film boyu sabit** (`one amber lamp above the hatch on the right`) | ISIK §2 · §6 | **KANITLI** | ADAY-86 (sönen pratik, duvardaki izi kaldı) · D193 ışık takvimi · ADAY-27/88 renk zıplaması | kılavuz §2 |
| B5 | Gövde kalıbı dört parça: yön + gölge yönü (ekran-uzayı) · gölge boyu (sözle) · kenar sertliği · gölge tarafı davranışı (`stays pure black` / `holds faint detail`) | ISIK §5 | HİPOTEZ | — | kılavuz §2 |
| B6 | Yön dünyada kilitli, ekran yanı kurulumdan türer: ters kurulumda güneşin ekran yanı değişmesi sıçrama değil fiziktir; aynı kurulumda değişmez | ISIK §2-§3 | HİPOTEZ | — | kılavuz §2 |
| B7 | Derece, Kelvin, oran gövdeye yazılmaz; planda durur | ISIK §0③ | HİPOTEZ | — | kılavuz §2 |
| B8 | Vakumda küresel lens, lens parlaması yok; anamorfik yalnız atmosferli/iç mekânda, sınırlı | SINEMA §11 | HİPOTEZ | B3 ile aynı yön | kılavuz §2 |
| B9 | Işık takvimi (güneş ↓ gölge ↑ renk ↓ monoton) | ISIK §2 | HİPOTEZ | eski D47 | kılavuz §2 (tek satır) |

## C · AÇI VE ÖLÇEK

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| C1 | Ardışık iki çekim aynı mekândaysa ölçek bir basamak ya da açı ≥30° değişir | ACI_YAYI §3 | HATTA VAR | `GECIS` §1-5 · `yonetmen` kural 5 | — |
| C2 | Eski öneri daha sıkı: ölçekte bir kademe **ve** açıda ≥45° (iki bağımsız klip benzedikçe mikro fark görünür) | ACI_YAYI §3 | HİPOTEZ | ölçülmedi; hat kuralı (YA DA, 30°) geçerli kalır | kılavuz §3 (not) |
| C3 | Açı sözlüğü ve vuruş → açı tablosu (keşif OTS · tehdit alt açı · yenilgi üst açı · çöküş eğik · epifani profil · hiçlik tepe) | KAMERA_ACISI §2-§3 | HİPOTEZ | dış (somutlaşmış simülasyon) | kılavuz §3 |
| C4 | Abartı eşikleri: eğik 5-15° ideal, 35°+ kiç; alt açı 45°+ grotesk; üst açı 45-60° "güvenlik kamerası" | KAMERA_ACISI §5 | HİPOTEZ | — | kılavuz §3 |
| C5 | Açı ve konum sayıyla: `tilted exactly 15 degrees` · `occupies only the lower third` (üst açıda konum yazılmazsa model figürü merkeze koyar) | KAMERA_ACISI §6③ | HİPOTEZ | — | kılavuz §3 |
| C6 | OTS karşıya büyük bir özne ister; boşluğa OTS bozuk kadraj okunur | KAMERA_ACISI §2 | HİPOTEZ | — | kılavuz §3 |
| C7 | "Sabitlik emri iki kez" ve "hareket süngeri: `subtle dust motes float slowly`, `slow rolling mist`" | KAMERA_ACISI §6①② | **RED** | atlas A12 (toz tarif edilince çizildi) · `HAREKET_VE_EFOR` §3 `slowly` tuzağı (KANITLI) | — |
| C8 | Yüz yakın planında geniş açı yok (Kubrick bakışı); 85 mm + sert yan ışık | SINEMA §13.2 | HİPOTEZ | yüz kilidi riski (eski D16) | kılavuz §4 |

## D · KURULUM DİZİSİ (açı yayı)

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| D1 | Kurulum çeşitliliği bandı (6 sahne → ≥3 · 12 sahne → ≤5-6; kurulum sayısı çekim sayısının yarısını geçmez) | ACI_YAYI §4 | HİPOTEZ | eski sahne birimleri; yön olarak kalır | kılavuz §3 |
| D2 | Dönüş: tanıtılmış kuruluma 3 çekim içinde dönmek iskelet kurar (A-B-A); dönüş oranı ≥%40 | ACI_YAYI §4b | HİPOTEZ | DIS_REFERANS: dış referans klipler tek kurulumda — depo filmleri ölçülmedi | kılavuz §3 |
| D3 | Şok bandı: ölçekte 2+ kademe sıçrama filmde en çok 1-2 kez, kırılma anına | ACI_YAYI §3 | HİPOTEZ | — | kılavuz §3 |
| D4 | Ayırma (A-B-A): iki özne aynı kadrajda değil, ardışık teklilerde | ACI_YAYI §2 | HATTA VAR | `GOSTERIM` ilke 3 (çekim başına tek özne) | — |
| D5 | "Küme": ardışık aynı kurulum, `continues the previous clip … same lens as Scene N` işaretiyle | ACI_YAYI §3 | **RED** | zincir dili ve başka çekime atıf film_dogrula M (atlas A09) | — |
| D6 | Omurga lens: çekimlerin ≥%60'ı tek odak uzaklığı, sapma gerekçeli | TEK_CEKIM §4 | HİPOTEZ | dış (1917) | kılavuz §3 |
| D7 | Tema → açı yayı eşlemesi · hazır dizilim şablonları | ACI_YAYI §5 §8 | **RED** | eski sahne sayıları; C3 + D2 yetiyor | — |

## E · ON SANİYEYİ DOLDURAN

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| E1 | 2-4 vuruş, son vuruş donmaz, durum değişimi kesmede | DOLULUK §0 §2 | HATTA VAR | `goruntu-yonetmeni` vuruş kuralı · `GOSTERIM` | — |
| E2 | Kilit fiil sınıfı: süreçli fiil (`hauls · works at · climbs`) 10 s taşır; noktasal fiil (`grabs · presses · turns`) bir anda biter, beden donar — dört ekle (direnç · aşama · alet · ağırlık) sürece çevrilir | DOLULUK §1 | HİPOTEZ | dış (Vendler); 10 s ritim kılavuzuyla aynı yön | kılavuz §5 |
| E3 | Başlangıç karesinde eylem zaten başlamış ama dengede (iki destek noktası yerde; adım ortası, sıçrama değil) | DOLULUK §2 ① | HİPOTEZ | `HAREKET_VE_EFOR` §1 (temas kurulu, KANITLI) ile uyumlu; "işin bitmiş hâli değil" kuralı korunur | kılavuz §5 |
| E4 | Tek çevre saati (kadraj kenarında sabit oranda sallanan kayış, damlayan sıvı, yürüyen gölge); ikincisi gürültü | DOLULUK §3② | HİPOTEZ | parçacık saat sayılmaz (atlas A12) | kılavuz §5 |
| E5 | İkinci görev: ana iş sürerken öteki el ikinci işte (dolgu jesti değil) | DOLULUK §3① | HİPOTEZ | — | kılavuz §5 |
| E6 | Yürüme mesafesi süreye ve yerçekimine uygun, sayıyla (1 g ~1,4 m/s → 10 s'de ~14 m) | TEK_CEKIM §3 | HİPOTEZ | "10 s'de 40 m ışınlanma" gözlemi | kılavuz §5 |

## F · KAMERA HAREKETİ, LENS, ÖZEL ÇEKİM

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| F1 | Rolling shutter / jöle negatif satırı | SINEMA §10 | **RED** | olumsuz blok yazılmaz (atlas A14); çare hızlı kamera yazmamak | — |
| F2 | Hızlı kamera (whip pan, hızlı yanal takip) yazılmaz | SINEMA §10 | HATTA VAR (kısmen) | ILK_30 §6 açılışta; geneli HİPOTEZ | kılavuz §4 |
| F3 | Dolly zoom ve rack focus tanımlanarak yazılır (`the subject's size stays exactly constant`); dolly zoom filmde en çok bir kez | SINEMA §12 | HİPOTEZ | "model kesme uydurur" gözlemi ölçülmedi | kılavuz §4 |
| F4 | POV filmde en çok bir; vizör içi POV kalıbı (nefes buğulu) | SINEMA §13.1 | HİPOTEZ · buğu **RED** | buğu 04.09.2026 sahip kararıyla reddedildi | kılavuz §4 |
| F5 | Roll tanımlanarak (`rotates slowly around its own optical axis … one unbroken move`) | SINEMA §13.3 | HİPOTEZ | — | kılavuz §4 (tek satır) |
| F6 | 20 meşhur sahne kalıbı promptu (K1-K20) | MESHUR §6 | **RED** (prompt) | kalıplar `slow motion` (K19), `anamorphic lens flares` (K14), `volumetric fog` (K6), `motionless`, `Audio:` tarifleri taşıyor — hat kurallarıyla çelişir; aile adları (izolasyon-ölçek · distopya · fiziksel kuvvet · tehdit) C3 ile kalır | — |
| F7 | Viral kare: yüzde duygu değişimi + yüksek hareket enerjisi | VIRAL §2.4 | BAŞKA KÜME | küme 7 (paylaşım) | — |
| F8 | Sensör, LOG/ACES, en-boy oranı | SINEMA §9 §14 §15 | **RED** | prompt etkisi yok ya da hat dışı (oran 16:9 sabit) | — |

---

## Sayım

| Etiket | Madde |
|---|:--:|
| HATTA VAR (tam ya da kısmen) | 8 (A1 A12 B1 B2 C1 D4 E1 F2) |
| **KANITLI (yeni)** | **7** (A3 A4 A5 A6 A10 B3 B4) |
| VAKA | 4 (A2 A7 A9 A15) |
| HİPOTEZ | 27 (F4'ün buğu kolu RED) |
| RED | 6 (C7 D5 D7 F1 F6 F8) |
| BAŞKA KÜME | 1 (F7) |
| **Toplam** | **53** |

**Sonuç:** kanıt sorun tarafında güçlü (yön, ölçek, mekân sıçraması, yön taşıyıcıları — üçer film), çözüm tarafında zayıf: tek olumlu ölçüm THIRD DUNE'un
"sayılı konum 25/25" kaydı. ~3.600 satırdan hatta yeni giren öz: 7 kanıtlı + 4 vakalı + 27 hipotez → tek kılavuz. Eski "hareket süngeri" (toz, sis) ve
20 kalıp promptu hat kurallarıyla çeliştiği için düştü.

**Ölçüm planı:** kılavuzla yazılan ilk filmin QA'sında — yön taşıyıcıları tek yönde mi (A4) · mekân değişiminde ışınlanma okundu mu (A5) · büyük nesnenin
ölçeği sabit mi (A6) · bloom/pus çıktı mı (B3).
