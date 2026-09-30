# 🧷 THE_FALSE_EARTH — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
varlık `UZAYLI_VARLIK` §4 · ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK → merkezî seçim → hook → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Metin çapası
> aynı CÜMLEYİ okutur, aynı NESNEYİ çizdirmez; modelin girdisi GÖRSELDİR.
>
> ⚠️ **BETİK DAVRANIŞI — 06.09.2026'da ÖLÇÜLDÜ, VARSAYIM DEĞİL:**
> `### 📸 IMAGE PROMPT` başlığı `prompt_kontrol.py`'nin BAŞLIK desenine UYAR;
> bu dosya DOSYA modunda normal imaj promptu gibi denetlenir (⑯ ⑮ ⑲ D79 ·
> uzunluk) — istenen budur. `## SAHNE n` başlığı TAŞIMADIĞI için KLASÖR
> modunun DİZİ kapılarına (⑩ kurulum · ⑪ açı · ⑬ tema) GİRMEZ.
> ⛔ **TEK KOŞUL: İngilizce prompt, başlıktan sonraki İLK çitli blok olmalı.**
> Künye bloğu araya girerse betik YANLIŞ bloğu ölçer ve anlamsız BLOCK verir.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
> ⛔ En az bir kutu işaretlenmeden paket yazılmaz; hiçbiri işaretlenmiyorsa
> dosya `⬜ BEKLİYOR` ile durur, SİLİNMEZ (§2.0 boş dosya kuralı).
> ⛔ Eski "iki insandan/araçtan fazlası" sayımı ÖLDÜ — kılavuz §1.
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: MIRA — 192/192
     klipte kask KAPALI, yüz yalnız vizörün ardından okunur [D208]
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: VİZÖR (tek düz
     panel + görünür koyu çerçeve) · LAMBANIN CAMI (novumun tek kanıtı)
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: ÇEKİRDEK
     HALKASI (12 m) + sarı mandal + ayırma kolu — üçü aynı gövdede, oranları bağlı
☑ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: SİYAH MADDE
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: —
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: 24.09.2026
     bölüm 4-5-6 taraması — LAMBANIN CAMI üç ayrı biçimde yazılmıştı
     ("teardrop of cloudiness" · "white mark" · "white oval mark"); novumun TEK
     KANITI olan nesnede bu bir ② DEVAMLILIK kırılmasıdır → R5 sayfası açıldı
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_FALSE_EARTH          FORMAT: yatay 32 dk (§2.9)   ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 3840×2160    SAHNE SAYISI: 50 (192 klip)
SAYFA: 5   TOPLAM PANEL: 18   ARİTMETİK: 4 + 3 + 4 + 4 + 3 = 18
   ⚠️ PLAN §ÜRETİM SIRASI DÖRT sayfa sayıyor (RK1 · RK3 · RC · RD). BEŞİNCİ sayfa
   (R5 · LAMBA) T6'nın ölçülmüş bulgusuyla açıldı ve gerekçesi §0'da yazılı.
   ⛔ SAHİP ONAYI GEREKİR [D74 kalıbı]: beşinci sayfa PLAN'a eklenecek mi?
   ⛔ Bu toplam §2 tablosunun panel toplamına EŞİT olmalı (§7 ①)
İMAJ MODELİ + SÜRÜM: ⬜ (üretim başlamadı)         TARİH: ⬜.⬜.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_FALSE_EARTH_KAPAK.md` (RK onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK S44 (K169-K174) → merkezî seçim S42 (K161-K164)
> → kapanış S50 (K190-K192) → bedel S47 (K181-K183) → açılış S01-S02 (K001-K004)
> → kusurlar S06 · S09 · S19 → kalan 40 sahne bölüm sırasıyla [PLAN §ÜRETİM SIRASI]

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | RK1 | 4 | MIRA — giysi · kask · vizör · sırt | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R2 | RD | 4 | SİYAH MADDE — gövde · uç · dal · kesit | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R3 | RN | 3 | LAMBA + FOTOĞRAF — çatlak ve oval iz | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R4 | RC | 4 | ÇEKİRDEK — halka · sarı mandal · ayırma kolu | 🟠 S42'den önce | | | ⬜ TASLAK |
| R5 | RK3 | 3 | LENA — odadaki kadın (kasksız) | 🟠 S03'ten önce | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp
   karşılaştırılır (yanlış dosyayla üretim yapılmasın).
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| M | mürettebat (kasklı, tek kişi) | insan | S01 | S50 | R1 | 🔴 kask+vizör — ayırt etme kanalı kapalı |
| L | odadaki kadın (kasksız, kayıtta) | insan | S03 | S48 | R5 | 🔴 iki yüz aynı filmde [D167] |
| B | siyah madde | canlı | S07 | S46 | R2 | 🔴 "canlı" sınıfı depoda hiç 5'i geçmedi |
| N | lamba + aile fotoğrafı | prop | S03 | S19 | R3 | 🟠 novumun TEK kanıtı · iz 20 mm |
| C | çekirdek halkası (amber) | prop | S04 | S47 | R4 | 🟠 12 m oran · sözle tutmuyor |
| Cy | sarı mandal | prop | S04 | S43 | R4 | 🟠 kadrajın tek renkli nesnesi |
| Cl | ayırma kolu (çelik, 1 m) | prop | S43 | S44 | R4 | 🟠 doruğun mekaniği |
| P | pod (4 m) | araç | S33 | S35 | — | 🟢 ölçek şahidi · silüet, metne devredildi |
| H | ana gemi gövde plakası | mekân | S04 | S50 | — | 🟢 ölçek şahidi · metne devredildi |
| S | kabuk (matt siyah, iç yüz) | mekân | S32 | S46 | R2 p1 | 🟠 maket okuması riski |
| W | sıcak pencere (yer imi) | olay | S01 | S50 | — | 🟢 tek nokta kaynak · metne devredildi |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Kod kanonu: kılavuz §2.
⛔ Risk sınıfı `ASTRONOT_DONANIM` eşya tablosundan alınır (burada tarif edilmez).
⛔ Envanterde olup sayfası olmayan varlık = çapasız varlık; sahnede yeniden
   tasarlanır. Sayfası olup hiçbir sahnede çağrılmayan = YETİM (§7 ②).
BELGEDE KALAN ↔ YALNIZ GÖRSELDE KİLİTLENEN ayrımı kılavuz §2 tablosundadır;
buraya yalnız SONUCU yazılır.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| M | K0 (temel) | temiz giysi | S01 | — | R1 p1 |
| M | K1 | sağ diz + sağ önkolda tek kir bölgesi (K024'ten) | S08 | S08 | R1 p1 (kir katmanı) |
| B | K0 (temel) | mat siyah, KATI, kuru, diri | S07 | — | R2 p1 |
| B | K1 | kesilmiş — kesit yüzeyi düz ve kuru | S44 | S44 | R2 p4 |
| B | K2 | ölü — yüzey gri-tebeşirli, boyuna yarıklar | S45 | S45 | R2 p3 |
| C | K0 (temel) | amber ışık gövdenin içinde dönüyor | S04 | — | R4 p1 |
| C | K1 | içinde siyah damar ilerliyor | S40 | S40 | R4 p2 |
| C | K2 | üç parça, kopuk uçlar çıplak metal, IŞIK YOK | S44 | S44 | R4 p3 |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönülüyorsa gerekçe satırı: GERİ DÖNÜŞ YOK. Kir
   birikir, hiç temizlenmez; siyah madde K0→K1→K2 tek yönlü; amber ışık K2'de
   söner ve hiçbir klipte geri gelmez.  [D147 · D84]
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en).
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişkidir. Bu dosyada
   hangisi seçildi ve NEDEN: AYRI PANEL. R2'de siyah maddenin üç durumu üç ayrı
   panele (p1 diri · p3 ölü · p4 kesit) yazıldı, çünkü fark RENK değil YÜZEY
   DOKUSUDUR ve tek panelde yan yana konursa model ikisini harmanlıyor. R4'te
   halkanın üç durumu için aynı karar geçerlidir.
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01-S02 | dış · vakum · konum lambası 3000 K | R1 p2 · R1 p4 | M | K0 | vizördeki yansıma · kara kürenin kadraj yeri |
| S03 | iç · oda · lamba 2700 K | R5 p1 · R3 p1 | L · N | K0 | kaydın bozulma bantları · konuşma |
| S04-S06 | iç · yuva · amber 2200 K | R4 p1 · R1 p1 | C · M | K0 | amberin gövde içinde dönme yönü |
| S07-S13 | dış · yüzey 0,98 g | R2 p1 · R1 p1 | B · M | K0 | kaburgaların şehir başına 12 sayısı |
| S19 | iç · oda · lamba 2700 K | R3 p1 · R3 p2 · R3 p3 | N | K0 | fotoğrafın elde tutuluş açısı |
| S32-S34 | dış · vakum | R2 p1 · R1 p2 | B · M | K0 | ölçek şahidi pod silüeti (4 m) |
| S36-S37 | iç · koridor 4500 K | R2 p2 · R1 p1 | B · M | K1 | dalların duvar köşelerini izlemesi |
| S39-S43 | iç · yuva · amber 2200 K | R4 p1 · R4 p2 · R1 p4 | C · M | K0→K1 | kelepçenin diş sayısı · ter |
| S44 | iç · bölme · konum lambası 3000 K | R4 p3 · R2 p4 · R1 p1 | C · B · M | K2 · K1 | üç parçanın ayrılma hızı |
| S45 | iç · koridor 4500 K | R2 p3 | B | K2 | kül gibi dağılmanın tanecik boyu |
| S46 | dış · vakum | R2 p1 · R2 p1 (kabuk kırpımı) | B · S | K0 | dokuz karanlık halkanın aralığı |
| S48 | iç · kokpit 4500/2200 K | R5 p1 (ekran kırpımı) | L | K0 | onarım bantlarının yüksekliği |
| S50 | dış · vakum | R1 p3 | M | K1 | kürelerin dört ayrı derinliği |
```
⛔ "METNE DEVREDİLEN" BOŞ BIRAKILAMAZ — referansın taşıyamadığı her şey
   (anlık eylem, geçici yansıma, hareket) buraya yazılır [kılavuz §5.1].
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2). Dördüncü varlık
   kadraj dışına alınır ya da metne devredilir — PLAN kararıdır.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   ⚠️ Dört eski paket TERSİNİ yazıyor ve iddia ÖLÇÜLMEDİ; bu dosyanın
   seçtiği yükleme biçimi: KIRPIM · gerekçe: sahne başına en çok 3 kayıt
   yüklenebiliyor (`VEO` §6 md.2); tam sayfa yüklenirse tek varlık için dört
   panelin dördü birden girer ve kota bir varlıkta tükenir. ⬜ İLK FİLM ÖLÇER:
   P1 denemesinde (S01-S02) kırpım ile tam sayfa YAN YANA denenir ve sonucu
   üretim defterine yazılır.
· Flow çağırma: `@R⬜` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun kopyasıdır; ayrışırsa
  tablo düzeltilir. Sayfası ⏳ olan sahne "ÜRETİLMEZ" damgası taşır.
```

## 6. 📸 REFERANS SAYFALARI
> Blok her sayfa için olduğu gibi tekrarlanır. R1 biçim örneğidir; kopyalarken
> içindeki metin SİLİNİR, iskelet kalır.
> ⛔ **İngilizce prompt BAŞLIKTAN SONRAKİ İLK çitli bloktur** (yukarıdaki
> ölçüm notu). Künye ve kabul sınavı promptun ALTINA yazılır.

### 📸 IMAGE PROMPT — SAYFA R1 · RK1 · MIRA — GİYSİ · KASK · VİZÖR · SIRT
```
IN FRAME: full body, face, hands, back
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey
seamless backdrop, even neutral key light with soft fill.

Exactly one human character — no clones, no second person. A woman standing
straight and facing the lens, sealed in a matt charcoal grey one-piece
pressure suit, dry and unreflective, the seams and stitching clearly visible.
One pale grey band is wrapped all the way around the LEFT shoulder. The visor
is optically clear glass with zero tint, zero mirror coating and zero
reflection, one single FLAT panel held in a visible dark frame, and the face
is fully readable through it AT EVERY HEAD ANGLE. The back of the suit is one
continuous smooth panel from collar to hip, unbroken, carrying nothing — one
smooth sculpted dorsal shell with a single flat vertical seam down its centre
and a shallow lumbar hollow above the hip. Her back silhouette is flat,
carrying nothing. Fixed wear that never moves: a dry
grey dust smear on the right forearm · a dry grey dust smear on the right knee.

NEGATIVE: no backpack, no tank, no hose, no
rear housing, no antenna, no light unit and no rear pack of any kind on the
back · no seamless helmet, no dome, no bubble, no mirrored or tinted visor,
no visorless helmet · no readable text, letters, digits or symbols on the
suit, the visor or the backdrop · no panel gutters, no labels, no captions,
no arrows, no callouts, no dimension lines, no panel titles · no bare skin
above the collar, at the wrist or at the ankle · no bloom, no glow, no soft
focus · no second figure anywhere in the frame.

Output: 16:9, 3840×2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş (kir bölgeleri okunur)
               p2 · profil — siluet hattı (sırtın düzlüğü profilde ölçülür)
               p3 · SIRT — düz siluet, POZİTİF yüzey [D79/D139]
               p4 · vizör ardı yüz CU [D146] — çerçeve ve düz panel görünür
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — model boş sırtı DOLDURMAK zorundadır;
   panelin işi ona ne KOYACAĞINI söylemektir: yasak değil MALZEME [D123 · D139].
   Bu sayfada verilen malzeme: TEK DÜŞEY DİKİŞ + BEL ÇUKURU + omuz kürek hattı.
⚠️ p4 aynı zamanda K163 · K164 · K057 · K059'un LIP-SYNC probunun girdisidir:
   ağzın okunduğu dört klip bu panelden doğar [KART 7 · D215].
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      sırt panelinde çıkıntı sayısı = 0 VE yüzey tarifi okunuyor (dikiş +
              bel çukuru sayılabiliyor) VE p4'te vizör çerçevesi görünüyor
  RET:        sırtta tek bir kutu/tüp/anten · vizörde tek bir yansıma · kubbe
              biçimi · vizörsüz kask · giysi üzerinde tek bir harf
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "sırtında bir şey
              taşıyor mu?" · doğru cevap: "hayır, sırt düz"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S01 ÜRETİLMEZ — KAPI 0)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 3
     (① kapalı vizör ② sol omuz bandı ③ kir bölgesi) — boy · ten · saç · yaş
     PLAN'da kalır, prompta GİRMEZ [D167].
```

### 📸 IMAGE PROMPT — SAYFA R2 · RD · SİYAH MADDE
```
IN FRAME: none
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill, one flat grey plate beneath.

Exactly 0 human characters. A single matt black form lying on the plate, one
metre long in the frame: a solid, dry, rigid form with a rounded blind end,
its cross-section round and even along its length. Its surface is completely
matt and gives back no highlight anywhere — no sheen, no wet look, no
translucency. The surface texture is fine and even, like fired unglazed
ceramic, with no scales, no pores, no ribs and no segments. It carries
exactly two branches and no more, both leaving the main form at a shallow
angle and both ending in the same rounded blind end. Where it touches the
plate the metal is drawn up into a shallow collar, unbroken and unburnt.

NEGATIVE: no liquid, no drip, no ooze, no
slime, no wet surface, no smoke, no vapour, no spark and no glow anywhere ·
no limbs, no face and no eyes on it · no scales, no fur and no
membrane · no rope look and no tentacle look · no third branch and no second form in the frame ·
no burn, no scorch and no crack in the plate · no readable text, letters,
digits or symbols anywhere · no labels, no captions, no arrows, no callouts,
no dimension lines · no bloom, no glow, no soft focus.

Output: 16:9, 3840×2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · DİRİ gövde + iki dal (K0) — yüzey dokusu ölçülür
               p2 · UÇ yakın plan — kör uç ve 80 cm'lik en
               p3 · ÖLÜ yüzey (K2) — gri-tebeşirli lekeler + boyuna yarıklar
               p4 · KESİT (K1) — düz, kuru kesit yüzeyi; dikiş/çekirdek/iplik YOK
⛔ D192 SAYISAL KART bu sayfanın sözleşmesidir ve her madde klibine iner:
   ≤3 dal · ≤3 uç · bir el genişliği / 10 s · 0 damla · 0 duman · 0 parlama ·
   yüzey KATI ve MAT. ⛔ Panelde bu sayıların hiçbiri YAZIYLA gösterilmez.
⚠️ Filmin 1 NUMARALI riski. "Canlı" kategorisi bu depoda hiç 5'i geçmedi
   (KART 2) ve OPEN CIRCUIT'te risk yalnız SIFATLA korunmuştu → ekrana dallanan
   bir şimşek geldi [A5 · D192].
```
```
KABUL SINAVI (R2) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de dal sayısı = 2 VE yüzeyde 0 parlama noktası VE p4'ün kesit
              yüzeyinde iç yapı (çekirdek · iplik · boşluk) sayısı = 0
  RET:        tek bir ıslak parlama · tek bir damla · üçüncü dal · pul/tüy/damar
              dokusu · halat ya da yılan okuması · kesitte iç organ görüntüsü
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "bu ıslak mı, kuru mu?"
              · doğru cevap: "kuru"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S07 ÜRETİLMEZ — KAPI 0)
  ⑲ KİMLİK YIĞINI: insan yok · uygulanmaz
```

### 📸 IMAGE PROMPT — SAYFA R3 · RN · LAMBA + FOTOĞRAF (NOVUM TAŞIYICISI)
```
IN FRAME: none
Photorealistic close still, 35mm film grain, plain neutral mid-grey seamless
backdrop, one warm 2700 K lamp as the only source, soft fill.

Exactly 0 human characters. A table lamp with a brass base and a clear glass
body, standing upright and lit from within. Up one side of the glass runs a
hairline crack, old and clean-edged, running with the glass and not across it.
Set into the material of that same glass is one white oval mark twenty
millimetres across, soft-edged on one side and sharp on the other. The mark is
IN the glass, not on it: it has no rim, no residue and no thickness.

Leaning against the lamp's base is a printed photograph, matt and slightly
curled at one corner. The photograph shows the same lamp in a small room, and
the lamp in it carries the same hairline crack up the same side. Over its
glass in the photograph lies one white oval flare sixteen millimetres across,
with the same soft edge on the same side as the mark in the real glass.

NEGATIVE: no readable text, letters, digits
or symbols on the lamp, the photograph, the backdrop or anywhere in frame ·
no second crack, no third mark and no second photograph · no lens flare, no
starburst, no bloom, no glow and no halo around the lamp · no reflection of
the photograph in the glass · no fingerprint, no dust and no smear on the
glass · no labels, no captions, no arrows, no callouts, no dimension lines ·
no soft focus — both the mark and the flare stay sharp at their sharp edge.

Output: 16:9, 3840×2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · lamba CU — çatlak (582 px) + oval iz (194 px) birlikte
               p2 · fotoğraf CU — aynı çatlak + oval parlama (155 px)
               p3 · İKİSİ AYNI KARADE (K070'in kadrajı) — dört unsur birden
⛔ İPTAL KAPISI ÖLÇÜTÜ [03_SAHNE_SIRALAMASI §8 · PLAN §NOVUM]:
   lambanın camındaki leke 20 mm → 194 px · fotoğraftaki parlama 16 mm → 155 px
   İKİSİ DE AYNI KAREDE ve ≥100 px. ÜÇ DENEMEDE OKUNMUYORSA FİLM ÜRETİLMEZ.
⭐ Önerme tam burada kuruluyor: yapı, nesnenin kusurunu (çatlak) ve NESNENİN
   RESMİNİN kusurunu (flaş parlaması) aynı özenle kopyalamış; ikisini ayırt
   edemiyor. Bu yüzden iz CAM KUSURU DEĞİL, FOTOĞRAF KUSURUDUR.
⚠️ GÖRÜNÜRLÜK MESAFEYE BAĞLI [D179]: CU 50mm @ 0,55 m → tam kanonik tarif ·
   MS 35mm @ 2,6 m → çatlak + "one small white mark" (izin ŞEKLİ yazılmaz) ·
   WS 24mm @ 4,0 m → yalnız lamba, iz YAZILMAZ. 29 px'te okunmaması TASARIMDIR.
```
```
KABUL SINAVI (R3) — dört alan ZORUNLU [D144]:
  KABUL:      p3'te dört unsur birden sayılabiliyor (gerçek çatlak · gerçek oval
              iz · fotoğraftaki çatlak · fotoğraftaki parlama) VE iki ovalin
              KESKİN kenarı AYNI tarafta
  RET:        izin cam ÜSTÜNDE bir leke gibi durması (kabartı · kalınlık · halka)
              · lambada ikinci çatlak · fotoğrafta çatlağın olmaması
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "fotoğraftaki lamba ile
              masadaki lamba aynı lamba mı, nereden anladın?" · doğru cevap:
              "aynı — çatlak aynı yerde"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S19 ÜRETİLMEZ — KAPI 0)
  ⑲ KİMLİK YIĞINI: insan yok · uygulanmaz
```

### 📸 IMAGE PROMPT — SAYFA R4 · RC · ÇEKİRDEK — HALKA · MANDAL · KOL
```
IN FRAME: none
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill.

Exactly 0 human characters. A section of a pale metal ring lying across the
frame at hip height, its body turned and even, machined and unpainted, warm
with an amber light held inside itself and showing through one narrow window
in its body. The amber is even and steady, and it does not spill onto the
backdrop.

Standing out of the ring's body, a hand's span apart: one yellow catch, a
span across, hinged at its lower edge and shown CLOSED, the only coloured
object in the frame; and one plain steel lever a metre long, standing upright
out of a slot in the ring and shown DOWN IN ITS SEAT. The lever's grip is
knurled along its upper third and its lower end is plain.

For scale, a sealed grey glove rests open on the ring's body at the frame's
lower edge.

NEGATIVE: no readable text, letters, digits
or symbols on the ring, the catch, the lever or anywhere in frame · no second
catch, no second lever and no other coloured object · no bloom, no glow, no
halo and no bleed from the amber · no rust, no scorch, no weld bead and no
bolt head · no labels, no captions, no arrows, no callouts, no dimension
lines, no panel titles · no human character, no face and no second glove ·
no soft focus, no depth-of-field blur, no tilt-shift and no miniature look.

Output: 16:9, 3840×2160, no text, no watermark.
```
```
ÖNCELİK: 🟠 S42'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · halka K0 — amber içeride, pencere ve gövde oranı
               p2 · halka K1 — pencereden görünen tek siyah damar (9 cm)
               p3 · halka K2 — ÜÇ parça, kopuk uçlar çıplak metal, IŞIK YOK
               p4 · mandal AÇIK + kol YUVADA — S43'ün iki durumu
⛔ ORAN KİLİDİ: halkanın kendisi 12 m'dir ve panel bir KESİTİDİR. Ölçek
   şahidi kadrajdaki ELDİVENDİR; panelde metre yazmaz, eldiven söyler [⑪].
⚠️ Sarı mandal kadrajın TEK renkli nesnesidir ve K164'te kararın taşıyıcısıdır.
   Rengi panelden gelir; promptta "yellow" dışında sıfat kullanılmaz.
```
```
KABUL SINAVI (R4) — dört alan ZORUNLU [D144]:
  KABUL:      p3'te parça sayısı = 3 VE hiçbirinde amber yok VE p1'de amber
              backdrop'a taşmıyor (backdrop üzerinde amber piksel = 0)
  RET:        dördüncü parça · p3'te tek bir amber nokta · mandalın ikinci bir
              kopyası · halkada okunur bir işaret ya da numara
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "hangi parça elle
              çekilen şey?" · doğru cevap: "çelik kol"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S42-S44 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok (eldiven ölçek şahidi) · uygulanmaz
```

### 📸 IMAGE PROMPT — SAYFA R5 · RK3 · LENA — ODADAKİ KADIN
```
IN FRAME: full body, face
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey
seamless backdrop, one warm 2700 K lamp as the only source, soft fill.

Exactly one human character — no clones, no second person. A woman standing
straight and facing the lens in soft indoor clothes: a pale long-sleeved top
and dark trousers, the fabric stiff and still, hanging without movement. She
wears no helmet, no pressure suit and no gloves, and her hands are bare and
open at her sides. Her hair is dark and cut close. She is lit only by the
warm lamp, from screen-left, and the light falls off to nothing on her screen-right.
Her face is fully readable, level and unguarded.

NEGATIVE: no helmet, no visor, no pressure
suit, no gloves, no breathing gear and no equipment of any kind on her ·
no readable text, letters, digits or symbols on the clothes or the backdrop ·
no second figure, no clone and no reflection of her anywhere · no bloom,
no glow, no halo and no lens flare from the lamp · no airbrushing, no waxy
skin, no face morphing, no beauty retouching — real skin pores · no labels,
no captions, no arrows, no callouts, no dimension lines · no soft focus ·
no wind, no drift and no movement in the fabric or the hair.

Output: 16:9, 3840×2160, no text, no watermark.
```
```
ÖNCELİK: 🟠 S03'ten önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — kasksızlık ve giysi (M'den ayıran birinci eksen)
               p2 · yüz CU — kayıtta okunan yüz
               p3 · yüz CU + ONARIM BANTLARI — K185'in ekran hâli, alt üçte bir
                    düz yatay bantlara dağılmış, AĞIZ ÇÖZÜNMÜYOR
⛔ LENA'NIN KLİBİNDE ÇIPLAK DERİ NEGATİFİ YAZILMAZ [D175 · D208 ayrımı]. O
   kasksız ve giysisizdir; cümle yazılırsa kapı onu ihlal sanar. SPEC C'de yazılı.
⛔ KİMLİK ÖZNİTELİĞİ TAVANI: üç — ① kasksız ve giysisiz ② açık renkli uzun kollu
   üst ③ hiç yaşlanmamış olması. ⭐ Üçüncüsü YAZILMAZ, KADRAJ söyler (fotoğrafla
   yan yana). ⛔ Yaş · boy · ten rengi promptta GEÇMEZ [D167].
⚠️ p3 bu paketin en pahalı panelidir: K185'in lip-sync riskini kadrajın İÇİNDE
   kapatır. Bantlar bir FİLTRE değil, onarılmış kaydın malzemesidir [D215].
⚠️ İKİ YÜZ AYNI FİLMDE [KART 12 · politika riski yüksek×yüksek]: M ve L asla
   aynı kadrajda değildir; L yalnız KAYIT içinde görünür (K006 · K114 · K185 · K186).
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_FALSE_EARTH_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
□ ① PANEL ARİTMETİĞİ  §1 künye toplamı = §2 tablo toplamı
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var mı · çağrılmayan sayfa
                      (YETİM) 0 mı · yoksa gerekçesi yazılı mı
□ ③ 120 PX TESTİ      panel 120 px'e inince şu öğeler hâlâ ayırt ediliyor:
                      R1 → sırtın DÜZLÜĞÜ · sol omuz bandı
                      R2 → yüzeyin MAT olması (parlama yokluğu) · dal sayısı 2
                      R3 → camdaki çatlağın YERİ (fotoğraftakiyle aynı taraf)
                      R4 → sarı mandalın rengi · kolun DİKEY duruşu
                      R5 → kasksız olması (M ile karışmaması)
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                      + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146]
□ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0 AMA yüzey POZİTİF tarifli
□ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — ayrım yalnız renge
                      dayanıyorsa panel reddedilir (önce fiilen sınanır)
□ ⑧ DURUM ÇİFTİ       §4'teki her çift aynı kadraj · aynı ışık yönü · ±%3
□ ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik ≤3 (betik: FIX)
□ ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin SONRASINI yazmıyor [D179]
□ ⑪ ÖLÇEK ŞAHİDİ      yapı panelinde 1H (kasklı gövde) kadrajda mı
□ ⑫ SEED / SHA KAYDI  hangi panel hangi seed ve özet — §2 tablosuna YAZILDI
□ ⑬ BAYT AYNILIĞI ⚙️  paketteki kimlik bloğu ile sahne promptu `diff` temiz mi
□ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ✅ GO — 24.09.2026
      (⑯ ⑮ ⑲ D79 · IN FRAME · politika sözlüğü · nesne-göreli taraf)
      Koşuda çıkan ve düzeltilenler: Output satırı Türkçeydi ("oran ·
      çözünürlük") → İngilizce · beş promptta `IN FRAME:` satırı yoktu →
      eklendi · R1'de D79 arka cümlesi kalıba uymuyordu → "Her back
      silhouette is flat, carrying nothing." · R2'de politika sözlüğü
      yığılmıştı (body×4 · teeth · tentacle · fur · feathers · membrane) →
      `form` ve kısaltma · R5'te "on her right" nesne-göreliydi → `screen-right`
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. 📋 DURUM — 24.09.2026

```
✅ Tetikleyici kontrolü işaretlendi (T1 · T2 · T3 · T4 · T6 — beşi)
✅ Envanter (11 varlık) · durum merdiveni (8 satır) · sahne eşlemesi (13 blok) yazıldı
✅ Beş sayfa bloğu yazıldı: R1 RK1 · R2 RD · R3 RN · R4 RC · R5 RK3 — 18 panel
✅ Beş kabul sınavı yazıldı (KABUL · RET · YABANCI GÖZ · SONUÇ · ⑲ dördü + biri)
✅ prompt_kontrol.py bu dosyada koşuldu → GO

⬜ ÜRETİM HENÜZ BAŞLAMADI. Bu yüzden şunlar boş ve boş kalmaları DOĞRUDUR:
   ⬜ SEED sütunu — Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]
   ⬜ SHA-256 sütunu — panel dosyası üretilince hesaplanır
   ⬜ DURUM sütunu — beşi de TASLAK; ONAYLI olmayan sayfanın sahnesi ÜRETİLMEZ
   ⬜ Beş KABUL SINAVI'nın SONUÇ satırı
   ⬜ İMAJ MODELİ + SÜRÜM · TARİH
   ⬜ §7 kabul kapısının 14 maddesi (⑭ dışında) — panel olmadan işaretlenemez
   ⬜ ⑦b GRİ TON ve ⑬ BAYT AYNILIĞI komutları fiilen koşulmadı

⛔ SAHİP KARARI BEKLİYOR: beşinci sayfa (R3 · RN · LAMBA) PLAN'ın dört sayfalık
   üretim sırasına eklenecek mi? Gerekçesi §0 T6'da yazılı ve ölçülmüş bir
   bulguya dayanıyor (24.09.2026 bölüm 4-5-6 taraması). Eklenirse PLAN
   §ÜRETİM SIRASI 0. maddesi "dördü" yerine "beşi" der.
```
