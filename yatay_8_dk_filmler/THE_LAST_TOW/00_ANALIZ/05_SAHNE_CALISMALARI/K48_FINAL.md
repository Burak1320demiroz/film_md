# 🔬 K48 — KİLİT KLİP · FINAL · SAHNE ÇALIŞMASI · THE_LAST_TOW

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları. Bu dosya bitmeden bu klibin promptu yazılmaz.

---

## 🪪 KİMLİK

```
KLİP:       K48  ·  SAHNE S12 (3/3 · KAPANIŞ)      BAŞLIK: ÇEKİCİ GİDER
BÖLÜM:      THE_LAST_TOW_BOLUM_2.md
ZAMAN:      470,0 s → 480,0 s     ⛔ FORMÜLLE: klip başlangıcı(n) = (n−1) × 10,0 s
VURUŞ:      kapanış imajı — K02'nin kafiyesi
B5 SATIRI:  tema kapanıyor
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Resif tam ışıkta; dikişte duran kesici kafası tek yeni işaret.
BAŞTA:           saha ışıkta, kadın kadrajın sağında küçük, dikişte bir şey duruyor
SONDA:           aynı kadraj; kadın iki adım daha uzaklaşmış, işaret yerinde — değişmeyecek
⛔ KLİP İÇİ DEĞİŞİM: VAR — bir eşik geçiliyor (bu rejimde her klip bir
   değişim taşır; ölçülmüş en zayıf eksen, T2V-CompBench 0,0687)
   Seçim: ② ARA DURUM cümlesi prompta yazılıyor
   Gerekçe: kapanışta değişim en KÜÇÜK olmalı: kafiye çiftinin okunması için kadraj K02 ile birebir aynı kalıyor, değişen yalnız ışık ve tek yeni nesne
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: KAFİYE — K02 ile aynı konum, yükseklik ve lens
LENS:           18 mm     MESAFE: 9,0 m     YÜKSEKLİK: 0,30 m
ÖLÇEK:          EWS (1)        AÇI TİPİ: zemin
KADRAJ ENİ:     18,0 m      ⛔ HESAPLANDI (36 mm / f × mesafe)
                          kadraja alınacak nesne resif sırtı 18 m + kesici kafası (kameradan 4,5 m'de) → SIĞIYOR ✅
ANA NESNE PİKSEL: 196 px   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  ölçek kademesi 1 (WS 2 → EWS 1) · azimut 75°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 — kadrajın sağında, yüksekliği 0,11 × kadraj eni
AYRIM EKSENİ:   n/a (ikinci giysi kadrajdan çıktı — çekiciyle gitti)
GİREN NESNE:    —
ÇIKAN NESNE:    çekici ve ikinci giysi (K47'de çıktı)
TAŞINAN NESNE:  kesici kafası — K43'ten beri dikişte, kalıcı
⛔ BİÇİM KİLİDİ: ⭐ kamera metni K02'den BİREBİR kopyalanır + kafiye işaret satırı taşınır
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      bütün saha ışıkta; dikey yüzeyler 370 K'de parlak, gölgeler uzun ve sert, dolgu 0
           ışık takvimi: gölge kenarı dikişe sahayı geçti — gölge kalmadı · monotonik ✅ (tek yön)
PALET:     IŞIK   ⛔ önceki sahneyle aynı değil
SES:       çekicinin gövde sesi uzaklaşıyor, sonra yalnız vizör içindeki nefes
MÜZİK:     var — tek katman, son 4 saniyede çekiliyor
FİZİK:     0,30 g · hard vakum · metalin üstünde 0 kare toz · gölge mutlak
           siyah, dolgu 0 · pas 0 · kıvılcım 0 · dışarıda ses yok
```

## 🎙️ REPLİK

```
REPLİK:    — (film boyu 0 replik)
İŞLEV:     — ⛔ boş replik yazılmadı, SİLİNMİŞ sayılmaz: SPEC'te sayıyla 0
AĞIZ:      okunmuyor — ağız vizör ardında ve film boyunca konuşmuyor
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
— (kapanış imajı ⭐VİRAL ölçütü taşımaz; işlevi TEMA)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D141 | kafiye çifti ekranda, niyette değil | kamera metni K02 ile birebir; SPEC B'de sayıyla |
| D210 | lockoff ve kafiye niyette kalmaz | `locked-off` + `the same position, height and lens as Clip 2` |
| D62 | montajda en çok düşen sahne final | SPEC A: K46-K48 kesilemez; üretim sırası K48'i üçüncü halkaya koyuyor |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 6 | ⚠️ | final kuyrukta kayboluyor / eksik üretiliyor (U-6) | K48 üretim sırasının 3. halkası; teslim satırında sahne sayısı ölçülecek | ⬜ üretimde |
| 3 | ⚠️ | uzak nesne <100 px okunmuyor | kesici kafası kameradan 4,5 m'de konumlandı → 196 px | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır
NÖTR TARİF:  —
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilit: `the cutter head stands in the seam, its shank locked between the two faces` — durum yazılır, hikâye yazılmaz
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 196 px ≥ 100
☑ önceki kliple ardışık çift bant içi (✅)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları gerekmedi
→ hepsi ✅ → THE_LAST_TOW_BOLUM_2.md'ye bu klibin IMAGE + VIDEO promptu yazılabilir
```
