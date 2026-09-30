INPUT MODE: V
FILM: (not supplied)
RUNTIME: 02:05
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: none (mode V)
SCENES OBSERVED: 14 · CUTS COUNTED: 13 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 01:59 - 02:05 (Başlık ve grafik bitiş kartı)
PRESENCE STRING: -1111111111111
LINES HEARD: none — room tone present
SETUPS REGISTERED: 13
LOCKOFF HELD: 11 / 14 clips

## SETUP LEDGER

S1 | 00:00 | - | ECU / Düşük Açı / Normal / Çeki kancası yuvası | A | MATCH | Kanca yuvası | 0
S2 | 00:05 | - | WS / Düşük Açı / Geniş / Araç ön görünümü | B | MATCH | Ön tampon | 0
S3 | 00:09 | - | WS / Göz Hizası / Geniş / Uçurum kenarı ve araç | C | MATCH | Uçurum kenarı | Hafif kayma (00:14)
S4 | 00:19 | - | ECU / Yüksek Açı / Normal / Eldiven ve kırık parça | D | MATCH | Eldivenler | 0
S5 | 00:23 | - | MCU / Göz Hizası / Normal / Gövde ve eldivenler | E | MATCH | Göğüs arması | 0
S6 | 00:27 | - | ECU / Yüksek Açı / Normal / Zemin ve eldivenler | D' | NEAR | Zemin düzlemi | 0
S7 | 00:29 | - | MS / Düşük Açı / Geniş / Astronot ve araç gövdesi | F | MATCH | Yan şasi | 0
S8 | 00:39 | - | WS / Yüksek Açı / Geniş / Astronot ve orange kayış | G | MATCH | Krater kenarı | Yavaş mikro itme (00:44)
S9 | 00:49 | - | MS / Düşük Açı / Normal / Araç tekerleği ve kayış | H | MATCH | Alt şasi | 0
S10 | 00:59 | - | ECU / Göz Hizası / Normal / Karabina ve kilit | I | MATCH | Karabina | 0
S11 | 01:09 | - | MCU / Düşük Açı / Normal / Çelik halat ve kanca | J | MATCH | Çelik halat | 0
S12 | 01:19 | - | EWS / Yüksek Açı / Aşırı Geniş / Asılı araç ve uçurum | K | MATCH | Kayalık çıkıntı | Yavaş sürüklenme (01:32)
S13 | 01:39 | - | WS / Yüksek Açı / Geniş / Araç üstü ve astronot | L | MATCH | Ön tekerlek | 0
S14 | 01:49 | - | MCU / Göz Hizası / Normal / Astronot ve parça | M | MATCH | Tampon köşesi | 0

## SETUP STRING

OBSERVED: ABCDED'FGHIJKLM
PLAN: none (mode V)
DIFFERS AT: none (mode V)

## PRESENCE STRING

-1111111111111

## RHYME PAIR

|  | İlk Kare | Son Kare | Aynı mı? |
| --- | --- | --- | --- |
| Kurulum / Boyut / Açı / Çapa / Değişken | A / ECU / Düşük Açı / Kanca yuvası | M / MCU / Göz Hizası / Tampon köşesi | Hayır |

VERDICT: PAIR FAILS — İlk kare makro kanca kırılma anı iken son kare astronotun kırık parçayı tuttuğu plan ölçeğindedir; kamera konumları ve açılar çakışmamaktadır.

## LOCKOFF VERIFICATION

| Scene | Declared | Observed | Movement starts at | Verdict |
| --- | --- | --- | --- | --- |
| S3 | Locked | Drift | 00:14 | MINOR DRIFT |
| S8 | Locked | Creep | 00:44 | MINOR DRIFT |
| S12 | Locked | Drift | 01:32 | MINOR DRIFT |

## SCORES SUMMARY

| # | Kategori | Puan | Sorun (Ledger satırları ve zaman damgaları) |
| --- | --- | --- | --- |
| 1 | Setup Fidelity | N/A | SPEC sunulmadı (Mode V). |
| 2 | Lockoff Integrity | 6/10 | 🟠 S3 (00:14), S8 (00:44), S12 (01:32) sahnelerinde sabit kadrajda hafif kayma ve mikro push-in gözlendi. |
| 3 | Rhyme Pair | 4/10 | 🔴 S1 (00:00) ve S14 (01:49) kadrajları çakışmıyor; açılış ve kapanış uyumu başarısız. |
| 4 | Return Consistency | 6/10 | 🟡 S4 (00:19) ve S6 (00:27) tekrarlarında açı ve ölçek hafifçe sapıyor. |
| 5 | Cluster Seams | N/A | Dikişli split-shot bulunmuyor. |
| 6 | Angle Arc & Deliberate Shocks | 7/10 | Planlanmamış aşırı ölçek sıçraması yok, geçişler tutarlı. |
| 7 | Screen Geometry | 7/10 | Ufuk ve nesne konumlandırması sahneler arası dengeli. |

VERDICT: RHYME BROKEN

## THE THREE THAT MATTER

1. **00:00 vs 01:49** — Açılış ve kapanış kareleri aynı kamerayı paylaşmıyor. *Düzeltme:* S14'ü S1 ile aynı A kurulumu açısına getirecek şekilde yeniden üretin.

2. **00:14, 00:44, 01:32** — Sabit durması gereken geniş açılarda mikro sürüklenmeler mevcut. *Düzeltme:* Kurguda yazılımsal stabilizasyon uygulayın.

3. **00:19 vs 00:27** — Yakın el çekimlerinde açı ve mesafe tam eşleşmiyor. *Düzeltme:* Aynı kamera yüksekliğini veren prompt sabitleyicisi kullanın.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* S3, S8 ve S12'deki mikro kaymalar kurguda hafif kenar kırpması ile sabitlenebilir.

* S1 ve S14 arasındaki RHYME PAIR uyumsuzluğu kurguda çözülemez; sahnelerden birinin aynı kamera konumundan yeniden üretilmesi gerekir.

## FLAGS FOR DOCUMENT CHECK

* SPEC belgesi sağlanmadığı için hedeflenen kurulum haritası doğrulanamadı.

## OUT-OF-SCOPE FLAGS

* CONTINUITY: S4 ve S14 sahnelerinde eldiven üzerindeki detaylar ve doku farklılık gösteriyor.

* LIGHTING: S3 ve S12 sahnelerinde gölge açıları hafif tonal sapma sergiliyor.
