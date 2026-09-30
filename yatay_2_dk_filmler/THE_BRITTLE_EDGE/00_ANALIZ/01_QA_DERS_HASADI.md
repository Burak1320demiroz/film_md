# 🧾 THE_BRITTLE_EDGE — QA + DERS HASADI

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
| D1 | AI klip içinde montaj/kesme yapıyor | Her video tek kesintisiz çekim; montaj/jump cut yasak | S00-S11 |
| D16 | Kask içinde yüz morphing geçiriyor | Opak siyah vizör; kask içi yüz görünmez, morphing sıfırlandı | S00-S11 |
| D34 | Model ekrana başlık kartı ve logo ekliyor | Prompt gövdesinde logo, metin veya başlık kartı yer almaz | S00, S11 |
| D42 | Yıpranma ve çizikler her karede değişiyor | Sarı gövdedeki çizik ve kirler 3 sabit çapa kelimesiyle kilitlenir | S00-S11 |
| D62 | Kurguda final sahnesi düşüyor | S11 finali tek yavaş kamera hareketiyle bağımsız vuruş olarak korunur | S11 |
| D78 | Novum sahneler arası ekranda kanıtlanmıyor | S02'de kırık yüzeyin yakın planı gevrek kırılmayı tek karede gösterir | S02, S03 |
| D138 | Giysi ve araca anlamsız metin basılıyor | Kostüm ve sarı gövde metinsiz endüstriyel boya ile tarif edilir | S00-S11 |
| D146 | Kask cam fanusa dönüşüyor | Altıgen çerçeveli gömülü opak siyah vizör olarak pozitif tanımlanır | S00-S11 |
| D157 | Novum taşıyıcısı tek karede okunmuyor | Kırık çekme kulağı ve sarı gövde aynı kadrajda net okunur | S00, S02, S03 |
| D167 | Fazla sıfatla karakter kimliği bozuluyor | 3 görsel çapa: kirli kırık beyaz giysi, turuncu kol şeritleri, siyah vizör | S00-S11 |
| D169 | Karakter zorlanması tek sahnede kalıyor | S05 ve S08'de eldivenli ellerde ve dizlerde mekanik zorlanma bedende gösterilir | S05, S08 |
| D174 | Model "screen-right" yönünü yanlış anlıyor | Yönler krater duvarı ve uçurum kenarı referansıyla verilir | S00-S11 |
| D176 | Araç zemine karışıyor | Koyu bazalt krater zemini ve endüstriyel parlak sarı gövde kontrastı | S00-S11 |
| D179 | I2V'de değişim sonrası kare veriliyor | IMAGE promptları eylemin öncesi t=0 anını gösterir | S00-S11 |
| D180 | Modelden sessizlik istenince gürültü üretiyor | Modelden sessizlik istenmez; AUDIO satırında mekanik titreşim yazılır | S00-S11 |
| D192 | Metal kopması cam tozu veya kıvılcıma dönüyor | Kopma anı cam tozu değil keskin mekanik çatlak olarak tarif edilir | S00 |
| D198 | Nesneler Dünya yerçekimiyle düşüyor | 0,16g Ay yerçekimi; kopan parça ve toz balistik yavaşça hareket eder | S00, S01, S08, S09 |
| D206 | Bedel bedende ödenmiyor | S08'de son temas koparken astronotun araca kilitlenen kaskı ve gerilen postürü | S08 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde uygulanmadı |
|---|---|
| D193, D201, D207, D208, D209, D210, D211, D212, D213, D215, D216 | Tavan ≤20 kuralı gereği bu ikincil dersler doğrudan kılavuz rehberinden ve genel kurallardan işletilecektir. |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_LOCKED_PULSE.md` | ⑨ KADRAJ | Kadrajda aksiyon başlangıcı elipsi | Aksiyon elipsi yapılmaz; kopma ve sapan geçirme kadraj içi gösterilir |
| `THE_LAST_SHIFT.md` | ⑥ FİZİK | Vakumda tozun atmosferik gibi çökmesi | Regolit tozu sürtünmesiz balistik eğriyle hareket eder |
| `THE_BORROWED_WEIGHT.md` | ⑩ OYUNCULUK | Karakterin şok anında tepkisiz kalması | S00 kopma sonrası astronotun anlık donakalması ve kask yönelimi |
| `KRONOS_SON_SINYAL.md` | ④ HİKAYE | Kurgu temposunun tekdüzeleşmesi | 12 sahnede ASL 10s korunurken iç hareket temposu S00 ve S08'de yükseltilir |
| `THE_TETHERED_MASS.md` | ② DEVAMLILIK | Halat gerginliğinin sahneler arası tutarsızlığı | Halat ve sapan gerilimi 7 nesne durum tablosuyla kontrol edilir |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| MÇ (Mekanik Çatışma/Kopma) | Çekme halatı kopması | Aşırı kıvılcım veya patlama yerine temiz mekanik ayrılma tarifi | S00 |
| YR (Yüksekten Düşme Riski) | Uçurum kenarında araç kayması | Dramatik takla/yuvarlanma yerine kayanın ön tekerleği durdurduğu kontrollü kayma | S01, S08 |

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
RED SINIFI:         2 adet
⛔ EN PAHALI ÜÇÜ:   D192 (Metal kopmasının cam tozuna dönmesi) · D198 (Ay yerçekiminde balistik toz ve parça hareketi) · D206 (Bedelin bedende ödenmemesi)
```
