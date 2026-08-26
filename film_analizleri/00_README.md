# 🎞️ film_analizleri — Dış Film Analiz Sistemi

> **Amaç:** Beğenilen, **bizim yapmadığımız** bir filmi **20 eşit parçaya**
> bölüp her parçayı ÜÇ ayrı mercekle analiz etmek — kamera, olay/sahne,
> tema — sonra tüm raporları tek bir sentez raporunda birleştirmek.
>
> Bu klasör depo kökünde AYRI durur: buradaki filmler bizim üretimimiz
> değildir. QA DEĞİLDİR — QA bizim yapımlara **puan verir**
> (`../kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/`); analiz bir filmi
> **söker** — nasıl kurulmuş, hangi kamera diliyle anlatılmış, tema nereden
> geçiyor. Skoru yoktur, skor tablolarına girmez, sayac.sh film sayımına
> GİRMEZ.

---

## 📦 KLASÖR YAPISI

```
film_analizleri/
├── 00_README.md                    ← bu dosya
├── ANALIZ_QA_PROMPTLARI/           🔍 GİRDİ — salt promptlar (dosyada
│   │                                  SADECE video ile verilecek prompt var)
│   ├── KAMERA_ANALIZ_PROMPT.md        parça → shot list, açı/ölçek/hareket,
│   │                                  kesme ritmi, kamera dili
│   ├── OLAY_ANALIZ_PROMPT.md          parça → sahne envanteri, beat beat
│   │                                  olaylar, diyalog, dramaturji
│   ├── TEMA_ANALIZ_PROMPT.md          parça → motif, ışık/renk, ses, tema
│   └── SENTEZ_ANALIZ_PROMPT.md        tüm parça raporları (metin) → bütün film
│                                      (opsiyonel 4. mercek: ../kilavuzlar_ve_
│                                       sistem_dosyalari/QA_PROMPTLARI/
│                                       KARAKTER_DEVAMLILIK_QA — segmente koşulur)
└── ANALIZ_EDILEN_FILMLER/          📊 ÇIKTI — film başına bir klasör
    └── <FILM_ADI>/
        ├── 00_KUNYE.md                künye · parça haritası · koşu tarihçesi
        ├── PARCA_01_KAMERA.md         ham raporlar (model çıktısı,
        ├── PARCA_01_OLAY.md            olduğu gibi — düzenlenmez)
        ├── PARCA_01_TEMA.md
        ├── PARCA_01_KARAKTER.md       (opsiyonel 4. mercek)
        ├── … (parça 02-20 aynı set)
        ├── 50_TAM_FILM_ANALIZI.md     ⭐ ajanın çapraz okuması — ara analiz
        │                                 olarak başlar, 20 partta kapanır
        ├── 60_DERS_SECKISI.md         ⭐ elenmiş dersler — kart G girdisi
        ├── 70_KARSILASTIRMA.md        ⭐ kaynak film ↔ bizim filmler:
        │                                 ölçülmüş fark + ÖLÇÜ KARTI
        ├── 90_ERKEN_SENTEZ_KOSULARI.md  varsa: kısır koşu arşivi
        ├── 91_SENTEZ_PAKETI_RAPORLAR.md sentez girdisi (etiketli birleşim)
        ├── 92_SENTEZ_KOSU_TALIMATI.md   sentez nasıl koşulur
        └── 99_SENTEZ_RAPORU.md        model sentezi (opsiyonel 2. okuma)
```

**Adlandırma:** `BUYUK_HARF_ALT_CIZGI` · Türkçe karakter yok · parça
numarası iki hane (`PARCA_01`, `PARCA_07`).

---

## ⭐ İŞ BÖLÜMÜ VE AKIŞ

**Operatör** filmi böler, promptları koşar, raporları ajana iletir.
**Ajan** film klasörünü açar, KUNYE'yi yazar, gelen raporları dosyalara
kaydeder. Promptlar QA rubrikleriyle aynı **salt prompt ilkesiyle**
yazıldı: dışarıdaki modele **medya + tek .md dosyası** verilir, başka hiçbir
şey.

```
0. HAZIRLIK
   · Operatör filmi 20 parçaya böler (toplam süre ÷ 20).
     ⚠️ Eşit kesilemiyorsa her parçanın SÜRESİNİ kaydet — timecode
        haritası yoksa sentez sıralamayı tahmin etmek zorunda kalır.
   · Ajan ANALIZ_EDILEN_FILMLER/<FILM_ADI>/ klasörünü ve 00_KUNYE.md'yi açar.

1. PARÇA ANALİZİ (parça başına 3-4 koşu)
   · Prompt dosyasının TAMAMI kopyalanır + parça videosu yüklenir
   · ⭐ VİDEOYLA BİRLİKTE ÜÇ SATIR YAZILIR — bu adım ATLANAMAZ:
        FILM: <ad> · PART: n/20 · TC: ~in–out
     Atlanırsa model kendine SAHTE part numarası ve timecode uydurur
     (ilk analizde üç ayrı partta oldu — bkz. NOBODY_WAS_ALIVE §süreç).
   · Gelen rapor ajana iletilir → ajan OLDUĞU GİBİ
     PARCA_<nn>_<MERCEK>.md dosyasına kaydeder — düzenleme yok
   · Opsiyonel 4. mercek (🧍 KARAKTER, QA_PROMPTLARI'ndan) koşulacaksa
     BÜTÜN partlara koşulur; boşluklu koşu en değerli bulguyu (partlar
     ARASI kimlik erozyonu) yakalayamaz.

2. ARA ANALİZ (ajan işi — her 3-5 partta bir)
   · Ajan biriken raporları çapraz okur: karakter eşleme tablosu, yapı,
     motif takibi, çelişki defteri, ders adayları.
   · 20 part bitince bu dosya 50_TAM_FILM_ANALIZI.md olur ve kapanır.

3. SENTEZ — OPSİYONEL İKİNCİ OKUMA (yalnız 20 part bitince, TEK KEZ)
   ⛔ PART BAŞINA KOŞMA. İlk analizde 18 kısır erken koşu yapıldı;
      sonuncusu girdisiz olduğu hâlde VAR OLMAYAN 8 partlık sentez
      UYDURDU. Erken sentez bilgi üretmez, uydurma riski taşır.
   · SENTEZ_ANALIZ_PROMPT.md + tüm raporların METNİ (video değil)
   · Raporların içindeki part numaraları güvenilmezse, pakete ajan
     tarafından GERÇEK part başlıkları eklenir (91_SENTEZ_PAKETI örneği)
   · Gelen rapor 99_SENTEZ_RAPORU.md dosyasına kaydedilir ve ajanın
     kendi okumasıyla KARŞILAŞTIRILIR

4. DERS ÇIKTIYSA
   · Ajan ders adaylarını 60_DERS_SECKISI.md'de eler: yalnız (a) üretim
     hattımıza uygulanabilen, (b) sayısal kilide çevrilebilen,
     (c) bilinen bir zayıflığımızı kapatan dersler kalır.
   · Oradan AGENTS.md görev kartı G ile LESSONS_LEARNED sistemine geçer.
     ⚠️ Dış film dersleri için kart G adım 5 ("önce kaynak rubriği
        yamala") GEÇERSİZDİR — yamanacak rubrik yok; ders doğrudan
        ilgili ÜRETİM kılavuzuna işlenir.
```

⛔ **Parça raporu ham çıktıdır** — QA sistemindeki `02_HAM_RAPORLAR` kuralının
aynısı: modelin çıktısı düzenlenmeden kaydedilir. Yorum/özet gerekiyorsa
`00_KUNYE.md`'ye yazılır, parça dosyasına dokunulmaz.

⛔ **Prompt dosyalarına Türkçe not/tarihçe YAZILMAZ** — salt prompt ilkesi.
Akış ve tarifin evi bu README'dir.

---

## 🧭 NEDEN 20 PARÇA × 3 MERCEK?

Tek geçişte bütün filmi analiz eden model detay kaybeder — kamera ölçeği,
kesme ritmi, mizansen ilk 2-3 dakikadan sonra genelleşir. Parça kısaldıkça
rapor **shot-list çözünürlüğüne** iner. Mercekler ayrıldıkça da tek koşu
tek iş yapar: kamera raporu tema yorumuyla, olay raporu shot listesiyle
sulanmaz (QA sistemindeki mercek ayrımıyla aynı gerekçe). Sentez promptu
60 yüksek çözünürlüklü raporu birleştirir; bütünün deseni (tempo eğrisi,
motif haritası, kamera imzası) parçalardan çıkar.

---

## 📝 DEĞİŞİKLİK KAYDI

```
15.08.2026  ⭐ İLK FİLM TAMAMLANDI — NOBODY WAS ALIVE WHEN WE LANDED
            (69 dk · 20 parça · 66 rapor). Sistem bu koşudan dört süreç
            dersi aldı, hepsi yukarıdaki akışa işlendi:
            ① header koşu başına doldurulur — atlandı, üç part kendine
              sahte part numarası/timecode uydurdu
            ② SENTEZ part başına koşulmaz — 18 kısır koşu oldu ve
              sonuncusu girdisiz olduğu hâlde 8 partlık sentez UYDURDU
            ③ parçalar eşit kesilmezse süreleri kaydedilir — 2:24-4:37
              arasında oynadı, timecode haritası tahmine kaldı
            ④ opsiyonel KARAKTER merceği ya bütün partlara koşulur ya
              hiç — en değerli bulgu partlar ARASI kesişimden çıkıyor
            İki yeni çıktı dosyası standartlaştı:
            50_TAM_FILM_ANALIZI.md (ajanın çapraz okuması) ·
            60_DERS_SECKISI.md (elenmiş dersler, kart G girdisi)

14.08.2026  Tek birleşik PARCA_ANALIZ_PROMPT üç ayrı merceğe bölündü
            (KAMERA · OLAY · TEMA — parça başına üç koşu), SENTEZ üç
            merceğin raporlarını birleştirecek şekilde güncellendi.
            İş bölümü netleşti: operatör koşar, ajan dosyalar.

14.08.2026  Klasör kilavuzlar_ve_sistem_dosyalari/FILM_ANALIZ'den depo
            köküne film_analizleri/ olarak taşındı — dış filmler üretim
            sistemine karışmasın diye.

14.08.2026  Klasör açıldı. Henüz hiç film analiz edilmedi.
```
