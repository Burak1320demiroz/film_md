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
                          yeni hat adayları (16.10.2026, sahip kararı bekliyor): ARASTIRMA/16_QA_PROMPT_DERSLERI (5 film · 269 bulgu · 13 ders Y1-Y13)
  GOSTERIM_COZUMLERI.md   zor anı kadraj, kesme ve sesle gösterme kataloğu
  GECIS_VE_SES_SUREKLILIGI.md  klipler arası keskin kesme + kesmede değişen arka ses çözümü (12.10.2026): prompt · yatak · geçiş (kurgu.py gecis/yataklar/klip_sesi)
  ILK_30_SANIYE_KILAVUZU.md    ✅ (12.10.2026) her filmde açılış hook'u: üç çekim iskeleti · vaat · sessiz okunurluk · üretim · deney defteri (ARASTIRMA/07 → 08)
  KAPAK_VE_BASLIK_KILAVUZU.md  ✅ (12.10.2026) yüzeyler · okunurluk · kareler.py kapak · başlık kalıbı · üretim yolu ve vaat sınırı · test · eski video bakımı (ARASTIRMA/09 → 10)
  GPT_IMAGE_OMNI_KILAVUZU.md   (16.10.2026) GPT Image karesi → Gemini Omni hareketi: pilot · referans/durum · kare düzeltme · devamlılık · diyalog · sorun-aşama · kayıt (ARASTIRMA/ham/26 → 11; K1-K8 sahipte)
  REPLIK_VE_KLIP_SESI_KILAVUZU.md  (16.10.2026) replik kaynağı seçimi · montaj öncesi ses kapısı · klip sesi ve vakum · telsiz filtresi (ARASTIRMA/12 → 13)
  KIMLIK_VE_REFERANS_KILAVUZU.md   (16.10.2026) yüz/giysi/bant tutarlılığı · ≤3 referans + rol · sayılı giysi tarifi · düzeltme · P17 deneyi · kare kabul listesi
  UZAY_FIZIGI_GORUNTU_KILAVUZU.md  (16.10.2026) vakumda itki, sıvı, EVA, itki yönü, Dünya hızı, kenetlenme: kamerada görünen + olumlu İngilizce tarif
  FRAGMAN_KILAVUZU.md              (21.10.2026) fragman yeni film değil · tek mekanik · spoiler kapısı kurguda ve pakette · 10 s dilim (FURNACE emsali) · ikinci fragman (eski FRAGMAN + PAKETLEME → ARASTIRMA/24)
  KURGU_SES_VE_MUZIK_KILAVUZU.md   (21.10.2026) plan ↔ kurgu eşlemesi · başlık kartı zincire girmez · tempo kesmeye hizalı · anempatik müzik · vakum sesi · ihraç (eski 3 kılavuz → ARASTIRMA/23)
  DUNYA_VE_TASARIM_KILAVUZU.md     (21.10.2026) ufuk ve arka plan nesnesi · yanaşma kadrajı · istasyon ölçüleri · kask çerçevesi, malzeme, kir · yüz · uzaylı canlı · kadro (eski 8 kılavuz → ARASTIRMA/22)
  KAMERA_VE_MEKAN_KILAVUZU.md      (21.10.2026) yön taşıyıcıları · mekân geçişi · ölçek çapası · konum/yönelim/hareket · ışık tetik kelimeleri · açı ve kurulum dizisi (eski 7 kılavuz → ARASTIRMA/21)
  HAREKET_VE_EFOR_KILAVUZU.md      (21.10.2026) temas ilk 2 s / kurulu, temas cümlesi yok · mikro → makro · yürüme platosu · efor dört parça · iki rejim · tripod (eski 11 kılavuz → ARASTIRMA/20)
  HIKAYE_YAPISI_KILAVUZU.md        (21.10.2026) novum karakteri zorlar · bedel bedende · jest en çok iki kez · film biter, doruk ve final kurgudan düşmez · tema · iki kişi (eski 8 kılavuz → ARASTIRMA/19)
  KARAKTER_VE_DIYALOG_KILAVUZU.md  (21.10.2026) karakter beş satırı · seçim kadrajda ve bedende · kesmede sıfırlanma yok · dolgu jesti yok · diyalog ekleri · model sesi tuzakları (eski 7 kılavuz → ARASTIRMA/18)
  SECIM_VE_KURGU_KILAVUZU.md       (16.10.2026) medya → seçim → timeline → taslak: beş karar · süreklilik · 10 s doldurma · ffmpeg kontrolleri · kim neyi görür · taslak kapısı
  QA_OKUMA_KILAVUZU.md    QA bulgusu → zaman → çekim → prompt → sınıf (sözleşme v1.0) — rapor-prompt skill'inin omurgası
                          (16.10.2026) hat dışı montajda QA numarası = kesme sırası → önce medya.py bol + NOTLAR MONTAJ EŞLEMESİ
  IZLEYICI_VERISI.md      yayın sonrası YouTube verisi: ne, nasıl, nereye, nasıl okunur
  AJAN_GOREVLERI.md       alt ajanlara verilen sabit görev metinleri
  QA_PROMPTLARI/          4 QA promptu (06.10.2026): Gemini için TARAMA (klip içi) · SUREKLILIK (kesme iki yanı) ·
                          ANLATIM_TESTI (plansız izleyici) · insan için IZLEME_FORMU. Eski 15 mercek arşivde.
  ARASTIRMA/              dış derin araştırma promptları (salt prompt: 01 · 03 · 05) · ham/ cevaplar · süzme (02 · 04 · 06) · kural dosyaların sonunda
                          qa_prompt_analizi_20261006/ (eski hat, 12 film) · qa_prompt_analizi_20261016/ (yeni hat, 5 film) → 16_QA_PROMPT_DERSLERI
  SABLON/                 yeni film klasörünün şablonu (FILM · SAHNELEME · KAPAK_VE_YAYIN · YAYIN_PAKETI · NOTLAR · timeline · ODA · PROMPTLAR)
  araclar/                film_dogrula (+ pilot · DERS uyarıları, 16.10) · medya (16.10: durum · al · bol) · kurgu · kareler ·
                          kor_ab · izleyici_kanca · ham_rapor_say
  test/                   kos.py (tek komut regresyon) · ornekler/ (yalnız metin; geçerli + kasıtlı bozuk film klasörleri)

.claude/agents/           18 alt ajan, 6 rolde (AGENTS §2b; sahneleyici · mekan-haritacisi · zincir-bekcisi ⏸️ yalnız zincir açıkken)
                          (senarist, diyalog-yazari, dramaturg, izleyici, yonetmen,
                          teknik-danisman, goruntu-yonetmeni, devamlilik, bilim-danismani,
                          ses-tasarimcisi, besteci, kapak-tasarimcisi, yayin, kurgucu, denetci,
                          sahneleyici, mekan-haritacisi, zincir-bekcisi)
.claude/skills/yeni-film  yönetici akış (tek otomatik tetik)
.claude/skills/{hikaye-odasi, sahneleme-odasi, ses-muzik, cekim-yaz, paketleme, klip-sec, medya-denetle}
                          faz prosedürleri — ana ajan dosya olarak okur; sahip /adıyla çağırabilir
                          (medya-denetle 16.10.2026: medyayı hatta alır, DURUM'u dosyaya getirir, hat dışı montajı böler)
```

## Film klasörü

```
<FORMAT>_filmler/<FILM>/   (yatay_2_dk · yatay_4_dk · yatay_8_dk · yatay_16_dk · dikey_shorts; künye: FORMAT · HEDEF_SURE;
                      her çekim 10 s → çekim sayısı = HEDEF_SURE/10; ayrı filmler/ kökü yok — 08.10.2026)
  FILM.md            hikâye · tretman · görsel kimlik · çekim listesi (+ zincir sütunları) · replikler · ses + müzik planı
  SAHNELEME.md       zincirler · anahtar kareler · mekân haritası · delta kontrolü (sahneleme odası)
  KAPAK_VE_YAYIN.md  kapak A/B
  YAYIN_PAKETI.md    tamamen İngilizce, yapıştırmaya hazır: başlık · açıklama · etiket · sabit yorum · Shorts
  PROMPTLAR/PILOT.md F3p pilot (1-3 çekim + KİMLİK CÜMLELERİ + PİLOT SORUSU, 16.10.2026)
  PROMPTLAR/G01.md…  çekim grubu başına promptlar + Flow iş emri + 8 SORU tablosu (G01 önce, kalanlar G01'i örnek alarak)
  ODA/               ajanların ham çıktıları (F<faz>_<ajan>_<tur>.md) + DURUM.md + MEDYA_DURUMU.md (medya.py üretir) +
                     F3p_pilot_karar.md · F5_uyari_cevaplari.md
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
  analiz/     türetilen, izleyiciye gitmeyen: kareler/<deneme>/ · tarama/<Cxx>/ · dikis/<Zk>_<i>/ · kor/<tur>/ ·
              montaj/<montaj adı>/ (medya.py bol: NN_ilk.png · NN_orta.png · bolum.md · bolum.tsv)
  izleyici/   YALNIZ izleyici ajanının okuyabildiği (kanca): taslak_<n>/ · animatik_<n>/ · kapak/
```
⛔ `izleyici/` altına yalnız izleyiciye gösterilecek kare kopyalanır; kanca başka yeri okutmaz.
⛔ Analiz çıktıları (`kareler.py` · `kor_ab.py`) `analiz/` altına yazılır, `kare/`'ye değil. `kare/` Flow'a girdi demektir.

## Komutlar

```bash
python3 uretim_hatti/araclar/film_dogrula.py <FILM klasörü>          # yapı/biçim kontrolü (+ --bolum yayin: faz 9 · pilot: F3p)
python3 uretim_hatti/araclar/medya.py durum|al <FILM> [--yaz]          # gerçek durum ↔ DURUM · NOTLAR DENEMELER satırları (16.10)
python3 uretim_hatti/araclar/medya.py bol <montaj.mp4> <FILM>          # hat dışı montajı kesmelerinden böl, başlangıç karesiyle eşle
python3 uretim_hatti/araclar/kurgu.py kontrol|liste|taslak <timeline>  # seçim → taslak film
python3 uretim_hatti/araclar/kurgu.py yukseklik <video> [--uygula]     # final ses −14 LUFS · −1 dBTP
python3 uretim_hatti/araclar/kareler.py cikar|kucult|kare|dikis|kuyruk …  # kare · kontak · dikiş · kuyruk
python3 uretim_hatti/araclar/kor_ab.py karistir|ac …                   # kör karşılaştırma
python3 uretim_hatti/araclar/ham_rapor_say.py                          # eski QA raporlarının sayımı
python3 uretim_hatti/test/kos.py [-v]                                 # araç değiştiyse: bütün testler (medya geçici üretilir)
```
