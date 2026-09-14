# 🎶 THE_DEEP_PRESSURE — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u ⬜ olarak okumalı."

TEMPO:        ⬜ BPM — sahne uzunluğuna HİZALI (§14: 10 s sahne →
              48/72/96/120/144 BPM; her sahne sınırı bir ölçü çizgisine düşer)
SÜRE:         ⬜ s = filmin RUNTIME'ı (hook + (sahne−1) × klip)
MÜZİKSİZ SAHNE: S⬜ — ⛔ her filmde EN AZ BİR tane (§10)
SUB-BASS:     ⬜ Hz + 90-160 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              sub-bass'ı hiç çalmaz, eşlikçi olmadan o katman yok demektir)
VURUŞ NOKTASI: ⬜ — kaç tane ve hangi saniyede (az olan güçlüdür)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: ⬜
GENRE: ⬜
TEMPO: ⬜ BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. ⬜
  2. ⬜

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  ⬜-⬜ s (S0): ⬜
  ⬜-⬜ s (S1): ⬜

SYNC RULE: ⬜

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     ⬜ (bu seri diegetik yapay ses kullanır: suit AI · telsiz · kayıt)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU: ⬜ | sahne | katmanlar (ad) | sayı | köprü | — ③ SES LAYER COUNT bunu ölçer
REPLİK SAYISI: ⬜
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Elle yazılan her kayıt er geç ızgara formülüyle çelişir ve ⑨ HİZALAMA
   KAPISI'nın ölçü aletini bozar.
```
