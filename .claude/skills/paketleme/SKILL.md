---
name: paketleme
description: Yeni hat faz 6 (kapak konsepti), faz 9 (final kapak · İngilizce yayın paketi · bilim doğrulaması · sahibin yayın onayı) ve faz 10 (yayın sonrası tutma eğrisi geri beslemesi) prosedürü. /yeni-film tarafından dosya olarak okunur; sahip /paketleme ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, AskUserQuestion, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*)
---

# Paketleme — faz 6 · faz 9 · faz 10

Kanal kararları bağlayıcıdır: `apexaic/KANAL_KIMLIGI.md` · `apexaic/youtube/PAKETLEME_SABLONU.md`.
Paket tamamen İngilizcedir. Faz döngüsü: `yeni-film` §2.

## §F6 — Kapak konsepti (faz 5'ten sonra; vaat erken kilitlenir)

1. **kapak-tasarimcisi** (faz 6) → `KAPAK_VE_YAYIN.md` §1 taslağı: 2-3 aday (`uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §7), her biri için tek cümlelik "görünen tarif".
   Çıktı: `ODA/F6_kapak-tasarimcisi_<tur>.md`.
2. **Paralel eleştiri:**
   - **izleyici** (KAPAK modu): yalnız adayların "görünen tarif"i.
   - **yonetmen** (faz 6 modu): an filmde var mı, ışık ve ölçek filmle aynı mı.
   - **yayin** (eleştirmen modu): vaat filmde var mı, spoiler veriyor mu.
3. **Yerleştir** → `KAPAK_VE_YAYIN.md` §1. Kapak anının çekimi `FILM.md` §4'te işaretlenir:
   risk sütununa "KAPAK ANI — kesilemez".
4. **Kapı:** Fable (F6 listesi).

## §F9 — Paket ve yayın onayı

1. **Final kapak** (`uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §7): sahip adayları aynı referanslarla üretir (varsayılan) ya da kapak-tasarimcisi gerçek bir kare seçer (dosya + saniye).
   - Her aday için `python3 uretim_hatti/araclar/kareler.py kapak <aday.png> --hedef ~/film_medya/<FILM>/izleyici/kapak/<A|B|C>/`
     → 360×202 · 168×94 · 120×68 · gri + `kapak.json`. 1280×720 uyarısı aşılamaz; bayraklar küçük kopyaya bakılarak kararlı.
   - **izleyici** (KAPAK modu, dosya yoluyla `168x94_masaustu_onerilen.png` ve `120x68_mobil_onerilen.png`): ne görüyor, tıklar mı.
   - Vaat denetimi bitmiş filme karşı: kapaktaki her varlığın göründüğü saniye. Test & Compare sırası: A ilk.
2. **yayin** (faz 9) → `YAYIN_PAKETI.md`: tamamen İngilizce, yapıştırmaya hazır başlık seçenekleri, açıklama,
   etiketler, sabit yorum, Shorts metni, kaynaklar, vaat denetimi. **bilim-danismani** (koşullu) her bilim
   cümlesini web'de doğrular. Düzeltmeler yayin'a geri gider.
   - Mekanik denetim: `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum yayin`. Karakter sayımı,
     kanal sabit bloğu, tam 3 hashtag, etiket ≤500, Türkçe karakter yok.
   - YouTube Studio'daki "Altered or synthetic content" kutusunu **sahip** işaretler; paket yalnız hatırlatır.
3. **İzleme:**
   - sahibin İzleme Formu A'sı (son taslak);
   - **en az 2 dış izleyici** (B): hikâyeyi bilmeyen gerçek insanlar;
   - Gemini anlatım testi (`uretim_hatti/QA_PROMPTLARI/ANLATIM_TESTI.md`, yeni sohbet, yalnız sesli video).
     Duyulan replikler (madde 7) §5 replik tablosuyla karşılaştırılır; A3/A4 satırları ses düzeltmesine gider.

   Sonuçlar `NOTLAR.md`'ye.
   - Gemini cevabını `FILM.md` §4 "anlatacağı bilgi" ile karşılaştır → `NOTLAR.md` ANLATIM.
   - İki ya da daha fazla kişinin koptuğu an → kurgu ya da çekim düzeltmesi (faz 8'e dön).
4. **Kapı:** `denetci` (Ö + F9). F9.1 ve F9.5 mekaniktir.
5. **Sahibin yayın onayı:** `AskUserQuestion`. Önce şunları göster:
   - `YAYIN_PAKETI.md` §1-§3: önerilen başlık, seçenekler, açıklama;
   - kapak A/B dosyaları;
   - izleme özeti;
   - `DURUM.md` AŞILAN KAPILAR: Fable'ın aştığı her yargı maddesi, gerekçesiyle.

   Seçenekler: yayınla · şunu düzelt (Diğer) · beklet. Cevap `DURUM.md` SAHİP CEVAPLARI'na.
6. Yayından ÖNCE kimlik kaydı `NOTLAR.md` KARARLAR'a: hangi başlık, hangi kapak, yayın saati.
   Sonradan hatırlanamaz.
7. Yayından ÖNCE açılış deney satırı (`IZLEYICI_VERISI.md` §3b, KABUL F9.7): test edilen tek açılış değişkeni,
   H1/H2/H3 ve başlık ile ilk replik saniyeleri `FILM.md` §4 AÇILIŞ tablosundan (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §8).

## §F10 — Geri besleme (yayından 48-72 saat sonra)

> Ne alınır, nasıl alınır, nereye yazılır: `uretim_hatti/IZLEYICI_VERISI.md` (07.10.2026).

1. Sahip YouTube Studio tutma eğrisini getirir (ekran görüntüsü ya da düşüş saniyeleri).
2. Her belirgin düşüş saniyesi → `kurgu.py liste <timeline> --zaman MM:SS` → hangi çekim.
3. `NOTLAR.md`'ye satır: saniye · çekim · anlatacağı bilgi · o çekimde tarama/izleyici ne demişti.
3b. **Giriş oranı** (30. saniye) ve trafik karışımı → `IZLEYICI_VERISI.md` §3 ve §3b. Kanalın tipik bandının altındaysa
   ilk 30 saniyeden kare çıkar (`kareler.py cikar <final> --aralik 1`) ve `uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2-§6 ile karşılaştır;
   bulgu NOTLAR'a. Eski videonun başını Studio'da kırpmak sahibin kararıdır (kılavuz §8).
3c. **Kapak ve başlık:** yüzeye göre tıklama oranı ve ortalama izlenme; Test & Compare sonucu (kazanan · aynı · sonuçsuz) → NOTLAR. Eski video bakımı (`uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §9): çok gösterim + düşük oranlı videolar için yeni kapak adayları, mevcut kapak ilk sırada test edilir; test yoksa bir kez değiştir, 14 gün dokunma; satır `IZLEYICI_VERISI.md` §3c.
4. ⛔ Tek filmin verisi kural olmaz. Aynı tür düşüş iki ayrı filmde kayıtlıysa sahibe
   "ARIZA_LISTESI'ne / BILINEN_TUZAKLAR'a girsin mi?" diye sorulur (AGENTS.md §1 ④).
