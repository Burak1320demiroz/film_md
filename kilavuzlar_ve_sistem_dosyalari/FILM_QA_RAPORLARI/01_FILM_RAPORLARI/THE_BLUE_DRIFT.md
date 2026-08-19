# 🔵 THE BLUE DRIFT — FİLM KAYDI

> **Durum:** yazım tamam, üretim S1 denemesiyle başladı.
> **Ölçüm:** üç mercek (🔧 🧩 📖) HİÇ koşulmadı — bu kayıt yalnız FİLME
> ÖZEL ÜRETİM KAPISI koşusunu taşır. ⛔ Kapı skoru 03-07 tablolarına
> ve LESSONS teknik tablosuna GİRMEZ.

---

## 🚪 KOŞU 1 — S1 tek klip kapısı

```
MALZEME:  1 klip (~10 s), as-built prompt = S1 VIDEO V1
RUBRİK:   FILME_OZEL/THE_BLUE_DRIFT_QA_CRITIQUE_PROMPT.md
HAM:      02_HAM_RAPORLAR/THE_BLUE_DRIFT_S1_KAPI_HAM.md
MOD:      D (SPEC gömülü)
```

⛔ **KOŞU EKSİK BİÇİMLİDİR — GÖZLEM SETİ SAYILIR.** Rapor rubriğin çıktı
şablonunu kullanmadı: künye, gözlem defteri, zaman kodu, atıf etiketi,
skor tablosu ve karar yok. Sonuç: bulgular gerçek ve işlenir, **ama**
① hiçbir kategoriye SAYI yazılmaz, ② atıf operatör tarafında yapılmıştır
(aşağıdaki tablo modelin değil, as-built metniyle yapılan karşılaştırmanın
sonucudur), ③ **C2 (arka planın zaman içinde sabitliği) ÖLÇÜLMEDİ** —
kapının açılış sebebi olan "arka plan değişti" şikâyeti hâlâ AÇIK.

### Bulgu → atıf defteri

| # | Bulgu | Atıf | Kanıt (as-built metninde) | Eylem |
|---|---|---|---|---|
| 1 | Telsiz konuşması / insan sesi duyuluyor | 🅐 MODEL DRIFT (prompt tarafı ağırlaştırıcı) | Yasak yazılıydı ama yalnız `AUDIO:` paragrafında ("No voices, no music"); NEGATIVE'de ses maddesi YOKTU. Ayrıca "on the radio channel" ifadesi çekim yapıyordu | Yasak NEGATIVE'e taşındı (25 video promptu); "radio channel" → "closed comms channel — carrier hiss only" |
| 2 | Pilotun elinde istenmeyen tablet/pano, sonra kayboluyor | 🅑 **PROMPT GAP** | Promptta pilotun 0.0–6.0 s arası eli HİÇ tarif edilmemişti; boşluğu model doldurdu | TIMELINE'a t=0 el durumu yazıldı ("both gloves empty and open at his sides — he carries nothing at any point") + `No unnamed prop…` negatifi 25 promptta |
| 3 | Numune kutusu yerde kendiliğinden beliriyor | 🅑 **PROMPT GAP** | Kutunun 6.0 s'den önceki yeri tanımsızdı | t=0 durumu yazıldı: kutu zaten pilotun ayağının dibinde, kapağı kapalı; 3.5 s'de kapak KOLDAN kaldırılıyor |
| 4 | Eller karota ve kutuya eriyor (merging) | 🅐 MODEL DRIFT | Kilit promptta VARDI: "Hand contacts keep clear structural boundaries — no merging" | Kural değil TASARIM değişti [AGENTS §8]: karota **işlenmiş uç kapak** eklendi, eldiven artık buza değil metale tutunuyor; negatif buna göre yeniden yazıldı |
| 5 | Vizör camı YOK gibi görünüyor (yüz açıkta okunuyor) | 🅑 **PROMPT GAP** | Promptta yalnız "optically clear … zero reflection" vardı — bu modele "cam çizme" demektir. D95'in üç görünürlük işareti (çerçeve + yaka mührü + tek parlama çizgisi) yalnız REFERANS PAKETİNDE yazılıydı, sahne promptlarında YOKTU | VİZÖR KİLİDİ 10 prompta gövdeye, 29 prompta negatife işlendi |
| ✅ | Kamera/kadraj · 2 insan · suit + turkuaz/amber · planetshine + bantlı dev · landerin yeri | 🅒 NOT A FINDING | — | korunur |

### Kapının kazandırdığı

```
🅑 PROMPT GAP sayısı: 3 / 5 bulgu.
Yani bu klip aynı promptla yeniden üretilseydi bulguların ÜÇÜ aynen
tekrarlardı — para iki kez yanardı. Kapının varlık sebebi tam olarak bu.
```

### ⬜ AÇIK MADDELER

```
⬜ C2 arka plan sabitliği ölçülmedi (rapor şablonu kullanılmadı) —
   operatörün "arka plan değişti" şikâyeti raporda DOĞRULANMADI:
   rapor tersine "environment flawless" dedi. İki olasılık ayrışmadı:
   ① kayma kare-içi (ilk kare ↔ son kare) idi ve rapor bakmadı,
   ② şikâyet IMAGE ile VIDEO arasındaki farktı.
   → Kapatma yolu: yeni koşuda şablon zorunlu; ledger'ın
     "first-frame vs last-frame" satırı doldurulmadan koşu kapanmaz.
⬜ Ses bulgusu 🅐 mı 🅑 mi tam ayrışmadı: yasak vardı ama yanlış blokta.
   Yeni koşu bunu ayırır (yasak artık NEGATIVE'de).
```
