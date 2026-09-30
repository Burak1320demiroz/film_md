# 🔬 K02 — KİLİT KLİP · NOVUM · ÇALIŞMA · GUNES_MEZARI

> ⛔ Başlık biçimi `## 🔬 K<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
KLİP:       K02   ·   SAHNE: S01   ·   ROL: NOVUM
BAŞLIK:     KAFES — taşınabilir bir güneş
BÖLÜM:      GUNES_MEZARI_BOLUM_1.md
ZAMAN:      10,0 s → 20,0 s     ⛔ FORMÜLLE [D122]: (n−1) × 10,0 s
VURUŞ:      ölçek şoku (S1 ikinci bilgi)        B5 SATIRI: —
⭐VİRAL:    hayır — kadrajda insan YOK
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Küre üç halkanın odağında, uzun kaburgalı bir geminin altında; gövdenin sırtında kapı boyunda tek bir aydınlık pencere var.
BAŞTA:           gemi kadrajın içine girmiş, küre halkaların odağında
SONDA:           gemi kadrajı geçmeye devam ediyor, küre halkaların odağında kalıyor
SON 3 s:         gemi kadrajı geçmeye devam ediyor, küre halkaların odağında kalıyor
⛔ KLİP İÇİ DEĞİŞİM: YOK — gemi sabit hızda geçer; hiçbir durum değişmez
KİLİT FİİLİ:     ETKİNLİK — `crosses` (gemi kadrajı geçer, bitişsiz)
DİRENÇ (evre ②): kürenin kendi ağırlığı halkalara biner: halkaların dış kenarı 5. saniyede bir kez gerilir
ÇEVRE SAATİ:     kürenin yüzeyindeki parlak hücreler — bir genişlik ~4 s   (tek · kenarda · oranlı)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  I        İŞARET: ilk kullanım (K04 buna DÖNER)
LENS:           24 mm     MESAFE: 25,0 m     YÜKSEKLİK: 12,0 m
ÖLÇEK:          WS        AÇI TİPİ: göz hizası
KADRAJ ENİ:     37,50 m      kadraja alınacak nesne: gemi 40,0 m · küre 9,0 m · pencere 2,0 m
                          Sığıyor mu: gemi taşar (bilinçli) · küre ve pencere TAM sığar
ANA NESNE PİKSEL: küre 922 px · pencere 205 px — ⭐ iki uç AYNI KAREDE [D78]      ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  C → I · ölçek Δ1 · azimut 110° · bant içi ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — ⛔ KART 10: insan sayısı cümlesi yazılmaz
AYRIM EKSENİ:   —
GİREN NESNE:    gemi gövdesi · üç halka · aydınlık pencere
ÇIKAN NESNE:    —
TAŞINAN NESNE:  küre (K01) → K21'de halkalardan ayrılır  → önceki K01 · sonraki K04
⛔ BİÇİM KİLİDİ: ⚠️ VAR — üç halkanın geometrisi ve pencerenin oranı; referans paketi RA kaydı (gemi) ve RO (küre)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      yalnız kürenin kendi ışığı gövdenin alt kaburgalarını yalıyor; aradaki hava pus taşımaz
           takvim: S1 tek değer · monotonik: evet
PALET:     koyu kızıl-altın / siyah
SES:       alçak uğultu (gövdenin taşıdığı yapısal ses)
MÜZİK:     YOK
FİZİK:     0,38 g · gemi kendi gücüyle ve sabit oranda alçalıyor; görünür egzoz YOK
           ortam kartından bu klibe düşen: kafes kuralı ① ve ② (kısık hâl) · görünür itki YOK → duman/egzoz sınıfı hiç açılmıyor
```

## 🎙️ REPLİK

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      —
```

## ⭐VİRAL — iki satır ZORUNLU (işaretliyse)

```
YÜZ:       —
HAREKET:   —
```

## 🎭 OYUNCULUK — izleyici cümlesi ve niyet kanalı

```
İZLEYİCİ CÜMLESİ: "(insansız klip) Bu ışık buraya ait ve buradan gitmiş."
TAŞIYAN KANAL:    — (insan yok)   (≤2 · OYUNCULUK_YAZIM §3)
TASK ONLY MU:     EVET — bilinçli: ölçek klibi
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D78 | ölçek iddiası TEK KAREDE iki ucuyla: küre 922 px ↔ kapı boyundaki pencere 205 px | pozitif gövdede iki nesne aynı cümlede: `a single lit window the height of a door on the hull's spine, and below it the caged sphere` |
| D157 | novum taşıyıcısı TEK KARE cümlesinde ADIYLA geçer | üçüncü satır: `the caged sphere between the ship's three rings` |
| D172 | askı NEREDE BİTTİĞİNİ söyler | `the three rings run from the spine down around it and end there; nothing else hangs from them, no cable, no hook` |
| D209 | dünya çapası üç cümle | gök: yıldız alanı + parçalanmış ay · ufuk: bazalt kule hattı · yer imi: kaidenin üç taş kemeri |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | #1 yapısal red profili | NEGATIVE kısaltıldı; boşluk pozitif: `no one is at the windows; the hull carries one lit window and nothing else` | ✅ |
| 2 | ⛔ | #3 yasak kökler | küre `held` ve `clamped`; `hang/float/hover` yok | ✅ |
| 3 | ⚠️ | #12 CAMERA satırındaki `tripod` kelimesi | `on a locked-off camera` yazıldı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   EVET   sınıf: PK — gemi `cathedral` ya da `warship` olarak adlandırılmaz
NÖTR TARİF:  gemi BİÇİM olarak: `a long ribbed hull, its spine broken into repeating arches`
POZİTİF KİLİT (yasak cümle yerine): `the sphere is clamped at the focus of the three rings and moves with the hull as one body`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
□ OLAY tek cümleyle yazıldı, BAŞTA/SONDA/SON 3 s ayrı         ✅
□ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px ✅
□ önceki kliple ardışık çift bant içi (ya da şok gerekçeli)     ✅
□ kurulum harfi + işaret satırı yazıldı                       ✅
□ ⛔ uyarıların hepsi kapandı                                  ✅
□ politika satırı yazıldı                                     ✅
□ ⭐VİRAL ise YÜZ + HAREKET satırları var                      ✅
□ kilit fiili SÜREÇ · direnç var · son satır SÜRDÜRME         ✅
→ hepsi ✅ → GUNES_MEZARI_BOLUM_1.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
