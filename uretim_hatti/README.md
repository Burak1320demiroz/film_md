# 🏭 ÜRETİM HATTI — yeni hat (05.10.2026)

Giriş noktası tek: **`/yeni-film`**. Yeni bir film başlatır ya da `ODA/DURUM.md`'den
kaldığı yerden sürdürür. Ana ajan **Fable**'dır (`.claude/settings.json`). Faz
kapılarını o onaylar. Sahibin onayı iki yerde kalır: **hikâye seçimi** (veto hakkı) ve
**yayın**. Kontrat: `../AGENTS.md`.

## Ne nerede

```
uretim_hatti/
  README.md               bu dosya
  BILINEN_TUZAKLAR.md     kanıtlı tuzaklar — yazarların ve teknik eleştirmenlerin zorunlu okuması (AJAN HARİTASI)
  ARIZA_LISTESI.md        ölçülmüş hikâye (H) · teknik (T) · QA (Q) arızaları — eleştirmenlerin sözlüğü
  ELESTIRI_PROTOKOLU.md   eleştiri biçimi · şiddet · tur kuralı
  KABUL_LISTELERI.md      faz kapıları — denetci okur, Fable karar verir
  FLOW_GERCEKLERI.md      Google Flow olgu sayfası (mod ↔ model, süre, 4K, kredi, ses, müzik) — araç bilgisi yalnız buradan
  PROMPT_HATA_ATLASI.md   kanıtlı prompt kalıpları: bunu yazma → şunu yaz (14 girdi + karantina)
  GOSTERIM_COZUMLERI.md   zor anı kadraj, kesme ve sesle gösterme kataloğu
  GECIS_VE_SES_SUREKLILIGI.md  klipler arası keskin kesme + kesmede değişen arka ses çözümü (12.10.2026): prompt · yatak · geçiş (kurgu.py gecis/yataklar/klip_sesi)
  ILK_30_SANIYE_KILAVUZU.md    ✅ (12.10.2026) her filmde açılış hook'u: üç çekim iskeleti · vaat · sessiz okunurluk · üretim · deney defteri (ARASTIRMA/07 → 08)
  KAPAK_VE_BASLIK_KILAVUZU.md  ✅ (12.10.2026) yüzeyler · okunurluk · kareler.py kapak · başlık kalıbı · üretim yolu ve vaat sınırı · test · eski video bakımı (ARASTIRMA/09 → 10)
  QA_OKUMA_KILAVUZU.md    QA bulgusu → zaman → çekim → prompt → sınıf (sözleşme v1.0) — rapor-prompt skill'inin omurgası
  IZLEYICI_VERISI.md      yayın sonrası YouTube verisi: ne, nasıl, nereye, nasıl okunur
  AJAN_GOREVLERI.md       alt ajanlara verilen sabit görev metinleri
  QA_PROMPTLARI/          4 QA promptu (06.10.2026): Gemini için TARAMA (klip içi) · SUREKLILIK (kesme iki yanı) ·
                          ANLATIM_TESTI (plansız izleyici) · insan için IZLEME_FORMU. Eski 15 mercek arşivde.
  ARASTIRMA/              dış derin araştırma promptları (salt prompt: 01 · 03 · 05) · ham/ cevaplar · süzme (02 · 04 · 06) · kural dosyaların sonunda
  SABLON/                 yeni film klasörünün şablonu (FILM · SAHNELEME · KAPAK_VE_YAYIN · YAYIN_PAKETI · NOTLAR · timeline · ODA · PROMPTLAR)
  araclar/                film_dogrula · kurgu · kareler · kor_ab · izleyici_kanca · ham_rapor_say
  test/                   kos.py (tek komut regresyon) · ornekler/ (yalnız metin; geçerli + kasıtlı bozuk film klasörleri)

.claude/agents/           18 alt ajan (senarist, diyalog-yazari, dramaturg, izleyici, yonetmen,
                          teknik-danisman, goruntu-yonetmeni, devamlilik, bilim-danismani,
                          ses-tasarimcisi, besteci, kapak-tasarimcisi, yayin, kurgucu, denetci,
                          sahneleyici, mekan-haritacisi, zincir-bekcisi)
.claude/skills/yeni-film  yönetici akış (tek otomatik tetik)
.claude/skills/{hikaye-odasi, sahneleme-odasi, ses-muzik, cekim-yaz, paketleme, klip-sec}
                          faz prosedürleri — ana ajan dosya olarak okur; sahip /adıyla çağırabilir
```

## Film klasörü

```
<FORMAT>_filmler/<FILM>/   (yatay_2_dk · yatay_4_dk · yatay_8_dk · yatay_16_dk · dikey_shorts; künye: FORMAT · HEDEF_SURE;
                      her çekim 10 s → çekim sayısı = HEDEF_SURE/10; ayrı filmler/ kökü yok — 08.10.2026)
  FILM.md            hikâye · tretman · görsel kimlik · çekim listesi (+ zincir sütunları) · replikler · ses + müzik planı
  SAHNELEME.md       zincirler · anahtar kareler · mekân haritası · delta kontrolü (sahneleme odası)
  KAPAK_VE_YAYIN.md  kapak A/B
  YAYIN_PAKETI.md    tamamen İngilizce, yapıştırmaya hazır: başlık · açıklama · etiket · sabit yorum · Shorts
  PROMPTLAR/G01.md…  çekim grubu başına promptlar + Flow iş emri
  ODA/               ajanların ham çıktıları (F<faz>_<ajan>_<tur>.md) + DURUM.md
  NOTLAR.md          denemeler · işaretleme · red · tarama · anlatım · izleme · kararlar · ajan günlüğü
  timeline.json      seçilen saniyeler
```

## Medya

```
~/film_medya/<FILM>/          (repo dışı · görsel, video ve ses repoya girmez)
  ref/        onaylı referanslar, numaralı, özne başına TEK sayfa: <No>.<AD>_v<k>.png (1.KARAKTER_v1.png · 2.MEKAN_v1.png …; No = FILM §3, sabit; açılar/yüz/durumlar aynı görselde panel)
  kare/       yalnız Flow'a GİREN kareler: başlangıç Cxx.png · anahtar kare Zk.n.png
  ham/        Flow'dan inen denemeler: Cxx_dN.mp4
  ses/        R01.wav replik · E01.wav efekt · O01.wav ortam · muzik_v1.wav
  cikti/      taslak_*.mp4 · final.mp4 · kapak_A.png / kapak_B.png
  analiz/     türetilen, izleyiciye gitmeyen: kareler/<deneme>/ · tarama/<Cxx>/ · dikis/<Zk>_<i>/ · kor/<tur>/
  izleyici/   YALNIZ izleyici ajanının okuyabildiği (kanca): taslak_<n>/ · animatik_<n>/ · kapak/
```
⛔ `izleyici/` altına yalnız izleyiciye gösterilecek kare kopyalanır; kanca başka yeri okutmaz.
⛔ Analiz çıktıları (`kareler.py` · `kor_ab.py`) `analiz/` altına yazılır, `kare/`'ye değil. `kare/` Flow'a girdi demektir.

## Komutlar

```bash
python3 uretim_hatti/araclar/film_dogrula.py <FILM klasörü>          # yapı/biçim kontrolü (+ --bolum yayin: faz 9)
python3 uretim_hatti/araclar/kurgu.py kontrol|liste|taslak <timeline>  # seçim → taslak film
python3 uretim_hatti/araclar/kurgu.py yukseklik <video> [--uygula]     # final ses −14 LUFS · −1 dBTP
python3 uretim_hatti/araclar/kareler.py cikar|kucult|kare|dikis|kuyruk …  # kare · kontak · dikiş · kuyruk
python3 uretim_hatti/araclar/kor_ab.py karistir|ac …                   # kör karşılaştırma
python3 uretim_hatti/araclar/ham_rapor_say.py                          # eski QA raporlarının sayımı
python3 uretim_hatti/test/kos.py [-v]                                 # araç değiştiyse: bütün testler (medya geçici üretilir)
```
