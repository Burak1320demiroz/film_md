# ❄️ THE SHATTERED BREATH — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası operatörde · master bu oturumda depoda yoktur.
> **Koşu:** 14.09.2026 · **on iki mercek** (①-⑫ hepsi) — **hepsi mod V / SELF-CONSISTENCY.**
>
> ⛔ **①·②·③·④·⑥·⑦·⑧·⑨·⑩·⑪·⑫ SKOR SATIRLARI T TABLOLARINA GİRMEDİ.**
> ① SPEC kapısı: `THE_SHATTERED_BREATH_QA_SPEC.md` **VARDIR** (`yatay_2_dk_filmler/THE_SHATTERED_BREATH/` içinde) ve mod D zorunlu merceklerin raporları `INPUT MODE: V` veya formatsız geldi / SCORES SUMMARY tablosu okunamadı → koşu TEKRARLANIR [D129].
> ② Aritmetik kapısı: ② DEVAMLILIK raporunda iddia edilen Σ=71 ile tablo toplamı Σ=75 uyuşmuyor → ARİTMETİK FABRİKE [D161].
> ⑨-⑫ Karantina kapısı: ⑨-⑫ plan sadakati mercekleri SPEC'siz mod V koşulduğundan karantinadadır [D190 · D184].
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır [qa-isle §1]. Kare/ses/hikaye doğrulaması gereken her satır ⬜ AÇIK.
>
> ⭐ **GEÇERLİ/ŞARTLI SATIRLAR:**
> - ⑤ ARKA PLAN: **8.3 ⚠️ ŞARTLI** (mod V self-consistency okuması; T5 tablosuna eklendi, verdict: FIELD DRIFTS BUT RECOVERABLE).

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · ~124 s / 125 s (raporlardan; ÖLÇÜLMEDİ) · 16:9 YATAY
          + 01:59-02:04 BAŞLIK KARTI ("THE SHATTERED BREATH")
MERCEK:   ① KARE (🚨 GEÇERSİZ · SCORES SUMMARY okunamadı / D129)
          · ② DEVAMLILIK (🚨 GEÇERSİZ · ARİTMETİK FABRİKE D161)
          · ③ SES (🚨 GEÇERSİZ · SCORES SUMMARY okunamadı)
          · ④ HİKAYE (🚨 GEÇERSİZ · SCORES SUMMARY okunamadı / D129)
          · ⑤ ARKA PLAN (8.3 ⚠️ ŞARTLI · T5)
          · ⑥ FİZİK (⛔ TEKRAR · D129)
          · ⑦ AKSİYON (⛔ TEKRAR · D129)
          · ⑧ EFOR (⛔ TEKRAR · D129)
          · ⑨ KADRAJ (🚨 GEÇERSİZ · D190 karantina)
          · ⑩ OYUNCULUK (🚨 GEÇERSİZ · D190 karantina / D205 sapan süre 41 s)
          · ⑪ IŞIK (🚨 GEÇERSİZ · D190 karantina)
          · ⑫ HOOK (🚨 GEÇERSİZ · D190 karantina)
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 14.09.2026 · çıkış kodu **2**

```
SPEC: yatay_2_dk_filmler/THE_SHATTERED_BREATH/THE_SHATTERED_BREATH_QA_SPEC.md → MOD D ZORUNLU

⚠️  ŞARTLI   ·  ⑤ ARKA PLAN   THE_SHATTERED_BREATH_ARKA_PLAN_HAM.md (n=6 Σ=50 ort=8.3, verdict: FIELD DRIFTS BUT RECOVERABLE)
⛔  TEKRAR   ·  ⑦ AKSİYON     THE_SHATTERED_BREATH_AKSIYON_HAM.md (SPEC var, mod V → D129)
⛔  TEKRAR   ·  ⑧ EFOR        THE_SHATTERED_BREATH_EFOR_HAM.md (SPEC var, mod V → D129)
⛔  TEKRAR   ·  ⑥ FİZİK       THE_SHATTERED_BREATH_FIZIK_HAM.md (SPEC var, mod V → D129)
🚨  GEÇERSİZ  ·  ② DEVAMLILIK  THE_SHATTERED_BREATH_DEVAMLILIK_HAM.md (ARİTMETİK FABRİKE Σ=71 ≠ 75 [D161])
🚨  GEÇERSİZ  ·  ⑨ KADRAJ      THE_SHATTERED_BREATH_KADRAJ_HAM.md (mod V karantina D190 / D184)
🚨  GEÇERSİZ  ·  ⑩ OYUNCULUK  THE_SHATTERED_BREATH_OYUNCULUK_HAM.md (mod V karantina D190 / D205)
🚨  GEÇERSİZ  ·  ⑪ IŞIK        THE_SHATTERED_BREATH_ISIK_HAM.md (mod V karantina D190 / D184)
🚨  GEÇERSİZ  ·  ⑫ HOOK        THE_SHATTERED_BREATH_HOOK_HAM.md (mod V karantina D190 / D184)
🚨  GEÇERSİZ  ·  ④ HİKAYE      THE_SHATTERED_BREATH_HIKAYE_HAM.md (SCORES SUMMARY okunamadı / D129)
🚨  GEÇERSİZ  ·  ① KARE        THE_SHATTERED_BREATH_KARE_HAM.md (SCORES SUMMARY okunamadı / D129)
🚨  GEÇERSİZ  ·  ③ SES         THE_SHATTERED_BREATH_SES_HAM.md (SCORES SUMMARY okunamadı)

TOPLAM 12 rapor · 🚨 8 GEÇERSİZ · ⛔ 3 TEKRAR · ⚠️ 1 ŞARTLI · ✅ 0 GO
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

- Özne: Male survivor astronaut, 88 Kelvin cryogenic methane-ethane ice moon surface with subterranean glowing amber geothermal energy lines.
- Eşleşen Film: `yatay_2_dk_filmler/THE_SHATTERED_BREATH`
