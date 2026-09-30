# ✅ THE_LAST_TOW — ÜRETİM ÖNCESİ KONTROL

> Kaynak: `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` — A0-A5 · B1-B6 · C · D · E
> = **18 madde.** Her madde DOSYA + SATIR ya da ÖLÇÜM ile cevaplanır; "evet" tek
> başına cevap değildir.
>
> Koşu: 28.09.2026 · yazım bitti, üretim 0 kare.

---

## 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### A0 — HİKÂYE ONAYI VAR MI ✅

```
00_ANALIZ/00_HIKAYE_ONAYI.md · ONAY: 28.09.2026 · sahip · TUR 1/3
12 sahne satırı · (n klip) toplamı 48 · jargon 0  → ㉙ temiz
⚠️ SAPMA 1 satır (S6 mekanizması) — ayrıca onaylandı: "ONAY — levha"
```
⭐ Sapmanın sebebi kayda geçti: onaylı satır (*"kabini yarım derece döndürür"*)
**filmin kendi kuralıyla çelişiyordu** — kabin resife kaynamış, döndürülemez.
Düzeltme hikâyeyi değil MEKANİZMAYI değiştirdi; bedel, istek ve öteki 11 satır aynı.

### A1 — Yasak ↔ anlatım çelişkisi ✅ (EN PAHALI HATA — bu filmde İKİ KEZ arandı)

| yasak | filmin anlatmak istediği | çelişti mi | çözüm |
|---|---|---|---|
| çekirdek ③ `0% bloom, no glow` | yalayan ışıkta parlayan dikey metal yüzeyler | **HAYIR** — parlaklık bir HALO değil, bir YÜZEY değeri: ışık yüzeye vuruyor, etrafına taşmıyor | pozitif cümle: `grazing light strikes every upright metal face and leaves the ground dark` |
| çekirdek ⑧ `never hovering` | dik duran anahtar, ayakta duran levha, asılı kalan kesici kafası | **HAYIR** — hiçbiri havada durmuyor, hepsi bir yüzeye DEĞİYOR ve orada kalıyor | her birinde temas noktası yazılı (`its handle clear of the surface` · `the bare foot of the plate` · `the shank rests between them`) |
| çekirdek ⑤ `real skin pores and sweat` | 43 klipte yüz kadrajda YOK | **EVET — ve bu filmde önceden kesildi** | yüzsüz 43 klipte ⑤ KISALTILDI: `Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture.` (GUNES_MEZARI'nde bu hata üretimden önce yakalanmıştı; burada hiç doğmadı) |
| kaynak kuralı | "değen şey birleşir" | ⛔ **YASAK CÜMLESİ HİÇ YAZILMADI** [D59 · D123] | ölçüm: `grep -ci "does not weld\|never welds\|no cold weld"` → **0/96**. Karşılığı pozitif: 17 klipte `bare metal that touches bare metal stays joined, and the ceramic-coated boots, gloves and outer fabric do not join` |

### A2 — Sahne sayısı tutuyor mu ✅

```
SAHNE PLANI: 4 3 5 4 4 4 4 5 3 4 5 3   → toplam 48 klip / 12 sahne
bölüm dosyalarında `## 🎬 KLİP` başlığı: 48      (ölçüm: grep -c)
hikâye onayında sahne satırı: 12 · (n klip) toplamı: 48
sahne tablosunda satır: 48 · kilit klip dosyası: 5 (K01·K03·K40·K43·K48)
⛔ SCENE COUNT (12) ≠ CLIP COUNT (48) — bu rejimde TASARIM, uyuşmazlık değil
```

### A3 — Süre tutuyor mu ✅ (varsayımla)

```
48 × 10,0 s = 480 s = 8:00   ·   B1 = 240 s · B2 = 240 s
⬜ AÇIK: klip süresi ARAÇTAN ÖLÇÜLECEK [D124]. 10,0 s bir VARSAYIMDIR ve
   PLAN'ın ilk bloğunda öyle yazılı. Ölçüm 10,0 s değilse ızgara, vuruş
   yüzdeleri ve ışık kenarı sayacı (2,0 cm/s × süre) yeniden hesaplanır.
⭐ Işık kenarı sayacı süreye BAĞLI: film gerçek zamanlıdır (480 s hikâye = 480 s
   ekran). Klip süresi değişirse kenarın mesafeleri de değişir — bu bağ SPEC C'de yazılı.
```

### A4 — Yasaklı sahne tipi var mı ✅ (biri VAR ve tasarımla çözüldü)

| yasaklı tip | filmde var mı | çözüm |
|---|---|---|
| bedenden bir şeyin ÇIKARILMASI (red #3 PB — sözlükle çözülmeyen tek sınıf) | ⚠️ **yakındı**: kabinden bir insan biçiminin çıkarılması | tasarımda kesildi: çıkarılan şey bir GİYSİDİR (nesne). `body`·`dead`·`corpse`·`remains` **0/96** (ölçüm). Eylem "çıkarma" değil: giysi DEVRİLİR, o TUTAR, sonra kızağa BIRAKIR |
| insansız kadraj + uzun negatif (red #2 YR) | ✅ K01 · K02 | o iki klipte negatif kısa (6 cümle) ve insan SAYIMI kurulmuyor: `No people, no figures, no silhouettes of people.` |
| tepeden makro + yüzsüz uzuv izolasyonu (red #13 PB — SAHNE İPTAL) | ⚠️ K43 aynı aileye yakın | kadraj değişti: 85 mm · 1,1 m · göz hizası · ufuk kadrajda; eller üst üste değil |
| yedi kimlik özniteliği (red #15 PK) | ❌ | kimlik 4 öznitelik; boy/ten/saç/yaş **0/96** |
| yüzü kapatan ekipman (POLİTİKA §3 imza ⑥) | ❌ kadın için | vizör optik berrak, yüz camdan okunur. ⚠️ İkinci giysinin paneli KOYU — ama o bir nesnedir ve yüzü yoktur |
| zombi · savaş · silah · kan | ❌ | film sözlüğünde hiç yok |

### A5 — FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI ✅

```
1 NUMARALI RİSK:  İŞLENMİŞ METAL YÜZEYE BASILAN METİN / NUMARA (KART 5 · D138)
                  — kart §3.8'in kendi uyarısı: "modelin numara basmaya en yatkın
                  olduğu yer işlenmiş metaldir"
POZİTİF BİÇİMİ:   ÜÇ SAYI taşıyor — 8 mm genişliğinde düz kaynak dikişleri ·
                  40 mm aralıklı perçin sıraları · 1-20 cm çapında göktaşı çukurları
KAPSAMA (ölçüm):  36/48 klipte pozitif cümle · 96/96 promptta çekirdek ④ metin yasağı
⛔ Sıfat yetmedi kontrolü: "temiz, işaretsiz metal" gibi bir SIFAT cümlesi
  hiçbir promptta tek başına kullanılmadı.
```

---

## 🔴 B. FİLMİN DORUĞU YAZILMIŞ MI

### B1 — Doruk anı bir sahnenin İÇİNDE mi ✅

```
DORUK ①  S10 · K37-K40 (360-400 s) — botlar kopuyor, giysi devriliyor, kadın tutuyor
DORUK ②  S11 · K43 (420-430 s) — merkezî seçim ve BEDEL
İkisi de bir sahnenin İÇİNDE ve ikisi de tek klipte bitmiyor: S10 dört klip,
S11 beş klip. Doruk bir KESME değil, bir SÜREÇ.
```

### B1b — Katmanlı dünya ise ışık takvimi var mı ✅ (bu filmin omurgası)

```
KART 6b tetiklendi: film İKİ BÖLGELİ — gölge (kaynaklar tutuyor) ve ışık
(kaynaklar kopuyor). Sınır KADRAJDA GÖRÜNÜR.
IŞIK TAKVİMİ (PLAN · Lighting Bible · 12 satır):
  yıldız yüksekliği 2,3° SABİT (yükselme 0,17°/saat → 8 dakikada 0,023°, ölçülemez)
  hareket eden: 40 m'lik sırtın GÖLGE KENARI · 2,0 cm/s · TEK YÖN
  kenarın dikişe mesafesi: 4,80 → 4,00 → 3,40 → 2,40 → 1,60 → 0,80 → 0,00 m
MONOTONİK ✅ — geri dönüş yok, duraksama yok, hızlanma yok [D193 · D201]
PALET de monotonik: GÖLGE (S01-S02) → KENAR (S03-S06) → IŞIK (S07-S12)
```

### B2 — Bedelli seçim var mı ✅

```
SEÇİM:  K43 — kesici kafasını kapanan açıklığa sokuyor
BEDEL:  aynı alet. K44'te kaynıyor, K45'te eli BOŞ geri dönüyor,
        K44-K48'de kemerdeki yuva BOŞ ve siluette görünüyor [D206]
⛔ "anlamak / fark etmek" bedel değildir kontrolü: bu filmin bedeli bir NESNE
  ve nesnenin yokluğu beş klipte kadrajda.
İKİNCİ KADEME: kızak çapası · K22-K23 (kalıcı)
ÜÇÜNCÜ KADEME: giysinin teslimi · K46 (seçilerek ödenir — son çekici)
```

### B3 — Tema hangi sahnede EKRANA çıkıyor ✅

```
TEMA: YALNIZLIK · tanım "Yıllardır her şeyi birbirinden ayrı tutan kadın, sonunda
      bir şeyi bir daha ayrılmayacak biçimde kendine bağlar."
MOTİF SAHNELERİ: S01 · S04 · S06 · S09 · S11 · S12   (6 ≥ 3 alt sınır)
EKRANDA NE GÖRÜLÜYOR:
  S01  eldiven yüzeylere yalnız SIRTIYLA değiyor (sakınma, 11 klipte)
  S04  kesiğin arkasından kapanması — ayırmanın imkânsızlığı
  S06  ilk kalıcı yapıştırma (çapa + levhanın ayağı)
  S09  ayıracak aletin tamamen bitmesi
  S11  avucun bilerek bastırması — İLK↔SON dönüşü
  S12  resifte ilk kez KASITLI bırakılan iz
⛔ Tema cümlesi TAKAS kalıbı değil (§3c moratoryumu): feda değil, dönüş tarifi.
```

### B4 — Açı yayı yazıldı mı ✅

```
KURULUM:      11 (ACI_YAYI §4 bandı 48 klipte 8-14 → bant içi)
ARDIŞIK ÇİFT: 47/47 bant içi (≥1 ölçek kademesi VE ≥45° azimut) — tablo
              03_SAHNE_SIRALAMASI §3'te klip klip yazılı
⚡ŞOK:        1 (K01→K02 · Δ2) — tavan 1-2 · gerekçe: filmin tek tanıtım kesmesi
AÇI TİPİ:     3 ≥3 (eye-level B·C·D·E·H·K · low-angle A·F·J · high-angle G·I)
DÖNÜŞ:        21/48 = %43,8 ≥ %40 · işaret satırı 37 klipte (74 promptta)
KÜME:         bu rejimde ARANMAZ (zincir kalktı, SAHNE PLANI beyan edildi)
BÖLÜM SINIRI: K24 (I · MS 3) ↔ K25 (D · CU 4) — Δ1 · 150° ✅ bant içi
⭐ OPTİK ARİTMETİĞİ 48/48 yapıldı ve BİR KARE KURTARDI: K01 ilk planda D
  (85 mm / 1,1 m → kadraj 0,47 m) idi ve 56 cm'lik anahtar SIĞMIYORDU.
  Kurulum C'ye (50 mm / 2,4 m → 1,73 m) taşındı. Kaydı: K01_HOOK.md
```

### B5 — İSTEK · ENGEL · BEDEL · MUHATAP ✅

```
İSTEK:   kapağı açmak ve içindekini son çekiciye teslim etmek (film başlamadan
         var olan bir İŞ — teslim emri yıllardır duruyor)
         ⛔ "anlamak/görmek/fark etmek" DEĞİL: fiiller AÇMAK ve TESLİM ETMEK
ENGEL:   ortam — kesilerek açılamaz (kesik arkasından kaynıyor); ayıran tek güç
         ısı farkı ve onu 44 günde bir gölge kenarı getiriyor
BEDEL:   kesici kafası · S11 (K43)   ⭐ sahne numarası VAR
MUHATAP: ortamın KALICI değişen parçası — RESİF. Cevap verme biçimi: her temasın
         izini TUTMASI. K48'deki iz ilk kez kasıtlı olan iz.
```

### B5b — AYRILIK (yalnız iki insanlı planlarda) — UYGULANMAZ

```
Tek yaşayan insan. Kadrajdaki ikinci basınç giysisi bir NESNEdir:
`Exactly one human character, no duplicates, no second person.` cümlesi 46/48
klipte yazılı ve DOĞRU (K01-K02'de insan yok, o iki klipte sayım kurulmuyor).
⛔ Bu satır "atlandı" değil "tetiklenmedi" — gerekçesi burada.
```

### B5c — ÜRETİM SIRASI ✅

```
① K43 (merkezî seçim + BEDEL)  ② K39 + K40 (doruk)  ③ K48 (kapanış)
④ K02 (kafiye çiftinin ilk yarısı)  ⑤ K01 (hook)  ⑥ kalan 43 klip, sahne sahne
⛔ İLK KABUL SATIRI K43 DEĞİLSE İKİNCİ KLİP ÜRETİLMEZ (üretim defteri §2)
⛔ K31 ile K43 aynı gün üretilmez (red #13 örüntüsü)
⛔ Referans paketi YAZILMADIĞI için ① bir KAPI değil; onun yerine iki
  iptal kapısı ve bir üretim-durur kuralı var (aşağıda E).
```

### B6 — POLİTİKA SATIRI ve ANLAM MALİYETİ ✅

```
EN RED-RİSKLİ KARE: K40
NÖTR TARİF: "A sealed second pressure suit, upright on the deck, tips forward as
            the two boot soles release from the plate; her gloved forearms take
            the weight level with her chest."
İKİNCİ RİSKLİ KARE: K43 (kadraj dersi uygulandı)
ANLAM MALİYETİ TABLOSU: PLAN §POLİTİKA SATIRI — 6 satır, üçü de dolu
  (ÖNLEM · MALİYET · TELAFİ). En ağır maliyet: "seyirci 'bu bir insan mı'
  sorusunu kendi cevaplıyor, film açık söylemiyor" — telafisi geometri.
```

---

## 🟠 C. SAYISAL KİLİTLER YAZILDI MI ✅

```
KLİP 48 × 10,0 s · SAHNE 12 · BÖLÜM 2 · REPLİK 0 · EKRAN METNİ 0,0 s
İNSAN ŞERİDİ --1111111111111111111111111111111111111111111111 (46/48)
YERÇEKİMİ 0,30 g · düşüş 1,40 m → 0,97 s · 0,60 m → 0,64 s · 0,35 m → 0,49 s
SICAKLIK dikey yüzey 370 K · yatay zemin 180 K · fark 190 K · genleşme 1,3 mm/m
AÇIKLIK 20 mm boşluk < 23 mm büyüme (18 m × 1,3 mm/m) → çerçeve oturuyor
ÖLÇÜ SÖZLÜĞÜ anahtar 56 cm · kesici 46 cm (sap 19 mm) · kapak 1,10 × 0,80 m ·
  levha 2,40 × 1,20 m · çerçeve dizisi 18 m · sırt 40 m · vizör 22 × 14 cm
GÖLGE KENARI 2,0 cm/s (72 m/saat) · devir 44 gün
SAYAÇ 3 kanal, üçü de monotonik (SPEC C bloğu)
```

**ÖLÇÜLEN KAPSAMA — iddia değil grep sonucu:**

| kilit | kaç promptta / klipte | ölçüm |
|---|---|---|
| `locked-off` | **96/96 prompt** | `grep -c locked-off` |
| PHYSICS satırı BİREBİR aynı | **48/48 video · 1 farklı metin** | `grep -h "^PHYSICS:" \| sort -u \| wc -l` = 1 |
| AUDIO ilk cümlesi BİREBİR | **48/48 video** | tam dizge sayımı |
| `CONTINUOUS ACTION:` | **72 prompt** = 36 klip × 2 (12 sahne başı hariç) | `grep -c` |
| dönüş işaret satırı | **74 prompt** = 37 klip × 2 (11 ilk kullanım hariç) | `grep -c` |
| metal üç kalem cümlesi | **36/48 klip** | metal yüzey kadrajda olan klipler |
| asimetri pozitif cümlesi | **17/48 klip** | temasın konu olduğu klipler |
| dünya çapası (üç cümle) | **13/48 klip** | gök/ufuk kadrajda olan klipler [D214] |
| zincir dili | **0/96** | `grep -ciE "exact last frame\|previous clip\|picks up where"` |
| tırnak (replik) | **0/96** | `grep -o '"' \| wc -l` |
| `seamless`·`bubble`·`dome`·`wraparound` | **0/96** | tek tek sayıldı |
| `body`·`dead`·`corpse`·`remains` (ikinci giysi için) | **0/96** | tek tek sayıldı; "full body" ㉖ sözlüğü ve "her body small" ayrı sayıldı |

## 🟠 D. RİSK SAYIMI ✅

```
TETİKLENEN: 8 / 13   (KART 3 · 4 · 5 · 6b · 9 · 10 · 12 · 13)
EŞİK: 5 → AŞILDI
UYGULANAN: KİLİT TAVANI. Malzeme AZALTILMADI (14.09.2026 kararı);
  20 ders kilidi PLAN'da, 7 satır `UYGULANMAYAN KİLİTLER`de gerekçeli.
KALAN EN YÜKSEK RİSK: 🟠 KART 3 (vizör biçimi) — referans paketi yazılmadığı
  için biçim kilidi YALNIZ metinde. Tek savunma: dört sayı + yasak kelime
  listesi + ikinci klipte elle kontrol + ÜRETİM DURUR kapısı.
```

## 🟡 E. QA'YA HAZIRLIK ✅

```
QA_SPEC:        THE_LAST_TOW_QA_SPEC.md — A/B/C/E blokları TAM
                ㉔ makine çapası 7/7 dolu · 9 satırlık YANLIŞ-POZİTİF DUVARI
MAKİNE KAPISI:  6 kapı · ALTISI DA ffmpeg 8.1 ile DOĞRULANDI (28.09.2026):
                showinfo · select · signalstats · crop · blackdetect · -sseof
                ⛔ [D142] kuru koşu yapıldı: `ffmpeg -hide_banner -filters`
GÖZ KAPISI:     5 (G1 iki gövde ayrımı · G2 atomik sınır · G3 ikinci panel ·
                G4 vizör biçimi · G5 metalde metin)
ÜRETİM DEFTERİ: klip başına satır · ilk satır K43 · üç araç ayarı kutusu
                (altyazı KAPALI · filigran YOK · konuşan ağız kadraj dışı)
BÖLÜM BEYANI:   iki yarım master için iki cümle SPEC A'da yazılı [D129]
DİYALOG KRİTİĞİ: KOŞULMAZ — replik 0, zincir tetiklenmiyor
```

---

## ⬜ ÖLÇÜM RANDEVULARI — tahmin YAZILMADI

| # | ne ölçülecek | nerede | neden şimdi yazılmadı |
|:--:|---|---|---|
| 1 | klip süresi [D124] | araçtan, ilk klipte | tercih değil aracın ayarı; 10,0 s bir varsayım |
| 2 | vizör biçimi (kubbe kayması) | ikinci üretilen klipte, gözle | referans paketi yazılmadı → tek savunma elle kontrol |
| 3 | K31 — ikinci giysinin panelinde yüz belirir mi | üretimde | iptal kapısı ①; belirirse üretim durur |
| 4 | K44 — atomik sınır mı, erime mi | üretimde | iptal kapısı ②; erime çıkarsa kanıt K45'e taşınır |
| 5 | ⭐viral üç aday (K16 · K27 · K40) | masterda | §2.3 kartının bandı 0-3 · hedef değil ÖLÇÜM |
| 6 | ⑫ orta bölüm düşüşü (S04-S06) | bölüm 1 masterında | KRONOS'un "LEAVES AT 00:48" arızası bu bandın aynısı |
| 7 | gölge içi YAVG < 12/255 | SPEC E kapı 3 | vakumda dolgu 0 — §3.2'nin TERSİ eşik |
| 8 | çekicinin feneri (K10) 100 px üstünde mi | masterda | 18 mm'de uzak nesne riski [D179] |

---

## 🧮 GENLEŞME SAYISININ DÜRÜST KAYDI — karta karşı ölçüm

```
Kart §3.8: "~100 K'den ~370 K'ye çıkan levha metrede yaklaşık 1,3 mm uzar."
ΔT = 270 K. Bu sayı α = 4,8 × 10⁻⁶ /K anlamına gelir — tungsten ya da Kovar
sınıfı düşük genleşmeli bir alaşım.
Yapı çeliği için α ≈ 12 × 10⁻⁶ /K → aynı ΔT'de 3,2 mm/m.
Alüminyum için α ≈ 23 × 10⁻⁶ /K → 6,2 mm/m.

FİLM KARTIN SAYISINI KULLANDI (1,3 mm/m → 18 m'de 23 mm) çünkü kart tek
kaynaktır ve iki film aynı sayıyı taşımalı. ⭐ SONUÇ HİKÂYE İÇİN GÜVENLİ:
boşluk 20 mm ve kartın sayısı bile onu kapatıyor (23 > 20). Çelik değeriyle
büyüme 58 mm olur, yani mekanik DAHA GÜÇLÜ çalışır — hikâye hiçbir yönde
kırılmıyor.
⬜ Kart sayısının hangi alaşımı varsaydığı YAZILI DEĞİL. Bu bir aday gözlem
  olarak `DERSLER/GOZLEM_DEFTERI.md`'ye taşındı; kartı DEĞİŞTİRMEK sahibin kararı.
```

---

## ✅ KAPI SONUCU

```
18 / 18 madde cevaplandı  ·  A0-A5 ✅  ·  B1-B6 ✅ (B5b tetiklenmedi, gerekçeli)
                          ·  C ✅  ·  D ✅  ·  E ✅
prompt_kontrol.py yatay_8_dk_filmler/THE_LAST_TOW
  → 📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik · 96 prompt
  → ⛔ 0 BLOCK · ✅ GO
  → image 161-250 kelime · video 196-267 kelime (bant 100-250 / 120-300)
DİYALOG KRİTİĞİ: koşulmadı — replik 0
ÜRETİM: 0 kare. 8 ölçüm randevusu ⬜ AÇIK, hiçbirine tahmin yazılmadı.
```
