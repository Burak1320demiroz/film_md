# 🔍 LOW POWER — QA KAYDI

> **Kaynak dosya:** `yatay_4_dk_filmler/LOW_POWER/`
> **Bu filmde İKİ ayrı QA var:**
> · **TEKNİK QA** (aşağıda) — `LESSONS_LEARNED.md` kalite tablosu + Ders 39-42
> · **SENARYO QA** (31.07.2026) — [aşağıdaki bölüm](#-senaryo-qa--31-temmuz-2026) · ham çıktı: [`../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SENARYO_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SENARYO_HAM.md)
>
> ⚠️ **Teknik QA'nın orijinal raporu dosya olarak mevcut değil** — timestamp'li
> ham bulgular derslerde korunmuş.

---

# 🔧 TEKNİK QA

## 📋 KÜNYE

```
FORMAT:        3-5 dk · yatay · bilimkurgu
QA KAPSAMI:    ⚠️ TEK SAHNE (S14) — compilation DEĞİL
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    ⚠️ HATALI — S14'e ait olmayan bir replik bildirilmiş
GENEL SKOR:    4/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 6/10 | kir/toz deseni her karede yeniden üretiliyor |
| Fizik | 3/10 | |
| Kamera | **8/10** | 🏆 **serinin en yüksek skoru** — sabit lockoff |
| Işık | 4/10 | mavi gün batımında bloom + motivasyonsuz fill |
| Çevre | 5/10 | |
| Canlı | N/A | |
| Hareket | 5/10 | |
| **Parçacık ve Malzeme** | **2/10** | 🚨 **PROJENİN EN DÜŞÜK SKORU** — tabloda YOK |
| **Diyalog ve Ses** | **3/10** | ⚠️ derslerde var, tabloda yok |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

> 🚨 **Projenin en düşük tek kategori skoru (Parçacık 2/10) kalite tablosunda
> görünmüyor.** Tabloda bu film 4/10 olarak duruyor ve iyi bir kamera skoruyla
> anılıyor. Gerçek darboğaz kayıt dışı.

---

## 🔬 HAM BULGULAR (korunmuş)

```
0:01 — AI Bloom on the blue sunset
0:02 — Burned-in gibberish subtitles fade in when the voiceover begins
0:05 — Dust drifting like zero-g underwater fluid
0:08 — Dust accumulation patterns on shoulders and chest shift completely
       between frames
0:09 — Unmotivated fill
```

---

## 🧪 ÜRETTİĞİ DERSLER — 4 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 39 | Parçacıkların sıvı gibi davranması — toz su altında süzülüyor | 2/10 parçacık |
| 40 | Diyalog tetikli altyazı — ses başlayınca yazı beliriyor | 3/10 diyalog |
| 41 | Yumuşak ışık ≠ bloom — atmosferli gezegenlerde yanlış teşhis | 4/10 ışık |
| 42 | Kir ve toz deseni sürüklenmesi | 6/10 karakter |

---

## 🏆 EN ÖNEMLİ BULGU: KAMERA 8/10

> *"Kamera ilk kez 8/10 — sabit lockoff stratejisi işe yarıyor, kesme sorunu
> bu sahnede yok."*

Projede bir kategoriyi 8'e çıkaran **tek** müdahale. Prompt cümlesi değil,
**çekim stratejisi.** Bu bulgu genelleştirilmedi — sabit lockoff'un bir filmin
yüzde kaçında kullanılabileceği hiç araştırılmadı.

---

## ⚠️ BU KAYDIN GEÇERLİLİK SINIRI

```
🚨 QA TEK SAHNE (S14) ÜZERİNDEN YAPILDI — film geneli temsil etmez
🚨 SPEC BLOĞU HATALI: S14'e ait olmayan bir replik künyeye yazılmış.
   Senaryoda S14 SESSİZ. Bu yüzden:
   → Ders 35 (lip-sync) bulgusu YANLIŞ SAHNEYE atfedilmiş olabilir
   → Ders 40 (altyazı) da aynı hatalı künyeden geliyor olabilir
   (LESSONS_LEARNED'in kendi uyarısı)
□ Parçacık 2/10 ve Diyalog 3/10 tabloya aktarılmamış
□ Kare çapası ve negatif ihlal ölçülmemiş
□ Filmin kalan ~29 sahnesi hiç QA edilmedi
```

**Tekrar QA gerekli mi?** **EVET — yüksek öncelik ve dolu SPEC ile.**
Bu QA'nın künyesi kanıtlı biçimde yanlış. Ders 40'ın geçerliliği doğrulanmamış.
Ayrıca 3-5 dk formatının tek veri noktası ve tek sahneye dayanıyor.

---
---

# 📖 SENARYO QA — 31 Temmuz 2026

> **Prompt:** `../../QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> **Ham çıktı:** [`../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SENARYO_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SENARYO_HAM.md)
> **Projede saklanan İLK senaryo QA çıktısı.**

```
BİLDİRİLEN SKOR:  7.0/10 (başlık) — 7.1/10 (takip satırı) ⚠️ tutarsız
VERDİKT:          SHOOT WITH TRIMS
SPEC BLOĞU:       🚨 HATALI — filmle uyuşmuyor
KAYIT DURUMU:     GEÇERSİZ — hikaye kalite tablosunda ortalamaya girmez
```

## 🚨 NEDEN GEÇERSİZ

Rapor, 7 sahnelik ve 254 saniyelik bir film eleştiriyor. Gerçek film 25 sahne
ve 249 saniye. `LOW_POWER_PLAN.md` ile karşılaştırma:

| Alan | Rapor | Gerçek film |
|---|---|---|
| Sahne sayısı | 7 | **25** (S0–S24) |
| Süre | 254s (4:14) | **249s** (4:09) |
| Diyalog | 1 monolog | **5 konuşmalı sahne** (S2, S10, S11, S20, S22) |
| Sessiz sahne | 4 | **20** |
| Viral ara sahne | 2 | **4** (S5, S14, S19, S23) |
| Seçim anı | 1:40 | **S20** (~3:15) |
| Protagonist | "botanist" | **tarımsal sistemler mühendisi** (Dr. Selin Aras, 44) |
| Tema | "sacrifice" (feda) | **"devretme"** — plan feda hikayesi olmadığını açıkça yazar |

### Doğrudan yanlış çıkan 3 bulgu

```
❌ "Up-before-down beat yok" (raporun en sert 3 bulgusundan biri)
   → S17 TOZ ŞEYTANI tam olarak o beat. Plan onu kendi cümlesiyle
     "filmin tek yukarı hareketi" diye işaretliyor, S18'de düşürüyor.

❌ Reçete 1: "paneli silmeye çalışsın, toz hemen geri gelsin"
   → S6 (SÜPÜRME) + S7 (GERİ DOLUYOR) zaten bu. Filmde var olan çözüm,
     eksiklik diye raporlanmış.

❌ Reçete 3: "seçimi gün batımı sahnesine kes"
   → S14 ile S20 arasında 6 sahne var. Raporun zaman çizgisi uydurma.
```

## ✅ SPEC'TEN BAĞIMSIZ, KULLANILABİLİR 3 GÖZLEM

```
1. ÖZGÜNLÜK 6/10 — The Martian / Silent Running yakınlığı.
   Plan bu riski biliyor ve bir bölümünü ayrışmaya ayırmış. Dış gözün yine
   de aynı yeri işaret etmesi, ayrışmanın izleyicide OKUNMADIĞINI gösterir.
   → Ayrışma sahne düzeyinde görünür kılınmalı, plan metninde değil.

2. "GÖRÜNENİ ANLATAN REPLİK" — 19 dakikalık gecikmeyi sözle açıklamak.
   Planın replikleri hâlâ TASLAK. S11 ve S20 yazılırken bu uyarı geçerli:
   gecikme bir REPLİKLE değil, cevabın hiç gelmemesiyle kurulmalı.

3. KAPAK/BAŞLIK HİZASI — kapak S14 temelli, S14 ~2:19'da.
   4:09'luk filmde kabul edilebilir ama daha önce hiç ölçülmemişti.
```

## 📌 SONUÇ

**Tekrar senaryo QA gerekli mi? EVET — doğru SPEC ile.**
Doğru künye: `25 sahne · 249s · 5 konuşmalı sahne · 20 sessiz · viral S5/S14/S19/S23 ·
seçim S20 · tema "devretme"`. Bu rapor bir hikaye ölçümü değil, **SPEC
doğrulamasının neden zorunlu olduğunun üçüncü kanıtı** olarak duruyor.

---
---

# 🎯 12 MERCEK QA RAPORLARI (CANLI SİSTEM · 10.09.2026)

> **Kapsam:** LOW_POWER 4:15 derleme kurgusu ve ses parçası.
> **Ham Raporlar:** [`LOW_POWER_KARE_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_KARE_HAM.md), [`LOW_POWER_DEVAMLILIK_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_DEVAMLILIK_HAM.md), [`LOW_POWER_SES_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SES_HAM.md), [`LOW_POWER_HIKAYE_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_HIKAYE_HAM.md), [`LOW_POWER_ARKA_PLAN_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_ARKA_PLAN_HAM.md), [`LOW_POWER_FIZIK_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_FIZIK_HAM.md), [`LOW_POWER_AKSIYON_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_AKSIYON_HAM.md), [`LOW_POWER_EFOR_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_EFOR_HAM.md), [`LOW_POWER_KADRAJ_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_KADRAJ_HAM.md), [`LOW_POWER_OYUNCULUK_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_OYUNCULUK_HAM.md), [`LOW_POWER_ISIK_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_ISIK_HAM.md), [`LOW_POWER_HOOK_HAM.md`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_HOOK_HAM.md)

### 📊 MERCEK SKOR ÖZETİ

| Mercek | İsim | Skor | Verdivet / Durum | Ham Rapor |
|:---:|---|:---:|---|:---:|
| **Lens 1** | Kare QA (Mod V) | **5.4 / 10** | 3 Blocker (Güneş paneli doğma, Sera klip tekrarı, Parmak erimesi) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_KARE_HAM.md) |
| **Lens 2** | Devamlılık QA | **5.1 / 10** | IDENTITY BREAK (Oyuncu yüz değişimi, Kask zıplaması, Yön/yer değişimi) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_DEVAMLILIK_HAM.md) |
| **Lens 3** | Ses & Akustik | **4.3 / 10** | REJECT (Line 7 kapalı ağız Blocker, 01:12 Dijital sessizlik çukuru Blocker) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_SES_HAM.md) |
| **Lens 4** | Anlatı & Hikaye | **7.8 / 10** | PASS (Güçlü tema & fedakarlık seçimi; 19s geç kanca & sera kapı tekrarı) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_HIKAYE_HAM.md) |
| **Lens 5** | Arka Plan | **5.0 / 10** | FIELD DRIFT (Kule mimari değişimi, Kar->Çöl zemin zıplaması, Sis zıtlığı) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_ARKA_PLAN_HAM.md) |
| **Lens 6** | Fizik & Dynamics | **4.6 / 10** | TWO GRAVITIES (Kabin içi 8.87 m/s² vs 4.13 m/s² yerçekimi, 2.5s süzülme) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_FIZIK_HAM.md) |
| **Lens 7** | Aksiyon Okunurluğu | **8.6 / 10** | ACTION READS (14/15 vuruş açık okunur; B9 şalter atlama belirsizliği) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_AKSIYON_HAM.md) |
| **Lens 8** | Efor & Bedel | **4.3 / 10** | WEIGHTLESS WORK (Merdiven tırmanış/anten ayar eforsuz; yorgunluk sıfırlanması) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_EFOR_HAM.md) |
| **Lens 9** | Kadraj / Plan Sadakati | **5.3 / 10** | RHYME BROKEN (10° dutch tilt ile rhyme pair çöküşü; S5'te plansız dolly creep) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_KADRAJ_HAM.md) |
| **Lens 10** | Oyunculuk & Mimik | **5.8 / 10** | MOSTLY LEGIBLE (Duygusal yorgunluğun S21'de sıfırlanması; S19 amacsız el kaldırma) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_OYUNCULUK_HAM.md) |
| **Lens 11** | Işık & Atmosfer | **4.9 / 10** | KEY WALKS (S22-S23 enerji ışını sönmesi; saat 9->2->10 ışık zıplaması) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_ISIK_HAM.md) |
| **Lens 12** | Hook & Paylaşım | **5.5 / 10** | HOOK MISSING (İlk 10s kanca eksikliği; finalde döngüsüz karanlık çıkış) | [`HAM`](../02_HAM_RAPORLAR/LOW_POWER/LOW_POWER_HOOK_HAM.md) |

---

### 🧪 BU RAPORLARDAN ÇIKARILAN ADAY DERSLER (`GOZLEM_DEFTERI.md`)

* **[[ADAY-58]]:** Alt Kadraj Kenarında Kendiliğinden Beliren Görsel Nesne Ve Eleman Spawning
* **[[ADAY-59]]:** Derleme Kurgusunda Yanlış Uygulanan Klip Tekrarı Ve Tekraren Kurgu Hatası
* **[[ADAY-60]]:** Ellerin Göğüste Birleşmesi Anında Parmakların Birbirine Erimesi Ve Şekil Bozulması
* **[[ADAY-61]]:** Sahneler Arası Aktör Ve Yüz Amblemi Değişimi Ve İz Hopping
* **[[ADAY-62]]:** Ardışık Sahnelerde Kask Takma/Çıkarma Hızlı Flicker'ı Ve Kir Resetlenmesi
* **[[ADAY-63]]:** Ekran Sayaç Ve Metrik Değerlerinin Gidişatının Tersine Düşmesi
* **[[ADAY-64]]:** Dialogue Repliğinin Hareketsiz Ve Kapalı Dudak Üzerine Oynaması
* **[[ADAY-65]]:** Sahne Kesmelerinde Mekân Sesinin Aniden Kesilmesiyle Dijital Sessizlik Boşluğu
* **[[ADAY-66]]:** Ekrandaki Fiziksel Zorlanma Ve Sarsıntının Sakin Ses Performansıyla Çakışması
* **[[ADAY-67]]:** Tekrarlayan Sera Giriş Kutusu Ve Gereksiz Geçiş Sahneleriyle Tempo Aksaması
* **[[ADAY-68]]:** Açılıştaki Durağan Peyzaj Kadrajıyla İzleyici İlk 19 Saniye Terk Riski
* **[[ADAY-69]]:** Verici Ve Ante Kulesi Mimarisinin Sahneler Arası Değişimi Ve Form Deformasyonu
* **[[ADAY-70]]:** Karlı Zirveden Kuru Çöl Vadisine Ani Mekân Ve Zemin Dönüşümü
* **[[ADAY-71]]:** Derinlik Ve Atmosferik Perspektifin Tersine Dönmesi Ve Zıtlık Uyumsuzluğu
* **[[ADAY-72]]:** Kabin İçi Serbest Düşüşlerde Çifte Yerçekimi İvmesi Tutarsızlığı
* **[[ADAY-73]]:** Serbest Enkaz Ve Malzemenin Yerçekimsiz Çözülümlü Düz Süzülmesi
* **[[ADAY-74]]:** Pnömatik Kapı Kapanma Hızının Ardışık Kesmelerde Yarıya Düşmesi
* **[[ADAY-75]]:** Çarpmada Sürücü Ve Beden Hareketinin İnerşiyel Eylemsizlik Uyumsuzluğu
* **[[ADAY-76]]:** Konsol Şalterine Dokunma Eyleminde Mekanik Değişim Belirsizliği Ve İzolasyon Eksikliği
* **[[ADAY-77]]:** Temizlenen Güneş Paneli Modülünde Görsel Ve Elektriksel Geri Bildirim Eksikliği
* **[[ADAY-78]]:** Merdiven Tırmanmada Basamak Ve Tutunma Eforunun Görselde İşlenmemesi
* **[[ADAY-79]]:** Mekanik Ayarlama Eyleminde Gövde Ve Ağırlık Kaldıradının Kullanılmaması
* **[[ADAY-80]]:** Sahneler Arası Yorgunluk Düzeyinin Geçişsiz Şekilde Aniden Sıfırlanması
* **[[ADAY-81]]:** Açılış Ve Kapanış Kadrajları Arasında Kamera Açısı Ve Ufkun Bozulması
* **[[ADAY-82]]:** Sabit Kadraj Klibi İçinde Plansız Yavaş Yakınlaşma Kayması
* **[[ADAY-83]]:** Aynı Kamera Kurulumuna Dönüşte Kamera Yüksekliği Ve Çapa Yeri Değişimi
* **[[ADAY-84]]:** Duygusal Dönüş Sahneleri Sonrası Beden Yorgunluğunun Aniden Resetlenmesi
* **[[ADAY-85]]:** Ekipman Hazırlık Sahnelerinde Nedensiz Hand Lift Ve Generek Jestler
* **[[ADAY-86]]:** Gökyüzü Elektrik Cihazı Ve Enerji Işını Pratik Kaynağının Kesmede Aniden Sönmesi
* **[[ADAY-87]]:** Aynı Dış Mekânda Güneş Işığı Açısının Radikal Şekilde Zıplaması
* **[[ADAY-88]]:** Ardışık Sahnelerde Aşırı Renk Sıcaklığı Ve Pozlama Dalgalanması
* **[[ADAY-89]]:** Açılış Statik Jenerik Ve Yavaş Açılış Nedeniyle İlk 10 Saniye Kanca Eksikliği
* **[[ADAY-90]]:** Finalde Statik Karanlık Ve Döngü Mekanizması Eksikliği




