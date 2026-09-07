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

---

## 🔴 DERS 140: KLON KLİBİN İLK YARIM SANİYESİNDE DOĞUP KAYBOLUYOR — NORMAL HIZDA GÖRÜNMEZ, ALTI MERCEKTEN BİRİ GÖRDÜ VE SANİYESİNİ YANLIŞ YAZDI

**Kaynak:** THE THIN ROOF QA (28.08.2026) — S3 · **30,20–30,50 s** · ① KARE
"Character 3/10 🔴 BLOCKER" · ② DEVAMLILIK "Quantity 1/10 · IDENTITY BREAK"
**Sorun:** klonun nerede doğduğu ilk kez ÖLÇÜLDÜ

D20 ve D69 klonun ARAÇ/KAPI giriş-çıkış anlarında doğduğunu söylüyordu. Bu
filmde araç yok, kapı yok, ikinci figür yok, ve klon yine doğdu. Ölçüm:

```
S3 klibinin ilk 0,8 saniyesi · 10 fps · sekiz kare:

  30,03  ✅ tek kask, tek yüz
  30,13  ✅ tek kask
  30,23  ⚠️ omzun sağında kubbe biçimli gri form
  30,33  🔴 İKİNCİ KASK — içinde İKİNCİ YÜZ
  30,43  🔴 iki kask, iki yüz, birbirinin içine geçmiş
  30,53  ✅ form omuza + çivit banda geri çözülüyor
  30,63  ✅ tek kask
  30,73  ✅ tek kask
```

**Klon 0,30 saniye yaşadı ve klibin ilk yarım saniyesinde doğdu** — yani
I2V'nin başlangıç karesine oturma penceresinde, tam bir kesmenin üstünde.

⭐ **Bu yüzden hiçbir izleme onu bulamaz.** 0,3 saniye, normal hızda bir
göz kırpmasıdır ve tam kesmenin üstünde olduğu için izleyici onu "kesme
titremesi" diye yutar. Altı mercekten yalnız ① gördü, ② de ondan kopyaladı;
ikisi de saniyeyi yanlış yazdı (0:35 · "cliff edge") çünkü klibi izlediler,
KARELERİNİ değil.

**ÇÖZÜM — kurgu kapısına dördüncü satır: HER KLİBİN İLK 0,6 SANİYESİ TARANIR**

```bash
# klip başına ~1 saniye · toplam maliyet 6 klipte ~10 saniye
for s in 0 1 2 3 4 5; do
  t=$(echo "$s * $KLIP" | bc)
  ffmpeg -v error -ss $t -i "$MASTER" -t 0.6 -vf "fps=10,scale=460:818" \
         -q:v 2 giris_S${s}_%02d.jpg -y
done
# altı şerit, altı bakış. Aranan: ikinci kask, ikinci yüz, ikinci el,
# ikinci gölge, omuzdan/kalçadan doğan form.
```

```
⛔ EŞİK: klibin İLK 0,5 SANİYESİNDE beliren ve KAYBOLAN her form bir
   üretim kusurudur — kalıcı olmaması onu hafifletmez, GİZLER.
   Bulunursa o klip yeniden üretilir; kırpmayla ya da 3 kare kesmeyle
   kurtarılmaz, çünkü kesme filmin ızgarasını bozar [D115].
```

**ÇÖZÜM — ① KARE rubriğinin DUPLICATE CHARACTER kontrolüne:**

```
SPECIFIC CHECK — CLIP-HEAD DUPLICATE: step through the FIRST HALF SECOND of
every clip frame by frame, not at playback speed. A duplicate head, face,
hand or shadow that is born out of the subject's own shoulder or hip and
dissolves back into it within a few frames is the most common form of this
failure and the least visible one: it sits on a cut, it lasts less than half
a second, and at speed it reads as a compression stutter. Report the frame
range, not the second.
```

> 🔗 Ders 20/69 (klon · giriş-çıkış sıcak noktası — bu ders yeni bir sıcak
> nokta ekliyor: KLİP BAŞI) · Ders 18 (yürüyüş eklem artikülasyonu) ·
> Ders 125 (cevabı bir komutta duran soru modele sorulmaz — burada komut
> `ffmpeg -t 0.6 -vf fps=10`).

---

## 🔴 DERS 146: "SEAMLESS VISOR" KUBBE DAVETİYESİDİR — VİZÖR BİÇİMİ SAYIYLA YAZILMADI, BİR FİLMDE ÜÇ KASK ÇIKTI

**KAPI:** BETİK · `prompt_kontrol.py` D79 kask bloğu (`\bsuit\b` → vizör cümlesi
şart). ⚠️ **Betik cümlenin VARLIĞINI ölçer, ETKİSİNİ ölçmez** — aşağıdaki
01.09.2026 vakasına bak.
**TEKRAR:** **3** · ⛔ **ÇALIŞMIYOR — dönüştürme borcu doğdu** [DERS_YAZIM_KONTRATI §3]. 3. vaka 05.09.2026 THE STANDING WIRE: SPEC C bloğu *"vizör TEK DÜZ PANEL, görünür koyu çerçeve içinde — kubbe DEĞİL · 0 ton · 0 ayna kaplaması · 0 çevre yansıması"* diyordu, `prompt_kontrol.py` klasör modunda **GO** verdi, ve ekranda 24 klibin ezici çoğunluğunda **KUBBE/BALON vizör** çıktı (105 s CU + 25 karelik sahne ızgarası, ikisine de BAKILDI); vizörde belirgin çevre yansıması da var. Filmde REFERANS_PAKETI yoktu, üretilmiş panel 0. · 2. vaka 01.09.2026 (YERÇEKİMİ FAZ 2)
**BORÇ:** cümleden ARACA. Aday dönüşüm `GOZLEM_DEFTERI` ADAY-2'de duruyor ve artık iki ölçülmüş filmi var: biçim kilidi olan varlığın **referans paneli üretilmemişse** `prompt_kontrol.py` GO veremez. ⭐ **06.09.2026 — ARACIN YARISI YAZILDI:** `../REFERANS_PAKETI_KILAVUZU.md` ve `../FILM_KLASOR_SABLONU/FILM_REFERANS_PAKETI.md` kuruldu; tetikleyici tablosu, sayfa kanonu, sahne→referans eşleme ve kabul kapısı artık YAZILI. ⛔ **BORÇ KAPANMADI:** kapının BETİK yarısı hâlâ yok — `prompt_kontrol.py` paketin VARLIĞINI ölçmüyor, çapraz bağ (§6.1 ②) ve bayt aynılığı (§6.1 ⑩) denetimleri yazılmadı. Ölçüldü (06.09): referans sayfası DOSYA modunda ⑯ ⑮ ⑲ D79 kapılarından geçiyor ama DİZİ kapılarına girmiyor ve "panel üretilmemişse GO yok" kuralını hiçbir kapı koşmuyor. Bu ders ⛔ ÇALIŞMIYOR damgasını KORUR. Kanıt aynı yönde: iki filmde de tarif eksiksizdi, ikisinde de tutmadı; tutan tek vaka (YERÇEKİMİ, mekik burnu) biçimin kadrajda YÜK TAŞIDIĞI vakaydı.

> ⛔ **01.09.2026 · 2. VAKA — VE BU VAKA DERSİN ÇÖZÜMÜNÜ ÇÜRÜTÜYOR.**
> YERÇEKİMİ, bu dersin reçetesini HARFİ HARFİNE uyguladı: vizör geometrisi
> ölçüyle yazıldı (`flat rectangular front glass measuring 24 by 16
> centimetres, held in a visible bright metal frame the width of a finger`),
> "seamless/bubble/dome/sphere" kelimelerinin hiçbiri hiçbir prompta girmedi,
> ve cümle FAZ 2'nin **dokuz promptunda** duruyordu. prompt_kontrol.py GO verdi.
> **Sonuç: kubbe çıkan altı klibin BEŞİNDE tam tarif ölçüleriyle vardı.**
> İki bağımsız denetim geçişi (biri KATALOGSUZ/kör, D164) aynı şeyi söyledi:
> *"kesintisiz kavisli balon, sıfır düz kenar, sıfır köşe; başın önünü ve
> yanlarını tamamen sarıyor."* Altı klipte de.
> ⭐ Kilidin İKİ yarısı vardı ve ayrıştılar: **GEOMETRİ 0/6 tuttu, OPTİK 6/6
> tuttu** — cam berrak, aynasız, yüz okunuyor. Dramayı taşıyan yarı kazandı,
> dekoratif yarı kaybetti.
> **Okunacak sonuç: vizör geometrisi METİNLE tutulamıyor.** Reçete "sayı yaz"
> demeye devam ederse üçüncü vaka gelir. Tek aday araç: karakterin yüz CU
> referans paneli (RA p4) üretilip seed'i yazılmadan yüz içeren klip
> üretilmez. Ders 165 adayı GOZLEM_DEFTERI'ndedir (mod V, film-dersi yazılamaz).

**Kaynak:** THE SKYLIGHT — ② 🟠 "helmet has opaque sides at 0:10, then wide clear
transparent sides at 4:10"; master kareleri 0:25 (beyaz kabuk + ön cam) · 4:15 (tam
saydam kubbe) · 5:05 (koyu tonlu kubbe) · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md`
**Sorun:** 1 film, iki üretim partisi, üç kask.

CHARACTER bible vizörün OPTİĞİNİ (berrak, tonsuz, yansımasız — D95) ve kaskın SIRTINI
(ünite yok, düz — D79) kilitledi; GEOMETRİSİNİ kilitlemedi. "closed helmet, its
seamless visor" cümlesi vizörün nereye kadar uzandığını her klipte modele bıraktı:
mağara partisinde beyaz kabuk içinde ön cam, kabin partisinde tam balon, son klipte
tonlu kubbe. D95 "optik berrak vizör 'kask yok' okunuyor" demişti; cevabı görünür
bir kabuk ÇERÇEVESİYDİ — ve çerçeveye hiç ölçü verilmedi. "Seamless" kelimesi
çerçevesizlik ister; çerçevesizlik kubbedir.

**ÇÖZÜM — vizör geometrisi sayıyla, bible'da ve her promptun kompakt kilidinde
kelimesi kelimesine:**

```
HELMET GEOMETRY LOCK: a white hard shell covers the top, back and both sides
of the head; the visor is ONE curved clear pane on the FRONT only, about 24 cm
wide and 16 cm high, set into the shell with a visible dark rim all the way
round; the sides of the helmet are opaque white, never glass; NOT a bubble,
NOT a dome, NOT a full-face sphere; the pane is colourless — zero tint, zero
mirror, zero reflection — the same pane in every scene.
```

"seamless", "bubble", "dome", "sphere" kelimeleri kask tarifine GİRMEZ.

> 🔗 Ders 5 (vizör kaybolması) · Ders 37 (kask aniden beliriyor) · Ders 79 (olumsuz
> kostüm kilidi çekirdeğe girmedikçe tutmuyor) · Ders 95 (optik kilit vardı, geometri
> yoktu — bu ders o boşluğu kapatır) · Ders 57 (kare kilidi).

---

## 🟡 DERS 147: ÜÇ SABİT AŞINMA İZİ TOZLU ODADA TUTMADI — MODEL MAĞARADA KİRİ BİRİKTİRDİ, KABİNDE BIBLE'A DÖNDÜ, İZLEYİCİ "KİR SIFIRLANDI" OKUDU

**Kaynak:** THE SKYLIGHT — ② 🟠 cat 3 "suit back heavily soiled at 2:20 → pristine at
4:10 (−6)"; master kareleri 2:25 (sırt ve bacaklar gri tozlu) · 4:15 (kabinde
tertemiz); bible "exactly three fixed wear marks" · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md`
**Sorun:** 2 film — ve D42'nin kendisi sebep. **2. vaka THE FROST LINE
(31.08.2026):** bu dersin faz satırı ("wear state: PHASE n") 50/50 promptta
YAZILIYKEN kırağı hem ERKEN geldi (PHASE 1 sahnesinde önkolda kırağı — kare
t14) hem dalgalandı (t23 temiz ↔ t193 hafif ↔ t204 yoğun). Faz METNİ tek
başına tutmuyor: fazın İLK sahnesinin onaylı karesi, aynı fazın sonraki
sahnelerine imaj referansı olarak girer [D153 mekanizması].

D42 aşınma izlerini sabitler ki her karede yeniden üretilmesinler; ortamın iz
EKLEMEDİĞİNİ varsayar. Dört dakika boyunca diz çöküp milimetrelik tozda çalışan bir
karakter için temiz takım OLANAKSIZ durumdur — model mağara partisinde takımı
kirletti (fizik doğru), kabin partisinde bible'ı tekrar okudu ve temizledi (prompt
doğru). İki parti de kendi promptuna uydu; FİLM kendisiyle çelişti. Kural sabitti,
hikâye birikimliydi.

**ÇÖZÜM — kir MONOTONİK bir sayaçtır: faz durumları yazılır, her prompt kendi faz
satırını taşır, son faz iç mekânlar dâhil sonraki her sahneye taşınır:**

```
WEAR LADDER (monotonic — dust is only ever added, never removed):
  PHASE 1 · surface, before entry: clean sand-white shell; only the three fixed marks.
  PHASE 2 · first chamber scenes: fine grey dust on both knees and shins; gloves dusted; back clean.
  PHASE 3 · deep chamber to exit: heavy grey dust on knees, shins, forearms and the lower back; boots grey to the ankle.
  PHASE 4 · ship, cabin, orbit: PHASE 3 state, unchanged — the suit stays dusty inside the cabin; no cleaning happens; the dust never resets.
Her sahnenin promptunda TEK satır: "wear state: PHASE n — <fazın metni>".
```

Cairn sayacı gibi: geriye gitmez, sıçramaz, faz değişimi yalnız sahneler ARASINDA.

> 🔗 Ders 42 (sabit yerleşim — bu ders onu TOZLU ortamda monotonik sayaca çevirir) ·
> Ders 58 (tekrarlayan varlık kimliği) · Ders 118 (sıra kilidi — kir de bir şerittir).

---

## 🔴 DERS 169: 25 SAHNELİK BİR FİZİKSEL İŞ FİLMİNDE ZORLANMA SÖZLÜĞÜ TEK SAHNEDE VARDI — DÜŞÜK YERÇEKİMİ AĞIRLIĞI AZALTIR, ATALETİ AZALTMAZ

**KAPI:** BETİK · `prompt_kontrol.py` ⑳ ZORLANMA KANALI (efor sahnesinde gövde tepkisi cümlesi var mı) — 02.09.2026
**TEKRAR:** 2 · 02.09.2026 THE SINKING STAKE · ⚠️ 04.09.2026 THE UPWARD FALL — ters yönde: efor sözlüğü UYGULANDI (8 sahnede 2 kanal) ama ÖNKOL kanal cümlesi (`the forearm tendons stand out through the glove`) mühürlü giysili filmde **çıplak deri** ürettirdi → cümle [[D175]] ile değişti

**Kaynak:** THE SINKING STAKE prompt dosyaları (02.09.2026) — **kendi
belgemizden sayıldı, rapordan değil.** 25 sahne, 25 TIMELINE, iki bölüm
dosyası:

```
strain        0        heave           0        grip tighten   0
tremor        0        stiff glove     0        clumsy         0
lean into     0        braced          1  (yalnız S13)
"working breath" 2     "shoulders low" 1  (ikisi de yalnız S13)
forearm      19  ← ONDOKUZUNUN ONDOKUZU KOSTÜM: "a white cuff on the
                    left forearm only". Zorlanma anlamında SIFIR.

→ 25 sahnenin 24'ünde fiziksel iş yapılıyor ve gövde hiçbir şey ödemiyor.
```

⭐ **MEKANİZMA — DÜŞÜK YERÇEKİMİ YAZARI KANDIRIR.** Plan 0,40 g yazar,
yazar "hafif" diye düşünür ve zorlanma cümlesini gereksiz sayar. Ama:

```
0,40 g'de AZALAN     ağırlık (kaldırma kuvveti)
0,40 g'de AZALMAYAN  KÜTLE ve ATALET
→ bir cismi başlatmak, durdurmak ve döndürmek AYNI eforu ister.
→ ve giysi maliyeti hiç azalmaz: basınçlı eldiven kapanmaya direnir,
  kask baş dönüşünü kısıtlar, sırt/kalça yükü ağırlık merkezini kaydırır.
```

⛔ **VE İKİNCİ TUZAK: TIMELINE KONUM YAZAR, GÖVDE YAZMAZ.** Bu deponun
TIMELINE biçimi "0.0s — X yapar · 4.0s — Y olur" diyerek NEREDE ve NE
sorularını cevaplıyor, NASIL sorusunu hiç sormuyor. Model de tam olarak
yazılanı üretiyor: iş yapılıyor, kimse ödemiyor.

**ÇÖZÜM — HER EFOR SAHNESİNİN TIMELINE'INDA EN AZ İKİ KANAL:**

```
Kanallar (ikisi seçilir, sahneye göre):
  ÖNKOL     "the forearm tendons stand out through the glove"
  KAVRAMA   "the grip slips a finger's width and is re-taken"
  GÖVDE     "he leans into it until his shoulders are below his hips"
  BACAK     "the rear boot loads and the knee bends before the pull"
  NEFES     "two breaths per pull, the second one shorter"
  KADANS    "the fourth pull is visibly slower than the first"
  ELDİVEN   "the fingers close slowly against the glove's own stiffness"

⭐ VE BEDEL SAHNEDEN SONRA DA GÖRÜNÜR: bir sonraki sahnenin ilk saniyesi
  toparlanmayı taşır (duruş, bir nefes, geciken bir hareket) — yoksa
  "FRESH RESET" olur ve iş hiç yapılmamış sayılır.

⛔ SAYI YAZILIR, SIFAT DEĞİL: "the fourth pull is slower than the first"
  ölçülebilir; "he strains" ölçülemez ve model onu çizmez [tarif kilidi
  %0, sayısal kilit %100 — 01_DERS_ETKINLIK_RAPORU §4].
```

⚠️ **DAHA FAZLA ACI DAHA İYİ DEĞİLDİR.** Sebepsiz gelen yorgunluk da hatadır:
gövde yalnız ekranda GÖSTERİLEN işin bedelini öder.

> 🔗 Ders 44 (0,38 g gerçek zamanlı) · Ders 154 ③ (insanın g'si adım SAYISIYLA
> yazılır — bu ders onu EFOR kanalına genişletir) · KARAKTER_VE_DUYGU §6
> (el/nefes/yürüyüş bütçesi — bu ders o bütçeye ZORLANMA'yı ekler) ·
> mercek ⑧ EFOR (bu dersin ölçüm aleti).
