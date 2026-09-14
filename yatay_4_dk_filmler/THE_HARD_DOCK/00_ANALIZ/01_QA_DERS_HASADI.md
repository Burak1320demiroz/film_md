# 🧾 THE_HARD_DOCK — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> **Revizyon 11.09.2026:** ilk hasat D197'yi "opak siyah aynalı vizör" diye okumuştu; dersin
> kendisi iki hâlden BİRİNİ seçip tek nitelik cümlesiyle kilitlemeyi ister ve tür kartı §4.1
> D5 "tam şeffaf" der. Kilit BERRAK olarak düzeltildi; D201 ışık kilidi kadrana bağlandı.

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D5 · D79 · D95 · D146 · D197 | vizör kaybolur / aynalı çıkar / kubbe çıkar / iki hâl arasında sıçrar | TEK nitelik: berrak DÜZ panel, görünür koyu-gri çerçeve, 0 ton, 0 ayna, üst kenarda tek parlama çizgisi, yaka halkası görünür, yüz her açıda okunur; "opaque/mirrored" 0 kez | S02-S24 (insanlı 14 sahne) + R1 |
| D139 · ⑮ | kamera arkaya geçince sırt ünitesi doğar | OTS kurulumunda sırt POZİTİF yüzey cümlesi ("one plain smooth panel, and the plain panel is what this shot shows") | S02 S04 S08 S12 S17 S21 S24 |
| D175 | mühürlü filmde uzuv adı deriyi çizdirdi | uzuv adı ±12 kelimede örtü adıyla; anatomi ayrıntısı 0; çıplak deri negatifi ÜÇ bölge | tüm insanlı promptlar |
| D32 · D78 | iki gövdeli karede oran/yön/dizilim bozuldu | V3 yalnız 1 kez; oran cümlesi (1/20 — moth/cathedral) + burun yönü + kesir merdiveni | S06 |
| D104 · YANASMA V5 | kameraya paralel eksende temas battı | kamera PORTA kilitli; gemi kadraja girer, kameraya doğru oturur | S16 S22 S23 |
| B1 (Tidal Hunt) | temas iki sahne ARASINA düştü | temas S22 içinde, saniyesi yazılı (6,0 s) | S22 |
| D198 · D23 | sıfır-g nesne donuk kaldı | kopan panel "continuous rotation … never freezes" | S02 S13 |
| D201 | komşu orbital sahnelerde güneş 120° sıçradı | güneş istasyonun arkasında, eksenin ~30° üstünde, kadraj dışı — kurulum başına sabit cümle; 24/24 aynı | S01-S24 |
| D202 · OYUNCULUK §2-§3 | seçim/bedel bedende okunmadı | ÇAPA ÜÇLÜSÜ (CHOICE S19 · COST S22 · FINAL S24); bakış eli önceler; tereddüt dur-geri gel; omuz iner ve kalır; alışkanlık kırılır | S08 S18 S19 S20 S24 |
| D179 | imaj değişimin SONRASINI yazdı | her IMAGE t = 0; S19 kapak KAPALI · S22 dikmeler UZUN · S20 omuz yüksek | S19 S20 S22 S24 |
| D157 · D73 | novum taşıyıcısı tek kareyi geçmedi | TEK KARE S23 0,0 s: DİKMELER + HALKA karede; iptal kapısı bu sahne | S23 |
| D192 | 1 numaralı risk sıfatla korundu | salınım SAYIYLA: 48 s / 10 s'de ~1/5 daire / hız sabit; pencere 6 s | tüm dış sahneler |
| D82 · D35 · SES §2a | insan sayı söyledi / on-the-nose | 8 replik MACHINE, <5 s, tek konuşmacı, sayı yalnız makinede; insan 0 | S02 S03 S06 S10 S15 S17 S24 |
| D138 · D45 | ölçü etikete döndü | gövdede metre yok (yalnız kamera cümlesi); oranlar halka/kask/avuç/gemi boyu | tüm promptlar |
| D50 · A1 | metin yasağı ekran içeriğini öldürdü | ekran/ibre/yazı 0; kanal: 4 lamba + pencere geometrisi + ses | S02-S24 |
| D34 | özel ad jenerik halüsinasyonu | "MIRA" hiçbir prompta girmez | tüm promptlar |
| KART 10 (Cold Burn S8) | insansız sahne + uzun negatif → yapısal red | insansız 10 sahnede NEGATIVE < 900 kr | S01 S05 S06 S07 S13-S16 S22 S23 |
| D124 | klip süresi varsayıldı | 10 s ⬜ ilk test klibinde ffprobe ile ÖLÇÜLECEK | üretim |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_COUNTED_TURN.md` | T2 DEVAMLILIK | Sahneler arası kurgu sıçramasında ışık yönü değişti. | Güneş istasyonun arkasında, kadraj dışı; kurulum başına sabit cümle (A/E/F arkadan · G önden · iç alçaktan turuncu). |
| `THE_GRAVITY_ANCHOR.md` | T6 FİZİK | Yüzen parçacıklar duraksadı. | Parçacıklara sürekli lineer vektör eklendi. |
| `THE_MIRROR_FAUNA.md` | T4 HİKAYE | AI uyarıları olay örgüsünü değiştirmedi. | AI ve astronot vizyonu S17'de kesin olarak ayrışır. |
| `THE_DRY_ANCHOR.md` | T7 AKSİYON | Yanaşma manevrası fiziksel temas hissettirmedi. | S22'de temas sahne İÇİNDE, saniyeli; dört dikmenin çökmesi rijit-gövde tek harekette; S23 durgunluk kanıtı. |
| `THE_AMBER_LATTICE.md` | T5 ARKA PLAN | Istasyon panelleri sahneler arası boyut değiştirdi. | Referans R3 (sekizgen yaka + kopuk kol screen-left) + ölçek şahidi gemi halkası 1/20; aynı istasyon cümlesi her dış promptta. |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| MÇ (Mekanik Çatışma) | temas anı "çarpışma/crash" okunur | nötr fizik tarifi: seats · struts compress to their stops · settles · no bounce; kelime yasağı yazılmadı [D123]; fırlatıcı/kablo sahnesi tümüyle SİLİNDİ | S22 |
| PK (Politika Kelimesi) | gövde hasarı kelimeleri | "kırık kol" sahnesi SİLİNDİ; gövdeye yönelik fiil 0; betik ⑯ T1 0 · T2 yığılma 0 | — |
| YR (Yanıltıcı Metin) | ekranda anlamsız yazı | ekran YOK; bilgi 4 lamba + pencere + ses | S02-S24 |
| KOMPOZİSYON (rubrik 3c) | yüz yok + el + makro reddedildi (YERCEKIMI S8) | kamera nesne hizasında, tepeden değil; parçalar ard arda derinlikte | S10 · S19 |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        18 satır
QA ARIZASI:         5 adet
RED SINIFI:         4 adet
⛔ EN PAHALI ÜÇÜ:   D146/D197 (vizör geometrisi metinle tutmuyor → R1 zorunlu) · D104/B1 (port-kilitli temas) · D201 (güneş kadranı)
```

