# 🧮 RAPOR KONTROL — THE_GRAVITY_ANCHOR

> **Tarih:** 10.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ⑩ OYUNCULUK | `THE_GRAVITY_ANCHOR_OYUNCULUK_HAM.md` | GEÇERSİZ | 9/57.0/6.3 | 9/57/6.33 | 9/57/6.3 | — |
| ⑪ IŞIK | `THE_GRAVITY_ANCHOR_ISIK_HAM.md` | GEÇERSİZ | None/None/None | 7/36/5.14 | 7/36/5.1 | — |
| ⑫ HOOK | `THE_GRAVITY_ANCHOR_HOOK_HAM.md` | GEÇERSİZ | 8/62.5/7.8 | 8/62.5/7.81 | 7/53.5/7.6 | — |
| ① KARE | `THE_GRAVITY_ANCHOR_KARE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ② DEVAMLILIK | `THE_GRAVITY_ANCHOR_DEVAMLILIK_HAM.md` | GEÇERSİZ | 12/66.0/5.5 | 12/66/5.5 | 12/66/5.5 | — |
| ③ SES | `THE_GRAVITY_ANCHOR_SES_HAM.md` | GEÇERSİZ | None/None/8.5 | None/None/None | None/0/None | — |
| ④ HİKAYE | `THE_GRAVITY_ANCHOR_HIKAYE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ⑤ ARKA PLAN | `THE_GRAVITY_ANCHOR_ARKA_PLAN_HAM.md` | GEÇERSİZ | 6/34.0/5.7 | 6/34/5.67 | 6/34/5.7 | — |
| ⑦ AKSİYON | `THE_GRAVITY_ANCHOR_AKSIYON_HAM.md` | GEÇERSİZ | 9/85.0/9.4 | 9/85/9.44 | 4/35/8.8 | — |
| ⑧ EFOR | `THE_GRAVITY_ANCHOR_EFOR_HAM.md` | GEÇERSİZ | 8/16.0/2.0 | 8/16/2.0 | 8/16/2.0 | — |
| ⑨ KADRAJ | `THE_GRAVITY_ANCHOR_KADRAJ_HAM.md` | GEÇERSİZ | 3/17.0/5.7 | 3/17/5.67 | 3/17/5.7 | — |

## ⑩ OYUNCULUK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — SEVERITY TALLY (0, 0, 8) ≠ yazılı etiketler (0, 0, 9) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]
- **ŞARTLI** — GAZE STRING YOK ya da `OBSERVED:` satırı okunamadı<br>bu merceğin makine çıktısı dizidir; dizisiz rapor sahne sahne sınanamaz

## ⑪ IŞIK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod ? koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.

## ⑫ HOOK — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — 1 hücre düzeltildi<br>Format Fit 9/10 → — (issue: "16:9 frame geometry clean an" — kusur yok, sayı taşıyamaz) [D186]

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

## ⑦ AKSİYON — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod V → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — 5 hücre düzeltildi<br>Beat Anatomy 10/10 → — (issue: "no in-scope source") [D131] · Contact Legibility 10/10 → — (issue: "no in-scope source") [D131] · Consequence Visibility 10/10 → — (issue: "no in-scope source") [D131] · Camera's Contract with the Action 10/10 → — (issue: "no in-scope source") [D131] · Agency & Intent 10/10 → — (issue: "no in-scope source") [D131]

## ⑧ EFOR — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Paket: qa-isle/scripts/rubrik_paketle.sh <film klasörü>
- **ŞARTLI** — SPEC NOVUM yazıyor, raporda PREMISE REGISTER YOK [D166]<br>STEP 0 koşulmamış → filmin kuralı kusur olarak puanlanmış olabilir; ⑩ ÖNERME KAPISI bu raporda ZORUNLU, kaynağı planda yazılı bulguların puanı geri verilir
- **ŞARTLI** — SEVERITY TALLY (2, 4, 2) ≠ yazılı etiketler (2, 2, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑨ KADRAJ — GEÇERSİZ
- **GEÇERSİZ** — ⑨-⑫ PLAN SADAKATİ MERCEĞİ mod V koşulmuş → koşu GEÇERSİZ [D190 · D184]<br>Bu dörtlü belgesiz koşulduğunda ekrandan bir plan uydurur ve kusuru NİYET sanıp puanlar. Rapor karantinadadır: T9-T12'ye satır girmez, 00_INDEX'te hücre ❌ KALIR, hiçbir bulgusu ders/sipariş üretmez. Koşu PAKET_9..12 ile mod D tekrarlanır.
- **ŞARTLI** — SEVERITY TALLY (1, 0, 1) ≠ yazılı etiketler (0, 0, 0) (🔴,🟠,🟡)<br>verdict bu tally'den türetildi → REGENERATE / kesme hükmü UYGULANMAZ [D161]

## ⑤ ÇAPRAZ KAPI
- **GEÇERSİZ** — ⑤ KESME YAYILIMI 12 > 1 → PARTİNİN TÜM SATIRLARI GEÇERSİZ [D107]<br>⑩ OYUNCULUK 9 · ⑫ HOOK 9 · ② DEVAMLILIK 21 · ⑤ ARKA PLAN 21 · ⑦ AKSİYON 9 · ⑨ KADRAJ 9
        ⭐ ÇÖZÜMÜ: master'ı ölç (olcum_kapisi.sh) ve --olcum-kesme <n> ile yeniden koş — ölçüm hakemdir, parti ayakta kalır [AGENTS §3]
- **ŞARTLI** — ⑤ sahne sayıları ayrışıyor: ⑩ OYUNCULUK 10 · ⑫ HOOK 10 · ② DEVAMLILIK 22 · ⑤ ARKA PLAN 22 · ⑦ AKSİYON 10 · ⑨ KADRAJ 10
- **ŞARTLI** — ⑦ ORTAK DEFTER ŞÜPHESİ — ⑩ OYUNCULUK + ⑫ HOOK + ⑦ AKSİYON + ⑨ KADRAJ künyeleri BİREBİR aynı [D110]<br>kesme 9 · sahne 10 · şerit 1111111111 — ve bu künye çoğunluktan sapıyor. Aynı oturumda arka arkaya koşulan iki mercek tek ölçümün iki kılıfı olabilir: azınlık İKİ oy değil, BİR oydur. ⛔ Doğrulama: iki raporun kesme ZAMAN KODLARI var mı? Yoksa sayım yapılmamış, devralınmıştır — o mercekler temiz oturumda yeniden koşulur.
- **NOT** — ①.9 teslim ekseni doğrulandı — plan 10 sahne, 4 merceğin çoğunluğu 10 [D188] · kaynak: THE_GRAVITY_ANCHOR_BOLUM_1.md
- **ŞARTLI** — ⑤ ŞERİT — çoğunluk `1111111111` (6 mercek); sapan: ⑤ ARKA PLAN<br>sapan merceğin şeridi 🚨; ÖNCE kendi sahne envanteriyle karşılaştırılır [D135]
- **NOT** — ⑤ replik ekseni doğrulandı — 5 mercek, 0 replik [D121]
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
