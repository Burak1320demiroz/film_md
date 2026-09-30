# 🔬 K24 — KİLİT KLİP · FINAL · ÇALIŞMA · THE_SIGNAL_KEEPERS

> ⛔ Başlık biçimi `## 🔬 K<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
KLİP:       K24   ·   SAHNE: S06 (4/4)   ·   ROL: FINAL · kapsama şablonunda DÖNÜŞ
BAŞLIK:     YUVA — berrak ton
BÖLÜM:      THE_SIGNAL_KEEPERS_BOLUM_2.md
ZAMAN:      230,0 s → 240,0 s     ⛔ FORMÜLLE [D122]: (n−1) × 10,0 s
VURUŞ:      kapanış imajı   ·   %100        B5 SATIRI: BEDEL (ikinci, küçük bedelin sonucu)
⭐VİRAL:    hayır — yüz kadrajda yok (yalnız eller), ① kanalı fiziksel olarak kapalı
KAFİYE:     ⭐ K10'un kadrajı (kurulum G) — kamera metni BİREBİR aynı
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Sondanın boş cam yuvasında artık kadının mavi küresi durur; bir
                 parmak ucu ona bir kez vurur ve ton BERRAKTIR.
BAŞTA:           küre yuvaya oturmuş, parmak ucu ona bir parmak boyu uzakta
SONDA:           ton çalmış, siyah taşın üstünde mavi bir leke kalmış, eller boş ve
                 açık kadrajdan çıkıyor
SON 3 s:         kadraj boş değil ama el yok: yalnız küre, yuva ve taştaki mavi leke;
                 ton sönerken oda tonu SÜRÜYOR
⛔ KLİP İÇİ DEĞİŞİM: VAR (donuk kadraj → berrak ton + leke). Seçim: ② ARA DURUM
   YASAĞI + START/ACTION/END. Gerekçe: kapanış imajı değişimi TAŞIMAK zorunda —
   filmin tek değişkeni bu karede kapanıyor.
   START STATE: `the blue glass sphere is seated in the probe's round glass seat,
     one gloved fingertip a finger's width from it`
   ACTION: `the fingertip taps the sphere once`
   END STATE: `the tone is clear, a blue stain of light lies on the black stone,
     the hands leave the frame open and empty`
   ARA DURUM YASAĞI: `the sphere does not crack, melt or change shape; the only
     change is the light on the stone`
KİLİT FİİLİ:     BAŞARIM — `taps once` + ETKİNLİK `lies` (leke sürüyor)
DİRENÇ (evre ②): küre yuvada bir parmak fazla oturuyor; parmak ucu ilk değdiğinde
                 küre yarım milimetre dönüyor, ton ondan SONRA geliyor (eşitsiz ivme)
ÇEVRE SAATİ:     taştaki mavi lekenin kenarı — ton sönerken kendi genişliğinin
                 üçte biri kadar daralıyor (tek · kenarda · oranlı)
CONTINUOUS ACTION (K23'ten): `the sphere has just lifted free of the shoulder seat` —
                 K23'ün `OLAY BAŞ → SON` hücresinin SON yarısı birebir [D207]
İLK ↔ SON:       K01'de eller gövdeye yakın, biri kürenin üstünde (DİNLEYEN) →
                 K24'te eller boş ve açık, küre artık onda değil (CEVAP VEREN)
                 [KARAKTER_KARTI §1 İLK↔SON satırı]
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  G        İŞARET: K10'un kadrajına dönüş — ara 14, yani kapının
                         tanımına göre DÖNÜŞ DEĞİL YENİDEN TANITIM (§3), ve bu
                         BİLİNÇLİ döngü kapanışıdır: aynı kadraj, başka bir dünya.
                         Kamera metni yine BİREBİR kopyalanır +
                         `— the same position, height and lens as Clip 10.`
LENS:           85 mm     MESAFE: 0,48 m     YÜKSEKLİK: 1,10 m
ÖLÇEK:          ECU       AÇI TİPİ: üst açı 25°   AZİMUT: 110°
KADRAJ ENİ:     0,20 m    (H = 0,11 m)   kadraja alınacak: cam yuva 0,12 m
                          Sığıyor mu: yuva kadraj yüksekliğini dolduruyor — BİLİNÇLİ
ANA NESNE PİKSEL: küre 0,09 m → 1700 px ✅ · parmak ucu 0,03 m → 544 px ✅ ·
                  taştaki leke ~0,06 m → 1133 px ✅   ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  K23 → K24 · ölçek kademesi 1 (CU → ECU) · azimut 90° → bant içi ✅
KAFİYE KONTROLÜ: K10 ile aynı harf → aynı ölçülen imza (⑥ birebir yazım kapısı):
                 85 mm · 0,48 m · 1,10 m · ECU · üst açı 25° · azimut 110° ✅
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   1   ⛔ `Exactly one human character, no duplicates, no second person.`
                    (kadrajda yalnız eller var ama gövde SAYILIR — insan 1)
AYRIM EKSENİ:   eldiven mat açık DEĞER · yuva koyu metal · küre tek RENK aksanı
GİREN NESNE:    mavi küre (K23'ten taşındı) · taştaki mavi leke
ÇIKAN NESNE:    eller (kadrajı boş ve açık terk ediyor)
TAŞINAN NESNE:  küre → önceki K23 (omuz yuvasından kalktı) · sonraki — (film bitiyor)
⛔ BİÇİM KİLİDİ: VAR — eldivenin biçimi 24/24 aynı cümle; küre K01'den beri aynı
                nesne (0,09 m · koyu mavi cam · metal yuvaya OTURUR, kordonla
                asılmaz) [D146 · D172+T1]
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      uyanan halkaların sıcak beyazı kadrajın dışından geliyor + kürenin KENDİ
           mavisi; ışık kürenin kenarını GEÇMİYOR (0% bloom, halo yok) — taştaki
           leke bir YANSIMA, bir hale değil
           takvim: S6'nın ikinci kademesi (ışık artmış ve kalmış) · monotonik: evet
PALET:     siyah taş / berrak mavi   ⛔ K21-K22'nin sıcak beyazından ayrı aksan
SES:       tek BERRAK ton + çok alçak oda tonu — filmin ikinci ve son tiz olayı
MÜZİK:     VAR ama son 2 saniyede çekiliyor; film oda tonuyla kapanıyor
FİZİK:     0,42 g · 3,1 bar · 240 K · kalın soğuk hava tizleri yutuyor → berrak ton
           bile YAKIN ve kısa duyuluyor
           ortam kartından bu klibe düşen: toz kalkmıyor (el yavaş çekiliyor);
           asılı toz perdesi YOK
```

## 🎙️ REPLİK

```
REPLİK:    — (insan sesi K20'de sonsuza dek kesildi; filmin son sesi bir CAM TONU)
İŞLEV:     —
AĞIZ:      okunmuyor — kadrajda ağız YOK
```

## ⭐VİRAL — iki satır ZORUNLU (işaretliyse)

```
YÜZ:       — (kadrajda yüz yok)
HAREKET:   — (ölçüldü: parmak ucu ve lekenin daralması var ama ① yüz kanalı
           kapalı → ⭐VİRAL değil; kapanış imajının işi viral değil DOYUM)
```

## 🎭 OYUNCULUK — izleyici cümlesi ve niyet kanalı

```
İZLEYİCİ CÜMLESİ: "Karşılığını görmeyeceği bir şeyi gönderdi ve bunu tamamlamak
                  istiyor."
TAŞIYAN KANAL:    parmak ucunun tek vuruşu + ellerin açık çekilmesi   (≤2)
TASK ONLY MU:     HAYIR — davranış harfi R (TEPKİ; ilk harf S'den FARKLI ✅);
                  tempo Y (yavaş)
TEMA:             UMUT — *"Karşılık beklemeden gönderilen şey, karşılığını sen
                  görmesen de bulur."* Bu kare temanın TEK KARE kanıtıdır:
                  gönderen kadrajdan çıkıyor, gönderilen kalıyor
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D210 · ⑩④ | kafiye çifti: CAMERA satırı K10'un BİREBİR kopyası | `— the same position, height and lens as Clip 10.` + aynı lens/mesafe/yükseklik |
| D172 + T1 | el ↔ küçük cam nesne kaynaşması | küre 1700 px (kadrajda çok büyük) · kordon/kayış 0 kare · kavrayıp çevirme YOK, yalnız TEK VURUŞ |
| ALIŞKANLIK (kart §4) | dokunmadan önce bir kez vurmak — filmin tanıma dili | üçüncü ve son kez: K05 yaprak → K11 kendi küresi → K24 yuvadaki küre |
| red #13 (PB) | yüzsüz izolasyon + tepeden makro + iki ön kol → SAHNE İPTAL | eksen 25° (tepeden değil) · tek el kadrajda · nesne özne, beden değil |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | ⛔3 / red #13 — iki yüzsüz yakın kadraj üst üste (K23 + K24) | K23 CU + gövde kadrajda · K24 ECU + nesne özne; ⛔ ikisi aynı gün üretilmez (üretim sırası ⑥) | ✅ |
| 2 | ⛔ | ⛔7 — `0% bloom / no glow` × ışık yayan küre | negatif satırı KALIYOR; taştaki leke YANSIMA olarak yazılıyor | ✅ |
| 3 | ⚠️ | ⚠️12 — klip içi durum değişimi | START/ACTION/END + ara durum yasağı yazıldı | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   EVET   sınıf: PB — yüzsüz yakın kadraj (red defteri #13'ün bir bileşeni)
NÖTR TARİF:  `an extreme close view of a round glass seat in the flank of a small
             probe, a dark blue glass sphere resting in it; one gloved fingertip
             enters from the right, taps the sphere once and withdraws` — tepeden
             makro YOK (eksen 25°), iki ön kol YOK, `faceless` kelimesi hiç
             yazılmıyor
NÖTR TARİF ②: nesne ADLANDIRILMAZ, FORMU tarif edilir: `a sphere of dark blue glass,
             a hand's-breadth across` [D67]
⛔ YASAK CÜMLE YAZILMAZ (D123) — "kimse görmeyecek" gibi ANLATI cümlesi prompta
  girmez; karşılığı POZİTİF kapanış satırıdır: `the hands leave the frame open and
  empty and the blue light stays on the stone`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
□ OLAY tek cümleyle yazıldı, BAŞTA/SONDA/SON 3 s ayrı         ✅
□ optik aritmetiği yapıldı — küre 1700 px · leke 1133 px      ✅
□ önceki kliple ardışık çift bant içi (1 kademe · 90°)        ✅
□ kurulum harfi + kafiye işareti yazıldı (K10)                ✅
□ ⛔ uyarıların hepsi kapandı                                  ✅
□ politika satırı yazıldı (iki nötr tarif)                     ✅
□ ⭐VİRAL ise YÜZ + HAREKET satırları var                      ✅ (değil, ölçüldü)
□ kilit fiili SÜREÇ/BAŞARIM · direnç var · son satır SÜRDÜRME ✅
□ İLK↔SON satırı kapandı (dinleyen eller → boş açık eller)     ✅
→ hepsi ✅ → THE_SIGNAL_KEEPERS_BOLUM_2.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
