# 🧑‍🚀 ASTRONOT DONANIM VE KİMLİK KILAVUZU — Giysi Üzerinden Karakter

> **Ne zaman okunur:** Yeni uzay filmi yazılırken, **Character Bible
> yazılmadan ÖNCE** (Kart A · sahne haritasıyla bible arasında).
> Kadrajda basınç giysili karakter varsa zorunlu.
> **Ne işe yarar:** Aynı beyaz giysiyi giyen karakterleri vizör kapalıyken
> ayırt ettirir; rozet, kişisel eşya, saat/bilek ve sırt ünitesini hem
> gerçekçi hem AI-üretilebilir çapalara çevirir.
> **Kaynak:** TUR 5 dış araştırması (03.09.2026) —
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 5. Ham raporlar:
> `URETIM_ONCESI_ANALIZ/TUR5_HAM_RAPORLAR/`. Kural buradan okunur,
> bulgunun nereden geldiği oradan okunur.
>
> ⚠️ **DÜRÜST SINIR:** Bu kılavuzun tarihsel satırları ansiklopedik/ikincil
> kaynaklara dayanır (hakemli değil); "⭐ öneri" işaretli satırlar ise
> raporların KENDİ tasarım icadıdır, ölçüm değildir. Hiçbir çapa henüz
> üretimde test edilmedi — ilk uygulamada ① KARE ve ② DEVAMLILIK
> skorlarıyla sınanır.

---

# 0. ⛔ ÜÇ KIRMIZI ÇİZGİ — her şeyden önce

```
① GERÇEK AD YOK. Prompta gerçek bayrak, ülke adı, ajans adı/logosu
   (meatball/worm dâhil), marka adı (saat markaları dâhil) YAZILMAZ —
   politika (milliyet → prompt_kontrol ⑯ BLOCK) + telif. Yerine bu
   kılavuzun jenerik İngilizce tanımları kullanılır.
② OKUNUR METİN YOK. İsimlik, yama yazısı, panel etiketi, dijital rakam —
   model küçük metni bozar ve depo yasağı zaten var [D34·D45·D138].
   Ekran = "glowing digital readout" gibi ışık soyutlaması; yama =
   salt geometri + renk + SAYILABİLİR öğe.
③ SERBEST UÇLU HORTUM YOK. İnce hortum ağı, kolye zinciri, sallanan
   kablo → sahneden sahneye kayar (yüksek risk sınıfı, §7). Hortum
   yazılacaksa iki ucu da adlandırılır ("from backpack to chest module")
   ya da hiç yazılmaz — YERÇEKİMİ bible'ının "no pack, tank, hose or
   cable" satırı meşru ve güçlü bir NEGATİF çapadır.
```

---

# 1. 🧩 DÖRT KATMAN MODELİ — çapa envanteri ve bütçesi

Karakter kimliği giysi üzerinde dört katmandan kurulur. **Her katmandan
en fazla 1-2 çapa** seçilir; hepsi birden yazılırsa karakter bloğu
uzunluk tavanını yer (KILAVUZ_REHBERI §7) ve eşyalar birbirini boğar
(rapor ilkesi: karakter başına ≤2 kişisel eşya).

```
KATMAN 1  ROL ŞERİDİ + AMBLEM   → §2, §3   uzak ölçekte KİM olduğu
KATMAN 2  SIRT SİLUETİ          → §4       uzak/orta ölçekte GÖREVİ
KATMAN 3  BİLEK DÜZENİ + SAAT   → §5, §6   orta/yakın ölçekte SÜRE/İŞ
KATMAN 4  KİŞİSEL EŞYA          → §8       yakın ölçekte İÇ DÜNYASI
```

Çapa seçim ölçütü (dördü birden aranır):
**BÜYÜK · GEOMETRİK · SAYILABİLİR · ASİMETRİK.**
Sayılabilir çapa aynı zamanda QA kilididir: "üç ışık", "altı segment",
"dört lamba" ① ve ⑥ merceğinin ölçebildiği sayılardır.

⛔ Seçilen çapalar Character Bible'a **tek İngilizce blok** olarak yazılır
ve `SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1 gereği kelimesi kelimesine
kopyalanır. **Üretimi başlamış filmin bible'ı DEĞİŞTİRİLMEZ** — bu
kılavuz yeni filmler ve yeni karakterler içindir.

---

# 2. 🎗️ ROL VE HİYERARŞİ — şerit sistemi

**Tarihsel temel (belgeli):** İlk Ay yürüyüşlerinde iki beyaz giysi
ayırt edilemedi; Apollo 13'ten itibaren komutanın kollarına, diz
altlarına ve vizör üstüne **kırmızı şeritler** dikildi ("commander
stripes"). Rus Orlan ekolü ikili sistemi kullanır: komutan **kırmızı**,
uçuş mühendisi **mavi** şeritli giysi. Şerit uzva 360° sarılır —
çevresel düz renk bandı AI'ın en iyi koruduğu işaret sınıfıdır (§7).

**Depo kuralı — rol → renk → konum:**

| Rol | Renk | Konum (asimetrik) | İngilizce kalıp |
|---|---|---|---|
| Komutan / lider | kırmızı veya turuncu | SAĞ kol + SAĞ uyluk, çevresel | `a bold red fabric stripe wrapped around the RIGHT forearm and RIGHT thigh` |
| Mühendis / ikinci | elektrik mavisi veya lacivert | SOL pazu + SOL uyluk, çevresel | `a bright electric blue stripe wrapped around the LEFT bicep and LEFT thigh` |
| Bilim / tıbbi | neon yeşil veya sarı | sırt ünitesi kenarı veya tek pazu | `a single neon green band along the edge of the backpack` |

```
□ Genişlik bandı: ~5 cm ("a five-centimeter-wide stripe" yazılabilir —
  genişlik değil VARLIK + RENK + KONUM çapadır)
□ Tarihsel uygulama İKİ TARAFLIDIR (iki kol + iki bacak); depo tek
  tarafı seçer (⭐ öneri): asimetri hem karakteri ayırır hem ayna/flip
  hatasını ⑥ merceğine ölçtürür (LEFT/RIGHT çapaları bible geleneği)
□ Filmde tek karakter varsa şerit HİYERARŞİ değil KİMLİK işidir: tek
  renk seç, her sahnede aynı yaz — YERÇEKİMİ'nin ORANGE/NAVY güçlendirme
  şeritleri bu sistemin depodaki ilk örneğidir
□ Işık kısıtı: karanlık sahnede renk okunmaz → şerit çapası gece
  sahnesine yaslanmaz; orada silüet (§4) devralır
```

---

# 3. 🔷 METİNSİZ AMBLEM DİLİ

**Tarihsel temel (belgeli):** Görev yaması ~10 cm bandındadır; standart
yerleşim **sol göğüs = görev yaması · sağ göğüs = ajans amblemi +
isimlik · sol omuz = bayrak**. Yama sembolojisi SAYILABİLİR çalışır:
mürettebat sayısı kadar yıldız, altı kişilik ekip için altıgen form,
yörünge eğimi kadar derece açı (Soyuz TMA-15M: 51°).

**Depo amblem seti (⭐ öneri — kurgusal, ülke-nötr, metinsiz):**

| Öğe | Konum | Tasarım | İngilizce kalıp | Risk |
|---|---|---|---|---|
| Ajans rozeti | sağ göğüs | tek kalın metalik şevron, koyu zemin, daire | `a textless circular badge with a thick metallic silver chevron on a dark navy background, embossed embroidery` | çok düşük |
| Görev yaması | sol göğüs | altıgen; mürettebat sayısı kadar altın nokta + tek turkuaz yarım daire | `a textless hexagonal mission patch with three distinct gold dots and a turquoise semicircle on black` | orta (nokta SAYISI kilitlenir) |
| Nötr sancak (bayrak muadili) | sol omuz | köşegenden ikiye bölünmüş iki renk | `a textless flag patch divided diagonally into matte grey and sun yellow on the left shoulder` | düşük |
| Sırt bloğu | sırt ünitesi üst kapağı | tek parlayan geometrik form | `a single glowing cyan triangle on a reflective silver square panel on the backpack` | orta |

```
□ Yama başına EN FAZLA 2-3 renk, TEK geometrik motif
□ Sayılabilir öğe sayısı = anlatı verisi (mürettebat sayısı, kalan gün)
  → plana kilit olarak yazılır; model sayıyı şaşırırsa ① mercek yakalar
□ Doku kelimesi gerçekçiliği taşır: "embossed embroidery" (nakış) /
  "heat-pressed matte polyurethane" (modern) — düz vektörel yama
  plastik durur
□ Karakter başına amblem YÜKÜ: uzak plan filmlerinde yalnız şerit + 1
  yama yeter; dört öğenin dördü yalnız yakın planlı, az karakterli
  filmde taşınır
□ Seri kimliği: aynı amblem seti bir SERİNİN imzası olabilir —
  karar sahibinde (SERI_VE_KANAL_STRATEJI_KILAVUZU.md §3)
```

---

# 4. 🎒 SIRT SİLUETİ VE YAŞAM DESTEK DIŞ ANATOMİSİ

**Dıştan görünür modüller (belgeli, EMU esaslı):**

```
SIRT ÜNİTESİ (PLSS)  dikdörtgen prizma, ~66×46×24 cm, mat beyaz
                     kapitone termal kumaş, omuz hizasına yükselir —
                     profil silueti neredeyse iki katına çıkar
YEDEK O2 (SOP)       ana bloğun ALTINA asılı, daha dar, yuvarlak hatlı
ACİL İTKİ (SAFER)    sırt grubunun altını/yanlarını saran U-profil,
                     24 küçük siyah lüle (sayılabilir!)
GÖĞÜS MODÜLÜ (DCM)   göğüs ortasında açılı metalik kutu: analog ibre +
                     parlayan segment ekran + renk halkalı soketler
KASK (EVVA)          küre + AYNA GİBİ ALTIN VİZÖR; üstte 4 lamba,
                     yanda tek kamera çıkıntısı
```

**Siluet → hikâye eşlemesi (yorum katmanı raporundan, ⭐ öneri):**

| Siluet | Görünüm | Uyduğu hikâye durumu |
|---|---|---|
| Modüler + dev sırt çantası (EMU tipi) | metal kilit halkaları, geniş omuz | rutin dış operasyon, alet işi, çoklu mürettebat |
| Yekpare, kask gövdeye birleşik (Orlan tipi) | boyunsuz, pürüzsüz, monolitik | uzun ve İZOLE EVA — otonom, yalnız figür |
| Atletik, koyu renkli, eklemli (yeni nesil) | kıvrılabilen diz/bel | gezegen yüzeyi: yürüyüş, çömelme, örnek alma |
| Sırt çantasız, karından hortumlu (kabin tipi) | ince tulum, göbek bağı | kabin içi, acil çıkış, klostrofobi — "araca bağlı" psikolojisi |

```
□ İki-üç karakter SIRTTAN ayrışır (kamera arkadan geldiğinde):
  A: sırtında U-profil itki paketi (köşeli taşma)
  B: yalnız yuvarlak hatlı yedek modül (küt sırt)
  C: DÜMDÜZ sırt — "no pack, no tank" (YERÇEKİMİ A karakteri örneği)
  → üç silüet üç kelime grubudur, uzak planda bile okunur
□ Sırt tarifi bible'da TEK cümledir ve her sahnede aynıdır; "flat back"
  ile "thruster frame" farkı YERÇEKİMİ'nde sınanmakta olan modeldir
□ Altın vizör en güvenilir tekil çapadır: "highly reflective gold
  sun-visor" — yansıma sahne ışığını taşır, model küreyi iyi korur
```

---

# 5. 📟 GÖSTERGELER, ALARM VE ARIZA GÖRSELLİĞİ

**Göstergeler (belgeli):** Oksijen basıncı analog İBREDİR (güç kesilse
de çalışır); kadran yeşil/sarı/kırmızı dilimlidir. Kalan süre ve
telemetri göğüs modülünün üst yüzündeki segmentli ekranda soluk
yeşil/sarımsı parlar. Panel etiketleri TERS basılıdır — astronot sağ
bileğindeki AYNAYLA okur (§6). Prompta rakam yazılmaz:
`a small analog gauge with a green-yellow-red arc` ·
`a faint green glowing digital readout` (metin/rakam tarif edilmez).

**Alarm konvansiyonu (belgeli):** sarı yanıp sönen ışık = ikaz,
kırmızı yanıp sönen ışık = kritik. İmza sesi düdük değil **"warble"**
— frekansı dalgalanan elektronik ötme; kritiklik arttıkça tizleşir.
AUDIO kalıbı (SES_VE_DIYALOG register: MACHINE ile uyumlu):

```
AUDIO: a low wavering electronic warble tone from inside the helmet
AUDIO: a harsh, fast, high-pitched warble alarm; a red light blinks
```

**Arıza görselliği — dış kameradan (belgeli vakalar):**

| Arıza | Dıştan görünen | İngilizce kalıp |
|---|---|---|
| Soğutma çöküşü / aşırı efor (Gemini 9A) | vizör içi süt beyazı buğu, damlacıklar; yüz silik gölge | `the inside of the visor fogs into an opaque milky layer; the face becomes a dim silhouette` |
| Soğukta yoğunlaşma | vizör iç yüzünde ince kırağı | `a thin crystalline frost creeps across the inside of the visor` |
| Su kaçağı (2013 EVA vakası) | kask içinde titrek, ışığı büken su kütlesi | `a wobbling blob of water clings inside the helmet, bending the light like a lens` |
| Isı tahliyesi / venting | sırt ünitesinden ~1 m'ye uzanan beyaz buz kristali jeti | `a fine white vapor jet of ice crystals vents from the backpack and slowly dissipates` |

```
□ Arıza görseli SAYILABİLİR yazılır ("a single white vapor jet") —
  ⑥ FİZİK merceği kilit ister
□ Arıza + panik ayrımı: görsel arıza tırmanırken karakter SAKİN
  kalabilir (dramatik ironi, HOOK §3.1) — buğu oyuncudan ucuzdur
□ Buhar jeti YÖN taşır: vakumda itki üretir — sahnede jet varsa
  gövde tepkisi ORTAM kartıyla (KILAVUZ_REHBERI §3.1) tutarlı olmalı
```

---

# 6. ⌚ BİLEK DÜZENİ VE SAAT

**Yerleşim (belgeli; iki kol iki işlev):**

```
SOL KOL   iş + zaman kolu
  · dirseğe yakın: spiral ciltli BİLEK KONTROL LİSTESİ (kavisli
    metal tabanlı, avuç içi boyu — sayfa ölçüsünde raporlar çelişti,
    sayı yazılmaz)
  · bileğe yakın: KRONOGRAF — giysi kolunun ÜZERİNE, uzun cırt
    kayışla (kayış rengi ayrı bir renk çapasıdır: haki/gri-yeşil)
SAĞ KOL   okuma + ölçüm kolu
  · BİLEK AYNASI (göğüs panelinin ters yazısını okumak için)
  · analog BASINÇ GÖSTERGESİ / dozimetre (eldiven halkasına yakın)
```

Depo bible'ı asimetriyi kendi içinde kurar (YERÇEKİMİ: saat SAĞ
manşette, oksijen halkası SOL bilekte) — tarihsel konum zorunlu
değildir; **zorunlu olan, seçilen konumun her sahnede aynı yazılması**.

**Jenerik saat tanımları (marka yerine — §0①):**

| Tip | İngilizce kalıp | Kamera notu |
|---|---|---|
| Mekanik kronograf (klasik) | `a steel manual-wind chronograph with matte black dial and white baton hands, on a long fabric strap over the suit sleeve` | siyah/beyaz kontrast orta ölçekte bile okunur |
| Erken dönem / retro | `a small chrome chronograph with a silver-beige dial and slim gold hands` | düşük kontrast — yalnız yakın plan |
| Dijital (kabin içi) | `a square black resin digital watch, its LCD a dead grey blank` | ekran uzaktan ÖLÜ gri boşluktur; rakam tarif edilmez |

**Saatin dramatik işlevi (belgeli):** yörüngede güneş ~45 dakikada bir
doğup batar — saat gece/gündüz geçişini, kalan oksijeni ve görev fazını
sayar. "Kalan süre" sahnesi kadran/ibreyle kurulur, rakamla değil.

**Durmuş saat — anlatı yükünün fizik gerekçesi (belgeli):**

```
· MEKANİK saat vakumda durur: yağ buharlaşır (outgassing), çark
  kilitlenir; termal şokta ibre bükülüp takılabilir
· LCD ekran gölge soğuğunda DONAR ve kararır
· elektronik devre radyasyonla çöker (bit kayması / kalıcı arıza)
→ "its hands stopped" (YERÇEKİMİ) fiziksel olarak meşru bir çapadır;
  duran DİJİTAL saat ise kararmış/ölü ekran olarak yazılır
```

---

# 7. 🤖 AI DEVAMLILIK RİSK SINIFLARI

Deponun kendi ders kayıtlarıyla (metin bozulması D34/D45/D138, varlık
kayması) örtüştüğü için kural olarak alındı; sınıflamanın kendisi
ölçüm değil pratik önceliklendirmedir:

| Risk | Öğeler | Kural |
|---|---|---|
| DÜŞÜK — güvenilir çapa | kask küresi + altın vizör · sırt prizması · göğüs kutusu · 360° çevresel şerit · iki renkli köşegen sancak | bible'ın omurgası bunlardan kurulur; hacim kelimeleri kullan ("massive rectangular block") |
| ORTA — kısa planda | renk halkalı soketler · kask lambaları · yama üstü nokta/yıldız | SAYISINI yaz ve kilitle ("four box-shaped headlamps", "three gold dots") — pan'de sayı halüsinasyonu ① merceğine ölçülür |
| YÜKSEK — kaçın | serbest uçlu hortum/kordon · kolye zinciri · küçük etiket/ters yazı · okunur ekran | bible'a girmez; girecekse yalnız statik yakın planda ve iki ucu adlandırılmış hâlde. Metin yerine ışık soyutlaması |

---

# 8. 🧸 KİŞİSEL EŞYA SİSTEMİ

`KARAKTER_VE_DUYGU_KILAVUZU.md` §4.4 eşya sahnesinin BÜTÇESİNİ verir
(1-2 nesne · sürenin ≥%5'i · tekrar eden varlık [D58] · yıpranma sabit
[D42]). Bu bölüm eşyanın KENDİSİNİ verir.

**Üç tasarım ilkesi (rapor derlemesi):**
**SAYILABİLİRLİK** (karakter başına ≤2 eşya — fazlası dramatik etkiyi
sıfırlar) · **YÜKSEK KONTRAST** (beyaz giysi üzerinde ahşap, pirinç,
soluk pembe) · **ASİMETRİ** (tek bilekte, tek tarafta — endüstriyel
simetriyi bozan şey "insan" okunur).

**İki fizik kuralı (belgeli):**

```
① BASINÇLI ELDİVEN İNCE EŞYA TUTAMAZ. Şişirilmiş eldivende ince motor
  beceri sıfıra iner — yüzük, fotoğraf, ince bileklik EVA eldiveniyle
  zarifçe tutulamaz. İnce/duygusal eşya sahnesi → kabin içi, eldivensiz.
  EVA'da eşya ancak iri tutamaklı veya kordonlu taşınır.
② SERBEST EŞYA SAHNEDEN KAÇAR. Yerçekimsizlikte bırakılan nesne süzülür,
  havalandırma akımına kapılır, menfeze gider. Her eşya YA bağlıdır
  (tether/velcro/D-ring — bağın kendisi görsel çapadır) YA DA serbest
  bırakılışı bir SAHNE OLAYIDIR ve nereye gittiği yazılır.
```

**Eşya → duygu vuruşu eşlemesi (belgeli vakalar + 2 film örneği):**

| Eşya | Vuruş | Köken | İngilizce kalıp |
|---|---|---|---|
| Kordonlu peluş ("yerçekimi göstergesi") | umut · bağ · "yörüngedeyiz" anlatımı | Sovyet/Rus geleneği, bugün tüm programlarda; belgeli vakalar ham raporda | `a small worn stuffed toy floats on a thin tether above the console, spinning slowly` |
| Kontrol listesine iliştirilmiş çizim/fotoğraf | mizah · insanlık · veda | Apollo destek ekiplerinin karikatür geleneği | `a spiral-bound wrist checklist, one page holding a small hand-drawn cartoon` |
| D-ring'e asılı tılsım (yüzük, tespih, madalyon) | kayıp · özlem | astronotların kişisel kit geleneği | `a single brass medallion clipped by a short steel tether to the chest D-ring, drifting with each motion` |
| Küçük müzik aleti (mızıka, çan) | kardeşlik · yalnızlığın kırılması | ilk uzay müziği vakası (belgeli) | `a tiny silver harmonica tethered to the suit, floating beside three small brass bells` |
| Ay tozuna bırakılan çocuk bilekliği | veda · yas | ⚠️ KURGU (film sahnesi; gerçekliği varsayım) — benzer belgeli jest: yüzeye bırakılan aile fotoğrafı | `a faded pink bead bracelet dropping from a bulky glove into grey dust` |
| Yontulan ahşap nesne | pragmatizm · hayatta kalma | KURGU (film sahnesi) | `a small plain wooden object on a sterile metal bench, whittled at the base` |

```
□ Eşya karakter AYIRICI da olabilir: aynı giysili iki karakterden
  yalnız birinin bileğinde renkli iplik — tek kelimelik fark yeter
□ Eşyanın kimlik kartı (renk · boyut · doku · hasar YERİ) bible'a
  yazılır ve göç etmez [D42]
□ Duygu vuruşunun sahneye dağıtımı KARAKTER_VE_DUYGU §6 tablosundan
```

---

# 9. 📝 BIBLE'A İNDİRME REÇETESİ — altı adım

```
1. ROL ŞERİDİ seç (renk + LEFT/RIGHT konum) — §2 tablosu
2. SIRT SİLUETİ seç (A/B/C ayrımı) — §4; tek karakterde de yazılır
3. BİLEK DÜZENİNDEN 1 öğe seç (saat VEYA gösterge VEYA liste) — §6
4. KİŞİSEL EŞYA ≤1 seç ve KARAKTER_VE_DUYGU §6 bütçesine bağla — §8
5. Amblemden gerekeni ekle (uzak planda yalnız şerit yeter) — §3
6. Tek İngilizce blok yaz → uzunluğu ölç (KILAVUZ_REHBERI §7 bandı) →
   sığmıyorsa katman at, cümle KISALTMA (kelimesi kelimesine kural
   bozulur) → prompt_kontrol koş (Kart P)
```

**Örnek — iki karakterli mini blok (⭐ öneri, şablon):**

```
Commander: white pressure suit, a bold red stripe wrapped around the
RIGHT forearm and RIGHT thigh, flat smooth back with a single vertical
spine seam, a steel manual-wind chronograph with matte black dial on a
grey fabric strap over the LEFT sleeve.
Engineer: identical white pressure suit, a bright electric blue stripe
wrapped around the LEFT bicep and LEFT thigh, a massive rectangular
white life-support backpack with a U-shaped thruster frame below it,
bare wrists.
```

İki karakter dört eksende ayrışır (renk · taraf · sırt · bilek) ve
hiçbir eksen metin/marka/bayrak taşımaz.

---

# 10. 🔗 ÇAPRAZ REFERANSLAR

```
SAHNE_DEVAMLILIK_KILAVUZU §2      kelimesi kelimesine çapalama (kural)
KARAKTER_VE_DUYGU_KILAVUZU §4.4/6 eşya BÜTÇESİ ve sahne dağıtımı
UZAY_SENARYO_KILAVUZU             tür/dramaturji tarafı
POLITIKA_VE_URETILEBILIRLIK §2    kelime sözlüğü (milliyet/marka riski)
SES_VE_DIYALOG_URETIM_KILAVUZU    MACHINE register — warble AUDIO satırı
KILAVUZ_REHBERI §7                prompt uzunluk bandı + bilinen tuzaklar
04_ARASTIRMA_BULGULARI §TUR 5     bu kılavuzun kaynak ve süzme kaydı
```
