# 🗺️ YAPI GRAFİĞİ — Tek Bakışta Proje

> **Son eşitleme:** 31 Temmuz 2026 · dosya sistemiyle karşılaştırılarak
>
> ⚠️ **SAYI YAZMA KURALI.** Bu dosya artık "42 ders", "30 film" gibi sabit
> sayı taşımaz. Sayılar haftada birkaç kez değişiyor ve altı ayrı belgeye
> elle kopyalandığı için hiçbiri doğru kalmadı. Bunun yerine **kaynağa işaret
> edilir.** Bir sayıya ihtiyacın varsa kaynağı aç:
>
> ```
> kaç ders var        → LESSONS_LEARNED.md
> kaç film ölçüldü    → FILM_QA_RAPORLARI/00_INDEX.md   ← tek doğru sayaç
> kaç film var        → FILM_QA_RAPORLARI/00_INDEX.md
> ```
>
> Bu dosyaya sayı eklersen bir sonraki hafta yalan söylemeye başlar.

---

## 1. KARAR AĞACI — Sırayla Sor

```
                         BİR FİLM
                             │
  ①  YÖN?  ──────────────────┴──────────────────┐
     │                                          │
  DİKEY (9:16)                              YATAY (16:9)
     │                                          │
     ▼                                          │
  SHORTS                                        │
  6 sahne × 8s = 48 sn          ②  SÜRE? ───────┼───────┬───────────┐
  süre seçimi YOK — sabit                       │       │           │
  (dal burada biter)                          2-4 dk  3-5 dk     7-9 dk
                                             12-13 sh  25 sh      60 sh
                                              ~2:00    4:09       8:00
                                                │       │           │
                                                └───────┴─────┬─────┘
                                                              │
                                       ③  TÜR? ──────────────┤
                                              │
                                        │
                                   BİLİMKURGU                (⏸️ RAFTA: zombi
                                        │                     §4.2 ve savaş §4.3.
                                        ▼                     Zombi 26.08.2026'da
                                 ④  ORTAM? (seçim)            kapandı — depo
                          ┌────────┼────────┐                 yalnız UZAY.
                       vakum     ince     Dünya               Kartlar duruyor,
                                 atm.      atm.               klasörler yok.)
```

> ⚠️ **③ TÜR sorusunun bugün tek cevabı var: BİLİMKURGU.** Dal 26.08.2026'da
> teke indi (kart H2). Karar ağacında bu adım şimdilik bir seçim değil, bir
> doğrulama: "bu gerçekten bir uzay filmi mi?" Değilse konsept reddedilir.

### Neden bu sıra?

```
① YÖN    → Her şeyi belirler. Dikey seçersen dal orada biter:
           shorts formatı sabittir, süre sorusu yoktur.
② SÜRE   → YAPIYI belirler: kaç sahne, kaç dosya, klip süresi,
           text-to-video mi start/end frame zinciri mi.
③ TÜR    → İÇERİĞİ belirler: hangi kilitler, hangi kurallar iptal,
           hangi politika riski.
④ ORTAM  → FİZİĞİ belirler. Bilimkurguda gerçek bir seçimdir (vakum /
           ince atm. / Dünya atm.). Karasal türler (zombi · savaş) hep
           Dünya atmosferiydi ama ikisi de RAFTA — 26.08.2026'dan beri
           bu soru yalnız bilimkurgu içinde sorulur.
```

> **Pratik sonuç:** Bilimkurgu ortamına göre üçe ayrılır ve fizik kuralları
> ters dönebilir (bkz. Bölüm 6). Karasal türlerin ortak fiziği (toz çöker,
> gölge yumuşak, ses normal) Bölüm 3.3'te durur — savaş rafta olsa da zombi
> ve diğer günümüz-Dünya konseptleri bu fiziği kullanmaya devam ediyor.

---

## 2. KLASÖR AĞACI

> Film listesi burada tutulmaz — değişiyor ve iki yerde tutulursa ayrışıyor.
> Tam liste ve ölçüm durumu: `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/00_INDEX.md`

```
kısafilmler/
│
├── dikey_shorts_filmler/          9:16 · 6 sahne × 8s · 48 sn · text-to-video
│                                  film başına KLASÖR (25.08.2026)
│                                  ⚠️ içinde 16:9 "YATAY_SHORTS" filmleri de var
│                                  ⛔ 3 dosya var; bu grafiğin eski sürümü 5
│                                     sayıyordu — GLASS_WORLD ve LAST_ARCHIVE
│                                     shorts dosyaları diskte YOK. Paletlerde
│                                     adı geçen COUNTING_RAIN ve REMEMBERING_DUST
│                                     shorts'ları da hiç yok. Durum ve güvenli
│                                     alan kuralları: dikey_shorts_filmler/00_README.md
│
├── yatay_2_4_dk_filmler_uzay/     16:9 · 12-13 sahne × 10s · ~2:00-2:10
│                                  film başına KLASÖR (25.08.2026)
│
│   (yatay_2_4_dk_filmler_zombi/ — 26.08.2026'da kart H2 ile KALDIRILDI,
│    tür de kapandı. Depo yalnız UZAY filmleri içindir. İkinci kaldırılış:
│    12.08'de silinmiş, 23.08'de geri açılmıştı.)
│                                     Türün açılış şartı bir BÜTÇEDİR —
│                                     klasörün 00_README.md'sinde yazılı
│
├── yatay_3_5_dk_filmler/          16:9 · 25 sahne × 10s · 4:09
│                                  film başına KLASÖR (PLAN+PART_A+PART_B+KAPAK)
│
├── yatay_7_9_dk_filmler/          16:9 · 60 sahne × 8s · 8:00
│   └── kilavuzlar/                start/end frame zinciri + 3 geçişli QA
│                                  (bu formatın kendi kılavuz seti burada)
│
├── yatay_10_20_dk_filmler/        ⚠️ sadece README — henüz film yok
│
└── kilavuzlar_ve_sistem_dosyalari/  → Bölüm 4
```

```
⚠️ İKİ BİLİNEN YAPISAL BORÇ

1. TÜR, KLASÖR ADINA YAPIŞTIRILMIŞ  (_uzay)
   Ölçeklenmiyor: 3-5 dk'ya ikinci bir tür eklersen yeni klasör gerekecek.
   Doğrusu tür etiketini dosya içinde tutmak. Şimdilik dokunulmadı —
   KILAVUZ_REHBERI mantıksal ayrımı zaten kuruyor. (12.08.2026: _zombi ve
   _savas klasörleri kaldırıldı. 23.08.2026: _zombi geri açıldı.
   26.08.2026: _zombi TEKRAR kaldırıldı ve tür kapandı — geriye tek tür
   kaldığı için borç şimdilik ödendi: `_uzay` soneki artık tek türü değil
   TÜM depoyu tarif ediyor. ⚠️ İkinci tür geri gelirse borç da geri gelir;
   doğru çözüm hâlâ tür etiketini DOSYA İÇİNDE tutmak.)

2. DOSYA vs KLASÖR TUTARSIZ
   HER format       → film başına KLASÖR (25.08.2026: 2-4 dk ve shorts
                      da tek dosyadan klasöre geçti — artık istisna yok)
   Kural şu: sahne sayısı 13'ü geçtiğinde klasöre geçilir. Yazılı değildi.
```

---

## 3. FİLM DURUMU — burada tutulmaz

> Eskiden bu bölümde bir "film matrisi" vardı. Silindi: `00_INDEX.md` ile
> ayrıştı ve ikisi farklı şey söylemeye başladı. **Tek sayaç kalsın.**

```
Hangi filmler var, hangisi ölçüldü, hangi skoru aldı, hangi ders nereden çıktı
  → FILM_QA_RAPORLARI/00_INDEX.md

Yeni film yazarken şablon arıyorsan
  → format kartı: KILAVUZ_REHBERI.md Bölüm 2
  → referans film: KILAVUZ_REHBERI.md Bölüm 1'deki "formata göre ek okuma"
```

---

## 4. KILAVUZ HARİTASI — katmanlara göre

```
kilavuzlar_ve_sistem_dosyalari/
│
├── 🧭 NAVİGASYON — buradan başla
│   ├── KILAVUZ_REHBERI.md ............... hangi filmde ne okunur (ADRES verir)
│   └── YAPI_GRAFI.md .................... bu dosya (YAPIYI gösterir)
│
├── 📚 ÇEKİRDEK KILAVUZ — her filmde geçerli
│   ├── LESSONS_LEARNED.md ............... ders DİZİNİ + teknik kalite tablosu
│   ├── DERSLER/ ......................... ders metinleri (9 tematik dosya
│   │                                      + hızlı referans bloğu)
│   ├── VEO_3_1_FAST_..._KILAVUZU.md ..... araç davranışı, tırnak sentaksı
│   ├── SAHNE_DEVAMLILIK_KILAVUZU.md ..... karakter çapalama, seed
│   ├── SINEMATOGRAFIK_TEKNIK_KILAVUZ.md . kamera sözlüğü · §17 karar tablosu
│   ├── SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md  vuruş haritası (§2, sahne
│   │                                      haritasından ÖNCE) + loop
│   │                                      + kamera psikolojisi (06.08.2026)
│   ├── HOOK_VE_ILK_SAHNE_KILAVUZU.md .... S0 karar + S1 tırmandırma,
│   │                                      hook tipolojisi, ses kancası,
│   │                                      hook-önce üretim kapısı (09.08.2026)
│   ├── FRAGMAN_KILAVUZU.md .............. iki formatlı teaser: dikey 3-6
│   │                                      vuruş · yatay 8-12 vuruş, spoiler
│   │                                      kapısı, tek mekanik (12.08.2026)
│   ├── TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md  klipler ARASI geçiş
│   │                                      (Ders 1 klip İÇİNİ kapsar)
│   ├── KURGU_VE_TESLIM_KILAVUZU.md ...... birim sözlüğü + 10 maddelik
│   │                                      kurgu kapısı + kırpma bütçesi
│   │                                      (21.08.2026 — beş dosyadan
│   │                                      konsolide, tek adres)
│   ├── SES_VE_DIYALOG_URETIM_KILAVUZU.md  replik/ses YAZIM tarafı:
│   │                                      register haritası + AUDIO
│   │                                      kalıpları (21.08.2026)
│   ├── KARAKTER_VE_DUYGU_KILAVUZU.md .... izleyici bağını kuran bütçeler:
│   │                                      göz · Kuleshov döngüsü · el ·
│   │                                      nefes · yürüyüş · eşya
│   │                                      (22.08.2026 — sahne haritasına
│   │                                      dağıtılır, sonradan eklenemez)
│   ├── KURGU_RITMI_VE_IHRAC_KILAVUZU.md . ASL eğrisi (KAYNAK) · örüntü
│   │                                      kırıcı · J/L-cut ses köprüsü ·
│   │                                      ihraç sayıları (22.08.2026)
│   │                                      ⚠️ KURGU_VE_TESLIM = KAPI,
│   │                                         bu dosya = KAYNAK
│   ├── TEMA_MUHENDISLIGI_KILAVUZU.md .... tema seçimi · tema→motif→sahne
│   │                                      matrisi · süre-tatmin kuralı ·
│   │                                      olay filmi teşhisi (22.08.2026)
│   ├── KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md  8 açının anlam sözlüğü ·
│   │                                      vuruş→açı karar tablosu ·
│   │                                      abartı/kiç eşikleri (22.08.2026)
│   ├── ACI_YAYI_VE_SEKANS_KILAVUZU.md ... sahneden sahneye açı/ölçek
│   │                                      sıçrama bandı · kurulum sayısı ·
│   │                                      yay şablonları (22.08.2026)
│   ├── MESHUR_SAHNE_KALIPLARI_KILAVUZU.md 20 ikonik sahne kalıbı ·
│   │                                      taşınabilirlik · homage/telif
│   │                                      sınırı (22.08.2026)
│   ├── ONERME_VE_NOVUM_KILAVUZU.md ...... KONSEPT kapısı: novum tipi ·
│   │                                      taşıyıcı (nesne × jest) · üç
│   │                                      kabul testi (22.08.2026)
│   │                                      ⚠️ vuruş tablosundan ÖNCE koşar
│   ├── FINAL_VE_PAYLASIM_KILAVUZU.md .... final tipi → davranış · tohum
│   │                                      bilgi %10-15 · görsel ikilem
│   │                                      (22.08.2026 — hook'un karşı ucu)
│   └── PAKETLEME_VE_VAAT_KILAVUZU.md .... kapak ANI senaryoda seçilir ·
│                                          vaat-teyit penceresi · dört
│                                          yüzeyli spoiler bütçesi [D114]
│                                          (22.08.2026)
│
├── 📱 FORMATA GÖRE
│   └── DIKEY_MIKRO_DRAMA_KILAVUZU.md .... 9:16 dramaturjisi: 6×8 vuruş
│                                          tablosu · Z-ekseni · kinesik
│                                          reset · bağımsızlık kuralı
│                                          (22.08.2026 — SHORTS_SISTEM_
│                                          PROMPTU'ndan ÖNCE okunur)
│
├── 🎭 TÜRE GÖRE
│   ├── UZAY_SENARYO_KILAVUZU.md ......... bilimkurgu
│   ├── SAVAS_SENARYO_KILAVUZU.md ........ savaş (tür ⏸️ rafta; dikey
│   │                                      THE_DULL_EDGE kullanmaya devam eder)
│   └── ⛔ ZOMBİ KILAVUZU YOK ............ sadece KILAVUZ_REHBERI §4.2 kartı
│
├── 📝 YAPIŞTIRILACAK PROMPTLAR (kılavuz değil, GİRDİ)
│   ├── IMAGE_VIDEO_PROMPT_TEMPLATES.md .. V2 prompt şablonu
│   ├── SHORTS_SISTEM_PROMPTU.md ......... dikey 9:16 sistem promptu
│   └── VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md  paketleme
│       ⚠️ Üçü de kökte duruyor ama QA promptları ayrı klasörde.
│          Aynı ayrımın iki tarafında — birleştirilmeli.
│
├── 🔬 PROMPT_KONTROL/ ................... üretimden ÖNCE koşan sıfır maliyetli kapı
│   ├── prompt_kontrol.py ................ sayar: uzunluk · yasak kelime ·
│   │                                      çekirdek imzası · GO/FIX/BLOCK
│   │                                      (akıştaki yeri: REHBER §6 adım 3.5)
│   ├── PROMPT_QA_CRITIQUE_PROMPT.md ..... yargılar: kilit SAYI mı TARİF mi
│   └── RAPORLAR/ ........................ koşu raporları
│
├── 🔮 URETIM_ONCESI_ANALIZ/ ............. para harcanmadan önce bakan tek yer
│   ├── 00_README.md ..................... akıştaki yeri + dürüstlük kuralı
│   ├── 01_DERS_ETKINLIK_RAPORU.md ....... hangi ders çalışıyor — kanıtla
│   ├── 02_RISK_KARTLARI.md .............. "filmde su var" → ne bozulacak
│   └── 03_PLAN_ONCESI_KONTROL_LISTESI.md  planı üretime sokmadan tara
│
├── 🔍 QA_PROMPTLARI/ .................... üretilmiş işin eleştirisi
│   │                                      ⭐ rubrikler SALT PROMPT (12.08.2026)
│   ├── 00_README.md ..................... klasör rehberi + ajan akışı
│   ├── CALISTIRMA_KAYITLARI.md .......... koşu tarihçesi + ders dipnotları
│   ├── FILME_OZEL/ ...................... film-özel üretim kapıları
│   ├── ARSIV_6_MERCEK/ .................. ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ
│   ├── 1_KARE_QA_....md ................. ① sahne içi · yatay VEYA dikey
│   │                                      (FORMAT: DİKEY → 9:16 · güvenli
│   │                                       alan · kanca kategorileri açılır)
│   ├── 2_DEVAMLILIK_QA_....md ........... ② sahneler arası · dünya + gövde
│   │                                      (yalnız video · 13 kategori)
│   ├── 3_SES_QA_....md .................. ③ konuşmacı atfı + sentetik ses
│   │                                      (yalnız TAM KURGU — tek klibe koşulmaz)
│   └── 4_HIKAYE_QA_....md ............... ④ dramaturji (+PLAN = MOD D ·
│                                          yalnız video = MOD V, satır Ⓥ)
│
├── 📊 FILM_QA_RAPORLARI/ ................ QA çıktıları — TEK SAYAÇ
│   ├── 00_INDEX.md ...................... ⭐ film listesi + ölçüm durumu
│   ├── 01_FILM_RAPORLARI/ ............... film başına QA kaydı
│   ├── 02_HAM_RAPORLAR/ ................. ham çıktı, özetlenmemiş
│   ├── T1_KARE_KALITE.md ................ ① skorları        ⭐ CANLI
│   ├── T2_DEVAMLILIK_KALITE.md .......... ② skorları        ⭐ CANLI
│   ├── T3_SES_KALITE.md ................. ③ skorları        ⭐ CANLI
│   ├── T4_HIKAYE_KALITE.md .............. ④ skorları        ⭐ CANLI
│   ├── 03_ 04_ 05_ 06_ 07_ .............. ⛔ KAPALI (22.08) — eski 6 mercekli
│   │                                      sistemin skorları, yeni satır YAZILMAZ
│   └── 08_YAYIN_PERFORMANS_TABLOSU.md ... ⭐ gerçek izleyici koşuları
│                                          (22.08.2026 — yukarıdaki altısını
│                                          bir MODEL doldurur, bunu VERİ
│                                          doldurur; çakışırsa bu üstündür)
│
└── 🎨 YAYIN
    ├── KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md  thumbnail psikolojisi
    ├── GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md  müzik · §7-19 kuram ve künye
    ├── SERI_VE_KANAL_STRATEJI_KILAVUZU.md .. evren modeli · kapak aile
    │                                         kimliği · playlist · kadans ·
    │                                         devam hakkı eşikleri (22.08.2026)
    └── YAYIN_VE_PERFORMANS_KILAVUZU.md ..... ⭐ AKIŞIN SON ADIMI: karar
                                              matrisi · sinyal/gürültü ·
                                              retention eğrisi → SAHNE ·
                                              gerçek veri → kılavuz
                                              revizyonu (22.08.2026)

FORMATA ÖZEL — kendi klasöründe durur
└── yatay_7_9_dk_filmler/kilavuzlar/
        ├── 5_FAZ_MIMARISI.md
        ├── FAZ_DOSYASI_SABLONU.md
        ├── KESINTISIZ_VIDEO_URETIM_TEKNIGI.md
        └── kalite_kontrol/ ............... 3 geçişli QA sistemi
                ⚠️ QA_2 (devamlılık) ile QA_PROMPTLARI/MANTIK_QA aynı hata
                   sınıfına bakıyor, iki farklı isimle. Ders numarası
                   çakışması riski duruyor.
```

---

## 5. ÜRETİM AKIŞI VE ÜÇ MERCEK

```
  PLAN         BIBLE        PROMPT       ÜRETİM              DEĞERLENDİR         YAYIN
   │             │            │            │                      │                │
konsept  ──► world/char ──► image+   ──► imaj ──► video ──┬── VIDEO_QA    ──►  kapak
tema         ortam/tür      video                        │   kare içi          başlık
sahne        negatif        self-                        ├── MANTIK_QA          açıklama
haritası     çekirdek       contained                    │   sahneler arası
                            ~2.500 krktr                 └── SENARYO_QA
                                                             dramatik
                                                                │
                                                          yeni ders
                                                                │
                                                        LESSONS_LEARNED
                                                            (döngü)
```

### Üç mercek neyi görür, neyi göremez

```
VIDEO_QA      TEK KLİP içi        girdi: video + SPEC
              → sahneler arası kaymayı GÖREMEZ, tek klibe bakıyor

MANTIK_QA     SAHNELER ARASI      girdi: yalnız video (tek mod)
              → "planlanan sahne eksik" DİYEMEZ, planı yok
              → çözemediğini FLAGS altına SORU yazar

SENARYO_QA    DRAMATİK            girdi: video (+PLAN varsa MOD D)
              → tozlu suit'in temizlenmesini SORUN SAYMAZ
```

> **İki girdi modu (05.08.2026):** altı rubrik de tek dosya çalışır.
> MOD D = SPEC/plan verildi, uygunluk ölçülür · MOD V = sadece video,
> film kendisiyle+fizikle ölçülür, belge isteyen denetim SORUYA döner.
> Mod V skorları tabloya `Ⓥ` işaretiyle girer.
> Ayrıntı: `QA_PROMPTLARI/00_README.md`

> **Kapsam sınırı blokları silinmemeli.** Üç raporun aynı hatayı üç kez
> saymadan birleştirilebilmesinin tek garantisi odur.

```
ÖLÇÜM KAPSAMI
   Ölçülüyor:    prompt sonrası video (3 mercek) · dikey · kapak
   Ölçülmüyor:   müzik · ses miksi · başlık paketi
                 (bilinçli beklemede — görüntü 3-5/10 bandındayken sıra
                  onlarda değil)
   KAPSAM DIŞI:  Bible tutarlılığı · anahtar kare · yayın sonrası veri
                 (05.08.2026 — ilk ikisi GİRDİYİ ölçer, oysa VIDEO_QA ve
                  MANTIK_QA zaten SONUCU ölçüyor; üçüncüsü analitik, QA
                  değil. Gerekçe: QA_PROMPTLARI/00_README §KAPSAM DIŞI)
   Güncel liste: QA_PROMPTLARI/00_README.md kapsam haritası
```

---

## 6. ORTAM FİZİĞİ — TERS DÖNEN KURALLAR

```
                    VAKUM           İNCE ATM.      DÜNYA ATM.     🆕 KALIN ATM.
                    (ay, uzay)      (Mars, %0.6)   (günümüz-Dünya) (3-5 atm)
──────────────────────────────────────────────────────────────────────────────
Toz                 yükselir,       yavaş çöker,   hızlı çöker    çok hızlı çöker
                    ÇÖKMEZ          yere oturur    yere oturur    ve KÜMELENİR
Gölge               MUTLAK SİYAH    yumuşak        yumuşak        yumuşak ama DERİN
Dolgu ışığı         YOK             VAR            VAR            ÇOK GÜÇLÜ
Dış ses             YOK             boğuk, zayıf   normal         GÜÇLÜ ve ALÇAK
Egzoz/duman         düz koni        yayılır,çöker  kıvrılır       KISA ve KALIN
Rüzgar kuvveti      yok             yok denecek    var            var ama yavaş
Kaldırma kuvveti    yok             ihmal          ihmal          ⭐ GERÇEK (yüzme)
──────────────────────────────────────────────────────────────────────────────
🆕 3.5 VAKUM + İTKİ (yanan geminin yanı):  3.1 tablosunun aynısı, tek fark —
   SÜZÜLME YOK: her serbest cisim kıça doğru düşer, D23 TETİKLENEMEZ.
🆕 3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK (Venüs 55 km):  toz YOK · gölge YOK ·
   bağıl rüzgâr 0 · kaldırma GERÇEK · güneş diski görünmez. D39 elenir.

İlgili dersler:     36, 39, 41 → HER BİRİNİN CEVABI ORTAMA GÖRE DEĞİŞİR
                    Kalın atmosferde 36 ve 39 TERSİNE döner.
Referans filmler:   DEAD_APPROACH · LOW_POWER · THE_HERD · UPHILL_DARK ·
                    LOSS_OF_LIFT  (LAST_ROAD 12.08.2026'da silindi)
```

> Ders 41 kendi içinde şunu yazıyor: *"Vakum filmlerinde bu ders GEÇERSİZDİR."*
> Ders 39: *"Ortama göre değişir — tek bir doğru yok."*
> Bu yüzden ortam, tür kadar önemli bir eksen.

---

## 7. BU DOSYAYI GÜNCELLERKEN

```
□ Sayı yazma. Kaynağa işaret et. (Bölüm 0'daki kural)
□ Film listesi ekleme. 00_INDEX.md'de duruyor.
□ Yeni klasör açılınca Bölüm 2 ve 4'e satır ekle
□ Yeni QA rubriği yazılınca Bölüm 4 ve 5'e ekle
□ Değişiklikten sonra dosya sistemiyle karşılaştır:
    ls -1 <her film klasörü>  →  Bölüm 2 ile uyuşuyor mu
    ls -1 kilavuzlar_ve_sistem_dosyalari/  →  Bölüm 4 ile uyuşuyor mu
□ Başlıktaki "Son eşitleme" tarihini güncelle
```

> **Neden bu bölüm var:** Bu dosya 31.07.2026'da dosya sistemiyle
> karşılaştırıldığında yedi ayrı yerde yanlıştı — var olmayan iki film
> listeliyor, iki klasörü hiç görmüyor, bir klasörün adını yanlış yazıyor,
> ders sayısını sekiz eksik sayıyordu. Haritanın yanlış olması, hiç harita
> olmamasından kötüdür.
