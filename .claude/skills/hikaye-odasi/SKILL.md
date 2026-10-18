---
name: hikaye-odasi
description: Yeni hat faz 1-3 prosedürü (hikâye odası · tretman · çekim listesi). /yeni-film tarafından dosya olarak okunur; sahip /hikaye-odasi ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, AskUserQuestion, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(git diff:*)
---

# Hikâye odası — faz 1-3

Faz döngüsü (yazar → paralel eleştiri → tur → yerleştir → kapı → kayıt) `yeni-film` §2'dedir.
Burada her fazın **neye özel** olduğu yazar. Görev metinleri: `uretim_hatti/AJAN_GOREVLERI.md`.

---

## §F1 — Hikâye odası (tavan 3 tur)

1. **senarist** (faz 1). Brif: konu · format · süre · karakter sayısı.
   Çıktı: `ODA/F1_senarist_1.md`. İçerik: gerilim cümlesi, havuz, eleme, A/B/C adayları, A'ya karşı.
2. **Paralel üç eleştiri:**
   - **dramaturg:** üç adayın tamamı, eleştiri dosyası olarak.
   - **yonetmen** (eleştirmen modu, faz 1 üretilebilirlik): üç aday.
   - **izleyici** (LOGLINE modu): yalnız üç logline. Başka hiçbir alan verilmez.
3. **Tur:** seçilecek adayda ÖLÜMCÜL bulgu varsa senarist revize eder (en çok 3 tur).
   Revizyonda yalnız o adayı değil üçünü de güncelleyebilir.
4. **Fable seçer.** `ODA/F1_secim.md`'ye yaz:
   - hangi aday ve neden (dramaturg'un "EN SAĞLAM"ı, yonetmen'in üretilebilirlik notu, izleyicinin tercihi);
   - açık kalan CİDDİ bulgular.
5. **Sahip vetosu:** `AskUserQuestion`, tek soru. Gösterilir:
   - üç logline;
   - senin seçimin (önerilen olarak ilk seçenek);
   - tek cümle gerekçe.

   Seçenekler: Fable'ın seçimi · diğer iki aday · ("Diğer" = değiştir notu).
   - Değiştir notu gelirse senarist o notla yeniden yazar: yeni tur.
   - Üç turda da veto edilirse sahibe konuyu değiştirmeyi öner.
6. **Yerleştir:** seçilen adayın alanları `FILM.md` §1'e birebir. `SEÇİM` ve `SAHİP` satırları doldurulur.
7. **Kapı:** F1 kabul listesi. Burada denetçi isteğe bağlıdır; sahip zaten gördü.

## §F2 — Tretman (tavan 2 tur)

1. **senarist** (faz 2): seçilen aday → sahne sahne tretman + `REPLİK İHTİYACI` satırı.
   - Replik ihtiyacı `var` ise künyede `REPLIK var` yap ve **diyalog-yazari**'nı çağır (tretman dosyasıyla).
2. **Paralel eleştiri:**
   - **dramaturg:** tretman (+ replik dosyası).
   - **izleyici** (METİN modu): tretmanın yalnız "ne olur" sütunu, sahne sırasıyla, olay dilinde.
     Sahne başlıkları, "ne değişir" sütunu ve hikâye alanları VERİLMEZ.
   - **ses-tasarimcisi** (eleştirmen modu): replik varsa her repliğin nereden duyulacağı.
3. **Karşılaştırma:** izleyicinin "NE İSTİYOR / SON" cevabını `FILM.md` §1 AMAÇ/SONUÇ ile
   karşılaştır. Tutmuyorsa bu bir ÖLÜMCÜL bulgudur: senariste geri gider.
   Kaydet: `ODA/F2_karsilastirma_<tur>.md`.
4. **Yerleştir:** tretman tablosu → `FILM.md` §2. Replik tablosu → §5.
   `FIZIK_IDDIASI` kesinleşir; `var` ise faz 3'te **bilim-danismani** inandırıcılık bakar.
5. **Kapı:** `denetci` (Ö + F2).

## §F3 — Çekim listesi (tavan 2 tur)

1. **yonetmen** (faz 3): onaylı tretman + replikler → çekim listesi, `FILM.md` §4 sütun sırasıyla +
   `GEREKEN REFERANSLAR` (numaralı `<No>.<AD>`, özne başına tek satır + panel listesi, sahip kararı 10.10.2026; §3 `No` sütunu + dosya `<No>.<AD>_v1.png`). Çıktı: `ODA/F3_yonetmen_<tur>.md`.
2. **Paralel eleştiri:**
   - **teknik-danisman:** çekim listesi.
   - **izleyici** (METİN modu = **metin animatiği**): YALNIZ "Ekranda görünen" sütunu, çekim
     sırasıyla. Replik varsa yalnız duyulan metin "(ses) …" olarak araya.
     "Anlatacağı bilgi" sütunu ASLA verilmez.
   - **bilim-danismani** (koşullu): fizik iddiası ekranda görülebiliyor mu.
   - **kurgucu** (16.10.2026, F3 kurgu gözü): çekim listesi + replik tablosu. Kesmenin iki yanı, tepki/bağlantı planı,
     mekân ilişkisi, 10 s'yi taşıyan hareket, kritik bilginin yedek yolu (`kurgucu.md` § Eleştirmen modu — faz 3). Bütün
     görüntü üretildikten sonra "burada bağlantı planı lazım" demek pahalı; burada söylenir.
3. **Metin animatiği karşılaştırması:** her çekim için tek tablo, `ODA/F3_animatik_<tur>.md`:
   `çekim · anlatacağı bilgi · izleyicinin anladığı (alıntı) · tuttu / kısmen / tutmadı`.
   - Kritik bilgiyi (amaç, engel, karar, sonuç) taşıyan çekimlerde "tutmadı" = ÖLÜMCÜL → yonetmen revize eder.
   - Diğerlerinde CİDDİ.
4. **Yerleştir:** tablo → `FILM.md` §4 (birebir). Referans listesi → §3.
5. **Mekanik kontrol:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum kunye hikaye cekim`.
   Hata varsa yonetmen'e geri.
6. **Kapı:** `denetci` (Ö + F3) → Fable.
7. **Pilot çekimleri (16.10.2026):** Fable kapıyı kapatırken 1-3 pilot çekimi seçer ve `DURUM.md` `PILOT` satırına yazar:
   - **en riskli an:** teknik-danisman'ın F3'te en ağır bulguyu verdiği çekim (temas, iki kişi aynı nesnede, kapıdan geçiş, vakumda itki);
   - **açılış:** C01 (ILK_30_SANIYE §6: deneme hakkı en çok onda);
   - **kimlik / konuşma:** ana karakterin yüzünün ve giysi işaretinin okunduğu çekim; model sesi filminde replikli olanı.
   Aynı çekim iki rolü taşıyorsa sayı azalır. Seçim gerekçesi tek satır.
8. **Sonra sahneleme:** `DURUM.md` → `ADIM sahneleme` ve `.claude/skills/sahneleme-odasi/SKILL.md` — **yalnız zincir açıkken**
   (yeni-film §1 "Faz 3'ün üç adımı"). Değilse ajansız kapanır: `SAHNELEME.md` §5'e "zincir yok — gerekçe", sonra `ADIM pilot`
   (`.claude/skills/cekim-yaz/SKILL.md` §F3p).
