---
name: ses-muzik
description: Yeni hat faz 4 (ses + müzik planı) ve faz 8 müzik finali prosedürü. /yeni-film tarafından dosya olarak okunur; sahip /ses-muzik ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*)
---

# Ses ve müzik — faz 4 · faz 8 (müzik)

Ortak kural: **modelin ürettiği ses kullanılmaz**. Taslakta atılır (`kurgu.py`), ham
dosyada kalır. Bütün ses kurguda bu planla kurulur.

- İstisna 1: `FILM.md` §5'te Kaynak = ağız kadrajda olan replik. O repliğin sesi klipten alınır (`timeline.json` ses parçası `giris`/`cikis` ile).
- İstisna 2 (sahip kararı 12.10.2026): Kaynak = **model sesi (…)** olan replik: Omni konuşmayı videoda üretir; o parça `timeline.json`'da
  `klip_sesi: true` (klibin sesi yalnız replik için filme girer, yatak yine kurgudan); kurgu kaydı yedek.
- Sahip kararı (06.10.2026): her filmde ortam yatağı + efekt + diyalog + müzik olur.
- Sahip kararı (12.10.2026, `uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md`): kesmede arka ses komple değişmez → mekân başına TEK kesintisiz
  yatak klipleri aşar (§6 ORTAM YATAĞI), her kesmeye geçiş türü + ses köprüsü (§6 GEÇİŞ), müzik kesmede kesilmez; **her filmde müzik
  promptu** `FILM.md` §7 `### MÜZİK PROMPTU` (F4 taslak, F8 kesin; `film_dogrula.py --bolum muzik`).

Faz döngüsü: `yeni-film` §2. Görev metinleri: `uretim_hatti/AJAN_GOREVLERI.md`.

## §F4 — Ses + müzik planı (tavan 2 tur)

1. **Yazarlar:** ses-tasarimcisi ve (MUZIK var ise) besteci. İkisi aynı mesajda paralel çağrılabilir;
   ikisinin de girdisi `FILM.md` §1-§5.
   - `ODA/F4_ses-tasarimcisi_<tur>.md`: sahne tablosu · ORTAM · KAYIT LİSTESİ · EFEKT LİSTESİ (her çekim) · ORTAM YATAĞI tablosu (mekân başına,
     klipleri aşar) · GEÇİŞ tablosu taslağı · (model sesi AÇIK filmde) mekân başına ORTAM SESİ cümlesi.
   - `ODA/F4_besteci_<tur>.md`: okuma cümlesi · müziksiz an · yaklaşık vuruş/susma · dinamik tablo · **MÜZİK PROMPTU taslağı** (```text, İngilizce).
2. **Paralel eleştiri:**
   - **kurgucu** (eleştirmen modu): müzik vuruşları ve susmaları çekim listesindeki kesmelere oturuyor mu; doruk müziksiz mi.
   - **diyalog-yazari** (koşullu, eleştirmen modu): replik yerleşimi, müzikle çakışma, ağız kadrajda mı.
   - **ses-tasarimcisi ↔ besteci:** biri diğerinin planındaki çakışmayı tek satırla yazabilir.
     İkinci yazar çağrısında karşı planı da girdi olarak ver.
3. **Yerleştir:** ses tablosu + ORTAM YATAĞI + GEÇİŞ tabloları → `FILM.md` §6; ORTAM SESİ cümleleri → §3. Müzik planı + MÜZİK PROMPTU taslağı → §7.
   Kayıt listesi ve efekt listesi ODA dosyasında kalır. §6'ya yolu yazılır.
4. **Mekanik kontrol:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum replik muzik` (müzik promptu M · yatak/geçiş uyarısı). **Kapı:** `denetci` (Ö + F4) → Fable.
5. **Sahibe iş listesi:** replik kayıt listesi + efekt listesi.
   - Her konuşan kendi tek ses profiliyle kaydedilir (diyalog-yazari SES PROFİLİ): aracı sahip seçer.
   - Replikler `~/film_medya/<FILM>/ses/R01.wav …`, efektler `ses/E01.wav …`, ortam yatakları `ses/yatak_<mekan>.wav` adlarıyla (§6 ORTAM YATAĞI tablosundaki dosya adı; mekân başına tek dosya, en az yatağın süresi kadar ya da döngü dikişi duyulmayan kayıt).
   - Ağız kadrajdaki ve model sesi repliklerin kaydı yok: ses klipten gelir (model sesi için yedek kayıt yalnız SMOKE P18 tutmazsa istenir).

## §F8 — Müzik finali (kurgu kesinleşince)

1. `python3 uretim_hatti/araclar/kurgu.py liste <FILM>/timeline.json` → kesme noktaları tablosu.
2. **besteci** (faz 8): kesme noktaları + faz 4 planı → İngilizce Flow Music promptu (kesin) +
   KESME NOKTALARI tablosu. Çıktı: `ODA/F8_besteci_<tur>.md` → `FILM.md` §7 `### MÜZİK PROMPTU` kesin sürüm (F4 taslağı tarihle altında kalır).
3. **kurgucu** (eleştirmen modu): vuruşlar gerçekten kesmelere oturuyor mu; müzik hiçbir kesmede kesilmiyor mu (planlı susmalar hariç).
4. **Sahibe iş:**
   - Google Flow Music'te üretim (resmî ürün, eski adı ProducerAI; Lyria 3.5); indirme `~/film_medya/<FILM>/ses/muzik_v1.wav`.
   - ⚠️ Ticari kullanım: resmî kaynakta açık izin cümlesi YOK; yalnız Google Hizmet Şartları ("Google won't claim ownership over that content").
     Para kazanan yayından önce sahip koşulları kendisi kontrol eder (`apexaic/POLITIKA_VE_RISK.md` §4). "Ücretli plan gerekir" ve "14 gün içinde silinir" bilgileri doğrulanmadı (`ARASTIRMA/04_SUZME_20261007.md` R8); dosyayı yine hemen indir.
5. Müzik, efektler ve replikler `timeline.json` → `ses` listesine (başlangıç saniyesi + kazanç; gerekirse `giris`/`cikis` ve `solma`);
   ortam yatakları → `yataklar` listesine (mekân başına, `baslangic`/`bitis` klipleri aşar, `gecis` 1-2 s örtüşme = çapraz geçiş);
   model sesi replik taşıyan parçalar `klip_sesi: true`. `kurgu.py taslak` sesli taslak üretir.
6. **Final yükseklik:** `python3 uretim_hatti/araclar/kurgu.py yukseklik <taslak.mp4>` ölçer. Hedef −14 LUFS · ≤ −1 dBTP.
   - Tutmuyorsa `--uygula -o ~/film_medya/<FILM>/cikti/final.mp4` iki aşamalı doğrusal düzeltme yapar.
   - Tepe aşılırsa miksteki en yüksek an kısılır ve tekrar koşulur.
