# 🔬 S47 — KİLİT SAHNE · FINAL · SAHNE ÇALIŞMASI · THE_SLOW_RAIN

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
SAHNE:      S47            BAŞLIK: ELİNİ KALDIRMAZ
BÖLÜM:      THE_SLOW_RAIN_BOLUM_4.md
ZAMAN:      470,0 s → 480,0 s       ⛔ FORMÜLLE [D122]: hook S0 klibin içinde → n × 10 s (klip 10 s VARSAYIM, araçtan ölçülür)
VURUŞ:      KAPANIŞ İMAJI               B5 SATIRI: İLK↔SON
⭐VİRAL:    evet  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Dışarıda kapı önünde durur; damlalar kaskına değip beyaz tortu bırakır, elini kaldırmaz (KAFİYE: S0)
BAŞTA:           kapı önünde, eller belde, damla iniyor
SONDA:           damla kask çerçevesine değer, beyaz puf; el kalkmaz; klip tutulan karede biter
⛔ KLİP İÇİ DEĞİŞİM: YOK [VAR / YOK]
   VAR ise: ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687). İki seçenek:
   ① değişimi sahne SINIRINA taşı  ② ARA DURUM YASAĞI cümlesini prompta yaz
   Seçim: —   Gerekçe: hareket var (damla/puf/el), durum değişimi yok — puf bir olay, kabuk/ışık durumu değişmiyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  A        İŞARET: yeniden tanıtım S0 (kafiye)
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           75 mm     MESAFE: 1.6 m     YÜKSEKLİK: 1.55 m
ÖLÇEK:          CU        AÇI TİPİ: eye-level close-up, frontal · az 0°
KADRAJ ENİ:     0.77 m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne kask + eller 0.45 m
                          Sığıyor mu: ✅   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: 2250 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]   · damla bilye 0,01 m → 50 px (sayılı, seyrek)
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 135°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 × 48 (her karede aynı)
AYRIM EKSENİ:   tek figür — soluk gri giysi ↔ koyu zemin/koyu kanat; teal göğüs bandı   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    damla        ÇIKAN NESNE: —
TAŞINAN NESNE:  kask tortusu (S24'ten) · sırt düz (kanat yok — kadraj dışı)
⛔ BİÇİM KİLİDİ: kask (düz pane + kalın koyu çerçeve) + — — referans paketi YOK (sahip); ilk onaylı kareler referans [D153/D154]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      amber pus dolgusu, tepe, gölge sığ   (ışık takvimi: dış sabit pus dolgusu / iç 3200 K sabit · monotonik: değişmez; iç↔dış geçişleri OLAY)
PALET:     dış amber pus · soluk gri giysi (tortulu)   ⛔ önceki sahneyle aynı olamaz [KURGU_RITMI §2 örüntü kırıcı] — ölçek değişti
SES:       damlanın kaskta 'tok'u; müzik çözülmez
MÜZİK:     var, alçak; son saniyede çözülmez (kadans yok)
FİZİK:     müzik çözülmez, alçak katman   (kart §3.9: sıcak yüzeyde puf 0,5 m / 2 s · rüzgâr yok · gölge sığ · güneş diski 0)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (film sessiz tasarımlı)
İŞLEV:     —
AĞIZ:      — ağız kapalı, konuşma yok
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       gözler damlayı izler, kaş kalkmaz; dudak kenarı düz (S0'ın tersi)
HAREKET:   damla iner, puf kalkar; eller belde — kaldırmamayı seçiyor
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D210 · D62 · KRONOS ⑨ | CAMERA satırı S0 ile BİREBİR + '— the same position, height and lens as Scene 0.' | kopya: A kurulumu cümlesi |
| D202 ÇAPA FINAL | BEFORE (S0): eldiven kalkık, kaş kalkık · AFTER (S47): eldivenler belde, kaş düz | aynı kanal (el + kaş) |
| D211 · D34 | son kare adlandırılmış: kask çerçevesinde beyaz puf, eller belde; kart 0 | 'The take ends on the held frame. No title card appears, no text fades in — the shot simply ends.' (yalnız bu sahnede) |
| ACILIS_KAPANIS §2 | tek değişken gövde (el); kanat kadraj dışı — sırt görünmez | IN FRAME: face · hands; sırt cümlesi YOK |
| TEMA payoff | boş askı (S45) + damla kaskta + el kalkmaz = KİMLİK ödemesi | müzik çözülmez, alçak katman |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U-1 | damla sayılı cümle | ✅ |
| 2 | ⚠️ | U-sarı-6 yüz CU | ≤3 öznitelik; çevre çapası kapı çerçevesi | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   hayır   sınıf: —
NÖTR TARİF:  —   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: 'both gloves stay at her sides for the whole take'
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
→ hepsi ✅ — THE_SLOW_RAIN_BOLUM_4.md'ye bu sahnenin 📸 + 🎥 promptu yazılabilir
```

## 🔗 KART BAĞI · SON 3 s · ÖLÜ SAHNE BEŞ SORUSU (`KARAKTER_KARTI` §10 · `SAHNE_DOLULUGU` §6)

```
KART BAĞI:        İLK↔SON (el kalkmaz) · TEL yok (sakin)
İZLEYİCİ CÜMLESİ: YÜZ: gözler damlayı izler, kaş kalkmaz (S0'ın tersi) · HAREKET: damla iner, puf kalkar; el belde — kaldırmamayı seçiyor
TAŞIYAN KANAL:    BAKIŞ + EL   TASK ONLY: hayır
SON 3 s:          stands with both gloves at her sides; a drop lands on the helmet rim and puffs white; the take ends on that
① FİİL   süreç ✅ (damla iner/puf kalkar, el tutulur)
② DİRENÇ ✅ (ikinci damla yolda)
③ TEK KİLİT ✅ · TIMELINE ≤3 satır
④ SINIR  ✅ (End/Start sınır satırı sahne haritasında)
⑤ SAAT   ✅ (inen damlalar (kenarda, sabit oran))
```
