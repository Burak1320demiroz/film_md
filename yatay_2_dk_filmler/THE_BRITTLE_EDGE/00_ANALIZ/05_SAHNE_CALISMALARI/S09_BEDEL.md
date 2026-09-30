# 🔬 S09 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_BRITTLE_EDGE

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
SAHNE:      S09            BAŞLIK: Askıda
BÖLÜM:      THE_BRITTLE_EDGE_BOLUM_2.md
ZAMAN:      90 s → 100 s       ⛔ FORMÜLLE [D122]: 0 + 9 × 10 = 90s - 100s
VURUŞ:      Doruk / Askıda Kriz        B5 SATIRI: MUHATAP
⭐VİRAL:    evet             → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Araç uçurum üzerinde tamamen askıda kalır; yeni sapan bağlantısı tüm kütleyi sırtlayarak dengede tutar.
BAŞTA:           Araç S08'in son karesindeki konumunda, tekerlekler boşlukta, sapan son derece gergin durumdadır.
SONDA:           Vinç yukarı çekişe geçer; sapan bağlantısı sağlam kalır ve araç yavaşça teras hizasına doğru yükselir.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz
   Gerekçe: Sapanın kopması veya aracın savrulması yasaklanır; tam dengeli ve kararlı çekiş gösterilir.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  E        İŞARET: küme S08 (continues previous clip from its exact last frame)
LENS:           28 mm     MESAFE: 3.5 m     YÜKSEKLİK: 1.2 m
ÖLÇEK:          MS        AÇI TİPİ: dramatik alçak açı
KADRAJ ENİ:     3.0 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 2.0 m (askıda sarı gövde ve sapan)
                          Sığıyor mu: evet (2.0m < 3.0m)
ANA NESNE PİKSEL: 340 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: S08 ile aynı kurulum harfi (E), 0 ölçek, 0° azimut → BİLİNÇLİ KÜME (S08 son karesinden devam)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 (terasta duran astronot)   ⛔ film boyu KİLİT: 1
AYRIM EKSENİ:   Sarı araç gövdesi ve turuncu sapan vs kraterin dipsiz karanlığı
GİREN NESNE:    yok        ÇIKAN NESNE: yok
TAŞINAN NESNE:  Askıdaki sarı keşif aracı → S10'da terasa varış
⛔ BİÇİM KİLİDİ: Sarı keşif aracının ana şasisi altından geçen turuncu sapan ve gergin çelik halat
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Sert 15° güneş ışığı araç şasisinin kenarında parlar; arka plan mutlak siyah uzay boşluğu
PALET:     Endüstriyel sarı, turuncu sapan, parlak çelik karabina, derin siyah gölge
SES:       Sapan liflerinin mikroskobik gerilme gıcırtısı, kask içi derin soluk
MÜZİK:     Gerilim doruk bas tonu
FİZİK:     Ay yerçekimi 0,16g; askıda kalan 800 kg kütlenin Ay'da ~130 kg ağırlık hissiyle dengelenmesi
```

## 🎙️ REPLİK (varsa)

Bu film diyalogsuzdur; replik yoktur.

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (kask arka planda araca kilitli)
HAREKET:   Koca sarı araç uçurumun üzerinde boşlukta sallanmadan asılı dururken vinç onu milim milim yukarı çeker
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D179 | I2V'de başlangıç anı kilitlenir | continues the previous clip from its exact last frame |
| D198 | Düşük yerçekiminde kütle dengesi | 0,16g dengeli askıda duruş, ani savrulma ve yerçekimi sıçraması yok |
| D1 | Tek kesintisiz sekans | No cuts, no jumps, uninterrupted hold and lift |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | S08-S09 devamlılık kopması riski | START FRAME S08 son karesi olarak kilitlendi; küme kamera metni birebir taşındı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Evet   sınıf: YR (Düşme Riski)
NÖTR TARİF:  Sentetik askı sistemiyle havada tutulan sarı metal aracın dengeli yükselişi.
POZİTİF KİLİT: Güvenli endüstriyel vinç kaldırması, stabil yük dengesi.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 340 px ≥100 px
[x] S08 ile bilinçli küme (0 ölçek, 0° azimut)
[x] kurulum harfi + işaret satırı yazıldı (E, küme S08)
[x] ⛔ uyarıların hepsi kapandı
[x] politika satırı yazıldı
[x] ⭐VİRAL HAREKET satırı var
→ hepsi ✅, THE_BRITTLE_EDGE_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir.
```
