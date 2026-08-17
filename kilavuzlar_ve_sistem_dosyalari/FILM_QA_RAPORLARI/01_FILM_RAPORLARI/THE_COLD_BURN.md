# ❄️ THE COLD BURN — FİLM QA KAYDI

> **Film dosyası:** `../../../yatay_3_5_dk_filmler/THE_COLD_BURN/`
> **Plan:** 30 sahne · 299 s · 12+ replik (tümü kask telsizi / gövdesiz EKO)
> **Ölçülen kurgu:** 225 s · 12 sahne · 7 replik (tümü ekranda insan)
> **QA tarihi:** 09.08.2026 · beş mercek, beşi de MOD V, beşi de AYNI dosya (D75 ✅)
> ⭐ **BEŞ raporlu İLK film — ve SES_QA rubriğinin İLK koşusu.**

---

## 📊 BEŞ MERCEĞİN DURUMU

| Mercek | Skor | Verdict | Geçerlilik |
|---|:--:|---|---|
| 🔧 VIDEO_QA | **5/10 Ⓥ** | REGENERATE (3 🔴) | ✅ mod V geçerli — SPEC yine yapıştırılmadı (operatör kuralı ② ×2) |
| 🧩 MANTIK_QA | **7/10** | FIXABLE IN EDIT | ✅ geçerli — serinin en yüksek 2. mantık skoru |
| 📖 SENARYO_QA | **4/10 Ⓥ** | REVISE STRUCTURE | ⚠️ ŞARTLI — skorun büyük kısmı KURGUNUN puanı (aşağıda) |
| 🧍 KARAKTER_QA | **6/10** | DRIFTS BUT RECOVERABLE | ✅ geçerli — KLONSUZ (D69/77 tekrarlamadı) |
| 🔊 SES_QA | **5/10** | AUDIBLE DRIFT, FIXABLE IN THE MIX | ✅ geçerli — rubriğin ilk koşusu, kapılar çalıştı |

Ham raporlar: `../02_HAM_RAPORLAR/THE_COLD_BURN_{TEKNIK,SENARYO,MANTIK,KARAKTER,SES}_HAM.md`

---

## 🚨 ANA BULGU — PLANIN YARISI EKRANDA YOK (kurgu kapısı 4/4 ihlal)

Kurgu kapısının [D72] dört maddesi de tutmuyor — **dördünün birden
delindiği ilk koşu:**

```
klip sayısı = plan        ❌  12 ≠ 30
süre ±2 s                 ❌  225 s ≠ 299 s (−74 s)
ekran metni 0.0 sn        ❌  3:40 yanık başlık kartı
CENTRAL CHOICE kurguda    ❌  S19 (iptal/wave-off) ekranda YOK
```

### Plan ↔ kurgu eşlemesi (film kaydının sahne numaraları raporlardan)

```
EKRANDA VAR (≈12/30):  S0 · S1 · S3 · S4 · S5+S6 · S7(kısmi) · S10/S18 ·
                       S12+S15 · S21(iptalsiz tek deneme) · S24 · S25
EKRANDA YOK (kritik):  S13 savrulma · S14 karar · S16 hesap ·
                       S17 DÖNÜŞÜ EŞLE (VİRAL #3) · S19 İPTAL (CENTRAL
                       CHOICE) · S20 ikinci deneme · S22 mandallar ·
                       S23 tutundu · S26 TAHLİYE (DORUK + VİRAL #4) ·
                       S27 tamir · S28 ilk yüzler · S29 planlı final
PLANDA OLMAYAN:        hyperspace sıçraması (S11') · başlık kartı (S12')
```

**Sonuç:** dört viral aranın ikisi (S17 · S27), bedelli seçim (S19),
doruk (S26) ve açılış-kapanış çiftinin ikinci yarısı (S29) üretimde/kurguda
yok. Filmin İKİ TIRMANIŞLI yapısının ikinci tırmanışı neredeyse tamamen
kayıp — senaryo merceğinin "two disjointed shorts" okuması tam olarak bunun
artefaktı. Ayrıca üretim planındaki dört kapı sahnesinin (S12→S21→S22→S25)
hiçbirinin kapı kaydı yok → **kayıtsız kapı, koşulmamış kapıdır [D74 ×3].**

---

## ⭐ FLAGS FOR DOCUMENT CHECK — CEVAPLAR (beş merceğin soruları)

### 📖 SENARYO

**S1. "Tek hikaye mi, iki ayrı senaryo mu?"**
TEK hikaye — 30 sahnelik tek plan (buzdan kaç → yanan gemiye yanaş →
yangını tahliyeyle öldür). "İkiye bölünmüş" okuması, ikinci tırmanışın
(S16-S28) ~%80'inin ekranda olmamasından. Bulgu senaryoya değil kurguya
yazılır [D72/D81 örüntüsü].

**S2. "Duygusal zirve istasyon patlaması mı (2:00)?"**
HAYIR. Patlama planın ORTA NOKTASIDIR (S12, vuruş haritasında %43-50).
Planlı doruk **S26 TAHLİYE KOLU** (%87), planlı climax **S21 temas**.
S26 ekranda hiç yok → Duygusal Yay ve Yapı skorları filmin değil eksik
kurgunun puanı → satır ⚠️ ŞARTLI.

**S3. "Son planlı sahne hyperspace sıçraması mı?"**
HAYIR. Planlı final S29: füzyon tahriki + hilal gezegen + fırtınanın izi
(açılış-kapanış çifti). Hyperspace planda YOK — plan füzyon der, sıçrama
demez. Başlık kartı A4 denetiminde açıkça yasaklı ("JENERİK: yok. Kapak
çıktısı kurguya EKLENMEZ [D34/D70/D72]").

### 🧩 MANTIK

**M1. "Çevresel sayaç planlı mı?"**
EVET — iki fiziksel kanal planlı: mekanik DURUŞ KÜRESİ + **10 segmentlik
yakıt rezerv göstergesi** (S16'da 2 yanık = %4, S20'de 1 = %2; sönmüş
segmentin yuvası görünür — D78 ① kuralıyla tasarlandı). İkisi de ekranda
okunmadı; gösterge sahneleri (S16 · S20) zaten kurguda yok →
**D78'in 3. vakası** (Dawn Front · Starless Circle · Cold Burn).

**M2. "Mavi örnek/kutu planlı bir kurulum mu?"**
KISMEN. S1 KAROT yetkinlik-kuruluş vuruşu; S4'teki KUTU ise klon
azaltımı için **siluet ayrıştırıcı** (A4 kararı: "mühendis KUTU taşıyor").
Plan örneğe hiçbir dramatik değer YÜKLEMEZ ve geri dönmez — "We have the
sample" repliği planda yok, MacGuffin statüsü üretimin icadı. Kutunun
S4→S5 arasında istiflenmesi kesme içinde kalıyor (plana uygun).
→ "terk edilmiş kurulum" bulgusu YARI DÜŞER: kurulum planlı değildi,
onu kurulum gibi gösteren replik plansızdı.

### 🧍 KARAKTER

**K1. "Kutu istifleniyor mu?"** → M2'nin cevabı. Devamlılık ihlali değil,
plansız repliğin yarattığı beklenti.

**K2. "Kasksız final planlı mı?"**
HAYIR. HELMET STATE SCHEDULE: kask S1-S25 KAPALI, kasksızlık YALNIZ
S26-S28 basınçlı iç hacimde. Planlı finalde (S29) insan yok. Uzay
fonunda kasksız kadın = plansız kart sahnesinin ikinci ihlali.

**K3 (pasaporttan, sorulmadan):** iki pasaportta da **"backpack"** —
bible her iki suit için **SIRT DÜZ** diyor ve D79 cümlesi 32 promptun
negatifinde YAZILIYDI. → **D79'un 4. vakası** ve ilk kez "negatif
çekirdeğe girdi, yine döndü" durumu — muhtemel sebep: üretim bu
promptlarla yapılmadı (aşağıda, ÜRETİM SORUSU).
Renk kilidi ise TUTTU: turkuaz=kadın pilot ✅ · amber/turuncu=erkek
mühendis ✅ · kırçıllı sakal ✅.

### 🔧 VIDEO

**V1. "İç mekânda kask çıkarma planlı mı?"**
Kısmen — yalnız S26-S28 (tahliye SONRASI basınçlı hacim). Yangın
sırasında kask kapalı kalmalı; ekrandaki vizör-kapalı iç sahneler plana
uygun.

**V2. "Vakum sert gerçekçilik mi?"**
EVET — Gerçekçilik çıpası 3: "VAKUMDA PATLAMA SESSİZDİR VE ATEŞ TOPU
YOKTUR; 0.4 s flaş, düz hatlarda parçalar." Ekrandaki bas gümbürtülü,
alevli patlama planın ihlali → bulgu AYAKTA (🔴).

**V3. "Başlık kartı istendi mi?"**
HAYIR — A4: jenerik yok; başlık yalnız KAPAK görseline post-prodüksiyonda
eklenir. ⚠️ Operatör 3:40'taki kartın metnini doğrulasın: "THE COLD BURN"
ise Unbroken City / Starless Circle ile birebir aynı zincir (kapak
başlığı kurguya sızdı — D72 zincirinin 3. vakası).

### 🔊 SES

**A1. "Vakumda patlama sesi?"** → V2. Planın ihlali; bulgu VIDEO_QA
kapsamında sayılır (çift sayım yok).

**A2. "1:20-1:40 mutlak sessizlik tasarım mı?"**
HAYIR. Planda "üç sahne tamamen müziksiz" var ama MÜZİKSİZ ≠ SESSİZ:
kabin uğultusu ve yatak sürer. 20 saniyelik dijital sıfır = miks hatası
→ **DERS 83'ün kaynağı.**

**A3 (register haritasından, sorulmadan — koşunun en değerli bulgusu):**
Rapor: 7 replik, 7'si HUMAN, 6'sı ekranda hareket eden ağızdan; makine
sesi 0. Plan: 12+ replik, insan replikleri **kapalı kask telsizinden,
kokpit arkadan çekilir, ağız kadrajda değil**; EKO **gövdesiz sentetik
ses**. Yani planın ses mimarisi üretimde TERSİNE dönmüş: EKO silinmiş,
sayı replikleri ("doksan saniye", "pencere on iki saniye", "modülde
yangın") ekrandaki insanlara devredilmiş, lip-sync sigortası (arkadan
kadraj) çökmüş. → **DERS 82'nin kaynağı.** Comms filtresinin kask
durumu yerine sahne değişimini takip etmesi de aynı kökten.

---

## ❓ ÜRETİM SORUSU — cevabı yalnız proje sahibinde

Sapmanın ölçeği (18 sahne yok · replikler bambaşka · EKO yok · hyperspace
icadı · sırt ünitesi 32 negatife rağmen geri geldi) tek bir soruyu
zorunlu kılıyor: **bu kurgu PART_A/PART_B promptlarıyla mı üretildi?**

```
□ Evet, promptlarla üretildi → 18 sahne üretilip mi düştü, hiç mi
  üretilmedi? Kapı kayıtları (S12·S21·S22·S25) nerede? [D74]
□ Hayır, başka bir akışla (ör. otomatik akış/özet prompt) üretildi →
  beş raporun prompt-iyileştirme önerileri BU PROMPTLARA uygulanmaz;
  önce üretim zinciri plana bağlanır.
```

Cevap gelmeden "prompt kilidi tutmadı" türü çıkarımlar (D79 ×4 dahil)
KESİN sayılmaz — dosyaya işlendi, ders sayacına şerhle girdi.

---

## 📚 BU KOŞUDAN ÇIKAN DERSLER

| Ders | Durum |
|---|---|
| **DERS 82** 🆕 | SES MİMARİSİ ÜRETİMDE TERSİNE DÖNDÜ — kaynak: SES_QA register haritası |
| **DERS 83** 🆕 | ORTAM YATAĞI KLİP SINIRINDA ÖLÜYOR — teslim öncesi ses kapısı |
| D72 | ×4 — kurgu kapısının 4 maddesi birden ihlal (ilk kez) |
| D74 | ×3 — dört üretim kapısının kaydı yok |
| D78 | ×3 — yakıt göstergesi + duruş küresi ekranda hiç okunmadı |
| D79 | ×4 ⚠️ şerhli — sırt ünitesi; üretim zinciri doğrulanmadan kesinleşmez |
| D65 | TUTTU ×5 — beş rapor da `FILM: (not supplied)` |
| D69/D77 | TEKRARLAMADI ✅ — klonsuz koşu (ama en riskli sahne S25 ekranda yok) |
| D75 | TUTTU — beş mercek aynı 225 s dosyayı ölçtü |

---

## 📋 ONARIM LİSTESİ (00_INDEX yapılacaklara işlendi)

```
MİKS SEANSI (yeniden üretim GEREKTİRMEZ — SES_QA ayrımı):
□ 1:20-1:40 mutlak sessizliğe yatak serilir (kabin uğultusu)      [D83]
□ 0:50 1 s'lik delik kapatılır · müzik kuyrukları yumuşatılır      [D83]
□ 3:00 diyalog altındaki yangın yatağı -6 dB ducking               [SES]
□ Kokpit repliklerine telsiz EQ'su geri uygulanır                  [SES]
KURGU:
□ 3:40 başlık kartı kurgudan çıkarılır (metni doğrula: kapak
  başlığı mı?)                                                     [D72]
□ Buz koşusuna foley adım sesi eklenir                             [SES]
YENİDEN ÜRETİM / YAPISAL (üretim sorusu cevaplanmadan başlanmaz):
□ Eksik omurga: S13-S14 · S16-S17 · S19-S20 · S22-S23 · S26-S28 · S29
  (öncelik: S19 CENTRAL CHOICE · S26 DORUK · S29 FİNAL)
□ S12 patlama vakum fiziğiyle yeniden (sessiz, 0.4 s flaş, ateş topu yok)
□ EKO geri getirilir; insan replikleri kask telsizi + arkadan kadraj [D82]
□ Sırt ünitesi görünen klipler yeniden (D79) — üretim zinciri
  doğrulandıktan sonra
```

---

> 📌 Bu kayıt kart C·D·E·E2·E3 adımlarıyla oluşturuldu. Skor satırları:
> teknik → `LESSONS_LEARNED.md` · hikaye → `03` · mantık → `04` ·
> karakter → `06` (Ses sütunu → 🔊 işaretçi) · ses → `07` (bu koşuyla
> AÇILDI). Plan dosyasının kendi içinde de bir uyumsuzluk not edildi:
> §QA SPEC "12 replik + S28 konuşmalı" derken DIALOGUE SCHEDULE "14
> replik / 11 sahne, S28 sessiz" diyor — sahibin düzeltmesi için bırakıldı.
