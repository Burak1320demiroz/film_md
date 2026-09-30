# 🧷 THE_FALLING_WORLD — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK S41 → merkezî seçim S42 → kapanış S47 →
> hook S00 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR.
> ⭐ **SAHİP KARARI 18.09.2026 (birebir):** "8 9 referans değil de 4 referans gerekli
> ve hangi referansın hangi sahnede kullanıldığı yazılsın." → DÖRT sayfa, ve §5'te
> 48 satırlık tam eşleme tablosu.
>
> ⚠️ `### 📸 IMAGE PROMPT` başlığı `prompt_kontrol.py`'nin başlık desenine UYAR;
> bu dosya DOSYA modunda imaj promptu gibi denetlenir, KLASÖR modunun dizi
> kapılarına girmez. İngilizce prompt başlıktan sonraki İLK çitli bloktur.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)
     kim: BEYAZ ve TURUNCU — 48/48 sahne, vizörler TAMAMEN OPAK, yüz hiç yok
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]
     hangi: ÜÇ HAT aynı kelimeyle okunuyor — ince sarı ortak halat (S04-S47) ·
     ince gri sandık kayışı (S01-S02) · kalın siyah yer servis bağlantısı (S07·S32-S35·S38)
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE
     hangi: keşif aracı (4 m) · kaçış gemisi (8 m) · devrilmiş kafes direk (14 m / 8 bölüm)
□ T4 İNSAN DIŞI CANLI                                            hangi: — (yok)
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY
     hangi: zemin çöküşü + toz sütunu — 48 sahnenin en az 20'sinde
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR
     rapor: gemi 3 ayrı bölümde · alet 4 sahnede · sarı halat 44 sahnede ·
     KRONOS_SON_SINYAL (aynı format) iki bölümde ikinci figürü KOPYALADI
```
**5/6 tetikleyici doğru → paket YAZILIR.**

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_FALLING_WORLD          FORMAT: yatay 8 dk · 48 sahne      ORAN: 16:9
SAYFA ORANI = FİLM ORANI         ÇÖZÜNÜRLÜK: 3840 × 2160            SAHNE SAYISI: 48
SAYFA: 4   TOPLAM PANEL: 16   ARİTMETİK: 4 sayfa × 4 panel = 16
YÜKLEME BİÇİMİ: KIRPILMIŞ PANEL  ·  gerekçe: bir sahnede en çok 3 kayıt yüklenir
   (`VEO` §6 md.2); tam sayfa yüklemek dört paneli birden gönderir ve model
   yanlış paneli çapa alır. ⚠️ Dört eski paket TERSİNİ yazıyor ve iddia ÖLÇÜLMEDİ.
· Flow çağırma: `@R1` `@R2` `@R3` `@R4` — etiket KOD, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
İMAJ MODELİ + SÜRÜM: ⬜ (ilk üretim gününde yazılır)     TARİH: ⬜.⬜.2026
VİDEO: OMNI 1.1 Flash (I2V)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_FALLING_WORLD_KAPAK.md` (R1-R4 onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU
> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: R1-R4 → DORUK S41 → merkezî seçim S42 → kapanış S47 → S00 → kalan 43

| # | sayfa | panel | ne | kullanıldığı sahneler | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|---|
| R1 | BEYAZ | 4 | kirli beyaz giysi · kobalt mavi omuz · köşeli sırt kutusu · OPAK pane · sol önkolda düz alet · İKİ DURUM (K0 S00-S15 / K1 S16-S47) | 46/48 (S45 · S47 hariç) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R2 | TURUNCU | 4 | yanık turuncu giysi · siyah üst kol · dar dikdörtgen sırt ünitesi · OPAK pane · bilek kumandası · bel onarım kiti | 46/48 (S45 · S47 hariç) | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R3 | HAT AİLESİ | 4 | ince sarı ortak halat · ince gri sandık kayışı · kalın siyah servis bağlantısı · sarı halka + hızlı bağlantı · düz alet | sarı halat S04-S47 · gri kayış S01-S02 · alet S01·S02·S39·S42 · sarı halka S31·S44 · siyah bağlantı S07·S32-S35·S38 | 🔴 ZORUNLU | | | ⬜ TASLAK |
| R4 | ARAÇ VE GEMİ | 4 | keşif aracı (K0 sağlam / K1 sol arka tekerlek ezik) · kaçış gemisi (dış · kapı eşiği · kabin) | araç S03-S13 · gemi S03·S19·S30-S47 | 🔴 ZORUNLU | | | ⬜ TASLAK |

```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ. Dördü de 🔴 çünkü dördü de
   filmin İLK üretilen karesinde (S41) birden kadrajdadır.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu sütun
   "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanır.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| F1 | kirli beyaz basınçlı giysi + opak pane | insan | S00 | S46 | R1 | 🔴 kask/vizör (KART 3) + ikinci figür (KART 4) |
| F2 | yanık turuncu basınçlı giysi + opak pane | insan | S00 | S46 | R2 | 🔴 kask/vizör (KART 3) + ikinci figür (KART 4) |
| H1 | ince sarı ortak emniyet halatı | prop | S04 | S44 | R3 | 🔴 biçim kilidi (D146) — üç hat karışabilir |
| H2 | ince gri sandık kayışı | prop | S01 | S02 | R3 | 🟠 biçim kilidi (D146) |
| H3 | kalın siyah yer servis bağlantısı | prop | S07 | S38 | R3 | 🟠 biçim kilidi (D146) |
| H4 | gemi kapısındaki sarı halka + hızlı bağlantı | prop | S31 | S44 | R3 | 🟡 ölçek |
| A1 | sol önkoldaki düz alet | prop | S01 | S42 | R3 | 🔴 politika yüzeyi (KART 12) |
| V1 | dört tekerlekli açık kafes keşif aracı | araç | S03 | S13 | R4 | 🟠 ölçek (KART 13) |
| V2 | küçük kaçış gemisi (dış · kapı eşiği · kabin) | araç | S03 | S47 | R4 | 🟠 ölçek (KART 13) |
| P1 | numune sandığı | prop | S00 | S02 | R3 | 🟡 ölçek |
| P2 | gümüş bant | prop | S17 | S47 | R1 (K1) | 🟡 yıpranma (D42) |
| M1 | devrilmiş kafes direk | mekân | S19 | S27 | — (metne devredildi) | 🟠 ölçek (KART 13) |
| M2 | servis galerisi | mekân | S14 | S18 | — (metne devredildi) | 🟡 |
| M3 | yüzey · yarık · kara delik gökyüzü | mekân | S00 | S47 | — (World Bible 3 cümle) | 🟠 dünya çapası (D209) |

```
⛔ KOD kullanılır, AD kullanılmaz [D34].
⛔ DÜRÜST KAYIT — ÜÇ VARLIK SAYFASIZ: M1 · M2 · M3. Dört sayfa bütçesi sahibin
   kararıdır; bu üçünün biçimi YALNIZ METİNLE tutuluyor. M3 için World Bible'ın
   üç cümlesi her geniş dış prompta BİREBİR girer [D209]; M1 için birim ölçüsü
   sayıyla kilitli (kafes gözü 0,6 m · direk 14 m · 8 bölüm). RİSK AÇIK KALDI ve
   04_UYARI_NOTLARI §3'te kayıtlı.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| F1 BEYAZ | K0 (temel) | — | S00 | — | R1 p1-p3 |
| F1 BEYAZ | K1 | sol manşet dış kabuğu içeri ezik + dört tur gümüş bant, eklem halkası dönmüyor | S16 | S17 | R1 p4 |
| F2 TURUNCU | K0 (temel) | — | S00 | — | R2 p1-p4 |
| V1 ARAÇ | K0 (temel) | — | S03 | — | R4 p1 |
| V1 ARAÇ | K1 | sol arka tekerlek jantı hat dışına bükük, her turda gözle görünür sapma | S09 | S09 | R4 p4 |

```
⛔ MERDİVEN TEK YÖNLÜDÜR — geri dönüş YOK. F1 K1 S16'dan S47'ye kadar taşınır,
   V1 K1 S09'dan S13'e (aracın kaybına) kadar.
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK.
   F1 K0↔K1 çifti: R1 p1 ve R1 p4 aynı 3/4 duruş, tek fark SOL MANŞET.
⚠️ Aynı sayfada iki durum: kılavuz §3 ② ölçülmemiş çelişkidir. Bu dosyada
   AYNI SAYFA seçildi (R1 p1 = K0, R1 p4 = K1); NEDEN: durum farkı tek nesnede
   (manşet) ve yan yana görülmesi yükleyenin karşılaştırmasını kolaylaştırıyor.
   Ayrı sayfa seçilseydi beşinci sayfa gerekirdi ve sahip dört sayfa dedi.
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME (48/48)

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | dış (tek güneş sol üst) | R1 p1 + R2 p1 | yarık kenarı | K0 | kayan gövde · kapanan kavrama |
| S01 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | kemer yakını | K0 | kayan sandık · aletin çıkışı |
| S02 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | kemer yakını | K0 | ayrılan kayış · düşen sandık |
| S03 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R4 p1 | yarık kenarı | K0 | anlık eylem ve toz — referans taşımaz |
| S04 | iç (araç kafesi · dış ışık) | R1 p1 + R2 p1 + R3 p1 | araç kabini | K0 | anlık eylem ve toz — referans taşımaz |
| S05 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | yol · yüksek geniş | K0 | anlık eylem ve toz — referans taşımaz |
| S06 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | yol · yüksek geniş | K0 | anlık eylem ve toz — referans taşımaz |
| S07 | iç (araç kafesi · dış ışık) | R1 p1 + R2 p1 + R3 p1 | araç kabini | K0 | anlık eylem ve toz — referans taşımaz |
| S08 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | ocak yolu | K0 | anlık eylem ve toz — referans taşımaz |
| S09 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | tekerlek | K0 | anlık eylem ve toz — referans taşımaz |
| S10 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | ocak yolu | K0 | anlık eylem ve toz — referans taşımaz |
| S11 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | ocak yolu | K0 | anlık eylem ve toz — referans taşımaz |
| S12 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | sahanlık | K0 | anlık eylem ve toz — referans taşımaz |
| S13 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | sahanlık | K0 | kopan plaka · düşen araç |
| S14 | iç (galeri · sarı lamba + soğuk dilim) | R1 p1 + R2 p1 + R3 p1 | galeri koridoru | K0 | anlık eylem ve toz — referans taşımaz |
| S15 | iç (galeri · sarı lamba + soğuk dilim) | R1 p1 + R2 p1 + R3 p1 | galeri koridoru | K0 | anlık eylem ve toz — referans taşımaz |
| S16 | iç (galeri · sarı lamba + soğuk dilim) | R1 p1 + R2 p1 + R3 p1 | kiriş ve manşet | K1 | inen kiriş · ezilen manşet |
| S17 | iç (galeri · sarı lamba + soğuk dilim) | R1 p1 + R2 p1 + R3 p1 | kiriş ve manşet | K1 | sarılan bant |
| S18 | iç (galeri · sarı lamba + soğuk dilim) | R1 p1 + R2 p1 + R3 p1 | galeri koridoru | K1 | anlık eylem ve toz — referans taşımaz |
| S19 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | yarık geniş | K1 | anlık eylem ve toz — referans taşımaz |
| S20 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | direk yanı | K1 | anlık eylem ve toz — referans taşımaz |
| S21 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | direk ekseni | K1 | anlık eylem ve toz — referans taşımaz |
| S22 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | direk yanı | K1 | anlık eylem ve toz — referans taşımaz |
| S23 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | karşı sahanlık | K1 | anlık eylem ve toz — referans taşımaz |
| S24 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | korkuluk · iki eldiven | K1 | anlık eylem ve toz — referans taşımaz |
| S25 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | yarık geniş | K1 | yük alan halat |
| S26 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | duvar | K1 | anlık eylem ve toz — referans taşımaz |
| S27 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | yarık geniş | K1 | anlık eylem ve toz — referans taşımaz |
| S28 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | duvar | K1 | anlık eylem ve toz — referans taşımaz |
| S29 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | korkuluk · iki eldiven | K1 | kapanan bilek kavraması |
| S30 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | platform geniş | K1 | anlık eylem ve toz — referans taşımaz |
| S31 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | sarı halka | K1 | anlık eylem ve toz — referans taşımaz |
| S32 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | platform geniş | K1 | anlık eylem ve toz — referans taşımaz |
| S33 | iç (kabin · 4500K panel) | R1 p1 + R2 p1 + R3 p1 | kontrol yeri | K1 | anlık eylem ve toz — referans taşımaz |
| S34 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | servis soketi | K1 | anlık eylem ve toz — referans taşımaz |
| S35 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | servis soketi | K1 | düşen siyah bağlantı |
| S36 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | güverte korkuluğu | K1 | sıkışan hat · kaybolan basamak |
| S37 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | güverte korkuluğu | K1 | anlık eylem ve toz — referans taşımaz |
| S38 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | kapı dışı geniş | K1 | anlık eylem ve toz — referans taşımaz |
| S39 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | güverte korkuluğu | K1 | anlık eylem ve toz — referans taşımaz |
| S40 | iç (kabin · 4500K panel) | R1 p1 + R2 p1 + R3 p1 | kontrol yeri | K1 | anlık eylem ve toz — referans taşımaz |
| S41 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | kapı dışı geniş | K1 | aktarılan ağırlık |
| S42 | dış (tek güneş sol üst) | R1 p1 + R2 p1 + R3 p1 | kemer halkası | K1 | ayrılan alt kol |
| S43 | iç (kabin · 4500K panel) | R1 p1 + R2 p1 + R3 p1 | kabin zemini | K1 | anlık eylem ve toz — referans taşımaz |
| S44 | iç (kabin · 4500K panel) | R1 p1 + R2 p1 + R3 p1 | kabin zemini | K1 | anlık eylem ve toz — referans taşımaz |
| S45 | dış (tek güneş sol üst) | R4 p3 | platform geniş | K1 | kalkış · çöken platform |
| S46 | iç (kabin · 4500K panel) | R1 p1 + R2 p1 + R3 p1 | kabin zemini | K1 | iki parmak · dönen eldiven |
| S47 | dış (tek güneş sol üst) | R4 p3 | gök | K1 | uzaklaşma · iki kabin ışığı |

```
⛔ "METNE DEVREDİLEN" BOŞ BIRAKILAMAZ — referansın taşıyamadığı her şey buraya
   yazılır [kılavuz §5.1]. Bu filmde referans HİÇBİR sahnede hareketi taşımaz:
   anlık eylem, toz, çöküş ve tutuş DAİMA metindedir.
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (`VEO` §6 md.2) — tablo 3'ü geçmiyor.
   Dördüncü varlık (M1 direk · M2 galeri · M3 dünya) metne devredildi.
⛔ S45 ve S47'de insan kadrajda YOK → yalnız R4 p3 (gemi dış) yüklenir.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun kopyasıdır; ayrışırsa
  tablo düzeltilir. Sayfası ⏳ olan sahne "ÜRETİLMEZ" damgası taşır.
```

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · BEYAZ

```
IN FRAME: full body, back
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill.

Exactly one human character — no clones, no second person. A man standing straight
and facing the lens, sealed in a dirty off-white hard-shell pressure suit with
cobalt-blue shoulder caps rising over the collar, dark grey joint rings at the
elbows and knees, heavy segmented dark-grey gloves and boots. His helmet is a hard
off-white shell seated in a dark grey collar ring with one flat front pane held in
a thick dark-grey rim; the pane is fully opaque matte black, showing no face, no
eyes and no skin from any angle. A short flat tool the length of a hand is clipped
along the outside of his left forearm. A dark crate hook hangs on the right of his
belt. The back of his suit is one continuous ribbed surface from collar to hip, and
one angular dark box is mounted flat on it, wide and square-edged, its upper edge
under the cobalt-blue shoulder caps. Fixed wear that never moves: grey dust on the
left cuff, on the right knee and across the lower back.

NEGATIVE: [KILAVUZ_REHBERI §5.3 tam liste] 0% bloom, no glow, every surface keeps
visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch
or sign — none on the suit, the helmet, the equipment or the backdrop — no subtitles,
no captions, no watermark. No face, no
eyes and no mouth behind the pane, and the pane stays fully opaque. No clear glass,
no tinted glass, no mirror coating, no reflection in the pane. No fabric, no cloth,
no flapping or billowing material. No back-mounted tank, hose or cable — the back
unit is one closed integral box. No bare skin anywhere — none at the wrist, none at the collar, none at the ankle. No panel gutters, no labels,
no captions, no arrows, no callouts, no dimension lines, no panel titles.

Output: 16:9, 3840 × 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş (K0)
               p2 · profil — siluet hattı ve omuz kapağı geometrisi
               p3 · SIRT — sürekli kaburgalı yüzey + köşeli kutu [D79/D139 karşılığı]
               p4 · SOL ÖNKOL CU — K1 durumu: ezik manşet + dört tur gümüş bant
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — panelin işi ona ne KOYACAĞINI söylemektir:
   yasak değil MALZEME [D123 · D139]. p3 bu yüzden POZİTİF tarifle yazıldı.
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      pane dört panelin dördünde de TAMAMEN opak · omuz kapağı kobalt mavi ·
              sırt kutusu KÖŞELİ ve GENİŞ · sol önkolda düz alet var
  RET:        pane'de herhangi bir yansıma, cam parıltısı ya da yüz izi ·
              kubbe/balon kask · sırt çantası/hortum · sağ önkolda alet
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "Bu adamın sırtındaki şey
              dar mı geniş mi, kutu mu dikdörtgen mi?" · doğru cevap: "geniş, köşeli kutu"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S00-S46 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 3
     (giysi rengi · omuz parçası · sırt ünitesi — yaş/boy/ten HİÇ yazılmadı)
```

### 📸 IMAGE PROMPT — SAYFA R2 · TURUNCU

```
IN FRAME: full body, back
Photorealistic full-length still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill.

Exactly one human character — no clones, no second person. A man standing straight
and facing the lens, sealed in a burnt-orange hard-shell pressure suit whose upper
arms are matte black from shoulder to elbow, dark grey joint rings at the elbows and
knees, heavy segmented dark-grey gloves and boots. His helmet is a hard burnt-orange
shell seated in a dark grey collar ring with one flat front pane held in a thick
dark-grey rim; the pane is fully opaque matte black, showing no face, no eyes and no
skin from any angle. A small flat control block the size of two fingers sits on his
left wrist with its cover shut. A flat repair kit hangs on the right of his belt. The
back of his suit is one continuous ribbed surface from collar to hip, and one narrow
dark rectangle stands on it, tall and thin, clear of the black upper arms. Fixed wear
that never moves: grey dust on both knees.

NEGATIVE: [KILAVUZ_REHBERI §5.3 tam liste] 0% bloom, no glow, every surface keeps
visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch
or sign — none on the suit, the helmet, the equipment or the backdrop — no subtitles,
no captions, no watermark. No face, no
eyes and no mouth behind the pane, and the pane stays fully opaque. No clear glass,
no tinted glass, no mirror coating, no reflection in the pane. No fabric, no cloth,
no flapping or billowing material. No back-mounted tank, hose or cable — the back
unit is one closed integral rectangle. No bare skin anywhere — none at the wrist, none at the collar, none at the ankle. No cobalt blue anywhere
on this suit. No panel gutters, no labels, no arrows, no callouts, no panel titles.

Output: 16:9, 3840 × 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş
               p2 · profil — siluet hattı ve siyah üst kol sınırı
               p3 · SIRT — sürekli kaburgalı yüzey + dar dikdörtgen [D139 karşılığı]
               p4 · SOL BİLEK CU — kumanda bloğu kapağı kapalı ve açık
⛔ R1 ile YAN YANA basılır: iki sırt ünitesi aynı sayfada karşılaştırılabilir olmalı.
   Ayrım üç kanalda: RENK + OMUZ GEOMETRİSİ + SIRT GEOMETRİSİ.
```
```
KABUL SINAVI (R2) — dört alan ZORUNLU [D144]:
  KABUL:      üst kollar omuzdan dirseğe SİYAH · sırt ünitesi DAR ve DİKDÖRTGEN ·
              sol bilekte kumanda bloğu · pane tamamen opak
  RET:        turuncu kolların üstünde mavi/gri şerit · geniş köşeli sırt kutusu ·
              sağ bilekte kumanda · pane'de yansıma
  YABANCI GÖZ: R1 ve R2 panellerini yan yana göster · soru: "Hangisi hangisi,
              tek bir farkla söyle" · doğru cevap: "omuzlar mavi olan / kolları siyah olan"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S00-S46 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: 3 (giysi rengi · üst kol · sırt ünitesi)
```

### 📸 IMAGE PROMPT — SAYFA R3 · HAT AİLESİ

```
IN FRAME: none
Photorealistic technical still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill. The frame holds these objects and
nothing else.

Five separate objects laid out side by side on a plain mid-grey surface, each one
fully visible end to end and none of them touching another. First, a yellow safety
line as thick as a pencil, laid in a long straight run, its free end finished with a
dark steel hook. Second, a grey crate strap half the thickness of the yellow line,
flat rather than round, laid in a shorter run with a plain buckle at one end. Third,
a black ground service umbilical four times the thickness of the yellow line, stiff
and ribbed along its length, with a heavy squared connector at one end. Fourth, a
yellow steel ring the width of a glove with a hinged quick connect on its lower side,
lying flat. Fifth, a short flat tool the length of a hand with a blunt squared end and
a plain grip, lying flat. The three lines run parallel so their thicknesses can be
compared directly, and the difference in thickness between each pair is obvious.

NEGATIVE: [KILAVUZ_REHBERI §5.3 tam liste] 0% bloom, no glow, every surface keeps
visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch
or sign — none on the objects and none on the backdrop — no subtitles, no captions,
no watermark.
No fabric, no cloth, no rope fibres, no braiding, no fraying. No sixth object, no
extra cable and no line that is not listed. No panel gutters, no labels, no arrows,
no callouts, no dimension lines, no panel titles.

Output: 16:9, 3840 × 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · beş nesne yan yana — KALINLIK KARŞILAŞTIRMASI (ana panel)
               p2 · sarı halat CU — kesit, kanca, hızlı bağlantı
               p3 · gri kayış + siyah bağlantı CU — ikisi yan yana
               p4 · düz alet CU — form, kavrama, kör uç
⛔ FİLMİN BÜTÜN MANTIĞI BU SAYFADA: S42'de hangi hattın ayrıldığı okunmazsa
   filmin anlamı TERSİNE döner [A5 · 1 numaralı risk]. Kalınlık farkı p1'de
   ölçülebilir olmalı — 1 : 0,5 : 4 oranı.
⛔ p4'te alet ADLANDIRILMAZ, yalnız FORMU gösterilir [D67 · KART 12].
```
```
KABUL SINAVI (R3) — dört alan ZORUNLU [D144]:
  KABUL:      p1'de üç hattın kalınlığı çıplak gözle sıralanabiliyor (siyah > sarı > gri) ·
              sarı halat kalem kalınlığında · siyah bağlantı sarının dört katı
  RET:        iki hat aynı kalınlıkta okunuyor · halat örgülü/lifli çıkmış ·
              altıncı bir nesne kadraja girmiş · alette keskin kenar görünüyor
  YABANCI GÖZ: p1'i göster · soru: "En ince hangisi, en kalın hangisi?" ·
              doğru cevap: "en ince gri, en kalın siyah"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S01·S02·S04-S47 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: — (insan yok)
```

### 📸 IMAGE PROMPT — SAYFA R4 · ARAÇ VE GEMİ

```
IN FRAME: none
Photorealistic technical still, 35mm film grain, plain neutral mid-grey seamless
backdrop, even neutral key light with soft fill. The frame holds these objects and
nothing else.

Two vehicles standing side by side on a plain mid-grey surface, both seen in three
quarter view with its nose pointing to the left of frame. On the left a four
wheeled open-cage rover about the length of two men, built of plain tube frame with
two low seats, a small hand reel between them, a low plain dash carrying one small
orange indicator, four heavy open wheels with deep tread, and no bodywork panels at
all. On the right a small white ship about the length of eight men standing on three
legs, its hull smooth and matte, one door open in its flank with a raised sill lip
and three inner steps behind it, a yellow steel ring bolted to the door frame, and a
deck socket at its base with a bent steel cover and a plain manual lever. A plain
scale bar stands between them at the height of a man.

NEGATIVE: [KILAVUZ_REHBERI §5.3 tam liste] 0% bloom, no glow, every surface keeps
visible texture. No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — no hull numbers, no roundels, no insignia, nothing on the
backdrop — no subtitles, no captions, no watermark. No miniature read, no tilt-shift, no shallow depth of field on either
vehicle. No third vehicle, no trailer and no structure that is not listed. No wings,
no canopy glass, no visible engine flame. No panel gutters, no labels, no arrows, no
callouts, no dimension lines, no panel titles.

Output: 16:9, 3840 × 2160, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · araç 3/4 — K0 sağlam, insan boyu ölçek çubuğuyla
               p2 · gemi 3/4 dış — üç ayak, kapı, eşik, sarı halka
               p3 · gemi UZAK — kapanış kadrajı için siluet ve iki kabin ışığı
               p4 · araç SOL ARKA TEKERLEK CU — K1 durumu: hat dışına bükük jant
⛔ Gemi kabini AYRI PANEL ALMIYOR: kabin iç hacmi metinle tutuluyor
   (kontrol yeri · iki koltuk · 4500K panel · turuncu zemin şeridi). DÜRÜST KAYIT:
   S33 · S40 · S43 · S44 · S46'nın iç kadrajı referanssızdır, risk 04_UYARI §3'te.
```
```
KABUL SINAVI (R4) — dört alan ZORUNLU [D144]:
  KABUL:      araç insan boyunun ~2 katı okunuyor · gemi ~8 katı · p3'te tam İKİ
              kabin ışığı sayılıyor · p4'te bükülme hat dışına çıkmış
  RET:        maket/tilt-shift okuması · gövde panelli kapalı araç · gemide kanat
              ya da cam kanopi · gövde numarası / amblem
  YABANCI GÖZ: p1 ve p2'yi göster · soru: "Bu ikisinden hangisi kaç adam boyunda?" ·
              doğru cevap: "soldaki iki, sağdaki sekiz"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · S03-S13 ve S30-S47 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: — (insan yok)
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `THE_FALLING_WORLD_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.
```
✅ ① PANEL ARİTMETİĞİ  §1 künye toplamı 16 = §2 tablo toplamı 16
✅ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var; çağrılmayan sayfa YOK (R1-R4 dördü de çağrılıyor)
✅ ③ DURUM MERDİVENİ   iki merdiven tek yönlü (F1 K0→K1 S16 · V1 K0→K1 S09), geri dönüş yok
✅ ④ METNE DEVREDİLEN  48/48 satırda dolu
✅ ⑤ SAHNE BAŞINA ≤3   48/48 satırda en çok 3 kayıt
⬜ ⑥ DURUM: dört sayfa da TASLAK — SEED ve SHA-256 üretim gününde yazılır.
   ⛔ Dördü ONAYLI olmadan HİÇBİR sahne üretilmez [D168 · KAPI 0].
```
