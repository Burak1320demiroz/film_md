# 🔬 S09 — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S09            BAŞLIK: SONRA KES, BİRLİKTE DÖN
BÖLÜM:      LOOK_UP_BOLUM_2.md
ZAMAN:      01:20 s → 01:30 s
VURUŞ:      Hat kesme & Asansöre çekilme (%75)  B5 SATIRI: İSTEK (ekibin tamamının kabine alınması)
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Mara eski takılı hattı keser, Eren ikisini kabine çeker, Noah kalkanı Mara'ya devreder ve beşi birlikte içeri girer.
BAŞTA:           Mara ve Noah dışarıda kısa tether ile bağlı, eski hat takılı.
SONDA:           Beş astronot ve tüm aktif hatlar kabin içinde, Noah kalkanı Mara'ya devretmiş.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz (Shot A: kordon kesme 0-2s, Shot B: makara çekişi & kalkan devri 2-10s)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  G         İŞARET: ilk kullanım

LENS:           65mm / 35mm     MESAFE: 1.2 m / 3.0 m   YÜKSEKLİK: 1.5 m
ÖLÇEK:          Close-up / Wide AÇI TİPİ: Eye level
KADRAJ ENİ:     1.0 m / 3.5 m   Kadraja alacak nesne: Bel kordonu kesicisi / Kabin içi beş kişi
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 400 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 2 · azimut 180° (kabin içinden bakış)   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5 (tüm beş ekip üyesi kabin içinde görünür)
AYRIM EKSENİ:   Mara (kask şeridi + kesici), Noah (hardal sarısı kask), Eren (makara), Cole (carbine), Jun (iç kumanda)
GİREN NESNE:    Kalkan devri Mara'nın eline   ÇIKAN NESNE: Kesik eski hat oda tarafında salınır
TASHINAN NESNE: Composite shield transferred from Noah to Mara (S09 -> S10)
⛔ BİÇİM KİLİDİ: Referans paketi R5 (Kalkan quick-release) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kabin içi parlak beyaz çalışma ışığı + oda tarafı acil kırmızısı
PALET:     Kabin duvarı kırık beyaz + beyaz kalkan + grafit giysiler
SES:       Hat kesilmesi hışırtısı + makara motoru + son atış sesi + kalkan klips tıkırtısı
MÜZİK:     Doruk gerilim ritmi
FİZİK:     Powered reel çekim momentumu, mikro yerçekimi kabin girişi
```

## 🎙️ REPLİK

```
REPLİK:    01:27 s · konuşan Eren · REGISTER H
İŞLEV:     Tamamlanma ("All five. Close it!")
AĞIZ:      okunuyor (doruk bedenleştirmesi — Eren el işareti vererek bağırır)
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       Eren'in yüzünde tam sayım kararlılığı, Noah'ın yüzünde eşiği geçiş rahatlaması.
HAREKET:   Eren'in makarası hızlı dönerek kordonu çeker, kalkan Noah'tan Mara'ya aktarılır.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D62 | Doruk kurguya eksiksiz girer | Kordon kesme ve kalkan devri adımları Shot A/B olarak ayrıldı |
| D213 | Aksiyon elipsi yasak | Kalkan devri eşikte elden ele net gösterilir |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Kalkan devri tek kalkan olmalı | Noah klipsi açar, Mara tutamağı kavrar | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Korumalı kesici bıçak sentetik emniyet hattını tek hareketle böler.
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
→ hepsi ✅: LOOK_UP_BOLUM_2.md'ye S09 promptları yazıldı.
```
