# 🔬 S08 — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · THE_BRITTLE_EDGE

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
SAHNE:      S08            BAŞLIK: Kopuş
BÖLÜM:      THE_BRITTLE_EDGE_BOLUM_2.md
ZAMAN:      80 s → 90 s       ⛔ FORMÜLLE [D122]: 0 + 8 × 10 = 80s - 90s
VURUŞ:      Bedel / Doruk Başlangıcı   B5 SATIRI: BEDEL
⭐VİRAL:    evet             → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Vinç çekişiyle sarı aracın ön tekerleği son kaya çıkıntısından kurtulup boşluğa kayar, zemin teması biter.
BAŞTA:           Ön tekerlek kaya çıkıntısına dayanmış durumdadır; turuncu sapan gerilmeye başlar.
SONDA:           Tekerlek kaya çıkıntısını terk etmiştir; araç tamamen uçurum boşluğuna doğru sarkmaktadır.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz
   Gerekçe: Tekerleğin kayayı terk etmesi tek akıcı planda verilir; aracın aniden terasın üstüne sıçraması yasaklanır.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  E        İŞARET: ilk kullanım
LENS:           28 mm     MESAFE: 3.5 m     YÜKSEKLİK: 1.2 m
ÖLÇEK:          MS        AÇI TİPİ: dramatik alçak açı
KADRAJ ENİ:     3.0 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 1.8 m (kaya kenarı, ön tekerlek ve sapan)
                          Sığıyor mu: evet (1.8m < 3.0m)
ANA NESNE PİKSEL: 340 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: S07'den (WS) S08'e (MS) -1 ölçek kademesi · azimut 50° → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 (terasta duran astronot silueti arka planda)   ⛔ film boyu KİLİT: 1
AYRIM EKSENİ:   Parlak sarı tekerlek jantı, siyah lastik vs koyu bazalt kaya çıkıntısı
GİREN NESNE:    yok        ÇIKAN NESNE: yok
TAŞINAN NESNE:  Kaya çıkıntısını terk eden ön tekerlek → S09'a askıda kalış aktarımı (KÜME)
⛔ BİÇİM KİLİDİ: 6 tekerlekli sarı keşif aracı, sol ön tekerlek ve kaya çıkıntısı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kaya çıkıntısı üzerinde keskin ışık-gölge sınırı; uçurum tarafı mutlak zifiri karanlık
PALET:     Koyu bazalt, sarı gövde, turuncu sapan lifleri, zifiri boşluk
SES:       Son kaya sürtünmesi sesi, ardından kask içinde anlık derin nefes durması ve sessizlik
MÜZİK:     Gerilim bas tonu
FİZİK:     Ay yerçekimi 0,16g; tekerleğin kayadan yavaşça ayrılıp sarkması; balistik mikro regolit parçacıkları
```

## 🎙️ REPLİK (varsa)

Bu film diyalogsuzdur; replik yoktur.

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (arka planda kask araca kilitlenmiş, gergin duruş)
HAREKET:   Tekerlek son desteği terk edip boşluğa kayarken sapan aniden tam yüke biner ve titremeksizin gerilir
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D206 | Bedel bedende ödenmiyor | Karakterin kaskını araca kilitlemesi ve bedenin emniyet kaybıyla gerilmesi |
| D202 | Merkezî seçim ve bedel bedende okunmalı | S08'de son temas koparken astronotun nefesi ve kasılan duruşu |
| D198 | Ay yerçekimi dinamikleri | 0,16g yavaş ve ağır çekim hissi veren salınım |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | S08 sonu ile S09 başı devamlılık sıçraması | S08 son karesi kilitlendi; S09 bu açıyı birebir sürdürür (KÜME) | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Evet   sınıf: YR (Düşme Riski)
NÖTR TARİF:  Tekerleğin kaya zeminle temasının kesilmesi, asılı yükün gergin sentetik kayışla tutulması.
POZİTİF KİLİT: Kontrollü mekanik askı, yuvarlanma veya düşme olmaksızın stabil salınım.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 340 px ≥100 px
[x] önceki sahneyle ardışık çift bant içi (-1 kademe, 50°)
[x] kurulum harfi + işaret satırı yazıldı (E, ilk kullanım)
[x] ⛔ uyarıların hepsi kapandı
[x] politika satırı yazıldı
[x] ⭐VİRAL HAREKET satırı var
→ hepsi ✅, THE_BRITTLE_EDGE_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir.
```
