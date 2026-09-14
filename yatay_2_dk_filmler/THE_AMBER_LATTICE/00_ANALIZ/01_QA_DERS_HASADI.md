# 🧾 THE_AMBER_LATTICE — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D01 Kamera | Ardışık sahnelerde açı/ölçek çakışması | Ardışık iki sahne aynı açıda/ölçekte olamaz; en az 1 kademe ölçek ve ≥45° açı değişimi zorunludur | S00-S09 tüm geçişler |
| D02 Karakter | İnsan dışı uzaylı yapısının form kaybı | Mat siyah titanyum-kitin kaplama ve kesintisiz kehribar sarısı amber damar geometrisi kilitlenir | S00-S09 tüm sahneler |
| D03 Fizik | Klip içi durum değişimi kararsızlığı | Klip içi aksiyon değişimi yapılmaz, durum değişimleri sahne sınırına (End/Start) yazılır; astronot gövdesi 1H ölçek şahididir | S01, S04, S07, S08 |
| D04 Işık | Siyah ve sarı renk patlaması | 3200K kehribar sarısı emisyon ışıkları mat siyah arka planla yüksek kontrast oluşturur, overexposed bloom engellenir | S00-S09 tüm sahneler |
| D05 Ekipman | Yapısal çapalama eksikliği | Gezegen obeliski ve ana amber kulesi tüm sahnelerde kuşbakışı ve göz hizası çapa hatlarında sabit tutulur | S00, S03, S06, S08, S09 |
| D06 Prompt | V2 şablon ihlali | Tüm video promptları Subject, Action, Environment, Camera, Lighting, Render, Negative yapısında yazılır | S00-S09 tüm promptlar |
| D07 Kurgu | Ritim monotonluğu | 10 sahnelik ASL tırmanışı: S00 statik kanca (10s), S04 ivme kazanma, S08 doruk uyanış (küre parçalanması), S09 döngüsel çıkış | S00, S04, S08, S09 |
| Ders 32 Mimar | Devasa yapılarda boyut kaybetme | Uzaylı obeliskinin boyut algısı için astronot (1H = 1.8m) veya keşif aracı (3H = 5.4m) kadraja eklenir | S00, S02, S05, S08 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_MIRROR_FAUNA` | T1 Kare Kalite | Uzaylı yapısının ölçek şahidi olmaması nedeniyle devasa kanyon derinliğinin anlaşılamaması | Kadrajın ön düzlemine EVA-4 astronotu (1H) veya zemin çatlağı yerleştirilerek mimari ölçek kilitlenecek |
| `THE_STONE_SKY` | T5 Arka Plan | Dev kule arka planında titreme ve doku değişimi | Obelisk yapısı `octagonal obsidian biosteel tower` kelimeleriyle dondurulacak |
| `THE_FORGOTTEN_ARCHITECTS` | T4 Hikaye | Antik yapının novumunun belirsiz kalması | Amber sarısı enerjinin uyanış merdiveni S00 (sönük) -> S04 (damarlar parlar) -> S08 (matriks tetiklenir) şeklinde kademeli verilecek |
| `THE_BENT_GRASS` | T2 Devamlılık | Renk paleti tutarsızlığı ve sarı tonda kayma | Strict color prompt: `charcoal black metal surface with 3200K glowing amber yellow energy veins` sabit tutulacak |
| `THE_CRACKED_HELMET` | T10 Oyunculuk/Kask | Kask vizör yansımasının sahneden sahneye değişmesi | Vizör yansıması `reflective dark gold visor showing glowing amber monolith` olarak sabitlenecek |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| MÇ (Motor Çökmesi) | Plazma / akışkan sarı sıvı simülasyonu | Sıvı simülasyonu yerine katı kristalize biyo-kehribar ışık çizgileri kullanılması | S04 amber damarlarının yayılışı |
| YR (Yanıltıcı Render) | Siyah arka planda aşırı sarı ışık patlaması (blooming) | Negatif prompta `overexposed yellow glare, blown out bloom, lens flare artifacts` eklenmesi | S08 amber matriks uyanış doruğu |
| TK (Tekrar Eden Kompozisyon) | Hızlı ve abartılı aksiyon taklidi | Yavaş, prosedürel, bilimsel keşif adımları ve mektup/öznitelik odaklı kurgu | S02 astronot keşif adımları |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        8 adet
QA ARIZASI:         5 adet
RED SINIFI:         3 adet
⛔ EN PAHALI ÜÇÜ:   MÇ (Akışkan Sıvı Reddi) · T2 (Renk Paleti Sapması) · Ders 32 (Ölçek Şahidi Yokluğu)
```
