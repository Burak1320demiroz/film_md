# 🔬 S47 — KİLİT SAHNE · FINAL · SAHNE ÇALIŞMASI · THE_FALLING_WORLD

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
SAHNE:      S47  (sahibin V48'si)      BAŞLIK: Uzaklaşan gemi
BÖLÜM:      THE_FALLING_WORLD_BOLUM_4.md      DRAMATİK SAHNE: D9 · İki kişi (S45-S47)
ZAMAN:      470 s → 480 s       ⛔ FORMÜLLE [D122]: sahne(n) = n × 10 s
VURUŞ:      ⑪ Kapanış imajı (%98-100)
B5 SATIRI:  KAPANIŞ — İSTEK karşılandı, ENGEL ortamda KALDI (tek açık uç)
⭐VİRAL:    HAYIR
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Küçük gemi yarılmış yüzeyden uzaklaşır; kara delik gökyüzünü doldurur.
BAŞTA:           gemi kadrajın alt üçte birinde, altında yarılmış yüzey okunuyor
SONDA:           gemi kadraj eninin üçte birinden küçük, yüzey kadrajın alt kenarında, disk gökyüzünü dolduruyor
⛔ KLİP İÇİ DEĞİŞİM: VAR — ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687).
   Seçim: ② ARA DURUM YASAĞI cümlesi prompta yazılır
   Gerekçe: uzaklaşma bu klibin İŞİDİR; kapanış imajı değişimin KENDİSİDİR
   ARA DURUM YASAĞI: the ship only moves away; it never grows, never turns back, never stops
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  H        İŞARET: ilk ve tek kullanım
(dönüşü yok — kapanış kurulumu filmde bir kez kullanılır; 24 kurulumun
tek kullanımlıkları: G · H · O · T · U dışı hepsi ≥2)
LENS:           24 mm     MESAFE: 60 m     YÜKSEKLİK: level with the ship's path
ÖLÇEK:          wide shot        AÇI TİPİ: eye level
KADRAJ ENİ:     90,0 m      ⛔ HESAPLANDI (§5.2): kesir = boyut × odak ÷ (mesafe × sensör)
                          Kadraja alınacak nesne gemi 8 m + yüzey kenarı + disk — 90,0 m üçünü birden alır
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: gemi 8 m → %8,9 kare genişliği = 171 px ✅ (300 m'de 34 px olurdu; mesafe HESAP SONUCU düzeltildi)   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S46 (Z · MS · low angle · kabin) → S47 (H · WS · eye level · gök) = 1 kademe + mekân değişir ✅ bant içi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — kadrajda insan gövdesi YOK. İnsan varlığı İKİ KABİN IŞIĞIYLA sayılır (2)
⛔ FİLM BOYU KİLİT: BEYAZ kadrajın SOL üçte birinde · TURUNCU SAĞ üçte birinde;
   merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
AYRIM EKSENİ:   ÜÇ kanal birden — ① RENK (kirli beyaz + kobalt mavi omuz ↔ yanık
                turuncu + siyah üst kol) ② OMUZ GEOMETRİSİ (köşeli geniş sırt ünitesi
                ↔ dar dikdörtgen sırt ünitesi) ③ KONUM (sol ↔ sağ üçte bir).
                ⛔ Yalnız RENK yetmez — insan kadrajda olmadığı için ayrım sorunu yok; SAYIM iki ışıkla yapılır [D141]
GİREN NESNE:    —
ÇIKAN NESNE:    gezegen yüzeyi KALICI olarak çıkıyor (kimse dönmeyecek)
TAŞINAN NESNE:  kabin kapısının dışında sallanan KESİK sarı uç — son nesne eki (S44'ten)
⛔ BİÇİM KİLİDİ: METİNLE TUTULMUYOR [D146] → referans sayfası ŞART: R4 ARAÇ VE GEMİ (gemi dış biçimi) — R1/R2/R3 bu karede kadrajda değil
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      aynı tek güneş sol üstten (film boyu sabit) + merceklenmiş diskin sabit yönü; gemi gövdesi üstten aydınlık, altı gezegen yansımasıyla soluk
           ışık takvimi: tek güneş film boyu SABİT saat yönünde (sol üst, kadraj
           dışı); ardışık sahne arası fark ≤30° ve ≤500 K · monotonik: ✅
PALET:     P1 açık yüzey (uzaktan)
           ⛔ önceki sahneyle aynı değil: S46 P6 kabin içiydi; dış/iç geçişi kapanışın kendisidir
SES:       Y1 — boğuk uğultu UZAKLAŞIYOR; son 2 saniyede yalnız alt kat kalır
           ⛔ önceki sahneyle aynı doku değil: S46 Y6 idi (fan + net telsiz); ses kapanışı mekân kapanışıyla aynı anda
MÜZİK:     VAR — tek uzun alt kat, 478. saniyede kesilir; son 2 saniye SESSİZ değil, yalnız uğultu
FİZİK:     §3.2 İNCE ATMOSFER + 0,30 g [D74 kaydı]. 0,30 g: gemi yükselirken ivmesi düşük çekimde DÜŞÜK görünmez — motor itisi gövdeyi 10 saniyede ≈400 m uzaklaştırır. Yüzeyden kalkan toz gemiyi izlemez, yerinde yavaş iner.
```

## 🎙️ REPLİK

```
REPLİK:    — (sahnede replik yok)
İŞLEV:     — kapanış sözsüzdür; son replik S46'da
AĞIZ:      okunmuyor (kadrajda insan yok)
```

## ⭐VİRAL

```
⭐VİRAL DEĞİL — kapanış imajı ⭐ etiketi almaz; işlevi TUTMAK değil BIRAKMAKTIR
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D141 | SPEC B FİNAL VURUŞ KANITI: iki kabin ışığı SAYILIR (2) ve gemi kadraj eninin üçte birini geçmez | iki ışık lekesi promptta SAYIYLA yazılır; gemi %8,9 kadraj eni — üçte birin çok altında ✅ |
| D202 | Çapa üçlüsünün FINAL ayağı | BEFORE (S00): iki gövde yerde, biri yarıkta · AFTER (S47): gövde yok, iki ışık var. Aynı kanal: SAYIM |
| D209 | World Bible ÜÇ cümle birebir: zemin · ufuk · diskin yönü | kapanış karesi üçünü de taşıyan TEK karedir; SPEC C DÜNYA ÇAPASI 3/3 |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | KART 10 — insansız sahne + uzun NEGATİF blok = yapısal red | bu sahnenin NEGATIVE bloğu <900 karakter; insana ait negatif cümleler (çıplak deri · yüz morfu · ikinci figür) DÜŞER | ✅ |
| 2 | ⚠️ | KART 13 — gemi maket okunabilir | ölçek şahidi: yarılmış yüzeyin kenarı ve yarık genişliği aynı karede; "no miniature read, no tilt-shift" negatifi | ✅ |
| 3 | ⚠️ | Kara delik kurgu/bilim sınırı | disk SABİT yönde, hiçbir sarsıntıda nabız atmaz, BÜYÜMEZ. Gelgit çöküşünün hızı KURGUDUR ve YAYIN_PAKETI VERIFIED SCIENCE satırlarına GİRMEZ | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR — kadrajda insan yok, alet yok, temas yok
SINIF:       — (tek kalem: KART 10 yapısal red profili, yukarıda kapatıldı)
NÖTR TARİF:  —
⛔ YASAK CÜMLE YAZILMAZ; NEGATIVE bloğu KISALTILMIŞ çekirdektir.
  POZİTİF KARŞILIĞI: the small ship keeps moving away from the split surface
  for the whole clip, two cabin lights steady in its flank.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve gemi 8 m → %8,9 kare genişliği = 171 px ✅ (300 m'de 34 px olurdu; mesafe HESAP SONUCU düzeltildi)
✅ önceki sahneyle ardışık çift bant içi
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL değil — kapanış imajı, gerekçesi yazıldı
→ hepsi ✅ — THE_FALLING_WORLD_BOLUM_4.md'ye bu sahnenin 📸 + 🎥 promptu YAZILABİLİR
```
