# 🔬 K03 — KİLİT KLİP · NOVUM · SAHNE ÇALIŞMASI · THE_LAST_TOW

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
KLİP:       K03  ·  SAHNE S01 (3/4 · KANIT)      BAŞLIK: RESİF
BÖLÜM:      THE_LAST_TOW_BOLUM_1.md
ZAMAN:      20,0 s → 30,0 s     ⛔ FORMÜLLE: klip başlangıcı(n) = (n−1) × 10,0 s
VURUŞ:      kuralın BİRİNCİ pozitif kanıtı
B5 SATIRI:  ENGEL · kanıt
⭐VİRAL:    hayır — yüz kadrajda yok
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Botun burnu anahtara değiyor; anahtar 0 cm kaymıyor, düştüğü yerde saplı kalıyor.
BAŞTA:           bot anahtarın 20 cm yanında, ağırlık geride
SONDA:           bot anahtara değmiş ve geçmiş; anahtar aynı yerde, aynı açıda — kaymadı, devrilmedi
⛔ KLİP İÇİ DEĞİŞİM: VAR — bir eşik geçiliyor (bu rejimde her klip bir
   değişim taşır; ölçülmüş en zayıf eksen, T2V-CompBench 0,0687)
   Seçim: ② ARA DURUM cümlesi prompta yazılıyor
   Gerekçe: ⭐ bu filmin en önemli klibi olabilir: kural burada YOKLUKTAN OLAYA çevriliyor. Değişim botun hareketidir, anahtarın hareketsizliği SONUÇtur
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  B        İŞARET: ilk kullanım
LENS:           35 mm     MESAFE: 6,0 m     YÜKSEKLİK: 1,50 m
ÖLÇEK:          WS (2)        AÇI TİPİ: göz hizası
KADRAJ ENİ:     6,17 m      ⛔ HESAPLANDI (36 mm / f × mesafe)
                          kadraja alınacak nesne anahtar 0,56 m + bot 0,32 m — ikisi aynı kadrajda → SIĞIYOR ✅
ANA NESNE PİKSEL: 348 px   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  ölçek kademesi 1 (EWS 1 → WS 2) · azimut 75°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 — `Exactly one human character, no duplicates, no second person.`
AYRIM EKSENİ:   n/a (tek gövde)
GİREN NESNE:    bot (kadının ilk görünüşü)
ÇIKAN NESNE:    —
TAŞINAN NESNE:  anahtar K01'den geliyor; bu klipten sonra kadraja girmiyor
⛔ BİÇİM KİLİDİ: bot: seramik kaplı, koyu gri, tabanı düz — ⛔ seramik kaplama KAYNAMAZ, asimetrinin pozitif ayağı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      fenerin ışığı kadraj dışından yandan; gölge mutlak siyah, jilet keskin, dolgu 0
           ışık takvimi: gölge kenarı dikişe 4,40 m · monotonik ✅ (tek yön)
PALET:     GÖLGE   ⛔ önceki sahneyle aynı değil
SES:       botun gövdeden iletilen kuru teması; anahtardan tek tık, yankı yok
MÜZİK:     yok — S1 müziksiz
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
— (bu klip ⭐VİRAL değil)
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D151 | kural POZİTİF OLAYLA kanıtlanır, yoklukla değil | bot DEĞİYOR (olay), anahtar KALIYOR (sonuç) |
| D59 | asimetri POZİTİF yazılır | `the ceramic-coated boot does not join; bare metal that touches bare metal stays joined` |
| U-1 | dört zorunlu kanıt klibinin BİRİNCİSİ | SPEC A: bu klip kurgudan çıkarılamaz |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | kural ekranda okunmuyor (U-1) | dört kanıt klibinin ilki; kart §3.8'in (c) kanıtı birebir uygulandı | ✅ |
| 9 | ⚠️ | "kaynamaz" demek yasak cümle tuzağı (D123) | asimetri pozitif hâlde, iki yarım cümlede | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır
NÖTR TARİF:  bir alete dokunan bir bot; şiddet ya da hasar sözlüğü yok
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilit: `the wrench keeps its exact position and angle after the boot passes`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 348 px ≥ 100
☑ önceki kliple ardışık çift bant içi (✅)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları gerekmedi
→ hepsi ✅ → THE_LAST_TOW_BOLUM_1.md'ye bu klibin IMAGE + VIDEO promptu yazılabilir
```
