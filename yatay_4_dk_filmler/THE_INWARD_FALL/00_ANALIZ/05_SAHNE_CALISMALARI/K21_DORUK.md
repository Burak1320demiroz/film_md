# 🔬 S06 (K21) — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · THE_INWARD_FALL

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
SAHNE:      S06 (K21 · 1/4 BELİRİŞ / DORUK)   BAŞLIK: Kovanı Yakalama
BÖLÜM:      THE_INWARD_FALL_BOLUM_2.md
ZAMAN:      200.0 s → 210.0 s     ⛔ FORMÜLLE [D122]: 0.0 + (21-1)*10.0
VURUŞ:      7 (Doruk)             B5 SATIRI: MUHATAP
⭐VİRAL:    evet                  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Sıfır-g merkez kovanına uçan teknisyen iki eliyle tahliye tutamağını yakalar.
BAŞTA:           Teknisyen tam ağırlıksızlıkta merkez aksına doğru süzülmektedir; kovanın titanyum tutamak barı yaklaşır.
SONDA:           İki eldivenli el metalik tutamağa kilitlenir; vizörde arkasında 8 RPM ile dönen jantın altın silueti parlar.
⛔ KLİP İÇİ DEĞİŞİM: YOK (süzülüş ve kenetlenme tek sürekli kinematik süreçtir).
   Seçim: ① değişimi sahne sınırına taşı   Gerekçe: K22'de dönen jantı sabit merkezden izleme vuruşuna bağlanır
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  H        İŞARET: ilk kullanım
LENS:           50 mm     MESAFE: 1.2 m     YÜKSEKLİK: 1.0 m
ÖLÇEK:          MCU       AÇI TİPİ: alt açı (30° azimut)
KADRAJ ENİ:     1.1 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 0.9 m
                          Sığıyor mu: EVET
ANA NESNE PİKSEL: 440 px  ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: K20→K21 ölçek MLS→MCU (Δ=1) · azimut -90°→30° (120°) → bant içi: EVET
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 (isimsiz teknisyen)
AYRIM EKSENİ:   Grafit gri EVA tulumu, altın vizör, parlak titanyum tutamak ve sonsuz uzay siyahı
GİREN NESNE:    Merkez kovan tutamağı     ÇIKAN NESNE: Yok
TAŞINAN NESNE:  Teknisyen gövdesi → sonraki K22'de kovana asılı durur
⛔ BİÇİM KİLİDİ: Referans Paketi R1 ve R2 kilitlendi [D146]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Sonsuz uzay siyahı ve altın vizör parlaması, merkez eksen ışığı (axial skimming ışık 15°)
PALET:     Altın sarısı, titanyum gri, derin uzay siyahı
SES:       Mutlak vakum sessizliği ardından gövdeden kaska iletilen tok metalik kenetlenme darbesi
MÜZİK:     yok
FİZİK:     0.0g tam ağırlıksızlık; dönmeyen merkez ekseninde sıfır merkezkaç
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       Vizörün yarı-ayna altın yüzeyinde, teknisyenin arkasında 8 RPM hızla fırıl fırıl dönen devasa istasyon jantının distorsiyonlu yansıması ve vizör ardında şokla açılmış göz bebekleri (≥374 px)
HAREKET:   İki eldivenin metalik tutamağa şiddetle çarpıp kenetlenişi ve havada serbest süzülen mikro buz kristallerinin kaska saçılışı
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D208 · Vizör Kimliği | Kask vizörü yarı-ayna altın yansıtıcıdır | "gold-reflective semi-mirrored visor reflecting the spinning rim" yazılacak |
| D202 · İrade ve Seçim | Karakterin doruk kurtuluş hamlesi | "both gloved hands lock firmly around titanium grab bar" yazılacak |
| D200 · Sıfır-g Fiziği | Tam ağırlıksızlık dinamiği | "perfect zero-g float with motionless center axis" yazılacak |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | Kask vizör ve tulum tutarsızlığı | Referans Paketi R1 panelleri birebir kilitlendi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR   sınıf: PK
NÖTR TARİF:  İki eldivenli el merkez kovan tutamağına kenetlenir; teknik tutunma eylemidir.
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilittir: Parmaklar tutamağı kavrayarak sıfır-g'de sabitlenir.
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
☑ ⭐VİRAL YÜZ + HAREKET satırları var
→ hepsi ✅ ise THE_INWARD_FALL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
