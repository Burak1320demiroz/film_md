# 🪞 THE SOLAR MIRROR — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası operatörde · master bu oturumda depoda yoktur.
> **Koşu:** 11.09.2026 · **on iki mercek** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR · 🎯 KADRAJ · 🎭 OYUNCULUK · 💡 IŞIK · 🪝 HOOK) — **on ikisi de mod V / SELF-CONSISTENCY.**
>
> ⛔ **KARE, SES VE HİKAYE SKOR SATIRLARI T1, T3 VE T4 TABLOLARINA GİRMEDİ.**
> ① SPEC kapısı: `THE_SOLAR_MIRROR_QA_SPEC.md` **VARDIR** (yatay_2_dk_filmler/THE_SOLAR_MIRROR/ içinde) ve mod D zorunlu merceklerin raporları `INPUT MODE: V` veya formatsız geldi / SCORES SUMMARY tablosu okunamadı → koşu TEKRARLANIR [D129].
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır [qa-isle §1]. Kare/ses/hikaye doğrulaması gereken her satır ⬜ AÇIK.
>
> ⭐ **GEÇERLİ/ŞARTLI SATIRLAR:**
> - ② DEVAMLILIK: **9.0 ⚠️ ŞARTLI** (mod V self-consistency okuması; D186 uyarınca kusursuz 7 kategori `—` yapıldı, ham: 9.6).
> - ⑤ ARKA PLAN: **4.4 ⚠️ ŞARTLI** (derin tarama, matrise girmez, T5 tablosuna eklendi; verdict: `SUBJECT DUPLICATE IN FIELD`).
> - ⑥ FİZİK: **6.8 ⚠️ ŞARTLI** (derin tarama, matrise girmez, T6 tablosuna eklendi; verdict: `MINOR SLIPS`).
> - ⑦ AKSİYON: **8.8 ⚠️ ŞARTLI** (risk tetikli, matrise girmez, T7 tablosuna eklendi; verdict: `ACTION READS`).
> - ⑧ EFOR: **2.9 ⚠️ ŞARTLI** (risk tetikli, matrise girmez, T8 tablosuna eklendi; verdict: `WEIGHTLESS WORK`).
> - ⑨ KADRAJ: **8.0 ⚠️ ŞARTLI** (plan sadakati, Mod V olduğu için T9 tablosuna ve /4 matrisine girmeyen mod V karantinası [D184/D190]; verdict: `MINOR DRIFT`).
> - ⑩ OYUNCULUK: **5.0 ⚠️ ŞARTLI** (plan sadakati, Mod V olduğu için T10 tablosuna ve /4 matrisine girmeyen mod V karantinası [D184/D190]; verdict: `TASK WITHOUT FEELING`).
> - ⑪ IŞIK: **4.0 ✅ GO** (plan sadakati, Mod V olduğu için T11 tablosuna ve /4 matrisine girmeyen mod V karantinası [D184/D190]; verdict: `LIT FROM NOWHERE`).
> - ⑫ HOOK: **5.6 ⚠️ ŞARTLI** (plan sadakati, Mod V olduğu için T12 tablosuna ve /4 matrisine girmeyen mod V karantinası [D184/D190]; verdict: `LEAVES AT 01:04`).

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · ~125 s / 124 s (raporlardan; ÖLÇÜLMEDİ) · 16:9 YATAY
          + 01:59-02:04 BAŞLIK KARTI ("THE SOLAR MIRROR")
MERCEK:   ① KARE (🚨 GEÇERSİZ · D129) · ② DEVAMLILIK 9,0 ⚠️ ŞARTLI
          · ③ SES (🚨 GEÇERSİZ · format okunamadı) · ④ HİKAYE (🚨 GEÇERSİZ · format okunamadı / D129)
          · ⑤ ARKA PLAN (4.4 ⚠️ ŞARTLI · T5) · ⑥ FİZİK (6.8 ⚠️ ŞARTLI · T6)
          · ⑦ AKSİYON (8.8 ⚠️ ŞARTLI · T7) · ⑧ EFOR (2.9 ⚠️ ŞARTLI · T8)
          · ⑨ KADRAJ (8.0 ⚠️) · ⑩ OYUNCULUK (5.0 ⚠️) · ⑪ IŞIK (4.0 ✅) · ⑫ HOOK (5.6 ⚠️) (⑨-⑫ mod V karantina D190)
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 11.09.2026 · çıkış kodu **2**

```
SPEC: yatay_2_dk_filmler/THE_SOLAR_MIRROR/THE_SOLAR_MIRROR_QA_SPEC.md → MOD D ZORUNLU

🚨 GEÇERSİZ  ·  ① KARE        THE_SOLAR_MIRROR_KARE_HAM.md (SCORES SUMMARY okunamadı / D129)
⚠️  ŞARTLI   ·  ② DEVAMLILIK  THE_SOLAR_MIRROR_DEVAMLILIK_HAM.md (n=5 Σ=45 ort=9.0, 7 hücre D186 ile `—`)
🚨 GEÇERSİZ  ·  ③ SES         THE_SOLAR_MIRROR_SES_HAM.md (SCORES SUMMARY okunamadı)
🚨 GEÇERSİZ  ·  ④ HİKAYE      THE_SOLAR_MIRROR_HIKAYE_HAM.md (SCORES SUMMARY okunamadı / D129)
⚠️  ŞARTLI   ·  ⑤ ARKA PLAN   THE_SOLAR_MIRROR_ARKA_PLAN_HAM.md (n=8 Σ=35 ort=4.4, verdict: SUBJECT DUPLICATE IN FIELD)
⚠️  ŞARTLI   ·  ⑥ FİZİK       THE_SOLAR_MIRROR_FIZIK_HAM.md (n=5 Σ=34 ort=6.8, verdict: MINOR SLIPS)
⚠️  ŞARTLI   ·  ⑦ AKSİYON     THE_SOLAR_MIRROR_AKSIYON_HAM.md (n=5 Σ=44 ort=8.8, 4 hücre D131 ile `—`, verdict: ACTION READS)
⚠️  ŞARTLI   ·  ⑧ EFOR        THE_SOLAR_MIRROR_EFOR_HAM.md (n=8 Σ=23 ort=2.9, verdict: WEIGHTLESS WORK)
⚠️  ŞARTLI   ·  ⑨ KADRAJ      THE_SOLAR_MIRROR_KADRAJ_HAM.md (n=4 Σ=32 ort=8.0, mod V karantina [D190], verdict: MINOR DRIFT)
⚠️  ŞARTLI   ·  ⑩ OYUNCULUK   THE_SOLAR_MIRROR_OYUNCULUK_HAM.md (n=6 Σ=30 ort=5.0, 3 hücre D131 ile `—`, verdict: TASK WITHOUT FEELING)
✅  GO        ·  ⑪ IŞIK        THE_SOLAR_MIRROR_ISIK_HAM.md (n=7 Σ=28 ort=4.0, verdict: LIT FROM NOWHERE)
⚠️  ŞARTLI   ·  ⑫ HOOK        THE_SOLAR_MIRROR_HOOK_HAM.md (n=7 Σ=39 ort=5.6, 1 hücre D186 ile `—`, verdict: LEAVES AT 01:04)

TOPLAM 12 rapor · 🚨 3 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 8 ŞARTLI · ✅ 1 GO
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

- Özne: Female astronaut, dark grey EVA suit, orbital hexagonal solar mirror array, shuttle.
- Eşleşen Film: `yatay_2_dk_filmler/THE_SOLAR_MIRROR`



