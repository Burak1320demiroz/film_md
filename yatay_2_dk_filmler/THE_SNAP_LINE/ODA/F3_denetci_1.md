# 🔍 F3 — Süreç ve Faz Denetçi Raporu (Tur 1)

**Film:** `yatay_2_dk_filmler/THE_SNAP_LINE`  
**Faz:** 3 (Çekim Listesi) · Tur: 1  
**Tarih:** 22.10.2026

---

## 1. Ö · ORTAK SÜREÇ MADDELERİ

| Madde | Durum | Kanıt / Dosya |
|---|:--:|---|
| Ö1 **M** — Zorunlu eleştiriler ODA/'da var | ✅ | `ODA/F3_teknik-danisman_1.md`, `ODA/F3_izleyici_1.md`, `ODA/F3_kurgucu_1.md`, `ODA/F3_bilim-danismani_1.md` |
| Ö2 **M** — GİRDİ satırları tam | ✅ | Tüm eleştirmenlerde GİRDİ eksiksiz mevcut |
| Ö6 — Açık ÖLÜMCÜL bulgu yok | ✅ | Dört eleştirmende de 0 ölümcül bulgu |
| Ö7 **M** — DURUM.md güncel | ✅ | Faz 3, Tur 1 kayıtlı |
| Ö8 — Metin çağrı tavanı (30) aşılmadı | ✅ | F1 (4) + F2 (6) + F3 (5) = 15 / 30 |

---

## 2. F3 · FAZ KABUL MADDELERİ

| Madde | Durum | Kanıt |
|---|:--:|---|
| F3.1 **M** — `film_dogrula.py` çekim kontrolü | ✅ | `film_dogrula.py` 12 çekim için 0 hata verdi; zihinsel fiil yok, süreler tam 10.0 s |
| F3.2 — Her çekim tek bilgi | ✅ | C01–C12 tek bilgi sütunu eksiksiz |
| F3.3 — İzleyici animatik okuması | ✅ | `ODA/F3_izleyici_1.md`: Görsel akış tam anlaşıldı |
| F3.4 — Teknik danışman riskleri | ✅ | El-nesne ve kordon kesilme temasları C09 kabarcık patlaması perdesiyle çözüldü |
| F3.5 — Toplam süre ve sonuç | ✅ | 12 × 10 s = 120 s; C12 acil durum sayacıyla sonuç gösteriyor |
| F3.6 **M** — Numaralı referanslar | ✅ | `1.MILLER`, `2.MEKAN`, `3.MAKAS`; özne başına tek sayfa |
| F3.7 — AÇILIŞ tablosu (C01–C03) | ✅ | C01 sorun, C02 insan, C03 kapak anı |
| F3.8 — Kurgucu 7 soru analizi | ✅ | `ODA/F3_kurgucu_1.md`: Kesme, ölçek ve mekân sürekliliği onaylandı |
| F3.9 — Pilot seçimi | ✅ | C01 (Açılış/akışkan), C02 (Kimlik/konuşma), C08 (En riskli an/kesme makası) |

---

## 3. KARAR
* **SONUÇ:** ✅ **KAPANDI**.
* Mekanik ve yargı engeli yoktur. Pilot adımına (F3p) geçilebilir.
