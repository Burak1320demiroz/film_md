# 🧮 RAPOR KONTROL — THE_HARD_DOCK

> **Tarih:** 12.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_HARD_DOCK_KARE_HAM.md` | GO | None/None/None | 9/67/7.44 | 9/67/7.4 | 7.4 |
| ② DEVAMLILIK | `THE_HARD_DOCK_DEVAMLILIK_HAM.md` | ŞARTLI | 12/109.0/9.1 | 12/109/9.08 | 12/109/9.1 | 9.1 ⚠️ ŞARTLI |
| ③ SES | `THE_HARD_DOCK_SES_HAM.md` | ŞARTLI | None/None/None | 9/80/8.89 | 4/34/8.5 | 8.5 ⚠️ ŞARTLI |

## ① KARE — GO

## ② DEVAMLILIK — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — Counter Logic N/A — ama SPEC sayaç yazıyor → ÖLÇÜM BOŞLUĞU, yokluk değil [D134]<br>kilit defterine ⬜ AÇIK; ②'nin sayaç satırı kareyle doldurulur
- **ŞARTLI** — kesme 15 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ③ SES — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 5 hücre düzeltildi<br>Speaker Attribution 10/10 → N/A (0 replik — sessizlik tasarımdır) · Synthetic Voice Tells 9/10 → N/A (0 replik — sessizlik tasarımdır) · Voice Identity 9/10 → — (issue: "-1 · 00:13 vs 03:51: Timbre " — kusur yok, sayı taşıyamaz) [D186] · Delivery vs Performance 9/10 → N/A (0 replik — sessizlik tasarımdır) · Turn-Taking & Acoustics 9/10 → N/A (0 replik — sessizlik tasarımdır)
- **ŞARTLI** — kesme 19 ≠ ÖLÇÜM 24 → bu merceğin FİLM BOYU sayıları ŞARTLI<br>ölçüm kazanır [AGENTS §3]; kesme/sahne türevi hükümler (REMOVE reçetesi, sıra iddiası, film boyu kategori) bu rapordan ALINMAZ

## ⑤ ÇAPRAZ KAPI
- **NOT** — ⑪ ÖLÇÜM HAKEM: kesme = 24 (ölçüldü) · raporlar: ① KARE 24 · ② DEVAMLILIK 15 · ③ SES 19
- **ŞARTLI** — ⑤ ölçümden sapan mercek(ler): ② DEVAMLILIK 15 · ③ SES 19<br>parti AYAKTA — anlaşmazlık ölçümle çözüldü; yalnız sapan mercek şartlıdır
- **ŞARTLI** — ⑤ sahne — ÖLÇÜM 24; sapan: ② DEVAMLILIK 16<br>sapan merceğin sahne haritası ölçümle yeniden okunur [AGENTS §3]
- **NOT** — ①.9 teslim ekseni doğrulandı — plan 24 sahne, ÖLÇÜM 24 [D188] · kaynak: THE_HARD_DOCK_BOLUM_1.md + THE_HARD_DOCK_BOLUM_2.md
- **ŞARTLI** — ⑤ replik sayıları ayrışıyor: ② DEVAMLILIK 9 · ③ SES 0<br>alıntı kimin yanıldığını söyler; LINES HEARD satırları yan yana okunur
- **ŞARTLI** — MERCEK YOKLAMASI — 1 zorunlu mercek HİÇ koşmadı<br>Eksik: ④ HİKAYE. Koşan: ① KARE · ② DEVAMLILIK · ③ SES. FİLM için zorunlu küme: ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE [D111]. Eksik mercek 'bulgu yok' DEĞİLDİR; ölçülmemiş eksendir ve tamlık matrisine giremez.
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
