# 🏛️ THE UNBROKEN CITY — Film QA Kaydı

> Oluşturma: 06.08.2026 · dört mercek aynı gün, dördü de MOD V (belgesiz)
> koşuldu; belge cevapları aşağıda bu kayda işlendi.
> Kaynak dosya: `yatay_2_4_dk_filmler_uzay/THE_UNBROKEN_CITY/THE_UNBROKEN_CITY_PLANET_FILM.md`

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 🔧 VIDEO_QA | ✅ Ⓥ mod V | **5/10** · REGENERATE (3 BLOCKER) | `02_HAM_RAPORLAR/THE_UNBROKEN_CITY_TEKNIK_HAM.md` |
| 📖 SENARYO_QA | ⚠️ Ⓥ mod V ŞARTLI | **5/10** · REVISE STRUCTURE | `..._SENARYO_HAM.md` |
| 🧩 MANTIK_QA | ✅ (rubrik zaten belgesiz) | **8.0/10** · FIXABLE IN EDIT — **serinin en yüksek mantık skoru** | `..._MANTIK_HAM.md` |
| 🧍 KARAKTER_QA | ✅ (opsiyonel 5. mercek) | **8/10** · DRIFTS BUT RECOVERABLE | `..._KARAKTER_HAM.md` |
| 🎨 KAPAK_QA | ❌ | — | — |

```
KÜNYE (plan)   16 sahne × 10 s = 160 s · 0 kesme · sessiz · ince atm. ·
               doruk S9 (kayıt cihazı kancaya) · S15 insansız fırlatma
KURGU (ölçülen) 165 s · merceklerce ~8 sahne okundu · fırlatma VAR ·
               2:40'ta yanık başlık kartı · doruk SEÇİMİ kurguda YOK
DERS 65 NOTU   dört raporun dördü de FILM: (not supplied) yazdı — kural
               bu koşuda TUTTU (Stone Sky'da tutmamıştı)
```

---

## 🔎 FLAGS FOR DOCUMENT CHECK — CEVAPLAR (plan dosyasından)

> Mod V raporları soru sordu; cevaplar plan/bible'dan verildi. Bu bölüm
> kart C/D/E/E2 adım 2'dir ve koşunun en değerli çıktısıdır.

### 🔧 VIDEO_QA soruları

**1. "0:40 duplicate — ayna duvarı planlı mı?"**
HAYIR. Bible'da ayna/yansıtıcı yüzey yok; HUMAN COUNT LOCK "tam 1 insan",
negatif çekirdekte ayrıca "no statue or silhouette shaped like a person".
→ **GERÇEK KLON İHLALİ.** DERS 69'un tekrarı, ama YENİ sıcak nokta:
biniş/iniş değil, **loş iç mekân** (tek ışık kaynaklı karanlık oda).
DERS 69'a tekrar kaydı işlendi.

**2. "1:20 el feneri + gölgeler tam siyah değil — fill yasak mıydı?"**
Lamba PLANLI: LAMP STATE SCHEDULE (S8-S9 + S12 açık). Zayıf dolgu %2
basınçlı ince atmosferde MEŞRU (Ders 41 · KILAVUZ §3.2). → İhlal değil;
bulgu düşürüldü.

**3. "2:40 başlık kartı — istenmiş miydi?"**
HAYIR — negatif çekirdek "no title card, no end card, no credits" der.
Dahası yanan metin (**"THE WINDOW THAT SHOWS NO SKY"**) üretim
belgesindeki **KAPAK PROMPTU A sürümünün kendi bölüm başlığıdır**
(`SUBJECT — THE WINDOW THAT SHOWS NO SKY`). Belge metni ekrana sızdı:
kapak üretimi film kurgusuna karışmış. → **DERS 72** + KILAVUZ §7 tuzağı.

### 📖 SENARYO_QA soruları

**1. "Engel/çatışma planlı mı, salt atmosfer mi?"**
Plan §0.4: BİLİNÇLİ tehditsiz dramaturji; tek dramatik motor S9 bedelli
seçim — kayıt cihazı (9 günlük görev verisi) kapı mekanizmasına verilir
ve geri alınamaz. **Kurguda mekân var (kanca 1:30'da inceleniyor), SEÇİM
YOK.** "Karakter hiç seçim yapmıyor / bedel yok / duygu yayı düz"
bulgularının üçü de aynı kök nedene iniyor: **planın doruğu kurguya
girmemiş.** Ders 62 sınıfının BEŞİNCİ tekrarı (Ring Walker · Holding
Field · Herd · Stone Sky · Unbroken City). → **DERS 72'nin 4. kilidi.**

**2. "S3 (ilk kap odası) S6'ya (ışık kuyulu oda) planlı yankı mı?"**
EVET — Çehov zinciri: S4 evler (3 ters kap = sakin veda) ↔ S10-S11 ilk
oda (3 ters kap + 1 DİK kâse = dokunulmayan çekirdek). Tekrar değil,
kurulum-ödeme çifti. Ayırt edici sayaçlar (duvar dokusu alaşım→moloz,
tavan 40→3 m) kurguda okunmayacak kadar zayıf üretilmiş — planlı ayrım
ekrana taşınamamış.

### 🧩 MANTIK_QA sorusu

**"Kanca-zincir mekanizması planlı bir etkileşim miydi?"**
EVET — SORUNUN KENDİSİ FİLMİN DORUĞUDUR. Plan S9: 8 kg kayıt cihazı
kancaya asılır, 4 m yuvaya iner, taş kapı açılır; bedel S12'de boş göğüs
yuvasıyla görülür. Mantık merceğinin "OPEN THREAD — asla kullanılmıyor"
bulgusu, senaryo merceğinin "seçim yok" bulgusunun mantık dilindeki
karşılığıdır. İki bağımsız mercek aynı kurgu boşluğunu buldu.
(Işık sıçraması 00:10↔02:10: plan DUSK→LATE DUSK→NIGHT EDGE ilerleyişi
planlıdır; kurguda ara sahneler sıkışınca sıçrama okunuyor — kurgu işi.)

### 🧍 KARAKTER_QA sorusu

**"Karakterin adı/arka planı belgede var mı?"**
Dr. Ece Aydan, 41, ksenoarkeolog-haritacı (Character Bible; ad kurala
uygun olarak hiçbir prompta yazılmadı). Rapor pasaportunun belgeyle
karşılaştırması üç ek bulgu verdi (mod V bilemezdi):
- **"rear backpack life support"** → Bible AÇIKÇA yasaklar: "No
  back-mounted tank, no hose, no cable." Üretim bible'a aykırı sırt
  ünitesi eklemiş.
- **"clean, minimal weathering"** → Bible'ın SABİT yıpranma izleri (sol
  önkol çiziği, bot burnu tozu, sağ omuz sürtmesi) üretilmemiş.
- Pasaportta **24 cm kayıt cihazı / boş yuva anlatısı hiç yok** — göğüs
  ünitesi jenerik "chest box" olarak üretilmiş. S9 bedeli görsel olarak
  kurulamazdı; doruk eksiğinin üretim tarafındaki kökü bu olabilir.

---

## 📊 KATEGORİ SKORLARI

**🔧 Teknik (Ⓥ):** Karakter 4 · Fizik 4 · Kamera 8 · Işık 6 · Çevre 5 ·
Canlı N/A · Parçacık 3 · Hareket 4 → **5/10** — 3 BLOCKER: klon 0:40 ·
yanık başlık 2:40 · fırlatma egzozu kütlesiz 2:32

**📖 Senaryo (Ⓥ ŞARTLI):** Kanca 5 · Önerme 6 · Yapı 5 · Karakter 4 ·
Tema 5 · Diyalog N/A · Yay 4 · Final 6 · Özgünlük 6 · Tutundurma 4 →
**5/10** — kök neden: doruk kurguda yok (yukarıda)

**🧩 Mantık:** Fizik 9 · Sayaç N/A · Coğrafya 8 · Zaman-Işık 7 ·
Kostüm-Prop 9 · Nedensellik 8 · Nicelik 10 · Kurulum 8 → **8.0/10**

**🧍 Karakter:** Yüz 9 · Saç-Beden 9 · Kostüm 8 · Yıpranma 8 · Ekipman 9
· Kesme 8 · Sayı N/A · Ses N/A → **8/10**

---

## 🧭 SONUÇ VE SONRAKİ ADIM

```
1. Klip envanteri çıkarılsın: kurgudaki her klip plan sahne numarasıyla
   eşleştirilsin (hangi sahneler üretildi, hangileri girmedi — özellikle
   S0 yanma dalgası, S3 ilk ayak izi, S9 seçim anı, S12 boş yuva).
2. S9 seçim anı + S12 boş yuva ÜRETİLMEDEN film yayınlanamaz — üç mercek
   üç dilde aynı boşluğu raporladı.
3. 2:40 başlık kartı kurgudan çıkarılsın (kapak çıktısı ayrı dosyadır).
4. Klon (0:40) ve merdiven teması (2:25) klipleri yeniden üretim adayı —
   film dosyası Bölüm 4 KAPI ölçütleri zaten bunları tanımlıyor.
5. Yeni ders: DERS 72 (kurgu kapısı yataya genellendi). DERS 69'a iç
   mekân tekrar kaydı düşüldü.
```
