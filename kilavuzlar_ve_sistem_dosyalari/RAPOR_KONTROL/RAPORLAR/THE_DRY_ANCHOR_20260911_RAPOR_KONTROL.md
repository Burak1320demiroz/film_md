# 🧮 RAPOR KONTROL — THE_DRY_ANCHOR

> **Tarih:** 11.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_DRY_ANCHOR_KARE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ② DEVAMLILIK | `THE_DRY_ANCHOR_DEVAMLILIK_HAM.md` | GEÇERSİZ | None/None/None | 12/85.5/7.12 | 9/63.5/7.1 | — |
| ③ SES | `THE_DRY_ANCHOR_SES_HAM.md` | GEÇERSİZ | None/None/9.0 | None/None/None | None/0/None | — |
| ④ HİKAYE | `THE_DRY_ANCHOR_HIKAYE_HAM.md` | GEÇERSİZ | None/None/2.9 | None/None/None | None/0/None | — |
| ⑤ ARKA PLAN | `THE_DRY_ANCHOR_ARKA_PLAN_HAM.md` | GEÇERSİZ | None/None/None | 6/51.5/8.58 | 5/41.5/8.3 | — |
| ⑥ FİZİK | `THE_DRY_ANCHOR_FIZIK_HAM.md` | GEÇERSİZ | 7/49.0/7.0 | 7/49.2/7.03 | 7/49.2/7.0 | — |
| ⑦ AKSİYON | `THE_DRY_ANCHOR_AKSIYON_HAM.md` | GEÇERSİZ | None/None/None | 9/89/9.89 | 1/9/9.0 | — |
| ⑧ EFOR | `THE_DRY_ANCHOR_EFOR_HAM.md` | GEÇERSİZ | None/None/None | 7/18/2.57 | 7/18/2.6 | — |
| ⑨ KADRAJ | `THE_DRY_ANCHOR_KADRAJ_HAM.md` | GEÇERSİZ | 5/50.0/10.0 | None/None/None | None/0/None | — |
| ⑩ OYUNCULUK | `THE_DRY_ANCHOR_OYUNCULUK_HAM.md` | GEÇERSİZ | 9/40.0/4.4 | None/None/None | None/0/None | — |
| ⑪ IŞIK | `THE_DRY_ANCHOR_ISIK_HAM.md` | GEÇERSİZ | 7/57.0/8.1 | None/None/None | None/0/None | — |
| ⑫ HOOK | `THE_DRY_ANCHOR_HOOK_HAM.md` | GEÇERSİZ | 8/49.0/6.1 | None/None/None | None/0/None | — |

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ② DEVAMLILIK — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 3 hücre düzeltildi<br>Costume Identity 7/10 → — (issue: "-3.0 · 00:40 (S4) / 01:20 (S" — kusur yok, sayı taşıyamaz) [D186] · Wear, Damage & Injury 5/10 → — (issue: "-5.0 · Monotonic wear rule v" — kusur yok, sayı taşıyamaz) [D186] · Quantity & Character Count 10/10 → — (issue: "No deductions. Single actor " — kusur yok, sayı taşıyamaz) [D186]
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ④ HİKAYE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑤ ARKA PLAN — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 1 hücre düzeltildi<br>Focus Honesty 10/10 → — (issue: "no in-scope source") [D131]

## ⑥ FİZİK — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — ARİTMETİK FABRİKE — rapor n=7 Σ=49 yazdı; kendi hücreleri n=7 Σ=49.2 (ort 7.03)<br>Hiçbir hücre kümesi iddia edilen toplamı üretmiyor. Rubriğin kendi ④ kuralı: "the table is right and the overall is wrong" — satır tabloya GİRMEZ [D161].
- **ŞARTLI** — Material Behaviour 7/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Nominal regolith shear and fabric dynamics across all clips" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Scale & Measurement 7.2/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Fixed height ratios between astronaut (~1.7 m) and lander (~" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Rates & Timing 7/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Consistent strike frequency and locomotion speed across shot" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Light & Shadow Physics 7.2/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Fixed 15° sun angle yielding coherent 3.7:1 shadow length ra" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — Human Biomechanics 7/10 — kesintinin KAYNAĞI yazılı değil [D186]<br>issue: "Human kinematic constraints preserved in suit movements" · kural ④: kaynağı listelenmeyen kesinti UYGULANMAZ, kategori dolu başlar. Zaman kodu ya da defter satırı yaz.
- **ŞARTLI** — SEVERITY TALLY (0, 0, 2) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — SPEC NOVUM yazıyor, raporda PREMISE REGISTER YOK [D166]<br>STEP 0 koşulmamış → filmin kuralı kusur olarak puanlanmış olabilir; ⑩ ÖNERME KAPISI bu raporda ZORUNLU, kaynağı planda yazılı bulguların puanı geri verilir
- **ŞARTLI** — 8 hücre düzeltildi<br>Beat Anatomy 10/10 → — (issue: "no in-scope source") [D131] · Spatial Geography Under Motion 10/10 → — (issue: "no in-scope source") [D131] · Threat Vector & Approach 10/10 → — (issue: "no in-scope source") [D131] · Contact Legibility 10/10 → — (issue: "no in-scope source") [D131] · Consequence Visibility 10/10 → — (issue: "no in-scope source") [D131] · Camera's Contract with the Action 10/10 → — (issue: "no in-scope source") [D131] · Agency & Intent 10/10 → — (issue: "no in-scope source") [D131] · The Stakes Object 10/10 → — (issue: "no in-scope source") [D131]
- **ŞARTLI** — SEVERITY TALLY (0, 0, 1) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑧ EFOR — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **ŞARTLI** — SPEC NOVUM yazıyor, raporda PREMISE REGISTER YOK [D166]<br>STEP 0 koşulmamış → filmin kuralı kusur olarak puanlanmış olabilir; ⑩ ÖNERME KAPISI bu raporda ZORUNLU, kaynağı planda yazılı bulguların puanı geri verilir
- **ŞARTLI** — SEVERITY TALLY (4, 7, 3) ≠ yazılı etiketler (4, 4, 4) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑨ KADRAJ — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑩ OYUNCULUK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑪ IŞIK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑫ HOOK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu, rubriğin başına SPEC yapıştırılarak mod D tekrarlanır.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑤ ÇAPRAZ KAPI
- **GEÇERSİZ** — ⑤ KESME YAYILIMI 2 > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]<br>① KARE 13 · ⑥ FİZİK 13 · ⑨ KADRAJ 12 · ⑩ OYUNCULUK 12 · ⑪ IŞIK 11 · ⑫ HOOK 12
        ⭐ ÇÖZÜMÜ: master'ı ölç (olcum_kapisi.sh) ve --olcum-kesme <n> ile yeniden koş — ölçüm hakemdir, parti ayakta kalır [AGENTS §3]
- **ŞARTLI** — ⑦ ORTAK DEFTER ŞÜPHESİ — ⑨ KADRAJ + ⑩ OYUNCULUK künyeleri BİREBİR aynı [D110]<br>kesme 12 · sahne 13 · şerit 1111111111111 — ve bu künye çoğunluktan sapıyor. Aynı oturumda arka arkaya koşulan iki mercek tek ölçümün iki kılıfı olabilir: azınlık İKİ oy değil, BİR oydur. ⛔ Doğrulama: iki raporun kesme ZAMAN KODLARI var mı? Yoksa sayım yapılmamış, devralınmıştır — o mercekler temiz oturumda yeniden koşulur.
- **GEÇERSİZ** — 🚨 TESLİM ŞÜPHESİ — plan 14 sahne yazıyor, 3 mercek 13 sahne saydı [D188]<br>kaynak: THE_DRY_ANCHOR_BOLUM_1.md + THE_DRY_ANCHOR_BOLUM_2.md · fark +1 sahne (≈ 1 klip). ⛔ İKİ ŞIK VAR ve rapor tarafından ayrılamaz: (a) makara eksik teslim edildi · (b) mercekler yanlış saydı. Merceklerin birbirini doğrulaması hiçbirini elemez: hepsi aynı makarayı izliyor, ve hem eksik makara hem ortak sayım hatası OYBİRLİĞİYLE onaylanır. Parti dışındaki tek referans plandır, hakem ise ölçümdür: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>` → `--olcum-sahne <n>`. ⛔ O gelene kadar kesme listesi, REMOVE reçetesi ve yeniden üretim UYGULANMAZ [D46 süre muhasebesi].
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `1111111111111` (5 mercek); sapan: ⑧ EFOR, ⑪ IŞIK, ⑫ HOOK<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 5 mercek, 0 replik [D121]
- **ŞARTLI** — 🚨 SUSKUNLUK — ⑤ ARKA PLAN film boyu iddia: filigran / sabit köşe işareti; sahibi ① KARE SUSTU [D162]<br>"…e Edges & Emergent Artifacts | 6.0/10 | -4.0 · 00:00–02:19 (static teal triangular watermark logo in bottom-right corner) |  ---  ## PRESENCE STRING  `111111…" → kareyle çözülür (⑪ köşe testi / tek kare); çözülene kadar HER İKİ merceğin o kategorisi sayı taşımaz
- **ŞARTLI** — 🚨 SUSKUNLUK — ⑫ HOOK film boyu iddia: filigran / sabit köşe işareti; sahibi ① KARE SUSTU [D162]<br>"…RMAT (00:00–00:28) — Standard 16:9 landscape file verified; watermark present in lower corner. SEVERITY TALLY 🔴 BLOCKER: 0   🟠 MA…" → kareyle çözülür (⑪ köşe testi / tek kare); çözülene kadar HER İKİ merceğin o kategorisi sayı taşımaz
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
