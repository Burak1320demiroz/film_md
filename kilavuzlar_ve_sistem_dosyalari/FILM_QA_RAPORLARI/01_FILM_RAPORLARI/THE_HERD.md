# 🔍 THE HERD — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_HERD_PLANET_FILM.md`
> — 3.401 satır · 15 sahne · 150 s · kalın atmosfer
> **Teknik QA (VIDEO_QA):** ❌ **GEÇERSİZ** — künye boş, yine de 3 BLOCKER üretti
> **Senaryo QA (SENARYO_QA):** ❌ **GEÇERSİZ** — kendi DUR kodunu yazdı, durmadı
> **Mantık QA (MANTIK_QA):** ✅ **4.0/10** · 03.08.2026
> Ham çıktılar (üçü de): `../02_HAM_RAPORLAR/THE_HERD_UC_MERCEK_HAM.md`

---

## 🚨 0. ÖNCE BU — İKİ MERCEK PLAN DOSYASINI ARAMADI

```
VIDEO_QA    "CHARACTER: UNVERIFIABLE (Prompt file missing)"
SENARYO_QA  "SPEC BLOCK PROVIDED: no — plan document not supplied"

GERÇEK      yatay_2_4_dk_filmler_uzay/THE_HERD_PLANET_FILM.md
            3.401 satır. Depoda duruyor. Aranmadı.
```

**Ders 54(b)'nin üçüncü tekrarı.** İlk ikisi Inversion'da olmuştu ve ders
şunu yazmıştı: *"Model dokümanın yokluğunu varsayıyor, doğrulamıyor."*
Reçete yazıldı, rubrik dosyalarına **hiç uygulanmadı** — bu çalıştırmada
uygulanmış olsaydı iki rapor da geçerli çıkardı.

→ Bu kayıttan sonra rubrikler düzeltildi (aşağıda §5).

---

## 🧩 1. MANTIK QA — geçerli rapor

```
RUBRİK:      MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — 8 kategori
QA TARİHİ:   03 Ağustos 2026
GİRDİ:       yalnız video (kurala uygun)
SÜRE:        152 s gözlendi · 14 sahne gözlendi
PLAN:        150 s · 15 sahne
GENEL SKOR:  4.0/10
GEÇERLİLİK:  ✅ GEÇERLİ
```

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | 5/10 | Dev ayak ölçeği karaktere göre kayıyor |
| Sayaç Mantığı | N/A | Rapor sayaç görmedi |
| Coğrafya | **4/10** | Gemi park yeri değişiyor |
| Zaman-Işık | 5/10 | Gölge yönü sahneler arası salınıyor |
| Kostüm-Prop | **3/10** | 🚨 Kask baloncuğu kayboluyor ve geri geliyor |
| Nedensellik | 4/10 | ⚠️ *"Sürü bırakılmadan önce gökte uçuyor"* — bkz. §2 |
| Nicelik | 5/10 | Çekilen vs uçan disk sayısı |
| Kurulum ve Terk | 6/10 | ⚠️ *"Fener kurulumsuz geliyor"* — bkz. §2 |

```
⚠️ RAPORUN KENDİ ARİTMETİK KUSURU
   Severity tally: 🟠 MAJOR 2 diyor.
   Contradiction log: 3 satır 🟠 MAJOR taşıyor.
   → Rubriğin Low Power'a (7.0 vs 7.1) yazdığı kusurun aynısı.
   Tabloya MANTIK'ın kendi skoru yazıldı, tally düzeltilmedi (ham çıktı
   dokunulmaz — kural ④).

⚠️ VERDICT alanı geçersiz değer taşıyor
   "FIXABLE IN EDIT / REGENERATION REQUIRED" — rubrikte üç değer var:
   COHERENT / FIXABLE IN EDIT / STRUCTURAL PROBLEM. Melez uydurulmuş.
```

---

## ⭐ 2. FLAGS FOR DOCUMENT CHECK — CEVAPLAR

> Kart E'nin ikinci yarısı. **Bu filmde iki bulgunun ikisi de yanlış çıktı**
> ve biri uygulanmış olsaydı filmin öncülünü yok edecekti.

### S1 — "Kask baloncuğu otomatik geri çekiliyor mu, yoksa üretim hatası mı?"

**ÜRETİM HATASI. Tartışmasız.**

```
PLAN NE DİYOR (§0.12)
  HELMET STATE SCHEDULE: kapalı S0-S11, 15 sahne.
  Açık: 0 sahne. Ara durum yok, geçiş yok.
```

Risk Kartı 3'ün ölçülmüş dördüncü tekrarı. Tarif kilidi yine tutmadı;
sayısal takvim yazılıydı ve yine tutmadı. → §4'te ele alınıyor.

### S2 — "00:18'deki diskler farklı bir tür mü, yoksa 00:28'de bıraktıkları mı?"

**Farklı bireyler, aynı tür. NEDENSELLİK HATASI YOK — rapor yanılıyor.**

```
PLAN NE DİYOR (RECURRING ENTITY BIBLE)
  | Sürü | S0, S1, S1.5, S2, S3, S7, S8, S9, S10 | 1.8 m saydam disk, 0.8 m/s |

  Sürü, filmin AÇILIŞINDAN itibaren dünyada VAR. Ortam faunası.
  Gemide olan şey başka: "sırtta 1.4 m'lik iki alık" — ve S2'nin adı
  "TIKALI ALIK: PROBLEM", S5'in adı "ALIĞI BOŞALTMAK".
  Yani hatçten çıkarılanlar, gemisinin alığını TIKAYAN bireylerdir.
```

🚨 **Raporun önerisi uygulanmış olsaydı film ölürdü.** Rapor diyor ki:
*"Regenerate scene 3 to remove sky discs, or move scene 3 after scene 5."*

```
PLAN §0.5 TERS SİMETRİ
  "S0'da sürü bir gemiyi indiriyor. S8'de aynı sürü bir gemiyi ..."

Gökteki sürü filmin AÇILIŞ GÖRÜNTÜSÜ ve ters simetrisinin yarısıdır.
Silinmesi ya da sıranın değişmesi, filmin yapısal iddiasını yok eder.
→ Kaleida Crash emsalinin aynısı: rubrik, filmin tek yapısal aracını
  kesme listesine yazdı. Belge kontrolü olmasa uygulanacaktı.
```

### S3 — (sorulmadı) "Fener kurulumsuz mu geliyor?"

**Hayır. Kurulum var, montajda okunmuyor.**

```
PLAN — RECURRING ENTITY BIBLE
  | Fener        | S0.5 (yuvada), S6, S7, S8 | 0.3 m mat turuncu silindir |
  | Fener yuvası | S0.5, S11                 | koyu oyuk, hardal sarısı bant |

S0.5 IMAGE PROMPT, ENVIRONMENT bloğu:
  "On the wall at the right edge of frame sits a 0.3 m matte orange
   cylinder clipped into a dark recess ringed with mustard-yellow tape."
```

Kurulum kadrajın **sağ kenarında** ve kokpit sahnesinin asıl konusu pencere.
Rapor onu görmedi çünkü **ekranda görünmüyor** — planda var, montajda
okunmuyor. Bu bir prompt hatası değil, **kompozisyon ağırlık hatası**:
Çehov nesnesi kadrajın kenarına konursa kurulmamış sayılır.

---

## 🚨 3. BELGE KONTROLÜNÜN BULDUĞU ASIL ŞEY — FİNAL MONTAJDA YOK

Rubrik bunu **söyleyemez** ("eksik" raporlaması yasak, haklı olarak).
Belge kontrolünde çıktı:

```
PLAN         S11 — FİNAL: BOŞ YUVA
             75mm, 1.2 m, sabit. Kadrajın merkezinde 0.32 m'lik BOŞ oyuk,
             iki açık yay klipsi, ve nesnenin yıllarca durduğu yerde
             solmamış temiz bir boya dikdörtgeni.
             → Çehov ödemesi + ters simetri + temanın taşıyıcısı

MONTAJ       14. sahne (02:18-02:27) = "Ship Interior, Looks out window"
             Bu S0.5'in kompozisyonu. S11 hiç yok.
```

**Ve SENARYO_QA bunu bağımsız olarak hissetti:**
> *"S13 Final cockpit check and fade out — REWRITE — Needs a stronger
> thematic closing image."*

Adını koyamadı ama yokluğunu ölçtü. Üç mercek tasarlandığı gibi çalıştı:
MANTIK göremez, SENARYO hisseder, belge kontrolü adını koyar.

```
🚨 ÜÇÜNCÜ TEKRAR — ARTIK ÖRÜNTÜ
   Ring Walker    plan "duygusal zirve" dediği S7-S8   → montajda yok
   Holding Field  S10 final, ters simetri              → montajda yok
   The Herd       S11 final, Çehov ödemesi             → montajda yok
   Üçü de filmin SON planlanan sahnesi. Üçü de ödeme sahnesi.
   → DERS 62
```

---

## 📌 4. NE YAPILACAK

```
🔴 YENİDEN ÜRET   S5, S6, S10, S11 karşılıkları — kask baloncuğu eksik
                  (MANTIK 00:28-00:47 ve 01:28 işaretledi)
🔴 ÜRETİLMEMİŞ    S11 FİNAL — filmin kapanış görüntüsü ve Çehov ödemesi
🟠 YENİDEN ÜRET   Gemi park geometrisi (01:48) — S8/S9 karşılığı
🟡 KOMPOZİSYON    S0.5'te fener yuvası kadrajın kenarında; merkeze yakın
                  bir konuma alınmalı yoksa S11 ödemesi okunmaz

⛔ UYGULANMAYACAK  MANTIK'ın 2. önerisi (gökteki sürüyü sil / sahne sırasını
                  değiştir). Filmin ters simetrisini yok eder. §2'ye bak.

⏳ YENİDEN ÇALIŞTIR  VIDEO_QA ve SENARYO_QA — plan dosyası artık
                  rubriklerde zorunlu arama adımı olarak yazılı (§5).
                  ⚠️ SENARYO_QA yine duracak: montaj 14 sahne / 152 s,
                     plan 15 sahne / 150 s. Sahne sayısı tutmuyor.
                     → Önce S11 üretilmeli.
```

---

## 🔧 5. BU RAPORDAN ÇIKAN RUBRİK DÜZELTMELERİ

Üç çalıştırma, üç **ölçme aleti** hatası ortaya çıkardı ve üçü de düzeltildi:

```
DERS 60  SENARYO_QA çıktı şablonunda "abort" bir ALAN'dı. Model alanı
         doldurup devam etti. → Alan kaldırıldı; DUR bloğu artık
         çıktının TAMAMI.

DERS 61  VIDEO_QA derlemede sahne sınırını gizli kesme sandı (0:07,
         🔴 BLOCKER). 15 sahnelik montajda sahne sınırı ZORUNLUDUR.
         → Derleme modu ile tek klip modu ayrıldı.

DERS 62  Üç filmde üç kez son sahne montajda yok. → Montaj kontrolü
         artık SON planlanan sahneden başlıyor.

+ Ders 51-54'ün hiç uygulanmamış reçeteleri (INPUT MISSING protokolü,
  film kimliği kapısı, dosya arama zorunluluğu) dört rubriğe işlendi.
```

---

> **Tarih:** 03.08.2026 · Ölçüm sapması ±1.3 (`../00_INDEX.md`).
> 1.5'tan küçük kategori farklarından sonuç çıkarma.
