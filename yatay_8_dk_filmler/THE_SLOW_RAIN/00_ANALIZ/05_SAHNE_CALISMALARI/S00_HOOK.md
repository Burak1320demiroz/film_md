# 🔬 S00 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · THE_SLOW_RAIN

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> sahneye düşen satırları. Bu dosya bitmeden bu sahnenin promptu yazılmaz.

---

## 🪪 KİMLİK

```
SAHNE:      S00            BAŞLIK: İLK DAMLA
BÖLÜM:      THE_SLOW_RAIN_BOLUM_1.md
ZAMAN:      0,0 s → 10,0 s       ⛔ FORMÜLLE [D122]: hook S0 klibin içinde → n × 10 s (klip 10 s VARSAYIM, araçtan ölçülür)
VURUŞ:      açılış imajı · S0 SORUSU               B5 SATIRI: İSTEK öncesi: bakımcı işte, damlayı yakalar
⭐VİRAL:    evet  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Eldiven kalkık, ilk yağmur damlası yavaş koşu temposunda (Dünya yağmurunun ~üçte biri) inip eldivene değer, beyaz kuru-kar yakası kalkar
BAŞTA:           eldiven kalkık, damla iniyor
SONDA:           damla eldivende buharlaşmış, beyaz puf düşüyor; el hâlâ yukarıda
⛔ KLİP İÇİ DEĞİŞİM: YOK [VAR / YOK]
   VAR ise: ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687). İki seçenek:
   ① değişimi sahne SINIRINA taşı  ② ARA DURUM YASAĞI cümlesini prompta yaz
   Seçim: —   Gerekçe: hareket var (damla/puf/el), durum değişimi yok — puf bir olay, kabuk/ışık durumu değişmiyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: ilk kullanım
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           75 mm     MESAFE: 1.6 m     YÜKSEKLİK: 1.55 m
ÖLÇEK:          CU        AÇI TİPİ: eye-level close-up, frontal · az 0°
KADRAJ ENİ:     0.77 m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne kask + kalkık eldiven 0.45 m
                          Sığıyor mu: ✅   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: 2250 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]   · damla bilye 0,01 m → 50 px (sayılı, seyrek)
ÖNCEKİ SAHNEYLE: — (ilk sahne)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 × 48 (her karede aynı)
AYRIM EKSENİ:   tek figür — soluk gri giysi ↔ koyu zemin/koyu kanat; teal göğüs bandı   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    damla (ilk) · eldiven        ÇIKAN NESNE: —
TAŞINAN NESNE:  kanat takımı (sırtta, kadraj dışı) → S1
⛔ BİÇİM KİLİDİ: kask (düz pane + kalın koyu çerçeve) + eldiven segmentli — referans paketi YOK (sahip); ilk onaylı kareler referans [D153/D154]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      amber pus dolgusu   (ışık takvimi: dış sabit pus dolgusu / iç 3200 K sabit · monotonik: değişmez; iç↔dış geçişleri OLAY)
PALET:     dış amber pus · soluk gri giysi · koyu zemin   ⛔ önceki sahneyle aynı olamaz [KURGU_RITMI §2 örüntü kırıcı] — ölçek değişti
SES:       tek diegetik: damlanın 'tok'u + kısa tıslama; müzik yok
MÜZİK:     yok — ilk 2 s tek diegetik ses; müzik en erken S1
FİZİK:     damla ~3 m/s, puf 0,5 m/2 s   (kart §3.9: sıcak yüzeyde puf 0,5 m / 2 s · rüzgâr yok · gölge sığ · güneş diski 0)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (film sessiz tasarımlı)
İŞLEV:     —
AĞIZ:      — ağız kapalı, konuşma yok
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       kaş kalkar, göz damlayı izler; ilk pufta göz kırpar
HAREKET:   damla iner, beyaz puf kalkıp kar olarak düşer; ikinci damla yolda
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D157 · D192 | novum taşıyıcı damla × eldiven; damla sayısı/boyu/hızı sayıyla | üçüncü satır: 'One large drop, the size of a marble, lands on the raised glove and flashes into a white puff that falls back as dry snow within two seconds; a few more drops descend at a slow jogging pace behind it.' |
| HEALING GROUND ② (kopuk eldiven) | kol gövdeye bağlı | 'her right glove raised palm-up at chest height, the sleeve running down into the lower left of frame, her helmet and shoulders behind the hand' |
| HOOK §2.2 · §2.6 | hareketin ortasında; NEREDE→KİM→NE YANLIŞ→TEPKİ | imaj: eldiven zaten kalkık, damla eldivene bir karış; video 0,0 s'de damla iner |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U-1 damla hızı/biçimi | pozitif sayı cümlesi + S0 iptal kapısı (kare kanıtı: iki ardışık karede damla yarım kadraj) | ✅ |
| 2 | ⚠️ | U-sarı-1 eldiven insert | kol kadraja bağlı yazıldı | ✅ |
| 3 | ⚠️ | U-sarı-6 yüz CU kimlik | ≤3 öznitelik; çevre çapası: 'the base door frame behind her' | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır — tek insan, eldiven, damla   sınıf: —
NÖTR TARİF:  'the glove stays raised for the whole take' pozitif   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: 'the glove stays raised for the whole take'
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
✅ önceki sahneyle ardışık çift bant içi (ya da şok gerekçeli)
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ — THE_SLOW_RAIN_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```

## 🔗 KART BAĞI · SON 3 s · ÖLÜ SAHNE BEŞ SORUSU (`KARAKTER_KARTI` §10 · `SAHNE_DOLULUGU` §6)

```
KART BAĞI:        İLK↔SON (eldiven kalkar) · ROL
İZLEYİCİ CÜMLESİ: YÜZ: kaş kalkar, göz damlayı izler (S0'da tek yüz değişimi) · HAREKET: damla iner, beyaz puf kalkar; elini kaldırıp bekliyor — damlanın nereye ineceğini bilmek istiyor
TAŞIYAN KANAL:    BAKIŞ + EL   TASK ONLY: hayır
SON 3 s:          keeps the glove up, a second drop is halfway down toward it
① FİİL   süreç ✅ (damla iner/puf kalkar, el tutulur)
② DİRENÇ ✅ (ikinci damla yolda)
③ TEK KİLİT ✅ · TIMELINE ≤3 satır
④ SINIR  ✅ (End/Start sınır satırı sahne haritasında)
⑤ SAAT   ✅ (inen damlalar (kenarda, sabit oran))
```
