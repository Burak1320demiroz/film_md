# 📚 FAZ 7 / BEDEL — QA DERSLERİ VE AKSİYON RAPORU (1. KOŞU)

> Koşu: 12.08.2026 · Girdi: **1 birleşik reel (~100 s) · MODE R —
> KARAR 5 ⑥'ya RAĞMEN** · Rubrik: `FAZ_07_QA_PROMPT.md` · Ham çıktı:
> `../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_SECOND_SHIP_FAZ07_HAM.md`
>
> **SKOR GEÇERSİZ — taban koşusu DEĞİLDİR.** Rapor on kategoriye de
> sayı verdi (ortalama 1.9), ama sıra kayması yüzünden segmentlerin
> beşi yanlış satıra karşı puanlandı: örneğin KAMERA DİSİPLİNİ 2/10
> yazıldı, oysa içerikle eşlendiğinde üç push-in ve yedi lockoff
> DOĞRU sahnelerde. Bu koşu bir **bulgu koşusudur**; skor tablosuna
> hiçbir satır yazılmaz. [→ D-AU]
>
> ⚠️ İki koşu üst üste (F6 · F7) teslimat yüzünden taban üretemedi.
> Denetimin bedeli ödendi, ölçüm alınamadı.

---

## 1. KÖK NEDEN #1 — TESLİMAT: yedi fazda ALTINCI protokol kayması, bu kez SIRA da kaydı

KARAR 5 ⑥ mekanik kapıyı yazmıştı: üretim klasörüne baştan
`s61.mp4 … s70.mp4` boş yuva şablonu açılacak, QA 10 ayrı adlandırılmış
dosyayla MODE T koşulacaktı. Yine reel gitti — ve F6'dan farklı olarak
bu kez **reel'in içindeki sıra da bozuktu.**

Rubriğin içerik-çelişki kuralı (STEP 0.5) kaymayı YAKALADI: beş
segmentin beşi için "content contradicts row" satırı yazıldı ve hangi
satıra benzediği tek tek bildirildi. **Rubrik yarısı çalıştı.**

```
Bu koşunun somut bedeli: on kategorinin en az dördü (EVENT DELIVERY,
CAMERA DISCIPLINE, PHASE CHAIN, WATCHER ANCHOR) kaymanın gürültüsüyle
puanlandı ve hiçbiri kullanılamaz. Ayrıca S65'in TEK gerçek sorusu
(iki figür birbirinin aynısı mı?) hiç ölçülmedi — rapor o segmenti
S64 satırına karşı denetledi ve "kadın yok" yazıp geçti. [→ §5 madde 1]
```

---

## 2. İÇERİK ÇAPASI — segmentler gerçekte hangi sahne

Rapor her segmentin içeriğini tarif etti; permütasyon tek ve nettir:

| Reel | Rapordaki içerik | GERÇEK sahne | Güven |
|---|---|---|---|
| 0:00–0:10 | plaka + 2 figür + push-in, plaka ölü | **S61** | ✅ yerinde |
| 0:10–0:20 | iki insan, lockoff, konuşma | **S63** | ✅ tek aday |
| 0:20–0:30 | bölme AÇILIYOR, push-in, kadın + 2 sedef | **S64** | ✅ tek aday |
| 0:30–0:40 | bölme açık, 2 figür, lockoff | **S65** | ✅ tek aday |
| 0:40–0:50 | 1 net figür + arkada yumuşak oturan, yavaş eğilme | **S66** | ✅ tek aday |
| 0:50–1:00 | Bekçi plakaya dokunuyor, oturan yok | **S62** | ✅ tek aday |
| 1:00–1:10 | kadın baş-omuz yakın plan | **S67** | ✅ yerinde |
| 1:10–1:20 | iki el + plaka, yüz yok | **S68** | ✅ yerinde |
| 1:20–1:30 | iki insan, kask çıkıyor | **S69** | ✅ yerinde |
| 1:30–1:40 | gökyüzü + ışık noktası, figür yok | **S70** | ✅ yerinde |

```
PERMÜTASYON:  61 · [63 64 65 66 62] · 67 68 69 70
Grup içinde TEK dosya (S62) sona düşmüş, diğer dördü birer öne kaymış.
Bu, alfabetik ya da rastgele bir karışma DEĞİL — zaman damgasına göre
sıralamanın imzası: S62 fazın ÇAPA SAHNESİ ve en çok yeniden üretilen
karesi, dolayısıyla dosyası grubun EN YENİSİ. NLE'ye "değişiklik
tarihine göre" alındığında tam olarak bu sıra çıkar. [→ §5 madde 2]
```

**Aşağıdaki tüm bulgular GERÇEK sahne numarasına göre yazılmıştır.**
Rapordaki yuva numaraları ham dosyada durur.

---

## 3. KÖK NEDEN #2 — ÜRETİM: dersler (numaralar F6'dan devam)

### D-AK 🔴 FAZIN BLOCKER'I: KASK ÇIKTI — kilit yalnız ELDİVENE yazılmıştı

Gerçek S69, 1:23: kadın kaskı **tamamen çıkarıyor**, çıplak baş, yüz ve
boyun kadrajda. Solunamaz atmosfer kilidi, faz blocker'ı, ve ÇEHOV 7'nin
S80'deki gerçek ateşlenmesi bir faz önce harcandı.

Kök neden promptun kendisinde ve grep'le kanıtlanabilir:

```
grep -n "helmet stays ON and sealed\|every helmet ON and sealed" FAZ_07_BEDEL.md
→ yalnız S61 (2 kez) ve S64 (2 kez).
  S63'te YOK · S67'de YOK · S69'da YOK.

Yani kask kilidi, kaskın çıkmasının hiç akla gelmediği sahnelere
yazıldı; ÇIKARMA EYLEMİNİN GEÇTİĞİ TEK SAHNEDE yazılmadı. S69'un
negatifi şunu diyor: "The glove NEVER comes off: no bare hand, no bare
skin, no exposed wrist" — model eldiveni çıkarmadı, KASKI çıkardı.
```

```
DERS [→ global DERS 89]: sahnenin eylemi bir ÇIKARMA ise, model
yasaklanan parçayı bırakır ve en yakın çıkarılabilir parçayı çıkarır.
Tek parçayı kilitlemek jesti iptal etmiyor, HEDEFİNİ değiştiriyor —
bu, F6 D-AD'nin (kemeri yasakla, kasa gelir) insan-ekipman
versiyonudur.

S69 yaması — pozitif tek-mühür sayımı, IMAGE + VIDEO NEGATIVE'e:
Exactly ONE seal is touched in this shot and it is the ring at his
right WRIST. Every other seal stays closed and untouched: both
helmets stay ON, locked and sealed at the collar for every frame,
both collar rings stay closed, both gloves stay on both hands. No
bare head, no bare face, no bare neck, no bare hand, no bare wrist,
no bare skin of any kind appears at any second.
```

### D-AL 🔴 DOLU VİZÖR PLAKASI İLK KEZ BATTI — ve kadraja bağlı battı

F4 D-Q'dan beri tutan (F6'da 4/4) plaka dili F7'de **iki sahnede**
delindi: gerçek S61 (0:00) ve gerçek S65 (0:30) — "highly reflective
glass imaging the room and the woman". Aynı koşuda gerçek S66'da (0:40)
plaka **dark matte, PASS**.

```
AYIRT EDİCİ DEĞİŞKEN KADRAJ: plaka kadrajda büyükken (S66, 85mm
chest-up, 3 m) dil tuttu; plaka küçükken (S61 tam boy 5→3.5 m ·
S65 iki tam figür 3.5 m) cam önseline döndü. Bekçi'nin bölmede
oturan kopyası ve bölme kenarı da "thick GLASS door jamb" olarak
raporlandı — cam önseli bu fazda dekora bile bulaştı.

DERS: dolu-plaka dili bir MALZEME tarifidir ve piksel bütçesi
düştüğünde model malzemeyi değil, "kask = cam vizör" önselini
çiziyor. Malzeme tarifine bir DEĞER tarifi eklenir:

Beş Bekçi sahnesinin hepsine (S61 S62 S64 S65 S66), SUBJECT'in
ilk cümlesine ve NEGATIVE'e:
The visor area is the DARKEST VALUE IN THE FRAME - a flat dark
grey-green cut-out that reads like a hole punched in the picture.
It is matte and light-absorbing: no highlight, no gradient, no
window, no reflection of the white room, of the floor, of a
person, or of anything else at any distance or any frame size.

+ ÜRETİM: geniş kadrajlarda (S61 · S64 · S65) onaylı R3 KASK
karesi start-frame olarak verilir — el sınıfında (D-AM) zorunlu
kılınan referans çözümü artık BAŞ için de gerekiyor.
```

### D-AM 🔴 DÖRT HANE: SINIF GENİŞLEDİ — dört sahne, dört kez beş parmak

Gerçek S61 (0:00) · S65 (0:30) · S62 (0:56) · S68 (1:10): **hepsinde
BEŞ hane.** Sayılabilir olan her karede beş. Sınıfın vaka sayısı üçten
yediye çıktı (F5 S45 · F5 S50 · F6 S55 · F7 ×4).

```
KRİTİK FARK: bu artık "el-dolu-kadraj" sınıfı değil. S61 ve S65 tam
boy geniş kadrajlar — el kadrajın küçük bir parçası ve yine beş
parmak. Yani: sayısal kilit + "count them" + insan-el negasyonu +
hafif profil kadrajı BİR ARADA yetmiyor.

DERS: prompt katmanı bu sınıfta TÜKENDİ (üçüncü kez tescil). Karar
üretim katmanına geçer ve kural sertleşir:
  ① R3 BEKÇİ MASTER'da parmak insan gözüyle sayılmadan hiçbir Bekçi
     sahnesi üretilmez (TETİK KAPISI 2 — bu koşuda uygulandığına dair
     kanıt yok, bkz. §6).
  ② Onaylı R3 karesi yalnız S62/S68'e değil, BEŞ BEKÇİ SAHNESİNİN
     HEPSİNE start-frame olarak verilir.
  ③ Kabul kriteri kadraj bazında: parmakların sayılamadığı bir açı
     KABUL EDİLEBİLİR ÇIKTIDIR; sayılabilip beş çıkan kare reddedilir.
```

### D-AN 🔴 FAZIN TEK ⛔ OLAYI HİÇ ÜRETİLMEDİ — 2-3 mm modelin hareket eşiğinin altında

Gerçek S68: zemin **hiç kabarmadı**. Filmin üçüncü ve son zemin tepkisi
(KARAR 3), sıfır replikle kurulan ahlaki denklemin görsel yarısı,
ekranda yok. Aynı sahnede ikinci beat de düştü: kadının eli halkaya
gitmedi, **plakaya** dokundu.

```
Rapor GROUND LEDGER'da net: "Ground response is entirely absent.
Floor remains dead still. Limits broken: swelling never rises."

DERS [→ global DERS 90]: sayısal kilit olayı GÜVENLİ yaptı ama
GÖRÜNMEZ de yaptı. 2-3 mm, 100mm lenste 70 cm'den, cilalı beyaz taşta,
kendi ışığı olmayan bir kabarma — modelin üretmemeyi seçtiği bir
"hiç"tir. Sayı korunur, OKUNURLUK KANCASI eklenir: hareketi ölçen bir
görsel referans yazılır.

S68 yaması (VIDEO, 2s ve 5s beat'leri):
2s — On the polished floor twenty centimeters aside, the long thin
highlight lying across the stone BENDS: the reflected line breaks
into a shallow arc and travels as the stone lifts into a smooth
swelling two or three millimeters proud, growing at the pace of a
held breath. The bulge is read ONLY by that bending highlight and
by the contact shadow at its foot - no crack, no seam, no light,
no dust.
5s — The pearl glove lifts off the plate and the highlight
straightens back into one line as the swelling sinks, until the
floor is flat and polished again.

+ ÜRETİM: S68'in END FRAME imajı zaten bütçede — o kare KABARMANIN
  ZİRVESİ olarak üretilir ve start+end çifti verilir. Kabul kriteri:
  start ve end kareleri yan yana konduğunda kabarma insan gözüyle
  ayırt ediliyor mu. Ayırt edilmiyorsa kare reddedilir.
```

### D-AO 🔴 KASA AİLESİ İKİNCİ KEZ — pozitif kenar dili yazıldı ve yine kasa çıktı

Gerçek S64 (0:20): bölme açılışında **kalın iç pervaz/kasa** —
üstelik rapor "thick **glass** door jamb" diyor. F6 D-AD yaması
("knife-thin edges, NO jamb, NO reveal, NO inner faces, NO frame,
a door frame is a failed frame" + "parting line PERFECTLY STRAIGHT")
S64'ün hem IMAGE hem VIDEO promptuna yazılmıştı.

```
DERS: aileyi pozitif dille kapatmak F6'da hatayı bir üye kaydırdı
(kemer → kasa); F7'de aynı üye ikinci kez geldi. Negasyon+pozitif
tarif bu sınıfta da tükendi. Kalan tek kaldıraç KADRAJ:

S64 yaması — kenar kadrajın DIŞINA çıkarılır:
Push-in'in bitiş kadrajı, açıklığın kenarlarını kadraj dışında
bırakacak biçimde daraltılır (4 m yerine 3 m'de biter): son üç
saniyede kadrajda YALNIZ açıklığın içi ve oturan figür kalır.
Görülmeyen kenar yanlış çizilemez.
⚠️ Bu, sahnenin bilgisini değiştirmez — bölmenin AÇILDIĞI zaten
   2s-4s'te hairline + genişleme ile okunuyor.
+ START + END FRAME imaj çifti (İMAJ ÇİFTİ KAPISI) bu sahnede
  zorunlu: END kare "kenarsız bölme içi" karesidir.
⚠️ F9 aynı dekorda geçiyor — bu çözüm orada da geçerli.
```

### D-AP 🔴 YARA İZİ TARAF DEĞİL, ÖZELLİK KAYBEDİYOR — 4 insan sahnesinin 3'ünde yanlış yerde

| Gerçek sahne | Olması gereken | Ekranda |
|---|---|---|
| S63 | adam: SAĞ elmacık | **SOL yanak** |
| S67 | kadın: SOL KAŞ (kaşı ikiye bölen) | **SOL ÇENE** |
| S69 | kadın: SOL KAŞ | **SAĞ yanak** |

```
Üç vakanın ikisi taraf hatası DEĞİL, ÖZELLİK hatası: iz kaşta değil
çenede/yanakta. "A fine faded white scar splitting her LEFT eyebrow"
cümlesi "yüzünün solunda bir yerde bir iz" olarak okunuyor.

DERS [→ global DERS 91]: iz bir TARAFA değil, bir ÖZELLİĞE ve bir
ÖLÇÜYE çapalanır; yüzün geri kalanı açıkça temiz ilan edilir.

Üç insan sahnesine (S63 S67 S69), SUBJECT + NEGATIVE:
Her scar is a 2 cm vertical white line that CROSSES THE HAIR OF HER
LEFT EYEBROW and splits it into two halves - it sits IN the brow,
not above it, not below it, not on the cheek, not on the jaw. The
rest of her face is completely unmarked: no scar, line or mark on
either cheek, jaw, chin, nose or forehead.
His scar is a 2 cm shiny burn mark ON THE BONE OF HIS RIGHT
CHEEK, below the outer corner of his right eye. The rest of his
face is completely unmarked.
```

### D-AQ 🔴 SINIRLI İZİN KAYBEDİLİR — "faint cool reflection" tam aynaya dönüştü

Gerçek S67: kadının vizörü **yansıtıcı cam**. Promptta çelişki var:

```
IMAGE SUBJECT :  "...a fully transparent, seamless visor; the face
                  reads clearly through the glass, WHICH CARRIES A
                  FAINT COOL REFLECTION."     ← izin veriliyor
NEGATIVE      :  "no tint, no mirror coating, no reflection that
                  hides what is behind it"    ← sınır konuyor
EKRANDA       :  tam ayna.
```

```
DERS [→ global DERS 88]: "hafif X ama abartma" biçimindeki her
sınırlı izin, tam X olarak çıkıyor. F6 D-AF'nin (kirli parmak ucu +
iz yasağı → duvarda iz) optik versiyonu. Kural aynı: KAYNAĞI SAHNEDEN
ÇIKAR, sonra yasakla.

S67 (ve tüm insan vizörü olan sahneler) yaması:
"which carries a faint cool reflection" cümlesi SİLİNİR. Yerine:
The visor is optically clear and carries NO reflection at all -
the eyes, the brows and the scar are the sharpest, brightest
things in the frame and nothing floats on the glass in front of
them.
```

### D-AR 🔴 KONUŞMA KİLİDİ ÜÇ SAHNEDE DELİNDİ — ağız hattı kilidi ilk kez ölçüldü ve battı

| Gerçek sahne | Kural | Ekranda |
|---|---|---|
| S63 | yalnız ADAM konuşur, başı 3/4 çevrik, ağız hattı okunmaz | **iki insan da konuşuyor, ağızlar net okunuyor** |
| S67 | konuşma YOK, ağız kapalı | **kadın konuşuyor (1:06), ağız net** |
| S69 | kadın ~4 kelime, baş 3/4 çevrik, ağız zor okunur | **kameraya dönük, ağız tam okunuyor (1:27)** |

```
DERS: KİLİT 2'nin (diyalog kadrajı) iki yarısı var ve ikisi de ayrı
ayrı battı — ① lisanssız sahnede ağız açılması, ② lisanslı pencerede
başın kameraya dönmesi. "his head is turned three quarters away
whenever he speaks" bir DURUM tarifi; model konuşmayı satmak için
başı çeviriyor [F4 sınıfı].

Yama — baş yönü bir SAYIYA ve bir ENGELE bağlanır:
S63/S69: the speaking head stays turned 100-120 degrees away from
the lens for every frame in which the lips move; the far cheek and
the ear are toward camera and THE MOUTH IS BEHIND THE HELMET RING
from this angle - the lips are never inside the frame's sharp
zone. The listening face keeps its lips CLOSED AND TOUCHING in
every frame.
S67 (+ konuşmasız tüm insan sahneleri): her lips stay closed and
touching for all ten seconds - not one frame of parting, no jaw
drop, no breath shape, no whisper.
```

### D-AS 🔴 ÇAPA SAHNE ÇAPA OLAMADI — plinth sütundan kalın kare bloğa dönüştü

Rapor PASSPORT: "The plinth starts as a slender column (S61), but in
[gerçek S62] and S68 it mutates into a massive, thick square block."

```
S62 üretim sırasının 1. sahnesi ve ⛔ ÇAPA SAHNE: plakanın malzemesi,
çapı ve zemin hizası orada kilitlenecekti. F9'un doruğu (S81-S86) AYNI
plakada geçiyor — kaçan ölçek altı sahneye yayılır.

DERS: promptta plakanın çapı üç sahnede de yazılı (40 cm) ama
PLİNTH'in geometrisi hiçbir yerde sayısal değil ("slender white
plinth"). Sayısal olmayan tek nesne, tam da mutasyona uğrayan nesne.

Üç sahneye (S61 S62 S68 + kenarda görünen S63 S69):
The plinth is a SLENDER ROUND COLUMN exactly 12 cm in diameter and
90 cm tall, the same matte white as the floor, with no base plate,
no plinth block, no pedestal, no taper - the 40 cm disc overhangs
it on every side, so the plate is more than three times wider than
the column that carries it.

⚠️ TETİK KAPISI 1 bu koşuda ya uygulanmadı ya da yan yana doğrulama
   yapılmadı — §6'da doküman sorusu.
```

### D-AT 🟡 İKİ YÜZEY/IŞIK KİLİDİ DELİNDİ — yönlü gölge ve kule tacında pencereler

```
① YÖNLÜ GÖLGE: gerçek S63 ve S69'da insanların ARKASINDA yönlü
   gölge. Kaynaksız 5600K kilidi "no visible lamp" diyor ama
   GÖLGENİN KENDİSİNİ tarif etmiyor. Yama:
   Shadows are almost absent in this room: the ONLY darkening
   anywhere is a faint contact shading directly under the boots.
   Nothing casts a shadow onto a wall or across the floor - no
   figure shadow, no cast shape, no direction of any kind.

② KULE TACI: gerçek S70'te tacın yakınında dört koyu dikdörtgen
   pencere/menfez. Boş yüzey kilidi dışarıda da gerekiyor:
   The tower's surface is ONE CONTINUOUS POURED WHITE SURFACE from
   the bottom of frame to its crown: no window, opening, vent,
   slit, port, hatch, panel, seam, band or dark rectangle of any
   size appears anywhere on it.
```

### D-AU 🔴 SIRA KAYMASI SKORU YOK ETMEDİ, ZEHİRLEDİ — rubrik puan üretmeye devam etti

Rubrik kaymayı yakaladı, her segment için "content contradicts row"
yazdı — ve sonra **on kategoriye de sayı verip 1.9 ortalama yayımladı.**
O tablodaki en az dört kategori kaymanın gürültüsü. En kötüsü:
"CAMERA DISCIPLINE 2/10 — push-ins and lockoffs fail their assigned
slots due to the clip shuffle" — yani rapor, hatanın kendi eşlemesinden
geldiğini BİLEREK sahneyi cezalandırdı.

```
DERS [→ global DERS 92]: eşleme çöktüğünde rubrik susmuyor, puan
üretmeye devam ediyor; okuyan da bunu üretim kalitesi sanıyor.
Rubriğe eşik konur — kaynak rubrik yaması bu dosyayla birlikte
FAZ_07_QA_PROMPT.md'ye işlendi (MAPPING COLLAPSE GATE):

  3+ segment satırıyla çelişiyorsa denetim durmaz ama SKOR DURUR:
  eşlemeden bağımsız kategoriler (1 · 2 · 3 · 5 · 9'un ışık yarısı)
  puanlanır, eşlemeye bağlı olanlar (4 · 8 · 10) UNVERIFIABLE yazılır
  ve ortalamaya girmez.
```

### D-AW 🟡 PROMPT ŞİŞMESİ — yedi fazlık kilit birikimi uzunluk bandını aştı

Bu koşunun yamaları promptlara işlendikten sonra ölçüm (README §6
bandı: imaj 1.700–2.300 · video 1.950–2.600 karakter):

```
Sıkıştırma öncesi:  imaj 2.174–2.934 · video 2.265–3.555
Sıkıştırma sonrası: imaj 2.174–2.623 · video 2.265–3.017
Bandın içinde kalan: yalnız S66 ve S70 (dokunulmayan iki sahne)
Toplam aşım: ~3.900 karakter (10 sahne × 2 prompt)
```

Her QA döngüsü kilit ekliyor, hiçbiri kilit çıkarmıyor. Yedinci fazda
prompt, bandın %15-20 üstünde. Bandın gerekçesi tam da bu koşuda
görünüyor: **en çok kilit taşıyan sahneler en çok kilidi düşürenler
oldu** (S68 ve S69 — en uzun iki prompt, en çok bulgu).

```
DERS (izlemede, henüz sayısal kanıt yok): kilit sayısı arttıkça tek
tek kilitlerin ağırlığı düşüyor olabilir. Kural önerisi — YENİ KİLİT
EKLERKEN ESKİ BİR KİLİT ÇIKAR: üst üste üç koşuda hiç tetiklenmemiş
negasyonlar (bu dekorda: "no bloom / no glow filter / no lens flare"
üçlüsünün iki üyesi, "no transitions", tekrarlanan yüz tarifleri)
sıkıştırılır. ⚠️ TUTAN kilit silinmez — tekrar silinir, kavram değil.
F8 promptları yazılmadan önce bir sıkıştırma geçişi yapılır.
```

### D-AV 🟡 SEGMENT MAP YİNE KUSURSUZ VE YİNE ŞÜPHELİ — F6 D-AI tekrarı

Rapor haritayı "MEASURED" ilan etti ve on segmenti de tam 10.0 s
verdi. F6'da aynı kusursuz harita varsayım çıkmıştı. Bu koşuda ek bir
çelişki var: harita ölçüldüyse kesmeler tespit edilmiş demektir, ama
aynı rapor segmentlerin içeriğinin satırlarla uyuşmadığını söylüyor —
yani sınırlar bulunmuş, sıra sorgulanmamış. Süre denetimi bu koşuda
da YAPILMAMIŞ sayılır; NLE'de klip başına doğrulanır
(F3 D-N → F4 D-V → F5 D-AB → F6 D-AI).

---

## 4. TUTAN TARAF — bu koşunun gerçek kazanımları

| Kilit | Kanıt |
|---|---|
| **⭐ ÖLÜ PLAKA YASASI [KARAR 3 / fazın omurgası]** | Plakanın göründüğü her karede sıfır tepki: S61 "plate does NOTHING", S68 "plate does NOTHING" — parlama, halka, ısı serabı, titreşim yok. Fazın en kolay batacak fikri (dokunulan diskin ödül vermesi) HİÇ batmadı. |
| **ZEMİN SESSİZLİĞİ (dokuz sahne)** | GROUND LEDGER: on segmentin onunda otonom zemin hareketi yok. Filmin en nadir efekti bedavaya harcanmadı — ama S68'de de olmadı [D-AN]. |
| **DESEN YASAĞI [F6 kalıtı]** | Hiçbir duvarda ışıklı desen, nokta, iplik, daire yok — önceki fazın dili bu faza sızmadı. |
| **METİN KİLİDİ** | On segmentte tek okunabilir karakter, altyazı, jenerik, watermark yok. |
| **DUVAR DÜZGÜNLÜĞÜ PUSH-IN ALTINDA [F6 D-AE yaması]** | İki push-in (S61 · S64) duvar boyunca ilerledi ve rapor hiçbir yatay panel çizgisi/bant bildirmedi — F6'nın en somut yaması ilk sahada tuttu. ⚠️ Yokluk kanıtı zayıftır; 2. koşuda doğrulanır. |
| **CESET KLİŞESİ YOK [KARAR 2]** | SEATED FIGURE LEDGER: mühürlü, sağlam, çürüme/kemik/toz yok, hiç kıpırdamıyor; S66'da yumuşak ve çözülmemiş kaldı. Yeni figür sınıfı ilk denemede temiz. |
| **BEKÇİ ÇAPASI (hane dışında)** | 2.10 m, düz çıplak sırt, tozsuz kabuk, uzun kollar, akışkan tek-akış hareket — altı ledger satırında da tuttu. Batan tek çapa noktası hane sayısı [D-AM] ve iki sahnede plaka [D-AL]. |
| **S70 IŞIK NOKTASI** | Kuyruk, alev, iz, hale, starburst, lens flare YOK; yana kaymadı, sadece büyüdü; ikinci nesne yok. Fazın en tuzaklı negasyon yığını temiz geçti. Tek hata tacın pencereleri [D-AT ②]. |
| **KAMERA DİSİPLİNİ (içerikle eşlendiğinde)** | Üç push-in gerçek S61 · S64 · S67'de, yedi lockoff diğerlerinde; yanal kaydırma YOK [KARAR 4 tuttu]; klip içi kesme bildirilmedi. Rapordaki 2/10 kaymanın eseri. |
| **FİGÜR SAYILARI** | Üçüncü kopya yok, fazladan figür yok, S70'te sıfır figür. S65'in lisanslı ikizi hiçbir yerde "hata" olarak raporlanmadı — rubriğin istisna dili çalıştı. |
| **RUBRİK İÇERİK-ÇELİŞKİ KURALI** | Beş kaymış segmentin beşini de yakaladı ve hangi satıra benzediğini yazdı. §2'deki yeniden atıf yalnız bu kural sayesinde mümkün oldu. |

---

## 5. AKSİYON LİSTESİ — öncelik sırasıyla

```
1. □ S65 TEK BAKIŞ (bedava, 60 sn): reel 0:30-0:40'ta iki figür
     BİRBİRİNİN AYNISI mı? Fazın omurgası bu tek soruda ve bu koşuda
     HİÇ ölçülmedi (segment S64 satırına karşı denetlendi).
     → aynıysa: en pahalı kare ilk denemede tutmuş demektir
     → farklıysa: S65 yeniden üretim listesinin başına girer
     Aynı bakışta: 0:40-0:50'de (gerçek S66) baş TAM düze dönüyor mu
     (dönüyorsa "itiraf" selamlaşmaya döndü — ayrı bulgu).

2. □ DOSYA SIRASI KAPISI (bedava, kalıcı) [D-AU · §1]:
     a) 10 klip s61.mp4 … s70.mp4 olarak adlandırılır
     b) NLE'ye ADA GÖRE sıralı alınır — "değişiklik tarihi" sıralaması
        bu koşuyu bitirdi
     c) kurgudan sonra tek kontrol: 0:00 plaka · 0:10 iki insan ·
        0:20 bölme açılıyor · ... (sahne başlıkları listesiyle)
     ⛔ Bu yapılmadan İKİNCİ KOŞU BAŞLATILMAZ.

3. □ ⛔ TETİK KAPISI 2 DENETİMİ [D-AM]: R3 BEKÇİ MASTER'da parmak
     insan gözüyle SAYILDI mı? Dört sahnede beş parmak, kapının
     çalışmadığını ya da hiç işletilmediğini söylüyor.
     → Sayılmadıysa: zincir önce tamamlanır.
     → Sayıldıysa ve R3 dört haneliyse: kapı start-frame katmanına
       genişletilir — BEŞ Bekçi sahnesinin hepsine onaylı el karesi.

4. □ PROMPT YAMALARI (yeniden üretimden önce, FAZ_07_BEDEL.md'ye —
     ⭐ bu maddenin tamamı 12.08.2026'da UYGULANDI):
     a) S69: tek-mühür sayımı + kask kilidi [D-AK]
     b) S61 S62 S64 S65 S66: vizör DEĞER kilidi ("darkest value in
        the frame") [D-AL]
     c) S68: kabarmanın okunurluk kancası (bükülen highlight) [D-AN]
     d) S64: bitiş kadrajı daraltılır, kenar kadraj dışına [D-AO]
     e) S63 S67 S69: yara izi özellik+ölçü çapası [D-AP]
     f) S67: "faint cool reflection" silindi [D-AQ]
     g) S63 S67 S69: ağız/baş yönü kilidi sayıya bağlandı [D-AR]
     h) S61 S62 S63 S68 S69: plinth 12 cm × 90 cm sayısal [D-AS]
     i) S63 S69: gölge yasağı · S70: kule tacı boş yüzey [D-AT]

5. □ YENİDEN ÜRETİM (kırmızılar, çapa sırasına göre):
     S62  ⛔ ÇAPA — plinth + hane [D-AS · D-AM]. Diğer plaka
          sahneleri onaysız başlamaz (TETİK KAPISI 1).
     S68  zemin tepkisi + halka beati + hane [D-AN · D-AM]
     S69  ⛔ BLOCKER — kask [D-AK] + tutuş beati + iz + ağız
     S61  vizör + hane [D-AL · D-AM]
     S64  kasa [D-AO] + hane
     S67  konuşma + vizör yansıması + iz [D-AR · D-AQ · D-AP]
     S63  ağız hattı + iz + gölge [D-AR · D-AP · D-AT]
     S70  taç pencereleri [D-AT ②] — tek hata, gerisi temiz
     S65  §5 madde 1'in sonucuna göre
     S66  §5 madde 1'in sonucuna göre (baş düze döndü mü)

5b. □ SIKIŞTIRMA GEÇİŞİ [D-AW]: yamalar sonrası promptların sekizi
     uzunluk bandının üstünde (imaj ≤2.300 · video ≤2.600). Bir
     sıkıştırma turu daha yapılır — tekrar silinir, kilit değil.
     Ölçüm komutu bu dosyada D-AW'de.

6. □ SÜRE DOĞRULAMASI [D-AV]: NLE'de 10 klip × 10.00 s; reel
     haritası kanıt sayılmaz. S65/S66 retime (8 s × 0.8) ayrıca.

7. □ İKİNCİ KOŞU: 10 adlandırılmış klip, MODE T, tam çıktı formatı.
     Skor tabanı o koşudur. Bu koşuda hiç ölçülemeyenler orada ilk
     kez ölçülür: S65 özdeşlik, S62 iki yerleştirmenin aynılığı,
     S66 eksik yükseliş, S64 düz ayrılma çizgisi, PHASE CHAIN.
```

---

## 6. FLAGS — dokümandan/operatörden cevaplanacak

```
① S62-S66 neden sırasız gitti? Klipler adlandırılmış mıydı, yoksa
   NLE'ye tarih sırasıyla mı alındı? (§2'nin hipotezi: S62 en çok
   yeniden üretilen sahne olduğu için dosyası en yeni.)
② TETİK KAPISI 2 işletildi mi? R3 BEKÇİ MASTER'ında parmak sayıldı
   mı, sayıldıysa kaç çıktı? Onaylı el karesi S62/S68 üretimine
   start-frame olarak verildi mi?
③ TETİK KAPISI 1 işletildi mi? S62 çapa karesi plaka/plinth ölçeğiyle
   yan yana doğrulandı mı — doğrulandıysa kalın kare blok neden
   geçti?
④ İMAJ ÇİFTİ KAPISI: S61 ve S64 start+END FRAME çiftiyle mi
   üretildi? S68'in END FRAME imajı (kabarma zirvesi) üretildi mi —
   üretildiyse kabarma o karede var mıydı?
⑤ S69'un kabul karesi insan gözüyle kontrol edildi mi? Kaskın
   çıktığı bir kare nasıl kabul edildi [KARAR 5 ⑦ doğrulama adımı]?
⑥ Sahneler kaç denemeyle kabul edildi? S65 için 8 varyasyon bütçesi
   kullanıldı mı?
```

---

## 7. F8+ VE SİSTEME TAŞINANLAR

```
① ÇIKARMA EYLEMİ HEDEF        Yasaklanan parçayı bırakır, en yakın
   DEĞİŞTİRİR                 çıkarılabiliri çıkarır. Çıkarma/açma
   [D-AK → DERS 89]           geçen her sahnede TÜM mühürler tek tek
                              sayılır. ⭐ F8 S80 ÇEHOV 7'nin gerçek
                              ateşlenmesi: orada eldiven ÇIKACAK —
                              kask kilidi oraya açıkça yazıldı.

② MALZEME TARİFİ KADRAJA      Dolu vizör plakası büyük kadrajda
   BAĞIMLI                    tuttu, küçük kadrajda cama döndü.
   [D-AL]                     Malzemeye DEĞER tarifi eklenir
                              ("darkest value in the frame") +
                              geniş kadrajlarda referans start-frame.
                              F8 S77 aynı figürü taşıyor.

③ PROMPT KATMANI TÜKENEN      Dört hane (7 vaka) ve kasa ailesi
   İKİ SINIF                  (2 vaka) prompt diliyle çözülmüyor.
   [D-AM · D-AO]              Çözüm referans/kadraj katmanında:
                              onaylı start-frame, ya da hatanın
                              görüneceği kenarı kadraj dışında
                              bırakmak. F9 aynı dekor + aynı el.

④ MİLİMETRİK OLAY ÜRETİLMEZ   2-3 mm'lik beat modelin eşiğinin
   [D-AN → DERS 90]           altında; F6 S58 dudak vakasıyla sınıf
                              KESİNLEŞTİ (gözlem değil, ders).
                              Sayı korunur, okunurluk kancası
                              (bükülen highlight / kontrast kenar)
                              eklenir; kabul start-end karşılaştırması.

⑤ SINIRLI İZİN KAYBEDİLİR     "hafif yansıma ama gizlemesin" = tam
   [D-AQ → DERS 88]           ayna. F6 ④'ün (iz kaynağını çıkar)
                              optik kardeşi. Prompt taraması: her
                              "faint/subtle/slight X" cümlesi, X
                              yasaklıysa SİLİNİR.

⑥ İZ ÖZELLİĞE ÇAPALANIR       "SOL kaş" yüzün solunda herhangi bir
   [D-AP → DERS 91]           yere gidiyor. Özellik + ölçü + "yüzün
                              geri kalanı temiz" üçlüsü.

⑦ EŞLEME ÇÖKÜNCE SKOR DURUR   Rubrik kaymayı yakalayıp yine de puan
   [D-AU → DERS 92]           yayımladı. MAPPING COLLAPSE kapısı
                              FAZ_07_QA_PROMPT.md'ye işlendi; F8
                              rubriği bu sürümden türetilir.

⑧ TESLİMAT: YEDİDE ALTI       Yazılı kural yedi fazda altı kez
   [§1 · F6 ⑤ tekrarı]        tutmadı; F7'de sıra da bozuldu. Kapı
                              artık iki adımlı: adlandırma + NLE'ye
                              ADA GÖRE alma + kurgu sonrası 10
                              başlıklı içerik kontrolü.
```

---

> **Bu dosya ne zaman güncellenir:** §5 madde 1'in tek-bakış sonucu
> netleşince (S65 özdeşlik + S66 baş yüksekliği), §6'daki kapı
> soruları cevaplanınca, yeniden üretimler bitince, ve 10 adlandırılmış
> klip MODE T ile ikinci kez koşulunca — skor tabanı o koşudur.
