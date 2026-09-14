# 🎞️ DIS_FILM_ANALIZI — kurtarılmış metodoloji (05.09.2026)

> ⛔ **HAT KAPALI.** `film_analizleri/` klasörü 05.09.2026'da sahip
> kararıyla depodan KALDIRILDI (kart H2). Analiz edilmiş film klasörleri,
> ham parça raporları ve DIKEY_4_PARCA paketi depoda YOKTUR.
>
> Buradaki iki şey İKİ AYRI gerekçeyle kurtarıldı — karıştırma:
> · **Ders seçkisi** → kartın ⛔ ③ kuralı: *"Dışarıdan atıf alan her dosya
>   SİLİNMEZ, TAŞINIR."* İki canlı film onu adresliyordu (aşağı bak).
> · **Dört analiz promptu** → ③ DEĞİL: depoda hiçbir yerden atıf almıyorlardı
>   (git grep ile doğrulandı). Kartın kılavuz maddesindeki gerekçeyle
>   korundular: *"bilgi ucuz, yeniden yazmak pahalı."*

---

## 📦 BURADA NE VAR

```
DIS_FILM_ANALIZI/
├── 00_README.md                        ← bu dosya
│
├── 🔍 METODOLOJİ — salt promptlar (dosyada SADECE modele verilecek
│                    prompt vardır; not/tarihçe yazılmaz)
│   ├── KAMERA_ANALIZ_PROMPT.md            parça → shot list, açı/ölçek/
│   │                                      hareket, kesme ritmi, kamera dili
│   ├── OLAY_ANALIZ_PROMPT.md              parça → sahne envanteri, beat
│   │                                      beat olaylar, diyalog, dramaturji
│   ├── TEMA_ANALIZ_PROMPT.md              parça → motif, ışık/renk, ses, tema
│   └── SENTEZ_ANALIZ_PROMPT.md            tüm parça raporları (metin) →
│                                          bütün film
│
└── 📊 ÖLÇÜM — hattın tek tamamlanmış koşusundan kalan tek çıktı
    └── NOBODY_WAS_ALIVE_DERS_SECKISI.md ⭐ CANLI: iki film bu seçkiden
                                          devraldı (aşağı bak)
```

---

## ⭐ NEDEN DURUYOR — ölçüm verisi filmle birlikte silinmez

Kart H2 ③ (26.08.2026 turu): *"ÖLÇÜM VERİSİ FİLMLE BİRLİKTE SİLİNMEZ."*
`NOBODY_WAS_ALIVE_DERS_SECKISI.md` yalnız bir arşiv değil, **canlı iki
filmin kaynağıdır** — ikisi de hikâye ve kamera gramerini bu seçkiden
devraldı ve dosyalarının §0.19 tablosunda ders ders yazılı:

```
yatay_2_dk_filmler/THE_LAST_SHIFT/THE_LAST_SHIFT_COLONY_FILM.md
     §0.19 DEVRALINAN DERSLER — deponun DIŞ FİLM ANALİZİNDEN hikâye ve
     kamera grameri devralan İLK filmi
yatay_2_dk_filmler/THE_HOLLOW_COUNT/THE_HOLLOW_COUNT_SALT_TERRACE_FILM.md
     §0.19 DEVRALINAN DERSLER — aynı analizden türetilen ikinci film
```

Seçki silinseydi bu iki filmin "neden böyle yazıldı" gerekçesi kaynaksız
kalırdı.

⚠️ **Seçkinin dersleri hâlâ ADAY.** LESSONS_LEARNED'a giriş yolu AGENTS.md
görev kartı **G**'dir; hiçbiri henüz üretimde ölçülmedi. Dış film dersleri
için kart G adım 5 ("önce kaynak rubriği yamala") GEÇERSİZDİR — yamanacak
rubrik yok, ders doğrudan ilgili ÜRETİM kılavuzuna işlenir.

---

⚠️ **`DIS_REFERANS_OLCUMU.md` bu hattın yeniden açılması DEĞİLDİR** (05.09.2026).
O dosya tek seferlik bir ÖLÇÜM çıktısıdır: kaynak klipler `.gitignore`'da,
ham raporlar depoya girmedi, yalnız iki tablo kurtarıldı (süre/kurulum ·
ölçek şahidi). Aşağıdaki akış hâlâ KAPALIDIR ve koşulmaz.

---

## 🔁 HAT YENİDEN AÇILIRSA

Dört prompt çalışır durumdadır. ⛔ Ama kurtarılan yalnız GİRDİ tarafıdır:
çıktı klasörünün şablonu (film klasörü iskeleti · `00_KUNYE.md` · adlandırma
kuralı · "neden 20 parça × 3 mercek" gerekçesi) taşınmadı — hepsi git'te durur,
`git show e9bcf36:film_analizleri/00_README.md`. Hat açılırsa oradan okunur.

Akış:

```
0. Operatör filmi 20 eşit parçaya böler (toplam süre ÷ 20).
   ⚠️ Eşit kesilemiyorsa her parçanın SÜRESİ kaydedilir — timecode
      haritası yoksa sentez sıralamayı tahmin etmek zorunda kalır.
1. Parça başına üç koşu: KAMERA · OLAY · TEMA.
   ⚠️ Dördüncü (opsiyonel) mercek 🧍 KARAKTER'di: ya BÜTÜN partlara koşulur
      ya HİÇ — en değerli bulgu (partlar ARASI kimlik erozyonu) boşluklu
      koşuda yakalanamaz. İlk koşunun 66 raporunun 6'sı bu mercekten geldi.
      ⛔ Bugün koşulamaz: rubriği `../QA_PROMPTLARI/ARSIV_6_MERCEK/
      KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` altında ARŞİVDE ve
      ÇALIŞTIRILMAZ damgalı (22.08.2026'da 6 mercekli sistem kapandı).
   ⭐ Videoyla birlikte ÜÇ SATIR yazılır, bu adım ATLANAMAZ:
        FILM: <ad> · PART: n/20 · TC: ~in–out
      Atlanırsa model kendine SAHTE part numarası ve timecode uydurur
      (ilk koşuda üç ayrı partta oldu).
   · Gelen rapor OLDUĞU GİBİ kaydedilir — ham çıktı düzenlenmez.
2. Ara analiz ajan işidir (her 3-5 partta bir çapraz okuma).
3. SENTEZ yalnız 20 part bitince, TEK KEZ koşulur.
   ⛔ PART BAŞINA KOŞMA. İlk koşuda 18 kısır erken sentez yapıldı;
      sonuncusu girdisiz olduğu hâlde VAR OLMAYAN 8 partlık sentez UYDURDU.
4. Ders çıktıysa eleme yapılır: yalnız (a) üretim hattımıza uygulanabilen,
   (b) sayısal kilide çevrilebilen, (c) bilinen bir zayıflığımızı kapatan
   dersler kalır. Oradan kart G ile LESSONS_LEARNED'a geçer.
```

⛔ **Bu bir QA değildir.** QA bizim yapımlara **puan verir**
(`../QA_PROMPTLARI/`); analiz bir filmi **söker**. Skoru yoktur, skor
tablolarına girmez, `sayac.sh` film sayımına GİRMEZ.

---

## 📝 DEĞİŞİKLİK KAYDI

```
05.09.2026  ⛔ film_analizleri/ KALDIRILDI (kart H2 · sahip kararı).
            İki şey kurtarıldı ve buraya taşındı (gerekçeler AYRI, bkz. baş
            kutusu): NOBODY_WAS_ALIVE ders seçkisi → kural ③ (dışarıdan atıf
            alıyordu) · dört analiz promptu → dış atfı yoktu, "yeniden yazmak
            pahalı" gerekçesiyle. Kaldırılan geri kalan içerik:
            · ANALIZ_EDILEN_FILMLER/NOBODY_WAS_ALIVE_WHEN_WE_LANDED/
              (73 dosya · 66 ham parça raporu · 50_TAM_FILM_ANALIZI ·
               70_KARSILASTIRMA · sentez paketi) — git'te DURUYOR,
              `git show e9bcf36:film_analizleri/...` ile okunabilir
            · ANALIZ_EDILEN_FILMLER/CORAK_TOPRAKLAR_HAREMININ_HUKUMDARIYIM/
              (16 rapor · 16:32) — ⛔ HİÇBİR COMMIT'TE YOKTU, GERİ ALINAMAZ
            · ANALIZ_QA_PROMPTLARI/DIKEY_4_PARCA/ (4 parça × tek kapsamlı
              prompt) — ⛔ HİÇBİR COMMIT'TE YOKTU, GERİ ALINAMAZ

15.08.2026  ⭐ İLK VE TEK TAMAMLANMIŞ KOŞU — NOBODY WAS ALIVE WHEN WE
            LANDED (69 dk · 20 parça · 66 rapor = 3 mercek × 20 + 6 KARAKTER).
            Hattın dört süreç dersi bu koşudan çıktı; üçü yukarıdaki akışta
            CANLI kural, dördüncüsü (KARAKTER merceği "hep ya da hiç") artık
            koşulamaz — rubriği 22.08.2026'da arşive kalktı, akışta ⚠️ olarak
            kayıtlı.

14.08.2026  Tek birleşik parça promptu üç merceğe bölündü (KAMERA · OLAY ·
            TEMA), SENTEZ üç merceği birleştirecek şekilde güncellendi.

14.08.2026  Hat açıldı (kilavuzlar_ve_sistem_dosyalari/FILM_ANALIZ →
            depo kökünde film_analizleri/).
```
