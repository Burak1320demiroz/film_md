# 🔬 S02 — SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S02            BAŞLIK: İLK TEMAS
BÖLÜM:      LOOK_UP_BOLUM_1.md
ZAMAN:      00:10 s → 00:20 s
VURUŞ:      İlk temas (%17) B5 SATIRI: BEDEL (Cole'un bot kilit kopması)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            C01 Cole'a çarpar, Cole'un sağ bot kilit mekanizması kopar ve duvarda savrulurken atış yapar.
BAŞTA:           Cole botları kilitli koridorda bekliyor.
SONDA:           Cole sağ bot kilidi kopmuş halde duvarda savrulup carbine ile atış yapıyor.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz (Çarpma 0-3s, bot kilit kopması 3-6s, duvarda atış 6-10s)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  B         İŞARET: ilk kullanım

LENS:           50mm            MESAFE: 2.0 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Medium-Close    AÇI TİPİ: Eye level
KADRAJ ENİ:     1.5 m           Kadraja alacak nesne: Cole gövdesi + kilit mekanizması
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 320 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 45°   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (kadrajda Cole odaklı)
AYRIM EKSENİ:   Cole (geniş omuz zırh plakaları + carbine)
GİREN NESNE:    C01 darbesi           ÇIKAN NESNE: yok
TAŞINAN NESNE:  Cole harness in (S01) / out (S03)
⛔ BİÇİM KİLİDİ: Referans paketi R1 (Cole donanımı) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Nötr beyaz çalışma ışığı + arka plan acil kırmızısı
PALET:     Grafit giysi + kıvılcım parlaması
SES:       Şiddetli çarpma + bot kilit kopma çatırtısı + kısa mermi patlamaları
MÜZİK:     Vurmalı aksiyon bas vuruşları
FİZİK:     Mikro yerçekimi çarpışma momentumu, savrulma ve silah tepkisi
```

## 🎙️ REPLİK

```
REPLİK:    00:14 s · konuşan Mara · REGISTER H
İŞLEV:     Komut ("Lock your boots!")
AĞIZ:      okunuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D16 | Bot kilit mekanizması kopması | Sağ bot kilit latch kopması ve kıvılcımsız sönümlü atış tarif edilir |
| D42 | Sönümlü kıvılcım | Namlu parlaması kısa sönümlü ışıkla verilir |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Bot kopma eylemi sayısal anlatılmalı | Latch separation and drift vectors detailed | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kömür renkli canlı gövdeye çarpar, metalik ayak kilidi braketten ayrılır.
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
→ hepsi ✅: LOOK_UP_BOLUM_1.md'ye S02 promptları yazıldı.
```
