# 🔊 THE ROSE COAT — ③ SES HAM RAPORU

> **Koşu:** 26.08.2026 · video-only (bu merceğin tek modu)
> **Rubrik:** `../../QA_PROMPTLARI/3_SES_QA_CRITIQUE_PROMPT.md`
> ⛔ Aşağısı MODELİN ÇIKTISIDIR, düzeltilmemiştir.

---

```
AUDIO ABSENT — RUN NOT STARTED
The file contains no audio information across its full runtime. This rubric
cannot distinguish a deliberately silent film from an upload whose audio track
was not encoded or was stripped in export. Both look identical here and one of
them is a delivery defect. A true digital silence — a flat floor with not even
room tone — is itself suspicious even when silence was intended: a designed
silent film normally still carries a room, a wind, a hum.
OPERATOR ACTION: confirm the master has an audio track, re-export, re-run.
No score is issued and no table row is created.
```

---

## ⚠️ OPERATÖR NOTU — bu blok bir SONUÇTUR, boş koşu değildir

Kart E3 ② kapısı: `AUDIO STATE C → koşu YOK · skor yazılmaz · master'ın ses
kanalı kontrol edilip yeniden ihraç edilir.` Kapı uygulandı: T3'e satır
yazılmadı.

⛔ **Ama aynı dosyada koşan diğer dört mercek bu bloğu görmedi.** Üçü
`LINES HEARD: none` yazıp geçti, biri (① KARE) `Dialogue & Audio =
UNVERIFIABLE (no sound)` yazdı. Yani "bu dosya bozuk ihraç edilmiş olabilir"
şüphesini partide yalnız bu mercek dile getirdi ve bu merceğin çıktısı hiçbir
tabloya satır bırakmıyor — şüphe kayda geçmeden buharlaşıyor.
Film kaydındaki §ÖLÇÜM KAPISI bu yüzden `ffprobe` ile kapatılmalıdır.
