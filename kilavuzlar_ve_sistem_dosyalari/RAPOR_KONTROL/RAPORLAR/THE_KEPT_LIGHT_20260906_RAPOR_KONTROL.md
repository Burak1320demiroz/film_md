# 🧮 RAPOR KONTROL — THE_KEPT_LIGHT

> **Tarih:** 06.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_KEPT_LIGHT_KARE_HAM.md` | GEÇERSİZ | 7/55.0/7.9 | 7/55/7.86 | 7/55/7.9 | — |
| ② DEVAMLILIK | `THE_KEPT_LIGHT_DEVAMLILIK_HAM.md` | GEÇERSİZ | 12/78.0/6.5 | 12/78/6.5 | 12/78/6.5 | — |
| ③ SES | `THE_KEPT_LIGHT_SES_HAM.md` | GEÇERSİZ | 4/27.0/6.8 | 4/27/6.75 | 4/27/6.8 | — |
| ④ HİKAYE | `THE_KEPT_LIGHT_HIKAYE_HAM.md` | GEÇERSİZ | 9/41.0/4.5 | 9/41/4.56 | 5/23/4.6 | — |
| ⑤ ARKA PLAN | `THE_KEPT_LIGHT_ARKA_PLAN_HAM.md` | GEÇERSİZ | 5/37.0/7.4 | 5/37/7.4 | 5/37/7.4 | — |
| ⑥ FİZİK | `THE_KEPT_LIGHT_FIZIK_HAM.md` | GEÇERSİZ | 7/36.0/5.1 | 7/36/5.14 | 7/36/5.1 | — |
| ⑦ AKSİYON | `THE_KEPT_LIGHT_AKSIYON_HAM.md` | GEÇERSİZ | 9/65.0/7.2 | 9/65/7.22 | 7/45/6.4 | — |
| ⑧ EFOR | `THE_KEPT_LIGHT_EFOR_HAM.md` | GEÇERSİZ | 7/15.0/2.1 | 7/13/1.86 | 7/13/1.9 | — |

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (1, 4, 6) ≠ yazılı etiketler (3, 7, 7) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — ⑨ ızgara KAYMIŞ — max |Δ| = 10.0 s · sapan kesmeler: 2:-10s, 3:-10s, 4:-10s, 21:+10s, 22:+10s, 23:+10s<br>ya kurgu ızgarada değil ya rapor zaman kodlarını uydurmuş; ⑪ ölçümü karar verir

## ② DEVAMLILIK — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur
- **ŞARTLI** — SEVERITY TALLY (0, 5, 2) ≠ yazılı etiketler (0, 4, 2) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — kesme 20 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — sahne haritası (7 sahne) kendi kesme sayısıyla (24) çelişiyor<br>rubriğin STEP 1 kuralı: en kısa kesme aralığının iki katından uzun blok → böl ve yeniden say. Film boyu hücreler sayı taşımaz [AGENTS ④]: Structure & Pacing, Emotional Arc, Ending, Retention Risk
- **ŞARTLI** — PRESENCE STRING 7 hane, kesme+1 = 25<br>şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]
- **ŞARTLI** — ⑨ ızgara KAYMIŞ — max |Δ| = 10.0 s · sapan kesmeler: 2:-10s, 3:-10s, 4:-10s, 21:+10s, 22:+10s, 23:+10s<br>ya kurgu ızgarada değil ya rapor zaman kodlarını uydurmuş; ⑪ ölçümü karar verir

## ⑤ ARKA PLAN — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — SEVERITY TALLY (0, 2, 1) ≠ yazılı etiketler (0, 1, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — kesme 20 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ⑥ FİZİK — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (1, 2, 1) ≠ yazılı etiketler (2, 3, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — kesme 20 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· gravity / medium: mixed (character experiences 1g, loose objects experience microgravity…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]
- **ŞARTLI** — 2 hücre düzeltildi<br>Contact Legibility 10/10 → — (issue: "no in-scope source") [D131] · Camera's Contract with the Action 10/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SEVERITY TALLY (0, 2, 3) ≠ yazılı etiketler (0, 1, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑧ EFOR — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· gravity / medium [appears normal 1G interior, vacuum exterior] what the body wears [heav…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]
- **GEÇERSİZ** — ARİTMETİK FABRİKE — rapor n=7 Σ=15 yazdı; kendi hücreleri n=7 Σ=13 (ort 1.86)<br>Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "the table is right and the overall is wrong" — satır tabloya GİRMEZ [D161].
- **ŞARTLI** — SEVERITY TALLY (3, 1, 0) ≠ yazılı etiketler (2, 1, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — COST CURVE'de 3 düşüş var, RESET LOG'da 2 satır<br>her düşüş toparlanma gösterilerek açıklanır; açıklanmayan düşüş bulgudur [⑧ pattern ③/⑪]
- **ŞARTLI** — kesme 20 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ⑤ ÇAPRAZ KAPI
- **NOT** — ⑪ ÖLÇÜM HAKEM: kesme = 24 (ölçüldü) · raporlar: ① KARE 23 · ② DEVAMLILIK 24 · ③ SES 20 · ④ HİKAYE 24 · ⑤ ARKA PLAN 20 · ⑥ FİZİK 20 · ⑦ AKSİYON 24 · ⑧ EFOR 20
- **ŞARTLI** — ⑤ ölçümden sapan mercek(ler): ③ SES 20 · ⑤ ARKA PLAN 20 · ⑥ FİZİK 20 · ⑧ EFOR 20<br>parti AYAKTA — anlaşmazlık ölçümle çözüldü; yalnız sapan mercek şartlıdır
- **ŞARTLI** — ⑤ sahne — ÖLÇÜM 25; sapan: ④ HİKAYE 7 · ⑤ ARKA PLAN 20 · ⑥ FİZİK 20 · ⑧ EFOR 20<br>sapan merceğin sahne haritası ölçümle yeniden okunur [AGENTS §3]
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `1-111111111-1111111111111` (2 mercek); sapan: ① KARE, ④ HİKAYE, ⑤ ARKA PLAN, ⑥ FİZİK, ⑧ EFOR<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 7 mercek, 0 replik [D121]
- **GEÇERSİZ** — 🔴 TESLİM KUSURU — filigran ÖLÇÜMLE doğrulandı<br>Master üzerinde sabit köşe işareti var. Hiçbir mercek yeniden koşulmaz; önce master YENİDEN İHRAÇ EDİLİR [D150 · D177]. ⛔ %3 crop yetmez: temizlik kadraj genişliğinin %12'sini götürür.
