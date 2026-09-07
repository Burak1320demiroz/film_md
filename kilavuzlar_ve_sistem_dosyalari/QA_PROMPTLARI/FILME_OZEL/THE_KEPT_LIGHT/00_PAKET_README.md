# 📦 QA PAKETİ — THE_KEPT_LIGHT

> Betikten üretildi (06.09.2026 · `rubrik_paketle.sh`). Elle düzenlenmez; SPEC değişince yeniden üretilir.
> Kaynak SPEC: `yatay_3_5_dk_filmler/THE_KEPT_LIGHT/THE_KEPT_LIGHT_QA_SPEC.md` · aile: yatay

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
| PAKET_9_KADRAJ.md | ⑨ KADRAJ | **D** | B + C(eş kadraj · ekran yönü) · koşul: KURULUM İSKELETİ var |
| PAKET_10_OYUNCULUK.md | ⑩ OYUNCULUK | **D** | A + C(insan · kask · ekran yönü) · koşul: replik 0 ya da CENTRAL CHOICE var |
| PAKET_11_ISIK.md | ⑪ IŞIK | **D** | C(ışık takvimi · atmosfer · yapı · kask) + ızgara · koşul: IŞIK TAKVİMİ var ya da ≥12 klip |
| PAKET_12_HOOK.md | ⑫ HOOK | **D** | A + B + KAPAK ANI · koşul: film yayınlanacak (kart Y) |

## Koşu
1. Master'ı ÖNCE ölç: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"` [⑪]
2. Her mercek AYRI ve TEMİZ oturumda [D110]; hepsine AYNI dosya [D75].
   ⛔ ①-④ ZORUNLU. ⑤⑥⑦⑧ risk tetiklidir — filmin risk kartları hangisini
   yazıyorsa o koşulur (00_README "hangi filme hangi mercekler"). Tetiklenmemiş
   merceği koşmamak eksik koşu DEĞİLDİR; tetiklenmişi koşmamak kartı okumamaktır.
   ⑨⑩⑪⑫ PLAN SADAKATİ mercekleridir [D184]: koşulu tablonun son sütununda;
   dördü de SPEC'siz koşulmaz (belgesiz koşu tanım gereği boş).
   ⛔ HAM ZİNCİR çıkan master'a (adım 1 · TESLİM SINIFI) HİÇBİR mercek koşulmaz.
3. Her paketin TAMAMINI yapıştır (künye + rubrik + belge) — yalnız kod bloğu değil.
4. Gelen raporu `02_HAM_RAPORLAR/`'a olduğu gibi kaydet, sonra:
   `python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <raporlar> --film yatay_3_5_dk_filmler/THE_KEPT_LIGHT --rapor --olcum-kesme <n> --olcum-sahne <n>`
   (⑪ ölçüm sayıları adım 1'den gelir; verilmezse kesme yayılımı partiyi toptan düşürür)
   GEÇERSİZ / TEKRAR dönerse T tablosuna satır YAZILMAZ.
