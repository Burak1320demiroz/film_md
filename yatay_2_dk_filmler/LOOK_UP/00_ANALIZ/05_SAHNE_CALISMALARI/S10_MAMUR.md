# 🔬 S10 — SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S10            BAŞLIK: KAPIYI KAPAT
BÖLÜM:      LOOK_UP_BOLUM_2.md
ZAMAN:      01:30 s → 01:40 s
VURUŞ:      Kapı kapanışı & kalkan baskısı (%83) B5 SATIRI: ENGEL (yaratık pençesinin kapı aralığına girmesi)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            C01 pençesi kapanan asansör kapısı aralığına girer; Mara ve Cole kalkanla bastırıp pençeyi çıkarır ve kapı mühürlenir.
BAŞTA:           Asansör kapısı kapanırken C01 pençesi aralığa takılmış.
SONDA:           Kalkan baskısıyla pençe çıkarılmış, asansör kapısı tam mühürlenmiş.
⛔ KLİP İÇİ DEĞİŞİM: YOK
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  D         İŞARET: dönüş S04

LENS:           35mm            MESAFE: 2.0 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Medium-Close    AÇI TİPİ: Eye level
KADRAJ ENİ:     1.6 m           Kadraja alacak nesne: Kapı aralığı + kompozit kalkan + C01 pençesi
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 300 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 180°   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (odakta Mara ve Cole kapı eşiğinde)
AYRIM EKSENİ:   Mara (kask dikey şeridi + kalkan tutuşu), Cole (geniş omuz plakaları)
GİREN NESNE:    C01 pençesi kapı eşiğine   ÇIKAN NESNE: C01 pençesi geri çekilir
TAŞINAN NESNE:  Door seal in (S10) / out (S11)
⛔ BİÇİM KİLİDİ: Referans paketi R5 (Kalkan) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kabin içi nötr beyaz ışık + kapı aralığından sızan kırmızı acil parlaması
PALET:     Kırık beyaz kalkan + metalik gri kapı panelleri
SES:       Kapı motoru iniltisi + kalkan metal sürtünmesi + mühürlenme vakum sesi
MÜZİK:     Doruk sonrası yankılanan bas atımları
FİZİK:     Kalkan baskısı ve kapı mekanik kapanma kuvveti
```

## 🎙️ REPLİK

```
REPLİK:    01:34 s · konuşan Mara · REGISTER H
İŞLEV:     Fiziksel baskı ("Push!")
AĞIZ:      okunuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D70 | Kapı mühür sürtünmesi | Kalkan ile kapı aralığı fiziksel teması sayısal yazılır |
| D192 | 1 numaralı risk | 5 insan ve 10 yaratık kadro sınırlaması korunur |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Pençe zorlaması uzuv kopması içermemeli | Claw releases under shield force without gore | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kompozit kalkan paneli organik pençeyi metalik kapı çerçevesinden dışarı bastırır.
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
→ hepsi ✅: LOOK_UP_BOLUM_2.md'ye S10 promptları yazıldı.
```
