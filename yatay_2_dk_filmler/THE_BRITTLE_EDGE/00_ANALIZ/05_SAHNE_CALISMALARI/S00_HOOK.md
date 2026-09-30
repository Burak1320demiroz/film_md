# 🔬 S00 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · THE_BRITTLE_EDGE

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
SAHNE:      S00            BAŞLIK: Kırılma
BÖLÜM:      THE_BRITTLE_EDGE_BOLUM_1.md
ZAMAN:      0 s → 10 s       ⛔ FORMÜLLE [D122]: hook + (n−1) × klip = 0 + 0 = 0s - 10s
VURUŞ:      Hook             B5 SATIRI: ENGEL
⭐VİRAL:    evet             → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Vinç gerilimi altında çelik çekme kulağı bükülmeden aniden ikiye ayrılır.
BAŞTA:           Çelik çekme kulağı gergin vinç kablosuyla çekilmektedir, yüzeyi donuk ve çatlaklıdır.
SONDA:           Çelik kulak ikiye bölünmüş, kablo boşluğa fırlamış, araç geriye kaymaya başlamıştır.
⛔ KLİP İÇİ DEĞİŞİM: VAR
   Seçim: ② ARA DURUM YASAĞI cümlesini prompta yaz
   Gerekçe: Kopma anı tek kesintisiz çekimde gerçekleşmeli; elastik uzama veya eğilme ara durumu yasaklanır, doğrudan ani gevrek kırılma gösterilir.
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: ilk kullanım
LENS:           50 mm     MESAFE: 1.0 m     YÜKSEKLİK: 0.8 m
ÖLÇEK:          CU        AÇI TİPİ: göz hizası (hafif açılı)
KADRAJ ENİ:     0.7 m     ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne 0.25 m (çekme kulağı ve kablo)
                          Sığıyor mu: evet (0.25m < 0.7m)
ANA NESNE PİKSEL: 420 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: açılış sahnesi (S00)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 (yakın nesne planı)   ⛔ film boyu KİLİT: 1
AYRIM EKSENİ:   Donuk gri çelik ve siyah vinç kablosu vs sarı şasi montaj plakası
GİREN NESNE:    yok        ÇIKAN NESNE: kopan kablo ucu (kadraj dışına fırlar)
TAŞINAN NESNE:  Kopan çelik çekme kulağı → sonraki S01 ve S02
⛔ BİÇİM KİLİDİ: Çelik silindirik halka biçimi, 40mm et kalınlığı, endüstriyel cıvata bağlantısı
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      Krater kenarından 15° alçak açılı sert tek yönlü güneş ışığı; derin siyah gölge
PALET:     Donuk bazalt grisi, endüstriyel parlak sarı şasi kenarı, mat siyah çelik kablo
SES:       Kablo gerilim iniltisi ve aniden keskin metalik kırılma "çat" sesi
MÜZİK:     yok (doğal gerilim)
FİZİK:     Ay yerçekimi 0,16g; kriyojenik gevrek kırılma (DBTT); plastik deformasyon yok; kıvılcım yok
```

## 🎙️ REPLİK (varsa)

Bu film diyalogsuzdur; replik yoktur.

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       — (kadrajda nesne yakın planı var, kask yok)
HAREKET:   Gergin çelik halka direnç göstermeksizin aniden çatlar, kablo kadraj dışına fırlarken araç hızla geriye kayar
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D192 | Metal kopması cam tozu veya kıvılcıma dönüyor | 2 parçaya ayrılan çelik halka, 1 çatlak çizgisi, 0 kıvılcım, 0 cam tozu |
| D157 | Novum taşıyıcısı tek karede okunmuyor | Çelik çekme kulağının kırık iki parçası ve sarı gövde aynı kadrajda net görünür |
| D1 | AI klip içinde montaj yapıyor | Tek kesintisiz çekim; no cuts, no montage |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | S00 metal kopmasının cam tozu veya kıvılcıma dönüşmesi riski | Sayısal kilit verildi: 2 parça, 1 düz çatlak hattı, 0 kıvılcım, 0 cam tozu | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   Evet   sınıf: MÇ (Mekanik Kopma)
NÖTR TARİF:  İki metal silindirik halkanın gerilim altında birbirinden ayrılması.
POZİTİF KİLİT: Temiz, sessiz mekanik ayrılma; patlama, alev veya kıvılcım olmaksızın çatlama.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
[x] OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
[x] optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 420 px ≥100 px
[x] açılış sahnesi kurulum A
[x] kurulum harfi + işaret satırı yazıldı
[x] ⛔ uyarıların hepsi kapandı
[x] politika satırı yazıldı
[x] ⭐VİRAL HAREKET satırı var
→ hepsi ✅, THE_BRITTLE_EDGE_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir.
```
