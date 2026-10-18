---
name: sahneleme-odasi
description: Yeni hat faz 3 sahneleme adımı (§F3b) — klip zinciri ve anahtar kare planı (sahneleyici · mekan-haritacisi · teknik-danisman · yonetmen · izleyici). /yeni-film tarafından dosya olarak okunur; sahip /sahneleme-odasi ile doğrudan da çağırabilir.
disable-model-invocation: true
allowed-tools: Agent, Read, Grep, Glob, Write, Edit, Bash(python3:*), Bash(git diff:*)
---

# Sahneleme odası — §F3b (tavan 2 tur)

> ⏸️ **16.10.2026: yalnız zincir açıkken koşulur** (AGENTS §2, yeni-film §1 "Faz 3'ün üç adımı"): yonetmen `ZİNCİR ADAYI` yazdı ·
> künyedeki araç başlangıç + bitiş karesi alıyor · `SMOKE_TEST.md` zincir sonuç tablosu dolu. Üçünden biri yoksa ajan çağrılmaz;
> Fable `SAHNELEME.md` §5'e "zincir yok — <gerekçe>" yazar ve `ADIM pilot`'a geçer. Neden: zincirin dayandığı araç davranışı hiç
> ölçülmedi, 5 yeni hat filminde 0 zincir üretildi, adım film başına 2-7 çağrı harcıyordu. Mekân ve ekran yönü sorusunu F3'te
> kurgucu sorar (kurgu gözü).

Çekim listesi kapısı (§F3) kapandıktan sonra, ses planından (faz 4) önce çalışır: uzun
planlar müzik ve ses noktalarını kaydırır. `DURUM.md`: `FAZ 3 · ADIM sahneleme`.
Faz döngüsü `yeni-film` §2'dedir. Görev metinleri: `uretim_hatti/AJAN_GOREVLERI.md`.

**Zincir nedir, neden geri geldi:**
- Ardışık klipler tek plan gibi akar: halka n'nin bitiş karesi = halka n+1'in başlangıç karesi.
- 22.09.2026'da kaldırılan zincir **prompt diliyle** kuruluyordu ("continues the previous clip"); o dil hâlâ yasaktır.
- Bu zincir **gerçek başlangıç + bitiş karesi görselleriyle** kurulur. Varsayılan B (anahtar kare). Yedekler: A (son kare), A′ (seçilen çıkış karesi), A+ (tazelenmiş kare).
- **Seçmeli:** film başına önerilen 2-3 zincir, zincir başına ≤4 halka.

## Ön koşul
- `FILM.md` künyesinde `KLIP_SURESI` ölçülmüş olmalı (aracın verdiği süre, saniye). Her çekim 10 s olduğundan
  (08.10.2026) zincir yalnız KLIP_SURESI ≥ 10 ölçülürse kurulur (SMOKE P14); yoksa adım kısa kapanır.
- Ölçülmemişse zincir planı yazılabilir ama faz 7 zincir üretimi `uretim_hatti/SMOKE_TEST.md`
  zincir bölümü koşulmadan başlamaz (Flow'un bitiş karesi davranışı bu depoda doğrulanmadı).
- Yonetmen hiç `ZİNCİR ADAYI` yazmadıysa ve sahneleyici de zincir önermezse adım kısa kapanır:
  `SAHNELEME.md` §5'te bütün çekimler zincir dışı, gerekçeyle.

## Akış
1. **sahneleyici** (yazar):
   - girdiler: `FILM.md` §1 + §4 + `KLIP_SURESI` + yonetmen'in `ZİNCİR ADAYI` satırları;
   - çıktı: `ODA/F3b_sahneleyici_<tur>.md` (SAHNELEME §1, §2, §4, §5 + "§4 SÜTUNLARI").
2. **mekan-haritacisi** (yazar modu): sahneleyici taslağı → §3 mekân haritası → `ODA/F3b_mekan-haritacisi_<tur>.md`.
3. **Paralel eleştiri** (tek mesaj):
   - **mekan-haritacisi** (eleştirmen modu): mesafe/süre, 180°, görünürlük;
   - **teknik-danisman** (faz 3 sahneleme modu): delta bütçesi, morf riski;
   - **yonetmen** (faz 3 sahneleme modu): zincir gerekçesi, H01, kesmenin taşıdığı bilgi;
   - **izleyici** (METİN modu): YALNIZ anahtar karelerin görünen tarifleri, zincir sırasıyla
     (`Poz / konum` + `Nesne durumu`, gerekirse kamera; zincir adı, gerekçe ve çekim kodu YOK).
     Karşılaştırma: izleyicinin anlattığı akış, zincirin taşıması gereken bilgiyle tutuyor mu
     → `ODA/F3b_karsilastirma_<tur>.md`.
4. **Tur:** ÖLÜMCÜL bulgu → sahneleyici (ve gerekirse mekan-haritacisi) revize eder.
5. **Yerleştir:**
   - `SAHNELEME.md` ← sahneleyici §1, §2, §4, §5 + mekan-haritacisi §3 (birebir kopya);
   - "§4 SÜTUNLARI" tablosu → `FILM.md` §4'ün `Zincir · Baş. karesi · Bitiş karesi` sütunları;
   - zincirli çekimlerin Flow modu `Frames to Video`, süresi 10 s (≤ `KLIP_SURESI`, yani KLIP_SURESI ≥ 10 şart).
6. **Mekanik kontrol:** `python3 uretim_hatti/araclar/film_dogrula.py <FILM> --bolum cekim sahneleme`.
7. **Kapı:** `denetci` (Ö + F3b) → Fable. Sonra `DURUM.md` → `FAZ 4 · ADIM —`.

## Bütçe
- Bu adım tipik olarak 5-7 ajan çağrısı.
- Zincir yoksa 2.
- Üretimde (faz 7) zincir başına 2 zincir-bekcisi çağrısı: biri anahtar kareler, biri dikişler.
