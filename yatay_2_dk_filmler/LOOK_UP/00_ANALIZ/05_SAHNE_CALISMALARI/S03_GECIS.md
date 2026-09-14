# 🔬 S03 — SAHNE ÇALIŞMASI · LOOK_UP

---

## 🪪 KİMLİK

```
SAHNE:      S03            BAŞLIK: KAÇIŞ HEDEFİ
BÖLÜM:      LOOK_UP_BOLUM_1.md
ZAMAN:      00:20 s → 00:30 s
VURUŞ:      Kaçış hedefi (%25) B5 SATIRI: İSTEK (ekibin asansöre doğru gerilemesi)
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Ekip sağdaki asansöre doğru geri çekilirken C10 gizlice üst şaft havalandırma deliğine süzülür.
BAŞTA:           Ekip koridor ortasında savunma konumunda.
SONDA:           Ekip asansör kapısına ulaşmış, C10 şaft havalandırmasına girmiş.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz (Shot A: Ekip gerilemesi 0-5s, Shot B: C10 havalandırma girişi 5-10s)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  C         İŞARET: ilk kullanım

LENS:           28mm / 50mm     MESAFE: 4.0 m     YÜKSEKLİK: 1.2 m
ÖLÇEK:          Wide / CU       AÇI TİPİ: Low angle
KADRAJ ENİ:     3.5 m           Kadraja alacak nesne: Asansör kapısı + üst havalandırma deliği
                           Sığıyor mu: evet
ANA NESNE PİKSEL: 180 px   (≥100 px sağlandı)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 90°   → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   5
AYRIM EKSENİ:   Mara (komutan dikey şerit), C10 (sol omuz dikey gri çizik)
GİREN NESNE:    C10 havalandırma deliğine  ÇIKAN NESNE: yok
TAŞINAN NESNE:  C10 shoulder abrasion in (S03) / out (S12)
⛔ BİÇİM KİLİDİ: Referans paketi R3 (C10 gri çiziği) onaylı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Nötr beyaz çalışma ışığı + kırmızı acil uyarısı
PALET:     Grafit duvar panelleri + metalik gri havalandırma
SES:       Seri pençe tıklamaları + metal sürtünme motifi
MÜZİK:     Gerilim drone ve bas atımları
FİZİK:     Mikro yerçekimi süzülmesi ve yüzey itişi
```

## 🎙️ REPLİK

```
REPLİK:    00:22 s · konuşan Mara · REGISTER H
İŞLEV:     Hedef belirleme ("Get the lift open.")
AĞIZ:      okunmuyor
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D78 | Azimut sıçraması denetimi | Low angle 28mm geniş açılım ile kapı aksı kurulur |
| D141 | C10 gri çizik devamlılığı | C10'un sol omzunda tek gri çizik görünür |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | C10 gri çiziği net gösterilmeli | Longitudinal gray scratch on left shoulder detail | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Kömür siyahı 4 uzuvlu canlı metal havalandırma açıklığına girer.
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
→ hepsi ✅: LOOK_UP_BOLUM_1.md'ye S03 promptları yazıldı.
```
