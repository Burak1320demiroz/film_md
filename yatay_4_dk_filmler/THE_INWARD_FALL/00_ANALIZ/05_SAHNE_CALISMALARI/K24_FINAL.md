# 🔬 S06 (K24) — KİLİT SAHNE · FINAL · SAHNE ÇALIŞMASI · THE_INWARD_FALL

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
SAHNE:      S06 (K24 · 4/4 KARAR / FINAL)    BAŞLIK: Serbest Atalet
BÖLÜM:      THE_INWARD_FALL_BOLUM_2.md
ZAMAN:      230.0 s → 240.0 s     ⛔ FORMÜLLE [D122]: 0.0 + (24-1)*10.0
VURUŞ:      8 (Çözüm / Final)     B5 SATIRI: MUHATAP
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Tahliye kapsülü merkez akstan fırlar; dönen jant geride kalarak uzayda küçülür.
BAŞTA:           Beyaz endüstriyel tahliye kapsülü istasyonun merkez aksındaki silindirik yuvadan pnömatik itkiyle düz hat boyunca ayrılır.
SONDA:           Kapsül uzay derinliğine doğru düz çizgide uzaklaşırken, arka planda 8 RPM devirle kontrolden çıkmış devasa istasyon jantı sessizce döner.
⛔ KLİP İÇİ DEĞİŞİM: YOK (kapsülün doğrusal eksenel uzaklaşması tek süreçtir).
   Seçim: ① değişimi sahne sınırına taşı   Gerekçe: Final karesidir, döngüyü kapatır
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  J        İŞARET: ilk kullanım
LENS:           20 mm     MESAFE: 15.0 m    YÜKSEKLİK: 0.0 m
ÖLÇEK:          ELS       AÇI TİPİ: göz hizası (0° azimut)
KADRAJ ENİ:     12.0 m    ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne ve istasyon silueti 9.5 m
                          Sığıyor mu: EVET
ANA NESNE PİKSEL: 210 px  ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: K23→K24 ölçek MCU→ELS (Δ=4) · azimut -45°→0° (45°) → bant içi: EVET (bilinçli final şoku: merkez kovandan sonsuz uzaya açılış)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0   ⛔ film boyu KİLİT: 1 (insan tahliye kapsülünün içindedir, dış kadraj boştur)
AYRIM EKSENİ:   Beyaz mat kapsül gövdesi, koyu gri dönen jant silueti ve sonsuz derin uzay
GİREN NESNE:    Yok      ÇIKAN NESNE: Tahliye kapsülü (merkezden uzaklaşır)
TAŞINAN NESNE:  İstasyon jantı (K01'deki yapı uzakta kalır — KAFİYE döngüsü)
⛔ BİÇİM KİLİDİ: Referans Paketi R2 (istasyon geometrisi ve tahliye kovanı) kilitlendi [D146]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Sonsuz uzay siyahı, axial skimming güneş ışığı 15° (değişmeyen sabit eksenel açı)
PALET:     Mat beyaz kapsül, titanyum gri istasyon jantı, derin uzay siyahı
SES:       Tam vakum mutlak sessizliği; mekanik sesler tamamen kesilir
MÜZİK:     yok (sessizlik kapanışı)
FİZİK:     0.0g tam ağırlıksızlık; dönmeyen eksenden düzgün doğrusal atalet hareketi (Newton 1. Yasa)
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
| D210 · Açılış Kapanış Çifti | KAFİYE: Değişen tek değişken sisteme bağlılıktır | "escape capsule drifts in pure inertial straight line away from spinning ring" yazılacak |
| D214 · Self-Contained | Tüm istasyon ve kapsül detayları promptta eksiksizdir | "white cylindrical escape pod, massive rotating ring structure in background" yazılacak |
| D200 · Ağırlıksızlık | Doğrusal atalet hareketi | "uniform rectilinear drift in zero gravity with no tumble" yazılacak |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Dönen jantın perspektifi ve kapsülün rotası bozulabilir | Eksenel bakış ve doğrusal ayrılma pozitif kilitlendi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR   sınıf: PK
NÖTR TARİF:  Tahliye kapsülü uzay istasyonundan ayrılarak sessizce uzaklaşır; saf teknik uzay aracı ayrılmasıdır.
⛔ YASAK CÜMLE YAZILMAZ — karşılığı POZİTİF kilittir: Kapsül düzgün hat boyunca süzülür.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
☑ önceki sahneyle ardışık çift bant içi (bilinçli final şoku gerekçeli)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil
→ hepsi ✅ ise THE_INWARD_FALL_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
