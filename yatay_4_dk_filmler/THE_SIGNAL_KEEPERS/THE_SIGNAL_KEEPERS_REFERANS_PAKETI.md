# 🧷 THE_SIGNAL_KEEPERS — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
varlık `UZAYLI_VARLIK` §4 · ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK K21 → merkezî seçim K19-K20 → kapanış K24 →
> K01 → gerisi [D168].
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
> ⛔ En az bir kutu işaretlenmeden paket yazılmaz.
```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: kâşif — kapalı
     berrak vizör 24/24 klip; D146'nın üç ölçülmüş vakası paketsiz filmlerde
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: VARLIK — bu
     deponun hiç üretmediği şey; metin tek başına tutmaz (⭐ paketin 1 numaralı sebebi)
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: şehir, kuleler,
     kaya geçidi ve salonun yuva sırası (KART 13 · ölçek sahneden sahneye kayıyor)
☑ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: tek varlık,
     kademeli olarak kadrajda (iz → siluet → parça → tam form → parça)
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: — (tekrar eden
     OLAY yok; ton üç kez duyulur ama olay değil eylemdir)
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: mavi cam küre ·
     sonda · varlık · yuva — dördü de dönüyor; THE_HERD kostüm 3/10 (kask baloncuğu
     kayboldu ve geri geldi) ve THE_COUNTED_TURN ② 3.0 (kimlik kırılması)
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_SIGNAL_KEEPERS          FORMAT: yatay 4 dk · 24 klip × 10,0 s
SAYFA ORANI = FİLM ORANI          ORAN: 16:9        ÇÖZÜNÜRLÜK: 4K (3840 × 2160)
SAHNE SAYISI: 6 sahne / 24 klip
SAYFA: 6   TOPLAM PANEL: 19   ARİTMETİK: R1 4 + R2 4 + R3 3 + R4 3 + R5 3 + R6 2 = 19
   ⛔ Bu toplam §2 tablosunun panel toplamına EŞİT olmalı (§7 ①)
İMAJ MODELİ + SÜRÜM: ⬜ ÜRETİMDE YAZILIR (model + sürüm birlikte)
TARİH: 28.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_SIGNAL_KEEPERS_KAPAK.md` (R onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK K21 → merkezî seçim K19+K20 → kapanış K24 → K01 → kalanı

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | VARLIK | 4 | tam form · avuç · siluet · omuz çatlağı | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R2 | GİYSİ + KASK | 4 | 3/4 tam boy · profil · SIRT · vizör ardı yüz | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R3 | SONDA + MAVİ KÜRE | 3 | sonda tam · cam yuva BOŞ · küre tek | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R5 | YUVA + YATAK | 3 | yuva çerçevesi · yuvanın yatağı · çekirdek | 🟠 K17'den önce | | | ⬜ TASLAK |
| R6 | KIRIK CAM PARÇASI | 2 | parça tek · parça avuçta | 🟠 K10'dan önce | | | ⬜ TASLAK |
| R4 | ŞEHİR + GEÇİT + SALON | 3 | geçit ağzı · kule dibi · salon derinliği | ⏳ K13'ten önce | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli klipten önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın klipleri ÜRETİLMEZ.
⛔ R1 ve R2 ikisi de 🔴: K21 (ilk üretilen klip) ikisini birden çağırır mı? HAYIR —
   K21'de varlık kadrajda DEĞİL. Ama R2 K21'in kendisi için zorunludur (gövde + kask
   alt kenarı kadrajda) ve R1 ikinci üretilen klip grubundan (K19) önce ONAYLI olmalı.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp
   karşılaştırılır (yanlış dosyayla üretim yapılmasın).
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk klip | son klip | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| H1 | kâşif — basınçlı giysi, kapalı berrak vizör | insan | K01 | K24 | R2 | 🟠 kask/vizör biçim kayması |
| C1 | varlık — mineral yüzeyli, gözü anılmayan gövde | canlı | K06 | K22 | R1 | 🔴 anatomi kayması (film 1 no) |
| O1 | mavi cam küre (omuz yuvasında) | prop | K01 | K24 | R3 | 🟠 el ↔ küçük cam kaynaşması |
| O2 | kırık mavi cam parçası | prop | K10 | K10 | R6 | 🟠 aynı sınıf + uzuv izolasyonu |
| O3 | ön kola gömülü düz panel | prop | K02 | K03 | R2 | 🟡 ekran daveti (gösterge YOK) |
| P1 | onarılmış insan sondası | araç | K17 | K24 | R3 | 🟠 yüzeyinde harf/arma daveti |
| P2 | sondanın çekirdeği (kısa silindir) | prop | K20 | K21 | R5 | 🟡 söküm/yerleştirme |
| M1 | yuva çerçevesi ve yuvanın yatağı | mekân | K16 | K24 | R5 | 🟡 tekrar eden birim sayımı |
| M2 | kaya geçidi ve şehrin kuleleri | mekân | K13 | K15 | R4 | 🟠 ölçek kayması (KART 13) |
| M3 | salon — iki sıra yuva, derinlik ışıksız | mekân | K16 | K24 | R4 | 🟠 "yüzlerce" doldurma riski |
| M4 | ışıklı alçak bitki bandı | mekân | K04 | K07 | — | 🟡 bloom ↔ kendi kaynağı |
| M5 | uçurum kenarı ve sisli vadi | mekân | K01 | K03 | — | 🟢 tek ışık, tek zemin |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Kod kanonu: kılavuz §2.
⛔ Risk sınıfı `ASTRONOT_DONANIM` eşya tablosundan alınır (burada tarif edilmez).
⚠️ SAYFASI OLMAYAN İKİ VARLIK — M4 ve M5 — ve bu BİLİNÇLİDİR: ikisi de TEK ışık
   kuralı ve TEK zemin cümlesiyle metinle tutulabiliyor (bitki kendi kaynağı ·
   sis oturur). Oranı sözle yazılamayan hiçbir öğe taşımıyorlar. ⛔ Biçim kayması
   çıkarsa sayfa açılır ve bu satır güncellenir.
⛔ YETİM sayfa: 0 — altı sayfanın altısı §5'te çağrılıyor.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç klibi | dönüşüm klibi | panel |
|---|---|---|---|---|---|
| C1 | K0 (iz) | yalnız gölge, gövde yok | K07 | — | R1 p3 |
| C1 | K3 (siluet) | uzun, ince, küçük düz baş | K06 | K06 | R1 p3 |
| C1 | K2 (parça) | açık avuç, dört eşit parmak | K10 | K10 | R1 p2 |
| C1 | K4 (tam form) | bütün gövde, sayılı anatomi | K13 | K13 · K15 · K16 | R1 p1 |
| C1 | K2 (parça, dönüş) | yalnız ön kol ve avuç | K19 | K19 | R1 p2 |
| O1 | K0 (omuz yuvasında) | yerinde, çizikli, kenarı çentikli | K01 | — | R3 p3 |
| O1 | K1 (sondanın yuvasında) | omuzdan gitti, sondaya oturdu | K24 | K23 → K24 | R3 p2 + p3 |
| M1 | K0 (ölü ve boş) | yatak karanlık, halkalar sönük | K17 | — | R5 p1 |
| M1 | K1 (uyanmış) | halka ışığı metalin İÇİNDE | K21 | K21 | R5 p1 |
```
⛔ MERDİVEN TEK YÖNLÜDÜR — C1'in merdiveni iz → siluet → parça → TAM FORM → parça
   biçiminde KAPANIYOR ve bu geri dönüş DEĞİLDİR: K4 yalnız S04-S05'te açılır,
   S06'da kadraja yalnız PARÇA girer (kılavuz "tam form en fazla bir-iki sahne").
   Gerekçe satırı: ölçek yürüyüşü (ardışık çift tam 1 kademe) S03 ve S06'ya geniş
   plan sokmuyor; 2,40 m'lik gövde o kadrajlara girmez [D74 · 03_SAHNE_SIRALAMASI §7c①].
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK (±%3 en).
   Bu paketteki iki çift: M1 (ölü ↔ uyanmış, R5 p1) ve O1 (omuzda ↔ sondada, R3).
⚠️ Aynı sayfada iki durum: kılavuz §3 ② bunu ölçülmemiş çelişki sayıyor. Bu dosyada
   seçim: AYNI PANELDE İKİ DURUM YAZILMAZ; her durum kendi paneline gider ve iki panel
   aynı kadraj metnini BİREBİR taşır. Sebep: tek panelde iki durum modelin ikisini
   karıştırıp bir ara durum çizmesine yol açıyor (ölçülmemiş ama maliyeti tek yönlü).
```

## 5. 🗺️ KLİP → REFERANS EŞLEME

| klip | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| K01 · K03 | dış · yansıyan tek kaynak | R2 p3 · R3 p3 | sırt + omuz yuvası | H1 K0 · O1 K0 | ön kol panelinin yanıp sönme ritmi · sisin alçalması |
| K02 | dış · yansıyan tek kaynak | R2 p4 · R2 p1 | vizör ardı yüz + ön kol paneli | H1 K0 | panelin atma aralığı · kaydın bozukluğu |
| K04 · K05 | dış · yansıyan + bitki ışığı | R2 p1 | gövde üst yarısı + eldiven | H1 K0 | yaprağın sönmesi · tozun kalkıp oturması |
| K06 | dış · yansıyan + bitki ışığı | R2 p2 · R1 p3 | sırt/profil + siluet | H1 K0 · C1 K3 | başın bir vuruş önce dönmesi |
| K07 | dış · bitki ışığı | R1 p3 (yalnız gölge hattı) | geniş gölge | C1 K0 | yaprakların dokunulmadan kapanma dizisi |
| K08 · K09 | dış · yansıyan tek kaynak | R2 p4 · R3 p3 | yüz + omuz yuvası | H1 K0 · O1 K0 | gölgenin genişlemesi · bakışın omza inmesi |
| K10 | dış · yansıyan + camın kendi mavisi | R1 p2 · R6 p2 | açık avuç + kırık parça | C1 K2 · O2 | avucun eşitsiz açılması · donuk ton |
| K11 | dış · yansıyan tek kaynak | R2 p4 · R3 p3 | yüz + küre + eldiven | H1 K0 · O1 K0 | berrak ton · vizör üstünden geçen ışık deseni |
| K12 | dış · yansıyan tek kaynak | R2 p3 · R1 p1 (kırpım: omuz levhası) | sırt + karanlık kütle | H1 K0 · C1 K4 | kütlenin kadrajı terki · tozun oturması |
| K13 · K15 | dış · yansıyan + şehir bandı | R1 p1 · R4 p1 · R2 p3 | tam form + geçit ağzı + sırt | C1 K4 · M2 | konum kilidi · dokuz adım mesafe |
| K14 | dış · yansıyan + şehir bandı | R4 p2 | kule dibi, zeminden | M2 | köprüdeki ışık bandının akışı |
| K16 | iç · nokta ışıklar, derinlik ışıksız | R1 p1 · R4 p3 | tam form + salon derinliği | C1 K4 · M3 | dört adım · derinliğin ışıksız kalması |
| K17 | iç · nokta ışıklar | R3 p1 · R3 p2 · R5 p1 | sonda + BOŞ cam yuva + yuva | P1 · M1 K0 | çerçevenin tek ince notası |
| K18 | iç · nokta ışıklar | R2 p4 · R3 p1 (kırpım: ızgara) | yüz + ızgara | H1 K0 · P1 | kaydın net duyulması |
| K19 | iç · nokta ışıklar | R1 p2 · R5 p3 · R2 p1 | ön kol + avuç + panel | C1 K2 · P2 | ret gecikmesi 0,8 s · havadaki el |
| K20 | iç · nokta ışıklar | R2 p4 · R5 p3 | yüz + çekirdek + iki halka | H1 K0 · P2 | iki çeyrek tur · sesin ortada kesilmesi |
| K21 | iç · nokta ışıklar → halka ışığı | R5 p1 · R5 p2 · R5 p3 | yuva + yatak + çekirdek | M1 K0→K1 · P2 | oturma direnci · ışığın tırmanması |
| K22 | iç · halka ışığı | R2 p4 · R5 p1 | yüz + yuva dizisi | H1 K0 · M1 K1 | dizinin yukarı dönmesi |
| K23 | iç · nokta ışıklar | R3 p3 · R2 p1 | omuz yuvası + küre + eldiven | O1 K0 | halkanın çeyrek turu · kürenin kalkması |
| K24 | iç · nokta ışıklar + kürenin mavisi | R3 p2 · R3 p3 · R6 p1 | cam yuva + küre | O1 K1 · P1 | berrak ton · taştaki mavi leke |
```
⛔ "METNE DEVREDİLEN" BOŞ BIRAKILAMAZ — referansın taşıyamadığı her şey
   (anlık eylem, geçici yansıma, hareket) buraya yazılır [kılavuz §5.1].
⛔ Bir klipte EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2). Bu tabloda hiçbir satırda
   3'ten fazla kayıt yok; K21 tam 3 (üçü de aynı sayfadan, R5).
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   ⚠️ Dört eski paket TERSİNİ yazıyor ve iddia ÖLÇÜLMEDİ. Bu dosyanın seçtiği
   yükleme biçimi: KIRPIM. Gerekçe: tam sayfada dört panel yan yana duruyor ve
   modelin hangi paneli çapa saydığı belirsiz — kırpım belirsizliği kaldırır.
   ⬜ ÖLÇÜM RANDEVUSU: ilk üç klipte kırpım/tam sayfa A-B denemesi yapılır ve
     sonuç bu satıra yazılır (varsayım olarak KALMAZ).
· Flow çağırma: `@R1` … `@R6` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarında `📎 REFERANS` satırı YOKTUR: bu rejimde eşleme YALNIZ burada
  durur, prompt tek başına çalışır (AGENTS §2 kural ③). Sayfası ⏳ olan klip
  "ÜRETİLMEZ" damgası taşır.
```

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · VARLIK
```
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill, deep focus.

Exactly one standing figure and no people anywhere in the frame. A tall thin standing
figure of dark mineral skin, on one axis, with two legs and two long forearms that
reach below the knee, one broad plate across the left shoulder with a single crack
running down it, and the front of its head one smooth mineral membrane with a faint
pattern of pale light moving under it. Its surface is matte and lightly crazed like
cooled basalt, dry and dusted with fine grey grit in the creases, and the plates meet
along clean worked seams. Its hands are open with four equal digits, no claws and no
nails. A plain grey scale bar shape of a human-figure silhouette stands beside it for
proportion, its head at three quarters of the figure's height.

NEGATIVE: No readable text, letters, digits or symbols on any surface — no labels, no
captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark.
Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy
texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No
second pair of limbs, no tail, no wings, no horns, no armour plates beyond the one
shoulder plate. No halo, no light shafts, no lens flare and no corona anywhere. Nothing
melts, warps or changes shape.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 TAM FORM — sayılı anatomi + ölçek şahidi
               p2 · AÇIK AVUÇ tek başına (ECU) — dört eşit parmak, kenarı
               p3 · SİLUET — arkadan ışıklı düz siyah leke + yerdeki GÖLGE hattı
               p4 · SOL OMUZ LEVHASI CU — tek çatlak, mineral doku
⛔ GÖZ HİÇBİR PANELDE ANILMAZ — ne pozitif ne negatif olarak [D123]. Zar yazılır.
⛔ "creature / alien / monster / being" kelimeleri hiçbir promptta yok — yalnız
   "a tall thin standing figure" gibi BİÇİM adları (politika + UZAYLI_VARLIK §6).
⛔ Kamera yayı: bu sayfada 3/4 ve profil VAR, ARKA GÖRÜNÜM YOK — film boyu yay ≤90°
   ve arka hiç açılmıyor; panel de açmaz.
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de sayılar TUTUYOR: 1 eksen · 2 bacak · 2 ön kol · 1 omuz levhası ·
              o levhada 1 çatlak · boy = yanındaki insan silueti boyunun 4/3'ü ·
              göz 0 · ikinci uzuv çifti 0
  RET:        herhangi bir panelde göz, ağız, kubbe/plaka kask, ikinci uzuv çifti,
              kuyruk, kanat ya da ikinci bir omuz levhası
  YABANCI GÖZ: paneli hiç okumamış birine p1'i göster · soru: "bu ne, ve kaç kolu var?"
              · doğru cevap: "canlı bir şey / bir yaratık" + "iki"  ⛔ "insan" cevabı RET
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · K13 · K15 · K16 · K19 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R2 · GİYSİ + KASK
```
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill, deep focus.

Exactly one human character — no clones, no second person. A person stands facing the
lens, sealed in an off-white pressure suit of thick creased multilayer nylon, with
dark-grey segmented joint guards at the elbows and knees and a faded burnt-orange band
wrapped all the way around the LEFT upper arm. A visible brushed-steel neck ring locks the helmet to a raised collar, and
steel rings close both wrists above heavy segmented dark-grey gloves that are one piece
with the sleeves. On the left shoulder a round brushed-steel seat holds a sphere of dark
blue glass a hand's breadth across, seated in it, no cord and no strap near it. A flat panel is set into the left forearm, flush with
the fabric, carrying one small even light and no display. The visor is optically clear glass with zero tint, zero
mirror coating and zero reflection, held in a visible thick dark-grey frame, and the
face is fully readable through it AT EVERY HEAD ANGLE, lit by a soft warm 3200K fill
from inside the chin of the helmet. The back of the suit is one continuous sculpted
surface from collar to hip, low-profile and unbroken, carrying nothing, with two shallow
recessed panels closed flush into it. Fixed wear that never moves: a matte
dusting of pale grey grit over the suit, heavier at the knees, and scuffed wrist rings.

NEGATIVE: No readable text, letters, digits or symbols on any surface, patch or sign —
no emblem, no badge, no rank mark, no flag, no labels, no captions, no arrows, no
callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm
film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no
waxy texture, no face morphing. 0% bloom, no glow, no soft focus, every surface keeps
visible texture. No bare skin anywhere — none above the collar, none at the wrists
between glove and sleeve, none at the ankles between boot and leg. The visor is one flat
clear pane in a thick dark rim — no dome, no bubble, no mirror coating, no tint and no
environment reflected in it. No backpack, no tank, no hose and no rear housing of any
kind.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek, duruş, ön kol paneli, omuz yuvası
               p2 · profil — siluet hattı, yaka halkası, kask kabuğunun kenarı
               p3 · SIRT — düz siluet, sürekli yüzey [D79/D139]
               p4 · vizör ardı yüz CU [D146] — tek düz pane, kalın çerçeve, çene dolgusu
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — model boş sırtı DOLDURMAK zorundadır;
   panelin işi ona ne KOYACAĞINI söylemektir: "one continuous sculpted surface …
   two shallow recessed panels closed flush into it" [D123 · D139].
⭐ ARKETİP: E BELGESEL (`UZAY_GIYSISI` §2). Üç zorunlu hafifletme yazılı: matte
   (grit) + creased/scuffed + tekstil eklem (nylon gövde, segmentli eklem koruması).
```
```
KABUL SINAVI (R2) — dört alan ZORUNLU [D144]:
  KABUL:      p4'te yüz panenin İÇİNDEN okunuyor · pane TEK ve DÜZ · çerçeve kalın ve
              koyu gri · yansıma yalnız üst kenarda TEK ince çizgi · p3'te sırt
              çıkıntı sayısı 0 ama yüzey tarif edilmiş
  RET:        kubbe / balon / çerçevesiz sarma / aynalı kaplama / tint; sırtta herhangi
              bir ünite, tank, hortum; giysinin herhangi bir yerinde harf ya da arma
  YABANCI GÖZ: p4'ü hiç okumamış birine göster · soru: "kaç cam var, ve düz mü?"
              · doğru cevap: "bir tane, düz"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · 21 insanlı klibin HİÇBİRİ ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0
     ⭐ Bilinçli: boy · ten · saç · yaş · yüz hatları HİÇ yazılmadı; kimlik dizisini
     dört GİYSİ özniteliği taşıyor (kumaş · eklem koruması · turuncu bant · omuz
     yuvası). Red defteri #15 tam bu yığından düştü [D167].
```

### 📸 IMAGE PROMPT — SAYFA R3 · SONDA + MAVİ KÜRE
```
Photorealistic product-style still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill, deep focus.

No people in the frame. An upright repaired machine stands on three short legs, its
body a squat metal drum the height of a human chest, its outer panels dented and scored
from a long fall. Three of those panels have been replaced with fitted plates of dark
mineral, matte and lightly crazed, their new edges flush with the metal and finely
worked. On the face of the drum, at the centre, a round seat of brushed metal a hand's
breadth across is empty, its rim clean and unscratched, and below it a fine grille of
close-set slots runs across the panel. A short dark cylinder the length of a forearm is
seated in the side panel with two knurled rings at its near end. Beside the machine,
lying alone on the backdrop, a single sphere of dark blue glass a hand's breadth across
is chipped at one edge and crossed by fine scratches, with no cord and no strap
anywhere near it.

NEGATIVE: No readable text, letters, digits or symbols on any surface, plate or panel —
no emblem, no badge, no flag, no serial mark, no labels, no captions, no arrows, no
callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm
film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no
glow, no soft focus, every surface keeps visible texture. No antenna dish, no solar
panel, no wheels, no flag pole and no second machine. No halo, no light shafts, no lens
flare and no corona around the glass.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · sonda TAM — üç mineral yama, ızgara, yan paneldeki silindir
               p2 · CAM YUVA CU — BOŞ hâl (K17) ve kürenin oturduğu hâl (K24) ayrı iki
                    kare, kadraj metni BİREBİR aynı (durum çifti)
               p3 · MAVİ KÜRE tek başına — çentik ve çizikler okunur
⛔ Sondanın hiçbir yüzeyinde harf, sayı, arma ya da bayrak YOK — bu dünyanın kuralı
   (novum: bu medeniyet yazmaz) ve aynı zamanda D138.
⛔ Küre KORDONLA ASILMAZ. Panelde kürenin yanında kayış, kordon, klips 0 kare
   [D172 + T1 · THE_COUNTED_TURN'ün 11 blokajından 8'i el ↔ küçük metal/cam kaynaşması].
```
```
KABUL SINAVI (R3) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de mineral yama sayısı TAM ÜÇ · ızgara slot dizisi düzenli ve okunur ·
              p3'te küre üstünde çentik 1 ve çizikler var · hiçbir panelde harf 0
  RET:        yüzeyde herhangi bir yazı/arma; kürenin yanında kordon/kayış; kürenin
              kenarında hale; ikinci bir makine
  YABANCI GÖZ: p1'i hiç okumamış birine göster · soru: "bu şey tamir edilmiş mi?"
              · doğru cevap: "evet — üç paneli başka bir malzemeyle kapatılmış"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · K17-K24 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R4 · ŞEHİR + GEÇİT + SALON
```
Photorealistic architectural still, 35mm film grain, deep focus, even neutral key light
with soft fill.

No people in the frame. A city of black basalt towers rises straight out of bare black
rock, each tower built in ribbed courses, the tallest of them running out of the top of
the frame. Long bridges cross between them, their decks carrying a warm orange-gold
band of light along the whole span. In the foreground a narrow passage is cut through
black rock and opens out toward the towers, its stone arch mouth three times the height
of a human figure. At the base of the nearest tower a black doorway is cut into the
rock, square and unlit. A plain grey scale bar shape of a human-figure silhouette
stands at the foot of the arch for proportion. Above the skyline a ringed giant planet
sits low over a straight black horizon, its ring a thin bright line, the planet as wide
as a palm held at arm's length. Low mist sits in the hollows of the rock and does not
rise.

NEGATIVE: No readable text, letters, digits or symbols on any surface — no signs, no
labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no
watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no
airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps
visible texture. No windows lit in rows, no vehicles, no aircraft, no crowd and no
standing shapes anywhere. No halo, no light shafts, no lens flare and no corona around
any lit surface.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: ⏳ K13'ten önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · GEÇİT AĞZI — kemer yüksekliği + ölçek şahidi (silüet)
               p2 · KULE DİBİ, ZEMİNDEN — kule kadrajı aşıyor, köprüde akan ışık bandı
               p3 · SALON — iki sıra yuva, yakın ÜÇÜ okunur, derinlik IŞIKSIZ
⛔ "yüzlerce yuva" HİÇBİR PANELDE YAZILMAZ (KART 13): model saymaz, doldurur.
   p3'te derinlik ışıksız olmak ZORUNDA — sayı fiziksel olarak okunamaz.
⛔ Köprüdeki ışık NOKTA dizisi olarak değil AKAN BANT olarak yazılır: 18 mm'de
   uzak bandın ince tekrar eden öğesi okunmaz ve model onu titreyen bir dizi yapar.
⛔ Metre prompt gövdesine GİRMEZ [D138]: ölçek her panelde bir SABİT ŞAHİDE bağlı
   (kemer ağzı = 3 gövde boyu · kule kadrajı aşar · yuva = göğüs yüksekliği).
```
```
KABUL SINAVI (R4) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de kemer ağzı = silüetin 3 katı · p2'de kule kadrajın üst kenarından
              ÇIKIYOR · p3'te okunur yuva sayısı TAM ÜÇ ve dördüncüsü karanlıkta
  RET:        herhangi bir panelde sıra sıra aydınlatılmış pencere; araç; kalabalık;
              köprüde titreyen nokta dizisi; herhangi bir yüzeyde yazı
  YABANCI GÖZ: p2'yi hiç okumamış birine göster · soru: "bu kule ne kadar yüksek?"
              · doğru cevap: "bilmiyorum — kadraja sığmıyor"  ⛔ bir sayı söylerse RET
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · K13 · K14 · K15 · K16 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R5 · YUVA + YATAK + ÇEKİRDEK
```
Photorealistic product-style still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill, deep focus.

No people in the frame. An upright cradle frame of dark worked metal stands alone, its
uprights chest high to a human figure and joined by two horizontal rails, the whole
frame dry and dusted with fine grey grit. At the centre of its lower rail a round
machined bed a hand's breadth across is sunk into the metal, cold and dark, a film of
grey dust lying in it, its inner wall cut with a fine thread. Around the rim of the
bed a narrow ring of the same metal is set flush. Beside the frame, lying alone on the
backdrop, a short dark cylinder the length of a forearm has two knurled rings at its
near end and a plain rounded cap at the other, its surface matte and scored with fine
use marks.

NEGATIVE: No readable text, letters, digits or symbols on any surface — no labels, no
captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark.
Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy
texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No
cable, no hose, no connector and no second cylinder. No halo, no light shafts, no lens
flare and no corona around the metal.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 K17'den önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · YUVA ÇERÇEVESİ tam — ölü hâl (K17) ve uyanmış hâl (K21) ayrı iki
                    kare, kadraj metni BİREBİR aynı (durum çifti)
               p2 · YATAK CU — yuvanın içi, diş, toz filmi
               p3 · ÇEKİRDEK tek başına — iki tırtıllı halka, kullanım izleri
⛔ p1'in UYANMIŞ karesinde ışık METALİN İÇİNDE kalır: hava taşmaz, hale yok, hüzme
   yok. Pozitif kural: "the light stays inside the metal and does not spread past it."
⛔ Çekirdeğin yanında kablo, hortum ya da konektör 0 kare — söküm klibinin (K20)
   riski tam bu sınıftır [D172 + T1].
```
```
KABUL SINAVI (R5) — dört alan ZORUNLU [D144]:
  KABUL:      p2'de yatağın DİŞİ ve TOZ FİLMİ okunuyor (çekirdeğin ilk bastırmada
              tutmaması buradan doğar) · p3'te halka sayısı TAM İKİ · p1'in uyanmış
              karesinde ışık metalin kenarını GEÇMİYOR
  RET:        yatakta ışık varken hale/hüzme; çekirdekte üçüncü halka; kablo/hortum;
              herhangi bir yüzeyde yazı
  YABANCI GÖZ: p2'yi hiç okumamış birine göster · soru: "buraya bir şey oturur mu?"
              · doğru cevap: "evet — yuvarlak bir şey, vidalanarak"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · K17 · K19 · K20 · K21 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R6 · KIRIK CAM PARÇASI
```
Photorealistic macro still, 35mm film grain, plain neutral mid-grey seamless backdrop,
even neutral key light with soft fill, deep focus.

No people in the frame. A single broken piece of dark blue glass the width of two
fingers lies alone on the backdrop, one edge sharp and freshly fractured with a clean
conchoidal face, the other edges dull and rounded from long handling. Its surface is
crossed by fine scratches and its body is the same deep blue all the way through, dark
and not transparent. Beside it, at the same distance from the lens, a large open hand
of dark mineral skin lies palm up, matte and lightly crazed like cooled basalt, four
equal digits, no claws and no nails, fine grey dust in the creases, and the broken
piece sits at the centre of that palm in the second frame of this pair.

NEGATIVE: No readable text, letters, digits or symbols on any surface — no labels, no
captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark.
Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy
texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No
second piece, no shards scattered around, no cord and no strap anywhere near the hand.
No halo, no light shafts, no lens flare and no corona around the glass.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 K10'dan önce   PANEL: 2   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · PARÇA tek başına — keskin kenar, kırık yüzeyi, çizikler
               p2 · PARÇA AVUÇTA — kadrajın merkezinde, avuç kadrajı aşıyor
⛔ Parça KAVRANMAZ, avuçta DURUR. Elin nesneyi tutup çevirmesi 0 kare.
⛔ Cam KAYNAK DEĞİLDİR: kendi mavisi RENKTİR, ışık yaymaz. Bu, O1 (bütün küre) ile
   birebir aynı malzeme kuralıdır — ikisi de ışık vermez, ikisi de TON verir.
   ⚙️ 28.09.2026 DÜZELTME: 05_SAHNE_CALISMALARI/K10_NOVUM.md'nin IŞIK satırı "camın
   KENDİ mavisi" diyordu; bu, K01/K09/K11/K23/K24'te aynı kürenin ışık vermemesiyle
   çelişiyordu (⑥ ekipman aynılığı). Kural tek: cam ışık vermez.
```
```
KABUL SINAVI (R6) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de keskin kenar TEK ve kırık yüzeyi okunuyor · parçanın rengi
              içten içe aynı koyu mavi · p2'de parça avucun merkezinde ve ≥1/4 kadraj
  RET:        ikinci bir parça; etrafa saçılmış kırıklar; camın kenarında hale;
              parçayı kavrayan parmaklar; kordon/kayış
  YABANCI GÖZ: p2'yi hiç okumamış birine göster · soru: "bu el bu şeye ne yapıyor?"
              · doğru cevap: "saklıyor / taşıyor"  ⛔ "eziyor / kırıyor" cevabı RET
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · K10 ÜRETİLMEZ ve TON KANALI
              iptal kapısı devreye girer — Plan B: tanıma K17'ye taşınır)
  ⑲ KİMLİK YIĞINI: 0 (insan yok)
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_SIGNAL_KEEPERS_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
□ ① PANEL ARİTMETİĞİ  §1 künye toplamı 19 = §2 tablo toplamı 19  ✅ yazıldı, panel ⬜
□ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te VAR ✅ · YETİM sayfa 0 ✅ ·
                      sayfasız varlık 2 (M4 · M5) ve gerekçesi §3'te YAZILI ✅
□ ③ 120 PX TESTİ      R1 p1: figürün silueti (uzun-ince + küçük düz baş) ·
                      R2 p1: kırık beyaz gövde ile koyu eklem koruması ayrımı ·
                      R3 p3: kürenin koyu mavi lekesi                      ⬜ ölçüm
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]  ⬜ ölçüm
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                      + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146]         ⬜ ölçüm
□ ⑥ D79/D139 SIRT     R2 p3: sırt çıkıntı sayısı 0 AMA yüzey POZİTİF tarifli ⬜ ölçüm
□ ⑦ D69 KLON          tek kişi istenen panelde (R2) figür sayısı = 1          ⬜ ölçüm
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — R2'nin ayrımı DEĞER olmak
                      zorunda (kırık beyaz gövde ↔ siyah bazalt); renge dayanırsa RET
□ ⑧ DURUM ÇİFTİ       iki çift (M1 R5 p1 · O1 R3) aynı kadraj · aynı ışık · ±%3 ⬜ ölçüm
□ ⑨ ⑲ KİMLİK YIĞINI   altı promptun altısında kişi başına öznitelik 0 ✅ yazıldı
□ ⑩ ⑳b DEĞİŞİM        hiçbir referans promptu değişimin SONRASINI yazmıyor ✅ yazıldı
                      (durum çiftleri AYRI panellerde, tek panelde iki durum yok)
□ ⑪ ÖLÇEK ŞAHİDİ      R1 p1 ve R4 p1'de insan silueti kadrajda ✅ yazıldı
□ ⑫ SEED / SHA KAYDI  hangi panel hangi seed ve özet — §2 tablosuna ⬜ YAZILACAK
□ ⑬ BAYT AYNILIĞI ⚙️  R2'nin kimlik bloğu ile bölüm promptlarının kimlik dizisi
                      `diff` temiz mi — ⬜ ölçüm (dört öznitelik, aynı sıra)
□ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ⬜ (⑯ ⑮ ⑲ D79)
⛔ Bu on dört madde işaretlenmeden ilk klip ÜRETİLMEZ.
⛔ ⭐ İLK KABUL SATIRI K21'dir: R2 ve R5 onaylanmadan hiçbir klip üretilmez;
  K21 kabul edilmezse ikinci klip üretilmez [üretim defteri §4].
```

## 8. ⬜ BEKLİYOR — üretim randevuları
```
⬜ Altı sayfanın altısı TASLAK: hiçbiri henüz üretilmedi (0 kare)
⬜ Seed ve SHA-256 sütunları boş — ilk üretim koşusunda doldurulur
⬜ Kabul kapısının 9 maddesi ⬜ ölçüm: panel üretilmeden ölçülemez
⬜ Kırpım ↔ tam sayfa yükleme biçimi A-B denemesi (§5'in ölçüm randevusu)
⬜ Flow'da `@R1` etiket çağrısının çalıştığı SINANMADI [D142 kalıbı]
```
