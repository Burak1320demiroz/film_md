# 🔬 S41 — KİLİT SAHNE · DORUK · SAHNE ÇALIŞMASI · THE_FALLING_WORLD

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
SAHNE:      S41  (sahibin V42'si)      BAŞLIK: Aktarılan ağırlık
BÖLÜM:      THE_FALLING_WORLD_BOLUM_4.md      DRAMATİK SAHNE: D8 · Son bağlantı (S38-S44)
ZAMAN:      410 s → 420 s       ⛔ FORMÜLLE [D122]: sahne(n) = n × 10 s
VURUŞ:      ⑨ Final aksiyonu — DORUK · KAPAK KARESİ (7:00+4 s)
B5 SATIRI:  BEDEL④ — BEYAZ kendi tutunma ihtimalini bırakır; ağırlığını TURUNCU'nun eline verir
⭐VİRAL:    EVET → YÜZ ve HAREKET satırları aşağıda
```

## 🎬 OLAY — tek cümle, ne DEĞİŞİYOR

```
OLAY:            TURUNCU basamaklara dayanıp BEYAZ'ın sağ bileğini kavrar; BEYAZ elini aktarır.
BAŞTA:           TURUNCU kapı eşiğinde gövdesini basamaklara dayamış, kolu uzanıyor; BEYAZ sağ eldiveniyle eşikte asılı
SONDA:           TURUNCU'nun eldiveni BEYAZ'ın sağ bileğinde kapalı; BEYAZ'ın eldiveni eşikten AYRILMIŞ
⛔ KLİP İÇİ DEĞİŞİM: VAR — ölçülmüş EN ZAYIF eksendir (T2V-CompBench 0,0687).
   Seçim: ② ARA DURUM YASAĞI cümlesi prompta yazılır
   Gerekçe: aktarımın kendisi doruktur; sınıra taşınırsa seçim kadraj dışında kalır
   ARA DURUM YASAĞI: his right glove is either on the sill or in the other glove; there is no frame where it holds neither
```

## 🎥 KURULUM — harf ve OPTİK ARİTMETİĞİ

```
KURULUM HARFİ:  X        İŞARET: DÖNÜŞ S38 (3 sahne sonra)
⛔ Kamera metni S38'den BİREBİR kopyalanır ve işaret satırı taşınır:
"— the same position, height and lens as Scene 38."
LENS:           24 mm     MESAFE: 6,4 m     YÜKSEKLİK: 5 m out from the door sill and 4 m below it
ÖLÇEK:          wide shot        AÇI TİPİ: low angle
KADRAJ ENİ:     9,6 m      ⛔ HESAPLANDI (§5.2): kesir = boyut × odak ÷ (mesafe × sensör)
                          Kadraja alınacak nesne asılı gövde 1,9 m + kapı ağzı 1,6 m + iki sarı kol — 9,6 m üçünü birden alır
                          Sığıyor mu: ✅
ANA NESNE PİKSEL: insan 1,9 m → %35 kare yüksekliği = 380 px ✅ · 120 px KAPAK TESTİ: iki ayrı leke ✅   ⛔ ≥100 px [D179]
ÖNCEKİ SAHNEYLE: S40 (U · MS · eye level · kabin) → S41 (X · WS · low angle · kapı dışı) = 2 kademe + mekân değişir ✅ bant içi
```

## 👤 KADRAJDAKİLER — devamlılık taşıyıcıları

```
İNSAN SAYISI:   2 — BEYAZ sol ALT üçte bir (asılı) · TURUNCU sağ üçte bir (eşikte) · merkez çizgisi geçilmiyor, YAKLAŞAN şey KOLLAR
⛔ FİLM BOYU KİLİT: BEYAZ kadrajın SOL üçte birinde · TURUNCU SAĞ üçte birinde;
   merkez çizgisi hiçbir sahnede geçilmez [KART 4 · KRONOS'ta iki kopyalanma vakası]
AYRIM EKSENİ:   ÜÇ kanal birden — ① RENK (kirli beyaz + kobalt mavi omuz ↔ yanık
                turuncu + siyah üst kol) ② OMUZ GEOMETRİSİ (köşeli geniş sırt ünitesi
                ↔ dar dikdörtgen sırt ünitesi) ③ KONUM (sol ↔ sağ üçte bir).
                ⛔ Yalnız RENK yetmez — P5'te gemi gövdesi beyaz; BEYAZ'ın giysisi gemiye karışmasın diye ayrımı KOBALT MAVİ OMUZ ve kir merdiveni taşır
GİREN NESNE:    TURUNCU'nun gövdesinin basamaklara dayanması (yapı yerine KENDİSİ sabit nokta olur — alışkanlık kırılır)
ÇIKAN NESNE:    BEYAZ'ın eşikteki tutuşu — KALICI
TAŞINAN NESNE:  sarı halatın İKİ kolu (S36'dan) · gemi halkası (S31'den) · kesici hâlâ sol önkolda (S39'dan) → S42'ye
⛔ BİÇİM KİLİDİ: METİNLE TUTULMUYOR [D146] → referans sayfası ŞART: R1 BEYAZ (bantlı manşet durumu) · R2 TURUNCU · R3 HAT AİLESİ · R4 GEMİ (kapı eşiği + iç basamaklar)
```

## 💡 IŞIK · 🔊 SES · ⚛️ FİZİK

```
IŞIK:      aynı tek güneş sol üstten; gemi gövdesi üstten aydınlık, asılı gövde kısmen gemi gölgesinde — ARKADA merceklenmiş disk
           ışık takvimi: tek güneş film boyu SABİT saat yönünde (sol üst, kadraj
           dışı); ardışık sahne arası fark ≤30° ve ≤500 K · monotonik: ✅
PALET:     P5 gemi platformu
           ⛔ önceki sahneyle aynı değil: S40 P6 kabin içiydi (4500K panel); geçiş sert ve gerekçeli
SES:       Y5 — gemi hazırlık uğultusu + gergin metal + iki nefes (biri telsizden)
           ⛔ önceki sahneyle aynı doku değil: S40 Y6 idi (basınçlı iç, fan); dış/iç doku farkı açık
MÜZİK:     VAR — tek alt kat, doruğun 4. saniyesinde giriyor; vuruş yok
FİZİK:     §3.2 İNCE ATMOSFER + 0,30 g [D74 kaydı]. 0,30 g: asılı gövde sallanır ama periyot Dünya'nın ~1,8 katı — salınım YAVAŞ ve GENİŞ. Aktarım anında gövde 0,4 m aşağı düşer ve iki eldiven arasında durur.
```

## 🎙️ REPLİK

```
REPLİK:    — (sahnede replik yok; son replik S40'ta, sonrası SESSİZ)
İŞLEV:     — doruk sözsüzdür: seçim EL ile yapılır
AĞIZ:      okunmuyor
```

## ⭐VİRAL

```
YÜZ:       — ⛔ DÜRÜST KAYIT: yüz kanalı FİZİKEN kapalı (opak vizör).
           ⭐ etiketi yalnız HAREKET satırıyla taşınıyor; sapma 02 §2'de kayıtlı.
           TELAFİ: "ifade değişimi"nin taşıyıcısı BAŞ AÇISIDIR — BEYAZ'ın kaskı
           aktarımdan önce yukarı, aktarımdan sonra AŞAĞI döner (iki kare arası
           adlandırılabilir fark).
HAREKET:   kadrajda HIZLANAN şey BEYAZ'ın gövdesidir: eldiveni eşikten ayrıldığı
           anda gövde 0,4 m serbest düşer ve iki eldiven arasında DURUR. 10
           saniyenin en hızlı 0,5 saniyesi budur ve kapak karesi onun BEFORE'udur.
```

## 🔒 BU SAHNEYE DÜŞEN KİLİTLER — `01_QA_DERS_HASADI.md`'den

| kaynak (ders/QA/red) | kilit cümlesi | prompta nasıl girecek |
|---|---|---|
| D179 | İmaj = ÇAPA'nın BEFORE'u; düşüş anı karede YOKTUR | ⭐ KAPAK KARESİ: iki eldiven ZATEN kapalı, yük ZATEN aktarılmış. Serbest düşüş karesi ÜRETİLMEZ — video onu içerir, imaj içermez |
| D202 | Çapa üçlüsünün CHOICE ayağı — BEFORE/AFTER gövde çifti | BEFORE: BEYAZ'ın eldiveni eşikte (kendi yükü kendinde) · AFTER: eldiven boşta, yük TURUNCU'da. S00'ın TAM TERSİ |
| D62 | KESİLEMEZ LİSTESİ: S41 · S42 · S45 · S47 | bu klip kurguda kırpılmaz; 10 saniyenin 10'u kullanılır |

## ⚠️ BU SAHNEYE DÜŞEN UYARILAR — `04_UYARI_NOTLARI.md`'den

| # | seviye | uyarı | ne yapıldı | durum |
|:--:|:--:|---|---|:--:|
| 1 | ⛔ | İPTAL KAPISI: asılı gövde + bilek kavrama TEK KAREDE okunmuyorsa film ÜRETİLMEZ | X kurulumu 380 px gövde + 9,6 m kadraj; iki leke 120 px'te ayrı okunuyor | ✅ |
| 2 | ⛔ | KART 4 — iki figür kopyalanması; bu karede gövdeler en yakın | konum kilidi + `Exactly two human characters, no duplicates, no third person.` + P4 probu | ✅ |
| 3 | ⛔ | Politika imzası ⑥ — yüzsüz gövde boşlukta asılı | ÇEVRESEL ÇAPA: gemi gövdesi, kapı ağzı ve basamaklar aynı karede; kare hiçbir anda "boşlukta yüzsüz gövde" değil | ✅ |
| 4 | ⚠️ | D169 — 0,30 g'de efor okunmazsa bedel okunmaz | EFOR satırı: TURUNCU'nun gövdesi basamaklara karşı geriliyor, dördüncü çekiş ilkinden yavaş; BEYAZ'ın sağ omzu yükü alırken 8 cm aşağı iniyor | ✅ |

## 🛡️ POLİTİKA

```
RİSKLİ Mİ:   ⚠️ EVET — orta
SINIF:       YR (yüzsüz izolasyon) — kısıtlanmış uzuv YOK, gövde SERBEST asılı
NÖTR TARİF:  temas ELDİVEN ↔ SERT MANŞET; sıfır ten. "tehlikeli durum" çerçevesi
             kurulmaz — kadrajın konusu KAVRAMA'dır, düşme değil.
⛔ YASAK CÜMLE YAZILMAZ. POZİTİF KARŞILIĞI:
  the orange glove closes around the hard cuff of his right wrist and holds it
  while his own glove leaves the sill; the two gloves stay locked for the rest
  of the clip.
⭐ KAPAK NOTU: KAPAK A bu karedir (sahibin seçimi). KAPAK B = S00 (bilek tutuşu).
  TEK DEĞİŞKEN KİLİDİ: ilk 48 saatte kapak VEYA başlık değişir, ikisi birden değil.
```

---

## ✅ KAPI — bu sahnenin promptu yazılabilir mi

```
✅ OLAY tek cümleyle yazıldı, BAŞTA/SONDA ayrı
✅ optik aritmetiği yapıldı — nesne kadraja SIĞIYOR ve insan 1,9 m → %35 kare yüksekliği = 380 px ✅ · 120 px KAPAK TESTİ: iki ayrı leke ✅
✅ önceki sahneyle ardışık çift bant içi
✅ kurulum harfi + işaret satırı yazıldı
✅ ⛔ uyarıların hepsi kapandı
✅ politika satırı yazıldı
✅ ⭐VİRAL: HAREKET satırı yazıldı · YÜZ satırı yerine BAŞ AÇISI telafisi yazıldı ve sapma kayıtlı
→ hepsi ✅ — THE_FALLING_WORLD_BOLUM_4.md'ye bu sahnenin 📸 + 🎥 promptu YAZILABİLİR
```
