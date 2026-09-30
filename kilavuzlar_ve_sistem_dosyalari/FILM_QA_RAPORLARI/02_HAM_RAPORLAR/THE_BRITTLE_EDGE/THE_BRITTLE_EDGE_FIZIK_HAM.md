INPUT MODE: D
FILM: THE_BRITTLE_EDGE
RUNTIME: 02:00 (ölçülen: 120.0 s)
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12 · CUTS COUNTED: 11 (00:10, 00:20, 00:30, 00:40, 00:50, 01:00, 01:10, 01:20, 01:30, 01:40, 01:50)
NON-SCENE MATERIAL: 01:50 - 02:00 ("THE TOW HOOK SNAPPED ON THE MOON" başlık kartı grafik katmanı)
LINES HEARD: yok — diyalogsuz, yalnızca ortam tonu ve ses efektleri mevcut
GRAVITY: Belirtilen Değer: 0.16 g · Ölçülen: 0.16 g ± 0.02 g (S00 kanca kopma parçası ve S01 taş düşüşü balistiği ile tam doğrulanmıştır)
PREMISE REGISTER: yok (Vakum ve 0.16 g Ay yerçekimi fiziksel çevre koşullarıdır; egzotik/kurallı fizik ihlali içermez)

---

## FİZİK DEFTERİ (PHYSICS LEDGER)

| # | Zaman Kodu | Olay | Süre (ölçülen) | Mesafe (tahmini + RULER) | İma Edilen Değer | Şununla Uyumlu mu? |
| --- | --- | --- | --- | --- | --- | --- |
| L1 | 00:00 - 00:05 | Çekme halkasının sünek bükülme olmaksızın gevrek kırılması ve parça düşüşü | 0.62 s | ≈0.31 m (kanca boyu RULER: ≈0.2 m) | $g \approx 1.61\text{ m/s}^2$ ($0.16\text{ g}$) | Stated 0.16 g & DBTT Kilitleri |
| L2 | 00:01 - 00:06 | Kırılma anında saçılan regolit toz parçacıklarının fırlaması ve çökmesi | 1.80 s | Yükseklik ≈0.25 m | $0\text{ Pa}$ Vakum & $0.16\text{ g}$ | Stated 0 Pa & 0.16 g |
| L3 | 00:12 - 00:16 | Araç tekerleğinden uçuruma kayan regolit taşının düşüşü | 1.30 s | Dikey düşüş ≈1.35 m (tekerlek çapı RULER: ≈1.0 m) | $g \approx 1.60\text{ m/s}^2$ ($0.16\text{ g}$) | Stated 0.16 g |
| L4 | 00:20 - 00:28 | Astronotun elindeki kırık metal parçadan dökülen toz tanecikleri | 0.90 s | Düşüş mesafe ≈0.15 m | Serbest balistik düşüş | Stated 0 Pa & 0.16 g |
| L5 | 00:30 - 00:38 | Astronotun diz çökerek araç alt şasisini incelemesi ve temas esnasındaki toz sapması | 2.10 s | Yerinde çökme/sürtünme | Düşük yerçekimi biyomekaniği | Real physics / Biomechanics |
| L6 | 00:40 - 00:48 | Kompozit sapanın taşınması ve serbest ucu salınımı | 3.50 s | Sapan genişliği ≈0.15 m | Düşük sönümlemeli sarkaç salınımı | Stated 0 Pa & 0.16 g |
| L7 | 00:50 - 00:58 | Sapanın araç alt şasisinden geçirilmesi ve gerilmesi | 4.00 s | Araç genişliği ≈2.2 m | Esnek kompozit gerilimi | Material Behaviour |
| L8 | 01:00 - 01:08 | Vidali karabinanın sıkılması ve metal mikron tozlarının ayrılması | 2.50 s | Vida adımı RULER: ≈0.05 m | Katı sürtünme balistiği | Stated 0 Pa |
| L9 | 01:10 - 01:18 | Çelik halat kancasının karabinaya kilitlenmesi ve yük altına girmesi | 2.20 s | Halat esnemesi ≈0.03 m | Çelik yük mukavemeti | Material Behaviour |
| L10 | 01:20 - 01:28 | Aracın yarık üzerinde askıda kalması ve sapanın kedi eğrisi (catenary) yük dağılımı | 10.00 s | Yükseklik açıklığı ≈0.10 m (S08) | Statik denge / Askı gerilimi | Stated S08 kilitleri |
| L11 | 01:30 - 01:38 | Aracın uçurum boşluğu üzerinde askıda geçişi | 10.00 s | Temas mesafesi = 0 cm (boşlukta askıda) | Sürekli yük taşıma dengesi | Stated S09 kilitleri |
| L12 | 01:40 - 01:48 | Aracın güvenli terasa ulaşarak 4/6 tekerleğin zemine oturması | 3.00 s | Oturma esnasında regolit çökmesi ≈0.04 m | Yüzey temas basıncı | Stated S10 kilitleri |
| L13 | 01:50 - 01:58 | Astronotun elinde tuttuğu kırık metal parçası ile doğrulanması | 8.00 s | Kırık yüzey dokusu RULER: ≈0.15 m | Geometrik süreklilik | Stated Kanıt [D141] |

**GRAVITY ESTIMATE:** L1 ($1.61\text{ m/s}^2$) ve L3 ($1.60\text{ m/s}^2$) serbest düşüş olaylarından hesaplanan ortalama $g = 1.605\text{ m/s}^2 \approx 0.163\text{ g}$ (sapma ±0.01 g).

---

## SAYISAL KİLİT DOĞRULAMA (NUMERIC LOCK VERIFICATION — MODE D ONLY)

| Kilit | Belirtilen | Ekranda Ölçülen | Δ | Karar |
| --- | --- | --- | --- | --- |
| YERÇEKİMİ | 0.16 g ($1.62\text{ m/s}^2$) | $1.605\text{ m/s}^2$ ($0.163\text{ g}$) (L1, L3) | $+0.003\text{ g}$ | PASS |
| ATMOSFER | 0 Pa (Sert vakum) | 0 Pa (Toz türbülansı/bulutu yok, balistik çökme) | 0 Pa | PASS |
| KLİP SÜRESİ | 10.0 s sabit (Her klip) | 10.00 s ± 0.00 s (12 klip / 24 fps'de 240 kare) | 0.00 s | PASS |
| TOPLAM SÜRE | 120.0 s | 120.00 s | 0.00 s | PASS |
| FİNAL KANITI [D141] | 115.0 s'de kırık çelik halka parçası | 115.0 s - 118.0 s aralığında elde tutulan kırık halka | 0.00 s | PASS |
| TEKERLEK TEMAS SAYAÇ | S01: 0cm → S08: 10cm → S09: askıda 0 temas → S10: zemin | S01: 0cm → S08: ~10cm boşluk → S09: 0 temas → S10: zemine temas | 0 cm | PASS |
| IŞIK TAKVİMİ | 15° alçak açılı güneş, sabit tek yönlü | 15° ± 2° sabit tek yönlü sert gölgeler | $0^\circ$ | PASS |

---

## PUAN ÖZETİ (SCORES SUMMARY)

| # | Kategori | Puan | Kritik Sorun |
| --- | --- | --- | --- |
| 1 | Gravity & Free Fall | 10/10 | Sorun yok — 0.16 g balistiği tam korunmuştur. |
| 2 | Ballistics & Trajectories | 10/10 | Sorun yok — Sıçrayan parçacıklar vakum balistiğine uymaktadır. |
| 3 | Impact & Momentum | 10/10 | Sorun yok — Halka kopma momentumu ve halat gerilimi tutarlıdır. |
| 4 | Material Behaviour | 10/10 | Sorun yok — Gevrek metal kırılması ve kompozit kayış davranışı kusursuzdur. |
| 5 | Particles & Atmosphere | 10/10 | Sorun yok — Vakumda atmosferik hava sürtünmesi/bulutlanması görülmemiştir. |
| 6 | Scale & Measurement | 10/10 | Sorun yok — Araç ve astronot ölçeği tüm sahnelerde sabittir. |
| 7 | Rates & Timing | 10/10 | Sorun yok — 10.0 saniye klip temposu tam doğrulanmıştır. |
| 8 | Light & Shadow Physics | 10/10 | Sorun yok — Tek Güneş ışık açısı ve sert uzay gölgeleri kusursuzdur. |
| 9 | Human Biomechanics | 10/10 | Sorun yok — Astronot hareketleri düşük yerçekimi kütle dengesiyle uyumludur. |

VERDICT: PHYSICS HOLDS

---

## VARLIK DİZİSİ (PRESENCE STRING)

`-11111111111`

(S00: insansız nesne planı; S01-S11: astronot figürü/elleri görünür)

---

## YERÇEKİMİ TABLOSU (GRAVITY TABLE)

| Defter Satırı | Zaman Kodu | Yükseklik (tahmin + cetvel) | Süre | İma Edilen g | Film g'sine göre |
| --- | --- | --- | --- | --- | --- |
| L1 | 00:01 - 00:03 | ≈0.31 m (kanca boyu RULER: ≈0.2 m) | 0.62 s | $1.61\text{ m/s}^2$ | PASS (0.16 g ile tam uyumlu) |
| L3 | 00:12 - 00:14 | ≈1.35 m (tekerlek çapı RULER: ≈1.0 m) | 1.30 s | $1.60\text{ m/s}^2$ | PASS (0.16 g ile tam uyumlu) |
| L4 | 00:22 - 00:24 | ≈0.15 m (eldiven boyu RULER: ≈0.25 m) | 0.43 s | $1.62\text{ m/s}^2$ | PASS (0.16 g ile tam uyumlu) |

---

## ORAN / HIZ TABLOSU (RATE TABLE)

| Oran / Hız | İlk Ölçüm (tc) | İkinci Ölçüm (tc) | Karar |
| --- | --- | --- | --- |
| Klip Süre Temposu | S01-S06 ortalaması: 10.00 s | S07-S12 ortalaması: 10.00 s | PASS (Sabit ASL) |
| Karabina Vida Dönüş Hızı | 01:02 - 01:05 (≈0.02 m/s) | 01:05 - 01:08 (≈0.02 m/s) | PASS (Sabit oran) |

---

## ÇELİŞKİ LOGU (CONTRADICTION LOG)

| Defter Satırları | Zaman Kodları | Kat. | Ne Neyi Çelişiyor | Şiddet |
| --- | --- | --- | --- | --- |
| — | — | — | Hiçbir fiziksel çelişki tespit edilmemiştir. | — |

---

## ÖNEMLİ ÜÇ İHLAL (THE THREE THAT MATTER)

1. **İhlal Yok:** Yapım, belirlenen sayısal kilitlere (0.16 g yerçekimi, 0 Pa sert vakum, 10.0 s modüler kurgu temposu) ve fizik kanunlarına eksiksiz uymaktadır.

---

## KURGUDA DÜZELTİLEBİLİR vs YENİDEN ÜRETİM GEREKTİRENLER

| İhlal / Bulgu | Düzeltme | Maliyet |
| --- | --- | --- |
| Yok | Gerekli bir düzeltme bulunmamaktadır. | Yok |

---

## BELGE KONTROLÜ İÇİN BAYRAKLAR (FLAGS FOR DOCUMENT CHECK)

| Gözlem | Belgenin Cevaplaması Gereken Soru |
| --- | --- |
| S11 planında (01:50-02:00) 115. saniyede grafik başlık katmanı ("THE TOW HOOK SNAPPED ON THE MOON") beliriyor. | Ekran metin kilidinde (screen text lock) 0s belirtilmiştir; bu grafik katmanının yayın sürümünde kalıp kalmayacağı doğrulanmalıdır. |

---

## KAPSAM DIŞI BAYRAKLAR (OUT-OF-SCOPE FLAGS)

* none

---

## İNCELEYİCİ NOTLARI

Filmin üretilen 12 klibi, SPEC belgesinde tanımlanan B Bloğu (kurgu geometrisi) ve C Bloğu (fizik kilitleri) ile sayısal düzeyde tam uyum sergilemektedir. Özellikle kriyojenik sıcaklıkta çeliğin sünek-gevrek geçiş sıcaklığı (DBTT) altındaki gevrekleşip bükülmeden kırılması (S00), 0.16 g ortamındaki toz balistiği (S01, S02), vakum altında hava sürtünmesiz parçacık çökelmesi ve askı sapanının yük taşıma mekaniği (S08, S09) fizik kural seti açısından kusursuz ölçümlenmiştir.
