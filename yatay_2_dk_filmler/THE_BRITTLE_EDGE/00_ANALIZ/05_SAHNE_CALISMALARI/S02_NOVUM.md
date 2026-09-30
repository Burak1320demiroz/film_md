# 🔬 S02 — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · THE_BRITTLE_EDGE

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
SAHNE:      S02            BAŞLIK: Teşhis
BÖLÜM:      THE_BRITTLE_EDGE_BOLUM_1.md
ZAMAN:      20 s → 30 s       ⛔ FORMÜLLE [D122]: 0 + 2 × 10 = 20s - 30s
VURUŞ:      Novum Tanıtımı   B5 SATIRI: ENGEL
⭐VİRAL:    orta
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Astronot kopan metal parçayı regolitten kaldırır; bükülmesiz, düz ve keskin kırık yüzeyini inceler.
BAŞTA:           Kırık çelik kulak parçası koyu bazalt regolit üzerinde durmaktadır; kalın eldivenli el kadraja uzanır.
SONDA:           Eldivenli parmaklar parçayı 15° güneş ışığına doğru çevirir; düz ve pürüzsüz kırılma yüzeyi parlar.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz
   Gerekçe: Eğilip alma ve yüzeyi inceleme tek kesintisiz planda gerçekleşir; eldivenin parçayı bırakması veya başka alete geçmesi yasaklanır.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  C        İŞARET: ilk kullanım
LENS:           50 mm     MESAFE: 0.6 m     YÜKSEKLİK: 0.4 m
ÖLÇEK:          ECU       AÇI TİPİ: alçak açı
KADRAJ ENİ:     0.4 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 0.15 m (kırık metal parçası ve parmak uçları)
                          Sığıyor mu: evet (0.15m < 0.4m)
ANA NESNE PİKSEL: 550 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: S01'den (WS) S02'ye (ECU) ölçek -3 kademe · azimut 50° → bant içi: evet (şok kesme novum vurgusudur)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 (yalnız eller kadrajda)   ⛔ film boyu KİLİT: 1
AYRIM EKSENİ:   Ağır kirli beyaz basınç eldiveni, turuncu bilek manşeti vs soğuk gri çelik
GİREN NESNE:    Eldivenli el (kadraj üstünden girer)   ÇIKAN NESNE: yok
TAŞINAN NESNE:  Kırık çelik parça (S00'dan gelir) → S03'te yere bırakılır
⛔ BİÇİM KİLİDİ: 40mm et kalınlığında, düz kırılmış çelik silindirik halka parçası
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Kırılma yüzeyine çarpan 15° alçak açılı doğrudan güneş yansıması
PALET:     Donuk bazalt grisi, donuk çelik, kirli kırık beyaz eldiven, turuncu manşet
SES:       Kask içi hızlı soluk alıp verme, eldivenin metale sürtünme mikro titreşimi
MÜZİK:     yok (sessiz gerilim)
FİZİK:     Ay yerçekimi 0,16g; parçanın eldivende hafifçe dengelenmesi; kriyojenik gevrek kırılma mikroyapısı
```

## 🎙️ REPLİK (varsa)

Bu film diyalogsuzdur; replik yoktur.

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (yalnız eldivenli eller kadrajda)
HAREKET:   Eldiven parçayı kaldırıp ışık altında çevirir; düz çatlak yüzeyinin pürüzsüzlüğü kanıtlanır
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D78 | Novum sahneler arası ekranda kanıtlanmıyor | S02'de kırık yüzeyin yakın planı gevrek kırılmayı tek karede gösterir |
| D157 | Novum taşıyıcısı tek karede okunmuyor | Kırık çelik çekme kulağı ve çatlak hattı kadraj merkezinde net görünür |
| D174 | Yön kadrajdaki nesneyle verilir | Işık krater kenarı açısından gelir, el parçayı güneşe doğru eğer |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⚠️ | Novumun ekranda ~60 piksel kalıp okunmama riski | 50mm ECU kullanıldı, kırık metal parçası kadrajda 550 piksel kaplar | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Hayır
NÖTR TARİF:  Eldivenli bir elin düz kırılmış metal parçayı tutarak incelemesi.
POZİTİF KİLİT: Statik mekanik inceleme, zararsız nesne tutuşu.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 550 px ≥100 px
[x] önceki sahneyle ardışık çift bant içi (-3 kademe, 50°)
[x] kurulum harfi + işaret satırı yazıldı (C, ilk kullanım)
[x] ⛔ uyarıların hepsi kapandı
[x] politika satırı yazıldı
→ hepsi ✅, THE_BRITTLE_EDGE_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir.
```
