# 🎈 LOSS OF LIFT — Kaldırma Kaybı | PART A

## AI Production Bible — Self-Contained Prompts
### PART A: Sahne 0-12 (13 sahne) | 16:9 Yatay | Görsel + Video
### _"Bir şeyin yükselmesi için senin inmen gerekir."_

> **PART A süresi:** Hook (9s) + 12 sahne × 10s = 129 saniye
> **Toplam film:** 25 sahne = 249 saniye = 4 dakika 09 saniye
> **PART B:** `LOSS_OF_LIFT_PART_B.md` (S13-S24) — henüz yazılmadı
> **Plan:** `LOSS_OF_LIFT_PLAN.md` — QA SPEC, risk kartları, ışık takvimi orada
> **PART A tamamen SESSİZDİR:** 0 replik (filmin tek repliği S22, PART B).

---

## ⚠️ PART A ÜRETİM NOTLARI (promptlardan önce oku)

```
① İNSANSIZ SAHNE (yalnız S0) — YAPISAL RED PROTOKOLÜ
   Cold Burn S8 tetikleyicisi: insansız sahne + uzun NEGATIVE +
   "Exactly 0 human figures" kalıbı → "having a hard time" reddi.
   Azaltım BAŞTAN uygulandı: S0'ın NEGATIVE bloğu KISA, insan imzası
   "Human count in this frame: zero — the one crewman is inside the
   gondola" biçiminde POZİTİF. Red gelirse KILAVUZ_REHBERI §7
   merdiveni: NEGATIVE'i tek Style satırına indir → etiketleri kaldır
   → "human" kelimesini çıkar → 3 satırlık prob → I2V.

② UZUNLUK BANDI — BİLİNÇLİ SAPMA GEREKÇESİ [Blue Drift §② emsali]
   Çapa kuralı kelimesi kelimesine kopya ister (kısaltılamaz) →
   video promptları 2.000-2.600 bandının üstünde kalır; TAVAN
   (~4.300) aşımı SIFIR hedefi tutturuldu. Bant aşımının yapısal
   azaltımı baştan uygulandı: 12 videonun 12'si I2V (onaylı IMAGE
   karesi start frame) ve karakter tarifi videoda KOMPAKT KİLİT
   SATIRINA iner (aşağıda ⑧) — çevre çapaları birebir kalır.
   İLK RED PROTOKOLÜ: önce HATA MESAJI sınıfına bak (§7 tablosu);
   aynı filmde 3 red / 0 başarı görülürse kısaltma değil 3 satırlık
   prob koşulur (Third Dune 5/0 ve Ring Light 3/0 desenleri).
   → prompt_kontrol 20.08.2026: 26 prompt · 0 BLOCK · FIX yalnız
     uzunluk — image 2.258-3.497 (GÖZLEM sınıfı) · video 2.737-3.846
     (bant 2.000-2.600 üstü, gerekçe bu not) · TAVAN (4.300) aşımı
     SIFIR. Kilit imzaları (tek çekim · bloom · metin · insan sayısı ·
     grain · D79 · yön kapıları): 0 bulgu. Parafraz avcısı: 0 şüphe.

③ OKRA-ÜSTÜ-OKRA KAPISI [plan 🃏 ①]
   Filmin 1 numaralı görsel riski. PART A'nın iki testi:
   S0 (küre okra denizden AYRIŞIYOR mu — doku: patch haritası,
   yürüyüş şeridi, gondol panelleri) ve S5 (insan formu parlak
   gölgesiz zeminde okunuyor mu). Okunmazsa HAZIR DÜŞÜŞ: zarf
   kabuğuna 12 m aralıklı KOYU DİKİŞ BANTLARI (prompt V2) —
   yeniden yazım gerekmez, plandaki 🎨 bölümü.

④ ÜRETİM KAPILARI [D74 — kayıtsız kapı koşulmamış kapıdır]
   Sıra: S0 (hovering/ölçek) → S5 (okunurluk) → S20 (PART_B, doruk)
   → S8 (mor patlaması). Her koşu dosya sonundaki KAPI KAYITLARI'na
   TEK SATIR yazılır.

⑤ "HOVERING" ÇAKIŞMASI [plan 🃏 ② · D59]
   Negatif çekirdek "never hovering" der; bu filmin gövdesi gerçekten
   havada durur. Çözüm İKİ AYRI CÜMLE: yasak yalnız PARÇACIKLARA
   ("particles obey 0.904 g — never hovering"), gövdeye POZİTİF durum
   ("floats in neutral buoyancy, settling at a constant 30 meters
   per hour... perfectly still, held by lift"). İki cümle aynı
   promptta ÇELİŞMEZ çünkü özneleri farklı. S0 kapısı bunu test eder.

⑥ ⛔ ÇAPA PARAFRAZ YASAĞI [Blue Drift S1 vakası, 18.08.2026]
   Bir çapa bloğu promptun içine KOPYALANIR, yeniden yazılmaz —
   eşanlamlı bile yasak [SAHNE_DEVAMLILIK §2.1]. Kanıt: Blue Drift
   S1 videosunda gezegen bloğu parafrazdı, ARKA PLAN yeniden uyduruldu.
   Bu dosyada promptlar sabit bloklardan ÜRETEÇLE basıldı (elle
   kopyalanmadı); doğrulama komutu ⚓ bölümünün sonunda.

⑦ BOŞ KABUKLAR (S4) — KLON SICAK NOKTASI [KART 4 · D20]
   Askıdaki üç boş suit kabuğu, tek kişilik filmde modelin ikinci
   insan çizeceği en olası yerdir. Üç katman: kabuklar BAŞSIZ ve
   boyun halkaları BOŞ KARANLIK; gövdede "no face, no figure, no
   body in any of them"; negatifte "no fourth figure exists".
   S4 temiz çıkmazsa DÜŞÜŞ: kabuk sayısı 3→0, yalnız boş askılar
   (LOW POWER S4'ün birebir çözümü — 7 askı 6'sı boş).

⑧ RENK VE KİLİT DİSİPLİNİ
   MOR yalnız S8-S9 (kolon odası) · AMBER yalnız S11 (verici nabzı,
   2 s periyot) · geri kalan her kare OKRA + nötr beyaz servis lambası.
   [D95] vizörün ÜÇ GÖRÜNÜR İŞARETİ (2 cm çerçeve · yaka mühür
   halkası · üst kenarda tek parlama çizgisi) suit'li 4 sahnenin
   IMAGE gövdelerinde tam cümle, VIDEO kilit satırında kısaltılmış.
   [D44] 0.904 g ≥ 0.5g → her videoda "ordinary Earth pace, real
   time, no slow motion". [D43] iki yama sahnesi (S1 · S6) EKLEME
   olarak yazıldı: rijit disk "oturur", yüzey "asla akmaz", alet
   rijit. [D89] tek mühür sayımı S4'te eylemin geçtiği sahnede.
```

---

# 📖 BÖLÜM 1 — THE BIBLES

---

## 🌍 WORLD BIBLE — VENÜS BULUT KATMANI

```
KONUM: Venüs orta bulut katmanı, ~54 km. Basınç ~0.5 bar, dışarısı
%96.5 CO2 + kükürt asidi aerosolü — SOLUNAMAZ ama basınç suit'i
şişirmez: kabuk ASİDE karşı, basınca değil. İç hacim (zarf) normal
hava: SOLUNABILIR ve CO2'den hafif olduğu için KALDIRMA GAZIDIR —
mürettebat, istasyonu havada tutan gazın içinde yaşar.

IŞIK: Güneş DİSKİ HİÇ GÖRÜNMEZ — bulutun içindesin. Işık her yönden,
gölgesiz, parlak. Yukarısı soluk kükürt-sarısı tül, aşağısı koyu
amber-kahve alt güverte. ZEMİN YOK, UFUK GÖLGESİ YOK, MAVİ GÖK YOK —
hiçbir sahnede. Gölgesizlik ÜRETİM HATASI DEĞİL FİZİKTİR [D41'in
yanlış teşhis zemini bu filmde yoktur; bloom yasağı yine de durur].

RÜZGAR: Süper-rotasyon istasyonu taşır → BAĞIL RÜZGAR 0-2 m/s.
Dışarısı cam gibi durgun: kumaş çırpmaz, hiçbir şey savrulmaz,
lanyard yerde ölü yatar. 400 km/s'lik akıntının içinde mutlak
durgunluk — filmin en rahatsız edici fiziği.

BATIŞ: Kaçak ~322 kg/saat → istasyon SABİT 30 m/saat alçalır
(= 0.83 cm/s — tek kadrajda yalnız S12'de, lomboz camına karşı
görünür). 61. gün: ilk 60 gün 11 tüple telafi edildi, tüpler bitti,
batış o zaman başladı. Kalan: TEK TÜP (S10).

SES: Yoğun CO2 + iç hava — tınılar ALÇAK ve KALIN. İçeride sürekli
yatak [D83]: alçak fan uğultusu + zarf gerilme tıkırtıları + kaçağın
İNCE KESİNTİSİZ ISLIĞI (kubbenin yukarısında bir yerde). Dışarıda:
uçsuz yumuşak sessizlik + kask içi nefes + bulut kütlesinin uzak
derin uğultusu ("felt more than heard").

SICAKLIK EKSENİ [plan ışık takvimi]: S0-S2 +35°C · S3-S7 +36°C ·
S8-S12 +40°C. Aşağısı ısı demektir; PART A'da tek görünür ucu S3
buğu/boncuk kanalıdır (S18'de PART_B aynı kadrajda KURU).

YERÇEKİMİ: 0.904 g — Dünya'ya en yakın ikinci gövde. Yürüyüş normal
tempo, düşen nesne ilk saniyede 4.4 m. AĞIR ÇEKİM YASAK [D44]:
her videoda "ordinary Earth pace, real time".
```

---

## 🏗️ STATION BIBLE — TERAZİ İSTASYONU

```
ZARF: 60 m yarı saydam küre, sütsü asit-geçirmez laminat, içeriden
ışık geçirir. Üstünde YÜZLERCE el yaması (patch disc) — okra-üstü-okra
riskine karşı ana doku kanalı. Tepesinden geçen gömme YÜRÜYÜŞ ŞERİDİ
(alçak kramponlu) + ince KILAVUZ RAYI. İç hacim: SOLUNABILIR hava.
GONDOL: kürenin altında kısa kafes boyunda asılı 11 m mat soluk
panelli kutu; yanda TEK YUVARLAK LOMBOZ (rivet çizgili çerçeve —
S12'nin ölçüm kenarı). İçinde: pin yayı · manifold · verici köşesi ·
kolon odası kapısı (kapı hiçbir karede görünmez [D69]).
KOLON ODASI: küçük koyu duvarlı oda; merkezinde 2.4 m × 60 cm mühürlü
cam kolon, berrak sıvıda TEK TEK süzülen soluk iplik demetleri,
tacında menekşe-macenta büyütme lambası — İSTASYONDAKİ TEK MOR IŞIK.
MANİFOLD: 12 yuva · 11 BOŞ açık bilezik · 1 DOLU çelik tüp · tek çelik
kol · iki boru (kalın izoleli YUKARI zarfa · ince YATAY sonda yatağına).
PİN YAYI: 60 cm pirinç çeyrek daire · 24 düz çentik · SIFIR rakam/harf ·
fosfor uçlu ibre · çentik yanı deliklerde pirinç pin izi — üsttekiler
bitişik, alttakiler gitgide seyrek (ilk 60 günün tutunması, son
günlerin hızlanan kaybı — metinsiz tarihçe).
KONDANSER PLAKASI: gondol boynu yanında 1 m² fırçalanmış çelik,
soğutma devresinin parçası; yüzü ince boncuk terli (S3) — PART_B
S18'de AYNI kadrajda KUPKURU.
VERİCİ: köşede küçük korumalı konsol — kapaklı toggle + tek gömme
AMBER tekrarlayıcı lamba (kanal açıkken 2 s'de bir nabız). Yazı yok.
SONDA YATAĞI (PART_B): katlı 12 m yardımcı balon + 250 kg taşıyıcı.
PART A'da kadraja girmez; bağlantısı yalnız manifolddaki ince boru.

ÖLÇEK KİLİDİ: zarf 60 m · gondol 11 m · kolon 2.4 m × 0.6 m · lomboz
~40 cm · pin yayı 60 cm · plaka 1 m · kol ~30 cm · adam 1.79 m.
```

---
## ⚓ ÇAPA BLOKLARI — KANONİK İNGİLİZCE TANIMLAR

```
⚓ KANONİK ÇAPA BLOKLARI [SAHNE_DEVAMLILIK §2.1] Aşağıdaki bloklar
KANONİKTİR: varlık hangi promptta görünüyorsa oraya KELİMESİ
KELİMESİNE kopyalanmıştır — eşanlamlı bile yasak. Sahneye özgü durum
bloktan SONRA ayrı cümleyle gelir; blok değişmez. Bu dosyanın
promptları bu bloklardan ÜRETEÇLE basıldı; parafraz olasılığı sıfır
değil, ölçülü: doğrulama komutu blokların altında.
```

**MAN — CORE (her insanlı IMAGE gövdesine, giyimle birlikte):**
```
the air engineer — a man in his early fifties, 1.79 m, thin, shoulders
slightly stooped, light olive skin with visible pores, sunken cheeks, deep
nasolabial lines, grey-brown eyes ringed with permanent fatigue, short
thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn scar
at his left temple, yellowed nail beds on his right hand
```

**MAN — İÇ MEKÂN SÜRÜMÜ (S1 S2 S3 S8 S9 S10 S11 S12 IMAGE):**
```
the air engineer — a man in his early fifties, 1.79 m, thin, shoulders
slightly stooped, light olive skin with visible pores, sunken cheeks, deep
nasolabial lines, grey-brown eyes ringed with permanent fatigue, short
thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn scar
at his left temple, yellowed nail beds on his right hand; he wears a faded
sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an old
light-grey knitted cardigan with a stretched-open collar; on the jumpsuit's
chest a blank darker rectangle of cloth marks where a patch was once sewn — it
carries no lettering, no emblem, nothing readable
```

**MAN — SUIT SÜRÜMÜ (S4 S5 S6 S7 IMAGE):**
```
the air engineer — a man in his early fifties, 1.79 m, thin, shoulders
slightly stooped, light olive skin with visible pores, sunken cheeks, deep
nasolabial lines, grey-brown eyes ringed with permanent fatigue, short
thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn scar
at his left temple, yellowed nail beds on his right hand; he wears a dirty
sand-white acid-rated hard-shell pressure suit with machined joint rings,
matte and finely scuffed, carrying exactly three fixed acid-bleached pale
zones — across the right shoulder, along the left forearm, over the knees —
identical in every frame; a low-profile sand-white helmet, CLOSED, his face
fully readable through the visor
```

**VİZÖR ÜÇ İŞARET [D95] (suit'li IMAGE gövdelerinde):**
```
The visor is one seamless optically clear pane in a 2-cm brushed-metal frame,
its lower seal ring visible where it meets the collar, one thin unbroken
specular line along its top edge — the glass is always present, never absent.
```

**MAN — VIDEO KİLİT SATIRI · SUIT (S4-S7 VIDEO):**
```
CONTINUITY LOCKS carried from the frame: exactly one human — the air engineer,
early fifties, thin, iron-grey hair, in the sand-white acid-rated hard-shell
pressure suit with its three fixed bleached zones (right shoulder, left
forearm, knees); helmet CLOSED, the visor a clear pane in its 2-cm brushed-
metal frame with the collar seal ring visible and one thin specular line at
its top edge; back silhouette flat.
```

**MAN — VIDEO KİLİT SATIRI · İÇ MEKÂN (iç mekân VIDEO'ları):**
```
CONTINUITY LOCKS carried from the frame: exactly one human — the air engineer,
early fifties, thin, iron-grey hair, grey stubble, in the faded sand-grey
thermal jumpsuit and light-grey knitted cardigan; the darker chest rectangle
stays blank, carrying no lettering.
```

**GÖK/DENİZ (her dış prompta):**
```
the cloud world — an endless ochre cloud sea under a bright sunless sky; the
light comes evenly from every direction, shadowless, with no sun disk, no
beam, no flare; above hangs a paler sulfur-yellow veil, below lies the deep
amber-brown lower deck, and no ground, no horizon shadow and no blue sky exist
anywhere
```

**DURGUNLUK (her dış prompta):**
```
The air is glass-calm: the station drifts with the wind it lives in, so the
relative wind is zero — nothing flutters, nothing sways, nothing is blown.
```

**YÜZERLİK — TAM (S0):**
```
The station floats in neutral buoyancy, settling at a constant 30 meters per
hour — far too slow for the eye; within this shot it is perfectly still, held
by lift, never bobbing, never swinging, never rising.
```

**YÜZERLİK — KISA (S5):**
```
The surface underfoot is perfectly still — the station settles at 30 meters
per hour, far too slow to see; nothing bobs, nothing sways.
```

**İSTASYON — TAM (S0):**
```
the station — a 60-meter translucent spherical envelope of milky acid-proof
laminate, lit through by the even daylight, mapped with hundreds of hand-laid
patch discs in faintly differing shades, a shallow recessed walkway strip with
low cleats and a thin guide rail running over its crown; beneath it, on a
short lattice neck, hangs an 11-meter boxy gondola of matte pale panels with
one round porthole in its flank
```

**TAÇ ALT KÜMESİ (S5 S6 S7):**
```
the crown of the station's envelope — a curving field of milky acid-proof
laminate mapped with hand-laid patch discs, the shallow recessed walkway strip
with low cleats and a thin guide rail running along it
```

**ZARF İÇİ (S1 S3):**
```
the inside of the envelope — a vast dim vault of milky laminate lit through by
even ochre daylight, shadowless, its walls mapped with hundreds of old patch
discs; the breathable lifting air is still, and a thin ceaseless leak-whistle
hangs somewhere far up in the dome
```

**KOLON (S8 S9):**
```
the culture column — a sealed vertical glass cylinder, 2.4 meters tall and 60
centimeters wide, standing in a machined frame, filled with clear liquid in
which pale filament strands drift with slow individual motion; a deep violet-
magenta grow lamp inside its crown floods the room — the only violet light
that exists anywhere on the station
```

**PİN YAYI (S2):**
```
the pin arc — a 60-centimeter quarter-circle of brushed brass bolted to the
wall, cut with 24 plain notches and carrying no numerals, no letters, no
markings of any kind; a phosphor-tipped needle rides along it, and a trail of
small brass pins sits in holes beside the notches above the needle — the
topmost pins almost touching, the lower ones spaced wider and wider apart
```

**MANİFOLD (S10 S12):**
```
the gas manifold — a wall rack of twelve cylinder sockets, eleven of them
empty open collars in a long row, one holding a single full steel cylinder;
beside the rack a single steel lever stands between two pipes — a thick
insulated line climbing up into the envelope, and a thinner line running level
into the probe-bay bulkhead
```

**KONDANSER PLAKASI (S3):**
```
the condenser plate — a one-meter square of brushed steel set into the wall
panel beside the gondola neck, part of the cooling loop, its face beaded with
a fine even film of condensation
```

**I2V BAŞLIK CÜMLESİ (12 videoda):**
```
START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it.
```

**DOĞRULAMA (parafraz avcısı — çıktı boşsa temiz):**
```
python3 - <<'X'
import re
# İngilizce PROMPT bloklarını tarar; Türkçe doküman blokları atlanır.
# I2V videolarda karakter KOMPAKT KİLİT satırı taşır (üretim notu ⑧) —
# "CONTINUITY LOCKS" içeren blokta tam MAN bloğu aranmaz.
KEYS={"cloud world":"endless ochre cloud sea under a bright sunless",
 "culture column":"filled with clear liquid in which pale filament",
 "pin arc":"24 plain notches and carrying no numerals",
 "gas manifold":"eleven of them empty open collars",
 "condenser plate":"beaded with a fine even film of condensation"}
MAN_SIG="sunken cheeks, deep nasolabial lines"
t=open("LOSS_OF_LIFT_PART_A.md").read()
n=0
for b in re.findall(r"```\n(.*?)\n```",t,re.S):
    f=re.sub(r"\s+"," ",b)
    if re.search(r"[ğĞşŞıİçÇöÖüÜ]",f): continue   # doküman bloğu
    for name,sig in KEYS.items():
        if name in f and sig not in f:
            print("PARAFRAZ ŞÜPHESİ:",name,"→",f[:70]); n+=1
    if "air engineer" in f and MAN_SIG not in f and "CONTINUITY LOCKS" not in f:
        print("PARAFRAZ ŞÜPHESİ: air engineer →",f[:70]); n+=1
print("sonuç:",n,"şüphe (0 olmalı)")
X
```

---
## 👤 CHARACTER BIBLE — HAVA MÜHENDİSİ

```
⚠️ PROMPT KURALI: Özel ad promptlara YAZILMAZ [D34] — "the air
engineer". Milliyet ifadesi YASAK (üretim reddi doğrulandı).

ADAM: Erkek, 51, 1.79 m, zayıf, omuzlar hafif düşük. Açık zeytin ten,
görünür gözenek. Çökük yanaklar, derin nazolabial çizgiler. Kalıcı
yorgunluk halkalı gri-kahve gözler. Kısa seyrelmiş kır saç, üç günlük
düzensiz gri sakal. Sol şakakta 4 cm eski yanık izi. Sağ el tırnak
yatakları asitten sarı.

İÇ MEKÂN (10 sahne: S1 S2 S3 S8 S9 S10 S11 S12 + PART_B S14-S20 bloğu):
soluk kum-grisi termal tulum (dirsek/diz aşınmış) + eski açık gri örgü
ceket (yakası genişlemiş) + göğüste SÖKÜLMÜŞ ARMANIN BOŞ KOYU İZİ —
"no lettering, no emblem, nothing readable" gövdede yazılır.

SUIT (4 sahne: S4 S5 S6 S7 + PART_B S21-S23): kirli kum-beyazı asit
kabuğu, işlenmiş eklem halkaları, mat ve ince çizikli. TAM ÜÇ AĞARMIŞ
BÖLGE — sağ omuz · sol ön kol · dizler — SABİT, her karede aynı [D42:
asit kirletmez AĞARTIR; sürüklenecek rastgele desen yok]. Düşük
profilli kum-beyaz kask, KAPALI.

[D95] VİZÖRÜN ÜÇ GÖRÜNÜR İŞARETİ (suit'li her IMAGE gövdesinde tam):
2 cm fırçalanmış metal çerçeve · yakada görünür mühür halkası · üst
kenarda tek kesintisiz parlama çizgisi. "The glass is always present,
never absent."

[D79] SIRT VE VİZÖR KİLİDİ — negatif blokta, suit görünen HER promptta:
sırt ünitesi YOK (düz siluet) · vizör optik berrak, sıfır renklendirme,
sıfır ayna kaplama.

HUMAN COUNT LOCK: Filmde TAM 1 insan. 21 sahnede görünür; S0 S13 S19
S24 insansız. Her prompt karede görünen sayıyı açıkça yazar.

HELMET STATE SCHEDULE (PART A): kapalı kask S4-S7 (4 sahne) · kasksız
S1-S3 ve S8-S12 (8 sahne) · insansız S0. Giyme/çıkarma hareketi 0 kare
— iki geçiş de sahne sınırında (S3→S4 · S7→S8) [D69 ①]. ARA DURUM YOK.
```

---

## 🎥 CAMERA BIBLE

```
KURAL: 25/25 sahne SABİT LOCKOFF. Pan yok, tilt yok, zoom yok, track
yok, kesme yok. Her sahne = tek kesintisiz çekim = ayrı video.

LENS KİLİDİ (küresel/spherical — anamorfik parlama YASAK):
- HOOK havadan (S0)                  → 24mm / 250 m
- GENİŞ (zarf içi, taç, manifold)    → 32mm / 3-9 m
- ORTA (S6 yama · S8 kolon)          → 35mm / 3.5-4 m
- DETAY (S2 yay · S9 avuç · S11)     → 85mm / 1.2-1.6 m

MESAFE: her prompt kamera mesafesini metre cinsinden CÜMLE içinde
yazar ("from a fixed position six meters away") — künye satırı değil
[D45: sayı+harf dizilimi ekrana sızar].

EKRAN YÖNÜ: Bu filmde yatay hedefe hareket YOK — tek eksen DİKEYDİR
(yukarı=gelecek, aşağı=ısı). Baş dönüşleri ekran-uzayında yazılır
("screen-left to screen-right"). D104 mıknatısı yapısal olarak zayıf:
kadrajda baskın tek ışık kaynağı yok (güneş diski görünmez).

SÜRE: Sahne başına 10 s (Hook = 9). ⚠️ Veo 3.1 native 8s üretir:
8s üret + 2s extend. ÜRETİM MODU: 12/12 video I2V — ÖNCE İMAJ
üretilir ve onaylanır, video onaylı kareden koşulur [D84 ① mantığı:
metin sahneler ARASI durumu kilitleyemez, kare kilitler].
```

---

## 💡 LIGHTING BIBLE — TEK RENGİN DİSİPLİNİ

```
PALET: OKRA (dünya) + MOR (yalnız kolon odası) + AMBER (yalnız S11
nabzı) + nötr beyaz servis lambaları (gondol içi). Başka renk YOK.

AİLE 1 — DIŞ / ZARF İÇİ (S0-S7): parlak gölgesiz okra, her yönden.
Gölge YOK ve bu DOĞRU [D41 tersine değil — bloom yine yasak: doku
kaybı yok, ışık kaynağı fiziksel]. S5 filmin en parlak karesi.
AİLE 2 — GONDOL İÇİ (S2 S10 S11 S12): loş; küçük gömme nötr beyaz
servis lambaları + lombozdan giren okra (sahneden sahneye DERİNLEŞİR:
S2 soluk → S10-S12 koyu geç ışık). Pirinç ve çelik lambayı temiz
çizgilerle tutar.
AİLE 3 — KOLON ODASI (S8 S9): TEK kaynak menekşe-macenta büyütme
lambası — YÖNLÜ, net düşüşlü (falloff), her yüzeyde doku. Okra bu
odaya girmez. "glowing/ethereal/radiant/shimmering" YASAK [D29] —
ışık hep fiziksel adla ("the violet-magenta flood of the grow lamp").

İç lamba envanteri sahne başına TEKtir ve promptta sayılıdır
(S2: iki lamba · S4: bir lamba · S10-S12: bir lamba).
```

---

## ⚙️ PHYSICS BIBLE

```
0.904 g: yürüyüş NORMAL TEMPO — her videoda "ordinary Earth pace,
real time, no slow motion" [D44 eşik kuralı: ≥0.5g'de zorunlu].
Negatife: "no slow motion, no floaty movement".

YÜZERLİK [⑤]: gövde cümlesi POZİTİF ("floats in neutral buoyancy,
settling at a constant 30 meters per hour — perfectly still, held by
lift"), parçacık yasağı AYRI ("particles obey 0.904 g — never
hovering, never swirling").

RÜZGAR: bağıl 0 → hiçbir kumaş kıpırdamaz, lanyard ölü yatar [D26:
halat hep GEVŞEK ve STATİK — gergin halat karesi PART A'da yok].

TEMAS [D11/D28/D43]: yama = EKLEME (rijit disk oturur, yüzey asla
yumuşamaz/akmaz, alet rijit) · avuç CAMDA (sıvıya temas 0 — sıvı
mühürlü kolonun içinde) · parmak uçları plakada (S3).

BUĞU: yalnız SOĞUK yüzeyde oluşur ve saniyeler içinde söner; boncuklar
akmaz, büyümez. Isı yükseldikçe kanal ölür (S18, PART_B).

MİKRO-OLAY OKUNURLUĞU [D90]: her küçük olayın ÖLÇEN KENARI yazılıdır —
pin ARALIĞI (S2) · rivet çizgisine karşı sis hattı (S12) · avuca
sürüklenen iplikler (S9) · yarım kalkan el (S10).
```

---
## 🔁 EŞLEŞTİRİLMİŞ KADRAJ ÇİFTİ — S3 ↔ S18 [Hollow Count emsali]

```
S18 (PART_B) bu SETUP'ı BİREBİR kopyalar; tek değişken buğu/boncuk:
SETUP (EN, kanonik): "Low fixed angle from the catwalk floor, camera
fixed seven meters away, 32mm spherical lens, tilted up; the man
small at frame bottom beside the condenser plate at shoulder height."
S3 : plaka boncuklu, nefes buğusu OLUŞUR ve söner.
S18: plaka KUPKURU ("bone-dry"), nefes buğu YAPMAZ. Başka fark yok.
```

---
# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART A: S0-S12)

> ⚡ **Her prompt tamamen bağımsızdır.** Bible'lara bakmanıza gerek yok.
> Sadece istediğiniz sahnenin 📸 veya 🎥 bloğunu kopyalayıp yapıştırın.
> Video promptları I2V içindir: önce IMAGE üretilir, onaylanır, video
> onaylı kareden koşulur.

---

## 🎬 SAHNE 0 (S0) — HOOK — GÖMÜLMEKTE (9 saniye)

> ⛔ ÜRETİM KAPISI 1 [hovering/ölçek]: pozitif yüzerlik cümlesi burada test edilir.
> Küre kıpırdamadan asılı duruyorsa cümle güçlendirilir (plan 🃏 ②).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. High aerial view
inside an endless cloud layer, bright sunless daylight. Human count in this
frame: zero.

SCENE: The camera holds a fixed position 250 meters out and slightly above,
looking gently down. Filling the frame: the cloud world — an endless ochre
cloud sea under a bright sunless sky; the light comes evenly from every
direction, shadowless, with no sun disk, no beam, no flare; above hangs a
paler sulfur-yellow veil, below lies the deep amber-brown lower deck, and no
ground, no horizon shadow and no blue sky exist anywhere. Near frame center
floats the station — a 60-meter translucent spherical envelope of milky acid-
proof laminate, lit through by the even daylight, mapped with hundreds of
hand-laid patch discs in faintly differing shades, a shallow recessed walkway
strip with low cleats and a thin guide rail running over its crown; beneath
it, on a short lattice neck, hangs an 11-meter boxy gondola of matte pale
panels with one round porthole in its flank. The gondola's keel trails through
the first thin wisps of the lower deck's top — the sphere rides clear, but the
small gondola beneath it is already in the mist to its knees. The station
floats in neutral buoyancy, settling at a constant 30 meters per hour — far
too slow for the eye; within this shot it is perfectly still, held by lift,
never bobbing, never swinging, never rising. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown.

CAMERA & LIGHT: Shot on a 24mm spherical lens from a fixed aerial position 250
meters away, f/8. Even shadowless ochre light from every direction; the
sphere's skin reads milky and faintly lit through, its patch map the only fine
texture in a world of soft cloud.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame:
zero — the one crewman is inside the gondola. 0% bloom, no glow filter, no
soft focus — every surface keeps texture. No readable text anywhere; no
subtitles, no title card, no watermark. The envelope and gondola are rigid and
unchanging — no melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
9-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed locked-
off aerial camera, no camera movement. Human count in this frame: zero — the
one crewman is inside the gondola.

SCENE: Fixed aerial position 250 meters out, looking gently down. the cloud
world — an endless ochre cloud sea under a bright sunless sky; the light comes
evenly from every direction, shadowless, with no sun disk, no beam, no flare;
above hangs a paler sulfur-yellow veil, below lies the deep amber-brown lower
deck, and no ground, no horizon shadow and no blue sky exist anywhere. Near
frame center: the station — a 60-meter translucent spherical envelope of milky
acid-proof laminate, lit through by the even daylight, mapped with hundreds of
hand-laid patch discs in faintly differing shades, a shallow recessed walkway
strip with low cleats and a thin guide rail running over its crown; beneath
it, on a short lattice neck, hangs an 11-meter boxy gondola of matte pale
panels with one round porthole in its flank. The gondola's keel trails through
the first thin wisps of the lower deck's top — the sphere rides clear, the
small gondola beneath it already in the mist. The station floats in neutral
buoyancy, settling at a constant 30 meters per hour — far too slow for the
eye; within this shot it is perfectly still, held by lift, never bobbing,
never swinging, never rising. The air is glass-calm: the station drifts with
the wind it lives in, so the relative wind is zero — nothing flutters, nothing
sways, nothing is blown.

TIMELINE: 0.0s — Stillness. The sphere hangs milky and patched against the
ochre; nothing in the frame moves. 3.0s — Far below, one vast slow swell rises
in the deck and flattens again — kilometer-scale, ponderous, silent. 6.0s — A
single thin wisp of deck mist slides past the gondola keel and stays. 9.0s —
Nothing else has moved. Hold on the last frame.

AUDIO: A deep, soft, low cloud-mass murmur, felt more than heard; thin distant
air-hiss; all tones low and thickened by the dense air. No voice, no music.

PHYSICS: 0.904 g. Neutral buoyancy — the station settles at a constant 30
meters per hour, invisible within this shot. Relative wind zero: nothing
flutters.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Human count in this frame: zero — the one crewman is inside the gondola.
0% bloom, no glow filter, no soft focus — every surface keeps texture. No
readable text anywhere; no subtitles, no title card, no watermark. The cloud
deck moves only as one slow vast mass — never fast, never turbulent; loose
particles obey 0.904 g, never hovering, never swirling. The envelope and
gondola are rigid and unchanging — no melting, no warping. Real time — no slow
motion. No speech, no voice, no music. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```


---

## 🎬 SAHNE 1 (S1) — YAMA

> [D43] temas-morph kilidi: yama EKLEME olarak yazıldı (rijit disk 'oturur'),
> yüzey 'değişmez'; alet ayrıca rijit kilitli. [D44] real time cümlesi gövdede.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a vast
translucent balloon vault, even ochre daylight. Exactly one human figure —
this film has exactly one human total.

SCENE: the inside of the envelope — a vast dim vault of milky laminate lit
through by even ochre daylight, shadowless, its walls mapped with hundreds of
old patch discs; the breathable lifting air is still, and a thin ceaseless
leak-whistle hangs somewhere far up in the dome. Kneeling on the narrow
service catwalk at the base of the wall: the air engineer — a man in his early
fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin with
visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes ringed
with permanent fatigue, short thinning iron-grey hair, patchy three-day grey
stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on his
right hand; he wears a faded sand-grey thermal jumpsuit, worn thin at the
elbows and knees, under an old light-grey knitted cardigan with a stretched-
open collar; on the jumpsuit's chest a blank darker rectangle of cloth marks
where a patch was once sewn — it carries no lettering, no emblem, nothing
readable. He presses a short hand roller-iron onto a fresh pale patch disc on
the inner skin; around and above the new disc, dozens of older discs in
faintly differing shades climb the wall like a map of old wounds. The roller
is a rigid solid tool of fixed shape. The disc is a rigid pre-formed piece
that adheres as one whole — the skin beneath it stays solid, never softening,
never flowing.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position six meters
away at chest height, f/5.6. Even shadowless ochre light through the skin; his
face lit soft and flat, pores visible.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): the inside of the envelope — a vast dim vault
of milky laminate lit through by even ochre daylight, shadowless, its walls
mapped with hundreds of old patch discs; the breathable lifting air is still,
and a thin ceaseless leak-whistle hangs somewhere far up in the dome. Kneeling
on the catwalk at the wall's base: the air engineer. A fresh pale patch disc
sits on the inner skin under his roller-iron; dozens of older discs climb the
wall above. Camera fixed six meters away, 32mm spherical lens, chest height.

TIMELINE: 0.0s — He holds the roller against the disc's lower edge, weighted,
ordinary Earth pace. 2.5s — One slow firm pass across the disc; it seats as
one rigid whole; a hair-thin darker adhesive line appears at its rim. The skin
beneath never softens, never flows; the roller never bends. 5.5s — A second
pass along the other edge, slower. 8.0s — He sits back on his heels and tilts
his head up along the vault — the patch map rising away above him. 10.0s —
Hold.

AUDIO: Low fan hum, sparse creak-ticks from the envelope skin, and the thin
ceaseless whistle of the leak far up in the dome — all tones low and thickened
by the dense air. No voice, no music.

PHYSICS: 0.904 g — Earth-normal weight; he moves at ordinary Earth pace, real
time, no slow motion. The dense air is still; nothing flutters.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The tool and the patch stay rigid — the wall surface never melts,
morphs or flows at the contact point.
```


---

## 🎬 SAHNE 2 (S2) — PİN YAYI — KATALİZÖR

> [D90] milimetrik olayın ölçen kenarı: pin ARALIĞI (en geniş boşluk) + klik
> sesi. [A1/D50] yay rakamsızdır — çentik ve pin konumu tek kanal.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Dim gondola
interior, close on a brass instrument, one man in profile. Exactly one human
figure — this film has exactly one human total.

SCENE: Filling the left half of the frame: the pin arc — a 60-centimeter
quarter-circle of brushed brass bolted to the wall, cut with 24 plain notches
and carrying no numerals, no letters, no markings of any kind; a phosphor-
tipped needle rides along it, and a trail of small brass pins sits in holes
beside the notches above the needle — the topmost pins almost touching, the
lower ones spaced wider and wider apart. In the right half, in profile, lit by
a small recessed neutral-white service lamp: the air engineer — a man in his
early fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin with
visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes ringed
with permanent fatigue, short thinning iron-grey hair, patchy three-day grey
stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on his
right hand; he wears a faded sand-grey thermal jumpsuit, worn thin at the
elbows and knees, under an old light-grey knitted cardigan with a stretched-
open collar; on the jumpsuit's chest a blank darker rectangle of cloth marks
where a patch was once sewn — it carries no lettering, no emblem, nothing
readable. He holds a single small brass pin between right thumb and
forefinger, poised at the empty hole beside the needle — a full notch below
the lowest pin in the trail, the widest gap on the arc. The phosphor tip of
the needle is a steady pale point.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.2
meters away, f/4. Two small neutral-white service lamps and a faint ochre
spill from the porthole; the brass catches the lamplight in clean unbroken
lines.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The arc carries notches only — no numerals, no letters, no scale
markings of any kind appear on it or anywhere else.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): the pin arc — a 60-centimeter quarter-circle of
brushed brass bolted to the wall, cut with 24 plain notches and carrying no
numerals, no letters, no markings of any kind; a phosphor-tipped needle rides
along it, and a trail of small brass pins sits in holes beside the notches
above the needle — the topmost pins almost touching, the lower ones spaced
wider and wider apart. The man in profile at frame right: the air engineer.
Camera fixed 1.2 meters away, 85mm spherical lens. Two neutral-white service
lamps; brass catching the light in clean lines.

TIMELINE: 0.0s — His right hand holds the small brass pin at the empty hole
beside the needle — one full notch below the lowest pin, the widest gap on the
arc. 2.5s — He presses the pin home. It seats with a single clean movement;
the gap it closes is visibly wider than every gap above it. 5.0s — His thumb
rests on the pin head. His eyes travel up the trail: pins nearly touching at
the top, spreading wider and wider toward his hand. 7.5s — The hand drops
away. The phosphor needle-tip holds steady, a pale point below the new pin.
10.0s — Hold on the arc and his still profile.

AUDIO: One soft brass click at 2.5s, carried dull through the wall; low fan
hum; the thin leak-whistle above; all tones low and thickened. No voice, no
music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The pin is
rigid; the arc is rigid; nothing bends or flows.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The arc carries plain notches only — no numerals, no letters, no
scale markings anywhere.
```


---

## 🎬 SAHNE 3 (S3) — NE SOLUYORSA O TUTUYOR

> ⭐ EŞLEŞTİRİLMİŞ KADRAJ ÇİFTİNİN İLK YARISI [Hollow Count emsali]: S18 (PART_B)
> aynı SETUP/CAMERA ile açılır, tek değişken BUĞU+boncuk (kilit: Bible'da).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Low-angle interior
of a vast translucent vault, a small man beside a steel plate. Exactly one
human figure — this film has exactly one human total.

SCENE: Low angle from the catwalk floor: the inside of the envelope — a vast
dim vault of milky laminate lit through by even ochre daylight, shadowless,
its walls mapped with hundreds of old patch discs; the breathable lifting air
is still, and a thin ceaseless leak-whistle hangs somewhere far up in the
dome. At frame bottom, small against the towering vault, stands the air
engineer — a man in his early fifties, 1.79 m, thin, shoulders slightly
stooped, light olive skin with visible pores, sunken cheeks, deep nasolabial
lines, grey-brown eyes ringed with permanent fatigue, short thinning iron-grey
hair, patchy three-day grey stubble, a 4-cm old burn scar at his left temple,
yellowed nail beds on his right hand; he wears a faded sand-grey thermal
jumpsuit, worn thin at the elbows and knees, under an old light-grey knitted
cardigan with a stretched-open collar; on the jumpsuit's chest a blank darker
rectangle of cloth marks where a patch was once sewn — it carries no
lettering, no emblem, nothing readable. Beside him at shoulder height: the
condenser plate — a one-meter square of brushed steel set into the wall panel
beside the gondola neck, part of the cooling loop, its face beaded with a fine
even film of condensation. He leans toward it, lips parted mid-breath; a soft
bloom of breath-fog spreads on the cold steel among the beads. Above him the
vault recedes upward, patch discs shrinking with distance — sixty meters of
the air he breathes, which is also the only thing holding the station up.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed low position seven
meters away, f/5.6, tilted up. Even shadowless ochre daylight through the
skin.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): Low fixed angle: the inside of the envelope — a
vast dim vault of milky laminate lit through by even ochre daylight,
shadowless, its walls mapped with hundreds of old patch discs; the breathable
lifting air is still, and a thin ceaseless leak-whistle hangs somewhere far up
in the dome. The man small at frame bottom beside the steel plate: the air
engineer. At his shoulder: the condenser plate — a one-meter square of brushed
steel set into the wall panel beside the gondola neck, part of the cooling
loop, its face beaded with a fine even film of condensation. Camera fixed
seven meters away, 32mm spherical lens, tilted up.

TIMELINE: 0.0s — He stands still before the plate, the vault towering over
him. 2.0s — He leans in and exhales once. Breath-fog blooms on the cold steel,
a soft grey oval among the condensation beads. 4.5s — The fog thins and fades;
the fine beads stay. He watches it go. 7.0s — He lays two fingertips lightly
on the plate's edge — clean contact, clear boundary — and holds them there.
10.0s — Hold: the man, the beaded plate, the sixty-meter vault of breathable
air above.

AUDIO: Low fan hum; sparse creak-ticks; the thin ceaseless leak-whistle far
above; one close soft human exhale at 2.0s. All tones low and thickened. No
voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The dense
air is still. Breath-fog forms only on the cold plate and fades within
seconds; the beads never run, never grow.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The fingertips rest ON the steel — they never sink into or merge
with it.
```


---

## 🎬 SAHNE 4 (S4) — DÖRT ASKI

> [D89] TEK MÜHÜR SAYIMI eylem sahnesine yazıldı (karabina KAPANIR, hiçbir mühür
> açılmaz). [KART 4] boş kabuklar = klon sıcak noktası; negatif çift katmanlı.
> [D69 ①] kask giyme hareketi 0 kare — sahne mühürlü açılır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Cramped suiting
alcove below a balloon vault, warm dim light. Exactly one human figure — this
film has exactly one human total.

SCENE: A narrow alcove at the gondola neck. On the wall, a rack of four heavy
hooks: three of them hold empty sand-white pressure-shell forms hanging limp
and hollow, their open neck rings showing nothing but shadowed emptiness
inside — no face, no figure, no body in any of them; the fourth hook is bare.
Facing the rack, already dressed, stands the air engineer — a man in his early
fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin with
visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes ringed
with permanent fatigue, short thinning iron-grey hair, patchy three-day grey
stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on his
right hand; he wears a dirty sand-white acid-rated hard-shell pressure suit
with machined joint rings, matte and finely scuffed, carrying exactly three
fixed acid-bleached pale zones — across the right shoulder, along the left
forearm, over the knees — identical in every frame; a low-profile sand-white
helmet, CLOSED, his face fully readable through the visor. The visor is one
seamless optically clear pane in a 2-cm brushed-metal frame, its lower seal
ring visible where it meets the collar, one thin unbroken specular line along
its top edge — the glass is always present, never absent. A thin coiled
lanyard hangs from a cleat beside the rack, its carabiner closed.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position four
meters away at chest height, f/5.6. One recessed neutral-white service lamp
above the rack; soft ochre daylight spilling down the neck from the vault
above.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The three hanging shells
are empty equipment — no face, no head, no body, no fourth figure anywhere.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): The suiting alcove: four hooks, three limp
empty sand-white shells with open neck rings and hollow darkness inside, one
bare hook. Standing before them, already sealed: the air engineer. The coiled
lanyard hangs from its cleat.

TIMELINE: 0.0s — He stands still before the rack. He does not look at the
empty shells. 2.5s — He lifts the coiled lanyard off the cleat with his right
glove — one object, one motion, ordinary pace. 5.0s — He clips its carabiner
to the ring on his chest plate: one clean click. EXACTLY ONE FASTENER IS
TOUCHED IN THIS SHOT AND IT CLOSES — every seal on the suit stays closed in
every frame: helmet locked, collar ring closed, both gloves on. No seal opens;
no bare skin appears at any second. 7.5s — He turns his upper body away from
the rack, lanyard coiled in his glove. The empty shells hang without moving.
10.0s — Hold.

AUDIO: One soft metallic click at 5.0s; the low fan hum below; his slow
breathing inside the closed helmet. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The hanging
shells are limp dead weight; they never stir.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The three hanging shells
stay empty and motionless — no face, no head, no body appears in or behind
them; no fourth figure exists.
```


---

## 🎬 SAHNE 5 (S5) — VİRAL #1 — SIRT

> ⛔ ÜRETİM KAPISI 2 [okra-üstü-okra okunurluk]: form okunmazsa HAZIR DÜŞÜŞ —
> zarfa 12 m aralıklı koyu dikiş bantları (plan 🃏 ①). [D26] lanyard STATİK
> gevşek yazıldı, dinamik halat karesi yok.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man standing on
top of a vast translucent balloon inside an endless cloud world. Exactly one
human figure — this film has exactly one human total.

SCENE: the crown of the station's envelope — a curving field of milky acid-
proof laminate mapped with hand-laid patch discs, the shallow recessed walkway
strip with low cleats and a thin guide rail running along it. Standing mid-
frame on the walkway strip, small against the sky: the air engineer — a man in
his early fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin
with visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes
ringed with permanent fatigue, short thinning iron-grey hair, patchy three-day
grey stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on
his right hand; he wears a dirty sand-white acid-rated hard-shell pressure
suit with machined joint rings, matte and finely scuffed, carrying exactly
three fixed acid-bleached pale zones — across the right shoulder, along the
left forearm, over the knees — identical in every frame; a low-profile sand-
white helmet, CLOSED, his face fully readable through the visor. The visor is
one seamless optically clear pane in a 2-cm brushed-metal frame, its lower
seal ring visible where it meets the collar, one thin unbroken specular line
along its top edge — the glass is always present, never absent. His thin
lanyard runs from his chest ring to the guide rail and lies slack along the
walkway, motionless. Around him in every direction: the cloud world — an
endless ochre cloud sea under a bright sunless sky; the light comes evenly
from every direction, shadowless, with no sun disk, no beam, no flare; above
hangs a paler sulfur-yellow veil, below lies the deep amber-brown lower deck,
and no ground, no horizon shadow and no blue sky exist anywhere. The laminate
underfoot is faintly translucent — the dim vault-light of the envelope's
interior reads softly through it between the patch discs. The surface
underfoot is perfectly still — the station settles at 30 meters per hour, far
too slow to see; nothing bobs, nothing sways. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position nine
meters along the walkway at chest height, f/8. The brightest frame of the
film: even shadowless ochre light from everywhere, no sun disk, no shadow
under him at all.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): the crown of the station's envelope — a curving
field of milky acid-proof laminate mapped with hand-laid patch discs, the
shallow recessed walkway strip with low cleats and a thin guide rail running
along it. Mid-frame on the walkway: the air engineer. The lanyard lies slack
from his chest ring to the guide rail. In every direction: the cloud world —
an endless ochre cloud sea under a bright sunless sky; the light comes evenly
from every direction, shadowless, with no sun disk, no beam, no flare; above
hangs a paler sulfur-yellow veil, below lies the deep amber-brown lower deck,
and no ground, no horizon shadow and no blue sky exist anywhere. The surface
underfoot is perfectly still — the station settles at 30 meters per hour, far
too slow to see; nothing bobs, nothing sways. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown. Camera fixed nine meters
away on the walkway, 32mm spherical lens, chest height.

TIMELINE: 0.0s — He stands still. An endless ochre sea in every direction; no
shadow falls from him. 2.5s — He turns his head slowly across the horizon,
screen-left to screen-right, taking three full seconds. 5.5s — One small step
forward along the walkway — weighted, ordinary Earth pace; the slack lanyard
slides a hand's width and lies still again. 8.0s — He stops. Stillness returns
completely. 10.0s — Hold.

AUDIO: Vast soft quiet; his own slow breathing inside the helmet; beneath it
the deep distant murmur of the cloud mass below, felt more than heard. No
voice, no music.

PHYSICS: 0.904 g — grounded, weighted steps at ordinary Earth pace, real time,
no slow motion. Relative wind zero: the lanyard never lifts, nothing flutters.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. No ground, no surface and
no object exists below the cloud deck — nothing emerges from it.
```


---

## 🎬 SAHNE 6 (S6) — DIŞ YAMA

> [D43] alet+disk+yüzey üçlü rijit kilit (Slow Stone kazıyıcı vakasının önlemi).
> Asit çiçeği = AĞARMIŞ rozet — leke değil, renk kaybı (asit kirletmez ağartır).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close work scene on
the curved top of a translucent balloon, endless clouds behind. Exactly one
human figure — this film has exactly one human total.

SCENE: the crown of the station's envelope — a curving field of milky acid-
proof laminate mapped with hand-laid patch discs, the shallow recessed walkway
strip with low cleats and a thin guide rail running along it. Kneeling on the
walkway over a fresh acid bloom — a pale bleached rosette the size of a spread
hand, faintly etched into the laminate: the air engineer — a man in his early
fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin with
visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes ringed
with permanent fatigue, short thinning iron-grey hair, patchy three-day grey
stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on his
right hand; he wears a dirty sand-white acid-rated hard-shell pressure suit
with machined joint rings, matte and finely scuffed, carrying exactly three
fixed acid-bleached pale zones — across the right shoulder, along the left
forearm, over the knees — identical in every frame; a low-profile sand-white
helmet, CLOSED, his face fully readable through the visor. The visor is one
seamless optically clear pane in a 2-cm brushed-metal frame, its lower seal
ring visible where it meets the collar, one thin unbroken specular line along
its top edge — the glass is always present, never absent. His left glove
steadies a rigid pre-formed patch disc over the rosette; his right glove holds
the short roller-iron, a rigid solid tool of fixed shape. His slack lanyard
lies motionless along the walkway to the rail. Behind and beyond the crown's
curve: the cloud world — an endless ochre cloud sea under a bright sunless
sky; the light comes evenly from every direction, shadowless, with no sun
disk, no beam, no flare; above hangs a paler sulfur-yellow veil, below lies
the deep amber-brown lower deck, and no ground, no horizon shadow and no blue
sky exist anywhere. The air is glass-calm: the station drifts with the wind it
lives in, so the relative wind is zero — nothing flutters, nothing sways,
nothing is blown.

CAMERA & LIGHT: Shot on a 35mm spherical lens from a fixed position four
meters away, low over the crown, f/5.6. Even shadowless ochre light; the
bleached rosette reads paler than the laminate around it.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): the crown of the station's envelope — a curving
field of milky acid-proof laminate mapped with hand-laid patch discs, the
shallow recessed walkway strip with low cleats and a thin guide rail running
along it. Kneeling over the pale bleached rosette: the air engineer. Left
glove on the rigid patch disc, right glove on the rigid roller-iron; lanyard
slack to the rail. Beyond the curve: the cloud world — an endless ochre cloud
sea under a bright sunless sky; the light comes evenly from every direction,
shadowless, with no sun disk, no beam, no flare; above hangs a paler sulfur-
yellow veil, below lies the deep amber-brown lower deck, and no ground, no
horizon shadow and no blue sky exist anywhere. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown. Camera fixed four meters
away, 35mm spherical lens.

TIMELINE: 0.0s — He holds the disc centered over the rosette, still. 2.5s — He
lays the disc down onto the laminate — it seats as one rigid whole, a discrete
piece on a solid surface. 5.0s — One slow firm roller pass across the disc; a
hair-thin darker adhesive line appears at its rim. The laminate beneath never
softens, never flows; the roller never bends. 7.5s — A second slower pass. His
gloves stay separate from tool and disc — clear boundaries throughout. 10.0s —
Hands still on the finished patch. Hold.

AUDIO: His slow breathing inside the helmet; the faint dull pressure of the
roller carried through the structure; beneath everything the deep distant
cloud murmur. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. Relative
wind zero: nothing flutters, the lanyard never moves.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The tool and the patch
stay rigid — the laminate never melts, morphs or flows at the contact point.
```


---

## 🎬 SAHNE 7 (S7) — AŞINMA

> [D38 mantığı] hasar SAYILI ve sınırlı: TAM 10 rozet, sayı kilitli. Duygusal
> vuruş S6↔S7 çifti: bir yama ↔ on yara.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man standing on
the curved top of a vast translucent balloon, looking along its surface.
Exactly one human figure — this film has exactly one human total.

SCENE: the crown of the station's envelope — a curving field of milky acid-
proof laminate mapped with hand-laid patch discs, the shallow recessed walkway
strip with low cleats and a thin guide rail running along it. He stands beside
the freshly finished patch disc, head turned to follow the crown's long curve:
the air engineer — a man in his early fifties, 1.79 m, thin, shoulders
slightly stooped, light olive skin with visible pores, sunken cheeks, deep
nasolabial lines, grey-brown eyes ringed with permanent fatigue, short
thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn scar
at his left temple, yellowed nail beds on his right hand; he wears a dirty
sand-white acid-rated hard-shell pressure suit with machined joint rings,
matte and finely scuffed, carrying exactly three fixed acid-bleached pale
zones — across the right shoulder, along the left forearm, over the knees —
identical in every frame; a low-profile sand-white helmet, CLOSED, his face
fully readable through the visor. The visor is one seamless optically clear
pane in a 2-cm brushed-metal frame, its lower seal ring visible where it meets
the collar, one thin unbroken specular line along its top edge — the glass is
always present, never absent. Along the curve beyond him, TEN more pale
bleached rosettes dot the laminate — small, scattered, each the size of a
spread hand, fading toward the far slope. More wounds than patches. His
lanyard lies slack to the rail. Beyond everything: the cloud world — an
endless ochre cloud sea under a bright sunless sky; the light comes evenly
from every direction, shadowless, with no sun disk, no beam, no flare; above
hangs a paler sulfur-yellow veil, below lies the deep amber-brown lower deck,
and no ground, no horizon shadow and no blue sky exist anywhere. The air is
glass-calm: the station drifts with the wind it lives in, so the relative wind
is zero — nothing flutters, nothing sways, nothing is blown.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position eight
meters away at chest height, f/8. Even shadowless ochre light; the rosettes
read as pale flecks against the milky laminate.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. Exactly ten distant
rosettes — the count never changes.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): the crown of the station's envelope — a curving
field of milky acid-proof laminate mapped with hand-laid patch discs, the
shallow recessed walkway strip with low cleats and a thin guide rail running
along it. He stands beside the finished patch: the air engineer. Along the
curve, TEN pale bleached rosettes dot the laminate, small and scattered.
Lanyard slack to the rail. Beyond: the cloud world — an endless ochre cloud
sea under a bright sunless sky; the light comes evenly from every direction,
shadowless, with no sun disk, no beam, no flare; above hangs a paler sulfur-
yellow veil, below lies the deep amber-brown lower deck, and no ground, no
horizon shadow and no blue sky exist anywhere. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown. Camera fixed eight meters
away, 32mm spherical lens.

TIMELINE: 0.0s — He stands over the new patch, head down, hands at his sides.
2.5s — He raises his head and turns it slowly along the crown's curve, screen-
left to screen-right. 5.0s — His gaze holds on the field of rosettes — ten
pale flecks between here and the far slope, none of them patched. 7.5s — His
gloved hands open slightly at his sides, then simply hang. 10.0s — He does not
move again. Hold.

AUDIO: His breathing inside the helmet, slower than before; the deep distant
cloud murmur; nothing else. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. Relative
wind zero: nothing flutters, nothing moves but the man.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. Exactly ten distant
rosettes — none appear, none vanish, the count never changes.
```


---

## 🎬 SAHNE 8 (S8) — AKCİĞER — İLK RENK

> ⛔ ÜRETİM KAPISI 3 [mor patlaması]: filmin ikinci rengi burada test edilir.
> [D69] sahne odanın İÇİNDE açılır, kapı/giriş 0 kare. [D29] anti-bloom:
> 'glowing' ailesi yok — ışık 'directional, clear falloff' olarak pozitif.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A small dark room
flooded with deep violet light from a glass column. Exactly one human figure —
this film has exactly one human total.

SCENE: A small dark-walled room. Filling its center: the culture column — a
sealed vertical glass cylinder, 2.4 meters tall and 60 centimeters wide,
standing in a machined frame, filled with clear liquid in which pale filament
strands drift with slow individual motion; a deep violet-magenta grow lamp
inside its crown floods the room — the only violet light that exists anywhere
on the station. The violet-magenta light is directional with clear falloff —
bright on the glass, dimming fast into the room's corners; every lit surface
keeps full texture. Standing one meter from the glass, his face and cardigan
washed in violet: the air engineer — a man in his early fifties, 1.79 m, thin,
shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. His breath
moves his shoulders; warm humidity films the air. This is the first and only
room of the station where any color other than ochre exists.

CAMERA & LIGHT: Shot on a 35mm spherical lens from a fixed position 3.5 meters
away at chest height, f/4. Single source: the grow lamp in the column's crown.
No ochre light reaches this room.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The violet light stays directional with hard falloff — no haze, no
halo. The filaments drift as discrete individual strands — never as a
connected mass.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): The small dark room; at its center the culture
column — a sealed vertical glass cylinder, 2.4 meters tall and 60 centimeters
wide, standing in a machined frame, filled with clear liquid in which pale
filament strands drift with slow individual motion; a deep violet-magenta grow
lamp inside its crown floods the room — the only violet light that exists
anywhere on the station. One meter from the glass, washed in violet: the air
engineer. Camera fixed 3.5 meters away, 35mm spherical lens, chest height.
Single light source: the grow lamp; directional, clear falloff, full texture
on every surface.

TIMELINE: 0.0s — He stands still before the column. Inside the glass, the pale
strands drift with slow individual motion, each on its own path. 3.0s — The
strand nearest the glass slowly rotates, catching the lamp light along its
length. 5.5s — He leans closer, his face moving fully into the violet light.
His breath deepens; his shoulders rise and fall. 8.0s — Stillness — the man
outside the glass, the drifting strands inside it, nothing else in the world.
10.0s — Hold.

AUDIO: A soft liquid circulation murmur from the column's base; a low pump
tick every few seconds; his slow breathing. All tones low and thickened. No
voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The strands
move only inside the sealed liquid, slow and individual; the glass and frame
are rigid.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The violet light stays directional with hard falloff — no haze, no
halo. The filaments drift as discrete individual strands — never as a
connected mass, never fast.
```


---

## 🎬 SAHNE 9 (S9) — CAM — TEK TEMAS

> [D11/D28] temas kilidi: avuç CAMDA, sıvı temas 0 (plan KART 1 kararı).
> [D90] görünmez şeyin (sıcaklık) ölçen kenarı: iplikler avuca sürüklenir.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close shot: a bare
hand flat on the glass of a violet-lit culture column. Exactly one human
figure — this film has exactly one human total.

SCENE: Close on the glass wall of the culture column — a sealed vertical glass
cylinder, 2.4 meters tall and 60 centimeters wide, standing in a machined
frame, filled with clear liquid in which pale filament strands drift with slow
individual motion; a deep violet-magenta grow lamp inside its crown floods the
room — the only violet light that exists anywhere on the station. Flat against
the outside of the glass: the bare right hand of the air engineer — a man in
his early fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin
with visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes
ringed with permanent fatigue, short thinning iron-grey hair, patchy three-day
grey stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on
his right hand; he wears a faded sand-grey thermal jumpsuit, worn thin at the
elbows and knees, under an old light-grey knitted cardigan with a stretched-
open collar; on the jumpsuit's chest a blank darker rectangle of cloth marks
where a patch was once sewn — it carries no lettering, no emblem, nothing
readable. The palm rests ON the glass with a clean structural boundary — skin
pressed slightly pale at the contact, every pore and crease sharp in the
violet light, the cardigan sleeve pushed up his forearm. Inside the glass,
centimeters from his palm, the pale strands hang in the liquid. His face is a
soft out-of-focus shape beyond the hand.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.6
meters away, f/2.8, focus on the hand and the glass plane. Single source: the
violet-magenta grow lamp, directional, clear falloff.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The hand stays OUTSIDE the sealed glass — it never touches the
liquid; palm and glass keep a clean boundary, the glass rigid and unbroken.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): Close on the glass of the culture column — a
sealed vertical glass cylinder, 2.4 meters tall and 60 centimeters wide,
standing in a machined frame, filled with clear liquid in which pale filament
strands drift with slow individual motion; a deep violet-magenta grow lamp
inside its crown floods the room — the only violet light that exists anywhere
on the station. The bare right hand of the air engineer — held a few
centimeters off the glass at 0s, sleeve pushed up. Camera fixed 1.6 meters
away, 85mm spherical lens, focus on the glass plane.

TIMELINE: 0.0s — The open hand waits just off the glass, fingers relaxed. 2.0s
— The palm settles flat onto the glass — clean contact, skin pressing slightly
pale, a clear structural boundary between hand and pane. 4.5s — Inside the
liquid, the strands nearest his palm lean and drift toward the warm patch of
glass, slow and individual — the warmth of the hand read only through their
motion. 7.5s — His thumb shifts one centimeter; over the next seconds the
nearest strands follow. 10.0s — Hold: the hand, the glass, the gathered
strands.

AUDIO: The soft circulation murmur; the low pump tick; his breathing close and
slow. No voice, no music.

PHYSICS: 0.904 g. Real time, no slow motion. The hand never enters the liquid;
the glass never flexes; the strands move only inside the sealed column,
slowly, each on its own path.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The palm rests ON the rigid glass — fingers never sink into, merge
with or pass through it; the strands never touch the hand and never form a
connected mass.
```


---

## 🎬 SAHNE 10 (S10) — HESAP — ORTA NOKTA

> [B2 hazırlığı] seçim geometrisi tek kadrajda kurulur: 11 boş + 1 dolu + kol +
> iki boru. Yarım kalkan el = dokunulmayan karar [D90 okunur mikro-beat].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man before a wall
rack of gas cylinders in a dim gondola. Exactly one human figure — this film
has exactly one human total.

SCENE: Filling the frame: the gas manifold — a wall rack of twelve cylinder
sockets, eleven of them empty open collars in a long row, one holding a single
full steel cylinder; beside the rack a single steel lever stands between two
pipes — a thick insulated line climbing up into the envelope, and a thinner
line running level into the probe-bay bulkhead. Standing before it in profile,
lit by a recessed neutral-white service lamp and the deepening ochre from the
porthole behind him: the air engineer — a man in his early fifties, 1.79 m,
thin, shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. His eyes
rest on the single full cylinder. The eleven empty collars read as a long row
of open mouths; the one cylinder stands among them like the last tooth. The
lever between the two pipes is centered at his chest height, untouched.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position four
meters away at chest height, f/5.6. Neutral lamp on brushed steel; the ochre
through the porthole warmer and deeper than before — late light.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The rack carries no numerals, no letters, no markings; eleven
collars stay empty, one cylinder only — the count never changes.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): the gas manifold — a wall rack of twelve
cylinder sockets, eleven of them empty open collars in a long row, one holding
a single full steel cylinder; beside the rack a single steel lever stands
between two pipes — a thick insulated line climbing up into the envelope, and
a thinner line running level into the probe-bay bulkhead. The man in profile
before it: the air engineer. Camera fixed four meters away, 32mm spherical
lens, chest height. Neutral lamp; deepening ochre from the porthole.

TIMELINE: 0.0s — He stands still before the rack, arms at his sides. 2.5s —
His head turns slowly along the row of eleven empty collars, one by one,
screen-left to screen-right. 5.0s — His gaze settles: the single full cylinder
— then the lever — then the two pipes it stands between, one climbing, one
running level. 7.5s — His right hand half-rises from his side and stops in
mid-air, short of the lever. 9.0s — The hand lowers again. He has touched
nothing. 10.0s — Hold.

AUDIO: Low fan hum; the thin leak-whistle, faint through the deck above; his
slow breathing. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. Every
object on the rack is rigid and still; nothing shifts.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The rack carries no numerals, no letters, no markings; eleven
collars stay empty and one cylinder only exists — the count never changes; the
lever is never touched.
```


---

## 🎬 SAHNE 11 (S11) — SÖYLEMEDİĞİ

> AMBER DİSİPLİNİ: PART A'da amber YALNIZ bu sahnede (plan 🎨 — üç kare/üç
> nabız ailesinin ilki). Konuşmama sahnesi: ağız kapalı kilidi negatifte.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man seated at a
small dark transmitter panel, one amber lamp. Exactly one human figure — this
film has exactly one human total.

SCENE: Close on a corner of the gondola: a small guarded transmitter console,
plain brushed metal, carrying no letters, no numerals, no markings — only a
fold-down toggle under a raised guard and one recessed amber repeater lamp,
lit mid-pulse. Seated before it on a low stool, forearms on knees, leaning
toward the panel: the air engineer — a man in his early fifties, 1.79 m, thin,
shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. The amber
pulse is the only warm artificial light that exists anywhere on the station;
it touches his face from below while the neutral service lamp holds the room
dim.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.4
meters away, f/2.8. One neutral-white service lamp, the amber lamp mid-pulse;
deep late ochre in the porthole beyond.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The amber lamp is the only amber light; the panel carries no text,
no symbols, no readout of any kind.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): The small guarded transmitter console — plain
metal, no markings, a fold-down toggle under a raised guard, one recessed
amber repeater lamp. Seated before it: the air engineer. Camera fixed 1.4
meters away, 85mm spherical lens.

TIMELINE: 0.0s — The panel is dark. He sits leaning toward it, forearms on
knees. 2.0s — He flips the guard up and the toggle with it: the amber repeater
lamp begins to pulse, once every 2 seconds, soft and recessed — the channel is
open. 4.0s — He watches the pulse. His jaw tightens once. His lips never part.
7.5s — He folds the guard back down. The lamp dies mid-pulse. 9.0s — The dark
panel; his face lit only by the neutral lamp again. 10.0s — Hold.

AUDIO: A faint carrier hiss while the channel is open — from 2.0s to 7.5s —
under the low fan hum; the hiss stops dead when the guard closes; his
breathing, even and slow. He never speaks. No voice, no music.

PHYSICS: 0.904 g. Real time, no slow motion. The lamp pulse holds an exact
2-second period while lit.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. His mouth stays closed throughout — no speech, no whisper, no lip
movement. The amber lamp is the only amber light; the panel carries no text,
no symbols, no readout.
```


---

## 🎬 SAHNE 12 (S12) — PART A KAPANIŞ — EŞİK

> [D90] batışın İLK görünür anı: rivet çizgisine karşı 10 s'de iki parmak
> tırmanan sis hattı (30 m/saat = ~0.8 cm/s — fizik doğru). Kol'a bakış var,
> temas yok; PART B S20 bu kadrajın cevabıdır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man between a
porthole and a cylinder rack in a dim gondola, mist at the glass. Exactly one
human figure — this film has exactly one human total.

SCENE: A wide fixed frame across the gondola: at frame left, the round
porthole; at frame right, the edge of the gas manifold — a wall rack of twelve
cylinder sockets, eleven of them empty open collars in a long row, one holding
a single full steel cylinder; beside the rack a single steel lever stands
between two pipes — a thick insulated line climbing up into the envelope, and
a thinner line running level into the probe-bay bulkhead. Between them, facing
the porthole, stands the air engineer — a man in his early fifties, 1.79 m,
thin, shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. Through the
glass: the top of the lower cloud deck has risen — a soft pale mist line
stands a hand's width ABOVE the porthole's midline, deep ochre light above it,
blank pale grey below it. The station has sunk into the top of the sea. A
rivet line crosses the porthole frame, a fixed mark against the mist.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position three
meters away at chest height, f/5.6. One neutral-white service lamp; the light
through the porthole dimmer and deeper than in any frame before it.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The rack carries no markings; eleven collars empty, one cylinder —
the count never changes.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): Wide across the gondola: the porthole at frame
left, the edge of the gas manifold — a wall rack of twelve cylinder sockets,
eleven of them empty open collars in a long row, one holding a single full
steel cylinder; beside the rack a single steel lever stands between two pipes
— a thick insulated line climbing up into the envelope, and a thinner line
running level into the probe-bay bulkhead at frame right, the man between them
facing the glass: the air engineer. Through the porthole the pale mist line of
the risen cloud deck stands a hand's width above the porthole's midline; a
rivet line crosses the frame as a fixed mark. Camera fixed three meters away,
32mm spherical lens.

TIMELINE: 0.0s — He stands at the glass, watching the mist. 3.0s — Read only
against the fixed rivet line, the mist line creeps upward — two finger-widths
over the whole shot, the sinking of the station made visible for the first
time. 6.0s — He turns his head from the porthole to the lever on the rack at
frame right, and holds there. 8.5s — He looks back to the glass. He goes to
neither. 10.0s — Hold: a man standing exactly between the window and the
choice.

AUDIO: Low fan hum; the leak-whistle; the faint creak-ticks slower now; his
breathing. No voice, no music.

PHYSICS: 0.904 g. Real time, no slow motion. The mist rises past the porthole
at the station's true sink rate — a slow visible creep of about one centimeter
per second against the glass; nothing else moves.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The mist line moves only upward and only slowly; the rack carries
no markings; the lever is never touched.
```

---

# 📋 PART A ÖZET TABLOSU

| # | Sahne | İnsan | Kask | Işık ailesi | Lens / mesafe | Sayaç kanalı |
|---|---|:---:|:---:|---|---|---|
| S0 | HOOK — GÖMÜLMEKTE (9s) | 0 | — | Dış parlak | 24mm / 250 m hava | gondol sisin içinde |
| S1 | YAMA | 1 | — | Zarf içi | 32mm / 6 m | yama haritası |
| S2 | PİN YAYI | 1 | — | Gondol loş | 85mm / 1.2 m | ⭐ pin aralığı (katalizör) |
| S3 | NE SOLUYORSA O TUTUYOR | 1 | — | Zarf içi | 32mm / 7 m | buğu + boncuk (S18 çifti) |
| S4 | DÖRT ASKI | 1 | ✔ | Alkov loş | 32mm / 4 m | 3 boş kabuk + 1 boş askı |
| S5 | VİRAL #1 — SIRT | 1 | ✔ | Dış EN PARLAK | 32mm / 9 m | — (ölçek) |
| S6 | DIŞ YAMA | 1 | ✔ | Dış parlak | 35mm / 4 m | asit rozeti |
| S7 | AŞINMA | 1 | ✔ | Dış parlak | 32mm / 8 m | TAM 10 rozet |
| S8 | AKCİĞER — İLK RENK | 1 | — | MOR (tek oda) | 35mm / 3.5 m | — |
| S9 | CAM — TEK TEMAS | 1 | — | MOR | 85mm / 1.6 m | ipliklerin avuca göçü |
| S10 | HESAP — ORTA NOKTA | 1 | — | Gondol koyu | 32mm / 4 m | 11 boş + 1 dolu |
| S11 | SÖYLEMEDİĞİ | 1 | — | Gondol + AMBER | 85mm / 1.4 m | amber nabız 2 s |
| S12 | PART A KAPANIŞ — EŞİK | 1 | — | Gondol en koyu | 32mm / 3 m | ⭐ rivet'e karşı sis hattı |

**Doğrulama:** 13 sahne · 26 prompt · insanlı 12 sahne / 24 prompt ·
suit'li 4 sahne (D79 negatifi 8/8 promptta) · replik 0 / altyazı bütçesi
0.0 sn · MOR yalnız S8-S9 · AMBER yalnız S11 · ışık ekseni monotonik
(parlak → koyu, plan takvimiyle birebir) · kamera 13/13 sabit lockoff ·
video üretim modu 12/12 I2V (S0 hariç — insansız hook T2V).

---

## 🚪 KAPI KAYITLARI [D74] — her koşu TEK SATIR

```
Format: TARİH · KAPI (S0/S5/S20/S8) · SONUÇ (GEÇTİ / V2 / DÜŞÜŞ) · not
20.08.2026 · DURUM: ÜRETİM BAŞLAMADI — kapı sırası S0 → S5 → S20
  (PART_B yazılınca) → S8. İlk koşudan önce PART_B beklenmez: S0 ve
  S5 kapıları PART A promptlarıyla koşulabilir.
20.08.2026 · YAZIM · PART A üreteçle basıldı (26 prompt, çapa blokları
  sabitlerden — parafraz 0 doğrulandı) · prompt_kontrol: 0 BLOCK,
  FIX yalnız uzunluk (üretim notu ②) · TR karakter taraması: 0.
(sonraki koşular buraya eklenecek)
```
