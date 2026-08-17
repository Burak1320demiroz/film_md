# 🌗 THE WRONG SHADOW — Yanlış Gölge

Dikey YouTube Shorts / Reels Production Document
Format: **9:16 (DİKEY)** | Sahne: 6 (Hook + 5 Ana Sahne) | Süre: Her sahne 8 saniye, toplam 48 saniye
Prompt yapısı: Her sahne için **1 görsel promptu + 1 video promptu** (tek versiyon, T2V)
Kaynak: **özgün konsept** — kaynak film yok
Zaman ve yer: **Günümüz · isimsiz kireçtaşı platosu** (promptlarda gerçek yer adı geçmez)
_"Gökyüzünde bir güneş var. Yerde iki güneşin gölgesi."_

---

## 🎯 BU SHORTS'UN TEK İŞİ

Dikey hattın üçüncü günümüz-Dünya konsepti (Winter Line, First Morning'den
sonra). İmkansızlık yine bir nesne değil — bu kez bir **eksik nesne**:

```
GÖKYÜZÜNDE GÖRÜNEN             YERDE OLAN
────────────────────────       ────────────────────────
tek güneş, açık gökyüzü        her nesnenin İKİ gölgesi var
başka hiçbir ışık kaynağı      ikinci gölgeler daha soluk, daha uzun
hiçbir şey hareket etmiyor     ve HEPSİ BİRLİKTE, görünür hızda DÖNÜYOR
```

Bu, THE HALF SKY'ın tersine çevrilmiş hâlidir ve dosya bunu bilerek yapar:
orada gökyüzünün bir bölümü ışığı GERİ VERMİYORDU (bir şey eksikti,
gökyüzünde). Burada yere ışık düşüren ikinci bir kaynak VAR ama gökyüzünde
GÖRÜNMÜYOR (bir şey fazla, yerde). İki film aynı sorunun iki yüzü:
ışık, kaynağını göstermek zorunda mı?

**RİSK SAYIMI: 1 / 9** — yalnız ikinci figür (Kart 4, her filmde).
Su yok · canlı yok · kask yok · ekran yok · diyalog yok · parçacık yok ·
patlama yok · sıfır-g yok. **Ama dürüst kayıt [THE LOW MOON emsali]:
bu filmin gerçek bir numaralı riski kartlarda yok** — ÇİFT GÖLGE
GEOMETRİSİ. Model gölgeyi ışık kaynağından türetir; kaynağı görünmeyen
ikinci bir gölge setini 6 sahnede tutarlı açıyla tutmak, deponun hiç
denemediği bir şeydir. Karşı önlem sayısaldır: her promptta iki gölge
setinin açı farkı DERECE olarak yazılır ve sahneden sahneye tek yönde
kapanır (bkz. GÖLGE TAKVİMİ).

---

## ⚠️ Genel Prodüksiyon Kuralları

1. **SIFIR KESME** — Her video 8 saniyelik, kesintisiz tek çekim. Her sahne
   AYRI üretilir. **Çekim başına TEK sürekli hareket.** [Ders 1]
2. **DİKEY SADAKAT (9:16) + GÜVENLİ ALAN** — Karakter **her karede alt
   1/4'ün dışında**. 1080×1920 karede platform arayüzü alt 484 px'i kapatır —
   `y=1436`'nın altı fiziksel olarak görünmez. Bkz. **📱 GÜVENLİ ALAN HARİTASI**.

   > **Bu konseptin dikeyde olmasının sebebi ve yapısal çelişkisi:**
   > Reveal nesnesi GÖLGE ve gölge yerde yaşar — güvenli alan kuralı ise
   > altı yasaklar (Sinking Hour'un çelişkisinin gölge versiyonu). Çözüm
   > aynı ailedendir: **kamera alçalır (0,5-1,2 m) ve neredeyse yatay
   > tutulur** — gölgeler böylece "karenin dibinde bir leke" değil,
   > kadranın ortasına diyagonal uzanan ÇİZGİLER olur. Dikey nesneler
   > (beş jalon + insan) gölgeyi orta banda taşır; 9:16, direk-gölge
   > çiftinin V şeklini tek kadrajda tutabilen tek orandır.
3. **İKİ LENS KİLİDİ** — Geniş/düzlük: **32mm** (S0, S2, S4, S5).
   Yakın/duygusal: **75mm** (S1, S3). İkisi asla tek karede karışmaz.
   Kamera mesafesi ve yüksekliği her promptta **metre** olarak yazılır.
4. **GÖSTER, ANLATMA** — Yönetmen notu yok. Hiçbir promptta "izleyici
   anlar", "ürpertici", "tekinsiz" geçmez — tekinsizlik geometriden çıkar.
5. **RENK DİLİ** — **Kireç beyazı plato + kavruk gri-yeşil bodur çalı +
   koyu haki saha kıyafeti + jalonların kırmızı-beyaz bantları + iki ton
   gölge grisi (koyu birinci / soluk ikinci) + S5'te akşam kehribarı.**

   > ⚠️ **Palet çakışma denetimi — dürüst kayıt.** Kireç tonu Last
   > Archive'ın paletinde geçiyor (dosyası kayıp, yalnız listelerde).
   > Ayırt edici öğe renk değil **gölgenin kendisinin palet olması**:
   > kadrandaki en önemli iki değer, aynı zeminin iki gri tonu. Seride
   > hiçbir konsept ana kontrastını gölge yoğunluğundan kurmadı. Jalon
   > kırmızısı kadranın %1'inden azında ve tek doygun renktir.
6. **KARAKTER SADAKATİ** — 6 görsel promptunun **6'sında da** aynı karakter
   bloğu birebir, kısaltmasız tekrarlanır. Köşeli parantez referansı
   kullanılmaz [Ders 45]. Kask yok — yüz 6 sahnede açık [Ders 16 morph
   yüzeyi]; karşı önlem: blok birebir tekrar + "photographed as a real
   person" satırı her promptta.
7. **VİRAL ZAMANLAMA (Hook)** — 0-2sn merak (öğle sonrası platoda ölçüm
   jalonlarına yürüyen adam — sıradan görüntü) → 2-5sn ipuçları (jalonların
   dipleri ÇATALLI: her direğin iki gölgesi var; adamın da) → 5-7sn tam
   reveal (beş jalonun beş soluk gölgesi de aynı yöne bakıyor ve hepsi
   birlikte, ÇIPLAK GÖZLE GÖRÜLÜR HIZDA dönüyor) → 7-8sn tek güçlü görüntü
   (adam durdu; koyu gölgesi durdu; soluk gölgesi dönmeye devam ediyor).
8. **TEK VİDEO PROMPTU** — Her sahnenin tek video promptu vardır ve T2V
   olarak yazılmıştır. Referans görselden üretim (I2V) yapacaksan: promptun
   başındaki teknik satırı ve `At 0s` beat'ini sil, yerine
   `"The scene begins exactly as the provided image."` yaz, kalan beat'leri
   düz nesre çevir. Karakteri/ortamı asla yeniden tarif etme.
9. **ELLER 6/6 BOŞ — SAPMA YOK** — Telefon, pusula, ölçüm aleti yok.
   Jalonlar zeminde DİKİLİ durur, hiçbir sahnede ele alınmaz. Deney
   bedenle yapılır: durmak, beklemek, gölgesinin dönüşünü izlemek.
10. **⛔ EKRANDA METİN SÜRESİ = 0,0 SANİYE [Ders 61]** — 6 sahnenin 6'sı
    canlı çekimdir. Jalon bantları düz kırmızı-beyaz DESENDİR; üzerlerinde
    rakam, çizik ölçek, harf YOKTUR. Kapak ayrı üretilir ve **videoya
    girmez**; başlık platformda yazılır.
11. **⛔ İKİNCİ KAYNAK ASLA GÖRÜNMEZ — BU FİLMİN 1 NUMARALI KURALI** —
    Gökyüzü 6 sahnenin 6'sında tek güneşli ve boştur. Model ikinci gölgeyi
    görünce gökyüzüne ikinci bir parlaklık, halo, mercek parlaması ya da
    "gizemli ışık" ekleyecektir — YASAK. İkinci kaynağın varlığı YALNIZ
    gölgelerden okunur. `the sky contains exactly one sun and nothing
    else — no second light source, no glow, no flare anywhere in the sky`
    satırı 6 görsel promptun 6'sında kalır.

---

## 🧬 VİRAL MEKANİK — "KAYNAĞI OLMAYAN GÖLGE"

```
Bu shorts'un imkansızlığı bir FAZLALIK: yerde, gökyüzünün
açıklayamadığı ikinci bir gölge seti var.

KURALLARI (her sahnede birebir aynı):
 · Birinci gölgeler NORMAL: görünen güneşle tam uyumlu, koyu,
   güneş alçaldıkça yavaşça uzar (gerçek fizik, tek yönlü).
 · İkinci gölgeler YANLIŞ: %60 yoğunlukta (daha soluk), daha uzun
   (alçak bir kaynağın geometrisi) ve saniyede 1,5 derece sabit
   hızla SAAT YÖNÜNDE döner — 8 saniyelik çekimde 12 derece:
   çıplak gözle görülür, ama acele etmez.
 · İki set TUTARLIDIR: bütün ikinci gölgeler aynı görünmez kaynağa
   göre hizalıdır — beş jalon, bir insan, her çalı: hepsi aynı anda,
   aynı açıyla döner. Kaynak tek. Sadece görünmüyor.
 · ÇİFT GÖLGE FİZİĞİ DOĞRU İŞLER: ikinci gölgenin içi birinci
   güneşin ışığıyla dolar → soluk gri. Birinci gölgenin içi görünmez
   kaynağın ışığıyla dolar → o da tam siyah değil. İKİ GÖLGENİN
   KESİŞTİĞİ BÖLGE her karede en koyu alandır. Bu, gerçek çift
   kaynaklı aydınlatmanın imzasıdır ve her promptta yazılır.
 · Gökyüzünde İKİNCİ HİÇBİR ŞEY YOKTUR: parlaklık yok, disk yok,
   bulut arkası ışıma yok. Yukarı bakan her çekim BOŞ mavi bulur.

İzleyicinin gözü ilk 2 saniyede "arazi ölçümü" der. 4. saniyede
jalon diplerinin çatallı olduğunu görür ve düzeltir: çift pozlama
değil, gölgeler gerçekten iki. 6. saniyede soluk setin DÖNDÜĞÜNÜ
görür ve bir kez daha düzeltir: bu bir kusur değil, bir KAYNAK —
gökyüzünde olmayan bir şey, yerde saat gibi işliyor. O an geriye
tek soru kalır: ışığı gördüğümüz şey mi, gölgesi olan şey mi?

Serinin önceki mekaniklerinden ayrı: süreksizlik değil (Winter
Line), sinyal yokluğu değil (Half Sky — bunun tam tersi), zaman
kaybı değil (First Morning), yörünge değil (Low Moon). Buradaki
mekanik EKSİK NEDEN: sonucu duran ama nedeni görünmeyen bir fizik.
```

### Mekaniğin insani karşılığı

```
Adam ölçüm için gelmişti — jalonları kendi dikmişti, gölgeden yön
okumayı meslek edinmiş biri. Filmin bedeli: bütün aletleri doğru
çalışıyor ve hiçbiri işe yaramıyor, çünkü ölçtüğü şeyin referansı
gökyüzünde değil. Tek kararı S3'te verilir ve tek jestle gösterilir:
ölçmeyi bırakır, kendi soluk gölgesinin ortasında durur ve onun
kendi çevresinde dönüşünü İZLER — insan, kendi güneş saatinin
mili olur.
```

---

## 📱 GÜVENLİ ALAN HARİTASI (9:16 · 1080×1920)

Kaynak: `kilavuzlar_ve_sistem_dosyalari/KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` §5
evrensel matrisi · denetleyen rubrik: `QA_PROMPTLARI/SHORTS_QA_CRITIQUE_PROMPT.md` §B

```
┌──────────────────────────────┐ y=0
│  ÜST KÖR NOKTA  200-254 px   │      sekmeler, profil
├──────────────────────────────┤ y=254
│                          │S │
│                          │A │
│        GÜVENLİ ALAN      │Ğ │      sağ 242 px: beğen/paylaş/yorum
│                          │  │
│                          │242
├──────────────────────────────┤ y=1436   ⛔ BURADAN AŞAĞISI GÖRÜNMEZ
│  ALT KÖR NOKTA    484 px     │      açıklama, müzik, CTA
└──────────────────────────────┘ y=1920
```

### ⚠️ BU FİLMİN YAPISAL ÇELİŞKİSİ VE ÇÖZÜMÜ

```
Reveal nesnesi GÖLGE — yerde yaşıyor.
Güvenli alan kuralı altı yasaklıyor.
```

Çözüm kadraj hilesi değil **kamera yüksekliği ve eğimi** [Dull Edge S4-S5
ve Sinking Hour emsali]:

> **Kamera alçak (0,5-1,2 m) ve neredeyse yatay tutulur.** Gölgeler böylece
> kadranın ortasına DİYAGONAL uzanan çizgiler olur; jalonlar ve insan o
> çizgilerin dikey karşılığıdır. Yerdeki bir geometriyi yukarıdan çekmek
> onu alt şeride gömer; yanından çekmek ona kareyi verir.

### Sahne sahne denetim

| Sahne | Reveal nesnesi | Doğal yeri | Karara bağlanan çözüm |
|:--:|---|:--:|---|
| S0 | çatallı jalon gölgeleri | ⚠️ yerde | kamera 1,2 m; jalonlar y400-1100; gölge yelpazesi y700-1350 |
| S1 | dönen tek gölge | ⚠️ yerde | kamera 0,5 m, eğik; jalon dibi + iki gölge merkezde y600-1250 |
| S2 | BOŞ gökyüzü | ✅ üst | tilt-up y254'e kadar; güneş kadraj DIŞI tutulur; figür y1250-1420 |
| S3 | insan-mil, dönen soluk gölge | ⚠️ yerde | kamera 0,9 m; figür y500-1350; soluk gölge ucu y≈800'de döner |
| S4 | HİZALANMA — iki setin üst üste binişi | ⚠️ yerde | kamera 0,8 m; beş jalon + tek gölgeler y500-1350 |
| S5 | ışıksız kalan gölgeler | ⚠️ yerde | kamera 0,6 m; figür oturmuş y900-1300; soluk gölgeler y700-1350 |

**Her görsel promptun COMPOSITION satırına eklenen zorunlu cümle:**

```
No part of the figure falls into the bottom quarter of the frame.
```

---

## 📖 Sabit Referanslar (Bibles)

### 👤 Character Bible

**Kimlik (yalnızca bu dosyada):** MERT SAYAR, 41, harita mühendisi.
Yirmi yıldır arazide; gölgeden saat, jalondan hiza okuyan son kuşaktan.
O gün platoya rutin bir höyük ölçümü için çıktı.

> ⚠️ **ÜRETİM UYARISI [Ders 34 / 45]:** Karakter Türk, ama promptlarda
> **milliyet ifadesi KULLANILMAZ** — geçmişte üretim reddine yol açtı.
> Karakterin adı hiçbir promptta yazılmaz. Gerçek bir kurum, ülke, il,
> bayrak ya da marka hiçbir promptta geçmez.

**Tam tarif — 6 GÖRSEL promptun 6'sında da birebir, kısaltmasız tekrarlanır:**

```
A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch.
```

**Hareket imzası (konsepte özgü):** Ölçüm insanı refleksleri: bir şeyi
anlamak için önce **kendi gölgesine bakar** — yön, saat, hiza hepsi orada.
Şaşkınlığı hızlanma değil **doğrulamadır**: gördüğü şeyi bir de başka
nesnenin gölgesinde kontrol eder (jalona bakar, sonra çalıya, sonra kendine).
En etkilendiği anda tamamen durur ve yalnız başı döner — gövde, dikili
bir jalon gibi sabit kalır.

**⚠️ JALON KİLİDİ [sayısal]:** Platoda **TAM BEŞ** ahşap ölçüm jalonu
dikilidir — düz kırmızı-beyaz bantlı, 2 metre boyunda, üzerlerinde hiçbir
rakam ya da harf yok. Beşi de 6 sahnenin 6'sında AYNI yerde durur, hiçbir
sahnede ele alınmaz, taşınmaz, devrilmez.

### 🌍 World Bible — KİREÇTAŞI PLATOSU, GÜNÜMÜZ

```
YER:      Günümüz Dünyası. Açık kireçtaşı platosu — soluk, neredeyse beyaz
          çakıllı zemin; tek tük bodur gri-yeşil çalı; ağaç yok, yapı yok,
          yol yok, direk hattı yok. Promptlarda yer adı geçmez.
ZAMAN:    Yaz, öğleden sonra. Film boyunca güneş ALÇALIR (tek yönde) —
          birinci gölgeler sahneden sahneye uzar. S5 gün batımına dakikalar
          kala biter.
YERÇEKİMİ: 1g. Rüzgar neredeyse yok — çalılar kıpırdamaz.
GÖKYÜZÜ:  Bulutsuz, derin yaz mavisi. GÖRÜNEN GÜNEŞ TEKTİR ve normaldir.
          ⛔ İkinci hiçbir parlaklık, disk, halo, ışıma yoktur (Kural 11).
SU:       GÖRÜNMEZ. Kuru plato; birikinti, dere, çamur, yağmur yok.
SES:      Yaz platosunun cılız sessizliği: uzak böcek vızıltısı yok
          (canlı yok), yalnız bot altında çakıl ve hafif hava.

⚠️ MERKEZİ FİZİKSEL İMKANSIZLIK — GÖLGE TAKVİMİ (sahne başına yazılır):
İki gölge seti arasındaki açı farkı tek yönde kapanır, S4'te sıfırlanır
(HİZALANMA) ve S5'te işaret değiştirir:

  S0   fark  70°   soluk set saat yönünde dönüyor (1,5°/sn)
  S1   fark  55°   aynı hız — 8 saniyede 12°
  S2   fark  40°   yukarı bakışta gökyüzü BOŞ
  S3   fark  25°   adam duruyor, soluk gölgesi onun çevresinde dönüyor
  S4   fark   0°   ÜST ÜSTE BİNİŞ — bir anlık tek, en koyu gölge; sonra ayrılır
  S5   fark -20°   soluk set öbür tarafa geçmiş; birinci set akşamla siliniyor

Her görsel promptta zorunlu satır:
"the second, fainter shadow set points approximately [X] degrees clockwise
from the true sun shadows and rotates clockwise at a steady 1.5 degrees
per second"
Her görsel promptta zorunlu fizik satırı:
"where the two shadows of one object overlap, the overlap is the darkest
area in frame; each single shadow stays half-filled by the other light"
```

### 🎥 Camera Bible

```
LENS KİLİDİ — çekim başına tam olarak bir lens:
  32mm → S0, S2, S4, S5   (düzlük / yelpaze / final)
  75mm → S1, S3           (yakın / duygusal)
MESAFE + YÜKSEKLİK KİLİDİ: her promptta metre cinsinden yazılır.
  Kamera hiçbir sahnede 1,2 metreden yüksek değildir (güvenli alan çözümü).
HAREKET SÖZLÜĞÜ (çekim başına TEK sürekli hareket):
  S0 yavaş ileri dolly · S1 sabit lockoff · S2 tilt-up · S3 sabit lockoff ·
  S4 sabit lockoff (⭐ hizalanma karesi — kamera KIPIRDAMAZ) · S5 yavaş pull-back
  El kamerası sarsıntısı YASAK. İki hareketi birleştirme.
SABİT KLİP SÜRESİ: her video promptu tam 8 saniye, tek kesintisiz çekim.
GÜNEŞ KADRAJI: Görünen güneş yalnız S2'de kadrajın KENARINA yaklaşır ama
  hiçbir sahnede kadraja GİRMEZ — flare riski sıfırlanır [Ders 3].
```

### 💡 Lighting Bible — İKİ KAYNAK, BİRİ GÖRÜNMEZ

```
KAYNAKLAR (adıyla yazılır, asla "cinematic lighting" denmez) [Ders 33]:
  · GÖRÜNEN GÜNEŞ: sert, sıcak, alçalan yaz güneşi. Koyu, keskin
    kenarlı birinci gölgeler. Sahneden sahneye uzar (tek yönlü).
  · GÖRÜNMEZ KAYNAK: yerdeki etkisi ikinci gölge setinden İBARETTİR.
    Gökyüzünde karşılığı yok, yüzeylerde ikinci parlama yok, çift
    speküler yok. Yoğunluğu birinci setin %60'ı; rengi NÖTR — sıcak
    ya da soğuk değil (renk verilirse model kaynak uydurur).
⚠️ [Ders 41/3/29] Açık kireç zemini + sert güneş = yüksek bloom riski.
   Zemin MAT tozlu kireçtir, parlamaz; "glowing/radiant" hiçbir promptta
   geçmez; gökyüzünde halo/flare yasak (Kural 11 ile aynı satırda).

IŞIK TAKVİMİ — tek yönlü, her promptta yazılır:
  S0 güneş ~40° · S1 ~34° · S2 ~28° · S3 ~21° · S4 ~14° · S5 ~6° (ufka yakın)
  Zorunlu satır: "the visible sun stands approximately [X] degrees above
  the horizon; the true shadows are longer than in the previous scene."
ZEMİN KİLİDİ [Ders 48]: "the terrain type, gravel texture and ground
colour are identical to the previous scene; only the light has changed."
```

### 🚫 Negative Bible

```
Kesme yok. Sarsıntı yok. Ağır çekim yok. Minyatür/oyuncak görünüm yok.
CGI havası yok. Hava fırçasız cilt yok. İkinci insan yok, insan yansıması
yok. Elde alet yok. Metin yok. Filigran yok.

KONSEPTE ÖZGÜ EKLER:
Gökyüzünde İKİNCİ IŞIK YOK: ikinci güneş yok, parlak nokta yok, disk yok,
halo yok, ışık sütunu yok, bulut ışıması yok, lens flare yok. Gölge
sayısı nesne başına TAM İKİ — üç gölge yok, gölge kalabalığı yok.
Gölgeler zeminden KALKMAZ, dikleşmez, şekil değiştirmez — yalnız döner
ve uzar. Soluk set ASLA koyu setten koyu değildir. Jalonlar devrilmez,
eğilmez, ele alınmaz. Güneş kadraja girmez. Su yok, bulut yok, rüzgar
savurması yok, toz bulutu yok.
```

**Negatif bloklara eklenecek kuyruk (her görsel promptun sonuna):**

```
no second sun, no second light in the sky, no bright spot in the sky, no
halo, no light pillar, no glow in the sky, no lens flare, no third shadow,
no shadow lifting off the ground, no shadow changing shape, no second
person, no human reflection, no animals, no birds, no clouds, no wind, no
dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow
filter, no CGI look, no waxy skin, no miniature look, no text, no letters,
no digits, no flag, no logo, no HUD overlay, no watermark
```

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

```
🔴 EN YÜKSEK RİSK — kartlarda yok, bu dosyada tanımlandı

ÇİFT GÖLGE GEOMETRİSİ
        Model gölgeyi kaynaktan türetir; kaynaksız ikinci set ya
        kaybolur ya çoğalır ya da gökyüzüne kaynak uydurulur.
        Kilitler: açı farkı DERECE ile (GÖLGE TAKVİMİ) · dönüş hızı
        1,5°/sn · nesne başına TAM İKİ gölge · kesişim en koyu alan ·
        gökyüzü boş (Kural 11 satırı 6/6).
        ÜRETİM SIRASI: S4 (hizalanma) önce üretilir; iki set üst üste
        binerken üçüncü gölge ya da gök parlaması çıkarsa film üretilmez
        [THE LOW MOON emsali].

DERS 3 / 29 / 41  BLOOM — açık kireç zemin + sert güneş + "gizemli ışık"
        beklentisi. Güneş kadraja girmez; zemin mat; gökyüzünde
        parlaklık yasak. En riskli sahne S2 (boş gökyüzü taraması).

🟡 ORTA RİSK

KART 4 / DERS 20  İKİNCİ FİGÜR — "exactly one human" 6 promptta
DERS 16           YÜZ MORPH — kask yok, yüz 6 sahnede açık; blok birebir
DERS 47 / 48      IŞIK VE ZEMİN İLERLEMESİ — güneş tek yönde alçalır,
                  birinci gölgeler tek yönde uzar; zemin 6 sahnede aynı
DERS 6            ARKA PLAN — jalon konumları, ufuk, çalılar sabit
DERS 12 / 44      AĞIR ÇEKİM — "yavaş dönen gölge" modeli slow-motion'a
                  çekebilir; dönüş GERÇEK hızda yavaştır (1,5°/sn),
                  "No slow motion" 6 videoda 6 kez
DERS 42           DESEN SÜRÜKLENMESİ — jalon bant düzeni 6 sahnede aynı

⬛ HER PROMPTTA

DERS 9 · 13 · 34 · 45 · 61   EKRANDA METİN YOK — jalonlarda rakam/harf yok,
        kıyafette logo yok, isim/bayrak hiçbir promptta geçmez.
```

---

## 🎬 SAHNE 0 — KANCA: ÇATAL

_"Beş direk dikti. On gölge saydı."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 0 of 6. Solo male land surveyor present-day light-anomaly discovery film. MAXIMUM VIRAL WRONG-PHYSICS SHOCK.
Lens: 32mm, f/8, ISO 100.
Camera Distance: Approximately 9 metres, camera height 1.2 metres, held level.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He stands mid-stride toward the survey poles, caught slowing down, head beginning to tilt down toward the ground.

ENVIRONMENT / BACKGROUND: A pale, near-white limestone gravel plateau under a cloudless deep summer sky, scattered low grey-green scrub, no trees, no buildings, no roads. EXACTLY FIVE plain wooden survey poles with flat red-and-white bands — no numbers, no letters, no markings — stand fixed upright in a loose line across the middle distance, each 2 metres tall. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky; the sun itself is outside the frame. The visible sun stands approximately 40 degrees above the horizon.

THE VIRAL MOMENT / REVEAL: Every object on the plateau casts TWO shadows. Each pole throws one dark, crisp shadow consistent with the sun — and a second, fainter, LONGER shadow forked away from it. The second, fainter shadow set points approximately 70 degrees clockwise from the true sun shadows and rotates clockwise at a steady 1.5 degrees per second. The man's own two shadows fork at his boots. Where the two shadows of one object overlap, the overlap is the darkest area in frame; each single shadow stays half-filled by the other light.

COMPOSITION: Vertical 9:16. The five poles stand between roughly twenty-one and fifty-seven percent of frame height, their forked shadow pairs fanning diagonally across the mid-frame between roughly thirty-six and seventy percent. He stands left of centre at roughly forty to seventy percent, held clear of the outer right eighth. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only pale gravel.

LIGHTING: Hard warm afternoon sunlight from frame right; matte chalky gravel, no specular shine anywhere. The dark shadow set is crisp and warm-edged; the faint set is neutral grey at sixty percent density. No bloom, no glow, no lens flare.

PHYSICS: Ordinary Earth gravity, still air — the scrub does not move. The poles are rigid and vertical. Both shadow sets lie flat on the ground and follow the terrain micro-relief correctly.

NEGATIVE: Exactly one human in the entire frame. Exactly five poles, each with exactly two shadows. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no third shadow, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, camera height 1.2 metres, one slow continuous forward dolly from 9 metres to 6 metres. Real-time motion at normal playback speed.

At 0s — A man in a dark-khaki field jacket walks unhurried across a pale limestone gravel plateau toward five red-and-white banded survey poles under a cloudless summer sky. An ordinary surveying afternoon.
At 2s — The dolly closes. The base of each pole reads wrong: every pole stands in a FORK of two shadows — one dark and crisp, one fainter and longer, split roughly 70 degrees apart.
At 3.5s — He slows, then stops. His own two shadows fork at his boots. He looks down at them, then at the nearest pole, then back — a surveyor cross-checking.
At 5s — The fainter shadow set is MOVING: all five faint pole shadows sweep clockwise together at a steady, naked-eye pace — about 12 degrees over the length of the shot — while the dark set stays fixed.
At 6.5s — He lifts his head and scans the empty blue sky. One sun, off-frame. Nothing else.
By 8s — He stands still; his dark shadow stands still; his faint shadow keeps turning. No cuts within the shot.

Exactly one human in this shot. Every object keeps exactly two shadows; the overlap of any pair is the darkest area in frame. The sky stays empty — no second light, no glow, no flare. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 1 — SANİYEDE BİR BUÇUK DERECE

_"Koyu olan saate uyuyor. Soluk olan kendi saatine."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 1 of 6. Solo male land surveyor present-day light-anomaly discovery film.
Lens: 75mm, f/4, ISO 100.
Camera Distance: Approximately 1.8 metres, camera height 0.5 metres, angled gently down at the base of one pole.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He crouches at the edge of frame beside the pole, forearms on his knees, hands hanging empty, eyes fixed on the shadows.

ENVIRONMENT / BACKGROUND: The base of ONE red-and-white banded wooden survey pole — no numbers, no letters — planted firm in pale limestone gravel. From its base, TWO shadows: one dark, crisp and fixed; one fainter, longer, at sixty percent density. The second, fainter shadow set points approximately 55 degrees clockwise from the true sun shadows and rotates clockwise at a steady 1.5 degrees per second. Where the two shadows overlap near the pole base, the overlap is the darkest area in frame; each single shadow stays half-filled by the other light. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky. The visible sun stands approximately 34 degrees above the horizon; the true shadows are longer than in the previous scene. The terrain type, gravel texture and ground colour are identical to the previous scene; only the light has changed.

THE VIRAL MOMENT / REVEAL: At this distance the motion is undeniable: the faint shadow sweeps across the gravel like the minute hand of an enormous clock — individual pebbles darken and lighten as its edge passes over them. The dark shadow does not move at all.

COMPOSITION: Vertical 9:16. The pole rises through the left third from roughly thirty to sixty-eight percent of frame height; its two shadows fan across the centre of frame between roughly fifty and seventy-three percent. His crouched figure holds the right edge from roughly forty to seventy percent, clear of the outer right eighth. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only gravel texture.

LIGHTING: Hard warm afternoon sun from frame right; matte chalk gravel, matte painted wood. The faint shadow's moving edge is soft but clearly defined — a penumbra, not a blur. No bloom, no glow, no lens flare.

PHYSICS: Ordinary Earth gravity, still air. The pole is rigid; nothing on it moves. Only the faint shadow moves, flat on the ground, at its steady clock-hand pace.

NEGATIVE: Exactly one human in the entire frame. One pole, exactly two shadows. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no third shadow, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm, locked off at 1.8 metres, camera height 0.5 metres, angled gently down. Real-time motion at normal playback speed.

At 0s — Low and close on the base of one red-and-white banded survey pole in pale gravel. Two shadows run from its base: one dark and fixed, one fainter and longer. A man crouches at the right edge of frame, forearms on knees, hands empty, watching.
At 2s — The faint shadow's edge sweeps steadily clockwise across the gravel — about 1.5 degrees per second, the pace of a clock's second hand seen up close. Individual pebbles darken and lighten as the edge passes over them.
At 4s — The dark shadow has not moved a millimetre. Where the two shadows cross near the pole base, the overlap stays the darkest patch in frame, sliding slowly as the faint set turns.
At 5.5s — His head tilts slightly to one side. He looks from the shadows up along the pole to its tip, then back down — verifying, twice.
At 7s — He reaches no conclusion. The faint shadow keeps turning at exactly the same rate.
By 8s — Roughly 12 degrees of sweep have passed. No cuts within the shot.

Exactly one human in this shot. One pole, exactly two shadows, both flat on the ground. The sky never appears. Everything moves at normal speed — the shadow is slow, not slowed down. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 2 — BOŞ GÖKYÜZÜ

_"Kaynağı aradı. Gökyüzü cevap vermedi."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 2 of 6. Solo male land surveyor present-day light-anomaly discovery film.
Lens: 32mm, f/8, ISO 100.
Camera Distance: Approximately 5 metres behind him, camera height 1.0 metre, tilted up.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He stands in the lower frame, seen from behind at a three-quarter angle, head tipped fully back, scanning the sky along the exact line his faint shadow points away from.

ENVIRONMENT / BACKGROUND: The pale limestone plateau falls away at the bottom of frame; above it, a vast, cloudless, deep-blue summer sky fills the upper two thirds of the vertical frame — COMPLETELY EMPTY. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky; the sun sits just beyond the upper-right frame edge, outside the frame. Two of the red-and-white banded survey poles flank him. The second, fainter shadow set points approximately 40 degrees clockwise from the true sun shadows and rotates clockwise at a steady 1.5 degrees per second — at his boots, the fork of his own two shadows is visible at the very bottom of the safe frame. Where the two shadows overlap, the overlap is the darkest area in frame. The visible sun stands approximately 28 degrees above the horizon; the true shadows are longer than in the previous scene. The terrain type, gravel texture and ground colour are identical to the previous scene; only the light has changed.

THE VIRAL MOMENT / REVEAL: The reveal is an ABSENCE: the direction every faint shadow points away from holds nothing at all. No second sun, no bright patch, no haze — just clean empty blue. The light has no address.

COMPOSITION: Vertical 9:16. Empty sky fills the frame from the top safe edge down to roughly fifty-five percent of frame height. He stands small between roughly sixty-five and seventy-four percent, left of centre, the two flanking poles rising beside him, all held clear of the outer right eighth. His forked shadows appear between roughly seventy and seventy-four percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only pale gravel.

LIGHTING: Hard warm afternoon sun from beyond the upper-right frame edge; clean gradient blue sky with absolutely no secondary brightening anywhere. Matte gravel, matte fabrics. No bloom, no glow, no lens flare, no halo.

PHYSICS: Ordinary Earth gravity, still air. The sky gradient is smooth and natural; atmospheric blue deepens toward the zenith exactly as a real cloudless sky does.

NEGATIVE: Exactly one human in the entire frame. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no third shadow, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, camera 5 metres behind him at height 1.0 metre, one slow continuous tilt-up. Real-time motion at normal playback speed.

At 0s — Framed low behind him: the man stands between two banded survey poles on the pale plateau, his two shadows forking at his boots — one dark and fixed, one faint and slowly turning.
At 2s — The camera begins one slow continuous tilt-up, past his shoulders and the pole tips, following the exact line his faint shadow points away from.
At 4s — The frame climbs into open sky: cloudless, deep summer blue, completely empty. The tilt keeps climbing. Nothing appears.
At 5.5s — The tilt settles high. Clean empty blue holds the frame, the sun itself staying just beyond the upper-right frame edge. No second light, no haze, no mark.
At 7s — Hold on the empty sky, steady.
By 8s — Nothing has appeared. No cuts within the shot.

Exactly one human in this shot. The sky stays completely empty — no second sun, no bright spot, no glow, no flare at any moment. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 3 — İNSAN MİL

_"Ölçmeyi bıraktı. Kadran oldu."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 3 of 6. Solo male land surveyor present-day light-anomaly discovery film.
Lens: 75mm, f/4, ISO 100.
Camera Distance: Approximately 3 metres, camera height 0.9 metres, level.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He stands perfectly upright and perfectly still, arms at his sides, feet together — deliberately holding the posture of a survey pole — chin down, eyes tracking the tip of his own faint shadow as it moves.

ENVIRONMENT / BACKGROUND: Open pale limestone gravel around him, the five banded poles soft in the background. From his boots, TWO shadows: the dark one fixed, reaching toward the lower left; the faint, longer one sweeping. The second, fainter shadow set points approximately 25 degrees clockwise from the true sun shadows and rotates clockwise at a steady 1.5 degrees per second. Where the two shadows overlap, the overlap is the darkest area in frame; each single shadow stays half-filled by the other light. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky. The visible sun stands approximately 21 degrees above the horizon; the true shadows are longer than in the previous scene. The terrain type, gravel texture and ground colour are identical to the previous scene; only the light has changed.

THE VIRAL MOMENT / REVEAL: A man standing still as a post, being used as one: his faint shadow turns slowly around him like the hand of a sundial, and he — the instrument-less surveyor — reads it with his eyes alone, measuring something the sky refuses to show.

COMPOSITION: Vertical 9:16. He stands centred slightly left, filling the frame from roughly twenty-six to seventy percent of frame height, clear of the outer right eighth. His dark shadow runs toward the lower left corner of the safe area; the faint shadow's tip sweeps through the mid-frame at roughly forty-two percent. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only gravel and the far end of his dark shadow.

LIGHTING: Warm, lowering afternoon sun from frame right rakes his face and jacket; long crisp dark shadow, fainter neutral second shadow at sixty percent density. Matte everything. No bloom, no glow, no lens flare.

PHYSICS: Ordinary Earth gravity, still air. His body is motionless — only his eyes move, and the faint shadow turns at its constant rate, flat on the ground.

NEGATIVE: Exactly one human in the entire frame. Exactly two shadows from his boots. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no third shadow, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm, locked off at 3 metres, camera height 0.9 metres, level. Real-time motion at normal playback speed.

At 0s — The man stands perfectly upright and still in open gravel, arms at his sides, feet together, like one more survey pole. Two shadows run from his boots: one dark and fixed, one faint and longer.
At 2s — The faint shadow sweeps slowly clockwise around him at its steady clock pace. His eyes track its tip; his head barely turns; his body does not move at all.
At 4s — The faint shadow's edge crosses a band of lighter gravel and its tip becomes easy to follow — a slow, certain hand on an enormous dial, with him as the gnomon.
At 5.5s — His breathing shows in his shoulders, slow and even. He keeps holding the pose, reading his own shadow the way he would read an instrument.
At 7s — The faint shadow keeps turning. The dark one has not moved.
By 8s — He is still standing, still reading. No cuts within the shot.

Exactly one human in this shot. Exactly two shadows from his boots, both flat on the ground. The sky never appears. Everything moves at normal speed — the shadow is slow, not slowed down. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 4 — VİRAL DORUK: HİZALANMA

_"İki gölge üst üste bindi. Bir saniyeliğine dünya normaldi."_

> ⭐ **ÜRETİM BURADAN BAŞLAR.** Filmin en pahalı karesi ve çift gölge
> geometrisinin en zor anı. Üst üste biniş sırasında üçüncü bir gölge,
> gökyüzünde parlama ya da gölge şekli bozulması çıkarsa film üretilmez —
> prompt iyileştirmeye dönmeden önce
> `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` oku.

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 4 of 6. Solo male land surveyor present-day light-anomaly discovery film. MAXIMUM VIRAL ALIGNMENT SHOCK.
Lens: 32mm, f/8, ISO 100.
Camera Distance: Approximately 7 metres, camera height 0.8 metres, level.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He stands among the five poles, feet apart, completely still, watching the ground.

ENVIRONMENT / BACKGROUND: The five red-and-white banded survey poles in their fixed line across the pale gravel, the man among them. THE ALIGNMENT INSTANT: the faint shadow set has swept all the way around to the true shadows — the second, fainter shadow set points approximately 0 degrees clockwise from the true sun shadows, still rotating clockwise at a steady 1.5 degrees per second. For this instant every object on the plateau casts what reads as ONE single shadow — and because the two lights stack, each merged shadow is DARKER than either alone: five poles and one man, each with one abnormally dark, doubled shadow. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky. The visible sun stands approximately 14 degrees above the horizon; the true shadows are longer than in the previous scene. The terrain type, gravel texture and ground colour are identical to the previous scene; only the light has changed.

THE VIRAL MOMENT / REVEAL: The plateau looks normal for one breath — one shadow per object, like any afternoon — except every shadow is too dark, ink-dark, denser than a single sun can make. The wrongness is no longer the fork; it is the depth.

COMPOSITION: Vertical 9:16. The five poles and the man fill the frame between roughly twenty-one and seventy percent of frame height, their single merged shadows running parallel toward the lower left, dark as cut slots in the pale gravel. He stands right of centre at roughly thirty-four to sixty-eight percent, clear of the outer right eighth. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only gravel and shadow tails.

LIGHTING: Low warm sun from frame right; the merged shadows are the darkest values in the entire film, hard-edged, flat on the ground. The gravel between them stays bright and matte. No bloom, no glow, no lens flare.

PHYSICS: Ordinary Earth gravity, still air. Each object casts exactly one visible shadow at this instant — the two sets in perfect overlap — and every merged shadow is visibly darker than any single shadow seen earlier.

NEGATIVE: Exactly one human in the entire frame. Exactly five poles. One merged shadow per object at this instant — no forked shadows, no third shadow. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, locked off at 7 metres, camera height 0.8 metres, dead level. The camera does not move at all. Real-time motion at normal playback speed.

At 0s — Wide and low among the five banded poles: every pole and the man cast a dark shadow and a faint shadow, the faint set now only a sliver apart from the dark set, still sweeping clockwise at its steady pace.
At 2s — The gap closes. Sliver by sliver, the faint shadows slide onto the dark ones — all five poles and the man in perfect unison.
At 3.5s — ALIGNMENT. For one breath the plateau reads normal: one shadow per object. But each merged shadow is ink-dark, visibly denser than any single shadow in the film. He looks down at his own doubled shadow.
At 5s — The faint set keeps moving and slides out the other side. The forks reopen, mirrored now, widening at the same steady 1.5 degrees per second.
At 6.5s — Five poles, one man, ten shadows again. He exhales; his shoulders drop slightly.
By 8s — The forks keep widening. No cuts within the shot.

Exactly one human in this shot. Never more than two shadows per object; during the overlap, exactly one darker shadow per object. The sky stays empty — no second light, no glow, no flare. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 5 — IŞIKSIZ GÖLGELER

_"Güneş gitti. Gölgeler kaldı."_

### 📸 GÖRSEL PROMPT

```
Cinematic photorealistic still image — Scene 5 of 6. Solo male land surveyor present-day light-anomaly discovery film.
Lens: 32mm, f/5.6, ISO 400.
Camera Distance: Approximately 11 metres, camera height 0.6 metres, level, pulling back.

SUBJECT: A 41-YEAR-OLD MAN land surveyor — sun-darkened olive skin with clearly visible pore texture, deep crow's feet from decades of squinting, dark brown eyes, heavy dark eyebrows, a short salt-and-pepper beard kept rough, a sun-chapped lower lip, no glasses, natural facial asymmetry. Photographed as a real person, not CGI. His dark grey hair is short and flattened by a worn DARK-KHAKI canvas field cap. He is 1.78 metres tall, lean and weathered. He wears a plain dark-khaki field jacket open over a faded charcoal T-shirt, dusty olive work trousers, and scuffed tan leather work boots — every fabric plain and matte, carrying no logo, characters, digits or symbols anywhere. His hands are bare and always empty; he carries no phone, no instrument, no bag, and wears no watch. He SITS on the gravel among the poles, knees drawn up, forearms resting across them, calm, watching his own remaining shadow.

ENVIRONMENT / BACKGROUND: The plateau in the last minutes before sunset: the visible sun stands approximately 6 degrees above the horizon, amber and weak, just beyond the right frame edge. The TRUE shadows have stretched thin and pale, dissolving into the dimming gravel — almost gone. THE FAINT SET HAS NOT DIMMED AT ALL: five pole shadows and one human shadow, still at their steady sixty-percent density, now the STRONGEST shadows on the plateau, all pointing their own way. The second, fainter shadow set points approximately 20 degrees counter-clockwise from the dying true shadows and rotates clockwise at a steady 1.5 degrees per second. The sky contains exactly one sun and nothing else — no second light source, no glow, no flare anywhere in the sky. The terrain type, gravel texture and ground colour are identical to the previous scene; only the light has changed.

THE VIRAL MOMENT / REVEAL: The visible sun is dying and its shadows are dying with it — but the sourceless shadows remain, crisp and certain in the amber dusk. By dark, they will be the only shadows left: shadows cast by nothing, on a plateau lit by something no one will ever see.

COMPOSITION: Vertical 9:16. He sits small right of centre between roughly fifty-two and sixty-eight percent of frame height, clear of the outer right eighth; the five poles stand around him between roughly twenty-six and sixty percent. The faint shadow lines rake diagonally across the mid-frame, the strongest marks in the dusk. No part of the figure falls into the bottom quarter of the frame; the bottom quarter carries only darkening gravel.

LIGHTING: Weak amber sunset light from frame right, long and thin; the plateau surface dims toward blue-grey while the faint shadow set stays at full sixty-percent density — the only crisp contrast left. No bloom, no glow, no lens flare, no sun disc in frame.

PHYSICS: Ordinary Earth gravity, still air. The true shadows fade smoothly as the sun sinks; the faint set neither fades nor stops, flat on the ground, steady.

NEGATIVE: Exactly one human in the entire frame. Exactly five poles. no second sun, no second light in the sky, no bright spot in the sky, no halo, no light pillar, no glow in the sky, no lens flare, no third shadow, no shadow lifting off the ground, no shadow changing shape, no second person, no human reflection, no animals, no birds, no clouds, no wind, no dust cloud, no slow motion, no water, no wet surfaces, no bloom, no glow filter, no CGI look, no waxy skin, no miniature look, no text, no letters, no digits, no flag, no logo, no HUD overlay, no watermark.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm, one slow continuous pull-back from 11 metres to 15 metres, camera height 0.6 metres, level. Real-time motion at normal playback speed.

At 0s — Amber dusk on the plateau. The man sits on the gravel among the five banded poles, knees drawn up, hands empty. Every object still carries two shadows: the true ones long, thin and fading; the faint ones crisp and steady.
At 2s — The camera begins pulling slowly back. The sun's light weakens visibly; the true shadows dissolve into the dimming gravel, pole by pole.
At 4s — Only the faint set remains strong: five pole shadows and one human shadow, still turning together at their steady pace, now the clearest marks on the plateau.
At 5.5s — He watches his own remaining shadow sweep slowly past his boots. He does not move. His calm is the calm of a man who has stopped needing the answer today.
At 7s — The pull-back opens the plateau wide: dusk, five poles, one seated man, six certain shadows under an empty darkening sky.
By 8s — The faint shadows are still turning. No cuts within the shot.

Exactly one human in this shot. The sky stays empty to the end — no second light, no glow, no flare. The faint shadows never fade and never stop. Everything moves at normal speed. No slow motion.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No camera shake. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎶 MÜZİK PROMPTU (Tek Global Tema — 48 sn)

Araç: Suno / Udio · tek parça · 48 saniye · söz yok, geleneksel melodi yok.

```
48-second minimalist ambient score, no vocals, no lyrics, no traditional melody. TWO DRONES AND NOTHING ELSE: 1. A warm sustained cello-and-viola drone in a low register — close, dry, steady. This is the visible sun. 2. THE SAME drone doubled a quarter-tone sharp, slightly quieter and more distant in the mix, so the two detuned layers beat slowly against each other. This is the unseen light. The audible BEATING between the two drones is the engine of the whole track.

Dynamic arc: 0-8s the warm drone alone for four seconds, then the detuned double fades in and the slow beating begins. 8-16s both drones steady; the beat frequency is slow and uneven, like something turning. 16-24s the detuned layer drifts very slightly closer in pitch; the beating slows. 24-32s closer still — long, patient waves of interference, near stillness. 32-40s THE ALIGNMENT: the two drones reach perfect unison and the beating STOPS — one pure, fused, darker-sounding tone for four full seconds — then the detune returns on the far side and the beating resumes, mirrored. 40-48s the warm drone fades with the sunset until only the detuned layer remains, quiet and steady, and the track is CUT by one second of true silence at 47s. No fade, no cadence, no resolution.

Mood: measured, patient, quietly wrong. Reference feel: the sustained restraint of Éliane Radigue and the slow harmonic patience of Jóhann Jóhannsson. Do not quote, sample or reproduce any melody, motif or lyric from either.

NO vocals, NO lyrics, NO choir, NO melody, NO percussion of any kind, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO orchestral swell, NO field recording, NO wind ambience.
```

> Yapı filmi birebir izler: iki dron = iki ışık kaynağı; aradaki **vuru
> (beating)** = iki gölge setinin açı farkı. Fark kapandıkça vuru yavaşlar,
> S4 hizalanmasında (32-40s) tam UNISON — müzikteki "tek koyu gölge" —
> sonra öbür tarafta yeniden açılır. 40-48s'de görünen güneşin dronu
> batar, görünmeyenin dronu kalır: S5'in ses karşılığı. 47. saniyedeki
> bir saniyelik mutlak sessizlik, cevapsız kalan soruyu keser.

---

## 🖼️ KAPAK PROMPTU (1080×1920)

⚠️ **Bu görsel videoya GİRMEZ** — yalnızca thumbnail [Ders 61].

> **Kaynak an: S0.** Kapağın tek sınavı 120 px testidir. Bu karede 120 px'te
> okunan şey bir DESENDİR: açık zemin üzerinde dikey çizgiler ve her
> çizginin dibinden çıkan V biçimli ÇİFT gölge. Tek gölge sıradan bir
> ikindidir; çatal, küçültmede bile "yanlış" okunur — izleyici neyin yanlış
> olduğunu adlandıramadan durur. Kapak kararı estetik değil, desen kararıdır.

```
Cinematic photorealistic vertical cover image, 1080x1920, 9:16. Present-day Earth,
pale limestone gravel plateau, cloudless deep-blue summer sky, hard afternoon light.

EXACTLY FIVE plain wooden survey poles with flat red-and-white bands — no numbers, no
letters, no markings — stand upright in a loose line receding up the frame. A
41-year-old man land surveyor in a plain dark-khaki field jacket and worn dark-khaki
canvas field cap stands among them, arms at his sides, head bowed toward the ground,
hands bare and empty. Photographed as a real person, not CGI.

EVERY OBJECT CASTS EXACTLY TWO SHADOWS. Each pole and the man throw one dark, crisp
shadow consistent with the afternoon sun — and a second, fainter, longer shadow forked
roughly 70 degrees away from it, all the faint shadows parallel to each other, all
pointing the same wrong way. Where the two shadows of one object overlap near its
base, the overlap is the darkest patch in the image; each single shadow stays
half-filled by the other light. The sky above is completely empty: one off-frame sun
and nothing else — no second light source, no bright spot, no halo, no flare.

COMPOSITION: The five poles and the man occupy the frame between roughly twenty-two
and sixty-eight percent of frame height, the forked shadow pairs fanning diagonally
across the pale gravel — the dominant graphic pattern of the image. The man stands
left of centre; the tallest pole rises just right of centre. Deep-blue empty sky fills
the top of the frame. Nothing story-critical falls in the top 254 pixels, the bottom
484 pixels, or the right 242 pixels; those bands are covered by platform UI.

LIGHTING: Hard warm afternoon sunlight from frame right on matte chalk-white gravel;
dark warm-edged first shadows, neutral-grey second shadows at sixty percent density.
No bloom, no glow filter, no lens flare, no halo, no visible sun disc.

NEGATIVE: Exactly one human, no second person, no human reflection. Exactly five
poles, exactly two shadows per object, no third shadow. No second sun, no bright spot
in the sky, no glow in the sky. No animals, no birds, no clouds, no trees, no
buildings, no roads. Not miniature, no CGI look, no waxy skin. No bloom, no glow
filter, no lens flare. No text, no letters, no digits, no flag, no logo, no HUD
overlay, no watermark.

Output: 9:16, 1080x1920, no text, no watermark.
```

**120 px testi:** küçültüldüğünde okunması gereken tek şey → *açık zeminde
dikey çizgiler ve her birinin dibinden çıkan V biçimli çatal gölgeler,
çatalların hepsi aynı yöne açılmış.* Yüz ve bantlar okunmazsa sorun değil;
**çatal deseni tek gölgeye iniyorsa ya da gökyüzünde parlak bir şey
belirmişse kapak başarısızdır, yeniden üret.**

> Kapak denetimi 120 px posta pulu testiyle elle yapılır (KAPAK_QA rubriği 12.08.2026'da kaldırıldı).

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ

**Başlık alternatifleri (≤40 karakter):**

```
1. Her şeyin iki gölgesi var
2. Gökyüzünde olmayan güneşin gölgesi
3. İkinci gölge kime ait?
```

**Açıklama (ilk satır kancadır):**

```
Gökyüzünde tek güneş var. Yerde iki güneşin gölgesi.
Ve ikinci gölgeler dönüyor — saat gibi, sahibi görünmeden.
#gizem #fizik #bilimkurgu #shorts #ai
```

**Sabitlenecek yorum:** "İki gölgenin kesiştiği yerin en koyu olması gerçek
fizik — çift kaynaklı aydınlatmanın imzası. Kaynağın görünmemesi ise... 🌗"

---

## 🔒 Master Cinema Lock

```
Photorealistic live-action cinematography, Kodak Vision3 color science,
natural film grain, no digital sharpening. Vertical 9:16 native framing.
One lens per shot (32mm or 75mm), camera distance and height stated in
metres; camera never higher than 1.2 metres. Single continuous 8-second
takes, 0 cuts, one camera move maximum per shot. Real-time motion at
normal playback speed — no slow motion ever. Earth gravity. Matte
surfaces; the sky holds exactly one sun and never any second light, glow
or flare. Exactly two shadows per object (one merged darker shadow only
at the S4 alignment); the faint set rotates clockwise at a steady 1.5
degrees per second. Exactly one human in every frame. No text of any
kind on screen at any moment.
```

---

## 📋 QA SPEC BLOĞU — üretim bitince QA promptlarına kopyalanır

```
FILM: THE WRONG SHADOW (dikey shorts)
FORMAT: 9:16 · 6 sahne × 8 s = 48 s · sahne başına 1 kesintisiz çekim, 0 kesme
İNSAN SAYISI: 1 (6/6 sahne)
CANLI: yok
JALON: TAM 5 — 6 sahnede aynı konumda, hiç ele alınmaz
GÖLGE: nesne başına TAM 2 · soluk set %60 yoğunluk, saat yönünde 1,5°/sn ·
       açı farkı S0 70° → S1 55° → S2 40° → S3 25° → S4 0° (hizalanma,
       tek koyu gölge) → S5 -20° (işaret değişimi) · kesişim en koyu alan
GÖKYÜZÜ: 6/6 sahnede tek güneş, ikinci hiçbir ışık/parlaklık yok;
       güneş hiçbir kadraja girmez
IŞIK: güneş 40°→34°→28°→21°→14°→6° (tek yönde alçalır); birinci gölgeler
       tek yönde uzar; S5'te birinci set söner, soluk set sönmez
LENS: 32mm (S0,S2,S4,S5) · 75mm (S1,S3)
KAMERA: S0 dolly-in · S1 lockoff · S2 tilt-up · S3 lockoff · S4 lockoff ·
       S5 pull-back · yükseklik ≤1,2 m
YASAKLAR: ikinci güneş/gök parlaması · üçüncü gölge · ağır çekim · su ·
          canlı · bulut · rüzgar · metin · ikinci insan
```

---

## ✅ Tutarlılık Kontrol Listesi

```
□ Karakter bloğu 6 görsel promptta birebir aynı mı?
□ Jalon sayısı 6 sahnede TAM BEŞ mi; hiçbirinde ele alınıyor mu?
□ Gölge açı farkı sahne sahne 70→55→40→25→0→-20 sırasını izliyor mu?
□ "1.5 degrees per second" 6 görsel promptta var mı?
□ Kesişim-en-koyu fizik satırı 6 görsel promptta var mı?
□ "The sky contains exactly one sun and nothing else" satırı 6/6 var mı?
□ Güneş yüksekliği tek yönde alçalıyor mu? (40→34→28→21→14→6)
□ Güneş hiçbir kadraja giriyor mu? (girmemeli — flare riski)
□ "No slow motion" 6 video promptunun 6'sında var mı?
□ "Exactly one human" 6 promptta var mı?
□ Hiçbir promptta su, canlı, bulut, rüzgar var mı?
□ Hiçbir figür alt 1/4'e ya da sağ şeride giriyor mu?
□ Ekranda metin süresi 0,0 saniye mi? Jalonlarda rakam/harf var mı?
□ Üretim S4'ten (hizalanma) başladı mı? S4 temiz çıkmadan diğer
  sahneler üretilmedi mi?
```

---

## 🎥 ÜRETİM NOTLARI + QA SONUCU (06.08.2026)

```
DURUM: 🔴 REGENERATE — üretilen kurgu KABUL EDİLMEDİ.

ÜRETİLEN: 64 s · 7 segment (~10 s'lik sahneler + jenerik kartı
"THE DEVIL'S DOUBLE" — isim modele ait, bu dosyada yok).
Plan: 6 × 8 = 48 s · metin 0,0 sn.

ÇEKİRDEK BAŞARISIZLIK: ÇİFT GÖLGE HİÇBİR KAREDE YOK. İki bağımsız QA
merceği (SHORTS_QA Ⓥ 5.6 · SENARYO_QA Ⓥ 3.0) 64 saniyede tek bir
ikinci gölge görmedi; 1,5°/sn dönme davranışı S5'te JALONLARIN
kendisine transfer oldu (havada yatay dönen jalonlar). Bu dosyanın
"EN YÜKSEK RİSK" kaydı üç modu öngörmüştü; gerçekleşen dördüncü mod:
imkansız davranış türetilmiş fenomenden birincil nesneye sıçrar.
→ DERS 73 · DERS 74 · DERS 70 (ikinci vaka)

RAPORLAR: FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_WRONG_SHADOW.md
(belge cevapları + yeniden üretim şartları orada).
```

## 🚪 KAPI KAYDI [DERS 74]

| Tarih | Kapı | Ölçülen | Sonuç |
|---|---|---|---|
| —.08.2026 | Tek-kare fizibilite [D73] | koşulmadı | ⛔ KAYIT YOK |
| —.08.2026 | S4-önce üretim kapısı | koşulmadı ya da sonucu yok sayıldı | ⛔ KAYIT YOK |
| 06.08.2026 | Kurgu kapısı [D70/72] | 7 klip · 64 s · jenerik kartı | 🔴 BATTI |

> Yeniden üretim bu tablonun İLK satırından başlar: S0 görsel promptu tek
> başına koşulur, karede nesne başına TAM İKİ gölge + kesişim-en-koyu
> fiziği okunmadan videoya geçilmez.
