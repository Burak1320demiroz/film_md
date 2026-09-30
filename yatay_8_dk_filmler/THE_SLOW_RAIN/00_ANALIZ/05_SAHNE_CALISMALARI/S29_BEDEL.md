# 🔬 S29 — KİLİT SAHNE · BEDEL · SAHNE ÇALIŞMASI · THE_SLOW_RAIN

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
SAHNE:      S29            BAŞLIK: KAYIŞI KESER
BÖLÜM:      THE_SLOW_RAIN_BOLUM_3.md
ZAMAN:      290,0 s → 300,0 s       ⛔ FORMÜLLE [D122]: hook S0 klibin içinde → n × 10 s (klip 10 s VARSAYIM, araçtan ölçülür)
VURUŞ:      HER ŞEYİN KAYBI (bedel)               B5 SATIRI: BEDEL: kanatlar · S29
⭐VİRAL:    evet  → evet ise YÜZ ve HAREKET satırları aşağıda ZORUNLU
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Elini tokaya götürür, iki parmak durur (KIRILMA); çekirdeğin kayışını keser, çekirdeği kucağına alır; kanatları çukurda bırakır (BEDEL)
BAŞTA:           el tokaya gider, iki parmak durur (KIRILMA)
SONDA:           kesici kayışı ayırır; çekirdek kucakta, kesik kayış tokada sallanır; kanat çukurda kalır
⛔ KLİP İÇİ DEĞİŞİM: YOK [VAR / YOK]
   VAR ise: ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687). İki seçenek:
   ① değişimi sahne SINIRINA taşı  ② ARA DURUM YASAĞI cümlesini prompta yaz
   Seçim: —   Gerekçe: hareket var (damla/puf/el), durum değişimi yok — puf bir olay, kabuk/ışık durumu değişmiyor
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  Y        İŞARET: ilk kullanım
⛔ dönüş veya küme ise kamera metni BİREBİR kopyalanır + işaret satırı taşınır

LENS:           75 mm     MESAFE: 1.5 m     YÜKSEKLİK: 1.40 m
ÖLÇEK:          CU        AÇI TİPİ: eye-level close-up, full profile · az 90°
KADRAJ ENİ:     0.72 m      ⛔ HESAPLANDI (§5.2) — kadraja alınacak nesne göğüs + toka + çekirdek 0.5 m
                          Sığıyor mu: ✅   [OPEN CIRCUIT: 5 kurulumun 5'i tutmuyordu]
ANA NESNE PİKSEL: 2667 px   ⛔ ≥100 px [D179 · ~60 px ekranda okunmuyor]
ÖNCEKİ SAHNEYLE: ölçek kademesi 1 · azimut 45°   → bant içi: ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ film boyu KİLİT: 1 × 48 (her karede aynı)
AYRIM EKSENİ:   tek figür — soluk gri giysi ↔ koyu zemin/koyu kanat; teal göğüs bandı   ⛔ yalnız RENK yetmez — gece sahnesinde iki koyu gövde
                     ayrılmaz; siluet/malzeme/boy çapası yazılır
GİREN NESNE:    kesik kayış ucu (yeni)        ÇIKAN NESNE: kanat takımı (çukurda kalır → S30 batar)
TAŞINAN NESNE:  çekirdek (kucağa) → S30 · kesik kayış → S45
⛔ BİÇİM KİLİDİ: kask (düz pane + kalın koyu çerçeve) + çekirdek (S10 onaylı karesi) + kanat çubuğu (S15 referansı) — referans paketi YOK (sahip); ilk onaylı kareler referans [D153/D154]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      amber pus dolgusu, tepe, gölge sığ   (ışık takvimi: dış sabit pus dolgusu / iç 3200 K sabit · monotonik: değişmez; iç↔dış geçişleri OLAY)
PALET:     dış amber pus · çekirdek mat metal · kanat koyu füme sıvıda   ⛔ önceki sahneyle aynı olamaz [KURGU_RITMI §2 örüntü kırıcı] — ölçek değişti
SES:       kesici hırıltısı, kayış ayrılır, sıvı
MÜZİK:     yok — yalnız kesici, kayış, sıvı (bedel sessiz)
FİZİK:     —   (kart §3.9: sıcak yüzeyde puf 0,5 m / 2 s · rüzgâr yok · gölge sığ · güneş diski 0 · KART 1 sıvı temas)
```

## 🎙️ REPLİK (varsa)

```
REPLİK:    — (film sessiz tasarımlı)
İŞLEV:     —
AĞIZ:      — ağız kapalı, konuşma yok
```

## ⭐VİRAL — yalnız işaretli sahnede, İKİ satır ZORUNLU

```
YÜZ:       dudaklar aralanır, göz tokada; kesimde göz bir an kapanır, sonra çekirdeğe
HAREKET:   iki parmak durur, kesici hızlı — kayış ayrılır, kanat yüzeyin altında kalır, çekirdek göğse çekilir
⛔ Ölçütsüz ⭐VİRAL etiketi DÜŞER [SENARYO_VE_VIRAL_KAMERA §2.4]
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D179 · D202 ÇAPA COST | imaj = 0,0 s: kayış BAĞLI, el tokada iki parmak durmuş; video içinde kesim | BEFORE: 'her left glove rests on the buckle, two fingers straightened, not moving; shoulders high' → AFTER: 'both arms closed around the core against her chest; the cut strap-end hangs from the buckle; shoulders down and stay down' |
| KARAKTER_KARTI §2 KIRILMA | alışkanlık (toka iki kez) BAŞLAR ve tamamlanmaz | 'the two fingers lift toward the buckle to tap it and stop a finger's width short; they hold there for two seconds; then the sleeve cutter goes to the strap without the tap' |
| KARAKTER_KARTI §3 · D213 | reddedilen nesne kadrajda ve sonra da orada; temas ilk 2 s | kanat çubuğu ve membran yüzeyin altında, kadrajın sol üçte birinde, klip boyu; kesici 0,0 s'de kayışta |
| KART 12 · POLİTİKA §2 | alet adı: 'sleeve cutter' — blade/knife yok; bele kadar sıvı: yüz görünür, çevre çapası | 'a hooked cutter on her left wrist parts the strap'; 'beside her the far edge of the lakebed is visible' |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | U-3 seçim/bedel bedende | Y kurulumu CU 1,5 m; tereddüt 2 s; omuz+el çifti saniyeli | ✅ |
| 2 | ⛔ | U-5 politika (bele kadar sıvı) | yan/profil CU, vizör açık, uzak kıyı çapası | ✅ |
| 3 | ⚠️ | U-sarı-6 yüz CU | ≤3 öznitelik | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   EVET — PB adayı: kısıtlanmış gövde (bele kadar sıvı) + alet   sınıf: PB
NÖTR TARİF:  'she stands waist-deep in the dark still liquid, side-on, face fully readable through the clear pane; a hooked cutter on her left wrist parts the chest strap; the wing-frame lies under the surface beside her'   ⛔ nesne ADLANDIRILMAZ, FORMU tarif edilir [D67]
⛔ YASAK CÜMLE YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
  karşılığı POZİTİF kilittir: 'the hooked cutter on her wrist parts the strap; the core comes to her chest'
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
KART BAĞI:        ALIŞKANLIK KIRILMASI · SINIR (çekirdeği bırakmaz) · BEDEL
İZLEYİCİ CÜMLESİ: YÜZ: dudaklar aralanır, göz tokada, sonra kapanır bir an · HAREKET: iki parmak durur 2 s, kesici hızlı — bırakmak istemiyor, bırakıyor
TAŞIYAN KANAL:    TEREDDÜT + BIRAKMA   TASK ONLY: hayır
SON 3 s:          holds the core against her chest with both arms; the cut strap hangs from the buckle; the wing stays in the pool behind
① FİİL   süreç ✅ (keser, çeker, sarar)
② DİRENÇ ✅ (iki parmak durur)
③ TEK KİLİT ✅ · TIMELINE ≤3 satır
④ SINIR  ✅ (End/Start sınır satırı sahne haritasında)
⑤ SAAT   ✅ (inen damlalar (kenarda, sabit oran))
```
