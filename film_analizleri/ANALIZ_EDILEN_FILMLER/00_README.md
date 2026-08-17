# 📊 ANALIZ_EDILEN_FILMLER — Çıktı Klasörü

> Her analiz edilen film **kendi klasörünü** alır. Promptlar ve çalıştırma
> tarifi: `../00_README.md` · `../ANALIZ_QA_PROMPTLARI/`
>
> **İş bölümü:** operatör promptları koşup raporları iletir; klasörü ve
> .md dosyalarını AJAN açar, raporları olduğu gibi kaydeder, çapraz
> okumayı ve ders seçkisini yazar.

## Analiz edilen filmler

| Film | Klasör | Durum |
|---|---|---|
| Nobody Was Alive When We Landed (YouTube · ~69 dk · muhtemel AI üretimi) | `NOBODY_WAS_ALIVE_WHEN_WE_LANDED/` | ✅ **TAMAMLANDI** · 20/20 part · 66 rapor · [tam analiz](NOBODY_WAS_ALIVE_WHEN_WE_LANDED/50_TAM_FILM_ANALIZI.md) · [ders seçkisi](NOBODY_WAS_ALIVE_WHEN_WE_LANDED/60_DERS_SECKISI.md) |

---

## Film klasörü şablonu

```
<FILM_ADI>/                        BUYUK_HARF_ALT_CIZGI · Türkçe karakter yok
├── 00_KUNYE.md                    ajan yazar (şablon aşağıda)
├── PARCA_01_KAMERA.md             ┐
├── PARCA_01_OLAY.md               ├ parça başına 3-4 mercek raporu —
├── PARCA_01_TEMA.md               │ model çıktısı OLDUĞU GİBİ, düzenlenmez
├── PARCA_01_KARAKTER.md           ┘ (4.'sü opsiyonel)
├── … (PARCA_02 … PARCA_20 aynı set)
├── 50_TAM_FILM_ANALIZI.md         ⭐ ajanın çapraz okuması — ara analiz
│                                     olarak başlar, 20 partta kapanır
├── 60_DERS_SECKISI.md             ⭐ elenmiş dersler · kart G girdisi
└── 99_SENTEZ_RAPORU.md            model sentezi (opsiyonel ikinci okuma)
```

## 00_KUNYE.md şablonu

```markdown
# 🎞️ KUNYE — <FILM ADI>

| Alan | Değer |
|---|---|
| Film | <ad, yıl, yönetmen — biliniyorsa> |
| Kaynak | <referans film / kendi üretimimiz> |
| Toplam süre | hh:mm:ss |
| Parça süresi | <eşitse ortalama; değilse aralık> |
| Analiz tarihi | GG.AA.YYYY |
| Model | <raporları koşan model> |

## 📁 DOSYA HARİTASI
<hangi dosya ne işe yarar — okuyucu buradan yön bulur>

## Parça haritası

| Parça | In | Out | Süre | 🎥 Kamera | 📖 Olay | 🎭 Tema | 🧍 Karakter |
|---|---|---|---|---|---|---|---|
| 01 | 00:00 | ... | ... | ⬜/✅ | ⬜/✅ | ⬜/✅ | ⬜/✅ |
| … | | | | | | | |

## Operatör notları
<gözlemler, şüpheli rapor bulguları, koşu tarihçesi>

## ⚙️ SÜREÇ DERSLERİ
<bu koşudan çıkan, sıradaki analizde uygulanacak operasyonel dersler>
```

⛔ **Parça dosyaları ham çıktıdır** — not düşülecekse `00_KUNYE.md`'ye ya
da `50_TAM_FILM_ANALIZI.md`'ye. Üretime aktarılacak ders çıktıysa önce
`60_DERS_SECKISI.md`'de elenir, oradan AGENTS.md kart G ile
LESSONS_LEARNED'a geçer.
