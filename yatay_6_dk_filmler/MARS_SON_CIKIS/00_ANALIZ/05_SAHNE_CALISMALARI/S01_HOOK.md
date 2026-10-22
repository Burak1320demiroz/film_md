# 🔬 S01 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · MARS_SON_CIKIS

---

## 🪪 KİMLİK

```
SAHNE:      S01            BAŞLIK: Kanca: Freni tut
BÖLÜM:      MARS_SON_CIKIS_BOLUM_1.md
ZAMAN:      00:00 s → 00:10 s
VURUŞ:      HOOK           B5 SATIRI: İSTEK
⭐VİRAL:    evet
```

## 🎬 OLAY VE 10 SANİYE EYLEM AKIŞI — hareketin zamana yayılımı

```
OLAY:            Yakın kadrajda ray üzerinde kayan ağır numune kasası Lena'nın fren kolunu çekmesi ve Aras'ın emniyet pimini takmasıyla durdurulur.
BAŞTA:           Kasa ray üzerinde momentumla hızla kaymaktadır.
SONDA:           Kasa frenlenmiş, ray sonundaki yuvaya oturmuş ve emniyet pimi kilitlenmiştir.

⛔ 10 SANİYE EYLEM AKIŞI (EYLEM TABANLI ZAMANLAMA):
   0-3 s (Giriş/Başlangıç):  Kasa ray üzerinde kayar; Lena sağ eldiveniyle fren kolunu kavrar.
   3-7 s (Gelişme/Aksiyon): Lena fren kolunu sertçe aşağı çeker, ray kıvılcım çıkararak yavaşlar.
   7-10 s (Sonuç/Geçiş):     Aras sol eliyle ağır metal pimi yuvaya sokar ve kilitler ("kork" kliği).
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A         İŞARET: ilk kullanım
LENS:           50mm      MESAFE: 2,0 m     YÜKSEKLİK: 1,4 m (Göz seviyesi)
ÖLÇEK:          MCU       AÇI TİPİ: Göz seviyesi
KADRAJ ENİ:     1,8 m     Sığıyor mu: Evet
ANA NESNE PİKSEL: 420 px
ÖNCEKİ SAHNEYLE: ölçek kademesi — · azimut —°   → bant içi: Evet (İlk sahne)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   2 (Lena & Aras)
AYRIM EKSENİ:   Lena petrol mavisi yan paneller + dar omuz; Aras oksit turuncu omuz panelleri + geniş gövde
GİREN NESNE:    Fren kolu
ÇIKAN NESNE:    —
TAŞINAN NESNE:  Ağır numune kasası (S01'den S02'ye)
BİÇİM KİLİDİ:   Evet (MARS_SON_CIKIS_REFERANS_PAKETI.md)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kızıl Mars dış ışığı, keskin güneş açısı
PALET:     Kızıl toz / Taş beyazı zırh / Grafit eklemler
SES:       Ray metalic sürtünmesi · kask içi telsiz solunumu
MÜZİK:     yok (Mekanik ses önde)
FİZİK:     Mars 0.38g yerçekimi, yüksek kütle ataleti
```

## 🎙️ REPLİK

```
REPLİK:    "Brake. Hold it." · 00:03 s · konuşan Lena · REGISTER Telsiz
İŞLEV:     Aksiyon koordinasyonu
AĞIZ:      okunmuyor (Vizör kapalı)
```

## ⭐VİRAL

```
YÜZ:       Lena'nın vizör arkasındaki gözleri pürüzsüz odakla kasaya kilitlenir.
HAREKET:   Lena'nın sağ eldiveni fren kolunu aşağı doğru sertçe çeker.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D210 | S01 pimi S31 kenetlenme leveri ile kafiye oluşturur | Fren kolu çekilişi ve pim kliği belirgin gösterilecek |
| D139 | Düz sırt kilidi | Smooth continuous back panel |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Ray ataleti düşük-g gibi hissettirmemeli | Kasanın durma anı ağır sönümlemeyle verildi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Mekanik kol çekimi ve metalik sabitleme pimi
```

---

## ✅ KAPI

```
✅ OLAY yazıldı
✅ Optik tamam (1.8m en, 420px nesne)
✅ Viral satırları dolu
→ MARS_SON_CIKIS_BOLUM_1.md S01 yazılabilir.
```
