# 🟠 THE BLIND RETURN — Film QA Kaydı

> Oluşturma: 07.08.2026 · dört mercek aynı gün koşuldu; üçü MOD V (belgesiz)
> aynı 169 saniyelik kurguyu ölçtü, VIDEO_QA koşusuna ise **video hiç
> yüklenmedi** (girdisiz koşu → DERS 80). Filmin dosyasında hazır SPEC bloğu
> vardı (§0.15) ve üç merceğin hiçbirine verilmedi — Starless Circle'la aynı
> operatör hatası.
> Kaynak dosya: `yatay_2_4_dk_filmler_uzay/THE_BLIND_RETURN/THE_BLIND_RETURN_MARS_STORM_FILM.md`

---

## 🎯 MERCEK DURUMU

| Mercek | Durum | Skor | Ham rapor |
|---|---|---|---|
| 🔧 VIDEO_QA | 🚨 **GEÇERSİZ — girdisiz koşu** (video yüklenmedi; rapor yine de REGENERATE verdikti yazdı → DERS 80) | — | `02_HAM_RAPORLAR/THE_BLIND_RETURN_TEKNIK_HAM.md` |
| 📖 SENARYO_QA | ⚠️ Ⓥ mod V · tam kurgu · **DERS 75 kapısı ÇALIŞTI** (169 s / 13 kesme ölçüldü, TAM KOŞU) | **4.0/10** · REVISE STRUCTURE | `..._SENARYO_HAM.md` |
| 🧩 MANTIK_QA | ✅ (rubrik zaten belgesiz) · tam kurgu | **4.0/10** · STRUCTURAL PROBLEM | `..._MANTIK_HAM.md` |
| 🧍 KARAKTER_QA | ✅ (opsiyonel 5. mercek) · tam kurgu | **4.0/10** · DRIFTS BUT RECOVERABLE | `..._KARAKTER_HAM.md` |
| 🎨 KAPAK_QA | ❌ | — | — |

```
KÜNYE (plan)    18 sahne × 10 s = 180 s · 0 kesme · 8 replik (hepsi SUIT AI,
                kadın hiç konuşmaz) · doruk S11 (kendini mühürleme) ·
                Çehov 4 = S15 yedek vizör · koda S15-S17 (pencere → yeni
                vizörle çıkış → kalkış)
KURGU (ölçülen) 169 s (−11 s ≈ 1 sahne eksik) · üç mercek de AYNI kurguyu
                ölçtü (2:49) · S0-S14 plan ızgarasına SANİYESİ SANİYESİNE
                oturuyor (çatlak 01:03 = plan S6 2.8 s ✓ · "Marker four"
                0:55 = S5 ✓ · köpük 01:50 = S11 ✓) · SON BLOK BOZUK:
                S15 kurguda YOK, 2:30-2:39'da S17 malzemesi (merdiven
                tırmanışı) S16'dan ÖNCE duruyor, kalkışın kendisi
                (ateşleme + koni + yükseliş) hiçbir mercekte görünmüyor
DERS 65 NOTU    dört raporun dördü de FILM: (not supplied) yazdı — kural TUTTU
DERS 75 NOTU    senaryo merceği malzeme kapısını koştu ve yazdı — yama TUTTU
```

---

## 🗺️ KURGU ↔ PLAN SAHNE EŞLEMESİ

Üç merceğin timecode'ları plan ızgarasıyla birleştirildi (mercek
numaralandırmaları kendilerine ait; bu tablo plan numarasıyla konuşur):

| Kurgu | Mercek gözlemi | Plan sahnesi | Uyum |
|---|---|---|---|
| 0:00-0:10 | sondaj ünitesi + "7 dk / 22 dk" | S0 HOOK | ✅ |
| 0:10-0:40 | koşu bloğu | S1-S2-S3 | ✅ (mercekler tek sahne saydı; S3 güneş yutuluşu ayrı okunmadı) |
| 0:40-0:50 | çömelme, "rüzgâra direnme" | S4 TEMAS | ✅ (bkz. aşağıda fizik notu) |
| 0:50-1:00 | "Marker four. You are on the line." | S5 | ✅ |
| 1:00-1:10 | düşüş, çatlak 01:03 | S6 | ✅ takvim tuttu |
| 1:10-1:20 | "Visor breach…" | S7 | ✅ |
| 1:20-1:40 | yoğun tozda yürüyüş | S8-S9 | ⚠️ S8 soluk disk ve S9 sapma krizi/çatlak uzaması hiçbir mercekte AYRI okunmadı; S9 repliği ("forty meters") hiçbir raporda yok |
| 1:40-1:50 | tüp çıkar, "A full seal…" | S10 | ✅ |
| 1:50-2:00 | köpük püskürtme, yüz silinir | S11 🎯 DORUK | ✅ kurguda VAR |
| 2:00-2:10 | kör yürüyüş, "180 meters. Five degrees right." | S12 | ✅ |
| 2:10-2:19 | kapak halkası, "Two meters…" | S13 | ✅ |
| 2:20-2:29 | hava kilidi, kask bütün çıkar | S14 | ✅ |
| — | — | **S15 PENCERE (ÇEHOV 4 + "forty hours")** | ❌ **KURGUDA YOK** |
| 2:30-2:39 | roket merdiveni tırmanışı | S17 malzemesi | 🚨 **YANLIŞ SIRADA** (S16'dan önce) · kalkış görünmüyor |
| 2:40-2:49 | yeni şeffaf vizörle çıkış, hab yanında | S16 | ✅ kendi slotunda |

**Sonuç:** Üç merceğin "uzamsal çöküş / üç çelişkili final" dediği şeyin
tamamı iki kurgu hatasıdır: **eksik S15 + yer değiştirmiş S16/S17.**
Mekânlar halüsinasyon değil — hava kilidi, 8 m yarım silindir hab
("corrugated tube") ve 400 m ötedeki 14 m çıkış aracı ("rocket") üçü de
planlı, ayrı yapılar. → **DERS 81'in kaynağı.**

---

## 🔎 FLAGS FOR DOCUMENT CHECK — CEVAPLAR (plan dosyasından)

> Mod V raporları soru sordu; cevaplar plan/bible'dan verildi. Bu bölüm
> kart D/E/E2 adım 2'dir ve koşunun en değerli çıktısıdır.

### 🧍 KARAKTER_QA + 🧩 MANTIK_QA ortak sorusu

**1. "Kask 01:56'da opaklaşıyor — kum için polarize mi oluyor?"**
HAYIR — polarizasyon değil, **filmin doruğu:** FOAM SCHEDULE (§0.12) köpüğün
S11 0.5-5.5 s'de vizörün TAMAMINI mat açık gri, pürüzlü, tam opak kabukla
örtmesini şart koşar; yüz S11-S14 arası GÖRÜNMEZ ve bu tasarımdır (§0.15
rubrik uyarısı bunu kelimesi kelimesine öngörmüştü). Kadın nefes için kendi
görüşünü mühürlüyor — "prop swap" bulgusu ve ona bağlı skor kayıpları
(Ekipman 3 · Kostüm-Prop 3) **tasarımın cezasıdır, DÜŞER.**
⚠️ Kalan üretim sorusu: iki mercek de kabuğu "featureless opaque shell"
diye tarif etti — planın pürüzlü KÖPÜK dokusu okunmamış olabilir; gerçek
VIDEO_QA koşusunda S11 klibinde doku kontrol edilir.

**2. "Çatlak vizör 02:40'ta bütün — silinen hasar mı?"**
HAYIR — **S16'nın YENİ ŞEFFAF VİZÖRÜ** (beş durumlu kask takvimi §0.12;
köpüklü eski vizör tezgahta kalır). AMA bulgu başka bir kimlikle **AYAKTA
KALIR:** yedek vizörü kuran Çehov sahnesi **S15 kurguda yok** — kurulumsuz
ödeme, izleyiciye (ve merceğe) "silinen hasar" olarak görünür. Devamlılık
ihlali değil, **kurgu hatası.** → DERS 81.

**3. "Sığınak silo mu, roket mi, oluklu tüp mü?" / "Roket buraya ait mi?"**
ÜÇÜ DE PLANLI ve AYRI: ribli koyu gri 8 m yarım silindir hab (= "silo" ve
"corrugated tube" aynı yapının iki okuması) · 2.5 m hava kilidi + 3 m yaşam
modülü içeride · 14 m çıkış aracı hab'ın 400 m solunda. Roket finale aittir
(S16 fon + S17 kalkış). Planlı sıra: S13 kapak → S14 hava kilidi → S15
pencere → S16 yeni vizörle çıkış → S17 kalkış. Kurguda S15 yok ve S17
malzemesi öne alınmış — "üç çelişkili final" bulgusunun kökü bu.
⚠️ Açık kalan: MANTIK'ın "kare içi kare" sorusu değil ama "square paneled
airlock ↔ round exterior" uyumsuzluğu — iç mekân planlıdır (sıcak beyaz
panel, çıplak duvar), geometri uyumu gerçek VIDEO_QA koşusunda bakılır.

### 📖 SENARYO_QA soruları

**1. "Amaçlanan final mekânı hangisi?"**
S17 KALKIŞ: kadın gemiye biner (2.5 s), ateşleme 5.5 s, kalkış 7.0 s, held
frame — araç kadraj üstünde parlak nokta. Film hava kilidinde bitmez.
**"S13-S14'ü kes (roket + tüp)" reçetesi REDDEDİLİR** — o iki klip filmin
planlı finali (S17) ve ödeme sahnesidir (S16). Doğru düzeltme kesmek değil:
S15'i eklemek + S16/S17 sırasını düzeltmek + kalkışın ekranda olduğunu
doğrulamak. (Stone Sky "S4'ü kes" emsalinin aynısı: mod V, kurgu hatasını
içerik zaafı olarak raporladı — DERS 72/73 örüntüsü.)

**2. "'Visor breach' repliği planda var mı?"**
EVET, birebir: S7 — "Visor breach. Your oxygen margin is halved." (§0.11).
Replik "görüneni anlatmak" için değil, **SAYAÇ A'nın (oksijen — tamamen
sesli kanal) ikinci okuması** için var: ekranda hiçbir gösterge olmadığı
için marj ancak sesle daralabilir. Kesme reçetesi REDDEDİLİR; ilk iki
kelime pahasına sayaç korunur.

**3. "Camera-carrier / tek seçim vizör tamiri" bulgusu**
CENTRAL CHOICE planda S11'dir ve **kurguda VAR** (01:50; merceğin kendisi
onu doruk ve "en iyi an" seçti). Merceğin okuyamadığı şey tamirin BEDELİ:
köpük çatlağı değil GÖRÜŞÜ mühürler — bu ancak S10 repliği + S12 kör
yürüyüşle birlikte "kendini kör etme takası" olarak okunur. Mercek kör
yürüyüşü gördü ama takas olarak adlandırmadı; final bloğu bozuk olduğu
için bedelin taşındığı koda da (S15 köpüklü kask tezgahta) ekranda yoktu.
Karakter 4 ve Tema 4 skorlarının önemli kısmı **kurgunun puanı.**

### 🧩 MANTIK_QA — cevap istemeyen ama belge karşılaştırmasının bulduğu şeyler

**4. `THE COUNTER: NONE` — plan DÖRT sayaç tanımlıyor (§0.9).**
DERS 78'in yeni vakası, ama bu kez YARIM: mercek iki sayacı fark etmeden
OKUDU — Sayaç A'nın (oksijen) rakamlarını "NUMBERS" listesine yazdı ve
Nicelik'e 6/10 verdi; Sayaç B'yi (çatlak) yıpranma zaman çizelgesi olarak
doğum anıyla (01:03) izledi. Sayaç C (görüş mesafesi 5 m → 3 m) ve
Sayaç D'nin zincir mantığı (11 işaretçi) hiç okunmadı; çatlağın S9 uzaması
(9 → 12 cm) hiçbir raporda yok. Rubrik dipnotundaki DERS 78 kuralı
("NONE satırını FLAGS'e soru olarak taşı") bu koşuda UYGULANMADI —
çalıştırma kaydına işlendi.

**5. Out-of-scope satırı: "geniş planlarda toz rüzgâra KARŞI akıyor."**
Plan tek yön şart koşar: SAĞ→SOL, 15 m/s, 18 sahnenin 18'inde (STORM
BEHAVIOR LOCK + AXIS LOCK). Ters yönlü akış varsa gerçek eksen ihlalidir —
gerçek VIDEO_QA koşusunda doğrulanacak, şimdilik aday bulgu.

**6. "Crouches, braces against wind" (0:40-0:50).**
Filmin fizik imzası fırtınanın İTMEMESİDİR (kumaş kıpırdamaz, kimse
sendelemez). Plandaki S4 çömelmesi refleks TEPKİ ÇAPASI'dır — kuvvet değil.
Merceğin "rüzgâra direnme" okuması yorumdur; ekranda kumaş çırpıyorsa ihlal
olur, bu da klip düzeyinde ancak VIDEO_QA doğrular. Aday bulgu.

### 🧍 KARAKTER_QA — pasaportun bible ile karşılaştırması (mod V bilemezdi)

| Pasaport ne gördü | Bible ne diyor | Sonuç |
|---|---|---|
| **"Backpack"** | "**No back-mounted tank, no hose, no cable**" | 🔴 **DERS 79'un ÜÇÜNCÜ vakası** (Unbroken City · Starless Circle · burada) — D79 cümlesi 06.08'de yazıldı, aynı gün yazılan bu filmin negatif çekirdeğine GİRMEDİ (D77 mekanizması) |
| "**Dual** headlamps" | "**a single** integrated helmet lamp" + ışık envanteri §0.13 kapalı liste | 🟠 ihlal — ikinci lamba envanterde yok |
| "Dark canister on **right** thigh" | "On her **LEFT THIGH** … sealant canister" | 🟠 ayna çevirmesi adayı (rubriğin kendi imza hatası: model sağ/solu serbestçe çevirir) — klip doğrulaması gerekir |
| "Olive skin … dark eyebrows" — yanık izi YOK | "a faint old burn mark along her **left jaw**" + sabit yıpranma izleri (incik tozu, sağ eldiven sürtmesi, sol uyluk aşınması) | 🟠 sabit izler yine üretilmemiş — D79 ikinci mekanizmasının tekrarı |

---

## 📊 KATEGORİ SKORLARI

**🔧 Teknik:** 🚨 GEÇERSİZ — girdisiz koşu (video yüklenmedi). Tabloya
girmez. → **DERS 80.** Tekrar koşusu: gerçek kurgu dosyası + §0.15 SPEC.

**📖 Senaryo (Ⓥ ŞARTLI):** Kanca 5 · Önerme 6 · Yapı **4** · Karakter **4** ·
Tema **4** · Diyalog 5 · Duygu Yayı **4** · Final **3** · Özgünlük 4 ·
Tutundurma 5 → **4.0/10** · REVISE STRUCTURE — Yapı/Final/Duygu Yayı büyük
ölçüde bozuk son bloğun (kayıp S15 + sıra) puanı.

**🧩 Mantık:** Fizik 6 · Sayaç **N/A** · Coğrafya **3** · Zaman-Işık 4 ·
Kostüm-Prop **3** · Nedensellik **3** · Nicelik 6 · Kurulum 5 → **4.0/10**

**🧍 Karakter:** Yüz 6 · Saç-Beden 6 · Kostüm 4 · Yıpranma **3** ·
Ekipman **3** · Kesme **3** · Sayı N/A · Ses N/A → **4.0/10** · DRIFTS

> ⚠️ Kesişen bulgular birleştirmede TEK sayılır (kart E2 adım 5): köpük
> kabuğu (Ekipman 3 ↔ Kostüm-Prop 3) ve yeni vizör (Yıpranma 3 ↔ Minor)
> iki tabloda aynı olayın iki dilidir. İkisi de belge kontrolünde büyük
> ölçüde düştü/kurguya devredildi — yani üç merceğin 4.0'ları filmin
> üretim kalitesinden çok **kurgusunun** notudur.
> ⚠️ Sayı-Ayrışma N/A + tek karakter: bu film, D69 klon serisinden sonra
> **klonsuz çıkan ilk çok-mekânlı koşu** — planda biniş/iniş HAREKETİ yine
> de var (S17 2.5 s'de gemiye girer); gerçek VIDEO_QA koşusunda o an kare
> kare taranmalı.

---

## 🚪 KURGU KAPISI — teslimden önce koşulmalıydı (DERS 70/72 → 81)

| Ölçüt | Plan | Kurgu | Sonuç |
|---|---|---|---|
| Klip sayısı = SCENE COUNT | 18 | ~17 | ❌ 1 eksik (S15) |
| Süre = RUNTIME ±2 s | 180 s | 169 s | ❌ −11 s |
| Ekran metni 0.0 sn | 0 | 0 gözlendi | ✅ (ilk kez — Unbroken City/Starless Circle'daki yanık kart zinciri burada YOK) |
| CENTRAL CHOICE kurguda | S11 | VAR (1:50) ve püskürtme ekranda | ✅ |
| **SIRA = plan sırası** (v2 · D81) | S14→S15→S16→S17 | S14→**S17**→**S16**, S15 yok | ❌ |
| **Kurulum sahneleri kurguda** (v2 · D81) | ÇEHOV 4 = S15 | YOK | ❌ |

**Dört maddelik eski kapı bile bu kurguyu durdururdu (iki ❌); yeni iki
madde (sıra + kurulum) üç merceğin bütün "yapısal çöküş" bulgularını
üretimden önce yakalar.**

---

## 🧭 SONUÇ VE SONRAKİ ADIM

```
1. 🔴 KURGU ONARIMI (üretim değil, kurgu — ucuz):
   a. S15 klibi kurguya eklenir (üretildiyse; üretilmediyse üretilir —
      Çehov 4 + "forty hours" repliği + köpüklü kaskın tezgahta kalışı).
   b. S16 ↔ S17 sırası düzeltilir: çıkış ÖNCE, kalkış SONRA.
   c. 2:30-2:39 klibi doğrulanır: kalkış (ateşleme 5.5 s, koni, yükseliş)
      klipte var mı? Yoksa S17 yeniden üretilir (LAUNCH LOCK §0.12).
2. 🔴 VIDEO_QA gerçek kurgu dosyasıyla yeniden koşulur (girdisiz koşu
   geçersiz — DERS 80). SPEC §0.15'ten kopyalanır → MOD D.
   Özel bakılacaklar: S11 köpük DOKUSU (pürüzlü köpük mü, düz kabuk mu) ·
   toz akış yönü (SAĞ→SOL ihlali adayı) · S4'te kumaş kıpırdaması ·
   S17 biniş anı klon taraması (D69) · kask lambası TEK mi.
3. 🟠 DERS 79 negatif çekirdek cümlesi ("flat back silhouette…") bu filmin
   36 promptuna eklenir; sırt ünitesi görünen klipler yeniden üretim adayı.
4. 🟠 Tüp uyluğu SOL mu SAĞ mı — klipten doğrulanır (ayna çevirmesi adayı).
5. ⚠️ S8/S9 doğrulaması: soluk disk anı ve "forty meters" repliği kurguda
   var mı? İki mercek de 1:20-1:40'ı tek blok okudu.
6. Kurgu onarımından sonra SENARYO_QA MOD D ile tekrar koşulur — mevcut
   Ⓥ satırı büyük ölçüde kurgunun puanı.
7. Yeni dersler: DERS 80 (medya kapısı) · DERS 81 (kurgu kapısı v2: sıra +
   kurulum). Tekrar kayıtları: DERS 78 (yarım vaka) · DERS 79 (3. vaka) ·
   DERS 77 (mekanizma: aynı gün yazılan ders plana akmadı).
```
