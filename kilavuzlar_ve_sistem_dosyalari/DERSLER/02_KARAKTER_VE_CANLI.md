# 📚 DERSLER — Karakter ve Canlı Devamlılığı

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Karakter ve Canlı Devamlılığı** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🔴 DERS 2: CANLI MORPH — ARKA PLAN CANLILARI DEĞİŞİYOR

**Kaynak:** The Canopy World QA — Canlılar: 4/10
**Sorun:** Arka plandaki canlılar (Moss Giant) sahne boyunca anatomik olarak değişiyor — iki ayaklıdan dört ayaklıya, maymundan dinozora dönüşüyor.

**ÇÖZÜM — Her canlı içeren prompt'a eklenecek:**
```
CREATURE ANATOMY LOCK: Every creature in this shot must maintain FIXED, RIGID
anatomy throughout the entire 10-second clip. Limb count, body shape, head
shape, and overall silhouette must remain identical from frame 1 to frame 300.
No morphing, no shape-shifting, no anatomical drift.
```

**ARKA PLAN CANLILARI İÇİN EK ÇÖZÜM:**
```
BACKGROUND CREATURE RULE: Any creature not in the immediate foreground must be
rendered with SHALLOW DEPTH OF FIELD (soft focus, slightly blurred) to reduce
the AI's tendency to over-detail and morph background elements. The creature's
SILHOUETTE must remain locked even when out of focus.
```

---

## 🟡 DERS 16: YÜZ MORPH — KASK ARKASINDA YÜZ DEĞİŞİMİ

**Kaynak:** The Slow Tide QA — Karakter: 4/10
**Sorun:** Kask camı arkasında yüz kemik yapısı, göz pozisyonu ve yüz hatları kareden kareye değişiyor.

**ÇÖZÜM — Her kask/vizör içeren sahneye eklenecek:**
```
FACE LOCK RULE: The character's face behind the visor must maintain IDENTICAL
bone structure, eye spacing, nose shape, and facial proportions throughout
the entire 10-second clip. No morphing, no shifting, no feature drift. The
face visible through the visor must be recognizably the SAME PERSON in every
frame — as if photographed by a real camera through real glass.
```

---

## 🔴 DERS 18: CANLI YÜRÜYÜŞÜ — HAYVANLAR KAYARAK HAREKET EDİYOR

**Kaynak:** The Tidal Hunt QA — Canlı: 2/10, Hareket: 3/10
**Sorun:** Canlılar yüzeyde kayarak hareket ediyor — bacak artikulasyonu yok, yüzeyle temas yok. Kuşlar uçarken tanımsız blob'lara dönüşüyor.

**ÇÖZÜM — Canlı hareketi içeren her sahneye eklenecek:**
```
CREATURE LOCOMOTION RULE: Every creature must move with ARTICULATED LIMB
MOTION appropriate to its body type:
- Walking/running creatures: each leg lifts, swings forward, plants, pushes
- Flying creatures: wings flap with visible joint articulation, maintain shape
- Swimming creatures: body undulates or fins stroke with consistent rhythm
Creatures must NEVER slide, glide, or drift across surfaces without visible
limb movement. Each footfall must show surface contact and weight transfer.
```

---

## 🔴 DERS 20: KARAKTER KLONLAMA — ÇİFT KİŞİ HATASI

**Kaynak:** The Kaleida Crash QA — Karakter: 5/10
**Sorun:** 1:25'te sahnede aynı karakterin ikinci bir kopyası belirdi — iki identik karakter aynı karede yürüyor. AI video modelleri bazen uzun sekanslar boyunca karakter tutarlılığını kaybedince yeni bir figür üretiyor.

**ÇÖZÜM — Her video prompt'una eklenecek:**
```
SINGLE CHARACTER RULE: There is EXACTLY ONE human character in this
entire scene — no duplicates, no clones, no reflections that become
independent figures, no second person appearing from any direction.
If a figure appears in frame that was not explicitly described in this
prompt, it is an ERROR. Only the single described character exists.
```

---

## 🔴 DERS 35: DUDAK SENKRONİZASYONU ÇÖKÜŞÜ — DİYALOG AĞIZDAN AYRIŞIYOR

**Kaynak:** The Dead Approach Compilation QA (Genel 3/10) — Diyalog & Ses: 3/10 — `0:11 — Lip-sync fails entirely on dialogue`
**Sorun:** Serinin diyaloglu filmlere geçişiyle ortaya çıkan ilk büyük yeni hata sınıfı. Ses üretiliyor, ağız hareket ediyor, ama ikisi eşleşmiyor: fonemler tutmuyor, replik bittikten sonra ağız hareket etmeye devam ediyor, ya da karakter hiç konuşmadan ses geliyor.

**Neden oluyor (üç ayrı sebep, üçü de ayrı çözüm ister):**
```
(a) ÇEKİM ÖLÇEĞİ: Geniş çekimde ağız piksel ızgarasında çok küçük kalıyor,
    model dudak detayına bütçe ayırmıyor.
(b) REPLİK UZUNLUĞU: 5 saniyeyi aşan repliklerde zamanla kayma (drift)
    birikiyor ve replik sonunda tamamen ayrışıyor.
(c) EKRAN DIŞI SES BELİRSİZLİĞİ: Prompt sesin nereden geldiğini
    söylemiyorsa model konuşan bir ağız İCAT EDİYOR.
```

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **Diyaloglu sahne = orta yakın çekim.** Konuşan karakter varsa lens ve mesafe buna göre kilitlenir. Geniş çekimde konuşma yazılmaz.
2. **Her replik 5 saniyenin ALTINDA.** Uzun cümle iki sahneye bölünür, tek klipte sıkıştırılmaz.
3. **Ekran dışı ses AÇIKÇA işaretlenir.** Bu, serinin en çok kullandığı yapı (AI sesi, radyo, kayıt) ve en çok hata verdiği yer:
```
The voice is off-screen audio only — no character speaks on camera,
no mouth is visible in frame, no lip movement is required or shown.
```
4. **Konuşan karakter varsa fonem sadakati istenir:**
```
her lip movements match the spoken words precisely for the full duration
of the line, and her mouth is still and closed before and after the line
```
5. **En güvenli yapı: tek konuşmacı, sıra alma, asla eşzamanlı.** İki ses aynı anda konuşursa lip-sync başarısı %40'ın altına düşer.

---

## 🔴 DERS 69: KLON SICAK NOKTASI ÖNGÖRÜLDÜ, METİN KİLİDİ YİNE TUTMADI — BİNİŞ/İNİŞ HAREKETİ KADRAJA ALINMAZ

**Kaynak:** THE STONE SKY dört mercek QA (05.08.2026) — teknik Karakter 3/10 ·
karakter Sayı-Ayrışma **1/10** · mantık Nicelik **1/10** ·
`1:40 — 🔴 two identical astronauts running side-by-side` (S10-B, araçtan iniş)

**Tekrar:** 06.08.2026 THE UNBROKEN CITY teknik QA — `0:40 — 🔴 duplicate
standing right side of the room`. Klon bu kez biniş/iniş değil, **LOŞ İÇ
MEKÂN** (tek ışıklı karanlık oda; planda ayna/heykel yasaklıydı). Sıcak
nokta listesi genişledi: araç binişi-inişi + loş iç mekân girişleri.

**Tekrar 2 — ve en kötüsü:** 06.08.2026 THE STARLESS CIRCLE mantık + karakter
QA — `2:10 — 🔴 two identical astronauts at the ship ladder` (Nicelik 1/10 ·
Sayı-Ayrışma 1/10). Klon, planın **S14 BİNİŞ** sahnesinde çıktı: "yedi
basamak + eşikte diziye son bakış". Yani bu ders yazıldıktan **bir gün
sonra** yazılan plana, dersin ① maddesinin tam olarak yasakladığı sahne tipi
eklendi. Ders LESSONS_LEARNED'da duruyordu, iki rubriğe de işlenmişti ve
plan aşamasına hiç ulaşmadı → **DERS 77.**

**Sorun:** Klon, planın ÖNCEDEN işaretlediği yerde çıktı. Plan Risk Kartı 4'ü
açmış, S2-B (binme) ve S10-B (inme) segmentlerini "klon sıcak noktası" ilan
etmiş, HUMAN COUNT LOCK yazmış, o segmentlere ayrıca *"exactly one human"* +
*"the seat behind her is EMPTY"* koymuştu. **Öngörü doğruydu; kilit türü
yanlıştı.** Sebep mekanik: binme/inme anında modelin kadrajında aynı insanın
İKİ durumu var (araçta + araç dışında) — model ikisini iki ayrı kişi olarak
çizmeye meyilli. Ders 20 klonu genel olarak yasaklıyordu; bu ders klonun
ÜRETİLDİĞİ tek sahne tipini kapatıyor. (İkinci vaka sayılabilir: Tidal Hunt
S1/S10 "iki kâşif" — orada da giriş/çıkış sahneleriydi.)

**ÇÖZÜM — PROMPT DEĞİL, SAHNE TASARIMI:**

```
① BİNİŞ/İNİŞ HAREKETİ HİÇBİR SEGMENTTE KADRAJA ALINMAZ — 0 kez.
   Karakter ya araçtadır ya araç dışındadır; ARADAKİ hareket kesmeyle
   atlanır. Kesmenin iki yakası şöyle yazılır:
     A segmenti: "she sits strapped in the rover seat, both hands on
                  the yoke" (araçta, tek insan)
     B segmenti: "she stands on the ground two meters from the rover;
                  the rover seat behind her is EMPTY, its harness strap
                  hanging slack" (dışarıda, koltuk BOŞ ve boşluğu
                  görünür bir propla kanıtlı)
② Boş koltuk cümlesi tek başına yetmez (Stone Sky'da yazılıydı ve tutmadı)
   — koltuğun boşluğu FİZİKSEL bir işaretle tarif edilir (sarkan kayış,
   koltukta duran eldiven), çünkü model "empty" sıfatını değil nesneyi çizer.
③ Kurgu kurtarması her filmde hazır tutulur: klon çıkarsa iki figürlü
   geniş plan kesilir, tek figürlü kadraj kalır (Stone Sky'da maliyet ~2 s).
```

> 🔗 Ders 20 (kopya karakter) genel yasağı koyar; bu ders tetikleyen sahne
> tipini (araç/kapı/airlock giriş-çıkışı) tasarımdan kaldırır. Ders 68 ile
> aynı sınıf: prompt cümlesi değil, karar değişikliği.

---
## 🔴 DERS 82: SES MİMARİSİ ÜRETİMDE TERSİNE DÖNDÜ — GÖVDESİZ AI SİLİNDİ, TELSİZ REPLİKLERİ EKRANDAKİ AĞIZLARA DEVREDİLDİ

**Kaynak:** THE COLD BURN beş mercek QA (09.08.2026) — SES_QA'nın İLK koşusu,
register haritası: 7 replik / 7 HUMAN / 0 MACHINE — `0:12-1:55 — six of
seven lines delivered by on-screen moving mouths`
**Sorun:** Plan tam tersini söylüyordu: 12+ replik, TÜMÜ kapalı kask
telsizinden (kokpit arkadan çekilir, ağız asla kadrajda değil) + gövdesiz
sentetik EKO. Ekranda EKO hiç yok, sayı replikleri ("doksan saniye",
"pencere on iki saniye", "modülde yangın") ekrandaki insanlara devredilmiş,
lip-sync sigortası çökmüş. Comms filtresi de kask durumunu değil sahne
değişimini takip ediyor (buzda telsizli, kokpitte kuru — kask ikisinde de
kapalı). Bu, DERS 35(c)'nin ("kaynağı belirtilmeyen ses için model konuşan
ağız İCAT EDER") film ölçeğine büyümüş hâli: kaynak kilitlenmeyen her
replik, üretimde "konuşan yüze" çekiliyor — model için en ucuz çözüm bu.

**ÇÖZÜM — diyaloglu her sahnenin promptunda ÜÇ ALAN zorunlu:**
```
1) SOURCE kilidi (pozitif):
   The line is heard through helmet comms radio / from a cabin speaker
   as a bodiless synthetic voice — the audio is band-limited comms.
2) KADRAJ kilidi (pozitif):
   Framed from behind; no face and no mouth is visible in frame
   while the line plays.
3) NEGATİF blok:
   no talking face, no moving lips, no on-camera speaker,
   no invented speaker for off-screen audio
```
**Operatör tarafı (kart E3 adım 2):** SES_QA raporunun register haritası
planın DIALOGUE SCHEDULE'ıyla karşılaştırılır. Harita ≠ plan ise bu bir
üretim ihlalidir ve mod V raporundaki "delivery/tell" bulguları bu bilgiyle
yeniden okunur — makine olması gereken sese "insan gibi değil" demek,
insan olması gerekene "fazla düz" demek kadar yanıltıcıdır.

> 🔗 Ders 35 (lip-sync üç sebep — (c) bu dersin tohumu) · Ders 82'nin
> kanıt aleti SES_QA'nın register sütunudur: mercek olmadan bu sapma
> "kötü oyunculuk" sanılıyordu, haritayla ÜRETİM İHLALİ olarak okundu.
> ⚠️ Şerh: Cold Burn'de üretimin PART_A/B promptlarıyla yapıldığı
> doğrulanamadı (film kaydındaki ÜRETİM SORUSU). Ders, kaynak kilidi
> yazılMAmış promptlar için kesin; yazılmış promptta da delinirse ilk
> kanıt bu koşudur.

---

## 🔴 DERS 91: YARA İZİ TARAFI DEĞİL, ÖZELLİĞİ KAYBEDİYOR — "SOL KAŞ" YÜZÜN SOLUNDA HERHANGİ BİR YER OLUYOR

**Kaynak:** THE SECOND SHIP · Faz 7 / BEDEL 1. koşusu (S63 · S67 · S69)
· `.../FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md` D-AP
**Sorun:** dört insan sahnesinin ÜÇÜNDE iz yanlış yerde; F3 D-H ve
F4 D-U'nun (taraf takası) devamı ama teşhis değişti

| Yazılı | Ekranda |
|---|---|
| kadın: kaşı ikiye bölen iz, SOL KAŞ | SOL ÇENE (S67) · SAĞ YANAK (S69) |
| adam: 2 cm yanık izi, SAĞ ELMACIK | SOL YANAK (S63) |

Üç vakanın **ikisi taraf hatası değil, ÖZELLİK hatası**: iz doğru
tarafta ama yanlış organda. "A fine faded white scar splitting her LEFT
eyebrow" cümlesi modele bir KONUM değil, bir BÖLGE veriyor: "yüzünün
solunda bir iz". Taraf kilidini sıkılaştırmak (bu depoda üç kez
denendi) bu vakayı çözmez — eksik olan taraf değil, tutamak.

**ÇÖZÜM — ÖZELLİK + ÖLÇÜ + "gerisi temiz" üçlüsü:**

```
Her scar is a 2 cm white line that CROSSES THE HAIR OF HER LEFT
EYEBROW and splits it into two halves - it sits IN the brow, not
above it, not below it, not on her cheek, jaw or chin. The rest of
her face is completely unmarked: no scar, line or mark on either
cheek, jaw, chin, nose or forehead.

His scar is a 2 cm shiny burn mark ON THE BONE OF HIS RIGHT CHEEK,
below the outer corner of his right eye. The rest of his face is
completely unmarked.

Üç bileşenin üçü de gerekli:
  ÖZELLİK  izin oturduğu organ ("kaşın KILI", "elmacık KEMİĞİ")
  ÖLÇÜ     2 cm — sayısal kilit [Ders 44 ailesi]
  KAPATMA  "yüzün geri kalanı tamamen işaretsiz" — izin göç
           edebileceği bütün yüzeyleri tek cümleyle kapatır
```

⚠️ Negatife yalnız "scar stays LEFT eyebrow" yazmak yetmiyor; negatif
tarafı korur, organı korumaz.

---
