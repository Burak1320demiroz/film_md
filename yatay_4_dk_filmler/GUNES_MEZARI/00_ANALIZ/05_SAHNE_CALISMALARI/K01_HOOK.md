# 🔬 K01 — KİLİT KLİP · HOOK · ÇALIŞMA · GUNES_MEZARI

> ⛔ Başlık biçimi `## 🔬 K<nn> — ...`'dir. `## ... SAHNE <n>` YAZILMAZ:
> `prompt_kontrol.py`'nin SAHNE_BASLIK deseni odur.
> ⛔ Bu dosyada PROMPT YOKTUR. Prompt bölüm dosyasına yazılır.

---

## 🪪 KİMLİK

```
KLİP:       K01   ·   SAHNE: S01   ·   ROL: HOOK
BAŞLIK:     KAFES — kısık bir güneş
BÖLÜM:      GUNES_MEZARI_BOLUM_1.md
ZAMAN:      0,0 s → 10,0 s     ⛔ FORMÜLLE [D122]: (n−1) × 10,0 s
VURUŞ:      açılış imajı + soru        B5 SATIRI: —
⭐VİRAL:    hayır — kadrajda insan YOK, ① kanalı fiziksel olarak kapalı
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            Kısık bir küre kendi ekseninde yavaş döner ve onu tutan metal bir kez daha inler.
BAŞTA:           küre dönüyor, halkaların iç kenarı kadrajın alt köşesinde
SONDA:           aynı hızda dönmeye devam ediyor, inleme bir kez daha yükseliyor
SON 3 s:         küre aynı hızda dönüyor, metal bir kez daha inliyor
⛔ KLİP İÇİ DEĞİŞİM: YOK — küre durum değiştirmez, yalnız döner (ölçülmüş en zayıf eksene hiç girilmiyor)
KİLİT FİİLİ:     ETKİNLİK — `turns` (bitişsiz süreç, sınıra kadar sürer)
DİRENÇ (evre ②): kürenin kendi ağırlığı halkaları geriyor: metalin inlemesi 4. ve 8. saniyede bir kez daha yükselir
ÇEVRE SAATİ:     kürenin yüzeyindeki daha parlak hücreler — bir hücre kendi genişliğini ~4 saniyede geçer   (tek · kenarda · oranlı)
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  C        İŞARET: ilk kullanım — ⭐ K24 bu metni BİREBİR tekrar eder (kafiye çifti)
LENS:           35 mm     MESAFE: 2,2 m     YÜKSEKLİK: 1,60 m
ÖLÇEK:          MS        AÇI TİPİ: üst açı 15°
KADRAJ ENİ:     2,26 m      kadraja alınacak nesne: kürenin yüzeyi (9,0 m) — kadrajdan taşar
                          Sığıyor mu: taşar ve bu BİLİNÇLİ: kadrajdan büyük olan şey büyük okunur
ANA NESNE PİKSEL: kadrajın tamamı küre yüzeyi · daha parlak hücreler ~0,9 m → 1530 px      ⛔ ≥100 px [D179]
ÖNCEKİ KLİPLE:  — (filmin ilk klibi)
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   0 — ⛔ KART 10: `Exactly 0 human` YAZILMAZ; boşluk POZİTİF tarif edilir
AYRIM EKSENİ:   — (insan yok)
GİREN NESNE:    küre ve üç halkanın iç kenarı
ÇIKAN NESNE:    —
TAŞINAN NESNE:  küre → K02'de tam görünür  → önceki — · sonraki K02
⛔ BİÇİM KİLİDİ: ⚠️ VAR — kürenin biçimi filmin 1 numaralı riski; pozitif biçim SAYIYLA yazıldı (kenar keskin · korona 0 kare · hücre 4 s'de bir genişlik)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      yalnız kürenin kendi ışığı; aradaki hava pus ve hale taşımaz
           takvim: S1 tek değer (kısık küre) — film boyu ilk kademe · monotonik: evet (artış yalnız S7'de ve OLAY olarak ilan edilmiş)
PALET:     koyu kızıl-altın / siyah
SES:       gerilen metalin alçak inlemesi — tek diegetik ses
MÜZİK:     YOK (ilk müzik 0:20 bandında)
FİZİK:     0,38 g · mühürlü soğuk gövde · küre BESLENEN bir kafeste TUTULUR ve sıkıştırılır
           ortam kartından bu klibe düşen: kafes kuralı ① — küre kendini tutmaz
```

## 🎙️ REPLİK

```
REPLİK:    —
İŞLEV:     —
AĞIZ:      —
```

## ⭐VİRAL — iki satır ZORUNLU (işaretliyse)

```
YÜZ:       —
HAREKET:   —
```

## 🎭 OYUNCULUK — izleyici cümlesi ve niyet kanalı

```
İZLEYİCİ CÜMLESİ: "(insansız klip — izleyici cümlesi kadrajdaki NESNE için yazılır) Bu şeyi bir yere götürüyorlar."
TAŞIYAN KANAL:    — (insan yok; taşıyıcı kanal NESNE hareketi)   (≤2 · OYUNCULUK_YAZIM §3)
TASK ONLY MU:     EVET — bilinçli: bu klip bir SORU klibidir, DAVRANIŞ ŞERİDİ'nde "—"
```

## 🔒 BU KLİBE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D192 · A5 | küre pozitif biçimi SAYIYLA: kenar keskin · çap halkaların iç açıklığının 4/5'i · hücre 4 s'de bir genişlik · korona 0 kare | üçüncü satır = klibin TEK kilidi, sayıyla |
| D59 | `hang/float/hover/suspend/still/frozen/stopped` yalnız negatif blokta; küre pozitif gövdede TUTULUR | `three machined rings close around it and it turns with the ship as one body` |
| red #2 (YR) | insansız klipte NEGATIVE kısaltılır, insan sayısı cümlesi yazılmaz | NEGATIVE = metin yasağı + fotogerçekçilik/grain + 1 sahneye özel; boşluk pozitif: `the flight deck above it is dark and unmanned` |
| D210 | kafiye çifti: K24'ün CAMERA satırı bu klibin CAMERA satırının BİREBİR kopyası | K24'e `— the same position, height and lens as Clip 1.` |

## ⚠️ BU KLİBE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | #1 yapısal red profili (insansız + uzun negatif) | NEGATIVE tek pozitif satıra indi; `Exactly 0 human` yok | ✅ |
| 2 | ⛔ | #4 1 numaralı risk yalnız sıfatla korunursa ateş topu gelir | dört sayı yazıldı; SPEC göz kapısı aynı dördünü sorar | ✅ |
| 3 | ⛔ | #3 yasak kökler pozitif gövdede yenilir | yedi kök yalnız negatifte; grep adım 10'da | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   EVET   sınıf: PK — `explosion/fireball/flash` kelimeleri NEGATİF BLOKTA BİLE yazılmaz
NÖTR TARİF:  nesne adlandırılmaz, BİÇİM tarif edilir: `a smooth sphere of dark red-gold light, its edge sharp against the black`
POZİTİF KİLİT (yasak cümle yerine): `the sphere is held at the focus of three machined rings and turns with them as one body`
```

---

## ✅ KAPI — bu klibin promptu yazılabilir mi

```
□ OLAY tek cümleyle yazıldı, BAŞTA/SONDA/SON 3 s ayrı         ✅
□ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve ≥100 px ✅
□ önceki kliple ardışık çift bant içi (ya da şok gerekçeli)     ✅
□ kurulum harfi + işaret satırı yazıldı                       ✅
□ ⛔ uyarıların hepsi kapandı                                  ✅
□ politika satırı yazıldı                                     ✅
□ ⭐VİRAL ise YÜZ + HAREKET satırları var                      ✅
□ kilit fiili SÜREÇ · direnç var · son satır SÜRDÜRME         ✅
→ hepsi ✅ → GUNES_MEZARI_BOLUM_1.md'ye bu klibin 📸 + 🎥 promptu yazılabilir
```
