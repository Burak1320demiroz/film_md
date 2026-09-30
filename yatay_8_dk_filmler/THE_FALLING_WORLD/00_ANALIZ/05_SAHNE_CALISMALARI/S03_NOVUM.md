# 🔬 S03 — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · THE_FALLING_WORLD

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
SAHNE:      S03  (sahibin V04'si)      BAŞLIK: Sırttaki gemi
BÖLÜM:      THE_FALLING_WORLD_BOLUM_1.md      DRAMATİK SAHNE: D2 · Tek çıkış (S03-S07)
ZAMAN:      30 s → 40 s       ⛔ FORMÜLLE [D122]: sahne(n) = n × 10 s
VURUŞ:      ② Kurulum (%0-10) — hedef ilan edilir
B5 SATIRI:  BEDEL① izi — numuneler gitti; BEYAZ'ın kemerindeki kanca BOŞ
⭐VİRAL:    HAYIR
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            İkisi araca koşarken ileride kaya sırtındaki küçük kaçış gemisi görünür.
BAŞTA:           iki gövde yarıktan uzaklaşıyor, kadrajın derinliğinde henüz araç yok
SONDA:           araç kadrajda, arkasında kaya sırtı ve üstünde küçük gemi okunuyor
⛔ KLİP İÇİ DEĞİŞİM: VAR — ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687).
   Seçim: ② ARA DURUM YASAĞI cümlesi prompta yazılır
   Gerekçe: hedefin görünmesi bu klibin İŞİDİR; sınıra taşınırsa kurulum vuruşu boşa çıkar
   ARA DURUM YASAĞI: the ship is either out of frame or fully visible; it never fades or brightens into view
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: DÖNÜŞ S00 (3 sahne sonra)
⛔ Kamera metni S00'dan BİREBİR kopyalanır ve işaret satırı taşınır:
"— the same position, height and lens as Scene 0."
LENS:           24 mm     MESAFE: 6 m     YÜKSEKLİK: ground level
ÖLÇEK:          medium long shot        AÇI TİPİ: low angle
KADRAJ ENİ:     9,0 m      ⛔ HESAPLANDI (§5.2): kesir = boyut × odak ÷ (mesafe × sensör)
                          Kadraja alınacak nesne iki koşan gövde + araç, derinlikte gemi — 9,0 m ön düzleme girer
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: insan 405 px (ön düzlem) · gemi 8 m / 900 m → 171 px sırt üstünde ✅   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S02 (B · CU · high angle · 270°) → S03 (A · MLS · low angle · 0°) = 2 kademe + 90° ✅ bant içi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   2 — BEYAZ sol üçte bir · TURUNCU sağ üçte bir, ikisi de kameradan UZAKLAŞIYOR
⛔ FİLM BOYU KİLİT: BEYAZ kadrajın SOL üçte birinde · TURUNCU SAĞ üçte birinde;
   merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
AYRIM EKSENİ:   ÜÇ kanal birden — ① RENK (kirli beyaz + kobalt mavi omuz ↔ yanık
                turuncu + siyah üst kol) ② OMUZ GEOMETRİSİ (köşeli geniş sırt ünitesi
                ↔ dar dikdörtgen sırt ünitesi) ③ KONUM (sol ↔ sağ üçte bir).
                ⛔ Yalnız RENK yetmez — uzaklaşan gövdelerde renk küçülür; ayrımı SIRT ÜNİTESİ SİLUETİ taşır (köşeli geniş ↔ dar dikdörtgen)
GİREN NESNE:    keşif aracı (hasarsız durum) · kaçış gemisi (uzak, kaya sırtında)
ÇIKAN NESNE:    numune sandığı KALICI olarak çıktı (S02) — izi BOŞ KEMER KANCASI olarak taşınıyor
TAŞINAN NESNE:  sarı ortak halat (S00'dan) · sol önkoldaki alet (S02'den) · boş kemer kancası (S02'den) → S04'e
⛔ BİÇİM KİLİDİ: METİNLE TUTULMUYOR [D146] → referans sayfası ŞART: R1 BEYAZ (hasarsız) · R2 TURUNCU · R4 ARAÇ VE GEMİ (iki varlık da ilk kez burada)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      aynı tek güneş sol üstten; uzaklaşan gövdeler güneşe karşı, sırt üniteleri koyu leke
           ışık takvimi: tek güneş film boyu SABİT saat yönünde (sol üst, kadraj
           dışı); ardışık sahne arası fark ≤30° ve ≤500 K · monotonik: ✅
PALET:     P1 açık yüzey
           ⛔ önceki sahneyle aynı değil: S02 de P1'di ama ölçek 2 kademe ve açı 90° değişiyor; örüntü kırıcı ÖLÇEK üzerinden tutuyor
SES:       Y1 — boğuk uğultu + çift nefes; nefes ritmi S02'ye göre HIZLANMIŞ (koşu kadansı)
           ⛔ önceki sahneyle aynı doku değil: aynı doku ama kadans değişti; S04'te doku Y2'ye geçiyor
MÜZİK:     İLK GİRİŞ — 2 saniye, tek uzun alt kat; 0:30'da girer
FİZİK:     §3.2 İNCE ATMOSFER + 0,30 g [D74 kaydı]. 0,30 g'de koşu adımı UZUN ve HAVADA KALMA süresi yüksek: her adım ≈0,9 s havada. Toz her basışta bir avuç kalkar ve yavaş iner.
```

## 🎙️ REPLİK

```
REPLİK:    — (sahnede replik yok)
İŞLEV:     — hedefin görünmesi SÖZLE değil KADRAJLA yapılır
AĞIZ:      okunmuyor
```

## ⭐VİRAL

```
⭐VİRAL DEĞİL — bu sahne kurulum vuruşudur, ölçütsüz ⭐ etiketi DÜŞER
[SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D209 | World Bible ÜÇ cümle birebir: zemin · ufuk · gökteki diskin yönü | bu sahne dünyanın ilk GENİŞ okunuşudur; üç cümle tam ve birebir girer |
| D42 | Kir merdiveni tek yönlü, geri dönmez | S00-S02'nin tozu üstlerinde; BEYAZ sağ diz + sırt altı, TURUNCU iki diz |
| D167 | Figür başına en çok üç öznitelik: giysi rengi · omuz parçası · sırt ünitesi | uzak kadrajda yalnız bu üçü yazılır; yaş/boy/ten PLAN'da kalır |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | D146 — araç ve gemi biçim kilidi ilk kez metinle tutulacak | R4 sayfası KAPI 0; araç ve gemi cümleleri promptta TAM yazılır, "as in the reference" YASAK | ✅ |
| 2 | ⚠️ | KART 13 — uzaktaki gemi maket okunabilir | gemi yanında ölçek şahidi: kaya sırtı ve insan boyu aynı karede; "no miniature read" negatifi | ✅ |
| 3 | ⚠️ | KART 6b — bölge geçişi (yüzey → araç kabini S04'te) | güneş yönü sabit; S04'ün kabin ışığı AYNI dış kaynaktan gelir | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR
SINIF:       —
NÖTR TARİF:  alet hâlâ önkolda ve düz; adlandırılmaz
⛔ NOVUM NOTU (dürüst kayıt): filmin novumu İLİŞKİ tipidir ve tek kare testini
  S41 geçer (`02_KONSEPT_VE_RISK` §3). S03 novumun İLK SONUCUNU taşır: dünyanın
  kuralı S01-S02'de kurulmuştur (bir hat kesilir, biri kalır) ve S03 o kuralın
  bedelini kadrajda gösterir — BOŞ KEMER KANCASI + TEK gemi. Kural cümlesi:
  bu dünyada kimse kendini kurtaramaz; her kurtuluş, birini bağlayan hattın
  BAŞKASI tarafından kesilmesidir.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve insan 405 px (ön düzlem) · gemi 8 m / 900 m → 171 px sırt üstünde ✅
✅ önceki sahneyle ardışık çift bant içi
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL değil — YÜZ/HAREKET satırları gerekmiyor
→ hepsi ✅ — THE_FALLING_WORLD_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu YAZILABİLİR
```
