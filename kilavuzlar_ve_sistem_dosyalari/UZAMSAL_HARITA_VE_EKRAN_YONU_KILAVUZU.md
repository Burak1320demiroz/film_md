# 🗺️ UZAMSAL HARİTA VE EKRAN YÖNÜ KILAVUZU

> Karakterler gemiye koşuyor ama yanlış yöne koşuyor. Gemi doğru tarafta
> duruyor ama burnu ters yöne bakıyor. İniyor ama kıçından yanaşıyor.
> Hedef bir çekimde ekranın sağında, sonrakinde solunda. Duman bir çekimde
> sağa, sonrakinde sola savruluyor. Bu kılavuz filmin **coğrafyasını**
> planda bir kez kurar ve her prompta o coğrafyanın **ekran karşılığını**
> yazdırır.
>
> Eklenme: 09.08.2026 · **Sürüm 2: 13.08.2026** — ilk sürüm konumu ve
> hareketi kilitliyordu, **yönelimi kilitlemiyordu**; gemilerin yanlış
> yöne bakması ve ters yanaşması oradan geliyordu (§0).
> **Sürüm 3: 17.08.2026** — Black Cradle S4 iki üretim reddiyle şunu
> ölçtü: yazılı kilit ne kadar sayılabilir olursa olsun, modelin
> KOMPOZİSYON REFLEKSLERİ (ışık mıknatısı + frontal refleks) bazı
> kadrajlarda kilidi ezer; çözüm kilidi büyütmek değil, kadrajı
> refleksle hizalamaktır (§0.1 · §6.7 · §6.8 · DERS 104).
> Araştırma: MANTIK_QA ham raporları (Coğrafya kategorisi) + Third Dune
> ilk uygulaması + dış kaynaklar (§12).
> Skorlar için tek kaynak: `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md`

---

# 0. 🚨 SÜRÜM 2 — NE DEĞİŞTİ, NEDEN

İlk sürüm üretimde bir kez uygulandı (THE THIRD DUNE) ve **kısmen tuttu.**
Ne tuttuğu ve neyin dışarıda kaldığı, bu sürümün tamamını belirledi:

```
✅ TUTAN — Third Dune'un SPATIAL LOCK bloğu dört sabit tanımladı,
   dördü de 25 sahne boyunca tuttu:
     ① araç ve üçüncü tepe hep sağ üçte bir
     ② yürüyüş hep ekran solundan sağına
     ③ kum sürüklenmesi hep soldan sağa
     ④ fırtına duvarı ve güneş hep solda
   → Yani mekanizma çalışıyor: SABİTİ AÇIKÇA SAYARSAN MODEL UYUYOR.

❌ TUTMAYAN — kilidin hiç bahsetmediği şeyler serbest kaldı:
     · iki figürün birbirine göre dizilimi  → DERS 86
     · nesnenin KENDİ yönelimi (burun/omuz hattı nereye bakıyor)
     · yanaşma/iniş geometrisi (hangi uç temas ediyor)
     · çekim sınırında giriş-çıkış eşlemesi
   → Kilit neyi söylemezse model orayı yazı-turaya bırakıyor.
```

**Sürüm 2'nin tek iddiası:** konum, yönelim ve hareket **üç ayrı şeydir**
(§2 İLKE 4). İlk sürüm üçünü tek satırda karıştırdı; bu yüzden "gemi sağ
üçte birde" yazan bir prompt, burnu sola bakan **ve** sola giden bir gemi
üretebiliyordu — kilidin hiçbir cümlesi ihlal edilmemiş oluyordu.

Yeni bölümler: §4.2 yönelim kilidi · §5 araç kartı (iniş/kalkış/yanaşma) ·
§6 figür kartı (koşu/bakış/dizilim) · §7 kesme matrisi · §9 üretim sonrası
kurtarma · §10.2 video denetim defteri.

---

# 0.1 🚨 SÜRÜM 3 — İKİ RED, BİR GEÇİŞ (Black Cradle S4, 16-17.08.2026)

Sürüm 2'nin varsayımı "kilit sayılabilirse tutar" idi (§1.1 Kanıt A).
Black Cradle S4 bunun SINIRINI ölçtü — kadraj: tüm arka planı kaplayan
tek baskın ışık (şafak duvarı), neredeyse görünmez bir hedef (siyah
lander) ve yanal koşu:

```
V1 — §6.1'e UYGUN prompt (hedef-dilim + yön aynı cümlede, betik kapısı
     temiz) → RED: koşucular hedefe değil IŞIĞA koştu.
     Mekanizma: yönelim ekseni boştu; model onu kadrajın en parlak
     öğesinden doldurdu. → IŞIK MIKNATISI (§6.7)

V2 — DÖRT KANALLI kilit (hedef-dilim+yön · omuz hattı · ışığa göre
     poz · yön negatifi) → YİNE RED: model hedefi ARKA PLANA atıp
     koşucuları KAMERAYA döndürdü.
     Mekanizma: frontal/portre refleksi — dört yazılı kanala rağmen
     kompozisyonu ele geçirdi. → FRONTAL REFLEKS (§6.8)

V3 — KAÇIŞ BASAMAĞI: kamera HEDEFİN YANINA taşındı; kameraya koşu =
     hedefe koşu (nötr çekim §6.3). Hedefin gövdesi ön planda, arka
     plan yalnız ışığın → GEÇTİ (operatör onayı, 17.08.2026).
```

**Sürüm 3'ün tek iddiası:** yazılı kilidin karşısında iki taraf var —
sahnenin geometrisi VE modelin refleksleri. Refleks iki denemede
yenilmiyorsa üçüncü yeniden yazım israftır; kadraj refleksin İSTEDİĞİ
cevabın doğru cevap OLDUĞU biçimde yeniden kurulur. Yeni bölümler:
§6.7 ışık mıknatısı · §6.8 frontal refleks ve iki yenilgi kuralı.

---

# 0.2 ⚡ YEDİ SATIRLIK ÖZET — acelesi olan ajan için

```
1. Filmin haritasını PLANA bir kez çiz, kamera tarafını seç (§3).
2. Her sahne için ÜÇ AYRI kilit yaz: KONUM · YÖNELİM · HAREKET (§4).
3. Yönelim ile hareket çakışır; çakışmıyorsa (fren, yanaşma, sürüklenme)
   bunu AÇIKÇA yaz — yazmazsan model rastgele seçer (§4.2).
4. Araç iniyor/yanaşıyorsa §5 kartını doldur: hangi uç temas ediyor,
   rampa hangi tarafta, iniş sonrası poz ne. İniş pozu haritaya yazılır.
5. Çekim sınırında: sağdan çıkan soldan girer (§7).
6. Video geldikten sonra §10.2 defterini doldur; bozuk çekim yeniden
   üretilmeden önce §9'a bak — yanlış yönün bir kısmı kurguda bedavaya
   düzeliyor (yatay çevirme).
7. Kadrajda TEK BASKIN ışık varsa dört kanallı ışık-yön kilidi yaz
   (§6.7); yön iki denemede ters çıkarsa üçüncüyü yazma — kamerayı
   hedefe taşı, hareketi kameraya doğru kur (§6.8 · DERS 104).
```

---

# 1. 🎯 SORUN VE KANIT — Coğrafya neden batıyor

MANTIK_QA'nın Coğrafya kategorisi depodaki en zayıf kategorilerden biri.
Ham raporlardaki bulgular sekiz sınıfa ayrılıyor; ikisinin dersi zaten var,
**bu kılavuz kalan altısı için yazıldı:**

| # | Hata sınıfı | Örnek (film · bulgu) | Çözüm |
|---|---|---|---|
| 1 | Biyom/arazi sıçraması | Kaleida: kristal ova → çam ormanı | ✅ DERS 48 |
| 2 | Tekrar eden lokasyon kimlik değiştiriyor | Deep Pressure: portal iki gelişte iki farklı portal | ✅ DERS 58 |
| 3 | **Geçişsiz mekân sıçraması** | Blind Return: kapak → oda → roket → boru, yolculuk yok · Holding Field: S4'te giden gemi S13'te park hâlinde | 🗺️ §7 |
| 4 | **Göreli konum / yön kayması** | Starless Circle: küre ufukta alçak → gökte yüksek · Kaleida: duman sütunu çekimler arası yön değiştiriyor · Holding Field: enkaz yönü dönüyor · Stone Sky: gölge yönü tamamen dönüyor | 🗺️ §2-4 |
| 5 | **Ölçek kayması** | Cold Burn: dok kapısı geniş çekimde dev, kilitlenme yakınında oyuncak | 🗺️ §4.6 |
| 6 | **Araç yönelimi ve yanaşma geometrisi** | Last Archive: gemi düz çizgili yazıtlara iniyor, dairesel dizinin merkezinden kalkıyor · Herd: gemi park yeri keyfî değişiyor, "ışınlanan gemi" · Third Dune: kalkış çanağı gövde biçimine uymuyor | 🆕 §5 |
| 7 | **Figür dizilimi ve koşu yönü** | Third Dune: 0:10 erkek solda / 0:20 kadın solda (DERS 86) · çapasız "toward the ship" cümleleri | 🆕 §6 |
| 8 | **Aynalanmış üretim** | Second Ship: kadının yara izi ters kaşta — "seed aynalı görselle mi eğitildi?" | 🆕 §8.3 · §9 |
| 9 | **Refleks kaynaklı yön gaspı** | Black Cradle S4: koşucular hedefe değil ŞAFAĞA koştu (V1); dört kanallı kilide rağmen hedef arkaya atılıp koşu KAMERAYA döndü (V2) | 🆕 §6.7 · §6.8 · DERS 104 |

**Kök sebep tek:** promptlar mekânı her sahnede sıfırdan tarif ediyor ve
tarif **dünya-uzayında** yapılıyor ("gemiye doğru", "üsse doğru koşar").
Modelin pusulası yok; "toward the ship" cümlesinden geminin ekranın
neresinde duracağını ve karakterin hangi yöne bakacağını türetemiyor.
Her üretimde yazı-tura atıyor.

### 1.1 ⚠️ Yazılı kilit tek başına yetmiyor — iki karşıt kanıt

Bu kılavuzun en önemli iki verisi birbirinin zıddı; ikisi birlikte
okunmalı:

```
KANIT A — SAYILI SABİT TUTUYOR
  Third Dune, dört sabiti liste hâlinde ve her prompta yazdı.
  25 sahnenin 25'inde tuttu. Sabit "sayılabilir" olduğu için
  model her karede aynı kararı verdi.

KANIT B — PROZA HÂLİNDEKİ KİLİT TUTMUYOR
  Blind Return'ün planı 18 sahnede tozun SAĞ→SOL akmasını şart koştu.
  Geniş planlarda toz RÜZGÂRA KARŞI aktı.
  ⚠️ Bu bulgu MANTIK_QA'nın out-of-scope satırından geldi; gerçek
     VIDEO_QA koşusuyla doğrulanmadı (D80). Kanıt sayılırken bu
     çekince taşınır.
```

```
KANIT C — SAYILI KİLİT BİLE REFLEKSE YENİLEBİLİR         🆕 SÜRÜM 3
  Black Cradle S4: dört kanallı, tamamen ekran-uzaylı ve sayılabilir
  kilit (hedef-dilim + omuz hattı + ışığa göre poz + yön negatifi)
  İKİ denemede İKİ kez yenildi — model önce özneyi ışığa, sonra
  kameraya döndürdü. Kilit ancak modelin kompozisyon refleksiyle
  ÇATIŞMADIĞI sürece tutuyor. Refleksle çatışan kadrajda çözüm
  kilidi büyütmek değil, kadrajı değiştirmektir (§6.8).
```

Aradaki fark, kılavuzun tüm tasarımını belirliyor: **kilit ne kadar
sayılabilir ve tekil olursa o kadar tutuyor** — ama yalnız modelin
refleksleriyle çatışmadığı yerde (Kanıt C). Bu yüzden §4'te her kilit
bir SAYIYA veya SAYILABİLİR BİR DEĞERE bağlanır (üçte bir, saat, derece,
kesir) ve sıfat kullanımı yasaklanır; refleksle çatışma §6.7-6.8'de
ayrıca ele alınır.

---

# 2. 📐 BEŞ İLKE — araştırmanın özü

```
İLKE 1 — EKRAN-UZAYI ÇALIŞIR, DÜNYA-UZAYI ÇALIŞMAZ
  ❌ "runs north toward the ship"        (model pusula bilmez)
  ❌ "runs toward the ship"              (taraf belirsiz — yazı-tura)
  ✅ "ship in background right third; characters run screen-left
      to screen-right toward it"         (kamera-göreli = güvenilir)

İLKE 2 — AKSİYON EKSENİ PROMPTTAN ÖNCE ÇİZİLİR (180° kuralı)
  Kaynak (kamp) ile hedef (gemi) arasına hayali bir çizgi çek.
  Kamera FİLM BOYUNCA bu çizginin TEK tarafında kalır.
  Sonuç: hedef her çekimde AYNI ekran tarafında görünür, hareket
  hep aynı yönde akar. Kamera çizgiyi atlarsa izleyici için
  karakterler "geri dönüyor" gibi görünür.

İLKE 3 — HARİTA PLANDA DURUR, PROMPTA ÇEVİRİSİ GİRER
  Kuşbakışı harita filme bir kez, PLAN'a çizilir (§3).
  Prompta haritanın kendisi DEĞİL, o çekim için ekran-uzayı
  çevirisi girer (§4). Kural ③ (self-contained) böyle korunur.

İLKE 4 — KONUM ≠ YÖNELİM ≠ HAREKET          ⭐ SÜRÜM 2'NİN ÇEKİRDEĞİ
  Bir nesnenin ekran yönü ÜÇ bağımsız bilgidir:
     KONUM    nesne kadrajın neresinde duruyor
     YÖNELİM  nesnenin burnu/yüzü/omuz hattı nereye bakıyor
     HAREKET  nesne hangi yöne gidiyor
  Üçü birbirinden türetilemez. "Gemi sağ üçte birde" cümlesi
  geminin hangi yöne baktığını SÖYLEMEZ; model boşluğu doldurur.
  Sağ üçte birde durup burnu sola bakan ve sola giden bir gemi,
  ilk sürümün hiçbir kuralını ihlal etmiyordu.
  ⛔ Kilidin üç satırı da yazılmadan sahne üretime gitmez.

İLKE 5 — SAYI YAZ, SIFAT YAZMA
  AGENTS.md §8'in ölçülmüş gerçeği: tarif kilitleri işe yaramadı,
  sayısal kilitler yaradı. Yön de bir sayıdır:
     ❌ "angled slightly toward the camera"
     ✅ "hull heading 10 o'clock; camera sees the port flank"
     ❌ "she looks off to the side"
     ✅ "shoulder line 60 degrees to screen-right, gaze 15 degrees
         further right than the shoulders"
```

---

# 3. 🗺️ KUŞBAKIŞI HARİTA — plan katmanı

**Nereye:** film PLAN dosyasına, RECURRING ENTITY kartından (Ders 58)
hemen sonra, sahne haritasından önce. **Ne zaman zorunlu:** filmde
birden fazla sahnede görünen sabit bir hedef (gemi, kapı, sur, kule)
ve ona doğru hareket varsa. Tek statik çekimlik shorts'ta gerekmez.

### 3.1 Şablon

```
## 🗺️ SPATIAL MAP — kuşbakışı (SADECE PLANDA DURUR, PROMPTA GİRMEZ)

            rüzgâr/toz sürüklenmesi →→
   ┌──────────────────────────────────────┐
   │                          ▲ GEMİ      │
   │                         (burun 10,   │
   │                          rampa kampa │
   │                          bakar)      │
   │           ···· koşu hattı ····       │
   │    ● KAMP                            │
   │  ☀ güneş: alçak, kamp tarafında      │
   └──────────────────────────────────────┘
        ▲ KAMERA — eksenin ALT yarısı, film boyunca

AKSİYON EKSENİ : KAMP → GEMİ hattı
KAMERA TARAFI  : eksenin ALT yarısı — FİLM BOYUNCA, istisnasız
EKRAN SONUCU   : gemi HEP ekran SAĞINDA · kampa dönüş HEP sağdan sola
YÖN TAŞIYICILARI (her çekimde aynı): rüzgâr/toz soldan sağa ·
                 duman sütunu sağa yatık · güneş ekran solunda alçak
```

### 3.2 Harita kartı — sabit yer işaretleri

Haritadaki her sabit nesne için bir satır. Bu tablo RECURRING ENTITY
kartının (Ders 58) coğrafya uzantısıdır — kimlik orada, **konum ve
yönelim burada:**

| Yer işareti | Konum (ekran tarafı) | **Yönelim (saat)** | Ölçek çapası |
|---|---|---|---|
| Gemi | background-right | burun 10 · rampa 7 (kampa bakar) | S1'de kare boyunun 1/8'i |
| Kamp | foreground-left | girişler 2 (gemiye bakar) | çadır boyu = insan boyu × 1.5 |
| Duman sütunu | background-center | sağa yatık | — |

**KURAL:** Kamera tarafı seçildikten sonra bu iki sütun ASLA değişmez.
"Gemi sağda" yazan filmde geminin solda göründüğü tek bir prompt bile
eksen ihlalidir — o prompt yeniden yazılır, harita değişmez. Yönelim
sütunu için de aynısı geçerli: **iniş pozu bir kez kararlaştırıldıktan
sonra filmin geri kalanı onu devralır** (§5.5).

### 3.3 ⭐ YÖN DEFTERİ — sahne × üç eksen

Haritanın sahneye inmiş hâli. Plana, sahne haritasının yanına yazılır;
her promptun SPATIAL LOCK bloğu bu satırdan türetilir. Üç sütunun
üçü de dolmadan o sahnenin promptu yazılmaz.

| Sahne | KONUM (hedef) | YÖNELİM (özne) | HAREKET (özne) | Taşıyıcı | Ölçek |
|---|---|---|---|---|---|
| S3 | gemi sağ üçte bir | figürler omuz hattı 65° sağa | ekran solundan sağına | toz sola→sağa | gemi 1/8 |
| S5 | gemi sağ üçte bir | figürler omuz hattı 70° sağa | ekran solundan sağına | toz sola→sağa | gemi 1/3 |
| S7 | rampa sağ yarı | figürler omuz hattı 80° sağa | ekran solundan sağına | toz sola→sağa | rampa 1/2 |
| S8 | kapak sağ üçte bir | figür sırtı kameraya (12) | kameradan uzağa — NÖTR | toz sola→sağa | kapak 2/3 |

**Defterin işi tek:** bir sütunda ters yönde bir hücre görürsen, o
sahne üretilmeden önce ya gerekçesi yazılır ya düzeltilir. Göz taraması
saniyeler sürüyor; aynı hatayı videoda bulmak bir yeniden üretim demek.

---

# 4. 🔒 ÜÇ EKSENLİ KİLİT — prompt katmanı

Her image ve video prompta, haritadan **o çekim için** türetilmiş
ekran-uzayı bloğu girer. Promptlar uzar; sorun değil — uzunluk bandı
aşılırsa önce başka bölümlerden kısalt, bu bloktan kısaltma.

### 4.0 ⭐ KİLİT KADEMELERİ — hangisine ne kadar güveniyoruz

Depoda ölçülmüş olanla olmayanı karıştırmamak için üç kademe var. Her
sahne **en az kademe 1 + kademe 2** yazar; kademe 3 opsiyoneldir.

```
KADEME 1 — ÜÇTE BİR DİLİ                       ✅ KANITLI
   "in the right third of the frame"
   Third Dune'da 25/25 sahnede tuttu. Konum kilidinin omurgası.

KADEME 2 — SAAT KADRANI + DERECE                🟡 DENENECEK
   "hull heading 10 o'clock" · "shoulder line 65 degrees to
   screen-right". Depoda hiç uygulanmadı; bu sürümün asıl bahsi.
   §11 test protokolü bunu ölçer.

KADEME 3 — KESİRLİ KOORDİNAT                    🔬 DENEYSEL
   "the nose sits at x=0.72, y=0.55 of the frame"
   Hiç denenmedi, modelin uyup uymadığı bilinmiyor. Kritik tek
   karede (master establishing) denenir, tüm filme yayılmaz.
   Uyulmazsa kademe 1-2 zaten ayakta kalır — bu yüzden eklemek
   risksiz, güvenmek riskli.
```

⚠️ Bir sahnede kademe 3 yazıp kademe 1'i atlama. Kademeler birbirinin
yedeğidir: model ince olanı ıskalarsa kaba olan tutar.

### 4.1 KONUM kilidi — nesne kadrajın neresinde

| Haritadaki bilgi | Prompta yazılacak biçim | Kademe |
|---|---|---|
| Hedefin yatay dilimi | `in the background right third of the frame` | 1 |
| Hedefin dikey yeri | `its base on the horizon line, upper half of frame` | 1 |
| Öznenin dilimi | `the two figures occupy the lower left quarter` | 1 |
| Kesirli koordinat | `the ramp foot sits at x=0.68, y=0.72 of the frame` | 3 |

### 4.2 ⭐ YÖNELİM kilidi — nesne nereye bakıyor

**Sürüm 2'nin çekirdek eklentisi. "Gemi yanlış yöne bakıyor"un panzehiri.**

Kadraj saati, kamera tepeden bakıyormuş gibi tanımlanır:

```
              12  (kameradan uzağa, arka plana)
         11 ·           · 1
      10 ·                 · 2
   9 (ekran soluna)  ●  3 (ekran sağına)
       8 ·                 · 4
          7 ·           · 5
               6  (doğrudan kameraya)
```

**Kadranın en kullanışlı sonucu — hangi yanı gördüğümüz otomatik belli:**

| Yönelim | Ekran karşılığı | Kameranın gördüğü yan | Prompt cümlesi |
|---|---|---|---|
| 12 | kameradan uzağa | kıç / sırt | `heading directly away from camera, stern toward the lens` |
| 1-2 | uzağa + sağa | kıç + **sancak** | `three-quarter rear view, starboard flank toward camera` |
| 3 | ekran sağına, tam profil | **sancak** | `full profile, nose to screen-right, starboard flank fills the frame` |
| 4-5 | kameraya + sağa | burun + **sancak** | `three-quarter front, nose toward screen-right, starboard flank visible` |
| 6 | doğrudan kameraya | burun / yüz | `nose pointed straight at the lens` |
| 7-8 | kameraya + sola | burun + **iskele** | `three-quarter front, nose toward screen-left, port flank visible` |
| 9 | ekran soluna, tam profil | **iskele** | `full profile, nose to screen-left, port flank fills the frame` |
| 10-11 | uzağa + sola | kıç + **iskele** | `three-quarter rear, port flank toward camera` |

> **Kural (ezberlenecek):** ekran SAĞINA bakan her yönelimde kamera
> **sancağı** (sağ yanı) görür; ekran SOLUNA bakan her yönelimde
> **iskeleyi** (sol yanı) görür. Promptta "starboard" yazıp gemiyi sola
> bakar hâlde tarif ediyorsan kilit kendi kendisiyle çelişiyordur ve
> model ikisinden birini seçer.

**İnsan için karşılığı** — omuz hattı derecesiyle:

```
0°    yüz tam kameraya            (kadran 6)
45°   dörtte üç, ekran sağına     (kadran 4-5)
90°   tam profil, ekran sağına    (kadran 3)
135°  dörtte üç sırt, sağa        (kadran 1-2)
180°  sırt tam kameraya           (kadran 12)
negatif dereceler aynısının ekran SOLU karşılığıdır (-90° = kadran 9)
```

### 4.2.1 ⛔ UYUM KURALI — yönelim ile hareket çakışır

**Varsayılan:** bir nesne baktığı yöne gider. Yönelim 3 ise hareket
ekran sağınadır. Bu cümle promptta AÇIKÇA kapatılır:

```
The hull heading and the direction of travel are the same; the ship
never moves stern-first.
```

**İstisnalar — biri geçerliyse gerekçesi promptta YAZILIR:**

| Durum | Yönelim ↔ hareket ilişkisi | Prompt cümlesi |
|---|---|---|
| Fren / retro ateşleme | ters | `hull heading 3 o'clock, still drifting screen-right but slowing; retro plumes fire screen-right, into the direction of travel` |
| Yanaşma (son metreler) | dik / yan kayma | `nose holds 12 o'clock while the hull translates screen-left at walking pace` |
| Sürüklenme, kontrol kaybı | rastgele ama SABİT | `hull yaws slowly from 1 o'clock to 2 o'clock while the whole mass keeps sliding screen-right` |
| Geri geri gitme | ters, kasıtlı | `the vehicle reverses stern-first to screen-left, nose still 3 o'clock` |
| İniş (dikey bileşen) | yönelim yatay, hareket dikey | `heading fixed at 10 o'clock throughout the descent; the hull only loses altitude, it does not rotate` |

⚠️ **Bu tablonun sebebi doğrudan senin şikâyetin:** yönelim ile hareketin
ilişkisi yazılmadığında model ikisini bağımsız seçiyor ve gemi kıçından
yanaşıyor, burnu geriye bakarak iniyor. İstisna yoksa uyum cümlesini yaz;
istisna varsa hangisi olduğunu yaz. Üçüncü seçenek yok.

### 4.3 HAREKET kilidi — nesne hangi yöne gidiyor

| Haritadaki bilgi | Prompta yazılacak biçim | Kademe |
|---|---|---|
| Yatay hareket | `run from screen-left to screen-right` | 1 |
| Çapraz hareket | `moves diagonally from background-left toward foreground-right` | 1 |
| Kameraya/kameradan | `walks directly away from the lens` (NÖTR — §7 kural 6) | 1 |
| Hız çapası | `covering roughly one third of the frame width every 4 seconds` | 2 |
| Yükseklik | `losing 15 metres of altitude across the shot` | 2 |

### 4.4 Kelime dağarcığı ve tuzaklar

**Tek sözlük kullan.** `screen-left` / `screen-right` bu deponun
standardıdır. `frame-left`, `camera-left` ve `screen-left` aynı şeyi
söyler; üçünü aynı promptta karıştırmak modele üç ayrı sistem varmış
izlenimi verir.

⚠️ **Yasak kelimeler (prompt gövdesinde):**

```
north / south / east / west            → modelin pusulası yok
çapasız toward / away                  → "toward the ship" ancak geminin
                                          ekran konumu AYNI CÜMLEDE varsa
behind the mountain (kamerasız tarif)  → kime göre arkada?
to his left / on the ship's left       → ⭐ NESNE-GÖRELİ TARAF, en sinsi
                                          tuzak: karakterin solu izleyicinin
                                          sağıdır. Her zaman ekran-göreli yaz.
port / starboard  (tek başına)         → nesne-göreli; ekran tarafıyla
                                          eşleştirilmeden kullanılmaz (§4.2)
```

### 4.5 IMAGE PROMPT bloğu — şablon + dolu örnek

V2 iskeletinde **CAMERA ile LIGHTING arasına** girer
(`IMAGE_VIDEO_PROMPT_TEMPLATES.md`). Blok artık **üç satırlıdır** —
konum, yönelim, hareket ayrı ayrı:

```
SPATIAL LOCK:
[KONUM]    Hedef nesne + ekran dilimi. Özne + ekran dilimi.
[YÖNELİM]  Hedefin saati + kameranın gördüğü yan. Öznenin omuz hattı
           derecesi + bakış yönü.
[HAREKET]  Öznenin ekran-uzayında hareket yönü + uyum/istisna cümlesi.
[ÖLÇEK]    Kesir. [TAŞIYICI] Rüzgâr/toz/duman yönü. [EKSEN] Eksen cümlesi.
```

Dolu örnek — "insanlar gemiye koşuyor" sahnesi, geniş çekim:

```
SPATIAL LOCK:
The ship sits in the background right third of the frame and the camp
tents occupy the foreground left corner. The hull heading is 10
o'clock, so the camera sees the port flank and the port landing strut;
the boarding ramp is lowered on the port side, its foot pointing toward
the camera. Three crew members run from screen-left to screen-right
toward that ramp, shoulder lines 70 degrees to screen-right and gaze 15
degrees further right than the shoulders, never turning to face the
camera. Their direction of travel matches the way they face; nobody
runs backwards or sideways. The ship spans approximately 1/8 of frame
height at this distance. Wind-blown dust drifts screen-left to
screen-right across every part of the frame. Camera stays on the same
side of the action line as every other shot in this film — the ship
never appears on the left side of the frame and its heading never
changes between shots.
```

> ⚠️ Ders 45: blok içinde köşeli parantezli etiket ve karakter adı
> KULLANMA — düz cümle yaz. `SPATIAL LOCK:` başlığının kendisi
> `CAMERA:`/`SCENE:` ile aynı risk sınıfındadır ve şimdilik korunur.
> Yukarıdaki şablondaki `[KONUM]` etiketleri **plan içindir, prompta
> yazılmaz** — dolu örnekte hiçbiri yok.

### 4.6 Ölçek kilidi — yaklaşma dizisi (Cold Burn panzehiri)

Hedefe yaklaşan sahne dizisinde hedefin kare içindeki boyu **kesir
olarak yazılır ve her çekimde bir öncekinden BÜYÜK olur:**

```
S3 (geniş, 120 m)   : ship spans 1/8 of frame height
S5 (orta, 40 m)     : ship spans 1/3 of frame height
S7 (rampa, 8 m)     : ramp and hull fill the right half of frame
S8 (temas, 2 m)     : hatch frame spans 2/3 of frame height
```

Kesirler PLAN'da sahne haritasının yanına yazılır; prompt kendi
kesrini SPATIAL LOCK içinde taşır. Dizi bir yerde küçülüyorsa ya
kamera geri çekiliyordur (bunu promptta açıkça söyle) ya da hata var.

⚠️ **Ölçek büyürken yönelim sabit kalır.** Yaklaşma dizisinin en sık
hatası, yakın çekimde geminin bir anda başka açıdan görünmesidir —
kesir büyüdü ama saat değişti. Dizinin her sahnesi aynı saati taşır;
saat değişecekse arada onu gösteren bir çekim olur.

### 4.7 VIDEO PROMPT — beat'lere yön yazılır

MOTION kırılımındaki her harekete ekran yönü eklenir; blok sonuna tek
satırlık eksen + yönelim hatırlatması girer:

```
MOTION (10 seconds, 32mm, fixed lockoff at 60 meters):
0s — Three crew members burst from the camp tents at frame-left,
     beginning their run toward the ship at background right.
4s — They cross the midground left-to-right, dust kicking up and
     drifting screen-right with the wind.
8s — The lead figure reaches the lowered ramp at frame-right,
     boots hitting metal.
10s — The other two close the gap, still moving left-to-right. No cuts.
Ship remains in the right third throughout and its heading stays 10
o'clock; no direction reversal, no rotation of the hull.
[PHYSICS + NEGATIVE bibles apply throughout]
```

⚠️ **Video promptunun kendi tuzağı:** bir beat "döner" derse model
tüm sahneyi döndürebilir. Dönüş varsa BAŞLANGIÇ ve BİTİŞ saatini
ikisini birden yaz: `the hull yaws from 10 o'clock to 12 o'clock
between 4s and 8s and holds there`.

### 4.8 NEGATIVE eklentisi

Coğrafyalı sahnelerin negatif bloğuna şu satır eklenir:

```
mirrored composition, direction reversal mid-scene, target switching
sides of frame, landmark teleportation, background relocation,
crossing the action line, hull rotating between shots, vehicle moving
stern-first, characters running backwards relative to the way they
face, figures swapping left-right order
```

Kadrajda TEK BASKIN ışık kaynağı varsa şu üçü de eklenir [DERS 104]:

```
no one runs or turns toward the dominant light source, no figure
turns to face the camera while moving laterally, the target never
drops into the background behind the moving subject
```

⚠️ `vehicle moving stern-first` satırı HAZIR LİSTEDİR, körlemesine
kopyalanmaz: kıç önde hareketin TASARIM olduğu filmde (Black Cradle —
geri geri yanaşma) bu satır atılır ve yerine tersi yazılır:
`never nose-first — the [canopy/bow] end never faces the target`.

---

# 5. 🚀 ARAÇ KARTI — iniş, kalkış, yanaşma

> **Neden ayrı bölüm:** insan iki eksenli bir nesnedir (nereye bakıyor,
> nereye gidiyor). Araç altı serbestlik derecesine sahiptir ve her biri
> ayrı bozulabilir — hangi uç önde, hangi yan kameraya dönük, hangi uç
> temas ediyor, kapı nerede, hangi yönde yavaşlıyor, indikten sonra
> hangi pozda duruyor. Depodaki araçlı filmlerin Coğrafya skorları bu
> yüzden kalabalık: Herd, Holding Field, Last Archive, Third Dune.
> 🆕 Yanaşma SEKANSININ vuruş/kompozisyon reçetesi ve ses/dramaturji
> kalıbı ayrı dosyadadır: `YANASMA_VE_KENETLENME_KILAVUZU.md`
> (17.08.2026) — bu bölüm geometrinin kendisini kilitler, o dosya
> hangi kadrajın güvenli olduğunu söyler.

### 5.1 ⛔ BEŞ SORU — araç hareket ediyorsa cevapsız bırakılamaz

```
① HANGİ UÇ ÖNDE?        burun mu, kıç mı, yan mı gidiyor
② HANGİ UÇ TEMAS EDER?  inişte ayaklar, yanaşmada hangi halka/kapak
③ KORİDOR NEREDEN?      geliş yönü saat + iniş açısı derece
④ NASIL YAVAŞLIYOR?     retro yönü, ters itki, alev/toz hangi yöne
⑤ KAPI NEREDE AÇILIR?   rampa/kapak hangi yanda, çıkan kişi hangi
                        ekran yönüne adım atar
```

Beşinin cevabı **plana**, harita kartının yönelim sütununa yazılır;
prompta o sahnenin karşılığı iner. Cevapsız bırakılan her soru bir
yazı-turadır ve dizinin ilerleyen sahnelerinde çelişki olarak çıkar.

### 5.2 İNİŞ DİZİSİ — dört sahnelik sayısal şablon

```
S1 YAKLAŞMA    konum: sağ üst çeyrek, ufkun üstünde
               yönelim: burun 10 · kamera iskeleyi görür
               hareket: ekran sağından soluna + alçalma
               ölçek: gövde kare boyunun 1/10'u
               ⚠️ burun 10, hareket sola: UYUMLU (10 = sol-uzak bileşen)

S2 SON YAKLAŞMA konum: sağ üçte bir, ufka değiyor
               yönelim: burun 10 — DEĞİŞMEZ
               hareket: yatay bileşen durur, yalnız alçalır
               fren: retro alevleri AŞAĞI ve İLERİ, yani hareketin içine
               ölçek: 1/4

S3 TEMAS       konum: sağ üçte bir, alt yarı
               yönelim: burun 10 — DEĞİŞMEZ
               hareket: yok; ayaklar zemine oturur
               toz: temas noktasından DIŞA, rüzgâr yönünde daha uzağa
               ölçek: 1/2

S4 İNİŞ SONRASI konum: sağ üçte bir  ← ARTIK SABİT, HARİTAYA YAZILIR
               yönelim: burun 10     ← ARTIK SABİT, FİLMİN SONUNA KADAR
               rampa: iskele yanında, ayağı kameraya dönük
               ölçek: sahnenin mesafesine göre, ama taraf ve saat asla
```

**S4'ün iki satırı bu bölümün en önemli çıktısıdır.** Herd'ün "gemi park
yeri keyfî değişiyor" ve Holding Field'ın "S4'te giden gemi S13'te park
hâlinde" bulguları, iniş pozunun hiç kaydedilmemiş olmasından doğuyor.
İniş bittiği anda gemi bir YER İŞARETİDİR ve harita kartına (§3.2) taşınır.

### 5.3 YANAŞMA / KENETLENME — uzay ve liman

Yanaşmanın inişten farkı: **iki nesne birden konumlanır** ve temas
noktaları eşleşmek zorundadır.

```
SABİT NESNE (istasyon/iskele)
   konum   : sol üçte bir, kadrajın dikeyini dolduruyor
   yönelim : kenetlenme halkası ekran SAĞINA bakar (kadran 3)
   ölçek   : kare boyunun 3/4'ü

GELEN ARAÇ
   konum   : sağdan girer, sağ üçte birde başlar
   yönelim : burun 9 — halkaya BAKAR (halka 3'e bakıyorsa araç 9'a bakar)
   hareket : ekran sağından soluna, yavaşlayarak
   fren    : alevler ekran SOLUNA — yani gidilen yöne (§5.3.1)
   prompt  : "the ship drifts screen-left and slows; its forward retro
              nozzles vent screen-left, ahead of the hull"
```

### 5.3.1 ⛔ FREN YÖNÜ — bu kılavuzun en kolay ters yazılan satırı

```
EZBER:  Alev, GİDİLEN yöne püskürür. Gövde ters yöne itilir.

  Sola giden araç yavaşlıyor  → alev SOLA çıkar (gövde sağa itilir)
  Sağa giden araç yavaşlıyor  → alev SAĞA çıkar (gövde sola itilir)
  Sola giden araç HIZLANIYOR  → alev SAĞA çıkar (arka motorlar)

⚠️ Yavaşlayan araçta alev ÖN uçtan, hızlanan araçta ARKA uçtan çıkar.
   Promptta hangi uçtan çıktığı da yazılır: "forward retro nozzles" /
   "main engines at the stern". Yazılmazsa model alevi hep arkaya koyar
   ve yanaşan gemi hızlanıyormuş gibi okunur.
```

**Temas eşleşmesi — kenetlenme anının tek cümlesi:**

```
The ship's nose ring meets the station's docking collar; the two
circular faces are parallel and both lie on a screen-left to
screen-right axis. Contact happens at the left third of the frame,
and neither body rotates during the last five metres.
```

### 5.4 KALKIŞ — inişin tersi değil, aynası

Kalkış promptu yazılırken en sık hata, iniş pozunun unutulmasıdır:
gemi başka bir saatte kalkar ve izleyici "başka gemi" okur.

```
KALKIŞ KURALI
 · Kalkışın 0s karesi, iniş sonrası pozun BİREBİR aynısıdır
   (konum + saat + rampa tarafı).
 · Yükselirken saat DEĞİŞMEZ; dönme varsa yükselme bittikten sonra
   ayrı bir beat'te ve iki saati birden yazarak olur.
 · Zeminde bıraktığı iz gövdenin biçimine ve ayak düzenine uyar.
   ⚠️ Third Dune kanıtı: kalkışta ortaya çıkan çukur, gövdenin
      biçimine uymayan derin bir çarpma krateri olarak üretildi.
      Promptta izin BİÇİMİ ve DERİNLİĞİ sayıyla yazılır:
      "four oval pads leave four shallow depressions 8 centimetres
       deep, arranged in the same rectangle as the landing feet;
       no crater, no circular pit"
```

### 5.5 İNİŞ SONRASI POZ DEVRİ — sahne sınırında

```
Bir araç yere indiği andan itibaren SABİT YER İŞARETİDİR.
 □ Konumu ve saati harita kartına yazılır (§3.2)
 □ Sonraki HER sahnenin SPATIAL LOCK'u aynı iki değeri tekrarlar
 □ Araç yeniden hareket edene kadar bu değerler tartışılmaz
 □ Araç kadrajda yoksa bile arka planda görünüyorsa aynı taraftadır
```

### 5.6 ARAÇ NEGATİFİ

Araçlı sahnelerin negatif bloğuna eklenir:

```
no stern-first motion, no hull rotation between shots, no landing gear
appearing on the wrong side, no ramp switching flanks, no exhaust
plume pointing against the direction of travel, no second identical
vehicle, no crater or impact pit under the landing feet
```

⚠️ İLK SATIR TASARIMA GÖRE TERSLENİR: araç bilerek kıç önde gidiyorsa
(retrograd fren, geri geri yanaşma — Black Cradle) `no stern-first
motion` yerine şu yazılır: `never nose-first — the notched tail and
dark engine nozzles LEAD; the canopy nose trails, pointing away from
the target`. Hangi ucun önde olduğu her promptta cümleyle söylenir
(§5.1 ①); söylenmezse model burnu çevirir.

---

# 6. 🏃 FİGÜR KARTI — koşu, yürüyüş, bakış

### 6.1 Koşu yönü hedeften TÜRETİLİR, hedefe atıfla yazılmaz

Bu, "insanlar yanlış yöne koşuyor"un tek cümlelik panzehiridir:

```
❌ "the crew run toward the ship"
     → geminin nerede olduğu bu cümlede yok; model gemiyi de koşuyu da
       serbest seçer ve ikisi tutmayabilir.

✅ "the ship stands in the right third of the frame; the crew run from
    screen-left to screen-right toward it"
     → hedefin konumu ve koşunun yönü AYNI CÜMLEDE; ikisi çelişemez.
```

**Kural:** `toward` kelimesi promptta ancak hedefin ekran dilimi aynı
cümlede yazılıysa geçebilir. Bu kural §10.1 kontrol listesinde ve
`prompt_kontrol.py` kapısında ayrıca aranır.

⚠️ **SINIR [Sürüm 3]:** bu cümle GEREKLİ ama kadrajda tek baskın ışık
kaynağı varsa YETERLİ DEĞİL — Black Cradle S4'te birebir bu kurala
uyan prompt reddedildi (koşucular ışığa döndü). O kadrajlarda §6.7'nin
dört kanalı birden yazılır; betik kapısı bu sınıfı GÖREMEZ (yönelim
eksenini aramaz), denetim insan gözüyle yapılır.

### 6.2 Gövde yönelimi — omuz hattı derecesi

Koşan bir figürün üç ayrı yönü vardır ve üçü ayrışabilir:

```
OMUZ HATTI   gövdenin baktığı yön     → hareket yönüyle çakışır
BAŞ          omuzdan en fazla 30° sapar
BAKIŞ        baştan en fazla 15° sapar
```

Prompt cümlesi:

```
Shoulder lines 70 degrees to screen-right, matching the direction of
travel; heads turned no more than 30 degrees off the shoulders, gaze 15
degrees further right. No runner faces the camera while moving
screen-right.
```

⚠️ **Son cümle önemli:** modeller koşan figürü kameraya döndürmeyi
sever (portre refleksi). Yasaklanmazsa figür sağa koşarken yüzü
kameraya bakar ve izleyici yönü kaybeder.

### 6.3 NÖTR ÇEKİMLER — kameraya doğru / kameradan uzağa koşu

Kadran 6 (kameraya) ve 12 (kameradan uzağa) **yönsüzdür.** Bu, kılavuzun
en kullanışlı aracıdır:

```
NÖTR ÇEKİM NE İŞE YARAR
 · Eksen atlaması gerekiyorsa köprü olur (§7 kural 1)
 · İki farklı yöne akan sahne dizisini birbirine bağlar
 · Yönü belirsiz kalan bir çekimi kurtarır — "hangi tarafa gidiyordu"
   sorusu sorulmaz
 · 🆕 KAÇIŞ BASAMAĞIDIR [Sürüm 3 · DERS 104]: yanal hareket modelin
   refleksine iki kez yenildiyse kamera hedefe taşınır ve hareket
   kameraya doğru kurulur — frontal refleks doğru cevaba dönüşür (§6.8)

NÖTR ÇEKİMİN BEDELİ
 · Momentum düşer; art arda iki nötr çekim koşuyu durgunlaştırır
 · Bir dizide en fazla BİR nötr çekim, o da geçiş noktasında
```

### 6.4 İKİ VE DAHA FAZLA FİGÜR — dizilim kilidi (DERS 86)

Ekran yönü kilidi tek özneli filmler için yazıldı; özne bir kişiyken
"ekran yönü" ile "dizilim" aynı şeydir, iki kişide ayrışır.

```
The ICE-BLUE figure stays on the screen-left side of the pair and the
DEEP-VIOLET figure on the screen-right side in every shot; their
left-right order never swaps.
```

- Kadrajın öznesi tek kişiyse (detay, tek kol, tek figür) cümle düşer.
- Sıralamanın bilinçli değiştiği sahne varsa — biri öne geçer, biri
  geride kalır — o sahnede cümle yerine değişimi TARİF ET; kilit
  sessizce bırakılmaz, açıkça devredilir.
- Üç ve daha fazla figürde sıralama soldan sağa **tam sayılır:**
  `from screen-left to screen-right the order is ICE-BLUE, DEEP-VIOLET,
  RUST-ORANGE, and this order never changes`.

### 6.5 BAKIŞ VE KARŞI AÇI

İki karakter konuşuyorsa bakışları **birbirini bulmak zorundadır:**

```
KURAL      Solda duran sağa bakar, sağda duran sola bakar.
           İkisi de aynı yöne bakıyorsa izleyici üçüncü bir kişi arar.

PROMPT     "the figure on the screen-left looks screen-right and
            slightly up; the figure on the screen-right looks
            screen-left and slightly down; their eye lines meet"

KARŞI AÇI  Karşı açı çekiminde HER ŞEY aynalanır: solda duran sağa
           geçer. Bu bir eksen ihlali DEĞİLDİR, karşı açının tanımıdır —
           yeter ki kamera eksenin aynı tarafında kalsın.
           ⚠️ Karşı açı promptunda taraf değişimini AÇIKÇA yaz, yoksa
              model önceki çekimin dizilimini kopyalar ve iki kişi de
              aynı tarafa bakar.
```

### 6.6 Dolu örnek — figürlü sahne

```
SPATIAL LOCK:
The lowered ramp fills the right half of the frame and its foot rests
at the bottom right corner. Two figures approach it from the left,
moving screen-left to screen-right, shoulder lines 80 degrees to
screen-right and matching their direction of travel. From screen-left
to screen-right the order is the taller lean figure then the shorter
stocky one, and this order does not change. Neither turns to face the
camera while moving. The hull heading stays 10 o'clock so the camera
sees the port flank behind the ramp. Sand drifts screen-left to
screen-right across the whole frame.
```

### 6.7 🆕 IŞIK MIKNATISI — baskın ışık kaynağı yön kilidini eziyor [DERS 104]

> **Ne zaman geçerli:** kadrajda TEK BASKIN ışık kaynağı (şafak/alacakaranlık
> hattı, patlama, projektör, yangın parıltısı) + hareketli özne varsa —
> özellikle hedef görsel olarak silikse (karanlık, siyah-üstü-siyah, uzak).

```
ÖLÇÜLEN MEKANİZMA (Black Cradle S4-V1, 16.08.2026):
Model, yönelimi yazılmamış hareketli özneyi kadrajın en parlak ve en
anlamlı öğesine DÖNDÜRÜYOR. İki eğitim refleksi üst üste biner:
 ① portre refleksi — koşan figürü ışığa/kameraya çevirme (§6.2 uyarısı)
 ② "ışığa/gün doğumuna koşan insan" klişesi
Hedef silikse (siyah gövde, küçük ışık havuzu) mıknatıs rakipsizdir:
model "bu karede önemli olan ışıktır, özne ona koşuyordur" der.
```

**DÖRT KANALLI IŞIK-YÖN KİLİDİ** — dördü birden yazılır, hiçbiri
diğerinin yerine geçmez:

```
① HEDEF-DİLİM + YÖN (§6.1 — aynı cümlede):
   "the lander stands at frame right; they run from screen-left to
    screen-right toward it"
② GÖVDE YÖNELİMİ (§6.2 — omuz hattı):
   "shoulder lines square to screen-right, matching the direction of
    travel; no runner faces the camera or turns back"
③ IŞIĞA GÖRE POZ — mıknatısı etkisiz kılan kanal:
   "their BACKS are to the dawn light — the warm band rims their back
    silhouettes; their faces and the ground ahead are lit only by
    their own lamps"
   → ışık-gölge kanıtı yönle AYNI şeyi söyler; model rim'i sırta
     çizmek için özneyi ışıktan uzağa çevirmek ZORUNDADIR
④ YÖN NEGATİFİ (§4.8 ek üçlüsü):
   "no one runs or turns toward the dominant light source; no
    direction reversal; no mirrored composition"
```

⚠️ **Dürüst kayıt:** bu dört kanal Black Cradle S4-V2'de YİNE yenildi —
ama farklı bir refleks tarafından (frontal refleks, §6.8). Kanalların
işlevi mıknatısı kapatmaktır; frontal refleksi kapatmaz. İki savunma
birlikte okunur: §6.7 promptun içinde savaşır, §6.8 savaşın gereksiz
olduğu kadrajı kurar.

### 6.8 🆕 FRONTAL REFLEKS VE İKİ YENİLGİ KURALI — kamerayı hedefe taşı [DERS 104]

```
ÖLÇÜLEN MEKANİZMA (Black Cradle S4-V2, 16.08.2026):
Dört kanallı kilide rağmen model kompozisyonu ele geçirdi: hedefi
ARKA PLANA attı, koşucuları KAMERAYA döndürdü. Yanal (profil) koşu,
baskın-ışıklı kadrajda iki denemede iki kez tutmadı. Model frontal
kompozisyon İSTİYOR — ve bunu her kilitten daha güçlü istiyor.
```

**İKİ YENİLGİ KURALI:**

```
Dört kanallı kilit AYNI sahnede İKİ kez yenilirse üçüncü yeniden
yazım DENENMEZ — para israfıdır. Bunun yerine kadraj, refleksin
istediği cevabın DOĞRU cevap olduğu biçimde yeniden kurulur:

  KAMERA HEDEFE TAŞINIR → kameraya hareket = hedefe hareket.
  Nötr çekimdir (§6.3, kadran 6); dizide EN FAZLA BİR kez kullanılır
  ve tercihen geçiş noktasına (koşu → biniş gibi) konur.
```

**KOMPOZİSYON ŞABLONU** (Black Cradle S4-V3 — GEÇTİ, 17.08.2026):

```
① Kamera hedefin YANINDA durur; hedefin gövde kenarı/parçası ön
   planda KADRAJA GİRER ("the craft's hull edge and one landing leg
   cut into the extreme RIGHT foreground") — hedef artık arka plana
   atılamaz, oradadır.
② Hedefin ışığı ön plana taşar ("its floodlight pool spills across
   the near foreground") — öznenin koştuğu yer aydınlıktır.
③ Baskın ışık TÜM arka planı alır ve özneyi ARKADAN rimler ("the dawn
   seam spans the full background width, back-lighting both runners");
   yüzler öznenin kendi lambalarıyla önden aydınlanır. Mıknatıs artık
   kompozisyonun düşmanı değil, arka fonudur.
④ Negatif iki cümleyle mühürlenir: "the target is NEVER behind the
   moving subject — its hull stays in the near foreground beside the
   camera; no craft appears in the background" + "the subject never
   turns away from the camera".
⑤ Yaklaşma mesafesi sayıyla: başlangıç/bitiş metre + güvenli alan
   bandı (figür kadrajın hangi yüzde bandında kalır).
```

Kazanç yan etkileri (ölçüldü): yüzler ve renk-aksan ayrımı yakın
mesafede okunur (Stone Sky'ın 90 m'de renk erimesi riski düşer);
"gemiye koşuyorlar mı" sorusu yapısal olarak cevaplanır (gemi kadrajda
ve kameranın yanında). Bedel: nötr çekim momentum düşürür — dizide tek
kalmalı ve S sınırında yön tekrar kurulmalıdır (§6.3 bedel notu).

**NE ZAMAN DOĞRUDAN V3 İLE BAŞLANIR** (iki yenilgiyi beklemeden):

```
□ hedef görsel olarak silik (siyah/karanlık/kamuflaj) VE
□ arka planda baskın ışık kaynağı VE
□ özne kameraya paralel (yanal) koşacaktı
→ üçü birdense yanal koşuyu HİÇ deneme; kamerayı hedefe koy.
   Black Cradle S4 bu profilin ilk ölçümüdür: V1+V2 bedeli iki
   üretim koşusuydu.
```

---

# 7. 🎬 ÇEKİMDEN ÇEKİME KURALLAR

```
KURAL 1 — EKSEN İHLALİ YASAK
  Kamera, haritada seçilen tarafta kalır. Eksen atlamak gerekiyorsa
  (bilinçli yön değişimi) atlama TEK bir nötr çekimle gösterilir:
  ya eksen ÜZERİNDEN çekilmiş bir çekim (hareket tam kameraya doğru /
  kameradan uzağa — §6.3) ya da kameranın hattı geçişi tek çekim içinde
  görünür. Sonraki tüm çekimler YENİ tarafta kalır ve harita güncellenir.

KURAL 2 — HEDEF, YAKLAŞMA BOYUNCA AYNI TARAFTA VE MONOTONİK BÜYÜR
  §4.6 kesir dizisi. Taraf + kesir + saat, üçü birden tutmalı.

KURAL 3 — ORYANTASYON DURUMU SAHNE SINIRINDA DEVREDİLİR
  Karakter dikey bir şeye tırmanıyorsa sonraki çekim onu tırmanırken
  devralır; dikeyden yatay zemine ışınlanamaz (Blind Return 02:38:
  dikey rokette tırmanış → yatay borunun yanında ayakta). Sahne
  promptunun 0s beat'i, önceki sahnenin son beat'indeki gövde
  pozisyonunu, saatini ve yönünü TEKRAR yazar.

KURAL 4 — MEKÂN DEĞİŞİMİ GEÇİŞLE KAZANILIR
  A'dan B'ye geçen karakter için ya kısa bir transit çekimi vardır
  ya da B'nin ilk çekimi geniştir ve A'yı arka planda gösterir
  ("kamp arkada küçülmüş, gemi önde"). İkisi de yoksa izleyici
  ışınlanma okur (Blind Return, Canopy World, Holding Field).

KURAL 5 — YÖN TAŞIYICILARI FİLM BOYUNCA TEK YÖNDE
  Rüzgâr, toz, duman, enkaz savrulması, bayrak, gölge: haritada tek ok,
  her promptta aynı ekran yönü. Bunlar izleyicinin pusulasıdır;
  taşıyıcı yön değiştirirse mekân dönmüş algılanır (Kaleida duman,
  Holding Field enkaz, Stone Sky gölge).
  ⚠️ Gölge, güneşin konumundan TÜREYEN bir taşıyıcıdır: güneş ekran
     solundaysa gölgeler ekran sağına düşer. İkisini ayrı ayrı yazma —
     bir promptta güneşi sola, gölgeyi sola koyarsan çelişki üretirsin.

KURAL 6 — ⭐ GİRİŞ-ÇIKIŞ EŞLEMESİ (yeni)
  Bir figür kadrajın sağ kenarından çıktıysa, sonraki çekime SOL
  kenardan girer. Yolculuk devam ediyorsa yön korunur; kenar değişir.
  Matris §7.1'de.

KURAL 7 — ⭐ HER KESMEDE ÜÇ SORU (yeni)
  Kesme yazılırken üç soru cevaplanır ve cevaplar yön defterine (§3.3)
  işlenir:
     · hedef hâlâ aynı tarafta mı?
     · özne hâlâ aynı yöne mi gidiyor?
     · aracın saati değişti mi — değiştiyse gösteren çekim var mı?
```

### 7.1 ⭐ KESME MATRİSİ

| Önceki çekimin son karesi | Sonraki çekimin ilk karesi | Sonuç |
|---|---|---|
| Sağ kenardan çıkıyor | Sol kenardan giriyor, sağa gidiyor | ✅ Yolculuk sürüyor |
| Sağ kenardan çıkıyor | Sağ kenardan giriyor, sola gidiyor | ❌ İzleyici "geri döndü" okur |
| Sağ kenardan çıkıyor | Kadrajın ortasında, sağa gidiyor | ✅ Kabul edilir (mesafe atlandı) |
| Kameraya doğru geliyor (kadran 6) | Herhangi bir yön | ✅ NÖTR — taraf burada değişebilir |
| Kameradan uzağa gidiyor (12) | Herhangi bir yön | ✅ NÖTR |
| Sağa gidiyor | Aynı figür sola gidiyor, nötr çekim yok | ❌ Eksen ihlali |
| Araç burun 10 | Aynı araç burun 2 | ❌ Gövde dönmüş; dönüşü gösteren çekim şart |
| Araç burun 10, hareketsiz | Aynı araç burun 10, başka mesafe | ✅ Yer işareti korunmuş |

---

# 8. 🖼️ GÖRSEL ÇAPA AKIŞI — haritayı görsele bağlamak

Metin kilidi tek başına yeterli olmayabilir. En güçlü çapa, coğrafyayı
**bir kez görselde kurup** sonraki üretimleri ona bağlamaktır:

```
1. MASTER ESTABLISHING IMAGE — en geniş açı, TÜM yer işaretleri
   kadrajda (gemi + kamp + yön taşıyıcıları), üç eksenli SPATIAL LOCK
   bloğuyla üretilir. Haritayla karşılaştır: gemi doğru tarafta mı,
   burnu doğru saatte mi? Değilse görseli yeniden üret — sonraki her
   şey bunun üstüne kurulacak. ⭐ Bu tek kare, filmin tüm coğrafyasının
   en ucuz sigortasıdır.
2. Ara açılar aynı seed + master'a referansla üretilir
   (SAHNE_DEVAMLILIK_KILAVUZU §3 Scene Foundation Workflow —
   Aşama 1-2 ile aynı mantık, coğrafya boyutu eklenmiş hâli).
3. I2V: her sahnenin videosu, master'la tutarlı image'den başlar.
```

### 8.1 ⭐ I2V ZİNCİRİ — video promptu image'in yönünü DEĞİŞTİREMEZ

```
Image'de gemi sağda ve burnu 10'da ise:
   ✅ video promptu bu iki değeri TEKRARLAR ve hareketi ekler
   ❌ video promptu "gemi sola doğru döner" derse iki girdi çelişir;
      model ya image'i bozar (morph) ya promptu yok sayar

KURAL: video promptunun 0s beat'i, image promptunun SPATIAL LOCK
       bloğunun konum ve yönelim satırlarını kelime kelime tekrar eder.
       Hareket satırı yenidir; konum ve yönelim devralınır.
```

### 8.2 Aynalanmış seed tuzağı

Second Ship'te kadının yara izi sürekli ters kaşta çıktı ve rapor doğru
soruyu sordu: *"seed aynalı bir görselle mi eğitildi?"* Sonuç:

```
BELİRTİ   Karakterin asimetrik işareti (yara, yama, tek omuz ekipmanı,
          göz bandı) çekimler arasında taraf değiştiriyor.
TEŞHİS    Bu bir EKRAN YÖNÜ hatası değil, KARAKTER ÇAPASI hatasıdır;
          bu kılavuz değil SAHNE_DEVAMLILIK_KILAVUZU çözer.
TUZAK     Klibi yatay çevirerek yara izini düzeltmek, filmin
          coğrafyasını ters çevirir (§9 ayna kapısı).
KARAR     Asimetrik işaret taşıyan karakter varsa çevirme YASAK;
          düzeltme üretim tarafında yapılır.
```

---

# 9. 🔧 KURTARMA — üretim sonrası onarım

> Bu bölüm sürüm 2'de eklendi çünkü yanlış yönün bir kısmı **yeniden
> üretim gerektirmiyor.** Stone Sky'ın ham raporu gölge yönü hatasını
> gördü ve düzeltmeyi kendisi önerdi: *"Flip S6 horizontally in the edit
> if no text/asymmetry prevents it"* — maliyet etiketi: **Cheap.**

### 9.1 Maliyet tablosu — önce ucuz olanı dene

| Hata | Onarım | Maliyet | Kapı |
|---|---|---|---|
| Tek çekim aynalanmış (hedef ters tarafta) | Kurguda yatay çevir | ~0 | §9.2 ayna kapısı |
| Gölge/güneş yönü ters | Kurguda yatay çevir | ~0 | §9.2 |
| Sahne sırası bozuk, coğrafya bu yüzden sıçrıyor | Kurguda yeniden sırala | 0 | Blind Return D81 emsali |
| Yön taşıyıcısı ters (toz/duman) | Çevir; olmuyorsa yeniden üret | ~0 → pahalı | §9.2 |
| Aracın saati yanlış | Yeniden üret | pahalı | çevirme İŞE YARAMAZ — çevirince hem saat hem taraf döner |
| İki figürün dizilimi ters | Çevir (tek çekimse) veya yeniden üret | ~0 → pahalı | §9.2 |
| Geçişsiz mekân sıçraması | Araya transit çekim üret | orta | §7 kural 4 |

### 9.2 ⛔ AYNA KAPISI — çevirmeden önce beş kontrol

Yatay çevirme, kadrajdaki HER ŞEYİ çevirir. Şunlardan biri varsa
çevirme yasaktır:

```
□ Kadrajda okunabilir metin, rakam, logo var mı        → varsa DUR
□ Karakterde asimetrik işaret var mı (yara, yama,
  tek omuzda ekipman, tek taraflı yıpranma)            → varsa DUR
□ Elle iş yapılıyor mu (hangi el aleti tutuyor)        → varsa DUR
□ Araçta asimetrik detay var mı (tek rampa, tek antenli
  gövde, tek taraflı hasar)                            → varsa DUR
□ O çekim, komşu çekimlerle zaten uyumlu mu — yani
  hatalı olan bu çekim mi, komşuları mı                → önce bunu belirle
```

Beşi de temizse çevirme, filmin coğrafyasını **tek kalemde** düzeltir
ve hiçbir kare yeniden üretilmez.

### 9.3 Çevirmenin görünmez bedeli

Bir çekim çevrildiğinde o çekimin **ışık yönü de** çevrilir. Güneş
solda kurulmuş bir filmde çevrilen çekimde güneş sağa geçer. Bu yüzden
ayna kapısına altıncı bir soru fiilen dahildir: **çevrilen çekimde
yönlü ışık kaynağı görünüyor mu?** Görünüyorsa çevirme, coğrafyayı
düzeltirken ışığı bozar — kazanç sıfırdır.

---

# 10. ✅ KONTROL LİSTELERİ

### 10.1 ÜRETİMDEN ÖNCE — coğrafyalı her sahne için

```
□ PLAN'da kuşbakışı harita + kamera tarafı + ekran sonucu yazılı mı?
□ Yön defteri (§3.3) bu sahne için üç sütunu da dolu mu?
□ SPATIAL LOCK üç satırı da taşıyor mu — KONUM, YÖNELİM, HAREKET?
□ Yönelim bir SAATE bağlı mı, yoksa sıfatla mı geçiştirilmiş?
□ Yönelim ile hareket çakışıyor mu; çakışmıyorsa istisna YAZILI mı? (§4.2.1)
□ Hareket ve bakış yönü EKRAN-uzayında mı yazılmış?
  (grep: "toward the" geçen her satırda hedefin ekran dilimi var mı?)
□ Nesne-göreli taraf kelimesi kaldı mı? (his left · the ship's left ·
  tek başına port/starboard)
□ Yaklaşma dizisiyse: ölçek kesri önceki sahneden büyük, saat AYNI mı?
□ Araç varsa §5.1 beş sorunun beşi de cevaplı mı?
□ Araç indiyse iniş pozu harita kartına yazıldı mı? (§5.5)
□ İki+ figür varsa dizilim cümlesi var mı? (§6.4 · DERS 86)
□ Yön taşıyıcıları (rüzgâr/duman/enkaz/gölge) önceki promptla aynı yönde mi?
□ Gölge yönü güneş konumuyla tutarlı mı? (§7 kural 5)
□ 0s beat'i önceki sahnenin son pozisyonunu, saatini ve yönünü devralıyor mu?
□ NEGATIVE'e §4.8 satırı (araç varsa §5.6 da) eklendi mi?
□ Kadrajda TEK BASKIN ışık kaynağı var mı? Varsa §6.7'nin DÖRT kanalı
  birden yazıldı mı (hedef-dilim+yön · omuz hattı · ışığa göre poz ·
  yön negatifi)?
□ "Silik hedef + baskın ışık + yanal koşu" üçlüsü mü? → yanal koşuyu
  hiç deneme, §6.8 kompozisyonuyla başla (kamera hedefte, nötr çekim)
□ Kıç önde/geri geri hareket TASARIMSA: §4.8/§5.6'daki "no stern-first"
  satırı ATILDI ve "never nose-first" karşıtıyla değiştirildi mi?
□ python3 .../PROMPT_KONTROL/prompt_kontrol.py <dosya> → yön kapısı temiz mi?
  (⚠️ kapı YÖNELİMİ ve refleks çatışmasını GÖREMEZ — son iki madde
   yalnız insan gözüyle denetlenir)
```

**Yön kapısı ne arar** (13.08.2026'da eklendi · sıfır maliyet, üretimden önce):

| Kontrol | Seviye | Ne yakalar |
|---|---|---|
| Dünya-uzayı yön kelimesi | ⛔ BLOCK | `12 degrees to the north` · `forty meters east of` |
| Çapasız `toward` | ⚠️ FIX | `runs toward the ship` — hedefin ekran dilimi aynı cümlede yok |
| Nesne-göreli taraf | ⚠️ FIX | `To her left, a stack of crates` (konum anlatıyor) |
| Araç var, yönelim yok | ⚠️ FIX | dosyada araç geçiyor ama saat/burun/yan tarifi hiç yok |

⛔ **Kapının bilerek SESSİZ kaldığı iki şey** — ikisi de çalışan
mekanizma, bulgu değil:

```
· "scar on her LEFT eyebrow"  → karakter ÖZELLİĞİ, nesne-göreli olmak
   ZORUNDA (Ders 58). Ekran-göreliye çevrilirse yara izi kesmeler
   arasında taraf değiştirir.
· "the northern crater rim" · "the western ridge" → yer işaretine AD
   veriyor, yön tarif etmiyor. Çıplak biçim (north/east) bulgudur,
   -ern biçimi değildir.
```

### 10.2 ⭐ ÜRETİMDEN SONRA — video denetim defteri

> Bu tablo QA rubriği DEĞİLDİR; operatörün 10 dakikada kendi doldurduğu
> ucuz denetimdir. Rubrik dış modelde koşar ve puan verir; bu defter
> sana hangi çekimin yeniden üretileceğini söyler.

**Tarama yöntemi:** her sahnenin **ilk ve son karesine** bak, arasını
izleme. Coğrafya hataları kesme sınırlarında yaşar; ortada değil.
🆕 Koşan/hareket eden figür varsa ÜÇÜNCÜ bakış: yüz nereye dönük —
profil mi, kameraya mı, ışığa mı? Yanlış dönük yüz kesme sınırında
değil karenin ORTASINDA yaşar ve defterin öteki sütunları temizken
bile sahneyi düşürür (Black Cradle S4-V1/V2).

| Sahne | Hedef tarafı | Özne yönü | Aracın saati | Taşıyıcı | Dizilim | ✅/❌ | Onarım (§9) |
|---|---|---|---|---|---|---|---|
| S1 | sağ | sola→sağa | 10 | sola→sağa | A sol, B sağ | ✅ | — |
| S2 | sağ | sola→sağa | 10 | sola→sağa | A sol, B sağ | ✅ | — |
| S3 | **sol** | sağa→sola | 10 | sola→sağa | A sağ, B sol | ❌ | yatay çevir (ayna kapısı temiz) |

```
DEFTERİN OKUNMASI
 · Bir sütunda tek bir hücre farklıysa   → o çekim bozuk, §9'a bak
 · Bir sütun ortadan itibaren komple
   değişiyorsa                            → eksen ihlali; hatalı olan
                                            çekim değil KAMERA KARARI
 · Taşıyıcı sütunu tek başına ters ise   → çevirme genelde çözer
 · Saat sütunu ters ise                   → çevirme ÇÖZMEZ, yeniden üret
```

---

# 11. 🧪 TEST PROTOKOLÜ — ders yazmadan önce

Sürüm 1 için yazılan protokol kısmen koştu; sonucu §0'da. Sürüm 2'nin
yeni kilitleri (kademe 2: saat kadranı) **henüz hiç ölçülmedi.** Kural
eklemek tek başına kaliteyi artırmıyor (AGENTS.md §8); mekanizmanın
çalıştığı ölçülmeli:

```
SÜRÜM 1 SONUCU (Third Dune, 11.08.2026)
  Dört sabit (konum + hareket + taşıyıcı + ışık tarafı) 25/25 tuttu.
  Kilidin söylemediği dizilim bozuldu → DERS 86.
  Coğrafya skoru için tek kaynak 04_MANTIK_KALITE_TABLOSU (satır ŞARTLI:
  üç MAJOR'ın ikisi belge kontrolünde düştü — DERS 87).
  ÇIKARIM: mekanizma çalışıyor; kapsamı eksikti.

SÜRÜM 3 SONUCU (Black Cradle S4, 16-17.08.2026 — üretim ölçümü)
  V1: §6.1'e uygun prompt → koşucular ışığa koştu (ışık mıknatısı).
  V2: dört kanallı kilit → hedef arkaya atıldı, koşu kameraya döndü
      (frontal refleks). V3: kamera hedefe taşındı (nötr çekim) →
      İLK DENEMEDE GEÇTİ (operatör onayı).
  ÇIKARIM: kilit-refleks çatışmasında kilidi büyütmek işe yaramıyor;
  kadrajı refleksle hizalamak tek denemede çözdü. İKİ YENİLGİ KURALI
  buradan yazıldı (§6.8). Kaynak rubrik yok — üretim gözlemi; ders
  kaydı DERS 104, kapı kayıtları THE_BLACK_CRADLE_PART_A.md sonunda.

SÜRÜM 2 TESTİ — sıradaki araçlı filmde koşulacak
1. Araç inişi veya yanaşması içeren 2-3 sahne seç.
2. Aynı sahneleri YÖNELİM KİLİDİYLE (kademe 2) ve kilitsiz üret.
3. §10.2 defterini ikisi için de doldur; sonra MANTIK_QA koş.
4. ⚠️ Ölçüm sapması ±1.5-2 puan (kural ⑥) — tek sahneyle karar verme,
   fark en az birkaç tekrar boyunca aynı yönde çıkmalı.
   ⭐ Defter bu yüzden değerli: "gemi burnu doğru saatte mi" sorusu
      SAYILABİLİR bir sorudur ve ölçüm sapmasından etkilenmez.
      Skor beklemeden karar verebileceğin tek veri budur.
5. Sonuç olumluysa → kart G ile ders yaz; kaynak rubrik MANTIK_QA'dır.
   Olumsuzsa → §4.2'yi gözden geçir, sonucu buraya işle.
6. Kademe 3 (kesirli koordinat) ayrıca ve YALNIZ master establishing
   karesinde denenir; tutmazsa sessizce düşer, filme yayılmaz.
```

---

# 12. 📚 KAYNAKLAR VE İLİŞKİLİ DOSYALAR

Dış kaynaklar (09.08.2026'da tarandı):

- Hailuo — Director's Guide: Shot-Reverse-Shot Spatial Logic
  (master shot anchoring, gaze-derece dili, eksen tanımı)
  <https://hailuoai.video/pages/knowledge/director-guide-shot-reverse-shot-spatial-logic>
- Replicate — How to prompt Veo 3 (kamera/kompozisyon kelime dağarcığı)
  <https://replicate.com/blog/using-and-prompting-veo-3>
- Scenario — Spatial Prompting with Veo 3 (görsel anotasyon/çizim yolu)
  <https://help.scenario.com/en/articles/spatial-prompting-for-videos-generation/>
- 180-degree rule — <https://en.wikipedia.org/wiki/180-degree_rule>
- Videomaker — Screen Direction
  <https://www.videomaker.com/article/12986-screen-direction/>

| İlişkili dosya | Bağlantı |
|---|---|
| `YANASMA_VE_KENETLENME_KILAVUZU.md` | yanaşma sekansının vuruş seti + ses kalıbı — §5'in reçete katmanı |
| `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | SPATIAL LOCK'un V2 iskeletindeki yeri (üç satırlı biçim) |
| `PROMPT_KONTROL/prompt_kontrol.py` | üretimden önceki yön kapısı — §10.1'in makine tarafı |
| `SAHNE_DEVAMLILIK_KILAVUZU.md` §3 | Scene Foundation Workflow — görsel çapa akışının temeli; aynalanmış seed (§8.2) oraya aittir |
| `DERSLER/` → DERS 48 | biyom sabiti (sınıf 1) |
| `DERSLER/` → DERS 58 | tekrar eden varlık kimliği (sınıf 2) — harita kartı onun uzantısı |
| `DERSLER/` → DERS 86 | iki kişilik kadrajda dizilim kilidi (§6.4'ün kaynağı) |
| `DERSLER/` → DERS 87 | coğrafya bulgusu filmin önermesi mi — bulgu tabloya girmeden önceki kapı |
| `DERSLER/` → DERS 104 | ışık mıknatısı + frontal refleks + iki yenilgi kuralı (§6.7-6.8'in kaynağı) |
| `yatay_3_5_dk_filmler/THE_BLACK_CRADLE/` | Sürüm 3'ün ölçüm filmi — S4 V1/V2/V3 kapı kayıtları PART_A sonunda; V3 kompozisyon şablonunun dolu örneği S4 promptudur |
| `QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` | Coğrafya kategorisini ölçen rubrik |
| `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | skorların tek kaynağı |
| `yatay_3_5_dk_filmler/THE_THIRD_DUNE/` | depodaki ilk uygulama — SPATIAL LOCK BIBLE örneği |
