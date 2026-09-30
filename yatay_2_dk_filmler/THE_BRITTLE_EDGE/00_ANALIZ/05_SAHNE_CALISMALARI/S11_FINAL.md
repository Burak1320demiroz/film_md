# 🔬 S11 — KİLİT SAHNE · FINAL · SAHNE ÇALIŞMASI · THE_BRITTLE_EDGE

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
SAHNE:      S11            BAŞLIK: Denge
BÖLÜM:      THE_BRITTLE_EDGE_BOLUM_2.md
ZAMAN:      110 s → 120 s       ⛔ FORMÜLLE [D122]: 0 + 11 × 10 = 110s - 120s
VURUŞ:      Final / Denge       B5 SATIRI: İSTEK
⭐VİRAL:    evet             → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Astronot kurtarılan sarı keşif aracının yanında durur; elindeki kırık çelik halkaya, sonra sağlam şasiye ve kraterin sonsuzluğuna bakar.
BAŞTA:           Astronot dört tekerleği de terasa oturmuş sarı aracın yanında durmaktadır, eldiveninde kırık çelik parça vardır.
SONDA:           Kamera yavaşça geriye ve yukarıya açılır; krater terasındaki astronot, kurtarılmış araç ve derin vadi geniş planda dengelenir.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz
   Gerekçe: Tek yavaş, pürüzsüz kamera hareketiyle kapanış; ani zıplama veya jenerik kartı yasaklanır.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: dönüş S00 (the same position and height family as Scene 0)
LENS:           40 mm     MESAFE: 2.2 m → 4.5 m (yavaşça açılan kamera)     YÜKSEKLİK: 1.4 m
ÖLÇEK:          MS/CU → WS     AÇI TİPİ: göz hizası
KADRAJ ENİ:     2.0 m → 4.0 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 1.8 m (astronot ve araç önü)
                                  Sığıyor mu: evet (1.8m < 2.0m)
ANA NESNE PİKSEL: 390 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: S10'dan (WS) S11'e (MS/CU) -1 kademe · azimut 60° → bant içi: evet
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 (Astronot Ekin)   ⛔ film boyu KİLİT: 1
AYRIM EKSENİ:   Kirli kırık beyaz basınç giysisi, turuncu kol şeritleri, siyah vizör vs sarı rover gövdesi
GİREN NESNE:    yok        ÇIKAN NESNE: yok
TAŞINAN NESNE:  Kırık çelik kulak parçası ve sağlam sarı keşif aracı (nihai durum)
⛔ BİÇİM KİLİDİ: Altıgen çerçeveli kask, opak siyah vizör, 6 tekerlekli sarı keşif aracı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Krater kenarından süzülen dingin, alçak açılı güneş ışığı; uzun gölgeler
PALET:     Donuk bazalt grisi, endüstriyel sarı, kırık beyaz, derin uzay siyahı
SES:       Kask içinde yavaşlayan ve sakinleşen soluk alıp verme, uzaktan gelen hafif mekanik soğuma çıtırtısı
MÜZİK:     Dingin, felsefi kapanış tınısı
FİZİK:     Ay yerçekimi 0,16g; durağan, dengeli postür; havada uçuşan toz yok
```

## 🎙️ REPLİK (varsa)

Bu film diyalogsuzdur; replik yoktur.

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (opak siyah vizörde kraterin ve sarı aracın yansıması)
HAREKET:   Kamera tek pürüzsüz akışla geriye ve yukarıya doğru yükselerek kurtarılmış koca aracı ve tek astronotu kraterin devasa ölçeğinde yalnız bırakır
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D62 | Kurguda final sahnesinin düşmesi | S11 finali tek yavaş kamera hareketiyle bağımsız vuruş olarak korunur |
| D210 | Kafiye çifti | S00 kopan parça ile S11 kurtarılan sağlam şasi kafiyesi |
| D34 | Model ekrana başlık kartı ekliyor | No title card, no end credits, no overlay text |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Final sahnesinin aceleye getirilmesi | 10 saniyelik tek plan yavaş geri çekilme hareketiyle planlandı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Ay yüzeyinde keşif aracı yanında duran bir astronotun genişleyen kadrajı.
POZİTİF KİLİT: Güvenli tamamlanış, durağan ve dingin kompozisyon.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 390 px ≥100 px
[x] önceki sahneyle ardışık çift bant içi (-1 kademe, 60°)
[x] kurulum harfi + işaret satırı yazıldı (A, dönüş S00)
[x] ⛔ uyarıların hepsi kapandı
[x] politika satırı yazıldı
[x] ⭐VİRAL HAREKET satırı var
→ hepsi ✅, THE_BRITTLE_EDGE_BOLUM_2.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir.
```
