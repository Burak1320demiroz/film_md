# 🔬 S24 — KİLİT SAHNE · NOVUM · SAHNE ÇALIŞMASI · THE_SLOW_RAIN

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
SAHNE:      S24            BAŞLIK: DAMLALARIN ARASINDA
BÖLÜM:      THE_SLOW_RAIN_BOLUM_3.md
ZAMAN:      240,0 s → 250,0 s       ⛔ FORMÜLLE [D122]: hook S0 klibin içinde → n × 10 s (klip 10 s VARSAYIM, araçtan ölçülür)
VURUŞ:      ORTA NOKTA · novum 4. nesne               B5 SATIRI: ENGEL: yağmur bedende
⭐VİRAL:    evet  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Damla perdesi omuz hizasında; her adımda kaskına damla değip beyaz tortu bırakıyor (TEK KARE)
BAŞTA:           damlalar omuz hizasında iniyor
SONDA:           üç damla kaska değer, üç beyaz puf; yürür
⛔ KLİP İÇİ DEĞİŞİM: YOK [VAR / YOK]
   VAR ise: ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687). İki seçenek:
   ① değişimi sahne SINIRINA taşı  ② ARA DURUM YASAĞI cümlesini prompta yaz
   Seçim: —   Gerekçe: hareket var (damla/puf/el), durum değişimi yok — puf bir olay, kabuk/ışık durumu değişmiyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  R        İŞARET: küme S23
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           35 mm     MESAFE: 3.5 m     YÜKSEKLİK: 1.50 m
ÖLÇEK:          MS        AÇI TİPİ: eye-level medium shot, three-quarter front · az 45°
KADRAJ ENİ:     3.60 m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne figür üst gövde + damlalar 0.9 m
                          Sığıyor mu: ✅   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: 960 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]   · damla bilye 0,01 m → 10 px (sayılı, seyrek)
ÖNCEKİ SAHNEYLE: ölçek kademesi 0 · azimut 0°   → bant içi: küme
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 × 48 (her karede aynı)
AYRIM EKSENİ:   tek figür — soluk gri giysi ↔ koyu zemin/koyu kanat; teal göğüs bandı   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    damlalar (omuz hizası)        ÇIKAN NESNE: —
TAŞINAN NESNE:  kızak + çekirdek (omuz kayışı) → S25
⛔ BİÇİM KİLİDİ: kask (düz pane + kalın koyu çerçeve) + kızak/kanat (S15 onaylı karesi imaj referansı) — referans paketi YOK (sahip); ilk onaylı kareler referans [D153/D154]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      amber pus dolgusu, tepe, gölge sığ   (ışık takvimi: dış sabit pus dolgusu / iç 3200 K sabit · monotonik: değişmez; iç↔dış geçişleri OLAY)
PALET:     (küme S23) (küme — aynı vuruşun devam klibi)
SES:       (küme S23) + kaskta 'tok'lar
MÜZİK:     alçak katman (var) — damla tokları önde
FİZİK:     damla ~3 m/s, seyrek sayılabilir   (kart §3.9: sıcak yüzeyde puf 0,5 m / 2 s · rüzgâr yok · gölge sığ · güneş diski 0)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (film sessiz tasarımlı)
İŞLEV:     —
AĞIZ:      — ağız kapalı, konuşma yok
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       her pufta göz kapanıp açılır, çene sıkı, bakış ileride (üsse)
HAREKET:   damlalar inerken adım sürer; üç puf kalkar; kızak kayışı omuzda gergin
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D157 TEK KARE | taşıyıcı damla kadrajın ≥1/10'u; ikinci olay yok | üçüncü satır: 'A few dozen large drops the size of marbles descend at a slow jogging pace through the frame around her at shoulder height; three of them meet her helmet rim in the take and each flashes into a white puff.' |
| D208 · D42 | kask tortusu S24'ten itibaren sabit bölge (çerçeve üstü) | imaj: 'a thin white rime along the top of the helmet rim' — pane berrak |
| D200 | damla sabit hız; bu karede düşen nesne yok | PHYSICS satırı: 'the drops fall at one steady rate, slowed by the dense air' |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U-1 | sayılı novum cümlesi birebir; iptal kapısı S24 | ✅ |
| 2 | ⚠️ | U-sarı-3 plato | küme S23 devamı; her adımda puf = görünür olay | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  —   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: 'she keeps walking between the drops at one steady pace'
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px
✅ önceki sahneyle ardışık çift bant içi (ya da şok gerekçeli)
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL ise YÜZ + HAREKET satırları var
→ hepsi ✅ — THE_SLOW_RAIN_BOLUM_3.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```

## 🔗 KART BAĞI · SON 3 s · ÖLÜ SAHNE BEŞ SORUSU (`KARAKTER_KARTI` §10 · `SAHNE_DOLULUGU` §6)

```
KART BAĞI:        ZAAF (kask tortusu başlar) · İSTEK sürer
İZLEYİCİ CÜMLESİ: YÜZ: her pufta göz kapanıp açılır, çene sıkı · HAREKET: damlalar iniyor, puflar kalkıyor, adım sürüyor — durmak istemiyor
TAŞIYAN KANAL:    NEFES + MESAFE   TASK ONLY: hayır
SON 3 s:          walks on between the hanging drops at the same pace, three white puffs rising off her helmet
① FİİL   süreç ✅ (yürür, puflar kalkar)
② DİRENÇ ✅ (adım kabuklu bacakla)
③ TEK KİLİT ✅ · TIMELINE ≤3 satır
④ SINIR  ✅ (End/Start sınır satırı sahne haritasında)
⑤ SAAT   ✅ (inen damlalar (kenarda, sabit oran))
```
