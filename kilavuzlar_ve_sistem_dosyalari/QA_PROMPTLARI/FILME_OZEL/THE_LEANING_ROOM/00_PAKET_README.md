# 📦 QA PAKETİ — THE_LEANING_ROOM

> Betikten üretildi (02.09.2026 · `rubrik_paketle.sh`). Elle düzenlenmez; SPEC değişince yeniden üretilir.
> Kaynak SPEC: `yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM/THE_LEANING_ROOM_QA_SPEC.md` · aile: yatay

| dosya | mercek | mod | belge |
|---|---|:--:|---|
| PAKET_1_KARE.md | ① KARE | **D** | A + B + UYARI |
| PAKET_2_DEVAMLILIK.md | ② DEVAMLILIK | V | yok (tasarım) |
| PAKET_3_SES.md | ③ SES | V | yok (tasarım) |
| PAKET_4_HIKAYE.md | ④ HİKAYE | **D** | A + UYARI |
| PAKET_5_ARKA_PLAN.md | ⑤ ARKA PLAN | V | yalnız üç kilit [D133] |
| PAKET_6_FIZIK.md | ⑥ FİZİK | **D** | sayısal kilitler |
| PAKET_7_AKSIYON.md | ⑦ AKSİYON | **D** | A + C · risk tetikli |
| PAKET_8_EFOR.md | ⑧ EFOR | **D** | A + C · risk tetikli |

## Koşu
1. Master'ı ÖNCE ölç: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"` [⑪]
2. Her mercek AYRI ve TEMİZ oturumda [D110]; hepsine AYNI dosya [D75].
   ⛔ ①-④ ZORUNLU. ⑤⑥⑦⑧ risk tetiklidir — filmin risk kartları hangisini
   yazıyorsa o koşulur (00_README "hangi filme hangi mercekler"). Tetiklenmemiş
   merceği koşmamak eksik koşu DEĞİLDİR; tetiklenmişi koşmamak kartı okumamaktır.
3. Her paketin TAMAMINI yapıştır (künye + rubrik + belge) — yalnız kod bloğu değil.
4. Gelen raporu `02_HAM_RAPORLAR/`'a olduğu gibi kaydet, sonra:
   `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <raporlar> --film yatay_2_4_dk_filmler_uzay/THE_LEANING_ROOM --rapor --olcum-kesme <n> --olcum-sahne <n>`
   (⑪ ölçüm sayıları adım 1'den gelir; verilmezse kesme yayılımı partiyi toptan düşürür)
   GEÇERSİZ / TEKRAR dönerse T tablosuna satır YAZILMAZ.
