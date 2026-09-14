# 🎞️ TEK ÇEKİM VE GİZLİ GEÇİŞ KILAVUZU

> **Bu projenin bir numaralı kuralı "kesme yok" (Ders 1) — ama bu kural
> bugüne kadar sadece KLİBİN İÇİ için uygulandı.** Klipler arasında ne
> olduğu hiç tasarlanmadı: 15 sahnelik bir film, 15 sert kesmeyle
> birleştirilen 15 ayrı klip olarak kalıyor.
>
> Bu kılavuz ikinci problemi çözer: ayrı üretilmiş klipleri, izleyicinin
> tek bir kesintisiz çekim sandığı bir akışa dikmek.

```
İKİ FARKLI PROBLEM — KARIŞTIRMA:

(A) KLİP İÇİ KESME     → Model hatası. Ders 1, %100 tekrarlı.
                          Çözüm: negatif blok. Zaten yapılıyor. ✅
(B) KLİPLER ARASI GEÇİŞ → Tasarım kararı. Şu an: sert kesme.
                          Çözüm: bu kılavuz. Yapılmıyor. 🆕
```

> Not: Sinema kaynaklarındaki donanım katmanı (Steadicam, ARRI Trinity,
> Stabileye, Nuke kompozitleme, ACEScg) bu hatta girmez — 📚 bilgi olarak
> §9'da özetlendi. Aynı ✅ prompt / 🎨 post / 📚 bilgi ayrımı geçerlidir
> (bkz. `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` §17, `GOOGLE_FLOW_MUSIC…` §18).

---

## 1. 🎯 TEKLİ ÇEKİM (SINGLE SHOT) ≠ YAKIN ÇEKİM (CLOSE-UP)

Sık karıştırılan iki kavram. Ayrımı bilmek prompt yazarken işe yarar:

```
TEKLİ ÇEKİM   Kadrajda TEK bir özne var. Geniş de olabilir, yakın da.
              Mesele MESAFE değil, İZOLASYON.
YAKIN ÇEKİM   Kadrajın darlığıyla ilgili. Yüz, el, bir nesne.

Bizim serimizin tamamı zaten tekli çekimdir (tek karakter kuralı).
Ama bu bir avantaja dönüştürülmemiş: izolasyon kadraj kararıyla
GÜÇLENDİRİLEBİLİR.
```

**Kesintisiz akışta izolasyonu derinleştirmenin üç yolu (✅ prompta yazılır):**

```
1. SIĞ ODAK İLE AYIRMA
   "shallow depth of field isolates her from the plain; the rim 6 km
   away falls completely soft" — karakterin dünyadan kopuşu

2. KADRAJI DARALTAN HAREKET (kesme olmadan ölçek değiştirme)
   Geleneksel kurguda geniş→yakın bir kesmeyle olur. Bizde kamera
   fiziksel olarak yaklaşır: "slow push-in from 12 to 3 meters" —
   TEK harekette geniş plandan tekli yakın plana geçilir.

3. ÇEVREYİ BOŞALTMA
   Karakter kadrajda kalır, çevredeki her şey (kaya, araç, iz) kadraj
   dışına çıkar. İzleyici karakterle yalnız kalır.
```

---

## 2. ⏱️ KESMESİZ RİTİM — "ÖLÜ ZAMAN" DİYE BİR ŞEY YOK

```
Geleneksel kurgu, zaman atlaması (ellipsis) sağlar: karakter kapıdan
çıkar, bir sonraki karede hedeftedir. Kesintisiz akışta bu güvenlik ağı
yoktur — yürüyüş fiilen izlenir.

BU BİR SORUN DEĞİL, BU SERİNİN ZATEN OLDUĞU ŞEY.
Koridor yürüyüşü, ufka çevrilen bakış, duraklama: bunlar boşluk değil,
karakterin düşünme süresidir ve bir sonraki krizin gerilimini kurar.

→ Uzay kılavuzu §8'in "Overview sahnesi ACELE ETTİRİLMEZ" kuralı,
  aynı ilkenin başka bir ifadesidir.
→ Ritim boşluğu sahneleri (yürüyüş, bekleme, bakış) filmden ÇIKARILMAZ;
  onlar filmi tek çekim hissine taşıyan dokudur.
```

---

## 3. 📐 MEKAN–SÜRE DENKLEMİ ✅

Kesintisiz çekimde mekan, senaryonun ritmine göre inşa edilir: 1917'de
karakterin siperden çıkışı 45 saniye sürecekse, siper tam o kadar uzun
yapılır. Bizde fiziksel set yok — ama **model mesafeyi kendi uyduruyor**
ve karakteri 10 saniyede 40 metre ışınlayabiliyor.

```
✅ PROMPT KURALI: Sahnedeki yürüme mesafesi, klip süresine ve
yerçekimine göre TUTARLI olmalı ve promptta sayı olarak geçmeli.

YAKLAŞIK YÜRÜME HIZLARI (kaba ama tutarlı kullanım için yeterli):
   1g   (Dünya, zombi/savaş)      ~1.4 m/s  → 10 saniyede ~14 m
   0.7g (Slow Stone tipi)          ~1.2 m/s  → 10 saniyede ~12 m
   0.38g (Mars, Low Power)         ~1.0 m/s  → 10 saniyede ~10 m
   0.11-0.17g (ay, damped step)    ~0.8 m/s  → 10 saniyede ~8 m

PROMPT DİLİ:
"she covers roughly 8 meters across the frame during the shot, a damped
low-gravity stride of about 0.8 m/s — no teleporting, no speed-up, the
distance covered matches the elapsed time exactly."

⚠️ Bu, sahneler ARASI süreklilik için de geçerlidir: S5 sonunda araçtan
30 m uzaktaysa, S6 başında 30 m uzakta olmalı. Sahne haritasına mesafe
sütunu eklemek bu hatayı baştan keser.
```

---

## 4. 🔭 OMURGA LENS — TEK ÇEKİM HİSSİNİN EN UCUZ YOLU

```
1917'nin tamamı %99 oranında TEK lensle (40mm) çekildi. Sebep sadece
pratik değil: lens değişimi, izleyicinin farkına varmadığı ama hissettiği
bir "kopuş" yaratır. Tek odak uzaklığı, tek bir gözün baktığı hissini verir.

MEVCUT SİSTEMİMİZ: her sahne tipine bir lens kilitli
(32mm geniş / 50-75mm orta / 85mm yüz / 100mm makro).
Bu tutarlı bir sistemdir ve YANLIŞ DEĞİLDİR — ama tek çekim hissini
zayıflatır: 15 sahnede 4 farklı bakış açısı vardır.

✅ ÖNERİ — "OMURGA LENS" İLANI (zorunlu değil, filme özel karar):
Her filmin Camera Bible'ında bir omurga lens ilan edilir ve sahnelerin
en az %60'ı onunla çekilir. Diğer lensler "sapma" olarak listelenir ve
her sapmanın bir gerekçesi yazılır.

  Örnek — THE REMEMBERING DUST:
    OMURGA: 32mm (ova, ölçek, iz sırası — filmin konusu mesafedir)
    SAPMA:  100mm makro sadece S2/S6.5/S12 (iz oluşumu — üç sahne)
            75mm sadece S5/S8 (diyalog) — gerekçe: replikte yüz gerekir

  Örnek — THE SLOW STONE:
    OMURGA: 50mm  ·  SAPMA: 32mm (5 ölçek sahnesi), 100mm (4 makro),
            85mm (3 duygusal zirve)
```

---

## 5. 🩹 GİZLİ GEÇİŞ KÜTÜPHANESİ — BU KILAVUZUN ASIL KATKISI ✅

Ana akım "tek çekim" filmlerin neredeyse hiçbiri gerçekten tek çekim
değildir: birden çok uzun çekim, izleyicinin göremediği noktalardan
birleştirilir. Rope'da bu zorunluluktu (10 dakikalık film bobini), sonra
bir üsluba dönüştü.

**Bizim durumumuz Rope'un aynısı:** klip süresi sınırlı (8-10 sn), film
uzun. Fark şu ki biz birleşme noktasını gizlemeye hiç çalışmadık.

### 5.1 Çalışma Prensibi

```
Gizli geçiş, İKİ PROMPTUN BİRLİKTE tasarlanmasıdır:

  SAHNE N        son 0.5-1 saniyede kadraj bir şeyle KAPANIR
  SAHNE N+1      ilk 0.5-1 saniyede kadraj AYNI ŞEYLE kapalı başlar
                 ve aynı yönde, aynı hızda açılır

Kurguda iki klip bu kapalı anda üst üste bindirilir (2-6 kare geçiş).
İzleyici kesmeyi göremez çünkü kesme anında ekranda bilgi yoktur.
```

### 5.2 Altı Teknik ve Prompt Kalıpları

#### ① KARANLIK PERDE (occluder wipe) — en güvenilir yöntem

```
SAHNE N (son beat):
"9s — A 2-meter dark basalt boulder passes between the lens and the
figure, moving left to right, filling the entire frame with unlit rock
surface for the final half second.
10s — Frame completely occluded by dark rock, no light, no detail.
No cuts."

SAHNE N+1 (ilk beat):
"0s — The frame opens completely occluded by the same dark unlit rock
surface 30 cm from the lens, still moving left to right at the same
speed; it clears within 0.5 seconds to reveal [yeni kadraj]."

BİZDE NEREDE VAR: kaya, gemi gövdesi, iniş ayağı, airlock kenarı,
karakterin sırtı/omzu, kask, oluşum sütunu.
```

#### ② TOZ PERDESİ — bu serinin doğal geçişi

```
Vakumda ve ince atmosferde toz zaten var. İniş, adım, kazıma, kalkış
sahnelerinde ekranı dolduran toz doğal bir perdedir.

SAHNE N: "10s — The dust plume rises across the lens and fills the
frame edge to edge with dense grey particles. No cuts."
SAHNE N+1: "0s — The frame opens filled with the same dense grey dust,
which falls out of frame under 0.11g over 0.8 seconds, revealing…"

⚠️ Toz taneleri her iki klipte de AYNI fizikle düşmeli (Ders 30/39).
```

#### ③ HIZLI ÇEVRİNME (whip pan)

```
Hareket bulanıklığı birleşme noktasını gizler.
SAHNE N: "10s — The camera whips right, the frame dissolving into
horizontal motion blur. No cuts."
SAHNE N+1: "0s — The frame opens in horizontal motion blur moving in the
same direction, settling within 0.4 seconds onto…"

⚠️ RİSK: Ders 10 (rolling shutter / jello) tam burada tetiklenir.
Her iki prompta da "no rolling shutter skew, no jello effect" eklenir.
⚠️ Bizim meditatif tonumuzda whip pan yabancı durur — nadir kullan.
```

#### ④ IŞIK OLAYI

```
Acil işaret ışığı, motor ateşlemesi, kask lambasının lense dönmesi.
SAHNE N: "10s — The amber beacon pulses directly into the lens,
the frame blowing to a flat amber field. No cuts."
SAHNE N+1: "0s — The frame opens as a flat amber field that falls back
to normal exposure over 0.5 seconds, revealing…"

⚠️ Ders 29 (bloom) riski yüksek: "flat amber field" yaz, "glowing"
veya "flare" YAZMA.
```

#### ⑤ HAREKET EŞLEŞMESİ (match on motion)

```
Perde yok — geçiş, aynı hareketin sürmesiyle gizlenir.
SAHNE N sonu: eldiven aşağı iniyor, kadrajın sol üçte birinde, orta hızda
SAHNE N+1 başı: aynı eldiven aynı yönde inmeye devam ediyor, aynı hızda

En zarif yöntem ama en kırılganı: iki klipte hız ve konum tutmazsa
seyirci "atlama" hisseder. Yalnızca yakın plan el/ayak hareketlerinde
dene.
```

#### ⑥ BİLİNÇLİ SERT KESME (hard cut) — bazen doğru cevap

```
1917'de karakter vurulduğunda ekran siyaha düşer ve orada kalır: hem
zaman atlaması hem anlatı aracıdır.

BİZDE NEREDE DOĞRUDUR:
  • Overview sahnesinden ÖNCE — nefes almak için kesme gerekir
  • Bir kısım/faz sınırında (7-9 dk formatında faz geçişleri)
  • Filmin son sahnesine girerken
Gizli geçişi HER sınırda kullanmak yorucu ve gösterişçi olur.
```

### 5.3 Bir Filmde Nasıl Dağıtılır

```
15 SAHNELİK FİLM (2-4 dk):
  4-6 gizli geçiş — birbirine bağlı, aynı mekanda geçen sahne kümeleri
  2-3 bilinçli sert kesme — faz/duygu değişimi noktaları
  Kalanlar düz kesme

⚠️ HEPSİNİ GİZLEME. Amaç "hiç kesme yok" numarası yapmak değil;
filmin bazı bölümlerinin tek nefeste akmasıdır.
```

### 5.4 🆕 SAHNE İÇİ KESME — AKSİYON GRAMERİ

> Buraya kadarki her şey sahne **sınırlarındaki** geçişi anlatıyor.
> Bu bölüm sahnenin **içindeki** kesme içindir. Depoda ilk uygulama:
> `yatay_2_dk_filmler/THE_DAWN_FRONT/THE_DAWN_FRONT_PLANET_FILM.md` §0.2
> (14 sahne × 10 s · 26 segment · 12 kesme).

```
GEREKÇE   Ders 1: model zaten kesiyor (8/8 filmde tetiklendi).
          Yasaklamak, modelin bizim seçmediğimiz yerden kesmesi
          demek. Aksiyon isteyen filmde kesmeyi SAHİPLENMEK,
          kontrolsüz hatayı sayısal bir kilide çeviriyor.
```

**İKİ MİMARİ VAR — ikisi de meşru, biri seçilir:**

```
MİMARİ 1 — KESME KURGUDA
  Her segment ayrı üretilir; promptta "no cuts" cümlesi AYNEN durur;
  kesme montajda yapılır.
  ✅ kare hassasiyeti, kadraj kontrolü tam, her segmentin referans imajı var
  ❌ klip sayısı segment sayısı kadar (14 sahne → 26 klip)
  ⚠️ TEK grade + TEK gren şart (§8); yoksa kesme "iki farklı film" olur

MİMARİ 2 — KESME PROMPTUN İÇİNDE   ⭐ THE_DAWN_FRONT bunu kullanıyor
  Sahne tek bir 10 saniyelik üretimdir; kesmeler promptun MOTION
  bloğunda segment segment ve saniyesiyle yazılıdır.
  ✅ klip sayısı sahne sayısı kadar; sahne içi renk/gren uyumu doğal
  ❌ 2. ve 3. segmentin REFERANS İMAJI YOK — model onları yorumlar;
     kıyafet ve ölçek kayması riski kesmeden sonra artıyor
  ❌ model "cut"ı bindirme veya morph olarak çizebilir
```

**⛔ MİMARİ 2'NİN VAZGEÇİLMEZ KURALI — A1 çelişkisi**

```
Kontrol listesi A1: "aynı dosyada hem YASAK hem ANLATIM varsa model
YASAĞI seçer, anlatım sessizce ölür." (Tidal Hunt'ın sayacı böyle öldü.)

Kesme İSTİYORSAN "no cuts" cümlesi o promptta OLAMAZ.
  ❌ "Single unbroken take: no cuts, no transitions"
  ✅ "CUT SCHEDULE: exactly two hard cuts, at 3.0s and 7.0s, and no
      others. Each segment is one unbroken locked-off take, no camera
      movement inside it. No dissolve, no fade, no wipe, no morph and
      no speed ramp at any cut."

⭐ Aynı filmde iki negatif çekirdek bulunur: tek çekimli sahnelerde
  eski cümle, çok çekimli sahnelerde CUT SCHEDULE. Hangisinin nereye
  gittiği plan dosyasının sahne haritasında yazılı olmalı.
```

**YEDİ KURAL (ayrıntı: THE_DAWN_FRONT §0.2.1)**

```
① eksen kilidi — tehlike hep aynı yanda, kaçış hep aynı yönde
② 30°/ölçek — ardışık segmentler ya 30° ya bir ölçek kademesi farklı
③ hareket üzerinde kes — duruşta değil
④ her segment kendi kurulumunu TAM yazar (lens + mesafe + açı +
   kadrajdaki her nesne) — Mimari 2'de referans imajı olmadığı için
   bu kural pazarlık dışıdır
⑤ kesme sayısı = gerilim eğrisi — nefes sahnesi 0, doruk 2
⑥ segment süreleri sayıyla yazılı, toplam tam 10 s
⑦ kamera segment İÇİNDE sabit — hareket kesmeden gelir
```

**📊 ÖLÇÜM** Rubriğe "bu film bilinçli sahne içinde kesiyor" uyarısı ve
planlı kesme saniyeleri QA SPEC bloğunda verilir; aksi hâlde MANTIK QA
bunu Ders 1 ihlali sayar. Ayrım: **plana yazılı kesme = tasarım ·
yazılı olmayan = ihlal · bindirme/fade/morph = her durumda ihlal.**

---

## 6. ⚠️ GİZLİ GEÇİŞİN ÜÇ ŞARTI — TUTMAZSA İLLÜZYON ÇÖKER

Carter filminin başarısız gizli kesmeleri (düz 2D plakalar, perspektif
bozulması, güneşli havadan bulutluya atlama) tek bir dersi öğretir:
**perde yeterli değildir, iki tarafın da eşleşmesi gerekir.**

```
ŞART 1 — IŞIK YÖNÜ VE SERTLİĞİ AYNI
  Yıldız hâlâ kadrajın solunda 9 derecede mi? Gölgeler aynı yönde mi?
  Vakumda gölge mutlak siyah, ara tonlu bir çıktı geçişi bozar.

ŞART 2 — DOKU VE KİRLENME SEVİYESİ AYNI
  Suitteki toz haritası (Ders 42) iki klipte birebir aynı olmalı.
  Mineral/kabuk seviyesi, hasar durumu, ekipman aynı.

ŞART 3 — PERSPEKTİF HIZI AYNI
  Perde açılırken kameranın hızı, N'in sonundaki hızla aynı olmalı.
  N yavaş push-in ile bitiyorsa, N+1 aynı hızda push-in ile başlar.
  Hız değişimi, perde olsa bile "kesme" olarak hissedilir.

→ QA'ya eklenecek madde: gizli geçiş kullanılan her sınırda bu üç
  şart tek tek işaretlenir. Tutmayan geçiş DÜZ KESMEYE çevrilir —
  kötü gizlenmiş kesme, dürüst kesmeden daha kötüdür.
```

---

## 7. 💡 360° AYDINLATMA VE PRATİK IŞIKLAR ✅

```
Kamera bir öznenin etrafında döndüğünde "kamera arkası" diye bir alan
kalmaz — geleneksel film ışıklarının saklanacağı yer yoktur. Çözüm:
kadrajın İÇİNDE görünen pratik ışıklar (practicals).

Birdman bunu kulis aynalarındaki ampullerle ve tavandaki ucuz disko
ışıklarıyla çözdü; 1917 gece sahnesinde yangın ve işaret fişeklerini
ana ışık kaynağı yaptı.

✅ BİZİM İÇİN: Zaten "motivated lighting" kuralımız var, ama ORBIT
sahnelerinde bir adım daha gerekiyor:

"As the camera orbits, the lighting on the far side of the subject comes
only from [görünür kaynak: the ice giant / the beacon / the open hatch] —
there is no additional off-screen film light, and the side facing away
from every visible source stays absolutely black."

⚠️ Orbit sahnesi yazarken şu soru cevaplanmalı: kamera 180 derece
döndüğünde karakterin YENİ arkasını ne aydınlatıyor? Cevabı yoksa
sahne yeniden kurgulanmalı.
```

---

## 8. 🎨 KURGUDA YAPILANLAR

```
🎨 GREN VE RENK EŞLEME
   İki klip birleştiğinde gren yapısı ve renk sıcaklığı farkı, perde
   olsa bile hissedilir. Tüm klipler tek grade altında toplanır ve
   üstüne TEK bir gren katmanı eklenir (klip başına ayrı gren YASAK).

🎨 GEÇİŞ BİNDİRMESİ
   Gizli geçiş noktasında 2-6 karelik çapraz bindirme (cross dissolve).
   Daha uzunu "geçiş" olarak görünür, daha kısası atlar.

🎨 SES SÜREKLİLİĞİ
   Görüntü gizlense de ses kesilirse geçiş ele verir. Nefes, suit fanı
   ve müzik geçiş boyunca KESİNTİSİZ akmalı (J-cut mantığı,
   SINEMATOGRAFIK §5.3).

🎨 HIZ İNCE AYARI
   Perde anında bir klibi %2-4 hızlandırmak/yavaşlatmak, hız
   uyumsuzluğunu kurtarır. Daha fazlası hareketi yapaylaştırır.
```

---

## 9. 📚 BU HATTA GİRMEYENLER

```
Steadicam / ARRI Trinity / Stabileye / Technocrane
  → Fiziksel operatör donanımı. Bizde karşılığı: "camera weight" dili
    (SINEMATOGRAFIK §8.2) ve "no camera shake" negatifi.

Nuke kompozitleme, rotoskop, AOV/LPE geçişleri, ST map, 3D tracking
  → Gerçek çekim + CG birleştirme hattı. Bizde birleştirilecek CG yok;
    "plaka uyumu" sorunumuz renk/gren eşlemeye indirgenir (§8).

ACEScg renk yönetimi
  → Bkz. SINEMATOGRAFIK §15: bu hatta log/RAW/ACES yok.

Stand-in'li durdurmalı prova, zemin bantlama, ekip koreografisi
  → Set pratiği. Bizdeki karşılığı: beat zaman kodları ve mesafe
    sayıları (§3). Promptun beat yapısı, blocking'in yerine geçer.
```

---

## 10. 🧪 ÖNERİLEN İLK DENEY

```
TEK FİLMDE DENE, TÜM KÜTÜPHANEYE UYGULAMA.

Aday: THE REMEMBERING DUST (15 sahne, tek mekan, tek karakter, toz
      perdesi doğal olarak mevcut — gizli geçiş için ideal)

PLAN:
  S1→S2   toz perdesi (botun kaldırdığı toz)
  S2→S3   karanlık perde (eldiven lensi geçer)
  S5→S6   hareket eşleşmesi (yürüyüş devam ediyor)
  S9→S10  toz perdesi (askıdaki tabaka çöküyor)
  S11→S12 BİLİNÇLİ SERT KESME (Overview'dan sonra nefes)
  S12→S13 karanlık perde (avuç kadrajı kaplar)

ÖLÇÜT: Yorumlarda "tek çekim mi bu?" sorusu geliyorsa teknik tutmuştur.
"Geçişler garip" geliyorsa §6'daki üç şarttan biri tutmamıştır.
```

---

## 11. ✅ KARAR TABLOSU

| Kavram | Kutu | Not |
|---|---|---|
| Tekli çekim izolasyonu (sığ odak, push-in) | ✅ prompt | §1 |
| Ritim boşluğu sahneleri | ✅ prompt | Kesilmez, filmi tek çekim yapan doku |
| Mesafe/süre/hız tutarlılığı | ✅ prompt | §3 — ışınlanmayı önler |
| Omurga lens ilanı | ✅ prompt | Filme özel karar, zorunlu değil (§4) |
| Karanlık perde / toz perdesi | ✅ prompt | En güvenilir iki yöntem (§5.2) |
| Whip pan geçişi | ⚠️ koşullu | Jello riski + tonumuza yabancı |
| Işık olayı geçişi | ⚠️ koşullu | Bloom riski — "flat field" dili |
| Hareket eşleşmesi | ✅ prompt | Sadece yakın plan el/ayak |
| Bilinçli sert kesme | ✅ tasarım | Overview öncesi ve faz sınırlarında |
| Üç şart denetimi | 🎨 QA | Tutmayan geçiş düz kesmeye çevrilir (§6) |
| Orbit'te uzak taraf ışığı | ✅ prompt | Cevabı yoksa sahne yeniden kurulur (§7) |
| Gren/renk eşleme, bindirme, ses sürekliliği | 🎨 post | §8 |
| Steadicam/Trinity/Nuke/ACEScg | 📚 bilgi | §9 |

---

## 📊 İLİŞKİLİ KILAVUZLAR

| Dosya | İlişki |
|---|---|
| `LESSONS_LEARNED.md` Ders 1 | Klip İÇİ kesme yasağı — bu kılavuz klipler ARASINI kapsar |
| `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` §5 | Görünmez geçişler (match cut, J-cut) — bu kılavuz onun genişletilmiş hâli |
| `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` §10 | Rolling shutter — whip pan geçişinde zorunlu |
| `SAHNE_DEVAMLILIK_KILAVUZU.md` | Karakter/ışık çapaları — §6'daki üç şartın altyapısı |
| `1_KARE_QA_CRITIQUE_PROMPT.md` | Gizli geçiş denetimi QA'ya madde olarak eklenmeli |
| `KESINTISIZ_VIDEO_URETIM_TEKNIGI.md` | Start/end frame zinciri — faz mimarisi kullanan hatta özel (10-20 dk), bu kılavuzla çakışmaz |
