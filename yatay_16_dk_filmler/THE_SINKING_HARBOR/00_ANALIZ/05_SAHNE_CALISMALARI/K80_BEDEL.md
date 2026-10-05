# 🔬 S20 · K80 — KİLİT KLİP · BEDEL · SAHNE ÇALIŞMASI · THE_SINKING_HARBOR

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları + `00_SAHNE_TABLOSU.md`'nin K80 satırı.

---

## 🪪 KİMLİK

```
SAHNE:      S20  ·  KLİP: K80  ·  ROL: 4/4 BEDEL       BAŞLIK: BİRAZ DAHA AŞAĞI
BÖLÜM:      THE_SINKING_HARBOR_BOLUM_7.md
ZAMAN:      790 s → 800 s     ⛔ FORMÜLLE [D122]: (n−1) × 10 s · n = 80
VURUŞ:      BEKLEYİŞ        B5 SATIRI: BEDEL ②
⭐VİRAL:    hayır
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Pilotun işaretiyle liman biraz daha iner ve geminin penceresi bulutla TAMAMEN örtülür.
BAŞTA:           pencerenin ALT ÇEYREĞİ bulutla kaplı, camın iç yüzü KURU
SONDA:           pencerenin TAMAMI bulutla örtülü, camın iç yüzünde nefes buğusu
⛔ KLİP İÇİ DEĞİŞİM: VAR — bedelin kendisi bu değişimdir
   Seçim: ② klip İÇİNDE, ÖLÇEN KENAR pencere çerçevesidir
   Gerekçe: ⭐ D179'un kapısı tam burada koşar: IMAGE promptu 0,0 saniyeyi yazar (alt çeyrek kaplı, cam KURU), VIDEO promptu örtülmeyi yapar. İlk yazımda imajın 'örtülü pencere'yi yazması THE HEALING GROUND'un arızasının birebir tekrarı olurdu — bedel yazılır, sebebi üretilmez.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  J        İŞARET: dönüş K73 (ara 7 klip → yeniden tanıtım) · eş kadraj dizisi K15 ↔ K29 ↔ K80

LENS:           50 mm     MESAFE: 2,2 m     YÜKSEKLİK: 1,60 m
ÖLÇEK:          CU        AÇI TİPİ: eye level
KADRAJ ENİ:     1,58 m      ⛔ HESAPLANDI — kadraja alınacak nesne pencere 1,50 m
                          Sığıyor mu: EVET — pencere kadrajı neredeyse tam dolduruyor (çerçeve ölçen kenar)
ANA NESNE PİKSEL: 3.636 px   ⛔ ≥100 px [D179] → GEÇTİ ✅
ÖNCEKİ KLİPLE:  ölçek kademesi K79 MWS → K80 CU = 2 kademe ✅ · bakım yolu → gemi penceresi, mekân DEĞİŞTİ   → bant içi: bant içi ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — ⭐ pilot bu klipte KADRAJDA DEĞİL, yalnız SESİ var
AYRIM EKSENİ:   — (insan yok)
GİREN NESNE:    nefes buğusu (camın İÇ yüzünde)
ÇIKAN NESNE:    pencerenin dışındaki derinlik — bulut onu kapatır
TAŞINAN NESNE:  ⭐ ALÇALMA SAYACI 4/4 kapanıyor (K15 alt çeyrek → K29 orta → K61 üst çeyrek → K80 tam)
⛔ BİÇİM KİLİDİ: pencere çerçevesi — sabit referans, dört klipte BİREBİR aynı prop çapası cümlesi [§3.5]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      amber alttan, kubbe 2/6; bulut pencereyi kapatınca içerideki tek kaynak kabin ışığı kalır — ışık KAYNAK DEĞİŞTİRMEZ, miktarı düşer
PALET:     amber + vizör içi buğu — S19'un (metal + sarı krank) paletinden FARKLI ✅
SES:       makine sesi KISIK, gezegenin ritmi ÖNDE; pilotun sesi TELSİZDEN (band-pass)
MÜZİK:     var — ② NABIZ katmanı; katman sayısı ≤4
FİZİK:     1,00 g · yoğun bulut katmanı · bulut YAPIYA opak, IŞIĞA geçirgen · su YOK
```

## 🎙️ REPLİK

```
REPLİK:    D31 · 6,0 s · pilot · REGISTER: İNSAN, telsiz band-pass
İŞLEV:     ⭐ BEDEL EMRİ — pilot kadrajda YOK, bedel PENCEREDE görünür. Replik kadraj dışı bir karara ait; kadrajda bir emir yok, bir SONUÇ var
AĞIZ:      okunmuyor — konuşan kadrajda değil [D82'nin pozitif üçlüsü: SOURCE + KADRAJ + NEGATİF]
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
YÜZ:       — (⭐VİRAL değil)
HAREKET:   — (⭐VİRAL değil)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| **D179** | IMAGE = ÇAPA'nın BEFORE'u | ⭐ IMAGE: *the lower quarter of the pane is covered by cloud and the inner glass is dry* · VIDEO 0,0 s AYNI cümle, 8,0 s'de tamamı örtülü |
| **D202** | bedel BEDENDE/KANALDA okunur | Kanal: PENCERE + NEFES. Dolgu jesti 0 |
| **D78** | sayaç tek karede kanıtlanır | Pencere çerçevesi ölçen kenar; a/b kare çifti K15 ↔ K80 |
| **D216** | katman ≤4 · telsiz filtresi | Replik band-pass; kesmede oda tonu köprüsü ≥0,2 s |
| **D56** | su YOK | ⛔ Bulut camı kapatıyor — "ıslak cam" en yakın su okuması. Negatif: *no water on the glass, no droplets, no condensation on the outside* + pozitif: iç yüzde NEFES buğusu (su değil, nem) |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | ⛔-1 SU — bulutun camı kapatması "ıslak pencere" okunabilir | Dışta damla 0, içte NEFES buğusu (nem, su değil); dış yüz KURU yazılır | ✅ |
| 2 | ⛔ | ⛔-6 alçalma yönü nesneye bağlı | *the cloud boundary climbs the frame of the pane* — koordinat değil NESNE | ✅ |
| 3 | ⚠️ | ⚠️-1 D217: "A little lower. Now." | İŞLEV: emir, tarif değil; alıcı kadrajda değil | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR — gövdeye değen kuvvet yok, hasar sözlüğü yok, insan yok
NÖTR TARİF:  — (risk yok)
POZİTİF KİLİT: — (risk yok)
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı ve İKİSİ FARKLI
☑ optik aritmetiği yapıldı — pencere 3.636 px
☑ ardışık çift K79→K80 = 2 kademe, mekân değişti ✅
☑ kurulum harfi J + dönüş işareti + eş kadraj dizisi yazıldı
☑ ⛔ uyarıların üçü de kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL değil
⭐ ÇAPA COST satırı 03 §2f'de: BEFORE/AFTER + 6,0 s
→ THE_SINKING_HARBOR_BOLUM_7.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
