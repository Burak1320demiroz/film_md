# 🔬 K01 — KİLİT KLİP · HOOK · SAHNE ÇALIŞMASI · THE_LAST_TOW

> ⛔ Başlık biçimi `## 🔬 S<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur ve bu klasörü ayrı bir
> film sanmasının tek yolu budur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.
>
> Girdi: `03_SAHNE_SIRALAMASI.md` satırı + `04_UYARI_NOTLARI.md`'nin bu
> klibe düşen satırları. Bu dosya bitmeden bu klibin promptu yazılmaz.

---

## 🪪 KİMLİK

```
KLİP:       K01  ·  SAHNE S01 (1/4 · BELİRİŞ)      BAŞLIK: RESİF
BÖLÜM:      THE_LAST_TOW_BOLUM_1.md
ZAMAN:      0,0 s → 10,0 s     ⛔ FORMÜLLE: klip başlangıcı(n) = (n−1) × 10,0 s
VURUŞ:      açılış imajı — filmin ilk sorusu
B5 SATIRI:  ENGEL (kural kurulur)
⭐VİRAL:    hayır — kadrajda insan yok, yüz kanalı kapalı
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Dik duran çelik anahtar duruyor; yalnız gölgesi 3 mm kayıyor.
BAŞTA:           insansız kadraj; bir metal levhanın üstünde 56 cm'lik çelik anahtar DİK duruyor
SONDA:           aynı duruş; tek değişen şey gölgenin 3 mm kayması — zaman geçtiğinin tek kanıtı
⛔ KLİP İÇİ DEĞİŞİM: VAR — bir eşik geçiliyor (bu rejimde her klip bir
   değişim taşır; ölçülmüş en zayıf eksen, T2V-CompBench 0,0687)
   Seçim: ② ARA DURUM cümlesi prompta yazılıyor
   Gerekçe: değişim minimumda tutuldu: hook bir DURUM sorusudur, olay değil. Gölgenin kayması hem zamanı hem ışık kenarının yaklaştığını tek kareyle söylüyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  C        İŞARET: ilk kullanım
LENS:           50 mm     MESAFE: 2,4 m     YÜKSEKLİK: 1,45 m
ÖLÇEK:          MS (3)        AÇI TİPİ: göz hizası
KADRAJ ENİ:     1,73 m      ⛔ HESAPLANDI (36 mm / f × mesafe)
                          kadraja alınacak nesne anahtar 0,56 m → SIĞIYOR ✅ (⚠️ ilk kurulum D'ydi:
                          85 mm/1,1 m kadrajı 0,47 m ve 56 cm'lik anahtar SIĞMIYORDU — optik
                          aritmetiği bu kareyi kurtardı, kurulum C'ye taşındı)
ANA NESNE PİKSEL: 1242 px   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  ölçek kademesi — (filmin ilk klibi) · azimut —°   → bant içi: n/a
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — ⛔ `No people, no figures, no silhouettes of people.` (red #2 YR: sayım cümlesi KURULMAZ)
AYRIM EKSENİ:   n/a (tek nesne)
GİREN NESNE:    anahtar (filmin ilk nesnesi)
ÇIKAN NESNE:    —
TAŞINAN NESNE:  anahtar → bir sonraki görülüşü K03 (tekmelenecek)
⛔ BİÇİM KİLİDİ: anahtar: 56 cm uzun, düz açık ağızlı, koyu çelik — tek ölçü, film boyu aynı [D146 kalıbı]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      fenerin ışığı kadraj dışından yandan; gölge mutlak siyah, jilet keskin, dolgu 0
           ışık takvimi: gölge kenarı dikişe 4,80 m · monotonik ✅ (tek yön)
PALET:     GÖLGE   ⛔ önceki sahneyle aynı değil
SES:       ilk 2 saniye temas yok; sonra gövdeden iletilen tek kuru tık
MÜZİK:     yok — S1 müziksiz (MUZIK dosyası)
FİZİK:     0,30 g · hard vakum · metalin üstünde 0 kare toz · gölge mutlak
           siyah, dolgu 0 · pas 0 · kıvılcım 0 · dışarıda ses yok
```

## 🎙️ REPLİK

```
REPLİK:    — (film boyu 0 replik)
İŞLEV:     — ⛔ boş replik yazılmadı, SİLİNMİŞ sayılmaz: SPEC'te sayıyla 0
AĞIZ:      okunmuyor — ağız vizör ardında ve film boyunca konuşmuyor
```

## ⭐VİRAL — yalnız işaretli klipte, İKİ satır ZORUNLU

```
— (bu klip ⭐VİRAL değil; ölçütü YÜZ + HAREKET ve ikisi de yok)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D157 | novum taşıyıcısı TEK KARE testini geçiyor: cümle anahtarın ADINI taşıyor | gövde ilk cümlesi anahtarla açılır |
| D138 | metalde bilgi taşıyan tek üç şey: 8 mm dikiş · 40 mm perçin · 1-20 cm çukur | pozitif üç kalem cümlesi |
| D59 | kaynak kuralı YASAK olarak yazılmaz | anahtarın DURUŞU yazılır, "kaymaz" yazılmaz |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | kuralın bütün kanıtları yokluk olursa okunmaz (U-1) | bu klip bilerek YOKLUK kanıtıdır — ama tek başına bırakılmıyor, K03 aynı anahtarı POZİTİF olayla kanıtlıyor | ✅ |
| 3 | ⚠️ | insansız klip + uzun negatif = yapısal red (U-3) | negatif çekirdeğin 8 cümlesinden 5'i yazılıyor, insan sayımı kurulmuyor | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⚠️ evet — sınıf YR (yapısal red): insansız kadraj
NÖTR TARİF:  nesne bir el aleti; tehdit sözlüğü yok, gerilim yalnız DURUŞTAN
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilit: `the wrench stands upright on the bare plate, its handle clear of the metal` — duruş yazılır, yasak yazılmaz
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 1242 px ≥ 100
☑ önceki kliple ardışık çift bant içi (n/a)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları gerekmedi (⭐VİRAL değil)
→ hepsi ✅ → THE_LAST_TOW_BOLUM_1.md'ye bu klibin IMAGE + VIDEO promptu yazılabilir
```
