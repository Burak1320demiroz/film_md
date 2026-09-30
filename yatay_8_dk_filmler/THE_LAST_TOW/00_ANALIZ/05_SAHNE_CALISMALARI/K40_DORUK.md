# 🔬 K40 — KİLİT KLİP · DORUK · SAHNE ÇALIŞMASI · THE_LAST_TOW

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
KLİP:       K40  ·  SAHNE S10 (4/4 · BEDEL)      BAŞLIK: DÜŞÜŞ
BÖLÜM:      THE_LAST_TOW_BOLUM_2.md
ZAMAN:      390,0 s → 400,0 s     ⛔ FORMÜLLE: klip başlangıcı(n) = (n−1) × 10,0 s
VURUŞ:      doruk ① — yükün bedende okunduğu kare
B5 SATIRI:  BEDEL bedende
⭐VİRAL:    EVET — ⭐VİRAL adayı (ölçülecek, hedef değil)
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Yük kadının önkollarında; omuz hattı 4 cm düşüyor ve nefesi iki kez kesiliyor.
BAŞTA:           ikinci giysi öne devrilmiş, kadının önkolları göğüs hizasında altına girmiş
SONDA:           yük taşınıyor; omuz hattı 4 cm aşağıda, dizler 8 cm bükülmüş, nefes iki kez kesilmiş
⛔ KLİP İÇİ DEĞİŞİM: VAR — bir eşik geçiliyor (bu rejimde her klip bir
   değişim taşır; ölçülmüş en zayıf eksen, T2V-CompBench 0,0687)
   Seçim: ② ARA DURUM cümlesi prompta yazılıyor
   Gerekçe: değişim EFOR eğrisidir: yük sabit, taşıyan gövde değişiyor. KRONOS ⑧ WEIGHTLESS WORK bulgusunun karşı önlemi tam burada
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  I        İŞARET: dönüş K38
LENS:           50 mm     MESAFE: 2,6 m     YÜKSEKLİK: 2,30 m
ÖLÇEK:          MS (3)        AÇI TİPİ: üst açı (20° aşağı)
KADRAJ ENİ:     1,87 m      ⛔ HESAPLANDI (36 mm / f × mesafe)
                          kadraja alınacak nesne iki gövde göğüsten yukarı + yük — 1,87 m kadraja sığıyor → SIĞIYOR ✅
ANA NESNE PİKSEL: 1231 px   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  ölçek kademesi 1 (CU 4 → MS 3) · azimut 90°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1 — ⛔ ikinci giysi bir NESNEdir: `Exactly one human character` cümlesi burada da doğru
AYRIM EKSENİ:   ⭐ GEOMETRİ: kadının omzunda kaburga hattı ve kemerinde kesici yuvası var; ikinci giysinin omzu DÜZ, kemeri YOK, vizörü KOYU. Renk ayrımı kullanılmıyor (U-5)
GİREN NESNE:    —
ÇIKAN NESNE:    —
TAŞINAN NESNE:  ikinci giysi K31'den geliyor → K46'da çekicinin kızağına bırakılacak
⛔ BİÇİM KİLİDİ: ikinci giysi: omuz kare, vizör koyu ve hiçbir şey vermiyor, kemer yok — her göründüğü klipte aynı üç kelime
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      gölge kenarı güvertede; dikey yüzeyler 370 K'de parlak, zemin 180 K'de koyu; dolgu 0
           ışık takvimi: gölge kenarı dikişe güvertede (0 m) — kapağın yüzünü geçmiş · monotonik ✅ (tek yön)
PALET:     IŞIK   ⛔ önceki sahneyle aynı değil
SES:       iki kopuşun kuru sesi, sonra yükün gövdeden iletilen basıncı; vizör içinde iki kesilmiş nefes
MÜZİK:     var — tek alçak katman, S10 boyunca kesilmiyor
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
YÜZ:       vizör ardında çene hattı geriliyor ve göz çevresi kısılıyor; ifade
           "hazır" değil "beklenmedik ağırlık" — değişim 10 saniyenin içinde OLUYOR
HAREKET:   kadrajın ortasında 78 kg'lık bir gövde 0,35 m öne geliyor ve duruyor;
           kareler arası piksel değişimi filmin en yükseği
⚠️ Ölçütü taşıyor ama ⭐VİRAL bir HEDEF değil: §2.3 kartının bandı 0-3 ve
  belirleyici değişken, bu kurulumun klibinde İKİNCİ bir hacim olayı olup
  olmadığıdır (28.09.2026 üçüncü ölçüm). Burada var: kopuş + yük.
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D206 | bedel BEDENDE ödenir | omuz 4 cm · diz 8 cm · nefes iki kez — üç sayı |
| D207 | yorgunluk kesmede sıfırlanmaz | S11'in ilk klibi bu duruşu CONTINUOUS ACTION ile devralır |
| D127 | ivme yazılmaz, süre ve mesafe yazılır | `comes forward 0.35 m and stops` |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 6 | ⛔ | WEIGHTLESS WORK — 0,30 g'de yük hafif render ediliyor (U-6) | üç kanal birden: omuz · diz · nefes; ağırlık sayıyla ve göğüs hizasında | ✅ |
| 5 | ⚠️ | iki koyu gövde renkle ayrılmıyor (U-5) | ayrım geometride: kaburga hattı ↔ düz omuz, kemer ↔ kemersiz, koyu vizör | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⚠️ evet — sınıf PB: bir insan biçiminin devrilip tutulması (red #3 ailesi)
NÖTR TARİF:  `a sealed second pressure suit, upright on the deck, tips forward as the two boot soles release; her gloved forearms take the weight level with her chest` — düşen bir NESNE, taşıyan bir GÖVDE
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilit: `the suit keeps its rigid shape and its dark visor throughout; nothing bends, nothing opens`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
☑ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
☑ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve 1231 px ≥ 100
☑ önceki kliple ardışık çift bant içi (✅)
☑ kurulum harfi + işaret satırı yazıldı
☑ ⛔ uyarıların hepsi kapandı
☑ politika satırı yazıldı
☑ ⭐VİRAL satırları YAZILDI (YÜZ + HAREKET)
→ hepsi ✅ → THE_LAST_TOW_BOLUM_2.md'ye bu klibin IMAGE + VIDEO promptu yazılabilir
```
