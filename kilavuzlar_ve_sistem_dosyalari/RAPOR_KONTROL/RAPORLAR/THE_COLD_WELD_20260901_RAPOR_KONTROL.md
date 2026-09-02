# 🧮 RAPOR KONTROL — THE_COLD_WELD

> **Tarih:** 01.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_COLD_WELD_KARE_HAM.md` | GEÇERSİZ | 8/41.0/5.1 | 8/41/5.12 | 8/41/5.1 | — |
| ② DEVAMLILIK | `THE_COLD_WELD_DEVAMLILIK_HAM.md` | GEÇERSİZ | 13/115.0/8.8 | 12/108/9.0 | 12/108/9.0 | — |
| ③ SES | `THE_COLD_WELD_SES_HAM.md` | GEÇERSİZ | 4/24.0/6.0 | 4/24/6.0 | 1/5/5.0 | — |
| ④ HİKAYE | `THE_COLD_WELD_HIKAYE_HAM.md` | GEÇERSİZ | 9/51.0/5.6 | 9/51/5.67 | 5/32/6.4 | — |
| ⑤ ARKA PLAN | `THE_COLD_WELD_ARKA_PLAN_HAM.md` | GEÇERSİZ | 6/30.0/5.0 | 6/30/5.0 | 6/30/5.0 | — |
| ⑥ FİZİK | `THE_COLD_WELD_FIZIK_HAM.md` | GEÇERSİZ | 5/31.0/6.2 | 5/31/6.2 | 5/31/6.2 | — |

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **NOT** — Dialogue & Audio 3/10 · film 0 replikli — hücrenin kaynağı SES FİZİĞİ (vakumda ses / senkron) olmalı; replik kaynaklıysa N/A'ya çevir (insan kararı)
- **ŞARTLI** — SEVERITY TALLY (3, 2, 1) ≠ yazılı etiketler (3, 2, 2) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **NOT** — ⑨ ızgara OTURUYOR — 14 kesme, max |Δ| = 1.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ② DEVAMLILIK — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **GEÇERSİZ** — ARİTMETİK FABRİKE — rapor n=13 Σ=115 yazdı; kendi hücreleri n=12 Σ=108 (ort 9.0)<br>Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "the table is right and the overall is wrong" — satır tabloya GİRMEZ [D161].
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur
- **ŞARTLI** — SEVERITY TALLY (0, 3, 4) ≠ yazılı etiketler (0, 1, 2) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 3 hücre düzeltildi<br>Ambience Continuity 7/10 → — (issue: "no in-scope source") [D131] · Mix Hierarchy & Levels 6/10 → — (issue: "no in-scope source") [D131] · Music & Silence 6/10 → — (issue: "no in-scope source") [D131]

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — yuvarlama — OVERALL 5.6 yazılmış, hücreler 5.67 veriyor<br>tablo haklıdır; TABLOYA GİRECEK SAYI düzeltilmiş ortalamadır
- **ŞARTLI** — sahne haritası (8 sahne) kendi kesme sayısıyla (16) çelişiyor<br>rubriğin STEP 1 kuralı: en kısa kesme aralığının iki katından uzun blok → böl ve yeniden say. Film boyu hücreler sayı taşımaz [AGENTS ④]: Structure & Pacing, Emotional Arc, Ending, Retention Risk
- **ŞARTLI** — PRESENCE STRING 8 hane, kesme+1 = 17<br>şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]

## ⑤ ARKA PLAN — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır

## ⑥ FİZİK — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (0, 1, 3) ≠ yazılı etiketler (0, 1, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑤ ÇAPRAZ KAPI
- **GEÇERSİZ** — ⑤ KESME YAYILIMI 2 > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]<br>① KARE 14 · ④ HİKAYE 16
- **ŞARTLI** — ⑤ sahne sayıları ayrışıyor: ② DEVAMLILIK 15 · ④ HİKAYE 8 · ⑤ ARKA PLAN 15 · ⑥ FİZİK 15
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `-11111111111111` (3 mercek); sapan: ① KARE, ④ HİKAYE<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 5 mercek, 0 replik [D121]
- **ŞARTLI** — 🚨 SUSKUNLUK — ⑤ ARKA PLAN film boyu iddia: filigran / sabit köşe işareti; sahibi ① KARE SUSTU [D162]<br>"…| Frame Edges & Emergent Artifacts | 5/10 | -2 · 0:00-2:29 (static mark bottom right) |  ## PRESENCE STRING -11111111111111  ## SEV…" → kareyle çözülür (⑪ köşe testi / tek kare); çözülene kadar HER İKİ merceğin o kategorisi sayı taşımaz
