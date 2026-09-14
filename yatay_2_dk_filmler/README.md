# 🎬 Yatay 2 Dakika Filmler — 12 Sahne · 2 Bölüm

> 🔁 **13.09.2026 · KLASÖR YENİDEN ADLANDIRILDI:** `yatay_2_4_dk_filmler_uzay/` →
> **`yatay_2_dk_filmler/`** (sahip kararı; `_uzay` tür soneki düştü — depo zaten
> yalnız uzay filmleri içindir, tür kartı `KILAVUZ_REHBERI` §4'te yaşar).
> Depodaki tarihli kayıtlarda geçen **"2-4 dk" bu formatın eski adıdır**,
> değiştirilmez. 12-sahne modül merdiveninin İLK basamağı: **bu klasör 12 sahne ·
> 2:00** → `yatay_4_dk_filmler/` 24 → `yatay_6_dk_filmler/` 36 → `yatay_8_dk_filmler/` 48.
>
> Geçerli kart: `KILAVUZ_REHBERI.md` §2.2 · iskelet §2.0 · akış AGENTS Kart A.

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 2:00 (12 × 10 s) — 13.09.2026 modül beyanı |
| **Oryantasyon** | 16:9 yatay |
| **Toplam sahne** | 12 — hook 12'nin İÇİNDEDİR (S0), ayrı sahne değil |
| **Yapı** | 2 bölüm × 6 sahne (BOLUM_1 = S0-S5 · BOLUM_2 = S6-S11) — betik ortadan böler |
| **Klip süresi** | 10 s / sahne — ⛔ plan yazılmadan ARAÇTAN ölçülür [D124] |
| **QA birimi** | FİLM — tek master, on iki mercek bir kez (bölüm QA'sı yalnız 6/8 dk hattında) |
| **Eski bant** | 12-18 sahne (2:00-3:00) — 13-18 sahneyle yazılmış filmler OLDUĞU GİBİ kalır, yeniden bölünmez |

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh yatay_2_dk_filmler <FILM_ADI> 12
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; sayaç kökteki
her girdiyi BİR FİLM sayar. 12'nin dışı bandın dışıdır: sahip izni + plana
gerekçe [D74].

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `FILM_QA_RAPORLARI/00_INDEX.md` tek sayaçtır
(`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`). Güncel tam örnek:
`THE_SOLAR_MIRROR/` (12 sahne / 2:00 · sekiz dosya) — referans: `KILAVUZ_REHBERI` §2.2.
