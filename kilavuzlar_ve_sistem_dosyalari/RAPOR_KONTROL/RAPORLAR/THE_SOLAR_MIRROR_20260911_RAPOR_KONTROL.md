# 🧮 RAPOR KONTROL — THE_SOLAR_MIRROR

> **Tarih:** 11.09.2026 · betikten üretildi, elle düzenlenmez · kaynak: `rapor_kontrol.py`

| mercek | dosya | karar | iddia n/Σ/ort | hücreler n/Σ/ort | düzeltme sonrası | TABLOYA |
|---|---|:--:|---|---|---|---|
| ① KARE | `THE_SOLAR_MIRROR_KARE_HAM.md` | GEÇERSİZ | None/None/None | None/None/None | None/0/None | — |
| ② DEVAMLILIK | `THE_SOLAR_MIRROR_DEVAMLILIK_HAM.md` | ŞARTLI | None/None/None | 12/115/9.58 | 5/45/9.0 | 9.0 ⚠️ ŞARTLI |
| ③ SES | `THE_SOLAR_MIRROR_SES_HAM.md` | GEÇERSİZ | None/None/8.6 | None/None/None | None/0/None | — |

## ① KARE — GEÇERSİZ
- **TEKRAR** — SPEC dosyası VAR, rapor mod ? → koşu TEKRARLANIR [D129]<br>ham rapor 02/'ye düşer, T tablosuna satır YAZILMAZ, kesme listesi / REMOVE / yeniden üretim UYGULANMAZ. Mod D: _KAYNAK/ rubriği + <FILM>_QA_SPEC.md AYNI mesajda, SPEC başta.
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ② DEVAMLILIK — ŞARTLI
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **ŞARTLI** — 7 hücre düzeltildi<br>Identity — Face, Hair & Build 10/10 → — (issue: "No deductions. Face geometry" — kusur yok, sayı taşıyamaz) [D186] · Wear, Damage & Injury 10/10 → — (issue: "No deductions. Suit cleanlin" — kusur yok, sayı taşıyamaz) [D186] · Equipment & Carried Objects 10/10 → — (issue: "No deductions. Tool loss at " — kusur yok, sayı taşıyamaz) [D186] · Spatial Geography 10/10 → — (issue: "No deductions. Spatial relat" — kusur yok, sayı taşıyamaz) [D186] · Time & Light Logic 10/10 → — (issue: "No deductions. Key sunlight " — kusur yok, sayı taşıyamaz) [D186] · World State & Prop Continuity 10/10 → — (issue: "No deductions. Array explosi" — kusur yok, sayı taşıyamaz) [D186] · Causality & Knowledge Logic 10/10 → — (issue: "No deductions. Pulling emerg" — kusur yok, sayı taşıyamaz) [D186]

## ③ SES — GEÇERSİZ
- **NOT** — bu merceğe belge verilmez — mod V tasarımdır; FLAGS koşudan SONRA SPEC C bloğundan cevaplanır
- **GEÇERSİZ** — SCORES SUMMARY tablosu okunamadı — hücre yok, ortalama doğrulanamaz

## ⑤ ÇAPRAZ KAPI
- **ŞARTLI** — MERCEK YOKLAMASI — 1 zorunlu mercek HİÇ koşmadı<br>Eksik: ④ HİKAYE. Koşan: ① KARE · ② DEVAMLILIK · ③ SES. FİLM için zorunlu küme: ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE [D111]. Eksik mercek 'bulgu yok' DEĞİLDİR; ölçülmemiş eksendir ve tamlık matrisine giremez.
- **ŞARTLI** — filigran ekseni ÖLÇÜLMEDİ<br>⑪ KÖŞE TESTİ sonucu verilmedi (`--olcum-filigran VAR|YOK`). Sekiz raporun sekizi de filigran bulgusu 0 yazabilir ve bu bir ölçüm DEĞİLDİR [D177]. Kesme/sahne sayısı için zaten var olan hakemliğin aynısı: `bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>`
