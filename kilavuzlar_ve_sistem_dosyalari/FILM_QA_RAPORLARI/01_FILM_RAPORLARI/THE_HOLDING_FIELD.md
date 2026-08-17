# 🔍 THE HOLDING FIELD — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_HOLDING_FIELD_PLANET_FILM.md`
> **Teknik QA (VIDEO_QA):** ⛔ kapıda durdu — künye "The Shift" dedi, doküman
> "THE HOLDING FIELD" diyor. Doğru davranış; film kimliği çözülünce yeniden.
> **Senaryo QA (SENARYO_QA):** ⛔ kapıda durdu — künye 134 s, plan 140 s.
> **Mantık QA (MANTIK_QA):** ✅ **4.0/10** · 03.08.2026 · ham rapor
> `../02_HAM_RAPORLAR/THE_HOLDING_FIELD_MANTIK_HAM.md`
>
> Üç mercek arka arkaya çalıştı; **yalnız doküman istemeyen mercek başlayabildi
> ve gerçek sorunu o buldu.** Diğer ikisi doğru sebeple durdu ama yanlış
> soyutlama seviyesinde: "başlık/süre uyuşmuyor" dediler, "video zaten bu film"
> demediler.

---

# 🧩 MANTIK QA

## 📋 KÜNYE

```
RUBRİK:        MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — 8 kategori
QA TARİHİ:     03 Ağustos 2026
GİRDİ:         yalnız video (rubrik doküman istemez — kurala uygun)
VİDEODAKİ AD:  "The Shift" — üretim sırasındaki geçici ad
SÜRE:          134 s (2:14) · gözlenen sahne: 13
PLAN:          140 s · 14 sahne
GENEL SKOR:    4.0/10
KARAR:         STRUCTURAL PROBLEM
GEÇERLİLİK:    ✅ GEÇERLİ — rubrik doküman istemiyor, kapı ihlali yok
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | **3/10** | 🚨 Yerçekimi sahneden sahneye normal ↔ ters gidiyor |
| Sayaç Mantığı | N/A | Rapor sayaç görmedi — 9 segmentli halka okunmamış |
| Coğrafya | **3/10** | Gemi S4'te gidiyor, S13'te park hâlinde |
| Zaman-Işık | **7/10** | ⭐ Güneş açısı ve gölge istikrarlı — ışık takvimi tuttu |
| Kostüm-Prop | **3/10** | Halka geometrisi değişiyor (3 uç ↔ 1 kol) |
| Nedensellik | 4/10 | Sebepsiz beliren ve kaybolan ikinci figür |
| Nicelik | 4/10 | Kol sayısı 3→1, insan sayısı 2→1 |
| Kurulum ve Terk | 4/10 | Kopan gemi paneli bir daha görünmüyor |

```
🔴 BLOCKER: 2    🟠 MAJOR: 2    🟡 MINOR: 1
```

---

## ⭐ 1. FLAGS FOR DOCUMENT CHECK — CEVAPLAR

> Rubriğin ikinci yarısı budur (AGENTS kart E). Rubrik doküman görmediği için
> soru sordu; cevaplar plan dosyasından verildi. **Bu bölüm raporun en değerli
> kısmıdır ve bu filmde teşhisi tamamen değiştirdi.**

### S1 — "Ortam dalgalanan / kırık yerçekimine sahip olacak şekilde mi tasarlandı?"

**HAYIR. Kesinlikle hayır. Bu, filmin tek yasağının ihlalidir.**

```
PLAN NE DİYOR (§0.13)
  Yerçekimi sabit 0.61 g. YÖN HİÇ DEĞİŞMEZ.
  Alan bir sürüklenme kuvvetidir — yalnız İNİŞ HIZINI sönümler.
  Yükselme diye bir durum YOKTUR.

PROMPT KİLİDİ
  "never rising" ifadesi 28 promptun 28'inde var.
  "NO OBJECT IS EVER MOTIONLESS IN MID-AIR" büyük harfle, 28/28.

EKRANDA NE VAR
  0:20  arka planda taşlar YUKARI süzülüyor
  0:42  kadın YUKARI süzülen taşlara dokunuyor
  1:30  yukarı bakış — enkaz gökyüzüne doğru YÜKSELİYOR
  2:00  yükselen taşların arasında yürüyor
```

Rapor buna "yerçekimi rastgele dönüyor" dedi ve Fizik'e 3/10 verdi — **doğru
gözlem, eksik teşhis.** Doküman olmadan bunun bir *alternatif durum* değil,
**yasak durum** olduğunu bilemezdi. Bu bir devamlılık kayması değil:
**filmin öncülü ters render edilmiş.**

> Rubriğin kendi ölçütü: *"geri giden sayaç bir devamlılık kayması değildir,
> filmin öncülünün çökmesidir — diğer her şey temiz olsa bile BLOCKER."*
> Burada geri giden şey sayaç değil, **dünyanın kuralı.**

### S2 — "S6'daki ikinci koyu figür halüsinasyon/klon mu, üretim glitch'i mi?"

**Üretim glitch'i.**

```
PLAN NE DİYOR (§0.12)
  HUMAN COUNT LOCK: tam 1 insan, 14 sahnenin 14'ünde.
  Mürettebat yok, pilot yok, ikinci silüet yok, ikinci yansıma yok.
```

Risk Kartı 4'ün ölçülmüş üçüncü tekrarı (Kaleida 1:25 · Tidal Hunt 0:00 ve
1:49 · burada 0:51). ⚠️ Öncekilerin üçü de **araca inme/binme** anındaydı;
bu ilk kez **açık arazide, yürüyüş sahnesinde** çıktı — kartın "en çok
iniş/kalkışta" tarifi genişletilmeli.

### S3 — (sorulmadı, cevaplanabilir) "Gemi S4'te gidiyor mu?"

**Hayır. S2 BAŞARISIZ bir tırmanıştır.**

```
PLAN NE DİYOR (S2 video promptu)
  3s — dört ayak yerden kesiliyor, gemi 0.06 m/s ile yükseliyor
  6s — on saniye tam itki toplam yarım metre kazandırdı
  8s — iticiler kesiliyor, gemi kazandığı yarım metreyi geri düşüyor
```

Bu sahne filmin **problemini kuran tek sahnedir** ve tam tersi üretilmiş.
Öncül iki yerden birden ölüyor: taşlar yükseliyor (kural yok) ve gemi
gidebiliyor (çatışma yok).

### S4 — (sorulmadı) "Halka 3 uçlu mu, 1 kollu mu?"

**1 kollu doğru.** `RECURRING ENTITY BIBLE`: *dış çap 3 m, kalınlık 0.4 m,
**tek kol**, aynı geometri iki kez.* Yani S12 (1 kol) doğru, S8 (3 uç)
sürüklenme.

🚨 **Bunun bedeli skordan büyük:** S4 ve S8 filmin **tek yapısal aracıydı**
(birebir aynı kadraj — dokunmayan el / kavıran el, LOW POWER S12/S20
modeli). Halka geometrisi değişince kadraj tekrarı okunmuyor ve
**yapı = tema** aracı ekrana hiç çıkmamış oluyor.

### S5 — (sorulmadı) "Kopan gemi paneli planda var mı?"

**Yok.** Planda gemide **zaten eksik olan** bir iskele itici kaportası var —
sabit, filmin başından beri orada olan bir tasarım özelliği. Model onu bir
**olaya** çevirmiş (inişte kopan panel). Rapor bunu haklı olarak "kurulup
terk edilen nesne" diye işaretledi; aslında hiç kurulmaması gerekiyordu.

---

## 🎬 2. SAHNE EŞLEŞTİRME — video 13 / plan 14

| Video | → Plan | Durum |
|:--:|:--:|---|
| 1 iniş + yan panel kopuyor | S0 | ⚠️ panel kopması planda yok |
| 2 rampa, taş **ağır** düşüyor | S0.5 | ⚠️ planda beden 1.0 m/s, yumuşak |
| 3 taşa vuruyor, arkada taşlar **yükseliyor** | S1 | 🔴 yükselme yasak |
| 4 gemi havalanıp **gidiyor** | S2 | 🔴 planda başarısız tırmanış |
| 5 asılı taşlara dokunuyor | S2.5 | ✅ |
| 6 yürüyor, **ikinci figür** | S3 | 🔴 klon |
| 7 dikmeden toz **aşağı** iniyor | S6 | ✅ doğru davranış |
| 8 **3 uçlu** kadran | S4 | 🟠 kol sayısı |
| 9 kum bırakıyor, aşağı düşüyor | S5 | ⚠️ sınırın iki hızı görünmüyor |
| 10 yukarı bakış, enkaz **yükseliyor** | S6.5 | 🔴 yükselme yasak |
| 11 kadransız yüzeye dokunuyor | S7 | ✅ |
| 12 **1 kollu** kadranı çeviriyor | S8 | ✅ doğru geometri |
| 13 asılı taşlar arasında yürüyor, gemi park | S9 | ⚠️ inen gökyüzü ve çarpan parça yok |
| — | **S10 FİNAL** | 🚨 **montajda yok** |

```
S10 = yükselen gemi + sönen son segment = filmin TERS SİMETRİSİ ve held frame'i.
Ring Walker sınıfı bulgu: planın kapanış görüntüsü hiç üretilmemiş.
⚠️ Bunu MANTIK_QA raporlayamaz (rubrik "eksik" demeyi yasaklıyor, haklı olarak).
   Buraya, belge kontrolünde girdi.
```

---

## 🔑 3. KÖK NEDEN — yasak değil, klişe kazandı

Yükselme 28/28 promptta yasaklıydı ve tutmadı. Sebep prompt'ta **eksik yasak**
değil, prompt'ta **fazla isim:**

```
28 PROMPTTA ANTI-GRAVİTE TETİKLEYİCİ SÖZCÜK SAYIMI
  "in mid-air"        28   ← yasak cümlesinin İÇİNDE, ama kelime orada
  "hang / hanging"    13   ← POZİTİF betimlemede
  "caught material"    4
  "suspended"          3
  "floating / float"   4
```

Ders 56'nın mekanizmasının aynısı: *"dalış" sözcüğü su üretiyor.* Burada
**"hang / suspended / floating"** anti-graviteyi üretiyor. Model olumsuzlamayı
değil **ismi** çiziyor — ve "havada asılı duran taş"ın eğitim verisindeki tek
karşılığı anti-gravitedir.

→ **DERS 59** olarak yazıldı. Düzeltme prompt'a cümle eklemek değil,
**pozitif betimlemeden tetikleyici ismi çıkarmak.**

---

## ✅ 4. NE TUTTU

```
IŞIK TAKVİMİ      Zaman-Işık 7/10 — bu rubriğin bu filmdeki en yüksek skoru
                  ve depoda Last Archive'dan sonraki en iyi ikinci değer.
                  §0.11'in monotonik tablosu (22° → 3°) ekranda tuttu.
                  → Katmanlı dünya kartının (6b) ilk açık başarısı.
SAYAÇ             Rapor "NONE" dedi — yani hiçbir çelişki bulamadı.
                  Ama 9 segmentli halkayı da hiç okumadı; sayaç görünmemiş.
                  → Bu bir başarı değil, ölçülememe. Bkz. §5.
HALKA (S12)       1 kollu, segmentli, ışıklı — Bible'a birebir uygun.
TOZUN YÖNÜ (S7)   Dikmeden aşağı inen toz doğru render edilmiş: kural
                  bazı sahnelerde TUTUYOR. Yani prompt yapılabilir bir şey
                  istiyor; sorun tutarlılıkta.
```

---

## 🚨 5. SAYAÇ HİÇ GÖRÜNMEMİŞ — sessiz kayıp

Plan filmin sayacını 9 segmentli halkanın **doluluğu** olarak tasarladı
(§0.10, Risk Kartı 5'in metinsiz çözümü): 9 ⬤ → 7 ⬤ → 3 ⬤ → 0 ⬤.

Rapor `COUNTER CURVE: NONE` yazdı — yani **13 sahne izledi ve sayacı hiç
fark etmedi.** Ekranda yanlış bir şey yok; sadece bir şey yok.

Bu, Ders 50'nin (Tidal Hunt sayacı) kardeşi ama farklı sebeple: orada yasak
anlatımı siliyordu, burada **anlatım kanalı fark edilemeyecek kadar küçük.**
9 küçük segmentin kaçının yandığı 2:14'lük bir videoda okunmuyor.

→ Plan dosyasına açık soru olarak eklendi. Prompt hatası değil, **tasarım
   ölçek hatası.**

---

## 📌 6. YAPILACAKLAR

```
🔴 ÜRETİM       S1, S2, S2.5, S3, S6.5, S9 yeniden üretilir — sözcük
                düzeltmesinden SONRA (Ders 59)
🔴 ÜRETİM       S10 hiç üretilmemiş; filmin finali eksik
🟠 ÜRETİM       S4 halka geometrisi S8 ile eşleşmeli (kadraj tekrarı)
🟡 KURGU        S13'ün arka planındaki park hâlindeki gemi maskelenebilir
✅ YAPILDI      Prompt sözlüğü temizlendi — film dosyası §0.13
✅ YAPILDI      Ders 59 yazıldı
⏳ BEKLİYOR     VIDEO_QA ve SENARYO_QA — film kimliği çözüldü, yeniden
                çalıştırılabilir (künyeye THE HOLDING FIELD / 140 s yazılacak,
                ama montaj 134 s ve 13 sahne olduğu için SENARYO_QA yine
                uyuşmazlık verecek → önce S10 üretilmeli)
```

---

> **Tarih:** 03.08.2026 · **Ölçüm sapması uyarısı:** kategori skorları ±1.3
> gürültü taşır (`../00_INDEX.md`). 1.5'tan küçük farklardan sonuç çıkarma.
