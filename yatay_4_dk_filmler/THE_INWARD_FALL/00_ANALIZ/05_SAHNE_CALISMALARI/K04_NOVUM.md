# 🔬 S02 (K04) — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · THE_INWARD_FALL

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
SAHNE:      S02 (K04 · 1/4 BELİRİŞ)    BAŞLIK: Servis Koridoru
BÖLÜM:      THE_INWARD_FALL_BOLUM_1.md
ZAMAN:      30.0 s → 40.0 s       ⛔ FORMÜLLE [D122]: 0.0 + (4-1)*10.0
VURUŞ:      3 (Tırmanış Başlangıcı / Novum)   B5 SATIRI: ENGEL
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Artan yapay yerçekimi (1.0g) altında merdiven sütununa doğru ağır adımlarla bakar.
BAŞTA:           Teknisyen servis rayı üzerinde durur; bacaklarına binen merkezkaç yükü 0.4g'den 1.0g'ye yükselmiştir.
SONDA:           Teknisyen kafes merdiven sütununun tabanına yönelir, ağırlaşan tulum adımlarını zorlar.
⛔ KLİP İÇİ DEĞİŞİM: YOK (artan yükün getirdiği ağırlaşma duruşu tek süreçtir).
   Seçim: ① değişimi sahne sınırına taşı   Gerekçe: K05'te manyetik botların raydan sökülüşüne bağlanır
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  D        İŞARET: ilk kullanım
LENS:           40 mm     MESAFE: 2.8 m     YÜKSEKLİK: 1.1 m
ÖLÇEK:          MLS       AÇI TİPİ: alt açı (45° azimut)
KADRAJ ENİ:     2.8 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne ve koridor 2.2 m
                          Sığıyor mu: EVET
ANA NESNE PİKSEL: 310 px  ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: K03→K04 ölçek MCU→MLS (Δ=1) · azimut -45°→45° (90°) → bant içi: EVET
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (isimsiz teknisyen)
AYRIM EKSENİ:   Grafit gri EVA tulumu, sarı reflektör şeritler, koyu titanyum koridor panelleri
GİREN NESNE:    Yok      ÇIKAN NESNE: Yok
TAŞINAN NESNE:  Tırabzan rayı → sonraki K05'te bot tabanlarıyla temas eder
⛔ BİÇİM KİLİDİ: Referans Paketi R1 ve R2 kilitlendi [D146]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Titanyum gri ve sarı reflektör, sert yan gölge (axial skimming ışık 15°)
PALET:     Titanyum gri, sarı ikaz reflektörleri, mat siyah raylar
SES:       Metal esneme gıcırtısı + 180 Hz rezonans uğultusu
MÜZİK:     yok
FİZİK:     1.0g artan yapay yerçekimi (8 RPM dönme devri); dönen silindir tabanında dikey baskı
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       —
HAREKET:   —
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D200 · İki Yerçekimi | Dönen jantta 1.0g yerçekimi baskısı | "centrifugal weight of 1.0g compresses heavy EVA boots to deck" yazılacak |
| D209 · Dünya Çapası | Tünel ve merdiven eksen geometrisi | "straight axis of radial ladder column provides structural horizon" yazılacak |
| D206 · Bedel Bedende | Ağırlığın gövdede hissedilmesi | "knees flex under heavy downward pull" yazılacak |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | Model sıradan Dünya yürüyüşü üretir | Ağırlaşan 1.0g yükü ve diz esnemesi pozitif tarif edildi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR   sınıf: PK
NÖTR TARİF:  Teknisyen servis tüneli rayı üzerinde tırabzana tutunarak adımlar; endüstriyel tesis yürüyüşüdür.
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilittir: İki el de tırabzana sağlamca temas halindedir.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil
→ hepsi ✅ ise THE_INWARD_FALL_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
