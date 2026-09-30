# 🔬 S30 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · SUSMAYAN_NOBETCI

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
SAHNE:      S30            BAŞLIK: Kapsül vurulur
BÖLÜM:      SUSMAYAN_NOBETCI_BOLUM_3.md
ZAMAN:      300,0 s → 310,0 s       ⛔ FORMÜLLE [D122]: n × 10 (hook S0'ın içinde) · 10 s klip VARSAYIM (K3)
VURUŞ:      BEDEL (numaralı bedel 1)
B5 SATIRI:  BEDEL — kaçış kapsülü yem olarak salınır ve vurulur
⭐VİRAL:    hayır — HAREKET var, YÜZ yok (dış WS) → YÜZ S29'da, HAREKET S30'da; tek sahnede ikisi yok → etiket düşer
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:     S29'da yuvasından ayrılan kapsül çekicinin yanından süzülür; motoru yanar, 3,0 s'de kapsül dikişinden
          ayrılır ve bir parçası dönerek çekicinin kenet halkasına çarpıp halkanın kenarını eğer.
BAŞTA:    (t=0 · IMAGE) üst açı WS: çekici kadrajın sol yarısında, burnu sağa (tahliye gemisine) dönük; SOL yanındaki
          kapsül yuvası BOŞ; turuncu bantlı kapsül yuvanın bir gövde boyu önünde süzülüyor, kıçında düz beyaz koni
          ZATEN YANIYOR (motor sınırda ateşlendi); uzakta sağ üstte uydu ışığı
SONDA:    kapsül iki parça, parçalar dönerek uzaklaşıyor; bir parça çekicinin burnundaki halkanın kenarından sekmiş,
          halkanın bir kenarı içe eğik kalmış (düz dairenin bir yayı içe basık); çekici hafif tepki dönüşünde
⛔ KLİP İÇİ DEĞİŞİM: VAR — ayrılma + halkanın eğilmesi
   Seçim ②: ayrılma HAREKET; halkanın eğilmesi TEMAS·DEĞİŞİM·SONUÇ üçlüsüyle tek anda (parça çarpar 5,0 s ·
   kenar basılır · sonuç 5,5-10 s eğik kenar kadrajda sabit) [D213] — ara durum yazılmaz
ZAMANLAMA: 0,0-3,0 s kapsül yanarak uzaklaşır · 3,0 s çakma ≤6 kare → ayrılma · 5,0 s bir parça halkanın sağ kenarına
           çarpar · 5,5-10,0 s halka eğik, parçalar dönerek küçülür, kristal konisi 2 s'de seyrelir
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  T        İŞARET: ilk kullanım (dönüş S32)
LENS:           35 mm     MESAFE: 40 m from the tug     YÜKSEKLİK: above the tug
ÖLÇEK:          wide shot             AÇI TİPİ: high angle
KADRAJ ENİ:     40 × 36/35 = 41 m → çekici 12 m (%29) + kapsülün ilk 15 m yolu SIĞAR; tahliye gemisi sağ kenar dışında
ANA NESNE PİKSEL: kapsül 2,4 m → 112 px ✅ · kenet halkası 2 m → 94 px ⚠️ (eğilme okunur mu?) → halka kenarına çarpan parça
                  ve basık yay HAREKETLE okunur; SONUÇ S34 (B profil) + S35 (I) + S39 (L 453 px) kurulumlarında tekrar görünür
ÖNCEKİ SAHNEYLE: S29 E (kokpit MS) → T (dış WS): ölçek 1 · mekân değişir ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0   IN FRAME: none   (pilot kokpitte, 40 m'den kanopi ~40 px — yazılmaz)
AYRIM EKSENİ:   çekici = kısa kutu + kanopi + burunda halka · kapsül = turuncu bantlı küçük silindir
GİREN NESNE:    —        ÇIKAN NESNE: kapsül (parçaları kadraj kenarına doğru)
TAŞINAN NESNE:  BOŞ YUVA (S31 · S32 · S44 · S47) · EĞİK HALKA (S34 · S35 · S36 · S39 · S41) · ekranda kanatlar açılır (S31)
BİÇİM KİLİDİ:   ÇEKİCİ ANATOMİ: kanopi 3 pencere paneli · burunda 1 halka 4 kelepçe yuvası · kıçta 1 ana motor · köşelerde
                4 soğuk gaz itici kümesi · sol yanda 1 kapsül yuvası
                KAPSÜL: 1 turuncu bant · 1 motor
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      sert güneş sol üstten kadraj dışı; gövdelerin güneşe bakan üst yüzleri parlak, gölge tarafları mutlak siyah;
           gezegen kenarının soğuk yansıması alt yüzeylere soluk
PALET:     P2 · önceki S29 P1 → değişti ✅
SES:       Y2 — DIŞ SES YOK (vakum): yalnız telsiz taşıyıcı hışırtısı + ağır nefesler (S29'dan) · önceki Y1 → değişti ✅
MÜZİK:     S29'daki tek nota katmanı 3,0 s'de kesilir (kurguda) — vuruşun sesi sessizliktir
FİZİK:     vakum 0 g: parçalar kazandıkları dönüşü sürdürür ("about one turn every three seconds") · kristal düz çizgide ·
           halkaya çarpan parça seker, halkaya YAPIŞMAZ, içinden GEÇMEZ · çekici küçük tepki dönüşü
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (telsizde yalnız nefes)
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (dış WS)
HAREKET:   ayrılan kapsül + sekip halkaya çarpan parça
⛔ etiket düşer — S29 E'nin YÜZ'ü ile çiftlenir (kurguda arka arkaya)
```

## 🎭 İZLEYİCİ CÜMLESİ · KART BAĞI · SON 3 s · ÖLÜ SAHNE BEŞ SORU

```
İZLEYİCİ CÜMLESİ: (insansız) "Kaçış yolunu kendi eliyle gönderdi ve bedel halkaya da sıçradı."
TAŞIYAN KANAL:    nesne (kapsül · halka)
TASK ONLY MU:     — (insansız; şerit B)
KART BAĞI:        ZAAF (halka eğikliği S34-S41) · SINIR (motor kullanımı → S31 kırılır)
ÇAPA ÜÇLÜSÜ:      SEÇİM S29 bedende (başparmak vurmaz, kol sonuna) · BEDEL S30 nesnede · bedenin AFTER'ı S31 (omuzlar
                  inmiş, yan pencerede boş yuva) [D202]
SON 3 s:          parçalar dönerek küçülür, halkanın basık yayı güneşte parlar ve öyle kalır
ÖLÜ SAHNE 5 SORU: ① fiil: süzülme/ayrılma/sekme SÜREÇ ✅ ② direnç: halkaya çarpma ✅ ③ tek kilit: vuruş biçimi ✅
                  ④ sınır: S31 boş yuva + açık kanatlar ✅ ⑤ saat: parçaların dönüş oranı ✅
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D192 (#1) | tek çakma ≤6 kare · ayrılma · dönüş · kristal ≤2 s | üçüncü satır + TIMELINE |
| D213 (#2) | parça 5,0 s halkaya çarpar → kenar basılır → sonuç 5,5-10 s | TIMELINE ikinci/üçüncü satır |
| D198 (#4) | parçalar "about one turn every three seconds, never slowing" | TIMELINE |
| D179 (#9) | IMAGE t=0: kapsül yuvanın önünde, koni yanıyor, halka DÜZ | IMAGE gövdesi |
| D202 (#10) | bedel nesnede + AFTER S31 bedende | S31 IMAGE 0,0 s satırı |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| R1 | ⛔ | vuruş ateş topu/duman | pozitif biçim sayıyla | ✅ |
| R6 | ⛔ | insansız + uzun NEGATIVE → YR | NEGATIVE ≤900 karakter, "human count zero" | ✅ |
| R5 | ⛔ | parça halkanın içinden geçer | "bounces off the ring's edge, nothing passes through" | ✅ |
| Y2 | ⚠️ | kapsül/çekici oranı kayar | "the capsule is about a fifth of the tug's length" | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   orta — insanlı çekicinin yakınında vuruş   sınıf: PB adayı
NÖTR TARİF:  "a small orange-banded capsule drifts ahead of the tug with a straight white engine cone; at 3.0s a single
             white point flashes at its seam and it parts into two pieces that turn away; one piece glances off the
             edge of the tug's nose ring and pushes that edge inward"
⛔ YASAK CÜMLE YAZILMAZ — pozitif kilit: "the pieces keep turning at the same rate; the pressed-in edge of the ring stays pressed in"
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi (03 §3)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları: etiket yok (gerekçe yukarıda)
→ SUSMAYAN_NOBETCI_BOLUM_3.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
