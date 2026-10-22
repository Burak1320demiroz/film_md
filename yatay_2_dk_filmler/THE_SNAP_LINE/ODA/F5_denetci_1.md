# 🔍 F5 — Süreç ve Faz Denetçi Raporu (Tur 1)

**Film:** `yatay_2_dk_filmler/THE_SNAP_LINE`  
**Faz:** 5 (Grup Promptları — G01) · Tur: 1  
**Tarih:** 22.10.2026

---

## 1. Ö · ORTAK SÜREÇ MADDELERİ

| Madde | Durum | Kanıt / Dosya |
|---|:--:|---|
| Ö1 **M** — Zorunlu eleştiriler ODA/'da var | ✅ | `ODA/F5_devamlilik_1.md`, `ODA/F5_teknik-danisman_1.md` |
| Ö2 **M** — GİRDİ satırları tam | ✅ | Her iki raporda GİRDİ eksiksiz mevcut |
| Ö6 — Açık ÖLÜMCÜL bulgu yok | ✅ | Devamlılık ve teknik danışmanda 0 ölümcül bulgu |
| Ö7 **M** — DURUM.md güncel | ✅ | Faz 5, Tur 1 |
| Ö8 — Metin çağrı tavanı (30) aşılmadı | ✅ | F1(4) + F2(6) + F3(6) + Pilot(1) + F4(5) + F5(3) = 25 / 30 |

---

## 2. F5 · FAZ KABUL MADDELERİ

| Madde | Durum | Kanıt |
|---|:--:|---|
| F5.1 **M** — Mekanik kontrol | ✅ | `film_dogrula.py --bolum kunye durum cekim prompt` 0 hata verdi |
| F5.2 — Tüm çekimler için promptlar | ✅ | C01–C12 arası tüm çekimlerin Görsel ve Video promptları tam |
| F5.3 — 10 s vuruş planı | ✅ | 0–10 saniye aralıkları boşluksuz, her vuruş ≥2 s, donan hareket yok |
| F5.4 — Kimlik cümleleri | ✅ | FILM §3'teki kimlik cümleleri her çekime harfi harfine taşındı |
| F5.5 — Temas ve perdeleme | ✅ | Makasın kordonu kesişi C09 gaz patlaması perdesiyle çözüldü |
| F5.6 — Model sesi replikleri | ✅ | C02, C04, C06, C08, C11 replikleri video promptunda birebir tırnak içinde |
| F5.7 — Devamlılık 8 soru | ✅ | `ODA/F5_devamlilik_1.md` 8 sorunun 8'ine de tam onay verdi |
| F5.8 — Teknik danışman | ✅ | `ODA/F5_teknik-danisman_1.md` riskleri ve model sınırlarını onayladı |
| F5.11 — DERS uyarıları gerekçesi | ✅ | DERS Y5 (sualtı ortamı) ve DERS Y8 (analog kadran) gerekçeleri kayda geçti |

---

## 3. KARAR
* **SONUÇ:** ✅ **KAPANDI**.
* Faz 5 promptları onaylandı. Faz 6 (Kapak Konsepti) adımına geçilebilir.
