# 🧾 THE_LISTENING_WORLD — QA + DERS HASADI

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
| D1 | Tek çekim AI tarafından kesiliyor | Klip içi kesme yok, kamera 10 saniye boyunca tek kesintisiz hareketi korur | S0–S15 |
| D16 | Kask arkasında yüz morphlanıyor | Vizör %100 opak parlak siyah kalkan; göz, yüz ve ten hiçbir karede görünmez | S0–S15 |
| D34 | Model jenerik metni ekliyor | Ekrana metin, başlık, altyazı veya yapay filigran basılmaz | S0–S15 |
| D42 | Yıpranma her karede yeniden üretiliyor | Koyu turuncu giysi ve mat kask yüzeyindeki ince buz çeperi sabit kalır | S0–S15 |
| D45 | Prompt iskeleti ekrana sızıyor | Estetik sıfatlar yasak; yalın fiziksel nesne, konum ve ışık fiilleri | S0–S15 |
| D62 | Montajda en çok düşen sahne final | S15 bağımsız yörünge açısı kurguda tam 10 saniye korunur | S15 |
| D70 | Üretim kilitleri kurguyu bağlamıyor | 16 klip tam 10.0 saniye, toplam süre tam 160 saniye, ekran metni 0.0 saniye | S0–S15 |
| D78 | Sahneler arası anlatım okunmuyor | Vericinin beyaz ışık ritmi ile buzdaki turkuaz yanıt ritmi tek karede sayılır | S8, S10, S11, S12 |
| D138 | Metin yasağı kostüme yazıldı | Giysi üzerinde hiçbir metin/amblem yok; kimlik yalnız renk ve formla verilir | S0–S15 |
| D139 | Düz sırt kilidi tutmuyor | Mat siyah sırt ünitesi kutu geometrisi ve kalın kablo bağlantılarıyla pozitif tarif | S0, S2, S7 |
| D141 | Klip var vuruş yok | S9 bekleyişi ve S10 ilk karşılık sahnesi net dramatik vuruş taşır | S9, S10 |
| D146 | Seamless visor kubbe davetiyesi | Opak vizör gömülü metalik çerçeve contasıyla geometrik olarak kilitlenir | S0–S15 |
| D157 | Novum taşıyıcısı tek karede yok | Cihazın beyaz vericisi × buzdaki biyolüminesans turkuaz damar | S8, S10, S11, S12 |
| D169 | Zorlanma sözlüğü tek sahnede | Düşük yerçekimli buzda adım atma ve eğilme fiziksel direnç ve efor taşır | S1, S7, S14 |
| D174 | Screen-right referansı kayıyor | Hareket yönü vadi duvarı ve sabit dev siyah kaya sütunları referansıyla verilir | S3, S4, S5 |
| D179 | İmaj promptu t=0 anını yazmıyor | İmaj promptları eylem başlangıç anını (t=0) kilitler | S0–S15 |
| D180 | Planlı mutlak sessizlik modelden istendi | Modelden sessizlik istenmez; ses miksi post-prodüksiyonda kask içi nefesle kurulur | S0–S15 |
| D201 | Vakumda güneş açısı komşu sahnede flip | Gaz devi EREON ve halkalarının yönü tüm dış açılarda tutarlıdır | S0–S15 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D198 | Sıfır-G serbest süzülme bu filmde yok; yüzeyde düşük yerçekimi (0.12g) geçerlidir |
| D203 | Replik envanteri yok; filmde karşılıklı diyalog bulunmamaktadır |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_DEAD_APPROACH.md | T1_KARE | Vakumda ölçek kaybı ve nesne birleşmesi | Ön planda keskin buz kenarı, orta planda insan, arka planda dev gaz devi katmanlanır |
| THE_COLD_WELD.md | T6_FIZIK | Vakum ortamında hatalı atmosferik gölge yumuşaması | Mutlak siyah gölgeler, motivasyonsuz dolgu ışığı sıfırlanır |
| THE_LOCKED_PULSE.md | T4_HIKAYE | Gönderilen sinyal ritminin izleyici tarafından sayılamaması | Sinyal darbeleri net saniye aralıklarıyla kompozit/kurgu notuna bağlanır |
| THE_LAST_SHIFT.md | T4_HIKAYE | Kurguda sahnelerin eksiltilerek anlatının kopması | 16 sahnenin tamamı kurgu listesinde tam süresiyle tutulur |
| THE_COLD_BURN.md | T2_DEVAMLILIK | Buz arazisinde yön ve yer imi kayması | EREON gezegeni ve ufuktaki dev kaya sütunları sabit yön çapası yapılır |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PB (Politika/Beden) | Yüzü tamamen kapalı astronotta anonimlik/yapay insan algısı | Endüstriyel keşif basınç giysisi, görünür gövde dikişleri ve mat donanım tarifi | S1 (yakın plan eldiven ve cihaz) |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        18 adet
QA ARIZASI:         5 adet
RED SINIFI:         1 adet
⛔ EN PAHALI ÜÇÜ:   D146 (vizör biçimi) · D78 (anlatım okunurluğu) · D209 (dünya çapası)
```
