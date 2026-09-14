# 🧮 RAPOR KONTROL — THE_TETHERED_MASS

> **Tarih:** 11.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ⑩ OYUNCULUK | `THE_TETHERED_MASS_OYUNCULUK_HAM.md` | GEÇERSİZ | 9/49.5/5.5 | 9/51.5/5.72 | 9/51.5/5.7 | — |
| ⑪ IŞIK | `THE_TETHERED_MASS_ISIK_HAM.md` | GEÇERSİZ | 7/46.0/6.6 | 7/46/6.57 | 6/40/6.7 | — |
| ⑫ HOOK | `THE_TETHERED_MASS_HOOK_HAM.md` | GEÇERSİZ | None/None/None | 8/68/8.5 | 3/23/7.7 | — |
| ① KARE | `THE_TETHERED_MASS_KARE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ② DEVAMLILIK | `THE_TETHERED_MASS_DEVAMLILIK_HAM.md` | GEÇERSİZ | 12/75.0/6.3 | 12/75/6.25 | 12/75/6.2 | — |
| ③ SES | `THE_TETHERED_MASS_SES_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ④ HİKAYE | `THE_TETHERED_MASS_HIKAYE_HAM.md` | GEÇERSİZ | None/None/7.4 | None/None/None | None/0/None | — |
| ⑤ ARKA PLAN | `THE_TETHERED_MASS_ARKA_PLAN_HAM.md` | GEÇERSİZ | 6/40.0/6.7 | 6/40/6.67 | 6/40/6.7 | — |
| ⑥ FİZİK | `THE_TETHERED_MASS_FIZIK_HAM.md` | GEÇERSİZ | None/None/None | 7/45/6.43 | 7/45/6.4 | — |
| ⑦ AKSİYON | `THE_TETHERED_MASS_AKSIYON_HAM.md` | GEÇERSİZ | 9/67.0/7.4 | 9/67/7.44 | 9/67/7.4 | — |
| ⑧ EFOR | `THE_TETHERED_MASS_EFOR_HAM.md` | GEÇERSİZ | 7/7.0/1.0 | 7/7/1.0 | 7/7/1.0 | — |
| ⑨ KADRAJ | `THE_TETHERED_MASS_KADRAJ_HAM.md` | GEÇERSİZ | None/None/None | 6/49/8.17 | 5/39/7.8 | — |

## ⑩ OYUNCULUK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **GEÇERSİZ** — ARİTMETİK FABRİKE — rapor n=9 Σ=49.5 yazdı; kendi hücreleri n=9 Σ=51.5 (ort 5.72)<br>Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "the table is right and the overall is wrong" — satır tabloya GİRMEZ [D161].
- **ŞARTLI** — PRESENCE STRING 16 hane, kesme+1 = 15<br>şerit sahne başına bir hanedir; sayı tutmuyorsa harita ya da sayım yanlış [D118]

## ⑪ IŞIK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — 1 hücre düzeltildi<br>Colour Temperature 6/10 → — (issue: "-4 · S27 (01:57) → S28 (02:0" — kusur yok, sayı taşıyamaz) [D186]
- **ŞARTLI** — KEY DIRECTION STRING 29 hane, kesme+1 = 32<br>dizi sahne başına bir hanedir; tutmuyorsa defter ya da kesme sayımı yanlış

## ⑫ HOOK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod ? koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — 5 hücre düzeltildi<br>Cover Second 9/10 → — (issue: "no in-scope source") [D131] · Share Moments Stand Alone 8/10 → — (issue: "no in-scope source") [D131] · Peak Placement 9/10 → — (issue: "no in-scope source") [D131] · Exit & Return 9/10 → — (issue: "no in-scope source") [D131] · Format Fit 10/10 → — (issue: "no in-scope source") [D131]

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ② DEVAMLILIK — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑤ ARKA PLAN — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — SEVERITY TALLY (0, 4, 5) ≠ yazılı etiketler (0, 3, 4) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑥ FİZİK — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (0, 3, 4) ≠ yazılı etiketler (0, 3, 2) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (0, 1, 8) ≠ yazılı etiketler (0, 1, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑧ EFOR — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SEVERITY TALLY (0, 4, 5) ≠ yazılı etiketler (0, 3, 7) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — COST CURVE sabit (0) ama efor olayı var<br>iş yapıldıysa borç ya artar ya toparlanır; düz eğri ÖLÇMEDİ demektir

## ⑨ KADRAJ — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod ? koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — 1 hücre düzeltildi<br>Rhyme Pair 10/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SETUP STRING 38 hane, plan iskeleti 17 hane<br>iki dizi aynı sahne sayısını saymalı; uzunluk tutmadan sapma okunamaz

## ⑤ ÇAPRAZ KAPI
- **GEÇERSİZ** — ⑤ KESME YAYILIMI 18 > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]<br>⑩ OYUNCULUK 14 · ⑪ IŞIK 31 · ① KARE 14 · ② DEVAMLILIK 32 · ⑤ ARKA PLAN 32 · ⑦ AKSİYON 14 · ⑧ EFOR 31
        ⭐ ÇÖZÜMÜ: master'ı ölç (olcum_kapisi.sh) ve --olcum-kesme <n> ile yeniden koş — ölçüm hakemdir, parti ayakta kalır [AGENTS §3]
- **ŞARTLI** — ⑤ sahne sayıları ayrışıyor: ⑩ OYUNCULUK 15 · ⑪ IŞIK 32 · ② DEVAMLILIK 32 · ⑤ ARKA PLAN 32 · ⑦ AKSİYON 15 · ⑧ EFOR 32
- **ŞARTLI** — ⑦ ORTAK DEFTER ŞÜPHESİ — ⑪ IŞIK + ⑧ EFOR künyeleri BİREBİR aynı [D110]<br>kesme 31 · sahne 32 · şerit 11111111111111111111111111111111 — ve bu künye çoğunluktan sapıyor. Aynı oturumda arka arkaya koşulan iki mercek tek ölçümün iki kılıfı olabilir: azınlık İKİ oy değil, BİR oydur. ⛔ Doğrulama: iki raporun kesme ZAMAN KODLARI var mı? Yoksa sayım yapılmamış, devralınmıştır — o mercekler temiz oturumda yeniden koşulur.
- **GEÇERSİZ** — 🚨 TESLİM ŞÜPHESİ — plan 16 sahne yazıyor, 4 mercek 32 sahne saydı [D188]<br>kaynak: THE_TETHERED_MASS_BOLUM_1.md + THE_TETHERED_MASS_BOLUM_2.md · fark -16 sahne (≈ 16 klip). ⛔ İKİ ŞIK VAR ve rapor tarafından ayrılamaz: (a) makara eksik teslim edildi · (b) mercekler yanlış saydı. Merceklerin birbirini doğrulaması hiçbirini elemez: hepsi aynı makarayı izliyor, ve hem eksik makara hem ortak sayım hatası OYBİRLİĞİYLE onaylanır. Parti dışındaki tek referans plandır, hakem ise ölçümdür: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>` → `--olcum-sahne <n>`. ⛔ O gelene kadar kesme listesi, REMOVE reçetesi ve yeniden üretim UYGULANMAZ [D46 süre muhasebesi].
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `11111111111111111111111111111111` (3 mercek); sapan: ⑩ OYUNCULUK, ⑫ HOOK, ⑥ FİZİK, ⑦ AKSİYON, ⑨ KADRAJ<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 6 mercek, 0 replik [D121]
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
