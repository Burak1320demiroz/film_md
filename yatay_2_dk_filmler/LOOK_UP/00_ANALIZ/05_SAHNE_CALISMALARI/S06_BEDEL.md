# 🔬 S06 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S06            BAŞLIK: KOPUŞ
BÖLÜM:      LOOK_UP_BOLUM_1.md
ZAMAN:      00:50 s → 01:00 s
VURUŞ:      Noah'ın kopuşu (%50)  B5 SATIRI: BEDEL (Noah'ın açıkta kalması ve omzunun zorlanması)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Noah omzunu kurtarmak için bot kilitlerini bırakır; boşlukta savrularak kordonu tavan braketine takılıp açıkta kalır.
BAŞTA:           Noah botları bağlı halde kalkan çekişiyle zorlanıyor.
SONDA:           Noah botları açık, emniyet kordonu tavan braketine takılmış halde eşikten 2-2.5m uzakta asılı.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz (Bot bırakma 0-2s, savrulma 2-5s, brakete takılma 5-8s)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  E         İŞARET: ilk kullanım

LENS:           28mm            MESAFE: 3.5 m     YÜKSEKLİK: 1.5 m
ÖLÇEK:          Wide            AÇI TİPİ: Eye level
KADRAJ ENİ:     3.0 m           Kadraja alacak nesne: Noah tüm beden + tavan braketi
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 220 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 0°   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (kadraj odağında Noah tek)
AYRIM EKSENİ:   Noah (hardal sarısı kask şeritleri + sol kolda ezik kalkan)
GİREN NESNE:    Tavan braketi         ÇIKAN NESNE: yok
TAŞINAN NESNE:  Snagged line in (S05) / out (S09)
⛔ BİÇİM KİLİDİ: Referans paketi R1 (D79 düz sırt paneli) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Nötr beyaz çalışma ışığı + kırmızı acil lambası
PALET:     Grafit tekstil + kırık beyaz paneller
SES:       İki bot kilit mekanizması tıkırtısı + kordon gerilimi kuru sesi
MÜZİK:     Yüksek gerilim drone ve vurmalı vuruşlar
FİZİK:     Mikro yerçekimi savrulması, kordon gerilim salınımı (2.2m yükseklik)
```

## 🎙️ REPLİK

```
REPLİK:    00:57 s · konuşan Noah · REGISTER H
İŞLEV:     Kopuş ve panik ("I'm caught!")
AĞIZ:      okunuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D139 | Düz sırt paneli kilidi | The back of the suit is one continuous smooth panel from collar to hip carrying nothing |
| D172 | Taşıyıcıyı aşan kordon | Kordon boşluktaki düğüme değil çatallı braket boynuna takılır |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Hat braket boynuna sıkışmalı | Braket detayında kordon wedging | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kordon gevşek halkası metal servis desteğinin çatallı alt koluna takılır.
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
→ hepsi ✅: LOOK_UP_BOLUM_1.md'ye S06 promptları yazıldı.
```
