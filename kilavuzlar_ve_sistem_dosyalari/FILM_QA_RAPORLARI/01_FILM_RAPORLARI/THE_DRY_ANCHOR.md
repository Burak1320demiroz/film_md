# ⚓ THE DRY ANCHOR — FİLM KAYDI

> **Durum:** film ÜRETİLDİ ve kurgulandı (operatör beyanı) · teslim dosyası operatörde · master bu oturumda depoda yoktur.
> **Koşu:** 11.09.2026 · **ON İKİ MERCEK** (🔧 KARE · 🔗 DEVAMLILIK · 🔊 SES · 📖 HİKAYE · 🖼️ ARKA PLAN · ⚖️ FİZİK · 🎯 AKSİYON · 💪 EFOR · 🎯 KADRAJ · 🎭 OYUNCULUK · 💡 IŞIK · 🪝 HOOK) — **on ikisi de mod V / SELF-CONSISTENCY.**
>
> 🚨 **PARTİ GEÇERSİZ: HİÇBİR SKOR SATIRI TABLOLARA GİRMEDİ [D129 · D162 · D184 · D188 · D190].**
>
> 1. **⑨-⑫ PLAN SADAKATİ MERCEKLERİ MOD V KARANTİNASI [D190 · D184]:** ⑨ KADRAJ, ⑩ OYUNCULUK, ⑪ IŞIK, ⑫ HOOK mercekleri belgesiz (Mode V) koşulduğunda ekrandan plan uydurur. T9-T12 tablolarına satır GİRMEZ, `00_INDEX` hücresi ❌ KALIR.
> 2. **①.9 TESLİM ŞÜPHESİ KAPISI [D188]:** Plan 14 sahne yazıyor (`THE_DRY_ANCHOR_BOLUM_1.md` S1-S6 + `BOLUM_2.md` S7-S14), raporlar 13/12/11 sahne bildirdi (kesme yayılımı > 1 `[D107]`). Eksik sahne teslim edilmeden kesme listesi / REMOVE reçetesi uygulanamaz.
> 3. **① SPEC KAPISI [D129]:** `THE_DRY_ANCHOR_QA_SPEC.md` depoda hazırdır. SPEC varken merceklerin Mode V koşulması nedeniyle tüm koşular TEKRARLANIR.
> 4. **⑤/⑫ SUSKUNLUK KAPISI [D162]:** ⑤ ARKA PLAN ve ⑫ HOOK mercekleri sağ alt köşede filigran/üçgen logo bildirdi, ancak ① KARE merceği bu konuda sustu.
>
> ⛔ **⑪ ÖLÇÜM KAPISI KOŞULAMADI** — master elde değil. Bu kaydın SÜRE ve SAHNE SAYISI satırları RAPOR KAYNAKLIDIR ve hiçbir kapıya sokulmamıştır [qa-isle §1]. Kare/ses doğrulaması gereken her satır ⬜ AÇIK.

---

## 📦 MALZEME

```
MALZEME:  teslim kurgusu · ~145 s (raporlardan; ÖLÇÜLMEDİ) · 16:9 YATAY
          + 02:20-02:25 BAŞLIK KARTI ("THIS DUST HAS NO BOTTOM")
MERCEK:   ① KARE (🚨 GEÇERSİZ) · ② DEVAMLILIK (🚨 GEÇERSİZ)
          · ③ SES (🚨 GEÇERSİZ) · ④ HİKAYE (🚨 GEÇERSİZ)
          · ⑤ ARKA PLAN (🚨 GEÇERSİZ) · ⑥ FİZİK (🚨 GEÇERSİZ)
          · ⑦ AKSİYON (🚨 GEÇERSİZ) · ⑧ EFOR (🚨 GEÇERSİZ)
          · ⑨ KADRAJ (🚨 GEÇERSİZ · D190) · ⑩ OYUNCULUK (🚨 GEÇERSİZ · D190)
          · ⑪ IŞIK (🚨 GEÇERSİZ · D190) · ⑫ HOOK (🚨 GEÇERSİZ · D190)
```

---

## §①.5 BETİK KOŞUSU — `rapor_kontrol.py` · 11.09.2026 · çıkış kodu **2**

```
SPEC: yatay_2_dk_filmler/THE_DRY_ANCHOR/THE_DRY_ANCHOR_QA_SPEC.md → MOD D ZORUNLU

①.10 GÖZ KAPILARI [D191] — SPEC'te 12 madde · hiçbir merceğin kapsamında DEĞİL,
      her biri TEK KAREYLE kapanır; kapanmadan parti kapanmaz:
      ⬜ ① SIRT — hiçbir karede sırt ünitesi yok (sırt kadrajda: 22,0 · 82,0 · 134,0 s)
      ⬜ ② VİZÖR — düz dikdörtgen pencere + görünür metal çerçeve; kubbe/kavisli pencere YOK
      ⬜ ③ BACAK SAYIMI — dört bacak; üçünde pabuç yüzeyde, dördüncüde (kadrajın sağında) rim hizasına kadar gömülü
      ⬜ ④ TOZ — 1 NUMARALI RİSK, SAYIYLA ÖLÇÜLÜR [A5 · D192]: 7,0 s'de halka genişliği ≤2 gövde genişliği (3,8 m) · yükseklik ≤ pabuç üst yüzü · 20,0 s'de kadrajda asılı zerre 0 · 38,0 s'de yere oturan toz katmanı ≤1 parmak (2 cm)
      ⬜ ⑤ KAZIK BAŞI — 38,0 s'de yerin üstünde vurulacak hiçbir şey kalmamış; baş toz sıfırının 1 parmak ALTI
      ⬜ ⑥ SAYAÇ ÇİZGİSİ — bacak gövdesinde toz yakası: 64,0 s'de BİR çizgi · 84,0 s'de İKİNCİ çizgi · 114,0 s'de İKİ ÇİZGİ BİRLEŞMİŞ
      ⬜ ⑦ KELEPÇE — 4,0 s iki dolu · 34,0 s üst yuva boş · 134,0 s iki boş
      ⬜ ⑧ METİN — hiçbir yüzeyde harf, rakam, işaret yok: giysi · gövde · zemin · aletler PÜRÜZSÜZ METİNSİZ
      ⬜ ⑨ HAT — 124,0 ve 134,0 s'de kadrajı çaprazlayan TEK gergin hat; ikinci hat veya sarkan gevşek hat YOK
      ⬜ ⑩ KASA — 134,0 s'de kasa YERDE ve kızak BOŞ (kasa kızakta DEĞİL)
      ⬜ ⑪ SESSİZLİK — 118,0-120,0 s dalga formunda mutlak sıfır (müzik · efekt · dip ses SIFIR; J-cut sessizlikten SONRA girer)
      ⬜ ⑫ GÖLGE YÖNÜ — 14/14 karede gölgeler SOLDAN SAĞA ve gölgelerin İÇİ DOLU (çift gölge · yumuşama sıçraması YOK)

🚨 GEÇERSİZ  ·  ① KARE        THE_DRY_ANCHOR_KARE_HAM.md
🚨 GEÇERSİZ  ·  ② DEVAMLILIK  THE_DRY_ANCHOR_DEVAMLILIK_HAM.md
🚨 GEÇERSİZ  ·  ③ SES         THE_DRY_ANCHOR_SES_HAM.md
🚨 GEÇERSİZ  ·  ④ HİKAYE      THE_DRY_ANCHOR_HIKAYE_HAM.md
🚨 GEÇERSİZ  ·  ⑤ ARKA PLAN   THE_DRY_ANCHOR_ARKA_PLAN_HAM.md
🚨 GEÇERSİZ  ·  ⑥ FİZİK       THE_DRY_ANCHOR_FIZIK_HAM.md
🚨 GEÇERSİZ  ·  ⑦ AKSİYON     THE_DRY_ANCHOR_AKSIYON_HAM.md
🚨 GEÇERSİZ  ·  ⑧ EFOR        THE_DRY_ANCHOR_EFOR_HAM.md
🚨 GEÇERSİZ  ·  ⑨ KADRAJ      THE_DRY_ANCHOR_KADRAJ_HAM.md (mod V karantinası [D190])
🚨 GEÇERSİZ  ·  ⑩ OYUNCULUK   THE_DRY_ANCHOR_OYUNCULUK_HAM.md (mod V karantinası [D190])
🚨 GEÇERSİZ  ·  ⑪ IŞIK        THE_DRY_ANCHOR_ISIK_HAM.md (mod V karantinası [D190])
🚨 GEÇERSİZ  ·  ⑫ HOOK        THE_DRY_ANCHOR_HOOK_HAM.md (mod V karantinası [D190])

TOPLAM 12 rapor · 🚨 12 GEÇERSİZ · ⛔ 0 TEKRAR · ⚠️ 0 ŞARTLI · ✅ 0 GO
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

- Özne: White EVA suit astronaut, desert planet surface, lander module & ground stakes.
- Eşleşen Film: `yatay_2_dk_filmler/THE_DRY_ANCHOR`
