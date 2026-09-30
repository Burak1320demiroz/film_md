# 🧭 00_ON_PLAN — THE_FALSE_EARTH, yeni-film akışından ÖNCE

> **Açılış:** 22.09.2026 · sahip isteği: *"32 dk ilk film için … başlamadan yeni-film akışına
> önce bir planlama yapalım, klasörü hazırla."*

Bu klasör filmin henüz **açılmamış** hâlidir. Film klasörünün içinde şimdilik yalnız bu klasör
durur; PLAN, BÖLÜM ve 00_ANALIZ dosyaları henüz yok, çünkü onlar onaylı sahne planıyla açılır
(`--sahne-plani`, çok klipli sahne rejimi).

| dosya | ne |
|---|---|
| `01_SAHIP_TRETMANI.md` | sahibin iki metni, birebir (kaynak) |
| `02_ON_PLAN.md` | **sürüm 3** — eleştiri 1 ve 2 → değişiklik tabloları · hikâyenin iç kuralları · 50 sahnelik taslak plan · kararlar (K1–K11) · ölçütlü denemeler (P0–P3) · riskler · akışa geçiş |
| `03_ELESTIRI_1.md` | sürüm 1'e (52 sahne) yazılan dokuz maddelik değerlendirme, birebir |
| `04_KLIP_ADIMLARI.md` | **sürüm 3** — 192 klibin her biri: ne değişiyor (BİLGİ · TEHLİKE · DAVRANIŞ) ya da bilinçli kalışın ETKİSİ + Mira'nın tavrı — sahne sürelerinin kaynağı |
| `05_ELESTIRI_2.md` | sürüm 2'ye yazılan yedi maddelik değerlendirme, birebir |

**Nasıl emilir:** hikâye onaylanınca `film_klasoru_ac.sh yatay_32_dk_filmler THE_FALSE_EARTH 192
--sahne-plani "…"` bu klasörün üstüne açılır. Betik, klasörde **yalnız** `00_ON_PLAN/` varsa
açılışa izin verir ve bu klasörü dokunmadan `00_ANALIZ/00_ON_PLAN/` altına taşır. Buraya başka
bir dosya koyma; koyarsan betik `⛔ ZATEN VAR` der.

⛔ Burada `## … SAHNE <n>` başlığı, satır başında `TEMA:` ve prompt başlığı yazılmaz
(`00_ANALIZ_README` ile aynı kural; `prompt_kontrol.py` bu yolu `00_ON_PLAN` deseniyle atlar).
