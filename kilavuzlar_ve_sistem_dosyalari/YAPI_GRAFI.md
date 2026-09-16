# 🗺️ YAPI GRAFİĞİ — Tek Bakışta Proje

> **Son eşitleme:** 31 Temmuz 2026 · dosya sistemiyle karşılaştırılarak
> (13.09.2026: yalnız §1 karar ağacı + §2 klasör ağacına 6/8 dk satırları eklendi; tam eşitleme yapılmadı)
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
  6 sahne × 8s = 48 sn          ②  SÜRE? ──┬───────┬───────┬───────┬───────────┐
  süre seçimi YOK — sabit                  │       │       │       │           │
  (dal burada biter)                     2 dk    4 dk    6 dk    8 dk     7-20 dk
                                         12 sh   24 sh   36 sh   48 sh    48-144 sh
                                         2:00    4:00    6:00    8:00     8:00-20:00
                                        ─── 12-SAHNE MODÜL MERDİVENİ ───  (FAZ hattı ·
                                        (13.09.2026 · yazım hepsinde aynı;   7 fazın
                                         6/8 dk'da QA birimi BÖLÜM = iki    üstünde
                                         yarım master × 12 mercek)          PERDE)
                                           │       │       │       │           │
                                           └───────┴───────┴───────┴─────┬─────┘
                                        ⚠️ 8 dk'da iki hat: MODÜL (48 sh · 2 bölüm ·
                                           yatay_8_dk_filmler) ↔ FAZ (5 faz · 10_20).
                                           Seçim mimariye göre, süreye göre değil.
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
├── yatay_2_dk_filmler/            16:9 · 12 sahne × 10s · 2:00 (13.09.2026 modül
│                                  beyanı — merdivenin ilk basamağı; 13-18
│                                  sahneli eski filmler olduğu gibi)
│                                  🔁 13.09.2026'ya kadar `yatay_2_4_dk_filmler_uzay/`
│                                  — "2-4 dk" = bu formatın eski adı
│                                  film başına KLASÖR (25.08.2026)
│
│   (yatay_2_4_dk_filmler_zombi/ — 26.08.2026'da kart H2 ile KALDIRILDI,
│    tür de kapandı. Depo yalnız UZAY filmleri içindir. İkinci kaldırılış:
│    12.08'de silinmiş, 23.08'de geri açılmıştı.)
│                                     Türün açılış şartı bir BÜTÇEDİR —
│                                     klasörün 00_README.md'sinde yazılı
│
├── yatay_4_dk_filmler/            16:9 · 24 sahne × 10s · 4:00 (13.09.2026 modül
│                                  beyanı; 25'li eski filmler olduğu gibi)
│                                  🔁 13.09.2026'ya kadar `yatay_3_5_dk_filmler/`
│                                  — "3-5 dk" = bu formatın eski adı
│                                  film başına KLASÖR
│
├── yatay_6_dk_filmler/            🆕 13.09.2026 · 16:9 · 36 sahne × 10 s · 6:00 · 2 × 18
│                                  yazım 3-5 dk ile aynı · ⭐ QA birimi BÖLÜM:
│                                  iki yarım master × 12 mercek = 24 rapor ·
│                                  rapor_kontrol.py --bolum n/2 · KILAVUZ_REHBERI §2.6
│
├── yatay_8_dk_filmler/            🆕 13.09.2026 · 16:9 · 48 sahne × 10 s · 8:00 · 2 × 24
│                                  aynı kural · §2.7 · ⚠️ faz hattı DEĞİL —
│                                  THE_SLOW_STONE 10_20'de kalır
│
│   ⭐ 01.09.2026 — YENİ FİLMLERDE KLASÖR İSKELETİ HER FORMATTA AYNI:
│      PLAN · BOLUM_1 · BOLUM_2 · KAPAK · MUZIK · YAYIN_PAKETI · QA_SPEC
│      (+ REFERANS_PAKETI — REFERANS_PAKETI_KILAVUZU §1'in altı
│       tetikleyicisinden biri doğruysa; KAPI 0, promptlardan ÖNCE)
│      Tanım: KILAVUZ_REHBERI §2.0 · kopya: FILM_KLASOR_SABLONU/
│      (eski filmler olduğu gibi kalır; yeniden bölünmez)
│   ⭐ 14.09.2026 — İKİ REJİM (reform · TODO_AKIS_VE_DERS_REFORMU.md):
│      00_ANALIZ/00_HIKAYE_ONAYI.md taşıyan klasör = YENİ REJİM →
│      prompt_kontrol ㉕-㉚ (kilit ≤20 · IN FRAME · NEGATIVE ≤11 cümle ·
│      çizelge sahtelik · hikâye onayı · sahne tablosu) + kelime bandı.
│      14.09'dan önce açılan 26 üretilmemiş film ESKİ kapılarla kalır;
│      film_klasoru_ac.sh --analiz-ekle onayı kopyalamaz (sahip kararı).
│
├── yatay_10_20_dk_filmler/        16:9 · 3 perde · bant 7-20 dk
│                                  (04.09.2026: yatay_7_9_dk_filmler/
│                                  kaldırıldı, bandın kısa ucu buraya
│                                  katıldı — THE_SLOW_STONE 48×10s·8:00)
│                                  ⚠️ üç filmden yalnız THE_SLOW_STONE
│                                  üretildi (QA 5/10); YERÇEKİMİ ve
│                                  THE_SECOND_SHIP yazıldı, üretilmedi
│                                  (05.09.2026: dikey_20_25_dk_filmler/
│                                  açıldığı gün kaldırıldı — depoda dört
│                                  film klasörü var, beşincisi yok)
│
└── kilavuzlar_ve_sistem_dosyalari/  → Bölüm 4
    (05.09.2026: film_analizleri/ kaldırıldı — dış film analiz hattı
     kapandı; kurtarılan metodoloji → DIS_FILM_ANALIZI/, Bölüm 4)
```

```
⚠️ İKİ BİLİNEN YAPISAL BORÇ

1. ✅ ÖDENDİ 13.09.2026 — TÜR, KLASÖR ADINA YAPIŞTIRILMIŞTI  (_uzay)
   Klasör `yatay_2_dk_filmler/` oldu; tür soneki düştü, tür artık yalnız
   KILAVUZ_REHBERI §4'te (dosya içinde) yaşar. Aşağıdaki kayıt tarihtir.
   Ölçeklenmiyordu: 3-5 dk'ya ikinci bir tür eklersen yeni klasör gerekecekti.
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

3. 🆕 14.09.2026 — İKİ REJİM AYNI DEPODA
   Eski klasör (00_HIKAYE_ONAYI yok) eski bantla, yeni klasör yeni kapılarla
   denetlenir; aynı betik, iki kural seti (prompt_kontrol.py rejim()).
   Bilinçli borç: 26 üretilmemiş eski filmden biri üretime girecekse sahip
   ya eski bantla üretir ya dosyayı şablondan kopyalayıp yeni rejime alır —
   arası yok. Borç, eski filmler üretilip/emekli edilince kendiliğinden kapanır.
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
│   │   ├── 00_YASAYAN_DERSLER.md ........ ⭐ 14.09.2026 · yeni filmin okuduğu
│   │   │                                  TEK liste (≤40 · ETİKET · DEĞİŞEN SATIR)
│   │   ├── 00_DERS_YAZIM_KONTRATI.md .... §2b film dersi = FREKANS ≥2 film +
│   │   │                                  DEĞİŞEN SATIR + KAPI + TEKRAR (14.09)
│   │   └── 00_HIZLI_REFERANS.md ......... arşiv kilit havuzu (çekirdek okuma değil)
│   ├── VEO_3_1_FAST_..._KILAVUZU.md ..... araç davranışı, tırnak sentaksı
│   ├── SAHNE_DEVAMLILIK_KILAVUZU.md ..... karakter çapalama, seed
│   ├── REFERANS_PAKETI_KILAVUZU.md ...... KAPI 0: hangi varlık kendi
│   │                                      referans sayfasını hak eder,
│   │                                      durum merdiveni, sayfa kanonu,
│   │                                      sahne→referans eşleme, kabul
│   │                                      kapısı (06.09.2026 · D146)
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
├── 🗂️ FILM_KLASOR_SABLONU/ .............. film klasörü iskeletinin KOPYASI
│   │                                      7 dosya taslağı · `cp -r` hedefi
│   │                                      tanım: KILAVUZ_REHBERI §2.0
│   └── 00_ANALIZ/ ....................... 14.09.2026: 00_HIKAYE_ONAYI.md (sahip
│                                          onayı · YENİ REJİM işareti · ㉙) ·
│                                          OKUMA_CEKIRDEGI.txt (TUR 2/3 manifesti,
│                                          ≤30 dosya) · 05_/00_SAHNE_TABLOSU.md
│                                          (>8 sahnede satır başına sahne · ㉚)
│
├── 🔬 PROMPT_KONTROL/ ................... üretimden ÖNCE koşan sıfır maliyetli kapı
│   ├── prompt_kontrol.py ................ sayar: uzunluk · yasak kelime ·
│   │                                      çekirdek imzası · GO/FIX/BLOCK
│   │                                      ⭐ KLASÖR MODU: film klasörü verilir,
│   │                                      bölümler birleşir (01.09.2026)
│   │                                      (akıştaki yeri: REHBER §6 adım 3.5)
│   │                                      ⭐ 14.09.2026 İKİ REJİM: 00_HIKAYE_ONAYI
│   │                                      olan klasörde kelime bandı (pozitif gövde)
│   │                                      + ㉕-㉚; eski klasör eski bant. Sabitler
│   │                                      betiğin başında (KELIME_BANDI · KILIT_TAVANI …)
│   ├── PROMPT_QA_CRITIQUE_PROMPT.md ..... yargılar: kilit SAYI mı TARİF mi
│   └── RAPORLAR/ ........................ koşu raporları
│
├── 🔮 URETIM_ONCESI_ANALIZ/ ............. para harcanmadan önce bakan tek yer
│   ├── 00_README.md ..................... akıştaki yeri + dürüstlük kuralı
│   ├── 01_DERS_ETKINLIK_RAPORU.md ....... hangi ders çalışıyor — kanıtla
│   ├── 02_RISK_KARTLARI.md .............. "filmde su var" → ne bozulacak
│   ├── 03_PLAN_ONCESI_KONTROL_LISTESI.md  planı üretime sokmadan tara
│   ├── 04_ARASTIRMA_BULGULARI.md ........ TUR n süzme kaydı — kuralın kaynağı
│   ├── 07-22_*_ARASTIRMA_PROMPTLARI.md .. derin araştırma promptları (salt prompt)
│   │                                      22_ = sahne doluluğu (TUR 19 ✅ → SAHNE_DOLULUGU_KILAVUZU · 15.09.2026)
│   └── TURn_HAM_RAPORLAR/ ............... koşulan promptların ham raporları
│
├── 🔍 QA_PROMPTLARI/ .................... üretilmiş işin eleştirisi
│   │                                      ⭐ rubrikler SALT PROMPT (12.08.2026)
│   ├── 00_README.md ..................... klasör rehberi + ajan akışı
│   ├── CALISTIRMA_KAYITLARI.md .......... koşu tarihçesi + ders dipnotları
│   ├── _KAYNAK/ ......................... ⭐ ON BEŞ RUBRİK — OPERATÖRÜN AÇTIĞI YER
│   │                                      13_UYUM = sahne ↔ PROMPT (⑬ · 11.09.2026)
│   │                                      14_HAREKET · 15_YON = hareket mantığı ·
│   │                                      yön/hedef (⑭⑮ · 14.09.2026 · henüz koşu yok)
│   │                                      yanına <FILM>_QA_SPEC.md yapıştırılır = mod D [D129]
│   │                                      (FILME_OZEL/ paketleri 11.09.2026'da silindi)
│   ├── ARSIV_6_MERCEK/ .................. ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ
│   ├── ARSIV_RUBRIK_DIYETI/ ............. ⛔ 14.09.2026 diyet-öncesi altı rubrik
│   │                                      + kesilen metinler — ÇALIŞTIRILMAZ
│   ├── ARSIV_CIKTI_KURALLARI.md ......... ortak çıktı kalıbının uzun hâli (tek kopya)
│   ├── _KAYNAK/1_KARE_DIKEY_EK.md ....... ① dikey ek — yalnız dikey filmde sona
│   │                                      yapıştırılır (rubrik tavanı 25 KB · sayac)
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
├── 🎞️ DIS_FILM_ANALIZI/ ................. ⛔ HAT KAPALI (05.09.2026) —
│   │                                      film_analizleri/ kaldırıldı, kart
│   │                                      H2 ③ gereği kurtarılanlar burada
│   ├── 00_README.md ..................... hattın durumu + akış (yeniden
│   │                                      açılırsa koşulacak tarif)
│   ├── KAMERA_/OLAY_/TEMA_/SENTEZ_ANALIZ_PROMPT.md  salt promptlar
│   └── NOBODY_WAS_ALIVE_DERS_SECKISI.md . ⭐ CANLI — THE_LAST_SHIFT ve
│                                          THE_HOLLOW_COUNT §0.19 tabloları
│                                          buradan devraldı. Skor üretmez,
│                                          T tablosuna girmez, sayaç saymaz
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
├── 🧮 RAPOR_KONTROL/ .................... QA raporunun ÇIKTI kapısı (01.09.2026)
│   ├── rapor_kontrol.py ................. n·Σ·ort · tally · ⑨ ızgara · --film →
│   │                                      ①.12 DERS DÖNÜŞÜ yoksa NOT (14.09)
│   └── ders_frekans.py .................. 🔁 14.09.2026 · VERDICT / düşük kategori
│                                          × farklı film (mod D/V) → dersleşmemiş
│                                          örüntüler; sayac 🔁 bloğu çağırır
│
├── 🛠️ BETİKLER (kök)
│   ├── sayac.sh ......................... sayılar (14.09: film/alet dersi ·
│   │                                      YAŞAYAN n/40 · rubrik ≤25 KB · 🔁 frekans)
│   ├── film_klasoru_ac.sh ............... klasör açar · >8 sahne → tablo ·
│   │                                      --kilit-sahne · 00_HIKAYE_ONAYI kopyası
│   └── okuma_cizelgesi.sh ............... yaşayan 40 ders + manifest çizelgesi
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

FAZ MİMARİSİ — 04.09.2026'da format klasöründen merkeze çıktı
├── 5_FAZ_MIMARISI.md ................ faz = dramatik işlev (5 fazlık yay)
├── FAZ_DOSYASI_SABLONU.md ........... faz dosyası iskeleti · 12 sahne
├── KESINTISIZ_VIDEO_URETIM_TEKNIGI.md  start/end frame zinciri
└── QA_PROMPTLARI/UC_GECISLI_QA/ ..... 3 geçişli QA sistemi
        ⚠️ Üçü de yatay_7_9_dk_filmler/kilavuzlar/'daydı; klasör kapanınca
           buraya alındı ve format-bağımsız oldu. Faz mimarisini kullanan
           tek canlı hat 10-20 dk'dır (bant 7-20).
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
