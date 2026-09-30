# 🔬 S00 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · THE_STATIC_VEIL

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
SAHNE:      S00            BAŞLIK: Toz Uyanışı
BÖLÜM:      THE_STATIC_VEIL_BOLUM_1.md
ZAMAN:      0.0 s → 10.0 s       ⛔ FORMÜLLE [D122]: hook + (n−1) × klip
VURUŞ:      Hook & Novum İlanı   B5 SATIRI: MUHATAP
⭐VİRAL:    evet  → YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Krater yamacında hareketsiz duran regolit tozu, elektrostatik yükle ince parıltılı iplikler hâlinde dikine yükselmeye başlar.
BAŞTA:           Krater gölgesi ve pilon hareketsiz, zemin dingin gri regolit örtüsü.
SONDA:           Zeminden 1-2 metre havaya dikine yükselen ve asılı kalan ince toz iplikleri kadrajı doldurur.
⛔ KLİP İÇİ DEĞİŞİM: YOK (süreç eylemi: partiküllerin dikine yükselişi kesintisiz sürdürülür)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: ilk kullanım

LENS:           24mm     MESAFE: 12.0 m     YÜKSEKLİK: 0.4 m
ÖLÇEK:          EWS      AÇI TİPİ: Düşük Açı (zemin hizası)
KADRAJ ENİ:     16.0 m   ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne (pilon ve toz alanı) 10.0 m
                          Sığıyor mu: evet
ANA NESNE PİKSEL: 240 px (pilon ve toz iplikleri)   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: açılış sahnesi (ilk kare)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 (açılışta insan yok, odak ortam ve toz anomalisi)
AYRIM EKSENİ:   koyu gri bazalt zemin ve parlak elektrostatik partiküller
GİREN NESNE:    dikine yükselen elektrostatik toz iplikleri
ÇIKAN NESNE:    yok
TAŞINAN NESNE:  toz iplikleri → S01'de astronot kaskına yapışacak
⛔ BİÇİM KİLİDİ: Referans paketi sayfa R2 (Pilon ve optik fener yuvası)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Zifiri krater gölgesi, krater kenarında jilet gibi keskin güneş hattı, 0 feathering
PALET:     Mat koyu gri regolit, zifiri siyah gölge, parıldayan açık gri mineral taneleri
SES:       Mutlak sessizlik + derinden gelen düşük frekanslı sismik dip uğultusu
MÜZİK:     yok (mutlak sessizlik gerilimi)
FİZİK:     0.16g Ay kütleçekimi, hava yok, rüzgar yok, atmosferik saçılma yok; tozlar dik yükselir ve yere inmez
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      okunmuyor
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       none (kadrajda insan yok)
HAREKET:   rüzgarsız vakum ortamında tozların fizik kurallarına meydan okurcasına dikine havalanması
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D200 | Vakumda toz süzülmez veya yere inmez | In airless vacuum, fine regolith dust rises vertically 1 to 2 meters and levitates without falling |
| D192 | 1 numaralı risk sayıyla yazılır | Dust particle size 10 to 100 microns, levitation height 1 to 2 meters |
| D211 | S0 hook sorusu net kurulmalı | Silent physical anomaly hook: vertical levitation in zero wind |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | D200 iki yerçekimi yanılsaması | Tozların yere inmesi engellendi; dik yükselme ve askıda kalma yazıldı | ✅ |
| 2 | ⚠️ | D211 ilk 2 saniyede görsel merak | İlk karede zemin üzerinden dik yükselen parıltılı iplikler belirgin kılındı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  Karasal olmayan kuru mineral toz partiküllerinin elektrostatik alan etkisiyle dikey levitasyonu
POZİTİF KİLİT: Fine dry mineral dust levitates vertically under electrostatic charge
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px (240px)
✅ önceki sahneyle ardışık çift: açılış sahnesi
✅ kurulum harfi + işaret satırı yazıldı (A · ilk kullanım)
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ olduğu için THE_STATIC_VEIL_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```
