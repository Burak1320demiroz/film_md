# ☀️ THE SILENT PERIHELION — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası operatörde · master bu oturumda depoda yoktur.
> **Koşu:** 13.09.2026 · **on iki mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR · 🎯 KADRAJ · 🎭 OYUNCULUK · 💡 IŞIK · 🪝 HOOK) — **on ikisi de mod V / SELF-CONSISTENCY.**
>
> ⛔ **KARE, SES VE HİKAYE SKOR SATIRLARI T1, T3 VE T4 TABLOLARINA GİRMEDİ.**
> ① SPEC kapısı: `THE_SILENT_PERIHELION_QA_SPEC.md` **VARDIR** (yatay_2_dk_filmler/THE_SILENT_PERIHELION/ içinde) ve mod D zorunlu merceklerin raporları `INPUT MODE: V` veya formatsız geldi / SCORES SUMMARY tablosu okunamadı → koşu TEKRARLANIR [D129].
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır [qa-isle §1].
> 🚨 **D107 KESME YAYILIMI KAPI UYARISI:** Merceklerin kesme sayımları (9–11 kesme) ayrıştığı için 12'li parti toplu denetimde `D107` bayrağı almıştır. Master ölçüldüğünde `--olcum-kesme` ile netleştirilecektir.
>
> ⭐ **TEKİL MERCEK DURUMLARI:**
> - ② DEVAMLILIK: **8.8 ⚠️ ŞARTLI** (mod V self-consistency okuması; T2 tablosuna yazıldı, verdict: FIXABLE IN EDIT).
> - ⑤ ARKA PLAN: **7.8 ✅ GO** (derin tarama, matrise girmez, T5 tablosuna yazıldı; verdict: FIELD DRIFTS BUT RECOVERABLE).
> - ⑥ FİZİK: **6.0 ⛔ TEKRAR** (derin tarama, SPEC hazır olduğu hâlde Mod V koşuldu [D129]).
> - ⑦ AKSİYON: **8.7 ⛔ TEKRAR** (risk tetikli, SPEC hazır olduğu hâlde Mod V koşuldu [D129]; verdict: ACTION READS).
> - ⑧ EFOR: **5.9 ⛔ TEKRAR** (risk tetikli, SPEC hazır olduğu hâlde Mod V koşuldu [D129]; verdict: MINOR DEBT).
> - ⑨ KADRAJ: **8.5 🚨 GEÇERSİZ / KARANTİNA** (plan sadakati merceği Mod V koşulduğu için karantinada [D184/D190]; verdict: RHYME BROKEN).
> - ⑩ OYUNCULUK: **6.7 🚨 GEÇERSİZ / KARANTİNA** (plan sadakati merceği Mod V koşulduğu için karantinada [D184/D190]; verdict: MOSTLY LEGIBLE).
> - ⑪ IŞIK: **5.6 🚨 GEÇERSİZ / KARANTİNA** (plan sadakati merceği Mod V koşulduğu için karantinada [D184/D190]; verdict: KEY WALKS).
> - ⑫ HOOK: **6.0 🚨 GEÇERSİZ / KARANTİNA** (plan sadakati merceği Mod V koşulduğu için karantinada [D184/D190]; verdict: LEAVES AT 00:25 s).

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · ~124 s / 125 s (raporlardan; ÖLÇÜLMEDİ) · 16:9 YATAY
          + 02:00-02:05 BAŞLIK KARTI ("THE SILENT PERIHELION")
MERCEK:   ① KARE (🚨 GEÇERSİZ · SCORES SUMMARY okunamadı / D129)
          · ② DEVAMLILIK (8.8 ⚠️ ŞARTLI · T2)
          · ③ SES (🚨 GEÇERSİZ · SCORES SUMMARY okunamadı)
          · ④ HİKAYE (7.4 🚨 GEÇERSİZ · SCORES SUMMARY okunamadı / D129)
          · ⑤ ARKA PLAN (7.8 ✅ GO · T5)
          · ⑥ FİZİK (6.0 ⛔ TEKRAR · Mod V [D129])
          · ⑦ AKSİYON (8.7 ⛔ TEKRAR · Mod V [D129])
          · ⑧ EFOR (5.9 ⛔ TEKRAR · Mod V [D129])
          · ⑨ KADRAJ (8.5 🚨 GEÇERSİZ / KARANTİNA · Mod V [D190])
          · ⑩ OYUNCULUK (6.7 🚨 GEÇERSİZ / KARANTİNA · Mod V [D190])
          · ⑪ IŞIK (5.6 🚨 GEÇERSİZ / KARANTİNA · Mod V [D190])
          · ⑫ HOOK (6.0 🚨 GEÇERSİZ / KARANTİNA · Mod V [D190])
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 13.09.2026 · çıkış kodu **2**

```
SPEC: yatay_2_dk_filmler/THE_SILENT_PERIHELION/THE_SILENT_PERIHELION_QA_SPEC.md → MOD D ZORUNLU

⚠️  ŞARTLI   ·  ② DEVAMLILIK  THE_SILENT_PERIHELION_DEVAMLILIK_HAM.md (n=12 Σ=105 ort=8.8, verdict: FIXABLE IN EDIT)
✅  GO        ·  ⑤ ARKA PLAN   THE_SILENT_PERIHELION_ARKA_PLAN_HAM.md (n=6 Σ=47 ort=7.8, verdict: FIELD DRIFTS BUT RECOVERABLE)
⛔  TEKRAR    ·  ⑥ FİZİK       THE_SILENT_PERIHELION_FIZIK_HAM.md (n=5 Σ=30 ort=6.0, Mod V / D129)
⛔  TEKRAR    ·  ⑦ AKSİYON     THE_SILENT_PERIHELION_AKSIYON_HAM.md (n=9 Σ=78 ort=8.7, Mod V / D129)
⛔  TEKRAR    ·  ⑧ EFOR        THE_SILENT_PERIHELION_EFOR_HAM.md (n=8 Σ=47 ort=5.9, Mod V / D129)
🚨  GEÇERSİZ  ·  ⑨ KADRAJ      THE_SILENT_PERIHELION_KADRAJ_HAM.md (n=5 Σ=41 ort=8.2, Mod V karantina [D190])
🚨  GEÇERSİZ  ·  ⑩ OYUNCULUK   THE_SILENT_PERIHELION_OYUNCULUK_HAM.md (n=9 Σ=60 ort=6.7, Mod V karantina [D190])
🚨  GEÇERSİZ  ·  ⑪ IŞIK        THE_SILENT_PERIHELION_ISIK_HAM.md (n=7 Σ=39 ort=5.6, Mod V karantina [D190])
🚨  GEÇERSİZ  ·  ⑫ HOOK        THE_SILENT_PERIHELION_HOOK_HAM.md (n=8 Σ=48 ort=6.0, Mod V karantina [D190])
🚨  GEÇERSİZ  ·  ④ HİKAYE      THE_SILENT_PERIHELION_HIKAYE_HAM.md (n=10 Σ=74 ort=7.4, SCORES SUMMARY okunamadı / D129)
🚨  GEÇERSİZ  ·  ① KARE        THE_SILENT_PERIHELION_KARE_HAM.md (SCORES SUMMARY okunamadı / D129)
🚨  GEÇERSİZ  ·  ③ SES         THE_SILENT_PERIHELION_SES_HAM.md (SCORES SUMMARY okunamadı)

TOPLAM 12 rapor · 🚨 7 GEÇERSİZ · ⛔ 3 TEKRAR · ⚠️ 1 ŞARTLI · ✅ 1 GO (toplu denetimde D107 kesme yayılımı uyarısı)
```

---

## §⑪ ÖLÇÜM KAPISI — **KOŞULAMADI**

```
master:      depoda YOK · operatör komut satırında master yolu vermedi
ffmpeg:      VAR — dosya bekleniyor
sonuç:       ölçüm yapılamadı → raporların SÜRE ve SAHNE SAYISI değerleri kapılara GİRDİ SAYILMAZ [D125]
```

Master video geldiğinde çalıştırılacak komut:
```bash
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master_yolu>"
```

---

## §③ KİMLİK KAPISI — **ATTRIBUTED ✅**

- Özne: Male astronaut Cale, dark gray flight suit with orange padded accents, helmet visor, spacecraft cockpit near stellar flare anomaly and geometric megastructure.
- Eşleşen Film: `yatay_2_dk_filmler/THE_SILENT_PERIHELION`
