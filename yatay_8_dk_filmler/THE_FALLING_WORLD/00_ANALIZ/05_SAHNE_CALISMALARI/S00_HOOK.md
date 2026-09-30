# 🔬 S00 — KİLİT SAHNE · HOOK · SAHNE ÇALIŞMASI · THE_FALLING_WORLD

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
SAHNE:      S00  (sahibin V01'si)      BAŞLIK: Bilek
BÖLÜM:      THE_FALLING_WORLD_BOLUM_1.md      DRAMATİK SAHNE: D1 · Ayaklarının altındaki dünya (S00-S02)
ZAMAN:      0 s → 10 s       ⛔ FORMÜLLE [D122]: sahne(n) = n × 10 s
VURUŞ:      ① Açılış imajı (%0-2) + ② Kurulum (%0-10) · HOOK TİPİ: IN MEDIAS RES
B5 SATIRI:  MUHATAP kurulur — ikinci insan filmin İLK saniyesinde var ve yardıma muhtaç
⭐VİRAL:    EVET → YÜZ ve HAREKET satırları aşağıda
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            TURUNCU yarığa beline kadar düşer; BEYAZ kayarak gelir ve bileğini yakalar.
BAŞTA:           iki gövde yarığın iki yanında, TURUNCU göğsüne kadar içeride, BEYAZ kayarak yaklaşıyor
SONDA:           bir eldiven bir sert manşeti kapatmış, iki gövde tek hat üzerinde
⛔ KLİP İÇİ DEĞİŞİM: VAR — ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687).
   Seçim: ② ARA DURUM YASAĞI cümlesi prompta yazılır
   Gerekçe: hook klibinde değişim sahne SINIRINA taşınamaz — değişimin kendisi kancadır
   ARA DURUM YASAĞI: the grip closes once and stays closed; his wrist is never released and never re-grabbed
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: ilk kullanım
(dönüşü S03'te — o promptta kamera metni BİREBİR kopyalanır + işaret satırı taşınır)
LENS:           24 mm     MESAFE: 6 m     YÜKSEKLİK: ground level
ÖLÇEK:          medium long shot        AÇI TİPİ: low angle
KADRAJ ENİ:     9,0 m      ⛔ HESAPLANDI (§5.2): kesir = boyut × odak ÷ (mesafe × sensör)
                          Kadraja alınacak nesne iki gövde + yarık ağzı, toplam 4,5 m — 9,0 m kadraja rahat girer
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: insan 1,9 m → %37,5 kare yüksekliği = 405 px ✅   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: — (filmin ilk karesi; ardışık çift yok)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   2 — BEYAZ (sol üçte bir, kenarda) · TURUNCU (sağ üçte bir, yarığın içinde)
⛔ FİLM BOYU KİLİT: BEYAZ kadrajın SOL üçte birinde · TURUNCU SAĞ üçte birinde;
   merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
AYRIM EKSENİ:   ÜÇ kanal birden — ① RENK (kirli beyaz + kobalt mavi omuz ↔ yanık
                turuncu + siyah üst kol) ② OMUZ GEOMETRİSİ (köşeli geniş sırt ünitesi
                ↔ dar dikdörtgen sırt ünitesi) ③ KONUM (sol ↔ sağ üçte bir).
                ⛔ Yalnız RENK yetmez — bu sahne P1 paletinde (sert güneş) ve ayrım üç kanalda da açık
GİREN NESNE:    sarı ortak emniyet halatı (iki kemer arasında gevşek) · sol önkoldaki düz alet (görünür ama kullanılmaz)
ÇIKAN NESNE:    —
TAŞINAN NESNE:  yok (filmin ilk sahnesi) → sarı halat S01'e, alet S01'e taşınır
⛔ BİÇİM KİLİDİ: METİNLE TUTULMUYOR [D146] → referans sayfası ŞART: R1 BEYAZ (hasarsız durum) · R2 TURUNCU · R3 HAT AİLESİ
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      tek sert güneş sol üstten, kadraj dışı; gölge kenarları ince atmosferde YUMUŞAK (vakum değil)
           ışık takvimi: tek güneş film boyu SABİT saat yönünde (sol üst, kadraj
           dışı); ardışık sahne arası fark ≤30° ve ≤500 K · monotonik: ✅
PALET:     P1 açık yüzey — pas-kahve zemin, üstte merceklenmiş disk
           ⛔ önceki sahneyle aynı değil: ilk sahne
SES:       Y1 — boğuk uğultu + kask içi İKİ AYRI nefes ritmi + yavaş toz
           ⛔ önceki sahneyle aynı doku değil: ilk sahne
MÜZİK:     YOK — ilk giriş S03'te 2 s. İlk 2 saniyede tek diegetik katman
FİZİK:     §3.2 İNCE ATMOSFER + 0,30 g [D74 kaydı]. 0,30 g: 2 m düşüş ≈ 1,17 s. Yarıktan kalkan toz SÜTUN hâlinde, yavaş ama KESİN oturur. Halat yük almıyor — gevşek.
```

## 🎙️ REPLİK

```
REPLİK:    — (sahnede replik yok)
İŞLEV:     — ilk 10 saniyede söz yok; iki nefes ritmi iki insanı ilan eder
AĞIZ:      okunmuyor — opak vizör, 48/48 sahnede
```

## ⭐VİRAL

```
YÜZ:       — ⛔ DÜRÜST KAYIT: yüz kanalı bu filmde FİZİKEN kapalı (opak vizör,
           sahibin sert kısıtı). ⭐VİRAL'in YÜZ satırı yazılamıyor; etiket
           yalnız HAREKET satırıyla taşınıyor. Bu bir sapmadır [D74] ve
           02_KONSEPT_VE_RISK §2'de bedeliyle birlikte kayıtlı.
HAREKET:   kadrajda HIZLANAN şey kayan gövdedir: BEYAZ ilk 1,2 saniyede yere
           doğru kayar, sonra durur; durduran şey el DEĞİL, yarığın kenarına
           dayanan iki bottur. Kavrama bundan SONRA kapanır ve bir daha açılmaz.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D179 | İmaj = ÇAPA'nın BEFORE'u; düşüş anı karede YOKTUR | IMAGE karesi tutuşun YÜK ALDIĞI anı gösterir: iki bot kenara dayalı, eldiven manşette kapalı — kayma DEĞİL |
| D202 | Çapa üçlüsü CHOICE/COST/FINAL aynı kanalda BEFORE/AFTER gövde çifti | S00 bu üçlünün BEFORE'udur: BEYAZ'ın eli BAŞKASININ bileğinde (S41'de tersi olacak) |
| D146 | Kask tek düz ön pane + kalın koyu gri çerçeve; seamless/dome/bubble yok | her iki kaskta pane tamamen opak; `IN FRAME:` satırına `face` yazılmaz |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | KART 4 — ikinci figür kopyalanması (KRONOS'ta iki vaka) | konum kilidi + `Exactly two human characters, no duplicates, no third person.` | ✅ |
| 2 | ⛔ | İPTAL KAPISI: ilk 10 saniyede "iki insan var ve biri düşüyor" okunmazsa film üretilmez | ölçek MLS ve iki gövde 405 px; ayrım üç kanalda | ✅ |
| 3 | ⚠️ | KART 6 — toz vakum gibi davranırsa ortam kartı bozulur | toz SÜTUN, sayıyla: "two slow dust columns"; "cloud of dust" yasak | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   HAYIR — bu sahnede politika yüzeyi yok
SINIF:       — (alet kadrajda var ama KULLANILMIYOR; kullanımı S02'de)
NÖTR TARİF:  alet adlandırılmaz, FORMU yazılır: a short flat tool on the outside
             of his left forearm [D67]
⛔ YASAK CÜMLE YAZILMAZ — "no cutting", "never drawn" gibi cümleler D123 tuzağıdır.
  POZİTİF KARŞILIĞI: the tool stays flat against his forearm for the whole clip.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve insan 1,9 m → %37,5 kare yüksekliği = 405 px ✅
✅ önceki sahneyle ardışık çift bant içi
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL: HAREKET satırı yazıldı · YÜZ satırı yazılamıyor ve SAPMA olarak kayıtlı
→ hepsi ✅ — THE_FALLING_WORLD_BOLUM_1.md'ye bu sahnenin 📸 + 🎥 promptu YAZILABİLİR
```
