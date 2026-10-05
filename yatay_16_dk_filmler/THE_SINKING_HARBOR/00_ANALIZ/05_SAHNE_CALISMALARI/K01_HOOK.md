# 🔬 S01 · K01 — KİLİT KLİP · HOOK · SAHNE ÇALIŞMASI · THE_SINKING_HARBOR

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları + `00_SAHNE_TABLOSU.md`'nin K01 satırı.

---

## 🪪 KİMLİK

```
SAHNE:      S01  ·  KLİP: K01  ·  ROL: 1/4 HOOK       BAŞLIK: ÖZET — YANAŞMA VE KENET
BÖLÜM:      THE_SINKING_HARBOR_BOLUM_1.md
ZAMAN:      0 s → 10 s     ⛔ FORMÜLLE [D122]: (n−1) × 10 s · n = 1
VURUŞ:      ÖZET        B5 SATIRI: İSTEK
⭐VİRAL:    hayır — kaynak kliplerden monte edilir, kendi karesi yok
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Üç kaynak klipten 4+3+3 saniyelik özet montaj: küçük beyaz gemi dev kaburgaya yaklaşır, temas eder, dört kenet kapanır.
BAŞTA:           ölçek geneli — gemi kadrajda küçük, kaburga iki yandan taşıyor (K06 [0,0→4,0])
SONDA:           okunur mekanik detay — dört kenet kapanmış, iki gövde kaymıyor (K10 [0,0→3,0])
⛔ KLİP İÇİ DEĞİŞİM: VAR — üç kaynak klip, üç ayrı durum
   Seçim: ① değişim KLİBE DEĞİL KESİME taşındı
   Gerekçe: K01 yeni görüntü ÜRETMEZ; üç kaynak klibin kesiminden doğar (sahibin planı §9 madde 6). Klip içi değişim diye bir şey yok — üç kesme var. Kesim listesi URETIM_DEFTERI §7'de.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  — (kesim kartı · harf TAŞIMAZ)        İŞARET: kaynak kliplerin kurulumları geçerli: K06 = D · K09 = E · K10 = F

LENS:           24 / 35 / 85 mm     MESAFE: 700 m / 12 m / 8 m     YÜKSEKLİK: yuva ekseni
ÖLÇEK:          EWS → WS → CU        AÇI TİPİ: eye level
KADRAJ ENİ:     1.050 m / 12,34 m / 3,39 m      ⛔ HESAPLANDI — kadraja alınacak nesne gemi 28 m / yuva halkası 8 m / kenet 0,90 m
                          Sığıyor mu: EVET — üçünde de ölçüldü
ANA NESNE PİKSEL: 102 px / 2.489 px / 1.020 px   ⛔ ≥100 px [D179] → üçü de GEÇTİ ✅
ÖNCEKİ KLİPLE:  ölçek kademesi — (filmin ilk klibi) · azimut 0° → 70° → 130°   → bant içi: EWS→WS 1 kademe ✅ · WS→CU 3 kademe = YANASMA §1.2'nin V5→V6 reçetesi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — üç kaynak klipte de insan kadrajda YOK
AYRIM EKSENİ:   — (insan yok)
GİREN NESNE:    gemi · liman kaburgası · yuva halkası · dört kenet · uzak halkalı gezegen
ÇIKAN NESNE:    —
TAŞINAN NESNE:  dördü de filmin sonuna kadar dönüyor: gemi (K93) · kaburga (K94) · yuva (K92) · kenet (K92)
⛔ BİÇİM KİLİDİ: VAR ve metinle tutulmuyor [D146] → gemi ve kaburga referans paketi sayfaları ONAYLI olmadan K06/K09/K10 üretilmez (KAPI 0)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      kaynak kliplerin ışığı — kubbe 6/6, kolon ışıkları beyaz
PALET:     siyah kaburga + beyaz gövde + alttan amber YOK (henüz)
SES:       H1 dış sesi + ızgara; kesme noktalarında oda tonu köprüsü ≥0,2 s [D216]
MÜZİK:     var — düşük, kokpit ses köprüsü
FİZİK:     1,00 g · yoğun hidrojen-helyum bulut katmanı · su YOK [D56]
```

## 🎙️ REPLİK

```
REPLİK:    H1 · 0,0 s · pilot (dış ses) · REGISTER: İNSAN, gövdesiz anlatıcı
İŞLEV:     görevin SEBEBİ ve "son adam" bilgisi — kadrajda bir adam yok, üç kaynak klipte de insan YOK
AĞIZ:      okunmuyor — konuşan hiçbir kaynak klipte kadrajda değil
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
YÜZ:       — (⭐VİRAL değil)
HAREKET:   — (⭐VİRAL değil)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| **D211** | ilk 10 s'de SORU olacak, kurulum değil | Kart, üç kesmeyle "bu yapı ne kadar büyük" sorusunu kurar; ekran metni 0,0 s |
| **D34** | özel ad ve başlık kartı 0 | Kartta ad yok; H1 dış sesi KURGUDA bindirilir, promptta yazı yok |
| **SAPMA 2** | K01-K04 yeni görüntü ÜRETMEZ | Bölüm dosyasında on alanlı KESİM KARTI; kaynak klip + saniye + kare + ses |
| **D56** | ortam maddesi su DEĞİL | Üç kaynak klibin üçü de su negatifini taşıyor (K06 dış klip) |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | ⛔-1 SU — "sinking harbor" adı modelden su çağırır | K01 kendi görüntüsünü üretmediği için risk kaynak kliplere taşındı; K06'nın promptunda MEDIUM LOCK var | ✅ |
| 2 | ⚠️ | ⚠️-7 klip süresi ARAÇTAN ölçülür | Kesim listesi kare cinsinden yazıldı (24 fps varsayımı AÇIK, ⬜ ölçüm) | ⬜ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR — kadrajda insan yok, gövdeye değen kuvvet yok, hasar sözlüğü yok
NÖTR TARİF:  — (risk yok)
POZİTİF KİLİT: — (risk yok)
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği üç kaynak klip için de yapıldı — üçü de ≥100 px
☑ ardışık çift: filmin ilk klibi; iç çift EWS→WS→CU ölçüldü
☑ kurulum: kesim kartı, kaynak harfler yazılı (D · E · F)
☑ ⛔ uyarı kapandı (SU kaynak klipte)
☑ politika satırı yazıldı — risk yok
☑ ⭐VİRAL değil, iki satır gerekmiyor
→ THE_SINKING_HARBOR_BOLUM_1.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
