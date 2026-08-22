# 🤖 AGENTS.md — Ajan Çalışma Kontratı

> **Bu dosyayı her görevden önce oku.** Amacı sana içerik öğretmek değil,
> **nereye yazacağını** söylemek. Ne yaptığını anlatan kılavuzlar ayrı yerde
> durur; burası "hangi olay olduğunda hangi dosyalar değişir" haritasıdır.
>
> **Kural:** Bu dosyaya sayı yazma. Sayı isteyen her cümle kaynağa işaret eder.
> Bir sayıyı iki yerde tutmak, birini yanlış tutmaktır.

---

# 0. İLK 60 SANİYE

Görev ne olursa olsun bu sırayla:

```
1.  bash kilavuzlar_ve_sistem_dosyalari/sayac.sh     → gerçek durum
2.  kilavuzlar_ve_sistem_dosyalari/KILAVUZ_REHBERI.md → üretim bilgisi
3.  bu dosyanın §3 görev kartlarından kendi görevini bul
4.  git status                                        → temiz mi başlıyorsun
```

**Kılavuz okumadan film yazma. Görev kartı okumadan dosya güncelleme.**

---

# 1. DEPO HARİTASI — ne nerede

```
kısafilmler/
│
├── AGENTS.md                      ← BU DOSYA · ajan yönlendirmesi
├── CLAUDE.md                      → bu dosyaya işaret eder
├── README.md                      proje tanıtımı
│
├── kilavuzlar_ve_sistem_dosyalari/   ⭐ SİSTEMİN BEYNİ
│   ├── KILAVUZ_REHBERI.md         ⭐ BURADAN BAŞLA — format/tür/ortam kartları,
│   │                                 negatif çekirdek, üretim akışı, tuzaklar
│   ├── YAPI_GRAFI.md                 karar ağacı + klasör ağacı (görsel özet)
│   ├── LESSONS_LEARNED.md            ders DİZİNİ + teknik kalite tablosu
│   ├── DERSLER/                      ders metinleri — 9 tematik dosya + hızlı
│   │                                 referans bloğu (07.08.2026'da bölündü)
│   ├── sayac.sh                      sayıları dosya sisteminden hesaplar
│   │
│   ├── SINEMATOGRAFIK_TEKNIK_KILAVUZ.md   lens/ışık/kamera + §17 karar tablosu
│   ├── SAHNE_DEVAMLILIK_KILAVUZU.md       karakter çapalama, seed
│   ├── UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md  kuşbakışı harita, ekran yönü, ölçek kilidi
│   ├── YANASMA_VE_KENETLENME_KILAVUZU.md  yanaşma vuruş seti + ses/dramaturji kalıbı
│   ├── TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md
│   ├── IMAGE_VIDEO_PROMPT_TEMPLATES.md    V2 prompt iskeleti
│   ├── VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md
│   ├── UZAY_SENARYO_KILAVUZU.md · SAVAS_SENARYO_KILAVUZU.md
│   ├── SHORTS_SISTEM_PROMPTU.md           dikey 9:16 hazır sistem promptu
│   ├── GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md
│   ├── KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md
│   ├── VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md paketleme (YT/IG/TikTok)
│   ├── SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md vuruş haritası + loop + kamera psikolojisi
│   ├── HOOK_VE_ILK_SAHNE_KILAVUZU.md      ilk iki sahne: S0 karar / S1 tırmandırma + hook tipolojisi
│   ├── FRAGMAN_KILAVUZU.md                fragman: dikey 3-6 / yatay 8-12 vuruş, spoiler kapısı
│   ├── KURGU_VE_TESLIM_KILAVUZU.md        birim sözlüğü + 10 maddelik kurgu kapısı + kırpma bütçesi (21.08.2026)
│   ├── SES_VE_DIYALOG_URETIM_KILAVUZU.md  replik/ses YAZIM tarafı: register + AUDIO kalıpları (21.08.2026)
│   ├── KARAKTER_VE_DUYGU_KILAVUZU.md      bağ kurma bütçeleri: göz · Kuleshov · el/nefes/yürüyüş (22.08.2026)
│   ├── KURGU_RITMI_VE_IHRAC_KILAVUZU.md   ASL eğrisi · örüntü kırıcı · ses köprüsü · ihraç sayıları (22.08.2026)
│   ├── SERI_VE_KANAL_STRATEJI_KILAVUZU.md evren modeli · kapak aile kimliği · devam hakkı (22.08.2026)
│   ├── YAYIN_VE_PERFORMANS_KILAVUZU.md    ⭐ akışın SON adımı: gerçek veri → kılavuz revizyonu (22.08.2026)
│   ├── ONERME_VE_NOVUM_KILAVUZU.md        KONSEPT kapısı: novum tipi + taşıyıcı satırı + üç kabul testi (22.08.2026)
│   ├── FINAL_VE_PAYLASIM_KILAVUZU.md      final tipi → davranış · tohum bilgi %10-15 · görsel ikilem (22.08.2026)
│   ├── DIKEY_MIKRO_DRAMA_KILAVUZU.md      9:16 dramaturjisi: 6×8 vuruş tablosu · kinesik reset (22.08.2026)
│   ├── PAKETLEME_VE_VAAT_KILAVUZU.md      kapak ANI senaryoda seçilir · vaat-teyit · spoiler bütçesi (22.08.2026)
│   ├── TEMA_MUHENDISLIGI_KILAVUZU.md      tema seçimi + tema→motif→sahne matrisi + süre-tatmin kuralı (22.08.2026)
│   ├── KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md  8 açının anlam sözlüğü + vuruş→açı tablosu + abartı eşikleri (22.08.2026)
│   ├── ACI_YAYI_VE_SEKANS_KILAVUZU.md     açı/ölçek sıçrama bandı + kurulum sayısı + yay şablonları (22.08.2026)
│   ├── MESHUR_SAHNE_KALIPLARI_KILAVUZU.md 20 ikonik sahne kalıbı + taşınabilirlik + homage/telif sınırı (22.08.2026)
│   │
│   ├── QA_PROMPTLARI/             🔍 RUBRİKLER (girdi) — üretilmiş işi eleştirir
│   │   │  ⭐ dördü de SALT PROMPT + TEK DOSYA çalışır: medya + rubrik,
│   │   │     başka hiçbir şey. Rubriğe YAZILMAZ: Türkçe not, tarih,
│   │   │     film adı, [DERS n] etiketi, depo yolu. Ders GÖVDEYE KURAL
│   │   │     olarak girer; numarası CALISTIRMA_KAYITLARI'ndaki iz
│   │   │     defterinde durur (17.08.2026 temizliği).
│   │   │     MOD D = SPEC verildi · MOD V = sadece video (skor `Ⓥ` işaretli)
│   │   ├── 00_README.md              ⭐ klasör rehberi: çalıştırma tarifi,
│   │   │                             mod sistemi, ajan akışı (kart eşlemesi)
│   │   ├── CALISTIRMA_KAYITLARI.md   koşu tarihçesi + ders dipnotları —
│   │   │                             12.08.2026'da rubriklerden taşındı
│   │   ├── FILME_OZEL/               film-özel üretim kapıları (tabloya girmez)
│   │   ├── ARSIV_6_MERCEK/           ⛔ eski 6 rubrik — ÇALIŞTIRILMAZ, kanıt
│   │   ├── 1_KARE_QA_CRITIQUE_PROMPT.md         ① sahne içi · yatay VEYA dikey
│   │   ├── 2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md   ② sahneler arası · dünya+gövde
│   │   ├── 3_SES_QA_CRITIQUE_PROMPT.md          ③ film boyu ses · YALNIZ KURGU
│   │   └── 4_HIKAYE_QA_CRITIQUE_PROMPT.md       ④ film boyu anlatı · (+PLAN)
│   │
│   ├── FILM_QA_RAPORLARI/         📊 SONUÇLAR (çıktı) — buraya YAZILIR
│   │   ├── 00_INDEX.md               ⭐ PROJEDEKİ TEK SAYAÇ + tamlık matrisi
│   │   ├── 01_FILM_RAPORLARI/        film başına kalıcı QA kaydı
│   │   ├── 02_HAM_RAPORLAR/          modelin ham çıktısı, dokunulmaz
│   │   ├── T1_KARE_KALITE.md         ① skorları        ⭐ CANLI
│   │   ├── T2_DEVAMLILIK_KALITE.md   ② skorları        ⭐ CANLI
│   │   ├── T3_SES_KALITE.md          ③ skorları        ⭐ CANLI
│   │   ├── T4_HIKAYE_KALITE.md       ④ skorları        ⭐ CANLI
│   │   ├── 03_ · 04_ · 05_ · 06_ · 07_   ⛔ KAPALI (22.08) — eski 6 mercekli
│   │   │                             sistemin skorları; yeni satır YAZILMAZ,
│   │   │                             yenilerle KARŞILAŞTIRILAMAZ
│   │   └── 08_YAYIN_PERFORMANS_TABLOSU.md ⭐ tek İZLEYİCİ tablosu — diğer
│   │                                 dördünü bir model doldurur, bunu
│   │                                 gerçek veri doldurur (22.08 açıldı)
│   │                                 (LESSONS_LEARNED teknik tablosu da
│   │                                  22.08'de KAPANDI → T1)
│   │
│   └── URETIM_ONCESI_ANALIZ/      🧪 META-ANALİZ — üretmeden önce oku
│       ├── 01_DERS_ETKINLIK_RAPORU.md    hangi ders işe yaradı, hangisi yaramadı
│       ├── 02_RISK_KARTLARI.md           malzeme başına geçmiş bozulma oranı
│       └── 03_PLAN_ONCESI_KONTROL_LISTESI.md  12 madde · ~15 dk · maliyet sıfır
│
├── dikey_shorts_filmler/          9:16 · tek dosya
├── yatay_2_4_dk_filmler_uzay/     16:9 · tek dosya · bilimkurgu
├── yatay_3_5_dk_filmler/          16:9 · FİLM KLASÖRÜ (PLAN + PART_A/B + KAPAK)
├── yatay_7_9_dk_filmler/          16:9 · FİLM KLASÖRÜ + kendi kilavuzlar/ dizini
│   └── kilavuzlar/kalite_kontrol/    ⚠️ bu formatın AYRI 3 geçişli QA sistemi
├── yatay_10_20_dk_filmler/        16:9 · 3 PERDE · FİLM KLASÖRÜ
│   └── THE_SECOND_SHIP/              120 sahne × 10s = 20:00 (8s'den sapma)
│
├── araştırmalar/                  🔬 DERİN ARAŞTIRMA RAPORLARI — dış modele
│                                     sipariş edilen raporlar (numaralı .md)
│                                     + sipariş arşivi (ARASTIRMA_PROMPTLARI.md);
│                                     kılavuzlar buradan damıtılır — üretimde
│                                     rapor değil kılavuz kullanılır
│
└── film_analizleri/               🎞️ DIŞ FİLM ANALİZLERİ — bizim yapmadığımız
    │                                 filmler, 20 parça × 3 mercek (KAMERA·OLAY·
    │                                 TEMA) + SENTEZ · film sayımına GİRMEZ
    ├── ANALIZ_QA_PROMPTLARI/         salt promptlar (video + tek dosya)
    └── ANALIZ_EDILEN_FILMLER/        film başına klasör (KUNYE + raporlar)
```

**Format seçimi, tür kilitleri, fizik kuralları → hepsi `KILAVUZ_REHBERI.md`'de.
Burada tekrarlanmaz.**

---

# 2. DEĞİŞMEZ KURALLAR

```
① SAYI TEK YERDE DURUR
   Film/ders/QA sayısı yazacaksan: 00_INDEX.md. Başka hiçbir belgeye yazma,
   kaynağa işaret et. Yazmadan önce: bash .../sayac.sh

② HER FİLM DOSYASI MARKDOWN BAŞLIĞI KULLANIR
   Sahne başlıkları ## ile başlar: "## 🎬 SAHNE 3 — BAŞLIK"
   Emoji ile başlayan düz satır YETMEZ. Gerekçe: sayaç, grep taraması ve
   herhangi bir gelecek parser başlıktan sayar — başlıksız dosya sayımdan
   ve taramadan düşer (4 dosyada oldu — bkz. §6; web paneli döneminde
   film fiilen sistemden kayboluyordu, panel gitti ama kural kalır).

③ PROMPT SELF-CONTAINED'DIR
   "[BIBLE'a bak" atfı yasak. Her prompt tek başına çalışmalı.
   Uzunluk bandı ve yasak kelimeler: KILAVUZ_REHBERI §7.

④ QA RAPORU GELDİĞİNDE HAM ÇIKTI KORUNUR
   Önce 02_HAM_RAPORLAR/ altına olduğu gibi kaydet, sonra özetle.
   Bu depoda 11 filmin ham raporu bir kez kayboldu. Tekrarlatma.

⑤ İŞ BİTİNCE COMMIT
   Yarım bırakma. Commit mesajı formatı: §5.

⑥ ÖLÇÜM SAPMASINI UNUTMA
   Aynı rubrik aynı filmi iki kez ölçtü, kategoriler 2 puana kadar oynadı.
   1.5'tan küçük skor farkları GÜRÜLTÜDÜR — "A filmi B'den iyi" deme.
   Ayrıntı: 00_INDEX.md · URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md §6b
```

---

# 3. GÖREV KARTLARI

> Her kart: **tetikleyici → dokunulacak dosyalar (sırayla) → bitiş kontrolü.**
> Karttaki sırayı bozma; sonraki adım öncekinin çıktısını kullanır.

---

## 🎬 A — YENİ FİLM YAZACAĞIM

**Kılavuz:** `KILAVUZ_REHBERI.md` §1 (dört soru) → §2/3/4 (kartlar) → §6 (akış)

```
OKU
 □ KILAVUZ_REHBERI.md · dört soruyu sırayla cevapla, okuma listeni çıkar
 □ URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md   ⛔ PLAN YAZILMADAN ÖNCE
      → 5+ risk çıkıyorsa malzeme azalt; prompt iyileştirmek işe yaramıyor
 □ Bölüm 8 film matrisindeki en yakın filmi şablon olarak aç

YAZ
 □ Dosya/klasörü doğru format klasörüne koy (§1 haritası)
      2-4 dk ve shorts  → tek .md dosyası
      3-5 dk / 7-9 dk   → film adıyla KLASÖR (PLAN + parçalar + KAPAK)
 □ Adlandırma: BUYUK_HARF_ALT_CIZGI.md · Türkçe karakter kullanma
 □ Sahne başlıkları ## ile (kural ②)
 □ PLAN → BIBLE → PROMPT sırası (KILAVUZ_REHBERI §6)
 □ ⭐ SAHNE HARİTASI YAZILIRKEN İKİ BÜTÇE DAĞITILIR (22.08.2026) —
      ikisi de üretimden SONRA eklenemez:
      · KARAKTER_VE_DUYGU_KILAVUZU.md §6 — göz · tepki planı · el ·
        yürüyüş · eşya sahnelerinin sayısı formattan hesaplanır
      · KURGU_RITMI_VE_IHRAC_KILAVUZU.md §2 — ardışık iki sahne aynı
        ölçek + palet + ses dokusunda OLAMAZ (örüntü kırıcı kapısı)
 □ ⭐ <FILM>_QA_SPEC.md yazılır — yazım paketinin son parçası [Ders 117]
      A bloğu ④ HİKAYE alanları · B kurgu geometrisi + İNSAN ŞERİDİ ·
      C belgesiz merceklerin FLAGS sorularını cevaplayan kilitler
      + TARGET ASL BAND / ASL CURVE satırları (KURGU_RITMI §1; sabit
        ızgaralı filmde gerekçe satırı ZORUNLU [D74])
      ⛔ SPEC dosyası yoksa film "yazımı tamam" sayılmaz

KONTROL ET
 □ URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md · 12 madde
      → maliyeti sıfır, 9 maddesi gerçek filmlerde gerçekten oldu
 □ ⭐ PROMPTLAR YAZILDIKTAN SONRA, TEK KARE ÜRETMEDEN → görev kartı P

GÜNCELLE
 □ KILAVUZ_REHBERI.md §8 film matrisine satır ekle
 □ FILM_QA_RAPORLARI/00_INDEX.md → tamlık matrisine "0/4" satırı ekle
 □ Klasörün README.md'si varsa film listesine ekle

BİTİŞ
 □ bash sayac.sh → toplam film sayısı 1 arttı mı
 □ commit
```

---

## 🔎 P — PROMPTLAR YAZILDI, ÜRETİM BAŞLAMADI

**Kapı:** `PROMPT_KONTROL/` · akıştaki yeri: KILAVUZ_REHBERI §6 adım 3.5
*(12.08.2026'da açıldı — 31.07'de yazıldığı söylenen dosya hiç
commit'lenmemişti; 18 commit tarandı, tek iz yok.)*

```
⛔ BU KART ATLANIRSA PARA HARCANIR. Buradaki her denetim üretimden
   ÖNCEdir ve sıfır kare tüketir.

1. BETİĞİ KOŞ — sayıları o hesaplar, sen yazma
     python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py <film dosyası>
     çıkış kodu 2 (BLOCK) → düzelt, tekrar koş, 2'ye geçme
     çıkış kodu 1 (FIX)   → bulguları oku, bilinçli sapma varsa dosyaya
                            TEK SATIR gerekçe yaz (D74: kaydı olmayan kapı)

2. RUBRİĞİ KOŞ — betiğin göremediği tek şey için
     PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md
     → kilit SAYI mı TARİF mi · sahne hangi dersi tetikliyor · A1

3. KARAR
     GO    → üretime geç (önce imaj, onaylanınca video)
     BLOCK → üretme. 5+ risk çıkıyorsa malzeme azalt; prompt
             iyileştirmek bu bandda işe yaramıyor.

⚠️ Betik bir SAYI değiştirdiyse (bant, eşik) belgeye elle yazma —
   prompt_kontrol.py başındaki sözlük tek kaynaktır.
```

---

## 🎥 B — FİLM ÜRETİLDİ (video çıktı)

```
 □ Üretim notlarını film dosyasının sonuna ekle
      hangi model · kaç deneme · reddedilen prompt varsa sebebi
 □ Yeni bir tuzak/red sebebi çıktıysa → KILAVUZ_REHBERI.md §7 BİLİNEN TUZAKLAR
      (rehberin en değerli bölümü, besle)
 □ Müzik: GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md §7-19
 □ Kapak: KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md (metinsiz üret)
 □ Fragman yazılacaksa: FRAGMAN_KILAVUZU.md (dikey 3-6 / yatay 8-12 vuruş)
 □ Paketleme: VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
 □ İhraç: KURGU_RITMI_VE_IHRAC_KILAVUZU.md §6 (1440p+ · −14 LUFS · −1,0 dBTP)
 □ 00_INDEX.md → filmin durumunu "üretildi" olarak işaretle
 □ Yayınlanacaksa → görev kartı Y
 □ commit
```

---

## 📡 Y — FİLM YAYINLANACAK / YAYINLANDI

**Kılavuz:** `YAYIN_VE_PERFORMANS_KILAVUZU.md` · tablo:
`FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md`
*(22.08.2026'da açıldı — üretim akışı 11. adımda bitiyordu, yayın sonrası
ölçüm hiçbir dosyada yoktu. Deponun bütün hook/kapak/başlık sayıları
DIŞ ARAŞTIRMA hipotezidir ve bu kart koşulmadan test edilmez.)*

```
⛔ SATIR YAYINDAN ÖNCE AÇILIR. Geriye dönük açılan kayıt 🚨 GEÇERSİZDİR:
   hangi kapak, hangi başlık, hangi hook tipi — bunlar sonradan
   hatırlanarak yazılamaz (kimlik kapısının yayın karşılığı).

YAYINDAN ÖNCE
 □ 08_YAYIN_PERFORMANS_TABLOSU.md → §1 kimlik satırı doldur
 □ Plan B kapağı hazır mı (KAPAK_FOTOGRAFI §7.2)
 □ ⛔ TEK DEĞİŞKEN KİLİDİ: ilk 48 saatte kapak VEYA başlık — ikisi değil
 □ Seri/playlist kararı: SERI_VE_KANAL_STRATEJI_KILAVUZU.md §5.1
      (bir film YALNIZ TEK resmi seride yer alabilir)

24 / 48 / 72 SAAT
 □ §2 metrik satırı · §3 eğri teşhisi · §4 karar satırı
 □ ⭐ Terk saniyesi IZGARA ARİTMETİĞİYLE SAHNEYE çevrilir —
      hizalama kapısıyla (ortak adım ⑨) aynı formül
 □ Suçlu değişken eleme sırası: paketleme → kurgu → ses → sahne →
      plan → format (ucuzdan pahalıya, kılavuz §4.2)

GERİ BESLEME — bu kartın VAR OLMA SEBEBİ
 □ Kılavuz §6 tablosundan hangi belgenin revize edileceğini bul
 □ ⛔ SIRA: veri → BELGE revizyonu → (ancak tekrarlarsa) ders.
      Yeni ders yazmak ilk refleks DEĞİLDİR [AGENTS §8]
 □ ⭐ QA skoru yüksek + gerçek metrik düşük çıktıysa: yanlış olan
      RUBRİKTİR → URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md
 □ Devam adaylığı: SERI_VE_KANAL_STRATEJI_KILAVUZU.md §4.2
      (üç filmde ölçülmeden tam kapıya geçilmez)

BİTİŞ
 □ Tablo satırı geçerlilik işareti taşıyor mu (✅ / ⚠️ / 🚨)
 □ commit
```

---

## ⛔ C/D/E/E3'ÜN ORTAK ADIMLARI — her rapor işlemede önce bunlar

```
① SPEC KAPISI [Ders 94 · teslim biçimi Ders 117]
   ⛔ SPEC BİR DOSYADIR, BÖLÜM DEĞİL. Aranacak yer önce film klasöründeki
      `<FILM>_QA_SPEC.md`; yoksa planın `📋 QA SPEC BLOĞU` bölümünden ÇIKARILIR
      ve o dosya açılır — QA anında operatörün eline iki dosya verilir:
      rubrik + SPEC. Blok planın içinde kaldığı sürece mod D koşulmuyor:
      SPEC hazır olduğu hâlde mod V koşulan film sayısı 6, mod D sayısı 0.
   Filmin planında `📋 QA SPEC BLOĞU` var mı (2-4 dk dosyalarında §0.15)?
   VAR + rapor mod V ise  → koşu bir ÖN KOŞU'dur:
        · skor satırı tabloya Ⓥ ⚠️ ŞARTLI girer,
        · 00_INDEX tamlık matrisinde o mercek hücresi ❌ KALIR,
        · kesme listeleri ve REMOVE reçeteleri UYGULANMAZ.
   Mod D bu depoda hâlâ hiç denenmedi; SPEC hazır olduğu hâlde mod V
   koşulan film sayısı 5 (Slow Stone · Starless Circle · Third Dune ·
   Ring Light · Banded Deep — 14.08, üç mercek birden).

② KİLİT ÇELİŞKİSİ DEFTERİ [Ders 96]
   Raporun, planda YAZILI bir kilide aykırı her bulgusu — bulgu listesinden
   ALINIR ve film kaydına şu deftere yazılır:
     | # | rapor ne dedi (timecode) | hangi kilit (§) | çözüm eylemi | sonuç |
   çözüm eylemi = master'ın O SANİYESİNİ izlemek/dinlemek (~10 sn iş)
   sonuç        = FİLM SAPTI / RAPOR UYDURDU / ⬜ AÇIK
   ⛔ ⬜ AÇIK madde varken: o merceğin skoru ŞARTLI, bulgudan ders
      yazılmaz, yeniden üretim siparişi verilmez.
   Sebep: aynı cümle hem "film bozuldu" (Ring Walker) hem "rapor uydurdu"
   (Low Power) olabilir; rapor tek başına ikisini ayırt edemez.

③ KİMLİK KAPISI [Ders 105]  ⛔ ①'DEN ÖNCE KOŞULUR
   Ham rapor bir film adının altına dosyalanmadan önce: raporun sahne
   listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir —
     · bir vuruş/sahne (ne gösteriyor)  ·  bir sayısal kilit (kaç, kaç
       metre, hangi yön)
   eşleşme < 2 → koşu UNATTRIBUTED: ham rapor korunur, film kaydı açılır,
                 ⛔ SKOR SATIRI YAZILMAZ, bulgudan ders yazılmaz
   ⛔ EKRANDAKİ YAZI ÇAPA DEĞİLDİR. Başlık kartı filmin en ağır ihlalidir;
      kimlik kanıtı olarak da geçersizdir — rubrik modele yasaklıyor,
      aynı yasak operatör için de geçerli.
   Sebep: Black Cradle fragmanında 15 kategorilik bir rapor + REGENERATE
   hükmü, altı vuruşun altısı tutmayan bir kurgu için üretildi; raporu
   filme bağlayan tek kanıt yanan başlık kartıydı (Starless Circle'da
   aynı şüphe 06.08'den beri çözülmedi).

④ KURGU KAPISI KAPISI [Ders 109]  ⛔ RAPOR İSTENMEDEN ÖNCE
   ⛔ ÖNCE AYIKLA, SONRA SAY [Ders 93 mekanizması]: sayım yapılmadan önce
      SAHNE-DIŞI MALZEME ayrılır — süresi ≤ 6 s VE ekranda metin taşıyan /
      statik kart / hiçbir sahnenin parmak izini taşımayan klip. Kurgunun
      başında veya sonundaysa: kayda TEK SATIR yazılır ("kart 5 s"),
      🔴 loglanır [D70/72] ve sayımın DIŞINDA tutulur. Ortasındaysa bu
      başka bir kurgudur, koşu durur.
      Sebep: eklenen 5 saniyelik bir kart, sahne şeridi plana birebir
      uyarken kapıyı düşürür ve ölçümü iptal ettirir.
   QA koşulmadan önce iki satır doğrulanır (sahne şeridi üzerinde):
     a) üretilen klip sayısı = planın SCENE COUNT'u
     b) kurgunun süresi      = planın RUNTIME'ı ± 2 s
     c) kurgunun SIRASI    = planın İNSAN ŞERİDİ  [Ders 118]
        Plandan 1 karakter = 1 sahne yazılır (1 = insan var · - = insansız),
        aynı dize raporun "who is present" sütunundan / PRESENCE STRING
        çıktısından yazılır ve yan yana konur.
        aynı  → sıra doğrulandı
        değil → ⛔ ÖNCE ÇÖZ, SONRA PUANLA: farklı yuvaların saniyeleri
                master'da izlenir. Sayı ve süre tutarken sıra bozuk olabilir —
                bir filmin doruğu bu yüzden yanlış yuvada ölçüldü.
   üçü de tutuyorsa koşu NORMAL. Biri tutmuyorsa koşu ÖN KOŞU'dur:
     · satır tabloya ⚠️ ŞARTLI girer,
     · film boyuna bakan kategoriler (Yapı · Duygu Yayı · Final ·
       Tutundurma · Ortam Devamlılığı · Kimlik Sürekliliği) SAYI TAŞIMAZ,
     · kesme listesi ve yeniden üretim siparişi UYGULANMAZ.
   ⛔ Kapı defteri kurgudan geriyse önce DEFTER güncellenir — kaydı
      olmayan kapı koşulmamış kapıdır [Ders 74].

⑤ ÇAPRAZ SAYIM KAPISI [Ders 107]  ⛔ AYNI DOSYAYA BİRDEN ÇOK MERCEK KOŞULDUYSA
   Raporların sahne/kesme sayıları yan yana yazılır:
     fark ≤ 1 → koşular birbirini doğruluyor, işle
     fark > 1 → o partinin TÜM satırları 🚨 GEÇERSİZ; tabloya girmez,
                bulgudan ders yazılmaz
   Ölçüm aleti kendi içinde tutarsızken filmin puanı tartışılmaz.
   ⚠️ Ayrıca mercekler AYNI OTURUMDA koşulduysa bağımsız ölçüm değildir
      [Ders 110]: severity sayıları ve sahne sınırları birebir tutuyorsa
      bu doğrulama değil KOPYADIR — her mercek temiz oturumda koşulur.

⑥ ÇAPRAZ GÖZLEM BİRLEŞTİRME [Ders 108]
   Birden çok raporda geçen her gözlem film kaydına şu tabloyla yazılır:
     | gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
   Gözlem TEK tabloda puanlanır (sahibi = rubriklerin kapsam listesinin
   gösterdiği mercek); diğer hücreler işaretçiye iner (→🔧) ve o kategori
   kaynaksız kaldığı için DÜŞÜRÜLMEZ.

⑦ ÇAPRAZ FİLM PARMAK İZİ KAPISI [Ders 112]  ⛔ MOD V RAPORLARINDA
   Rapor işlenmeden önce, AYNI rubriğin son iki koşusunun künye satırı yan
   yana konur: SÜRE · SEGMENT SAYISI · ORTALAMA SAHNE SÜRESİ · kart saniyesi.
     üçü de ±%5 içinde aynıysa → 🚨 PARMAK İZİ ŞÜPHESİ: rapor işlenir ama
     SÜRE VE SAHNE SAYISI HİÇBİR KAPIYA GİRDİ SAYILMAZ; operatör dosyanın
     kendi süresini OKUR ve kurgu kapısını (④) O SAYIYLA koşar.
   Sebep: iki farklı filmin iki ayrı raporu 62/63 s · 7 segment · ~10 s
   sahne · 0:58'de başlık kartı bildirdi. ⑤ aynı DOSYAYA koşulan mercekleri
   karşılaştırır; bu kapı FARKLI dosyalara koşulan aynı merceği karşılaştırır.

⑧ FRAGMAN MERCEK KAPISI [Ders 111]
   Malzeme bir FRAGMAN mı? Merceği ① KARE'dir (dikeyse `FORMAT: DİKEY`);
   ④ HİKAYE fragmana koşulmaz [FRAGMAN_KILAVUZU §0] ve fragman satırı FİLM
   tablolarına (T1-T4) girmez. Yanlış mercek koşulduysa: ham rapor korunur,
   film kaydı açılır, ⛔ SKOR SATIRI YAZILMAZ, kesme/reçete UYGULANMAZ.

⑨ HİZALAMA KAPISI [Ders 115]  ⛔ ⑤'TEN SONRA, PLAN ELDEYSE HER KOŞUDA
   Raporun sahne SAYISI hiçbir kapıya girdi sayılmaz; ızgara PLANDAN alınır:
     sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
   Replikli filmde doğrulama replik zaman koduyla yapılır:
     beklenen = sahne başlangıcı + repliğin prompt TIMELINE'ındaki ofseti
     |Δ| ≤ 2 s → sahne yerinde · |Δ| ≈ klip süresinin katı → sahne kaymış
   Sessiz filmde: raporun blokları ardışık ızgara dilimlerinin birleşimi mi?
   ⭐ Kapı master açılmadan koşar ve kimlik kapısının (③) sayısal biçimidir:
      uydurulmuş zaman kodları ızgaraya oturmaz.
   Sonuç film kaydına IZGARA GERİ ALMA tablosu olarak yazılır; raporun
   kendi sahne haritası o tabloyla değiştirilir.

⑩ ÖNERME KAPISI [Ders 87 · kapsamı Ders 116]  ⛔ HANGİ MERCEKTEN GELİRSE GELSİN
   Coğrafya · Kostüm-Prop · Zaman-Işık · Çevre · Fizik · Ses mimarisi ·
   Ekipman durumu bulguları tabloya işlenmeden ÖNCE planın logline + sahne
   haritası + sayısal kilit listesine karşı okunur:
     kaynağı planda YAZILI → bulgu DÜŞER, film kaydına "önerme" yazılır
     kaynağı yok           → bulgu ayakta
   ⛔ Bulguyu getiren merceğin adı bu kararı değiştirmez. Kapı 12.08'de
      yalnız kart E'ye yazıldı; 20.08'de aynı yanlış okuma dört mercekten
      geldi ve biri filmin PLANLI FİNALİNİ kesmeyi önerdi.
```

---

## 🔧 C — ① KARE RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/1_KARE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ SPEC)

```
⛔ FORMAT KAPISI (22.08.2026): raporun ilk satırında `FORMAT:` var mı?
   YATAY → kategori 12-14 (9:16 · güvenli alan · kanca) N/A olmalı
   DİKEY → o üçü PUANLI olmalı; boşsa koşu eksiktir, tabloya girmez
   Rubrik aspect'i dosyadan ölçer. Rapor formatı başlıktan aldığını
   söylüyorsa ölçüm yapılmamıştır.
```

```
⛔ ÖNCE KAPI: raporun ilk satırındaki INPUT MODE nedir?
   MOD D → SPEC prompt dosyasından kopyalandı, uygunluk ölçüldü.
   MOD V → SPEC yok; film kendisiyle + fizikle ölçüldü. Geçerli bir
           çalıştırmadır. Skor satırı `Ⓥ` ile işaretlenir, FLAGS FOR
           DOCUMENT CHECK soruları plan dosyasından cevaplanır (adım 2'de).
   Rapor "INPUT MISSING" diyorsa rubrik güncel değildir ya da modele eski
   sürüm verilmiştir — 05.08.2026'dan beri geçersiz bir çıktıdır.

1. HAM RAPORU KAYDET       02_HAM_RAPORLAR/<FILM>_KARE_HAM.md
                           model çıktısı olduğu gibi, düzenlemeden

2. FİLM KAYDINI YAZ/GÜNCELLE  01_FILM_RAPORLARI/<FILM>.md
                           yoksa oluştur · üst blokta dört merceğin durumu,
                           künye, kategori skor tablosu, bulgular
                           (şablon: 01_FILM_RAPORLARI/THE_INVERSION.md)

3. SKOR SATIRINI EKLE      LESSONS_LEARNED.md · teknik kalite tablosu
                           ⚠️ teknik skor BURAYA gider, 03/04 tablolarına DEĞİL
   | Film | Sahne | Karakter | Fizik | Kamera | Işık | Çevre | Canlı | Hareket | Toplam |

4. SAYACI GÜNCELLE         00_INDEX.md · §SAYIM + tamlık matrisi (🔧 sütunu)

5b. ⭐ PROMPT REÇETESİNİ GREP'LE  [Ders 85]
    Raporun her REMOVE / REPLACE önerisi uygulanmadan önce:
       grep -rn "<önerideki tam dize>" <FILM klasörü>/
    çıktı BOŞ                → reçete DÜŞER (rapor promptu görmedi, uydurdu)
    çıktı YASAĞIN İÇİNDE     → reçete DÜŞER (çalışan yasağı silme önerisi)
    ⚠️ Third Dune'da "REMOVE 'title card, cinematic poster'" önerisi filmin
       metin yasağını silecekti; dize depoda yalnız yasağın içinde vardı.
    ADD önerileri bu kapıdan muaf.

5. YENİ DERS VAR MI?       → görev kartı G

6. commit
```

---

## 📖 D — ④ HİKAYE RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/4_HIKAYE_QA_CRITIQUE_PROMPT.md` · girdi: video (+ PLAN)

```
⛔ İKİ MOD VAR (05.08.2026'dan beri):
   MOD D — plan dosyası verildi. Sahne sayısı · süre · diyalog sayısı plana
           karşı doğrulanır; tutmazsa skor GEÇERSİZ ve tabloya ~~üstü
           çizili~~ girer (örnek: Low Power satırı). Zirve kontrolü yapılır.
   MOD V — plan yok. Film ekranda göründüğü hâliyle puanlanır; on kategori
           de yazılır, zirve kontrolü SORUYA döner. Satır `Ⓥ` + ⚠️ ŞARTLI.
   Eski "plan olmadan çalıştırılmaz" kuralı kaldırıldı: hiç çalışmayan bir
   senaryo denetimi kimseyi korumuyordu (üç Dawn Front çalıştırması boşa
   gitti).

1. 02_HAM_RAPORLAR/<FILM>_HIKAYE_HAM.md       ham çıktı
2. 01_FILM_RAPORLARI/<FILM>.md                📖 HİKAYE QA bölümü
   ⭐ mod V ise: FLAGS FOR DOCUMENT CHECK sorularını plan dosyasından
      CEVAPLA ve cevapları buraya yaz (kart E adım 2 ile aynı iş)
3. FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md      skor satırı — T1'E DEĞİL
   | Film | Format | Kanca | Önerme | Yapı | Karakter | Tema | Diyalog | Duygu Yayı | Final | Özgünlük | Tutundurma | Toplam |
   geçerlilik işareti:  ✅ geçerli · ⚠️ ŞARTLI · 🚨 GEÇERSİZ
   mod V satırı:  film adının yanına `Ⓥ` + ⚠️ ŞARTLI
4. 00_INDEX.md                                📖 sütunu + sayım
5. Yeni ders → kart G
6. commit
```

---

## 🔗 E — ② DEVAMLILIK RAPORU GELDİ
*(22.08.2026'da eski E + E2 kartları birleşti — rubrikler birleştiği için.
Karakter artık opsiyonel derin mercek DEĞİL, bu merceğin gövde yarısıdır.)*

**Rubrik:** `QA_PROMPTLARI/2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**

```
⛔ TERSİ KURAL: Bu rubriğe DOKÜMAN VERİLMEZ. Baseline STEP 1'de videodan
   kurulan sahne envanteri + karakter pasaportudur. "Eksik sahne" ve
   "eksik karakter" raporlaması bu rubrikte yasaktır.

⛔ İKİ YARI KAPISI: rapor 13 kategoriyi de taşıyor mu?
   GÖVDE 1-6   kimlik · kostüm · yıpranma · ekipman · çapraz kesme · fizik
   DÜNYA 7-13  sayaç · coğrafya · zaman-ışık · dünya propu · nedensellik
               · nicelik+sayı · kurulum
   Gövde yarısı boşsa koşu YARIMDIR — eski MANTIK_QA'nın ölçtüğü kadarını
   ölçmüştür ve tabloya tam satır olarak girmez.

⛔ ⚠️ PARTIAL KAPISI: kanıtı 3 sahneden az ya da sürenin %25'inden azı
   olan kategori numarasız kalır ve ortalamaya girmez. Numaralı bir
   ⚠️ PARTIAL hücresi aritmetik hatasıdır.

1. 02_HAM_RAPORLAR/<FILM>_DEVAMLILIK_HAM.md   ham çıktı
2. ⭐ FLAGS FOR DOCUMENT CHECK sorularını plan dosyasından CEVAPLA
      → rubriğin ikinci yarısı budur; en değerli bulgular buradan çıktı
      → cevapları 01_FILM_RAPORLARI/<FILM>.md içine yaz
2b. ⭐ "BU DEĞİŞİM FİLMİN ÖNERMESİ Mİ?"  [Ders 87 · artık ORTAK ADIM ⑩]
      Coğrafya · Kostüm-Prop · Zaman-Işık bulgusu TABLOYA İŞLENMEDEN önce
      planın logline + orta nokta + sayaç kanalları okunur.
      evet → bulgu DÜŞER, film kaydına "önerme" yazılır, satır ŞARTLI
      hayır → bulgu ayakta
      ⚠️ Third Dune: üç MAJOR'ın ikisi buradan düştü (araç gömülmesi =
         filmin orta noktası · kalkış çanağı = planlı S22)
2c. ⭐ KİMLİK / SAYAÇ KAPISI — diğer bütün skorları ezen iki bulgu
      Rapor IDENTITY BREAK (başka yüz ya da ekranda kopya karakter) veya
      sayaç tersinmesi bildiriyorsa, ortalama ne olursa olsun verdict'in
      ilk satırı odur ve film kaydına ÖNCE o yazılır.

3. FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md   skor satırı
   | Film | Kimlik | Kostüm | Yıpranma | Ekipman | Çapraz Kesme | Fizik |
     Sayaç | Coğrafya | Zaman-Işık | Dünya Propu | Nedensellik |
     Nicelik+Sayı | Kurulum | Toplam |
4. 00_INDEX.md                                ② sütunu + sayım
5. Yeni ders → kart G
6. commit
```

---

## 🧍 E2 — KALDIRILDI (22.08.2026)

> Karakter merceği ② DEVAMLILIK'in **gövde yarısı** oldu; ayrı kartı yok.
> Karakter raporu geldiğinde **kart E**'ye bak. Eski kartın tek kuralı
> oraya taşındı: kesişen kostüm-prop bulguları artık kural değil YAPI
> gereği tekildir — gövde 1-6, dünya 7-13.

---

## 🔊 E3 — ③ SES RAPORU GELDİ

**Rubrik:** `QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md` · girdi: **yalnız video**
*(22.08.2026: artık OPSİYONEL DEĞİL — kurguda ses varsa zorunlu dört
mercekten biri. Eski karakter merceğinin ses/performans yarısı da buraya
geldi: ses bu merceğin, beden ②'nin.)*

```
⛔ TERSİ KURAL: Bu rubriğe DOKÜMAN VERİLMEZ. Baseline STEP 1'de kurgudan
   kurulan ses defteridir. "Eksik replik" raporlaması yasaktır.

⛔ İKİ KAPI, ikisi de koşudan ÖNCE operatörün işi:
   ① MALZEME: tek klip değil, TAM KURGU verilir. Bu rubriğin ölçtüğü şeyin
      çoğu kesmelerin ARASINDA yaşar — tek klip koşusu tabloya girmez
      (DERS 75'in bu mercekteki karşılığı).
   ② SES: raporun header'ında AUDIO STATE var mı?
      A dolu · B sessiz ama ses tasarımlı · C tamamen sessiz → koşu YOK
      · D ses kesintili. Rapor `AUDIO ABSENT — RUN NOT STARTED` döndüyse
      skor yazılmaz; master'ın ses kanalı kontrol edilip yeniden ihraç edilir.

1. 02_HAM_RAPORLAR/<FILM>_SES_HAM.md          ham çıktı

2. ⭐ REGISTER DOĞRULAMASI — bu kartın en kritik adımı
      Raporun dialogue ledger'ındaki HUMAN / MACHINE / UNCLEAR işaretleri
      plan dosyasıyla karşılaştırılır. Seri diegetik yapay ses kullanıyor
      (Blind Return 8/8 suit AI · Cold Burn 12/12 telsiz-AI).
      → MACHINE olması gereken bir repliğe "sentetik duruyor" bulgusu
        yazıldıysa BULGU DÜŞER, tabloya işlenmez.
      → UNCLEAR replikler plandan cevaplanır, cevap film kaydına yazılır.
      ⚠️ Bu adım atlanırsa rubrik çalışan tasarımı bozmaya yönlendirir.

3. ⭐ FLAGS FOR DOCUMENT CHECK sorularını plan/senaryo dosyasından CEVAPLA
      → cevapları 01_FILM_RAPORLARI/<FILM>.md · 🔊 SES QA bölümüne yaz

4. FILM_QA_RAPORLARI/T3_SES_KALITE.md          skor satırı
   | Film | Ses Durumu | Atıf | Sentetik | Ses Kimliği | Aktarım |
     Sıra Alma | Ambiyans | SFX Senk | Miks | Müzik | Toplam |

5. 00_INDEX.md · ③ sütunu + sayım — ③ artık matrisin /4 paydasının
   TAM ÜYESİDİR (22.08'e kadar opsiyonel derin mercekti ve bu yüzden
   34 film kaydının yalnız 5'inde ses raporu vardı)

6. ⚠️ KESİŞİM BİRLEŞTİRME — aynı filme koşulan diğer mercekler:
      ① KARE 8. kategorisi (Diyalog ve Ses) → tek klip ölçüldüyse yerinde
        kalır; AYNI KURGU ölçüldüyse ses bulguları ③'e devredilir
      ② DEVAMLILIK ile kesişim YOK — ses bu merceğin, beden ②'nin;
        ayrım rubriklerin kapsam bloğunda yapısaldır
      OUT-OF-SCOPE FLAGS satırları ilgili merceğin kaydına taşınır
      (dudak-fonem · vakumda ses · altyazı → ① KARE)

7. ⭐ "FIXABLE IN THE MIX vs REQUIRES REGENERATION" tablosunu 00_INDEX
   YAPILACAKLAR listesine iki ayrı blok olarak geçir — bu merceğin
   diğerlerinden farkı, bulgularının çoğunun YENİDEN ÜRETİM GEREKTİRMEMESİ

8. Yeni ders → kart G
9. commit
```

---

## 📚 G — YENİ DERS ÇIKTI

```
1. Dersi İKİ yere işle (07.08.2026'dan beri dersler klasörde):
   a) DERSLER/ içindeki uygun TEMATİK dosyanın sonuna ekle
      (kamera/karakter/fizik/ışık/ekipman/metin/kurgu/QA/sistem —
      hangisi olduğuna LESSONS_LEARNED.md'deki dosya tablosundan karar ver)
      ## 🔴/🟡 DERS <n>: BAŞLIK
      **Kaynak:** hangi film, hangi skor
      **Sorun:** kaç filmde tekrarladı
      **ÇÖZÜM — prompt'a eklenecek:** ``` kod bloğu ```
   b) LESSONS_LEARNED.md · DERS DİZİNİ tablosuna satır ekle
      numara dizindeki EN YÜKSEK numaradan devam eder — tematik dosyanın
      içindeki son numaraya BAKMA, numaralar dosyalara dağınık

2. ⭐ TARİF DEĞİL SAYI YAZ
   Kanıtlanmış tek mekanizma sayısal kilit. "Toz yavaş çöksün" değil,
   "toz 3 saniyede yüzeye oturur" yaz. Tarif kilitleri ölçülebilir
   şekilde işe yaramadı — URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md

3. Ders tür/ortama özelse → KILAVUZ_REHBERI §3 veya §4 ilgili kartına
   "İlgili ders" satırına numarayı ekle
4. Tür-bağımsızsa ve her prompta girecekse → §5 NEGATİF ÇEKİRDEK
   ⚠️ Çekirdek 9 film dosyasına kopyalanmış durumda. Değiştirirsen:
      grep -rl "no camera teleportation" --include="*.md" .
5. ⭐ ÖNCE KAYNAK RUBRİĞİ YAMALA [Ders 63]
   Dersin **Kaynak** satırındaki çalıştırma hangi rubrikten çıktıysa yama
   ÖNCE oraya yazılır. Kaynak rubrik yamalanmadan diğerlerine geçilmez.
   ⛔ YAMA SADECE KURALDIR (17.08.2026 salt-prompt temizliği):
      İngilizce · gövdeye · emir kipinde · numara/tarih/film adı YOK.
      Rubriğe girmesi yasak: "[DERS n]" · "12.08.2026'da X filmi..." ·
      "../LESSONS_LEARNED.md" · Türkçe açıklama.
      Sebep: rubrik operatörün videoyla birlikte yapıştırdığı TEK dosya;
      göremediği bir derse atıf, modelin uyduracağı bir boşluktur.
   ⛔ 5c KARDEŞ RUBRİK TARAMASI [Ders 111] — kaynak rubrik yamandıktan sonra
      dersin tarif ettiği hatayı ÜRETEBİLECEK her rubrik açılır. Ölçüt tek
      soru: "bu rubrik aynı malzemeyi görse aynı hatayı yapar mıydı?"
        evet  → yamanır, iz defterine satır girer
        hayır → iz defterine "D<n> → <rubrik> · GEREKMEZ · <sebep>" yazılır
      Tarama yapılmadan kart kapanmaz. D63 SIRA'yı söyler, KAPSAM'ı değil:
      D106 tek rubriğe işlendi ve aynı gün ikinci rubrikte tekrarladı.
   ⭐ Numara, tarih, film ve çalıştırma kaydı ŞURAYA yazılır:
      QA_PROMPTLARI/CALISTIRMA_KAYITLARI.md
        · ilgili rubriğin bölümü → "N kez çalıştırıldı · son <tarih> · sonuç"
        · §DERS → RUBRİK İZ DEFTERİ → "D<n> → <rubrik> · <bölüm adı>"
      ⛔ Ders hangi rubriklere işlendiyse iz defterine O SATIR yazılmadan
         kart kapanmaz — rubrikte artık aranacak etiket yok, tek iz burası.
   ⚠️ 03.08'de Ders 60/61/62 yazıldı ve DÖRT rubrik düzeltildi; 60 ile 62'yi
      ÜRETEN SHORTS_QA atlandı, iki gün sonra aynı hatayı üretti.
6. QA promptunun ders sayısı referansını güncelle
7. bash sayac.sh → boşluk uyarısı var mı
   ⚠️ Betik benzersiz numarayı en büyük numarayla karşılaştırır; ÇİFT
      yazılmış numarayı göremez (çift numara boşluk yaratmaz).
      Ayrıca kontrol et:
      cat kilavuzlar_ve_sistem_dosyalari/DERSLER/*.md \
        | grep -oE "^## .{0,4} DERS [0-9]+" \
        | grep -oE "[0-9]+" | sort -n | uniq -d
      → çıktı SADECE "60 61 62" olmalı (tarihsel çift numaralar, dizinde
        a/b olarak kayıtlı) — başka numara çıkarsa yeni çift açılmış demektir
8. commit
```

---

## 🧱 H — YENİ FORMAT / TÜR / ORTAM EKLENDİ

```
 □ KILAVUZ_REHBERI.md → §2 (format) / §3 (ortam) / §4 (tür) kartı
      yeni tür için §4.4 boş şablonundan başla
 □ YAPI_GRAFI.md → karar ağacına dal + klasör ağacına satır
 □ Yeni klasör açıldıysa → sayac.sh içindeki klasör listesine ekle
 □ commit
```

## 🧱 H2 — FORMAT / TÜR / KLASÖR KALDIRILDI (H'nin tersi)

> Sistem büyümeye hazırdı, küçülmeye değil — 12.08.2026'da zombi/savaş
> klasörleri silindi ve dört harita günlerce silinen klasörü göstermeye
> devam etti. Bir klasör silinince AYNI dört nokta güncellenir:

```
 □ AGENTS.md §1 haritasından satırı sil
 □ YAPI_GRAFI.md → karar ağacındaki dal + klasör ağacındaki satır
 □ sayac.sh içindeki klasör listesinden çıkar
 □ FILM_QA_RAPORLARI/00_INDEX.md → o klasörün bölümü/satırları kaldırılır
 □ KILAVUZ_REHBERI.md → tür/format kartı SİLİNMEZ, başına ⏸️ RAFTA yazılır
      (kılavuz bilgisi ucuz, yeniden yazmak pahalı)
 □ bash sayac.sh → toplam, 00_INDEX ile tutuyor mu
 □ commit (tip: bakim)
```

---

## 🌐 I — WEB PANELİ (KALDIRILDI)

> Panel (`web/`) 21.08.2026'da depodan kaldırıldı — kart H2 bu tarihte
> uygulandı ve dört haritadan panel satırları silindi. Panel geri
> gelirse git geçmişindeki bu kartın eski hâli temel alınır
> (`git log --all -- web/`). O güne dek "panele dokundum" diye bir
> görev yok.

---

# 4. YAZIM STANDARDI

```
DOSYA ADI      BUYUK_HARF_ALT_CIZGI.md · Türkçe karakter yok · ASCII
FİLM BAŞLIĞI   # <emoji> FILM ADI — Türkçe Alt Başlık
SAHNE BAŞLIĞI  ## 🎬 SAHNE <n> — BAŞLIK          ← ## şart (kural ②)
PROMPT         ``` kod bloğu içinde · blok dışına Türkçe açıklama yazma
BIBLE          ## <emoji> WORLD/CHARACTER/SHIP/CAMERA BIBLE — <ad>
TARİH          GG.AA.YYYY (02.08.2026)
```

**Bir sayfayı iki iş yapmaya zorlama.** Rubrik `QA_PROMPTLARI/`'da, sonuç
`FILM_QA_RAPORLARI/`'da, ders `LESSONS_LEARNED.md`'de durur.

---

# 5. COMMIT KURALI

> ⛔ **COMMIT'İ SADECE PROJE SAHİBİ ATAR.** Ajan `git commit` / `git push`
> ÇALIŞTIRMAZ (`.claude/settings.json` deny kuralıyla da engellidir).
> Görev kartlarındaki "commit" adımı = "iş commit'e HAZIR bırakılır" demektir;
> aşağıdaki format, sahibin atacağı commit mesajı içindir.

```
<tip>: <ne değişti>

tipler:  film    yeni/güncellenen film dokümanı
         qa      QA raporu, skor tablosu, film kaydı
         ders    LESSONS_LEARNED
         kilavuz kılavuz/sistem dosyası
         panel   web/
         bakim   temizlik, düzeltme, yapı
```

- QA raporu ve skor satırını **aynı** commit'e koy — ayrılırsa tablo yalan söyler.
- İş bitmeden commit atma; yarım bırakılan güncelleme, hiç yapılmamıştan kötüdür.

---

# 6. BİLİNEN AÇIKLAR — bunlara güvenme

> 02.08.2026 denetiminde bulundu. Düzeltilene kadar ajanın bilmesi gerekir.

```
🔴 4 dosya başlık standardı dışında (V1 düz metin — kural ② ihlali):
   THE_BREATHING_STORM · THE_DEEP_PRESSURE · THE_ETERNAL_ENGINE · THE_PULSE
   (panel varken bu dosyalar parser'dan düşüyordu; panel 21.08.2026'da
   kaldırıldı ama başlıksızlık hâlâ tarama/sayaç hatası üretir)
   Ayrıca: THE_DEEP_ROOT puanı var ama 13 sahnenin 0'ı yazılmış ·
   THE_WAKING_GROUND yok — format kartına dürüst kayıt düşüldü
   (KILAVUZ_REHBERI §2.4, 21.08.2026)

🟡 URETIM_ONCESI_ANALIZ/01 ders etkinlik raporu 01.08.2026 kesitinde
   (50 ders); D51-119 hiç ölçülmedi — rapor yeniden koşulmalı

🟡 sayac.sh · ① KARE sayısı eksik
   Regex kalın yazılmış tablo satırlarını (| **Film** | **Full**) atlıyor.
   Diğer çıktıları güvenilir. ⛔ 22.08'den beri ayrıca BAYAT: saydığı
   LESSONS_LEARNED teknik tablosu KAPANDI, canlı tablo T1_KARE_KALITE.md.

🟡 Ders sayısı üç belgede farklı
   Gerçek kaynak LESSONS_LEARNED.md. URETIM_ONCESI_ANALIZ/00_README ve
   yapılcaklar.md bayat sayı taşıyor.

🟡 Kırık dosya referansları
   SUREKLILIK_LEDGERI.md · THE_RISING_SNOW_KAPAK.md
   THE_GLASS_WORLD_SHORTS.md · THE_LAST_ARCHIVE_SHORTS.md

🟡 QA sistemi çatallı
   QA_PROMPTLARI/ (yatay, 8-11 kategori) ve
   yatay_7_9_dk_filmler/kilavuzlar/kalite_kontrol/ (3 geçişli) ayrı sistemler.
   İki sistemden gelen skorlar aynı tabloda karşılaştırılamaz.

🟡 KILAVUZ_REHBERI §8 film matrisi bayat — depodaki filmlerin çoğu listede yok.
🟡 dikey_shorts_filmler/ içinde 16:9 YATAY dosyalar var (klasör adı yanıltıyor).
🟡 yapılcaklar.md bozuk — terminal çıktısı kaydedilmiş, cümleler yarım.
```

---

# 7. DOĞRULAMA — iş bitince çalıştır

```bash
bash kilavuzlar_ve_sistem_dosyalari/sayac.sh   # sayılar tuttu mu, ders boşluğu var mı
git status                                      # her şey commit'lendi mi

# başlıksız (panelden düşecek) film dosyası var mı — çıktı boş olmalı
for f in dikey_shorts_filmler/*.md yatay_2_4_dk_filmler_*/*.md; do
  [ "$(grep -cE '^#' "$f")" -lt 3 ] && echo "BAŞLIKSIZ: $f"
done

```

---

# 8. AJANA SON SÖZ

```
Bu sistemin ölçülmüş gerçeği: kural eklemek kaliteyi artırmadı.
Kalite yükselten üç olayın üçü de kural değil, karar değişikliğiydi —
sabit lockoff kamera, sahneleri ayrı üretmek, tarif yerine sayısal kilit.

Yeni bir ders yazmadan önce sor: bu prompt cümlesiyle mi çözülüyor,
yoksa planla, sahne haritasıyla veya kurguyla mı? İkincisiyse dersi
LESSONS_LEARNED'a yazmak onu çözmez.

Ayrıntı: URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md
```

---

> **Bu dosya ne zaman güncellenir**
> □ Yeni klasör/format eklenince → §1 haritası + kart H
> □ Yeni QA rubriği eklenince → yeni görev kartı (§3)
> □ §6'daki bir açık kapanınca → satırı sil
> □ Yeni bir "hangi dosyayı güncelleyeceğim" sorusu çıkınca → yeni kart
>
> Bu dosyaya **içerik** taşıma. Adres ver, kaynağa yolla.
