# 🧮 RAPOR KONTROL — THE_SHATTERED_BREATH

> **Tarih:** 13.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ⑦ AKSİYON | `THE_SHATTERED_BREATH_AKSIYON_HAM.md` | TEKRAR | None/None/None | 9/77/8.56 | 6/50/8.3 | — |
| ⑤ ARKA PLAN | `THE_SHATTERED_BREATH_ARKA_PLAN_HAM.md` | ŞARTLI | None/None/None | 6/50/8.33 | 6/50/8.3 | 8.3 ⚠️ ŞARTLI |
| ② DEVAMLILIK | `THE_SHATTERED_BREATH_DEVAMLILIK_HAM.md` | ŞARTLI | None/None/None | 13/109/8.38 | 9/69/7.7 | 7.7 ⚠️ ŞARTLI |
| ⑧ EFOR | `THE_SHATTERED_BREATH_EFOR_HAM.md` | TEKRAR | 7/19.0/2.7 | 7/19/2.71 | 7/19/2.7 | — |
| ⑥ FİZİK | `THE_SHATTERED_BREATH_FIZIK_HAM.md` | TEKRAR | 7/49.0/7.0 | 7/49/7.0 | 7/49/7.0 | — |
| ④ HİKAYE | `THE_SHATTERED_BREATH_HIKAYE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ⑫ HOOK | `THE_SHATTERED_BREATH_HOOK_HAM.md` | GEÇERSİZ | None/None/None | 8/71/8.88 | 5/41/8.2 | — |
| ⑪ IŞIK | `THE_SHATTERED_BREATH_ISIK_HAM.md` | GEÇERSİZ | 7/27.0/3.9 | 7/27/3.86 | 7/27/3.9 | — |
| ⑨ KADRAJ | `THE_SHATTERED_BREATH_KADRAJ_HAM.md` | GEÇERSİZ | None/None/None | 5/50/10.0 | 0/0/None | — |
| ① KARE | `THE_SHATTERED_BREATH_KARE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ⑩ OYUNCULUK | `THE_SHATTERED_BREATH_OYUNCULUK_HAM.md` | GEÇERSİZ | 9/43.0/4.8 | 9/43/4.78 | 9/43/4.8 | — |
| ③ SES | `THE_SHATTERED_BREATH_SES_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |

## ⑦ AKSİYON — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — SPEC NOVUM yazıyor, raporda PREMISE REGISTER YOK [D166]<br>STEP 0 koşulmamış → filmin kuralı kusur olarak puanlanmış olabilir; ⑩ ÖNERME KAPISI bu raporda ZORUNLU, kaynağı planda yazılı bulguların puanı geri verilir
- **ŞARTLI** — 3 hücre düzeltildi<br>Consequence Visibility 9/10 → — (issue: "no in-scope source") [D131] · Camera's Contract with the Action 9/10 → — (issue: "no in-scope source") [D131] · Agency & Intent 9/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SEVERITY TALLY (0, 0, 4) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑤ ARKA PLAN — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — SEVERITY TALLY (0, 2, 2) ≠ yazılı etiketler (0, 2, 1) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ② DEVAMLILIK — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 4 hücre düzeltildi<br>Counter Logic 10/10 → — (issue: "no in-scope source") [D131] · Causality & Knowledge Logic 10/10 → — (issue: "no in-scope source") [D131] · Quantity & Character Count 10/10 → — (issue: "no in-scope source") [D131] · Setup & Abandonment 10/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur

## ⑧ EFOR — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — PREMISE REGISTER yalnız ORTAMI yazıyor, filmin KURALINI değil [D166]<br>kayıtlı: "· gravity / medium        [lunar/extraterrestrial vacuum surface, low-gravity visual setti…" · SPEC'te NOVUM var → ⑩ ÖNERME KAPISI ZORUNLU; novum kaynaklı kesintiler DÜŞER ve ortalama yeniden hesaplanır [D130]

## ⑥ FİZİK — TEKRAR
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — SEVERITY TALLY (0, 0, 1) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑫ HOOK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod ? koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **ŞARTLI** — 3 hücre düzeltildi<br>Cover Second 10/10 → — (issue: "no in-scope source") [D131] · Share Moments Stand Alone 10/10 → — (issue: "no in-scope source") [D131] · Format Fit 10/10 → — (issue: "no in-scope source") [D131]

## ⑪ IŞIK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.

## ⑨ KADRAJ — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod ? koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **ŞARTLI** — 5 hücre düzeltildi<br>Lockoff Integrity 10/10 → — (issue: "no in-scope source") [D131] · Rhyme Pair 10/10 → — (issue: "no in-scope source") [D131] · Return Consistency 10/10 → — (issue: "no in-scope source") [D131] · Angle Arc & Deliberate Shocks 10/10 → — (issue: "no in-scope source") [D131] · Screen Geometry 10/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SETUP STRING 12 hane, plan iskeleti 13 hane<br>iki dizi aynı sahne sayısını saymalı; uzunluk tutmadan sapma okunamaz

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑩ OYUNCULUK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **ŞARTLI** — süre 41 s ≠ ortanca (4 mercek) 124 s (tolerans ±12.4) → ZAMAN EKSENİ uydurma sayılır [D205]<br>zaman kodları, DROP-OFF saniyeleri ve sahne aralıkları bu rapordan ALINMAZ; mercek temiz oturumda yeniden koşulur [D112 · D125]

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑤ ÇAPRAZ KAPI
- **NOT** — ⑤ kesme sayıları birbirini doğruluyor (yayılım 0): ⑧ EFOR 11 · ⑥ FİZİK 11 · ⑪ IŞIK 11 · ⑩ OYUNCULUK 11
- **ŞARTLI** — ⑤ SÜRE — ortanca (4 mercek) 124 s; sapan: ⑩ OYUNCULUK 41 [D205]<br>⑧ EFOR 124 · ⑥ FİZİK 125 · ⑪ IŞIK 124 · ⑩ OYUNCULUK 41
        süre bir DOSYA özelliğidir; aynı makaraya bakan iki merceğin süresi %10'dan fazla ayrışamaz — sapan merceğin zaman ekseni 🚨, parti düşmez
- **ŞARTLI** — ⑦ ORTAK DEFTER ŞÜPHESİ — ⑧ EFOR + ⑥ FİZİK + ⑪ IŞIK + ⑩ OYUNCULUK künyeleri BİREBİR aynı [D110]<br>kesme 11 · sahne 12 · şerit 111111111111 — ve bu künye çoğunluktan sapıyor. Aynı oturumda arka arkaya koşulan iki mercek tek ölçümün iki kılıfı olabilir: azınlık İKİ oy değil, BİR oydur. ⛔ Doğrulama: iki raporun kesme ZAMAN KODLARI var mı? Yoksa sayım yapılmamış, devralınmıştır — o mercekler temiz oturumda yeniden koşulur.
- **NOT** — ①.9 teslim ekseni doğrulandı — plan 12 sahne, 4 merceğin çoğunluğu 12 [D188] · kaynak: THE_SHATTERED_BREATH_BOLUM_1.md + THE_SHATTERED_BREATH_BOLUM_2.md
- **NOT** — ⑤ şerit ekseni doğrulandı — 8 mercek `111111111111`
- **NOT** — ⑤ replik ekseni doğrulandı — 4 mercek, 0 replik [D121]
- **ŞARTLI** — 🚨 SUSKUNLUK — ⑤ ARKA PLAN film boyu iddia: filigran / sabit köşe işareti; sahibi ① KARE SUSTU [D162]<br>"…Frame Edges & Emergent Artifacts | 7/10 | -3 · 00:00–01:59 (persistent AI generator logo watermark in bottom-right corner across all scenes) |  ---  ## PRESEN…" → kareyle çözülür (⑪ köşe testi / tek kare); çözülene kadar HER İKİ merceğin o kategorisi sayı taşımaz
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
