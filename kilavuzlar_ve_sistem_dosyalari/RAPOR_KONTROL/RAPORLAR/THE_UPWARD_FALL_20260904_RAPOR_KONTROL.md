# 🧮 RAPOR KONTROL — THE_UPWARD_FALL

> **Tarih:** 04.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ⑦ AKSİYON | `THE_UPWARD_FALL_AKSIYON_HAM.md` | GEÇERSİZ | 7/66.0/9.4 | 8/76/9.5 | 8/76/9.5 | — |
| ⑤ ARKA PLAN | `THE_UPWARD_FALL_ARKA_PLAN_HAM.md` | ŞARTLI | 9/46.0/5.1 | 9/46/5.11 | 9/46/5.1 | 5.1 ⚠️ ŞARTLI |
| ② DEVAMLILIK | `THE_UPWARD_FALL_DEVAMLILIK_HAM.md` | ŞARTLI | 3/17.0/5.6 | 3/17/5.67 | 3/17/5.7 | 5.7 ⚠️ ŞARTLI |
| ⑧ EFOR | `THE_UPWARD_FALL_EFOR_HAM.md` | TEKRAR | 7/11.0/1.6 | 7/11/1.57 | 7/11/1.6 | — |
| ⑥ FİZİK | `THE_UPWARD_FALL_FIZIK_HAM.md` | TEKRAR | 9/54.0/6.0 | 9/54/6.0 | 9/54/6.0 | — |
| ④ HİKAYE | `THE_UPWARD_FALL_HIKAYE_HAM.md` | TEKRAR | 9/54.0/6.0 | 9/54/6.0 | 9/54/6.0 | — |
| ① KARE | `THE_UPWARD_FALL_KARE_HAM.md` | TEKRAR | 8/47.0/5.8 | 8/47/5.88 | 4/19/4.8 | — |
| ③ SES | `THE_UPWARD_FALL_SES_HAM.md` | GO | 0/0.0/None | 0/0/None | 0/0/None | — (sayı taşıyan hücre yok) |

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **GEÇERSİZ** — ARİTMETİK FABRİKE — rapor n=7 Σ=66 yazdı; kendi hücreleri n=8 Σ=76 (ort 9.5)<br>Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "the table is right and the overall is wrong" — satır tabloya GİRMEZ [D161].
- **ŞARTLI** — SEVERITY TALLY (0, 0, 2) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑤ ARKA PLAN — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — SEVERITY TALLY (0, 3, 6) ≠ yazılı etiketler (0, 3, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ② DEVAMLILIK — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — yuvarlama — OVERALL 5.6 yazılmış, hücreler 5.67 veriyor<br>tablo haklıdır; TABLOYA GİRECEK SAYI düzeltilmiş ortalamadır
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur

## ⑧ EFOR — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· gravity/medium: inverted gravity for loose objects, standard 1g for character wears: tac…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]
- **ŞARTLI** — COST CURVE sabit (0) ama efor olayı var<br>iş yapıldıysa borç ya artar ya toparlanır; düz eğri ÖLÇMEDİ demektir

## ⑥ FİZİK — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (1, 3, 5) ≠ yazılı etiketler (1, 2, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ④ HİKAYE — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>

## ① KARE — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — yuvarlama — OVERALL 5.8 yazılmış, hücreler 5.88 veriyor<br>tablo haklıdır; TABLOYA GİRECEK SAYI düzeltilmiş ortalamadır
- **ŞARTLI** — 4 hücre düzeltildi<br>Scale & Physics 7/10 → — (issue: "no in-scope source") [D131] · Camera 7/10 → — (issue: "no in-scope source") [D131] · Lighting 7/10 → — (issue: "no in-scope source") [D131] · Particles & Materials 7/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SEVERITY TALLY (0, 3, 0) ≠ yazılı etiketler (1, 4, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **NOT** — ⑨ ızgara OTURUYOR — 21 kesme, max |Δ| = 0.0 s (hook 10 · klip 10) → zaman kodları uydurulmamış [D115]

## ③ SES — GO
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır

## ⑤ ÇAPRAZ KAPI
- **NOT** — ⑪ ÖLÇÜM HAKEM: kesme = 21 (ölçüldü) · raporlar: ⑦ AKSİYON 21 · ⑤ ARKA PLAN 21 · ② DEVAMLILIK 21 · ⑧ EFOR 21 · ⑥ FİZİK 21 · ④ HİKAYE 21 · ① KARE 21 · ③ SES 21
- **NOT** — ⑤ her mercek ölçümle uyuşuyor → kesme ekseni doğrulandı
- **NOT** — ⑤ sahne ekseni ölçümle doğrulandı (22)
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `111111111111111111111` (4 mercek); sapan: ② DEVAMLILIK, ⑧ EFOR, ① KARE<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 7 mercek, 0 replik [D121]
