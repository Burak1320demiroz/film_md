# 🔬 S05 — SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S05            BAŞLIK: İKİ YÖNDEN GELİYORLAR
BÖLÜM:      LOOK_UP_BOLUM_1.md
ZAMAN:      00:40 s → 00:50 s
VURUŞ:      Kuşatma (%42) B5 SATIRI: ENGEL (iki yönlü yaratık baskısı)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            C04 tavandan, C05 alt raydan saldırır; C04 Noah'ın kalkanlı kolunu geriye bükerek zorlar.
BAŞTA:           Noah kalkanı önde savunma düzeninde duruyor.
SONDA:           C04 kalkan kenarını çekerek Noah'ın sol omzunu geriye zorluyor.
⛔ KLİP İÇİ DEĞİŞİM: YOK
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  D         İŞARET: dönüş S04

LENS:           35mm            MESAFE: 2.0 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Medium-Close    AÇI TİPİ: Eye level
KADRAJ ENİ:     1.6 m           Kadraja alacak nesne: Noah kalkanı + C04 pençesi
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 280 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 0 · azimut 0°   → bant içi: evet (KÜME)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5
AYRIM EKSENİ:   Noah (hardal sarısı kask şeritleri + sol kol kalkanı)
GİREN NESNE:    C04 tavan pençesi, C05 alt ray pençesi
TAŞINAN NESNE:  Shield in (S04) / out (S06)
⛔ BİÇİM KİLİDİ: Referans paketi R5 (Kalkan quick-release) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Nötr beyaz çalışma ışığı + kırmızı acil lambası
PALET:     Kırık beyaz kalkan + kömür siyahı yaratık gövdesi
SES:       Stereo pençe sesleri + metal sürtünme gıcırtısı
MÜZİK:     Gelişen ritmik bas vuruları
FİZİK:     Mikro yerçekiminde tork ve moment zorlanması (0g atalet)
```

## 🎙️ REPLİK

```
REPLİK:    00:44 s · konuşan Cole · REGISTER H
İŞLEV:     Tehdit teşhisi ("They're flanking us.")
AĞIZ:      okunuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D169 | 0g Efor fiziksel anlatımı | Tork ve omzun geriye bükülme kadansı sıfat yerine fiziksel kuvvetle yazılır |
| D175 | Bare skin negatifi | Ten alanları açıkta bırakılmaz |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Kalkan zorlanması bükülme vektörüyle anlatılmalı | Shoulder torque and mechanical strain detailed | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kömür siyahı 4 uzuvlu canlı kalkan kenarını kavrayıp geriye doğru çeker.
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
→ hepsi ✅: LOOK_UP_BOLUM_1.md'ye S05 promptları yazıldı.
```
