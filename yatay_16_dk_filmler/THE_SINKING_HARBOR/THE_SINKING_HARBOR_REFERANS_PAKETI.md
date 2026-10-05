# 🧷 THE_SINKING_HARBOR — REFERANS PAKETİ

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
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: V1 V2 V3
   92/92 klipte kask KAPALI; üç kişiyi ayıran tek kanal GİYSİ GEOMETRİSİ
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: K1
   "koyu katman" sözle yazılabilir ama ÇİZDİRİLEMEZ — ahtapot/doku/su daveti
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: A1 Y1 S1
   28 m gemi · 48 km liman · 3 km sonda — üçü AYNI kadrajda (K57 · K93)
☑ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: K1
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: Y2
   kolon söndürme olayı 6 → 5 → 4 → 3 → 2 → 1 → 0, yedi klipte sayılır
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: K1 S2
   K1 on dört klipte döner; S2 (bilezik) beş klipte ECU'da
⭐ ALTI TETİKLEYİCİNİN ALTISI DA DOĞRU. 0.5'in 4. sorusu "ANALİZ KARAR VERSİN"
   idi; ölçüm sonucu PAKET YAZILIR ve KAPI 0 olur [02_KONSEPT §5b].
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_SINKING_HARBOR          FORMAT: yatay 16 dk   ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 3840 × 2160   SAHNE SAYISI: 24 (92 klip)
SAYFA: 7   TOPLAM PANEL: 28   ARİTMETİK: 7 sayfa × 4 panel = 28

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: referans sayfaları → DORUK S21 → merkezî seçim S12 → kapanış S24 → S01 → kalanı

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | GİYSİ VE KASK | 4 | V1 V2 V3 · vizör · sırt | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R2 | KOYU KATMAN | 4 | K1 dört durumu · K2 | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R3 | SONDA BOYNU | 4 | S1 S2 S3 · gerilen kıvrım | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R4 | LİMAN GÖVDESİ | 4 | Y1 Y2 · eğim · 1H şahidi | 🟠 S02'den önce | | | ⬜ TASLAK |
| R5 | GEMİ | 4 | A1 · yuva halkası · kenet | 🟠 S02'den önce | | | ⬜ TASLAK |
| R6 | MEKANİK TAKIM | 4 | P1 P2 P3 P4 | 🟠 S18'den önce | | | ⬜ TASLAK |
| R7 | İÇ HACİMLER | 4 | M1 M2 M3 | ⏳ sonra | | | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
PANEL TOPLAMI: 4+4+4+4+4+4+4 = 28 — §1 künyesiyle EŞİT ✅ (kabul kapısı ①)
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanır.
⛔ R1 · R2 · R3 ONAYLI olmadan HİÇBİR klip üretilmez: üçü de 🔴, çünkü üçü de
   film boyunca dönüyor (V 63 klip · K1 14 klip · S1-S2 11 klip).
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| V1 | inci beyazı seramik plakalı basınç giysisi | insan | S02 | S24 | R1 | 🔴 vizör + sırt ünitesi |
| V2 | kobalt yakalı beyaz panelli basınç giysisi | insan | S02 | S24 | R1 | 🔴 vizör + sırt ünitesi |
| V3 | bakır kuplajlı saten beyaz ağır iş kabuğu | insan | S03 | S24 | R1 | 🔴 vizör + sırt + diz desteği |
| K1 | koyu katman | canlı | S06 | S24 | R2 | 🔴 ahtapot/doku/su daveti |
| K2 | soluk damar örüntüsü | canlı | S11 | S24 | R2 | 🔴 kök/sinir/damar benzetmesi |
| S1 | sonda boynu (3 km, kadrajda üst bölüm) | araç | S09 | S21 | R3 | 🟠 ölçek kayması |
| S2 | işlenmiş metal bilezik | prop | S09 | S10 | R3 | 🟠 ECU'da biçim sapması |
| S3 | bağlantı gövdesi (×3) | prop | S16 | S21 | R3 | 🟡 sayı kayması (3 → 4) |
| Y1 | liman gövdesi (48 km) | mekân | S02 | S24 | R4 | 🔴 oyuncak-maket okuması |
| Y2 | kolon (sert beyaz ışık sütunu) | olay | S02 | S24 | R4 | 🟠 sayı kayması (6→0) |
| A1 | gemi (28 m) | araç | S02 | S24 | R5 | 🟠 oran kayması |
| A2 | yuva halkası + dört kenet | mekân | S03 | S23 | R5 | 🟡 kenet sayısı |
| P1 | pim | prop | S16 | S21 | R6 | 🟡 ECU biçim |
| P2 | yuva (eğilmiş ağız) | prop | S18 | S21 | R6 | 🔴 "eğilmiş" okunmuyor |
| P3 | kriko (sarı krank) | prop | S13 | S19 | R6 | 🟡 renk tek ayrım olmasın |
| P4 | boşaltma kolu | prop | S16 | S21 | R6 | 🟡 — |
| M1 | kontrol odası paneli (işaretsiz) | mekân | S08 | S12 | R7 | 🔴 metin/ölçek daveti |
| M2 | kare pencere (dört cıvatalı segment) | mekân | S07 | S22 | R7 | 🟠 dış yüzde kondensasyon |
| M3 | kokpit (üç koltuk) | mekân | S02 | S24 | R7 | 🟡 — |
```
⛔ KOD kullanılır, AD kullanılmaz [D34]. Filmde HİÇBİR özel ad geçmez
   (ne prompt ne replik) — sahibin planındaki adlar PLAN'da kalır [02_KONSEPT §1].
⛔ Risk sınıfı `ASTRONOT_DONANIM` eşya tablosundan alınır.
YETİM SAYFA: 0 — on dokuz kodun on dokuzu §5'te çağrılıyor (kabul kapısı ②).
ÇAPASIZ VARLIK: 0 — envanterdeki her kodun bir sayfası var.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| K1 | K0 (yok) | kadrajda değil | S01 | S06 | — |
| K1 | K1 KABUK | yalnız bir YÜZEY: mat, parlamasız, kenarı var | S06 | S09 | R2 p1 |
| K1 | K2 PARÇA | bir KIVRIM bileziğin üstünde gerilir | S09 | S11 | R2 p2 |
| K1 | K3 ÖRÜNTÜ | bulutun içinde soluk damarlar (K2) | S11 | S20 | R2 p3 |
| K1 | K4 BÜTÜN ÖRÜNTÜ | nabız ilerler, sonda AYNI ritimde cevap verir | S20 | — | R2 p4 |
| Y2 | K0 | altı kolon yanıyor | S02 | S07 | R4 p2 |
| Y2 | K1 | bir kolon kırılır ve titrer | S07 | S24 | R4 p2 |
| P2 | K0 | yuva ağzı YUVARLAK | S16 | S18 | R6 p2 |
| P2 | K1 | ağız BİR YANDAN içe basılmış (eğik) | S18 | S21 | R6 p2 |
| P2 | K2 | ağız yeniden yuvarlak, pim serbest | S21 | — | R6 p2 |
```
⛔ MERDİVEN TEK YÖNLÜDÜR. ⚠️ P2 K1 → K2 GERİ DÖNÜŞ GİBİ GÖRÜNÜR ve gerekçesi
   şudur: yuva kendi kendine düzelmiyor, KRİKO onu açıyor (S19 · K74-K76).
   Yani K2 bir geri dönüş değil, ÜÇÜNCÜ bir durum: "zorla açılmış yuva" —
   eski bası izi (grey band) şankta KALIR ve K82'de hâlâ görünür [D147 · D84].
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK.
   R2 p1↔p2 ve R6 p2'nin üç hâli bu kuralla çekilir (±%3 en).
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişkidir. Bu dosyanın
   seçimi: **AYNI SAYFADA** (R2'nin dört paneli = K1'in dört durumu).
   GEREKÇE: K1'in durumları arasındaki FARK bu filmin novumudur; ayrı
   sayfalarda üretilirse fark ölçülemez, aynı sayfada panel panel ölçülür.
   ⛔ Bu bir KARARDIR, ölçüm değil — QA'da sınanacak [⬜ üretim sonrası].

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01 | dış · kubbe 6/6 | R4 p1 · R5 p1 | liman + gemi | K0 | geminin yaklaşma hızı |
| S02 | iç kokpit · amber | R1 p4 · R7 p3 | yüz + üç koltuk | K0 | boş koltuğun BOŞLUĞU |
| S03 | dış yuva · sert beyaz | R5 p3 · R1 p2 | kenet + siluet | K0 | kenedin kapanmamışlığı |
| S04 | iç koridor · tavan beyazı | R1 p1 · R7 p1 | üç giysi + panel | K0 | kapalı kapının ardı |
| S05 | iç tünel · kısık beyaz | R6 p3 · R1 p3 | kriko + sırt | K0 | sıkışmış bacağın yönü |
| S06 | dış yuva · alçak amber | R2 p1 · R5 p3 | KABUK + halka | K1 | yüzeyin BİR KEZ kıpırdaması |
| S07 | iç oda · kırmızı alarm | R7 p1 · R7 p2 · R4 p2 | panel + pencere + kolon | K1 | alarmın ritmi |
| S08 | iç oda · iki tavan lambası | R7 p1 · R1 p4 | panel + yüz | K1 | iki eğrinin ANLAMI |
| S09 | sonda kamerası · tek lamba | R3 p2 · R2 p2 | bilezik + kıvrım | K2 | kıvrımın gerilme HIZI |
| S10 | sonda kamerası · ilk amber | R3 p2 · R2 p2 | bilezik + kıvrım | K2 | gevşemenin SEBEBİ |
| S11 | gezegen + oda · geniş amber | R2 p3 · R1 p4 | damarlar + yüz | K3 | ölçeğin ŞOKU |
| S12 | iç oda · alttan amber | R7 p1 · R1 p4 | panel + iki yüz | K3 | cevapsız kalan emir |
| S13 | iç koridor + gemi · düz beyaz | R1 p1 · R6 p3 · R7 p1 | üç giysi + kriko | K3 | dönüş yolunun TANIDIKLIĞI |
| S14 | iç gemi · 4500 K beyaz | R7 p3 · R1 p3 | kokpit + sırt | K3 | görev bölünmesinin riski |
| S15 | dış yol · alttan amber | R4 p3 · R1 p1 · R6 p3 | kaburga + figür + kriko | K3 | yapının BÜYÜKLÜĞÜ |
| S16 | dış yol · sis | R4 p3 · R3 p3 | kaburga + bağlantı | K3 | sisin KURULUĞU |
| S17 | dış yol + gemi · amber | R4 p4 · R1 p2 | kopan kesim + siluet | K3 | düşmenin SÜRESİ [D127] |
| S18 | dış · amber baskın | R4 p4 · R6 p2 | eğim + yuva | K3 | eğimin GERİ DÖNMEZLİĞİ |
| S19 | dış platform + pencere | R6 p2 · R6 p3 · R7 p2 | yuva + kriko + pencere | K3 | krankın AĞIRLIĞI |
| S20 | dış + yüz + pencere · amber | R2 p4 · R1 p4 · R7 p2 | nabız + yüz + pencere | K4 | buğunun zamanı |
| S21 | dış · gevşeyen amber | R6 p1 · R2 p4 · R3 p1 | pim + katman + boyun | K4 | bırakmanın KENDİLİĞİ |
| S22 | dış + gemi · amber + beyaz | R4 p4 · R5 p2 | boşluk + gemi yanı | K4 | geçişin tek şansı |
| S23 | iç gemi + yuva · beyaz | R7 p3 · R5 p3 | kokpit + kenet | K4 | dört açılmanın SIRASI |
| S24 | dış + kokpit · açılan kubbe | R5 p1 · R4 p1 · R2 p3 · R7 p3 | gemi + liman + damar + kokpit | K4 | açık avucun ANLAMI |
```
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2).
   ⚠️ İHLAL: S07 (3 ✅) · S13 (3 ✅) · S15 (3 ✅) · S19 (3 ✅) · S20 (3 ✅) ·
   S21 (3 ✅) · **S24 (4 ⛔)**. S24'ün kararı: R7 p3 METNE DEVREDİLİR —
   kokpit iç hacmi K96'da zaten R5+R4+R2 ile aynı kadrajda değil, ayrı klipte
   (K96). Klip bazında yükleme: K93 → R5 p1 · K94 → R4 p1 · K95 → R2 p3 ·
   K96 → R7 p3 + R1 p3. Yani sahne satırı 4 gösteriyor, KLİP başına en çok 2.
   ⭐ Bu ayrım çok klipli rejimin getirdiği yeni bir durumdur: §5'in "sahne"
   birimi ile yükleme birimi (KLİP) artık aynı değil [04_UYARI §4a aday 22].
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   Bu dosyanın seçtiği yükleme biçimi: **KIRPIM**.
   GEREKÇE: tam sayfa yüklenince nötr gri fon da girdi oluyor ve dört eski
   paketin üçünde sahne arka planı griye kayma riski QA'da not edilmiş;
   ⚠️ iddia ÖLÇÜLMEDİ, bu film de ölçmeyecek (üretim 0 kare) — karar
   kılavuzun yazılı tercihine uyar, ölçüme değil [D74 kaydı].
· Flow çağırma: `@R1` … `@R7` — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun kopyasıdır.
```

## 6. 📸 REFERANS SAYFALARI
> ⛔ **İngilizce prompt BAŞLIKTAN SONRAKİ İLK çitli bloktur.**
> Künye ve kabul sınavı promptun ALTINA yazılır.

### 📸 IMAGE PROMPT — SAYFA R1 · GİYSİ VE KASK (V1 · V2 · V3)
```
IN FRAME: face · torso · hands · back
Reference page 1 of 7.
Photorealistic full-length still, 35mm film grain, plain mid-grey seamless backdrop,
even neutral key light with soft fill.

Exactly three human characters in a row facing the lens, each sealed in a hard pressure
suit, no clones and no fourth person. Left: pearl-white
ceramic plating, champagne-gold lines along every joint. Middle: white technical
pressure panelling, cobalt collar trim. Right: satin white heavy work shell, copper
shoulder couplings, a dark brace over the left knee, edges worn to bare grey in three
places. Each chest carries one shape raised in the material itself, no colour difference
and no marking on it: three wings, a rectangular grid, a circle.

Every helmet is a closed white hard shell with one curved clear pane held in a visible
dark rim. The glass is optically clear with zero tint, zero mirror coating and zero
reflection, each face fully readable at every head angle, with one thin specular line
along the pane's upper edge only. Each collar seal ring is visible.

The back of every suit is one continuous smooth panel from collar to hip, carrying
nothing — a flat back silhouette with a single vertical seam down its centre and no
housing, no pack, no tank and no hose. Gloves and boots are plain, each cuff matching
its own suit's trim.

NEGATIVE: Exactly 3 human characters in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · üçü yan yana 3/4 tam boy — ölçek, duruş, göğüs geometrisi farkı
               p2 · profil, tek giysi — siluet hattı ve omuz kaburgası
               p3 · SIRT, tek giysi — düz siluet, tek dikey dikiş [D79/D139]
               p4 · vizör ardı yüz CU — her kafa açısında okunur [D146]
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — p3 sırta ne KOYULACAĞINI söyler:
   tek dikey dikiş + omuz kaburgası. Yasak değil MALZEME [D123 · D139].
⭐ Üç göğüs şekli KABARTMADIR, rozet DEĞİL: sahibin "rozet" isteği buraya
   böyle indi, çünkü okunabilir arma D45/D138 ile çatışıyor [02_KONSEPT §1].
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      üç giysi GRİ TONDA bile ayırt edilebiliyor (göğüs şekli: üç kanat / dikdörtgen ızgara / daire)
  RET:        vizörde tek yansıma · sırtta tek çıkıntı · göğüste tek harf veya rakam · kubbe vizör
  YABANCI GÖZ: paneli hiç okumamış biri · soru: hangi giysi en ağır işi yapıyor · doğru cevap: sağdaki (bakır kuplaj + yıpranma + diz desteği)
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 3 (giysi · kask · eldiven — ten/saç/yaş YAZILMADI)
```

### 📸 IMAGE PROMPT — SAYFA R2 · KOYU KATMAN (K1) VE DAMAR ÖRÜNTÜSÜ (K2)
```
IN FRAME: none
Reference page 2 of 7.
Photorealistic still, 35mm film grain, no backdrop — the subject fills the frame.

A single vast dark surface, matt and even, with no highlight anywhere on it and no
pattern printed on it. It is one unbroken sheet, not a body: it has no limbs, no arms,
no head, no eyes, no mouth and no face, and nothing on it is paired or symmetrical. Its
edge is a clean soft line where it meets the light behind it, and along that edge it
carries long slow folds that each run out of frame without ending. The folds are of
different lengths and none of them repeats another's curve.

Behind and below the surface, broad soft amber cloud belts fill the rest of the frame
with zero hard edge in them. Inside those belts a pattern of long pale veins runs in
slow curves, branching and rejoining, each vein a little brighter than the cloud it
lies in. The veins are smooth-walled and even in width, with no root tips, no hairs, no
bundles and no membrane between them, and no two branches meet at the same angle.

Nothing in the frame is wet, nothing is translucent and nothing has suckers, scales,
chitin, fur or skin texture of any kind. The surface is as dry as sheet metal and as
matt as soot.

NEGATIVE: Exactly 0 human characters in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · K1 KABUK — yalnız yüzey ve kenar, kadrajın üçte ikisi
               p2 · K2 PARÇA — bir kıvrım soluk metal bileziğin ÜSTÜNDE gerilmiş
               p3 · K3 ÖRÜNTÜ — bulutun içinde damar ağı, geniş plan
               p4 · K4 BÜTÜN ÖRÜNTÜ — damarlarda ilerleyen parlama + yük alan boyun
⛔ göz · yüz · ağız kelimeleri promptta HİÇ ANILMAZ — ne pozitif ne negatif
   [D123]. Yukarıdaki promptta geçiyorlar çünkü bu bir REFERANS sayfasıdır,
   sahne promptu değil: burada yokluk listesi biçimi TUTAR, 10 s klipte tutmaz.
⭐ D56 (MEDIUM LOCK) bu sayfanın tek amacı: "katman" kelimesi modelde SU
   üretiyor. "as dry as sheet metal and as matt as soot" ölçülebilir çapadır.
```
```
KABUL SINAVI (R2) — dört alan ZORUNLU [D144]:
  KABUL:      yabancı göz "bu nedir" sorusuna CANLI demiyor ama HAREKET EDİYOR diyor
  RET:        kol · uzuv · göz · ağız · emme çanağı · pul · kürk · ıslaklık · simetri · ahtapot okuması
  YABANCI GÖZ: paneli hiç okumamış biri · soru: bu yüzeyin kaç tarafı var · doğru cevap: "belli değil / bir tane" (⛔ "iki yanı" cevabı simetri kaçağıdır, panel reddedilir)
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R3 · SONDA BOYNU (S1) · BİLEZİK (S2) · BAĞLANTI GÖVDESİ (S3)
```
IN FRAME: full body
Reference page 3 of 7.
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, even
neutral key light with soft fill.

A smooth pale machined column stands upright in the frame, its surface finely turned in
close parallel rings so the light breaks along it in fine even lines. Around its base,
three heavy link bodies are set at equal spacing, each one about a seventh of the
column's height, each with a knurled collar and a jaw that closes on the column; two of
them stand square to the column's axis and the third leans about twelve degrees out of
line, with a visible wedge of shadow opening at one side of its base.

Part way up the column, a separate smooth collar ring is fitted, wider than the column
and finely turned on its outer face, its rim a clean square edge. A single suited figure
in a white hard pressure suit and closed helmet stands beside the column for scale,
reaching to about a fifth of its height.

Every surface is bare machined metal or matt white. There is no marking of any kind on
the column, the collar, the link bodies or the ground.

NEGATIVE: Exactly 1 human character in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · tam boy + 1H ölçek şahidi (kasklı gövde kadrajda)
               p2 · bilezik ECU — işlenmiş yüzey ve rim keskinliği
               p3 · üç bağlantı gövdesi — biri 12° eğik, gölge kaması
               p4 · bilezik + ÜSTÜNE gerilmiş koyu kıvrım (R2 p2 ile EŞ KADRAJ)
⛔ 120 PX TESTİ bu sayfada ZORUNLU: K63 ve K83 bu üçlüyü 36 m'lik kadrajda
   203 px figürle gösteriyor; eğiklik orada okunmazsa S16 ve S21 ÜRETİLMEZ.
⭐ p4, R2 p2 ile AYNI kadraj · AYNI ışık yönü · ±%3 en olmak ZORUNDA —
   novumun tek kanıtı bu iki panelin FARKI [§4 durum çifti].
```
```
KABUL SINAVI (R3) — dört alan ZORUNLU [D144]:
  KABUL:      üç bağlantı gövdesi tek karede SAYILABİLİYOR ve eğik olan 120 px'te bile belli
  RET:        dört bağlantı · eğikliğin kaybolması · bilezikte harf/çizik deseni · kolonun silindir olmaktan çıkması
  YABANCI GÖZ: paneli hiç okumamış biri · soru: üç parçadan hangisi bozuk · doğru cevap: eğik olan (gölge kaması tek yanda)
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 1 (giysi — yalnız ölçek şahidi)
```

### 📸 IMAGE PROMPT — SAYFA R4 · LİMAN GÖVDESİ (Y1) VE KOLON (Y2)
```
IN FRAME: full body
Reference page 4 of 7.
Photorealistic still, 35mm film grain, no backdrop — the structure and the cloud fill
the frame.

An enormous black structure lies across the frame, built as a long run of heavy
repeating ribs with a flat pressurised hull skin between them, its two ends running out
of the frame on both sides. The ribs are of one depth all the way along and the hull
skin is matt with visible plate texture, every plate the same size. The far end of the
structure is as sharp as the near end.

From the structure's underside, six slender columns of hard white light stand straight
down into the cloud below, evenly spaced, each one a clean parallel-sided shaft with no
flare and no halo around it. Below them, broad soft amber cloud belts fill the lower
half of the frame with zero hard edge in them, no ground and no horizon anywhere. Above
the structure, a bright sourceless dome of pale cloud with no sun disc in it.

One tiny suited figure in a white pressure suit stands on an open walkway at the
structure's near edge, about a six-hundredth of the structure's length, for scale.

NEGATIVE: Exactly 1 human character in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🟠 S02'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · bütün gövde + 1H şahidi — 48 km oranı
               p2 · altı kolon, eşit aralık — sayı kilidi (6→5→4→3→2→1→0)
               p3 · kaburga altı bakım yolu — figür 108 px ölçeğinde
               p4 · kopan 18 m'lik döşeme kesimi — iki yırtık uç
⛔ UZAY_USSU §1: ölçek SÖZLE yazılamaz, ŞAHİTLE yazılır. p1 ve p3'te 1H
   (kasklı gövde, 1,90 m) kadrajda OLMAK ZORUNDA.
⭐ Y2'nin sayısı filmin sayacıdır: 6/6 → 0/6 yedi klipte. p2 bu sayımın
   okunabilirlik çapasıdır — kolonlar EŞİT aralıklı, yoksa eksik sayılamaz.
```
```
KABUL SINAVI (R4) — dört alan ZORUNLU [D144]:
  KABUL:      figür kadrajda ve gövde oyuncak-maket OKUNMUYOR (kabul kapısı ⑦b gri tonda da)
  RET:        tilt-shift bulanıklık bandı · kolonlarda halo · kaburga derinliğinin değişmesi · ufuk çizgisi
  YABANCI GÖZ: paneli hiç okumamış biri · soru: bu yapı ne kadar büyük · doğru cevap: "bir şehir kadar / kilometrelerce" (⛔ "bir gemi kadar" cevabı oran kaybıdır)
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 1 (giysi — yalnız ölçek şahidi)
```

### 📸 IMAGE PROMPT — SAYFA R5 · GEMİ (A1) VE YUVA HALKASI (A2)
```
IN FRAME: full body
Reference page 5 of 7.
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, even
neutral key light with soft fill.

A white hulled ship about the length of eight standing people, its nose facing screen-right and seen three-quarter front.
Its hull is a single smooth pressurised form with a blunt nose, a flat underside and two
short fixed fins at the stern; the plating is matt white with visible plate texture and
three panels on the flank are worn to bare grey at their edges. A square window with a
heavy dark frame of four bolted segments is set into the flank, and a round hatch with a
visible dark seal ring is set behind it. The ship carries no marking of any kind on any
surface.

Behind it stands a heavy pale structural collar, a ring wide enough for the ship to sit
inside, with four large clamps spaced around it. Each clamp is a jaw of bare grey metal
on a short arm, and all four stand open with their jaws clear of the hull by about a
hand's width, bare metal showing inside every one.

One suited figure in a white pressure suit and closed helmet stands on the ring for
scale, reaching about a tenth of the ship's length.

NEGATIVE: Exactly 1 human character in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🟠 S02'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 ön tam gövde + 1H şahidi — 28 m oranı
               p2 · yan görünüm — pencere ve kapak konumu, yıpranma yerleri
               p3 · yuva halkası + DÖRT kenet, hepsi AÇIK — sayı kilidi
               p4 · aynı halka, DÖRT kenet KAPALI — durum çifti (±%3 en)
⛔ p3 ↔ p4 DURUM ÇİFTİDİR: aynı kadraj, aynı ışık yönü, aynı mesafe, TEK
   FARK kenetlerin hâli. K07 (D02 "dört kenet hazır") · K20 (D06 "kenetler
   kıpırdamıyor") · K92 (dört kenet GERÇEKTEN açılır) üçü de buradan beslenir.
```
```
KABUL SINAVI (R5) — dört alan ZORUNLU [D144]:
  KABUL:      dört kenet tek karede sayılabiliyor ve açık/kapalı farkı 120 px'te belli
  RET:        beş kenet · gövdede harf veya numara · burun biçiminin değişmesi · kanat eklenmesi
  YABANCI GÖZ: paneli hiç okumamış biri · soru: gemi yuvaya bağlı mı · doğru cevap: p3'te DEĞİL, p4'te BAĞLI
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 1 (giysi — yalnız ölçek şahidi)
```

### 📸 IMAGE PROMPT — SAYFA R6 · MEKANİK TAKIM — PİM (P1) · YUVA (P2) · KRİKO (P3) · KOL (P4)
```
IN FRAME: none
Reference page 6 of 7.
Photorealistic still, 35mm film grain, plain neutral mid-grey seamless backdrop, even
neutral key light with soft fill.

Four machined objects laid out in a row and lit the same way. First, a pale steel pin
about two palms long with a plain collar at one end and a thin lanyard loop on the
collar; its shank is smooth with one grey band of bearing wear along a single side.
Second, a dark socket block with the pin's seat bored through it, shown twice: once with
its mouth perfectly round, and once with its mouth visibly pressed in on one side so
the bore is an oval and one wall stands closer than the other. Third, a short jack body
with two flat bearing pads, a square-cut screw thread and a crank handle painted bright
yellow, the only painted surface in the frame. Fourth, a long plain release handle, a
straight bar with a cross grip and a quadrant slot at its base.

Every other surface is bare machined metal, matt and uncoated. There is no marking of
any kind on any of the four objects, and no scale bar, no ruler and no reference card
anywhere in the frame.

NEGATIVE: Exactly 0 human characters in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: 🟠 S18'den önce   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · pim tek başına — şanktaki tek gri bası izi
               p2 · yuva ÜÇ hâli: yuvarlak · bir yandan basılı · zorla açılmış
               p3 · kriko — sarı krank ve kare vida; gri tonda da ayırt edilir
               p4 · kol — çeyrek yuvası, üst/orta/alt üç konum
⛔ ⑦b GRİ TON KAPISI bu sayfada EN KRİTİK: kriko sarı kranktan ayırt
   ediliyorsa panel REDDEDİLİR — ayrım BİÇİMDE olmalı (kare vida + iki pad).
⭐ P2'nin üç hâli R6 p2'de TEK panelde yan yana: filmin on klibi (K72-K82)
   bu farkın okunmasına bağlı. Okunmazsa S18-S21 ÜRETİLMEZ.
```
```
KABUL SINAVI (R6) — dört alan ZORUNLU [D144]:
  KABUL:      yuvanın "bir yandan basılı" hâli gri tonda ve 120 px'te okunuyor
  RET:        yuva ağzının yuvarlak kalması · sarının tek ayrım olması · nesnelerde ölçü çizgisi · cetvel
  YABANCI GÖZ: paneli hiç okumamış biri · soru: bu dört parçadan hangisi hasarlı · doğru cevap: yuva (ağzı oval)
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0 (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R7 · İÇ HACİMLER — PANEL (M1) · PENCERE (M2) · KOKPİT (M3)
```
IN FRAME: 
Reference page 7 of 7.
Photorealistic still, 35mm film grain, no backdrop — the interiors fill the frame.

Three interior details of the same vessel, lit by its own even cold white panels with no
flare anywhere. First, a wide dark control panel at chest height: its face is matt and
completely blank, with no scale, no tick, no dial markings, no labels and no numbers of
any kind, carrying only a row of three short closed clamp bodies, one recessed dial and
one short slider in a plain slot. Second, a small square window set into a matt pale
wall, its pane about as wide as a pair of shoulders, held in a heavy dark frame of four
bolted segments with the bolt heads catching hard metal highlights; the pane's outer
face is completely dry and clean. Third, a cockpit with exactly three padded seats in a
row, each with a wide belt lying across its cushion, a plain console across the front
and a canopy above.

Every surface is matt white, matt dark grey or bare metal. There is no marking, no
lettering, no digit and no symbol anywhere in the frame.

NEGATIVE: Exactly 0 human characters in frame, no duplicates, no extra person. No water anywhere — no ocean, no sea, no waves, no bubbles, no splash, no spray, no wet surfaces, no coral, no fish, no diving gear. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any surface — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. No tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame.

Output: 16:9, 3840 x 2160, no text, no watermark.
```
```
ÖNCELİK: ⏳ sonra   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · kontrol odası paneli — tamamen işaretsiz yüz, üç kenet + kadran + sürgü
               p2 · pencere — dört cıvatalı segment, dış yüz KURU
               p3 · kokpit — tam ÜÇ koltuk, üç kemer
               p4 · aynı kokpit, kamera omuz üstünde (X kurulumu) — sırt yüzeyi
⛔ M1 bu filmin en yüksek METİN riski: "panel" kelimesi modelde ölçek,
   rakam ve etiket üretiyor. Negatifle değil, POZİTİF BOŞLUKLA tutulur:
   "matt and completely blank ... carrying only" [D45 · D138].
⛔ p2'nin dış yüzü KURU: ⑱ `pencere` negatifinin görsel çapası. K80'de
   buğu camın İÇİNDE birikir ve bu AYRIM üretilebilir olmalı.
```
```
KABUL SINAVI (R7) — dört alan ZORUNLU [D144]:
  KABUL:      panelin yüzünde harf · rakam · tik · kadran işareti SAYISI = 0 [D45/D138]
  RET:        ölçek çizgisi · rakam · dört koltuk · pencerenin dış yüzünde damla veya buğu
  YABANCI GÖZ: paneli hiç okumamış biri · soru: bu panelde kaç şey var · doğru cevap: üç kenet + bir kadran + bir sürgü = beş
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 0 (insan yok)
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_SINKING_HARBOR_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
☑ ① PANEL ARİTMETİĞİ  7 × 4 = 28 — §1 künyesi 28, §2 tablosu 28 ✅ EŞİT
☑ ② ÇAPRAZ BAĞ        §5'teki 24 sahnenin her kodu §3'te var · YETİM 0 ·
                      çapasız varlık 0 ✅
⬜ ③ 120 PX TESTİ      üç zorunlu öğe: ① R3'te EĞİK bağlantı ② R5'te DÖRT
                      kenedin açık/kapalı farkı ③ R6'da OVAL yuva ağzı
                      → ÜRETİMDE ÖLÇÜLÜR, tahmin yazılmadı
⬜ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 hedef [D45/D138]
⬜ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                      + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146]
⬜ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0 AMA yüzey POZİTİF tarifli (R1 p3)
⬜ ⑦ D69 KLON          R1'de figür sayısı = 3 (istenen) · R3-R5'te = 1
⬜ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — R1 (üç giysi) ve
                      R6 (sarı krank) bu testin iki kritik sayfası
☑ ⑧ DURUM ÇİFTİ       üç çift yazılı: R2 p1↔p2 · R3 p2↔p4 · R5 p3↔p4 ✅
☑ ⑨ ⑲ KİMLİK YIĞINI   R1 = 3 öznitelik · diğer altı sayfa ≤1 ✅ (tavan 3)
☑ ⑩ ⑳b DEĞİŞİM        yedi promptun yedisi DURUMU yazıyor, değişimi değil ✅
☑ ⑪ ÖLÇEK ŞAHİDİ      R3 p1 · R4 p1 · R4 p3 · R5 p1 → 1H kadrajda ✅
⬜ ⑫ SEED / SHA KAYDI  üretimde §2 tablosuna yazılır
⬜ ⑬ BAYT AYNILIĞI ⚙️  R1'in kimlik bloğu ile bölüm promptlarının giysi
                      cümleleri `diff` — ⚠️ BİLİNÇLİ FARK VAR: sahne promptu
                      üç giysinin yalnız KADRAJDAKİNİ yazar, üçünü birden
                      yazmaz. Kapı "bayt aynılığı" değil "çelişki yok" olarak
                      koşar; gerekçe burada [D74]
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: 0 BLOCK ✅
⛔ ③ ④ ⑤ ⑥ ⑦ ⑦b ⑫ ⑬ işaretlenmeden ilk klip ÜRETİLMEZ — yedisi de ÜRETİM
   anında ölçülür, bugün tahmin YAZILMADI [D124 kalıbı].
```

## 8. 🔁 DÖNGÜ — paketi GEÇERSİZ kılan şeyler [kılavuz §7.2]
```
⛔ İmaj modeli ya da sürümü değişirse → yedi sayfa GEÇERSİZ, yeniden üretilir
⛔ Veo sürümü değişirse → yükleme biçimi (kırpım) yeniden sınanır
⛔ Bir giysinin göğüs geometrisi değişirse → R1 + 63 klibin giysi cümlesi
⛔ K1'in durum merdiveni değişirse → R2 + R3 p4 + 14 klip
⚠️ QA'da biçim sapması çıkarsa sayfa GEÇERSİZ olur, sahne DEĞİL: önce panel
   yeniden üretilir, sonra o sahnenin klipleri.
```

## 9. ⬜ BEKLİYOR — bu dosyanın açık kalanları
```
☑ Tetikleyici kontrolü işaretlendi (altı tetikleyicinin ALTISI)
☑ Envanter (19 kod) · merdiven (10 satır) · eşleme (24 sahne) yazıldı
☑ Yedi sayfa bloğu yazıldı (R1-R7), yedisinin de kabul sınavı dolu
⬜ Kabul kapısının yedi maddesi ÜRETİMDE ölçülür, seed ve SHA boş
⬜ DURUM: yedi sayfanın yedisi TASLAK — hiçbiri ONAYLI değil
⛔ Bu yüzden bugün KLİP ÜRETİLEMEZ. Paket KAPI 0'dır [D168].
```
