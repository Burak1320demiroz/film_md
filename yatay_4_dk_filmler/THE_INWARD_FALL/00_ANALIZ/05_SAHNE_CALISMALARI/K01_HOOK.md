# 🔬 S01 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · THE_INWARD_FALL

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
SAHNE:      S01 (K01 · 1/3 KURULUM)    BAŞLIK: Jant Zemini
BÖLÜM:      THE_INWARD_FALL_BOLUM_1.md
ZAMAN:      0.0 s → 10.0 s       ⛔ FORMÜLLE [D122]: 0.0 + (1-1)*10.0
VURUŞ:      1 (Durum / Hook)     B5 SATIRI: İSTEK
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Dış jant zemininde düşen çelik pim yana kavisle saparak tırabzan ayağına çarpar.
BAŞTA:           Teknisyenin elindeki 15 cm çelik pim eldivenden kayıp zemin yönünde serbest düşüşe geçer.
SONDA:           Pim dikey düşmek yerine 1.4 m düşüşte 0.6 m geriye saparak tırabzan ayağına çarpar.
⛔ KLİP İÇİ DEĞİŞİM: YOK (pimin düşüş ve sapma kavisi tek sürekli fiziksel süreçtir).
   Seçim: ① değişimi sahne sınırına taşı   Gerekçe: K02'de gövde savrulması eylemine bağlanır
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: ilk kullanım
LENS:           35 mm     MESAFE: 3.2 m     YÜKSEKLİK: 1.4 m
ÖLÇEK:          LS        AÇI TİPİ: göz hizası (0° azimut)
KADRAJ ENİ:     3.5 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne ve tırabzan 2.8 m
                          Sığıyor mu: EVET
ANA NESNE PİKSEL: 220 px  ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: açılış karesi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (isimsiz teknisyen)
AYRIM EKSENİ:   Grafit gri EVA tulumu ve parlak sarı reflektör şeritleri; kask vizörü yarı-ayna altın kaplama
GİREN NESNE:    Yok      ÇIKAN NESNE: Yok
TAŞINAN NESNE:  Çelik pim → sonraki K02'de zeminde görünür
⛔ BİÇİM KİLİDİ: Referans Paketi R1 (EVA giysisi) ve R2 (jant zemin profili) kilitlendi [D146]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Soğuk çelik gri, axial skimming ışık 15° (dönme eksenine paralel) · monotonik sabit
PALET:     Soğuk çelik gri, mat siyah kafes, sarı ikaz çizgileri
SES:       Vakum bas tıkırtısı + 120 Hz derin itici türbin iniltisi
MÜZİK:     yok (saf diegetik mekanik sesler)
FİZİK:     0.4g dönme yerçekimi (5 RPM, R=60m); serbest düşen nesnede Coriolis sapması (a = 2ω×v)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor — diyalogsuz film, vizör arkasında ağız kapalı
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       —
HAREKET:   —
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D157 · Novum | Cümle taşıyıcı nesnenin adını içerir | "steel pin deflects sideways" kelimeleri açıkça yazılacak |
| D192 · Risk A5 | 1 numaralı risk pozitif sayıyla kilitlenir | "falls 1.4 m with a 0.6 m lateral parabolic curve" yazılacak |
| D200 · İki Yerçekimi | Dönme yerçekimi ve Coriolis ayrımı | "rotational centrifugal acceleration pushes body to floor" belirtilecek |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | Serbest düşen parçayı model düz düşürür | 0.6 m kavisli yana sapma sayısı yazıldı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR   sınıf: PK
NÖTR TARİF:  15 cm uzunluğunda silindirik çelik montaj pimi zemin kafesine çarpar; tehlikeli cisim veya silah değildir.
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilittir: Teknisyenin elleri eldivenli ve açıkça tırabzana uzanır vaziyettedir.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi (açılış karesi)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil (K03 viral)
→ hepsi ✅ ise THE_INWARD_FALL_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
