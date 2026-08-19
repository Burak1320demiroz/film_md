# 🔵 THE BLUE DRIFT — Mavi Süzülüş | PART A

## AI Production Bible — Self-Contained Prompts
### PART A: Sahne 0-12 (13 sahne) | 16:9 Yatay | Görsel + Video + Diyalog
### _"Onları kurtaran şey, hiçbir şey yapmamalarıydı."_

> **PART A süresi:** Hook (9s) + 12 sahne × 10s = 129 saniye
> **Toplam film:** 25 sahne = 249 saniye = 4 dakika 09 saniye
> **PART B:** `THE_BLUE_DRIFT_PART_B.md` (S13-S24)
> **Plan:** `THE_BLUE_DRIFT_PLAN.md` — QA SPEC, risk kartları, A4 kararları orada

---

## ⚠️ PART A ÜRETİM NOTLARI (promptlardan önce oku)

```
① İNSANSIZ SAHNELER (S7 · S8 · S12) — YAPISAL RED PROTOKOLÜ
   Cold Burn S8'de doğrulanan tetikleyici: insansız sahne + uzun
   NEGATIVE + "Exactly 0 human figures" kalıbı → "having a hard time"
   reddi. Azaltım BAŞTAN uygulandı: insansız sahnelerin NEGATIVE bloğu
   KISA tutuldu, boş kadraj POZİTİF anlatıldı ve insan sayısı imzası
   "Human count in this frame: zero — both crew are inside the craft"
   biçiminde yazıldı. Yapısal red yine gelirse: KILAVUZ_REHBERI §7
   merdiveni (NEGATIVE'i tek Style satırına indir → etiketleri kaldır
   → "human" kelimesini çıkar → 3 satırlık prob → I2V).

② UZUNLUK BANDI — BİLİNÇLİ SAPMA GEREKÇESİ [Black Cradle §② emsali]
   İki karakterli sahnelerde iki kanonik çapa bloğu + kask cümleleri +
   D79 negatifi zorunlu (çapa kuralı kelime kelime kopya ister,
   kısaltılamaz) → birçok prompt 1.700-2.100 / 2.000-2.600 bandının
   üstünde kalır; tavan (~4.300) aşımı hedefi SIFIR. prompt_kontrol
   çıktısı bu notun altına işlenir. KAPATMA YOLU: bir sahne red
   alırsa O promptun NEGATIVE bloğu tek satır pozitif Style cümlesine
   indirilir (−600-800 karakter). İLK RED PROTOKOLÜ: önce HATA MESAJI
   sınıfına bak (§7 tablosu); aynı filmde 3 red / 0 başarı görülürse
   kısaltma değil 3 satırlık prob koşulur.
   → prompt_kontrol 17.08.2026: 26 prompt · 0 BLOCK · FIX yalnız
     uzunluk — image 1.964-3.487 (bant üstü kısmı GÖZLEM sınıfı) ·
     video 2.438-3.826 (bant 2.000-2.600 üstü) · TAVAN (4.300) aşımı
     SIFIR. Yönelim kilidi ve çapasız-yön bulguları aynı gün kapatıldı
     (araç görünen dış sahnelere blok-sonrası "canopy nose" yönelim
     cümleleri eklendi; S7 tırmanış cümlesi ekran dilimiyle yazıldı).

③ MAVİ-ÜSTÜ-MAVİ KAPISI
   Filmin ana kapısı S21'dir (PART_B) ama PART A'nın kendi iki testi
   var: S0 (kırağı gerçekten MAVİ planetshine'da mı okunuyor — palet
   testi) ve S4 (aurora kilidi testi). Form okunmazsa HAZIR DÜŞÜŞ:
   lander omurgasına İKİ ince beyaz konum şeridi ışığı (prompt V2) —
   plandaki 🎨 bölümü.

④ KAPI KAYDI [D74]: S21 · S15 · S4 · S0 kapılarının her koşusu bu
   dosyanın sonuna TEK SATIR olarak yazılır. Kayıtsız kapı,
   koşulmamış kapıdır.

⑤ AURORA KİLİDİ + DİKEY IŞIK MIKNATISI [D104'ün bu filmdeki hâli]
   Model "kuzey ışıkları" klişesine kayar: YEŞİL renk, hızlı dalga,
   tüm göğü kaplama. Kilit her gök sahnesinde: yalnız MAVİ-MENEKŞE
   ("never green"), 10 saniyede TEK yavaş dalga, taban açısı sahne
   sahne sabit (S0 taç → S2 70° → S3 60° → S4 50° → S6 45° → S7 40°,
   monotonik iner), zemin gölgesi üretmez, planetshine'ı bastırmaz.
   ⚠️ Bu filmde tek baskın ışık UFUKTA değil TEPEDEDİR — D104
   mıknatısının dikey hâli: model koşucuların BAŞINI yukarı çevirir.
   S4 nötr çekimdir (kamera landerin yanında, koşu KAMERAYA DOĞRU —
   Black Cradle V3'ün kanıtlanmış çözümü İLK denemede kullanılır) ve
   negatifine "neither figure looks up, no direction reversal"
   yazılıdır. prompt_kontrol yönelimi GÖREMEZ — insan gözüyle denetle.

⑥ ⛔ ÇAPA PARAFRAZ HATASI — 18.08.2026'da SAHADA GÖRÜLDÜ (S1 videosu)
   BULGU: S1 videosunda karakterler/iş/araç doğru, ARKA PLAN yanlış.
   SEBEP: gezegen ve zemin çapa blokları IMAGE promptunda TAM, VIDEO
   promptunda PARAFRAZ yazılmıştı. Kaybolan dört kilit: "deep sapphire
   gas giant" · "filling the upper HALF of the sky" (oran!) · "darker
   indigo latitude stripes" · "crossed by low pressure ridges".
   Oran ve doku kilitsiz kalınca model gökyüzünü ve ovayı yeniden
   uydurdu [SAHNE_DEVAMLILIK §2.1: eşanlamlı bile yasak].
   ⚠️ HATA S1'E ÖZEL DEĞİLDİ: denetimde 22 parafraz + 9 kısaltılmış
   kırağı kilidi bulundu (S1-S4 · S7 · S8 · S11 · S12 ve PART_B'nin
   yörünge sahneleri). Hepsi 18.08'de kanonik bloğa çevrildi.
   ⭐ SAYIM ARTIK İDDİA DEĞİL, ÖLÇÜM: aşağıdaki DOĞRULAMA bloğundaki
   sayılar grep ile üretildi ve komutu orada yazılıdır.
   ⛔ KURAL: bir çapa bloğu promptun içine KOPYALANIR, yeniden
   yazılmaz. Sahneye özgü kadraj/oran cümlesi bloktan SONRA gelir.

⑦ KERTE ANA GEMİDEDİR
   Sesi telsizden gelir; S9'un ortasından S11'e kadar bağlantı
   KOPUKTUR (KERTE 0 replik). S9'daki replik YARIDA KESİLİR — bu bir
   üretim hatası değil, sahnenin kendisidir; timeline'da yazılıdır.
```

---

# 📖 BÖLÜM 1 — THE BIBLES

---

## 🔵 WORLD BIBLE — MAVİ DEV "DERİN" & KIRAĞI UYDUSU

```
GEZEGEN ("the blue giant"): Metan-mavisi dev; uydudan bakınca
gökyüzünün YARISINI kaplar. Derin safir zemin, daha koyu lacivert
enlem bantları, kutupta soluk menekşe pus. Kendi ışığı yok — yıldızın
aydınlattığı yüzü uydunun gece yarısını MAVİ dolgu ışığıyla aydınlatır
(PLANETSHINE). Filmin ışık imzası: gece yüzeyi karanlık değil, mavi
bir yarı-ışık içindedir; yörüngede gölgeler mutlak siyah değil, MAVİ
albedo dolgusuyla yumuşaktır.

YÜZEY: Ufka kadar mavi-gri AZOT KIRAĞISI ovası — ince taneli, MAT;
alçak basınç sırtları (1-3 m), seyrek koyu çatlak ağları. Lamba
havuzlarının dışında hiçbir renk maviden sıcak değildir.

ATMOSFER: İnce azot, Dünya basıncının %2'si. Anlamı: - RÜZGAR HİÇBİR
ŞEYİ DEVİRMEZ; kumaş çırpmaz. - Kalkan kırağı tozu 0.4g'de 3 saniyede
GERİ OTURUR. - SES BOĞUK VE ALÇAKTIR; yüksek frekans taşınmaz. -
Gökyüzünün üst yarısı gezegen, kalanı keskin yıldızlar.

PLAZMA PERDESİ: Zenitten sarkan yarı saydam MAVİ-MENEKŞE aurora
şeritleri. S0'da zenitte soluk TAÇ; sonra taban iner: S2 70° → S3 60°
→ S4 50° → S6 45° → S7 40° (kalkış penceresi tabanı 40°'ye inmeden
kapanır). Dalgalanma YAVAŞ: 10 saniyede TEK dalga. Renk bandı DAR:
yalnız mavi-menekşe — ⛔ YEŞİL YOK (yeşil aurora Dünya oksijen
klişesidir; bu atmosferde fiziksel olarak yanlış). Perde ışık
ÜRETİR ama gölge ÜRETMEZ ve planetshine'ı asla bastırmaz. Öldüren
perde değil: perdeye eşlik eden görünmez parçacık yağmuru —
korumasız elektroniği bozar. Taban yüksekliği filmin metinsiz geri
sayım kanalıdır.

YERÇEKİMİ (YÜZEY): 0.4g. Adımlar temaslı ve ağırlıklı, koşu gerçek
koşu. GERÇEK ZAMAN [Ders 44]: insan temposu Dünya'yla aynı; ağır
çekim YOK — her yüzey promptunda "real time, ordinary Earth pace".

SICAKLIK: Gece yüzü -180°C. Kask kapalı; nefes buharı dışarıda yok.

IŞIK BÜTÇESİ (yüzey): TAM 5 yapay kaynak — 2 kask lambası + 2 göğüs
lambası + 1 karın projektörü (lander). Doğal ışık: mavi planetshine
(ana dolgu) + perde (üst ton). Havuzlar nötr beyaz adalardır.

YÖRÜNGE: Siyah uzay, keskin sabit yıldızlar; kadrajın altında/yanında
gezegenin dev mavi kavisi. ⭐ ALBEDO DOLGUSU VAR VE MAVİ: gölge
tarafları soluk mavi dolguyla okunur (Cold Burn'ün beyazının, Black
Cradle'ın sıfırının MAVİ üçüncüsü). Sert beyaz güneş tek doğrudan
kaynak. VAKUM: dışarıda ses SIFIR, pus yok, lens parlaması yok.

YERÇEKİMİ (YÖRÜNGE): 0g. Kayışlı bedenler koltuğa kilitli; serbest
nesne düz hatta süzülür; "yüzme" yok. ARIZA SONRASI ARTIK DÖNÜŞ:
araç 1°/s ile yavaşça yuvarlanır (asimetrik itici ölümünün mirası) —
kabin camında yıldız alanı belli belirsiz kayar; S13-S15'te (PART_B)
sorunun kendisi olur.
```

---

## ⚓ ÇAPA BLOKLARI — KANONİK İNGİLİZCE TANIMLAR

```
⚓ KANONİK ÇAPA BLOKLARI [SAHNE_DEVAMLILIK §2.1] Aşağıdaki bloklar
KANONİKTİR: varlık hangi promptta görünüyorsa oraya KELİMESİ
KELİMESİNE kopyalanmıştır — eşanlamlı bile yasak. Sahneye özgü durum
(koşu, arıza, uçuş konfigürasyonu) bloktan SONRA ayrı cümleyle
eklenir; blok değişmez.

PILOT: the pilot — man, mid-forties, 1.83 m, broad-shouldered and
lean, warm tan skin with visible pores, dark brown eyes, a broad nose
once broken at the bridge, short black hair greying at the temples, a
thin old scar on his left cheekbone; matte cobalt-blue hard-shell
suit, dark graphite flex-weave joints, machined articulation rings,
thin inlaid TEAL accent lines on the shoulder plates and forearms,
finely scuffed with use

ENGINEER: the engineer — woman, mid-thirties, 1.69 m, wiry, pale
cool-toned skin with visible pores and faint freckles, grey-green
eyes, a small notch scar splitting her left eyebrow, dark auburn hair
in a near-shaved crop; same matte cobalt-blue hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely
scuffed with use

KASK CÜMLESİ (kasklı sahnelerde bloğun hemen ardına): low-profile cobalt-blue helmet CLOSED, [his/her] face fully readable through the visor
(VİZÖR KİLİDİ — kasklı yüz görünen her promptta bir kez, gövdede:)
Each visor is one seamless optically clear pane in a 2-cm brushed-metal frame, its lower seal ring visible where it meets the suit collar, one thin specular line along its top edge — the glass is always present, never absent.
(Kasksız tek sahne S23 PART_B'dedir: BARE-HEADED.)

LANDER — TAM BLOK (araç ÖZNE olduğu sahnede: S7): the lander — a
9-meter angular LIFTING-BODY craft, no plain cylinder: broad flat
belly, sharp chine lines running nose to tail, a low blended forward
canopy, two short swept strakes, twin main engines recessed in a
notched tail, four downward LIFT NOZZLES under the belly, four
landing legs that fold up into flush belly wells, recessed thruster
quads at bow and stern, and a 40-cm domed emergency-beacon housing on
the left shoulder line; satin steel-blue composite panels with crisp
recessed seams over a graphite-grey structural spine, one thin
SIGNAL-WHITE chevron line down each flank, and a side hatch

LANDER — ZEMİN SÜRÜMÜ (S0-S4; araç 30-300 m uzakta, kadrajın öznesi
değil — tam bloğun ALT KÜMESİDİR, çelişen kelime içermez): the lander
— the same 9-meter angular lifting-body craft, satin steel-blue with
one thin SIGNAL-WHITE chevron line down each flank, standing level on
four landing legs, its single belly floodlight cutting a hard-edged
pool of white light onto the blue-grey frost

LANDER — UÇUŞ SÜRÜMÜ (S8): the lander — the same 9-meter angular
lifting-body craft in FLIGHT CONFIGURATION, all four landing legs
folded away into flush belly wells, its belly line clean, satin
steel-blue with one thin SIGNAL-WHITE chevron line down each flank

LANDER — ÖLÜ SÜRÜM (S12 · PART_B S13/S15): the lander — the same
9-meter angular lifting-body craft in FLIGHT CONFIGURATION, all four
landing legs folded away, its belly line clean, satin steel-blue with
one thin SIGNAL-WHITE chevron line down each flank, every thruster
cold and every window dark — DEAD, the only light on it the 40-cm
beacon dome on its left shoulder line pulsing warm amber once every
2 seconds

GEZEGEN — YÜZEY SÜRÜMÜ (her dış yüzey promptuna): the blue giant — a
deep sapphire gas giant filling the upper half of the sky, banded
with darker indigo latitude stripes, a faint violet haze at its pole,
lighting the whole night surface with a soft even blue planetshine

GEZEGEN — YÖRÜNGE SÜRÜMÜ (S8-S12 dış/cam): the blue giant — a deep
sapphire gas giant banded with darker indigo latitude stripes, its
vast sunlit curve filling the lower frame, washing every shadow with
a soft blue albedo fill

KIRAĞI KİLİDİ (her yüzey promptuna): The plain is pale blue-grey
nitrogen frost, fine-grained and matte, crossed by low pressure
ridges; under the planetshine everything reads in tones of blue, and
no colour warmer than blue exists outside the artificial lamp pools.

AURORA KİLİDİ (gök görünen yüzey promptlarına — taban açısı sahneye
göre): Overhead hangs the plasma curtain: translucent ribbons of
electric blue-violet light, their lower edge [N] degrees above the
horizon, rippling in one slow wave every 10 seconds. The curtain is
light only — it casts no shadow and never overpowers the blue
planetshine. Its colour is narrow blue-violet; it is never green.

IŞIK BÜTÇESİ CÜMLESİ (her yüzey promptuna): Exactly five artificial
light sources exist on this surface: two helmet lamps, two chest
lamps, and the lander's single belly floodlight.

BACAK DURUMU [Cold Burn dördüncü tur dersi]: İniş bacakları YALNIZ
S0-S7 (kalkışın ilk 4,5 saniyesi dahil) açıktır. S7'nin 4,5.
saniyesinden film sonuna kadar: bacaklar KATLI, kapaklar kapalı,
karın hattı düz — kalkış sonrası araç görünen HER promptta "in FLIGHT
CONFIGURATION … no landing leg, no leg well and no open gear door is
visible" gövdede yazılır.

DOĞRULAMA (PART A blok sayımı · 18.08.2026'da GREP İLE ÖLÇÜLDÜ,
elle yazılmadı): GEZEGEN yüzey çapası 10 prompt · GEZEGEN yörünge
çapası 6 prompt · KIRAĞI kilidi 12 prompt · parafraz 0.
Doğrulama komutu (çıktı 0 olmalı — parafraz kalmışsa listeler):
  python3 - <<'X'
  import re,glob
  S="deep sapphire gas giant filling the upper half of the sky"
  O="deep sapphire gas giant banded with darker indigo latitude"
  for f in sorted(glob.glob("THE_BLUE_DRIFT_PART_*.md")):
      for b in re.findall(r"```\n(.*?)\n```", open(f).read(), re.S):
          t=re.sub(r"\s+"," ",b)
          if "blue giant" in t and S not in t and O not in t: print(f,t[:80])
  X
```

---

## 🚀 SHIP BIBLE — ALBATROS (lander) & SILA (ana gemi)

```
LANDER ("the lander"): 9 m AÇILI KALDIRMA GÖVDESİ — düz silindir
DEĞİL, gövde YATAY durur. Geniş düz karın, burun-kuyruk keskin CHINE
hatları, alçak kaynaşık kanopi, iki kısa strake, kuyruk çentiğinde
İKİ ana motor, karın altında DÖRT kaldırma lülesi, karın yuvalarına
katlanan DÖRT iniş bacağı. SATEN ÇELİK MAVİSİ kompozit paneller —
kırağı gibi mat değil: ince gömme derz dokusu ve kenar ışığı tutan
hafif saten. Her yanda tek İNCE SİNYAL BEYAZI şevron çizgisi. Yan
kapak. Sol omuz hattında 40 cm kubbeli ACİL VERİCİ (mekanik kurmalı,
korumalı barada): S10'dan itibaren 2 saniyede bir SICAK AMBER nabız.

İTİCİLER: Burun ve kıçta gömme itici kümeleri — S8'deki parçacık
sağanağından sonra HEPSİ ÖLÜ (S9'dan itibaren hiçbir promptta hiçbir
jet ateşlemez; tek istisna PART_B S15'in TAHLİYE PUFLARI — o motor
değil, airlock valfinden verilen kabin havasıdır).

KALKIŞ SIRASI (Cold Burn'de kanıtlanan dört adım — hiçbir promptta
değişmez):
① dört karın lülesi ateşler (araç hâlâ ayakta)
② araç düz seviyede yükselir
③ 20 m'de (S7'de 4,5 s) dört bacak yuvalara katlanır, kapaklar kapanır
④ kuyruktaki iki ana motor yanar, kaldırma kesilir, burnu ileride
  hızlanır
⛔ Kuyruk motoru asla yere doğru ateşlemez; dikleşme yok.

KABİN — "UÇUŞ GÜVERTESİ" (18.08.2026'da büyütüldü: aynı kilitler, daha
derin mimari; filmin kadrajlarının çoğu ARKADAN olduğu için tasarım
SIRTTAN okunacak biçimde kuruldu):
2.2 m genişlik, iki YÜKSEK ARKALIKLI işlenmiş koltuk kabuğu YAN YANA
(solda pilot, sağda mühendis). Koltuk arkalıkları kadrajın öznesidir:
açık başlık kafesi, omuz üstünden geçen kayış dokuması ve arkalık
boyunca inen İNCE BORU ÇİZGİSİ — SOLDA TURKUAZ, SAĞDA AMBER. Bu çizgi
ikinci rol kanalıdır: yüz görünmediğinde kim kim, oradan okunur.
ORTA OMURGA: iki koltuk arasında işlenmiş konsol omurgası; ayağında
30 cm PİRİNÇ TAHLİYE VALF KOLU (PART_B'nin "son motoru"), boyunca alçak
bir amber şerit.
YAN KONSOLLAR: her dirsek hizasında eğik panel, soyut segment çubukları.
TAVAN KEMERİ: mürettebatın üstünde nervürlü yapısal kemer — TAM 6 kapaklı
toggle (metin YOK) ve İKİ gömme TURKUAZ şerit lamba; ikisi koltuk
sırtlarını yukarıdan yıkar (arkadan kadrajın kenar ışığı budur).
KANOPİ — ÜÇ PANEL: ortada tek geniş ön cam 1.4 × 0.5 m (ölçek kilidi
DEĞİŞMEDİ), iki yanında işlenmiş grafit çerçevelerle ayrılmış İKİ eğik
çeyrek panel. Sarma his verir; dışarısı arkadan bakışta geniş görünür.
ZEMİN: ızgara döşeme, eşik hattında ince mavi kenar ışığı, sintine
boyunca klipslenmiş kablo demetleri.
PANEL: analog ağırlıklı — soyut amber/turkuaz IŞIK SEGMENTLERİ (doluluk
gösterir, metin/rakam ASLA), ortada 12 cm'lik MEKANİK DURUŞ KÜRESİ
(elektriksiz; arıza sonrası dönüşün tek göstergesi — döner, despin
bitince DURUR). Sağ panelde 12 cm'lik MEKANİK KABİN BASINÇ İBRESİ:
numarasız yay skala, 10 kademe çentik, fosfor kadran.
ARIZA SONRASI (S9'dan itibaren): panel segmentleri, tavan şeritleri ve
zemin kenar ışığı KARANLIK; yanan yalnız üç şey — duruş küresi arka
ışığı, ibrenin fosfor kadranı, S10'dan sonra 2 saniyede bir amber
tekrarlayıcı lamba. Bu üçlü, karanlık kabinin tüm ışık bütçesidir.

⚓ KOKPİT ÇAPA CÜMLESİ (kabin mimarisi görünen her promptta, birebir):
THE COCKPIT: two high-backed machined seat shells side by side — thin
TEAL piping down the left seat back, AMBER down the right — a machined
console spine between them, canted side consoles at both elbows, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy: one wide
central pane flanked by two angled quarter-panes in graphite frames.

ANA GEMİ ("the main ship"): 135 m YILDIZLARARASI transfer gemisi —
lander'ın TAM 15 KATI. Saten çelik mavisi gövde, seyrek ince beyaz
konum çizgileri; burun sensör kubbesi · kapitoneli ALTI yaşam modülü
· açık altıgen kafes omurga · omurga ortasında AÇIK YAKALAMA AĞZI
(12 × 7 × 5 m · 2 kızak kolu · 4 açık kelepçe · ağız çerçevesinde
DÖRT BEYAZ ÇERÇEVE IŞIĞI) · iki bıçak sırtı radyatör kanadı · kıçta
füzyon bloğu. DÖNMEZ. PART A'da yalnız UZAK NOKTA olarak görünür
(S11'de iki kez yanıp sönen ışık · S12'de sabit parıltı noktası);
gövde geometrisi PART_B'de kadraja girer.

ÖLÇEK KİLİDİ: lander 9 m · ana gemi 135 m (15×) · yakalama ağzı
12 × 7 × 5 m · yuva payı 1.5 m · kelepçe 4 · çerçeve ışığı 4 · verici
kubbesi 40 cm · kabin 2.2 m · ön cam 1.4 × 0.5 m · duruş küresi 12 cm
· basınç ibresi 12 cm · valf kolu 30 cm · karot 40 cm · pilot 1.83 m
· mühendis 1.69 m. Tüm sahnelerde birebir korunur.
ORAN CÜMLESİ (ikisi aynı karedeyse — PART_B): "the lander is
one-fifteenth of its length — this time the cathedral comes to the
moth."
```

---

## 👤 CHARACTER BIBLE — PİLOT & MÜHENDİS & KERTE

```
⚠️ PROMPT KURALI: Özel ad promptlara YAZILMAZ (Ders 34) — "the pilot"
/ "the engineer". Milliyet ifadesi YASAK.

PİLOT ("the pilot"): Erkek, 44, 1.83 m, geniş omuzlu-kuru. Koyu
buğday ten, görünür gözenek. Koyu kahve gözler, köprüsünden kırılmış
geniş burun, şakakları grileşen kısa siyah saç, sol elmacıkta ince
eski iz. SUIT: mat kobalt mavisi sert kabuk — segmentli göğüs/omuz
plakaları, grafit esnek-örgü eklemler, işlenmiş eklem halkaları, omuz
ve ön kollarda İNCE KAKMA TURKUAZ ÇİZGİ, ince çizikli. Düşük
profilli kobalt kask, tek parça optik berrak panoramik vizör, sırt DÜZ.

MÜHENDİS ("the engineer"): Kadın, 36, 1.69 m, sırım. Açık soğuk ten,
görünür gözenek + seyrek çil. Gri-yeşil gözler, SOL KAŞI bölen küçük
çentik izi, neredeyse kazınmış koyu kızıl-kahve saç. SUIT: aynı sert
kabuk, İNCE KAKMA AMBER ÇİZGİ aksanları, ince çizikli. Aynı kobalt
kask, berrak vizör, sırt DÜZ.

AYIRT EDİCİLİK KİLİDİ: TURKUAZ çizgi = pilot · AMBER çizgi = mühendis
· 1.83 ↔ 1.69 boy farkı · koşuda pilot önde eli boş, mühendis KAROT
KUTUSU taşır. İki karakterli her prompta bu satırlar yazılır.

HUMAN COUNT LOCK: Filmde TAM 2 insan. Her promptta karede görünen
sayı (0 / 1 / 2) açıkça yazılır. Üçüncü figür, kopya, yansımada
fazladan yüz, arka planda siluet YOK.

HELMET STATE SCHEDULE: İnsan görünen 18 sahnenin 17'sinde kask
KAPALI; kasksız tek sahne S23 (PART_B, basınçlı hangar güvertesi).
PART A'da kasksız sahne YOKTUR; ara durum YOKTUR. Arıza sonrası da
suitler mühürlü kalır (kabin basıncı PART_B'de harcanacaktır — kask
açmak ölüm olur; mantık zinciri planda).

SIRT VE VİZÖR KİLİDİ [DERS 79 · zorunlu]: Sırt ünitesi YOK — sırt
silueti DÜZ. Vizör optik berrak: renklendirme, aynalama, ÇEVRE
YANSIMASI sıfır; yüz her karede okunur. ⚠️ Bu iki cümle bible'da
BIRAKILMAZ — insan görünen 36 promptun 36'sında negatif bloğun
İÇİNDE yazılıdır (bu dosyada 20'si).

KERTE (AI — "a calm neutral synthetic voice"): GÖVDESİZ ve BU ARAÇTA
DEĞİL — ana gemidedir, sesi telsizden gelir. Ekranı, avatarı, yüzü,
robotu YOK. Asla görselleşmez. S9 ortası - S11 arası bağlantı KOPUK
(0 replik). ⭐ D82 SİGORTASI: SAYI söyleyen her replik KERTE'nindir;
üretimde bir insana devredilemez.
```

---

## 🎥 CAMERA BIBLE

```
KURAL: 25/25 sahne SABİT LOCKOFF. Pan yok, tilt yok, zoom yok, track
yok, kesme yok. Her sahne = tek kesintisiz çekim = ayrı video.

LENS KİLİDİ (küresel/spherical — anamorfik yatay parlama YASAK):
- HOOK havadan                     → 24mm
- DIŞ GENİŞ (yüzey, yörünge)       → 32mm
- KABİN (arkadan/yandan, koltuklar)→ 35mm
- DETAY (panel, ibre, valf)        → 85mm

MESAFE: her prompt kamera mesafesini metre cinsinden yazar.

KOKPİT DİYALOG KURALI: konuşmalı kabin sahneleri (S6 · S9 · S10 ·
S11) İKİ KOLTUĞUN ARKASINDAN çekilir — ağızlar kadrajda değildir,
replikler telsiz sesidir. S2 dış diyalog sahnesinde konuşan KERTE'dir
(gövdesiz, telsizden).

EKRAN YÖNÜ KİLİDİ [UZAMSAL kılavuz]: Tehdit GÖKTEN iner — yatay yön
çatışması yapısal olarak zayıf. Tek koşu sahnesi S4 ve NÖTR ÇEKİMDİR
(kamera landerin yanında, koşu KAMERAYA DOĞRU — kanıtlanmış çözüm).
Yüzeyde gölgeler lamba havuzlarından RADYALDİR (planetshine
gölgesizdir); tek yönlü gölge sistemi kurulmaz.

SÜRE: Sahne başına 10 saniye (Hook = 9). ⚠️ Veo 3.1 native 8s üretir:
8s üret + 2s extend uygula.
```

---

## 💡 LIGHTING BIBLE — BEŞ MAVİNİN AYRIŞMASI

```
⭐ FİLMİN ASIL İŞİ BU TABLODUR. Beş mavi TON + DOKU ile ayrışır ve
ilgili cümleler promptların gövdesinde yazılıdır:
  GEZEGEN  → DERİN SAFİR: koyu, bantlı, doygun — kadrajın en koyusu
  YÜZEY    → KIRAĞI MAVİ-GRİSİ: soluk, mat, ince taneli — en açık ton
  AURORA   → ELEKTRİK MENEKŞE-MAVİSİ: yarı saydam, tek ışıklı ton
  GÖVDELER → SATEN ÇELİK MAVİSİ: derzli; kenar ışığını (rim) tutar
  SUITLER  → MAT KOBALT PLAKA + grafit örgü + renkli çizgiler

SICAK RENK TEK AİLEDİR: AMBER = insan eliyle yakılmış ışık. PART A'da
üç yerde yaşar: mühendisin çizgisi (hep) · S7 kalkış jetlerinin sıcak
beyaz ışığı (mavi dünyada ilk sıcak renk — viral anın kendisi) ·
S10'dan sonra verici nabzı (2 s). Ateş, alev, patlama: 0 kare.

AİLE 1 — GECE YÜZEYİ (S0-S6): mavi planetshine ana dolgu (yumuşak,
gölgesiz) + TAM 5 yapay kaynak (sert kenarlı nötr beyaz havuzlar) +
tepede perde (üst ton, gölgesiz). Havuzların dışı karanlık DEĞİL —
soluk mavi yarı-ışık; ama renk maviden sıcak olamaz.

AİLE 2 — KALKIŞ (S7): dört lüle + kuyruk motorlarının SICAK BEYAZ jet
ışığı mavi kırağıyı 30 m yarıçapında ilk kez ısıtır; jetler
uzaklaşınca ova yeniden maviye döner.

AİLE 3 — YÖRÜNGE (S8-S12): tek sert beyaz güneş — kadraj SOLUNDAN;
jilet gölge, AMA gölge tarafı mutlak siyah değil: gezegenden MAVİ
albedo dolgusu (imza). Pus yok, halo yok, parlama yok.

AİLE 4 — KABİN: S5-S6 loş + soyut amber/turkuaz segmentler; S9'dan
sonra KARANLIK KABİN — üç mekanik ışık (küre arka ışığı · ibre
fosforu · amber nabız) + camdan giren mavi gezegen ışığı.

ANTİ-BLOOM: "glowing/ethereal/radiant/shimmering" YASAK. Işık kaynağı
her zaman net ve fiziksel ("the blue planetshine", "hard sunlight
from frame left", "the amber pulse of the beacon dome").
```

---

## ⚙️ PHYSICS BIBLE

```
YÜZEY (0.4g · %2 atmosfer): - Koşu gerçek koşu: temaslı, ağırlıklı,
GERÇEK ZAMAN [Ders 44] — her yüzey promptunda "real time, ordinary
Earth pace". - Kalkan kırağı tozu düşer, 3 saniyede OTURUR; asılı
perde yok. - Rüzgar kumaş çırpmaz. - Ses alçak, tok, boğuk. - KALKIŞ
(VTOL, S7): dört karın lülesi düz AŞAĞI; dört ayrı jet = dört ayrı
toz halkası, balistik yay çizip oturur. Sıra: lüleler → yükselme →
bacak katlanması (4,5 s / 20 m) → kuyruk motorları. Dikleşme YOK.

PERDE: taban 10 dakikada 90°→40° iner (sahne başına planlı açı);
10 saniyede tek dalga; ışık kuvvet uygulamaz — tehdit görünmez
parçacık yağmuru ve pencere. S8'de perde kenarı geçilirken gövde
kenarlarında 2 saniyelik soluk mavi-beyaz statik iplikler (St. Elmo
sınıfı) görünür — kısa, ince, tekrar etmez.

YÖRÜNGE (0g · vakum): - DIŞARIDA SES SIFIR. - S9'dan itibaren TÜM
iticiler ölü: hiçbir jet, hiçbir kıvılcım, hiçbir parça — arıza
SESSİZDİR, ışıklar sadece yanmaz. - Serbest araç Kepler yörüngesinde:
düz, sabit, öngörülebilir süzülüş + 1°/s artık yuvarlanma (10 s'lik
sahnede ~10° — camda yıldız alanı belli belirsiz kayar). - Kayışlı
bedenler koltukta OTURUR pozda [D23: serbest süzülen gövde 0 kare]. -
Yıldızlar her zaman KESKİN NOKTA — gerçek zamanlı çekimde iz/yay
oluşmaz. - Temas/eldiven: net yapısal sınır, erime yok.
```

---

## 🚫 NEGATIVE BIBLE (çekirdek — sahneye göre uyarlanır)

```
İNSANLI SAHNE ÇEKİRDEĞİ: Single unbroken take, fixed locked-off
camera — no cuts, no transitions, no pans, no zoom, no camera
movement of any kind. Exactly [N] human figures in this frame (this
film has exactly two humans total) — no extra crew, no duplicates, no
clones, no background figures, no extra faces in reflections. Thin
teal lines = the pilot, thin amber lines = the engineer — the two are
never identical. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no waxy texture, no face morphing, identical bone
structure throughout. The suits have NO back-mounted unit: no
backpack, no tank, no hose, no cable, no rear housing of any kind —
both back silhouettes are flat. Each visor is optically clear glass
with zero tint, zero mirror coating and zero reflection of the
environment; the face behind it is fully readable in every frame, at
every head angle. Suits and gear identical to the description — no
drift, nothing appears or disappears mid-shot. The frost stays matte
and the hulls stay satin — never glossy, never mirror-like. The
aurora, where visible, is narrow blue-violet only — never green,
never rainbow, casting no shadow. No readable text, letters, digits
or symbols on any panel, display, patch or hull — abstract light
segments only. No subtitles, no captions, no title card, no
watermark. All hand-surface contacts keep a clear structural boundary
— no merging, no phasing, no extra fingers. All particles obey the
stated gravity with continuous physical momentum — never hovering,
never frozen, never swirling or flowing like liquid. Terrain and
hulls static and stable — no melting, no warping, no swimming
texture. No Unreal Engine look, no CGI aesthetic, no video game
aesthetic. Photorealistic with 35mm film grain.

İNSANSIZ SAHNE ÇEKİRDEĞİ (kısa — yapısal red azaltımı, üretim notu
①): Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Human count in this frame: zero — both crew are inside the
craft. 0% bloom, no glow filter, no soft focus — every surface keeps
texture. The frost stays matte, the hulls stay satin — never glossy,
never mirror-like. The aurora, where visible, is blue-violet only —
never green, casting no shadow. No readable text anywhere. No
subtitles, no title card, no watermark. All particles obey the stated
gravity with continuous momentum — never hovering, never swirling.
Terrain and hulls static — no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.

DİYALOGLU SAHNEDE EK: The spoken lines are heard only — never shown
as text. No subtitles, no captions, no transcript. One speaker at a
time. All human voices come over the suit radio channel; no mouth is
readable in frame. The synthetic voice is radio-only from the distant
ship — it has no body, no face, no avatar, and no third figure ever
appears.

ARIZA SAHNELERİNDE EK (S8-S12): The failure is silent and dark — no
sparks, no explosion, no fire, no smoke, no debris, no venting; the
lights simply go out.
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART A: S0-S12)

> ⚡ **Her prompt tamamen bağımsızdır.** Bible'lara bakmanıza gerek yok.
> Sadece istediğiniz sahnenin 📸 veya 🎥 bloğunu kopyalayıp yapıştırın.

---

## 🎬 SAHNE 0 (S0) — HOOK: YARIM GÖK (9 saniye)

> 🎯 **REFERANS:** **RA** p1 (zemin konfig., uzak)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. High
aerial night view of a frost moon beneath a giant blue planet.
Exactly 2 human figures in frame, tiny with distance, helmets closed.

SCENE: The camera hangs 300 meters above an endless plain, aimed just
below the horizon so the sky fills the upper half of the frame. That
upper half IS a planet: the blue giant — a deep sapphire gas giant
filling the upper half of the sky, banded with darker indigo latitude
stripes, a faint violet haze at its pole, lighting the whole night
surface with a soft even blue planetshine. At the very top of the
frame, a faint arc of blue-violet auroral light crowns the zenith.
Below the horizon line: The plain is pale blue-grey nitrogen frost,
fine-grained and matte, crossed by low pressure ridges; under the
planetshine everything reads in tones of blue, and no colour warmer
than blue exists outside the artificial lamp pools. Near frame center
on the plain, two tiny suited figures work over a core drill, each
inside the small hard-edged white pool of its own helmet and chest
lamps. Forty meters from them at screen-right: the lander — the same
9-meter angular lifting-body craft, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool
of white light onto the blue-grey frost. Its canopy nose points
toward screen-right.

ENVIRONMENT: Night side of a large icy moon. Thin nitrogen
atmosphere, 2% of Earth pressure. -180°C. Gravity 0.4g. Exactly five
artificial light sources exist on this surface: two helmet lamps, two
chest lamps, and the lander's single belly floodlight.

CAMERA & LIGHT: 24mm spherical lens, fixed aerial position 300 meters
up. Main fill: soft even blue planetshine from the giant — shadowless.
The three white lamp pools are the only non-blue islands.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human
figures — no others anywhere. Both suits have NO back-mounted unit —
back silhouettes flat; visors optically clear, zero mirror coating.
0% bloom, no glow filter, no soft focus. The frost stays matte, the
hulls satin — never glossy. The aurora is blue-violet only — never
green. No readable text anywhere. No subtitles, no title card, no
watermark. Terrain static — no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
9-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off aerial camera, no camera movement. Exactly 2 human figures
in frame, tiny with distance, helmets closed.

SCENE: Camera 300 meters up, aimed just below the horizon: the upper
half of the frame is the blue giant — a deep sapphire gas giant
filling the upper half of the sky, banded with darker indigo latitude
stripes, a faint violet haze at its pole, lighting the whole night
surface with a soft even blue planetshine. A faint arc of blue-violet
auroral light crowns the zenith at the top of frame. Below: The plain
is pale blue-grey nitrogen frost, fine-grained and matte, crossed by
low pressure ridges; under the planetshine everything reads in tones
of blue, and no colour warmer than blue exists outside the artificial
lamp pools. Two tiny suited figures work over a core drill near frame
center, each in its own hard white lamp pool. Forty meters
screen-right: the lander — the same 9-meter angular lifting-body
craft, satin steel-blue with one thin SIGNAL-WHITE chevron line down
each flank, standing level on four landing legs, its single belly
floodlight cutting a hard-edged pool of white light onto the
blue-grey frost, its canopy nose pointing toward screen-right.
Exactly five artificial light sources exist on this
surface: two helmet lamps, two chest lamps, and the lander's single
belly floodlight.

TIMELINE:
0.0s — Stillness. Three white pools on a blue plain; the giant hangs
banded and silent above.
3.0s — One tiny figure kneels; its lamp pool shortens. The other
stands motionless.
6.0s — One slow wave crosses the auroral arc at the zenith, left to
right, taking a full 3 seconds.
9.0s — Nothing else has moved. Hold on the last frame.

AUDIO: A deep, muffled moon ground-tone, low and sparse; thin airy
hiss; one slow human breath over a radio channel. No high frequencies
— the atmosphere is too thin to carry them. No voice, no music.

PHYSICS: Gravity 0.4g, thin 2% atmosphere: nothing flutters, nothing
drifts. Real time, ordinary Earth pace.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no others. Both back
silhouettes flat — no back-mounted unit; visors optically clear, zero
mirror coating. 0% bloom, no glow filter, no soft focus. The frost
stays matte, the hulls satin — never glossy. The aurora is blue-violet
only — never green, casting no shadow. No readable text anywhere. No
subtitles, no title card, no watermark. Particles obey 0.4g with
continuous momentum — never hovering, never swirling. Terrain static —
no melting, no warping. The background is identical in every frame —
same planet, same sky, same horizon, same ridges: nothing in it
changes, appears or disappears during the shot. No Unreal Engine look,
no CGI aesthetic. Photorealistic with 35mm film grain. No speech, no
voice, no radio chatter, no callout, no music, no score — this scene
is wordless. No unnamed prop: nothing appears in or vanishes from a
hand, and no clipboard, tablet, screen or tool exists that this prompt
does not name.
```

---

## 🎬 SAHNE 1 (S1) — KAROT

> 🎯 **REFERANS:** **RE** p1·p2 + **RA** p1 (30 m arkada)
> ⚠️ **VIDEO PROMPTU V2 (18.08.2026)** — ilk üretimde figürler, iş ve
> araç doğru çıktı, ARKA PLAN değişti. Sebep prompt hatasıydı: gezegen
> çapa bloğu bu promptta PARAFRAZ yazılmıştı (IMAGE'da tam, VIDEO'da
> kısaltılmış) ve gökyüzü oranı ("upper half of the sky") kilitsiz
> kalmıştı. V2'de kanonik blok + kırağı kilidi birebir geri kondu,
> negatife arka plan sabitlik cümlesi eklendi. Ayrıntı: üretim notu ⑥.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a frost moon under blue planetshine, lamplight islands.
Exactly 2 human figures in frame — this film has exactly two humans
total.

SCENE: Two astronauts work over a core drill inside overlapping pools
of hard white lamplight. Kneeling: the engineer — woman, mid-thirties,
1.69 m, wiry, pale cool-toned skin with visible pores and faint
freckles, grey-green eyes, a small notch scar splitting her left
eyebrow, dark auburn hair in a near-shaved crop; same matte
cobalt-blue hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid AMBER accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile cobalt-blue
helmet CLOSED, her face fully readable through the visor. She draws a 40-cm core of milky blue-white nitrogen ice from the drill sleeve — solid, banded with thin darker layers, capped at each end by a machined grey collar that the gloves grip. Standing beside her: the pilot
— man, mid-forties, 1.83 m, broad-shouldered and lean, warm tan skin
with visible pores, dark brown eyes, a broad nose once broken at the
bridge, short black hair greying at the temples, a thin old scar on
his left cheekbone; matte cobalt-blue hard-shell suit, dark graphite
flex-weave joints, machined articulation rings, thin inlaid TEAL
accent lines on the shoulder plates and forearms, finely scuffed with
use; low-profile cobalt-blue helmet CLOSED, his face fully readable
through the visor. He holds an open slim sample case. Thirty meters
behind them: the lander — the same 9-meter angular lifting-body craft,
satin steel-blue with one thin SIGNAL-WHITE chevron line down each
flank, standing level on four landing legs, its single belly
floodlight cutting a hard-edged pool of white light onto the blue-grey
frost. Above, filling the upper sky: the blue giant — a deep sapphire
gas giant filling the upper half of the sky, banded with darker indigo
latitude stripes, a faint violet haze at its pole, lighting the whole
night surface with a soft even blue planetshine. The plain is pale
blue-grey nitrogen frost, fine-grained and matte, crossed by low
pressure ridges; under the planetshine everything reads in tones of
blue, and no colour warmer than blue exists outside the artificial
lamp pools. Each visor is one seamless optically clear pane in a 2-cm
brushed-metal frame, its lower seal ring visible where it meets the
suit collar, one thin specular line along its top edge — the glass is
always present, never absent.

CAMERA & LIGHT: 35mm spherical lens, fixed 8 meters from the pair at
chest height. Exactly five artificial light sources exist on this
surface: two helmet lamps, two chest lamps, and the lander's single
belly floodlight. Faces lit by lamp spill through clear visors.
-180°C, gravity 0.4g, thin 2% nitrogen atmosphere.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures, no extra faces in
reflections. Teal lines = pilot, amber lines = engineer — never
identical. The suits have NO back-mounted unit — both back silhouettes
are flat. No visor is tinted, mirrored, open or missing — no
environment reflection beyond that single specular line, and every
face behind glass stays fully readable; the face behind it is fully
readable. 0% bloom, no soft focus. Photorealistic skin with pores — no
airbrushing, no face morphing. The frost stays matte, the hulls satin
— never glossy. No readable text anywhere. No subtitles, no watermark.
Hand-object contacts keep clear structural boundaries — no merging, no
extra fingers. Particles obey 0.4g — never hovering. Terrain static.
No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off
camera, no camera move. Exactly 2 human figures in frame — this film
has exactly two humans total.

START FRAME: the approved still from this scene's IMAGE prompt.
Everything in that frame is already correct — faces, suits, helmets,
craft, sky, ground, framing. Do not redesign any of it; animate it.
CONTINUITY LOCKS carried from the frame: exactly 2 humans; thin TEAL
accent lines = the pilot (man, 1.83 m); thin AMBER accent lines = the
engineer (woman, 1.69 m); both helmets CLOSED, each visor a clear pane
in a 2-cm metal frame with a visible collar seal ring and one thin
specular line at its top edge; both backs flat with no back-mounted
unit.

SCENE (as in the start frame): Night surface under blue planetshine.
Overlapping hard white pools from their helmet and chest lamps; 30
meters behind them the lander — the same 9-meter angular lifting-body
craft, satin steel-blue with one thin SIGNAL-WHITE chevron line down
each flank, standing level on four landing legs, its single belly
floodlight cutting a hard-edged pool of white light onto the blue-grey
frost. Above, filling the upper sky: the blue giant — a deep sapphire
gas giant filling the upper half of the sky, banded with darker indigo
latitude stripes, a faint violet haze at its pole, lighting the whole
night surface with a soft even blue planetshine. The plain is pale
blue-grey nitrogen frost, fine-grained and matte, crossed by low
pressure ridges; under the planetshine everything reads in tones of
blue, and no colour warmer than blue exists outside the artificial
lamp pools. Camera fixed 8 meters away, 35mm spherical lens, chest
height.

TIMELINE: At 0.0s the closed sample case is already lying on the frost at the pilot's feet, lid down, and both of his gloves are empty and open at his sides — he carries nothing at any point. 0.0s — The engineer, kneeling, draws the 40-cm ice core from the drill sleeve, both gloves closed on the core's machined END CAP, never on the ice itself — careful, weighted, ordinary Earth pace. 3.5s — She holds it upright and still while the pilot crouches and lifts the case lid by its machined handle. 6.0s — She lowers the core into the cradle in one clean move; glove and cap stay separate objects throughout, with a visible gap closing to a hard contact. 8.5s — He closes the lid with the flat of his palm. A puff of frost dust from her boot falls and settles within 3 s.

AUDIO: Muffled low sounds only: drill sleeve scrape carried dull
through the ground, twin suit-fan hums on the closed comms channel —
carrier hiss only, thin airy hiss. No voices, no music.

PHYSICS: Gravity 0.4g — grounded, weighted movement, real time,
ordinary Earth pace, no slow motion. Thin air: nothing flutters. All
lifted dust falls and settles within 3 seconds.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicate,
no background figure, no face in reflections. Both suits have NO
back-mounted unit — back silhouettes flat. No visor is tinted,
mirrored, open or missing — no environment reflection beyond that
single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. Skin keeps pores — no airbrushing,
no face morphing. The frost stays matte — never glossy. No readable
text, subtitles or watermark. Hand contacts keep clear structural boundaries — gloves grip the machined end cap, fingers never sink into or merge with the ice or the case, no extra finger. Particles obey 0.4g — never
hovering, never swirling. The background is identical in every frame —
same planet, sky, horizon and ridges: nothing changes, appears or
disappears during the shot. No CGI aesthetic. Photorealistic with 35mm
film grain. No speech, voice, radio chatter, callout, music or score —
this scene is wordless. No unnamed prop: nothing appears in or vanishes from a hand; no clipboard, tablet, screen or unnamed tool. No auroral curtain, ribbon or green light in this frame.
```

---

## 🎬 SAHNE 2 (S2) — UYARI

> 🎯 **REFERANS:** **RE** p3 (ikisi yan yana) · **RA** p1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a frost moon; a vast auroral curtain has dropped from the
zenith. Exactly 2 human figures in frame — this film has exactly two
humans total.

SCENE: Two astronauts stand at the drill site, both helmets tilted
back, looking up. Foreground left: the pilot — man, mid-forties, 1.83
m, broad-shouldered and lean, warm tan skin with visible pores, dark
brown eyes, a broad nose once broken at the bridge, short black hair
greying at the temples, a thin old scar on his left cheekbone; matte
cobalt-blue hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid TEAL accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile cobalt-blue
helmet CLOSED, his face fully readable through the visor. Beside him:
the engineer — woman, mid-thirties, 1.69 m, wiry, pale cool-toned skin
with visible pores and faint freckles, grey-green eyes, a small notch
scar splitting her left eyebrow, dark auburn hair in a near-shaved
crop; same matte cobalt-blue hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
cobalt-blue helmet CLOSED, her face fully readable through the visor.
Overhead hangs the plasma curtain: translucent ribbons of electric
blue-violet light, their lower edge 70 degrees above the horizon,
rippling in one slow wave every 10 seconds. The curtain is light only
— it casts no shadow and never overpowers the blue planetshine. Its
colour is narrow blue-violet; it is never green. Behind the curtain:
the blue giant — a deep sapphire gas giant filling the upper half of
the sky, banded with darker indigo latitude stripes, a faint violet
haze at its pole, lighting the whole night surface with a soft even
blue planetshine. Thirty meters behind the pair: the lander — the same
9-meter angular lifting-body craft, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank, standing level on four
landing legs, its single belly floodlight cutting a hard-edged pool of
white light onto the blue-grey frost. The plain is pale blue-grey
nitrogen frost, fine-grained and matte, crossed by low pressure
ridges; under the planetshine everything reads in tones of blue, and
no colour warmer than blue exists outside the artificial lamp pools.
Each visor is one seamless optically clear pane in a 2-cm
brushed-metal frame, its lower seal ring visible where it meets the
suit collar, one thin specular line along its top edge — the glass is
always present, never absent.

CAMERA & LIGHT: 32mm spherical lens, fixed 10 meters from the pair at
chest height. Exactly five artificial light sources exist on this
surface: two helmet lamps, two chest lamps, and the lander's single
belly floodlight. -180°C, gravity 0.4g.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures. Teal lines = pilot, amber
lines = engineer — never identical. The suits have NO back-mounted
unit — both back silhouettes are flat. No visor is tinted, mirrored,
open or missing — no environment reflection beyond that single
specular line, and every face behind glass stays fully readable. 0%
bloom, no soft focus. The aurora is blue-violet only — never green,
never rainbow, casting no shadow. The frost stays matte — never
glossy. No readable text anywhere. No subtitles, no watermark. Terrain
static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off
camera, no camera move. Exactly 2 human figures in frame — this film
has exactly two humans total. One synthetic voice speaks over the
radio; no human speaks.

START FRAME: the approved still from this scene's IMAGE prompt.
Everything in that frame is already correct — faces, suits, helmets,
craft, sky, ground, framing. Do not redesign any of it; animate it.
CONTINUITY LOCKS carried from the frame: exactly 2 humans; thin TEAL
accent lines = the pilot (man, 1.83 m); thin AMBER accent lines = the
engineer (woman, 1.69 m); both helmets CLOSED, each visor a clear pane
in a 2-cm metal frame with a visible collar seal ring and one thin
specular line at its top edge; both backs flat with no back-mounted
unit.

SCENE (as in the start frame): The drill site under blue planetshine;
30 meters behind them the lander — the same 9-meter angular
lifting-body craft, satin steel-blue with one thin SIGNAL-WHITE
chevron line down each flank, standing level on four landing legs, its
single belly floodlight cutting a hard-edged pool of white light onto
the blue-grey frost. Overhead hangs the plasma curtain: translucent
ribbons of electric blue-violet light, their lower edge 70 degrees
above the horizon, rippling in one slow wave every 10 seconds — light
only, casting no shadow, never green. Behind it: the blue giant — a
deep sapphire gas giant filling the upper half of the sky, banded with
darker indigo latitude stripes, a faint violet haze at its pole,
lighting the whole night surface with a soft even blue planetshine.
The plain is pale blue-grey nitrogen frost, fine-grained and matte,
crossed by low pressure ridges; under the planetshine everything reads
in tones of blue, and no colour warmer than blue exists outside the
artificial lamp pools. Camera fixed 10 meters away, 32mm spherical
lens, chest height.

TIMELINE:
0.0s — Both work over the drill site, unhurried, ordinary Earth pace.
2.5s — A calm neutral synthetic voice over the radio, level and
unhurried, in Turkish: "Plazma yaprağı erken. Perde iniyor. Pencere
dört dakika."
5.0s — Both freeze. The pilot's helmet tilts back, up toward the
curtain; one second later the engineer's follows.
8.0s — Neither moves. One slow wave crosses the curtain overhead,
taking a full 3 seconds. Hold.

AUDIO: Muffled low world-tone; twin suit-fan hums and slow breathing
on the closed comms channel — carrier hiss only. The synthetic voice
at 2.5s is the only speech — heard only, never shown as text.

PHYSICS: Gravity 0.4g, real time, ordinary Earth pace. Thin air:
nothing flutters. The curtain light exerts no force.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures. Both suits have NO back-mounted unit — back
silhouettes flat. No visor is tinted, mirrored, open or missing — no
environment reflection beyond that single specular line, and every
face behind glass stays fully readable. 0% bloom, no soft focus. The
aurora is blue-violet only — never green, casting no shadow. The frost
stays matte — never glossy. No readable text anywhere. The spoken line
is heard only — no subtitles, no captions, no transcript. One speaker;
the synthetic voice is radio-only from the distant ship — no body, no
avatar, no third figure. No mouth is readable in frame. Particles obey
0.4g. Terrain static. The background is identical in every frame —
same planet, sky, horizon and ridges: nothing changes, appears or
disappears during the shot. No CGI aesthetic. Photorealistic with 35mm
film grain. Beyond the stated line there is no other voice, no
background chatter, no music, no score. No unnamed prop: nothing appears in or vanishes from a hand; no clipboard, tablet, screen or unnamed tool. No auroral curtain, ribbon or green light in this frame.
```

---

## 🎬 SAHNE 3 (S3) — TOPLAMA

> 🎯 **REFERANS:** **RE** p3 · **RA** p1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a frost moon; the auroral curtain has dropped lower.
Exactly 2 human figures in frame — this film has exactly two humans
total.

SCENE: Hurried but disciplined field-packing. In the foreground: the
engineer — woman, mid-thirties, 1.69 m, wiry, pale cool-toned skin
with visible pores and faint freckles, grey-green eyes, a small notch
scar splitting her left eyebrow, dark auburn hair in a near-shaved
crop; same matte cobalt-blue hard-shell suit, dark graphite flex-weave
joints, machined articulation rings, thin inlaid AMBER accent lines on
the shoulder plates and forearms, finely scuffed with use; low-profile
cobalt-blue helmet CLOSED, her face fully readable through the visor —
locking the slim sample case shut. A step behind, mid-stride toward
the craft: the pilot — man, mid-forties, 1.83 m, broad-shouldered and
lean, warm tan skin with visible pores, dark brown eyes, a broad nose
once broken at the bridge, short black hair greying at the temples, a
thin old scar on his left cheekbone; matte cobalt-blue hard-shell
suit, dark graphite flex-weave joints, machined articulation rings,
thin inlaid TEAL accent lines on the shoulder plates and forearms,
finely scuffed with use; low-profile cobalt-blue helmet CLOSED, his
face fully readable through the visor — carrying the folded drill
frame. A low kick of frost dust hangs at his boot, mid-fall.
Twenty-five meters behind: the lander — the same 9-meter angular
lifting-body craft, satin steel-blue with one thin SIGNAL-WHITE
chevron line down each flank, standing level on four landing legs, its
single belly floodlight cutting a hard-edged pool of white light onto
the blue-grey frost. Overhead hangs the plasma curtain: translucent
ribbons of electric blue-violet light, their lower edge 60 degrees
above the horizon, rippling in one slow wave every 10 seconds — light
only, casting no shadow, never green. Behind it, filling the sky: the
blue giant — a deep sapphire gas giant filling the upper half of the
sky, banded with darker indigo latitude stripes, a faint violet haze
at its pole, lighting the whole night surface with a soft even blue
planetshine. The plain is pale blue-grey nitrogen frost, fine-grained
and matte, crossed by low pressure ridges; under the planetshine
everything reads in tones of blue, and no colour warmer than blue
exists outside the artificial lamp pools. Each visor is one seamless
optically clear pane in a 2-cm brushed-metal frame, its lower seal
ring visible where it meets the suit collar, one thin specular line
along its top edge — the glass is always present, never absent.

CAMERA & LIGHT: 35mm spherical lens, fixed 6 meters away at chest
height. Exactly five artificial light sources exist on this surface:
two helmet lamps, two chest lamps, and the lander's single belly
floodlight. -180°C, gravity 0.4g.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures. Teal lines = pilot, amber
lines = engineer — never identical. The suits have NO back-mounted
unit — both back silhouettes are flat. No visor is tinted, mirrored,
open or missing — no environment reflection beyond that single
specular line, and every face behind glass stays fully readable. 0%
bloom, no soft focus. The aurora is blue-violet only — never green,
casting no shadow. The frost stays matte — never glossy. No readable
text anywhere. No subtitles, no watermark. Hand contacts keep clear
structural boundaries. Particles obey 0.4g — never hovering. Terrain
static. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera, no camera movement. Exactly 2 human figures
in frame — this film has exactly two humans total. No one speaks.

CHARACTERS: The engineer — woman, mid-thirties, 1.69 m, wiry, pale
cool-toned skin with visible pores and faint freckles, grey-green
eyes, a small notch scar splitting her left eyebrow, dark auburn hair
in a near-shaved crop; same matte cobalt-blue hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile cobalt-blue helmet CLOSED, her face fully
readable through the visor. The pilot — man, mid-forties, 1.83 m,
broad-shouldered and lean, warm tan skin with visible pores, dark
brown eyes, a broad nose once broken at the bridge, short black hair
greying at the temples, a thin old scar on his left cheekbone; matte
cobalt-blue hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid TEAL accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile cobalt-blue
helmet CLOSED, his face fully readable through the visor. Teal =
pilot, amber = engineer — never identical, never duplicated. Each
visor is one seamless optically clear pane in a 2-cm brushed-metal
frame, its lower seal ring visible where it meets the suit collar, one
thin specular line along its top edge — the glass is always present,
never absent.

SCENE: The drill site under blue planetshine; 25 meters behind, the
lander — the same 9-meter angular lifting-body craft, satin steel-blue
with one thin SIGNAL-WHITE chevron line down each flank, standing
level on four landing legs, its single belly floodlight cutting a
hard-edged pool of white light onto the blue-grey frost. Overhead the
plasma curtain: translucent ribbons of electric blue-violet light,
lower edge 60 degrees above the horizon, one slow wave every 10
seconds — never green, casting no shadow. The plain is pale blue-grey
nitrogen frost, fine-grained and matte, crossed by low pressure
ridges; under the planetshine everything reads in tones of blue, and
no colour warmer than blue exists outside the artificial lamp pools.
Camera fixed 6 meters away, 35mm spherical lens, chest height.

TIMELINE:
0.0s — The engineer snaps the sample case shut, both thumbs on the
latches — firm, unhurried, ordinary Earth pace.
3.0s — The pilot lifts the folded drill frame; a kick of frost dust
from his boot rises knee-high, falls, and settles within 3 seconds.
6.0s — She stands with the case; both turn toward the lander,
shoulders square to it.
9.0s — They walk out of the near pool of lamplight into the blue
half-light, backs to camera. Hold.

AUDIO: Muffled low world-tone; case latches click dull through the
ground; twin suit-fan hums and controlled breathing on the closed
comms channel — carrier hiss only. No voices, no music.

PHYSICS: Gravity 0.4g — grounded, weighted, real time, ordinary
Earth pace, no slow motion. Lifted dust settles within 3 seconds.
Thin air: nothing flutters.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures. The suits have NO back-mounted unit — both back
silhouettes are flat. No visor is tinted, mirrored, open or missing —
no environment reflection beyond that single specular line, and every
face behind glass stays fully readable. 0% bloom, no soft focus. The
aurora is blue-violet only — never green, casting no shadow. The frost
stays matte — never glossy. No readable text anywhere. No subtitles,
no watermark. Particles obey 0.4g — never hovering, never swirling.
Terrain static. The background is identical in every frame — same
planet, same sky, same horizon, same ridges: nothing in it changes,
appears or disappears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. No speech, no voice, no radio
chatter, no callout, no music, no score — this scene is wordless. No
unnamed prop: nothing appears in or vanishes from a hand, and no
clipboard, tablet, screen or tool exists that this prompt does not
name.
```

---

## 🎬 SAHNE 4 (S4) — VİRAL #1: PERDE (nötr çekim — kameraya koşu)

> 🎯 **REFERANS:** **RE** p3 ⭐ (koşu — boy farkı + kutu) · **RA** p4 (bacak + chine yakını)

> ⚠️ ÜRETİM NOTU ⑤: Kamera LANDERİN YANINDADIR; koşu kameraya doğru =
> araca doğru (Black Cradle S4 V3'ün kanıtlanmış çözümü, ilk denemede).
> Baskın ışık TEPEDE — negatifte "neither figure looks up" zorunlu.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
surface of a frost moon; a vast auroral curtain fills the upper half
of the sky. Exactly 2 human figures in frame — this film has exactly
two humans total.

SCENE: Camera stands at ground level beside the lander's landing leg,
looking straight out across the open plain. Running TOWARD the camera
across the frost, 40 meters out: first the pilot — man, mid-forties,
1.83 m, broad-shouldered and lean, warm tan skin with visible pores,
dark brown eyes, a broad nose once broken at the bridge, short black
hair greying at the temples, a thin old scar on his left cheekbone;
matte cobalt-blue hard-shell suit, dark graphite flex-weave joints,
machined articulation rings, thin inlaid TEAL accent lines on the
shoulder plates and forearms, finely scuffed with use; low-profile
cobalt-blue helmet CLOSED, his face fully readable through the visor —
empty-handed, one full stride ahead. Behind him: the engineer — woman,
mid-thirties, 1.69 m, wiry, pale cool-toned skin with visible pores
and faint freckles, grey-green eyes, a small notch scar splitting her
left eyebrow, dark auburn hair in a near-shaved crop; same matte
cobalt-blue hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid AMBER accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile cobalt-blue
helmet CLOSED, her face fully readable through the visor — carrying
the slim sample case. Both faces are toward the camera, shoulders
square to it, eyes level — neither looks up. Above and behind them the
sky is a wall: Overhead hangs the plasma curtain: translucent ribbons
of electric blue-violet light, their lower edge 50 degrees above the
horizon, rippling in one slow wave every 10 seconds. The curtain is
light only — it casts no shadow and never overpowers the blue
planetshine. Its colour is narrow blue-violet; it is never green.
Below it: the blue giant — a deep sapphire gas giant filling the upper
half of the sky, banded with darker indigo latitude stripes, a faint
violet haze at its pole, lighting the whole night surface with a soft
even blue planetshine, its banded limb meeting the horizon. At the
frame's right edge, close to camera: one landing leg and the lower
chine line of the lander, satin steel-blue with its thin SIGNAL-WHITE
chevron, its belly floodlight laying a hard pool of white light across
the foreground frost. The plain is pale blue-grey nitrogen frost,
fine-grained and matte, crossed by low pressure ridges; under the
planetshine everything reads in tones of blue, and no colour warmer
than blue exists outside the artificial lamp pools. Each visor is one
seamless optically clear pane in a 2-cm brushed-metal frame, its lower
seal ring visible where it meets the suit collar, one thin specular
line along its top edge — the glass is always present, never absent.

CAMERA & LIGHT: 32mm spherical lens, fixed at ground level beside the
lander, 1.2 meters high. Exactly five artificial light sources exist
on this surface: two helmet lamps, two chest lamps, and the lander's
single belly floodlight. Gravity 0.4g, -180°C.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures — no extra
crew, no duplicates, no background figures. Teal lines = pilot, amber
lines = engineer — never identical. Neither figure looks up; no
direction reversal — both run toward the camera. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. The aurora is blue-violet only —
never green, never rainbow, casting no shadow. The frost stays matte —
never glossy. No readable text anywhere. No subtitles, no watermark.
Particles obey 0.4g. Terrain static. No CGI aesthetic. Photorealistic
with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera at ground level beside the lander, no camera
movement. Exactly 2 human figures in frame — this film has exactly
two humans total. No one speaks.

START FRAME: the approved still from this scene's IMAGE prompt.
Everything in that frame is already correct — faces, suits, helmets,
craft, sky, ground, framing. Do not redesign any of it; animate it.
CONTINUITY LOCKS carried from the frame: exactly 2 humans; thin TEAL
accent lines = the pilot (man, 1.83 m); thin AMBER accent lines = the
engineer (woman, 1.69 m); both helmets CLOSED, each visor a clear pane
in a 2-cm metal frame with a visible collar seal ring and one thin
specular line at its top edge; both backs flat with no back-mounted
unit.

SCENE (as in the start frame): Camera at ground level beside the
lander's landing leg — running toward the camera IS running toward the
craft. Behind and above the runners, the sky is a wall: the plasma
curtain, translucent ribbons of electric blue-violet light, lower edge
50 degrees above the horizon, rippling in one slow wave every 10
seconds — light only, casting no shadow, never green. Below it: the
blue giant — a deep sapphire gas giant filling the upper half of the
sky, banded with darker indigo latitude stripes, a faint violet haze
at its pole, lighting the whole night surface with a soft even blue
planetshine, its banded limb meeting the horizon. Frame right, close:
one landing leg and the lower chine of the satin steel-blue hull, the
belly floodlight laying a hard white pool across the foreground frost;
the craft's canopy nose points toward screen-right, out of frame. The
plain is pale blue-grey nitrogen frost, fine-grained and matte,
crossed by low pressure ridges; under the planetshine everything reads
in tones of blue, and no colour warmer than blue exists outside the
artificial lamp pools.

TIMELINE:
0.0s — Both figures mid-run, 40 meters out, closing toward camera —
real running gait, grounded, ordinary Earth pace. Faces toward
camera, eyes level; neither looks up.
4.0s — 20 meters out. One slow wave rolls across the curtain above
them, taking 3 seconds; small kicks of frost dust fall behind their
boots and settle within 3 seconds.
8.0s — The pilot reaches the edge of the floodlight pool, filling
frame left; the engineer is one stride behind with the case.
10.0s — Hold as both cross into the white pool.

AUDIO: Rhythmic muffled boot impacts carried through the ground; two
sets of controlled hard breathing on the closed comms channel —
carrier hiss only; thin airy hiss. No voices, no music.

PHYSICS: Gravity 0.4g — real running, grounded, weighted, real time,
ordinary Earth pace, no slow motion. Dust settles within 3 seconds.
The curtain exerts no force.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures — no extra crew, no duplicates,
no background figures; neither looks up, neither turns back, no
direction reversal — both run toward the camera the whole shot. Both
suits have NO back-mounted unit — back silhouettes flat. Each visor is
optically clear glass — zero tint, zero mirror coating, zero
environment reflection. 0% bloom, no soft focus. The aurora is
blue-violet only — never green, no shadow. The frost stays matte —
never glossy. No readable text, no subtitles, no watermark. Particles
obey 0.4g — never hovering, never swirling. The background is
identical in every frame — same planet, same sky, same horizon:
nothing changes or appears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. No speech, voice, radio chatter,
callout, music or score — this scene is wordless. No unnamed prop:
nothing appears in or vanishes from a hand; no clipboard, tablet,
screen or unnamed tool.
```

---

## 🎬 SAHNE 5 (S5) — BİNİŞ (arkadan · uçuş güvertesi)

> 🎯 **REFERANS:** **RD** p1 ⭐ (arkadan geniş — bu sahnenin birebir
> kadrajı) · **RD** p4 (canlı panel) · **RE** (arkadan sürümler)

> [D69 ①] Kapak/merdiven hareketi kadraj DIŞI: S4 koşuyla biter, S5
> kabinde kayış takarken açılır.
> ⚠️ **18.08.2026 · İKİ DEĞİŞİKLİK:** ① kabin "uçuş güvertesi" olarak
> büyütüldü (koltuk kabukları + boru çizgisi + tavan kemeri + üç panelli
> kanopi — kilitler aynı) · ② sahne TAMAMEN ARKADAN kadraja alındı,
> **yüz 0 kare**. Rol kanalı artık iki katman: suit çizgisi + koltuk
> boru çizgisi (solda turkuaz, sağda amber).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. The flight
deck of a small two-seat spacecraft, seen from behind the crew, night.
Exactly 2 human figures in frame — this film has exactly two humans
total.

SCENE: A 2.2-metre-wide flight deck. THE COCKPIT: two high-backed machined seat shells side by side — thin TEAL piping down the left seat back, AMBER down the right — a machined console spine between them, canted side consoles at both elbows, a ribbed overhead arch carrying six guarded toggles and two recessed teal strip lights, and a three-pane wraparound canopy: one wide central pane flanked by two angled quarter-panes in graphite frames.

BOTH CREW ARE SEEN FROM DIRECTLY BEHIND — the backs of two helmets, two seat shells and two shoulder lines. No face is visible anywhere in this shot, and none is reflected in the glass. Left seat: the pilot, man, 1.83 m, matte cobalt-blue hard-shell suit, thin inlaid TEAL accent lines on the shoulder plates and forearms, low-profile cobalt-blue helmet CLOSED, its collar seal ring visible at the back of his neck. Right seat: the engineer, woman, 1.69 m, same matte cobalt-blue suit with thin inlaid AMBER accent lines, low-profile cobalt-blue helmet CLOSED, its collar seal ring visible at the back of her neck. Both backs are flat — no backpack, no tank, no hose, no cable, no rear housing of any kind. The pilot has both cross-harness straps drawn over his shoulder
plates, hands at the centre buckle; the engineer is seating the slim
sample case into a rack at her right elbow. Ahead of them the analog
panel: abstract amber and teal light segments with no text, a 12-cm
mechanical attitude sphere at centre, softly back-lit. Beyond the
three canopy panes: the pale blue-grey nitrogen frost plain under blue
planetshine, and high in the central pane the lower ribbons of the
blue-violet plasma curtain.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.2 metres behind the seat backs and 20 cm above them, centred on the console spine, looking forward through the canopy. Cabin light is low and directional: the two overhead teal strips wash down the seat backs and helmet crowns, the panel's amber and teal segments throw a warm-cool edge onto both shoulder lines, a thin blue rim light runs along the floor sill, and blue planetshine comes flat through the three canopy panes.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both seen from behind — no extra crew, no duplicate, no third seat, no figure outside the canopy. NO FACE anywhere: not turned, not in profile, not reflected in the glass or in any surface. Teal piping and teal accent lines = the pilot on the left; amber = the engineer on the right — never swapped, never identical. Both backs are flat — no back-mounted unit of any kind. Both helmets stay CLOSED and locked, each collar seal ring visible — no helmet is removed, lifted or half-worn. Exactly six guarded toggles on the overhead arch, exactly two overhead strips, exactly three canopy panes — these counts never change. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits or symbols on any panel, toggle or surface — abstract light segments only; no screen, no display graphics, no hologram, no HUD. The aurora in the glass is blue-violet only — never green. No unnamed prop: nothing appears in or vanishes from a hand; no clipboard, tablet, screen or unnamed tool. Hand contacts keep clear structural boundaries — no merging, no extra finger. No subtitles, no watermark. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off
camera, no camera move. Exactly 2 human figures in frame, both seen
from directly behind — this film has exactly two humans total. No one
speaks.

SCENE: The flight deck of a small two-seat spacecraft. THE COCKPIT:
two high-backed machined seat shells side by side — thin TEAL piping
down the left seat back, AMBER down the right — a machined console
spine between them, canted side consoles at both elbows, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy: one wide central pane
flanked by two angled quarter-panes in graphite frames.

BOTH CREW ARE SEEN FROM DIRECTLY BEHIND — the backs of two helmets,
two seat shells and two shoulder lines. No face is visible anywhere in
this shot, and none is reflected in the glass. Both wear the same
matte cobalt-blue hard-shell suit. Left seat: the pilot, man, 1.83 m,
thin inlaid TEAL accent lines on the shoulder plates and forearms,
low-profile cobalt-blue helmet CLOSED, its collar seal ring visible at
the back of his neck. Right seat: the engineer, woman, 1.69 m, thin
inlaid AMBER accent lines, low-profile cobalt-blue helmet CLOSED, its
collar seal ring visible at the back of her neck. Both backs are flat
— no backpack, no tank, no hose, no cable, no rear housing of any
kind. Beyond the three canopy panes: the frost plain under blue
planetshine, the lower ribbons of the blue-violet plasma curtain high
in the central pane. The analog panel ahead carries abstract amber and
teal light segments and a 12-cm mechanical attitude sphere at centre.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.2 metres behind the seat
backs and 20 cm above them, centred on the console spine, looking
forward through the canopy. Cabin light is low and directional: the
two overhead teal strips wash down the seat backs and helmet crowns,
the panel's amber and teal segments throw a warm-cool edge onto both
shoulder lines, a thin blue rim light runs along the floor sill, and
blue planetshine comes flat through the three canopy panes.

TIMELINE:
0.0s — The engineer, on the right, pushes the slim sample case into
the rack at her elbow; a dull latch click. Her gloves and the case
stay separate objects, contact hard and clean.
2.5s — The pilot draws both harness straps down over his shoulder
plates to the centre buckle — one clean metallic seat.
5.0s — She pulls her own straps tight; both pairs of gloves settle
onto the armrests and stop moving.
7.5s — The attitude sphere's backlight steadies; a faint vibration
begins in the airframe and the two overhead teal strips hold even.
10.0s — Hold: two helmet backs and two seat shells against the wide
blue view.

AUDIO: Close, quiet interior — harness buckles seating, twin suit-fan
hums on the closed comms channel — carrier hiss only, a low airframe
tick as systems spin up. No voices, no music.

PHYSICS: Gravity 0.4g inside the parked craft — weighted arms,
ordinary Earth pace, real time. Nothing floats.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, seen from
behind — no extra crew, no duplicate, no third seat. NO FACE anywhere:
not turned, not in profile, not reflected. Teal piping and teal accent
lines = the pilot on the left; amber = the engineer on the right —
never swapped, never identical. Both backs are flat — no back-mounted
unit of any kind. Both helmets stay CLOSED and locked — none removed,
lifted or half-worn. Exactly six guarded toggles on the overhead arch,
exactly two overhead strips, exactly three canopy panes — these counts
never change. 0% bloom, no glow filter, no soft focus. No readable
text, letters or digits on any panel, toggle or surface — abstract
light segments only; no screen, no HUD, no hologram. The aurora in the
glass is blue-violet only — never green. No unnamed prop: nothing
appears in or vanishes from a hand. Hand contacts keep clear
structural boundaries — no merging, no extra finger. No subtitles, no
watermark. No CGI aesthetic. Photorealistic with 35mm film grain. The
background beyond the canopy is identical in every frame — same plain,
same curtain, same horizon: nothing changes, appears or disappears
during the shot. No speech, voice, radio chatter or music — this scene
is wordless.
```

## 🎬 SAHNE 6 (S6) — ATEŞLEME

> 🎯 **REFERANS:** **RD** p1·p4 · **RE** (arkadan sürümler)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Two-seat
spacecraft cockpit from behind, night launch imminent. Exactly 2
human figures in frame, seen from behind — this film has exactly two
humans total.

SCENE: Camera directly behind and between the two headrests, 1.5
meters back, looking forward over their shoulders — no face visible,
both figures read by suit and helmet from behind. Left: the pilot —
man, mid-forties, 1.83 m, broad-shouldered and lean; matte cobalt-blue
hard-shell suit, dark graphite flex-weave joints, machined
articulation rings, thin inlaid TEAL accent lines on the shoulder
plates and forearms, finely scuffed with use; low-profile cobalt-blue
helmet CLOSED — his gloved right hand closed firmly around the flight
lever. Right: the engineer — woman, mid-thirties, 1.69 m, wiry; same
matte cobalt-blue hard-shell suit with thin inlaid AMBER accent lines
on the shoulder plates and forearms, finely scuffed with use;
low-profile cobalt-blue helmet CLOSED — both her gloves flat on the
armrests. Ahead, the analog panel: abstract amber and teal light
segments brightened to launch state, no text, the 12-cm mechanical
attitude sphere level at center. Through the central canopy pane (1.4
× 0.5 m): the pale blue-grey frost plain under blue planetshine, and
in the upper third of the glass the ribbons of the plasma curtain,
their lower edge 45 degrees above the horizon — electric blue-violet,
never green. COCKPIT: two high-backed machined seat shells — thin TEAL
piping down the left seat back, AMBER down the right — a machined
console spine between them, canted side consoles, a ribbed overhead
arch carrying six guarded toggles and two recessed teal strip lights,
and a three-pane wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats at headrest height. Cabin dim; panel segments and sphere
backlight are the main sources; blue planetshine through the glass.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both seen
from behind — no extra crew, no duplicates, no faces in reflections.
Teal lines = pilot, amber lines = engineer — never identical. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. No readable text, letters or
digits anywhere — abstract light segments only. The aurora in the
glass is blue-violet only — never green. No subtitles, no watermark.
No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the cockpit, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. Two radio voices speak, one at a time;
no mouth is ever visible.

SCENE: Camera directly behind and between the two headrests, 1.5
meters back, looking forward over their shoulders. Left seat: the
pilot — man, mid-forties, 1.83 m, broad-shouldered and lean; matte
cobalt-blue hard-shell suit, thin inlaid TEAL accent lines on the
shoulder plates and forearms; low-profile cobalt-blue helmet CLOSED —
right glove on the flight lever. Right seat: the engineer — woman,
mid-thirties, 1.69 m, wiry; same suit with thin inlaid AMBER accent
lines; low-profile cobalt-blue helmet CLOSED — gloves flat on the
armrests. Teal = pilot, amber = engineer — never identical, never
duplicated. Analog panel in launch state: abstract amber and teal
segments, no text, 12-cm mechanical attitude sphere level. Through the
1.4 × 0.5 m central canopy pane: frost plain in blue planetshine,
curtain ribbons in the upper third of the glass, lower edge 45 degrees
— blue-violet, never green. COCKPIT: two high-backed machined seat
shells — thin TEAL piping down the left seat back, AMBER down the
right — a machined console spine between them, canted side consoles, a
ribbed overhead arch carrying six guarded toggles and two recessed
teal strip lights, and a three-pane wraparound canopy in machined
graphite frames.

TIMELINE:
0.0s — Still cockpit; a low airframe vibration builds slowly.
1.5s — The pilot's voice over the radio, low and even, in Turkish:
"Kalkıyoruz. Sıkı tutun."
4.5s — A calm neutral synthetic voice answers through the radio,
level, in Turkish: "Motorlar hazır. Pencere sekiz saniye."
7.0s — The pilot's glove tightens on the lever; panel segments step
one notch brighter.
9.0s — The airframe vibration deepens. Hold — the launch itself is
not in this shot.

AUDIO: Low rising airframe rumble, harness creak, twin suit-fan hums.
The two radio lines are the only speech — one speaker at a time,
heard only, never shown as text.

PHYSICS: Gravity 0.4g, real time. Vibration is subtle — nothing
shakes loose, nothing floats.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. No readable text anywhere —
abstract light segments only. The spoken lines are heard only — no
subtitles, no captions, no transcript. One speaker at a time; the
synthetic voice is radio-only from the distant ship — no body, no
avatar, no third figure. No mouth is readable in frame. The aurora in
the glass is blue-violet only — never green. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 7 (S7) — VİRAL #2: KALKIŞ

> 🎯 **REFERANS:** **RA** p1 → p2 ⭐ (bacak katlanışı — durum çifti geçişin kendisi)

> ⛔ ÜRETİM KAPISI 3 (plan sırası: S21 → S15 → S4 → S0; S7 kapı listesi
> dışında ama kalkış reçetesi Cold Burn'de kanıtlı — reçete değişmez).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night
launch from a frost moon under a giant blue planet. Human count in
this frame: zero — both crew are inside the craft.

SCENE: Wide exterior, 80 meters from the craft, camera at 2 meters
height. Caught at the first instant of launch: the lander — a 9-meter
angular LIFTING-BODY craft, no plain cylinder: broad flat belly, sharp
chine lines running nose to tail, a low blended forward canopy, two
short swept strakes, twin main engines recessed in a notched tail,
four downward LIFT NOZZLES under the belly, four landing legs that
fold up into flush belly wells, recessed thruster quads at bow and
stern, and a 40-cm domed emergency-beacon housing on the left shoulder
line; satin steel-blue composite panels with crisp recessed seams over
a graphite-grey structural spine, one thin SIGNAL-WHITE chevron line
down each flank, and a side hatch — its canopy nose pointing toward
screen-right. All four belly LIFT NOZZLES are firing straight down —
four tight warm-white jets, the first warm light this blue world has
seen. Their light pushes the blue off the frost in a 30-meter radius,
revealing its fine grain in warm white; four distinct rings of frost
dust kick outward in low ballistic arcs. The craft still stands level
on its four legs, a hand's width of light already under each footpad.
Above: the plasma curtain, translucent electric blue-violet ribbons,
lower edge 40 degrees above the horizon, one slow wave every 10
seconds — never green; behind it: the blue giant — a deep sapphire gas
giant filling the upper half of the sky, banded with darker indigo
latitude stripes, a faint violet haze at its pole, lighting the whole
night surface with a soft even blue planetshine. The plain is pale
blue-grey nitrogen frost, fine-grained and matte, crossed by low
pressure ridges; under the planetshine everything reads in tones of
blue, and no colour warmer than blue exists outside the artificial
lamp pools.

CAMERA & LIGHT: 32mm spherical lens, fixed 80 meters away, 2 meters
high. Sources: four warm-white jets (dominant, local), blue
planetshine everywhere else, curtain overhead. -180°C, gravity 0.4g,
thin 2% atmosphere.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the craft. 0% bloom, no glow
filter, no soft focus. The frost stays matte, the hull satin — never
glossy. The aurora is blue-violet only — never green. No readable
text anywhere. No subtitles, no title card, no watermark. Dust obeys
0.4g in ballistic arcs — never hovering, never swirling. Terrain and
hull static — no melting, no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera, no camera movement. Human count in this
frame: zero — both crew are inside the craft.

SCENE: Wide exterior, camera fixed 80 meters from the craft at 2
meters height, 32mm spherical lens. The lander — a 9-meter angular
LIFTING-BODY craft, no plain cylinder: broad flat belly, sharp chine
lines running nose to tail, a low blended forward canopy, two short
swept strakes, twin main engines recessed in a notched tail, four
downward LIFT NOZZLES under the belly, four landing legs that fold up
into flush belly wells, recessed thruster quads at bow and stern, and
a 40-cm domed emergency-beacon housing on the left shoulder line;
satin steel-blue composite panels with crisp recessed seams over a
graphite-grey structural spine, one thin SIGNAL-WHITE chevron line
down each flank, and a side hatch — its canopy nose pointing toward
screen-right. Above: the plasma curtain, electric blue-violet ribbons,
lower edge 40 degrees above the horizon — never green; behind it: the
blue giant — a deep sapphire gas giant filling the upper half of the
sky, banded with darker indigo latitude stripes, a faint violet haze
at its pole, lighting the whole night surface with a soft even blue
planetshine. The plain is pale blue-grey nitrogen frost, fine-grained
and matte, crossed by low pressure ridges; under the planetshine
everything reads in tones of blue, and no colour warmer than blue
exists outside the artificial lamp pools.

TIMELINE (four-step launch — exact order):
0.0s — All four belly LIFT NOZZLES fire straight down: four tight
warm-white jets, four rings of frost dust kicking outward in low
ballistic arcs that settle within 3 seconds. The jet light pushes the
blue off the frost in a 30-meter radius — the first warm light this
world has seen.
1.5s — The craft rises LEVEL, dead flat, on the four jets.
4.5s — At 20 meters height all four landing legs fold up into their
flush belly wells; the gear doors close — after 4.5s no landing leg,
no leg well and no open gear door is visible in any frame.
6.0s — The twin main engines in the notched tail light with a hard
warm-white glare; the belly jets cut out.
8.0s — The craft accelerates with its nose toward the upper-right
corner of the frame, its warm light shrinking; the frost below fades
back to blue.
10.0s — Only a receding point of engine light under the curtain.
Hold.

AUDIO: A deep muffled double concussion carried through the ground,
then a sustained low muffled roar that thins as the craft climbs; no
high frequencies. No voices, no music.

PHYSICS: Gravity 0.4g, thin 2% atmosphere. Dust rings are ballistic:
out, down, settled within 3 seconds — no hanging curtain of dust. The
tail engines never point at the ground; the craft never pitches
vertical. Real time.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the craft. 0% bloom, no glow filter, no soft focus. After 4.5s no
landing leg, no leg well and no open gear door is visible in any
frame. The frost stays matte, the hull satin — never glossy. The
aurora is blue-violet only — never green. No readable text anywhere.
No subtitles, no title card, no watermark. Dust obeys 0.4g with
continuous momentum — never hovering, never swirling. Terrain and hull
static — no melting, no warping. The background is identical in every
frame — same planet, same sky, same horizon, same ridges: nothing in
it changes, appears or disappears during the shot. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain. No
speech, no voice, no radio chatter, no callout, no music, no score —
this scene is wordless. No unnamed prop: nothing appears in or
vanishes from a hand, and no clipboard, tablet, screen or tool exists
that this prompt does not name.
```

---

## 🎬 SAHNE 8 (S8) — PERDENİN KENARI

> 🎯 **REFERANS:** **RA** p2 (uçuş konfigürasyonu)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A small
spacecraft climbing through the lower edge of an auroral curtain,
high above a frost moon. Human count in this frame: zero — both crew
are inside the craft.

SCENE: High altitude, the horizon a soft blue curve low in the frame.
Center: the lander — the same 9-meter angular lifting-body craft in
FLIGHT CONFIGURATION, all four landing legs folded away into flush
belly wells, its belly line clean, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank — climbing nose-high, its
canopy nose pointing toward the upper right of frame, through the
LOWER EDGE of the plasma curtain: translucent electric
blue-violet ribbons fill the middle of the frame around and above the
craft, rippling in one slow wave every 10 seconds, never green. Along
the hull's upper edges run a few thin, pale blue-white static
filaments — short, hair-thin, tracing the chine lines for a moment.
Above the curtain, black sky and hard stars; below, the frost plain
curves away in soft blue planetshine, and the blue giant — a deep sapphire gas giant banded with darker indigo latitude stripes, a faint violet haze at its pole, its sunlit curve washing every shadow with a soft blue albedo fill, its banded limb rising at frame left. The twin tail engines burn steady
warm-white.

CAMERA & LIGHT: 32mm spherical lens, fixed in space ahead and to the
side of the climb path, craft 60 meters away. Sources: curtain light
(soft, shadowless), engine glare (warm, local), blue planetshine from
below.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the craft. 0% bloom, no glow
filter, no soft focus. The hull stays satin — never glossy. The
aurora is blue-violet only — never green; the static filaments are
hair-thin and brief — no lightning bolts, no sparks, no fire, no
explosion. No landing leg, no leg well, no open gear door visible.
No readable text anywhere. No subtitles, no title card, no watermark.
Hull static — no melting, no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera in space, no camera movement. Human count in
this frame: zero — both crew are inside the craft.

SCENE: High above the frost moon; horizon a soft blue curve low in
frame, the blue giant — a deep sapphire gas giant banded with darker
indigo latitude stripes, a faint violet haze at its pole, its sunlit
curve washing every shadow with a soft blue albedo fill, its banded
limb rising at frame left. The lander — the same 9-meter angular
lifting-body craft in FLIGHT CONFIGURATION, all four landing legs
folded away into flush belly wells, its belly line clean, satin
steel-blue with one thin SIGNAL-WHITE chevron line down each flank —
climbs nose-high, its canopy nose pointing toward the upper right of
frame, on twin warm-white tail engines, entering the LOWER EDGE of the
plasma curtain: translucent electric blue-violet ribbons, one slow
wave every 10 seconds, never green. Camera fixed 60 meters off the
climb path, 32mm spherical lens.

TIMELINE:
0.0s — The craft climbs into the curtain's lower ribbons; the
blue-violet light slides across the satin hull.
2.0s — Thin pale blue-white static filaments trace the chine lines
and the beacon dome for about 2 seconds, then die — hair-thin, brief,
no sparks.
4.5s — The craft clears the upper edge of the ribbons into black
star-field.
6.5s — Hard white sunlight strikes the hull for the first time from
frame left: a razor rim along the chines, the shadow side softened by
faint blue albedo fill from the giant below.
9.0s — The engines burn steady; the craft shrinks slowly toward the
upper right. Hold.

AUDIO: Sound thins away to nothing as the craft climbs out of the
atmosphere — by 5s, hard vacuum silence except a faint radio-static
bed. No voices, no music.

PHYSICS: Thin air fading to vacuum; no shockwaves, no buffeting
visible. The static filaments carry no force. Stars stay sharp fixed
points — no streaks, no trails. Real time.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the craft. 0% bloom, no glow filter, no soft focus. The hull stays
satin — never glossy. The aurora is blue-violet only — never green;
the filaments are hair-thin and brief — no lightning, no sparks, no
fire, no explosion, no debris. No landing leg, no leg well and no open
gear door is visible in any frame. No readable text anywhere. No
subtitles, no title card, no watermark. Hull static — no melting, no
warping. The background is identical in every frame — same planet,
same sky, same horizon, same ridges: nothing in it changes, appears or
disappears during the shot. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. No speech, no voice, no radio
chatter, no callout, no music, no score — this scene is wordless. No
unnamed prop: nothing appears in or vanishes from a hand, and no
clipboard, tablet, screen or tool exists that this prompt does not
name.
```

---

## 🎬 SAHNE 9 (S9) — ÖLÜ ARAÇ

> 🎯 **REFERANS:** **RD** p4 → p2 ⭐ (panel ölümü — canlı→ölü çifti) · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dying
spacecraft cabin in orbit, lights failing. Exactly 2 human figures in
frame, seen from behind — this film has exactly two humans total.

SCENE: Camera directly behind and between the two headrests, 1.5
meters back. Left: the pilot — man, mid-forties, 1.83 m,
broad-shouldered and lean; matte cobalt-blue hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
TEAL accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile cobalt-blue helmet CLOSED, its collar seal ring
visible. Right: the engineer — woman, mid-thirties, 1.69 m, wiry; same
suit with thin inlaid AMBER accent lines, finely scuffed with use;
low-profile cobalt-blue helmet CLOSED, its collar seal ring visible.
Both strapped in, seated, motionless. The analog panel ahead is DYING:
most of its abstract amber and teal light segments already dark, a
last few segments at the right edge still lit. What remains alive: the
pale backlight of the 12-cm mechanical attitude sphere and the soft
phosphor face of a 12-cm mechanical pressure dial — an unnumbered arc
scale with ten tick marks, needle high. Through the central canopy
pane (1.4 × 0.5 m): black space, hard stars, and the sunlit blue curve
of the giant filling the lower glass, washing the dark cabin in faint
blue. COCKPIT: two high-backed machined seat shells — thin TEAL piping
down the left seat back, AMBER down the right — a machined console
spine between them, canted side consoles, a ribbed overhead arch
carrying six guarded toggles and two recessed teal strip lights, and a
three-pane wraparound canopy in machined graphite frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: the dying panel remnants, sphere backlight, phosphor
dial, blue planet-light through the glass. Dim, cold, quiet.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus. The failure is silent and
dark — no sparks, no smoke, no fire; the lights simply go out. No
readable text, letters or digits anywhere — abstract segments, an
unnumbered dial. No subtitles, no watermark. No CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the cabin, no camera movement. Exactly
2 human figures in frame, both seen from behind — this film has
exactly two humans total. One synthetic radio voice speaks and is CUT
OFF mid-word; no human speaks.

SCENE: Camera directly behind and between the two headrests, 1.5
meters back, 35mm spherical lens. Left seat: the pilot — man,
mid-forties, 1.83 m, broad-shouldered and lean; matte cobalt-blue
hard-shell suit with thin inlaid TEAL accent lines on the shoulder
plates and forearms; low-profile cobalt-blue helmet CLOSED, its collar
seal ring visible. Right seat: the engineer — woman, mid-thirties,
1.69 m, wiry; same suit with thin inlaid AMBER accent lines;
low-profile cobalt-blue helmet CLOSED, its collar seal ring visible.
Teal = pilot, amber = engineer — never identical, never duplicated.
Both strapped in, motionless. Analog panel lit in launch state:
abstract amber and teal segments, no text; 12-cm mechanical attitude
sphere; 12-cm mechanical pressure dial with unnumbered arc scale,
needle high. Through the 1.4 × 0.5 m central canopy pane: black space,
hard stars, the sunlit blue curve of the giant low in the glass.
COCKPIT: two high-backed machined seat shells — thin TEAL piping down
the left seat back, AMBER down the right — a machined console spine
between them, canted side consoles, a ribbed overhead arch carrying
six guarded toggles and two recessed teal strip lights, and a
three-pane wraparound canopy in machined graphite frames.

TIMELINE:
0.0s — Steady cabin hum; panel fully lit.
2.0s — A calm neutral synthetic voice over the radio, in Turkish:
"Ana bara sıfır. İtici—" — the line is CUT OFF mid-word into a wash
of static.
3.0s — The panel dies in sequence, left to right: amber and teal
segments going dark row by row over 3 seconds. No sparks — the lights
simply go out.
6.5s — The static fades to silence. What remains lit: the attitude
sphere's pale backlight, the phosphor dial. The star-field in the
glass drifts almost imperceptibly — a slow 1-degree-per-second roll.
9.0s — Neither figure moves. Two still helmets in a dark cabin over a
blue planet. Hold.

AUDIO: Cabin hum collapsing to near-silence as the panel dies; the
cut-off synthetic line and its static wash; then only two slow
breaths on the suit channel. No music.

PHYSICS: Zero gravity — both bodies held by harnesses, seated
posture, no free-floating limbs. The residual roll is 1 degree per
second: the stars in the glass drift slowly, nothing else moves.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus. The failure is silent and dark — no
sparks, no explosion, no fire, no smoke, no debris; the lights simply
go out. No readable text anywhere — abstract segments, unnumbered
dial. The spoken fragment is heard only — no subtitles, no captions.
The synthetic voice is radio-only — no body, no avatar, no third
figure. No mouth is readable in frame. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 10 (S10) — NABIZ

> 🎯 **REFERANS:** **RD** p2 (ölü panel + amber lamba) · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dark
dead spacecraft cabin in orbit; one small amber lamp has just come
alive. Exactly 2 human figures in frame, seen from behind — this film
has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back,
angled slightly toward the right seat. Right: the engineer — woman,
mid-thirties, 1.69 m, wiry; matte cobalt-blue hard-shell suit, dark
graphite flex-weave joints, machined articulation rings, thin inlaid
AMBER accent lines on the shoulder plates and forearms, finely scuffed
with use; low-profile cobalt-blue helmet CLOSED — leaning into her
harness, her right glove on a small recessed mechanical crank handle
at the side panel, mid-turn. Left: the pilot — man, mid-forties, 1.83
m, broad-shouldered and lean; same matte cobalt-blue hard-shell suit
with thin inlaid TEAL accent lines, finely scuffed with use;
low-profile cobalt-blue helmet CLOSED — both his gloves resting
motionless on his knees. The panel is DEAD: dark segments, lit only by
the pale backlight of the 12-cm mechanical attitude sphere and the
phosphor face of the unnumbered pressure dial. On the panel above the
crank, a small round AMBER REPEATER LAMP is lit at the peak of its
pulse — a warm point in a cold blue-dark cabin. Through the canopy:
black space, hard stars, the sunlit blue curve of the giant low in the
glass. COCKPIT: two high-backed machined seat shells — thin TEAL
piping down the left seat back, AMBER down the right — a machined
console spine between them, canted side consoles, a ribbed overhead
arch carrying six guarded toggles and two recessed teal strip lights,
and a three-pane wraparound canopy in machined graphite frames. The
overhead strips and the floor rim light are dark.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: sphere backlight, phosphor dial, the amber pulse,
faint blue planet-light through the glass.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus — the amber lamp is a small
hard point, not a haze. No readable text, letters or digits anywhere.
No subtitles, no watermark. Hand contacts keep clear structural
boundaries. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One human radio voice speaks; nothing
answers.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens, angled slightly toward the right seat. Right seat: the
engineer — woman, mid-thirties, 1.69 m, wiry; matte cobalt-blue
hard-shell suit with thin inlaid AMBER accent lines on the shoulder
plates and forearms; low-profile cobalt-blue helmet CLOSED, its collar
seal ring visible. Left seat: the pilot — man, mid-forties, 1.83 m,
broad-shouldered and lean; same suit with thin inlaid TEAL accent
lines; low-profile cobalt-blue helmet CLOSED, its collar seal ring
visible. Teal = pilot, amber = engineer — never identical, never
duplicated. The panel is dead and dark; alive only: the attitude
sphere's pale backlight and the phosphor pressure dial. Through the
canopy: stars and the blue curve of the giant, drifting almost
imperceptibly with the craft's slow roll. COCKPIT: two high-backed
machined seat shells — thin TEAL piping down the left seat back, AMBER
down the right — a machined console spine between them, canted side
consoles, a ribbed overhead arch carrying six guarded toggles and two
recessed teal strip lights, and a three-pane wraparound canopy in
machined graphite frames. The overhead strips and the floor rim light
are dark.

TIMELINE:
0.0s — The engineer unlatches a small recessed crank handle at the
side panel with her right glove — a dry mechanical click in the
silence.
2.0s — Three firm turns of the crank, weighted and deliberate; a
faint spring-wound whir.
5.0s — A small round AMBER REPEATER LAMP on the panel lights, holds
half a second, dies — then pulses again: once every 2 seconds, steady.
6.5s — Her voice over the suit radio, quiet and level, in Turkish:
"Verici sağlam. Görünür olmamız yeter."
8.5s — She settles back into her harness. The pilot has not moved;
his gloves stay on his knees. The amber pulse keeps its rhythm. Hold.

AUDIO: Near-silent dead cabin: the crank's dry ratchet, the faint
whir, two slow breaths on the suit channel, her single quiet line —
heard only, never shown as text. A soft click marks each amber pulse.
No music.

PHYSICS: Zero gravity — both bodies harnessed, seated posture, arm
movement deliberate and controlled; no free-floating limbs. The
star-field drifts at 1 degree per second. The amber pulse period is
exactly 2 seconds.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus — the amber lamp is a hard point,
not a haze. No readable text anywhere. The spoken line is heard only —
no subtitles, no captions. No mouth is readable in frame. Hand
contacts keep clear structural boundaries. No sparks, no fire — the
cabin stays dark and calm. The background is identical in every frame
— same planet, same sky, same horizon, same ridges: nothing in it
changes, appears or disappears during the shot. No CGI aesthetic.
Photorealistic with 35mm film grain. Beyond the stated line there is
no other voice, no background chatter, no music, no score. No unnamed
prop: nothing appears in or vanishes from a hand, and no clipboard,
tablet, screen or tool exists that this prompt does not name.
```

---

## 🎬 SAHNE 11 (S11) — CEVAP

> 🎯 **REFERANS:** **RD** p2 · **RE** (arkadan)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Through a
dead spacecraft's windshield: a far light near the limb of a blue
giant. Exactly 2 human figures in frame, seen from behind — this film
has exactly two humans total.

SCENE: Camera behind and between the two headrests, 1.5 meters back.
The wide windshield (1.4 × 0.5 m) dominates the frame. Through it: the
blue giant — a deep sapphire gas giant banded with darker indigo
latitude stripes, a faint violet haze at its pole, its sunlit curve
washing every shadow with a soft blue albedo fill; its sunlit curve
fills the lower half of the glass, against black space and hard stars
above. Near the giant's limb, a single hard white POINT OF LIGHT: the
main ship — still hundreds of kilometres away, reading only as one
bright point, caught at the instant of a signal flash. In the
foreground, from behind: left, the pilot — man, mid-forties, 1.83 m,
broad-shouldered and lean; matte cobalt-blue hard-shell suit with thin
inlaid TEAL accent lines on the shoulder plates and forearms, finely
scuffed with use; low-profile cobalt-blue helmet CLOSED — his helmet
turned toward the engineer. Right: the engineer — woman, mid-thirties,
1.69 m, wiry; same suit with thin inlaid AMBER accent lines, finely
scuffed with use; low-profile cobalt-blue helmet CLOSED — her helmet
turned toward him. Two dark helmets facing each other over a dead
panel, lit by the sphere backlight, the phosphor dial, and the amber
repeater lamp mid-pulse. COCKPIT: two high-backed machined seat shells
— thin TEAL piping down the left seat back, AMBER down the right — a
machined console spine between them, canted side consoles, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy in machined graphite
frames.

CAMERA & LIGHT: 35mm spherical lens, fixed 1.5 meters behind the
seats. Sources: blue planet-light through the glass, sphere
backlight, phosphor dial, amber pulse.

NEGATIVE: Fixed locked-off camera. Exactly 2 human figures, both from
behind — no extra crew, no duplicates, no faces in reflections. The
suits have NO back-mounted unit — both back silhouettes are flat. No
visor is tinted, mirrored, open or missing — no environment reflection
beyond that single specular line, and every face behind glass stays
fully readable. 0% bloom, no soft focus — the far ship is a hard
point, not a haze. No readable text anywhere. No subtitles, no
watermark. No CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera inside the dark cabin, no camera movement.
Exactly 2 human figures in frame, both seen from behind — this film
has exactly two humans total. One synthetic radio voice speaks
through static; no human speaks.

SCENE: Camera behind and between the headrests, 1.5 meters back, 35mm
spherical lens; the 1.4 × 0.5 m central canopy pane dominates the
frame. Through it: the blue giant — a deep sapphire gas giant banded
with darker indigo latitude stripes, a faint violet haze at its pole,
its sunlit curve washing every shadow with a soft blue albedo fill;
its curve fills the lower glass; black space and hard stars above; the
whole view drifting almost imperceptibly with the craft's slow roll.
Left seat: the pilot — man, mid-forties, 1.83 m, broad-shouldered and
lean; matte cobalt-blue hard-shell suit with thin inlaid TEAL accent
lines; low-profile cobalt-blue helmet CLOSED, its collar seal ring
visible. Right seat: the engineer — woman, mid-thirties, 1.69 m, wiry;
same suit with thin inlaid AMBER accent lines; low-profile cobalt-blue
helmet CLOSED, its collar seal ring visible. Teal = pilot, amber =
engineer — never identical, never duplicated. The dead panel below the
glass: sphere backlight, phosphor dial, amber repeater lamp pulsing
once every 2 seconds. COCKPIT: two high-backed machined seat shells —
thin TEAL piping down the left seat back, AMBER down the right — a
machined console spine between them, canted side consoles, a ribbed
overhead arch carrying six guarded toggles and two recessed teal strip
lights, and a three-pane wraparound canopy in machined graphite
frames.

TIMELINE:
0.0s — Still cabin; only the amber pulse and the slow drift of stars.
3.0s — Near the giant's limb, a single hard point of light BLINKS —
twice, half a second apart. Distant, deliberate, unmistakable.
5.0s — The pilot's helmet turns toward the engineer; one second
later hers turns to him. Neither speaks.
7.0s — A calm neutral synthetic voice arrives through a wash of
static, thin but clear, in Turkish: "Sizi görüyoruz. Yörüngeniz
temiz. Hiçbir şey yapmayın."
9.5s — The two helmets hold, facing each other. The amber lamp
pulses. Hold.

AUDIO: Near-silence: two slow breaths on the suit channel, the soft
click of each amber pulse, then the static-washed synthetic line —
heard only, never shown as text. No music.

PHYSICS: Zero gravity — both bodies harnessed, seated posture, head
turns slow and deliberate. Star-field drift 1 degree per second. The
distant blink is a light signal only — no beam, no ray.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Exactly 2 human figures, both from behind — no extra
crew, no duplicates, no faces in reflections. The suits have NO
back-mounted unit — both back silhouettes are flat. No visor is
tinted, mirrored, open or missing — no environment reflection beyond
that single specular line, and every face behind glass stays fully
readable. 0% bloom, no soft focus — the far ship stays a hard point;
no visible beam, no ray, no lens flare. No readable text anywhere. The
spoken line is heard only — no subtitles, no captions. The synthetic
voice is radio-only from the distant ship — no body, no avatar, no
third figure. No mouth is readable in frame. The background is
identical in every frame — same planet, same sky, same horizon, same
ridges: nothing in it changes, appears or disappears during the shot.
No CGI aesthetic. Photorealistic with 35mm film grain. Beyond the
stated line there is no other voice, no background chatter, no music,
no score. No unnamed prop: nothing appears in or vanishes from a hand,
and no clipboard, tablet, screen or tool exists that this prompt does
not name.
```

---

## 🎬 SAHNE 12 (S12) — PART A KAPANIŞ: SÜZÜLÜŞ

> 🎯 **REFERANS:** **RA** p3 ⭐ (ÖLÜ durum + amber nabız)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A dead
spacecraft adrift above a blue giant, one amber light alive. Human
count in this frame: zero — both crew are inside the craft.

SCENE: Wide exterior, camera fixed in space 30 meters from the craft.
Center: the lander — the same 9-meter angular lifting-body craft in
FLIGHT CONFIGURATION, all four landing legs folded away, its belly
line clean, satin steel-blue with one thin SIGNAL-WHITE chevron line
down each flank, every thruster cold and every window dark — DEAD, the
only light on it the 40-cm beacon dome on its left shoulder line
pulsing warm amber once every 2 seconds — caught at the peak of a
pulse. The craft hangs slightly rolled, adrift, its canopy nose at
screen-left, notched tail at screen-right. Below and behind it: the
blue giant — a deep sapphire gas giant banded with darker indigo
latitude stripes, a faint violet haze at its pole, its sunlit curve
washing every shadow with a soft blue albedo fill; its curve fills the
lower two-thirds of the frame; hard white sunlight rims its upper
chines from frame left. Above, black space and hard stars — and far
off near the giant's limb, one tiny steady point of light: the main
ship, still hundreds of kilometres away, the cathedral this moth is
waiting for.

CAMERA & LIGHT: 32mm spherical lens, fixed 30 meters away. Sources:
hard white sunlight from frame left, soft blue albedo fill from the
giant below, the amber beacon pulse.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this
frame: zero — both crew are inside the craft. 0% bloom, no glow
filter, no soft focus — the beacon is a hard warm point, not a haze.
The hull stays satin — never glossy. No engine light, no jets, no
venting — the craft is dead except the beacon. No landing leg, no leg
well, no open gear door visible. No readable text anywhere. No
subtitles, no title card, no watermark. Hull static — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9 widescreen, photorealistic.
Fixed locked-off camera in space, no camera movement. Human count in
this frame: zero — both crew are inside the craft.

SCENE: Wide exterior, camera fixed 30 meters from the craft, 32mm
spherical lens. Center: the lander — the same 9-meter angular
lifting-body craft in FLIGHT CONFIGURATION, all four landing legs
folded away, its belly line clean, satin steel-blue with one thin
SIGNAL-WHITE chevron line down each flank, every thruster cold and
every window dark — DEAD, the only light on it the 40-cm beacon dome
on its left shoulder line pulsing warm amber once every 2 seconds, its
canopy nose at screen-left, notched tail at screen-right. Below: the
blue giant — a deep sapphire gas giant banded with darker indigo
latitude stripes, a faint violet haze at its pole, its sunlit curve
washing every shadow with a soft blue albedo fill; its curve fills the
lower two-thirds of the frame; hard white sunlight rims the upper
chines from frame left. Far off near the giant's limb: one tiny steady
point of light — the main ship, hundreds of kilometres away.

TIMELINE:
0.0s — The dead craft drifts, rolling slowly — about 1 degree per
second, barely perceptible. The beacon pulses at 0.0s.
2.0s — Pulse. The warm amber flash slides across the satin hull and
dies.
4.0s — Pulse. The star-field behind the craft has shifted a few
degrees with the roll; the stars themselves stay sharp fixed points.
6.0s — Pulse. Nothing else moves — no jets, no light, no correction.
8.0s — Pulse. The distant point of light near the giant's limb holds
steady.
10.0s — Pulse, and hold: a moth adrift, one heartbeat of amber, a
cathedral far away.

AUDIO: Hard vacuum silence — no sound exists outside the hull. Total
quiet. No voices, no music.

PHYSICS: Ballistic drift: the craft follows its orbit unpowered,
rolling at a constant 1 degree per second — constant rate, no
wobble, no correction. Beacon period exactly 2 seconds. Stars stay
sharp points — no streaks.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no
pans, no zoom. Human count in this frame: zero — both crew are inside
the craft. 0% bloom, no glow filter, no soft focus — the beacon is a
hard warm point, not a haze. The hull stays satin — never glossy. No
engine light, no jets, no venting, no debris — the craft is dead
except the beacon; the failure is silent. No landing leg, no leg well
and no open gear door is visible in any frame. No readable text
anywhere. No subtitles, no title card, no watermark. Hull static — no
melting, no warping. The background is identical in every frame — same
planet, same sky, same horizon, same ridges: nothing in it changes,
appears or disappears during the shot. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain. No speech, no voice,
no radio chatter, no callout, no music, no score — this scene is
wordless. No unnamed prop: nothing appears in or vanishes from a hand,
and no clipboard, tablet, screen or tool exists that this prompt does
not name.
```

---

# 📋 PART A ÖZET TABLOSU

| # | Sahne | İnsan | Işık ailesi | Perde tabanı | Replik | Lens / mesafe |
|---|---|:---:|---|:---:|:---:|---|
| S0 | HOOK — YARIM GÖK (9s) | 2 (uzak) | Gece yüzeyi | zenit tacı | — | 24mm / 300 m hava |
| S1 | KAROT | 2 | Gece yüzeyi | (kadraj dışı) | — | 35mm / 8 m |
| S2 | UYARI | 2 | Gece yüzeyi | 70° | KERTE | 32mm / 10 m |
| S3 | TOPLAMA | 2 | Gece yüzeyi | 60° | — | 35mm / 6 m |
| S4 | VİRAL #1 — PERDE (nötr çekim) | 2 | Gece yüzeyi | 50° | — | 32mm / araç yanı, kameraya koşu |
| S5 | BİNİŞ (arkadan · uçuş güvertesi) | 2 (arkadan) | Kabin | (kanopide) | — | 35mm / 1.2 m arkadan |
| S6 | ATEŞLEME | 2 (arkadan) | Kabin | 45° (camda) | PİLOT+KERTE | 35mm / 1.5 m |
| S7 | VİRAL #2 — KALKIŞ | 0 | Kalkış | 40° | — | 32mm / 80 m |
| S8 | PERDENİN KENARI | 0 | Yörünge geçiş | kenar geçilir | — | 32mm / 60 m |
| S9 | ÖLÜ ARAÇ | 2 (arkadan) | Karanlık kabin | — | KERTE (kesilir) | 35mm / 1.5 m |
| S10 | NABIZ | 2 (arkadan) | Karanlık kabin | — | MÜHENDİS | 35mm / 1.5 m |
| S11 | CEVAP | 2 (arkadan) | Karanlık kabin | — | KERTE | 35mm / 1.5 m |
| S12 | SÜZÜLÜŞ | 0 | Yörünge | — | — | 32mm / 30 m |

**Doğrulama:** 13 sahne · 26 prompt · insanlı 10 sahne / 20 prompt
(D79 negatif çifti 20/20) · replikli 5 sahne / 6 replik (KERTE 4 —
biri yarıda kesilir · PİLOT 1 · MÜHENDİS 1) · sessiz 8 sahne · perde
tabanı monotonik taç → 70° → 60° → 50° → 45° → 40° → kenar geçişi ·
bacaklar S7 4,5 s'den sonra 0 kare · S9'dan itibaren tüm iticiler ölü,
0 jet karesi · amber nabız S10'dan itibaren 2 s periyot, her sahnede
aynı.

---

## 🚪 KAPI KAYITLARI [D74] — her koşu TEK SATIR

```
Format: TARİH · KAPI (S21/S15/S4/S0) · SONUÇ (GEÇTİ / V2 / DÜŞÜŞ) · not
17.08.2026 · DURUM: ÜRETİM BAŞLAMADI — kapı sırası S21 (PART_B) →
  S15 (PART_B) → S4 → S0; ilk iki kapı PART_B promptlarını bekler.
18.08.2026 · S1 video (kapı dışı deneme, operatör raporu) · V2 —
  figür/iş/araç DOĞRU, ARKA PLAN değişti. Kök sebep prompt tarafında:
  gezegen + kırağı çapaları VIDEO promptunda parafrazdı (IMAGE'da
  tamdı). Denetim tüm dosyaya yayıldı: 22 parafraz + 9 kısa kırağı
  kilidi kanonik bloğa çevrildi, 25 video promptunun negatifine ARKA
  PLAN SABİTLİK cümlesi eklendi, S4 videosu tavan altına indirildi
  (4.365 → 4.281). prompt_kontrol: 0 BLOCK. Yeni deneme V2 promptla.
  ⚠️ Referans paketi henüz üretilmedi — S1 tekrarında RA p1 + RE
  p1·p2 sayfaları yüklenirse arka plan ikinci kanalla da kilitlenir.
18.08.2026 · S1 kapı koşusu (FILME_OZEL rubriği, tek klip) · GÖZLEM SETİ
  — 5 bulgu, 3'ü PROMPT GAP. Uygulanan onarımlar: ① ses yasağı 25 video
  promptunun NEGATIVE'ine taşındı + "radio channel" çekicisi kaldırıldı ·
  ② VİZÖR KİLİDİ (2 cm çerçeve + yaka mührü + tek parlama çizgisi) 10
  gövdeye / 29 negatife işlendi [D95 artık yalnız referans paketinde
  değil] · ③ S1 t=0 durumu yazıldı (kutu yerde, eller boş) + "no unnamed
  prop" negatifi 25 prompta · ④ karota İŞLENMİŞ UÇ KAPAK eklendi, eldiven
  buza değil metale tutunuyor (temas erimesine karşı kural değil TASARIM
  değişikliği) · ⑤ S1'e aurora yasağı (perde henüz inmedi).
  ⚠️ YAPISAL KARAR: S1 · S2 · S4 video promptları tavanı aşıyordu
  (4.3-4.6k). Üçü de I2V'ye alındı — onaylı IMAGE karesi start frame,
  video promptu yalnız hareket + kilit taşıyor (3.657 / 3.830 / 3.811).
  Bu üç sahnede ÖNCE İMAJ üretilir; T2V koşulmaz.
  ⬜ AÇIK: arka planın kare-içi sabitliği hâlâ ölçülmedi.
18.08.2026 · TASARIM GÜNCELLEMESİ (operatör isteği) · KABİN → UÇUŞ
  GÜVERTESİ: yüksek arkalıklı koltuk kabukları + arkalıkta boru çizgisi
  (SOL turkuaz / SAĞ amber) + orta konsol omurgası + eğik yan konsollar
  + nervürlü tavan kemeri (TAM 6 kapaklı toggle, TAM 2 turkuaz şerit) +
  ÜÇ PANELLİ sarma kanopi (orta cam 1.4 × 0.5 m ölçek kilidi DEĞİŞMEDİ)
  + ızgara zemin ve eşik kenar ışığı. Tüm eski kilitler yerinde: analog
  panel, metin 0, duruş küresi, 10 çentikli ibre, pirinç valf, arıza
  sonrası ÜÇ ışık (tavan şeritleri ve zemin ışığı da söner).
  · S5 tamamen ARKADAN kadraja alındı — YÜZ 0 KARE; rol kanalı ikiye
    çıktı (suit çizgisi + koltuk boru çizgisi).
  · Kokpit çapa cümlesi 22 kabin promptuna işlendi; 20 promptta
    "windshield" → "canopy / central canopy pane" terminolojisi.
  · RD referans sayfası yeniden yazıldı: p1 artık ARKADAN GENİŞ ve
    S5'in birebir kadrajı; §4 kapısına yeni sayı kilitleri eklendi.
  · prompt_kontrol: 0 BLOCK (S5 video 4.298, tavan 4.300).
(sonraki koşular buraya eklenecek)
```




