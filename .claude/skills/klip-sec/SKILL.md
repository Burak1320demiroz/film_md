---
name: klip-sec
description: Yeni hat faz 7 (denemeleri düzenleme, işaretleme, kareli animatik karşılaştırması) ve faz 8 (Gemini taraması, seçim, timeline, taslak kurgu, izleyici/dramaturg kontrolü) prosedürü. /yeni-film tarafından dosya olarak okunur; sahip /klip-sec ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(ffmpeg:*), Bash(ffprobe:*), Bash(ls:*), Bash(mkdir:*), Bash(cp:*)
---

# Klip seç — faz 7 · faz 8

Fable videonun hareketini **göremez**. Bu fazda karar dört kaynağa dayanır:
- sahibin işareti;
- Gemini taraması (zaman kodu + kanıt; puansız);
- kare sayfaları (`kareler.py`);
- izleyici / dramaturg.

"Bulunamadı" "temiz" demek değildir. Faz döngüsü: `yeni-film` §2.

> QA bulgusunu okuma, birleştirme, çekime eşleme ve sınıflama: `uretim_hatti/QA_OKUMA_KILAVUZU.md` (07.10.2026).

## §F7 — Denemeler ve işaretleme

1. **Düzen:** sahip denemeleri `~/film_medya/<FILM>/ham/Cxx_dN.mp4` adlarıyla indirir.
   Her deneme `NOTLAR.md` DENEMELER'e bir satır — **16.10.2026'dan beri `medya.py al <FILM> --yaz`** yazar: süre · ses akışı ·
   araç/mod · prompt (`G0n · p:sha8`) · girdi (kare + referans). Sonra `medya.py durum <FILM> --yaz`: adı kurala uymayan dosyaları
   sahibe yeniden adlandırma listesi olarak ver (`Gemini_Generated_Video_….mp4` → `ham/C07_d1.mp4`).
2. **İşaretleme (sahibin işi):** her deneme için ✅ kullanılabilir (aralıkla) ya da ❌ (tek cümle neden)
   → `NOTLAR.md` İŞARETLEME. ❌ olanlar `cekim-yaz` §F7 başarısız çekim döngüsüne gider.
3. **Kör karşılaştırma (isteğe bağlı, riskli çekimde):**
   ```bash
   python3 uretim_hatti/araclar/kor_ab.py karistir <dosyalar…> --hedef ~/film_medya/<FILM>/analiz/kor/<tur>
   python3 uretim_hatti/araclar/kor_ab.py ac ~/film_medya/<FILM>/analiz/kor/<tur>   # seçim yazıldıktan SONRA
   ```
4. **Kareli animatik karşılaştırması** (`cekim-yaz` §F7 7c'den): izleyicinin KARE modu cevabını
   `FILM.md` §4 "anlatacağı bilgi" ile çekim çekim karşılaştır → `ODA/F7_animatik_<n>.md`
   (çekim · bilgi · izleyicinin anladığı · tuttu/tutmadı).

## §F8 — Tarama, seçim, taslak (tavan 2 tur)

1. **Tarama (sahibin işi):** `uretim_hatti/QA_PROMPTLARI/TARAMA.md` Gemini uygulamasında, her koşu yeni sohbette.
   - VİDEO MODU: tek ham klip ya da ≤90 sn'lik taslak parçası.
   - KARE MODU: temas, efor ya da hızlı hareket olan riskli 2-3 sn. Gemini videoyu 1 kare/sn okur;
     `kareler.py cikar <klip> --aralik 0.25 --sayfa` kontak sayfası verilir.
   - "Ne olmalı" bloğunu `FILM.md`'den sen doldur (People · Environment · Sound · Camera · Main object)
     ve hazır metin olarak ver. Plan ve hikâye verilmez.
   - Sonuç gelince `NOTLAR.md` TARAMA tablosuna. Taslakta zaman → çekim:
     `kurgu.py liste <timeline> --zaman MM:SS.s`.
   - "İnsan doğrulaması" sütunu sahibin cevabıyla dolar.
   - `BILINEN_TUZAKLAR` §D: kesme hata değildir, doğru fizik kusur değildir.
2. **Kare sayfaları:** ✅ işaretli her deneme için
   `python3 uretim_hatti/araclar/kareler.py cikar <deneme> --hedef ~/film_medya/<FILM>/analiz/kareler/<deneme>/ --aralik 0.5 --sayfa`.
   **Kesme dikişleri (12.10.2026):** çekim sırasındaki her ardışık ✅ çift için
   `python3 uretim_hatti/araclar/kareler.py dikis <Ca_dN> <Cb_dM> --hedef ~/film_medya/<FILM>/analiz/dikis/<Ca>_<Cb>/`
   (fark görüntüsü + SSIM: jump cut ya da renk sıçraması bayrağı; `GECIS_VE_SES_SUREKLILIGI.md` §3). Çıktı klasörleri kurgucuya girdi.
3. **kurgucu** (faz 8): işaretleme + tarama + kare klasörleri + dikiş klasörleri + çekim listesi + `FILM.md` §6 ORTAM YATAĞI/GEÇİŞ + (varsa) zincir dikiş kararları
   (`NOTLAR.md`) → seçim tablosu + `timeline.json` taslağı + kesin GEÇİŞ tablosu. Çıktı: `ODA/F8_kurgucu_<tur>.md`.
   16.10.2026'dan beri kurgucunun Bash'i var: taslağını kendisi `kurgu.py kontrol` ile sınar, `medya.py durum` ile eksik ✅'yi görür.
   **Hat dışı montaj** (sahip montajı kendisi yaptıysa): önce `.claude/skills/medya-denetle/SKILL.md` — montaj bölünür, plan çekimine
   eşlenir; kurgucu o eşlemeden timeline'ı geri kurar (montajdaki aralıklar) ve düzeltmeleri önerir.
   Taslağı `<FILM>/timeline.json`'a, kesin GEÇİŞ tablosunu `FILM.md` §6'ya kopyala.
   - Zincirli halkalar `"zincir": "Zk"` alanını taşır, ardışık durur, dikişte ≤0,3 s kırpılır.
   - Her parçanın `gecis` alanı (kesme varsayılan · karisim 0,3-0,8 · karartma 0,5-1,5; karışım ≤ kesmelerin ¼'ü, karartma ≤ 2), `yataklar` mekân başına,
     model sesi replik taşıyan parçalar `klip_sesi: true` (12.10.2026).
   - `kurgu.py kontrol` sırayı denetler, fazla kırpmada uyarır, geçiş kısalmalarıyla toplam süreyi yazar.
4. **Mekanik kontrol:** `python3 uretim_hatti/araclar/kurgu.py kontrol <FILM>/timeline.json`.
   Hata = kurgucuya geri.
5. **Taslak:** `kurgu.py taslak <FILM>/timeline.json` → `~/film_medya/<FILM>/cikti/taslak_*.mp4`
   (model sesi atılır — `klip_sesi: true` parçalar hariç; `ses` ve `yataklar` eklenir; `gecis` karışım/karartma xfade ile). Ardından
   `kareler.py cikar <taslak> --hedef ~/film_medya/<FILM>/izleyici/taslak_<n>/ --aralik 1`.
6. **Paralel kontrol:**
   - **Süreklilik (sahibin işi):** `uretim_hatti/QA_PROMPTLARI/SUREKLILIK.md` taslak üzerinde, ≤90 sn parçalar,
     yeni sohbet. Kesme listesi: `kurgu.py liste <timeline> --kesmeler`; `?` satırlarını sen SAME/NEW yap.
     Sonuç `NOTLAR.md` SÜREKLİLİK'e.
   - **izleyici** (KARE modu): yalnız `izleyici/taslak_<n>/NN.png` yolları.
   - **dramaturg** (faz 8 modu): kurgu sırası + kare sayfası açıklaması → H02 bitiş, H01 tekrar, H07 doruk.
7. **Müzik finali:** `ses-muzik` §F8.
8. **Kapı:** `denetci` (Ö + F8) → Fable. Sonra sahibe: taslağı izle → İzleme Formu A
   (`uretim_hatti/QA_PROMPTLARI/IZLEME_FORMU.md`). Cevaplar `NOTLAR.md` İZLEME.
