# 🧾 THE_STATIC_VEIL — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D200 | Tek kadrajda iki yerçekimi | 0.16g Ay kütleçekimi: adımlar yavaş; toz partikülleri elektrostatik dik yükselir, yere parabolik inmez | S0, S1, S4 |
| D202 | Bedelde seçim okunmuyor | Astronot kaderine boyun eğmez; tereddütlü elden sonra bataryayı bilerek şaseye çarpar | S8, S9 |
| D206 | Bedel bedende ödenmiyor | Batarya patlayıp göstergeler söndükten sonra duraksar, omuzları çöker, adımları temkinleşir | S9, S11 |
| D208 | Giysi kimliği tutarsız | Beyaz sert kompozit, gri esnek körük eklem, altın aynalı vizör, sırtsız gövde | S0–S11 |
| D209 | Dünya çapası / yön sapması | Çapa: zemin rayı + fener pilonu; astronot soldan sağa ilerler | S1–S11 |
| D211 | S0 soru yok / S11 çıkış yok | S0'da rüzgarsız havada dik yükselen toz sorusu; S11'de fenerin yanışıyla çözülmüş çıkış | S0, S11 |
| D212 | Ardışık sahnede aynı vuruş | Silme (S2) → Arama (S3) → Varış (S4) → Soket (S5); eylemler farklılaşır | S2↔S3, S7↔S8 |
| D213 | Aksiyon elipsi kadraj dışı | Bataryanın metal pilona vurulması ve ark kadraj içinde açıkça gösterilir | S9, S10 |
| D214 | Kadrajda olmayan beden tarifi | IN FRAME satırına katı uyum; görünmeyen uzuvlar prompta yazılmaz | S0–S11 |
| D146 | Biçim kilidi metinle tutmuyor | Referans paketiyle astronot giysisi, fener gövdesi ve krater zemini kilitlenir | S0–S11 |
| D174 | Model yönü karıştırıyor | Ekran yönü kılavuz rayı ve hedef pilon referansıyla sabitlenir | S1–S10 |
| D192 | 1 numaralı risk tarifte kaldı | Toz yüksekliği 1-2 m, tane boyutu 10-100 μm, ark süresi ≤0.3 s sayıyla yazıldı | S0, S1, S4, S9 |
| D139 | Boş sırt modele bırakıldı | Kamera arkadayken: "the back of the suit is one continuous smooth panel from collar to hip" | S1, S6, S11 |
| D141 | Klip var vuruş yok | Her 10 saniyelik sahnede tek ve net bir eylem/vuruş tamamlanır | S0–S11 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D182 | Replik/diyalog yok — diyalog senkronizasyon dersi muaf |
| D194 | Tek karakterli film — çift karakter ayrılık dersi muaf |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_BRITTLE_EDGE` | T14 HAREKET | Adım kadansı vakumda bazen aşırı hızlı üretildi | 0.16g yavaş ve yaylanan adım ifadesi tüm hareket sahnelerinde |
| `THE_SHADOW_LINE` | T11 IŞIK | Gölge hattında difüzyon ve atmosferik yumuşama sızdı | Jilet keskin gölge hattı, zero feathering, no ambient fill |
| `THE_BURNING_PLUME` | T4 HİKAYE | Bedel sahnesinde karakter tepkisi gecikti | S9'da temas ile eşzamanlı gösterge sönüşü ve anında kinesik çöküş |
| `THE_SINKING_STAKE` | T13 UYUM | Üretim sırası kronolojik yapılınca doruk sahnesi yarım kaldı | Üretim sırası: Referans Paketi → S9 Doruk → S0 Hook → S11 Final |
| `THE_SCOURED_GLASS` | T2 DEVAMLILIK | Cam aşınması sahneler arasında tutarsız dalgalandı | Toz kaplama ve matlaşma oranı sahne sahne artan monoton yüzdelerle bağlandı |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PB (Patlama/Bomba) | Batarya patlaması ve kıvılcım | Yangın/alev yok; ≤0.3s beyaz-mavi elektriksel ark olarak nötr tanımlandı | S9 Batarya çarpması |
| KT (Kask/Travma) | Kask camı kırılması / boğulma | Cam asla çatlamaz; tehlike camın dıştan tozla zımparalanıp matlaşmasıdır | S2 Vizör silme |
| TK (Tehlikeli Kimyasal) | Yanıcı duman / gaz sızıntısı | Vakumda duman ve gaz yok; tozlar kuru elektrostatik mineral taneleridir | S0, S1, S4 |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        14 adet (≤20 tavanı içinde)
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   D200 (Tek kadrajda iki yerçekimi) · D139 (Boş sırt anomalisi) · PB S9 (Batarya arkı nötr tarifi)
```
