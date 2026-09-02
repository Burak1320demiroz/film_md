# 🧮 RAPOR KONTROL — QA raporunun çıktı kapısı

> `prompt_kontrol.py` girdiyi (promptu) denetler; **bu betik çıktıyı (raporu)**.
> 01.09.2026'ya kadar çıktı tarafında tek satır kod yoktu; AGENTS ortak adımları
> aynı kontrolleri prose olarak taşıyordu ve bir partide altı raporun beşi kendi
> aritmetik kapısından geçemedi [D161]. Betik koşulmadan T tablosuna satır yazılmaz.

```
python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py \
        <rapor.md> [<rapor.md> ...] [--film <film klasörü>] [--hook 10] [--klip 10] [--rapor] \
        [--olcum-kesme <n>] [--olcum-sahne <n>]     # ⑪ ölçümü hakem yapar
```

| ne ölçer | kaynak |
|---|---|
| SPEC var + ①/④/⑥ mod V → TEKRAR | D129 |
| n · Σ · Σ/n hücrelerden; iddiayla kıyas · "no in-scope source"+sayı → `—` · 0 replikte diyalog-yalnız hücre → N/A | D131 · D161 |
| SEVERITY TALLY ↔ yazılı 🔴🟠🟡 (timecode ile tekilleştirilmiş) | D161 |
| şerit uzunluğu = kesme+1 · ④ harita ↔ kesme sayısı (film boyu hücreler düşer) | D118 · D121 |
| kesme zaman kodları planın ızgarasına oturuyor mu (⑨) | D115 |
| SPEC sayaç yazarken ② "Counter N/A" → ölçüm boşluğu | D134 |
| birden çok rapor: kesme · sahne · şerit · replik · ⭐ SUSKUNLUK (film boyu iddia ↔ sahibin sessizliği) | D107 · D162 |

**Çıkış:** 0 GO · 1 ŞARTLI · 2 TEKRAR/GEÇERSİZ. `--rapor` → `RAPORLAR/<FILM>_<tarih>_RAPOR_KONTROL.md`.

⛔ Betik **bulgunun doğruluğunu** ölçmez — o iş kare/ses ister (⑪ ölçüm kapısı,
② kilit defteri). Ölçtüğü tek şey raporun kendi içinde ve partinin kendi arasında
tutup tutmadığıdır. Rubrik metnine kural EKLENMEZ; kural buraya, çıktı kapısına
gelir (rubrik hacmi: `sayac.sh` 🧭).
