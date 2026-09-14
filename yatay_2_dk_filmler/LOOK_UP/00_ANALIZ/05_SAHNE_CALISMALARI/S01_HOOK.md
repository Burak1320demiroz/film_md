# 🔬 S01 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S01            BAŞLIK: YANLIŞ YÖN
BÖLÜM:      LOOK_UP_BOLUM_1.md
ZAMAN:      00:00 s → 00:10 s
VURUŞ:      Hook (%8)       B5 SATIRI: ENGEL (tavandan sürpriz kuşatma)
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Noah ve Mara batı kapısına bakarken tavandan sarkan C01 pençesini fark eder ve C01 Cole'a fırlar.
BAŞTA:           Beş insan batı kapısına kilitlenmiş, tehdidi henüz fark etmemiş.
SONDA:           C01 tavan kirişinden Cole'a fırlamış, temas anından hemen önceki kare.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz (Shot A: bakış yükselişi, Shot B: geniş fırlayış)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A         İŞARET: ilk kullanım

LENS:           35mm / 28mm     MESAFE: 2.5 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Medium / Wide   AÇI TİPİ: Eye level / Low angle
KADRAJ ENİ:     1.8 m           Kadraja alacak nesne: 1.25 m (C01) + kasklı iki astronot
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 240 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: — (İlk sahne)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (tüm sahnelerde 5)
AYRIM EKSENİ:   Mara (tek beyaz dikey kask şeridi), Noah (hardal sarısı çapraz kask şeritleri), Cole (omuz zırh plakaları)
GİREN NESNE:    C01 ön pençesi        ÇIKAN NESNE: yok
TAŞINAN NESNE:  Noah composite shield → sonraki S04 / S08 / S09
⛔ BİÇİM KİLİDİ: Referans paketi R1 (giysi) & R3 (C01 anatomisi) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Nötr beyaz çalışma ışığı + arka plan kırmızı acil lambası
PALET:     Grafit tekstil + kırık beyaz paneller + acil kırmızısı
SES:       Ortam fanı + tek pençe tıklaması + kask içi nefes
MÜZİK:     yok (00:00-00:04 mutlak sessizlik / ortam sesleri)
FİZİK:     Mikro yerçekimi, zemin bot bağlantıları, süzülen dekor parçacıkları
```

## 🎙️ REPLİK

```
REPLİK:    00:05 s · konuşan Noah · REGISTER H
İŞLEV:     HOOK uyarısı ("Above us!")
AĞIZ:      okunuyor (vizör berrak)
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       Noah'ın gözleri vizör arkasında büyür, bakışı yukarı kayar.
HAREKET:   C01 tavan ızgarasından fırlayarak hızlı balistik trajectory çizer.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D1 | Tek çekim AI kesmesi yasak | Shot A ve Shot B timeline ofsetleriyle net ayrılır |
| D34 | Karakter özel adı kullanılmaz | Promptlarda commander / rookie genel ünvanları kullanılır |
| D79 | Berrak vizör camı | Visor is optically clear glass zero tint |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Tehdit ilk karede görünmeli | C01 pençesi 0. saniyede ızgarada hazır | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır (PK/PB güvenli)
NÖTR TARİF:  Kanca biçimli organik donanım tavan ızgarasını kavrar.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
[x] önceki sahneyle ardışık çift bant içi
[x] kurulum harfi + işaret satırı yazıldı
[x] uyarıların hepsi kapandı
[x] politika satırı yazıldı
[x] ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅: LOOK_UP_BOLUM_1.md'ye S01 promptları yazıldı.
```
