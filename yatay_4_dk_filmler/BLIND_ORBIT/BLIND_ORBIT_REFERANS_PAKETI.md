# 🧷 BLIND_ORBIT — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
görünüş `UZAY_GIYSISI_SINEMATIK_TASARIM` §11 (arketip T) · ölçek `UZAY_USSU` §1-§2.2 ·
seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0 — sahip kararı 05.10.2026:
> "Yazılsın"). Sıra: bu dosya → kabul kapısı → seed kilidi → K15 (İPTAL KAPISI) →
> K20 → K21 (DORUK) → K18 (merkezî seçim) → K24 → K23 → K01 → K02 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Bu filmde üç yerde
> birden: iki kasklı figür (aynı arketip T) · dev dönen istasyon (oran) · dört kancalı
> kenet halkası (sayı + iki durum).
>
> ⚠️ **BETİK DAVRANIŞI (06.09.2026 ölçümü):** `### 📸 IMAGE PROMPT` başlığı
> `prompt_kontrol.py` başlık desenine uyar; dosya DOSYA modunda imaj promptu gibi
> denetlenir. ⛔ İngilizce prompt başlıktan sonraki İLK çitli bloktur.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: pilot + mühendis — ikisi de
                                                               arketip T, 15 insanlı klip
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: vizör (tek düz pane + kalın
                                                               çerçeve) · kenet halkası (yumuşak
                                                               halka + DÖRT kanca)
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: LARK 26 m ↔ VESPER ~900 m
                                                               (1:35) · kara delik + bükük yay
□ T4 İNSAN DIŞI CANLI                                          hangi: — (yok)
☑ T5 TEKRAR EDEN İNSAN DIŞI OLAY                               hangi: itici gaz konisi (düz, kısa,
                                                               bir gövde boyunda söner) — K01 K03
                                                               K07 K13 · metne devredildi (§5)
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                          rapor: istasyon 7 klipte · kokpit 8 ·
                                                               servis/optik bölme 7
```

## 1. 🎫 PAKET KÜNYESİ

```
FILM: BLIND_ORBIT          FORMAT: yatay 4 dk · çok klipli sahne · 24 klip / 6 sahne
SAYFA ORANI = FİLM ORANI  ORAN: 16:9   ÇÖZÜNÜRLÜK: 4K
SAYFA: 8   TOPLAM PANEL: 23   ARİTMETİK: RK1 4 + RK2 4 + RA 3 + RB 3 + RI1 3 + RI2 3 + RO 2 +
                                          RD 1 = 23
   ⛔ Bu toplam §2 tablosunun panel toplamına EŞİT (§7 ①) ✅
İMAJ MODELİ + SÜRÜM: ⬜ üretim günü yazılır (Nano Banana 2 · Flow)   TARİH: 05.10.2026 (yazım)
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `BLIND_ORBIT_KAPAK.md` (RK onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

> ⛔ ÜRETİM SIRASI DRAMATİK SIRA DEĞİLDİR [D168].
> Sıra: RD → RB → RO → RA → RI1 → RI2 → RK1 → RK2 → K15 → K20 → K21 → K18 → K24 → K23 → K01 → kalanı.
> Gerekçe: K15 (1 numaralı risk, İPTAL KAPISI) yalnız RB + RO + RD ister — insan sayfaları
> onaylanmadan iptal kapısı ölçülebilir.

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| RD | kara delik | 1 | siyah disk + ince kehribar bant + bükük yay | 🔴 ZORUNLU (K15 önce) | | | ⬜ TASLAK |
| RB | istasyon | 3 | uzun koyu silindir · 3 kanat · ön yüzde tek kenet · uzak uçta motor halkası | 🔴 ZORUNLU (K15 önce) | | | ⬜ TASLAK |
| RO | kenet halkası | 2 | iki durum: dört kanca AÇIK ↔ KAPALI | 🔴 ZORUNLU (K15 önce) | | | ⬜ TASLAK |
| RA | servis gemisi | 3 | kısa küt gövde · burun penceresi · sol yanda yırtık dikiş | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RI1 | kokpit | 3 | iki koltuk · konsol · ekran · tek kehribar çizgi · T-kabza | 🟠 K04'ten önce | | | ⬜ TASLAK |
| RI2 | servis geçidi + optik bölme | 3 | raylı geçit · vana çarkı · retiküllü yuvarlak pencere | 🟠 K02'den önce | | | ⬜ TASLAK |
| RK1 | pilot | 4 | inci beyazı T · altın şerit SAĞ · kanat rozeti | 🔴 ZORUNLU | | | ⬜ TASLAK |
| RK2 | mühendis | 4 | beyaz nervürlü T · kobalt şerit SOL · altıgen rozet · bilek göstergesi | 🔴 ZORUNLU | | | ⬜ TASLAK |

```
🔴 üretim başlamadan · 🟠 belirli klipten önce · ⏳ ertelenebilir (bu pakette yok)
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ (kılavuz §7.2)
⛔ ONAYLI olmayan sayfanın klipleri ÜRETİLMEZ.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa "arayüzde yok"
   yazılır ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: `shasum -a 256 <panel.png>` — üretimden önce yeniden hesaplanıp karşılaştırılır.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk klip | son klip | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| RK1 | pilot (kasklı, arketip T) | insan | K04 | K23 | RK1 | 🔴 kubbe vizör · sırt ünitesi · kimlik karışması |
| RK2 | mühendis (kasklı, arketip T) | insan | K02 | K22 | RK2 | 🔴 kubbe vizör · sırt ünitesi · kimlik karışması |
| RA | küçük servis gemisi (hasarlı) | araç | K01 | K24 | RA | 🟠 ölçek (minyatür okuma) · hasarın kayması |
| RB | dönen istasyon | araç / yapı | K01 | K24 | RB | 🔴 oran · kanat sayısı · dönüş yönü |
| RO | kenet halkası + dört kanca | prop (mekanizma) | K02 | K22 | RO | 🔴 kanca sayısı · iki halkanın tek yüzeye erimesi |
| RD | kara delik | ortam | K01 | K24 | RD | 🟠 parlama (bloom/halo) · yayın kaybolması |
| RI1 | kokpit | mekân | K04 | K23 | RI1 | 🟠 ekran metni · koltuk sayısı |
| RI2 | servis geçidi + optik bölme | mekân | K02 | K22 | RI2 | 🟠 retikülde rakam/ölçek çizgisi |

```
⛔ KOD kullanılır, AD kullanılmaz [D34] — "LARK / VESPER / Lena / Noah" hiçbir promptta yok.
⛔ YETİM 0 · ÇAPASIZ 0 (her kodun ≥1 klibi var, her kadraj varlığının sayfası var).
BELGEDE KALAN: itici gaz konisi (T5 — hareket, panel taşıyamaz) · titreşim · motor ışığı (S6).
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç klibi | dönüşüm klibi | panel |
|---|---|---|---|---|---|
| RA | K0 (temel = HASARLI) | sol yanda yırtık dikiş — film boyu sabit | K01 | — | RA p1-p3 |
| RO | K0 kancalar AÇIK | — | K02 | — | RO p1 |
| RO | K1 kancalar KAPALI | dört kanca kenarın üstüne oturdu | K21 (6,5 s) | K21 | RO p2 |
| RI1 | ekran AÇIK ↔ KARA | ekran K16'dan itibaren siyah — panel ÇİFTİ değil, metne devredildi | K04 | K16 | RI1 p2 (açık) |

```
⛔ MERDİVEN TEK YÖNLÜDÜR — RO K1'den K0'a dönülmez; RA hasarı onarılmaz.
⛔ DURUM ÇİFTİ RO p1 ↔ p2: aynı kadraj · aynı ışık yönü (sol üst) · aynı mesafe, TEK FARK kanca
   konumu (±%3 en).
⚠️ Aynı sayfada iki durum (RO): kılavuz §3 ② ölçülmemiş çelişkidir. SEÇİLDİ çünkü iki durumun
   AYNI halka olduğu tek görselde kilitlenmezse K21 iki farklı mekanizma çizer (sayı + biçim);
   panel ayrımı kırpımla sağlanır, yükleme tek panel.
```

## 5. 🗺️ KLİP → REFERANS EŞLEME

| klip | iç/dış + ışık | yüklenecek KIRPIM | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| K01 | dış · kehribar sol üst | RA p1 · RB p1 · RD p1 | profil, eksen | RA K0 | iki gövdenin birlikte dönüşü · burun teması 8,0 s |
| K02 | iç · bölme loş | RK2 p3 · RI2 p3 · RO p1 | OTS sırttan | RO K0 | iki parmak işareti · halkanın retiküle kayması |
| K03 | dış | RA p2 · RB p1 · RD p1 | profil | RA K0 | gaz konisi · yana kayma |
| K04 | iç · kokpit | RK1 p3 · RK2 p3 · RI1 p1 | arkadan üst açı | — | kabza iki sıkış · bakış faz farkı |
| K05 | dış | RB p2 · RD p1 | alt açı 3/4 | — | çeyrek tur · istek tonu |
| K06 | iç · kokpit | RK1 p3 · RK2 p3 · RI1 p1 | arkadan üst açı | — | büyük düzeltme · kabzanın geri itmesi |
| K07 | dış | RA p2 · RB p1 · RD p1 | profil | RA K0 | dört karşı-itki · bir gövde boyu |
| K08 | iç · kokpit | RK1 p3 · RK2 p3 · RI1 p1 | arkadan üst açı | — | 1,2 s gecikme · baş eğme |
| K09 | iç · geçit | RK2 p1 · RI2 p1 | sırttan alt açı | — | raylarda çekilme · kayış iki çekiş |
| K10 | iç · geçit | RK2 p2 · RI2 p2 | OTS sol omuz CU | — | çarkın takılması · ikinci yüklenme |
| K11 | iç · kokpit | RK1 p3 · RI1 p1 | arkadan üst açı | — | ekranın bir kez kararıp dönmesi |
| K12 | iç · geçit | RK2 p2 · RI2 p2 | OTS sol omuz CU | — | gösterge okuma · omuz inişi |
| K13 | dış | RA p1 · RB p1 · RD p1 | profil | RA K0 | geminin dönmeye başlaması |
| K14 | iç · kokpit | RK1 p3 · RI1 p1 | arkadan üst açı | — | kanatların yavaşlaması |
| K15 | dış · gövde kamerası | RB p3 · RO p1 · RD p1 | eksen boyunca | RO K0 | ⛔ yüz durur · kara delik çeyrek tur |
| K16 | iç · kokpit | RK1 p3 · RI1 p1 | arkadan üst açı | ekran KARA | ekran siyah (metin) · elin çekilmesi |
| K17 | iç · bölme | RK2 p3 · RI2 p3 · RO p1 | OTS sırttan | RO K0 | tek kayış çekişi · vizörün cama eğilmesi |
| K18 | iç · kokpit | RK1 p4 · RI1 p3 | 3/4 ön MCU | ekran KARA | başparmak durur · el gevşer |
| K19 | iç · bölme | RK2 p3 · RI2 p3 · RO p1 | OTS sırttan | RO K0 | halkanın büyümesi · açık el |
| K20 | dış · halka ağzı | RA p3 · RO p1 | frontal eksen | RO K0 | temas 3,0 s · bir parmak esneme |
| K21 | dış · makro | RO p1 · RO p2 | üst açı CU | RO K0 → K1 | dört kanca 2,0 · 3,5 · 5,0 · 6,5 s |
| K22 | iç · bölme | RK2 p3 · RI2 p3 · RO p2 | OTS sırttan | RO K1 | tavan panelinin yanması · titreşim |
| K23 | iç · kokpit | RK1 p4 · RI1 p3 | 3/4 ön MCU | — | elin dizine açılması · motor ışığı |
| K24 | dış | RA p1 · RB p1 · RD p1 | profil (K01 kafiye) | RA K0 · RO K1 | birlikte taşınma · bant kayması |

```
⛔ "METNE DEVREDİLEN" boş değil (24/24).
⛔ Bir klipte EN ÇOK 3 kayıt (`VEO` §6 md.2) — 24/24 ✅ (K21'de aynı sayfanın iki paneli = 2).
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3] · seçilen biçim: KIRPIM ·
   gerekçe: SIGNAL_KEEPERS ile aynı (sayfa yüklemesinde model panel bölmelerini kopyalıyor —
   ölçülmedi, risk tarafı seçildi).
· Flow çağırma: `@RK1` · `@RB` … — etiket KOD, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
· Bölüm dosyalarındaki `📎 REFERANS` satırı bu tablonun özetidir; ayrışırsa tablo düzeltilir.
```

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA RD · KARA DELİK
```
IN FRAME: none
Photorealistic still of deep space, 35mm film grain, deep focus.

A black hole fills the centre of the frame: a perfectly black disc wrapped in a thin sharp band of hot amber light that crosses in front of it edge-on, with a fainter bent arc of the same amber light curving over the top of the disc and another under it. The band is brightest on its left side and fades toward the right. Around it lies black space with a few faint stars, more of them far from the disc. No structure, no ship and no planet anywhere in the frame.

NEGATIVE: No readable text, letters, digits or symbols on any surface in the frame — no labels, no captions, no arrows, no callouts, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No halo, no light shafts, no lens flare and no corona around any lit surface.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU (K15 önce)   PANEL: 1   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · tam kare — disk + bant + üst/alt yay (sol taraf parlak = ışık yönü sol üst)
⛔ "glowing / accretion glow" YAZILMAZ — ince sert bant: halo davetiyesi kapalı.
```
```
KABUL SINAVI (RD):
  KABUL:      disk tam siyah · bant İNCE ve keskin kenarlı · üst VE alt yay görünür · bant solda parlak
  RET:        disk çevresinde bulanık hale · bant kalın sis · yay yok · gezegen/gemi belirmesi
  YABANCI GÖZ: soru "ışık hangi yandan geliyor?" · doğru cevap: "sol"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · dış klipler ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RB · İSTASYON
```
IN FRAME: none
Photorealistic three-panel still of one large structure in deep space, 35mm film grain, deep focus, the three panels side by side on a black ground.

Panel one, a side-on profile: a huge dark station, a long dark metal cylinder about twenty times as long as it is wide, with three dark flat radiator fins standing out from it at equal angles and running half its length, one round docking collar at the centre of its flat front face on the right, and a ring of large dark engine bells at its far end on the left. Panel two, a low three-quarter view from below the front: the three fins at equal angles, one pointing straight down. Panel three, straight along the axis at the front face: a flat round face, the docking collar at its exact centre, the three fins standing out behind it at equal angles like a three-pointed star. The hull is matte dark grey plating with fine panel seams and no markings. Hard amber light falls from the upper left; every shadow is black and hard-edged. A small off-white craft one thirtieth of the cylinder's length hangs beside the front face in panel one, for scale.

NEGATIVE: No readable text, letters, digits or symbols on any surface in the frame — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No tilt-shift look and no miniature read — the far end of the structure is as sharp as the near end; no logo, emblem or painted marking on any hull.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU (K15 önce)   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · profil (A kurulumu) — oran 1:20 + ölçek şahidi gemi 1/30
               p2 · alt 3/4 (D kurulumu) — kanat dizilişi
               p3 · eksen boyunca ön yüz (G kurulumu) — kenet tam merkezde, üç kanat yıldız
⭐ ÖLÇEK ŞAHİDİ: 1H burada yok (istasyon 900 m'de insan piksel altı) → şahit RA gemisi (26 m).
```
```
KABUL SINAVI (RB):
  KABUL:      kanat sayısı = 3 (üç panelde) · kenet ön yüzün MERKEZİNDE · uzak uç yakın uç kadar keskin
  RET:        2 ya da 4 kanat · halka-istasyon (simit) · pencere/logo · minyatür bulanıklığı
  YABANCI GÖZ: p3'ü göster · soru "kaç kanat?" · doğru cevap: "üç"
  SONUÇ:      ⬜ (geçmezse K15 dahil 7 RB klibi ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RO · KENET HALKASI (iki durum)
```
IN FRAME: none
Photorealistic two-panel still of one docking mechanism, 35mm film grain, deep focus, the two panels side by side on dark hull plating, the same view and the same light in both.

Seen from above at a slight angle, a round docking collar about two and a half metres across: a soft pale grey outer ring of thick padded material pressed face to face against a bright steel rim, two separate rims with a clean seam between them. Around it stand exactly four large hook-shaped steel latches, evenly spaced, each on its own hinge. Panel one: all four latches stand open, raised away from the rim. Panel two: all four latches are closed over the rim and seated, gripping its edge. Dark matte hull plating surrounds the ring. Hard amber light falls from the upper left and leaves black, hard-edged shadows under each latch.

NEGATIVE: No readable text, letters, digits or symbols on any surface in the frame — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. The two rims never merge into one surface; no sparks and no flashes anywhere.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU (K15 önce)   PANEL: 2   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · K0 kancalar AÇIK (K02 · K15 · K17 · K19 · K20 · K21 başı)
               p2 · K1 kancalar KAPALI (K21 sonu · K22)
⛔ DURUM ÇİFTİ — aynı kadraj · aynı ışık · ±%3 en (§4).
```
```
KABUL SINAVI (RO):
  KABUL:      kanca sayısı = 4 (iki panelde) · eşit aralık · yumuşak halka + çelik kenar İKİ ayrı yüzey
  RET:        3/5/6 kanca · iki halka tek yüzeye erimiş · kıvılcım · kancalar istasyon kanadına benziyor
  YABANCI GÖZ: p2'yi göster · soru "kaç kanca kapalı?" · doğru cevap: "dört"
  SONUÇ:      ⬜ (geçmezse K21 — FİNAL VURUŞ KANITI — ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RA · SERVİS GEMİSİ (hasarlı, film boyu)
```
IN FRAME: none
Photorealistic three-panel still of one small spacecraft in deep space, 35mm film grain, deep focus, the three panels side by side on a black ground.

A small off-white service ship, short and blunt, about four times as long as it is wide: a wide window across its nose, a round docking collar below the nose facing forward, a cluster of small nozzles on each side and one large dark engine bell at the stern. Its hull is off-white matte composite with fine panel seams, scuffed at the edges, no markings. On its left side, by the nozzle cluster, the hull is opened along one seam, the edges cold and torn, and a few nozzles there are bent. Panel one: side-on profile, nose to the left. Panel two: three-quarter view of the left side, the torn seam toward the camera. Panel three: nose-on, the window above and the docking collar centred below it. Hard amber light from the upper left; shadows black and hard-edged.

NEGATIVE: No readable text, letters, digits or symbols on any surface in the frame — no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No tilt-shift look and no miniature read; no logo, emblem or painted marking on any hull; no gas, no smoke and no debris near the ship.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · profil (A · K01 K13 K24)   p2 · sol 3/4 — yırtık dikiş (K03 K07)
               p3 · burun (I · K20)
⛔ Gaz konisi panele GİRMEZ (T5 — hareket metne devredildi); panel durağan hasarı kilitler.
```
```
KABUL SINAVI (RA):
  KABUL:      pencere 1 · kenet 1 · yan lüle kümesi 2 · ana motor çanı 1 · hasar YALNIZ sol yanda
  RET:        hasar iki yanda · alev/duman · enkaz bulutu · logo/bayrak · uçak kanadı
  YABANCI GÖZ: p2'yi göster · soru "hasar hangi yanda?" · doğru cevap: "sol"
  SONUÇ:      ⬜ (geçmezse 6 RA klibi ÜRETİLMEZ: K01 K03 K07 K13 K20 K24)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RI1 · KOKPİT
```
IN FRAME: none
Photorealistic three-panel still of one empty spacecraft cockpit, 35mm film grain, deep focus, the three panels side by side.

A narrow cockpit with two seats side by side facing a wide forward window. Between the seats a low console holds one dark rectangular display at its centre and, on a small panel beside it, a single thin amber line of light. On the inner armrest of each seat sits a T-shaped hand grip with a small round cap on its top. Each seat has a lap strap and shoulder straps. The ceiling panels are white, the walls light grey and the floor dark graphite. The cabin is lit by cold blue-grey panel light; one small amber lamp sits on the console. Panel one: from behind and above both seats toward the window, the display lit a flat pale grey. Panel two: close on the console, the display, the amber line and the left seat's grip. Panel three: from the front right of the left seat, the seat, its grip and the console edge, the window behind.

NEGATIVE: No readable text, letters, digits or symbols on any display, surface, patch or sign — no graphics on the display, no labels, no captions, no arrows, no callouts, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 K04'ten önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · C kurulumu (K04 K06 K08 K11 K14 K16)   p2 · konsol + kabza (rezerv çizgisi)
               p3 · H kurulumu arka planı (K18 K23)
⛔ Ekran KARA durumu panel değil METİN (K16'dan itibaren "flat black rectangle").
```
```
KABUL SINAVI (RI1):
  KABUL:      koltuk 2 · ekran 1 · kehribar çizgi 1 · T-kabza 2 · hiçbir yüzeyde harf/rakam
  RET:        ekranda grafik/rakam · üçüncü koltuk · uçak kokpiti göstergeleri · yazılı etiket
  YABANCI GÖZ: p2'yi göster · soru "konsolda kaç ışık çizgisi var?" · doğru cevap: "bir"
  SONUÇ:      ⬜ (geçmezse 8 kokpit klibi ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RI2 · SERVİS GEÇİDİ + OPTİK BÖLME
```
IN FRAME: none
Photorealistic three-panel still of one empty spacecraft interior, 35mm film grain, deep focus, the three panels side by side.

A low narrow passage of pale grey panels with a rail along each wall and a cold white strip light along the white ceiling; the floor is dark graphite. Halfway along, set in the right-hand wall at chest height, a heavy steel hand-wheel the width of a helmet, its rim worn bright, with a short webbing loop beside it. At the far end, a small round bay: a small round window the width of a helmet with two fine cross-hair lines etched on it, and a padded support seat with a lap strap facing the window. Panel one: along the passage from low at one end, the hand-wheel halfway and the round window at the far end. Panel two: close on the hand-wheel and the webbing loop. Panel three: from behind the support seat toward the round window and its two cross-hair lines, black space beyond.

NEGATIVE: No readable text, letters, digits or symbols on any surface, patch or sign — no scale marks on the window, no labels, no captions, no arrows, no callouts, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture. 0% bloom, no glow, no soft focus, every surface keeps visible texture.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 K02'den önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · E kurulumu (K09)   p2 · F kurulumu arka planı (K10 K12)
               p3 · B kurulumu (K02 K17 K19 K22) — retikül iki çizgi
```
```
KABUL SINAVI (RI2):
  KABUL:      ray 2 · çark 1 · yuvarlak pencere 1 · retikül çizgisi 2 (artı biçimi) · ölçek işareti 0
  RET:        retikülde rakam/çentik · kare pencere · çark yerine kol/levye · ikinci pencere
  YABANCI GÖZ: p3'ü göster · soru "camda kaç çizgi var?" · doğru cevap: "iki, artı gibi"
  SONUÇ:      ⬜ (geçmezse 7 geçit/bölme klibi ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok · 0
```

### 📸 IMAGE PROMPT — SAYFA RK1 · PİLOT
```
IN FRAME: face · full body · back
Photorealistic four-panel still, 35mm film grain, plain mid-grey seamless backdrop, even neutral key light, deep focus.

Exactly one human character — no clones, no second person. A woman in her mid-thirties with dark hair pulled back and steady dark eyes stands facing the lens, sealed in a close-fitting pearl-white pressure suit of matte technical textile. A matte scuffed pearl-white composite chest plate and matching shoulder plates are edged in worn dark-grey rubber where they meet the textile. A thin dark-gold neck ring locks the helmet to the collar and matching dark-gold rings close both wrists above heavy segmented off-white gloves one piece with the sleeves. One wide band of dark-gold textile is wrapped all the way around her RIGHT forearm and her RIGHT thigh. On the left of her chest sits a small textless raised badge shaped like a pair of swept wings. The helmet is a low hard pearl-white shell with a single flat front pane set inside a thick dark-grey rim; the pane is optically clear with zero tint and zero mirror coating, a soft cool 5600K fill from inside the rim lights her face, and her face is fully readable through it at every head angle. The back of the suit is one continuous sculpted surface from collar to hip, low-profile, with two shallow recessed panels, closed and smooth, carrying nothing. Panels: three-quarter full length · profile · the back · the face close behind the pane.

NEGATIVE: No readable text, letters, digits or symbols on any surface, patch or sign — no emblem lettering, no rank mark, no flag, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No bare skin anywhere — none above the collar, none at the wrists between glove and sleeve, none at the ankles between boot and leg. The visor is one flat clear pane in a thick dark rim — no dome, no bubble, no mirror coating, no tint and no environment reflected in it. No back-mounted unit, no backpack, no tank, no hose and no rear housing of any kind.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — şerit SAĞ (önkol + uyluk)   p2 · profil — kask kabuğu, yaka halkası
               p3 · SIRT — sürekli yüzey [D79/D139] (C kurulumu: K04-K16)
               p4 · vizör ardı yüz CU [D146] (H kurulumu: K18 · K23)
⭐ ARKETİP T (teknokratik form-fit): mat tekstil + kompozit plaka + dar kask · hafifletme: mat ·
   aşınmış kenar (scuffed / worn rubber) · tekstil eklem.
⛔ "seamless visor" YAZILMAZ [D146].
```
```
KABUL SINAVI (RK1):
  KABUL:      p4'te yüz panenin İÇİNDEN okunuyor · pane TEK ve DÜZ · çerçeve kalın koyu gri ·
              altın şerit SAĞ önkol + SAĞ uylukta · p3 sırt çıkıntısı 0 ama iki gömme panel görünür
  RET:        kubbe/balon · aynalı/renkli pane · sırtta ünite/tank · şerit solda · rozette harf
  YABANCI GÖZ: p1'i göster · soru "altın bant hangi kolda?" · doğru cevap: "sağ"
  SONUÇ:      ⬜ (geçmezse 8 pilot klibi ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: kişi başına öznitelik = 3 (yaş · saç · göz) ✅
```

### 📸 IMAGE PROMPT — SAYFA RK2 · MÜHENDİS
```
IN FRAME: face · full body · back
Photorealistic four-panel still, 35mm film grain, plain mid-grey seamless backdrop, even neutral key light, deep focus.

Exactly one human character — no clones, no second person. A man in his late thirties with a short greying beard stands facing the lens, sealed in a close-fitting white pressure suit of ribbed technical textile with cobalt-blue textile joint panels at the elbows and knees. A brushed-steel neck ring locks the helmet to the collar and steel rings close both wrists above heavy segmented off-white gloves one piece with the sleeves. One wide band of cobalt-blue textile is wrapped all the way around his LEFT upper arm and his LEFT thigh. A small textless raised cobalt hexagon badge sits on the right of his chest, and on his left wrist a round analogue gauge with a single needle on a plain dial. The helmet is a low hard white shell with a single flat front pane set inside a thick dark-grey rim; the pane is optically clear with zero tint and zero mirror coating, a soft cool 5600K fill from inside the rim lights his face, and his face is fully readable through it at every head angle. The back of the suit is one continuous sculpted surface from collar to hip, low-profile, with two shallow recessed panels, closed and smooth, carrying nothing. Panels: three-quarter full length · profile · the back and right shoulder · the face close behind the pane.

NEGATIVE: No readable text, letters, digits or symbols on any surface, patch or sign — no numbers on the gauge dial, no rank mark, no flag, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No bare skin anywhere — none above the collar, none at the wrists between glove and sleeve, none at the ankles between boot and leg. The visor is one flat clear pane in a thick dark rim — no dome, no bubble, no mirror coating, no tint and no environment reflected in it. No back-mounted unit, no backpack, no tank, no hose and no rear housing of any kind.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — kobalt şerit SOL (pazı + uyluk), altıgen rozet (E · K09)
               p2 · profil — sol omuz + bilek göstergesi (F kurulumu: K10 · K12)
               p3 · SIRT + sağ omuz — sürekli yüzey [D79/D139] (B kurulumu: K02 K17 K19 K22)
               p4 · vizör ardı yüz CU [D146] — film içinde kullanılmaz; kimlik kaydı
⭐ AYRIŞMA (D208): RK1 ↔ RK2 dört eksende zıt — şerit tarafı SAĞ↔SOL · renk altın↔kobalt ·
   rozet kanat↔altıgen · göğüs kompozit plaka↔nervürlü tekstil · koltuk SOL↔SAĞ.
```
```
KABUL SINAVI (RK2):
  KABUL:      kobalt şerit SOL pazı + SOL uylukta · bilek göstergesi tek ibre, kadran yazısız ·
              altıgen rozet sağ göğüste · p3 sırt çıkıntısı 0 ama iki gömme panel görünür
  RET:        şerit sağda · göstergede rakam · kubbe/balon · sırtta ünite · RK1 ile aynı göğüs plakası
  YABANCI GÖZ: p1'i RK1 p1 ile yan yana göster · soru "hangisi pilot?" · doğru cevap: "altın bantlı"
  SONUÇ:      ⬜ (geçmezse 10 mühendis klibi ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: kişi başına öznitelik = 2 (yaş · sakal) ✅
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

> ⛔ Sınanmamış kapı yazılmaz [D142]; makine kapısı `BLIND_ORBIT_QA_SPEC.md`
> 🅴 E BLOĞU'na `DOĞRULANDI` satırıyla girer.

```
☑ ① PANEL ARİTMETİĞİ  §1 künye 23 = §2 tablo 1+3+2+3+3+3+4+4 = 23
☑ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var · YETİM 0
□ ③ 120 PX TESTİ      panel 120 px'e inince: RO kanca sayısı · RK şerit tarafı · RB kanat sayısı
□ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
□ ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur + kalın çerçeve
□ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0 AMA iki gömme panel görünür
□ ⑦ D69 KLON          RK1 · RK2 panellerinde figür = 1 · RI1 · RI2'de figür = 0
□ ⑦b GRİ TON ⚙️       `ffmpeg -i <panel> -vf hue=s=0` — RK1↔RK2 ayrımı gri tonda da taraf +
                      rozet biçimiyle okunur mu (renk tek kanal değil)
□ ⑧ DURUM ÇİFTİ       RO p1 ↔ p2 aynı kadraj · aynı ışık · ±%3
☑ ⑨ ⑲ KİMLİK YIĞINI   RK1 3 · RK2 2 (betik koşuldu)
☑ ⑩ ⑳b DEĞİŞİM        RO çifti dışında hiçbir sayfa değişimin SONRASINI yazmıyor [D179]
□ ⑪ ÖLÇEK ŞAHİDİ      RB p1'de RA gemisi 1/30 oranında kadrajda
□ ⑫ SEED / SHA KAYDI  §2 tablosuna yazılacak
☑ ⑬ BAYT AYNILIĞI     bölüm promptlarının kimlik parçaları PLAN Character Bible "PROMPT HÂLİ"
                      satırlarıyla aynı üreteçten (kısaltma, ekleme yok)
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: 0 BLOCK (insansız sayfalarda
                      "insan sayısı" FIX'i bilinçli — red #2: "Exactly 0 human" yazılmaz)
⛔ □ kalan maddeler ÜRETİM GÜNÜ işaretlenir; işaretlenmeden ilk klip ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR — üretim randevuları

```
⬜ 8 sayfa üretilmedi (0/23 panel) · seed / SHA boş
⬜ Kabul kapısı ③ ④ ⑤ ⑥ ⑦ ⑦b ⑧ ⑪ ⑫ üretim günü
⬜ İMAJ MODELİ + SÜRÜM künyeye yazılacak
```
