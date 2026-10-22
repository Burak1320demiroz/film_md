# 18 · SÜZME — KARAKTER, OYUNCULUK, DİYALOG (eski kılavuzlardan hatta)

> **Ne:** Eski hattın karakter/oyunculuk/diyalog kılavuzlarının madde madde süzmesi. Sahip kararı (21.10.2026):
> "kılavuzları analiz edip üretim hattına yeni kılavuz olarak ekleyelim" — kopyalama değil süzme; AGENTS §7
> KOPYALANMAZ kuralı gereği her madde kanıtıyla etiketlenir. Çıktı: `uretim_hatti/KARAKTER_VE_DIYALOG_KILAVUZU.md`.
> **Okunan (7 dosya · ~4.100 satır):** `KARAKTER_VE_DUYGU` (462) · `KARAKTER_KARTI_VE_DAVRANIS` (400) · `OYUNCULUK_YAZIM` (465) ·
> `DIYALOG_SAHNESI_VE_MUHATAP` (386) · `SES_VE_DIYALOG_URETIM` (427) · `POST_TRAVMA_VE_DURUM_HAFIZASI` (167) ·
> `AI_FILMLER_ICIN_DOGAL_DIYALOG_YAZIMI` (1.808, 21.10.2026 hat uyarlaması). Hepsi `kilavuzlar_ve_sistem_dosyalari/` altında, dokunulmadı.
> **Karşılaştırılan hat dosyaları:** `diyalog-yazari` ajanı · `REPLIK_VE_KLIP_SESI_KILAVUZU` · `ARIZA_LISTESI` (H06 H09 H12 T02 T12) ·
> `BILINEN_TUZAKLAR` · `ILK_30_SANIYE_KILAVUZU` §4 · `GPT_IMAGE_OMNI_KILAVUZU`.
> **Kanıt kaynakları:** eski `DERSLER/` (D35 D82 D202 D207 D217 · ADAY-26/84/85) · `MOONMOTHER/ODA/QA_DERSLER.md` (D2 D3 D9) ·
> `ARASTIRMA/16` Y13 · `ARASTIRMA/11` · `REPLIK_VE_KLIP_SESI` §0.

## Etiketler

| Etiket | Anlamı | Hatta nasıl girer |
|---|---|---|
| **HATTA VAR** | aynı kural hat dosyasında yazılı | girmez; adres gösterilir |
| **KANITLI** | ≥2 filmde kayıtlı vaka (eski QA raporları yapay zekâ yazdı — ARIZA'nın uyarısı geçerli) | kural olarak, kaynağıyla |
| **VAKA** | tek kayıt; çözümün etkisi ölçülmedi | `HİPOTEZ (vaka: …)` |
| **HİPOTEZ** | dış araştırma ya da yazarın tasarımı; hatta 0 ölçüm | `HİPOTEZ`, kısa |
| **RED** | sözleşmeyle ya da yeni ölçümle çelişiyor, kapalı format, ya da kapanmış araç | girmez; gerekçe burada |
| **BAŞKA KÜME** | konu başka kümenin | o kümede süzülür |

---

## A · KARAKTER

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| A1 | Karakter ekranda bir şey ister, kaybeder; istek bir iş, bedel sahne numarasıyla | KARTI §1 · DUYGU §3 | HATTA VAR | ARIZA H06 · H12 panzehiri | — |
| A2 | **İsteğin hedefi kadrajda görünür** (yürüyüşün gittiği yer, uzandığı nesne) | DUYGU §3 | **KANITLI** | MOONMOTHER D3 (hedef görünmeyen yürüyüş "sıkıcı", amaç 30 s geç anlaşıldı) · H03 yürüme dolgusu 24/52 | kılavuz §1 |
| A3 | **Seçim iki şeyden birine gitmektir:** seçilen ve reddedilen kadrajda, reddedilen sonra da orada | KARTI §3 · OYUNCULUK §2 | **KANITLI** | D202 "görünmez seçim" 5 film · MOONMOTHER D2 (seçim çekimi kurguda yok) · eski dikey teşhis: seçim duruş değişikliğiydi | kılavuz §2 |
| A4 | **Seçimin önce/sonra beden farkı** aynı kanalda, adlandırılabilir ("omuz iner", "el bırakır") | OYUNCULUK §2 ÇAPA | **KANITLI** | D202 (⑩ "THE CHOICE IS INVISIBLE" 4 film) | kılavuz §2 |
| A5 | Karakter kartı 8 satır (rol · istek · baskı tepkisi · alışkanlık · sınır · zaaf · tel · ilk↔son) | KARTI §1 | HİPOTEZ (sadeleşir) | 0 ölçüm; kartla yazılmış film ⑩'da hiç koşulmadı. Beş satıra iner: İSTEK · BASKI TEPKİSİ · ALIŞKANLIK · ZAAF · İLK↔SON | kılavuz §1 |
| A6 | Alışkanlık jesti: 3 tekrar (birebir aynı cümle) + 1 kırılma, seçim/bedel sahnesinde | KARTI §2 | HİPOTEZ | dış vaka (*Le Samouraï*, *All Is Lost*); depoda uygulanıp ölçülmedi | kılavuz §1 |
| A7 | Zaafı olmayan figür "avatar" okunur; kusursuz yetkinlik soğuk | KARTI §7 · §9 | HİPOTEZ | Fiske (dış); D206/⑧ "NOBODY PAYS" ile aynı yön (eski) | kılavuz §1 |
| A8 | İlk ↔ son eylem farkı tek cümleyle adlandırılır | KARTI §6 | HİPOTEZ | ⑩ kat. 8 hiçbir filmde 7'yi geçmedi (eski, ölçüm tarafı); yazım tarafı sınanmadı | kılavuz §1 |
| A9 | Mizah tehlikenin ortasında değil hemen sonrasında | KARTI §9 | HİPOTEZ | Zillmann (dış) | kılavuz §6 (tek satır) |
| A10 | Davranış şeridi (G T D K B R S harfleri, dağılım tablosu) | KARTI §4 | **RED** | ölçülmemiş bürokrasi; özü (K'dan sonra G yok) A3 + B5'te kalır | — |
| A11 | Format tablosu (dikey 6×8 s · 3-5 dk 25 sahne · 7-9 dk 60×8 s) | DUYGU §3 · KARTI §6 §10 | **RED** | kapanmış formatlar; hat formatı 2·4·8·16 dk, çekim 10 s | — |
| A12 | Tek kişilik film: nesne → beden → geçmiş karar kanalları sırayla | KARTI §8 | HİPOTEZ | tek dış vaka, zaman damgası doğrulanmadı | kılavuz §6 (tek satır) |

## B · OYUNCULUK (bedene yazım)

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| B1 | **Kesmede sıfırlanma yok:** önceki çekimin son bedeni (yorgunluk, şok, eğilme) sonrakinin ilk karesine taşınır | OYUNCULUK §5 · POST_TRAVMA §1 | **KANITLI** | D207 4 film · ADAY-26 · ADAY-84 · ⑩ desen ⑧ | kılavuz §3 |
| B2 | Darbe sonrası toparlanma kademeli (en çok bir kademe/çekim); düşen sonraki çekimde yürüyerek başlamaz | POST_TRAVMA §1 | VAKA | D207 çözümü; merdivenin etkisi ölçülmedi (POST_TRAVMA §5) | kılavuz §3 |
| B3 | Sakatlık uzuvla yazılır ("dragging the left boot", "limping" değil) | POST_TRAVMA §1.2 | VAKA | eski PROMPT_HATA §3 3a (asimetrik işaret kolu değişti) | kılavuz §3 |
| B4 | Acı/yara kelimesi yok; beden mekaniği yazılır | POST_TRAVMA §1.2 | HATTA VAR | BILINEN_TUZAKLAR §A (şiddet kelimeleri reddi) | — |
| B5 | **Dolgu jesti yazılmaz** (eldiven kontrolü, kaska dokunma, "adjusts the suit", sebepsiz el kaldırma) | OYUNCULUK §6 · KARTI §2 | **KANITLI** | ADAY-85 → D202 (LOW_POWER S5/S19) · ⑩ desen ⑨ | kılavuz §3 |
| B6 | Her jestin önünde kadrajda görünen bir tetik (olaysız jest = "duygu spreyi") | OYUNCULUK §6 | HİPOTEZ | ⑩ desen ④ (eski ölçüm adı); yazım tarafı sınanmadı | kılavuz §3 |
| B7 | Niyet sözlüğü: bakış eli önceler · ağırlık önce kayar · tereddüt dur-git · bırakma yavaş · tempo kontrastı · mesafe sayaç | OYUNCULUK §3 | HİPOTEZ | dış (motor kontrol literatürü); depoda prompt kalıbı olarak ölçülmedi | kılavuz §3 (5 kalıp) |
| B8 | "still / motionless / frozen" tek başına → resim gibi donma; durgunluk nefes + sabit bakış + tek mikro hareketle | OYUNCULUK §4 | HATTA VAR (kısmen) | `goruntu-yonetmeni`: son vuruş donmaz (LAST_GATE 87/92); vuruş içi durgunluğa genişletmek HİPOTEZ | kılavuz §3 |
| B9 | Görünür nefes omuz hattında (basınç giysisinde göğüs okunmaz) | OYUNCULUK §3 ⑦ · DUYGU §4.2 | HİPOTEZ | dış; vizör buğusu sahip kararıyla reddedilmişti (eski) | kılavuz §3 |
| B10 | Dorukta duygu gövde/el/omuzda; yüz doruğun öncesi ve sonrasında | DUYGU §4.3 · OYUNCULUK §7 | HİPOTEZ | dış ölçüm (Aviezer 2012, Meeren 2005); hatta ölçülmedi | kılavuz §3 |
| B11 | Basınç giysisinde öfke/iğrenme bedenden zayıf okunur; korku çift kanal (kaçan bakış + sığ nefes) | DUYGU §4.3 | HİPOTEZ | dış (Front Psychol 2020) | kılavuz §6 |
| B12 | Gözyaşı / ıslak göz bloom ve doku kaybı riski | DUYGU §0④ | VAKA | eski D3 · D41 | kılavuz §6 |
| B13 | Donuk oyunculuk → yakın plan yalnız tepki anında | — | HATTA VAR | ARIZA T12 | — |
| B14 | Göz/el/yürüyüş/eşya yüzde bütçeleri (%12 · %15 · %10 · %5 · tepki %25 · Kuleshov her 30 s) | DUYGU §1-§6 | **RED** | dış sayı, sahne harcar, 0 ölçüm; fikir (beden kanalları) B7'de kalır | — |
| B15 | Laban eşlemesi (Indirect/Sustained/Bound…) | OYUNCULUK §3 | **RED** | prompta girmez, B7 sözlüğü işi görür | — |
| B16 | Vizör içi aydınlatma bloğu · "kask açılmaz" ekipman kilidi | DUYGU §0② §1 | BAŞKA KÜME | uzay giysisi/ekipman → küme 4 (Dünya ve tasarım) · `KIMLIK_VE_REFERANS` | — |
| B17 | Hasar hafızası · kadro kilidi ("exactly N people", giden gelmez) | POST_TRAVMA §2-§3 | BAŞKA KÜME | süreklilik → küme 4/5 · `KIMLIK_VE_REFERANS` | — |
| B18 | Kapı adayları (prompt_kontrol ㉒ NİYET KANALI, SPEC ÇAPA bloğu) | OYUNCULUK §9 · KARTI §10 | **RED** | eski araçlar yeni hatta koşulmaz (AGENTS §7) | — |

## C · DİYALOG

| # | Madde | Kaynak | Etiket | Kanıt / gerekçe | Hatta |
|:--:|---|---|---|---|---|
| C1 | Görüneni söyleyen replik silinir | SES §1 · §2a.1 | HATTA VAR | D217 2 film · H09 · `diyalog-yazari` silme testi | — |
| C2 | Duygu adı söylenmez (afraid, scared, "I feel") | SES §2a.2 | HATTA VAR | `diyalog-yazari` alt metin | — |
| C3 | Konuşma profili; adlar silinince ayırt edilir (swap testi) | SES §2a.4 · DOGAL §4-§5 | HATTA VAR | `diyalog-yazari` §3 | — |
| C4 | Değiş tokuş: her alışveriş bilgi/ilişki/karar değiştirir; değiştirmeyen silinir | DIYALOG_SAHNESI §2 §6 | HATTA VAR | `diyalog-yazari` §1 + çıktı NEDEN satırı | — |
| C5 | Gecikme bandı (≤0,3 onay · 0,5-1 ret beklentisi · 1-2 açık ret) | DIYALOG_SAHNESI §3 | HATTA VAR | `diyalog-yazari` §7 | — |
| C6 | "As you know" yok; bilgi dirençle gelir (suçlama, pazarlık) | SES §2a.3 · DOGAL §8 | HATTA VAR (kısmen) | `diyalog-yazari` kulak testi "as you know" yok; "bilgiyi talebin gerekçesi yap" eklenir (HİPOTEZ) | kılavuz §4 |
| C7 | **Sayı, birim, geri sayım makine sesinde; insan ağzına geçmez** | SES §1 SAYI KURALI | VAKA | D82 COLD BURN (sayılar ağızlara geçti, senkron çöktü); `diyalog-yazari` makine satırında var ama kural değil | kılavuz §4 |
| C8 | **Model sesi repliğini sıfatla sarma** ("hesitant", "calm breathing", "warm and low") | — | **KANITLI** | Y13: MAYDAY #19 "hesitant" takılma çağırdı · #31 acil replik sakin sıfatlarla düz okundu (MAYDAY · FURNACE) | kılavuz §5 |
| C9 | **Kadrajda tek kişi + kadraj dışı replik model sesinde ikilenir** | — | **KANITLI** | Y13: FURNACE #1 #30. Kadraj dışı ses kurgu kaydıyla yapılır | kılavuz §5 |
| C10 | VEO sentaksı: ton zarfla verilir ("in a weary voice") | SES §3 | **RED** | C8 ölçümüyle ters yönde; hat biçimi `REPLIK_VE_KLIP_SESI` §3 (`she says: <line>`, kısa aynı ses tarifi) | — |
| C11 | Dinleyenin bedeni: tepki replik bitmeden başlar; konuşanın hareketi sözden önce | DIYALOG_SAHNESI §4 | HİPOTEZ | konuşma analizi (yüz yüze); telsiz/kaskta ölçülmedi | kılavuz §4 |
| C12 | **Sinyalin/repliğin muhatabı kadrajda ya da hemen sonraki çekimde** | DIYALOG_SAHNESI §1 §5 | VAKA | MOONMOTHER D9 (ışık sinyalinin muhatabı yok → "neyi tetiklediği anlaşılmıyor") | kılavuz §4 |
| C13 | En güçlü kurulum: kadraj dışı ses + dinleyen kadrajda (Kuleshov'un diyalog hâli) | DIYALOG_SAHNESI §5 · DUYGU §2 | HİPOTEZ | dış (Smith, *Shirin*); C9 nedeniyle ses kurgu kaydıyla | kılavuz §4 |
| C14 | Muhatap tipleri: cevapsız telsiz (sessizlik cevaptır) · makine · nesne · kayıt; saf monolog yazılmaz | DIYALOG_SAHNESI §1 | HİPOTEZ | dış tipoloji; eski "monolog 9/9 bilgi yığını" iddiası kaynaksız | kılavuz §4 |
| C15 | Söz ≠ eylem (yalan) bağ kurar, fedakârlığa bağlıysa | SES §2a.6 | HİPOTEZ | dış (ADT) | kılavuz §6 |
| C16 | İroni penceresinde replik nötr yazılır | SES §2a.7 | HİPOTEZ | dış | kılavuz §6 |
| C17 | Son replik doruktan önce biter; doruk ve final sessiz | DIYALOG_SAHNESI §8 | HİPOTEZ | eski planlardan öneri; ölçülmedi | kılavuz §4 |
| C18 | Doğal İngilizce: kısaltma, kısa parça, planlı tek kesinti; çeviri kokusu (hiper-formalite, calque) | SES §2a.5 · DOGAL §13 | HİPOTEZ | dış korpus; izleyicinin çoğu anadili İngilizce değil (ILK_30 §4) → kısa ve sık kelime | kılavuz §4 |
| C19 | Tek konuşmacı, üst üste binme yok; dinleyenin ağzı kapalı yazılır | SES §2 · DIYALOG_SAHNESI §4 §7 | HATTA VAR | `REPLIK_VE_KLIP_SESI` §3 · `diyalog-yazari` | — |
| C20 | Replik 10 s'ye sığar; konuşma bitince kalan vuruşa tepki/sonuç | SES §2 · DOGAL §16 | HATTA VAR | `REPLIK_VE_KLIP_SESI` §2 · 10 s ritim kılavuzu | — |
| C21 | Her replik <5 s · diyalog yalnız medium+ · kasksız sahnede konuşma yok | SES §2 | **RED** | eski Veo/kask kilitleri; hat `REPLIK_VE_KLIP_SESI` §1-§3 ve 12.10 model sesi kararı | — |
| C22 | Diyalog merdiveni (kadraj dışı → kayıt → ekranda ağız "PROB B'siz girmez" → hibrit) | SES · DIYALOG_SAHNESI §7 | **RED** | 12.10.2026 model sesi kararıyla aşıldı | — |
| C23 | Telsiz dili ve protokolün kırıldığı an duygudur | SES §2a.8 | HATTA VAR | `diyalog-yazari` §4 | — |
| C24 | İlk insan sesi yapısal anda ("biyolojik şalter", P300) | SES §1a.2 | HATTA VAR (kısmen) | ILK_30 §4 (ilk 2 s insan sesi yok); P300 gerekçesi laboratuvar, film değil | — |
| C25 | DIALOGUE_CRITIQUE T9 testi · kapı adayı | DIYALOG_SAHNESI §9 | **RED** | eski araç | — |
| C26 | Vakum sesi, yatak, AUDIO bloğu | SES §4 §5 | HATTA VAR | `REPLIK_VE_KLIP_SESI` §4 · `GECIS_VE_SES_SUREKLILIGI` | — |

---

## Sayım

| Etiket | Madde |
|---|:--:|
| HATTA VAR (tam ya da kısmen) | 15 |
| KANITLI | 7 (A2 A3 A4 B1 B5 C8 C9) |
| VAKA | 5 (B2 B3 B12 C7 C12) |
| HİPOTEZ | 18 |
| RED | 9 |
| BAŞKA KÜME | 2 (B16 B17) |
| **Toplam** | **56** |

**Sonuç:** ~4.100 satırdan hatta yeni giren öz: 7 kanıtlı kural + 5 vakalı + 18 hipotez → tek kılavuz (~180 satır).
En değerli bulgu yeni ölçümden geldi, eski kılavuzdan değil: C8 ve C9 (model sesinde sıfat sarmalı ve kadraj dışı replik).
C10 eski bir kuralın yeni ölçümle çürüdüğü yer.

**Ölçüm planı:** kılavuzla yazılan ilk filmin QA'sında şu dört soru sorulur — seçim kadrajdan okunuyor mu (A3-A4) ·
kesmede beden sıfırlanıyor mu (B1) · dolgu jesti var mı (B5) · model sesli replik takılıyor/düz okunuyor mu (C8).
İki filmde aynı yönde çıkan HİPOTEZ, sahip kararıyla kurala döner (AGENTS §1b).
