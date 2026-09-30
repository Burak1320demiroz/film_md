# 🧷 GUNES_MEZARI — REFERANS PAKETİ

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

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: tek figür, 18 klipte (6 klip insansız)
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: vizör panesi + kask kabuğu
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: gemi · kaide · şehir silueti
☐ T4 İNSAN DIŞI CANLI                                           hangi: — (filiz 1 klipte, hareketsiz; ayrı RV kaydı AÇILMADI, RD p3'e gömüldü)
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: buhar yakası + kırağı pası
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                           rapor: küre 5 klipte İKİ HÂLDE · çekirdek 5 klipte
```

⭐ Sahip 4. soruda **YAZILSIN** dedi; bu blok yine de ölçülür çünkü tetikleyici
listesi hangi VARLIKLARIN sayfa alacağını da belirler. Altı tetikleyiciden beşi
doğru, T4 tek başına sayfa açmayacak kadar küçük (1 klip · hareket 0).

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: GUNES_MEZARI          FORMAT: yatay 4 dk        ORAN: 16:9
SAYFA ORANI = FİLM ORANI · ÇÖZÜNÜRLÜK: 3840×2160     KLİP: 24 (7 sahne)
SAYFA: 6   TOPLAM PANEL: 25   ARİTMETİK: 6+4+5+4+3+3 = 25
İMAJ MODELİ + SÜRÜM: ⬜ (üretim gününde yazılır)      TARİH: ⬜.⬜.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `GUNES_MEZARI_KAPAK.md` (RK1 onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK K21 → BEDEL K17 → FİNAL K24 → HOOK K01 → kalanı.

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| RK1 | zırh ve kask | 6 | tek figürün kimliği — siluet · sırt · vizör ardı yüz | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| RO | küre — iki hâl + buhar yakası | 4 | filmin 1 numaralı riski [A5] | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| RA | gemi | 5 | üç halka · kapı boyunda pencere · oran | 🔴 ZORUNLU (K02 · K21) | ⬜ | ⬜ | ⬜ TASLAK |
| RB | salıverme kaidesi | 4 | üç taş kemer · yuva · dört kilit yuvası | 🟠 K13'ten önce | ⬜ | ⬜ | ⬜ TASLAK |
| RP | çekirdek + anahtar çubuğu | 3 | iki el aleti, oran ve arayüz | 🟠 K15'ten önce | ⬜ | ⬜ | ⬜ TASLAK |
| RD | şehir ve oyuk | 3 | dünya çapası · sıcak kaya oyuğu + filiz | 🟠 K04'ten önce | ⬜ | ⬜ | ⬜ TASLAK |

```
🔴 üretim başlamadan · 🟠 belirli klipten önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın klipleri ÜRETİLMEZ. ⏳ sayfa YOK — altısı da ilk
   çağrıldığı klipten ÖNCE onaylanır.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu sütun
   "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp
   karşılaştırılır, yanlış dosyayla üretim yapılmasın.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk klip | son klip | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| RK1 | tek figür — zırh · kask · pelerin · hilal yanıklı sol eldiven | insan | K03 | K23 | RK1 | 🔴 YÜKSEK — vizör biçimi metinle tutmuyor [D146] · sırt ünitesi [D79/D139] |
| RO-a | küre · TAŞIMA hâli (kısık, halkaların odağında) | olay/nesne | K01 | K21 | RO p1-p2 | 🔴 YÜKSEK — filmin 1 numaralı riski; ateş topu / korona okuması |
| RO-b | küre · ÇALIŞMA hâli (kaidenin alanında, yüksekte) | olay/nesne | K22 | K24 | RO p3 | 🟠 ORTA — gökte disk, hüzme riski |
| RO-c | buhar yakası (sıcak gövde temasında dik beyaz yaka) | olay | K07 | K19 | RO p4 | 🟡 ORTA-DÜŞÜK — yükseklik ve ritim yazılı |
| RA | gemi — uzun kaburgalı gövde, üç halka, tek aydınlık pencere | araç | K02 | K23 | RA | 🟠 ORTA — oran ve halka sayısı klipler arası kayar [D32] |
| RB | salıverme kaidesi — üç taş kemer, yuva, dört kilit yuvası | mekân | K04 | K21 | RB | 🟠 ORTA — yuvanın iç geometrisi |
| RP-a | güç çekirdeği — kaburgalı çelik silindir, iki mühür halkası | prop | K15 | K21 | RP p1-p2 | 🟠 ORTA — elde alet buharlaşıyor [D152] |
| RP-b | anahtar çubuğu — ön kol boyunda düz çelik çubuk | prop | K15 | K20 | RP p3 | 🟠 ORTA — çubuk diske dönüşüyor [D138 çatışması] |
| RD-a | şehir — siyah bazalt, kaburga ritmi kuleler, oturan heykeller | mekân | K02 | K24 | RD p1-p2 | 🟠 ORTA — dünya çapası kayması [D209] |
| RD-b | kaya oyuğu + üç yapraklı filiz | mekân/canlı | K07 | K24 | RD p3 | 🟡 ORTA-DÜŞÜK — canlı anatomisi, 1 klipte |

```
⛔ KOD kullanılır, AD kullanılmaz [D34].
⛔ Envanter 10 satır / sayfa 6 — her satırın bir PANELİ var, ÇAPASIZ varlık 0.
⛔ YETİM (sayfası olup hiçbir klipte çağrılmayan) sayfa 0.
BELGEDE KALAN: sayılabilir ve yer belirten bilgi — halka SAYISI, kilit yuvası
SAYISI, mühür halkası SAYISI, yanık izinin ELİ ve YERİ, filiz sayısı.
YALNIZ GÖRSELDE: doku, kapitone sıklığı, kir dağılımı, metalin iplik yönü,
bazaltın tane boyu.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum | ne değişti | başlangıç klibi | dönüşüm klibi | panel |
|---|---|---|---|---|---|
| RK1 | K0 (temel) | kırağı pası YOK | K03 | — | RK1 p1-p4 |
| RK1 | K1 | pelerin kenarı + omuz kapaklarında soluk kırağı pası | K04 | K04 | RK1 p5 |
| RK1 | K2 | aynı pas, daha yoğun — gemi içinde de ÇÖZÜLMEZ | K15 | K15 | RK1 p6 |
| RO | a (taşıma) | kısık · koyu kızıl-altın · halkaların iç açıklığının 4/5'i | K01 | — | RO p1-p2 |
| RO | b (çalışma) | açılmış · yüksekte · gökte tırnak genişliğinde disk | K22 | K21 | RO p3 |
| RA | K0 | altı pencere yanık | K02 | — | RA p1-p4 |
| RA | K1 | bir pencere yanık, sonra hiçbiri | K18 | K18 | RA p5 |
| RB | K0 | yuva ölü ve karanlık | K13 | — | RB p3 |
| RB | K1 | yuva ışık almış | K19 | K19 | RB p4 |

```
⛔ MERDİVEN TEK YÖNLÜ — geri dönüş YOK. Kırağı pası hiçbir klipte AZALMAZ;
   geminin pencereleri hiçbir klipte geri YANMAZ; yuva bir daha SÖNMEZ.
⛔ DURUM ÇİFTİ: aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK.
⚠️ AYNI SAYFADA İKİ DURUM — kılavuz §3 ② bunu ölçülmemiş bir çelişki sayar.
   BU DOSYANIN SEÇİMİ: AYNI SAYFA (RK1 p1↔p5↔p6 · RO p2↔p3 · RA p1↔p5 · RB p3↔p4).
   NEDEN: depo pratiği bu yönde ve kırağı pası ancak temel hâlle YAN YANA
   görülünce ölçülebilir; ayrı sayfa ikinci bir kimlik kayması kapısı açardı.
   ⬜ ÖLÇÜM BORCU: ilk üretimde iki durumun özne karışması yaratıp yaratmadığı
   `GUNES_MEZARI_URETIM_DEFTERI.md`'ye yazılır.
```

## 5. 🗺️ KLİP → REFERANS EŞLEME

| klip | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| K01 | DIŞ · kafes ışığı | RO p1 | makro yüzey | RO-a | dönme hızı · hücrenin 4 s'lik geçişi · halkanın inlemesi |
| K02 | DIŞ · kafes ışığı | RA p1 · RO p2 | 3/4 profil | RA-K0 · RO-a | geminin kadrajı geçiş hızı · pencerenin yanık olması |
| K03 | İÇ · kafes ışığı | RK1 p4 | vizör ardı yüz CU | RK1-K0 | kaşların toplanması · kaskın bir derece inmesi · kaydın başlaması |
| K04 | DIŞ · fener + ay | RA p1 · RB p1 · RD p1 | geniş kurulum | RA-K0 · RK1-K1 | kuru tanenin sürüklenme oranı · kayışın sarkması |
| K05 | DIŞ · fener + ay | RK1 p5 · RD p2 | tam boy | RK1-K1 | adım kadansı (3 adım / 2 s) · pelerinin savrulması |
| K06 | DIŞ · fener + ay | RK1 p3 | ARKA | RK1-K1 | omuzla yüklenme · menteşe kırağısının dökülmesi |
| K07 | DIŞ · fener + ay | RD p3 · RO p4 | diz çökmüş orta | RO-c | buhar yakasının 2 s'lik ritmi · avucun taşta durması |
| K08 | DIŞ · fener + ay | RK1 p6 | eldiven makro | RK1-K1 | parmakların bir kez bastırıp gevşemesi |
| K09 | DIŞ · fener + ay | RD p2 · RK1 p1 | tam boy | RK1-K1 | kaskın duvarı soldan sağa taraması |
| K10 | İÇ · kule lambası | RK1 p1 | tam boy | RK1-K1 | lambanın 2 s'lik sönüp yanması · kaydın döngüsü |
| K11 | İÇ · kule lambası | RK1 p6 | levha makro | RK1-K1 | döngünün iki kez başa dönmesi |
| K12 | İÇ · kule lambası | RK1 p4 | vizör ardı yüz CU | RK1-K1 | avucun levhaya inmesi · ışığın sönmesi |
| K13 | DIŞ · fener | RB p1 · RB p3 | orta | RB-K0 | kolun sonuna kadar inmesi · omuzların düşmesi |
| K14 | DIŞ · fener | RB p3 | yuva makro | RB-K0 | fenerin çeyrek dönüşü · dört yuvanın sırayla aydınlanması |
| K15 | İÇ · gemi lambaları | RP p1 · RA p5 | orta | RP-a · RA-K0 | çekirdeğin 2 s'lik nabzı · rampanın açık olması |
| K16 | İÇ · gemi lambaları | RK1 p4 | profil CU | RK1-K2 | parmakların tek tek açılması · kolun yerinde kalması |
| K17 | İÇ · gemi lambaları | RP p2 · RK1 p4 | orta | RP-a · RK1-K2 | iki çeyrek tur · üç lambanın sönmesi · nefes |
| K18 | DIŞ · fener | RP p1 · RA p5 | kayış makro | RA-K1 | çekişin oranı — 2 s'de bir el genişliği |
| K19 | DIŞ · fener + yuva | RP p2 · RB p4 | orta | RB-K1 | ilk oturmanın tutmaması · kırağının sıyrılması |
| K20 | DIŞ · fener + yuva | RP p3 · RA p3 | çubuk CU | RP-b | avucun bir el genişliği önünde durması · çubuğun yutulması |
| K21 | DIŞ · devralma | RA p3 · RO p2 | geniş kurulum | RO-a→b | halkaların açılma sırası · kürenin kadrajı 8 s'de terki |
| K22 | DIŞ · yeni güneş | RD p2 · RO p3 | orta, üst açı | RO-b | ışık kenarının duvardan kaldırıma inmesi |
| K23 | DIŞ · yeni güneş | RK1 p1 · RA p5 · RD p1 | tam boy | RK1-K2 · RA-K1 | kaskın sokağı taraması · ellerin kapanmaması |
| K24 | DIŞ · yeni güneş | RD p3 | oyuk makro | RD-b | ışık kenarının oyuk içindeki 5 s'lik geçişi · yaprak ucu |

```
⛔ "METNE DEVREDİLEN" hiçbir satırda BOŞ DEĞİL — panel biçimi verir, metin olayı.
⛔ Bir klipte EN ÇOK 3 kayıt yüklenir; en kalabalık satırlar K04 ve K23 = 3.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR.
   GEREKÇE: panel oluğu ve etiket sızıntısı depoda ÖLÇÜLDÜ (YERÇEKİMİ üç önlem ·
   BLUE DRIFT · UPHILL DARK); "tam sayfa yükle" iddiası hiç ölçülmedi.
· Flow çağırma etiketi KOD olur, asla özel ad [D34]. ⚙️ `@RK1` biçimi SINANMAMIŞ —
  arayüzde yoksa panel dosyası elle yüklenir ve bu satır düzeltilir.
```

## 6. 📸 REFERANS SAYFALARI

> ⛔ İngilizce IMAGE PROMPT, başlıktan sonraki **İLK** çitli bloktur; künye ve
> kabul sınavı promptun ALTINA yazılır (kılavuz §6 · kapı bu bloğu ölçer).
> ⛔ Sayfa promptu bir BÖLÜM promptu değildir: kelime bandı ve ㉗ koşmaz, ama
> negatif çekirdeğin imzası (bloom · metin · film grain · insan sayısı) taşınır.

### 📸 IMAGE PROMPT — SAYFA RK1 · zırh ve kask (tek figür)

```
IN FRAME: full body · back · face
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey backdrop, even neutral key with soft fill.

Exactly one human character, no clones and no second person. A woman standing straight and facing the lens in a heavy pressure suit of matte graphite quilted textile: squared composite shoulder caps rising to a raised collar ring, a scuffed graphite breastplate, a brushed-steel neck ring and steel wrist rings, heavy segmented dark gloves continuous with the sleeves. A crescent scorch the width of two fingers crosses the knuckles on the back of her LEFT glove, on the leather itself, not the cuff and not the fingers; no other burn or mark anywhere. The helmet is a squared hard graphite shell seated deep into the collar ring, two small square lamps set into the brow, a single flat front pane inside a thick dark rim; a soft warm 3200K fill from inside the chin lights her face, fully readable through the clear pane at every head angle; one thin unbroken specular line along the pane's upper edge is its only reflection. Her back is one continuous ribbed surface from collar to hip, closed and smooth, the shoulder caps wrapping over its upper edge and carrying two shallow recessed panels, nothing else. A long worn dark cloak falls to her calves; three ribs of tarnished dull-gold thread cross the upper chest; matte pale frost rime lies along the cloak hem and both shoulder caps.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. No back-mounted unit: no backpack, no tank, no hose, no cable and no rear housing of any kind — her back silhouette is flat. No dome, no bubble and no frameless wrap-around pane on the helmet. No bare skin anywhere: nothing exposed above the collar, at the wrist or at the ankle.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 6   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş   p2 · profil — siluet hattı ve pelerin   p3 · SIRT — düz siluet + iki gömme panel [D79/D139]   p4 · vizör ardı yüz CU [D146]   p5 · kırağı pası K1 — pelerin kenarı + omuz kapakları   p6 · SOL eldiven sırtı makro — hilal yanık izi [D91]
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146]. Kalın koyu çerçeve gotik ağırlığı da taşıyan ÜRETİLEBİLİR karşılıktır.
⛔ Sırtta yokluk listesi TEK BAŞINA tutmadı (iki filmde de ünite üretildi) — p3 sırta ne KOYULACAĞINI söyler: tek sürekli kaburgalı yüzey + iki sığ gömme panel + pelerin [D139].
⭐ p6 filmin KANIT zinciridir: K08 ve K11 aynı izi taşımak zorunda, yoksa suçlama düşer.
⚠️ Gri tonda zırh (mat grafit) ile bazalt duvar aynı değere düşer; figürü ayıran TEK kanal kırağı pasıdır — p5 ve p6 bu yüzden ZORUNLU panel.
```

```
KABUL SINAVI (RK1) — dört alan ZORUNLU [D144]:
  KABUL:       vizör TEK düz pane · çerçeve kalın ve koyu · yüz p1-p4'ün dördünde de okunuyor · sırtta çıkıntı sayısı 0 · yanık izi SOL elde ve parmak boğumlarında
  RET:         kubbe · balon · çerçevesiz sarma pane · sırtta herhangi bir ünite · sağ elde yanık · ikinci bir iz · çıplak deri
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Vizör kaç parçadan oluşuyor?" · doğru cevap: "Bir — tek düz cam, kalın koyu bir çerçevenin içinde."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 3 (kadın · mat grafit giysi · hilal yanık izi) — boy, ten rengi, saç ve yaş YAZILMADI [D167 · red defteri #15]
```
### 📸 IMAGE PROMPT — SAYFA RO · küre — iki hâl + buhar yakası

```
IN FRAME: none
Photorealistic still, 35mm film grain, plain black backdrop, the only light in frame coming from the subject itself.

A smooth sphere of dark red-gold light, its edge sharp against the black, its surface mottled like cooling iron with a few brighter cells lying across it. Three machined rings of dark scuffed metal close around it and end there, holding it at their focus, the sphere filling four fifths of their inner opening; nothing else is fixed to the rings, and they carry no cable and no hook. The light is read only on the surfaces it touches: the inner faces of the rings and the ribbed metal above them. The air around the sphere is clear and carries nothing.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. Human count zero: no people, no figures and no silhouettes of people. No corona, no rays, no halo, no light shafts, no lens flare and no haze around the sphere. No flame, no fire, no plasma arc and no sparks. No second sphere.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · makro yüzey — hücrelerin dokusu ve kenarın keskinliği   p2 · TAŞIMA hâli — üç halka + küre, 3/4 profil (oran 4/5)   p3 · ÇALIŞMA hâli — gökte disk, bazalt kule hattının üstünde   p4 · buhar yakası — sıcak taşın üstünde dik beyaz yaka, bir el yüksekliği
⭐ Bu sayfa filmin 1 NUMARALI RİSKİNİN aracıdır [D192 · A5]. Metin dört sayıyı taşır; panel onları GÖSTERİR.
⛔ p2 ile p3 aynı sayfada iki DURUMDUR (§4): aynı ışık yönü ve aynı mesafede üretilir, tek fark ölçek ve parlaklıktır.
⛔ p4 §3.9 kartının kanıt nesnesidir: yükseklik ve ritim YAZILI — bir el yüksekliği, 2 s'de bir kalkıp çöken yaka.
⛔ Halkalar p2 ve p3 arasında AÇILIR ama SÖKÜLMEZ: paneller aynı üç halkayı gösterir, K21 yalnız açıklığı değiştirir.
```

```
KABUL SINAVI (RO) — dört alan ZORUNLU [D144]:
  KABUL:       kürenin kenarı tek karede takip edilebiliyor · korona 0 · halkaların iç açıklığına oranı 4/5 · aradaki hava pussuz · halka sayısı 3
  RET:         ateş topu · korona · ışın hüzmesi · lens parlaması · ikinci küre · kıvılcım · halkada kablo
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Bu ışık nereden geliyor, etrafında hale var mı?" · doğru cevap: "Kürenin kendisinden; hale yok."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = — (kadrajda insan yok)
```
### 📸 IMAGE PROMPT — SAYFA RA · gemi

```
IN FRAME: none
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, soft top light with a faint reflection from below.

A long ribbed hull, its spine broken into repeating arches in the same ribbed language as a stone arcade, its bow to screen left. One lit window the height of a door is set into the spine, and there is exactly one lit window and no other. Three machined rings run from the spine down under the hull and end there, a portable copy of a stone cradle cut in metal. The hull reads about twenty-four body-lengths of a standing figure from bow to stern, and the window reads a little taller than that figure. Exactly one suited figure stands at the hull's flank as a scale witness, no more than a dark silhouette, no second person and no crew. Matte dark metal, scuffed along every edge, no gloss anywhere.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. Exactly one human figure in frame, the scale witness: no second person and no crew. No second ship and no other craft. No exhaust, no plume, no engine glow and no visible thruster. No dome and no bubble canopy. No landing lights and no beacons.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU (K02 · K21)   PANEL: 5   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · profil — tam siluet + ölçek şahidi (1H)   p2 · 3/4 ön — üç halka ve pencere ilişkisi   p3 · halka grubu makro — kilit ağzı ve üç halkanın dizilimi   p4 · tepe — omurga kemerlerinin ritmi   p5 · pencere durumu K1 — aynı pencere KARANLIK (p1 ile aynı kadraj)
⛔ Metre prompt gövdesine GİRMEZ [D138]: oran GÖVDE BOYU cinsinden yazıldı (1H = kasklı gövde · UZAY_USSU §1).
⭐ Üç halka kaidenin İŞLENMİŞ METALDE KABA KOPYASIDIR: bütün geri hikâye tek görüntüde, repliksiz.
⛔ p5 bir DURUM ÇİFTİDİR: p1 ile aynı kadraj, aynı ışık, tek fark pencerenin yanık olmaması.
⚠️ Gemi K02 ve K21 kadrajının DIŞINA taşar; panel tam gövdeyi gösterir, prompt taşmayı bilerek yazar.
```

```
KABUL SINAVI (RA) — dört alan ZORUNLU [D144]:
  KABUL:       halka sayısı 3 · aydınlık pencere sayısı 1 · gövde boyu ölçek şahidine göre ~24 gövde · burun ekran soluna bakıyor
  RET:         dördüncü halka · ikinci aydınlık pencere · egzoz konisi · kubbe kabin · ikinci gemi
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Gövdede kaç halka ve kaç aydınlık pencere var?" · doğru cevap: "Üç halka, bir pencere."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = — (ölçek şahidi silüet; öznitelik 0)
```
### 📸 IMAGE PROMPT — SAYFA RB · salıverme kaidesi

```
IN FRAME: none
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, one hard directional key from the side with weak fill.

Three stone arches of black basalt standing side by side in the same ribbed language as a city of thin towers, their span about four body-lengths of a standing figure. At their centre, set into the stone floor between them, a round open socket faces the sky: a machined cylindrical seat with exactly four shallow lock slots around its rim, frost crusted in every slot. A long machined engage lever stands at the foot of the left arch, about one and a half forearms long. Exactly one suited figure stands beside the middle arch as a scale witness, no more than a dark silhouette, no second person. Dry black stone, frost in every crack, no gloss anywhere.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. Exactly one human figure in frame, the scale witness: no second person. No machinery, no cables, no pipes and no panels on the arches. No second socket. No light coming out of the socket in this reference.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🟠 K13'ten önce   PANEL: 4   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · geniş kurulum — üç kemer + ölçek şahidi   p2 · devreye alma kolu ve yuvanın ilişkisi   p3 · yuva makro K0 — dört kilit yuvası, ölü ve karanlık   p4 · yuva durumu K1 — aynı kadraj, yuva IŞIK ALMIŞ
⛔ Kaide, geminin üç halkasının ORİJİNALİDİR: aynı kaburga dili, taşta. Bu benzerlik geri hikâyeyi repliksiz taşır.
⛔ p4 bir DURUM ÇİFTİDİR: p3 ile aynı kadraj, tek fark yuvanın ışık alması (K19'un sonucu) — ışık yuvanın İÇİNDEN, hüzme yok.
⛔ Kolun BOYU yazılı çünkü K13 kolun sonuna kadar inmesini ölçüyor; boy kayarsa hareketin süresi de kayar.
```

```
KABUL SINAVI (RB) — dört alan ZORUNLU [D144]:
  KABUL:       kemer sayısı 3 · kilit yuvası sayısı 4 · yuva bir silindir için işlenmiş · kolun boyu ~1,5 ön kol · kemerlerde makine yok
  RET:         dördüncü kemer · üç ya da beş kilit yuvası · kabloyla bağlı kaide · ikinci yuva · kemerlerde panel
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Yuvanın ağzında kaç kilit yuvası var?" · doğru cevap: "Dört."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = — (ölçek şahidi silüet)
```
### 📸 IMAGE PROMPT — SAYFA RP · çekirdek + anahtar çubuğu

```
IN FRAME: none
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, even product light with clean fill.

Two objects laid on a neutral surface with one empty heavy segmented dark glove beside them for scale, no person in frame, no arm and no hand inside the glove. First object: a ribbed steel cylinder about the length of a standing figure's torso and a third of that across, two seal rings at its near end, its ribs deep and evenly spaced, the metal scuffed and matte. Second object: a plain steel bar the length of a forearm, square in section, one end cut into a simple key profile, a bright steel collar a third of the way along it. The glove rests against the cylinder so its size can be read against the ribs. Matte metal, worn edges, no gloss anywhere.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. Human count zero: no people and no figures. No screens, no indicators, no lamps and no readouts on either object. No cables, no hoses and no connectors. No second bar and no second cylinder. No disc and no medallion.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🟠 K15'ten önce   PANEL: 3   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · çekirdek 3/4 — kaburga ritmi + eldivenle oran   p2 · mühür halkaları makro — iki halka ve yatak yüzeyi   p3 · anahtar çubuğu — tam boy + anahtar profili ve bilezik
⭐ Anahtar bir DİSK değil ÇUBUKTUR: parmak ucu işi gövde eylemine büyütüldü [MIKRO_AKSIYON §1] ve amblem yasağıyla çatışma böyle çözüldü [D138].
⛔ Alet TEK RİJİT PARÇA yazılır, parmakların alet üstündeki hareketi TARİF EDİLMEZ [MIKRO_AKSIYON §3 ③].
⛔ Filiz bu sayfada DEĞİL: K24 filizi RD p3'te, oyuğun içinde, bir parmak boyunda ve üç yapraklı, 1 adet.
⚠️ Çubuk K20'de kilit tarafından YUTULUR — panel onun SAĞLAM hâlini gösterir, sonrası prompt işidir [D179].
```

```
KABUL SINAVI (RP) — dört alan ZORUNLU [D144]:
  KABUL:       çekirdek eldivene göre ~bir gövde uzunluğu · mühür halkası sayısı 2 · çubuk bir ön kol boyu ve KARE kesitli · göstergesi 0
  RET:         ekranı/lambası olan çekirdek · üç mühür halkası · ikinci çubuk · kablo · DİSK biçimli anahtar · amblem
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Silindirin ucunda kaç halka var?" · doğru cevap: "İki."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 1 (yalnız eldiven, ölçek için — kişi yok)
```
### 📸 IMAGE PROMPT — SAYFA RD · şehir ve oyuk (dünya çapası)

```
IN FRAME: none
Photorealistic still, 35mm film grain, the film's own single light: one hard low source out of frame, long straight shadows, weak fill, no haze.

A city of black basalt: thin ribbed towers standing to a straight horizon, an avenue of giant seated statues whose knees stand higher than a walking figure, frost crusted along every ledge and in every crack, drifted dry snow along the paving. Above it a black sky thick with stars and one shattered moon low over the rooftops, its remnant ring a thin arc, the moon about as wide as a plate held at arm's length. At the city's edge three stone arches carry a round open socket facing the sky. At the foot of one wall a rock hollow the width of two hands, the stone around it bare where the rest is frost-crusted, a thin upright collar of white vapour standing off its lip about a hand's height; inside the hollow, standing out of warm bare stone, one dark maroon shoot the length of a finger with exactly three leaves.

NEGATIVE: 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No emblem, no badge, no patch, no rank mark and no flag anywhere. No panel gutters and no borders between views. Human count zero: no people, no figures and no silhouettes of people. No haze, no fog, no mist and no light shafts. No vegetation anywhere except the single shoot inside the hollow. No second moon, no planet and no lights in the sky but the stars. No water, no liquid and no melting ice.

Output: 16:9, 3840×2160, no text, no watermark.
```

```
ÖNCELİK: 🟠 K04'ten önce   PANEL: 3   SEED: ⬜ (Flow alanı üretimden önce sınanır [D142])   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · geniş kurulum — kule hattı + parçalanmış ay + kaide silueti (DÜNYA ÇAPASI üçlüsü)   p2 · heykel caddesi — diz yüksekliği ve kaburga ritmi   p3 · kaya oyuğu makro — buhar yakası + üç yapraklı filiz
⭐ p1 World Bible'ın ÜÇ CÜMLESİNİN görsel karşılığıdır [D209]: gök · ufuk · yer imi. 13 dış klibin hepsi bu üç cümleyi birebir taşır.
⛔ Işık BU SAYFADA sahnenin KENDİ ışığıdır, nötr stüdyo ışığı değil: mekân varlığı kendi ışığında kilitlenir [REFERANS §4.1].
⛔ p3 canlı kaydıdır: filiz SAYILI ve BOYUTLU, hareket 0 — ayrı RV sayfası bu yüzden açılmadı.
⛔ Pus yasağı §3.9 kartının D74 sapmasıdır: uzun gece pusu yağdırdı, gölge SERT ve DERİN.
```

```
KABUL SINAVI (RD) — dört alan ZORUNLU [D144]:
  KABUL:       ay genişliği bir kol boyu tabak · ay sayısı 1 · gökte başka cisim 0 · filiz 1 adet, üç yaprak, bir parmak boyu · başka bitki 0 · pus 0
  RET:         ikinci ay · gezegen diski · pus · ışık hüzmesi · başka bitki · eriyen buz · su · gökte uçan enkaz
  YABANCI GÖZ: paneli hiç okumamış biri · soru: "Gökte kaç cisim ve oyuğun içinde kaç filiz var?" · doğru cevap: "Bir ay; bir filiz."
  SONUÇ:       ⬜ (geçmezse sayfa yeniden üretilir ve o varlığın klipleri ÜRETİLMEZ)
  ⑳ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = — (kadrajda insan yok)
```
## 7. ✅ KABUL KAPISI — üretim başlamadan önce

> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `GUNES_MEZARI_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.

```
☑ ① PANEL ARİTMETİĞİ  künye 25 = tablo 6+4+5+4+3+3 = 25 ✅
☑ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te VAR (10/10) · YETİM sayfa 0 ✅
☑ ③ 120 PX TESTİ      RK1 p1 omuz kapakları + pelerinin dik yakası · RO p2 kürenin
                      kenarı · RA p1 üç halka · RD p1 kule ritmi — dördü de ayırt edilir
☑ ④ METİN SAYIMI      altı promptta harf/rakam/ok/ölçü çizgisi yasağı VAR [D45/D138]
☑ ⑤ D79 VİZÖR         optik berrak · yansıma yalnız üst kenarda tek çizgi · yüz HER
                      KAFA AÇISINDA okunur + GÖRÜNÜR KALIN ÇERÇEVE (kubbe/balon yasak)
☑ ⑥ D79/D139 SIRT     çıkıntı sayısı 0 AMA p3 yüzeyi POZİTİF tarifli
☑ ⑦ D69 KLON          insan taşıyan üç promptta sayı BEYAN EDİLDİ (RK1 1 · RA 1 · RB 1)
☑ ⑧ DURUM ÇİFTİ       RK1 p1↔p5↔p6 · RO p2↔p3 · RA p1↔p5 · RB p3↔p4 — hepsi aynı
                      kadraj, aynı ışık yönü, tek değişken
☑ ⑨ ⑲ KİMLİK YIĞINI   RK1'de öznitelik 3 (≤3) · başka sayfada kişi yok
☑ ⑩ ⑳b DEĞİŞİM        hiçbir panel değişimin SONRASINI yazmıyor [D179] — RP p3 çubuğu
                      SAĞLAM, RA p1 pencere YANIK, RB p3 yuva ÖLÜ
☑ ⑪ ÖLÇEK ŞAHİDİ      RA p1 · RB p1'de 1H kasklı gövde · RP'de boş eldiven
☐ ⑫ SEED / SHA KAYDI  ⬜ üretim gününde §2 tablosuna yazılır
☐ ⑬ SAYI AYNILIĞI ⚙️  RK1 promptu ↔ PLAN Character Bible: pane 1 · alın lambası 2 ·
                      altın kaburga 3 · gömme panel 2 · yanık SOL el boğumları — beş
                      değer tek tek karşılaştırılır (sayfa promptu kısaltıldığı için
                      BAYT diff'i DEĞİL; kısaltma kelime bandı kapısının sonucu)
☐ ⑭ GRİ TON TESTİ ⚙️  `ffmpeg -i <panel> -vf hue=s=0 gri.png` — ayrım yalnız renge
                      dayanıyorsa panel REDDEDİLİR. ⚠️ BU FİLMDE KRİTİK: zırh mat
                      grafit, şehir siyah bazalt; gri tonda figürü ayıran tek şey
                      KIRAĞI PASI olmalı (RK1 p5/p6). ⬜ panel gelince koşulur
⛔ Bu on dört madde işaretlenmeden ilk klip ÜRETİLMEZ. Bugün 11 ✅ / 3 ⬜ ve
   üçünün hepsi PANEL DOSYASI gerektiriyor — metinle kapatılamaz.
```

## 8. ⬜ ÜRETİM GÜNÜNE KALAN

```
⬜ SEED ve SHA-256 sütunları (altı sayfa)      ⬜ İMAJ MODELİ + SÜRÜM + TARİH
⬜ DURUM: TASLAK → ONAYLI (altı sayfa)         ⬜ ⑫ ⑬ ⑭ maddeleri
⬜ KABUL SINAVI "SONUÇ" satırları (altı sayfa)
⬜ Aynı sayfada iki durumun özne karışması yaratıp yaratmadığı (§4 ölçüm borcu)
⬜ `@RK1` biçiminde çağırmanın Flow'da çalışıp çalışmadığı (§5 son satır)
```
