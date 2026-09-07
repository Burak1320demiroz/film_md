# 🎓 DERS SEÇKİSİ — kendi üretimimize aktarılacaklar

> ⛔ **05.09.2026 — KURTARILDI.** Bu dosyanın eski adresi
> `film_analizleri/ANALIZ_EDILEN_FILMLER/NOBODY_WAS_ALIVE_WHEN_WE_LANDED/60_DERS_SECKISI.md`
> idi; o klasör kart H2 ile kaldırıldı. Kartın ⛔ ③ kuralı gereği
> (dışarıdan atıf alan dosya silinmez, taşınır) buraya alındı — iki canlı
> film hâlâ bu seçkiden devralıyor, bkz. `00_README.md`.
> Aşağıda adı geçen `50_TAM_FILM_ANALIZI.md`, `70_KARSILASTIRMA.md` ve 66
> ham parça raporu **depoda YOKTUR**; git geçmişinde durur:
> `git show e9bcf36:film_analizleri/ANALIZ_EDILEN_FILMLER/NOBODY_WAS_ALIVE_WHEN_WE_LANDED/50_TAM_FILM_ANALIZI.md`

> **Kaynak:** NOBODY WAS ALIVE WHEN WE LANDED · 69 dk · 20 parça ×
> 3-4 mercek = 66 rapor · tam analiz: `50_TAM_FILM_ANALIZI.md`
> (⛔ depoda yok — yukarıdaki kutuya bak)
>
> Ham listede 36 teknik + 9 tuzak vardı. Bu dosya **elenmiş seçkidir:**
> yalnız (a) bizim üretim hattımıza doğrudan uygulanabilen, (b) sayısal
> kilide çevrilebilen, (c) bilinen bir zayıflığımızı kapatan dersler
> kaldı. Gerisi analiz dosyasında arşivde durur.
>
> ⛔ **Bunlar hâlâ ADAY.** LESSONS_LEARNED'a giriş yolu: AGENTS.md
> **görev kartı G** — numara DERS DİZİNİ'ndeki en yüksek numaradan devam
> eder, yama önce kaynak rubriğe yazılır. Bu dosya kart G'nin girdisidir,
> çıktısı değil.
>
> ✅ **15.08.2026 — İLK SAHA DENEMESİ YAPILDI.** Bu seçkinin 11 dersi
> `yatay_2_4_dk_filmler_uzay/THE_SLOW_LIGHT_RELAY_FIELD_FILM.md` filmine
> uygulandı; hangi dersin hangi sahneye girdiği o dosyanın §0.19
> tablosunda satır satır yazılı. Film henüz ÜRETİLMEDİ — dersler
> "planda çalışıyor" aşamasında, "ekranda tuttu" aşamasında değil.
> ⭐ Kart G'ye taşımadan önce bu filmin QA sonuçlarını bekle: bir dersin
> gerçekten işe yarayıp yaramadığını ancak üretim gösterir
> (`URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` mantığı).
>
> ⭐ **Neden bu film:** Açılışında "Dreamina" jeneriği var — büyük
> olasılıkla AI üretimi ve ortalama çekim uzunluğu 9 saniye. Yani bizim
> kısıtlarımızla çalışan biri 69 dakikalık bir film çıkarmış. Buradaki
> her çözüm bizim boyumuzda test edilmiş demektir.

---

## 🥇 BİRİNCİ HALKA — AI üretim riskini DÜŞÜREN dersler

Bu dördü yalnız "iyi sinema" değil; bizim en pahalı üç sorunumuzu
(yüz tutarlılığı · yaratık tutarlılığı · içerik reddi) doğrudan azaltıyor.

### ⭐ A1 · Kötü haberi SIRTTAN çek
**Kaynak:** P06 (30 sn silüet hold) · P16 (üçüncü kişi yüzsüz oklüzyon)
**Film ne yapıyor:** Ekibin "iki önceki keşif ekibi kayboldu" haberini
aldığı an, kamera yüzlere kesmiyor — dev pencere önünde 30 saniye
silüet halinde sırtlarını tutuyor.
**Bize çevirisi (prompt kilidi):**
```
BAD-NEWS BEAT = backs to camera, silhouette against the brightest
surface in the room; hold ≥20 s; NO reaction close-up in this scene.
```
**Neden bizim için kritik:** Yüz üretmiyoruz → yüz tutarlılık riski
sıfır. Duygu kadrajın kendisinden geliyor. Bu, D69/D91 sınıfı kimlik
sapmalarının en ucuz panzehiri.
**Gideceği yer:** SINEMATOGRAFIK_TEKNIK_KILAVUZ + HOOK_VE_ILK_SAHNE

### ⭐ A2 · Yaratığı PARÇAYLA tarif et, bütününü gösterme
**Kaynak:** P09 — dev iskelet pençe hologramı: *"Elimizdeki en büyük
kayıt bu... ve bu bütün bir hayvan DEĞİL."*
**Film ne yapıyor:** 69 dakikada yaratığı bir kez, 5 saniye gösteriyor
(P01). Geri kalan her tehdit tarifi PARÇA üzerinden: pençe, iz, ses,
tanık anlatısı.
**Bize çevirisi:**
```
CREATURE RULE: the creature appears in ≤2 shots total, ≤6 s combined.
Every other threat beat = a PART (limb, track, sound, witness account,
damage pattern). Never a full-body reveal in a wide shot.
```
**Neden kritik:** Yaratık, AI üretiminde en tutarsız nesnedir. Bu kural
tutarlılık sorununu ANLATI kararına çeviriyor — dehşet artıyor, risk
düşüyor. Zombi/uzay/savaş türlerinin üçünde de geçerli.
**Gideceği yer:** UZAY_SENARYO_KILAVUZU + KILAVUZ_REHBERI §7

### ⭐ A3 · Ölümü GORE ile değil ARAYÜZLE göster
**Kaynak:** P02 (biosign sayaçları sırayla 0'a düşer) · P11 ("BIOSIG 0")
**Film ne yapıyor:** 81 kişinin ölümü tek bir ekran grafiğiyle
bildiriliyor; katliam karesi hiç üretilmiyor.
**Bize çevirisi:**
```
MASS-DEATH BEAT = screen graphic / counter only. Numeric drop to 0
readable in frame ≥3 s. No bodies, no blood in the same scene.
```
**Neden kritik:** Şiddet içeren prompt reddi riski sıfır, üretim
maliyeti bir ekran klibi. Dehşet tam.
**Gideceği yer:** KILAVUZ_REHBERI §7 BİLİNEN TUZAKLAR (red sebepleri)

### ⭐ A4 · Hızlı nesneyi TAKİP ETME — sabit kadrajdan GEÇİR
**Kaynak:** P12 shot 8 — inen gemiyi kovalamak yerine, ağaç
tepelerinden yukarı bakan sabit kadrajdan geçiriyor; hızı türbülans ve
dökülen yapraklar anlatıyor.
**Bize çevirisi:**
```
FAST-OBJECT PASS = locked-off frame, object crosses through; motion
told by debris/dust/turbulence in frame. Camera does NOT track.
```
**Neden kritik:** Kamera-nesne senkronu AI'da en sık bozulan şey.
Bu bizim "sabit lockoff kamera" kararımızın bağımsız doğrulanması —
dış bir yapımcı da aynı çözüme varmış.
**Gideceği yer:** SINEMATOGRAFIK_TEKNIK_KILAVUZ §17 karar tablosu

---

## 🥈 İKİNCİ HALKA — plan/dramaturji dersleri

### B1 · Ulaşmayan mesaj = tüm filmin motoru
**Kaynak:** P02 → P20 (filmin omurgası)
**Film ne yapıyor:** Reese tam uyarıyı kaydediyor ("kurtarma değil ASKER
gönderin"), Dünya'ya yalnız 4 baytlık "HELP" ulaşıyor. Ekip 18 part
boyunca uyarısı olmadan ilerliyor; seyirci uyarıyı biliyor. Finalde
uyarı ulaşıyor — ama ekip gittikten sonra.
**Bize çevirisi (plan bloğu):**
```
§ IRONY LOCK — plana yazılır:
  what the audience knows at minute X : ______
  what the characters know at minute X: ______
  the gap closes at minute: ______ (and at what cost: ______)
```
**Neden değerli:** Prompt cümlesiyle çözülmez — PLAN kararıdır. Tek
yazım kararı, 60 dakikalık gerilim üretiyor. 10-20 dk formatımızda
birebir çalışır.
**Gideceği yer:** SENARYO_VE_VIRAL_KAMERA_KILAVUZU + plan şablonu

### B2 · Sayısal kuralı DRAMATİK SAATE çevir
**Kaynak:** P09 (*"6 saat tolere edersin, 30 saatte ciğerinden çıkmaz.
Kasklar hep kapalı."*) → P12 (kasklar çıkarılır)
**Film ne yapıyor:** Kuralı önce sayıyla kilitliyor, sonra karakterler o
sayının içinde risk alıyor. Seyirci geri sayımı kendisi işletiyor.
**Bize çevirisi:**
```
Her tür kartında EN AZ BİR kural "sayı + ihlal bedeli" formunda
yazılır ve filmde EN AZ BİR KEZ ihlal edilir:
  "<X> saat/dakika sonra <somut bedel>" + ihlal sahnesi planda işaretli
```
**Neden değerli:** Bizim "tarif değil sayı" ilkemizin (D-ETKINLIK
raporu) dramaturji katmanı. Sayı yalnız üretimi değil, gerilimi de
kilitliyor.
**Gideceği yer:** UZAY_SENARYO_KILAVUZU · SAVAS_SENARYO_KILAVUZU

### B3 · Brifing = ışık ritüeli (statik sahne tuzağının çözümü)
**Kaynak:** P09 01:31 — *"Oturun."* + oda ışıkları söner + hologram açılır
**Bize çevirisi:**
```
EXPOSITION SCENE = light state changes ON SCREEN at scene start
(room lights OFF → single practical/hologram becomes sole key, uplight).
Information is delivered from that new light state, not the old one.
```
**Neden değerli:** Bilgi sahnesi bizim en sık ölü kare ürettiğimiz yer.
Işık durumu değişimi, aynı bilgiyi sahneye çeviriyor.
**Gideceği yer:** SINEMATOGRAFIK_TEKNIK_KILAVUZ (ışık) + prompt şablonu

### B4 · Matched-cut ile öncesi/sonrası
**Kaynak:** P17 shot 6→7 — aynı yükseklik, aynı hareket, aynı lens:
önce yeşil orman, hemen ardından kül çölü.
**Bize çevirisi (üretim tarifi):**
```
BEFORE/AFTER PAIR = iki klip, AYNI prompt, tek kelime farkı
  (örn. "lush green canopy" ↔ "grey ash stumps, no foliage").
  Aynı kamera cümlesi, aynı açı, aynı hareket. Kesme sert.
```
**Neden değerli:** AI üretiminde neredeyse bedava; iki klip tek fikir
anlatıyor. Kıyamet/çöküş anlatan her filmde kullanılabilir.
**Gideceği yer:** IMAGE_VIDEO_PROMPT_TEMPLATES (yeni kalıp)

### B5 · Hız kartını sona sakla
**Kaynak:** Film boyu ASL 7-22 sn; ilk gerçek aksiyon ritmi (5.76 sn,
0.5 sn'lik mikro-kesmeler) %90 noktasında (P18) geliyor.
**Bize çevirisi:**
```
RHYTHM BUDGET: filmin ilk %75'inde ASL bandı sabit tutulur.
Aksiyon ritmi (ASL < format tabanının yarısı) YALNIZ bir kez,
son çeyrekte kullanılır.
```
**Neden değerli:** Kısa formatta hızlı kesmeyi baştan harcıyoruz;
sonra tırmandıracak kartımız kalmıyor.
**Gideceği yer:** SENARYO_VE_VIRAL_KAMERA_KILAVUZU (vuruş haritası)

---

## ⛔ ÜÇÜNCÜ HALKA — bu filmin DÜŞTÜĞÜ yerler (tuzak dersleri)

### T-A · Kurulumu ödemeden bırakma
**Kanıt:** Üç kurulum açıldı, üçü de kapanmadı — kaptanın parlayan
gözleri (P08, tek görülme), Rain'in panodan aldığı gizli not (P10),
*"büyük olan ve küçük olan"* (P20 01:01).
**Bizim kuralımız:**
```
PLAN KAPISI: her kurulum satırının yanına ÖDEME SAHNESİ numarası
yazılır. Numarası olmayan kurulum PLANDAN SİLİNİR.
```
69 dakikada seyirci affeder; 2-10 dakikada affetmez.
**Gideceği yer:** 03_PLAN_ONCESI_KONTROL_LISTESI (13. madde)

### T-B · Ekip kompozisyonunu kilitlemedi
**Kanıt:** 4 cryo podu (P11) ↔ köprüde 5 kişi (P10) ↔ kamyon dolusu
asker (P15-P18) ↔ finalde 2 kişi. Askerlerin nereden geldiği ekranda
hiç kurulmuyor. Üstelik karakter merceği kaptanın yara izini P10'da
SAĞ, P11'de SOL yanakta buldu, P12-P13'te hiç bulamadı.
**Bizim kuralımız:** Zaten var (KARAKTER pasaportu + sayı kilidi) —
bu film onu **doğruluyor**: kilitlemeyen, yarıda "kim gemide?" sorusunu
istem dışı gizeme çeviriyor.
**Gideceği yer:** SAHNE_DEVAMLILIK_KILAVUZU (doğrulayıcı örnek olarak)

### T-C · Aksiyon coğrafyasını kurmadı
**Kanıt:** P18 — kaçan ekip ile yürüyen düşman falanksı arasındaki
mesafe hiç gösterilmiyor; tehdidin aciliyeti muğlak kalıyor.
**Bizim kuralımız:** UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU'nun tam
konusu. Kural: **cross-cut'tan ÖNCE tek geniş kadrajla mesafe kilidi.**
**Gideceği yer:** UZAMSAL_HARITA (doğrulayıcı örnek)

---

## 📋 KART G'YE GEÇİŞ — sıradaki adım

```
1. bash kilavuzlar_ve_sistem_dosyalari/sayac.sh     → mevcut ders sayısı
2. LESSONS_LEARNED.md · DERS DİZİNİ → en yüksek numarayı bul
3. Bu seçkiden alınacakları seç (öneri: A1-A4 + B1-B2 = 6 ders,
   gerisi ikinci turda) ve numaralandır
4. Her dersi TEMATİK DERSLER/ dosyasına yaz:
   ## 🔴/🟡 DERS <n>: BAŞLIK
   **Kaynak:** dış film analizi — NOBODY WAS ALIVE WHEN WE LANDED, P<nn>
   **Sorun:** bizde kaç filmde tekrarladı
   **ÇÖZÜM — prompt'a eklenecek:** ``` yukarıdaki kilit bloğu ```
5. ⚠️ Bu dersler DIŞ KAYNAKLI: "Kaynak" satırı bir QA çalıştırması
   değil, bu analiz. Kart G adım 5'teki "önce kaynak rubriği yamala"
   kuralı BURADA GEÇERSİZ — yamanacak rubrik yok. Bunun yerine
   ilgili ÜRETİM kılavuzuna işlenir (her dersin altında yazılı).
```

⛔ **Sayı yazma:** Bu dosyaya ders sayısı/toplam yazılmadı ve
yazılmayacak. Tek sayaç: `FILM_QA_RAPORLARI/00_INDEX.md` ve
`LESSONS_LEARNED.md`.
